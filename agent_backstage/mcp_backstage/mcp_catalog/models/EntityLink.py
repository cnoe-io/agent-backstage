"""Model for EntityLink"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Entitylink(BaseModel):
    """A link to external information that is related to the entity."""

    type: Optional[str] = None
    """An optional value to categorize links into specific groups"""
    icon: Optional[str] = None
    """An optional semantic key that represents a visual icon."""
    title: Optional[str] = None
    """An optional descriptive title for the link."""
    url: str
    """The url to the external site, document, etc."""

class EntitylinkResponse(APIResponse):
    """Response model for Entitylink"""
    data: Optional[Entitylink] = None

class EntitylinkListResponse(APIResponse):
    """List response model for Entitylink"""
    data: List[Entitylink] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
