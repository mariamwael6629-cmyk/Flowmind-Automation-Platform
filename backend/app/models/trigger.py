from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Trigger(Base):
    __tablename__ = "triggers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    detail: Mapped[str] = mapped_column(String(255), default="")
    icon: Mapped[str] = mapped_column(String(10), default="🔗")
    icon_bg: Mapped[str] = mapped_column(String(40), default="rgba(88,130,255,.1)")
    icon_color: Mapped[str] = mapped_column(String(20), default="var(--el)")
    active: Mapped[bool] = mapped_column(Boolean, default=True)
