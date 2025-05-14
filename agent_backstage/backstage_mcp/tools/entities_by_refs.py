"""Tools for /entities/by-refs operations"""

import logging
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from ..api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_entities_by_refs() -> Dict[str, Any]:
    """
    
    
    Get a batch set of entities given an array of entityRefs.
    
    Returns:
        API response data
    """
    logger.debug(f"Making POST request to /entities/by-refs")
    params = {}
    data = None
    # Add parameters to request
    
    success, response = await make_api_request(
        "/entities/by-refs",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
