# Copyright CNOE Contributors (https://cnoe.io)
# SPDX-License-Identifier: Apache-2.0

from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from .agent import agent_backstage
from .state import AgentState

def build_graph() -> CompiledStateGraph:
    graph_builder = StateGraph(AgentState)
    graph_builder.add_node("agent_backstage", agent_backstage)

    graph_builder.add_edge(START, "agent_backstage")
    graph_builder.add_edge("agent_backstage", END)

    return graph_builder.compile()

graph = build_graph() 