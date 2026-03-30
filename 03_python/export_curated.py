from pathlib import Path
import duckdb

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = ROOT_DIR / "02_sql" / "00_database" / "workforce_intelligence.duckdb"
OUTPUT_DIR = ROOT_DIR / "04_exports"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

conn = duckdb.connect(str(DB_PATH))

tables = [
    "mart_workforce",
    "mart_hiring",
    "mart_learning",
    "mart_engagement",
    "mart_operations",
    "mart_site_summary",
]

for table in tables:
    file_path = OUTPUT_DIR / f"{table}.csv"
    conn.execute(f"COPY {table} TO '{file_path.as_posix()}' (HEADER, DELIMITER ',')")
    print(f"Exported: {table} -> {file_path}")

conn.close()
print("Curated export complete.")