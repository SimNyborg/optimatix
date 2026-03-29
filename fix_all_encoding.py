#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from pathlib import Path

def fix_encoding(file_path):
    """
    Fix double-encoded UTF-8 and mojibake in HTML files.
    Tries multiple approaches to restore correct encoding.
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        # Try to detect and fix the encoding
        # First, try UTF-8 with error handling
        try:
            # Try reading as UTF-8
            content = data.decode('utf-8')
            
            # Check if there are double-encoded characters
            # These appear as mojibake like Ã¸, Ã©, etc.
            if 'Ã' in content or 'ï¿½' in content:
                # This is likely UTF-8 bytes interpreted as Latin-1
                # Re-encode to bytes as Latin-1, then decode as UTF-8
                content_bytes = content.encode('latin-1')
                content = content_bytes.decode('utf-8', errors='replace')
        except UnicodeDecodeError:
            # If UTF-8 fails, try Latin-1
            content = data.decode('latin-1', errors='replace')
            # Try to fix any double-encoding
            try:
                if 'Ã' in content or 'ï¿½' in content:
                    content_bytes = content.encode('latin-1')
                    content = content_bytes.decode('utf-8', errors='replace')
            except:
                pass
        
        # Remove BOM if present
        if content.startswith('\ufeff'):
            content = content[1:]
        
        # Write back as UTF-8 without BOM
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

# Process all HTML files
template_dir = Path('templates')
count = 0

for html_file in sorted(template_dir.glob('*.html')):
    if fix_encoding(html_file):
        print(f"✓ Fixed: {html_file.name}")
        count += 1
    else:
        print(f"✗ Error: {html_file.name}")

print(f"\nProcessed {count} files")
