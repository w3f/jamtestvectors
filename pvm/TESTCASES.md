# Testcases

This file contains a human-readable index of all of the testcases,
along with their disassemblies and other relevant information.


## gas_basic_consume_all

```
      :                          @0
     0: 52 00                    r0 = r0
     2:                          invalid
```

Program should end with: trap

Final value of the program counter: 2

Gas consumed: 2 -> 0


## inst_add

Initial non-zero registers:
   * r7 = 0x1
   * r8 = 0x2

```
      :                          @0
     0: 08 87 09                 r9 = r7 + r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x3 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_add_imm

Initial non-zero registers:
   * r7 = 0x1

```
      :                          @0
     0: 02 79 02                 r9 = r7 + 0x2
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x3 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_add_with_overflow

Initial non-zero registers:
   * r7 = 0xffffffff
   * r8 = 0x2

```
      :                          @0
     0: 08 87 09                 r9 = r7 + r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_and

Initial non-zero registers:
   * r7 = 0x5
   * r8 = 0x3

```
      :                          @0
     0: 17 87 09                 r9 = r7 & r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_and_imm

Initial non-zero registers:
   * r7 = 0x5

```
      :                          @0
     0: 12 79 03                 r9 = r7 & 0x3
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_branch_eq_imm_nok

```
      :                          @0
     0: 04 07 d2 04              r7 = 0x4d2
     4: 07 27 d3 04 06           jump 10 if r7 == 1235
      :                          @1
     9: 00                       trap
      :                          @2
    10: 04 07 ef be ad de        r7 = 0xdeadbeef
    16:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0x4d2 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 9

Gas consumed: 10000 -> 9997


## inst_branch_eq_imm_ok

```
      :                          @0
     0: 04 07 d2 04              r7 = 0x4d2
     4: 07 27 d2 04 06           jump 10 if r7 == 1234
      :                          @1
     9: 00                       trap
      :                          @2
    10: 04 07 ef be ad de        r7 = 0xdeadbeef
    16:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap

Final value of the program counter: 16

Gas consumed: 10000 -> 9996


## inst_branch_eq_nok

```
      :                          @0
     0: 04 07 d2 04              r7 = 0x4d2
     4: 04 08 d3 04              r8 = 0x4d3
     8: 18 87 04                 jump 12 if r7 == r8
      :                          @1
    11: 00                       trap
      :                          @2
    12: 04 07 ef be ad de        r7 = 0xdeadbeef
    18:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0x4d2 (initially was 0x0)
   * r8 = 0x4d3 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 11

Gas consumed: 10000 -> 9996


## inst_branch_eq_ok

```
      :                          @0
     0: 04 07 d2 04              r7 = 0x4d2
     4: 04 08 d2 04              r8 = 0x4d2
     8: 18 87 04                 jump 12 if r7 == r8
      :                          @1
    11: 00                       trap
      :                          @2
    12: 04 07 ef be ad de        r7 = 0xdeadbeef
    18:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)
   * r8 = 0x4d2 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 18

Gas consumed: 10000 -> 9995


## inst_branch_greater_or_equal_signed_imm_nok

```
      :                          @0
     0: 04 07 f6                 r7 = 0xfffffff6
     3: 2d 17 0a 05              jump 8 if r7 >=s 10
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xfffffff6 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 7

Gas consumed: 10000 -> 9997


## inst_branch_greater_or_equal_signed_imm_ok

```
      :                          @0
     0: 04 07 0a                 r7 = 0xa
     3: 2d 17 f6 05              jump 8 if r7 >=s 4294967286
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap

Final value of the program counter: 14

Gas consumed: 10000 -> 9996


## inst_branch_greater_or_equal_signed_nok

```
      :                          @0
     0: 04 07 f6                 r7 = 0xfffffff6
     3: 04 08 0a                 r8 = 0xa
     6: 2b 87 04                 jump 10 if r7 >=s r8
      :                          @1
     9: 00                       trap
      :                          @2
    10: 04 07 ef be ad de        r7 = 0xdeadbeef
    16:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xfffffff6 (initially was 0x0)
   * r8 = 0xa (initially was 0x0)

Program should end with: trap

Final value of the program counter: 9

Gas consumed: 10000 -> 9996


## inst_branch_greater_or_equal_signed_ok

