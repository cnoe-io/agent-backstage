"""Tools for /entities operations"""

import logging
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from ..api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def GetEntities(order: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    
    
    Get all entities matching a given filter.
    
    Returns:
        API response data
    """
    logger.debug(f"Making GET request to /entities")
    params = {}
    data = None
    # Add parameters to request
    if order is not None:
    params["order"] = order
    success, response = await make_api_request(
        "/entities",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
