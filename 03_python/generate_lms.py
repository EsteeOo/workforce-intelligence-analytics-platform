from datetime import datetime, timedelta
import random
import pandas as pd

from shared_logic import RAW_DIRS, COURSES

TODAY = datetime(2026, 3, 31)


def load_hris():
    hris_path = RAW_DIRS["hris"] / "hris_employee_master.csv"
    return pd.read_csv(hris_path)


def assignment_date():
    start = datetime(2025, 1, 1)
    days_range = (TODAY - start).days
    return start + timedelta(days=random.randint(0, days_range))


def due_date_from_assignment(assign_date, mandatory):
    base_days = 30 if mandatory == 1 else 75
    variation = random.randint(-5, 20)
    return assign_date + timedelta(days=max(10, base_days + variation))


def employee_course_count(department, employment_status, country):
    if employment_status == "Terminated":
        return random.choices([1, 2, 3], weights=[0.55, 0.32, 0.13])[0]

    department_course_weights = {
        "Operations": [0.18, 0.44, 0.28, 0.10],
        "Supply Chain": [0.20, 0.44, 0.26, 0.10],
        "Customer Support": [0.24, 0.46, 0.22, 0.08],
        "Sales": [0.28, 0.44, 0.20, 0.08],
        "Technology": [0.12, 0.30, 0.36, 0.22],
        "Finance": [0.14, 0.34, 0.32, 0.20],
        "Commercial": [0.22, 0.42, 0.24, 0.12],
        "People": [0.10, 0.28, 0.36, 0.26],
    }

    base_weights = department_course_weights[department][:]

    country_adjustments = {
        "UK":         [0.00, 0.00, 0.00, 0.00],
        "Germany":    [0.06, 0.04, -0.06, -0.04],
        "France":     [0.02, 0.02, -0.02, -0.02],
        "Netherlands":[-0.04, -0.02, 0.02, 0.04],
        "Ireland":    [0.03, 0.01, -0.02, -0.02],
    }[country]

    adjusted = [max(0.01, w + a) for w, a in zip(base_weights, country_adjustments)]
    total = sum(adjusted)
    adjusted = [w / total for w in adjusted]

    return random.choices([1, 2, 3, 4], weights=adjusted)[0]


def select_courses(course_count, department):
    mandatory_courses = [c for c in COURSES if c["mandatory"] == 1]
    optional_courses = [c for c in COURSES if c["mandatory"] == 0]

    selected_courses = []

    mandatory_bias = {
        "Operations": 0.88,
        "Supply Chain": 0.83,
        "Customer Support": 0.78,
        "Sales": 0.68,
        "Technology": 0.60,
        "Finance": 0.64,
        "Commercial": 0.66,
        "People": 0.56,
    }

    if random.random() < mandatory_bias[department]:
        selected_courses.append(random.choice(mandatory_courses))

    remaining = course_count - len(selected_courses)

    pool = optional_courses.copy()
    random.shuffle(pool)

    for course in pool:
        if len(selected_courses) >= course_count:
            break
        selected_courses.append(course)

    if len(selected_courses) < course_count:
        extra_pool = [c for c in mandatory_courses if c not in selected_courses]
        random.shuffle(extra_pool)
        for course in extra_pool:
            if len(selected_courses) >= course_count:
                break
            selected_courses.append(course)

    return selected_courses[:course_count]


def completion_probability(department, mandatory, employment_status, country, tenure_months, manager_flag):
    department_base = {
        "Operations": 0.44,
        "Supply Chain": 0.52,
        "Customer Support": 0.62,
        "Sales": 0.67,
        "Technology": 0.80,
        "Finance": 0.88,
        "Commercial": 0.73,
        "People": 0.92,
    }[department]

    country_adjustment = {
        "UK": 0.02,
        "Germany": -0.14,
        "France": -0.05,
        "Netherlands": 0.11,
        "Ireland": -0.08,
    }[country]

    mandatory_adjustment = 0.20 if mandatory == 1 else -0.07
    status_adjustment = -0.26 if employment_status == "Terminated" else 0.00
    tenure_adjustment = -0.12 if tenure_months < 6 else (-0.05 if tenure_months < 12 else 0.03)
    manager_adjustment = 0.04 if manager_flag == 1 else 0.00

    # Make department/country extremes a bit more pronounced
    interaction_adjustment = 0.0
    if department == "Operations" and country == "Germany":
        interaction_adjustment -= 0.06
    if department == "Supply Chain" and country == "Germany":
        interaction_adjustment -= 0.05
    if department == "People" and country == "Netherlands":
        interaction_adjustment += 0.03
    if department == "Finance" and country == "Netherlands":
        interaction_adjustment += 0.03
    if department == "Technology" and country == "UK":
        interaction_adjustment += 0.02
    if department == "Operations" and country == "Ireland":
        interaction_adjustment -= 0.03

    noise = random.uniform(-0.08, 0.08)

    probability = (
        department_base
        + country_adjustment
        + mandatory_adjustment
        + status_adjustment
        + tenure_adjustment
        + manager_adjustment
        + interaction_adjustment
        + noise
    )

    return min(max(probability, 0.06), 0.98)