```
      :                          @0
     0: 04 07 0a                 r7 = 0xa
     3: 04 08 f6                 r8 = 0xfffffff6
     6: 2b 87 04                 jump 10 if r7 >=s r8
      :                          @1
     9: 00                       trap
      :                          @2
    10: 04 07 ef be ad de        r7 = 0xdeadbeef
    16:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)
   * r8 = 0xfffffff6 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 16

Gas consumed: 10000 -> 9995


## inst_branch_greater_or_equal_unsigned_imm_nok

```
      :                          @0
     0: 04 07 0a                 r7 = 0xa
     3: 34 17 f6 05              jump 8 if r7 >=u 4294967286
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xa (initially was 0x0)

Program should end with: trap

Final value of the program counter: 7

Gas consumed: 10000 -> 9997


## inst_branch_greater_or_equal_unsigned_imm_ok

```
      :                          @0
     0: 04 07 f6                 r7 = 0xfffffff6
     3: 34 17 0a 05              jump 8 if r7 >=u 10
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap

Final value of the program counter: 14

Gas consumed: 10000 -> 9996


## inst_branch_greater_or_equal_unsigned_nok

```
      :                          @0
     0: 04 07 0a                 r7 = 0xa
     3: 04 08 f6                 r8 = 0xfffffff6
     6: 29 87 04                 jump 10 if r7 >=u r8
      :                          @1
     9: 00                       trap
      :                          @2
    10: 04 07 ef be ad de        r7 = 0xdeadbeef
    16:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xa (initially was 0x0)
   * r8 = 0xfffffff6 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 9

Gas consumed: 10000 -> 9996


## inst_branch_greater_or_equal_unsigned_ok

```
      :                          @0
     0: 04 07 f6                 r7 = 0xfffffff6
     3: 04 08 0a                 r8 = 0xa
     6: 29 87 04                 jump 10 if r7 >=u r8
      :                          @1
     9: 00                       trap
      :                          @2
    10: 04 07 ef be ad de        r7 = 0xdeadbeef
    16:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)
   * r8 = 0xa (initially was 0x0)

Program should end with: trap

Final value of the program counter: 16

Gas consumed: 10000 -> 9995


## inst_branch_greater_signed_imm_nok

```
      :                          @0
     0: 04 07 f6                 r7 = 0xfffffff6
     3: 35 17 0a 05              jump 8 if r7 >s 10
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xfffffff6 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 7

Gas consumed: 10000 -> 9997


## inst_branch_greater_signed_imm_ok

```
      :                          @0
     0: 04 07 0a                 r7 = 0xa
     3: 35 17 f6 05              jump 8 if r7 >s 4294967286
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap

Final value of the program counter: 14

Gas consumed: 10000 -> 9996


## inst_branch_greater_unsigned_imm_nok

```
      :                          @0
     0: 04 07 0a                 r7 = 0xa
     3: 32 17 f6 05              jump 8 if r7 >u 4294967286
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xa (initially was 0x0)

Program should end with: trap

Final value of the program counter: 7

Gas consumed: 10000 -> 9997


## inst_branch_greater_unsigned_imm_ok

```
      :                          @0
     0: 04 07 f6                 r7 = 0xfffffff6
     3: 32 17 0a 05              jump 8 if r7 >u 10
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap

Final value of the program counter: 14

Gas consumed: 10000 -> 9996


## inst_branch_less_or_equal_signed_imm_nok

```
      :                          @0
     0: 04 07 0a                 r7 = 0xa
     3: 2e 17 f6 05              jump 8 if r7 <=s 4294967286
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xa (initially was 0x0)

Program should end with: trap

Final value of the program counter: 7

Gas consumed: 10000 -> 9997


## inst_branch_less_or_equal_signed_imm_ok

```
      :                          @0
     0: 04 07 f6                 r7 = 0xfffffff6
     3: 2e 17 0a 05              jump 8 if r7 <=s 10
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap

Final value of the program counter: 14

Gas consumed: 10000 -> 9996


## inst_branch_less_or_equal_unsigned_imm_nok

```
      :                          @0
     0: 04 07 f6                 r7 = 0xfffffff6
     3: 3b 17 0a 05              jump 8 if r7 <=u 10
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xfffffff6 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 7

Gas consumed: 10000 -> 9997


## inst_branch_less_or_equal_unsigned_imm_ok

