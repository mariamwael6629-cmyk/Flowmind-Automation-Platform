# 🚀 FlowMind: AI-Powered Workflow Automation Platform

FlowMind is a modern, full-stack workflow automation engine designed to connect disjointed applications and automate business processes seamlessly. By leveraging artificial intelligence, FlowMind translates plain English instructions into complex, multi-step visual event pipelines with advanced branching logic, real-time monitoring, and structured ROI tracking.

---

## 🏗️ Platform Architecture

FlowMind operates on a highly scalable **Trigger-Logic-Action** node infrastructure:

*   **Triggers:** Supports instant webhooks (`POST /hooks/*`), custom API events, and time-based automation routines (Cron jobs).
*   **Conditional Logic:** Implements native IF/THEN branching, filters, and dynamic data loops to handle complex decision trees with zero code.
*   **Actions & Integrations:** Built-in connection layers for **500+ applications** including Slack, HubSpot, Gmail, Salesforce, Stripe, Shopify, GitHub, Jira, and AWS.

---

## ✨ Key Features

### 🎨 1. Visual Workflow Canvas
A professional-grade, drag-and-drop node editor with animated connections and color-coded components (Blue for Triggers, Purple for Logic/AI, Green for Actions) that makes managing complex corporate workflows completely intuitive.

### 🤖 2. Plain-English AI Assistant
Users can type natural language instructions and the backend's keyword-driven assistant (`/api/ai/chat`) generates a multi-step workflow suggestion, mapping recognised apps onto a visual pipeline.

### ⏱️ 3. Flexible Scheduling Hub
Run granular automations on demand. Out-of-the-box support for event-driven webhooks, interval syncing (e.g., checking data streams every 15 minutes), and macro calendar triggers (e.g., daily digests or weekly analytics reports).

### 👥 4. Multi-Tenant Enterprise Workspaces
Built for team collaboration with granular, role-based permission tiers (**Admin**, **Editor**, **Viewer**). Teams can isolate integration keys, review detailed audit trails, and manage independent workspaces for engineering, marketing, or sales departments.

### 📊 5. Real-Time Analytics & Live Terminal
*   **Streaming Execution Logs:** Track background data mutations, webhooks, and live executions as they happen.
*   **Intelligent Diagnostics:** Immediate fault isolation and auto-retry capabilities for rate limits or expired authentication headers.
*   **ROI Analytics:** Interactive reporting dashboards tracking absolute time saved, task volume scales, and financial quarter savings.

---

## 🛠️ Tech Stack

*   **Frontend:** Vanilla JavaScript / HTML5 / Modern CSS3 (responsive, glassmorphism dark-mode UI), no build step required.
*   **Backend:** Python 3.11+, FastAPI, SQLAlchemy 2.0, Pydantic v2, JWT auth (`python-jose`), `passlib`/`bcrypt` password hashing.
*   **Database:** SQLite by default (zero setup), swappable to PostgreSQL/MySQL via the `DATABASE_URL` env var.
*   **API Docs:** Auto-generated OpenAPI/Swagger UI at `/docs` and ReDoc at `/redoc`.

---

## 📁 Project Structure

```
Flowmind-Automation-Platform/
├── frontend/
│   └── index.html          # Complete single-page app (HTML/CSS/JS, no build step)
├── backend/
│   ├── app/
│   │   ├── main.py         # FastAPI app entrypoint, CORS, router wiring
│   │   ├── core/           # Settings (.env loader) and security (JWT/hashing)
│   │   ├── db/             # SQLAlchemy engine/session setup
│   │   ├── models/         # SQLAlchemy ORM models (User, Workflow, Template, ...)
│   │   ├── schemas/        # Pydantic request/response schemas
│   │   ├── api/routes/     # REST endpoints (auth, workflows, templates, ai, ...)
│   │   ├── services/       # Business logic (auth, AI replies, analytics, simulation)
│   │   └── seed.py         # Idempotent demo-data seeding
│   ├── requirements.txt
│   ├── .env.example        # Copy to .env and fill in your own secret
│   └── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Backend setup

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env             # then edit .env and set a real SECRET_KEY
uvicorn app.main:app --reload --port 8000
```

The API is now live at `http://localhost:8000`, with interactive docs at
`http://localhost:8000/docs`. On first run it auto-creates the SQLite
database (`flowmind.db`) and seeds demo templates/integrations/triggers/notifications.

### 2. Frontend setup

The frontend is a single static HTML file — no build step needed. Serve it
with any static file server, for example:

```bash
cd frontend
python3 -m http.server 5500
```

Then open `http://localhost:5500/index.html` in your browser. The page
talks to the backend at `http://localhost:8000/api` by default. To point it
at a different backend URL, set `window.FLOWMIND_API_BASE` before the main
script runs (e.g. in a small inline `<script>` tag), or edit the
`API_BASE` constant near the bottom of `index.html`.

If the backend isn't running, the page still renders using its built-in
static demo content — only the live data (templates, integrations,
analytics, notifications, AI chat, auth) is skipped.

### 3. Environment variables (`backend/.env`)

| Variable | Description | Default |
|---|---|---|
| `APP_NAME` | Display name used in API responses | `FlowMind API` |
| `DEBUG` | Enable debug mode | `true` |
| `DATABASE_URL` | SQLAlchemy database URL | `sqlite:///./flowmind.db` |
| `SECRET_KEY` | Secret used to sign JWTs — **change this** | `dev-secret-key` |
| `ALGORITHM` | JWT signing algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token lifetime in minutes | `60` |
| `CORS_ORIGINS` | Comma-separated list of allowed origins | `http://localhost:5500,http://127.0.0.1:5500` |
| `OPENAI_API_KEY` | Optional — not currently used, reserved for swapping the rule-based AI assistant for a real LLM call | _(empty)_ |

---

## 🔌 API Overview

| Area | Endpoints |
|---|---|
| Auth | `POST /api/auth/signup`, `POST /api/auth/login`, `GET /api/auth/me` |
| Workflows | `GET/POST /api/workflows`, `GET/PUT/DELETE /api/workflows/{id}` |
| Templates & Integrations | `GET /api/templates`, `GET /api/integrations` |
| Executions & Triggers | `GET /api/executions/recent`, `GET /api/triggers`, `PATCH /api/triggers/{id}` |
| Analytics | `GET /api/analytics/monitoring`, `GET /api/analytics/overview` |
| AI Assistant | `POST /api/ai/chat` |
| Notifications | `GET /api/notifications`, `PATCH /api/notifications/mark-read` |

Full interactive documentation (request/response schemas, try-it-out) is
available at `/docs` while the backend is running.

---

## 🧪 Tested

All endpoints above have been exercised end-to-end (signup → login → authenticated
workflow CRUD, AI chat, trigger/notification mutations) and the frontend has
been verified in a real browser against a live backend with no console errors.
