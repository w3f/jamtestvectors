from bin_to_json import StfTestVector
from jam_types import (
    Null,
    OpaqueHash,
    Struct,
    PreimagesXt,
    Enum,
    TimeSlot,
    ServiceId,
    U32,
    ByteSequence,
    Errno,
    ServicesStatistics
)
from jam_types import class_name as n

class PreimagesMapEntry(Struct):
    type_mapping = [
        ('hash', n(OpaqueHash)),
        ('blob', n(ByteSequence)),
    ]

class PreimagesLookupMetaMapKey(Struct):
    type_mapping = [
        ('hash', n(OpaqueHash)),
        ('length', n(U32)),
    ]

class PreimagesLookupMetaMapEntry(Struct):
    type_mapping = [
        ('key', n(PreimagesLookupMetaMapKey)),
        ('value', 'Vec<TimeSlot>'),
    ]

class PreimagesAccountMapData(Struct):
    type_mapping = [
        ('preimages', 'Vec<PreimagesMapEntry>'),
        ('lookup_meta', 'Vec<PreimagesLookupMetaMapEntry>'),
    ]

class PreimagesAccountMapEntry(Struct):
    type_mapping = [
        ('id', n(ServiceId)),
        ('data', n(PreimagesAccountMapData))
    ]    

class PreimagesState(Struct):
    type_mapping = [
        ('accounts', 'Vec<PreimagesAccountMapEntry>'),
        ('statistics', n(ServicesStatistics)),
    ]

class PreimagesInput(Struct):
    type_mapping = [
        ('preimages', n(PreimagesXt)),
        ('slot', n(TimeSlot)),
    ]

class PreimagesOutput(Enum):
    type_mapping = {
        0: ('ok', n(Null)),
        1: ('err', n(Errno))
    }

class PreimagesTestVector(StfTestVector):
    state_class = n(PreimagesState)
    input_class = n(PreimagesInput)
    output_class = n(PreimagesOutput)
    errno_map = {
        0: "preimage_unneeded",
        1: "preimages_not_sorted_unique",
    }