```
      :                          @0
     0: 04 07 0a                 r7 = 0xa
     3: 3b 17 f6 05              jump 8 if r7 <=u 4294967286
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap

Final value of the program counter: 14

Gas consumed: 10000 -> 9996


## inst_branch_less_signed_imm_nok

```
      :                          @0
     0: 04 07 0a                 r7 = 0xa
     3: 20 17 f5 05              jump 8 if r7 <s 4294967285
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xa (initially was 0x0)

Program should end with: trap

Final value of the program counter: 7

Gas consumed: 10000 -> 9997


## inst_branch_less_signed_imm_ok

```
      :                          @0
     0: 04 07 f6                 r7 = 0xfffffff6
     3: 20 17 0a 05              jump 8 if r7 <s 10
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap

Final value of the program counter: 14

Gas consumed: 10000 -> 9996


## inst_branch_less_signed_nok

```
      :                          @0
     0: 04 07 0a                 r7 = 0xa
     3: 04 08 f6                 r8 = 0xfffffff6
     6: 30 87 04                 jump 10 if r7 <s r8
      :                          @1
     9: 00                       trap
      :                          @2
    10: 04 07 ef be ad de        r7 = 0xdeadbeef
    16:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xa (initially was 0x0)
   * r8 = 0xfffffff6 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 9

Gas consumed: 10000 -> 9996


## inst_branch_less_signed_ok

```
      :                          @0
     0: 04 07 f6                 r7 = 0xfffffff6
     3: 04 08 0a                 r8 = 0xa
     6: 30 87 04                 jump 10 if r7 <s r8
      :                          @1
     9: 00                       trap
      :                          @2
    10: 04 07 ef be ad de        r7 = 0xdeadbeef
    16:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)
   * r8 = 0xa (initially was 0x0)

Program should end with: trap

Final value of the program counter: 16

Gas consumed: 10000 -> 9995


## inst_branch_less_unsigned_imm_nok

```
      :                          @0
     0: 04 07 f6                 r7 = 0xfffffff6
     3: 2c 17 0a 05              jump 8 if r7 <u 10
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xfffffff6 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 7

Gas consumed: 10000 -> 9997


## inst_branch_less_unsigned_imm_ok

```
      :                          @0
     0: 04 07 0a                 r7 = 0xa
     3: 2c 17 f6 05              jump 8 if r7 <u 4294967286
      :                          @1
     7: 00                       trap
      :                          @2
     8: 04 07 ef be ad de        r7 = 0xdeadbeef
    14:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap

Final value of the program counter: 14

Gas consumed: 10000 -> 9996


## inst_branch_less_unsigned_nok

```
      :                          @0
     0: 04 07 f6                 r7 = 0xfffffff6
     3: 04 08 0a                 r8 = 0xa
     6: 2f 87 04                 jump 10 if r7 <u r8
      :                          @1
     9: 00                       trap
      :                          @2
    10: 04 07 ef be ad de        r7 = 0xdeadbeef
    16:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xfffffff6 (initially was 0x0)
   * r8 = 0xa (initially was 0x0)

Program should end with: trap

Final value of the program counter: 9

Gas consumed: 10000 -> 9996


## inst_branch_less_unsigned_ok

```
      :                          @0
     0: 04 07 0a                 r7 = 0xa
     3: 04 08 f6                 r8 = 0xfffffff6
     6: 2f 87 04                 jump 10 if r7 <u r8
      :                          @1
     9: 00                       trap
      :                          @2
    10: 04 07 ef be ad de        r7 = 0xdeadbeef
    16:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)
   * r8 = 0xfffffff6 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 16

Gas consumed: 10000 -> 9995


## inst_branch_not_eq_imm_nok

```
      :                          @0
     0: 04 07 d2 04              r7 = 0x4d2
     4: 0f 27 d2 04 06           jump 10 if r7 != 1234
      :                          @1
     9: 00                       trap
      :                          @2
    10: 04 07 ef be ad de        r7 = 0xdeadbeef
    16:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0x4d2 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 9

Gas consumed: 10000 -> 9997


## inst_branch_not_eq_imm_ok

