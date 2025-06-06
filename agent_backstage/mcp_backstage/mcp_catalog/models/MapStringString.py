"""Model for MapStringString"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Mapstringstring(BaseModel):
    """Construct a type with a set of properties K of type T"""


class MapstringstringResponse(APIResponse):
    """Response model for Mapstringstring"""
    data: Optional[Mapstringstring] = None

class MapstringstringListResponse(APIResponse):
    """List response model for Mapstringstring"""
    data: List[Mapstringstring] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
