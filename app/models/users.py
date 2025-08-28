from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.models.base import Base


class User(Base):
    """
    User model
    """

    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
    password: Mapped[str]
