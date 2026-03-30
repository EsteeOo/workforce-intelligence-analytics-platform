# Data Quality Checks

## Completeness
- Key dimensions such as department, country, and site validated as populated
- Core metric fields checked for nulls across curated marts

## Consistency
- Standard naming conventions maintained across source, staging, and curated layers
- Date fields standardised to reporting periods where required
- Reusable metric definitions applied consistently in Power BI

## Accuracy
- Row counts validated between raw, staging, and curated layers
- Aggregation outputs cross-checked against source-level totals
- KPI calculations reviewed against expected logic

## Integrity
- Relationships validated in the semantic model
- Shared dimensions used consistently across marts
- No duplicate business keys expected in curated outputs at reporting grain

## Monitoring
- SQL quality check scripts implemented for raw and staging layers
- Quick validation scripts used to confirm source distributions and behavioural realism