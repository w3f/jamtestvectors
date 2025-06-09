#!/usr/bin/env bash
#
# Convert STF binary vectors to JSON.

set -euo pipefail
 
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Relative to this script folder
DEFAULT_JAM_SPEC="full"
DEFAULT_VECTORS_DIR="$(realpath "../../../crates/node/data/stf-vectors")"

usage() {
    cat << EOF
Usage: $0 [OPTIONS] SUBSYSTEM

Convert STF binary vectors to JSON format.

ARGUMENTS:
    SUBSYSTEM       Subsystem to process (safrole|disputes|history|reports|assurances|statistics|authorizations|preimages|accumulate|all)

OPTIONS:
    -h, --help      Show this help message
    -v, --verbose   Enable verbose output
    -s, --spec SPEC Set JAM_SPEC (tiny|full, default: full)
    -d, --dir DIR   Set SOURCE_DIR (default: crates/node/data/stf-vectors)

ENVIRONMENT:
    JAM_SPEC        Specification type (tiny|full)
    VECTORS_DIR     Vectors directory
EOF
}

VERBOSE=false
SUBSYSTEM=""

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
        -*)
            echo "Unknown option: $1" >&2
            usage >&2
            exit 1
            ;;
        *)
            if [[ -z "$SUBSYSTEM" ]]; then
                SUBSYSTEM="$1"
                shift
            else
                echo "Too many arguments" >&2
                usage >&2
                exit 1
            fi
            ;;
    esac
done

if [[ -z "$SUBSYSTEM" ]]; then
    echo "Error: SUBSYSTEM argument is required" >&2
    usage >&2
    exit 1
fi

function prepare_environment() {
    JAM_SPEC="${JAM_SPEC:-$DEFAULT_JAM_SPEC}"
    if [[ "$JAM_SPEC" != "tiny" && "$JAM_SPEC" != "full" ]]; then
        echo "Error: JAM_SPEC must be 'tiny' or 'full', got '$JAM_SPEC'" >&2
        exit 1
    fi
    export JAM_SPEC

    VECTORS_DIR="${VECTORS_DIR:-$DEFAULT_VECTORS_DIR/$JAM_SPEC}"
    VECTORS_DIR="$(realpath "$VECTORS_DIR")"

    # Validate subsystem choice
    if [[ ! " ${subsystems[*]} " =~ " ${SUBSYSTEM} " ]]; then
        echo "Error: Invalid subsystem '${SUBSYSTEM}'" >&2
        echo "Allowed subsystems are: ${subsystems[*]}" >&2
        exit 1
    fi

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

    # Validate main.py exists
    if [[ ! -x "./main.py" ]]; then
        echo "Error: main.py not found or not executable" >&2
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

function process_subsystem() {
    local subsystem="$1"
    local sub_src_dir="${VECTORS_DIR}/${subsystem}"
    local processed=0
    local skipped=0
    
    echo "[Processing subsystem: $subsystem]"
    
    if [[ ! -d "$sub_src_dir" ]]; then
        echo "Warning: Subsystem directory '$sub_src_dir' not found, skipping" >&2
        return 0
    fi
    
    local total_files=0
    for src_file in "$sub_src_dir"/*.bin; do
        [[ -f "$src_file" ]] && total_files=$((total_files + 1))
    done
    
    if [[ $total_files -eq 0 ]]; then
        echo "  No files found in $sub_src_dir"
        return 0
    fi
    
    for src_file in "$sub_src_dir"/*.bin; do
        if [[ ! -f "$src_file" ]]; then
            continue
        fi

        local filename=$(basename "$src_file")
        local dst_json="${sub_src_dir}/${filename%.*}.json"
        
        if [[ "$VERBOSE" == true ]]; then
            echo "  [$((processed + skipped + 1))/$total_files] Processing: $filename"
            echo "    Source: $src_file"
            echo "    JSON:   $dst_json"
        else
            echo "  [$((processed + skipped + 1))/$total_files] Processing $filename..."
        fi
        
        # Convert to JSON
        if ./main.py --subsystem "$subsystem" "$src_file" > "$dst_json"; then
            processed=$((processed + 1))
            [[ "$VERBOSE" == true ]] && echo "    ✓ Success"
        else
            echo "    Error: Failed to process $filename" >&2
            rm -f "$dst_json"  # Clean up partial file
            exit 1
        fi
        
        [[ "$VERBOSE" == true ]] && echo
    done
    
    echo "  Subsystem $subsystem: $processed files processed"
    [[ $skipped -gt 0 ]] && echo "  Subsystem $subsystem: $skipped files skipped" || true
}

# Valid subsystems
declare -a subsystems=(
    "safrole"
    "disputes"
    "history"
    "reports"
    "assurances"
    "statistics"
    "authorizations"
    "preimages"
    "accumulate"
    "all"
)

prepare_environment

echo "Converting binary STF vectors from: '$VECTORS_DIR'"
echo "JAM_SPEC: $JAM_SPEC"
echo

if [[ "$SUBSYSTEM" != "all" ]]; then
    subsystems=($SUBSYSTEM)
fi

for sub in "${subsystems[@]}"; do
    if [[ "$sub" != "all" ]]; then
        process_subsystem "$sub"
    fi
done
echo
echo "Conversion complete!"
exit 0
