"""User catalog management tools for Backstage MCP"""

import logging
from typing import Dict, Any
from ..api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("backstage_mcp")

async def get_user_catalog_entities(user_id: str) -> Dict[str, Any]:
    """
    Get catalog entities for a specific user

    Args:
        user_id: The ID of the user to fetch entities for

    Returns:
        Dictionary containing the catalog entities for the user
    """
    logger.debug(f"Getting catalog entities for user: {user_id}")

    params = {"user_id": user_id}
    
    logger.debug(f"Making API request with params: {params}")
    success, data = await make_api_request("catalog/entities", params=params)

    if not success:
        logger.error(f"Failed to retrieve user catalog entities: {data.get('error')}")
        return {"error": data.get("error", "Failed to retrieve user catalog entities")}

    logger.info("Successfully retrieved user catalog entities")
    return data 