CREATE OR REPLACE VIEW mart_hiring AS
SELECT
    country,
    department,
    job_role,
    gender,
    application_month,
    COUNT(*) AS application_count,
    SUM(reached_screen_flag) AS screen_count,
    SUM(reached_interview_flag) AS interview_count,
    SUM(reached_offer_flag) AS offer_count,
    SUM(hired_flag) AS hired_count,
    ROUND(SUM(reached_screen_flag) * 1.0 / COUNT(*), 4) AS screen_rate,
    ROUND(SUM(reached_interview_flag) * 1.0 / COUNT(*), 4) AS interview_rate,
    ROUND(SUM(reached_offer_flag) * 1.0 / COUNT(*), 4) AS offer_rate,
    ROUND(SUM(hired_flag) * 1.0 / COUNT(*), 4) AS hire_rate
FROM stg_ats_pipeline
GROUP BY
    country, department, job_role, gender, application_month;