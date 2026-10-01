from app.services.nl_sql_service import generate_sql
from app.services.sql_executor import execute_sql
from app.services.answer_service import generate_answer


def process_question(question: str):

    sql = generate_sql(question)

    results = execute_sql(sql)

    answer = generate_answer(
        question,
        sql,
        results
    )

    return {
        "question": question,
        "sql": sql,
        "results": results,
        "answer": answer
    }