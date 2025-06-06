"""Model for EntitiesBatchResponse"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Entitiesbatchresponse(BaseModel):
    """Entitiesbatchresponse model"""

    items: List[str]
    """The list of entities, in the same order as the refs in the request. Entries
that are null signify that no entity existed with that ref."""

class EntitiesbatchresponseResponse(APIResponse):
    """Response model for Entitiesbatchresponse"""
    data: Optional[Entitiesbatchresponse] = None

class EntitiesbatchresponseListResponse(APIResponse):
    """List response model for Entitiesbatchresponse"""
    data: List[Entitiesbatchresponse] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
