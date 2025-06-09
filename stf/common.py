from jam_types import Struct

class Dump(Struct):
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
