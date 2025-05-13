"""Model for EntityFacetsResponse"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Entityfacetsresponse(BaseModel):
    """Entityfacetsresponse model"""

    facets: Dict

class EntityfacetsresponseResponse(APIResponse):
    """Response model for Entityfacetsresponse"""
    data: Optional[Entityfacetsresponse] = None

class EntityfacetsresponseListResponse(APIResponse):
    """List response model for Entityfacetsresponse"""
    data: List[Entityfacetsresponse] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
