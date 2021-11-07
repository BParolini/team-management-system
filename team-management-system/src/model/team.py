import uuid
from datetime import time
from typing import Optional, List

from pydantic import BaseModel

from src.model.business_unit import BusinessUnit
from src.model.cloud_cost_center import CloudCostCenter
from src.model.integration import Integration
from src.model.tribe import Tribe
from src.model.user import User


class Team(BaseModel):
    id: uuid
    created_at: time
    updated_at: time
    deleted_at: time
    description: str
    elastic_searchID: str
    email: str
    key_name: str
    name: str
    nickname: str
    business_unit_id: Optional[uuid]
    tribe_id: Optional[uuid]
    business_unit: Optional[BusinessUnit]
    tribe: Optional[Tribe]
    cloud_cost_centers: List[CloudCostCenter]
    integrations: List[Integration]
    users: List[User]
