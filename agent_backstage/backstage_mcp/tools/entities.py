"""Entity management tools for Backstage MCP"""

import logging
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from ..api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("backstage_mcp")

async def get_entities(
    order: Optional[List[str]] = None,
    filter: Optional[Dict[str, Any]] = None,
    limit: int = 100,
) -> Dict[str, Any]:
    """
    Get entities from Backstage with filtering options

    Args:
        order: List of fields to order results by
        filter: Dictionary of filter criteria
        limit: Maximum number of entities to return (default: 100)

    Returns:
        List of entities with pagination information
    """
    logger.debug("Getting entities with filters:")
    logger.debug(f"Order: {order}")
    logger.debug(f"Filter: {filter}")
    logger.debug(f"Limit: {limit}")

    params = {}

    if order:
        params["order"] = order

    if filter:
        params["filter"] = filter

    params["limit"] = limit

    logger.debug(f"Making API request with params: {params}")
    success, data = await make_api_request("entities", params=params)

    if not success:
        logger.error(f"Failed to retrieve entities: {data.get('error')}")
        return {"error": data.get("error", "Failed to retrieve entities")}

    logger.info("Successfully retrieved entities")
    return data
