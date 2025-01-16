# Host Invoke  
- m: The newly created PVM.  
- machine map: **m** in GP.  

## hostInvokeHALT  
- m program: [0, 0, 5, 61, 7, 0, 0, 2, 1] (u32 [0x20000] = a0)
1. Successfully read gas, registers from memory and retrieved m.  
2. Successfully executed m's program and caused regular HALT.

## hostInvokeOOB  
1. Failed to read m's gas and registers from memory.

## hostInvokeWHO  
1. Failed to retrieve m from the machine map.  

## hostInvokeHOST  
- m program: [0, 0, 1, 10, 1] (call host gas)
1. Successfully read gas, registers from memory and retrieved m.  
2. Successfully executed m's program and caused HOST.

## hostInvokeFAULT
- m program: [0, 0, 5, 61, 7, 0, 0, 2, 1] (u32 [0x20000] = a0)
1. Successfully read gas, registers from memory and retrieved m.  
2. Failed to execute m's program due to a memory permission error and caused FAULT.

## hostInvokeOOG 
- m program: [0, 0, 1, 10, 1] (call host gas)
1. Successfully read gas, registers from memory and retrieved m.  
2. Failed to execute m's program due to insufficient gas and caused OOG.

## hostInvokePANIC 
- m program: [0, 0, 1, 0, 1] (call trap)
1. Successfully read gas, registers from memory and retrieved m.  
2. Successfully executed m's program and caused PANIC.  
