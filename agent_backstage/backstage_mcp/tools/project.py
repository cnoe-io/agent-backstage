"""Project management tools for Backstage MCP"""

import logging
from typing import Dict, Any, List
from ..api.client import make_api_request
from .user_groups import get_user_groups

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("backstage_mcp")

async def get_project_details(project_name: str, user_id: str) -> Dict[str, Any]:
    """
    Get details of a specific project owned by the groups that the specified user is a member of.

    Args:
        project_name: The name of the project to find
        user_id: The ID of the user whose groups' projects are being searched

    Returns:
        Dictionary containing the details of the specified project if found

    Raises:
        ValueError: If the project is not found for the user
    """
    logger.debug(f"Getting project details for project: {project_name}, user: {user_id}")

    # Get user's groups
    groups = await get_user_groups(user_id)
    
    if not groups:
        logger.info("No groups found for user")
        raise ValueError(f"No groups found for user {user_id}")

    # Get projects owned by these groups
    params = {
        "filter": f"kind=system,relations.ownedBy=group:default/{','.join(groups)}"
    }
    
    logger.debug(f"Making API request with params: {params}")
    success, data = await make_api_request("entities", params=params)

    if not success:
        logger.error(f"Failed to retrieve projects: {data.get('error')}")
        raise ValueError(f"Failed to retrieve projects: {data.get('error')}")

    # Find the specific project
    for project in data.get("items", []):
        if project["metadata"]["name"].lower() == project_name.lower():
            logger.info(f"Found project: {project_name}")
            return project

    logger.error(f"Project '{project_name}' not found for user '{user_id}'")
    raise ValueError(f"Project '{project_name}' not found for user '{user_id}'")

async def get_projects_by_user(user_id: str) -> Dict[str, Any]:
    """
    Get all projects owned by the groups that the specified user is a member of.

    Args:
        user_id: The ID of the user to fetch projects for

    Returns:
        Dictionary containing all projects owned by the user's groups
    """
    logger.debug(f"Getting projects for user: {user_id}")

    # Get user's groups
    groups = await get_user_groups(user_id)
    
    if not groups:
        logger.info("No groups found for user")
        return {"items": []}

    # Get projects owned by these groups
    params = {
        "filter": f"kind=system,relations.ownedBy=group:default/{','.join(groups)}"
    }
    
    logger.debug(f"Making API request with params: {params}")
    success, data = await make_api_request("entities", params=params)

    if not success:
        logger.error(f"Failed to retrieve projects: {data.get('error')}")
        return {"error": data.get("error", "Failed to retrieve projects")}

    logger.info(f"Successfully retrieved projects for user's groups")
    return data 