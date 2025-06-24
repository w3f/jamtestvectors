# Binary to JSON conversion support utilities.
#
# Depends on [`jam_types`](https://github.com/davxy/jam-types)

import json
import glob
from jam_types import Struct, ScaleBytes, spec

class StfTestVector(Struct):
    state_class = None
    input_class = None
    output_class = None
    errno_map = None

    def __init__(self, data):
        self.type_mapping = [
            ('input', self.input_class),
            ('pre_state', self.state_class),
            ('output', self.output_class),
            ('post_state', self.state_class)
        ]
        super().__init__(data)

    def decode(self):
        decoded = super().decode()
        output = decoded['output']
        if isinstance(output, dict):
            errno = output.get('err')
            if errno is not None and self.errno_map is not None:
                decoded['output']['err'] = self.errno_map.get(errno, "other_error")
        return decoded


def convert_to_json(filename, subsystem_type, spec_name = None):
    if spec_name in ("tiny", "full"):
        spec.set_spec(spec_name)
    print("* Converting:", filename)
    with open(filename, 'rb') as file:
        blob = file.read()
        scale_bytes = ScaleBytes(blob)
        dump = subsystem_type(data=scale_bytes)
        decoded = dump.decode()
        json_filename = str(filename).replace('.bin', '.json')
        with open(json_filename, 'w') as json_file:
            json.dump(decoded, json_file, indent=4)
            json_file.write('\n')

def convert_group(group_name, spec_name, subsystem_type):
    if spec_name in ("tiny", "full"):
        spec.set_spec(spec_name)
    print(f"\n[Converting {group_name} ({spec_name})]")
    for file in glob.glob(f"{spec_name}/*.bin"):
        convert_to_json(file, subsystem_type)
