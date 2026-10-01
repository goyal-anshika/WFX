from sqlalchemy import text

from app.database import engine
from app.services.sql_validator import validate_sql


def execute_sql(sql: str):

    valid, message = validate_sql(sql)

    if not valid:
        raise ValueError(message)

    with engine.connect() as connection:

        result = connection.execute(text(sql))

        rows = result.mappings().all()

    return [dict(row) for row in rows]