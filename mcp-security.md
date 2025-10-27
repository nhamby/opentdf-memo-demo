# OpenTDF secure context access for LLMs

**Goal:** Provide fine-grained access to secure files for LLMs.

Our OpenTDF MCP server will authenticate the end user using OIDC. The end user will explicitly authorize the LLM to access secure files that the end user can access. i.e., explicit permission delegation.

**Implementation Details:**
- Permissions granted on per-file or per-folder basis for granular control
- Option for persistent, one-time, or time-limited access to context.

## Secure RAG

Exists

## 