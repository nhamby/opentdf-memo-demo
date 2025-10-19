# USAF Memo MCP Server

A specialized MCP (Model Context Protocol) server for creating USAF memos using the Quillmark rendering engine and the usaf_memo Quill template.

## Features

- **Resources**: Provides context about the usaf_memo Quill template
  - `memo://schema` - Field schemas with descriptions and requirements
  - `memo://example` - Example USAF memo in markdown format
  - `memo://description` - Metadata about the usaf_memo Quill

- **Tools**: Markdown to PDF rendering
  - `render_memo_to_pdf` - Converts USAF memo markdown files to PDF

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

The server uses stdio transport for communication with MCP clients:

```bash
python server.py
```

### Using with MCP Clients

Configure your MCP client to use this server. Example configuration for Claude Desktop:

```json
{
  "mcpServers": {
    "usaf-memo": {
      "command": "python",
      "args": ["/path/to/memo-mcp/server.py"]
    }
  }
}
```

### Resources

Query available resources to get information about the USAF memo template:

- **Schema**: Get detailed information about all available fields, their types, and requirements
- **Example**: Get a complete example memo to use as a template
- **Description**: Get metadata about the Quill including supported output formats

### Tools

**render_memo_to_pdf**

Renders a USAF memo markdown file to PDF.

Parameters:
- `markdown_file_path` (string): Path to the markdown file to render

Returns:
- Path to the generated PDF file in the `output/` directory

Example memo structure:

```markdown
---
QUILL: usaf_memo
memo_for:
  - RECIPIENT ORG/SYMBOL
  - ORGANIZATION NAME
memo_from:
  - SENDER ORG/SYMBOL
  - ORGANIZATION NAME
  - Street Address
  - City, State ZIP
subject: Subject Line of the Memo
signature_block:
  - FIRST M. LAST, Rank, USSF
---

First paragraph of the memo body.

Second paragraph with more details.

- Bullet point
  - Nested bullet point

**Bold text** and _italic text_ are supported.
```

### Required Fields

The following fields are required in the frontmatter:
- `memo_for` - Recipient information (multiline)
- `memo_from` - Sender information (multiline)
- `subject` - Subject line
- `signature_block` - Signature block (multiline)

### Optional Fields

- `date` - Date of memo (YYYY-MM-DD); defaults to today
- `letterhead_title` - Title in letterhead
- `letterhead_caption` - Caption in letterhead
- `references` - References for the memo (array)
- `cc` - Carbon copy recipients (array)
- `distribution` - Distribution list (array)
- `attachments` - Attachments (array)
- `tag_line` - Footer tag line

## Output

Rendered PDFs are saved to the `output/` directory with timestamps:
- Format: `memo_YYYYMMDD_HHMMSS.pdf`
- The output directory is automatically created if it doesn't exist
- Output files are gitignored

## Dependencies

- **quillmark** (>=0.4.0) - Markdown rendering engine with Quill support
- **mcp** (>=1.18.0) - Model Context Protocol server framework

## Architecture

The server is built using:
- **FastMCP**: Simplified MCP server framework
- **Quillmark**: Rust-based markdown rendering with typst backend
- **usaf_memo Quill**: Custom template for USAF official memorandums

## Error Handling

The server provides clear error messages for common issues:
- Missing markdown files
- Invalid QUILL tags (must be `usaf_memo`)
- Parsing errors in markdown
- Rendering failures

## Testing

Run the test suite to verify functionality:

```bash
python /tmp/test_mcp_server.py
```

This tests:
- Resource retrieval (schema, example, description)
- PDF rendering
- Error handling for invalid inputs
