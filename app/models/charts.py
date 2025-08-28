import uuid as uuid_pkg
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.models.base import Base


class Entry(Base):
    """
    Entry model. Entry is a row of a chart.
    """

    __tablename__ = 'entries'

    text: Mapped[str]
    result: Mapped[str]
    chart_uuid: Mapped[uuid_pkg.UUID] = mapped_column(
        ForeignKey('charts.uuid')
    )


class Chart(Base):
    """
    Chart model. Chart is a group of entries.
    """

    __tablename__ = 'charts'

    name: Mapped[str]
    code: Mapped[str] = mapped_column(unique=True)
    dice: Mapped[str]
    entries: Mapped[List['Entry']] = relationship(
        init=False, cascade='all, delete-orphan'
    )
