from pydantic import BaseModel
from app.schemas import LocationBaseSchema
from typing import Optional


class LocationSchema(LocationBaseSchema):
    id: int
    is_active: bool


class LocationSlimSchema(LocationBaseSchema):
    id: int
    is_active: bool


class LocationCreateSchema(LocationBaseSchema):
    pass


class LocationUpdateSchema(BaseModel):
    name: Optional[str] = None
    postcode: Optional[str] = None
    address: Optional[str] = None
    is_active: Optional[bool] = None
