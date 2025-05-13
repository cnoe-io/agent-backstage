"""Tools for /entities/by-query operations"""

import logging
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from ..api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def GetEntitiesByQuery(fullTextFilterTerm: Optional[str] = None, fullTextFilterFields: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    
    
    Search for entities by a given query.
    
    Returns:
        API response data
    """
    logger.debug(f"Making GET request to /entities/by-query")
    params = {}
    data = None
    # Add parameters to request
    if fullTextFilterTerm is not None:
    params["fullTextFilterTerm"] = fullTextFilterTerm
if fullTextFilterFields is not None:
    params["fullTextFilterFields"] = fullTextFilterFields
    success, response = await make_api_request(
        "/entities/by-query",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
