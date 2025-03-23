# Host Lookup

## hostLookupOK_s
1. Successfully read service account **s** from initial service account.  
2. Read the preimage blob hash from memory and compute h.  
3. Successfully read the preimage blob.  
4. Write the preimage blob into memory.  
5. Write the length of the preimage blob into omega_7.  

## hostLookupOK_d_omega_7
1. Successfully read service account from delta with service index = omega_7.  
2. Read the preimage blob hash from memory and compute h.  
3. Successfully read the preimage blob.  
4. Write the preimage blob into memory.  
5. Write the length of the preimage blob into omega_7.  

## hostLookupOOB
1. Successfully read service index = 0 from delta.  
2. Failed to read the preimage blob hash from memory due to a permission error.  

## hostLookupNONE
1. Successfully read service index = 0 from delta.  
2. Read the preimage blob hash from memory and compute h.  
3. Failed to read the preimage blob due to an invalid preimage blob key.  