# Generated MCP Server

This is an automatically generated Model Context Protocol (MCP) server based on an OpenAPI specification.

## Setup

1. Copy `.env.example` to `.env` and fill in your API credentials:
```bash
cp .env.example .env
```

2. Install dependencies:
```bash
poetry install
```

3. Run the server:
```bash
poetry run python -m server
```

## Available Tools

The following tools are available through the MCP server:


### POST /refresh


Refresh the entity related to entityRef.


### GET /entities


Get all entities matching a given filter.


### GET /entities/by-uid/{uid}


Get a single entity by the UID.


### DELETE /entities/by-uid/{uid}


Delete a single entity by UID.


### GET /entities/by-name/{kind}/{namespace}/{name}


Get an entity by an entity ref.


### GET /entities/by-name/{kind}/{namespace}/{name}/ancestry


Get an entity's ancestry by entity ref.


### POST /entities/by-refs


Get a batch set of entities given an array of entityRefs.


### GET /entities/by-query


Search for entities by a given query.


### GET /entity-facets


Get all entity facets that match the given filters.


### POST /locations


Create a location for a given target.


### GET /locations


Get all locations


### GET /locations/{id}


Get a location by id.


### DELETE /locations/{id}


Delete a location by id.


### GET /locations/by-entity/{kind}/{namespace}/{name}


Get a location for entity.


### POST /analyze-location


Validate a given location.


### POST /validate-entity


Validate that a passed in entity has no errors in schema.

