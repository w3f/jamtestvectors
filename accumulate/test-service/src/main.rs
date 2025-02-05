#![cfg_attr(any(target_arch = "riscv32", target_arch = "riscv64"), no_std)]
#![cfg_attr(any(target_arch = "riscv32", target_arch = "riscv64"), no_main)]

extern crate alloc;

use alloc::vec::Vec;
use jam_types::{
    AccumulateItem, Hash, PackageInfo, ServiceId, Slot, TransferRecord, WorkOutput, WorkPayload,
};

#[cfg(not(any(target_arch = "riscv32", target_arch = "riscv64")))]
fn main() {}

#[allow(dead_code)]
struct Service;
jam_pvm_common::declare_service!(Service);

impl jam_pvm_common::Service for Service {
    fn refine(
        _id: ServiceId,
        payload: WorkPayload,
        _package_info: PackageInfo,
        _extrinsics: Vec<Vec<u8>>,
    ) -> WorkOutput {
        [&b"Hello "[..], payload.take().as_slice()].concat().into()
    }
    fn accumulate(_slot: Slot, _id: ServiceId, items: Vec<AccumulateItem>) -> Option<Hash> {
        for item in items.into_iter() {
            if let Ok(data) = item.result {
                jam_pvm_common::accumulate::set_storage(item.package.as_slice(), &data)
                    .expect("not enough balance?!");
            }
        }
        None
    }
    fn on_transfer(_slot: Slot, _id: ServiceId, _items: Vec<TransferRecord>) {}
}
