import uuid
from datetime import time
from typing import List

from pydantic import BaseModel

from src.model.team import Team


class User(BaseModel):
    id: uuid
    created_at: time
    updated_at: time
    deleted_at: time
    name: str
    email: str
    github_user_id: int
    github_username: str
    teams: List[Team]
