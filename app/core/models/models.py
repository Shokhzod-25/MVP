from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.base import Base


class Templates(Base):
    title: Mapped[str] = mapped_column(String)
    path: Mapped[str] = mapped_column(String)
