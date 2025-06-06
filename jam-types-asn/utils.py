import os
import re
import json
import asn1tools
import glob

def get_schema_files(full = False):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    schema_files = [ os.path.join(script_dir, "jam-types.asn") ]
    if full:
        schema_files += [ os.path.join(script_dir, "full-const.asn") ]
    else:
        schema_files += [ os.path.join(script_dir, "tiny-const.asn") ]
    return schema_files
    

# Tweaks:
# - Support for user defined tweak callback. This is called first.
# - JSON uses snake case, ASN.1 requires kebab case.
# - JSON prefix octet strings with '0x', ASN doesn't like it.
def make_asn1_parsable(json_str, json_tweaks_callback):
    if json_tweaks_callback is not None:
        json_obj = json.loads(json_str)
        json_obj = json_tweaks_callback(json_obj)
        json_str = json.dumps(json_obj, indent=4)
    json_str = json_str.replace('_', '-').replace('0x', '')
    return json_str


def path_to_root_type(path):
    # Strip the directory path and extension
    name = os.path.splitext(os.path.basename(path))[0]   
    # Remove "_X" if it ends with a number
    name = re.sub(r'_\d+$', '', name)   
    # Convert kebab-case or snake_case to PascalCase
    name = re.sub(r'[-_](\w)', lambda m: m.group(1).upper(), name)   
    # Capitalize the first character
    name = name[0].upper() + name[1:]   
    return name    


def validate(schema, json_file, json_tweaks_callback = None):  
    print("* Validating: ", json_file)

    if "TestCase" in schema.types:
        root_type = "TestCase"   
    else:
        # Auto-detect root type from schema
        root_type = path_to_root_type(json_file)
        
    # Decode from json using the schema
    json_bytes = open(json_file, "rb").read()
    json_str_org = json_bytes.decode('utf-8')
    json_str_org = make_asn1_parsable(json_str_org, json_tweaks_callback)
    
    json_bytes = json_str_org.encode('utf-8')
    decoded = schema.decode(root_type, json_bytes, check_constraints=True)

    # Encode to json using the schema
    encoded = schema.encode(root_type, decoded, check_constraints=True)
    # Original json uses snake case, asn1 requires kebab case
    json_str = encoded.decode('utf-8')
    json_obj = json.loads(json_str)
    # Strings are converted to arrays of characters,
    # map back to single string.
    json_str = json.dumps(json_obj, indent = 4)

    assert (json_str.rstrip().lower() == json_str_org.rstrip().lower())

def validate_group(group_name, group_schema, spec_name, json_tweaks_callback = None):
    print(f"\n[Validating {group_name} ({spec_name})]")
    schema_files = get_schema_files(spec_name == "full")
    if group_schema is not None:
        schema_files += [group_schema]
    schema = asn1tools.compile_files(schema_files, codec="jer")
    for json_file in glob.glob(f"{spec_name}/*.json"):
        validate(schema, json_file, json_tweaks_callback)
