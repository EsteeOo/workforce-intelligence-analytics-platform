CREATE OR REPLACE VIEW mart_learning AS
SELECT
    country,
    department,
    course_name,
    mandatory_flag,
    assignment_month,
    COUNT(*) AS learning_record_count,
    SUM(completed_flag) AS completed_count,
    SUM(overdue_flag) AS overdue_count,
    ROUND(SUM(completed_flag) * 1.0 / COUNT(*), 4) AS completion_rate,
    ROUND(SUM(overdue_flag) * 1.0 / COUNT(*), 4) AS overdue_rate,
    ROUND(AVG(days_to_complete), 1) AS avg_days_to_complete
FROM stg_lms_learning_records
GROUP BY
    country, department, course_name, mandatory_flag, assignment_month;