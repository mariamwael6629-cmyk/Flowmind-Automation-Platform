from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.execution import Execution
from app.models.trigger import Trigger
from app.schemas.execution import ExecutionOut, TriggerOut, TriggerUpdate
from app.services.simulation import ensure_fresh_execution
from app.services.utils import time_ago

router = APIRouter(tags=["monitoring"])


@router.get("/executions/recent", response_model=list[ExecutionOut])
def recent_executions(limit: int = Query(default=6, le=50), db: Session = Depends(get_db)):
    ensure_fresh_execution(db)
    rows = db.query(Execution).order_by(Execution.created_at.desc()).limit(limit).all()
    return [
        ExecutionOut(id=r.id, message=r.message, status=r.status, time_ago=time_ago(r.created_at))
        for r in rows
    ]


@router.get("/triggers", response_model=list[TriggerOut])
def list_triggers(db: Session = Depends(get_db)):
    return db.query(Trigger).order_by(Trigger.id).all()


@router.patch("/triggers/{trigger_id}", response_model=TriggerOut)
def update_trigger(trigger_id: int, payload: TriggerUpdate, db: Session = Depends(get_db)):
    trigger = db.query(Trigger).filter(Trigger.id == trigger_id).first()
    if not trigger:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Trigger not found")
    trigger.active = payload.active
    db.commit()
    db.refresh(trigger)
    return trigger
