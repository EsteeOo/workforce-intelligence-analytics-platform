# Data Generation Plan

## Objective
Define the logic used to generate representative workforce datasets across workforce, hiring, learning, engagement, and workforce operations domains.

## Design Principles
- Data generation follows defined table grain
- Variation is intentional rather than random
- Country, site, department, and role differences are visible in the final data
- Workforce conditions reflect imbalance, pressure, and uneven outcomes
- Cross-domain patterns are preserved to support analytical storytelling

## Domains
- HRIS
- ATS
- LMS
- Engagement
- Timekeeping

## Core Behaviour Patterns
- Larger workforce concentration in selected countries and sites
- Higher attrition in early tenure and selected operational areas
- Lower training completion in higher-pressure functions
- Lower engagement in sites with higher pressure and overtime
- Hard-to-fill roles concentrated in selected role families
- Overtime and absence clustered in selected sites and functions

## Output Standard
Each dataset is exportable as a raw CSV extract to the corresponding source folder.

## Behaviour Controls

### Workforce Distribution
- The United Kingdom carries the largest workforce share
- Germany carries elevated attrition and lower engagement
- The Netherlands represents the strongest stability and engagement
- Ireland remains smaller but shows local pressure patterns
- France shows moderate risk with lower training completion than higher-performing locations

### Department Conditions
- Operations and Supply Chain carry the highest pressure
- Customer Support carries elevated early attrition risk
- Technology is harder to hire for but shows stronger training completion
- People and Finance show stronger stability and training compliance

### Cross-Domain Patterns
- Low engagement increases attrition likelihood
- High overtime increases absence likelihood
- Low training completion is more common in higher-pressure functions
- Hard-to-fill roles create pressure through prolonged vacancy periods