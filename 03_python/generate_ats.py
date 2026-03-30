from datetime import datetime, timedelta
import random
import pandas as pd

from shared_logic import (
    RAW_DIRS,
    DEPARTMENTS,
    choose_country,
    choose_gender,
)

TODAY = datetime(2026, 3, 31)
APPLICATION_COUNT = 8000

STAGES = ["Applied", "Screen", "Interview", "Offer", "Hired"]

STAGE_CONVERSION = {
    "Screen": 0.72,
    "Interview": 0.58,
    "Offer": 0.46,
    "Hired": 0.35,
}

TIME_BETWEEN_STAGES = {
    "Applied": (1, 4),
    "Screen": (3, 8),
    "Interview": (5, 14),
    "Offer": (2, 9),
}


def random_application_date():
    start = TODAY - timedelta(days=365)
    return start + timedelta(days=random.randint(0, 365))


def choose_role_by_department(department):
    role_map = {
        "Operations": ["Site Engineer", "Project Manager", "Construction Supervisor"],
        "Supply Chain": ["Procurement Specialist", "Logistics Coordinator", "Warehouse Manager"],
        "Customer Support": ["Customer Support Rep", "Customer Success Manager"],
        "Sales": ["Sales Executive", "Account Manager"],
        "Technology": ["Data Analyst", "Data Engineer", "Software Engineer"],
        "Finance": ["Financial Analyst", "Accountant"],
        "Commercial": ["Commercial Analyst", "Pricing Manager"],
        "People": ["HR Advisor", "HR Business Partner"],
    }
    return random.choice(role_map[department])


def adjust_conversion_rates(country, department, gender):
    rates = STAGE_CONVERSION.copy()

    if department in ["Operations", "Supply Chain"]:
        rates["Interview"] -= 0.04
        rates["Offer"] -= 0.03

    if department == "Technology":
        rates["Offer"] -= 0.05
        rates["Hired"] -= 0.04

    if country == "Germany":
        rates["Interview"] -= 0.03
        rates["Offer"] -= 0.03

    if country == "Netherlands":
        rates["Interview"] += 0.03
        rates["Offer"] += 0.02

    if gender == "Female" and department in ["Operations", "Supply Chain"]:
        rates["Hired"] -= 0.03

    for key in rates:
        rates[key] = min(max(rates[key], 0.15), 0.90)

    return rates


def create_application(i):
    candidate_id = f"CAND{i:06d}"
    application_date = random_application_date()

    country = choose_country()
    department = random.choice(DEPARTMENTS)
    job_role = choose_role_by_department(department)
    gender = choose_gender()

    stage_dates = {"Applied_date": application_date}
    current_stage = "Applied"

    rates = adjust_conversion_rates(country, department, gender)

    prev_stage = "Applied"
    prev_date = application_date

    for next_stage in ["Screen", "Interview", "Offer", "Hired"]:
        if random.random() <= rates[next_stage]:
            min_days, max_days = TIME_BETWEEN_STAGES[prev_stage]
            next_date = prev_date + timedelta(days=random.randint(min_days, max_days))
            stage_dates[f"{next_stage}_date"] = next_date
            current_stage = next_stage
            prev_stage = next_stage
            prev_date = next_date
        else:
            break

    hired_flag = 1 if current_stage == "Hired" else 0

    return {
        "candidate_id": candidate_id,
        "application_date": application_date.date(),
        "country": country,
        "department": department,
        "job_role": job_role,
        "gender": gender,
        "current_stage": current_stage,
        "hired_flag": hired_flag,
        "Applied_date": stage_dates.get("Applied_date").date() if stage_dates.get("Applied_date") else None,
        "Screen_date": stage_dates.get("Screen_date").date() if stage_dates.get("Screen_date") else None,
        "Interview_date": stage_dates.get("Interview_date").date() if stage_dates.get("Interview_date") else None,
        "Offer_date": stage_dates.get("Offer_date").date() if stage_dates.get("Offer_date") else None,
        "Hired_date": stage_dates.get("Hired_date").date() if stage_dates.get("Hired_date") else None,
    }


def generate_ats():
    data = [create_application(i) for i in range(1, APPLICATION_COUNT + 1)]
    df = pd.DataFrame(data)

    output_path = RAW_DIRS["ats"] / "ats_pipeline.csv"
    df.to_csv(output_path, index=False)

    print(f"ATS dataset created: {output_path}")
    print(f"Rows: {len(df)}")
    print(df["current_stage"].value_counts(dropna=False))
    print(df["hired_flag"].value_counts(dropna=False))
    print(df.head())


if __name__ == "__main__":
    generate_ats()