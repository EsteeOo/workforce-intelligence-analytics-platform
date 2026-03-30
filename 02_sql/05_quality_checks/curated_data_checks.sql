SELECT 'mart_workforce' AS object_name, COUNT(*) AS row_count FROM mart_workforce
UNION ALL
SELECT 'mart_hiring', COUNT(*) FROM mart_hiring
UNION ALL
SELECT 'mart_learning', COUNT(*) FROM mart_learning
UNION ALL
SELECT 'mart_engagement', COUNT(*) FROM mart_engagement
UNION ALL
SELECT 'mart_operations', COUNT(*) FROM mart_operations
UNION ALL
SELECT 'mart_site_summary', COUNT(*) FROM mart_site_summary;