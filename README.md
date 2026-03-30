# Workforce Intelligence Analytics Platform

## Overview

This project delivers an end-to-end workforce analytics platform, combining data engineering, analytical modelling, and executive reporting to provide a comprehensive view of workforce performance, risk, and operational efficiency.

## Business Problem

Organisations often struggle to understand workforce performance holistically due to fragmented data across HR, learning, and operational systems.

This leads to:
- Limited visibility into attrition drivers  
- Disconnected hiring and retention strategies  
- Poor tracking of compliance and learning completion  
- Lack of insight into employee engagement and wellbeing  
- Inability to identify operational pressure and workforce strain  

## Solution

This platform consolidates workforce data into a structured analytics pipeline and delivers a multi-page Power BI dashboard that enables:

- End-to-end workforce visibility  
- Identification of attrition and retention risks  
- Analysis of hiring funnel performance  
- Monitoring of learning and compliance metrics  
- Assessment of engagement and sentiment  
- Detection of operational pressure and workload strain  

## Architecture Overview

The solution follows a layered data architecture:

- Source Layer (Python data generation)  
- Raw Layer (DuckDB ingestion)  
- Staging Layer (cleaning and validation)  
- Curated Layer (analytical marts)  
- Semantic Layer (Power BI model)  
- Consumption Layer (dashboards)  

## Project Structure

- 01_raw  
- 02_sql  
- 03_python  
- 04_powerbi  
- 05_docs  
- 06_governance  
- 07_diagrams  
- 08_automation  
- 09_exports  
- 10_outputs  

## Data Modelling Approach

The data model follows a curated mart-based structure:

- Domain-based marts (workforce, hiring, learning, engagement, operations)  
- Shared dimensions (department, country, site)  
- Centralised measures in Power BI  
- Relationships enabling cross-domain analysis  

## Key Metrics

- Attrition Rate  
- Early Attrition Rate  
- Hiring Conversion Rates  
- Completion Rate  
- Engagement Score  
- Wellbeing Score  
- Intent to Leave Rate  
- Overtime Rate  
- Absence Rate  
- Pressure Rate  

## Dashboard Overview

1. Executive Overview  
2. Workforce & Retention  
3. Hiring Funnel  
4. Learning & Compliance  
5. Engagement & Sentiment  
6. Operations & Workforce Pressure  

## Key Insights

- Attrition levels are elevated across several departments  
- Engagement scores are below optimal thresholds  
- Hiring is largely replacement-driven  
- Learning completion highlights compliance gaps  
- Operational pressure is increasing  

## Governance and Quality

- Business glossary  
- Data dictionary  
- Metric dictionary  
- Data lineage  
- Data quality checks  

## Automation Design

- Python data generation  
- SQL transformation layers  
- Structured refresh pipeline  
- Ready for orchestration tools  

## Tools and Technologies

- Python  
- SQL (DuckDB)  
- Power BI  
- DAX  

## Future Enhancements

- Power BI Service deployment  
- Copilot narrative insights  
- Predictive analytics (attrition forecasting)  
- Full pipeline automation  

## Closing

This project demonstrates end-to-end capability across analytics engineering, data modelling, business intelligence, and governance.