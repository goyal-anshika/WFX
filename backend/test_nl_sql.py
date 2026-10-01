from app.services.nl_sql_service import generate_sql


question = "Which buyer has the highest number of sales orders?"

sql = generate_sql(question)

print("\nGENERATED SQL:")
print(sql)