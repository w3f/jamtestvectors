# Host Eject  

## hostEjectOK  
1. Read the preimage blob hash from memory.  
2. Successfully retrieve service **d** based on the service index d.
3. Successfully remove service **d** from x.u.d and insert service **s** into x.u.d.  

## hostEjectOOB  
1. Failed to read the preimage blob hash from memory.  

## hostEjectWHO  
1. Read the preimage blob hash from memory.  
2. Failed to retrieve **d** with the corresponding d because d equals xs.  

## hostEjectHUH  
1. Read the preimage blob hash from memory.  
2. Successfully retrieve service **d** based on the service index d.
3. Failed to update x.u.d because **d.i** ≠ 2.  
