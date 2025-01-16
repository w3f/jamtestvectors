# Host Void  
- m: The newly created PVM.  
- machine map: **m** in GP.  

## hostVoidOK  
1. Successfully retrieved m.  
2. Successfully set m's page value to [0,0,...] and set m's page access to inaccessible.  

## hostVoidOOB  
1. Pages from p to (p+c) are already inaccessible, leading to an OOB error.  

## hostVoidWHO  
1. Failed to retrieve m from the machine map.  