#!/usr/bin/env python3
#
# Convert binary encoded test vectors to JSON.
#
# Depends on: [jam_types](https://github.com/davxy/jam-types)

import argparse
import json
import os
import sys
from pathlib import Path

from jam_types import Struct, ByteSequence, ScaleBytes
from jam_types import class_name as n

class EcTestVector(Struct):
    type_mapping = [
        ("data", n(ByteSequence)),
        ("shards", "Vec<ByteSequence>"),
    ]

def convert_single_file(src_file, dst_file=None):
    """Convert a single binary file to JSON."""
    with open(src_file, 'rb') as file:
        blob = file.read()
        scale_bytes = ScaleBytes(blob)
        dump = EcTestVector(data=scale_bytes)
        decoded = dump.decode()
        
        if dst_file:
            with open(dst_file, 'w') as out_file:
                json.dump(decoded, out_file, indent=4)
        else:
            print(json.dumps(decoded, indent=4))

def convert_batch_single_spec(vectors_dir, jam_spec, verbose=False):
    """Convert all binary files in a directory to JSON for a single spec."""
    # Determine the actual vectors directory
    if jam_spec:
        vectors_path = Path(vectors_dir) / jam_spec
    else:
        vectors_path = Path(vectors_dir)
    
    vectors_path = vectors_path.resolve()
    
    if not vectors_path.exists():
        print(f"Error: Source directory '{vectors_path}' does not exist", file=sys.stderr)
        return 0
    
    print(f"Converting binary erasure-coding vectors from: '{vectors_path}'")
    if jam_spec:
        print(f"JAM_SPEC: {jam_spec}")
    print()
    
    # Find all .bin files
    bin_files = list(vectors_path.glob("*.bin"))
    
    if not bin_files:
        print(f"  No .bin files found in {vectors_path}")
        return 0
    
    processed = 0
    total_files = len(bin_files)
    
    for i, src_file in enumerate(bin_files, 1):
        filename = src_file.name
        dst_json = src_file.with_suffix('.json')
        
        if verbose:
            print(f"  [{i}/{total_files}] Processing: {filename}")
            print(f"    Source: {src_file}")
            print(f"    JSON:   {dst_json}")
        else:
            print(f"  [{i}/{total_files}] Processing {filename}...")
        
        try:
            convert_single_file(src_file, dst_json)
            processed += 1
            if verbose:
                print("    ✓ Success")
        except Exception as e:
            print(f"    Error: Failed to process {filename}: {e}", file=sys.stderr)
            # Clean up partial file
            if dst_json.exists():
                dst_json.unlink()
            return processed
        
        if verbose:
            print()
    
    print()
    print("Conversion complete!")
    print(f"Processed: {processed} files")
    return processed

def convert_batch(vectors_dir, jam_spec, verbose=False):
    """Convert all binary files in a directory to JSON."""
    if jam_spec:
        # Process single spec
        convert_batch_single_spec(vectors_dir, jam_spec, verbose)
    else:
        # Process both specs
        total_processed = 0
        for spec in ['tiny', 'full']:
            print(f"=== Processing {spec} spec ===")
            processed = convert_batch_single_spec(vectors_dir, spec, verbose)
            total_processed += processed
            print()
        
        print("=== Overall Summary ===")
        print(f"Total files processed: {total_processed}")

def main():
    parser = argparse.ArgumentParser(description='Convert erasure-coding binary test vectors to JSON')
    parser.add_argument('filename', type=str, nargs='?', help='Single file to convert (if not provided, batch mode)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('-s', '--spec', choices=['tiny', 'full'], help='JAM_SPEC for batch mode (tiny|full)')
    parser.add_argument('-d', '--dir', default='.', help='Vectors directory for batch mode (default: current directory)')
    parser.add_argument('--batch', action='store_true', help='Force batch mode even if filename is provided')

    args = parser.parse_args()

    # Check environment variables
    jam_spec = args.spec or os.environ.get('JAM_SPEC')
    vectors_dir = args.dir or os.environ.get('VECTORS_DIR', '.')

    # Validate JAM_SPEC if provided
    if jam_spec and jam_spec not in ['tiny', 'full']:
        print(f"Error: JAM_SPEC must be 'tiny' or 'full', got '{jam_spec}'", file=sys.stderr)
        sys.exit(1)

    # Determine mode
    if args.filename and not args.batch:
        # Single file mode
        convert_single_file(args.filename)
    else:
        # Batch mode
        convert_batch(vectors_dir, jam_spec, args.verbose)

if __name__ == '__main__':
    main()
