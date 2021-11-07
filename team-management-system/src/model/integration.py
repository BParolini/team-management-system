import uuid
from datetime import time
from typing import Optional

from pydantic import BaseModel

from src.model.team import Team


class Integration(BaseModel):
    id: uuid
    created_at: time
    updated_at: time
    deleted_at: time
    information: str
    platform: str
    team_id: Optional[uuid]
    team: Optional[Team]
