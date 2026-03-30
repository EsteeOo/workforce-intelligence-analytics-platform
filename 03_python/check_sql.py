from pathlib import Path
import sys
import duckdb

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = ROOT_DIR / "02_sql" / "00_database" / "workforce_intelligence.duckdb"


def run_query(sql_file_relative_path):
    sql_file_path = ROOT_DIR / sql_file_relative_path

    with open(sql_file_path, "r", encoding="utf-8") as f:
        sql = f.read()

    conn = duckdb.connect(str(DB_PATH))
    result = conn.execute(sql).fetchdf()
    conn.close()

    print(result)


if __name__ == "__main__":
    target = sys.argv[1].lower() if len(sys.argv) > 1 else "raw"

    if target == "raw":
        run_query("02_sql/05_quality_checks/raw_data_checks.sql")
    elif target == "staging":
        run_query("02_sql/05_quality_checks/staging_data_checks.sql")
    elif target == "curated":
        run_query("02_sql/05_quality_checks/curated_data_checks.sql")
    else:
        print("Use: python 03_python/check_sql.py [raw|staging|curated]")