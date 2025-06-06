"""Model for AnalyzeLocationGenerateEntity"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Analyzelocationgenerateentity(BaseModel):
    """This is some form of representation of what the analyzer could deduce.
We should probably have a chat about how this can best be conveyed to
the frontend. It'll probably contain a (possibly incomplete) entity, plus
enough info for the frontend to know what form data to show to the user
for overriding/completing the info."""

    fields: List[str]
    entity: str

class AnalyzelocationgenerateentityResponse(APIResponse):
    """Response model for Analyzelocationgenerateentity"""
    data: Optional[Analyzelocationgenerateentity] = None

class AnalyzelocationgenerateentityListResponse(APIResponse):
    """List response model for Analyzelocationgenerateentity"""
    data: List[Analyzelocationgenerateentity] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
