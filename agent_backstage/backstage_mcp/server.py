#!/usr/bin/env python3
"""
Backstage MCP Server

This server provides a Model Context Protocol (MCP) interface to the Backstage API,
allowing large language models and AI assistants to manage Backstage resources.
"""
import logging
import os
import sys
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Import tools
from agent_backstage.backstage_mcp.tools import refresh
from agent_backstage.backstage_mcp.tools import entities
from agent_backstage.backstage_mcp.tools import entities_by_refs
from agent_backstage.backstage_mcp.tools import entities_by_query
from agent_backstage.backstage_mcp.tools import entity_facets
from agent_backstage.backstage_mcp.tools import locations
from agent_backstage.backstage_mcp.tools import analyze_location
from agent_backstage.backstage_mcp.tools import validate_entity
# Import user-specific tools
from agent_backstage.backstage_mcp.tools import user_catalog
from agent_backstage.backstage_mcp.tools import user_groups
from agent_backstage.backstage_mcp.tools import user_projects
# Import component and project tools
from agent_backstage.backstage_mcp.tools import component
from agent_backstage.backstage_mcp.tools import project

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create server instance
mcp = FastMCP("Backstage MCP Server")

# Register refresh tools
mcp.tool()(refresh.refresh_entity)

# Register entities tools
mcp.tool()(entities.get_entities)

# Register entities_by_refs tools
mcp.tool()(entities_by_refs.get_entities_by_refs)

# Register entities_by_query tools
mcp.tool()(entities_by_query.get_entities_by_query)

# Register entity_facets tools
mcp.tool()(entity_facets.get_entity_facets)

# Register locations tools
mcp.tool()(locations.create_location)
mcp.tool()(locations.get_locations)

# Register analyze_location tools
mcp.tool()(analyze_location.analyze_location)

# Register validate_entity tools
mcp.tool()(validate_entity.validate_entity)

# Register user-specific tools
mcp.tool()(user_catalog.get_user_catalog_entities)
mcp.tool()(user_groups.get_user_groups)
mcp.tool()(user_projects.get_user_projects)

# Register component tools
mcp.tool()(component.get_component_details)

# Register project tools
mcp.tool()(project.get_project_details)
mcp.tool()(project.get_projects_by_user)

# Start server when run directly
if __name__ == "__main__":
    mcp.run()
