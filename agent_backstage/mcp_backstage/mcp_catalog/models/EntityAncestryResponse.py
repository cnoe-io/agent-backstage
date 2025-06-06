"""Model for EntityAncestryResponse"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Entityancestryresponse(BaseModel):
    """Entityancestryresponse model"""

    items: List[Dict]
    rootEntityRef: str

class EntityancestryresponseResponse(APIResponse):
    """Response model for Entityancestryresponse"""
    data: Optional[Entityancestryresponse] = None

class EntityancestryresponseListResponse(APIResponse):
    """List response model for Entityancestryresponse"""
    data: List[Entityancestryresponse] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
