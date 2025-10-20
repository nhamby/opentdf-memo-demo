#!/bin/bash
# MCP Server Initialization

set -e

cd "$(dirname "$0")"

echo "Installing memo-mcp dependencies..."
pip install -q -r memo-mcp/requirements.txt

echo "Creating output directory..."
mkdir -p memo-mcp/output

echo "Done! Restart Claude Code to load MCP servers."
