"""Component management tools for Backstage MCP"""

import logging
from typing import Dict, Any, Tuple, List
from ..api.client import make_api_request
from .project import get_project_details

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("backstage_mcp")

async def get_component_details(
    project_name: str,
    user_id: str,
    org_name: str,
    repo_name: str,
    component_description: str = None,
    lifecycle: str = None,
    language_stack: str = None
) -> Tuple[str, str, str, str, str, str, List[str], str, str, str]:
    """
    Get details of a specific component owned by the groups that the specified user is a member of.

    Args:
        project_name: The name of the project to find
        user_id: The ID of the user whose groups' components are being searched
        org_name: The organization name for the component
        repo_name: The name of the component to find
        component_description: The description of the component
        lifecycle: The lifecycle of the component
        language_stack: The language stack of the component

    Returns:
        Tuple containing:
        - Project source location
        - Trimmed project source location
        - Component owner
        - Component name
        - Component title
        - Component description
        - Component tags
        - Component type
        - Component lifecycle
        - Component stack
    """
    logger.debug(f"Getting component details for project: {project_name}, repo: {repo_name}")

    try:
        if project_name != "other":
            project_details = await get_project_details(project_name, user_id)
            
            project_source_location = project_details.get("metadata", {}).get("annotations", {}).get("backstage.io/source-location", "")
            component_owner = project_details.get("metadata", {}).get("name", "")
            component_name = repo_name
            component_title = repo_name.replace("-", " ").replace("_", " ").title()
            component_description = component_description or f"Repository for {repo_name}"
            component_tags = project_details.get("metadata", {}).get("tags", [])
            component_owner = f"user:{user_id}"
            component_type = project_details.get("spec", {}).get("type", "")
            component_lifecycle = lifecycle
            component_stack = language_stack
            trimmed_project_source_location = project_source_location.replace(
                "https://github.com/cisco-eti/outshift-platform-backstage-data/tree/main/", ""
            ).replace("url:", "")
        else:
            project_source_location = f"https://github.com/{org_name}/{repo_name}"
            component_owner = f"user:{user_id}"
            component_name = repo_name
            component_title = repo_name.replace("-", " ").replace("_", " ").title()
            component_tags = ["other"]
            component_type = "service"
            component_lifecycle = lifecycle
            component_stack = language_stack
            trimmed_project_source_location = project_source_location

        return (
            project_source_location,
            trimmed_project_source_location,
            component_owner,
            component_name,
            component_title,
            component_description,
            component_tags,
            component_type,
            component_lifecycle,
            component_stack,
        )

    except Exception as e:
        logger.error(f"Error getting component details: {str(e)}")
        raise 