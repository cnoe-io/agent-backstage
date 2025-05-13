"""Model for Location"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Location(BaseModel):
    """Entity location for a specific entity."""

    target: str
    type: str
    id: str

class LocationResponse(APIResponse):
    """Response model for Location"""
    data: Optional[Location] = None

class LocationListResponse(APIResponse):
    """List response model for Location"""
    data: List[Location] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
