"""Model for EntityRelation"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Entityrelation(BaseModel):
    """A relation of a specific type to another entity in the catalog."""

    targetRef: str
    """The entity ref of the target of this relation."""
    type: str
    """The type of the relation."""

class EntityrelationResponse(APIResponse):
    """Response model for Entityrelation"""
    data: Optional[Entityrelation] = None

class EntityrelationListResponse(APIResponse):
    """List response model for Entityrelation"""
    data: List[Entityrelation] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
