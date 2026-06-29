from fastapi import APIRouter

from app.schemas.analytics import ChatRequest, ChatResponse
from app.services import ai_service

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest):
    reply = ai_service.generate_reply(payload.message)
    return ChatResponse(reply=reply)
