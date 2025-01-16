# Host Import  

## hostImportOK  
1. Successfully read import segments from initial import segments.  
2. Write import segments into memory.  

## hostImportOK_gt_wg
The size to be wrote is larger than wg (24 in our case), so only wg bytes will be wrote into memory.  
1. Successfully read import segments from initial import segments.  
2. Write import segments into memory.  

## hostImportOOB  
1. Successfully read import segments from initial import segments.  
2. Failed to write the import segments into memory due to a permission error.  

## hostImportNONE  
1. Length of import segment is lower than omega_7.  