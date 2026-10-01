from app.services.sql_executor import execute_sql


sql = """
SELECT company_name
FROM buyers
ORDER BY company_name
LIMIT 5
"""


results = execute_sql(sql)

print("\nDATABASE RESULTS:")

for row in results:
    print(row)