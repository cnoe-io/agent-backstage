# Copyright 2025 CNOE
# SPDX-License-Identifier: Apache-2.0

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class MsgType(str, Enum):
    """Message types for the agent."""
    human = "human"
    assistant = "assistant"
    system = "system"

class Message(BaseModel):
    """A message in the conversation."""
    type: MsgType
    content: str

class OutputState(BaseModel):
    """The output state of the agent."""
    messages: List[Message] = Field(default_factory=list)

class BackstageInput(BaseModel):
    """The input state for the Backstage agent."""
    messages: List[Message] = Field(default_factory=list)

class AgentState(BaseModel):
    """The state of the agent."""
    backstage_input: BackstageInput = Field(default_factory=BackstageInput)
    backstage_output: Optional[OutputState] = None 