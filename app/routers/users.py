from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.users import User
from app.schemas.misc import FilterPage, Message
from app.schemas.users import (
    UserList,
    UserPublic,
    UserSchemaCreate,
    UserSchemaUpdate,
)
from app.security import get_current_user, get_password_hash
from app.utils.messages import UserMessage

Session = Annotated[AsyncSession, Depends(get_db)]
CurrentUser = Annotated[User, Depends(get_current_user)]

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/', response_model=UserList)
async def get_users(
    filter_users: Annotated[FilterPage, Query()], session: Session
):
    query = await session.scalars(
        select(User)
        .where(User.is_deleted == False)  # noqa
        .offset(filter_users.offset)
        .limit(filter_users.limit)
    )

    users = query.all()

    return {'users': users}


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
async def create_user(user: UserSchemaCreate, session: Session):
    db_user = await session.scalar(
        select(User).where(User.email == user.email)
    )

    if db_user:
        if db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail=UserMessage.email_already_exists(),
            )

    hashed_password = get_password_hash(user.password)

    db_user = User(name=user.name, email=user.email, password=hashed_password)

    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)

    return db_user


@router.put('/{uuid}', response_model=UserPublic)
async def update_user(
    uuid: str,
    user: UserSchemaUpdate,
    session: Session,
    current_user: CurrentUser,
):
    if str(current_user.uuid) != uuid:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail=UserMessage.not_enough_permissions(),
        )

    try:
        current_user.name = user.name
        current_user.email = user.email

        if user.password:
            current_user.password = get_password_hash(user.password)

        await session.commit()
        await session.refresh(current_user)

        return current_user

    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail=UserMessage.email_already_exists(),
        )


@router.delete('/{uuid}', response_model=Message)
async def delete_user(uuid: str, session: Session, current_user: CurrentUser):
    if str(current_user.uuid) != uuid:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail=UserMessage.not_enough_permissions(),
        )

    if current_user.is_deleted:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=UserMessage.user_already_deleted(),
        )

    current_user.soft_delete()
    await session.commit()

    return {'message': UserMessage.user_deleted()}
