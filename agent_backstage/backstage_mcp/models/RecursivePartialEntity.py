"""Model for RecursivePartialEntity"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Recursivepartialentity(BaseModel):
    """Makes all keys of an entire hierarchy optional."""

    apiVersion: Optional[str] = None
    """The version of specification format for this particular entity that
this is written against."""
    kind: Optional[str] = None
    """The high level entity type being described."""
    metadata: Optional[str] = None
    spec: Optional[str] = None
    relations: Optional[List[str]] = None
    """The relations that this entity has with other entities."""

class RecursivepartialentityResponse(APIResponse):
    """Response model for Recursivepartialentity"""
    data: Optional[Recursivepartialentity] = None

class RecursivepartialentityListResponse(APIResponse):
    """List response model for Recursivepartialentity"""
    data: List[Recursivepartialentity] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
