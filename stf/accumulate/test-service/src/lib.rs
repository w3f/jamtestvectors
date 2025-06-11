#![cfg_attr(any(target_arch = "riscv32", target_arch = "riscv64"), no_std)]

extern crate alloc;
use alloc::format;
use jam_pvm_common::*;
use jam_types::*;

#[allow(dead_code)]
struct Service;
declare_service!(Service);

impl jam_pvm_common::Service for Service {
	fn refine(
		id: ServiceId,
		payload: WorkPayload,
		_package_hash: WorkPackageHash,
		_context: RefineContext,
		_auth_code_hash: CodeHash,
	) -> WorkOutput {
		info!("This is Refine in the Test Service {id:x}h with payload len {}", payload.len());
		[&b"Hello "[..], payload.take().as_slice()].concat().into()
	}
	fn accumulate(_slot: Slot, id: ServiceId, items: Vec<AccumulateItem>) -> Option<Hash> {
		info!("This is Accumulate in the Test Service {id:x}h with {} items", items.len());
		for out in items.into_iter().filter_map(|x| x.result.ok()) {
			accumulate::set_storage(b"last", &out).expect("balance low");
		}
		None
	}
	fn on_transfer(slot: Slot, id: ServiceId, items: Vec<TransferRecord>) {
		items.into_iter().for_each(|i| {
			info!(
				"Transfer at {slot} from {:x}h to {id:x}h of {} memo {}",
				i.source, i.amount, i.memo
			);
			let msg = format!(
				"Transfer at {slot} from {:x}h to {id:x}h of {} memo {}",
				i.source, i.amount, i.memo,
			);
			accumulate::set_storage(b"lasttx", msg.as_bytes()).expect("balance low");
		});
	}
}
