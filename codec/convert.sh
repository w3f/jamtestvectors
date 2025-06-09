#!/usr/bin/env bash
#
# Convert codec binary vectors to JSON.

set -euo pipefail
 
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

CONVERT_ONE="./convert.py"

# Relative to this script folder
# It will be extended with full/tiny depending on the JAM_SPEC variable value
DEFAULT_JAM_SPEC="full"
DEFAULT_VECTORS_DIR="$(realpath ".")"

usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Convert codec binary vectors to JSON format.

OPTIONS:
    -h, --help      Show this help message
    -v, --verbose   Enable verbose output
    -s, --spec SPEC Set JAM_SPEC (tiny|full, default: full)
    -d, --dir  DIR  Set VECTORS_DIR (default: crates/node/data/codec-vectors)

ENVIRONMENT:
    JAM_SPEC        Specification type (tiny|full)
    VECTORS_DIR     Vectors directory
EOF
}

VERBOSE=false

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            exit 0
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -s|--spec)
            JAM_SPEC="$2"
            shift 2
            ;;
        -d|--dir)
            VECTORS_DIR="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1" >&2
            usage >&2
            exit 1
            ;;
    esac
done

function prepare_environment() {
    JAM_SPEC="${JAM_SPEC:-$DEFAULT_JAM_SPEC}"
    if [[ "$JAM_SPEC" != "tiny" && "$JAM_SPEC" != "full" ]]; then
        echo "Error: JAM_SPEC must be 'tiny' or 'full', got '$JAM_SPEC'" >&2
        exit 1
    fi
    export JAM_SPEC

    VECTORS_DIR="${VECTORS_DIR:-$DEFAULT_VECTORS_DIR/$JAM_SPEC}"
    VECTORS_DIR="$(realpath "$VECTORS_DIR")"

    # Validate Python environment
    if ! python3 -c "import sys; print(f'Python {sys.version}')" 2>/dev/null; then
        echo "Error: Python3 not available in current environment" >&2
        exit 1
    fi

    # Validate source directory exists
    if [[ ! -d "$VECTORS_DIR" ]]; then
        echo "Error: Source directory '$VECTORS_DIR' does not exist" >&2
        exit 1
    fi

    # Validate CONVERT_ONE exists
    if [[ ! -x $CONVERT_ONE ]]; then
        echo "Error: $CONVERT_ONE not found or not executable" >&2
        exit 1
    fi

    # Check and activate jam-types virtual environment
    if [[ -z "${PIP_LOCAL_VENVS:-}" ]]; then
        PIP_LOCAL_VENVS="$HOME/.local/pip"
        echo "PIP_LOCAL_VENVS not defined, using default: $PIP_LOCAL_VENVS"
    fi

    JAM_TYPES_VENV="$PIP_LOCAL_VENVS/jam-types"
    JAM_TYPES_ACTIVATE="$JAM_TYPES_VENV/bin/activate"

    if [[ ! -f "$JAM_TYPES_ACTIVATE" ]]; then
        echo "Error: jam-types virtual environment not found at '$JAM_TYPES_VENV'" >&2
        echo "Install the jam-types environment first" >&2
        echo "Alternatively, set PIP_LOCAL_VENVS to the correct path:" >&2
        exit 1
    fi

    echo "Activating jam-types environment: $JAM_TYPES_VENV"
    source "$JAM_TYPES_ACTIVATE"

    # Verify the environment is properly activated
    if [[ "${VIRTUAL_ENV:-}" != "$JAM_TYPES_VENV" ]]; then
        echo "Error: Failed to activate jam-types virtual environment" >&2
        echo "Expected VIRTUAL_ENV to be '$JAM_TYPES_VENV' but got '${VIRTUAL_ENV:-}'" >&2
        exit 1
    fi
}

# File type mappings: "filename:parser_type" (parser_type defaults to filename if not specified)
declare -a file_type_map=(
    "refine_context"
    "work_item"
    "work_package"
    "work_result_0:work_result"
    "work_result_1:work_result"
    "work_report"
    "header_0:header"
    "header_1:header"
    "tickets_extrinsic"
    "disputes_extrinsic"
    "preimages_extrinsic"
    "assurances_extrinsic"
    "guarantees_extrinsic"
    "extrinsic"
    "block"
)

prepare_environment

echo "Converting binary codec vectors from: '$VECTORS_DIR'"
echo "JAM_SPEC: $JAM_SPEC"
echo

processed=0
skipped=0
total_files=${#file_type_map[@]}

for entry in "${file_type_map[@]}"; do
    # Parse filename and type
    if [[ "$entry" == *":"* ]]; then
        file="${entry%:*}"
        type="${entry#*:}"
    else
        file="$entry"
        type="$entry"
    fi
    
    src_file="${VECTORS_DIR}/${file}.bin"
    dst_json="${VECTORS_DIR}/${file}.json"
    
    # Check if source file exists
    if [[ ! -f "$src_file" ]]; then
        echo "Warning: Source file '$src_file' not found, skipping" >&2
        skipped=$((skipped + 1))
        continue
    fi
    
    if [[ "$VERBOSE" == true ]]; then
        echo "[$((processed + skipped + 1))/$total_files] Processing: $file (type: $type)"
        echo "  Source: $src_file"
        echo "  JSON:   $dst_json"
    else
        echo "[$((processed + skipped + 1))/$total_files] Processing $file..."
    fi
    
    # Convert to JSON
    if $CONVERT_ONE --type "$type" "$src_file" > "$dst_json"; then
        processed=$((processed + 1))
        [[ "$VERBOSE" == true ]] && echo "  ✓ Success"
    else
        echo "Error: Failed to process $file" >&2
        rm -f "$dst_json"  # Clean up partial file
        exit 1
    fi
    
    [[ "$VERBOSE" == true ]] && echo
done

echo
echo "Conversion complete!"
echo "Processed: $processed files"
[[ $skipped -gt 0 ]] && echo "Skipped: $skipped files"
exit 0