```
      :                          @0
     0: 04 07 d2 04              r7 = 0x4d2
     4: 0f 27 d3 04 06           jump 10 if r7 != 1235
      :                          @1
     9: 00                       trap
      :                          @2
    10: 04 07 ef be ad de        r7 = 0xdeadbeef
    16:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap

Final value of the program counter: 16

Gas consumed: 10000 -> 9996


## inst_branch_not_eq_nok

```
      :                          @0
     0: 04 07 d2 04              r7 = 0x4d2
     4: 04 08 d2 04              r8 = 0x4d2
     8: 1e 87 04                 jump 12 if r7 != r8
      :                          @1
    11: 00                       trap
      :                          @2
    12: 04 07 ef be ad de        r7 = 0xdeadbeef
    18:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0x4d2 (initially was 0x0)
   * r8 = 0x4d2 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 11

Gas consumed: 10000 -> 9996


## inst_branch_not_eq_ok

```
      :                          @0
     0: 04 07 d2 04              r7 = 0x4d2
     4: 04 08 d3 04              r8 = 0x4d3
     8: 1e 87 04                 jump 12 if r7 != r8
      :                          @1
    11: 00                       trap
      :                          @2
    12: 04 07 ef be ad de        r7 = 0xdeadbeef
    18:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)
   * r8 = 0x4d3 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 18

Gas consumed: 10000 -> 9995


## inst_cmov_if_zero_imm_nok

Initial non-zero registers:
   * r10 = 0x1

```
      :                          @0
     0: 55 a7 64                 r7 = 100 if r10 == 0
     3:                          invalid
```

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_cmov_if_zero_imm_ok

```
      :                          @0
     0: 55 a7 64                 r7 = 100 if r10 == 0
     3:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0x64 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_cmov_if_zero_nok

Initial non-zero registers:
   * r8 = 0x64
   * r10 = 0x1

```
      :                          @0
     0: 53 a8 07                 r7 = r8 if r10 == 0
     3:                          invalid
```

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_cmov_if_zero_ok

Initial non-zero registers:
   * r8 = 0x64

```
      :                          @0
     0: 53 a8 07                 r7 = r8 if r10 == 0
     3:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0x64 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_div_signed

Initial non-zero registers:
   * r7 = 0x80000010
   * r8 = 0x7

```
      :                          @0
     0: 40 87 09                 r9 = r7 /s r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0xedb6db70 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_div_signed_by_zero

Initial non-zero registers:
   * r7 = 0x80000010

```
      :                          @0
     0: 40 87 09                 r9 = r7 /s r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0xffffffff (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_div_signed_with_overflow

Initial non-zero registers:
   * r7 = 0x80000000
   * r8 = 0xffffffff

```
      :                          @0
     0: 40 87 09                 r9 = r7 /s r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x80000000 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_div_unsigned

Initial non-zero registers:
   * r7 = 0x80000010
   * r8 = 0x7

```
      :                          @0
     0: 44 87 09                 r9 = r7 /u r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x12492494 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_div_unsigned_by_zero

Initial non-zero registers:
   * r7 = 0x80000010

```
      :                          @0
     0: 44 87 09                 r9 = r7 /u r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0xffffffff (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_div_unsigned_with_overflow

Initial non-zero registers:
   * r7 = 0x80000000
   * r8 = 0xffffffff
   * r9 = 0x1234

```
      :                          @0
     0: 44 87 09                 r9 = r7 /u r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x0 (initially was 0x1234)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_fallthrough

```
      :                          @0
     0: 11                       fallthrough
      :                          @1
     1:                          invalid
```

Program should end with: trap

Final value of the program counter: 1

Gas consumed: 10000 -> 9998


## inst_jump

```
      :                          @0
     0: 04 07 d2 04              r7 = 0x4d2
     4: 05 03                    jump 7
      :                          @1
     6: 00                       trap
      :                          @2
     7: 04 07 ef be ad de        r7 = 0xdeadbeef
    13:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap

Final value of the program counter: 13

Gas consumed: 10000 -> 9996


## inst_load_i16

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20002 (0x2 bytes) = [0x81, 0x82]

```
      :                          @0
     0: 42 07 00 00 02           r7 = i16 [0x20000]
     5:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xffff8281 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 5

Gas consumed: 10000 -> 9998


## inst_load_i8

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20001 (0x1 bytes) = [0x81]

```
      :                          @0
     0: 4a 07 00 00 02           r7 = i8 [0x20000]
     5:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xffffff81 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 5

Gas consumed: 10000 -> 9998


## inst_load_imm

```
      :                          @0
     0: 04 07 ef be ad de        r7 = 0xdeadbeef
     6:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap

Final value of the program counter: 6

Gas consumed: 10000 -> 9998


## inst_load_imm_and_jump

```
      :                          @0
     0: 06 27 d2 04 06           r7 = 1234, jump 6
      :                          @1
     5: 00                       trap
      :                          @2
     6: 04 08 ef be ad de        r8 = 0xdeadbeef
    12:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0x4d2 (initially was 0x0)
   * r8 = 0xdeadbeef (initially was 0x0)

Program should end with: trap

Final value of the program counter: 12

Gas consumed: 10000 -> 9997


## inst_load_indirect_i16_with_offset

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x81, 0x82, 0x83, 0x84]

