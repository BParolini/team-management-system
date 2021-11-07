import uuid
from datetime import time
from typing import List

from pydantic import BaseModel

from src.model.team import Team


class League(BaseModel):
    id: uuid
    created_at: time
    updated_at: time
    deleted_at: time
    name: str
    nickname: str
    description: str
    tribes: List[Team]
