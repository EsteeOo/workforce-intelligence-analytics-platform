CREATE OR REPLACE VIEW stg_lms_learning_records AS
SELECT
    learning_record_id,
    employee_id,
    course_id,
    course_name,
    mandatory_flag,
    assignment_date,
    due_date,
    completion_date,
    completion_status,
    days_to_complete,
    overdue_flag,
    department,
    country,
    CASE WHEN completion_status = 'Completed' THEN 1 ELSE 0 END AS completed_flag,
    DATE_TRUNC('month', assignment_date) AS assignment_month,
    DATE_TRUNC('month', due_date) AS due_month,
    DATE_TRUNC('month', completion_date) AS completion_month
FROM raw_lms_learning_records;