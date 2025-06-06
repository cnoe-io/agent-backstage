"""Model for JsonObject"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Jsonobject(BaseModel):
    """A type representing all allowed JSON object values."""


class JsonobjectResponse(APIResponse):
    """Response model for Jsonobject"""
    data: Optional[Jsonobject] = None

class JsonobjectListResponse(APIResponse):
    """List response model for Jsonobject"""
    data: List[Jsonobject] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
