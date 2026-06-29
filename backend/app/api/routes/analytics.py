from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.analytics import AnalyticsOverviewOut, MonitoringOut
from app.services import analytics_service

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/monitoring", response_model=MonitoringOut)
def monitoring(db: Session = Depends(get_db)):
    return analytics_service.get_monitoring(db)


@router.get("/overview", response_model=AnalyticsOverviewOut)
def overview(db: Session = Depends(get_db)):
    return analytics_service.get_overview(db)
