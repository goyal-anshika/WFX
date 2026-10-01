from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_query_service import process_question


router = APIRouter(
    prefix="/api/ai",
    tags=["AI"]
)


class QuestionRequest(BaseModel):
    question: str


@router.post("/query")
def ask_question(request: QuestionRequest):

    return process_question(request.question)