from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class UserSchema(BaseModel):
    name: str
    email: EmailStr


class UserSchemaCreate(UserSchema):
    password: str


class UserSchemaUpdate(UserSchema):
    password: str | None = None


class UserPublic(BaseModel):
    uuid: UUID
    name: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]
