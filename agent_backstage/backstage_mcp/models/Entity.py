"""Model for Entity"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Entity(BaseModel):
    """The parts of the format that's common to all versions/kinds of entity."""

    relations: Optional[List[str]] = None
    """The relations that this entity has with other entities."""
    spec: Optional[str] = None
    metadata: str
    kind: str
    """The high level entity type being described."""
    apiVersion: str
    """The version of specification format for this particular entity that
this is written against."""

class EntityResponse(APIResponse):
    """Response model for Entity"""
    data: Optional[Entity] = None

class EntityListResponse(APIResponse):
    """List response model for Entity"""
    data: List[Entity] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
