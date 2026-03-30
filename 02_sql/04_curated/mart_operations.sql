CREATE OR REPLACE VIEW mart_operations AS
SELECT
    country,
    department,
    shift_type,
    work_month,
    COUNT(*) AS record_count,
    ROUND(AVG(scheduled_hours), 2) AS avg_scheduled_hours,
    ROUND(AVG(actual_hours), 2) AS avg_actual_hours,
    ROUND(AVG(overtime_hours), 2) AS avg_overtime_hours,
    ROUND(AVG(absence_hours), 2) AS avg_absence_hours,
    SUM(overtime_flag) AS overtime_record_count,
    SUM(absence_flag) AS absence_record_count,
    SUM(high_overtime_flag) AS high_overtime_count,
    SUM(pressure_flag) AS pressure_record_count,
    ROUND(AVG(pressure_flag), 4) AS pressure_rate
FROM stg_timekeeping_weekly_records
GROUP BY
    country, department, shift_type, work_month;