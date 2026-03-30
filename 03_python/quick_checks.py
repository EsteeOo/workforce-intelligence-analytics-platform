import sys
from pathlib import Path
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT_DIR / "01_raw"


def read_csv(path):
    return pd.read_csv(path)


def check_hris():
    path = RAW_DIR / "hris" / "hris_employee_master.csv"
    df = read_csv(path)

    print("\n=== HRIS CHECK ===")
    print(f"Rows: {len(df):,}\n")

    print("Employment status:")
    print(df["employment_status"].value_counts(dropna=False), "\n")

    print("Gender split:")
    print(df["gender"].value_counts(dropna=False), "\n")

    print("Country distribution:")
    print(df["country"].value_counts(dropna=False), "\n")

    print("Department distribution:")
    print(df["department"].value_counts(dropna=False), "\n")

    print("Salary summary by level:")
    print(df.groupby("job_level")["salary"].agg(["count", "min", "median", "max"]), "\n")


def check_ats():
    path = RAW_DIR / "ats" / "ats_pipeline.csv"
    df = read_csv(path)

    print("\n=== ATS CHECK ===")
    print(f"Rows: {len(df):,}\n")

    print("Current stage counts:")
    print(df["current_stage"].value_counts(dropna=False), "\n")

    print("Hired flag counts:")
    print(df["hired_flag"].value_counts(dropna=False), "\n")

    hired_df = df[df["hired_flag"] == 1]

    print("Gender split among hired:")
    print(hired_df["gender"].value_counts(dropna=False), "\n")

    print("Country split among hired:")
    print(hired_df["country"].value_counts(dropna=False), "\n")

    print("Department split among hired:")
    print(hired_df["department"].value_counts(dropna=False), "\n")


def check_lms():
    path = RAW_DIR / "lms" / "lms_learning_records.csv"
    df = read_csv(path)

    print("\n=== LMS CHECK ===")
    print(f"Rows: {len(df):,}\n")

    print("Completion status:")
    print(df["completion_status"].value_counts(dropna=False), "\n")

    print("Mandatory flag:")
    print(df["mandatory_flag"].value_counts(dropna=False), "\n")

    print("Overdue flag:")
    print(df["overdue_flag"].value_counts(dropna=False), "\n")

    print("Completion by department:")
    dept_completion = (
        df.groupby("department")["completion_status"]
        .apply(lambda s: (s == "Completed").mean())
        .sort_values(ascending=False)
        .round(3)
    )
    print(dept_completion, "\n")

    print("Completion by country:")
    country_completion = (
        df.groupby("country")["completion_status"]
        .apply(lambda s: (s == "Completed").mean())
        .sort_values(ascending=False)
        .round(3)
    )
    print(country_completion, "\n")


def check_engagement():
    path = RAW_DIR / "engagement" / "engagement_surveys.csv"
    df = read_csv(path)

    print("\n=== ENGAGEMENT CHECK ===")
    print(f"Rows: {len(df):,}\n")

    print("Average engagement by department:")
    print(df.groupby("department")["engagement_score"].mean().sort_values(ascending=False).round(1), "\n")

    print("Average engagement by country:")
    print(df.groupby("country")["engagement_score"].mean().sort_values(ascending=False).round(1), "\n")

    print("Average wellbeing by department:")
    print(df.groupby("department")["wellbeing_score"].mean().sort_values(ascending=False).round(1), "\n")

    print("Intent to leave rate by department:")
    intent_dept = (
        df.groupby("department")["intent_to_leave_flag"]
        .mean()
        .sort_values(ascending=False)
        .round(3)
    )
    print(intent_dept, "\n")

    print("Intent to leave rate by country:")
    intent_country = (
        df.groupby("country")["intent_to_leave_flag"]
        .mean()
        .sort_values(ascending=False)
        .round(3)
    )
    print(intent_country, "\n")


def check_timekeeping():
    path = RAW_DIR / "timekeeping" / "timekeeping_weekly_records.csv"
    df = read_csv(path)

    print("\n=== TIMEKEEPING CHECK ===")
    print(f"Rows: {len(df):,}\n")

    print("Average overtime by department:")
    print(df.groupby("department")["overtime_hours"].mean().sort_values(ascending=False).round(2), "\n")

    print("Average absence by country:")
    print(df.groupby("country")["absence_hours"].mean().sort_values(ascending=False).round(2), "\n")

    print("Pressure flag counts:")
    print(df["pressure_flag"].value_counts(dropna=False), "\n")

    print("Pressure rate by department:")
    pressure_dept = (
        df.groupby("department")["pressure_flag"]
        .mean()
        .sort_values(ascending=False)
        .round(3)
    )
    print(pressure_dept, "\n")

    print("Pressure rate by country:")
    pressure_country = (
        df.groupby("country")["pressure_flag"]
        .mean()
        .sort_values(ascending=False)
        .round(3)
    )
    print(pressure_country, "\n")


def run_all():
    check_hris()
    check_ats()
    check_lms()
    check_engagement()
    check_timekeeping()


def run_last_two():
    check_engagement()
    check_timekeeping()


def main():
    if len(sys.argv) < 2:
        print("Usage: python 03_python/quick_checks.py [hris|ats|lms|engagement|timekeeping|last_two|all]")
        return

    target = sys.argv[1].lower()

    if target == "hris":
        check_hris()
    elif target == "ats":
        check_ats()
    elif target == "lms":
        check_lms()
    elif target == "engagement":
        check_engagement()
    elif target == "timekeeping":
        check_timekeeping()
    elif target == "last_two":
        run_last_two()
    elif target == "all":
        run_all()
    else:
        print("Invalid option. Use: hris, ats, lms, engagement, timekeeping, last_two, or all")


if __name__ == "__main__":
    main()