Initial non-zero registers:
   * r7 = 0x20000

```
      :                          @0
     0: 21 78 01                 r8 = i16 [r7 + 1]
     3:                          invalid
```

Registers after execution (only changed registers):
   * r8 = 0xffff8382 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_load_indirect_i16_without_offset

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x81, 0x82, 0x83, 0x84]

Initial non-zero registers:
   * r7 = 0x20000

```
      :                          @0
     0: 21 78                    r8 = i16 [r7 + 0]
     2:                          invalid
```

Registers after execution (only changed registers):
   * r8 = 0xffff8281 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 2

Gas consumed: 10000 -> 9998


## inst_load_indirect_i8_with_offset

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x81, 0x82, 0x83, 0x84]

Initial non-zero registers:
   * r7 = 0x20000

```
      :                          @0
     0: 15 78 01                 r8 = i8 [r7 + 1]
     3:                          invalid
```

Registers after execution (only changed registers):
   * r8 = 0xffffff82 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_load_indirect_i8_without_offset

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x81, 0x82, 0x83, 0x84]

Initial non-zero registers:
   * r7 = 0x20000

```
      :                          @0
     0: 15 78                    r8 = i8 [r7 + 0]
     2:                          invalid
```

Registers after execution (only changed registers):
   * r8 = 0xffffff81 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 2

Gas consumed: 10000 -> 9998


## inst_load_indirect_u16_with_offset

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x12, 0x34, 0x56, 0x78]

Initial non-zero registers:
   * r7 = 0x20000

```
      :                          @0
     0: 25 78 01                 r8 = u16 [r7 + 1]
     3:                          invalid
```

Registers after execution (only changed registers):
   * r8 = 0x5634 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_load_indirect_u16_without_offset

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x12, 0x34, 0x56, 0x78]

Initial non-zero registers:
   * r7 = 0x20000

```
      :                          @0
     0: 25 78                    r8 = u16 [r7 + 0]
     2:                          invalid
```

Registers after execution (only changed registers):
   * r8 = 0x3412 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 2

Gas consumed: 10000 -> 9998


## inst_load_indirect_u32_with_offset

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20005 (0x5 bytes) = [0x12, 0x34, 0x56, 0x78, 0x9a]

Initial non-zero registers:
   * r7 = 0x20000

```
      :                          @0
     0: 01 78 01                 r8 = u32 [r7 + 1]
     3:                          invalid
```

Registers after execution (only changed registers):
   * r8 = 0x9a785634 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_load_indirect_u32_without_offset

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x12, 0x34, 0x56, 0x78]

Initial non-zero registers:
   * r7 = 0x20000

```
      :                          @0
     0: 01 78                    r8 = u32 [r7 + 0]
     2:                          invalid
```

Registers after execution (only changed registers):
   * r8 = 0x78563412 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 2

Gas consumed: 10000 -> 9998


## inst_load_indirect_u8_with_offset

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x12, 0x34, 0x56, 0x78]

Initial non-zero registers:
   * r7 = 0x20000

```
      :                          @0
     0: 0b 78 01                 r8 = u8 [r7 + 1]
     3:                          invalid
```

Registers after execution (only changed registers):
   * r8 = 0x34 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_load_indirect_u8_without_offset

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x12, 0x34, 0x56, 0x78]

Initial non-zero registers:
   * r7 = 0x20000

```
      :                          @0
     0: 0b 78                    r8 = u8 [r7 + 0]
     2:                          invalid
```

Registers after execution (only changed registers):
   * r8 = 0x12 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 2

Gas consumed: 10000 -> 9998


## inst_load_u16

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x12, 0x34, 0x56, 0x78]

