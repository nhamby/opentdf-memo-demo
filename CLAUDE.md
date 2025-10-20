# OpenTDF Memo Demo - Claude Code Documentation

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

**Resources:**
- `memo://usage` - Usage and writing tips (REQUIRED before writing memos)
- `memo://schema` - Field schema for USAF memos
- `memo://example` - Example USAF memo markdown

**Tools:**
- `mcp__memo-mcp__render_memo_to_pdf` - Render markdown memo to PDF

**IMPORTANT Memo Guidelines:**
- Paragraphs auto-number - DO NOT use headers or manual numbering
- Keep it simple - focus on text and content
- No classification markings in the template
- Use bullets for nested paragraphs
- Markdown support: bold, italics, links, code, strikethrough

## Common Workflows

### Decrypt Report and Create Memo

**Workflow:**
1. Find encrypted file: e.g. `Glob` pattern `**/CLASSIFIED_REPORT*` or `**/*.ntdf`
2. Decrypt: `mcp__opentdf-mcp__decrypt(input: "/path/to/file.ntdf")`
3. Review content and extract key points
4. Get memo guidelines: `ReadMcpResourceTool(server: "memo-mcp", uri: "memo://usage")`
5. Create memo markdown with QUILL frontmatter
6. Render to PDF: `mcp__memo-mcp__render_memo_to_pdf(markdown_file_path: "...")`

**Example Task:**
```
User: "decrypt CLASSIFIED_REPORT and write an urgent memo to Congress"
→ Find .ntdf file
→ Decrypt with opentdf-mcp
→ Analyze decrypted content
→ Create USAF memo markdown
→ Render to PDF
```

### USAF Memo Structure

**Required Frontmatter:**
```yaml
---
QUILL: usaf_memo
letterhead_title: DEPARTMENT OF THE AIR FORCE
letterhead_caption: YOUR SQUADRON HERE
memo_for:
  - Recipient Organization/Symbol
memo_from:
  - Sender ORG/SYMBOL
  - Organization Name
  - Street Address
  - City State ZIP
subject: Your subject line here
signature_block:
  - FIRST M. LAST, Rank, USAF
---
```

**Optional Fields:**
- `date:` (YYYY-MM-DD format, defaults to today)
- `cc:` (array)
- `attachments:` (array)
- `distribution:` (array)
- `references:` (array)
- `tag_line:` (e.g., "Aim High")

## Best Practices

### Planning
- Use TodoWrite for multi-step workflows (3+ steps)
- Mark tasks in_progress before starting work
- Complete tasks immediately after finishing (don't batch)

### OpenTDF
- Prefer nanoTDF format (`format: "nano"`) for better compatibility
- Decrypt tool auto-detects TDF vs nanoTDF format
- Check available attributes with `list_attributes` before encrypting

### USAF Memos
- ALWAYS read `memo://usage` before creating memos
- Let auto-numbering handle paragraph structure
- Keep formatting minimal - focus on content clarity
- Use bold for emphasis on urgent items
- PDF output goes to `memo-mcp/output/` directory

### File Operations
- Check if files exist with Glob before attempting operations
- Use absolute paths for all file operations
- Read files before editing/writing to ensure correct handling

## Project Files

- `CLASSIFIED_REPORT.ntdf` - Example encrypted report
- `URGENT_MEMO_TO_CONGRESS.md` - Example memo markdown
- `memo-mcp/output/` - Directory for rendered PDF memos
- `setup-mcp.sh` - MCP server setup script

## Tips & Gotchas

- **Memo auto-numbering**: Don't fight it - use simple paragraphs and bullets
- **Decryption**: Returns JSON with `decryptedData` and `success` fields
- **PDF rendering**: Returns path to generated PDF in `memo-mcp/output/`
- **Classification**: The template itself doesn't handle classification markings
- **Date format**: Use YYYY-MM-DD in frontmatter (e.g., `2025-10-20`)

## Quick Reference

**Decrypt workflow:**
```
Glob → Decrypt → Analyze content
```

**Memo workflow:**
```
Read usage → Create markdown → Render PDF
```

**Combined workflow:**
```
Decrypt report → Extract insights → Create memo → Render PDF
```

## Additional Resources

- OpenTDF Documentation: Check opentdf-mcp server docs
- USAF Memo Examples: `memo://example` resource
- Quill Templates: usaf_memo template system
