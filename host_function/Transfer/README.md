# Host Transfer  

## hostTransferOK  
1. Read the transfer memo from memory.  
2. Successfully deducted the balance of **xs** and inserted a deferred transfer.  

## hostTransferOOB  
1. Failed to read the transfer memo from memory.  

## hostTransferWHO  
1. Failed to add deferred transfer due to receiver not existing.  

## hostTransferLOW  
1. Failed to add deferred transfer due to **g** being less than the receiver's **g**.  

## hostTransferHIGH  
1. Failed to add deferred transfer due to **g** being larger than **ϱ**.  

## hostTransferCASH  
1. Failed to add deferred transfer due to insufficient balance of **xs**.  