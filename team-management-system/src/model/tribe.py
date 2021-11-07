import uuid
from datetime import time
from typing import Optional, List

from pydantic import BaseModel

from src.model.league import League
from src.model.team import Team


class Tribe(BaseModel):
    id: uuid
    created_at: time
    updated_at: time
    deleted_at: time
    name: str
    description: str
    league_id: Optional[uuid]
    league: Optional[League]
    teams: List[Team]
