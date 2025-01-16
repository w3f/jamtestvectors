# Host Historical Lookup  

## hostHistoricalLookupOK_d_s 
omega7 = NONE, so the service index is read as the initial service index (s) from delta.  
1. Successfully read service index = 0 from delta.  
2. Read the preimage blob hash from memory and compute **h**.  
3. Successfully read the preimage blob from the historical lookup function **Λ**.  
4. Write the preimage blob into memory.  
5. Write the length of the preimage blob into **omega_7**.  

## hostHistoricalLookupOK_d_omega7 
omega7 ≠ NONE, so the service index is read as omega7 from delta.  
1. Successfully read service index = 0 from delta.  
2. Read the preimage blob hash from memory and compute **h**.  
3. Successfully read the preimage blob from the historical lookup function **Λ**.  
4. Write the preimage blob into memory.  
5. Write the length of the preimage blob into **omega_7**.  

## hostHistoricalLookupOOB  
omega7 ≠ NONE, so the service index is read as omega7 from delta.  
1. Successfully read service index = 0 from delta.  
2. Failed to read the preimage blob hash from memory because of a permission error.  

## hostHistoricalLookupNONE  
omega7 ≠ NONE, so the service index is read as omega7 from delta.  
1. Successfully read service index = 0 from delta.  
2. Read the preimage blob hash from memory and compute **h**.  
3. Failed to read the preimage blob from the historical lookup function **Λ** because of an invalid timeslot.  
