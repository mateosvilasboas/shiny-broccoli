from typing import List

from pydantic import BaseModel, ConfigDict


class EntrySchema(BaseModel):
    text: str
    result: str


class ChartSchema(BaseModel):
    name: str
    code: str
    dice: str


class ChartPublic(ChartSchema):
    entries: List[EntrySchema]

    model_config = ConfigDict(from_attributes=True)


class ChartList(BaseModel):
    charts: List[ChartPublic]

    model_config = ConfigDict(from_attributes=True)


class ChartRoll(ChartSchema):
    entry: EntrySchema