```
      :                          @0
     0: 4c 07 00 00 02           r7 = u16 [0x20000]
     5:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0x3412 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 5

Gas consumed: 10000 -> 9998


## inst_load_u32

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x12, 0x34, 0x56, 0x78]

```
      :                          @0
     0: 0a 07 00 00 02           r7 = u32 [0x20000]
     5:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0x78563412 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 5

Gas consumed: 10000 -> 9998


## inst_load_u8

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x12, 0x34, 0x56, 0x78]

```
      :                          @0
     0: 3c 07 00 00 02           r7 = u8 [0x20000]
     5:                          invalid
```

Registers after execution (only changed registers):
   * r7 = 0x12 (initially was 0x0)

The memory contents after execution should be unchanged.

Program should end with: trap

Final value of the program counter: 5

Gas consumed: 10000 -> 9998


## inst_move_reg

Initial non-zero registers:
   * r7 = 0x1

```
      :                          @0
     0: 52 79                    r9 = r7
     2:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 2

Gas consumed: 10000 -> 9998


## inst_mul

Initial non-zero registers:
   * r7 = 0x3
   * r8 = 0x7

```
      :                          @0
     0: 22 87 09                 r9 = r7 * r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x15 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_mul_imm

Initial non-zero registers:
   * r7 = 0x3

