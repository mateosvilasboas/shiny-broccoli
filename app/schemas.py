from typing import Any, List
from pydantic import BaseModel, ConfigDict


class Input(BaseModel):
    text: str


class Output(BaseModel):
    explanation: str

    model_config = ConfigDict(
        from_attributes=True
    )