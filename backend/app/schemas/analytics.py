from pydantic import BaseModel


class MonitoringSparklines(BaseModel):
    executions: list[int]
    success: list[int]
    response: list[int]
    workflows: list[int]


class MonitoringOut(BaseModel):
    executions_today: int
    success_rate: float
    avg_response: float
    active_workflows: int
    sparklines: MonitoringSparklines


class AnalyticsOverviewOut(BaseModel):
    time_saved: str
    tasks_automated: int
    cost_saved: str
    error_rate: float
    weekly_executions: list[int]


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str
