"""User projects management tools for Backstage MCP"""

import logging
from typing import Dict, Any, List
from ..api.client import make_api_request
from .user_groups import get_user_groups

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("backstage_mcp")

async def get_user_projects(user_id: str) -> Dict[str, Any]:
    """
    Get projects owned by groups that a user is a member of

    Args:
        user_id: The ID of the user to fetch projects for

    Returns:
        Dictionary containing projects owned by the user's groups
    """
    logger.debug(f"Getting projects for user: {user_id}")

    # First get user's groups
    groups = await get_user_groups(user_id)
    
    if not groups:
        logger.info("No groups found for user")
        return {"items": []}

    # Then get projects owned by these groups
    params = {
        "filter": f"kind=Project,spec.owner in ({','.join(groups)})"
    }
    
    logger.debug(f"Making API request with params: {params}")
    success, data = await make_api_request("entities", params=params)

    if not success:
        logger.error(f"Failed to retrieve user projects: {data.get('error')}")
        return {"error": data.get("error", "Failed to retrieve user projects")}

    logger.info(f"Successfully retrieved projects for user's groups")
    return data 