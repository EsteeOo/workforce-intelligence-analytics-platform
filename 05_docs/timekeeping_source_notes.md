# Timekeeping Source Notes

## Dataset
timekeeping_weekly_records.csv

## Grain
One row per employee per week

## Core Fields
- timekeeping_record_id
- employee_id
- week_start_date
- country
- department
- shift_type
- scheduled_hours
- actual_hours
- overtime_hours
- absence_hours
- pressure_flag

## Behaviour Design
- Overtime risk varies by department and country
- Operations and Supply Chain carry the highest pressure
- Absence varies by country, department, and employee tenure
- Pressure is flagged where overtime or absence reaches elevated thresholds