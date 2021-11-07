import uuid
from datetime import time
from typing import Optional

from pydantic import BaseModel

from src.model.team import Team


class CloudCostCenter(BaseModel):
    id: uuid
    created_at: time
    updated_at: time
    deleted_at: time
    label: str
    identifier: str
    team_id: Optional[uuid]
    team: Optional[Team]
