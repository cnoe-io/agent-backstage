"""Model for EntityFacet"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Entityfacet(BaseModel):
    """Entityfacet model"""

    value: str
    count: float

class EntityfacetResponse(APIResponse):
    """Response model for Entityfacet"""
    data: Optional[Entityfacet] = None

class EntityfacetListResponse(APIResponse):
    """List response model for Entityfacet"""
    data: List[Entityfacet] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
