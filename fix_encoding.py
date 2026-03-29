import os
from pathlib import Path
import sys

template_dir = Path('templates')

print("Scanning for encoding issues...")

for html_file in sorted(template_dir.glob('*.html')):
    print(f"\nProcessing: {html_file.name}")
    
    try:
        with open(html_file, 'rb') as f:
            raw_bytes = f.read()
        
        # Try to detect what encoding the file actually is
        # Check for common mojibake patterns
        has_mojibake = False
        
        # Try UTF-8 first
        try:
            content = raw_bytes.decode('utf-8')
            # Check if we have replacement characters
            if '\ufffd' in content or 'ï¿½' in content:
                has_mojibake = True
                print(f"  → Found mojibake/replacement chars in UTF-8 decode")
        except UnicodeDecodeError:
            has_mojibake = True
            print(f"  → UTF-8 decode failed")
        
        if has_mojibake:
            # Try latin-1 (ISO-8859-1) decode - this should handle any byte sequence
            print(f"  → Re-decoding as latin-1...")
            content = raw_bytes.decode('latin-1')
            
            # Now write back as UTF-8
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Fixed and rewritten as UTF-8")
        else:
            print(f"  ✓ Already correct")
    
    except Exception as e:
        print(f"  ✗ Error: {e}")

print("\n✓ All files processed!")
