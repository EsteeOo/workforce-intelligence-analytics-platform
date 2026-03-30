# Staging Plan

## Objective
Standardise and prepare raw source data for downstream reporting and dimensional modelling.

## Staging Principles
- Preserve source granularity
- Standardise names and formats
- Derive reusable analytical flags
- Avoid report-specific aggregation in staging
- Keep staging logic source-aligned

## Planned Staging Outputs
- stg_hris_employee_master
- stg_ats_pipeline
- stg_lms_learning_records
- stg_engagement_surveys
- stg_timekeeping_weekly_records

## Planned Derived Fields
- active_flag
- attrition_flag
- early_tenure_flag
- hired_flag standardisation
- completed_flag
- overdue_flag standardisation
- high_pressure_flag
- week and month helper fields