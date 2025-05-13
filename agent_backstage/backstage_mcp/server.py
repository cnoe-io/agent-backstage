#!/usr/bin/env python3
"""
backstage MCP Server

This server provides a Model Context Protocol (MCP) interface to the backstage,
allowing large language models and AI assistants to interact with the service.
"""
import logging
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Import tools
from agent_backstage.backstage.tools import refresh
from agent_backstage.backstage.tools import entities
from agent_backstage.backstage.tools import entities_by-refs
from agent_backstage.backstage.tools import entities_by-query
from agent_backstage.backstage.tools import entity-facets
from agent_backstage.backstage.tools import locations
from agent_backstage.backstage.tools import analyze-location
from agent_backstage.backstage.tools import validate-entity

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create server instance
mcp = FastMCP("backstage MCP Server")

# Register tools
# Register refresh tools
mcp.tool()(refresh.RefreshEntity)

# Register entities tools
mcp.tool()(entities.GetEntities)

# Register entities_by-refs tools
mcp.tool()(entities_by-refs.GetEntitiesByRefs)

# Register entities_by-query tools
mcp.tool()(entities_by-query.GetEntitiesByQuery)

# Register entity-facets tools
mcp.tool()(entity-facets.GetEntityFacets)

# Register locations tools
mcp.tool()(locations.CreateLocation)
mcp.tool()(locations.GetLocations)

# Register analyze-location tools
mcp.tool()(analyze-location.AnalyzeLocation)

# Register validate-entity tools
mcp.tool()(validate-entity.ValidateEntity)


# Start server when run directly
if __name__ == "__main__":
    mcp.run()
