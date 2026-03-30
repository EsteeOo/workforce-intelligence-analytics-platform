# SQL Model Plan

## Objective

Implement a structured transformation layer between the raw source extracts and the reporting model.

## SQL Layer Structure

- Raw tables ingest landed source extracts
- Staging views standardise, clean, and derive reusable fields
- Curated marts provide reporting-ready analytical outputs

## Raw Domains

- HRIS
- ATS
- LMS
- Engagement
- Timekeeping

## Transformation Approach

The SQL layer is designed to preserve source integrity while separating cleaning, standardisation, and business-oriented modelling into distinct layers.

### Raw Layer
- Preserves source-aligned structure
- Supports validation of row counts and ingestion logic

### Staging Layer
- Standardises data types and naming
- Derives analytical flags and helper dates
- Keeps transformations source-aligned

### Curated Layer
- Applies business logic for reporting
- Aggregates data into marts aligned to workforce, hiring, learning, engagement, and operations domains
- Supports direct consumption in Power BI

## Planned Outputs

- Source-aligned raw tables
- Reusable staging views
- Reporting marts across workforce, hiring, capability, engagement, and pressure

## Modelling Direction

The reporting model follows a curated mart design with shared dimensions in Power BI, enabling cross-domain filtering and executive reporting.