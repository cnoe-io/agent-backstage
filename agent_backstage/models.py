# Copyright 2025 CNOE
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class BackstageEntity(BaseModel):
    """A Backstage entity."""
    kind: str
    metadata: Dict[str, Any]
    spec: Dict[str, Any]
    relations: Optional[List[Dict[str, Any]]] = None

class BackstageLocation(BaseModel):
    """A Backstage location."""
    type: str
    target: str
    presence: Optional[str] = None

class BackstageFacet(BaseModel):
    """A Backstage facet."""
    name: str
    value: Any

class BackstageQuery(BaseModel):
    """A Backstage query."""
    filter: Dict[str, Any]
    fields: Optional[List[str]] = None
    limit: Optional[int] = None
    offset: Optional[int] = None

class BackstageResponse(BaseModel):
    """A Backstage API response."""
    items: List[BackstageEntity]
    total_count: int
    page_info: Optional[Dict[str, Any]] = None

class UserInputRequest(BaseModel):
    """An input that the user should provide for the agent to be able to take action."""
    field_name: str = Field(description="The name of the field that should be provided.")
    field_description: str = Field(
        description="A description of what this field represents and how it will be used.",
    )
    field_values: List[str] = Field(
        description="A list of possible values that the user can provide for this field.",
    )

class AgentResponseMetadata(BaseModel):
    """Metadata about the response from Agent."""
    user_input: bool = Field(description="Indicates if the response requires user input")
    input_fields: List[UserInputRequest]

class AgentResponse(BaseModel):
    """Response from Backstage Agent."""
    answer: str = Field(description="The response from the Agent")
    metadata: AgentResponseMetadata = Field(
        description="""Metadata about the response. Set user_input if the response has user input and \
corresponding and input fields""",
    )

class ChatBotQuestion(BaseModel):
    """Model for chat bot questions."""
    question: str
    chat_id: str 