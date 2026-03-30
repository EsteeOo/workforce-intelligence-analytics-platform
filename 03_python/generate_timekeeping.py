from datetime import datetime, timedelta
import random
import pandas as pd

from shared_logic import RAW_DIRS, OVERTIME_RISK_BY_DEPARTMENT, ABSENCE_RISK_BY_COUNTRY

TODAY = datetime(2026, 3, 31)
START_DATE = datetime(2025, 10, 1)


def load_hris():
    hris_path = RAW_DIRS["hris"] / "hris_employee_master.csv"
    return pd.read_csv(hris_path)


def weekly_dates():
    dates = []
    current = START_DATE
    while current <= TODAY:
        dates.append(current)
        current += timedelta(days=7)
    return dates


def scheduled_hours_by_department(department):
    base = {
        "Operations": 40,
        "Supply Chain": 40,
        "Customer Support": 37.5,
        "Sales": 37.5,
        "Technology": 37.5,
        "Finance": 37.5,
        "Commercial": 37.5,
        "People": 37.5,
    }[department]
    return base


def choose_shift_type(department):
    shift_map = {
        "Operations": [("Day", 0.55), ("Night", 0.20), ("Rotating", 0.25)],
        "Supply Chain": [("Day", 0.50), ("Night", 0.20), ("Rotating", 0.30)],
        "Customer Support": [("Day", 0.65), ("Evening", 0.25), ("Rotating", 0.10)],
        "Sales": [("Day", 0.90), ("Hybrid", 0.10)],
        "Technology": [("Day", 0.75), ("Hybrid", 0.25)],
        "Finance": [("Day", 0.85), ("Hybrid", 0.15)],
        "Commercial": [("Day", 0.80), ("Hybrid", 0.20)],
        "People": [("Day", 0.85), ("Hybrid", 0.15)],
    }

    values = shift_map[department]
    names = [x[0] for x in values]
    weights = [x[1] for x in values]
    return random.choices(names, weights=weights, k=1)[0]


def overtime_hours(department, country, employment_status):
    if employment_status == "Terminated":
        return 0.0

    base_risk = OVERTIME_RISK_BY_DEPARTMENT[department]
    country_adjustment = {
        "UK": 0.03,
        "Germany": 0.05,
        "France": 0.01,
        "Netherlands": -0.02,
        "Ireland": 0.04,
    }[country]

    probability = min(max(base_risk + country_adjustment, 0.03), 0.65)

    if random.random() > probability:
        return 0.0

    if department in ["Operations", "Supply Chain"]:
        return round(random.uniform(2, 16), 1)
    if department == "Customer Support":
        return round(random.uniform(1, 10), 1)
    if department in ["Technology", "Sales", "Commercial"]:
        return round(random.uniform(1, 8), 1)

    return round(random.uniform(0.5, 5), 1)


def absence_hours(country, department, tenure_months, employment_status):
    if employment_status == "Terminated":
        return 0.0

    base_risk = ABSENCE_RISK_BY_COUNTRY[country]

    department_adjustment = {
        "Operations": 0.03,
        "Supply Chain": 0.03,
        "Customer Support": 0.02,
        "Sales": 0.00,
        "Technology": -0.01,
        "Finance": -0.01,
        "Commercial": 0.00,
        "People": -0.01,
    }[department]

    tenure_adjustment = 0.02 if tenure_months < 6 else (0.01 if tenure_months < 12 else 0.00)

    probability = min(max(base_risk + department_adjustment + tenure_adjustment, 0.01), 0.22)

    if random.random() > probability:
        return 0.0

    absence_options = [4.0, 7.5, 8.0, 16.0, 24.0, 32.0, 40.0]
    weights = [0.18, 0.20, 0.18, 0.18, 0.12, 0.09, 0.05]
    return random.choices(absence_options, weights=weights, k=1)[0]


def create_timekeeping_records(hris_df):
    records = []
    week_dates = weekly_dates()
    record_id = 1

    for _, row in hris_df.iterrows():
        employee_id = row["employee_id"]
        country = row["country"]
        department = row["department"]
        employment_status = row["employment_status"]
        tenure_months = row["tenure_months"]

        shift_type = choose_shift_type(department)
        scheduled_hours = scheduled_hours_by_department(department)

        for work_week_start in week_dates:
            ot_hours = overtime_hours(department, country, employment_status)
            abs_hours = absence_hours(country, department, tenure_months, employment_status)

            actual_hours = max(0.0, scheduled_hours + ot_hours - abs_hours)
            pressure_flag = 1 if ot_hours >= 8 or abs_hours >= 16 else 0

            records.append(
                {
                    "timekeeping_record_id": f"TMK{record_id:08d}",
                    "employee_id": employee_id,
                    "week_start_date": work_week_start.date(),
                    "country": country,
                    "department": department,
                    "shift_type": shift_type,
                    "scheduled_hours": scheduled_hours,
                    "actual_hours": round(actual_hours, 1),
                    "overtime_hours": ot_hours,
                    "absence_hours": abs_hours,
                    "pressure_flag": pressure_flag,
                }
            )

            record_id += 1

    return pd.DataFrame(records)


def generate_timekeeping():
    hris_df = load_hris()
    timekeeping_df = create_timekeeping_records(hris_df)

    output_path = RAW_DIRS["timekeeping"] / "timekeeping_weekly_records.csv"
    timekeeping_df.to_csv(output_path, index=False)

    print(f"Timekeeping dataset created: {output_path}")
    print(f"Rows: {len(timekeeping_df)}")
    print(timekeeping_df.head())


if __name__ == "__main__":
    generate_timekeeping()