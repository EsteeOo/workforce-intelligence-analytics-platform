# Data Model Design

## Overview
The data model is structured to integrate multiple workforce domains into a unified analytical framework. The design follows a dimensional modelling approach, with clearly defined fact tables and shared dimensions.

---

# Core Dimensions

## dim_employee
**Grain:** One row per employee

| Column | Description |
|---|---|
employee_id | Unique employee identifier
gender | Gender category
ethnicity | Ethnicity category
age_band | Age group classification
hire_date | Employee hire date
termination_date | Employee termination date (if applicable)
job_level | Job seniority level
job_role | Job title
department | Department name
country | Country
site | Physical or organisational site

---

## dim_date
**Grain:** One row per date

| Column | Description |
|---|---|
date | Calendar date
year | Year
quarter | Quarter
month | Month
month_name | Month name
week | Week number

---

## dim_job_role
**Grain:** One row per job role

| Column | Description |
|---|---|
job_role | Job title
job_family | Job grouping
job_level | Seniority band

---

## dim_department
**Grain:** One row per department

| Column | Description |
|---|---|
department | Department name
function | Functional grouping

---

## dim_location
**Grain:** One row per site

| Column | Description |
|---|---|
site | Site name
country | Country
region | Region

---

# Fact Tables

---

## fact_workforce_snapshot
**Grain:** One row per employee per month

| Column | Description |
|---|---|
employee_id | Employee identifier
snapshot_date | Month snapshot date
headcount_flag | 1 if active
attrition_flag | 1 if employee left in that month
tenure_months | Tenure at snapshot
salary | Salary value

---

## fact_attrition_events
**Grain:** One row per employee exit

| Column | Description |
|---|---|
employee_id | Employee identifier
termination_date | Exit date
attrition_type | Voluntary / Involuntary
reason | Exit reason

---

## fact_hiring_pipeline
**Grain:** One row per candidate per stage

| Column | Description |
|---|---|
candidate_id | Candidate identifier
job_role | Role applied for
stage | Application stage
stage_date | Date of stage
status | Passed / Failed
time_in_stage_days | Duration in stage

---

## fact_learning_records
**Grain:** One row per employee per course

| Column | Description |
|---|---|
employee_id | Employee identifier
course_id | Course identifier
completion_status | Completed / Incomplete
completion_date | Completion date
score | Assessment score

---

## fact_engagement_scores
**Grain:** One row per employee per survey period

| Column | Description |
|---|---|
employee_id | Employee identifier
survey_date | Survey period
engagement_score | Overall engagement
wellbeing_score | Wellbeing rating
manager_score | Manager support score

---

## fact_workforce_operations
**Grain:** One row per employee per day

| Column | Description |
|---|---|
employee_id | Employee identifier
date | Work date
hours_worked | Hours worked
overtime_hours | Overtime hours
absence_flag | 1 if absent
shift_type | Shift classification

---

# Relationships

- dim_employee → all fact tables via employee_id
- dim_date → all fact tables via date fields
- dim_job_role → workforce and hiring
- dim_department → workforce and engagement
- dim_location → workforce and operations

---

# Data Behaviour Design (Critical)

The dataset will intentionally reflect real-world imbalance and variation:

## Workforce Distribution
- Larger headcount in specific countries and sites
- Uneven department sizes
- Senior roles concentrated in fewer locations

## Attrition Patterns
- Higher attrition in:
  - early tenure (< 12 months)
  - specific departments (e.g. operations)
  - specific sites
- Lower attrition in senior roles

## Hiring Patterns
- Drop-off at interview stages
- Longer hiring cycles for senior roles
- Hard-to-fill roles concentrated in specific job families

## Learning Patterns
- Higher completion in corporate roles
- Lower completion in operational roles
- Overdue training clustered in specific departments

## Engagement Patterns
- Lower engagement in high-pressure sites
- Correlation between low engagement and higher attrition

## Workforce Operations
- Overtime concentrated in understaffed sites
- Absence spikes in specific locations
- Shift patterns vary by job role

---

# Design Principle

The model is structured to ensure:
- measurable variation across dimensions
- realistic imbalance across workforce segments
- cross-domain relationships enabling multi-layer analysis