import re

from app.core.config import get_settings

settings = get_settings()

APP_KEYWORDS = {
    "typeform": "Typeform",
    "hubspot": "HubSpot",
    "salesforce": "Salesforce",
    "gmail": "Gmail",
    "email": "Email",
    "slack": "Slack",
    "stripe": "Stripe",
    "shopify": "Shopify",
    "github": "GitHub",
    "jira": "Jira",
    "notion": "Notion",
    "airtable": "Airtable",
    "sheets": "Google Sheets",
    "twitter": "Twitter",
    "zendesk": "Zendesk",
}

TRIGGER_WORDS = ["when", "every time", "on new", "whenever"]


def generate_reply(message: str) -> str:
    """Rule-based workflow generator used as the offline fallback for the AI assistant.

    If OPENAI_API_KEY is configured this could be swapped for a real call to the
    OpenAI Chat Completions API; without a key we deterministically parse the
    message for known app names and produce a believable workflow summary.
    """
    text = message.lower()
    apps_found = [label for key, label in APP_KEYWORDS.items() if key in text]

    if not apps_found:
        return (
            "I can help with that! Tell me which apps you'd like to connect "
            "(e.g. \"When a new Typeform response comes in, add the lead to HubSpot "
            "and notify Slack\") and I'll build the workflow for you."
        )

    steps = []
    icons = ["①", "②", "③", "④", "⑤"]
    colors = ["var(--el)", "var(--vi)", "var(--em)", "var(--pk)", "var(--am)"]
    for i, app in enumerate(apps_found[:5]):
        action = "New event" if i == 0 else "Process / notify"
        steps.append(f'<span style="color:{colors[i % len(colors)]}">{icons[i]} {app}</span> → {action}')

    is_trigger_phrase = any(w in text for w in TRIGGER_WORDS)
    intro = "Got it! I've built this workflow:" if is_trigger_phrase else "Here's a workflow based on your request:"
    saved = round(1.5 + len(apps_found) * 0.8, 1)

    return (
        f"{intro}<br><br>" + "<br>".join(steps) +
        f"<br><br>Estimated time saved: <strong style=\"color:var(--em)\">~{saved} min/run</strong>. "
        "Ready to activate?"
    )