def completion_date_from_assignment(assign_date, due_date, completed, department, mandatory, country):
    if not completed:
        return None

    timing_profile = {
        "Operations": (10, 60),
        "Supply Chain": (8, 52),
        "Customer Support": (5, 40),
        "Sales": (4, 34),
        "Technology": (3, 26),
        "Finance": (2, 20),
        "Commercial": (4, 30),
        "People": (2, 16),
    }

    min_days, max_days = timing_profile[department]

    if mandatory == 1:
        max_days = max(8, max_days - 10)

    country_delay = {
        "UK": 0,
        "Germany": 5,
        "France": 2,
        "Netherlands": -3,
        "Ireland": 3,
    }[country]

    min_days = max(1, min_days + min(country_delay, 0))
    max_days = max(min_days + 1, max_days + max(country_delay, 0))

    completion_date = assign_date + timedelta(days=random.randint(min_days, max_days))

    if completion_date > TODAY:
        completion_date = TODAY

    return completion_date


def create_learning_records(hris_df):
    records = []
    learning_id = 1

    for _, row in hris_df.iterrows():
        employee_id = row["employee_id"]
        department = row["department"]
        country = row["country"]
        employment_status = row["employment_status"]
        tenure_months = row["tenure_months"]
        manager_flag = row["manager_flag"]

        course_count = employee_course_count(department, employment_status, country)
        selected_courses = select_courses(course_count, department)

        for course in selected_courses:
            mandatory = course["mandatory"]
            assign_date = assignment_date()
            due_date = due_date_from_assignment(assign_date, mandatory)

            prob = completion_probability(
                department=department,
                mandatory=mandatory,
                employment_status=employment_status,
                country=country,
                tenure_months=tenure_months,
                manager_flag=manager_flag,
            )

            completed = 1 if random.random() <= prob else 0
            completion_date = completion_date_from_assignment(
                assign_date=assign_date,
                due_date=due_date,
                completed=completed,
                department=department,
                mandatory=mandatory,
                country=country,
            )

            overdue_flag = 1 if completed == 0 and due_date < TODAY else 0

            if completion_date is not None:
                completion_status = "Completed"
                days_to_complete = (completion_date - assign_date).days
            else:
                completion_status = "Incomplete"
                days_to_complete = None

            records.append(
                {
                    "learning_record_id": f"LRN{learning_id:07d}",
                    "employee_id": employee_id,
                    "course_id": course["course_id"],
                    "course_name": course["course_name"],
                    "mandatory_flag": mandatory,
                    "assignment_date": assign_date.date(),
                    "due_date": due_date.date(),
                    "completion_date": completion_date.date() if completion_date else None,
                    "completion_status": completion_status,
                    "days_to_complete": days_to_complete,
                    "overdue_flag": overdue_flag,
                    "department": department,
                    "country": country,
                }
            )

            learning_id += 1

    return pd.DataFrame(records)


def generate_lms():
    hris_df = load_hris()
    lms_df = create_learning_records(hris_df)

    output_path = RAW_DIRS["lms"] / "lms_learning_records.csv"
    lms_df.to_csv(output_path, index=False)

    print(f"LMS dataset created: {output_path}")
    print(f"Rows: {len(lms_df)}")
    print(lms_df["completion_status"].value_counts(dropna=False))
    print(lms_df["mandatory_flag"].value_counts(dropna=False))
    print(lms_df["overdue_flag"].value_counts(dropna=False))
    print(lms_df.head())


if __name__ == "__main__":
    generate_lms()