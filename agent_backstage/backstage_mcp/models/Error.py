"""Model for Error"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo

class Error(BaseModel):
    """Error model"""

    error: Dict
    request: Optional[Dict] = None
    response: Dict

class ErrorResponse(APIResponse):
    """Response model for Error"""
    data: Optional[Error] = None

class ErrorListResponse(APIResponse):
    """List response model for Error"""
    data: List[Error] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
