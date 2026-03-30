CREATE OR REPLACE VIEW stg_timekeeping_weekly_records AS
SELECT
    timekeeping_record_id,
    employee_id,
    week_start_date,
    country,
    department,
    shift_type,
    scheduled_hours,
    actual_hours,
    overtime_hours,
    absence_hours,
    pressure_flag,
    DATE_TRUNC('month', week_start_date) AS work_month,
    CASE WHEN overtime_hours > 0 THEN 1 ELSE 0 END AS overtime_flag,
    CASE WHEN absence_hours > 0 THEN 1 ELSE 0 END AS absence_flag,
    CASE WHEN overtime_hours >= 8 THEN 1 ELSE 0 END AS high_overtime_flag
FROM raw_timekeeping_weekly_records;