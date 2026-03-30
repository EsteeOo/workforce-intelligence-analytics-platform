CREATE OR REPLACE VIEW stg_ats_pipeline AS
SELECT
    candidate_id,
    application_date,
    country,
    department,
    job_role,
    gender,
    current_stage,
    hired_flag,
    Applied_date,
    Screen_date,
    Interview_date,
    Offer_date,
    Hired_date,
    DATE_TRUNC('month', application_date) AS application_month,
    CASE WHEN current_stage IN ('Screen', 'Interview', 'Offer', 'Hired') THEN 1 ELSE 0 END AS reached_screen_flag,
    CASE WHEN current_stage IN ('Interview', 'Offer', 'Hired') THEN 1 ELSE 0 END AS reached_interview_flag,
    CASE WHEN current_stage IN ('Offer', 'Hired') THEN 1 ELSE 0 END AS reached_offer_flag
FROM raw_ats_pipeline;