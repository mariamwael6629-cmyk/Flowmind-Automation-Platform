import random

from sqlalchemy.orm import Session

from app.models.workflow import Workflow
from app.schemas.analytics import AnalyticsOverviewOut, MonitoringOut, MonitoringSparklines


def get_monitoring(db: Session) -> MonitoringOut:
    active_workflows = db.query(Workflow).filter(Workflow.status == "active").count()
    base_active = 138 + active_workflows
    return MonitoringOut(
        executions_today=24891 + random.randint(0, 40),
        success_rate=99.8,
        avg_response=round(random.uniform(1.1, 1.35), 2),
        active_workflows=base_active,
        sparklines=MonitoringSparklines(
            executions=[65, 80, 70, 90, 85, 75, 95, 88, 92, 100, 78, 85],
            success=[98, 99, 97, 100, 99, 100, 98, 100, 99, 100, 98, 99],
            response=[60, 70, 55, 80, 65, 72, 58, 90, 68, 74, 62, 70],
            workflows=[70, 75, 80, 72, 85, 88, 80, 82, 90, 86, 88, 92],
        ),
    )


def get_overview(db: Session) -> AnalyticsOverviewOut:
    workflow_count = db.query(Workflow).count()
    return AnalyticsOverviewOut(
        time_saved="184h",
        tasks_automated=48291 + workflow_count * 12,
        cost_saved="$12.4k",
        error_rate=0.19,
        weekly_executions=[60, 77, 67, 87, 73, 100, 83],
    )
