from typing import Any, List
from pydantic import BaseModel, ConfigDict


class Input(BaseModel):
    text: str


class Output(BaseModel):
    text: str
    label: str
    score: float

    model_config = ConfigDict(
        from_attributes=True
    )


class OutputList(BaseModel):
    classified_data_list: List[Output]

    model_config = ConfigDict(
        from_attributes=True
    )