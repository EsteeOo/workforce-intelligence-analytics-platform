# Refresh Orchestration

## Overview

The platform follows a structured refresh sequence from source generation through to reporting consumption.

## Refresh Sequence

### 1. Source Generation
Python scripts generate the source datasets for workforce, hiring, learning, engagement, and operations.

### 2. Raw Ingestion
Source extracts are loaded into DuckDB raw tables.

### 3. Staging Transformations
Staging SQL views apply standardisation, validation, and reusable analytical flags.

### 4. Curated Mart Refresh
Curated marts are rebuilt to provide reporting-ready datasets.

### 5. Export Layer
Curated outputs are exported for semantic consumption in Power BI.

### 6. Reporting Refresh
Power BI is refreshed using the curated outputs.

## Operational Notes
- The current implementation supports local execution
- The design is structured for future orchestration in tools such as Fabric pipelines or Airflow
- Governance artefacts support traceability and repeatability across refresh cycles