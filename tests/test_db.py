from dataclasses import asdict

import pytest
from sqlalchemy import select

from app.models.users import User
from app.security import get_password_hash


@pytest.mark.asyncio
async def test_db_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        password_hash = get_password_hash('senha')
        new_user = User(
            name='alice', email='teste@test', password=password_hash
        )
        session.add(new_user)
        await session.commit()

    user = await session.scalar(select(User).where(User.name == 'alice'))

    assert asdict(user) == {
        'created_at': time,
        'deleted_at': None,
        'is_deleted': False,
        'email': 'teste@test',
        'uuid': user.uuid,
        'name': 'alice',
        'password': password_hash,
    }
