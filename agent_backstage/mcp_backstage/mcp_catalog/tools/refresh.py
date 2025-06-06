"""Tools for /refresh operations"""

import logging
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from mcp_catalog.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def RefreshEntity() -> Dict[str, Any]:
    """
    
    Refresh the entity related to entityRef.
    Returns:
        API response data
    """
    logger.debug(f"Making POST request to /refresh")
    params = {}
    data = None
    # Add parameters to request
    
    success, response = await make_api_request(
        "/refresh",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
