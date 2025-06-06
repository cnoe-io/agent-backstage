"""Model for LocationInput"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Locationinput(BaseModel):
    """Locationinput model"""

    type: str
    target: str

class LocationinputResponse(APIResponse):
    """Response model for Locationinput"""
    data: Optional[Locationinput] = None

class LocationinputListResponse(APIResponse):
    """List response model for Locationinput"""
    data: List[Locationinput] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
