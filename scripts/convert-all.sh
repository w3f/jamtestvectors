#!/bin/bash

# Get the directory containing this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Get the parent directory
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

# Check if jam_types python library can be imported
if ! python3 -c "import jam_types" 2>/dev/null; then
    echo "Error: We depend on jam-types. Please install the jam_types Python library." >&2
    exit 1
fi

echo "Searching for convert.py scripts in: $PARENT_DIR"

# Find all convert.py files and execute them
find "$PARENT_DIR" -name "convert.py" -type f | while read -r convert_script; do
    echo "Executing: $convert_script"
    cd "$(dirname "$convert_script")"
    python3 "$(basename "$convert_script")"
done

echo "All convert.py scripts have been executed."
