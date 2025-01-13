# Host Export  

## hostExportOK  
1. Successfully read **x** from memory.  
2. Successfully appended **x** to export segments and wrote the export segment index + length of export segments into omega_7.  

## hostExportOK_gt_wg
The size to be read is larger than wg (24 in our case), so only wg bytes will be read from memory.  
1. Successfully read **x** from memory.  
2. Successfully appended **x** to export segments and wrote the export segment index + length of export segments into omega_7.  

## hostExportOOB  
1. Failed to read **x** from memory due to a permission error.  

## hostExportFULL  
1. Export segment index + length of export segments exceeds the WM limit (2^11).  
