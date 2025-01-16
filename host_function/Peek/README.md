# Host Peek  
- vm: The PVM that is currently executing the program.  
- m: The newly created PVM.  
- machine map: **m** in GP.

## hostPeekOK  
1. Successfully read data from m.memory.  
2. Successfully wrote data to vm.memory.  

## hostPeekOOB  
1. Failed to read data from m.memory or failed to write data to vm.memory.  

## hostPeekWHO  
1. Failed to retrieve m from the machine map.  