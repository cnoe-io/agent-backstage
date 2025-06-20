# Copyright 2025 CNOE
# SPDX-License-Identifier: Apache-2.0
# Generated by CNOE OpenAPI MCP Codegen tool

"""Model for Entityfacet"""

from typing import List, Optional
from pydantic import BaseModel, Field
from .base import APIResponse, PaginationInfo


class Entityfacet(BaseModel):
    """Entityfacet model"""


class EntityfacetResponse(APIResponse):
    """Response model for Entityfacet"""

    data: Optional[Entityfacet] = None


class EntityfacetListResponse(APIResponse):
    """List response model for Entityfacet"""

    data: List[Entityfacet] = Field(default_factory=list)
    pagination: Optional[PaginationInfo] = None
