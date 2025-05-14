"""Tools for /entities/by-query operations"""

import logging
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from ..api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_entities_by_query(full_text_filter_term: Optional[str] = None, full_text_filter_fields: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    
    
    Search for entities by a given query.
    
    Returns:
        API response data
    """
    logger.debug(f"Making GET request to /entities/by-query")
    params = {}
    data = None
    # Add parameters to request
    if full_text_filter_term is not None:
        params["fullTextFilterTerm"] = full_text_filter_term
    if full_text_filter_fields is not None:
        params["fullTextFilterFields"] = full_text_filter_fields
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
