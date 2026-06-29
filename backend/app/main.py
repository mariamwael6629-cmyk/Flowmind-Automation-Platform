from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import ai, analytics, auth, executions, notifications, templates, workflows
from app.core.config import get_settings
from app.db.database import Base, SessionLocal, engine
from app.seed import seed_all

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="REST API powering the FlowMind workflow automation platform.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_all(db)
    finally:
        db.close()


@app.get("/", tags=["health"])
def root():
    return {"name": settings.app_name, "status": "ok", "docs": "/docs"}


@app.get("/api/health", tags=["health"])
def health():
    return {"status": "ok"}


app.include_router(auth.router, prefix="/api")
app.include_router(workflows.router, prefix="/api")
app.include_router(templates.router, prefix="/api")
app.include_router(executions.router, prefix="/api")
app.include_router(analytics.router, prefix="/api")
app.include_router(ai.router, prefix="/api")
app.include_router(notifications.router, prefix="/api")
