#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

# Mapping af replacement characters til rigtige danske karakterer
replacements = {
    'ï¿½ndskrevne': 'håndskrevne',
    'hï¿½ndskrevne': 'håndskrevne',
    'hï¿½nds': 'hånds',
    'ï¿½nske': 'ønske',
    'ï¿½nskede': 'ønskede',
    'ï¿½nsker': 'ønsker',
    'ï¿½ndt': 'ændt',
    'ï¿½ndt': 'ændt',
    'vï¿½rdif': 'værdif',
    'ï¿½rdifuld': 'værdifuld',
    'ï¿½rdi': 'værdi',
    'nï¿½r': 'når',
    'besï¿½g': 'besøg',
    'pï¿½': 'på',
    'mï¿½': 'må',
    'spï¿½rg': 'spørg',
    'sp¿½rge': 'spørge',
    'hï¿½j': 'høj',
    'krï¿½v': 'kræv',
    'undersï¿½g': 'undersøg',
    'afhjï¿½lp': 'afhjælp',
    'lï¿½sn': 'løsn',
    'bï¿½de': 'både',
    'overfï¿½r': 'overfør',
    'stï¿½rre': 'større',
    'ï¿½r': 'år',
    'gï¿½re': 'gøre',
}

template_dir = Path('templates')

for html_file in sorted(template_dir.glob('*.html')):
    print(f"Processing: {html_file.name}", end=" ")
    
    try:
        content = html_file.read_text(encoding='utf-8')
        original = content
        
        # Apply all replacements
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        # If content changed, write it back
        if content != original:
            html_file.write_text(content, encoding='utf-8')
            print("✓ Fixed")
        else:
            print("✓ OK")
            
    except Exception as e:
        print(f"✗ Error: {e}")

print("\nDone!")
