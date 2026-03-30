SELECT 'stg_hris_employee_master' AS view_name, COUNT(*) AS row_count FROM stg_hris_employee_master
UNION ALL
SELECT 'stg_ats_pipeline', COUNT(*) FROM stg_ats_pipeline
UNION ALL
SELECT 'stg_lms_learning_records', COUNT(*) FROM stg_lms_learning_records
UNION ALL
SELECT 'stg_engagement_surveys', COUNT(*) FROM stg_engagement_surveys
UNION ALL
SELECT 'stg_timekeeping_weekly_records', COUNT(*) FROM stg_timekeeping_weekly_records;