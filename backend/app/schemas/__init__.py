from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PlayerBaseSchema(BaseModel):
    firstname: str
    lastname: Optional[str] = None
    country_code: Optional[str] = None


class MatchBaseSchema(BaseModel):
    date: datetime
    duration_minutes: Optional[int] = 0
    teamA_name: str
    teamB_name: str
    teamA_score: Optional[int] = 0
    teamB_score: Optional[int] = 0
    location_id: Optional[int] = None
    mvp_id: Optional[int] = None


class LocationBaseSchema(BaseModel):
    name: str
    postcode: Optional[str] = None
    address: Optional[str] = None