# JSON validation using ASN.1 schema support utilities.
#
# Depends on [`asn1tools`](https://github.com/davxy/asn1tools)
 
import os
import re
import json
import asn1tools
import glob


def get_schema_files(full=False):
    """Get the list of schema files for compilation.
    
    Args:
        full: If True, use full-const.asn, otherwise use tiny-const.asn
        
    Returns:
        List of absolute paths to schema files
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    schema_files = [os.path.join(script_dir, "jam-types.asn")]
    
    if full:
        schema_files.append(os.path.join(script_dir, "full-const.asn"))
    else:
        schema_files.append(os.path.join(script_dir, "tiny-const.asn"))
    
    return schema_files


def make_asn1_parsable(json_str, json_tweaks_callback=None):
    """Transform JSON to be parsable by ASN.1 schema.
    
    Transformations:
    - Apply user-defined tweak callback if provided
    - Convert snake_case to kebab-case (JSON uses snake case, ASN.1 requires kebab case)
    - Remove '0x' prefix from hex strings (ASN.1 doesn't like it)
    
    Args:
        json_str: Original JSON string
        json_tweaks_callback: Optional callback to modify JSON object
        
    Returns:
        Modified JSON string compatible with ASN.1
    """
    if json_tweaks_callback is not None:
        json_obj = json.loads(json_str)
        json_obj = json_tweaks_callback(json_obj)
        json_str = json.dumps(json_obj, indent=4)
    
    # Convert snake_case to kebab-case and remove hex prefixes
    json_str = json_str.replace('_', '-').replace('0x', '')
    return json_str


def path_to_type_name(path):
    """Convert file path to ASN.1 type name.
    
    Converts filename to PascalCase for ASN.1 type detection.
    
    Args:
        path: File path
        
    Returns:
        PascalCase type name
    """
    # Strip directory path and extension
    name = os.path.splitext(os.path.basename(path))[0]
    # Remove "_X" suffix if it ends with a number
    name = re.sub(r'_\d+$', '', name)
    # Convert kebab-case or snake_case to PascalCase
    name = re.sub(r'[-_](\w)', lambda m: m.group(1).upper(), name)
    # Capitalize the first character
    name = name[0].upper() + name[1:]
    return name


def validate(schema, json_file, root_type = None, json_tweaks_callback = None):
    """Validate a JSON file against an ASN.1 schema.
    
    Args:
        schema: Compiled ASN.1 schema
        json_file: Path to JSON file to validate
        root_type_name: Optional schema type name to be used to parse the json_file
        json_tweaks_callback: Optional callback to modify JSON before validation

    If the `root_type_name` arg is None or is not present in the schema, then the root
    type for decoding is determined as follows:
    - If the schema contains "TestCase", use that type
    - Otherwise, derive the type from the filename (e.g., "my_type.json" → "MyType")

    """
    print("* Validating:", json_file)

    # Determine root type used for decoding
    if root_type is None:
        if "TestCase" in schema.types:
            root_type = "TestCase"
        else:
            # Auto-detect root type from filename
            root_type = path_to_type_name(json_file)

    # Read and prepare JSON
    with open(json_file, "rb") as f:
        json_bytes = f.read()
    
    json_str_org = json_bytes.decode('utf-8')
    json_str_org = make_asn1_parsable(json_str_org, json_tweaks_callback)

    # Validate by round-trip encoding/decoding
    json_bytes = json_str_org.encode('utf-8')
    decoded = schema.decode(root_type, json_bytes, check_constraints=True)
    encoded = schema.encode(root_type, decoded, check_constraints=True)
    
    # Normalize for comparison
    json_str = encoded.decode('utf-8')
    json_obj = json.loads(json_str)
    json_str = json.dumps(json_obj, indent=4)

    # Verify round-trip consistency
    assert json_str.rstrip().lower() == json_str_org.rstrip().lower()

def validate_group(group_name, group_schema, spec_name, json_tweaks_callback=None):
    """Validate a group of JSON files against an ASN.1 schema.
    
    Args:
        group_name: Name of the validation group (for display)
        group_schema: ASN.1 schema file name (or None for base schema only)
        spec_name: Specification name ("tiny", "full")
        json_tweaks_callback: Optional callback to modify JSON before validation
    """
    print(f"\n[Validating {group_name} ({spec_name})]")
    
    # Build schema file list
    schema_files = get_schema_files(spec_name == "full")
    if group_schema is not None:
        schema_files.append(group_schema)
    
    # Compile schema and validate all JSON files
    schema = asn1tools.compile_files(schema_files, codec="jer")
    for json_file in glob.glob(f"{spec_name}/*.json"):
        validate(schema, json_file, None, json_tweaks_callback)
