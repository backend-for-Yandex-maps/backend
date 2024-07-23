# app/schema/schema.py

from pydantic import BaseModel, ValidationError
from typing import Optional


class ReviewSchema(BaseModel):
    name: str
    icon_href: str
    date: str
    stars: int
    review_text: str
    response: Optional[str]
    points_id: int


class input_data_ya(BaseModel):
    id_ya: int


class input_data_type_request(BaseModel):
    type_parse: str
