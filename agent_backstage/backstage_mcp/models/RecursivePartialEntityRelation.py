"""Model for RecursivePartialEntityRelation"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Recursivepartialentityrelation(BaseModel):
    """A relation of a specific type to another entity in the catalog."""

    targetRef: Optional[str] = None
    """The entity ref of the target of this relation."""
    type: Optional[str] = None
    """The type of the relation."""

class RecursivepartialentityrelationResponse(APIResponse):
    """Response model for Recursivepartialentityrelation"""
    data: Optional[Recursivepartialentityrelation] = None

class RecursivepartialentityrelationListResponse(APIResponse):
    """List response model for Recursivepartialentityrelation"""
    data: List[Recursivepartialentityrelation] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
