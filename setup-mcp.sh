claude mcp add --transport stdio opentdf-mcp --env OPENTDF_PLATFORM_ENDPOINT=OPENTDF_PLATFORM_ENDPOINT --env OPENTDF_CLIENT_ID=opentdf-sdk --env OPENTDF_CLIENT_SECRET=secret -- /workspaces/opentdf-demo-server/opentdf-memo-demo/opentdf-mcp/opentdf-mcp-server

claude mcp add --transport stdio memo-mcp python /workspaces/opentdf-demo-server/opentdf-memo-demo/memo-mcp/server.py