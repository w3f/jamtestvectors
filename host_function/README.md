# Host function test vectors (Based on GP-0.5.4)

This set of test vectors is primarily used to test the host functions of GP-B.6, B.7, and B.8.  

The test vectors mainly (only) verify whether the changes to all parameters before and after the execution of the host functions meet expectations.

For more details about the test vectors, please refer to the note section below.

## B.6 General Functions
- [ ] Gas
  - [ ] OK  
- [x] Lookup  
  - [x] OK_s
  - [x] OK_d_omega7 
  - [x] OOB  
  - [x] NONE  
- [x] Read  
  - [x] OK_s
  - [x] OK_d_omega7
  - [x] OOB  
  - [x] NONE  
- [x] Write  
  - [x] OK  
  - [x] OOB  
  - [x] NONE
  - [x] FULL  
- [x] Info  
  - [x] OK  
  - [x] OOB  
  - [x] NONE  

## B.7 Accumulate Functions
- [ ] Bless  
  - [ ] OK  
  - [ ] OOB  
  - [ ] WHO  
- [ ] Assign 
  - [ ] OK  
  - [ ] OOB  
  - [ ] CORE
- [ ] Designate 
  - [ ] OK  
  - [ ] OOB 
- [ ] Checkpoint
  - [ ] OK
- [x] New  
  - [x] OK  
  - [x] OOB  
  - [x] CASH  
- [x] Upgrade  
  - [x] OK  
  - [x] OOB  
- [x] Transfer  
  - [x] OK  
  - [x] OOB  
  - [x] WHO  
  - [x] CASH  
  - [x] LOW  
- [x] Eject  
  - [x] OK  
  - [x] OOB  
  - [x] WHO  
  - [x] HUH  
- [x] Query  
  - [x] OK_0_timeslots 
  - [x] OK_1_timeslots 
  - [x] OK_2_timeslots 
  - [x] OK_3_timeslots   
  - [x] OOB  
  - [x] NONE  
- [x] Solicit  
  - [x] OK_no_timeslots 
  - [x] OK_2_timeslots 
  - [x] OOB  
  - [x] FULL  
  - [x] HUH  
- [x] Forget  
  - [x] OK_0_timeslots  
  - [x] OK_1_timeslots   
  - [x] OK_2_timeslots   
  - [x] OK_3_timeslots    
  - [x] OOB  
  - [x] HUH  
- [x] Yield  
  - [x] OK  
  - [x] OOB    


## B.8 Refine Functions
- [x] Historical_lookup  
  - [x] OK_d_s 
  - [x] OK_d_omega7
  - [x] OOB  
  - [x] NONE  
- [x] Import  
  - [x] OK 
  - [x] OK_gt_wg  
  - [x] OOB  
  - [x] NONE  
- [x] Export  
  - [x] OK  
  - [x] OK_gt_wg  
  - [x] OOB  
  - [x] FULL  
- [x] Machine  
  - [x] OK  
  - [x] OOB  
- [x] Peek  
  - [x] OK  
  - [x] OOB  
  - [x] WHO  
- [x] Poke  
  - [x] OK  
  - [x] OOB  
  - [x] WHO  
- [x] Zero  
  - [x] OK  
  - [x] OOB  
  - [x] WHO  
- [x] Void  
  - [x] OK  
  - [x] OOB  
  - [x] WHO  
- [x] Invoke  
  - [x] HALT  
  - [x] OOB 
  - [x] OOG
  - [x] WHO  
  - [x] HOST  
  - [x] FAULT  
  - [x] PANIC
- [x] Expunge  
  - [x] OK  
  - [x] WHO  

---

# Note

## Test Case Structure
All parameters used by the host functions will be provided in **JSON** format, following the definitions in GP.

## Test Case Prefix
In all test cases, variables with the prefix **initial** represent the state of the variable **before execution**, while those with the prefix **expected** represent the state of the variable **after execution**.

