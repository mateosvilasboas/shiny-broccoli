from http import HTTPStatus
from typing import Annotated

import dice
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.charts import Chart
from app.schemas.charts import ChartList, ChartPublic, ChartRoll
from app.utils.messages import ChartMessage

Session = Annotated[AsyncSession, Depends(get_db)]

router = APIRouter(
    prefix='/charts',
    tags=['charts'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/', status_code=HTTPStatus.OK, response_model=ChartList)
async def get_charts(session: Session):
    query = await session.scalars(
        select(Chart)
        .options(selectinload(Chart.entries))
        .filter(
            Chart.is_deleted == False,  # noqa
        )
    )

    charts = query.all()

    return {'charts': charts}


@router.get('/{code}', status_code=HTTPStatus.OK, response_model=ChartPublic)
async def get_chart(code: str, session: Session):
    query = await session.scalars(
        select(Chart)
        .options(selectinload(Chart.entries))
        .filter(
            Chart.code == code.capitalize(),
            Chart.is_deleted == False,  # noqa
        )
    )

    chart = query.first()

    if not chart:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail=ChartMessage.chart_not_found(code)
        )

    return chart


@router.get(
    '/roll/{code}', status_code=HTTPStatus.OK, response_model=ChartRoll
)
async def roll_chart(code: str, session: Session):
    query = await session.scalars(
        select(Chart)
        .options(selectinload(Chart.entries))
        .filter(
            Chart.code == code.capitalize(),
            Chart.is_deleted == False,  # noqa
        )
    )

    chart = query.first()

    if not chart:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, 
            detail=ChartMessage.chart_not_found(code.capitalize())
        )
    if not chart.entries:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=ChartMessage.entries_not_found(code.capitalize())
        )

    dice_roll = dice.roll(chart.dice)
    dice_roll = sum(dice_roll)

    for entry in chart.entries:
        if entry.result == str(dice_roll):
            rolled_entry = entry
            break

    return {
        'name': chart.name,
        'code': chart.code,
        'dice': chart.dice,
        'entry': rolled_entry,
    }
