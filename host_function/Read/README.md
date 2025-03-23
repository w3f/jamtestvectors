# Host Read

## hostReadOK_s
1. Successfully read service account **s** from initial service account.  
2. Read the storage key from memory and compute k.  
3. Successfully read the storage value.  
4. Write the storage value into memory.  
5. Write the length of the storage value into omega_7.  

## hostReadOK_d_omega7
1. Successfully read service account from initial delta with service index = omega_7.  
2. Read the storage key from memory and compute k.  
3. Successfully read the storage value.  
4. Write the storage value into memory.  
5. Write the length of the storage value into omega_7.  

## hostReadOOB
1. Successfully read service account **s** from initial service account.  
2. Failed to read the storage key from memory due to a permission error.  

## hostReadNONE
1. Successfully read service account **s** from initial service account.  
2. Read the storage key from memory and compute k.   
3. Failed to read the storage value due to an invalid storage key.