from bin_to_json import StfTestVector
from jam_types import (
    Enum,
    Errno,
    Struct,
    TimeSlot,
    OpaqueHash,
    Entropy,
    ReadyQueue,
    AccumulatedQueue,
    ServiceId,
    ServiceInfo,
    ByteSequence,
    Privileges,
    ServicesStatistics
)
from jam_types import class_name as n

class AccumulateStorageMapEntry(Struct):
    type_mapping = [
        ('key', n(ByteSequence)),
        ('value', n(ByteSequence)),
    ]

class AccumulatePreimagesMapEntry(Struct):
    type_mapping = [
        ('hash', n(OpaqueHash)),
        ('blob', n(ByteSequence)),
    ]

class AccumulateAccountMapData(Struct):
    type_mapping = [
        ('service', n(ServiceInfo)),
        ('storage', 'Vec<AccumulateStorageMapEntry>'),
        ('preimages', 'Vec<AccumulatePreimagesMapEntry>')
    ]

class AccumulateAccountMapEntry(Struct):
    type_mapping = [
        ('id', n(ServiceId)),
        ('data', n(AccumulateAccountMapData))
    ]    

class AccumulateState(Struct):
    type_mapping = [
        ('slot', n(TimeSlot)),
        ('entropy', n(Entropy)),
        ('ready_queue', n(ReadyQueue)),
        ('accumulated', n(AccumulatedQueue)),
        ('privileges', n(Privileges)),
        ('statistics', n(ServicesStatistics)),
        ('accounts', 'Vec<AccumulateAccountMapEntry>'),
    ]  

class AccumulateInput(Struct):
    type_mapping = [
        ('slot', n(TimeSlot)),
        ('reports', 'Vec<WorkReport>'),
    ]

class AccumulateOutput(Enum):
    type_mapping = {
        0: ('ok', n(OpaqueHash)),
        1: ('err', n(Errno))
    }

class AccumulateTestVector(StfTestVector):
    state_class = 'AccumulateState'
    input_class = 'AccumulateInput'
    output_class = 'AccumulateOutput'