```
      :                          @0
     0: 23 79 07                 r9 = r7 * 7
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x15 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_negate_and_add_imm

Initial non-zero registers:
   * r8 = 0x2

```
      :                          @0
     0: 28 89 01                 r9 = -r8 + 1
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0xffffffff (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_or

Initial non-zero registers:
   * r7 = 0x5
   * r8 = 0x3

```
      :                          @0
     0: 0c 87 09                 r9 = r7 | r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x7 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_or_imm

Initial non-zero registers:
   * r7 = 0x5

```
      :                          @0
     0: 31 79 03                 r9 = r7 | 0x3
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x7 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_rem_signed

Initial non-zero registers:
   * r7 = 0x80000011
   * r8 = 0x7

```
      :                          @0
     0: 46 87 09                 r9 = r7 %s r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0xfffffffa (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_rem_signed_by_zero

Initial non-zero registers:
   * r7 = 0x80000010

```
      :                          @0
     0: 46 87 09                 r9 = r7 %s r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x80000010 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_rem_signed_with_overflow

Initial non-zero registers:
   * r7 = 0x80000000
   * r8 = 0xffffffff
   * r9 = 0xdeadbeef

```
      :                          @0
     0: 46 87 09                 r9 = r7 %s r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x0 (initially was 0xdeadbeef)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_rem_unsigned

Initial non-zero registers:
   * r7 = 0x80000010
   * r8 = 0x7

```
      :                          @0
     0: 49 87 09                 r9 = r7 %u r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x4 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_rem_unsigned_by_zero

Initial non-zero registers:
   * r7 = 0x80000010

```
      :                          @0
     0: 49 87 09                 r9 = r7 %u r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x80000010 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_rem_unsigned_with_overflow

Initial non-zero registers:
   * r7 = 0x80000000
   * r8 = 0xffffffff

```
      :                          @0
     0: 49 87 09                 r9 = r7 %u r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x80000000 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_ret_halt

Initial non-zero registers:
   * r0 = 0xffff0000

```
      :                          @0
     0: 13 00                    jump [r0 + 0]
```

Program should end with: halt

Final value of the program counter: 0

Gas consumed: 10000 -> 9999


## inst_ret_invalid

```
      :                          @0
     0: 13 00                    jump [r0 + 0]
```

Program should end with: trap

Final value of the program counter: 0

Gas consumed: 10000 -> 9999


## inst_set_greater_than_signed_imm_0

Initial non-zero registers:
   * r7 = 0xfffffff6
   * r9 = 0xdeadbeef

```
      :                          @0
     0: 3d 79 0a                 r9 = r7 >s 10
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x0 (initially was 0xdeadbeef)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_set_greater_than_signed_imm_1

Initial non-zero registers:
   * r7 = 0xa

```
      :                          @0
     0: 3d 79 f6                 r9 = r7 >s -10
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_set_greater_than_unsigned_imm_0

Initial non-zero registers:
   * r7 = 0xa
   * r9 = 0xdeadbeef

```
      :                          @0
     0: 27 79 f6                 r9 = r7 >u 0xfffffff6
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x0 (initially was 0xdeadbeef)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_set_greater_than_unsigned_imm_1

Initial non-zero registers:
   * r7 = 0xfffffff6

```
      :                          @0
     0: 27 79 0a                 r9 = r7 >u 0xa
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_set_less_than_signed_0

Initial non-zero registers:
   * r7 = 0xa
   * r8 = 0xfffffff6
   * r9 = 0xdeadbeef

```
      :                          @0
     0: 3a 87 09                 r9 = r7 <s r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x0 (initially was 0xdeadbeef)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_set_less_than_signed_1

Initial non-zero registers:
   * r7 = 0xfffffff6
   * r8 = 0xa

```
      :                          @0
     0: 3a 87 09                 r9 = r7 <s r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_set_less_than_signed_imm_0

Initial non-zero registers:
   * r7 = 0xa
   * r9 = 0xdeadbeef

```
      :                          @0
     0: 38 79 f6                 r9 = r7 <s -10
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x0 (initially was 0xdeadbeef)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_set_less_than_signed_imm_1

Initial non-zero registers:
   * r7 = 0xfffffff6

```
      :                          @0
     0: 38 79 0a                 r9 = r7 <s 10
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_set_less_than_unsigned_0

Initial non-zero registers:
   * r7 = 0xfffffff6
   * r8 = 0xa
   * r9 = 0xdeadbeef

```
      :                          @0
     0: 24 87 09                 r9 = r7 <u r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x0 (initially was 0xdeadbeef)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_set_less_than_unsigned_1

Initial non-zero registers:
   * r7 = 0xa
   * r8 = 0xfffffff6

```
      :                          @0
     0: 24 87 09                 r9 = r7 <u r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_set_less_than_unsigned_imm_0

Initial non-zero registers:
   * r7 = 0xfffffff6
   * r9 = 0xdeadbeef

```
      :                          @0
     0: 1b 79 0a                 r9 = r7 <u 0xa
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x0 (initially was 0xdeadbeef)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_set_less_than_unsigned_imm_1

Initial non-zero registers:
   * r7 = 0xa

```
      :                          @0
     0: 1b 79 f6                 r9 = r7 <u 0xfffffff6
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_shift_arithmetic_right

Initial non-zero registers:
   * r7 = 0x80000075
   * r8 = 0x3

```
      :                          @0
     0: 4d 87 09                 r9 = r7 >>a r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0xf000000e (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_shift_arithmetic_right_imm

Initial non-zero registers:
   * r7 = 0x80000075

```
      :                          @0
     0: 19 79 03                 r9 = r7 >>a 3
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0xf000000e (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_shift_arithmetic_right_imm_alt

Initial non-zero registers:
   * r8 = 0x3

```
      :                          @0
     0: 50 89 75 00 00 80        r9 = 2147483765 >>a r8
     6:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0xf000000e (initially was 0x0)

Program should end with: trap

Final value of the program counter: 6

Gas consumed: 10000 -> 9998


## inst_shift_arithmetic_right_with_overflow

Initial non-zero registers:
   * r7 = 0x80000075
   * r8 = 0x21

```
      :                          @0
     0: 4d 87 09                 r9 = r7 >>a r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0xc000003a (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_shift_logical_left

Initial non-zero registers:
   * r7 = 0x80000075
   * r8 = 0x3

```
      :                          @0
     0: 37 87 09                 r9 = r7 << r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x3a8 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_shift_logical_left_imm

Initial non-zero registers:
   * r7 = 0x80000075

```
      :                          @0
     0: 09 79 03                 r9 = r7 << 3
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x3a8 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_shift_logical_left_imm_alt

Initial non-zero registers:
   * r8 = 0x3

```
      :                          @0
     0: 4b 89 75 00 00 80        r9 = 2147483765 << r8
     6:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x3a8 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 6

Gas consumed: 10000 -> 9998


## inst_shift_logical_left_with_overflow

Initial non-zero registers:
   * r7 = 0x80000075
   * r8 = 0x21

```
      :                          @0
     0: 37 87 09                 r9 = r7 << r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0xea (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_shift_logical_right

Initial non-zero registers:
   * r7 = 0x80000075
   * r8 = 0x3

```
      :                          @0
     0: 33 87 09                 r9 = r7 >> r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1000000e (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_shift_logical_right_imm

Initial non-zero registers:
   * r7 = 0x80000075

```
      :                          @0
     0: 0e 79 03                 r9 = r7 >> 3
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1000000e (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_shift_logical_right_imm_alt

Initial non-zero registers:
   * r8 = 0x3

```
      :                          @0
     0: 48 89 75 00 00 80        r9 = 2147483765 >> r8
     6:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1000000e (initially was 0x0)

Program should end with: trap

Final value of the program counter: 6

Gas consumed: 10000 -> 9998


## inst_shift_logical_right_with_overflow

Initial non-zero registers:
   * r7 = 0x80000075
   * r8 = 0x21

```
      :                          @0
     0: 33 87 09                 r9 = r7 >> r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x4000003a (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_store_imm_u16

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

```
      :                          @0
     0: 4f 03 00 00 02 34 12     u16 [0x20000] = 4660
     7:                          invalid
```

Final non-zero memory chunks:
   * 0x20000-0x20002 (0x2 bytes) = [0x34, 0x12]

Program should end with: trap

Final value of the program counter: 7

Gas consumed: 10000 -> 9998


## inst_store_imm_u32

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

```
      :                          @0
     0: 26 03 00 00 02 78 56 34 12 u32 [0x20000] = 305419896
     9:                          invalid
```

Final non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x78, 0x56, 0x34, 0x12]

Program should end with: trap

Final value of the program counter: 9

Gas consumed: 10000 -> 9998


## inst_store_imm_u8

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

```
      :                          @0
     0: 3e 03 00 00 02 12        u8 [0x20000] = 18
     6:                          invalid
```

Final non-zero memory chunks:
   * 0x20000-0x20001 (0x1 bytes) = [0x12]

Program should end with: trap

Final value of the program counter: 6

Gas consumed: 10000 -> 9998


## inst_store_u16

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero registers:
   * r7 = 0x12345678

```
      :                          @0
     0: 45 07 00 00 02           u16 [0x20000] = r7
     5:                          invalid
```

Final non-zero memory chunks:
   * 0x20000-0x20002 (0x2 bytes) = [0x78, 0x56]

Program should end with: trap

Final value of the program counter: 5

Gas consumed: 10000 -> 9998


## inst_store_u32

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero registers:
   * r7 = 0x12345678

```
      :                          @0
     0: 16 07 00 00 02           u32 [0x20000] = r7
     5:                          invalid
```

Final non-zero memory chunks:
   * 0x20000-0x20004 (0x4 bytes) = [0x78, 0x56, 0x34, 0x12]

Program should end with: trap

Final value of the program counter: 5

Gas consumed: 10000 -> 9998


## inst_store_u8

Initial page map:
   * RW: 0x20000-0x21000 (0x1000 bytes)

Initial non-zero registers:
   * r7 = 0x12345678

```
      :                          @0
     0: 47 07 00 00 02           u8 [0x20000] = r7
     5:                          invalid
```

Final non-zero memory chunks:
   * 0x20000-0x20001 (0x1 bytes) = [0x78]

Program should end with: trap

Final value of the program counter: 5

Gas consumed: 10000 -> 9998


## inst_sub

Initial non-zero registers:
   * r7 = 0x2
   * r8 = 0x1

```
      :                          @0
     0: 14 87 09                 r9 = r7 - r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_sub_imm

Initial non-zero registers:
   * r7 = 0x2

```
      :                          @0
     0: 02 79 ff                 r9 = r7 + 0xffffffff
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_sub_with_overflow

Initial non-zero registers:
   * r7 = 0x2
   * r8 = 0x4

```
      :                          @0
     0: 14 87 09                 r9 = r7 - r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0xfffffffe (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_trap

```
      :                          @0
     0: 00                       trap
```

Program should end with: trap

Final value of the program counter: 0

Gas consumed: 10000 -> 9999


## inst_xor

Initial non-zero registers:
   * r7 = 0x5
   * r8 = 0x3

```
      :                          @0
     0: 1c 87 09                 r9 = r7 ^ r8
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x6 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


## inst_xor_imm

Initial non-zero registers:
   * r7 = 0x5

```
      :                          @0
     0: 1f 79 03                 r9 = r7 ^ 0x3
     3:                          invalid
```

Registers after execution (only changed registers):
   * r9 = 0x6 (initially was 0x0)

Program should end with: trap

Final value of the program counter: 3

Gas consumed: 10000 -> 9998


