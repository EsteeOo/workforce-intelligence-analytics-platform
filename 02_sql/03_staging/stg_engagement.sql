CREATE OR REPLACE VIEW stg_engagement_surveys AS
SELECT
    survey_id,
    employee_id,
    survey_date,
    country,
    department,
    engagement_score,
    wellbeing_score,
    manager_support_score,
    career_growth_score,
    inclusion_score,
    intent_to_leave_flag,
    DATE_TRUNC('month', survey_date) AS survey_month,
    CASE WHEN engagement_score < 50 THEN 1 ELSE 0 END AS low_engagement_flag,
    CASE WHEN wellbeing_score < 50 THEN 1 ELSE 0 END AS low_wellbeing_flag,
    CASE WHEN manager_support_score < 55 THEN 1 ELSE 0 END AS low_manager_support_flag
FROM raw_engagement_surveys;