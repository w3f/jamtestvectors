from bin_to_json import StfTestVector
from jam_types import (
    Null,
    OpaqueHash,
    Struct,
    TimeSlot,
    AuthPools,
    AuthQueues,
    CoreIndex
)
from jam_types import class_name as n


class CoreAuthorizer(Struct):
    type_mapping = [
        ('core', n(CoreIndex)),
        ('auth_hash', n(OpaqueHash)),
    ]

class AuthorizationsState(Struct):
    type_mapping = [
        ('auth_pools', n(AuthPools)),
        ('auth_queues', n(AuthQueues)),
    ]

class AuthorizationsInput(Struct):
    type_mapping = [
        ('slot', n(TimeSlot)),
        ('auths', 'Vec<CoreAuthorizer>')
    ]

class AuthorizationsOutput(Null):
    pass

class AuthorizationsTestVector(StfTestVector):
    state_class = n(AuthorizationsState)
    input_class = n(AuthorizationsInput)
    output_class = n(AuthorizationsOutput)
