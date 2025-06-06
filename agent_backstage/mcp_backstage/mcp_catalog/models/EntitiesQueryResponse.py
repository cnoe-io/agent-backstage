"""Model for EntitiesQueryResponse"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Entitiesqueryresponse(BaseModel):
    """Entitiesqueryresponse model"""

    items: List[str]
    """The list of entities paginated by a specific filter."""
    totalItems: float
    pageInfo: Dict

class EntitiesqueryresponseResponse(APIResponse):
    """Response model for Entitiesqueryresponse"""
    data: Optional[Entitiesqueryresponse] = None

class EntitiesqueryresponseListResponse(APIResponse):
    """List response model for Entitiesqueryresponse"""
    data: List[Entitiesqueryresponse] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
