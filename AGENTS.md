
# OpenTDF Memo Demo

## Project Overview

This demo showcases OpenTDF encryption/decryption capabilities integrated with USAF memo generation. The project demonstrates how to:
- Decrypt OpenTDF-encrypted documents (TDF/nanoTDF formats)
- Generate official USAF memos using the usaf_memo Quill template
- Render memos to PDF format

## Available MCP Servers

### opentdf-mcp
Provides OpenTDF encryption and decryption capabilities.

**Tools:**
- `mcp__opentdf-mcp__encrypt` - Encrypt data with attributes (supports TDF/nanoTDF)
- `mcp__opentdf-mcp__decrypt` - Decrypt TDF/nanoTDF files (auto-detects format)
- `mcp__opentdf-mcp__list_attributes` - List available data attributes

**Usage Example:**
```
# Decrypt a file
mcp__opentdf-mcp__decrypt(input: "/path/to/file.ntdf")

# Encrypt data
mcp__opentdf-mcp__encrypt(
  data: "sensitive content",
  attributes: ["https://example.com/attr/classification/secret"],
  format: "nano"  # Use nano for better compatibility
)
```

### memo-mcp
Helps create USAF memos using the usaf_memo Quill template.

**Tools:**
- `mcp__memo-mcp__render_memo_to_pdf` - Render markdown memo to PDF
- `mcp__memo-mcp__get_memo_schema` - Retrieve the schema for memo markdown frontmatter, ensuring proper structure and compliance.
- `mcp__memo-mcp__get_usage` - Access usage guidelines for creating memos.
- `mcp__memo-mcp__get_memo_example` - Fetch an example memo for reference.

**IMPORTANT Memo Guidelines:**
- Paragraphs auto-number - NEVER use headings or numbering
- Keep it simple - focus on text and content
- Use bullets for nested paragraphs/lists
- Do not use bullets for top-level paragraphs
- If you are deriving from a classified source:
  - Add classification banner
  - Add portion markings at the beginning of each paragraph

## Common Workflows

### Decrypt Report and Create Memo

**Workflow:**
1. Find encrypted file: e.g. `Glob` pattern `**/*.ntdf`
2. Decrypt: `mcp__opentdf-mcp__decrypt(input: "/path/to/file.ntdf")`
3. Review content and extract key points
4. Get memo guidelines: 
  - `mcp__memo-mcp__get_memo_schema()` or `memo://schema`
  - `mcp__memo-mcp__get_usage()` or `memo://usage`
  - `mcp__memo-mcp__get_memo_example()` or `memo://example`
5. Create memo markdown with QUILL frontmatter in `drafts/`
6. Render to PDF: `mcp__memo-mcp__render_memo_to_pdf(markdown_file_path: "...")`

**Example Task:**
```
User: "decrypt CLASSIFIED_REPORT and write an urgent memo to Congress"
→ Find .ntdf file
→ Decrypt with opentdf-mcp
→ Analyze decrypted content
- Read memo usage, schema, and example
→ Create USAF memo markdown
→ Render to PDF
```

## Best Practices

### OpenTDF
- Prefer nanoTDF format (`format: "nano"`) for better compatibility
- Decrypt tool auto-detects TDF vs nanoTDF format
- Check available attributes with `list_attributes` before encrypting

### File Operations
- Check if files exist with Glob before attempting operations
- Use absolute paths for all file operations
- Read files before editing/writing to ensure correct handling
- Create markdown files in `drafts/` before rendering to pdf