SELECT 'raw_hris_employee_master' AS table_name, COUNT(*) AS row_count FROM raw_hris_employee_master
UNION ALL
SELECT 'raw_ats_pipeline', COUNT(*) FROM raw_ats_pipeline
UNION ALL
SELECT 'raw_lms_learning_records', COUNT(*) FROM raw_lms_learning_records
UNION ALL
SELECT 'raw_engagement_surveys', COUNT(*) FROM raw_engagement_surveys
UNION ALL
SELECT 'raw_timekeeping_weekly_records', COUNT(*) FROM raw_timekeeping_weekly_records;