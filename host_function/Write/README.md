## hostWriteOK  
1. Successfully read service account **a** from the initial service account.  
2. Read the storage key from memory and compute **k**.  
3. Read the storage value from memory.  
4. Successfully updated the storage value.  
5. Write the length of the original storage value into **omega_7**.  

## hostWriteOOB  
1. Successfully read service account **a** from the initial service account.  
2. Failed to read the storage key from memory due to a permission error.  

## hostWriteFULL  
1. Successfully read service account **a** from the initial service account.  
2. Read the storage key from memory and compute **k**.  
3. Failed to update the storage value due to insufficient balance.  

## hostWriteNONE  
1. Successfully read service account **a** from the initial service account.  
2. Read the storage key from memory and compute **k**.  
3. Successfully deleted the storage based on the storage key.  
4. Write **NONE** to **omega_7** since the previous storage key no longer exists.  
