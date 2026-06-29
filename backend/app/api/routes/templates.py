from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.integration import Integration
from app.models.template import Template
from app.schemas.template import IntegrationOut, TemplateOut

router = APIRouter(tags=["catalog"])


@router.get("/templates", response_model=list[TemplateOut])
def list_templates(limit: int = Query(default=6, le=200), db: Session = Depends(get_db)):
    return db.query(Template).order_by(Template.id).limit(limit).all()


@router.get("/integrations", response_model=list[IntegrationOut])
def list_integrations(db: Session = Depends(get_db)):
    return db.query(Integration).order_by(Integration.sort_order).all()
