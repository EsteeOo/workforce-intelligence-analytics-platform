CREATE OR REPLACE TABLE raw_hris_employee_master (
    employee_id VARCHAR,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR,
    ethnicity VARCHAR,
    age_band VARCHAR,
    country VARCHAR,
    site VARCHAR,
    department VARCHAR,
    job_role VARCHAR,
    job_level VARCHAR,
    hire_date DATE,
    termination_date DATE,
    employment_status VARCHAR,
    tenure_months INTEGER,
    salary INTEGER,
    manager_flag INTEGER
);

CREATE OR REPLACE TABLE raw_ats_pipeline (
    candidate_id VARCHAR,
    application_date DATE,
    country VARCHAR,
    department VARCHAR,
    job_role VARCHAR,
    gender VARCHAR,
    current_stage VARCHAR,
    hired_flag INTEGER,
    Applied_date DATE,
    Screen_date DATE,
    Interview_date DATE,
    Offer_date DATE,
    Hired_date DATE
);

CREATE OR REPLACE TABLE raw_lms_learning_records (
    learning_record_id VARCHAR,
    employee_id VARCHAR,
    course_id VARCHAR,
    course_name VARCHAR,
    mandatory_flag INTEGER,
    assignment_date DATE,
    due_date DATE,
    completion_date DATE,
    completion_status VARCHAR,
    days_to_complete INTEGER,
    overdue_flag INTEGER,
    department VARCHAR,
    country VARCHAR
);

CREATE OR REPLACE TABLE raw_engagement_surveys (
    survey_id VARCHAR,
    employee_id VARCHAR,
    survey_date DATE,
    country VARCHAR,
    department VARCHAR,
    engagement_score DOUBLE,
    wellbeing_score DOUBLE,
    manager_support_score DOUBLE,
    career_growth_score DOUBLE,
    inclusion_score DOUBLE,
    intent_to_leave_flag INTEGER
);

CREATE OR REPLACE TABLE raw_timekeeping_weekly_records (
    timekeeping_record_id VARCHAR,
    employee_id VARCHAR,
    week_start_date DATE,
    country VARCHAR,
    department VARCHAR,
    shift_type VARCHAR,
    scheduled_hours DOUBLE,
    actual_hours DOUBLE,
    overtime_hours DOUBLE,
    absence_hours DOUBLE,
    pressure_flag INTEGER
);