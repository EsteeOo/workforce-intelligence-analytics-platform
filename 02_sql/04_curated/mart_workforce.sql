CREATE OR REPLACE VIEW mart_workforce AS
SELECT
    country,
    site,
    department,
    job_role,
    job_level,
    gender,
    ethnicity,
    COUNT(*) AS employee_count,
    SUM(active_flag) AS active_headcount,
    SUM(attrition_flag) AS attrition_count,
    ROUND(SUM(attrition_flag) * 1.0 / COUNT(*), 4) AS attrition_rate,
    SUM(CASE WHEN attrition_flag = 1 AND early_tenure_flag = 1 THEN 1 ELSE 0 END) AS early_attrition_count,
    ROUND(AVG(tenure_months), 1) AS avg_tenure_months,
    ROUND(AVG(salary), 0) AS avg_salary,
    SUM(manager_flag) AS manager_count
FROM stg_hris_employee_master
GROUP BY
    country, site, department, job_role, job_level, gender, ethnicity;