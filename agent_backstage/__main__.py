# Copyright 2025 CNOE
# SPDX-License-Identifier: Apache-2.0

import asyncio
import logging
import os
from typing import Dict, Any

from .langgraph import create_backstage_graph
from .state import AgentState, Message, MsgType

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def run_backstage_agent():
    """Main entry point for the Backstage agent."""
    # Create the workflow graph
    graph = create_backstage_graph()

    # Initialize the state
    state = {
        "backstage": AgentState(
            backstage_input={
                "messages": [
                    Message(
                        type=MsgType.human,
                        content="Hello, I need help with Backstage."
                    )
                ]
            }
        )
    }

    # Run the workflow
    result = await graph.ainvoke(state)
    logger.info("Workflow completed")
    logger.debug(f"Result: {result}")

def main():
    """Entry point for the CLI."""
    asyncio.run(run_backstage_agent())

if __name__ == "__main__":
    main() 