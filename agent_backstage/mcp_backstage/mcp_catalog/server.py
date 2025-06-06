#!/usr/bin/env python3
"""
catalog MCP Server

This server provides a Model Context Protocol (MCP) interface to the catalog,
allowing large language models and AI assistants to interact with the service.
"""
import logging
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Import tools
from mcp_catalog.tools import refresh
from mcp_catalog.tools import entities
from mcp_catalog.tools import entities_by_refs
from mcp_catalog.tools import entities_by_query
from mcp_catalog.tools import entity_facets
from mcp_catalog.tools import locations
from mcp_catalog.tools import analyze_location
from mcp_catalog.tools import validate_entity

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create server instance
mcp = FastMCP("catalog MCP Server")

# Register tools
# Register refresh tools
mcp.tool()(refresh.RefreshEntity)

# Register entities tools
mcp.tool()(entities.GetEntities)

# Register entities_by_refs tools
mcp.tool()(entities_by_refs.GetEntitiesByRefs)

# Register entities_by_query tools
mcp.tool()(entities_by_query.GetEntitiesByQuery)

# Register entity_facets tools
mcp.tool()(entity_facets.GetEntityFacets)

# Register locations tools
mcp.tool()(locations.GetLocations)
mcp.tool()(locations.CreateLocation)

# Register analyze_location tools
mcp.tool()(analyze_location.AnalyzeLocation)

# Register validate_entity tools
mcp.tool()(validate_entity.ValidateEntity)


# Start server when run directly
def main():
    mcp.run()

if __name__ == "__main__":
    main()
