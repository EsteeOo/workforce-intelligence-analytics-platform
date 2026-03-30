# LMS Source Notes

## Dataset
lms_learning_records.csv

## Grain
One row per employee-course assignment

## Core Fields
- learning_record_id
- employee_id
- course_id
- course_name
- mandatory_flag
- assignment_date
- due_date
- completion_date
- completion_status
- days_to_complete
- overdue_flag
- department
- country

## Behaviour Design
- Completion probability varies by department, course type, employment status, and country
- Mandatory courses have higher completion rates than optional courses
- Higher-pressure functions show lower completion and higher overdue volume
- Stronger functions show more consistent learning compliance
- Country-level behavioural variation introduces differentiated compliance maturity across regions