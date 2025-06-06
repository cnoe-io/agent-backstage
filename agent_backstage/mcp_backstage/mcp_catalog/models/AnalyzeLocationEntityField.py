"""Model for AnalyzeLocationEntityField"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Analyzelocationentityfield(BaseModel):
    """Analyzelocationentityfield model"""

    description: str
    """A text to show to the user to inform about the choices made. Like, it could say
"Found a CODEOWNERS file that covers this target, so we suggest leaving this
field empty; which would currently make it owned by X" where X is taken from the
codeowners file."""
    value: str
    state: str
    """The outcome of the analysis for this particular field"""
    field: str
    """e.g. "spec.owner"? The frontend needs to know how to "inject" the field into the
entity again if the user wants to change it"""

class AnalyzelocationentityfieldResponse(APIResponse):
    """Response model for Analyzelocationentityfield"""
    data: Optional[Analyzelocationentityfield] = None

class AnalyzelocationentityfieldListResponse(APIResponse):
    """List response model for Analyzelocationentityfield"""
    data: List[Analyzelocationentityfield] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
