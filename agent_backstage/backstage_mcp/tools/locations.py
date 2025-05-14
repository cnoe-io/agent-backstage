"""Tools for /locations operations"""

import logging
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from ..api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def create_location(dry_run: Optional[str] = None) -> Dict[str, Any]:
    """
    
    
    Create a location for a given target.
    
    Returns:
        API response data
    """
    logger.debug(f"Making POST request to /locations")
    params = {}
    data = None
    # Add parameters to request
    if dry_run is not None:
        params["dryRun"] = dry_run
    success, response = await make_api_request(
        "/locations",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response

async def get_locations() -> Dict[str, Any]:
    """
    
    
    Get all locations
    
    Returns:
        API response data
    """
    logger.debug(f"Making GET request to /locations")
    params = {}
    data = None
    # Add parameters to request
    
    success, response = await make_api_request(
        "/locations",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
