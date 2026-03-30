from datetime import datetime, timedelta
import random
import pandas as pd

from shared_logic import (
    RAW_DIRS,
    fake,
    choose_country,
    choose_site,
    choose_department,
    choose_job_role,
    choose_gender,
    choose_ethnicity,
    choose_age_band,
    JOB_LEVEL_MAP,
    ATTRITION_RISK_BY_COUNTRY,
)

EMPLOYEE_COUNT = 2400
TODAY = datetime(2026, 3, 31)
START_DATE = datetime(2020, 1, 1)


def random_hire_date():
    days_range = (TODAY - START_DATE).days
    return START_DATE + timedelta(days=random.randint(0, days_range))


def tenure_in_months(hire_date, end_date):
    return max(0, (end_date.year - hire_date.year) * 12 + (end_date.month - hire_date.month))


def salary_by_level(level):
    salary_ranges = {
        "Junior": (26000, 36000),
        "Mid": (38000, 56000),
        "Senior": (58000, 82000),
        "Manager": (78000, 115000),
    }
    low, high = salary_ranges[level]
    return random.randint(low, high)


def attrition_probability(country, department, level, tenure_months_value):
    base = ATTRITION_RISK_BY_COUNTRY[country]

    department_adjustment = {
        "Operations": 0.08,
        "Supply Chain": 0.06,
        "Customer Support": 0.07,
        "Sales": 0.04,
        "Technology": -0.01,
        "Finance": -0.03,
        "Commercial": 0.02,
        "People": -0.03,
    }[department]

    level_adjustment = {
        "Junior": 0.06,
        "Mid": 0.03,
        "Senior": -0.01,
        "Manager": -0.04,
    }[level]

    tenure_adjustment = 0.12 if tenure_months_value < 12 else -0.02

    probability = base + department_adjustment + level_adjustment + tenure_adjustment
    return min(max(probability, 0.02), 0.45)


def termination_date_from_probability(hire_date, probability):
    if random.random() >= probability:
        return None

    min_exit_days = 30
    max_exit_days = max(min_exit_days, (TODAY - hire_date).days)
    exit_offset = random.randint(min_exit_days, max_exit_days)
    exit_date = hire_date + timedelta(days=exit_offset)

    if exit_date > TODAY:
        return None
    return exit_date


def create_employee_record(employee_number):
    employee_id = f"EMP{employee_number:05d}"

    country = choose_country()
    site = choose_site(country)
    department = choose_department()
    job_role = choose_job_role(department)
    job_level = JOB_LEVEL_MAP[job_role]

    gender = choose_gender()
    ethnicity = choose_ethnicity()
    age_band = choose_age_band()

    hire_date = random_hire_date()
    active_tenure = tenure_in_months(hire_date, TODAY)

    probability = attrition_probability(
        country=country,
        department=department,
        level=job_level,
        tenure_months_value=active_tenure,
    )

    termination_date = termination_date_from_probability(hire_date, probability)

    employment_status = "Active" if termination_date is None else "Terminated"
    end_date = TODAY if termination_date is None else termination_date
    final_tenure = tenure_in_months(hire_date, end_date)

    salary = salary_by_level(job_level)
    manager_flag = 1 if job_level == "Manager" else 0

    return {
        "employee_id": employee_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": gender,
        "ethnicity": ethnicity,
        "age_band": age_band,
        "country": country,
        "site": site,
        "department": department,
        "job_role": job_role,
        "job_level": job_level,
        "hire_date": hire_date.date(),
        "termination_date": termination_date.date() if termination_date else None,
        "employment_status": employment_status,
        "tenure_months": final_tenure,
        "salary": salary,
        "manager_flag": manager_flag,
    }


def generate_hris_dataset():
    records = [create_employee_record(i) for i in range(1, EMPLOYEE_COUNT + 1)]
    df = pd.DataFrame(records)

    output_path = RAW_DIRS["hris"] / "hris_employee_master.csv"
    df.to_csv(output_path, index=False)

    print(f"HRIS dataset created: {output_path}")
    print(f"Rows: {len(df)}")
    print(df.head())


if __name__ == "__main__":
    generate_hris_dataset()