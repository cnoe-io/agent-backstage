"""Model for RecursivePartialEntityMeta"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Recursivepartialentitymeta(BaseModel):
    """Recursivepartialentitymeta model"""


class RecursivepartialentitymetaResponse(APIResponse):
    """Response model for Recursivepartialentitymeta"""
    data: Optional[Recursivepartialentitymeta] = None

class RecursivepartialentitymetaListResponse(APIResponse):
    """List response model for Recursivepartialentitymeta"""
    data: List[Recursivepartialentitymeta] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
