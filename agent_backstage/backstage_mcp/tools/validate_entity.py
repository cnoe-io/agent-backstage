"""Tools for /validate-entity operations"""

import logging
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from ..api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def validate_entity() -> Dict[str, Any]:
    """
    
    
    Validate that a passed in entity has no errors in schema.
    
    Returns:
        API response data
    """
    logger.debug(f"Making POST request to /validate-entity")
    params = {}
    data = None
    # Add parameters to request
    
    success, response = await make_api_request(
        "/validate-entity",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
