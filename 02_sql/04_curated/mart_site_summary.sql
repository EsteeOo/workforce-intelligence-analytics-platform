CREATE OR REPLACE VIEW mart_site_summary AS
WITH workforce AS (
    SELECT
        country,
        site,
        COUNT(*) AS headcount,
        SUM(active_flag) AS active_headcount,
        SUM(attrition_flag) AS attrition_count,
        ROUND(SUM(attrition_flag) * 1.0 / COUNT(*), 4) AS attrition_rate
    FROM stg_hris_employee_master
    GROUP BY country, site
),
learning AS (
    SELECT
        h.country,
        h.site,
        ROUND(AVG(CASE WHEN l.completion_status = 'Completed' THEN 1.0 ELSE 0.0 END), 4) AS completion_rate,
        ROUND(AVG(CASE WHEN l.overdue_flag = 1 THEN 1.0 ELSE 0.0 END), 4) AS overdue_rate
    FROM stg_lms_learning_records l
    JOIN stg_hris_employee_master h
        ON l.employee_id = h.employee_id
    GROUP BY h.country, h.site
),
engagement AS (
    SELECT
        h.country,
        h.site,
        ROUND(AVG(e.engagement_score), 1) AS avg_engagement_score,
        ROUND(AVG(e.wellbeing_score), 1) AS avg_wellbeing_score,
        ROUND(AVG(e.intent_to_leave_flag), 4) AS intent_to_leave_rate
    FROM stg_engagement_surveys e
    JOIN stg_hris_employee_master h
        ON e.employee_id = h.employee_id
    GROUP BY h.country, h.site
),
operations AS (
    SELECT
        h.country,
        h.site,
        ROUND(AVG(t.overtime_hours), 2) AS avg_overtime_hours,
        ROUND(AVG(t.absence_hours), 2) AS avg_absence_hours,
        ROUND(AVG(t.pressure_flag), 4) AS pressure_rate
    FROM stg_timekeeping_weekly_records t
    JOIN stg_hris_employee_master h
        ON t.employee_id = h.employee_id
    GROUP BY h.country, h.site
)
SELECT
    w.country,
    w.site,
    w.headcount,
    w.active_headcount,
    w.attrition_count,
    w.attrition_rate,
    l.completion_rate,
    l.overdue_rate,
    e.avg_engagement_score,
    e.avg_wellbeing_score,
    e.intent_to_leave_rate,
    o.avg_overtime_hours,
    o.avg_absence_hours,
    o.pressure_rate
FROM workforce w
LEFT JOIN learning l
    ON w.country = l.country AND w.site = l.site
LEFT JOIN engagement e
    ON w.country = e.country AND w.site = e.site
LEFT JOIN operations o
    ON w.country = o.country AND w.site = o.site;