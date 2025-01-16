# Templates Overview

- [hostRefineTemplet](#hostRefineTemplet)
- [hostAccumulateTemplet](#hostAccumulateTemplet)
- [hostGeneralTemplet](#hostGeneralTemplet)

---

# hostRefineTemplet
## **Element Descriptions**

### **1. `name`**
- **Type**: String
- **Description**: The name of the template or configuration.  
```json
"hostRefineTemplet"
```

---

### **2. `initial-gas`**
- **Type**: $\mathbb{N}_G$
- **Description**: The initial gas
```json
10000
```

---

### **3. `initial-regs`**
- **Type**: $\left[\!\left[ \mathbb{N}_R \right]\!\right]_{13}$
- **Description**: The initial PVM register
```json
[
  4294901760, 4278059008, 0, 0, 0, 0, 0, 4278124544, 12, 0, 0, 0, 0
]
```

---

### **4. `initial-memory-permission`**
- **Type**: $\mathbb{M} \mathbf{.A}$
- **Description**: Defines memory access permissions.  
- **Fields**:
  - `start`: $N$
  - `length`: $N$
  - `mode`: $\mathbb{[0,1,2]}$
```json
[
  {
    "start": 4278124544,
    "length": 12,
    "mode": 2
  }
]
```

---

### **5. `initial-memory`**
- **Type**: $\mathbb{M} \mathbf{.V}$
- **Description**: The initial memory content values at specific addresses.  
- **Fields**:
  - `start`: $N$
  - `contents`: $\mathbb{Y}$
```json
[
  {
    "start": 4278124544,
    "contents": [10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
  }
]
```

---

### **6. `initial-refine-map`**
- **Type**: $\mathbb{N}\to M$
- **Description**: Initial Refine m map
- **Fields**:
  - `P`: $\mathbb{Y}$
  - `U`: $\mathbb{M}$
  - `I`: $N_R$
```json
{
  "0": {
    "P": [0, 1, 2, 3, 4],
    "U": {
      "start": 4278124544,
      "contents": [10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
    },
    "I": 0
  }
}
```

---

### **7. `initial-export-segment`**
- **Type**: $\left[\!\left[ \mathbb{Y} \right]\!\right]$
- **Description**: Initial export segment
```json
[[]]
```

---

### **8. `initial-import-segment`**
- **Type**: $\left[\!\left[ \mathbb{G} \right]\!\right]$
- **Description**: Initial import segment
```json
[[]]
```

---

### **9. `initial-export-segment-index`**
- **Type**: $N$
- **Description**: Initial export segment index
```json
0
```

---

### **10. `expected-gas`**
- **Type**: $N_G$
- **Description**: The expected gas after computation
```json
9990
```

---

### **11. `expected-regs`**
- **Type**: $\left[\!\left[ \mathbb{N}_R \right]\!\right]_{13}$
- **Description**: The PVM register after computation
```json
[
  4294901760, 4278059008, 0, 0, 0, 0, 0, 4278124544, 12, 0, 0, 0, 0
]
```

---

### **12. `expected-memory`**
- **Type**: $\mathbb{M} \mathbf{.V}$
- **Description**: The expected memory contents after computation.  
```json
[
  {
    "start": 4278124544,
    "contents": [10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
  }
]
```

---

### **13. `expected-refine-map`**
- **Type**: $\mathbb{N}\to M$
- **Description**: The expected refine-map after computation.  
- **Fields**:
  - `P`: $\mathbb{Y}$
  - `U`: $\mathbb{M}$
  - `I`: $N_R$
```json
{
  "0": {
    "P": [0, 1, 2, 3, 4],
    "U": {
      "start": 4278124544,
      "contents": [10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
    },
    "I": 0
  }
}
```

---

### **14. `expected-export-segment`**
- **Type**: $\left[\!\left[ \mathbb{Y} \right]\!\right]$
- **Description**: The expected state of export segments after computation.  
```json
[[]]
```
---

# hostAccumulateTemplet
## **Element Descriptions**

### **1. `name`**
- **Type**: String
- **Description**: The name of the template or configuration.  
```json
"hostAccumulateTemplet"
```

---

### **2. `initial-gas`**
- **Type**: $\mathbb{N}_G$
- **Description**: The initial gas amount.  
```json
10000
```

---

### **3. `initial-regs`**
- **Type**: $\left[\!\left[ \mathbb{N}_R \right]\!\right]_{13}$
- **Description**: The initial PVM register values.  
```json
[
  4294901760, 4278059008, 0, 0, 0, 0, 0, 4278124544, 12, 0, 0, 0, 0
]
```

---

### **4. `initial-memory-permission`**
- **Type**: $\mathbb{M} \mathbf{.A}$
- **Description**: Memory access permissions.  
- **Fields**:
  - `start`: $N$
  - `length`: $N$
  - `mode`: $\mathbb{[0,1,2]}$
```json
[
  {
    "Start": 4278124544,
    "Length": 12,
    "Mode": 2
  }
]
```

---

### **5. `initial-memory`**
- **Type**: $\mathbb{M} \mathbf{.V}$
- **Description**: The initial memory content values at specific addresses.  
- **Fields**:
  - `start`: $N$
  - `contents`: $\mathbb{Y}$
```json
[
  {
    "start": 4278124544,
    "contents": [10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
  }
]
```

---

### **6. `initial-xcontent-x`**
- **Type**: $\textbf{X}$
- **Description**: Initial x context
```json
{
  "D": {},
  "I": 1,
  "S": 0,
  "U": {
    "D": {
      "0": {
        "code_hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "balance": 10000,
        "min_item_gas": 100,
        "min_memo_gas": 200,
        "s_map": {
          "0x0000000000000000000000000000000000000000000000000000000000000000": [0, 1, 2, 3]
        },
        "l_map": {
          "0x1111111111111111111111111111111111111111111111111111111111111111": [0, 1, 2, 3]
        },
        "p_map": {
          "0x2222222222222222222222222222222222222222222222222222222222222222": [0, 1, 2, 3]
        }
      }
    },
    "upcoming_validators": null,
    "authorizations_pool": [null, null],
    "privileged_state": {
      "chi_m": 0,
      "chi_a": 0,
      "chi_v": 0,
      "chi_g": null
    }
  },
  "T": []
}
```

---

### **7. `initial-xcontent-y`**
- **Type**: $\textbf{X}$
- **Description**: Initial y context
```json
{
  "D": null,
  "I": 0,
  "S": 0,
  "U": null,
  "T": null
}
```

---

### **8. `initial-timeslot`**
- **Type**: $N$
- **Description**: The initial timeslot. 
```json
0
```

---

### **9. `expected-gas`**
- **Type**: $\mathbb{N}_G$
- **Description**: The gas amount after computation.  
```json
9990
```

---

### **10. `expected-regs`**
- **Type**: $\left[\!\left[ \mathbb{N}_R \right]\!\right]_{13}$
- **Description**: The PVM register values after computation.  
```json
[
  4294901760, 4278059008, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0
]
```

---

### **11. `expected-memory`**
- **Type**: $\mathbb{M} \mathbf{.V}$
- **Description**: The memory content values after computation.  
```json
[
  {
    "start": 4278124544,
    "contents": [10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
  }
]
```

---

### **12. `expected-xcontent-x`**
- **Type**: $\textbf{X}$
- **Description**: The expected x content for after computation.  
```json
{
  "D": null,
  "I": 0,
  "S": 0,
  "U": null,
  "T": [
    {
      "sender_index": 0,
      "receiver_index": 0,
      "amount": 0,
      "memo": [0, 1, 2, 3],
      "gas_limit": 0
    }
  ]
}
```

---

### **13. `expected-xcontent-y`**
- **Type**: $\textbf{X}$
- **Description**: The expected y content for after computation.  
```json
{
  "D": null,
  "I": 0,
  "S": 0,
  "U": null,
  "T": null
}
```

# hostGeneralTemplet
## **Element Descriptions**

### **1. `name`**
- **Type**: String
- **Description**: The name of the template or configuration.  
```json
"hostGeneralTemplet"
```

---

### **2. `initial-gas`**
- **Type**: $\mathbb{N}_G$
- **Description**: The initial gas amount.  
```json
10000
```

---

### **3. `initial-regs`**
- **Type**: $\left[\!\left[ \mathbb{N}_R \right]\!\right]_{13}$
- **Description**: The initial PVM register values.  
```json
[
  4294901760,
  4278059008,
  0,
  0,
  0,
  0,
  0,
  4278124544,
  12,
  0,
  0,
  0,
  0
]
```

---

### **4. `initial-memory-permission`**
- **Type**: $\mathbb{M} \mathbf{.A}$
- **Description**: Memory access permissions.  
- **Fields**:
  - `start`: $N$
  - `length`: $N$
  - `mode`: $\mathbb{[0,1,2]}$
```json
[
  {
    "Start": 4278124544,
    "Length": 12,
    "Mode": 2
  }
]
```

---

### **5. `initial-memory`**
- **Type**: $\mathbb{M} \mathbf{.V}$
- **Description**: The initial memory content values at specific addresses.  
- **Fields**:
  - `start`: $N$
  - `contents`: $\mathbb{Y}$
```json
[
  {
    "start": 4278124544,
    "contents": [10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
  }
]
```

---

### **6. `initial-service-account`**
- **Type**: $\mathbb{A}$
- **Description**: Initial service account
```json
{
  "service_index": 1,
  "code_hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "balance": 1111,
  "min_item_gas": 2222,
  "min_memo_gas": 3333,
  "code_size": 0,
  "s_map": {
    "0x0000000000000000000000000000000000000000000000000000000000000000": [0, 1, 2, 3]
  },
  "l_map": {
    "0x1111111111111111111111111111111111111111111111111111111111111111": [0, 1, 2, 3]
  },
  "p_map": {
    "0x2222222222222222222222222222222222222222222222222222222222222222": [0, 1, 2, 3]
  }
}
```

---

### **7. `initial-service-index`**
- **Type**: $N$
- **Description**: Initial service index
```json
0
```

---

### **8. `initial-delta`**
- **Type**: $\mathbb{N_s}\to \mathbb{A}$
- **Description**: Initial delta a map of service index and service.
```json
{
  "0": {
    "service_index": 1,
    "code_hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "balance": 1111,
    "min_item_gas": 2222,
    "min_memo_gas": 3333,
    "code_size": 0,
    "s_map": {
      "0x0000000000000000000000000000000000000000000000000000000000000000": [0, 1, 2, 3]
    },
    "l_map": {
      "0x1111111111111111111111111111111111111111111111111111111111111111": [0, 1, 2, 3]
    },
    "p_map": {
      "0x2222222222222222222222222222222222222222222222222222222222222222": [0, 1, 2, 3]
    }
  }
}
```

---

### **9. `expected-gas`**
- **Type**: $\mathbb{N}_G$
- **Description**: The gas amount after computation.  
```json
9990
```

---

### **10. `expected-regs`**
- **Type**: $\left[\!\left[ \mathbb{N}_R \right]\!\right]_{13}$
- **Description**: The PVM register values after computation.  
```json
[
  4294901760,
  4278059008,
  0,
  0,
  0,
  0,
  0,
  4278124544,
  12,
  0,
  0,
  0,
  0
]
```

---

### **11. `expected-memory`**
- **Type**: $\mathbb{M} \mathbf{.V}$
- **Description**: The memory content values after computation.  
```json
[
  {
    "start": 4278124544,
    "contents": [10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
  }
]
```

---

### **12. `expected-service-account`**
- **Type**: $\mathbb{A}$
- **Description**: Represents the expected state of the service account after computation.  
```json
{
  "service_index": 1,
  "code_hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "balance": 1111,
  "min_item_gas": 2222,
  "min_memo_gas": 3333,
  "code_size": 0,
  "s_map": {
    "0x0000000000000000000000000000000000000000000000000000000000000000": [0, 1, 2, 3]
  },
  "l_map": {
    "0x1111111111111111111111111111111111111111111111111111111111111111": [0, 1, 2, 3]
  },
  "p_map": {
    "0x2222222222222222222222222222222222222222222222222222222222222222": [0, 1, 2, 3]
  }
}
```