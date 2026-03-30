from pathlib import Path
import duckdb

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = ROOT_DIR / "02_sql" / "00_database" / "workforce_intelligence.duckdb"


def run_sql_file(relative_path):
    sql_file_path = ROOT_DIR / relative_path

    with open(sql_file_path, "r", encoding="utf-8") as f:
        sql = f.read()

    conn = duckdb.connect(str(DB_PATH))
    conn.execute(sql)
    conn.close()

    print(f"Executed: {sql_file_path}")


if __name__ == "__main__":
    files_to_run = [
        "02_sql/01_ddl/create_raw_tables.sql",
        "02_sql/02_raw_load/load_raw_tables.sql",
        "02_sql/03_staging/stg_hris.sql",
        "02_sql/03_staging/stg_ats.sql",
        "02_sql/03_staging/stg_lms.sql",
        "02_sql/03_staging/stg_engagement.sql",
        "02_sql/03_staging/stg_timekeeping.sql",
        "02_sql/04_curated/mart_workforce.sql",
        "02_sql/04_curated/mart_hiring.sql",
        "02_sql/04_curated/mart_learning.sql",
        "02_sql/04_curated/mart_engagement.sql",
        "02_sql/04_curated/mart_operations.sql",
        "02_sql/04_curated/mart_site_summary.sql",
    ]

    for file_path in files_to_run:
        run_sql_file(file_path)