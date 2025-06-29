# Copyright 2025 CNOE
# SPDX-License-Identifier: Apache-2.0
# Generated by CNOE OpenAPI MCP Codegen tool

"""Tools for /entities operations"""

import logging
from typing import Dict, Any, List
from agent_backstage.protocol_bindings.mcp_server.mcp_backstage.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_entities(
    param_fields: List[str] = None,
    param_limit: int = None,
    param_filter: List[str] = None,
    param_offset: int = None,
    param_after: str = None,
    param_order: List[str] = None,
) -> Dict[str, Any]:
    '''
    Retrieves all entities matching the specified filters and query parameters.

    Args:
        param_fields (List[str], optional): Comma-separated list of simplified JSON paths to select specific fields of the entity data to retain in the response. Defaults to None.
        param_limit (int, optional): Maximum number of records to return in the response. Defaults to None.
        param_filter (List[str], optional): One or more filter sets to match against each entity. Each filter set is a comma-separated list of conditions (ANDed), and multiple filter sets are ORed. Conditions can be of the form `<key>` (existence) or `<key>=<value>` (equality). Defaults to None.
        param_offset (int, optional): Number of records to skip in the query page. Defaults to None.
        param_after (str, optional): Pointer to the previous page of results for pagination. Defaults to None.
        param_order (List[str], optional): List of fields to order the results by. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response containing the list of entities matching the query and filter parameters.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      get:
        summary: Get all entities matching a given filter.
        operationId: getEntities
        parameters:
          - in: query
            name: fields
            schema:
              type: array
              items:
                type: string
            description: Comma-separated list of simplified JSON paths to select specific fields of the entity data to retain in the response.
            required: false
            style: form
            explode: false
          - in: query
            name: limit
            schema:
              type: integer
            description: Maximum number of records to return in the response.
            required: false
          - in: query
            name: filter
            schema:
              type: array
              items:
                type: string
            description: One or more filter sets to match against each entity. Each filter set is a comma-separated list of conditions (ANDed), and multiple filter sets are ORed. Conditions can be of the form `<key>` (existence) or `<key>=<value>` (equality).
            required: false
            style: form
            explode: false
          - in: query
            name: offset
            schema:
              type: integer
            description: Number of records to skip in the query page.
            required: false
          - in: query
            name: after
            schema:
              type: string
            description: Pointer to the previous page of results for pagination.
            required: false
          - in: query
            name: order
            schema:
              type: array
              items:
                type: string
            description: List of fields to order the results by.
            required: false
            style: form
            explode: false
        responses:
          '200':
            description: A JSON array of entities matching the query and filter parameters.
            content:
              application/json:
                schema:
                  type: object
                  additionalProperties: true
          '400':
            description: Invalid request parameters.
          '500':
            description: Internal server error.
    '''
    logger.debug("Making GET request to /entities")

    params = {}
    data = {}

    if param_fields is not None:
        params["fields"] = param_fields
    if param_limit is not None:
        params["limit"] = param_limit
    if param_filter is not None:
        params["filter"] = param_filter
    if param_offset is not None:
        params["offset"] = param_offset
    if param_after is not None:
        params["after"] = param_after
    if param_order is not None:
        params["order"] = param_order

    success, response = await make_api_request("/api/catalog/entities", method="GET", params=params, data=data)

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response