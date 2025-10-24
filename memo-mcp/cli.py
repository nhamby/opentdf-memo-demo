#!/usr/bin/env python3
"""
CLI wrapper for the USAF Memo MCP Server

This provides a simple command-line interface for testing the server
functionality without needing a full MCP client.
"""

import sys
import json
import argparse
import os
import traceback
from pathlib import Path

# Import server components
from server import (
    get_memo_schema,
    get_memo_example,
    get_memo_description,
    render_memo_to_pdf,
)


def cmd_schema(args):
    """Show the field schema for USAF memos."""
    schema = json.loads(get_memo_schema())
    if args.json:
        print(json.dumps(schema, indent=2))
    else:
        print("USAF Memo Field Schema")
        print("=" * 60)
        for field_name,field_schema in schema["properties"].items():
            print(f"{field_name}: {field_schema}")


def cmd_example(args):
    """Show an example USAF memo."""
    example = get_memo_example()
    if args.output:
        Path(args.output).write_text(example)
        print(f"Example saved to: {args.output}")
    else:
        print(example)


def cmd_description(args):
    """Show the description of the usaf_memo Quill."""
    desc = json.loads(get_memo_description())
    if args.json:
        print(json.dumps(desc, indent=2))
    else:
        print("USAF Memo Quill Description")
        print("=" * 60)
        print(f"Name: {desc['name']}")
        print(f"Backend: {desc['backend']}")
        print(f"Description: {desc['description']}")
        print(f"Supported Formats: {', '.join(desc['supported_formats'])}")


def cmd_render(args):
    """Render a markdown file to PDF."""
    try:
        print(f"Rendering {args.input}...")
        output_path = render_memo_to_pdf(args.input)
        print(f"✓ PDF generated: {output_path}")
        
        file_size = os.path.getsize(output_path)
        print(f"  File size: {file_size:,} bytes")
        
        return 0
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        traceback.print_exc()
        return 1


def main():
    parser = argparse.ArgumentParser(
        description="USAF Memo MCP Server CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s schema              # Show field schema
  %(prog)s example             # Show example memo
  %(prog)s example -o my.md    # Save example to file
  %(prog)s render my.md        # Render memo to PDF
  %(prog)s description --json  # Show description as JSON
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    subparsers.required = True
    
    # Schema command
    schema_parser = subparsers.add_parser("schema", help="Show field schema")
    schema_parser.add_argument("--json", action="store_true", help="Output as JSON")
    schema_parser.set_defaults(func=cmd_schema)
    
    # Example command
    example_parser = subparsers.add_parser("example", help="Show example memo")
    example_parser.add_argument("-o", "--output", help="Save example to file")
    example_parser.set_defaults(func=cmd_example)
    
    # Description command
    desc_parser = subparsers.add_parser("description", help="Show Quill description")
    desc_parser.add_argument("--json", action="store_true", help="Output as JSON")
    desc_parser.set_defaults(func=cmd_description)
    
    # Render command
    render_parser = subparsers.add_parser("render", help="Render memo to PDF")
    render_parser.add_argument("input", help="Input markdown file")
    render_parser.set_defaults(func=cmd_render)
    
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
