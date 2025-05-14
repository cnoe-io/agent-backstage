"""Tools for /entity-facets operations"""

import logging
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from ..api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_entity_facets(facet: List[str]) -> Dict[str, Any]:
    """
    
    
    Get all entity facets that match the given filters.
    
    Returns:
        API response data
    """
    logger.debug(f"Making GET request to /entity-facets")
    params = {}
    data = None
    # Add parameters to request
    if facet is not None:
        params["facet"] = facet
    success, response = await make_api_request(
        "/entity-facets",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
