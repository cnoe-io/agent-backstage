# Copyright 2025 Cisco
# SPDX-License-Identifier: Apache-2.0

.PHONY: build setup-venv activate-venv install run run-acp run-client langgraph-dev help

add-copyright-license-headers:
	@echo "Adding copyright license headers..."
	docker run --rm -v $(shell pwd)/agent_backstage:/workspace ghcr.io/google/addlicense:latest -c "CNOE" -l apache -s=only -v /workspace

setup-venv:
	@echo "======================================="
	@echo " Setting up the Virtual Environment   "
	@echo "======================================="
	@if [ ! -d ".venv" ]; then \
		python3 -m venv .venv; \
		echo "Virtual environment created."; \
	else \
		echo "Virtual environment already exists."; \
	fi

	@echo "======================================="
	@echo " Activating virtual environment       "
	@echo "======================================="
	@if [ -f ".venv/bin/activate" ]; then \
		. .venv/bin/activate; \
		echo "Virtual environment activated."; \
	else \
		echo "Activation script not found. Please check the virtual environment setup."; \
		exit 1; \
	fi

	@echo "======================================="
	@echo " Installing dependencies with Poetry  "
	@echo "======================================="
	. .venv/bin/activate && poetry install

activate-venv:
	@echo "Activating virtual environment..."
	@if [ -d ".venv" ]; then \
		. .venv/bin/activate; \
	else \
		echo "Virtual environment not found. Please run 'make setup-venv' first."; \
	fi

build:
	@echo "======================================="
	@echo " Updating git submodules...           "
	@echo "======================================="
	git submodule update --init --recursive

	@echo "======================================="
	@echo " Building the package using poetry... "
	@echo "======================================="
	poetry build

install:
	@echo "======================================="
	@echo " Activating virtual environment and    "
	@echo " Installing poetry the current package "
	@echo "======================================="
	. .venv/bin/activate && poetry install

run: build install
	@echo "Running the application..."
	. .venv/bin/activate && . .env && python3 -m agent_backstage

run-acp: setup-venv build install
	. .venv/bin/activate && wfsm deploy -m ./deploy/acp/agent.json -e ./deploy/acp/agent-env.yaml

run-client: build install
	@echo "Running the client..."
	. .venv/bin/activate && set -a && . .env && set +a && \
	python3 client/client_agent.py

run-curl-client: build install
	@echo "Running the curl client..."
	. .venv/bin/activate && set -a && . .env && set +a && \
	./client/client_curl.sh

langgraph-dev: build install
	@echo "Running the LangGraph agent..."
	. .venv/bin/activate && . .env && langgraph dev

help:
	@echo "Available targets:"
	@echo "  setup-venv       Create virtual environment in .venv and install dependencies"
	@echo "  activate-venv    Activate the virtual environment"
	@echo "  build            Build the project using poetry"
	@echo "  install          Install the package"
	@echo "  run              Build, install, and run the application"
	@echo "  run-acp          Deploy using wfsm with ACP configuration"
	@echo "  run-client       Run the client application"
	@echo "  langgraph-dev    Run the LangGraph agent"
	@echo "  help             Show this help message" 