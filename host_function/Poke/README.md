# Host Poke  
- vm: The PVM that is currently executing the program.  
- m: The newly created PVM.  
- machine map: **m** in GP.

## hostPokeOK 
1. Successfully read data from vm.memory.   
2. Successfully wrote data to m.memory.  

## hostPokeOOB  
1. Failed to write data to m.memory or failed to read data from vm.memory.  

## hostPokeWHO  
1. Failed to retrieve m from the machine map.  
