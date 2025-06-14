#!/bin/bash

# Get the directory containing this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Get the parent directory
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

# Check if jam_types python library can be imported
if ! python3 -c "import asn1tools" 2>/dev/null; then
    echo "Error: We depend on asn1tools. Please install the asn1tools Python library." >&2
    exit 1
fi

echo "Searching for validate.py scripts in: $PARENT_DIR"

# Find all validate.py files and execute them
find "$PARENT_DIR" -name "validate.py" -type f | while read -r validate_script; do
    echo "Executing: $validate_script"
    cd "$(dirname "$validate_script")"
    python3 "$(basename "$validate_script")"
done

echo "All validate.py scripts have been executed."
