from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MissionBase(BaseModel):
    title: str
    assigned_to: str
    status: str
    priority: int
    deadline: datetime

    def to_dict(self) -> dict:
        return self.model_dump()

class MissionCreate(MissionBase):
    id: int

class MissionUpdate(BaseModel):
    title: Optional[str] = None
    assigned_to: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[int] = None
    deadline: Optional[datetime] = None

    def to_dict(self) -> dict:
        return self.model_dump(exclude_unset=True)

class MissionResponse(MissionBase):
    id: int
    created_at: datetime
