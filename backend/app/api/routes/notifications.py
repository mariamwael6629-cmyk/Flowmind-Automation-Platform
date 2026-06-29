from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user_optional
from app.db.database import get_db
from app.models.notification import Notification
from app.models.user import User
from app.schemas.execution import NotificationOut
from app.services.utils import time_ago

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.get("", response_model=list[NotificationOut])
def list_notifications(
    db: Session = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
):
    query = db.query(Notification)
    query = query.filter(Notification.user_id == current_user.id) if current_user else query.filter(Notification.user_id.is_(None))
    rows = query.order_by(Notification.created_at.desc()).limit(20).all()
    return [
        NotificationOut(
            id=r.id, message=r.message, icon=r.icon, icon_bg=r.icon_bg,
            icon_color=r.icon_color, read=r.read, time_ago=time_ago(r.created_at),
        )
        for r in rows
    ]


@router.patch("/mark-read", status_code=204)
def mark_all_read(
    db: Session = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
):
    query = db.query(Notification)
    query = query.filter(Notification.user_id == current_user.id) if current_user else query.filter(Notification.user_id.is_(None))
    query.update({Notification.read: True})
    db.commit()
    return None
