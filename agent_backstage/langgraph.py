# Copyright 2025 CNOE
# SPDX-License-Identifier: Apache-2.0

from typing import Annotated, TypedDict
from langgraph.graph import Graph, StateGraph
from .agent import agent_backstage
from .state import AgentState

class BackstageState(TypedDict):
    """The state of the Backstage workflow."""
    backstage: AgentState

def create_backstage_graph() -> Graph:
    """Create the Backstage workflow graph."""
    workflow = StateGraph(BackstageState)

    # Add the Backstage agent node
    workflow.add_node("backstage", agent_backstage)

    # Set the entry point
    workflow.set_entry_point("backstage")

    # Set the exit point
    workflow.set_finish_point("backstage")

    return workflow.compile() 