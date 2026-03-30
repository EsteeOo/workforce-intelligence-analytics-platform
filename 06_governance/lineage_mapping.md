# Lineage Mapping

## End-to-End Data Flow

### Source Layer
Synthetic enterprise datasets are generated in Python for:
- HRIS
- ATS
- LMS
- Engagement
- Timekeeping

### Raw Layer
Generated source extracts are landed as raw files and loaded into DuckDB raw tables.

### Staging Layer
Raw source tables are cleaned, standardised, and enhanced with reusable analytical flags and helper date logic.

### Curated Layer
Business logic is applied to create reporting-ready marts:
- mart_workforce
- mart_hiring
- mart_learning
- mart_engagement
- mart_operations
- mart_site_summary

### Semantic Layer
Curated marts are imported into Power BI, connected through shared dimensions, and extended with DAX measures.

### Consumption Layer
Insights are surfaced through six report pages:
- Executive Overview
- Workforce & Retention
- Hiring Funnel
- Learning & Compliance
- Engagement & Sentiment
- Operations & Workforce Pressure

## Traceability Principle
Each reported KPI can be traced from:
Python source generation → raw ingest → staging logic → curated mart → semantic measure → dashboard visual