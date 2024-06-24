# Testcases

This file contains a human-readable index of all of the testcases,
along with their disassemblies and other relevant information.


## inst_add

Initial non-zero registers:
   * r7 = 0x1
   * r8 = 0x2

```
      :                          @0
     0: 08 79 08                 r9 = r7 + r8
```

Registers after execution (only changed registers):
   * r9 = 0x3 (initially was 0x0)

Program should end with: trap


## inst_add_imm

Initial non-zero registers:
   * r7 = 0x1

```
      :                          @0
     0: 02 79 02                 r9 = r7 + 0x2
```

Registers after execution (only changed registers):
   * r9 = 0x3 (initially was 0x0)

Program should end with: trap


## inst_add_with_overflow

Initial non-zero registers:
   * r7 = 0xffffffff
   * r8 = 0x2

```
      :                          @0
     0: 08 79 08                 r9 = r7 + r8
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap


## inst_and

Initial non-zero registers:
   * r7 = 0x5
   * r8 = 0x3

```
      :                          @0
     0: 17 79 08                 r9 = r7 & r8
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap


## inst_and_imm

Initial non-zero registers:
   * r7 = 0x5

```
      :                          @0
     0: 12 79 03                 r9 = r7 & 0x3
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap


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
```

Registers after execution (only changed registers):
   * r7 = 0x4d2 (initially was 0x0)
   * r8 = 0x4d3 (initially was 0x0)

Program should end with: trap


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
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)
   * r8 = 0x4d2 (initially was 0x0)

Program should end with: trap


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
```

Registers after execution (only changed registers):
   * r7 = 0x4d2 (initially was 0x0)
   * r8 = 0x4d2 (initially was 0x0)

Program should end with: trap


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
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)
   * r8 = 0x4d3 (initially was 0x0)

Program should end with: trap


## inst_cmov_if_zero_imm_nok

Initial non-zero registers:
   * r10 = 0x1

```
      :                          @0
     0: 55 a7 64                 r7 = 100 if r10 == 0
```

Program should end with: trap


## inst_cmov_if_zero_imm_ok

```
      :                          @0
     0: 55 a7 64                 r7 = 100 if r10 == 0
```

Registers after execution (only changed registers):
   * r7 = 0x64 (initially was 0x0)

Program should end with: trap


## inst_cmov_if_zero_nok

Initial non-zero registers:
   * r8 = 0x64
   * r10 = 0x1

```
      :                          @0
     0: 53 87 0a                 r7 = r8 if r10 == 0
```

Program should end with: trap


## inst_cmov_if_zero_ok

Initial non-zero registers:
   * r8 = 0x64

```
      :                          @0
     0: 53 87 0a                 r7 = r8 if r10 == 0
```

Registers after execution (only changed registers):
   * r7 = 0x64 (initially was 0x0)

Program should end with: trap


## inst_div_signed

Initial non-zero registers:
   * r7 = 0x80000010
   * r8 = 0x7

```
      :                          @0
     0: 40 79 08                 r9 = r7 /s r8
```

Registers after execution (only changed registers):
   * r9 = 0xedb6db70 (initially was 0x0)

Program should end with: trap


## inst_div_signed_by_zero

Initial non-zero registers:
   * r7 = 0x80000010

```
      :                          @0
     0: 40 79 08                 r9 = r7 /s r8
```

Registers after execution (only changed registers):
   * r9 = 0xffffffff (initially was 0x0)

Program should end with: trap


## inst_div_signed_with_overflow

Initial non-zero registers:
   * r7 = 0x80000000
   * r8 = 0xffffffff

```
      :                          @0
     0: 40 79 08                 r9 = r7 /s r8
```

Registers after execution (only changed registers):
   * r9 = 0x80000000 (initially was 0x0)

Program should end with: trap


## inst_div_unsigned

Initial non-zero registers:
   * r7 = 0x80000010
   * r8 = 0x7

```
      :                          @0
     0: 44 79 08                 r9 = r7 /u r8
```

Registers after execution (only changed registers):
   * r9 = 0x12492494 (initially was 0x0)

Program should end with: trap


## inst_div_unsigned_by_zero

Initial non-zero registers:
   * r7 = 0x80000010

```
      :                          @0
     0: 44 79 08                 r9 = r7 /u r8
