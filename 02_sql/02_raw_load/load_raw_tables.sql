DELETE FROM raw_hris_employee_master;
DELETE FROM raw_ats_pipeline;
DELETE FROM raw_lms_learning_records;
DELETE FROM raw_engagement_surveys;
DELETE FROM raw_timekeeping_weekly_records;

INSERT INTO raw_hris_employee_master
SELECT * FROM read_csv_auto('01_raw/hris/hris_employee_master.csv', header=true);

INSERT INTO raw_ats_pipeline
SELECT * FROM read_csv_auto('01_raw/ats/ats_pipeline.csv', header=true);

INSERT INTO raw_lms_learning_records
SELECT * FROM read_csv_auto('01_raw/lms/lms_learning_records.csv', header=true);

INSERT INTO raw_engagement_surveys
SELECT * FROM read_csv_auto('01_raw/engagement/engagement_surveys.csv', header=true);

INSERT INTO raw_timekeeping_weekly_records
SELECT * FROM read_csv_auto('01_raw/timekeeping/timekeeping_weekly_records.csv', header=true);