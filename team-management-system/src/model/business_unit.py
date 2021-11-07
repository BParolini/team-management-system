import uuid
from datetime import time
from typing import List

from pydantic import BaseModel

from src.model.team import Team


class BusinessUnit(BaseModel):
    id: uuid
    created_at: time
    updated_at: time
    deleted_at: time
    name: str
    description: str
    teams: List[Team]