```

Registers after execution (only changed registers):
   * r9 = 0xffffffff (initially was 0x0)

Program should end with: trap


## inst_div_unsigned_with_overflow

Initial non-zero registers:
   * r7 = 0x80000000
   * r8 = 0xffffffff

```
      :                          @0
     0: 44 79 08                 r9 = r7 /u r8
```

Program should end with: trap


## inst_fallthrough

```
      :                          @0
     0: 11                       fallthrough
```

Program should end with: trap


## inst_jump

```
      :                          @0
     0: 04 07 d2 04              r7 = 0x4d2
     4: 05 03                    jump 7
      :                          @1
     6: 00                       trap
      :                          @2
     7: 04 07 ef be ad de        r7 = 0xdeadbeef
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap


## inst_load_imm

```
      :                          @0
     0: 04 07 ef be ad de        r7 = 0xdeadbeef
```

Registers after execution (only changed registers):
   * r7 = 0xdeadbeef (initially was 0x0)

Program should end with: trap


## inst_move_reg

Initial non-zero registers:
   * r7 = 0x1

```
      :                          @0
     0: 52 79                    r9 = r7
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap


## inst_mul

Initial non-zero registers:
   * r7 = 0x3
   * r8 = 0x7

```
      :                          @0
     0: 22 79 08                 r9 = r7 * r8
```

Registers after execution (only changed registers):
   * r9 = 0x15 (initially was 0x0)

Program should end with: trap


## inst_mul_imm

Initial non-zero registers:
   * r7 = 0x3

```
      :                          @0
     0: 23 79 07                 r9 = r7 * 7
```

Registers after execution (only changed registers):
   * r9 = 0x15 (initially was 0x0)

Program should end with: trap


## inst_negate_and_add_imm

Initial non-zero registers:
   * r8 = 0x2

```
      :                          @0
     0: 28 89 01                 r9 = -r8 + 1
```

Registers after execution (only changed registers):
   * r9 = 0xffffffff (initially was 0x0)

Program should end with: trap


## inst_or

Initial non-zero registers:
   * r7 = 0x5
   * r8 = 0x3

```
      :                          @0
     0: 0c 79 08                 r9 = r7 | r8
```

Registers after execution (only changed registers):
   * r9 = 0x7 (initially was 0x0)

Program should end with: trap


## inst_or_imm

Initial non-zero registers:
   * r7 = 0x5

```
      :                          @0
     0: 31 79 03                 r9 = r7 | 0x3
```

Registers after execution (only changed registers):
   * r9 = 0x7 (initially was 0x0)

Program should end with: trap


## inst_rem_signed

Initial non-zero registers:
   * r7 = 0x80000010
   * r8 = 0x7

```
      :                          @0
     0: 46 79 08                 r9 = r7 %s r8
```

Program should end with: trap


## inst_rem_signed_by_zero

Initial non-zero registers:
   * r7 = 0x80000010

```
      :                          @0
     0: 46 79 08                 r9 = r7 %s r8
```

Registers after execution (only changed registers):
   * r9 = 0x80000010 (initially was 0x0)

Program should end with: trap


## inst_rem_signed_with_overflow

Initial non-zero registers:
   * r7 = 0x80000000
   * r8 = 0xffffffff

```
      :                          @0
     0: 46 79 08                 r9 = r7 %s r8
```

Program should end with: trap


## inst_rem_unsigned

Initial non-zero registers:
   * r7 = 0x80000010
   * r8 = 0x7

```
      :                          @0
     0: 49 79 08                 r9 = r7 %u r8
```

Registers after execution (only changed registers):
   * r9 = 0x4 (initially was 0x0)

Program should end with: trap


## inst_rem_unsigned_by_zero

Initial non-zero registers:
   * r7 = 0x80000010

```
      :                          @0
     0: 49 79 08                 r9 = r7 %u r8
```

Registers after execution (only changed registers):
   * r9 = 0x80000010 (initially was 0x0)

Program should end with: trap


## inst_rem_unsigned_with_overflow

Initial non-zero registers:
   * r7 = 0x80000000
   * r8 = 0xffffffff

```
      :                          @0
     0: 49 79 08                 r9 = r7 %u r8