## Service Account Dictionaries
**Storage** and **Preimage** dictionaries are stored according to the definitions in GP, but the **Lookup** dictionary is slightly different because its key contains two elements and cannot be directly stored in JSON. The calculation process for each type of key is as follows:  

---

### Storage Dictionary
**Assumption**  
- Service index = 0  
- Raw storage key = `0x00000000`  
- Storage value = `0x00000000`  

---

#### Calculation Formula: `H(E4(s) ⌢ µko⋅⋅⋅+kz)`
Convert the service index to **little endian** 4 bytes, concatenate it with the storage key, and apply the **blake2b** hash.

- `E4(s) = E4(0) = 0x00000000`  
- `µko⋅⋅⋅+kz = 0x00000000`  
- `H(E4(s) ⌢ µko⋅⋅⋅+kz) = H(0x0000000000000000) =`  
  **`0x81e47a19e6b29b0a65b9591762ce5143ed30d0261e5d24a3201752506b20f15c`**  

#### Example of JSON Format:
```json
"s_map": {
  "0x81e47a19e6b29b0a65b9591762ce5143ed30d0261e5d24a3201752506b20f15c": [
    0,
    0,
    0,
    0
  ]
}
```

---

### Preimage Blob Dictionary
**Assumption**   
- Preimage Blob = `[15, 15, 14, 14, 13, 13, 12, 12, 11, 11, 10, 10]`  
  (i.e., `0xffffeeeeddddccccbbbbaaaa`)  
- `Preimage Blob Hash =`  
  **`H(0xffffeeeeddddccccbbbbaaaa) = 0x0be802c135a8c671aa22d990fbb26116d9844a458d89d05aa013272a64160337`**  

---

#### Calculation Formula: `H(µho⋅⋅⋅+32)`
Hash the **Preimage Blob Hash** again.

- `H(0x0be802c135a8c671aa22d990fbb26116d9844a458d89d05aa013272a64160337) =`  
  **`0x3ee347e16fb6594af50ce1cc49996bb7a5e39c7d60d5371eca76dc72785cc5ad`**  

#### Example of JSON Format:
```json
"p_map": {
  "0x3ee347e16fb6594af50ce1cc49996bb7a5e39c7d60d5371eca76dc72785cc5ad": [
    15,
    15,
    14,
    14,
    13,
    13,
    12,
    12,
    11,
    11,
    10,
    10
  ]
}
```

---

### Preimage Lookup Dictionary
The key of the preimage lookup contains two elements:  
- The preimage blob hash  
- The preimage blob length  

The value contains one element:  
- The timeslots  

Since a JSON key can only be a string, only the preimage blob hash is stored as the key. The preimage blob length is stored within the corresponding value. As a result, the modified key contains only one element:  
- The preimage blob hash  

The modified value contains two elements:  
- The preimage blob length  
- The timeslots  

---

**Assumption**  
- Preimage Blob = `[15, 15, 14, 14, 13, 13, 12, 12, 11, 11, 10, 10]`  
- `Preimage Blob Hash = 0x0be802c135a8c671aa22d990fbb26116d9844a458d89d05aa013272a64160337`  
- `Preimage Blob Length = 12`  
- `Timeslots = [100]`  

---

#### Original Preimage Lookup
`{Preimage Blob Hash, Preimage Blob Length} -> Timeslots` =   
  **`{0x0be802c135a8c671aa22d990fbb26116d9844a458d89d05aa013272a64160337, 12} -> [100]`**  

#### Modified Preimage Lookup
`Preimage Blob Hash -> {Preimage Blob Length, Timeslots}` =   
  **`0x0be802c135a8c671aa22d990fbb26116d9844a458d89d05aa013272a64160337 -> {12, [100]}`**  

---

#### Example of JSON Format:
```json
"l_map": {
  "0x0be802c135a8c671aa22d990fbb26116d9844a458d89d05aa013272a64160337": {
    "l": 12,
    "t": [
      100
    ]
  }
}
```