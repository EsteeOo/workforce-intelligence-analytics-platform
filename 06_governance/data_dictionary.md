# Data Dictionary

## mart_workforce

| Column | Description |
|---|---|
| country | Employee country grouping |
| site | Site or office location |
| department | Functional department |
| job_role | Role title |
| job_level | Role seniority category |
| gender | Gender category |
| ethnicity | Ethnicity category |
| employee_count | Employee volume in the grouped segment |
| active_headcount | Active employee count |
| attrition_count | Leaver count |
| attrition_rate | Attrition rate within the segment |
| early_attrition_count | Early leaver count |
| avg_tenure_months | Average tenure in months |
| avg_salary | Average salary within the segment |
| manager_count | Count of managerial roles |

## mart_hiring

| Column | Description |
|---|---|
| country | Hiring country |
| department | Hiring department |
| job_role | Role being hired |
| gender | Candidate gender |
| application_month | Month of application |
| application_count | Total applications |
| screen_count | Candidates reaching screening stage |
| interview_count | Candidates reaching interview stage |
| offer_count | Offers issued |
| hired_count | Successful hires |
| screen_rate | Screen conversion rate |
| interview_rate | Interview conversion rate |
| offer_rate | Offer conversion rate |
| hire_rate | Hire conversion rate |

## mart_learning

| Column | Description |
|---|---|
| country | Learning country |
| department | Learning department |
| course_name | Learning course |
| mandatory_flag | Mandatory vs optional indicator |
| assignment_month | Assignment month |
| learning_record_count | Learning assignment volume |
| completed_count | Completed learning count |
| overdue_count | Overdue learning count |
| completion_rate | Completion percentage |
| overdue_rate | Overdue percentage |
| avg_days_to_complete | Average completion time |

## mart_engagement

| Column | Description |
|---|---|
| country | Engagement country |
| department | Engagement department |
| survey_month | Survey month |
| survey_count | Survey response volume |
| avg_engagement_score | Average engagement score |
| avg_wellbeing_score | Average wellbeing score |
| avg_manager_support_score | Average manager support score |
| avg_career_growth_score | Average career growth score |
| avg_inclusion_score | Average inclusion score |
| intent_to_leave_rate | Intent to leave rate |
| low_engagement_count | Count of low engagement responses |
| low_wellbeing_count | Count of low wellbeing responses |
| low_manager_support_count | Count of low manager support responses |

## mart_operations

| Column | Description |
|---|---|
| country | Operations country |
| department | Operations department |
| shift_type | Shift pattern |
| work_month | Operational month |
| record_count | Operational record volume |
| avg_scheduled_hours | Average scheduled hours |
| avg_actual_hours | Average actual hours |
| avg_overtime_hours | Average overtime hours |
| avg_absence_hours | Average absence hours |
| overtime_record_count | Records with overtime |
| absence_record_count | Records with absence |
| high_overtime_count | High overtime records |
| pressure_record_count | Pressure records |
| pressure_rate | Pressure rate |

## mart_site_summary

| Column | Description |
|---|---|
| country | Site country |
| site | Site name |
| headcount | Total site headcount |
| active_headcount | Active site headcount |
| attrition_count | Site leaver count |
| attrition_rate | Site attrition rate |
| completion_rate | Site learning completion rate |
| overdue_rate | Site overdue learning rate |
| avg_engagement_score | Site average engagement |
| avg_wellbeing_score | Site average wellbeing |
| intent_to_leave_rate | Site intent to leave rate |
| avg_overtime_hours | Site average overtime |
| avg_absence_hours | Site average absence |
| pressure_rate | Site operational pressure rate |