```

Registers after execution (only changed registers):
   * r9 = 0x80000000 (initially was 0x0)

Program should end with: trap


## inst_ret_halt

Initial non-zero registers:
   * r0 = 0xffff0000

```
      :                          @0
     0: 13 00                    jump [r0 + 0]
```

Program should end with: halt


## inst_ret_invalid

```
      :                          @0
     0: 13 00                    jump [r0 + 0]
```

Program should end with: trap


## inst_set_greater_than_signed_imm_0

Initial non-zero registers:
   * r7 = 0xfffffff6

```
      :                          @0
     0: 3d 79 0a                 r9 = r7 >s 10
```

Program should end with: trap


## inst_set_greater_than_signed_imm_1

Initial non-zero registers:
   * r7 = 0xa

```
      :                          @0
     0: 3d 79 f6                 r9 = r7 >s -10
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap


## inst_set_greater_than_unsigned_imm_0

Initial non-zero registers:
   * r7 = 0xa

```
      :                          @0
     0: 27 79 f6                 r9 = r7 >u 0xfffffff6
```

Program should end with: trap


## inst_set_greater_than_unsigned_imm_1

Initial non-zero registers:
   * r7 = 0xfffffff6

```
      :                          @0
     0: 27 79 0a                 r9 = r7 >u 0xa
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap


## inst_set_less_than_signed_0

Initial non-zero registers:
   * r7 = 0xa
   * r8 = 0xfffffff6

```
      :                          @0
     0: 3a 79 08                 r9 = r7 <s r8
```

Program should end with: trap


## inst_set_less_than_signed_1

Initial non-zero registers:
   * r7 = 0xfffffff6
   * r8 = 0xa

```
      :                          @0
     0: 3a 79 08                 r9 = r7 <s r8
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap


## inst_set_less_than_signed_imm_0

Initial non-zero registers:
   * r7 = 0xa

```
      :                          @0
     0: 38 79 f6                 r9 = r7 <s -10
```

Program should end with: trap


## inst_set_less_than_signed_imm_1

Initial non-zero registers:
   * r7 = 0xfffffff6

```
      :                          @0
     0: 38 79 0a                 r9 = r7 <s 10
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap


## inst_set_less_than_unsigned_0

Initial non-zero registers:
   * r7 = 0xfffffff6
   * r8 = 0xa

```
      :                          @0
     0: 24 79 08                 r9 = r7 <u r8
```

Program should end with: trap


## inst_set_less_than_unsigned_1

Initial non-zero registers:
   * r7 = 0xa
   * r8 = 0xfffffff6

```
      :                          @0
     0: 24 79 08                 r9 = r7 <u r8
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap


## inst_set_less_than_unsigned_imm_0

Initial non-zero registers:
   * r7 = 0xfffffff6

```
      :                          @0
     0: 1b 79 0a                 r9 = r7 <u 0xa
```

Program should end with: trap


## inst_set_less_than_unsigned_imm_1

Initial non-zero registers:
   * r7 = 0xa

```
      :                          @0
     0: 1b 79 f6                 r9 = r7 <u 0xfffffff6
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap


## inst_shift_arithmetic_right

Initial non-zero registers:
   * r7 = 0x80000075
   * r8 = 0x3

```
      :                          @0
     0: 4d 79 08                 r9 = r7 >>a r8
```

Registers after execution (only changed registers):
   * r9 = 0xf000000e (initially was 0x0)

Program should end with: trap


## inst_shift_arithmetic_right_imm

Initial non-zero registers:
   * r7 = 0x80000075

```
      :                          @0
     0: 19 79 03                 r9 = r7 >>a 3
```

Registers after execution (only changed registers):
   * r9 = 0xf000000e (initially was 0x0)

Program should end with: trap


## inst_shift_arithmetic_right_imm_alt

Initial non-zero registers:
   * r8 = 0x3

```
      :                          @0
     0: 50 89 75 00 00 80        r9 = 2147483765 >>a r8
```

Registers after execution (only changed registers):
   * r9 = 0xf000000e (initially was 0x0)

Program should end with: trap


## inst_shift_arithmetic_right_with_overflow

Initial non-zero registers:
   * r7 = 0x80000075
   * r8 = 0x21

```
      :                          @0
     0: 4d 79 08                 r9 = r7 >>a r8
