from datetime import datetime
import random
import pandas as pd

from shared_logic import RAW_DIRS

SURVEY_DATES = [
    datetime(2025, 3, 31),
    datetime(2025, 9, 30),
    datetime(2026, 3, 31),
]


def load_hris():
    hris_path = RAW_DIRS["hris"] / "hris_employee_master.csv"
    return pd.read_csv(hris_path)


def load_lms():
    lms_path = RAW_DIRS["lms"] / "lms_learning_records.csv"
    return pd.read_csv(lms_path)


def employee_training_completion_map(lms_df):
    completion_map = (
        lms_df.groupby("employee_id")["completion_status"]
        .apply(lambda s: (s == "Completed").mean())
        .to_dict()
    )
    return completion_map


def clamp(value, low=0, high=100):
    return max(low, min(high, value))


def base_scores(department, country):
    department_base = {
        "Operations": {"engagement": 54, "wellbeing": 49, "manager": 58, "growth": 50, "inclusion": 60},
        "Supply Chain": {"engagement": 58, "wellbeing": 53, "manager": 61, "growth": 54, "inclusion": 62},
        "Customer Support": {"engagement": 62, "wellbeing": 57, "manager": 63, "growth": 56, "inclusion": 64},
        "Sales": {"engagement": 66, "wellbeing": 60, "manager": 65, "growth": 63, "inclusion": 65},
        "Technology": {"engagement": 74, "wellbeing": 69, "manager": 71, "growth": 72, "inclusion": 68},
        "Finance": {"engagement": 78, "wellbeing": 74, "manager": 74, "growth": 70, "inclusion": 72},
        "Commercial": {"engagement": 69, "wellbeing": 64, "manager": 67, "growth": 66, "inclusion": 67},
        "People": {"engagement": 81, "wellbeing": 76, "manager": 78, "growth": 72, "inclusion": 76},
    }[department]

    country_adjustment = {
        "UK": {"engagement": 2, "wellbeing": 1, "manager": 1, "growth": 1, "inclusion": 1},
        "Germany": {"engagement": -10, "wellbeing": -11, "manager": -8, "growth": -6, "inclusion": -5},
        "France": {"engagement": -4, "wellbeing": -4, "manager": -3, "growth": -2, "inclusion": -2},
        "Netherlands": {"engagement": 7, "wellbeing": 6, "manager": 4, "growth": 3, "inclusion": 4},
        "Ireland": {"engagement": -5, "wellbeing": -5, "manager": -3, "growth": -3, "inclusion": -2},
    }[country]

    adjusted = {
        metric: department_base[metric] + country_adjustment[metric]
        for metric in department_base
    }
    return adjusted


def survey_time_adjustment(survey_date, department):
    if survey_date.year == 2025 and survey_date.month == 3:
        return 0

    if survey_date.year == 2025 and survey_date.month == 9:
        if department in ["Operations", "Supply Chain"]:
            return -2
        return 1

    if survey_date.year == 2026 and survey_date.month == 3:
        if department in ["Operations", "Supply Chain"]:
            return -4
        if department in ["People", "Finance", "Technology"]:
            return 2
        return 0

    return 0


def intent_to_leave_probability(engagement, wellbeing, manager_support):
    score = 0.05

    if engagement < 50:
        score += 0.30
    elif engagement < 60:
        score += 0.16
    elif engagement < 70:
        score += 0.07

    if wellbeing < 50:
        score += 0.18
    elif wellbeing < 60:
        score += 0.08

    if manager_support < 55:
        score += 0.12
    elif manager_support < 65:
        score += 0.05

    score += random.uniform(-0.03, 0.03)

    return min(max(score, 0.02), 0.80)


def create_engagement_records(hris_df, completion_map):
    records = []
    survey_id = 1

    for _, row in hris_df.iterrows():
        employee_id = row["employee_id"]
        department = row["department"]
        country = row["country"]
        employment_status = row["employment_status"]
        tenure_months = row["tenure_months"]
        manager_flag = row["manager_flag"]

        training_completion = completion_map.get(employee_id, 0.5)

        for survey_date in SURVEY_DATES:
            base = base_scores(department, country)
            time_adj = survey_time_adjustment(survey_date, department)

            training_adj = (training_completion - 0.6) * 18
            tenure_adj = -4 if tenure_months < 6 else (-2 if tenure_months < 12 else 1)
            manager_role_adj = 2 if manager_flag == 1 else 0
            active_adj = -6 if employment_status == "Terminated" else 0

            engagement = clamp(
                base["engagement"] + time_adj + training_adj + tenure_adj + manager_role_adj + active_adj + random.uniform(-8, 8)
            )
            wellbeing = clamp(
                base["wellbeing"] + time_adj + (training_completion - 0.6) * 10 + tenure_adj + active_adj + random.uniform(-9, 9)
            )
            manager_support = clamp(
                base["manager"] + time_adj + manager_role_adj + active_adj + random.uniform(-7, 7)
            )
            career_growth = clamp(
                base["growth"] + (training_completion - 0.6) * 12 + tenure_adj + random.uniform(-8, 8)
            )
            inclusion = clamp(
                base["inclusion"] + active_adj + random.uniform(-7, 7)
            )

            intent_prob = intent_to_leave_probability(engagement, wellbeing, manager_support)
            intent_to_leave = 1 if random.random() <= intent_prob else 0

            records.append(
                {
                    "survey_id": f"SRV{survey_id:07d}",
                    "employee_id": employee_id,
                    "survey_date": survey_date.date(),
                    "country": country,
                    "department": department,
                    "engagement_score": round(engagement, 1),
                    "wellbeing_score": round(wellbeing, 1),
                    "manager_support_score": round(manager_support, 1),
                    "career_growth_score": round(career_growth, 1),
                    "inclusion_score": round(inclusion, 1),
                    "intent_to_leave_flag": intent_to_leave,
                }
            )

            survey_id += 1

    return pd.DataFrame(records)


def generate_engagement():
    hris_df = load_hris()
    lms_df = load_lms()
    completion_map = employee_training_completion_map(lms_df)

    engagement_df = create_engagement_records(hris_df, completion_map)

    output_path = RAW_DIRS["engagement"] / "engagement_surveys.csv"
    engagement_df.to_csv(output_path, index=False)

    print(f"Engagement dataset created: {output_path}")
    print(f"Rows: {len(engagement_df)}")
    print(engagement_df.head())


if __name__ == "__main__":
    generate_engagement()