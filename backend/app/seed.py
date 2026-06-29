from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from app.models.integration import Integration
from app.models.notification import Notification
from app.models.template import Template
from app.models.trigger import Trigger
from app.services.simulation import seed_initial_executions

TEMPLATES = [
    ("Lead Nurture Pipeline", "Qualify leads, enrich with Clearbit, add to CRM, trigger personalised emails.", "popular", ["Typeform", "HubSpot", "Gmail"]),
    ("AI Customer Support Triage", "Classify tickets with GPT-4o, route to teams, auto-reply to FAQs.", "ai", ["Zendesk", "GPT-4o", "Slack"]),
    ("E-commerce Order Flow", "From Shopify purchase to fulfilment, confirmation email, and review request.", "new", ["Shopify", "ShipBob", "Klaviyo"]),
    ("Social Media Scheduler", "Generate AI captions, resize for each platform, schedule and track engagement.", "popular", ["Buffer", "GPT-4o", "Twitter"]),
    ("Invoice → Accounting Sync", "Parse PDF invoices with AI, extract line items, reconcile in QuickBooks.", "ai", ["Gmail", "GPT-4o", "QuickBooks"]),
    ("GitHub → Jira Auto-linker", "Detect PR mentions, create tickets, assign to sprint, notify on merge.", "new", ["GitHub", "Jira", "Slack"]),
]

INTEGRATIONS = [
    ("Slack", "#4a154b"), ("Jira", "#0052cc"), ("Gmail", "#ea4335"), ("HubSpot", "#ff7a59"),
    ("Salesforce", "#00a1e0"), ("Stripe", "#6772e5"), ("Shopify", "#96bf48"), ("GitHub", "#333"),
    ("Notion", "#172b4d"), ("Figma", "#e01e5a"), ("Facebook Ads", "#1877f2"), ("LinkedIn", "#0072b1"),
    ("AWS", "#ff9900"), ("Google Sheets", "#4285f4"), ("Airtable", "#00d1b2"), ("Klaviyo", "#e63946"),
    ("Git", "#f05032"), ("Zapier", "#764abc"),
]

TRIGGERS = [
    ("Webhook: new-lead", "POST /hooks/new-lead · instant", "🔗", "rgba(88,130,255,.1)", "var(--el)", True),
    ("Daily report email", "Every day at 9:00 AM UTC", "⏰", "rgba(16,217,160,.1)", "var(--em)", True),
    ("CRM sync", "Every 15 minutes", "🔄", "rgba(251,191,36,.1)", "var(--am)", True),
    ("Weekly analytics digest", "Every Monday 8:00 AM", "📊", "rgba(139,92,246,.1)", "var(--vi)", True),
    ("Payment failed handler", "Stripe webhook · on event", "💳", "rgba(244,114,182,.1)", "var(--pk)", True),
    ("Churn risk detector", "ML score trigger · paused", "🔔", "rgba(255,255,255,.05)", "var(--t3)", False),
]

NOTIFICATIONS = [
    ("Email campaign completed — 2,341 sent", "✓", "rgba(16,217,160,.1)", "var(--em)", 2),
    ("AI detected bottleneck in CRM Sync", "🤖", "rgba(88,130,255,.1)", "var(--el)", 14),
    ("Slack rate limit hit — retry scheduled", "⚠", "rgba(251,191,36,.1)", "var(--am)", 60),
    ('Sarah Chen shared "Product Launch Flow"', "👥", "rgba(139,92,246,.1)", "var(--vi)", 180),
]


def seed_all(db: Session) -> None:
    if db.query(Template).count() == 0:
        for title, desc, category, tags in TEMPLATES:
            db.add(Template(title=title, description=desc, category=category, tags=tags))

    if db.query(Integration).count() == 0:
        for i, (name, color) in enumerate(INTEGRATIONS):
            db.add(Integration(name=name, color=color, category="general", sort_order=i))

    if db.query(Trigger).count() == 0:
        for name, detail, icon, icon_bg, icon_color, active in TRIGGERS:
            db.add(Trigger(name=name, detail=detail, icon=icon, icon_bg=icon_bg, icon_color=icon_color, active=active))

    if db.query(Notification).count() == 0:
        now = datetime.now(timezone.utc)
        for message, icon, icon_bg, icon_color, minutes_ago in NOTIFICATIONS:
            db.add(
                Notification(
                    user_id=None, message=message, icon=icon, icon_bg=icon_bg,
                    icon_color=icon_color, read=False, created_at=now - timedelta(minutes=minutes_ago),
                )
            )

    db.commit()
    seed_initial_executions(db)
