"""User groups management tools for Backstage MCP"""

import logging
from typing import Dict, Any, List
from ..api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("backstage_mcp")

async def get_user_groups(user_id: str) -> List[str]:
    """
    Get groups that a user is a member of

    Args:
        user_id: The ID of the user to fetch groups for

    Returns:
        List of group names that the user is a member of
    """
    logger.debug(f"Getting groups for user: {user_id}")

    params = {
        "filter": f"kind=Group,spec.members={user_id}"
    }
    
    logger.debug(f"Making API request with params: {params}")
    success, data = await make_api_request("entities", params=params)

    if not success:
        logger.error(f"Failed to retrieve user groups: {data.get('error')}")
        return []

    groups = [entity["metadata"]["name"] for entity in data.get("items", [])]
    logger.info(f"Successfully retrieved {len(groups)} groups for user")
    return groups 