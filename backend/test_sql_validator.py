from app.services.sql_validator import validate_sql


def test(sql):
    valid, message = validate_sql(sql)

    print("\nSQL:")
    print(sql)

    print("Valid:", valid)
    print("Message:", message)


test(
    "SELECT * FROM finished_goods LIMIT 5"
)

test(
    "DELETE FROM finished_goods"
)

test(
    "SELECT * FROM finished_goods"
)
    