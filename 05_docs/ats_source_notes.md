# ATS Source Notes

## Dataset
ats_pipeline.csv

## Grain
One row per candidate application

## Core Fields
- candidate_id
- application_date
- country
- department
- job_role
- gender
- current_stage
- hired_flag
- Applied_date
- Screen_date
- Interview_date
- Offer_date
- Hired_date

## Behaviour Design
- The dataset represents a point-in-time recruitment pipeline snapshot
- Each candidate is assigned a current stage based on stage progression
- Hiring conversion varies by department, country, and selected demographic conditions
- Technology and operational roles are more difficult to convert through later stages
- The hiring distribution preserves visible imbalance across workforce segments