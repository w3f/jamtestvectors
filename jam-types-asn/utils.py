import os
import re
import json
import asn1tools
import glob


def get_schema_files(full = False):
    schema_files = [ "../jam-types-asn/jam-types.asn" ]
    if full:
        schema_files += [ "../jam-types-asn/full-const.asn" ]
    else:
        schema_files += [ "../jam-types-asn/tiny-const.asn" ]
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


def path_to_schema_name(path):
    # Strip the directory path and extension
    name = os.path.splitext(os.path.basename(path))[0]   
    # Remove "_X" if it ends with a number
    name = re.sub(r'_\d+$', '', name)   
    # Convert kebab-case or snake_case to PascalCase
    name = re.sub(r'[-_](\w)', lambda m: m.group(1).upper(), name)   
    # Capitalize the first character
    name = name[0].upper() + name[1:]   
    return name    


def validate(schema, path, schema_name = None, json_tweaks_callback = None):  
    print("* Validating: ", path)

    if schema_name is None:
        schema_name = path_to_schema_name(path)
        
    # Decode from json using the schema
    json_bytes = open(path, "rb").read()
    json_str_org = json_bytes.decode('utf-8')
    json_str_org = make_asn1_parsable(json_str_org, json_tweaks_callback)
    
    json_bytes = json_str_org.encode('utf-8')
    decoded = schema.decode(schema_name, json_bytes, check_constraints=True)

    # Encode to json using the schema
    encoded = schema.encode(schema_name, decoded, check_constraints=True)
    # Original json uses snake case, asn1 requires kebab case
    json_str = encoded.decode('utf-8')
    json_obj = json.loads(json_str)
    # Strings are converted to arrays of characters,
    # map back to single string.
    json_str = json.dumps(json_obj, indent = 4)

    assert (json_str.rstrip().lower() == json_str_org.rstrip().lower())

def validate_group(group_name, group_schema, spec_name):
    print(f"\n[Validating {group_name} ({spec_name})]")
    schema = asn1tools.compile_files(get_schema_files(spec_name == "full") + [group_schema], codec="jer")
    for json_file in glob.glob(f"{spec_name}/*.json"):
        validate(schema, json_file, "TestCase")

