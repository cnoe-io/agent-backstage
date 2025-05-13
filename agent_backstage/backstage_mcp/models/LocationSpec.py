"""Model for LocationSpec"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Locationspec(BaseModel):
    """Holds the entity location information."""

    target: str
    type: str

class LocationspecResponse(APIResponse):
    """Response model for Locationspec"""
    data: Optional[Locationspec] = None

class LocationspecListResponse(APIResponse):
    """List response model for Locationspec"""
    data: List[Locationspec] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
