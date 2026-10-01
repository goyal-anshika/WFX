import re


ALLOWED_TABLES = {
    "suppliers",
    "buyers",
    "finished_goods",
    "sales_orders",
    "tech_packs",
    "sales_invoices",
}


def validate_sql(sql: str):

    sql = sql.strip()
    sql_lower = sql.lower()

    # Only allow SELECT queries
    if not sql_lower.startswith("select"):
        return False, "Only SELECT queries are allowed."

    # Prevent multiple SQL statements
    if ";" in sql[:-1]:
        return False, "Multiple SQL statements are not allowed."

    # Block dangerous SQL commands
    forbidden = [
        "insert",
        "update",
        "delete",
        "drop",
        "alter",
        "truncate",
        "create",
        "grant",
        "revoke",
    ]

    for keyword in forbidden:
        if re.search(rf"\b{keyword}\b", sql_lower):
            return False, f"SQL keyword '{keyword}' is not allowed."

    # Require an allowed WFX table
    if not any(
        re.search(rf"\b{table}\b", sql_lower)
        for table in ALLOWED_TABLES
    ):
        return False, "Query does not reference an allowed WFX table."

    # Aggregation queries normally return a small number of rows
    aggregation_functions = [
        "count(",
        "sum(",
        "avg(",
        "min(",
        "max(",
    ]

    is_aggregation = any(
        function in sql_lower
        for function in aggregation_functions
    )

    # Normal queries must have LIMIT
    if not is_aggregation and not re.search(r"\blimit\s+\d+", sql_lower):
        return False, "SQL query must contain a LIMIT clause."

    return True, "SQL is valid."