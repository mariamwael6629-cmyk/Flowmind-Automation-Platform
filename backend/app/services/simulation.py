import random
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from app.models.execution import Execution

SAMPLE_EXECUTIONS = [
    ("s", "HubSpot lead enrichment"),
    ("s", "Stripe webhook processed"),
    ("s", "Email sequence fired"),
    ("w", "OpenAI rate limit — queuing"),
    ("s", "GitHub PR → Jira ticket"),
    ("s", "Shopify order fulfilled"),
    ("e", "Salesforce auth expired"),
    ("s", "Daily report sent"),
    ("s", "Airtable record updated"),
    ("s", "Slack alert fired"),
]

FRESH_AFTER_SECONDS = 5


def ensure_fresh_execution(db: Session) -> None:
    """Keep the execution log feeling alive by inserting a new simulated
    entry whenever the most recent one is older than a few seconds.
    """
    latest = db.query(Execution).order_by(Execution.created_at.desc()).first()
    now = datetime.now(timezone.utc)
    if latest is not None:
        created = latest.created_at.replace(tzinfo=timezone.utc) if latest.created_at.tzinfo is None else latest.created_at
        if (now - created).total_seconds() < FRESH_AFTER_SECONDS:
            return
    status, message = random.choice(SAMPLE_EXECUTIONS)
    db.add(Execution(message=message, status=status, duration_ms=random.uniform(400, 2200), created_at=now))
    db.commit()


def seed_initial_executions(db: Session) -> None:
    if db.query(Execution).count() > 0:
        return
    now = datetime.now(timezone.utc)
    for i, (status, message) in enumerate(SAMPLE_EXECUTIONS[:5]):
        db.add(
            Execution(
                message=message,
                status=status,
                duration_ms=random.uniform(400, 2200),
                created_at=now - timedelta(seconds=(5 - i) * 4),
            )
        )
    db.commit()
