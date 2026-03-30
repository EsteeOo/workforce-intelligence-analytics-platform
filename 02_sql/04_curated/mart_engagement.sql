CREATE OR REPLACE VIEW mart_engagement AS
SELECT
    country,
    department,
    survey_month,
    COUNT(*) AS survey_count,
    ROUND(AVG(engagement_score), 1) AS avg_engagement_score,
    ROUND(AVG(wellbeing_score), 1) AS avg_wellbeing_score,
    ROUND(AVG(manager_support_score), 1) AS avg_manager_support_score,
    ROUND(AVG(career_growth_score), 1) AS avg_career_growth_score,
    ROUND(AVG(inclusion_score), 1) AS avg_inclusion_score,
    ROUND(AVG(intent_to_leave_flag), 4) AS intent_to_leave_rate,
    SUM(low_engagement_flag) AS low_engagement_count,
    SUM(low_wellbeing_flag) AS low_wellbeing_count,
    SUM(low_manager_support_flag) AS low_manager_support_count
FROM stg_engagement_surveys
GROUP BY
    country, department, survey_month;