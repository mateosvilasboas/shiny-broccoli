import uuid as uuid_pkg
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
)

from app.utils.mixins import BaseMixins


class Base(DeclarativeBase, MappedAsDataclass, BaseMixins):
    """
    Base class for all models
    """

    uuid: Mapped[uuid_pkg.UUID] = mapped_column(
        init=False,
        nullable=False,
        index=True,
        primary_key=True,
        unique=True,
        default_factory=uuid_pkg.uuid4,
    )
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
