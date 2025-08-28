from pydantic import BaseModel


class FilterPage(BaseModel):
    offset: int = 0
    limit: int = 100


class Token(BaseModel):
    access_token: str
    token_type: str


class Message(BaseModel):
    message: str