```

Registers after execution (only changed registers):
   * r9 = 0xc000003a (initially was 0x0)

Program should end with: trap


## inst_shift_logical_left

Initial non-zero registers:
   * r7 = 0x80000075
   * r8 = 0x3

```
      :                          @0
     0: 37 79 08                 r9 = r7 << r8
```

Registers after execution (only changed registers):
   * r9 = 0x3a8 (initially was 0x0)

Program should end with: trap


## inst_shift_logical_left_imm

Initial non-zero registers:
   * r7 = 0x80000075

```
      :                          @0
     0: 09 79 03                 r9 = r7 << 3
```

Registers after execution (only changed registers):
   * r9 = 0x3a8 (initially was 0x0)

Program should end with: trap


## inst_shift_logical_left_imm_alt

Initial non-zero registers:
   * r8 = 0x3

```
      :                          @0
     0: 4b 89 75 00 00 80        r9 = 2147483765 << r8
```

Registers after execution (only changed registers):
   * r9 = 0x3a8 (initially was 0x0)

Program should end with: trap


## inst_shift_logical_left_with_overflow

Initial non-zero registers:
   * r7 = 0x80000075
   * r8 = 0x21

```
      :                          @0
     0: 37 79 08                 r9 = r7 << r8
```

Registers after execution (only changed registers):
   * r9 = 0xea (initially was 0x0)

Program should end with: trap


## inst_shift_logical_right

Initial non-zero registers:
   * r7 = 0x80000075
   * r8 = 0x3

```
      :                          @0
     0: 33 79 08                 r9 = r7 >> r8
```

Registers after execution (only changed registers):
   * r9 = 0x1000000e (initially was 0x0)

Program should end with: trap


## inst_shift_logical_right_imm

Initial non-zero registers:
   * r7 = 0x80000075

```
      :                          @0
     0: 0e 79 03                 r9 = r7 >> 3
```

Registers after execution (only changed registers):
   * r9 = 0x1000000e (initially was 0x0)

Program should end with: trap


## inst_shift_logical_right_imm_alt

Initial non-zero registers:
   * r8 = 0x3

```
      :                          @0
     0: 48 89 75 00 00 80        r9 = 2147483765 >> r8
```

Registers after execution (only changed registers):
   * r9 = 0x1000000e (initially was 0x0)

Program should end with: trap


## inst_shift_logical_right_with_overflow

Initial non-zero registers:
   * r7 = 0x80000075
   * r8 = 0x21

```
      :                          @0
     0: 33 79 08                 r9 = r7 >> r8
```

Registers after execution (only changed registers):
   * r9 = 0x4000003a (initially was 0x0)

Program should end with: trap


## inst_sub

Initial non-zero registers:
   * r7 = 0x2
   * r8 = 0x1

```
      :                          @0
     0: 14 79 08                 r9 = r7 - r8
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap


## inst_sub_imm

Initial non-zero registers:
   * r7 = 0x2

```
      :                          @0
     0: 02 79 ff                 r9 = r7 + 0xffffffff
```

Registers after execution (only changed registers):
   * r9 = 0x1 (initially was 0x0)

Program should end with: trap


## inst_sub_with_overflow

Initial non-zero registers:
   * r7 = 0x2
   * r8 = 0x4

```
      :                          @0
     0: 14 79 08                 r9 = r7 - r8
```

Registers after execution (only changed registers):
   * r9 = 0xfffffffe (initially was 0x0)

Program should end with: trap


## inst_trap

```
      :                          @0
     0: 00                       trap
```

Program should end with: trap


## inst_xor

Initial non-zero registers:
   * r7 = 0x5
   * r8 = 0x3

```
      :                          @0
     0: 1c 79 08                 r9 = r7 ^ r8
```

Registers after execution (only changed registers):
   * r9 = 0x6 (initially was 0x0)

Program should end with: trap


## inst_xor_imm

Initial non-zero registers:
   * r7 = 0x5

```
      :                          @0
     0: 1f 79 03                 r9 = r7 ^ 0x3
```

Registers after execution (only changed registers):
   * r9 = 0x6 (initially was 0x0)

Program should end with: trap


