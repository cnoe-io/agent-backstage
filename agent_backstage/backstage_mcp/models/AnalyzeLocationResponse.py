"""Model for AnalyzeLocationResponse"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Analyzelocationresponse(BaseModel):
    """Analyzelocationresponse model"""

    generateEntities: List[str]
    existingEntityFiles: List[str]

class AnalyzelocationresponseResponse(APIResponse):
    """Response model for Analyzelocationresponse"""
    data: Optional[Analyzelocationresponse] = None

class AnalyzelocationresponseListResponse(APIResponse):
    """List response model for Analyzelocationresponse"""
    data: List[Analyzelocationresponse] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
