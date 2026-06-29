from pydantic import BaseModel


class ExecutionOut(BaseModel):
    id: int
    message: str
    status: str
    time_ago: str


class TriggerOut(BaseModel):
    id: int
    name: str
    detail: str
    icon: str
    icon_bg: str
    icon_color: str
    active: bool


class TriggerUpdate(BaseModel):
    active: bool


class NotificationOut(BaseModel):
    id: int
    message: str
    icon: str
    icon_bg: str
    icon_color: str
    read: bool
    time_ago: str
