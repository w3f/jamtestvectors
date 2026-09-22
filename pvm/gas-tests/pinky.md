Gas simulation at offset 0 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r9 = u8 [r7 + 11]
    D=========================eER  jump 24 if r9 == 0
```

Gas simulation at offset 6 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeE---------------------------------------R............  r9 = r8 >> 0x3
    DeE---------------------------------------R............  r10 = 0x17290
    .DeE--------------------------------------R............  r9 = r9 + r10
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R............  r9 = u8 [r9 + 0]
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 12] = a2
    .DeeE-------------------------------------------------R  fallthrough
```

Gas simulation at offset 24 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = i16 [r7 + 6]
    DeE---------------------------------------R.............  r8 = r8 & 0x7
    DeE---------------------------------------R.............  r10 = 0x1
    .DeE--------------------------------------R.............  r8 = r8 << 0x8
    .D========================eE--------------R.............  r9 = r9 & 0xfffffffffffff8ff
    .D=========================eE-------------R.............  r8 = r8 | r9
    ..D=========================eE------------R.............  r9 = r8 + r10
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R.............  u8 [r7 + 2] = a3
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r7 + 6] = r8
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 8] = r9
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u8 [r7 + 22] = 0
    ...DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 61 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u8 [r7 + 14]
    D=========================eER  jump 85 if r8 == 0
```

Gas simulation at offset 67 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r8 = u8 [r7 + 18]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r9 = u8 [r7 + 20]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  u8 [r7 + 14] = 0
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 19] = a2
    .D========================eE------------------------R  jump 100 if r8 == 0
```

Gas simulation at offset 83 with total cost of 22:

```
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 85 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r7 + 19]
    D=========================eE--------------R  jump 116 if r8 == 0
```

Gas simulation at offset 92 with total cost of 26:

```
    DeER.........................  r8 = r8 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 19] = a1
    DeeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 100 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r7 + 13]
    D=========================eE--------------R  jump 83 if r8 == 0
```

Gas simulation at offset 107 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r7 + 21]
    D=========================eE--------------R  jump 136 if r9 != 0
```

Gas simulation at offset 114 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 83
```

Gas simulation at offset 116 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r7 + 13]
    D=========================eE--------------R  jump 83 if r8 == 0
```

Gas simulation at offset 123 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r8 = u8 [r7 + 20]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r9 = u8 [r7 + 21]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 19] = a1
    .D========================eE------------------------R  jump 83 if r9 == 0
```

Gas simulation at offset 136 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u16 [r7 + 6]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r10 = u8 [r7 + 15]
    DeE---------------------------------------R  r9 = r9 & 0xf
    .D========================eE--------------R  r9 = r8 >> r9
    .D========================eE--------------R  jump 170 if r10 == 0
```

Gas simulation at offset 152 with total cost of 45:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.....  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.....  r10 = u8 [r7 + 16]
    D=========================eeeeeeeeeeeeeeeeeeeeER  jump 181 if r10 == 0
```

Gas simulation at offset 159 with total cost of 21:

```
    DeER....................  r9 = r8 - r9
    DeER....................  r10 = 0x8
    D=eeeeeeeeeeeeeeeeeeeeER  jump 193 if r8 >=u r10
```

Gas simulation at offset 168 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 83
```

Gas simulation at offset 170 with total cost of 21:

```
    DeER....................  r9 = r9 + r8
    DeER....................  r10 = 0x8
    D=eeeeeeeeeeeeeeeeeeeeER  jump 193 if r8 >=u r10
```

Gas simulation at offset 179 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 83
```

Gas simulation at offset 181 with total cost of 21:

```
    DeER....................  r9 = r9 ^ 0xffffffffffffffff
    D=eER...................  r9 = r9 + r8
    DeE-R...................  r10 = 0x8
    D=eeeeeeeeeeeeeeeeeeeeER  jump 83 if r8 <u r10
```

Gas simulation at offset 193 with total cost of 21:

```
    DeER....................  r8 = zext16 r9
    DeER....................  r10 = 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeER  jump 83 if r10 <u r8
```

Gas simulation at offset 202 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 6] = r9
    DeeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 207 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r9 = u8 [r7 + 8]
    D=========================eER  jump 231 if r9 == 0
```

Gas simulation at offset 213 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeE---------------------------------------R............  r9 = r8 >> 0x3
    DeE---------------------------------------R............  r10 = 0x17290
    .DeE--------------------------------------R............  r9 = r9 + r10
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R............  r9 = u8 [r9 + 0]
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 9] = a2
    .DeeE-------------------------------------------------R  fallthrough
```

Gas simulation at offset 231 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = i16 [r7 + 0]
    DeE---------------------------------------R.............  r8 = r8 & 0x7
    DeE---------------------------------------R.............  r10 = 0x1
    .DeE--------------------------------------R.............  r8 = r8 << 0x8
    .D========================eE--------------R.............  r9 = r9 & 0xfffffffffffff8ff
    .D=========================eE-------------R.............  r8 = r8 | r9
    ..D=========================eE------------R.............  r9 = r8 + r10
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r7 + 0] = r8
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 2] = r9
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u8 [r7 + 10] = a3
    ...DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 263 with total cost of 54:

```
    DeER.....................................................  r2 = 0
    DeER.....................................................  r7 = r7 + 0x7ff
    DeER.....................................................  r9 = r8 & 0x1
    .DeER....................................................  r11 = r8 >> 0x1
    .DeER....................................................  r10 = r8 >> 0x2
    ..DeER...................................................  r12 = r8 >> 0x3
    ..DeER...................................................  r8 = r8 << 0x3b
    ..DeER...................................................  r11 = r11 & 0x1
    ...DeER..................................................  r10 = r10 & 0x1
    ...DeER..................................................  r12 = r12 & 0x1
    ...DeER..................................................  r8 = r8 >> 0x3f
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u8 [r7 + 12] = a2
    ....DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r7 + 36] = a4
    ....DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r7 + 62] = a5
    ....DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r7 + 121] = a3
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r7 + 139] = a1
    .....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 143] = 0
    .....D========================eE------------------------R  jump 355 if r8 == 0
```

Gas simulation at offset 319 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u16 [r7 + 133]
    D=========================eE--------------R  jump 341 if r8 == 0
```

Gas simulation at offset 327 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 362 if r9 == 0
```

Gas simulation at offset 330 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 368 if r11 == 0
```

Gas simulation at offset 333 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 374 if r10 == 0
```

Gas simulation at offset 336 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 380 if r12 == 0
```

Gas simulation at offset 339 with total cost of 22:

```
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 341 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r8 = i16 [r7 + 129]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r2 = u16 [r7 + 131]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 135] = r8
    .DeeE-----------------------------------------------R  fallthrough
```

Gas simulation at offset 355 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 133] = r2
    DeeeeeeeeeeeeeeeeeeeeE-----R  jump 330 if r9 != 0
```

Gas simulation at offset 362 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 13] = 0
    DeeeeeeeeeeeeeeeeeeeeE-----R  jump 333 if r11 != 0
```

Gas simulation at offset 368 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 37] = 0
    DeeeeeeeeeeeeeeeeeeeeE-----R  jump 336 if r10 != 0
```

Gas simulation at offset 374 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 122] = 0
    DeeeeeeeeeeeeeeeeeeeeE-----R  jump 339 if r12 != 0
```

Gas simulation at offset 380 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 63] = 0
    DeeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 385 with total cost of 52:

```
    DeER...................................................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 0] = r6
    .DeE------------------------R..........................  r9 = r8 >> 0xd
    .D=eE-----------------------R..........................  r9 = r9 << 0x2
    .DeE------------------------R..........................  r10 = 0x10000
    ..D=eE----------------------R..........................  r9 = r9 + r10
    ..D==eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r9 = i32 [r9 + 0]
    ..D===========================eER......................  r9 = r9 + r10
    ...D=======================eE---R......................  r6 = r7 + 0x7ff
    ...D===========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r9 + 0]
```

Gas simulation at offset 421 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r7 = u64 [r6 + 585]
    DeE------------------------R...........................  r10 = 0x17c80
    .D========================eeER.........................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r12 = u64 [r10 + 24]
    .DeeE-------------------------------------------------R  fallthrough
```

Gas simulation at offset 441 with total cost of 26:

```
    DeER.........................  r7 = r6 + 0x27f
    D=eeER.......................  r7 = r9 if r9 != 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r0 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    .D==eE----------------------R  r1 = r1 + 0x18
    ..DeeeeeeeeeeeeeeeeeeeeeeE--R  jump [r12 + 0]
```

Gas simulation at offset 461 with total cost of 2:

```
    DeER.  r9 = r8 >> 0x5
    DeER.  r10 = 0x201
    D=eER  jump 638 if r9 >=u r10
```

Gas simulation at offset 472 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeE---------------------------------------R...........  r8 = r8 & 0x1f
    D=eE--------------------------------------R...........  r8 = r8 << 0x2
    DeE---------------------------------------R...........  r9 = 0x10020
    .D=eE-------------------------------------R...........  r8 = r8 + r9
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R...........  r8 = i32 [r8 + 0]
    .D===========================eE-----------R...........  r9 = r9 + r8
    .DeE--------------------------------------R...........  r8 = 0
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r9 + 0]
```

Gas simulation at offset 496 with total cost of 47:

```
    D.................................................  r7 = r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 0]
    .DeE-----------------------R......................  r1 = r1 + 0x18
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 511 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r7 = u64 [r6 + 585]
    DeE------------------------R...........................  r10 = 0x17c80
    .D========================eeER.........................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r12 = u64 [r10 + 40]
    .DeeeeeeeeeeeeeeeE------------------------------------R  jump 441
```

Gas simulation at offset 532 with total cost of 47:

```
    DeER..............................................  r8 = r8 & 0x7ff
    D=eER.............................................  r7 = r7 + r8
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER....................  r7 = u8 [r7 + 0]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE--R....................  r0 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R....................  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R....................  r6 = u64 [r1 + 0]
    .D========================eE-R....................  r1 = r1 + 0x18
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 554 with total cost of 2:

```
    DeER.  r8 = r8 & 0x7
    D=eER  jump 690 if r8 == 2
```

Gas simulation at offset 562 with total cost of 2:

```
    DeER.  r9 = 0x4
    D=eER  jump 661 if r8 == r9
```

Gas simulation at offset 568 with total cost of 2:

```
    DeER.  r9 = 0x7
    D=eER  jump 742 if r8 != r9
```

Gas simulation at offset 575 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u16 [r6 + 521]
    D=========================eE--------------R  r5 = r8 << 0x32
    .D=========================eE-------------R  r9 = r5 >> 0x3a
    .DeE--------------------------------------R  r10 = 0x3f
    .D=========================eE-------------R  r5 = r5 >> 0x32
    ..D=========================eE------------R  jump 758 if r9 >=u r10
```

Gas simulation at offset 596 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r8 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r9 = 0x17c80
    .D========================eeE-------------R..................................  r9 = r7 if r8 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r9 = u64 [r9 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r8 if r8 != 0
    ...D.........................................................................  r8 = r5
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 14, jump [r9 + 0]
```

Gas simulation at offset 629 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 521]
    D...........................  r12 = r7
    DeeeeeeeeeeeeeeeE----------R  jump 773
```

Gas simulation at offset 638 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r7 = u64 [r6 + 585]
    DeE---------------------------------------R............  r10 = 0x17c80
    .D========================eeE-------------R............  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r12 = u64 [r10 + 56]
    .DeeeeeeeeeeeeeeeE------------------------------------R  jump 441
```

Gas simulation at offset 661 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r8 = u8 [r6 + 548]
    D=========================eE--------------R............  r7 = r7 + r8
    D==========================eE-------------R............  r7 = r7 + 0x7ff
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 161]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r0 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r6 = u64 [r1 + 0]
    ..D========================eE-------------------------R  r1 = r1 + 0x18
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 690 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r7 = u8 [r6 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r6 + 553]
    .D========================eE--------------R.............  r9 = r7 & 0xe0
    .D========================eE--------------R.............  r8 = r8 & 0x1f
    .D=========================eE-------------R.............  r8 = r8 | r9
    ..DeE-------------------------------------R.............  r9 = 0x1
    ..D========================eE-------------R.............  r7 = r7 & 0x7f
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r6 + 552] = a0
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r6 + 553] = a1
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R.  u16 [r6 + 569] = r9
    ...D....................................................  r7 = r8
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R.  r0 = u64 [r1 + 16]
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 8]
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D================================================eER  r1 = r1 + 0x18
    ....D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 742 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 0]
    .DeE--------------------------------------R.......  r1 = r1 + 0x18
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 758 with total cost of 28:

```
    DeER...........................  r9 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r9
    D==eER.........................  r7 = r7 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r12 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 773 with total cost of 56:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r7 = u8 [r6 + 550]
    DeE------------------------R...............................  r9 = r5 >> 0x8
    DeE------------------------R...............................  r10 = 0x20
    .DeE-----------------------R...............................  r11 = 0x1
    .D========================eER..............................  r7 = r7 & 0x4
    .D=========================eeER............................  r11 = r10 if r7 != 0
    ..D==========================eER...........................  r8 = r8 + r11
    ..D===========================eER..........................  r8 = r8 << 0x31
    ..D============================eER.........................  r8 = r8 >> 0x31
    ..D=============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 521] = r8
    ...DeE----------------------------------------------------R  jump 835 if r9 >=u 63
```

Gas simulation at offset 809 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r7 = u8 [r6 + 549]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  u8 [r6 + 549] = a5
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 553] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R  r0 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R  r5 = u64 [r1 + 8]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    .D=========================eE-----------------------R  r1 = r1 + 0x18
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 835 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r8 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r9 = 0x17c80
    .D========================eeE-------------R..................................  r9 = r7 if r8 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r9 = u64 [r9 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r8 if r8 != 0
    ...D.........................................................................  r8 = r5
    ...D.........................................................................  r5 = r12
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 16, jump [r9 + 0]
```

Gas simulation at offset 870 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r9 = u8 [r6 + 551]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r10 = u8 [r6 + 553]
    DeE------------------------R.............................  r8 = r5 & 0x30
    .D========================eER............................  r9 = r9 & 0x1
    .D=========================eeER..........................  r8 = r5 if r9 == 0
    ..D=======================eE--R..........................  r9 = r10 & 0xc0
    ..D==========================eER.........................  r9 = r9 | r8
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--R.........................  u8 [r6 + 549] = a0
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 553] = a2
    ...D.....................................................  r7 = r8
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r0 = u64 [r1 + 16]
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE---R  r5 = u64 [r1 + 8]
    ....D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  r6 = u64 [r1 + 0]
    ....D========================eE-------------------------R  r1 = r1 + 0x18
    ....D========================eeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 917 with total cost of 25:

```
    DeER........................  r8 = 0x1
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r0 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    .DeE-----------------------R  r1 = r1 + 0x18
    .DeeeeeeeeeeeeeeeE---------R  jump 5285
```

Gas simulation at offset 934 with total cost of 25:

```
    DeER........................  r8 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r0 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    .DeE-----------------------R  r1 = r1 + 0x18
    .DeeeeeeeeeeeeeeeE---------R  jump 5285
```

Gas simulation at offset 950 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r0 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r5 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r6 = u64 [r1 + 0]
    DeE------------------------R...........................................................................  r1 = r1 + 0x18
    .DeE-----------------------R...........................................................................  r8 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r7 = u8 [r8 + 13]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r9 = u8 [r8 + 37]
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r10 = u8 [r8 + 63]
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = u8 [r8 + 122]
    ...D========================eeeE--------------------R..................................................  r7 = r7 >u 0
    ....D==============================================eeeER...............................................  r9 = r9 >u 0
    ....D=================================================eER..............................................  r9 = r9 << 0x1
    .....D=================================================eER.............................................  r2 = r9 | r7
    .....D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................  r9 = u16 [r8 + 133]
    .....D=============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r12 = u8 [r8 + 143]
    ......D============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u8 [r8 + 153]
    ......D=================================================eeeE-----------------R.........................  r11 = r11 >u 0
    .......D================================================eeeE-----------------R.........................  r10 = r10 >u 0
    .......D===================================================eE----------------R.........................  r11 = r11 << 0x2
    ........D==================================================eE----------------R.........................  r10 = r10 << 0x3
    ........D===================================================eE---------------R.........................  r10 = r10 | r11
    .........D==================================================eeeE-------------R.........................  r9 = r9 >u 0
    .........D==================================================================eER........................  r7 = r7 << 0x6
    ..........D====================================================eE-------------R........................  r9 = r9 << 0x4
    ..........D==================================================================eER.......................  r7 = r7 | r9
    ..........D==================================================eE----------------R.......................  r9 = r2 | r10
    ...........D================================================================eE-R.......................  r10 = r12 << 0x7
    ...........D==================================================================eER......................  r7 = r7 | r10
    ...........D===================================================================eER.....................  r7 = r7 | r9
    ............D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..............  u8 [r8 + 153] = 0
    ............D===============================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 624] = a5
    ............D=============eeeeeeeeeeeeeeeeeeeeeeE-----------------------------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 1045 with total cost of 78:

```
    DeER.............................................................................  r1 = r1 + 0xffffffffffffff88
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  u64 [r1 + 112] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  u64 [r1 + 104] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  u64 [r1 + 96] = r6
    .D...............................................................................  r6 = r7
    .DeE------------------------R....................................................  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  u64 [r1 + 72] = r5
    ..D========================eER...................................................  r5 = r5 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = i32 [r5 + 592]
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u16 [r5 + 114]
    ...D=================================================eER.........................  r9 = r7 + 0x1
    ...D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 592] = r9
    ...D=================================================eE-------------------------R  jump 1101 if r8 == 0
```

Gas simulation at offset 1086 with total cost of 26:

```
    DeER.........................  r8 = r8 + 0xffffffffffffffff
    DeER.........................  r7 = r7 & 0x1
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 114] = r8
    D=eE------------------------R  jump 1152 if r7 == 0
```

Gas simulation at offset 1098 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 1402
```

Gas simulation at offset 1101 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r5 + 116]
    D=========================eE--------------R  jump 1135 if r8 == 0
```

Gas simulation at offset 1108 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r5 + 121]
    D=========================eE--------------R  jump 1135 if r8 == 0
```

Gas simulation at offset 1115 with total cost of 57:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.................  r8 = u8 [r5 + 118]
    D=========================eE--------------R.................  r8 = r8 + 0x1
    .D=========================eE-------------R.................  r9 = r8 & 0xff
    ..D=========================eeeE----------R.................  r9 = r9 <u 0x20
    ...D===========================eeE--------R.................  r8 = 0 if r9 == 0
    ...D=============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 118] = a1
    ....DeeE---------------------------------------------------R  fallthrough
```

Gas simulation at offset 1135 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = i16 [r5 + 112]
    D=========================eE--------------R...........  r8 = r8 + 0x1
    DeE---------------------------------------R...........  r7 = r7 & 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 114] = r8
    .DeE-------------------------------------------------R  jump 1402 if r7 != 0
```

Gas simulation at offset 1152 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u16 [r5 + 8]
    D=========================eE--------------R  jump 1221 if r7 == 0
```

Gas simulation at offset 1159 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r7 = r7 + 0xffffffffffffffff
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u16 [r5 + 32]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u16 [r5 + 8] = r7
    .D========================eE--------------R  jump 1252 if r8 == 0
```

Gas simulation at offset 1172 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r7 = r8 + 0xffffffffffffffff
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u16 [r5 + 56]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u16 [r5 + 32] = r7
    .D========================eE--------------R  jump 1283 if r8 == 0
```

Gas simulation at offset 1185 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r7 = r8 + 0xffffffffffffffff
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u16 [r5 + 136]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u16 [r5 + 56] = r7
    .D========================eE--------------R  jump 1334 if r8 == 0
```

Gas simulation at offset 1200 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 124]
    DeE---------------------------------------R  r8 = r8 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u16 [r5 + 136] = r8
    .D========================eE--------------R  r7 = r7 & 0x1
    .D=========================eE-------------R  jump 1379 if r7 == 0
```

Gas simulation at offset 1218 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 1402
```

Gas simulation at offset 1221 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r7 = u8 [r5 + 22]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = i16 [r5 + 6]
    DeE---------------------------------------R.............  r9 = 0x7
    .D========================eE--------------R.............  r10 = r7 + 0xffffffffffffffff
    .D=========================eeE------------R.............  r9 = r10 if r7 != 0
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 22] = a2
    ..D=======================eE---------------------------R  r7 = r8 + 0x1
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r8 = u16 [r5 + 32]
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u16 [r5 + 8] = r7
    ...D========================eE-------------------------R  jump 1172 if r8 != 0
```

Gas simulation at offset 1252 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r7 = u8 [r5 + 46]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = i16 [r5 + 30]
    DeE---------------------------------------R.............  r9 = 0x7
    .D========================eE--------------R.............  r10 = r7 + 0xffffffffffffffff
    .D=========================eeE------------R.............  r9 = r10 if r7 != 0
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 46] = a2
    ..D=======================eE---------------------------R  r7 = r8 + 0x1
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r8 = u16 [r5 + 56]
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u16 [r5 + 32] = r7
    ...D========================eE-------------------------R  jump 1185 if r8 != 0
```

Gas simulation at offset 1283 with total cost of 57:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.................  r7 = u16 [r5 + 58]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.................  r8 = u8 [r5 + 63]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.................  r9 = i16 [r5 + 54]
    .DeE--------------------------------------R.................  r11 = 0x6
    .D========================eeE-------------R.................  r11 = 0x1 if r8 == 0
    ..D=======================eE--------------R.................  r8 = r7 >> 0x1
    ...D========================eE------------R.................  r10 = r7 >> r11
    ...D=========================eE-----------R.................  r7 = r7 ^ r10
    ....D=========================eE----------R.................  r7 = r7 << 0x3f
    ....D==========================eE---------R.................  r7 = r7 >> 0x31
    ....D===========================eE--------R.................  r7 = r7 | r8
    ....D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 58] = r7
    .....D====================eE-------------------------------R  r7 = r9 + 0x1
    .....DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R  r8 = u16 [r5 + 136]
    .....D=====================eeeeeeeeeeeeeeeeeeeeeeeeeE------R  u16 [r5 + 56] = r7
    ......D========================eE--------------------------R  jump 1200 if r8 != 0
```

Gas simulation at offset 1334 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r7 = i16 [r5 + 126]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r8 = u8 [r5 + 141]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 136] = r7
    .D========================eE------------------------R  jump 1550 if r8 == 0
```

Gas simulation at offset 1350 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = u8 [r5 + 144]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = u8 [r5 + 124]
    D=========================eE--------------R...........  r8 = r8 + 0xffffffffffffffff
    .D=========================eE-------------R...........  r9 = r8 & 0xff
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 144] = a1
    .D==========================eeeeeeeeeeeeeeeeeeeeE----R  jump 1621 if r9 == 0
```

Gas simulation at offset 1373 with total cost of 2:

```
    DeER.  r7 = r7 & 0x1
    D=eER  jump 1402 if r7 != 0
```

Gas simulation at offset 1379 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u16 [r5 + 132]
    D=========================eE--------------R  jump 1402 if r7 == 0
```

Gas simulation at offset 1387 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r7 = i16 [r5 + 134]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 626] = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u8 [r5 + 630] = 0x1
    .DeeE-----------------------------------------------R  fallthrough
```

Gas simulation at offset 1402 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r5 + 104]
    DeE------------------------R  r8 = 0x3ff0000000000000
    DeeeeeeeeeeeeeeeE----------R  r0 = 24, jump 33002
```

Gas simulation at offset 1420 with total cost of 26:

```
    DeER.........................  r8 = r7 << 0x1
    D=eER........................  r8 = r8 >> 0x1
    .DeER........................  r9 = 0x7ff0000000000000
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r5 + 104] = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 64] = r6
    ..DeeeeeeeeeeeeeeeeeeeeE----R  jump 1459 if r9 <u r8
```

Gas simulation at offset 1445 with total cost of 2:

```
    DeER.  r8 = 0x40144ace15b7e8e7
    D=eER  jump 2893 if r7 <s r8
```

Gas simulation at offset 1459 with total cost of 15:

```
    DeER..............  r8 = 0xc0144ace15b7e8e7
    DeeeeeeeeeeeeeeeER  r0 = 26, jump 33002
```

Gas simulation at offset 1474 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u8 [r5 + 11]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r5 + 104] = r7
    D=========================eER  jump 1674 if r8 == 0
```

Gas simulation at offset 1484 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u16 [r5 + 6]
    DeE---------------------------------------R  r7 = 0
    D=========================eE--------------R  jump 1677 if r8 <u 8
```

Gas simulation at offset 1495 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r5 + 12]
    D=========================eE--------------R  jump 1677 if r9 == 0
```

Gas simulation at offset 1503 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 13]
    D=========================eE--------------R  jump 1773 if r7 == 0
```

Gas simulation at offset 1511 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 21]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r5 + 15]
    D=========================eE--------------R  r7 = r7 & 0xf
    .D=========================eE-------------R  r7 = r8 >> r7
    .D========================eE--------------R  jump 1664 if r9 == 0
```

Gas simulation at offset 1528 with total cost of 45:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.....  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.....  r9 = u8 [r5 + 16]
    D=========================eeeeeeeeeeeeeeeeeeeeER  jump 1760 if r9 == 0
```

Gas simulation at offset 1536 with total cost of 22:

```
    DeER.....................  r7 = r8 - r7
    D=eER....................  r7 = zext16 r7
    D==eeeeeeeeeeeeeeeeeeeeER  jump 1674 if r7 >u 2046
```

Gas simulation at offset 1547 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 1773
```

Gas simulation at offset 1550 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......  r7 = u8 [r5 + 143]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......  r8 = u8 [r5 + 145]
    .D========================eE--------------R......  r9 = r7 & 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeER  jump 1579 if r9 != 0
```

Gas simulation at offset 1565 with total cost of 1:

```
    DeER  jump 1591 if r8 <u 2
```

Gas simulation at offset 1569 with total cost of 26:

```
    DeER.........................  r8 = r8 + 0xfe
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 145] = a1
    DeeeeeeeeeeeeeeeE-----------R  jump 1591
```

Gas simulation at offset 1579 with total cost of 1:

```
    DeER  jump 1591 if r8 >=u 126
```

Gas simulation at offset 1583 with total cost of 26:

```
    DeER.........................  r8 = r8 + 0x2
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 145] = a1
    DeeE------------------------R  fallthrough
```

Gas simulation at offset 1591 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeE---------------------------------------R...........  r7 = r7 >> 0x1
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  u8 [r5 + 143] = a0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = u8 [r5 + 144]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  r7 = u8 [r5 + 124]
    .D========================eE--------------R...........  r8 = r8 + 0xffffffffffffffff
    .D=========================eE-------------R...........  r9 = r8 & 0xff
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 144] = a1
    ..D=========================eeeeeeeeeeeeeeeeeeeeE----R  jump 1373 if r9 != 0
```

Gas simulation at offset 1621 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u8 [r5 + 125]
    DeE------------------------R  r7 = r7 & 0x1
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 124] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 144] = 0x8
    .DeeeeeeeeeeeeeeeeeeeeE----R  jump 1649 if r7 == 0
```

Gas simulation at offset 1638 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 141] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 143] = a1
    DeeeeeeeeeeeeeeeE----------R  jump 1379
```

Gas simulation at offset 1649 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 141] = 0x1
    DeE------------------------R  r7 = r7 & 0x1
    D=eE-----------------------R  jump 1379 if r7 == 0
```

Gas simulation at offset 1661 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 1402
```

Gas simulation at offset 1664 with total cost of 3:

```
    DeER..  r7 = r7 + r8
    D=eER.  r7 = zext16 r7
    D==eER  jump 1773 if r7 <=u 2046
```

Gas simulation at offset 1674 with total cost of 2:

```
    DeER.  r7 = 0
    DeeER  fallthrough
```

Gas simulation at offset 1677 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r5 + 35]
    D=========================eE--------------R  jump 1822 if r8 == 0
```

Gas simulation at offset 1685 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u16 [r5 + 30]
    DeE---------------------------------------R  r8 = 0
    D=========================eE--------------R  jump 1822 if r9 <u 8
```

Gas simulation at offset 1696 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r10 = u8 [r5 + 36]
    D=========================eE--------------R  jump 1822 if r10 == 0
```

Gas simulation at offset 1703 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r5 + 37]
    D=========================eE--------------R  jump 1858 if r8 == 0
```

Gas simulation at offset 1711 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r5 + 45]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r10 = u8 [r5 + 39]
    D=========================eE--------------R  r8 = r8 & 0xf
    .D=========================eE-------------R  r8 = r9 >> r8
    .D========================eE--------------R  jump 1746 if r10 == 0
```

Gas simulation at offset 1727 with total cost of 45:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.....  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.....  r10 = u8 [r5 + 40]
    D=========================eeeeeeeeeeeeeeeeeeeeER  jump 1845 if r10 == 0
```

Gas simulation at offset 1734 with total cost of 22:

```
    DeER.....................  r8 = r9 - r8
    D=eER....................  r8 = zext16 r8
    D==eeeeeeeeeeeeeeeeeeeeER  jump 1756 if r8 >u 2046
```

Gas simulation at offset 1744 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 1858
```

Gas simulation at offset 1746 with total cost of 3:

```
    DeER..  r8 = r8 + r9
    D=eER.  r8 = zext16 r8
    D==eER  jump 1858 if r8 <=u 2046
```

Gas simulation at offset 1756 with total cost of 15:

```
    DeER..............  r8 = 0
    DeeeeeeeeeeeeeeeER  jump 1822
```

Gas simulation at offset 1760 with total cost of 4:

```
    DeER...  r7 = r7 ^ 0xffffffffffffffff
    D=eER..  r7 = r7 + r8
    D==eER.  r7 = zext16 r7
    D===eER  jump 1674 if r7 >u 2046
```

Gas simulation at offset 1773 with total cost of 77:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.....................................  r7 = u8 [r5 + 17]
    DeE---------------------------------------R.....................................  r8 = 0x172d0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.....................................  r9 = u8 [r5 + 22]
    .D========================eE--------------R.....................................  r7 = r7 << 0x3
    .D=========================eE-------------R.....................................  r7 = r7 + r8
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u64 [r7 + 0]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.........................  r8 = u8 [r5 + 0]
    ..DeE-------------------------------------------------R.........................  r10 = r1 + 0x58
    ..D=======================eE--------------------------R.........................  r9 = r9 + r10
    ..D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 88] = r7
    ...D=======================eE--------------------------------------------------R  r7 = r5 - r8
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r8 = u8 [r9 + 0]
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r7 = u8 [r7 + 4]
    ....D================================================eeeE----------------------R  r7 = r7 * r8
    ....DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------------------------------R  r8 = u8 [r5 + 35]
    ....D=========================eE-----------------------------------------------R  jump 1685 if r8 != 0
```

Gas simulation at offset 1822 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u16 [r5 + 112]
    D=========================eE--------------R  jump 1911 if r9 >=u 2
```

Gas simulation at offset 1830 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r11 = 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r5 + 61]
    DeE---------------------------------------R  r6 = 0
    .D========================eE--------------R  jump 1944 if r9 != 0
```

Gas simulation at offset 1842 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 1980
```

Gas simulation at offset 1845 with total cost of 4:

```
    DeER...  r8 = r8 ^ 0xffffffffffffffff
    D=eER..  r8 = r8 + r9
    D==eER.  r8 = zext16 r8
    D===eER  jump 1756 if r8 >u 2046
```

Gas simulation at offset 1858 with total cost of 77:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.....................................  r8 = u8 [r5 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.....................................  r9 = u8 [r5 + 41]
    DeE---------------------------------------R.....................................  r10 = 0x172d0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.....................................  r11 = u8 [r5 + 46]
    .DeE--------------------------------------R.....................................  r12 = r1 + 0x58
    .D========================eE--------------R.....................................  r9 = r9 << 0x3
    ..D========================eE-------------R.....................................  r9 = r9 + r10
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r9 = u64 [r9 + 0]
    ..D========================eE-------------------------R.........................  r11 = r11 + r12
    ...DeE------------------------------------------------R.........................  r10 = r5 + 0x18
    ...D======================eE--------------------------R.........................  r10 = r10 - r8
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 88] = r9
    ....D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u8 [r11 + 0]
    ....D======================eeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r9 = u8 [r10 + 4]
    ....D================================================eeeE----------------------R  r8 = r9 * r8
    ....DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------------------------------R  r9 = u16 [r5 + 112]
    .....D========================eE-----------------------------------------------R  jump 1830 if r9 <u 2
```

Gas simulation at offset 1911 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r5 + 118]
    D=========================eE--------------R  jump 1932 if r9 >=u 16
```

Gas simulation at offset 1919 with total cost of 26:

```
    DeeER........................  r11 = 0xf - r9
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r9 = u8 [r5 + 61]
    .DeE-----------------------R.  r6 = 0
    .D========================eER  jump 1944 if r9 != 0
```

Gas simulation at offset 1930 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 1980
```

Gas simulation at offset 1932 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r11 = r9 + 0xfffffffffffffff0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r5 + 61]
    .DeE--------------------------------------R  r6 = 0
    .D========================eE--------------R  jump 1980 if r9 == 0
```

Gas simulation at offset 1944 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r5 + 62]
    D=========================eE--------------R  jump 1980 if r9 == 0
```

Gas simulation at offset 1951 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u16 [r5 + 58]
    D=========================eE--------------R  r9 = r9 & 0x1
    D==========================eE-------------R  jump 2307 if r9 != 0
```

Gas simulation at offset 1962 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r9 = u8 [r5 + 48]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r10 = u64 [r1 + 64]
    D=========================eE--------------R............  r9 = r10 - r9
    .D=========================eE-------------R............  r9 = r9 + 0x7ff
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u8 [r9 + 53]
    .DeeE-------------------------------------------------R  fallthrough
```

Gas simulation at offset 1980 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r10 = u8 [r5 + 145]
    DeE---------------------------------------R..........  r9 = r8 | r7
    .DeE--------------------------------------R..........  r9 = r9 & 0xff
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 80] = r10
    .D=eeeeeeeeeeeeeeeeeeeeE----------------------------R  jump 2158 if r9 == 0
```

Gas simulation at offset 1999 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r11
    DeE------------------------R  r7 = r7 & 0xff
    D=eeeeeeeeeeeeeeeeeeeeE----R  jump 2051 if r7 == 0
```

Gas simulation at offset 2009 with total cost of 14:

```
    DeER.............  i32 r9 = clz r7
    D=eeER...........  i32 r7 = r7 << r9
    .DeE-R...........  r9 = r9 << 0x17
    .D==eeER.........  i32 r10 = r7 >> 0x8
    ..D=eE-R.........  r11 = r7 >> 0x7
    ...D==eeER.......  r11 = r11 & ~r10
    ....D=eeER.......  i32 r10 = r10 - r9
    ....DeE--R.......  r7 = r7 << 0x18
    ....D===eER......  r11 = r11 & 0x1
    .....D===eeER....  i32 r7 = r7 - r11
    .....D=====eeER..  i32 r7 = r7 >> 0x1f
    ......D=eE----R..  r9 = r10 + 0x4e800000
    ......D======eeER  i32 r7 = r7 + r9
    .......DeeE-----R  fallthrough
```

Gas simulation at offset 2051 with total cost of 21:

```
    DeER....................  r8 = r8 & 0xff
    D=eeeeeeeeeeeeeeeeeeeeER  jump 2105 if r8 == 0
```

Gas simulation at offset 2058 with total cost of 22:

```
    DeER.....................  i32 r9 = clz r8
    D=eeER...................  i32 r8 = r8 << r9
    .DeE-R...................  r9 = r9 << 0x17
    .D==eeER.................  i32 r10 = r8 >> 0x8
    ..D=eE-R.................  r11 = r8 >> 0x7
    ...D==eeER...............  r11 = r11 & ~r10
    ....D=eeER...............  i32 r10 = r10 - r9
    ....DeE--R...............  r8 = r8 << 0x18
    ....D===eER..............  r11 = r11 & 0x1
    .....D===eeER............  i32 r8 = r8 - r11
    .....D=====eeER..........  i32 r8 = r8 >> 0x1f
    ......D=eE----R..........  r9 = r10 + 0x4e800000
    ......D======eeER........  i32 r8 = r8 + r9
    .......DeE------R........  r0 = 0x1c
    .......DeeeeeeeeeeeeeeeER  jump 33520
```

Gas simulation at offset 2105 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  r0 = 28, jump 33520
```

Gas simulation at offset 2110 with total cost of 16:

```
    DeeER..............  i32 r8 = r7 + 0
    DeE-R..............  r7 = 0x45fe0000
    .DeeeeeeeeeeeeeeeER  r0 = 30, jump 34436
```

Gas simulation at offset 2123 with total cost of 15:

```
    DeeER.............  i32 r7 = r7 + 0
    DeE-R.............  r8 = 0x42c80000
    DeeeeeeeeeeeeeeeER  r0 = 32, jump 33520
```

Gas simulation at offset 2136 with total cost of 16:

```
    DeeER..............  i32 r8 = r7 + 0
    DeE-R..............  r7 = 0x42bfc28f
    .DeeeeeeeeeeeeeeeER  r0 = 34, jump 34436
```

Gas simulation at offset 2149 with total cost of 25:

```
    D...........................  r9 = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r10 = u64 [r1 + 80]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r11 = u64 [r1 + 56]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 2158 with total cost of 23:

```
    DeER......................  r7 = r6 | r11
    D=eER.....................  r7 = r7 | r10
    D==eER....................  r7 = r7 & 0xff
    .D==eeeeeeeeeeeeeeeeeeeeER  jump 2480 if r7 == 0
```

Gas simulation at offset 2172 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r9
    DeE------------------------R  r7 = r11 & 0xff
    D=eeeeeeeeeeeeeeeeeeeeE----R  jump 2235 if r7 == 0
```

Gas simulation at offset 2182 with total cost of 22:

```
    DeER.....................  i32 r8 = clz r7
    D=eeER...................  i32 r7 = r7 << r8
    .DeE-R...................  r8 = r8 << 0x17
    .D==eeER.................  i32 r9 = r7 >> 0x8
    ..D=eE-R.................  r10 = r7 >> 0x7
    ...D==eeER...............  r10 = r10 & ~r9
    ....D=eeER...............  i32 r9 = r9 - r8
    ....DeE--R...............  r7 = r7 << 0x18
    ....D===eER..............  r10 = r10 & 0x1
    .....D===eeER............  i32 r7 = r7 - r10
    .....D=====eeER..........  i32 r7 = r7 >> 0x1f
    ......D=eE----R..........  r8 = r9 + 0x4e800000
    ......D======eeER........  i32 r7 = r7 + r8
    .......DeE------R........  r8 = 0x46008c00
    .......DeE------R........  r0 = 0x24
    .......DeeeeeeeeeeeeeeeER  jump 34436
```

Gas simulation at offset 2235 with total cost of 15:

```
    DeER..............  r8 = 0x46008c00
    DeeeeeeeeeeeeeeeER  r0 = 36, jump 34436
```

Gas simulation at offset 2246 with total cost of 27:

```
    DeeER.........................  i32 r7 = r7 + 0
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 48] = r7
    DeeeeeeeeeeeeeeeeeeeeE-------R  jump 2331 if r6 == 0
```

Gas simulation at offset 2254 with total cost of 23:

```
    DeER......................  i32 r7 = clz r6
    .DeeER....................  i32 r8 = r6 << r7
    ..DeER....................  r7 = r7 << 0x17
    ..D=eeER..................  i32 r9 = r8 >> 0x8
    ...DeE-R..................  r10 = r8 >> 0x7
    ....D=eeER................  r10 = r10 & ~r9
    .....DeeER................  i32 r9 = r9 - r7
    .....DeE-R................  r8 = r8 << 0x18
    .....D==eER...............  r10 = r10 & 0x1
    ......D==eeER.............  i32 r8 = r8 - r10
    ......D====eeER...........  i32 r8 = r8 >> 0x1f
    .......DeE----R...........  r7 = r9 + 0x4e800000
    .......D=====eeER.........  i32 r7 = r7 + r8
    ........DeE-----R.........  r8 = 0x463f4400
    ........DeE-----R.........  r0 = 0x26
    ........DeeeeeeeeeeeeeeeER  jump 34436
```

Gas simulation at offset 2307 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeE---------------------------------------R..........  r6 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r10 = u8 [r5 + 145]
    .DeE--------------------------------------R..........  r9 = r8 | r7
    .D=eE-------------------------------------R..........  r9 = r9 & 0xff
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 80] = r10
    ..D=eeeeeeeeeeeeeeeeeeeeE---------------------------R  jump 1999 if r9 != 0
```

Gas simulation at offset 2328 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 2158
```

Gas simulation at offset 2331 with total cost of 15:

```
    DeER..............  r7 = 0
    DeER..............  r8 = 0x463f4400
    DeeeeeeeeeeeeeeeER  r0 = 38, jump 34436
```

Gas simulation at offset 2344 with total cost of 25:

```
    DeeER.......................  i32 r8 = r7 + 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 48]
    .DeeeeeeeeeeeeeeeE---------R  r0 = 40, jump 33520
```

Gas simulation at offset 2354 with total cost of 45:

```
    DeeER...........................................  i32 r6 = r7 + 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER....................  r8 = u64 [r1 + 80]
    .D========================eeeeeeeeeeeeeeeeeeeeER  jump 2415 if r8 == 0
```

Gas simulation at offset 2362 with total cost of 22:

```
    DeER.....................  i32 r7 = clz r8
    D=eeER...................  i32 r8 = r8 << r7
    .DeE-R...................  r7 = r7 << 0x17
    .D==eeER.................  i32 r9 = r8 >> 0x8
    ..D=eE-R.................  r10 = r8 >> 0x7
    ...D==eeER...............  r10 = r10 & ~r9
    ....D=eeER...............  i32 r9 = r9 - r7
    ....DeE--R...............  r8 = r8 << 0x18
    ....D===eER..............  r10 = r10 & 0x1
    .....D===eeER............  i32 r8 = r8 - r10
    .....D=====eeER..........  i32 r8 = r8 >> 0x1f
    ......D=eE----R..........  r7 = r9 + 0x4e800000
    ......D======eeER........  i32 r7 = r7 + r8
    .......DeE------R........  r8 = 0x46b0dc00
    .......DeE------R........  r0 = 0x2a
    .......DeeeeeeeeeeeeeeeER  jump 34436
```

Gas simulation at offset 2415 with total cost of 15:

```
    DeER..............  r7 = 0
    DeER..............  r8 = 0x46b0dc00
    DeeeeeeeeeeeeeeeER  r0 = 42, jump 34436
```

Gas simulation at offset 2428 with total cost of 16:

```
    DeeER..............  i32 r8 = r7 + 0
    D..................  r7 = r6
    .DeeeeeeeeeeeeeeeER  r0 = 44, jump 33520
```

Gas simulation at offset 2437 with total cost of 16:

```
    DeeER..............  i32 r8 = r7 + 0
    DeE-R..............  r7 = 0x3f800000
    .DeeeeeeeeeeeeeeeER  r0 = 46, jump 34436
```

Gas simulation at offset 2450 with total cost of 15:

```
    DeeER.............  i32 r7 = r7 + 0
    DeE-R.............  r8 = 0x42c80000
    DeeeeeeeeeeeeeeeER  r0 = 48, jump 33520
```

Gas simulation at offset 2463 with total cost of 16:

```
    DeeER..............  i32 r8 = r7 + 0
    DeE-R..............  r7 = 0x431fca3d
    .DeeeeeeeeeeeeeeeER  r0 = 50, jump 34436
```

Gas simulation at offset 2476 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r9 = u64 [r1 + 56]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 2480 with total cost of 17:

```
    DeeER...............  i32 r9 = r9 + 0
    .DeeER..............  i32 r8 = r7 + 0
    .D..................  r7 = r9
    ..DeeeeeeeeeeeeeeeER  r0 = 52, jump 33520
```

Gas simulation at offset 2491 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = i32 [r5 + 100]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 24] = r7
    DeE------------------------R  r7 = 0x3f639ff9
    DeeeeeeeeeeeeeeeE----------R  r0 = 54, jump 33992
```

Gas simulation at offset 2508 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = i32 [r5 + 88]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u64 [r1 + 48] = r7
    DeE-------------------------------------------------R  r7 = 0xffffffffbfe7002f
    .DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 56, jump 33992
```

Gas simulation at offset 2528 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = i32 [r5 + 96]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 40] = r7
    DeE------------------------R  r7 = 0x3f8b0904
    D...........................  r8 = r6
    .DeeeeeeeeeeeeeeeE---------R  r0 = 58, jump 33992
```

Gas simulation at offset 2547 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = i32 [r5 + 84]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 80] = r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u64 [r1 + 32] = r7
    DeE-------------------------------------------------R  r7 = 0xffffffffc0000000
    .DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 60, jump 33992
```

Gas simulation at offset 2567 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r7
    DeE------------------------R  r7 = 0x3f79896a
    D...........................  r8 = r6
    DeeeeeeeeeeeeeeeE----------R  r0 = 62, jump 33992
```

Gas simulation at offset 2583 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = i32 [r5 + 92]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeE------------------------R  r7 = 0x3f4eba39
    DeeeeeeeeeeeeeeeE----------R  r0 = 64, jump 33992
```

Gas simulation at offset 2599 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = i32 [r1 + 24]
    DeE------------------------R  r7 = 0x3cb94332
    DeeeeeeeeeeeeeeeE----------R  r0 = 66, jump 33992
```

Gas simulation at offset 2616 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = i32 [r5 + 80]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 24] = r8
    D....................................................  r6 = r7
    DeE-------------------------------------------------R  r7 = 0xffffffffbfe4746c
    .DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 68, jump 33992
```

Gas simulation at offset 2635 with total cost of 16:

```
    DeER...............  r7 = r7 ^ 0xffffffff80000000
    DeeER..............  i32 r8 = r6 + 0
    .DeeER.............  i32 r7 = r7 + 0
    .DeeeeeeeeeeeeeeeER  r0 = 70, jump 33520
```

Gas simulation at offset 2650 with total cost of 28:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...  r8 = u64 [r1 + 8]
    D=========================eER..  r8 = r8 ^ 0xffffffff80000000
    DeeE------------------------R..  i32 r7 = r7 + 0
    .D=========================eeER  i32 r8 = r8 + 0
    .DeeeeeeeeeeeeeeeE------------R  r0 = 72, jump 33520
```

Gas simulation at offset 2668 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r7
    DeeE-----------------------R  i32 r8 = r7 + 0
    .DeE-----------------------R  r7 = 0x3d34a6a0
    .DeeeeeeeeeeeeeeeE---------R  r0 = 74, jump 33992
```

Gas simulation at offset 2684 with total cost of 25:

```
    D...........................  r6 = r7
    DeER........................  r7 = 0xffffffffbfeccd54
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u64 [r1 + 80]
    DeeeeeeeeeeeeeeeE----------R  r0 = 76, jump 33992
```

Gas simulation at offset 2700 with total cost of 16:

```
    DeER...............  r7 = r7 ^ 0xffffffff80000000
    DeeER..............  i32 r8 = r6 + 0
    .DeeER.............  i32 r7 = r7 + 0
    .DeeeeeeeeeeeeeeeER  r0 = 78, jump 33520
```

Gas simulation at offset 2715 with total cost of 28:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...  r8 = u64 [r1 + 0]
    D=========================eER..  r8 = r8 ^ 0xffffffff80000000
    DeeE------------------------R..  i32 r7 = r7 + 0
    .D=========================eeER  i32 r8 = r8 + 0
    .DeeeeeeeeeeeeeeeE------------R  r0 = 80, jump 33520
```

Gas simulation at offset 2732 with total cost of 16:

```
    D..................  r6 = r7
    DeeER..............  i32 r8 = r7 + 0
    .DeER..............  r7 = 0x3f8b3765
    .DeeeeeeeeeeeeeeeER  r0 = 82, jump 33992
```

Gas simulation at offset 2747 with total cost of 25:

```
    DeeER.......................  i32 r7 = r7 + 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = i32 [r1 + 16]
    DeeeeeeeeeeeeeeeE----------R  r0 = 84, jump 33520
```

Gas simulation at offset 2757 with total cost of 25:

```
    DeeER.......................  i32 r7 = r7 + 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = i32 [r1 + 32]
    DeeeeeeeeeeeeeeeE----------R  r0 = 86, jump 33520
```

Gas simulation at offset 2767 with total cost of 28:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...  r8 = u64 [r1 + 40]
    D=========================eER..  r8 = r8 ^ 0xffffffff80000000
    DeeE------------------------R..  i32 r7 = r7 + 0
    .D=========================eeER  i32 r8 = r8 + 0
    .DeeeeeeeeeeeeeeeE------------R  r0 = 88, jump 33520
```

Gas simulation at offset 2785 with total cost of 28:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...  r8 = u64 [r1 + 48]
    D=========================eER..  r8 = r8 ^ 0xffffffff80000000
    DeeE------------------------R..  i32 r7 = r7 + 0
    .D=========================eeER  i32 r8 = r8 + 0
    .DeeeeeeeeeeeeeeeE------------R  r0 = 90, jump 33520
```

Gas simulation at offset 2803 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = u8 [r5 + 154]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = u64 [r1 + 8]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u32 [r5 + 80] = r9
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R..................................................  u32 [r5 + 84] = r6
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R..................................................  u32 [r5 + 88] = r7
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r7 = u64 [r1 + 24]
    .D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u32 [r5 + 92] = r7
    .D========================eE-------------------------------------------------R.........................  r8 = r8 + 0x1
    ..D========================eE------------------------------------------------R.........................  r9 = r8 & 0xff
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R.........................  r10 = u64 [r1 + 80]
    ..D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u32 [r5 + 96] = r10
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R........................  r10 = u64 [r1 + 56]
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u32 [r5 + 100] = r10
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeE--R.......................  u8 [r5 + 154] = a1
    ...D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 64]
    ....D=======================================================================eE------------------------R  jump 2893 if r9 <u 8
```

Gas simulation at offset 2855 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r7 = i32 [r5 + 604]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u8 [r5 + 154] = 0
    .D========================eeE-------------R............  i32 r7 = r7 + 0x1
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 604] = r7
    .D==========================eE------------------------R  jump 2893 if r7 <u 735
```

Gas simulation at offset 2876 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = i32 [r5 + 600]
    D=========================eE--------------R...........  r7 = r7 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 600] = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u32 [r5 + 604] = 0
    .DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 2893 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = i16 [r5 + 148]
    DeE---------------------------------------R...........  r8 = 0xffff000000000000
    .D========================eE--------------R...........  r9 = r7 << 0x30
    .D=========================eE-------------R...........  r8 = r8 + r9
    .D========================eE--------------R...........  r7 = r7 + 0xffffffffffffffff
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 148] = r7
    ..D=========================eE-----------------------R  jump 3265 if r8 == 0
```

Gas simulation at offset 2925 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r5 + 146]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 147]
    DeE---------------------------------------R  r9 = 0x2
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u8 [r5 + 146] = a2
    .D========================eE--------------R  jump 2993 if r8 == r9
```

Gas simulation at offset 2944 with total cost of 56:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER................  unlikely
    DeE---------------------------------------R................  r8 = r8 & 0x1
    DeE---------------------------------------R................  r9 = 0x17bf4
    DeE---------------------------------------R................  r10 = 0x17c3c
    .DeE--------------------------------------R................  r11 = 0x1
    .DeeE-------------------------------------R................  r10 = r9 if r8 == 0
    ..DeeE------------------------------------R................  r7 = r11 & ~r7
    ...D=eE-----------------------------------R................  r9 = r7 << 0x3
    ...D==eE----------------------------------R................  r9 = r9 + r10
    ...D===eeeeeeeeeeeeeeeeeeeeeeeeeE---------R................  r9 = i16 [r9 + 0]
    ....DeE-----------------------------------R................  r8 = r8 ^ 0x9
    ....DeeeeeeeeeeeeeeeeeeeeeeeeeE-----------R................  u64 [r5 + 64] = r10
    ....D=eeeeeeeeeeeeeeeeeeeeeeeeeE----------R................  u64 [r5 + 72] = r8
    ....D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 148] = r9
    .....DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u8 [r5 + 153] = a0
    .....DeeE-------------------------------------------------R  fallthrough
```

Gas simulation at offset 2993 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u64 [r5 + 512]
    D=========================eE--------------R  jump 3101 if r7 != 0
```

Gas simulation at offset 3001 with total cost of 26:

```
    DeER.........................  r8 = 0x30a98
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 80] = r8
    D=eE------------------------R  r7 = r8 + 0x2750
    .D=eE-----------------------R  r7 = r7 & 0xfffffffffffffffc
    .DeE------------------------R  r8 = 0x1
    .DeeE-----------------------R  fallthrough
```

Gas simulation at offset 3020 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r8 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r9 = i32 [r7 + 0]
    .D=========================eE-------------R............  r4 = r9 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r9 = r9 & 0xff
    ..D=========================eE------------------------R  jump 3020 if r9 != 0
```

Gas simulation at offset 3051 with total cost of 15:

```
    DeER..............  r7 = 0xf00
    DeER..............  r8 = 0
    DeeeeeeeeeeeeeeeER  r0 = 92, jump 26445
```

Gas simulation at offset 3062 with total cost of 51:

```
    D.....................................................  r6 = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u64 [r1 + 80]
    D=========================eER.........................  r7 = r8 + 0x2000
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 1872] = 0
    .DeE-------------------------------------------------R  jump 32020 if r6 == 0
```

Gas simulation at offset 3079 with total cost of 15:

```
    DeER..............  r9 = 0x1e000
    D.................  r7 = r6
    DeER..............  r8 = 0
    DeeeeeeeeeeeeeeeER  r0 = 94, jump 27934
```

Gas simulation at offset 3093 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r5 + 512] = r6
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 64]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 3101 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = i16 [r5 + 544]
    DeE---------------------------------------R..................................  r8 = 0x18518
    D=========================eE--------------R..................................  r7 = r7 << 0x3
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R..................................  u64 [r1 + 72] = r8
    .D=========================eE-------------R..................................  r7 = r7 + r8
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r8 = u64 [r7 + 0]
    .D...........................................................................  r7 = r6
    ..D==================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 96, jump [r8 + 0]
```

Gas simulation at offset 3128 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r8 = u8 [r5 + 558]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r7 = i16 [r5 + 544]
    D=========================eER............................  r9 = r8 << 0x1
    .D========================eER............................  r10 = r8 << 0x3
    .D=========================eER...........................  r9 = r10 - r9
    .DeE-------------------------R...........................  r10 = 0x172f0
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 80] = r10
    ..D=========================eER..........................  r9 = r9 + r10
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r10 = u16 [r9 + 4]
    ..D=======================eE---------------------------R.  r7 = r7 + 0x1
    ...D=======================eE--------------------------R.  r11 = zext16 r7
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE--R.  u16 [r5 + 544] = r7
    ...D==================================================eER  jump 3500 if r10 >=u r11
```

Gas simulation at offset 3172 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = i16 [r5 + 542]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r10 = u16 [r9 + 0]
    D=========================eE--------------R...........  r7 = r7 + 0x1
    .D=========================eE-------------R...........  r11 = zext16 r7
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 542] = r7
    .D==========================eE-----------------------R  jump 3252 if r11 != r10
```

Gas simulation at offset 3191 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r5 + 557]
    D=========================eE--------------R.............  r10 = r9 << 0x2
    .DeE--------------------------------------R.............  r7 = 0x17250
    .D=========================eE-------------R.............  r10 = r10 + r7
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r12 = u8 [r10 + 3]
    ..DeE-------------------------------------------------R.  r11 = r8 + 0x1
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  u16 [r5 + 542] = 0
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R.  u8 [r5 + 558] = a4
    ...D=================================================eER  jump 3309 if r8 >=u r12
```

Gas simulation at offset 3224 with total cost of 78:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......................................  unlikely
    DeE---------------------------------------R......................................  r7 = r11 << 0x1
    DeE---------------------------------------R......................................  r11 = r11 << 0x3
    .DeE--------------------------------------R......................................  r11 = r11 - r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R......................................  r9 = u64 [r1 + 80]
    .D=========================eE-------------R......................................  r9 = r9 + r11
    .D==========================eE------------R......................................  r9 = r9 + 0x2
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u16 [r9 + 0]
    ..D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r7
    ..DeeeeeeeeeeeeeeeE-------------------------------------------------------------R  jump 3500
```

Gas simulation at offset 3252 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeE---------------------------------------R...........  r9 = r9 + 0x2
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  r7 = u16 [r9 + 0]
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r7
    .DeeeeeeeeeeeeeeeE-----------------------------------R  jump 3500
```

Gas simulation at offset 3265 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 153]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u64 [r5 + 72]
    D=========================eE--------------R  jump 5284 if r7 >=u r8
```

Gas simulation at offset 3277 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r6 = u64 [r5 + 64]
    DeE---------------------------------------R............  r7 = r7 << 0x3
    D=========================eE--------------R............  r6 = r6 + r7
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r6 + 6]
    .D==================================================eER  jump 3389 if r7 == 0
```

Gas simulation at offset 3293 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 122]
    D=========================eE--------------R  jump 3364 if r7 == 0
```

Gas simulation at offset 3300 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r7 = u8 [r5 + 117]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 116] = a0
    DeeeeeeeeeeeeeeeE-----------------------------------R  jump 3378
```

Gas simulation at offset 3309 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = i16 [r5 + 540]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r11 = u16 [r10 + 0]
    D=========================eE--------------R...........  r8 = r8 + 0x1
    .D=========================eE-------------R...........  r12 = zext16 r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 540] = r8
    .D==========================eeeeeeeeeeeeeeeeeeeeE----R  jump 3467 if r12 != r11
```

Gas simulation at offset 3329 with total cost of 26:

```
    DeER.........................  r8 = r9 + 0x1
    DeER.........................  r10 = 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r5 + 540] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = a1
    .DeeeeeeeeeeeeeeeeeeeeE-----R  jump 3353 if r9 != r10
```

Gas simulation at offset 3346 with total cost of 25:

```
    DeER........................  r8 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = 0
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 3353 with total cost of 27:

```
    DeER..........................  r8 = r8 << 0x2
    D=eER.........................  r7 = r7 + r8
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 2]
    DeeeeeeeeeeeeeeeE------------R  jump 3471
```

Gas simulation at offset 3364 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 116]
    D=========================eE--------------R  jump 3378 if r7 == 0
```

Gas simulation at offset 3371 with total cost of 26:

```
    DeER.........................  r7 = r7 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 116] = a0
    DeeE------------------------R  fallthrough
```

Gas simulation at offset 3378 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 119]
    D=========================eE--------------R  jump 3389 if r7 != 0
```

Gas simulation at offset 3385 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 122] = 0
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 3389 with total cost of 45:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.....  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.....  r7 = u8 [r6 + 5]
    D=========================eeeeeeeeeeeeeeeeeeeeER  jump 3414 if r7 == 0
```

Gas simulation at offset 3396 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 98, jump 61
```

Gas simulation at offset 3403 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u64 [r1 + 72]
    D=========================eER  r7 = r7 + 0x19
    DeeeeeeeeeeeeeeeE-----------R  r0 = 100, jump 61
```

Gas simulation at offset 3414 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r6 + 7]
    D=========================eER  jump 5112 if r7 == 0
```

Gas simulation at offset 3421 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 2]
    D=========================eE--------------R  jump 3450 if r7 == 0
```

Gas simulation at offset 3428 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = u8 [r5 + 3]
    DeE---------------------------------------R...........  r8 = 0xf
    D=========================eE--------------R...........  r7 = r7 + 0x1
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  u8 [r5 + 2] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  u8 [r5 + 4] = a1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 5] = a0
    .DeeeeeeeeeeeeeeeE-----------------------------------R  jump 4960
```

Gas simulation at offset 3450 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 5]
    D=========================eE--------------R  jump 3717 if r7 == 0
```

Gas simulation at offset 3458 with total cost of 26:

```
    DeER.........................  r7 = r7 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 5] = a0
    DeeeeeeeeeeeeeeeE-----------R  jump 4960
```

Gas simulation at offset 3467 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r10 + 2]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 3471 with total cost of 78:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u8 [r5 + 558] = a0
    DeE------------------------R.....................................................  r8 = r7 << 0x1
    DeE------------------------R.....................................................  r7 = r7 << 0x3
    .DeE-----------------------R.....................................................  r7 = r7 - r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r8 = u64 [r1 + 80]
    .D=========================eER...................................................  r7 = r7 + r8
    ..D=========================eER..................................................  r9 = r7 + 0x2
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u16 [r9 + 0]
    ..D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r7
    ...DeeE-------------------------------------------------------------------------R  fallthrough
```

Gas simulation at offset 3500 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r5 + 571]
    D=========================eE--------------R  jump 3773 if r8 == 0
```

Gas simulation at offset 3509 with total cost of 73:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.................................  unlikely
    DeE---------------------------------------R.................................  r7 = sext16 r7
    D=eE--------------------------------------R.................................  r7 = r7 << 0x3
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.................................  r8 = u64 [r1 + 72]
    .D========================eE--------------R.................................  r7 = r7 + r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r8 = u64 [r7 + 0]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R......................  u8 [r5 + 571] = 0
    .D..........................................................................  r7 = r6
    ..D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 102, jump [r8 + 0]
```

Gas simulation at offset 3533 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r8 = u8 [r5 + 558]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r7 = i16 [r5 + 544]
    D=========================eER............................  r9 = r8 << 0x1
    .D========================eER............................  r10 = r8 << 0x3
    .D=========================eER...........................  r9 = r10 - r9
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R...........................  r10 = u64 [r1 + 80]
    ..D=========================eER..........................  r9 = r9 + r10
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r10 = u16 [r9 + 4]
    ..D=======================eE---------------------------R.  r7 = r7 + 0x1
    ..D========================eE--------------------------R.  r11 = zext16 r7
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE--R.  u16 [r5 + 544] = r7
    ...D==================================================eER  jump 3773 if r10 >=u r11
```

Gas simulation at offset 3572 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = i16 [r5 + 542]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r10 = u16 [r9 + 0]
    D=========================eE--------------R...........  r7 = r7 + 0x1
    .D=========================eE-------------R...........  r11 = zext16 r7
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 542] = r7
    .D==========================eE-----------------------R  jump 3651 if r11 != r10
```

Gas simulation at offset 3591 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r5 + 557]
    D=========================eE--------------R.............  r10 = r9 << 0x2
    .DeE--------------------------------------R.............  r7 = 0x17250
    .D=========================eE-------------R.............  r10 = r10 + r7
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r12 = u8 [r10 + 3]
    ..DeE-------------------------------------------------R.  r11 = r8 + 0x1
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  u16 [r5 + 542] = 0
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R.  u8 [r5 + 558] = a4
    ...D=================================================eER  jump 3663 if r8 >=u r12
```

Gas simulation at offset 3624 with total cost of 78:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......................................  unlikely
    DeE---------------------------------------R......................................  r7 = r11 << 0x1
    DeE---------------------------------------R......................................  r11 = r11 << 0x3
    .DeE--------------------------------------R......................................  r11 = r11 - r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R......................................  r9 = u64 [r1 + 80]
    .D=========================eE-------------R......................................  r9 = r9 + r11
    .D==========================eE------------R......................................  r9 = r9 + 0x2
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u16 [r9 + 0]
    ..D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r7
    ..DeeeeeeeeeeeeeeeE-------------------------------------------------------------R  jump 3773
```

Gas simulation at offset 3651 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeE---------------------------------------R...........  r9 = r9 + 0x2
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  r7 = u16 [r9 + 0]
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r7
    .DeeeeeeeeeeeeeeeE-----------------------------------R  jump 3773
```

Gas simulation at offset 3663 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = i16 [r5 + 540]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r11 = u16 [r10 + 0]
    D=========================eE--------------R...........  r8 = r8 + 0x1
    .D=========================eE-------------R...........  r12 = zext16 r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 540] = r8
    .D==========================eeeeeeeeeeeeeeeeeeeeE----R  jump 3740 if r12 != r11
```

Gas simulation at offset 3682 with total cost of 26:

```
    DeER.........................  r8 = r9 + 0x1
    DeER.........................  r10 = 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r5 + 540] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = a1
    .DeeeeeeeeeeeeeeeeeeeeE-----R  jump 3706 if r9 != r10
```

Gas simulation at offset 3699 with total cost of 25:

```
    DeER........................  r8 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = 0
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 3706 with total cost of 27:

```
    DeER..........................  r8 = r8 << 0x2
    D=eER.........................  r7 = r7 + r8
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 2]
    DeeeeeeeeeeeeeeeE------------R  jump 3744
```

Gas simulation at offset 3717 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r8 = u8 [r5 + 3]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r7 = u8 [r5 + 4]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 5] = a1
    .D========================eE------------------------R  jump 4948 if r7 == 0
```

Gas simulation at offset 3731 with total cost of 26:

```
    DeER.........................  r7 = r7 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 4] = a0
    DeeeeeeeeeeeeeeeE-----------R  jump 4960
```

Gas simulation at offset 3740 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r10 + 2]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 3744 with total cost of 78:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u8 [r5 + 558] = a0
    DeE------------------------R.....................................................  r8 = r7 << 0x1
    DeE------------------------R.....................................................  r7 = r7 << 0x3
    .DeE-----------------------R.....................................................  r7 = r7 - r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r8 = u64 [r1 + 80]
    .D=========================eER...................................................  r7 = r7 + r8
    ..D=========================eER..................................................  r9 = r7 + 0x2
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u16 [r9 + 0]
    ..D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r7
    ...DeeE-------------------------------------------------------------------------R  fallthrough
```

Gas simulation at offset 3773 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u64 [r5 + 512]
    D=========================eE--------------R  jump 3885 if r8 != 0
```

Gas simulation at offset 3781 with total cost of 26:

```
    DeER.........................  r8 = 0x30a98
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r8
    D=eE------------------------R  r7 = r8 + 0x2750
    .D=eE-----------------------R  r7 = r7 & 0xfffffffffffffffc
    .DeE------------------------R  r8 = 0x1
    .DeeE-----------------------R  fallthrough
```

Gas simulation at offset 3800 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r8 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r9 = i32 [r7 + 0]
    .D=========================eE-------------R............  r4 = r9 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r9 = r9 & 0xff
    ..D=========================eE------------------------R  jump 3800 if r9 != 0
```

Gas simulation at offset 3831 with total cost of 15:

```
    DeER..............  r7 = 0xf00
    DeER..............  r8 = 0
    DeeeeeeeeeeeeeeeER  r0 = 104, jump 26445
```

Gas simulation at offset 3842 with total cost of 51:

```
    D.....................................................  r6 = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u64 [r1 + 56]
    D=========================eER.........................  r7 = r8 + 0x2000
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 1872] = 0
    .DeE-------------------------------------------------R  jump 32020 if r6 == 0
```

Gas simulation at offset 3859 with total cost of 15:

```
    DeER..............  r9 = 0x1e000
    D.................  r7 = r6
    DeER..............  r8 = 0
    DeeeeeeeeeeeeeeeER  r0 = 106, jump 27934
```

Gas simulation at offset 3873 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u16 [r5 + 544]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r5 + 512] = r6
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 64]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 3885 with total cost of 73:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.................................  unlikely
    DeE---------------------------------------R.................................  r7 = sext16 r7
    D=eE--------------------------------------R.................................  r7 = r7 << 0x3
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.................................  r8 = u64 [r1 + 72]
    .D========================eE--------------R.................................  r7 = r7 + r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r8 = u64 [r7 + 0]
    .D..........................................................................  r7 = r6
    .D==================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 108, jump [r8 + 0]
```

Gas simulation at offset 3905 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r8 = u8 [r5 + 558]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r7 = i16 [r5 + 544]
    D=========================eER............................  r9 = r8 << 0x1
    .D========================eER............................  r10 = r8 << 0x3
    .D=========================eER...........................  r9 = r10 - r9
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R...........................  r10 = u64 [r1 + 80]
    ..D=========================eER..........................  r9 = r9 + r10
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r10 = u16 [r9 + 4]
    ..D=======================eE---------------------------R.  r7 = r7 + 0x1
    ..D========================eE--------------------------R.  r11 = zext16 r7
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE--R.  u16 [r5 + 544] = r7
    ...D==================================================eER  jump 4122 if r10 >=u r11
```

Gas simulation at offset 3944 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = i16 [r5 + 542]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r10 = u16 [r9 + 0]
    D=========================eE--------------R...........  r7 = r7 + 0x1
    .D=========================eE-------------R...........  r11 = zext16 r7
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 542] = r7
    .D==========================eE-----------------------R  jump 4023 if r11 != r10
```

Gas simulation at offset 3963 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r5 + 557]
    D=========================eE--------------R.............  r10 = r9 << 0x2
    .DeE--------------------------------------R.............  r7 = 0x17250
    .D=========================eE-------------R.............  r10 = r10 + r7
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r12 = u8 [r10 + 3]
    ..DeE-------------------------------------------------R.  r11 = r8 + 0x1
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  u16 [r5 + 542] = 0
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R.  u8 [r5 + 558] = a4
    ...D=================================================eER  jump 4035 if r8 >=u r12
```

Gas simulation at offset 3996 with total cost of 78:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......................................  unlikely
    DeE---------------------------------------R......................................  r7 = r11 << 0x1
    DeE---------------------------------------R......................................  r11 = r11 << 0x3
    .DeE--------------------------------------R......................................  r11 = r11 - r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R......................................  r9 = u64 [r1 + 80]
    .D=========================eE-------------R......................................  r9 = r9 + r11
    .D==========================eE------------R......................................  r9 = r9 + 0x2
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u16 [r9 + 0]
    ..D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r7
    ..DeeeeeeeeeeeeeeeE-------------------------------------------------------------R  jump 4122
```

Gas simulation at offset 4023 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeE---------------------------------------R...........  r9 = r9 + 0x2
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  r7 = u16 [r9 + 0]
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r7
    .DeeeeeeeeeeeeeeeE-----------------------------------R  jump 4122
```

Gas simulation at offset 4035 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = i16 [r5 + 540]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r11 = u16 [r10 + 0]
    D=========================eE--------------R...........  r8 = r8 + 0x1
    .D=========================eE-------------R...........  r12 = zext16 r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 540] = r8
    .D==========================eeeeeeeeeeeeeeeeeeeeE----R  jump 4089 if r12 != r11
```

Gas simulation at offset 4054 with total cost of 26:

```
    DeER.........................  r8 = r9 + 0x1
    DeER.........................  r10 = 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r5 + 540] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = a1
    .DeeeeeeeeeeeeeeeeeeeeE-----R  jump 4078 if r9 != r10
```

Gas simulation at offset 4071 with total cost of 25:

```
    DeER........................  r8 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = 0
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 4078 with total cost of 27:

```
    DeER..........................  r8 = r8 << 0x2
    D=eER.........................  r7 = r7 + r8
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 2]
    DeeeeeeeeeeeeeeeE------------R  jump 4093
```

Gas simulation at offset 4089 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r10 + 2]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 4093 with total cost of 78:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u8 [r5 + 558] = a0
    DeE------------------------R.....................................................  r8 = r7 << 0x1
    DeE------------------------R.....................................................  r7 = r7 << 0x3
    .DeE-----------------------R.....................................................  r7 = r7 - r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r8 = u64 [r1 + 80]
    .D=========================eER...................................................  r7 = r7 + r8
    ..D=========================eER..................................................  r9 = r7 + 0x2
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u16 [r9 + 0]
    ..D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r7
    ...DeeE-------------------------------------------------------------------------R  fallthrough
```

Gas simulation at offset 4122 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r5 + 571]
    D=========================eE--------------R  jump 4372 if r8 == 0
```

Gas simulation at offset 4131 with total cost of 73:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.................................  unlikely
    DeE---------------------------------------R.................................  r7 = sext16 r7
    D=eE--------------------------------------R.................................  r7 = r7 << 0x3
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.................................  r8 = u64 [r1 + 72]
    .D========================eE--------------R.................................  r7 = r7 + r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r8 = u64 [r7 + 0]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R......................  u8 [r5 + 571] = 0
    .D..........................................................................  r7 = r6
    ..D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 110, jump [r8 + 0]
```

Gas simulation at offset 4155 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r8 = u8 [r5 + 558]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r7 = i16 [r5 + 544]
    D=========================eER............................  r9 = r8 << 0x1
    .D========================eER............................  r10 = r8 << 0x3
    .D=========================eER...........................  r9 = r10 - r9
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R...........................  r10 = u64 [r1 + 80]
    ..D=========================eER..........................  r9 = r9 + r10
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r10 = u16 [r9 + 4]
    ..D=======================eE---------------------------R.  r7 = r7 + 0x1
    ..D========================eE--------------------------R.  r11 = zext16 r7
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE--R.  u16 [r5 + 544] = r7
    ...D==================================================eER  jump 4372 if r10 >=u r11
```

Gas simulation at offset 4194 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = i16 [r5 + 542]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r10 = u16 [r9 + 0]
    D=========================eE--------------R...........  r7 = r7 + 0x1
    .D=========================eE-------------R...........  r11 = zext16 r7
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 542] = r7
    .D==========================eE-----------------------R  jump 4273 if r11 != r10
```

Gas simulation at offset 4213 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r5 + 557]
    D=========================eE--------------R.............  r10 = r9 << 0x2
    .DeE--------------------------------------R.............  r7 = 0x17250
    .D=========================eE-------------R.............  r10 = r10 + r7
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r12 = u8 [r10 + 3]
    ..DeE-------------------------------------------------R.  r11 = r8 + 0x1
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  u16 [r5 + 542] = 0
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R.  u8 [r5 + 558] = a4
    ...D=================================================eER  jump 4285 if r8 >=u r12
```

Gas simulation at offset 4246 with total cost of 78:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......................................  unlikely
    DeE---------------------------------------R......................................  r7 = r11 << 0x1
    DeE---------------------------------------R......................................  r11 = r11 << 0x3
    .DeE--------------------------------------R......................................  r11 = r11 - r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R......................................  r9 = u64 [r1 + 80]
    .D=========================eE-------------R......................................  r9 = r9 + r11
    .D==========================eE------------R......................................  r9 = r9 + 0x2
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u16 [r9 + 0]
    ..D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r7
    ..DeeeeeeeeeeeeeeeE-------------------------------------------------------------R  jump 4372
```

Gas simulation at offset 4273 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeE---------------------------------------R...........  r9 = r9 + 0x2
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  r7 = u16 [r9 + 0]
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r7
    .DeeeeeeeeeeeeeeeE-----------------------------------R  jump 4372
```

Gas simulation at offset 4285 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = i16 [r5 + 540]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r11 = u16 [r10 + 0]
    D=========================eE--------------R...........  r8 = r8 + 0x1
    .D=========================eE-------------R...........  r12 = zext16 r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 540] = r8
    .D==========================eeeeeeeeeeeeeeeeeeeeE----R  jump 4339 if r12 != r11
```

Gas simulation at offset 4304 with total cost of 26:

```
    DeER.........................  r8 = r9 + 0x1
    DeER.........................  r10 = 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r5 + 540] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = a1
    .DeeeeeeeeeeeeeeeeeeeeE-----R  jump 4328 if r9 != r10
```

Gas simulation at offset 4321 with total cost of 25:

```
    DeER........................  r8 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = 0
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 4328 with total cost of 27:

```
    DeER..........................  r8 = r8 << 0x2
    D=eER.........................  r7 = r7 + r8
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 2]
    DeeeeeeeeeeeeeeeE------------R  jump 4343
```

Gas simulation at offset 4339 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r10 + 2]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 4343 with total cost of 78:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u8 [r5 + 558] = a0
    DeE------------------------R.....................................................  r8 = r7 << 0x1
    DeE------------------------R.....................................................  r7 = r7 << 0x3
    .DeE-----------------------R.....................................................  r7 = r7 - r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r8 = u64 [r1 + 80]
    .D=========================eER...................................................  r7 = r7 + r8
    ..D=========================eER..................................................  r9 = r7 + 0x2
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u16 [r9 + 0]
    ..D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r7
    ...DeeE-------------------------------------------------------------------------R  fallthrough
```

Gas simulation at offset 4372 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u64 [r5 + 512]
    D=========================eE--------------R  jump 4484 if r8 != 0
```

Gas simulation at offset 4380 with total cost of 26:

```
    DeER.........................  r8 = 0x30a98
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r8
    D=eE------------------------R  r7 = r8 + 0x2750
    .D=eE-----------------------R  r7 = r7 & 0xfffffffffffffffc
    .DeE------------------------R  r8 = 0x1
    .DeeE-----------------------R  fallthrough
```

Gas simulation at offset 4399 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r8 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r9 = i32 [r7 + 0]
    .D=========================eE-------------R............  r4 = r9 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r9 = r9 & 0xff
    ..D=========================eE------------------------R  jump 4399 if r9 != 0
```

Gas simulation at offset 4430 with total cost of 15:

```
    DeER..............  r7 = 0xf00
    DeER..............  r8 = 0
    DeeeeeeeeeeeeeeeER  r0 = 112, jump 26445
```

Gas simulation at offset 4441 with total cost of 51:

```
    D.....................................................  r6 = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u64 [r1 + 56]
    D=========================eER.........................  r7 = r8 + 0x2000
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 1872] = 0
    .DeE-------------------------------------------------R  jump 32020 if r6 == 0
```

Gas simulation at offset 4458 with total cost of 15:

```
    DeER..............  r9 = 0x1e000
    D.................  r7 = r6
    DeER..............  r8 = 0
    DeeeeeeeeeeeeeeeER  r0 = 114, jump 27934
```

Gas simulation at offset 4472 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u16 [r5 + 544]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r5 + 512] = r6
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 64]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 4484 with total cost of 73:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.................................  unlikely
    DeE---------------------------------------R.................................  r7 = sext16 r7
    D=eE--------------------------------------R.................................  r7 = r7 << 0x3
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.................................  r8 = u64 [r1 + 72]
    .D========================eE--------------R.................................  r7 = r7 + r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r8 = u64 [r7 + 0]
    .D..........................................................................  r7 = r6
    .D==================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 116, jump [r8 + 0]
```

Gas simulation at offset 4504 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r8 = u8 [r5 + 558]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r9 = i16 [r5 + 544]
    D=========================eER............................  r7 = r8 << 0x1
    .D========================eER............................  r10 = r8 << 0x3
    .D=========================eER...........................  r7 = r10 - r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R...........................  r10 = u64 [r1 + 80]
    ..D=========================eER..........................  r7 = r7 + r10
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r10 = u16 [r7 + 4]
    ..D=======================eE---------------------------R.  r9 = r9 + 0x1
    ..D========================eE--------------------------R.  r11 = zext16 r9
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE--R.  u16 [r5 + 544] = r9
    ...D==================================================eER  jump 4702 if r10 >=u r11
```

Gas simulation at offset 4543 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r9 = i16 [r5 + 542]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r10 = u16 [r7 + 0]
    D=========================eE--------------R...........  r9 = r9 + 0x1
    .D=========================eE-------------R...........  r11 = zext16 r9
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 542] = r9
    .D==========================eE-----------------------R  jump 4691 if r11 != r10
```

Gas simulation at offset 4563 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r5 + 557]
    D=========================eE--------------R.............  r10 = r9 << 0x2
    .DeE--------------------------------------R.............  r7 = 0x17250
    .D=========================eE-------------R.............  r10 = r10 + r7
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r12 = u8 [r10 + 3]
    ..DeE-------------------------------------------------R.  r11 = r8 + 0x1
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  u16 [r5 + 542] = 0
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R.  u8 [r5 + 558] = a4
    ...D=================================================eER  jump 4613 if r8 >=u r12
```

Gas simulation at offset 4596 with total cost of 27:

```
    DeER..........................  r7 = r11 << 0x1
    DeER..........................  r11 = r11 << 0x3
    D=eER.........................  r11 = r11 - r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u64 [r1 + 80]
    .D=========================eER  r7 = r7 + r11
    .DeeeeeeeeeeeeeeeE-----------R  jump 4691
```

Gas simulation at offset 4613 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = i16 [r5 + 540]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r11 = u16 [r10 + 0]
    D=========================eE--------------R...........  r8 = r8 + 0x1
    .D=========================eE-------------R...........  r12 = zext16 r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 540] = r8
    .D==========================eeeeeeeeeeeeeeeeeeeeE----R  jump 4667 if r12 != r11
```

Gas simulation at offset 4632 with total cost of 26:

```
    DeER.........................  r8 = r9 + 0x1
    DeER.........................  r10 = 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r5 + 540] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = a1
    .DeeeeeeeeeeeeeeeeeeeeE-----R  jump 4656 if r9 != r10
```

Gas simulation at offset 4649 with total cost of 25:

```
    DeER........................  r8 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = 0
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 4656 with total cost of 27:

```
    DeER..........................  r8 = r8 << 0x2
    D=eER.........................  r7 = r7 + r8
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 2]
    DeeeeeeeeeeeeeeeE------------R  jump 4671
```

Gas simulation at offset 4667 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r10 + 2]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 4671 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  u8 [r5 + 558] = a0
    DeE------------------------R..  r8 = r7 << 0x1
    DeE------------------------R..  r7 = r7 << 0x3
    .DeE-----------------------R..  r7 = r7 - r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u64 [r1 + 80]
    .D=========================eER  r7 = r7 + r8
    .DeeE------------------------R  fallthrough
```

Gas simulation at offset 4691 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeE---------------------------------------R...........  r7 = r7 + 0x2
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  r9 = u16 [r7 + 0]
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r9
    .DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 4702 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 571]
    D=========================eE--------------R  jump 4933 if r7 == 0
```

Gas simulation at offset 4711 with total cost of 73:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.................................  unlikely
    DeE---------------------------------------R.................................  r7 = sext16 r9
    D=eE--------------------------------------R.................................  r7 = r7 << 0x3
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.................................  r8 = u64 [r1 + 72]
    .D========================eE--------------R.................................  r7 = r7 + r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r8 = u64 [r7 + 0]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R......................  u8 [r5 + 571] = 0
    .D..........................................................................  r7 = r6
    ..D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 118, jump [r8 + 0]
```

Gas simulation at offset 4735 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r8 = u8 [r5 + 558]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r9 = i16 [r5 + 544]
    D=========================eER............................  r7 = r8 << 0x1
    .D========================eER............................  r10 = r8 << 0x3
    .D=========================eER...........................  r7 = r10 - r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R...........................  r10 = u64 [r1 + 80]
    ..D=========================eER..........................  r7 = r7 + r10
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r10 = u16 [r7 + 4]
    ..D=======================eE---------------------------R.  r9 = r9 + 0x1
    ..D========================eE--------------------------R.  r11 = zext16 r9
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE--R.  u16 [r5 + 544] = r9
    ...D==================================================eER  jump 4933 if r10 >=u r11
```

Gas simulation at offset 4774 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r9 = i16 [r5 + 542]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r10 = u16 [r7 + 0]
    D=========================eE--------------R...........  r9 = r9 + 0x1
    .D=========================eE-------------R...........  r11 = zext16 r9
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 542] = r9
    .D==========================eE-----------------------R  jump 4922 if r11 != r10
```

Gas simulation at offset 4794 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r5 + 557]
    D=========================eE--------------R.............  r10 = r9 << 0x2
    .DeE--------------------------------------R.............  r7 = 0x17250
    .D=========================eE-------------R.............  r10 = r10 + r7
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r12 = u8 [r10 + 3]
    ..DeE-------------------------------------------------R.  r11 = r8 + 0x1
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  u16 [r5 + 542] = 0
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R.  u8 [r5 + 558] = a4
    ...D=================================================eER  jump 4844 if r8 >=u r12
```

Gas simulation at offset 4827 with total cost of 27:

```
    DeER..........................  r7 = r11 << 0x1
    DeER..........................  r11 = r11 << 0x3
    D=eER.........................  r11 = r11 - r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u64 [r1 + 80]
    .D=========================eER  r7 = r7 + r11
    .DeeeeeeeeeeeeeeeE-----------R  jump 4922
```

Gas simulation at offset 4844 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = i16 [r5 + 540]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r11 = u16 [r10 + 0]
    D=========================eE--------------R...........  r8 = r8 + 0x1
    .D=========================eE-------------R...........  r12 = zext16 r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 540] = r8
    .D==========================eeeeeeeeeeeeeeeeeeeeE----R  jump 4898 if r12 != r11
```

Gas simulation at offset 4863 with total cost of 26:

```
    DeER.........................  r8 = r9 + 0x1
    DeER.........................  r10 = 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r5 + 540] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = a1
    .DeeeeeeeeeeeeeeeeeeeeE-----R  jump 4887 if r9 != r10
```

Gas simulation at offset 4880 with total cost of 25:

```
    DeER........................  r8 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = 0
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 4887 with total cost of 27:

```
    DeER..........................  r8 = r8 << 0x2
    D=eER.........................  r7 = r7 + r8
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 2]
    DeeeeeeeeeeeeeeeE------------R  jump 4902
```

Gas simulation at offset 4898 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r10 + 2]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 4902 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  u8 [r5 + 558] = a0
    DeE------------------------R..  r8 = r7 << 0x1
    DeE------------------------R..  r7 = r7 << 0x3
    .DeE-----------------------R..  r7 = r7 - r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u64 [r1 + 80]
    .D=========================eER  r7 = r7 + r8
    .DeeE------------------------R  fallthrough
```

Gas simulation at offset 4922 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeE---------------------------------------R...........  r7 = r7 + 0x2
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  r7 = i16 [r7 + 0]
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 544] = r7
    .DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 4933 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 112]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 104]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r6 = u64 [r1 + 96]
    .DeE--------------------------------------R.......  r1 = r1 + 0x78
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 4948 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 1]
    D=========================eE--------------R  jump 4960 if r7 == 0
```

Gas simulation at offset 4955 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 4] = 0xf
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 4960 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 26]
    D=========================eE--------------R  jump 4988 if r7 == 0
```

Gas simulation at offset 4967 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = u8 [r5 + 27]
    DeE---------------------------------------R...........  r8 = 0xf
    D=========================eE--------------R...........  r7 = r7 + 0x1
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  u8 [r5 + 26] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  u8 [r5 + 28] = a1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 29] = a0
    .DeeeeeeeeeeeeeeeE-----------------------------------R  jump 5036
```

Gas simulation at offset 4988 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 29]
    D=========================eE--------------R  jump 5003 if r7 == 0
```

Gas simulation at offset 4995 with total cost of 26:

```
    DeER.........................  r7 = r7 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 29] = a0
    DeeeeeeeeeeeeeeeE-----------R  jump 5036
```

Gas simulation at offset 5003 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r8 = u8 [r5 + 27]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r7 = u8 [r5 + 28]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 29] = a1
    .D========================eE------------------------R  jump 5024 if r7 == 0
```

Gas simulation at offset 5016 with total cost of 26:

```
    DeER.........................  r7 = r7 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 28] = a0
    DeeeeeeeeeeeeeeeE-----------R  jump 5036
```

Gas simulation at offset 5024 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 25]
    D=========================eE--------------R  jump 5036 if r7 == 0
```

Gas simulation at offset 5031 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 28] = 0xf
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 5036 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 50]
    D=========================eE--------------R  jump 5064 if r7 == 0
```

Gas simulation at offset 5043 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = u8 [r5 + 51]
    DeE---------------------------------------R...........  r8 = 0xf
    D=========================eE--------------R...........  r7 = r7 + 0x1
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  u8 [r5 + 50] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  u8 [r5 + 52] = a1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 53] = a0
    .DeeeeeeeeeeeeeeeE-----------------------------------R  jump 5112
```

Gas simulation at offset 5064 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 53]
    D=========================eE--------------R  jump 5079 if r7 == 0
```

Gas simulation at offset 5071 with total cost of 26:

```
    DeER.........................  r7 = r7 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 53] = a0
    DeeeeeeeeeeeeeeeE-----------R  jump 5112
```

Gas simulation at offset 5079 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r8 = u8 [r5 + 51]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r7 = u8 [r5 + 52]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 53] = a1
    .D========================eE------------------------R  jump 5100 if r7 == 0
```

Gas simulation at offset 5092 with total cost of 26:

```
    DeER.........................  r7 = r7 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 52] = a0
    DeeeeeeeeeeeeeeeE-----------R  jump 5112
```

Gas simulation at offset 5100 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 49]
    D=========================eE--------------R  jump 5112 if r7 == 0
```

Gas simulation at offset 5107 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 52] = 0xf
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 5112 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r6 + 4]
    D=========================eE--------------R  jump 5203 if r7 == 0
```

Gas simulation at offset 5119 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 10]
    D=========================eE--------------R  jump 5140 if r7 != 0
```

Gas simulation at offset 5126 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 12]
    D=========================eE--------------R  jump 5140 if r7 == 0
```

Gas simulation at offset 5133 with total cost of 26:

```
    DeER.........................  r7 = r7 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 12] = a0
    DeeE------------------------R  fallthrough
```

Gas simulation at offset 5140 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 34]
    D=========================eE--------------R  jump 5161 if r7 != 0
```

Gas simulation at offset 5147 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 36]
    D=========================eE--------------R  jump 5161 if r7 == 0
```

Gas simulation at offset 5154 with total cost of 26:

```
    DeER.........................  r7 = r7 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 36] = a0
    DeeE------------------------R  fallthrough
```

Gas simulation at offset 5161 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 119]
    D=========================eE--------------R  jump 5182 if r7 != 0
```

Gas simulation at offset 5168 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 121]
    D=========================eE--------------R  jump 5182 if r7 == 0
```

Gas simulation at offset 5175 with total cost of 26:

```
    DeER.........................  r7 = r7 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 121] = a0
    DeeE------------------------R  fallthrough
```

Gas simulation at offset 5182 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 60]
    D=========================eE--------------R  jump 5203 if r7 != 0
```

Gas simulation at offset 5189 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 62]
    D=========================eE--------------R  jump 5203 if r7 == 0
```

Gas simulation at offset 5196 with total cost of 26:

```
    DeER.........................  r7 = r7 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 62] = a0
    DeeE------------------------R  fallthrough
```

Gas simulation at offset 5203 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r6 + 3]
    D=========================eE--------------R  jump 5229 if r7 == 0
```

Gas simulation at offset 5210 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 151]
    D=========================eE--------------R  jump 5229 if r7 != 0
```

Gas simulation at offset 5218 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 152] = 0x1
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 623] = 0x1
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 5229 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r7 = u8 [r6 + 2]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r8 = u64 [r5 + 72]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 153] = a0
    .D========================eE------------------------R  jump 5284 if r7 >=u r8
```

Gas simulation at offset 5243 with total cost of 76:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER....................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R....................................  r8 = u64 [r5 + 64]
    DeE---------------------------------------R....................................  r7 = r7 << 0x3
    D=========================eE--------------R....................................  r7 = r7 + r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = i16 [r7 + 0]
    .D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 148] = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------------------------------R  r6 = u64 [r1 + 64]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------------------------------R  r8 = u8 [r5 + 146]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------------------------------R  r7 = u8 [r5 + 147]
    ..DeE-------------------------------------------------------------------------R  r9 = 0x2
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u8 [r5 + 146] = a2
    ..D========================eE-------------------------------------------------R  jump 2944 if r8 != r9
```

Gas simulation at offset 5281 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 2993
```

Gas simulation at offset 5284 with total cost of 2:

```
    DeeER  trap
```

Gas simulation at offset 5285 with total cost of 27:

```
    DeER..........................  r9 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r9 = u8 [r9 + 644]
    D==========================eER  jump 5342 if r9 == 0
```

Gas simulation at offset 5296 with total cost of 61:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  unlikely
    DeE---------------------------------------R.....................  r9 = r7 + r8
    D=eE--------------------------------------R.....................  r9 = r9 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R.....................  r9 = u8 [r9 + 639]
    .DeE--------------------------------------R.....................  r8 = r8 | 0xa80
    ..D=========================eeeE----------R.....................  r10 = r9 <u 0xc0
    ...D========================eE------------R.....................  r11 = r9 & 0x3f
    ...D===========================eeE--------R.....................  r11 = r9 if r10 != 0
    ....D============================eE-------R.....................  r10 = r11 & 0x30
    ....D============================eE-------R.....................  r9 = r11 & 0xcf
    .....D============================eE------R.....................  r10 = r10 + 0xffffffffffffffd0
    .....D=============================eeE----R.....................  r9 = r11 if r10 != 0
    ......DeE---------------------------------R.....................  r10 = r7 + r8
    ......D==============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r10 + 0] = a2
    ......DeeeeeeeeeeeeeeeE----------------------------------------R  jump 5352
```

Gas simulation at offset 5342 with total cost of 27:

```
    DeER..........................  r8 = r8 | 0xa80
    D=eER.........................  r9 = r7 + r8
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r9 = u8 [r9 + 0]
    .DeeE------------------------R  fallthrough
```

Gas simulation at offset 5352 with total cost of 27:

```
    DeER..........................  r8 = r8 + r7
    DeER..........................  r7 = r9 & 0x1
    DeER..........................  r9 = r9 >> 0x1
    .DeER.........................  r9 = r9 + 0x80
    .DeER.........................  r7 = r7 | 0x40
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 0] = a2
    .DeeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 5372 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xffffffffffffff90
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 104] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 96] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 88] = r6
    .DeE------------------------R...  r7 = 0x30008
    .D=eE-----------------------R...  r5 = r7 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u8 [r5 + 651]
    ..D==========================eER  jump 5903 if r8 == 0
```

Gas simulation at offset 5401 with total cost of 76:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER....................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R....................................  r8 = i32 [r5 + 605]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 72] = r8
    DeE-------------------------------------------------R..........................  r7 = r7 + 0x8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R..........................  u64 [r1 + 80] = r7
    .DeE------------------------------------------------R..........................  r7 = 0x10140
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------R..........................  u64 [r1 + 48] = r7
    .DeE------------------------------------------------R..........................  r7 = 0x17cd8
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------R..........................  u64 [r1 + 32] = r7
    ..DeE-----------------------------------------------R..........................  r7 = 0x17d18
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 40] = r7
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u64 [r1 + 24] = 0xffff
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u64 [r1 + 16] = 0xfffb
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 8] = 0xfffe
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = 0xfffa
    ...DeeeeeeeeeeeeeeeE----------------------------------------------------------R  jump 5509
```

Gas simulation at offset 5464 with total cost of 75:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...................................  r7 = u8 [r5 + 622]
    D=========================eE--------------R...................................  r7 = r7 ^ 0x80
    D==========================eE-------------R...................................  r7 = r7 << 0x3
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...................................  r8 = u64 [r1 + 40]
    .D==========================eE------------R...................................  r7 = r7 + r8
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r8 = u64 [r7 + 0]
    .D............................................................................  r7 = r6
    ..D===================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 120, jump [r8 + 0]
```

Gas simulation at offset 5490 with total cost of 2:

```
    DeER.  r8 = r7 & 0x1
    D=eER  jump 5939 if r8 != 0
```

Gas simulation at offset 5497 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = i32 [r5 + 605]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u64 [r1 + 72]
    D=========================eE--------------R  jump 5907 if r7 != r8
```

Gas simulation at offset 5509 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r8 = u16 [r5 + 625]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r6 = u8 [r5 + 633]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 617] = r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R  r7 = u64 [r1 + 80]
    .DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 122, jump 22431
```

Gas simulation at offset 5530 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 622] = a0
    DeE------------------------R  jump 5545 if r6 == 0
```

Gas simulation at offset 5537 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 634]
    D=========================eE--------------R  jump 5639 if r7 == 0
```

Gas simulation at offset 5545 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 632]
    D=========================eE--------------R  jump 5564 if r7 == 0
```

Gas simulation at offset 5553 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......  r7 = u8 [r5 + 631]
    D=========================eE--------------R......  r7 = r7 & 0x4
    D==========================eeeeeeeeeeeeeeeeeeeeER  jump 5645 if r7 == 0
```

Gas simulation at offset 5564 with total cost of 1:

```
    DeER  jump 5572 if r6 != 0
```

Gas simulation at offset 5567 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 634] = 0
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 5572 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = i16 [r5 + 625]
    D=========================eE--------------R...........  r7 = r7 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 625] = r7
    .D=========================eE------------------------R  r8 = zext16 r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r6 = u64 [r1 + 80]
    .D....................................................  r7 = r6
    .DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 124, jump 22431
```

Gas simulation at offset 5596 with total cost of 76:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r8 = u8 [r5 + 622]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r9 = u64 [r1 + 48]
    D=========================eER..................................................  r8 = r8 + r9
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = i8 [r8 + 0]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.........................  u8 [r5 + 621] = a0
    .D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 623] = a1
    .D==================================================eE------------------------R  r7 = r8 & 0xff
    ..D=================================================eE------------------------R  jump 5845 if r8 <s 0
```

Gas simulation at offset 5624 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = i16 [r5 + 625]
    D=========================eE--------------R...........  r8 = r8 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 625] = r8
    .DeeeeeeeeeeeeeeeE-----------------------------------R  jump 5851
```

Gas simulation at offset 5639 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 634] = 0x1
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 5645 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r5 + 625]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 80]
    D...........................  r7 = r6
    DeeeeeeeeeeeeeeeE----------R  r0 = 126, jump 22431
```

Gas simulation at offset 5659 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r5 + 631]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r5 + 630]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r9 = u8 [r5 + 626]
    D=========================eER.........................  r7 = r7 & 0xef
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 631] = a0
    .D========================eE-------------------------R  r8 = r8 | 0x100
    .D....................................................  r7 = r6
    .DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 128, jump 22969
```

Gas simulation at offset 5691 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r5 + 630]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r9 = u8 [r5 + 625]
    D=========================eER.........................  r7 = r7 + 0xffffffffffffffff
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 630] = a0
    .D=========================eE------------------------R  r7 = r7 & 0xff
    .D==========================eE-----------------------R  r8 = r7 | 0x100
    .D....................................................  r7 = r6
    ..DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 130, jump 22969
```

Gas simulation at offset 5722 with total cost of 77:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r7 = u8 [r5 + 630]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r11 = u8 [r5 + 634]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 56] = r11
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R...........................  r9 = u8 [r5 + 631]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R...........................  r10 = u64 [r1 + 16]
    .D========================eE------------------------R...........................  r7 = r7 + 0xffffffffffffffff
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r8 = u64 [r1 + 24]
    ..D================================================eeER.........................  r10 = r8 if r11 == 0
    ..D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 64] = r10
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u8 [r5 + 630] = a0
    ...D=======================eE--------------------------------------------------R  r7 = r7 & 0xff
    ...D========================eE-------------------------------------------------R  r8 = r7 | 0x100
    ...D............................................................................  r7 = r6
    ....DeeeeeeeeeeeeeeeE----------------------------------------------------------R  r0 = 132, jump 22969
```

Gas simulation at offset 5772 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r7 = u8 [r5 + 630]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u8 [r5 + 631]
    D=========================eER...........................  r7 = r7 + 0xffffffffffffffff
    D=========================eER...........................  r8 = r8 | 0x4
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u8 [r5 + 630] = a0
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u8 [r5 + 631] = a1
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R..  r8 = u64 [r1 + 0]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R..  r7 = u64 [r1 + 8]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..  r9 = u64 [r1 + 56]
    ..D=================================================eeER  r8 = r7 if r9 == 0
    ..D.....................................................  r7 = r6
    ...DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 134, jump 22431
```

Gas simulation at offset 5813 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 625] = a0
    D...........................  r7 = r6
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u64 [r1 + 64]
    DeeeeeeeeeeeeeeeE----------R  r0 = 136, jump 22431
```

Gas simulation at offset 5828 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r5 + 626] = a0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = i32 [r5 + 605]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u64 [r1 + 72]
    D=========================eER  jump 5509 if r7 == r8
```

Gas simulation at offset 5843 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 5907
```

Gas simulation at offset 5845 with total cost of 1:

```
    DeER  jump 5464 if r7 == 128
```

Gas simulation at offset 5851 with total cost of 73:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.................................  unlikely
    DeE---------------------------------------R.................................  r7 = r7 & 0x7
    D=eE--------------------------------------R.................................  r7 = r7 << 0x3
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.................................  r8 = u64 [r1 + 32]
    .D========================eE--------------R.................................  r7 = r7 + r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r8 = u64 [r7 + 0]
    .D..........................................................................  r7 = r6
    .D==================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 138, jump [r8 + 0]
```

Gas simulation at offset 5873 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r7 = u8 [r5 + 623]
    D=========================eER.  r7 = r7 & 0x40
    D==========================eER  jump 5464 if r7 == 0
```

Gas simulation at offset 5884 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r5 + 619]
    D...........................  r7 = r6
    DeeeeeeeeeeeeeeeE----------R  r0 = 140, jump 22431
```

Gas simulation at offset 5896 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 621] = a0
    DeeeeeeeeeeeeeeeE----------R  jump 5464
```

Gas simulation at offset 5903 with total cost of 15:

```
    DeER..............  r9 = 0
    DeeeeeeeeeeeeeeeER  jump 5976
```

Gas simulation at offset 5907 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u16 [r5 + 641]
    D=========================eE--------------R  jump 5976 if r9 == 0
```

Gas simulation at offset 5915 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u16 [r5 + 643]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r5 + 645]
    DeE---------------------------------------R  r9 = r9 & 0x1
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u16 [r5 + 641] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u8 [r5 + 651] = 0
    .D========================eE--------------R  jump 5972 if r9 != 0
```

Gas simulation at offset 5938 with total cost of 2:

```
    DeeER  trap
```

Gas simulation at offset 5939 with total cost of 28:

```
    DeER...........................  r7 = r7 << 0x10
    D=eER..........................  r8 = r7 >> 0x10
    .D=eER.........................  r7 = r8 >> 0x20
    .D=eER.........................  r8 = r8 >> 0x10
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..  u16 [r5 + 641] = 0
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 643] = r8
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 645] = a0
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-R  u8 [r5 + 651] = 0
    ..DeE-------------------------R  r9 = 0x1
    ...DeeeeeeeeeeeeeeeE----------R  jump 5976
```

Gas simulation at offset 5972 with total cost of 2:

```
    DeER.  r9 = 0x1
    DeeER  fallthrough
```

Gas simulation at offset 5976 with total cost of 48:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER........  unlikely
    DeE---------------------------------------R........  r7 = r7 & 0xff
    DeE---------------------------------------R........  r8 = r8 << 0x30
    D=eE--------------------------------------R........  r7 = r7 << 0x20
    .DeE--------------------------------------R........  r8 = r8 >> 0x20
    .D=eE-------------------------------------R........  r7 = r7 | r8
    .D==eE------------------------------------R........  r7 = r7 | r9
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R........  r0 = u64 [r1 + 104]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R........  r5 = u64 [r1 + 96]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R........  r6 = u64 [r1 + 88]
    ..D==eE-----------------------------------R........  r1 = r1 + 0x70
    ..D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 6010 with total cost of 49:

```
    DeER................................................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u64 [r1 + 0] = r6
    .DeE------------------------R.......................  r8 = r7 + 0x7ff
    .D=eE-----------------------R.......................  r8 = r8 + 0x1e1
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r6 = u8 [r8 + 70]
    ..D==========================eER....................  r10 = r6 & 0x8
    ..D===========================eeeeeeeeeeeeeeeeeeeeER  jump 6051 if r10 != 0
```

Gas simulation at offset 6035 with total cost of 21:

```
    DeER....................  r3 = 0
    DeER....................  r2 = 0
    DeER....................  r9 = r6 & 0x10
    .DeER...................  r4 = 0x1
    .DeeeeeeeeeeeeeeeeeeeeER  jump 6135 if r9 != 0
```

Gas simulation at offset 6048 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 6432
```

Gas simulation at offset 6051 with total cost of 2:

```
    DeER.  r10 = r6 & 0x2
    D=eER  jump 6067 if r10 != 0
```

Gas simulation at offset 6057 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r10 = u16 [r8 + 48]
    DeE---------------------------------------R  r11 = 0x8
    D=========================eE--------------R  jump 6035 if r10 <u r11
```

Gas simulation at offset 6067 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...............  r10 = u8 [r8 + 66]
    DeE---------------------------------------R...............  r11 = 0xf
    .D========================eeE-------------R...............  r10 = r11 & ~r10
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...............  r11 = u16 [r8 + 50]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R...............  r12 = u16 [r8 + 52]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R...............  r9 = u16 [r8 + 54]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER....  r5 = u16 [r8 + 56]
    ...D========================eE-----------------------R....  r11 = r11 >> r10
    ...D========================eE-----------------------R....  r12 = r12 >> r10
    ....D=======================eE-----------------------R....  r9 = r9 >> r10
    .....D==============================================eER...  r10 = r5 >> r10
    .....D=======================eE-----------------------R...  r11 = r11 & 0x1
    ......D======================eE-----------------------R...  r9 = r9 & 0x1
    ......D======================eE-----------------------R...  r12 = r12 << 0x1
    ......D==============================================eER..  r10 = r10 << 0x1
    ......D=======================eE-----------------------R..  r12 = r12 & 0x2
    .......D==============================================eER.  r10 = r10 & 0x2
    .......D=======================eE-----------------------R.  r3 = r12 | r11
    ........D==============================================eER  r2 = r10 | r9
    ........D=====================eE-------------------------R  r9 = r6 & 0x10
    .........DeE---------------------------------------------R  r4 = 0x1
    .........D=====================eE------------------------R  jump 6432 if r9 == 0
```

Gas simulation at offset 6135 with total cost of 2:

```
    DeER.  r9 = r6 & 0x4
    D=eER  jump 6152 if r9 != 0
```

Gas simulation at offset 6141 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u16 [r8 + 48]
    DeE---------------------------------------R  r10 = 0x8
    D=========================eE--------------R  jump 6432 if r9 <u r10
```

Gas simulation at offset 6152 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r8 + 3]
    D=========================eE--------------R  jump 6174 if r9 != 0
```

Gas simulation at offset 6159 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r11 = u8 [r8 + 0]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r10 = u8 [r8 + 1]
    .D========================eE--------------R  r9 = r10 | r11
    .D=========================eE-------------R  r9 = sext8 r9
    .D==========================eE------------R  jump 6337 if r9 <s 0
```

Gas simulation at offset 6174 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r8 + 7]
    D=========================eE--------------R  jump 6197 if r9 != 0
```

Gas simulation at offset 6181 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r11 = u8 [r8 + 4]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r10 = u8 [r8 + 5]
    .D========================eE--------------R  r9 = r10 | r11
    .D=========================eE-------------R  r9 = sext8 r9
    .D==========================eE------------R  jump 6347 if r9 <s 0
```

Gas simulation at offset 6197 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r8 + 11]
    D=========================eE--------------R  jump 6220 if r9 != 0
```

Gas simulation at offset 6204 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r11 = u8 [r8 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r10 = u8 [r8 + 9]
    .D========================eE--------------R  r9 = r10 | r11
    .D=========================eE-------------R  r9 = sext8 r9
    .D==========================eE------------R  jump 6354 if r9 <s 0
```

Gas simulation at offset 6220 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r8 + 15]
    D=========================eE--------------R  jump 6242 if r9 != 0
```

Gas simulation at offset 6227 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r11 = u8 [r8 + 12]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r10 = u8 [r8 + 13]
    .D========================eE--------------R  r9 = r10 | r11
    .D=========================eE-------------R  r9 = sext8 r9
    .D==========================eE------------R  jump 6361 if r9 <s 0
```

Gas simulation at offset 6242 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r8 + 19]
    D=========================eE--------------R  jump 6264 if r9 != 0
```

Gas simulation at offset 6249 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r11 = u8 [r8 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r10 = u8 [r8 + 17]
    .D========================eE--------------R  r9 = r10 | r11
    .D=========================eE-------------R  r9 = sext8 r9
    .D==========================eE------------R  jump 6368 if r9 <s 0
```

Gas simulation at offset 6264 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r8 + 23]
    D=========================eE--------------R  jump 6286 if r9 != 0
```

Gas simulation at offset 6271 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r11 = u8 [r8 + 20]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r10 = u8 [r8 + 21]
    .D========================eE--------------R  r9 = r10 | r11
    .D=========================eE-------------R  r9 = sext8 r9
    .D==========================eE------------R  jump 6375 if r9 <s 0
```

Gas simulation at offset 6286 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r8 + 27]
    D=========================eE--------------R  jump 6308 if r9 != 0
```

Gas simulation at offset 6293 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r11 = u8 [r8 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r10 = u8 [r8 + 25]
    .D========================eE--------------R  r9 = r10 | r11
    .D=========================eE-------------R  r9 = sext8 r9
    .D==========================eE------------R  jump 6382 if r9 <s 0
```

Gas simulation at offset 6308 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r8 + 31]
    D=========================eE--------------R  jump 6432 if r9 != 0
```

Gas simulation at offset 6315 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r11 = u8 [r8 + 28]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r10 = u8 [r8 + 29]
    .D========================eE--------------R  r9 = r10 | r11
    .D=========================eE-------------R  r9 = sext8 r9
    .D==========================eE------------R  jump 6432 if r9 >=s 0
```

Gas simulation at offset 6330 with total cost of 15:

```
    DeER..............  r4 = 0
    DeER..............  r12 = r8 + 0x1c
    DeeeeeeeeeeeeeeeER  jump 6388
```

Gas simulation at offset 6337 with total cost of 15:

```
    DeER..............  r4 = 0x1000000
    D.................  r12 = r8
    DeeeeeeeeeeeeeeeER  jump 6388
```

Gas simulation at offset 6347 with total cost of 15:

```
    DeER..............  r4 = 0
    DeER..............  r12 = r8 + 0x4
    DeeeeeeeeeeeeeeeER  jump 6388
```

Gas simulation at offset 6354 with total cost of 15:

```
    DeER..............  r4 = 0
    DeER..............  r12 = r8 + 0x8
    DeeeeeeeeeeeeeeeER  jump 6388
```

Gas simulation at offset 6361 with total cost of 15:

```
    DeER..............  r4 = 0
    DeER..............  r12 = r8 + 0xc
    DeeeeeeeeeeeeeeeER  jump 6388
```

Gas simulation at offset 6368 with total cost of 15:

```
    DeER..............  r4 = 0
    DeER..............  r12 = r8 + 0x10
    DeeeeeeeeeeeeeeeER  jump 6388
```

Gas simulation at offset 6375 with total cost of 15:

```
    DeER..............  r4 = 0
    DeER..............  r12 = r8 + 0x14
    DeeeeeeeeeeeeeeeER  jump 6388
```

Gas simulation at offset 6382 with total cost of 2:

```
    DeER.  r4 = 0
    DeER.  r12 = r8 + 0x18
    DeeER  fallthrough
```

Gas simulation at offset 6388 with total cost of 31:

```
    DeER..............................  r11 = r11 >> 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......  r9 = u8 [r12 + 2]
    DeE------------------------R......  r10 = r10 >> 0x6
    D=eE-----------------------R......  r10 = r10 & 0x2
    .D=eE----------------------R......  r10 = r10 | r11
    .D========================eER.....  r11 = r9 & 0x3
    .D========================eER.....  r9 = r9 << 0x3a
    ..D========================eER....  r11 = r11 << 0x8
    ..D========================eER....  r9 = r9 >> 0x3f
    ..D=eE-----------------------R....  r10 = r10 << 0x10
    ..D=========================eER...  r11 = r11 | r4
    ...D=========================eER..  r9 = r9 | r11
    ...D==========================eER.  r9 = r9 | r10
    ...D===========================eER  r4 = r9 | 0x400
    ....DeeE-------------------------R  fallthrough
```

Gas simulation at offset 6432 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u16 [r8 + 48]
    D=========================eE--------------R  jump 6516 if r9 == 255
```

Gas simulation at offset 6441 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u16 [r8 + 46]
    D=========================eE--------------R  jump 6516 if r9 == 0
```

Gas simulation at offset 6448 with total cost of 4:

```
    DeeER..  i32 r11 = r4 >> 0x10
    .D=eER.  r12 = r11 & 0xff
    ..DeeER  i32 r10 = r4 >> 0x8
    ..D=eER  jump 6492 if r12 == 0
```

Gas simulation at offset 6461 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......  r9 = u8 [r8 + 93]
    D=========================eE--------------R......  r9 = r9 & 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeER  jump 6492 if r9 == 0
```

Gas simulation at offset 6471 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 6509 if r3 == 0
```

Gas simulation at offset 6474 with total cost of 3:

```
    DeeER.  i32 r9 = r4 >> 0x18
    D==eER  jump 6498 if r9 == 0
```

Gas simulation at offset 6480 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r9 = u8 [r8 + 71]
    D=========================eE--------------R...........  r9 = r9 | 0x40
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 71] = a2
    .DeeeeeeeeeeeeeeeE-----------------------------------R  jump 6498
```

Gas simulation at offset 6492 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 6509 if r3 == 0
```

Gas simulation at offset 6495 with total cost of 1:

```
    DeER  jump 6516 if r12 == 0
```

Gas simulation at offset 6498 with total cost of 16:

```
    DeER...............  r9 = r4 & 0x1
    D=eeER.............  r3 = r11 if r9 == 0
    .DeeER.............  r2 = r10 if r9 == 0
    .DeeeeeeeeeeeeeeeER  jump 6516
```

Gas simulation at offset 6509 with total cost of 3:

```
    DeeER.  r10 = 0 if r12 == 0
    D.....  r3 = r11
    .D....  r2 = r10
    .DeeER  fallthrough
```

Gas simulation at offset 6516 with total cost of 56:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER................  unlikely
    DeE---------------------------------------R................  r2 = r2 << 0x2
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R................  r9 = u64 [r8 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R................  r10 = u16 [r8 + 44]
    .DeE--------------------------------------R................  r2 = r2 + r3
    .D=eE-------------------------------------R................  r11 = r2 & 0x1f
    .D==eE------------------------------------R................  r7 = r7 + r11
    ..D=======================eE--------------R................  r11 = r10 << 0x1
    ..D========================eE-------------R................  r9 = r9 + r11
    ..D==eE-----------------------------------R................  r7 = r7 + 0x7ff
    ...D==eeeeeeeeeeeeeeeeeeeeeeeeeE----------R................  r7 = u8 [r7 + 417]
    ...DeE------------------------------------R................  r6 = r6 << 0x1
    ...D=eE-----------------------------------R................  r11 = r6 & 0x1c0
    ....D=====================eE--------------R................  r10 = r10 + 0x1
    ....D==========================eE---------R................  r7 = r7 | r11
    ....D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r9 + 0] = r7
    ....D======================eeeeeeeeeeeeeeeeeeeeeeeeeE-----R  u16 [r8 + 44] = r10
    .....DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r5 = u64 [r1 + 8]
    .....D======================eeeeeeeeeeeeeeeeeeeeeeeeeE----R  r6 = u64 [r1 + 0]
    .....D=========================eE-------------------------R  r1 = r1 + 0x10
    .....DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 6577 with total cost of 30:

```
    DeER.............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....  u64 [r1 + 0] = r5
    .DeE------------------------R....  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  r10 = u16 [r5 + 521]
    ..D=========================eER..  r7 = r10 << 0x32
    ..D==========================eER.  r11 = r7 >> 0x3a
    ...DeE-------------------------R.  r12 = 0x3f
    ...D.............................  r9 = r8
    ...D==========================eER  jump 6644 if r11 >=u r12
```

Gas simulation at offset 6607 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r10 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r8 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r11 = 0x17c80
    .D========================eeE-------------R..................................  r11 = r8 if r10 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r11 = u64 [r11 + 80]
    ..DeE-------------------------------------------------R......................  r8 = r7 >> 0x32
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ...D======================eeE-------------------------R......................  r7 = r10 if r10 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 142, jump [r11 + 0]
```

Gas simulation at offset 6642 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 6685
```

Gas simulation at offset 6644 with total cost of 28:

```
    DeER...........................  r11 = r10 & 0x1f
    DeER...........................  r7 = r9 & 0x3f
    .DeER..........................  r8 = r5 + 0x1a1
    .D=eER.........................  r9 = r8 + r11
    ..DeER.........................  r10 = r10 & 0x3
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r9 + 0] = a0
    ..D=eE------------------------R  jump 6685 if r10 != 0
```

Gas simulation at offset 6665 with total cost of 32:

```
    DeeeER.............................  r9 = r11 <u 0x10
    .DeE-R.............................  r10 = r11 + 0xfffffffffffffff0
    .DeE-R.............................  r11 = r11 | 0x10
    ..D=eeER...........................  r11 = r10 if r9 == 0
    ..D===eER..........................  r9 = zext16 r11
    ..D====eER.........................  r8 = r8 + r9
    ...D====eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 0] = a0
    ...DeeE---------------------------R  fallthrough
```

Gas simulation at offset 6685 with total cost of 56:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R................  r7 = u8 [r5 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R................  r8 = i16 [r5 + 521]
    DeE---------------------------------------R................  r9 = 0x20
    .D========================eE--------------R................  r7 = r7 & 0x4
    .DeE--------------------------------------R................  r10 = 0x1
    .D=========================eeE------------R................  r10 = r9 if r7 != 0
    ..D==========================eE-----------R................  r8 = r8 + r10
    ..D===========================eE----------R................  r8 = r8 << 0x31
    ..D============================eE---------R................  r8 = r8 >> 0x31
    ..D=============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r8
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  r0 = u64 [r1 + 8]
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  r5 = u64 [r1 + 0]
    ...D======================eE------------------------------R  r1 = r1 + 0x10
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeE------R  jump [r0 + 0]
```

Gas simulation at offset 6729 with total cost of 27:

```
    DeER..........................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r9 = u8 [r7 + 570]
    D==========================eER  jump 6784 if r9 == 0
```

Gas simulation at offset 6740 with total cost of 53:

```
    DeER....................................................  r10 = r8 & 0x7
    DeER....................................................  r8 = r8 << 0x2
    D=eER...................................................  r10 = r10 << 0xc
    .DeER...................................................  r11 = r8 & 0xe0
    .D=eER..................................................  r10 = r10 | r11
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r11 = u16 [r7 + 523]
    ..DeE-----------------------R...........................  r8 = r8 & 0x300
    ..D=eE----------------------R...........................  r8 = r8 | r10
    ..D========================eER..........................  r10 = r11 & 0xc1f
    ...D========================eER.........................  r8 = r8 | r10
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 523] = r8
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u8 [r7 + 570] = 0
    ...DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 6784 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r9 = u16 [r7 + 523]
    D=========================eE--------------R............  r9 = r9 & 0x7fe0
    .DeE--------------------------------------R............  r10 = r8 & 0x7
    .DeE--------------------------------------R............  r8 = r8 >> 0x3
    .D=========================eE-------------R............  r8 = r8 | r9
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 523] = r8
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u8 [r7 + 547] = a3
    ..DeE-------------------------------------------------R  r9 = 0x1
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R  u8 [r7 + 570] = a2
    ...DeeeeeeeeeeeeeeeeeeeeeeE---------------------------R  jump [r0 + 0]
```

Gas simulation at offset 6819 with total cost of 27:

```
    DeER..........................  r8 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r9 = u8 [r8 + 573]
    D==========================eER  jump 6872 if r9 == 0
```

Gas simulation at offset 6830 with total cost of 77:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.....................................  r9 = u8 [r8 + 560]
    D=========================eE--------------R.....................................  r7 = r7 + r9
    D==========================eE-------------R.....................................  r7 = r7 + 0x7ff
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u8 [r7 + 161]
    .D========================eE--------------------------R.........................  r9 = r9 + 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.........................  u8 [r8 + 560] = a2
    .D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 562] = a0
    ..DeeE-------------------------------------------------------------------------R  fallthrough
```

Gas simulation at offset 6858 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = u8 [r8 + 573]
    D=========================eE--------------R...........  r7 = r7 ^ 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 573] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 6872 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u8 [r8 + 567]
    D=========================eE--------------R  jump 6953 if r9 == 0
```

Gas simulation at offset 6880 with total cost of 2:

```
    DeER.  r10 = 0x1
    D=eER  jump 6858 if r9 != r10
```

Gas simulation at offset 6886 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r9 = u8 [r8 + 561]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r10 = u8 [r8 + 562]
    D=========================eE--------------R............  r7 = r7 + r9
    .D=========================eE-------------R............  r7 = r7 + 0x7ff
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 449] = a3
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r7 = u8 [r8 + 561]
    .D=========================eE-------------------------R  r7 = r7 + 0x1
    ..D=========================eE------------------------R  r9 = r7 & 0x3
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 561] = a0
    ..D==========================eE-----------------------R  jump 6858 if r9 != 0
```

Gas simulation at offset 6923 with total cost of 2:

```
    DeER.  r7 = r7 & 0xff
    DeER.  r9 = 0x20
    D=eER  jump 7083 if r7 != r9
```

Gas simulation at offset 6934 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  u8 [r8 + 567] = 0x2
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = u8 [r8 + 573]
    D=========================eE--------------R...........  r7 = r7 ^ 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 573] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 6953 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r10 = u8 [r8 + 561]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r9 = u8 [r8 + 562]
    D=========================eE--------------R............  r7 = r7 + r10
    .D=========================eE-------------R............  r7 = r7 + 0x7ff
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 449] = a2
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r10 = u8 [r8 + 550]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r7 = u16 [r8 + 527]
    ..D========================eE-------------------------R  r10 = r10 & 0x20
    ..D=========================eeeeeeeeeeeeeeeeeeeeE-----R  jump 6998 if r10 != 0
```

Gas simulation at offset 6987 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 7059 if r7 <u r9
```

Gas simulation at offset 6990 with total cost of 2:

```
    DeER.  r9 = r9 + 0x8
    D=eER  jump 7007 if r7 <u r9
```

Gas simulation at offset 6996 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 7059
```

Gas simulation at offset 6998 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 7059 if r7 <u r9
```

Gas simulation at offset 7001 with total cost of 2:

```
    DeER.  r9 = r9 + 0x10
    D=eER  jump 7059 if r7 >=u r9
```

Gas simulation at offset 7007 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r8 + 561]
    D=========================eE--------------R  jump 7031 if r7 != 0
```

Gas simulation at offset 7015 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..............  r9 = u8 [r8 + 560]
    D=========================eE--------------R..............  r9 = r9 + 0xffffffffffffffff
    .D=========================eeeE-----------R..............  r9 = r9 <u 0x1
    .D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 575] = a2
    ..DeeE--------------------------------------------------R  fallthrough
```

Gas simulation at offset 7031 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeE---------------------------------------R............  r9 = 0x1
    D=eE--------------------------------------R............  r7 = r7 + r9
    D==eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R............  u8 [r8 + 561] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  u8 [r8 + 567] = a2
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r7 = u8 [r8 + 573]
    .D=========================eE-------------R............  r7 = r7 ^ r9
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 573] = a0
    ..DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 7059 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r8 + 560]
    D=========================eER.........................  r7 = r7 + 0x3
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 560] = a0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r7 = u8 [r8 + 573]
    .D========================eE-------------------------R  r7 = r7 ^ 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 573] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 7083 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  u8 [r8 + 567] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = u8 [r8 + 573]
    D=========================eE--------------R...........  r7 = r7 ^ 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 573] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 7101 with total cost of 27:

```
    DeER..........................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u8 [r7 + 484]
    D==========================eER  jump 7233 if r8 == 0
```

Gas simulation at offset 7112 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r8 = r8 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u8 [r7 + 484] = a1
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r7 + 488]
    .D========================eE--------------R  jump 7264 if r8 == 0
```

Gas simulation at offset 7128 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r8 = r8 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u8 [r7 + 488] = a1
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r7 + 492]
    .D========================eE--------------R  jump 7295 if r8 == 0
```

Gas simulation at offset 7144 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r8 = r8 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u8 [r7 + 492] = a1
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r7 + 496]
    .D========================eE--------------R  jump 7326 if r8 == 0
```

Gas simulation at offset 7160 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r8 = r8 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u8 [r7 + 496] = a1
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r7 + 500]
    .D========================eE--------------R  jump 7357 if r8 == 0
```

Gas simulation at offset 7176 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r8 = r8 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u8 [r7 + 500] = a1
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r7 + 504]
    .D========================eE--------------R  jump 7388 if r8 == 0
```

Gas simulation at offset 7192 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r8 = r8 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u8 [r7 + 504] = a1
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r7 + 508]
    .D========================eE--------------R  jump 7419 if r8 == 0
```

Gas simulation at offset 7208 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r8 = r8 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u8 [r7 + 508] = a1
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r7 + 512]
    .D========================eE--------------R  jump 7450 if r8 == 0
```

Gas simulation at offset 7224 with total cost of 26:

```
    DeER.........................  r8 = r8 + 0xffffffffffffffff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 512] = a1
    DeeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 7233 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = u8 [r7 + 481]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r9 = u8 [r7 + 482]
    D=========================eE--------------R...........  r8 = r8 << 0x1
    .D========================eE--------------R...........  r9 = r9 << 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 481] = a1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 482] = a2
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u8 [r7 + 488]
    ..D========================eE------------------------R  jump 7128 if r8 != 0
```

Gas simulation at offset 7264 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = u8 [r7 + 485]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r9 = u8 [r7 + 486]
    D=========================eE--------------R...........  r8 = r8 << 0x1
    .D========================eE--------------R...........  r9 = r9 << 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 485] = a1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 486] = a2
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u8 [r7 + 492]
    ..D========================eE------------------------R  jump 7144 if r8 != 0
```

Gas simulation at offset 7295 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = u8 [r7 + 489]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r9 = u8 [r7 + 490]
    D=========================eE--------------R...........  r8 = r8 << 0x1
    .D========================eE--------------R...........  r9 = r9 << 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 489] = a1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 490] = a2
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u8 [r7 + 496]
    ..D========================eE------------------------R  jump 7160 if r8 != 0
```

Gas simulation at offset 7326 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = u8 [r7 + 493]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r9 = u8 [r7 + 494]
    D=========================eE--------------R...........  r8 = r8 << 0x1
    .D========================eE--------------R...........  r9 = r9 << 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 493] = a1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 494] = a2
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u8 [r7 + 500]
    ..D========================eE------------------------R  jump 7176 if r8 != 0
```

Gas simulation at offset 7357 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = u8 [r7 + 497]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r9 = u8 [r7 + 498]
    D=========================eE--------------R...........  r8 = r8 << 0x1
    .D========================eE--------------R...........  r9 = r9 << 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 497] = a1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 498] = a2
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u8 [r7 + 504]
    ..D========================eE------------------------R  jump 7192 if r8 != 0
```

Gas simulation at offset 7388 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = u8 [r7 + 501]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r9 = u8 [r7 + 502]
    D=========================eE--------------R...........  r8 = r8 << 0x1
    .D========================eE--------------R...........  r9 = r9 << 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 501] = a1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 502] = a2
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u8 [r7 + 508]
    ..D========================eE------------------------R  jump 7208 if r8 != 0
```

Gas simulation at offset 7419 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = u8 [r7 + 505]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r9 = u8 [r7 + 506]
    D=========================eE--------------R...........  r8 = r8 << 0x1
    .D========================eE--------------R...........  r9 = r9 << 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 505] = a1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 506] = a2
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u8 [r7 + 512]
    ..D========================eE------------------------R  jump 7224 if r8 != 0
```

Gas simulation at offset 7450 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = u8 [r7 + 509]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r9 = u8 [r7 + 510]
    D=========================eE--------------R...........  r8 = r8 << 0x1
    .D========================eE--------------R...........  r9 = r9 << 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 509] = a1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 510] = a2
    .DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 7475 with total cost of 76:

```
    DeER...........................................................................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r1 + 0] = r5
    .DeE------------------------R..................................................  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................  r9 = u8 [r5 + 551]
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................  r10 = u8 [r5 + 575]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r5 + 560] = 0
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r5 + 567] = 0
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u8 [r5 + 573] = 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u8 [r5 + 574] = a3
    ...D================================================eER........................  r9 = r9 & 0x10
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 575] = 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeE----R  jump 7527 if r9 == 0
```

Gas simulation at offset 7522 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 548] = 0
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 7527 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 525] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 566] = 0
    DeeeeeeeeeeeeeeeE----------R  r0 = 146, jump 6010
```

Gas simulation at offset 7541 with total cost of 98:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r7 = i16 [r5 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r8 = i16 [r5 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r9 = i16 [r5 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r10 = i16 [r5 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  r11 = i16 [r5 + 537]
    .D========================eE------------------------R................................................  r8 = r8 << 0x1
    .D========================eE------------------------R................................................  r9 = r9 << 0x1
    .D========================eE------------------------R................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u16 [r5 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R..............................................  u16 [r5 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R..............................................  u16 [r5 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r5 + 535] = r10
    ...D================================================eE-----------------------R.......................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  u16 [r5 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................  r0 = u64 [r1 + 8]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r5 = u64 [r1 + 0]
    ....D=======================================================================eE-R.....................  r1 = r1 + 0x10
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 7606 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r6
    .D.............................  r5 = r7
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u8 [r6 + 573]
    ..D=========================eER  jump 7634 if r8 == 0
```

Gas simulation at offset 7630 with total cost of 15:

```
    DeER..............  r8 = 0
    DeeeeeeeeeeeeeeeER  jump 7673
```

Gas simulation at offset 7634 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r6 + 561]
    D=========================eE--------------R.............  r8 = r8 + r5
    D==========================eE-------------R.............  r8 = r8 + 0x7ff
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r8 + 449] = 0xffffffffffffffff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r8 = u8 [r6 + 561]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r9 = u8 [r6 + 573]
    .D=========================eE-------------------------R.  r8 = r8 + 0x1
    ..D=========================eE------------------------R.  r8 = r8 & 0x1f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 561] = a1
    ..D========================eE--------------------------R  r8 = r9 ^ 0x1
    ...DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 7673 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r9 = u16 [r6 + 521]
    DeE------------------------R............................  r10 = 0x2000
    D=========================eER...........................  r9 = r9 << 0x34
    D==========================eER..........................  r9 = r9 >> 0x34
    .D==========================eER.........................  r9 = r9 | r10
    .DeE--------------------------R.........................  r8 = r8 & 0x1
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 539] = r9
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u8 [r6 + 573] = a1
    ..D.....................................................  r7 = r5
    ..DeeeeeeeeeeeeeeeE------------------------------------R  r0 = 150, jump 7101
```

Gas simulation at offset 7709 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 152, jump 6010
```

Gas simulation at offset 7717 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 7785 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r6
    .D.............................  r5 = r7
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r6 + 573]
    ..D=========================eER  jump 7843 if r7 == 0
```

Gas simulation at offset 7809 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u16 [r6 + 539]
    D=========================eE--------------R  r9 = r8 >> 0x8
    .DeE--------------------------------------R  r10 = 0x3f
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u8 [r6 + 573] = 0
    .D=========================eE-------------R  jump 7901 if r9 <u r10
```

Gas simulation at offset 7827 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r8 = r8 + r5
    D==eER.........................  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeE------------R  jump 7933
```

Gas simulation at offset 7843 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r7 = u8 [r6 + 561]
    D=========================eE--------------R.............  r7 = r7 + r5
    D==========================eE-------------R.............  r7 = r7 + 0x7ff
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r7 + 449] = 0xffffffffffffffff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r7 = u8 [r6 + 561]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r8 = u8 [r6 + 573]
    .D=========================eE-------------------------R.  r7 = r7 + 0x1
    ..D=========================eE------------------------R.  r7 = r7 & 0x1f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 561] = a0
    ..D========================eE--------------------------R  r7 = r8 ^ 0x1
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u16 [r6 + 539]
    ...D========================eE-------------------------R  r7 = r7 & 0x1
    ...D=========================eE------------------------R  r9 = r8 >> 0x8
    ....DeE------------------------------------------------R  r10 = 0x3f
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 573] = a0
    ....D=========================eE-----------------------R  jump 7827 if r9 >=u r10
```

Gas simulation at offset 7901 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 156, jump [r10 + 0]
```

Gas simulation at offset 7933 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 554] = a0
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeE----------R  r0 = 158, jump 7101
```

Gas simulation at offset 7945 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 160, jump 6010
```

Gas simulation at offset 7953 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 8021 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r6
    .D.............................  r5 = r7
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u8 [r6 + 573]
    ..D=========================eER  jump 8049 if r8 == 0
```

Gas simulation at offset 8045 with total cost of 15:

```
    DeER..............  r9 = 0
    DeeeeeeeeeeeeeeeER  jump 8088
```

Gas simulation at offset 8049 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r6 + 561]
    D=========================eE--------------R.............  r8 = r8 + r5
    D==========================eE-------------R.............  r8 = r8 + 0x7ff
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r8 + 449] = 0xffffffffffffffff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r8 = u8 [r6 + 561]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r9 = u8 [r6 + 573]
    .D=========================eE-------------------------R.  r8 = r8 + 0x1
    ..D=========================eE------------------------R.  r8 = r8 & 0x1f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 561] = a1
    ..D========================eE--------------------------R  r9 = r9 ^ 0x1
    ..DeeE-------------------------------------------------R  fallthrough
```

Gas simulation at offset 8088 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r8 = u16 [r6 + 521]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r11 = u16 [r6 + 529]
    DeE------------------------R.....................  r9 = r9 & 0x1
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................  u8 [r6 + 573] = a2
    .D========================eER....................  r11 = r11 + 0xfffffffffffffeff
    .D========================eER....................  r9 = r8 >> 0x4
    .DeE------------------------R....................  r12 = 0x40
    ..D========================eER...................  r9 = r9 & 0x38
    ..D========================eeeeeeeeeeeeeeeeeeeeER  jump 8135 if r11 >=u r12
```

Gas simulation at offset 8119 with total cost of 16:

```
    DeER...............  r8 = r8 & 0xcff
    DeER...............  r10 = 0x2000
    D=eER..............  r8 = r8 | r10
    D==eER.............  r9 = r9 + r8
    .DeeeeeeeeeeeeeeeER  jump 8159
```

Gas simulation at offset 8135 with total cost of 4:

```
    DeER...  r10 = r8 & 0xc00
    DeER...  r8 = r8 << 0x3b
    D=eER..  r8 = r8 >> 0x3d
    .D=eER.  r8 = r8 | r10
    .DeE-R.  r10 = 0x23c0
    .D=eER.  r9 = r9 | r10
    .D==eER  r9 = r9 | r8
    ..DeeER  fallthrough
```

Gas simulation at offset 8159 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 539] = r9
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeE----------R  r0 = 164, jump 7101
```

Gas simulation at offset 8171 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 166, jump 6010
```

Gas simulation at offset 8179 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 8247 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r6
    .D.............................  r5 = r7
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r6 + 573]
    ..D=========================eER  jump 8305 if r7 == 0
```

Gas simulation at offset 8271 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u16 [r6 + 539]
    D=========================eE--------------R  r9 = r8 >> 0x8
    .DeE--------------------------------------R  r10 = 0x3f
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u8 [r6 + 573] = 0
    .D=========================eE-------------R  jump 8363 if r9 <u r10
```

Gas simulation at offset 8289 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r8 = r8 + r5
    D==eER.........................  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeE------------R  jump 8395
```

Gas simulation at offset 8305 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r7 = u8 [r6 + 561]
    D=========================eE--------------R.............  r7 = r7 + r5
    D==========================eE-------------R.............  r7 = r7 + 0x7ff
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r7 + 449] = 0xffffffffffffffff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r7 = u8 [r6 + 561]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r8 = u8 [r6 + 573]
    .D=========================eE-------------------------R.  r7 = r7 + 0x1
    ..D=========================eE------------------------R.  r7 = r7 & 0x1f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 561] = a0
    ..D========================eE--------------------------R  r7 = r8 ^ 0x1
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u16 [r6 + 539]
    ...D========================eE-------------------------R  r7 = r7 & 0x1
    ...D=========================eE------------------------R  r9 = r8 >> 0x8
    ....DeE------------------------------------------------R  r10 = 0x3f
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 573] = a0
    ....D=========================eE-----------------------R  jump 8289 if r9 >=u r10
```

Gas simulation at offset 8363 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 170, jump [r10 + 0]
```

Gas simulation at offset 8395 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r8 = u8 [r6 + 521]
    D=========================eER.............................  r9 = r8 & 0x2
    D=========================eER.............................  r8 = r8 >> 0x4
    .D=========================eER............................  r8 = r8 & 0x4
    .D==========================eER...........................  r8 = r8 | r9
    .DeE--------------------------R...........................  r7 = r7 & 0xff
    ..D==========================eER..........................  r7 = r7 >> r8
    ..D===========================eER.........................  r7 = r7 & 0x3
    ..D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 555] = a0
    ...D......................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE-------------------------------------R  r0 = 172, jump 7101
```

Gas simulation at offset 8433 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 174, jump 6010
```

Gas simulation at offset 8441 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 8509 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r6
    .D.............................  r5 = r7
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u8 [r6 + 573]
    ..D=========================eER  jump 8537 if r8 == 0
```

Gas simulation at offset 8533 with total cost of 15:

```
    DeER..............  r8 = 0
    DeeeeeeeeeeeeeeeER  jump 8576
```

Gas simulation at offset 8537 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r6 + 561]
    D=========================eE--------------R.............  r8 = r8 + r5
    D==========================eE-------------R.............  r8 = r8 + 0x7ff
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r8 + 449] = 0xffffffffffffffff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r8 = u8 [r6 + 561]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r9 = u8 [r6 + 573]
    .D=========================eE-------------------------R.  r8 = r8 + 0x1
    ..D=========================eE------------------------R.  r8 = r8 & 0x1f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 561] = a1
    ..D========================eE--------------------------R  r8 = r9 ^ 0x1
    ...DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 8576 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r9 = u8 [r6 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r10 = u8 [r6 + 554]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r11 = i16 [r6 + 521]
    D=========================eER............................  r9 = r9 & 0x10
    .D========================eER............................  r10 = r10 << 0x4
    .D=========================eER...........................  r9 = r9 << 0x8
    .D==========================eER..........................  r9 = r9 | r10
    .DeE--------------------------R..........................  r8 = r8 & 0x1
    ..D=======================eE--R..........................  r11 = r11 << 0x31
    ..D========================eE-R..........................  r11 = r11 >> 0x3d
    ..D==========================eER.........................  r9 = r9 | r11
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 539] = r9
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u8 [r6 + 573] = a1
    ...D.....................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE------------------------------------R  r0 = 178, jump 7101
```

Gas simulation at offset 8628 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 180, jump 6010
```

Gas simulation at offset 8636 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 8704 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r6
    .D.............................  r5 = r7
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r6 + 573]
    ..D=========================eER  jump 8762 if r7 == 0
```

Gas simulation at offset 8728 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u16 [r6 + 539]
    D=========================eE--------------R  r9 = r8 >> 0x8
    .DeE--------------------------------------R  r10 = 0x3f
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u8 [r6 + 573] = 0
    .D=========================eE-------------R  jump 8820 if r9 <u r10
```

Gas simulation at offset 8746 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r8 = r8 + r5
    D==eER.........................  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeE------------R  jump 8852
```

Gas simulation at offset 8762 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r7 = u8 [r6 + 561]
    D=========================eE--------------R.............  r7 = r7 + r5
    D==========================eE-------------R.............  r7 = r7 + 0x7ff
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r7 + 449] = 0xffffffffffffffff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r7 = u8 [r6 + 561]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r8 = u8 [r6 + 573]
    .D=========================eE-------------------------R.  r7 = r7 + 0x1
    ..D=========================eE------------------------R.  r7 = r7 & 0x1f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 561] = a0
    ..D========================eE--------------------------R  r7 = r8 ^ 0x1
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u16 [r6 + 539]
    ...D========================eE-------------------------R  r7 = r7 & 0x1
    ...D=========================eE------------------------R  r9 = r8 >> 0x8
    ....DeE------------------------------------------------R  r10 = 0x3f
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 573] = a0
    ....D=========================eE-----------------------R  jump 8746 if r9 >=u r10
```

Gas simulation at offset 8820 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 184, jump [r10 + 0]
```

Gas simulation at offset 8852 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 556] = a0
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeE----------R  r0 = 186, jump 7101
```

Gas simulation at offset 8864 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 188, jump 6010
```

Gas simulation at offset 8872 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 8940 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r6
    .D.............................  r5 = r7
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u8 [r6 + 573]
    ..D=========================eER  jump 8968 if r8 == 0
```

Gas simulation at offset 8964 with total cost of 15:

```
    DeER..............  r8 = 0
    DeeeeeeeeeeeeeeeER  jump 9007
```

Gas simulation at offset 8968 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r6 + 561]
    D=========================eE--------------R.............  r8 = r8 + r5
    D==========================eE-------------R.............  r8 = r8 + 0x7ff
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r8 + 449] = 0xffffffffffffffff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r8 = u8 [r6 + 561]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r9 = u8 [r6 + 573]
    .D=========================eE-------------------------R.  r8 = r8 + 0x1
    ..D=========================eE------------------------R.  r8 = r8 & 0x1f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 561] = a1
    ..D========================eE--------------------------R  r8 = r9 ^ 0x1
    ...DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 9007 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r9 = u8 [r6 + 554]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r10 = u16 [r6 + 521]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r11 = u8 [r6 + 550]
    D=========================eER............................  r9 = r9 << 0x4
    .D========================eER............................  r10 = r10 >> 0xc
    .D=========================eER...........................  r9 = r9 | r10
    .DeE-------------------------R...........................  r8 = r8 & 0x1
    .D========================eE-R...........................  r11 = r11 & 0x10
    ..D========================eER...........................  r11 = r11 << 0x8
    ..D=========================eER..........................  r9 = r9 | r11
    ..D==========================eER.........................  r9 = r9 | 0x8
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 539] = r9
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u8 [r6 + 573] = a1
    ...D.....................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE------------------------------------R  r0 = 192, jump 7101
```

Gas simulation at offset 9059 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 194, jump 6010
```

Gas simulation at offset 9067 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 9135 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r6
    .D.............................  r5 = r7
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r6 + 573]
    ..D=========================eER  jump 9207 if r7 == 0
```

Gas simulation at offset 9159 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u16 [r6 + 539]
    D=========================eE--------------R  r9 = r8 >> 0x8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  u8 [r6 + 573] = 0
    .D=========================eE-------------R  jump 9263 if r9 <u 63
```

Gas simulation at offset 9175 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeE---------------------------------------R.............  r8 = r8 & 0x1f
    D=eE--------------------------------------R.............  r8 = r8 + r5
    .D=eE-------------------------------------R.............  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R.............  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.............  r8 = u8 [r6 + 551]
    ..D========================eE-------------R.............  r8 = r8 & 0x18
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 557] = a0
    ..D=========================eE-------------------------R  jump 9309 if r8 != 0
```

Gas simulation at offset 9204 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 9345
```

Gas simulation at offset 9207 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r7 = u8 [r6 + 561]
    D=========================eE--------------R.............  r7 = r7 + r5
    D==========================eE-------------R.............  r7 = r7 + 0x7ff
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r7 + 449] = 0xffffffffffffffff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r7 = u8 [r6 + 561]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R.  r8 = u8 [r6 + 573]
    .D=========================eE-------------------------R.  r7 = r7 + 0x1
    ..D=========================eE------------------------R.  r7 = r7 & 0x1f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 561] = a0
    ..D========================eE--------------------------R  r7 = r8 ^ 0x1
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u16 [r6 + 539]
    ...D========================eE-------------------------R  r7 = r7 & 0x1
    ...D=========================eE------------------------R  r9 = r8 >> 0x8
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 573] = a0
    ....D=========================eE-----------------------R  jump 9175 if r9 >=u 63
```

Gas simulation at offset 9263 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 198, jump [r10 + 0]
```

Gas simulation at offset 9295 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r6 + 551]
    D=========================eER.  r8 = r8 & 0x18
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.  u8 [r6 + 557] = a0
    D==========================eER  jump 9345 if r8 == 0
```

Gas simulation at offset 9309 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......  r8 = u16 [r6 + 521]
    D=========================eE--------------R......  r9 = r8 & 0x1f
    .D========================eE--------------R......  r8 = r8 & 0xffffffffffffffe0
    .D=========================eeeeeeeeeeeeeeeeeeeeER  jump 9334 if r9 != 31
```

Gas simulation at offset 9324 with total cost of 26:

```
    DeER.........................  r8 = r8 ^ 0x400
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 521] = r8
    DeeeeeeeeeeeeeeeE-----------R  jump 9345
```

Gas simulation at offset 9334 with total cost of 27:

```
    DeER..........................  r8 = r8 | r9
    D=eER.........................  r8 = r8 + 0x1
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 521] = r8
    DeeE-------------------------R  fallthrough
```

Gas simulation at offset 9345 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r6 + 555]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r6 + 556]
    .D========================eE--------------R.............  r10 = r8 << 0x3f
    .D========================eE--------------R.............  r8 = r8 << 0x6
    .D=========================eE-------------R.............  r10 = r10 >>a 0x3f
    ..D========================eE-------------R.............  r8 = sext8 r8
    ..D=========================eE------------R.............  r8 = r8 >> 0x7
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER...  u8 [r6 + 531] = a2
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------R...  u8 [r6 + 533] = a0
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r6 + 535] = a3
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 537] = a1
    ...D....................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 200, jump 7101
```

Gas simulation at offset 9392 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 202, jump 6010
```

Gas simulation at offset 9400 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 9468 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r6
    .D...........................  r5 = r7
    .DeE------------------------R  r6 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeE----------R  r0 = 206, jump 6819
```

Gas simulation at offset 9491 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r7 = u16 [r6 + 521]
    D=========================eER...........................  r7 = r7 << 0x34
    D==========================eER..........................  r7 = r7 >> 0x34
    D===========================eER.........................  r7 = r7 | 0x2000
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 539] = r7
    .D......................................................  r7 = r5
    .DeeeeeeeeeeeeeeeE-------------------------------------R  r0 = 208, jump 7101
```

Gas simulation at offset 9517 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 210, jump 6010
```

Gas simulation at offset 9525 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 9593 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r6
    .D...........................  r5 = r7
    .DeE------------------------R  r6 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeE----------R  r0 = 214, jump 6819
```

Gas simulation at offset 9616 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r6 + 539]
    D=========================eER.  r7 = r8 >> 0x8
    DeE-------------------------R.  r9 = 0x3f
    .D=========================eER  jump 9663 if r7 >=u r9
```

Gas simulation at offset 9629 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 216, jump [r10 + 0]
```

Gas simulation at offset 9661 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 9678
```

Gas simulation at offset 9663 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r8 = r8 + r5
    D==eER.........................  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 9678 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 554] = a0
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeE----------R  r0 = 218, jump 7101
```

Gas simulation at offset 9690 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 220, jump 6010
```

Gas simulation at offset 9698 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 9766 with total cost of 27:

```
    DeER..........................  r1 = r1 + 0xffffffffffffffe0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 24] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 16] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 8] = r6
    .D............................  r5 = r7
    .DeE------------------------R.  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = 0xc00
    ..D...........................  r7 = r5
    ..DeeeeeeeeeeeeeeeE----------R  r0 = 224, jump 6819
```

Gas simulation at offset 9796 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r7 = u16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r8 = u16 [r6 + 521]
    D=========================eER....................  r9 = r7 + 0xfffffffffffffeff
    .D========================eER....................  r7 = r8 >> 0x4
    .DeE------------------------R....................  r10 = 0x40
    .D=========================eER...................  r7 = r7 & 0x38
    ..D========================eeeeeeeeeeeeeeeeeeeeER  jump 9841 if r9 >=u r10
```

Gas simulation at offset 9820 with total cost of 29:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER....  r9 = u64 [r1 + 0]
    D=========================eER...  r9 = r9 + 0xff
    D==========================eER..  r8 = r8 & r9
    DeE--------------------------R..  r9 = 0x2000
    .D==========================eER.  r8 = r8 + r9
    .D===========================eER  r7 = r7 + r8
    .DeeeeeeeeeeeeeeeE-------------R  jump 9866
```

Gas simulation at offset 9841 with total cost of 28:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...  r9 = u64 [r1 + 0]
    D=========================eER..  r9 = r9 & r8
    DeE-------------------------R..  r8 = r8 << 0x3b
    D=eE------------------------R..  r8 = r8 >> 0x3d
    .D=========================eER.  r8 = r8 | r9
    .DeE-------------------------R.  r9 = 0x23c0
    .D=eE------------------------R.  r7 = r7 | r9
    .D==========================eER  r7 = r7 | r8
    ..DeeE------------------------R  fallthrough
```

Gas simulation at offset 9866 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 539] = r7
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeE----------R  r0 = 226, jump 7101
```

Gas simulation at offset 9878 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 228, jump 6010
```

Gas simulation at offset 9886 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 24]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 16]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 8]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x20
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 9955 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r6
    .D...........................  r5 = r7
    .DeE------------------------R  r6 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeE----------R  r0 = 232, jump 6819
```

Gas simulation at offset 9978 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r6 + 539]
    D=========================eER.  r7 = r8 >> 0x8
    D==========================eER  jump 10023 if r7 >=u 63
```

Gas simulation at offset 9989 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 234, jump [r10 + 0]
```

Gas simulation at offset 10021 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 10038
```

Gas simulation at offset 10023 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r8 = r8 + r5
    D==eER.........................  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 10038 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r8 = u8 [r6 + 521]
    D=========================eER.............................  r9 = r8 & 0x2
    D=========================eER.............................  r8 = r8 >> 0x4
    .D=========================eER............................  r8 = r8 & 0x4
    .D==========================eER...........................  r8 = r8 | r9
    .DeE--------------------------R...........................  r7 = r7 & 0xff
    ..D==========================eER..........................  r7 = r7 >> r8
    ..D===========================eER.........................  r7 = r7 & 0x3
    ..D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 555] = a0
    ...D......................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE-------------------------------------R  r0 = 236, jump 7101
```

Gas simulation at offset 10076 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 238, jump 6010
```

Gas simulation at offset 10084 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 10152 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r6
    .D...........................  r5 = r7
    .DeE------------------------R  r6 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeE----------R  r0 = 242, jump 6819
```

Gas simulation at offset 10175 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r7 = u8 [r6 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r8 = u8 [r6 + 554]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r9 = i16 [r6 + 521]
    D=========================eER............................  r7 = r7 & 0x10
    .D========================eER............................  r8 = r8 << 0x4
    .D========================eER............................  r9 = r9 << 0x31
    .D=========================eER...........................  r7 = r7 << 0x8
    .D==========================eER..........................  r7 = r7 | r8
    ..D========================eE-R..........................  r9 = r9 >> 0x3d
    ..D==========================eER.........................  r7 = r7 | r9
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 539] = r7
    ..D......................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE------------------------------------R  r0 = 244, jump 7101
```

Gas simulation at offset 10220 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 246, jump 6010
```

Gas simulation at offset 10228 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 10296 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r6
    .D...........................  r5 = r7
    .DeE------------------------R  r6 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeE----------R  r0 = 250, jump 6819
```

Gas simulation at offset 10319 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r6 + 539]
    D=========================eER.  r7 = r8 >> 0x8
    DeE-------------------------R.  r9 = 0x3f
    .D=========================eER  jump 10366 if r7 >=u r9
```

Gas simulation at offset 10332 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 252, jump [r10 + 0]
```

Gas simulation at offset 10364 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 10381
```

Gas simulation at offset 10366 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r8 = r8 + r5
    D==eER.........................  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 10381 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 556] = a0
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeE----------R  r0 = 254, jump 7101
```

Gas simulation at offset 10393 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 256, jump 6010
```

Gas simulation at offset 10401 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 10469 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r6
    .D...........................  r5 = r7
    .DeE------------------------R  r6 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeE----------R  r0 = 260, jump 6819
```

Gas simulation at offset 10492 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r7 = u8 [r6 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r8 = u8 [r6 + 554]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r9 = u16 [r6 + 521]
    D=========================eER............................  r7 = r7 & 0x10
    .D========================eER............................  r8 = r8 << 0x4
    .D========================eER............................  r9 = r9 >> 0xc
    .D=========================eER...........................  r7 = r7 << 0x8
    .D=========================eER...........................  r8 = r8 | r9
    ..D=========================eER..........................  r7 = r7 | r8
    ..D==========================eER.........................  r7 = r7 | 0x8
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 539] = r7
    ..D......................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE------------------------------------R  r0 = 262, jump 7101
```

Gas simulation at offset 10537 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 264, jump 6010
```

Gas simulation at offset 10545 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 10613 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r6
    .D...........................  r5 = r7
    .DeE------------------------R  r6 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeE----------R  r0 = 268, jump 6819
```

Gas simulation at offset 10636 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r6 + 539]
    D=========================eER.  r7 = r8 >> 0x8
    D==========================eER  jump 10695 if r7 >=u 63
```

Gas simulation at offset 10647 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 270, jump [r10 + 0]
```

Gas simulation at offset 10679 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r6 + 551]
    D=========================eER.  r8 = r8 & 0x18
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.  u8 [r6 + 557] = a0
    D==========================eER  jump 10724 if r8 != 0
```

Gas simulation at offset 10693 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 10760
```

Gas simulation at offset 10695 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeE---------------------------------------R.............  r8 = r8 & 0x1f
    D=eE--------------------------------------R.............  r8 = r8 + r5
    .D=eE-------------------------------------R.............  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R.............  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.............  r8 = u8 [r6 + 551]
    ..D========================eE-------------R.............  r8 = r8 & 0x18
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 557] = a0
    ..D=========================eE-------------------------R  jump 10760 if r8 == 0
```

Gas simulation at offset 10724 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......  r8 = u16 [r6 + 521]
    D=========================eE--------------R......  r9 = r8 & 0x1f
    .D========================eE--------------R......  r8 = r8 & 0xffffffffffffffe0
    .D=========================eeeeeeeeeeeeeeeeeeeeER  jump 10749 if r9 != 31
```

Gas simulation at offset 10739 with total cost of 26:

```
    DeER.........................  r8 = r8 ^ 0x400
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 521] = r8
    DeeeeeeeeeeeeeeeE-----------R  jump 10760
```

Gas simulation at offset 10749 with total cost of 27:

```
    DeER..........................  r8 = r8 | r9
    D=eER.........................  r8 = r8 + 0x1
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 521] = r8
    DeeE-------------------------R  fallthrough
```

Gas simulation at offset 10760 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r6 + 555]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r6 + 556]
    .D========================eE--------------R.............  r10 = r8 << 0x3f
    .D========================eE--------------R.............  r8 = r8 << 0x6
    .D=========================eE-------------R.............  r10 = r10 >>a 0x3f
    ..D========================eE-------------R.............  r8 = sext8 r8
    ..D=========================eE------------R.............  r8 = r8 >> 0x7
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER...  u8 [r6 + 531] = a2
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------R...  u8 [r6 + 533] = a0
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r6 + 535] = a3
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 537] = a1
    ...D....................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 272, jump 7101
```

Gas simulation at offset 10807 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 274, jump 6010
```

Gas simulation at offset 10815 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r6 + 537]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D========================eE------------------------R..................................................  r9 = r9 << 0x1
    .D========================eE------------------------R..................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R..................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r6 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R................................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 535] = r10
    ...D================================================eE-----------------------R.........................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r6 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  r0 = u64 [r1 + 16]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r5 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x18
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 10883 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r6
    .D...........................  r5 = r7
    .DeE------------------------R  r6 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeE----------R  r0 = 278, jump 6819
```

Gas simulation at offset 10906 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r6 + 539]
    D=========================eER.  r7 = r8 >> 0x8
    D==========================eER  jump 10965 if r7 >=u 63
```

Gas simulation at offset 10917 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 280, jump [r10 + 0]
```

Gas simulation at offset 10949 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r6 + 551]
    D=========================eER.  r8 = r8 & 0x18
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.  u8 [r6 + 557] = a0
    D==========================eER  jump 10994 if r8 != 0
```

Gas simulation at offset 10963 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 11030
```

Gas simulation at offset 10965 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeE---------------------------------------R.............  r8 = r8 & 0x1f
    D=eE--------------------------------------R.............  r8 = r8 + r5
    .D=eE-------------------------------------R.............  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R.............  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.............  r8 = u8 [r6 + 551]
    ..D========================eE-------------R.............  r8 = r8 & 0x18
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 557] = a0
    ..D=========================eE-------------------------R  jump 11030 if r8 == 0
```

Gas simulation at offset 10994 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......  r9 = u16 [r6 + 521]
    D=========================eE--------------R......  r10 = r9 & 0x1f
    .D========================eE--------------R......  r9 = r9 & 0xffffffffffffffe0
    .D=========================eeeeeeeeeeeeeeeeeeeeER  jump 11019 if r10 != 31
```

Gas simulation at offset 11009 with total cost of 26:

```
    DeER.........................  r9 = r9 ^ 0x400
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 521] = r9
    DeeeeeeeeeeeeeeeE-----------R  jump 11030
```

Gas simulation at offset 11019 with total cost of 27:

```
    DeER..........................  r9 = r9 | r10
    D=eER.........................  r9 = r9 + 0x1
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 521] = r9
    DeeE-------------------------R  fallthrough
```

Gas simulation at offset 11030 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r6 + 555]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r10 = u8 [r6 + 556]
    .D========================eE--------------R.............  r11 = r9 << 0x3f
    .D========================eE--------------R.............  r9 = r9 << 0x6
    .D=========================eE-------------R.............  r11 = r11 >>a 0x3f
    ..D========================eE-------------R.............  r9 = sext8 r9
    ..D=========================eE------------R.............  r9 = r9 >> 0x7
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER...  u8 [r6 + 531] = a3
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------R...  u8 [r6 + 533] = a0
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r6 + 535] = a4
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 537] = a2
    ...DeE-------------------------------------------------R  jump 11187 if r8 == 0
```

Gas simulation at offset 11072 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r7 = u16 [r6 + 521]
    DeE---------------------------------------R.......  r10 = 0x7
    .D========================eE--------------R.......  r9 = r7 << 0x31
    .D=========================eE-------------R.......  r9 = r9 >> 0x3d
    .DeE--------------------------------------R.......  r8 = 0x8c1f
    ..D=========================eeeeeeeeeeeeeeeeeeeeER  jump 11123 if r9 != r10
```

Gas simulation at offset 11094 with total cost of 22:

```
    DeER.....................  r9 = r7 >> 0x5
    D=eER....................  r10 = r9 & 0x1f
    .DeER....................  r11 = 0x1d
    .D=eeeeeeeeeeeeeeeeeeeeER  jump 11146 if r10 == r11
```

Gas simulation at offset 11106 with total cost of 21:

```
    DeER....................  r11 = 0x1f
    D=eeeeeeeeeeeeeeeeeeeeER  jump 11164 if r10 != r11
```

Gas simulation at offset 11112 with total cost of 26:

```
    DeER.........................  r7 = r7 & 0x8c1f
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 521] = r7
    DeeeeeeeeeeeeeeeE-----------R  jump 11187
```

Gas simulation at offset 11123 with total cost of 28:

```
    DeER...........................  r9 = r9 + 0x1
    DeER...........................  r8 = 0x8fff
    D=eER..........................  r7 = r7 & r8
    D=eER..........................  r9 = r9 << 0xc
    .D=eER.........................  r7 = r7 | r9
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 521] = r7
    .DeeeeeeeeeeeeeeeE------------R  jump 11187
```

Gas simulation at offset 11146 with total cost of 27:

```
    DeER..........................  r7 = r7 & 0x8c1f
    DeER..........................  r8 = 0x800
    D=eER.........................  r7 = r7 ^ r8
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 521] = r7
    .DeeeeeeeeeeeeeeeE-----------R  jump 11187
```

Gas simulation at offset 11164 with total cost of 29:

```
    DeER............................  r9 = r9 << 0x5
    DeER............................  r7 = r7 & 0x8c1f
    D=eER...........................  r8 = r9 + 0x20
    .D=eER..........................  r8 = r8 & 0x3e0
    .D==eER.........................  r7 = r7 | r8
    .D===eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 521] = r7
    .DeeE--------------------------R  fallthrough
```

Gas simulation at offset 11187 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = i16 [r6 + 529]
    D=========================eE--------------R...........  r7 = r7 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 529] = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r0 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r6 = u64 [r1 + 0]
    .D=========================eE------------------------R  r1 = r1 + 0x18
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 11212 with total cost of 54:

```
    DeER.....................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u16 [r7 + 521]
    DeE-------------------------R............................  r9 = 0x1
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r11 = u8 [r7 + 551]
    .D=========================eER...........................  r12 = r8 << 0x34
    .D==========================eER..........................  r12 = r12 >> 0x34
    ..D==========================eER.........................  r10 = r12 | 0x2000
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--R.........................  r12 = u8 [r7 + 449]
    ..D========================eE--R.........................  r11 = r11 & 0x18
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 539] = r10
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u8 [r7 + 561] = a2
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u8 [r7 + 562] = a5
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u8 [r7 + 564] = a5
    ....D========================eE-------------------------R  jump 11284 if r11 == 0
```

Gas simulation at offset 11263 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r9 = u16 [r7 + 523]
    DeE---------------------------------------R............  r8 = r8 & 0xfffffffffffffbe0
    D=========================eE--------------R............  r9 = r9 & 0x41f
    .D=========================eE-------------R............  r8 = r8 | r9
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 521] = r8
    .DeeE-------------------------------------------------R  fallthrough
```

Gas simulation at offset 11284 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = i16 [r7 + 529]
    D=========================eE--------------R...........  r8 = r8 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 529] = r8
    .DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 11298 with total cost of 79:

```
    DeER..............................................................................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u64 [r1 + 0] = r5
    .DeE------------------------R.....................................................  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r9 = u8 [r5 + 561]
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r8 = u16 [r5 + 539]
    ..DeE------------------------R....................................................  r10 = 0x3f
    ..D=========================eER...................................................  r11 = r7 + r9
    ..D==========================eER..................................................  r11 = r11 + 0x7ff
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r11 = u8 [r11 + 449]
    ...D========================eE--------------------------R.........................  r9 = r9 + 0x1
    ...D========================eE--------------------------R.........................  r12 = r8 >> 0x8
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.........................  u8 [r5 + 561] = a2
    ....D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 562] = a4
    ....D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 563] = a4
    ....D========================eE--------------------------------------------------R  jump 11387 if r12 >=u r10
```

Gas simulation at offset 11353 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 286, jump [r10 + 0]
```

Gas simulation at offset 11385 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 11402
```

Gas simulation at offset 11387 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 11402 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = i16 [r5 + 529]
    D=========================eER.........................  r8 = r8 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 529] = r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u8 [r5 + 554] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r0 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r5 = u64 [r1 + 0]
    .D========================eE-------------------------R  r1 = r1 + 0x10
    .D=========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 11427 with total cost of 79:

```
    DeER..............................................................................  r8 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r10 = u16 [r8 + 521]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r4 = u16 [r8 + 529]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r12 = u8 [r8 + 561]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r11 = u8 [r8 + 566]
    .DeE------------------------R.....................................................  r2 = 0xc00
    .D=eE-----------------------R.....................................................  r3 = 0x40
    ..D========================eER....................................................  r9 = r7 + r12
    ..D========================eER....................................................  r11 = r11 << 0x2
    ..D=========================eER...................................................  r9 = r9 + 0x7ff
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r9 = u8 [r9 + 449]
    ...D=======================eE--------------------------R..........................  r12 = r12 + 0x1
    ...D========================eE-------------------------R..........................  r7 = r7 + r11
    ...D=========================eE------------------------R..........................  r7 = r7 + 0x7ff
    ....D=================================================eER.........................  r11 = r9 & 0xffffffffffffffe3
    ....D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 483] = a4
    .....D=====================eE----------------------------------------------------R  r7 = r4 + 0xfffffffffffffeff
    .....D======================eeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R  u8 [r8 + 561] = a5
    .....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  u8 [r8 + 562] = a2
    ......D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 565] = a4
    ......D=====================eE---------------------------------------------------R  r9 = r10 >> 0x4
    ......D======================eE--------------------------------------------------R  r11 = zext16 r7
    .......D======================eE-------------------------------------------------R  r7 = r9 & 0x38
    .......D======================eeeeeeeeeeeeeeeeeeeeE------------------------------R  jump 11539 if r11 >=u r3
```

Gas simulation at offset 11512 with total cost of 28:

```
    DeER...........................  r9 = r10 & 0xcff
    DeER...........................  r10 = 0x2000
    D=eER..........................  r9 = r9 | r10
    .D=eER.........................  r7 = r7 + r9
    .DeE-R.........................  r4 = r4 + 0x1
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r8 + 529] = r4
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r8 + 539] = r7
    ..DeeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 11539 with total cost of 29:

```
    DeER............................  r9 = r10 & 0xc00
    DeER............................  r10 = r10 << 0x3b
    D=eER...........................  r10 = r10 >> 0x3d
    .D=eER..........................  r9 = r9 | r10
    .DeE-R..........................  r10 = 0x23c0
    .D=eER..........................  r7 = r7 | r10
    .D==eER.........................  r7 = r7 | r9
    ..DeE-R.........................  r4 = r4 + 0x1
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r8 + 529] = r4
    ..D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r8 + 539] = r7
    ..DeeeeeeeeeeeeeeeeeeeeeeE-----R  jump [r0 + 0]
```

Gas simulation at offset 11575 with total cost of 79:

```
    DeER..............................................................................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u64 [r1 + 0] = r5
    .DeE------------------------R.....................................................  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r8 = u8 [r5 + 561]
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r9 = u8 [r5 + 566]
    ..D=========================eER...................................................  r8 = r8 + r7
    ..D==========================eER..................................................  r8 = r8 + 0x7ff
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r10 = u8 [r8 + 449]
    ..D=========================eE--------------------------R.........................  r9 = r9 << 0x2
    ...D=========================eE-------------------------R.........................  r9 = r9 + r7
    ...D==========================eE------------------------R.........................  r8 = r9 + 0x7ff
    ...D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 484] = a3
    ....D======================eeeeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  r8 = u16 [r5 + 539]
    ....D===============================================eE---------------------------R  r9 = r8 >> 0x8
    ....DeE--------------------------------------------------------------------------R  r11 = 0x3f
    .....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 562] = a3
    .....D===============================================eE--------------------------R  jump 11671 if r9 >=u r11
```

Gas simulation at offset 11637 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 292, jump [r10 + 0]
```

Gas simulation at offset 11669 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 11686
```

Gas simulation at offset 11671 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 11686 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r8 = u8 [r5 + 521]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r9 = i16 [r5 + 529]
    D=========================eER.............................  r10 = r8 & 0x2
    .D========================eER.............................  r8 = r8 >> 0x4
    .D=========================eER............................  r8 = r8 & 0x4
    .D==========================eER...........................  r8 = r8 | r10
    .DeE--------------------------R...........................  r7 = r7 & 0xff
    ..D========================eE-R...........................  r9 = r9 + 0x1
    ..D==========================eER..........................  r7 = r7 >> r8
    ..D===========================eER.........................  r7 = r7 & 0x3
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER...  u16 [r5 + 529] = r9
    ...D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 555] = a0
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R  r0 = u64 [r1 + 8]
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R  r5 = u64 [r1 + 0]
    ....D========================eE--------------------------R  r1 = r1 + 0x10
    ....D========================eeeeeeeeeeeeeeeeeeeeeeE-----R  jump [r0 + 0]
```

Gas simulation at offset 11737 with total cost of 78:

```
    DeER.............................................................................  r8 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r11 = u8 [r8 + 561]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r12 = u8 [r8 + 550]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r9 = u8 [r8 + 563]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r10 = i8 [r8 + 565]
    .D=========================eER...................................................  r7 = r7 + r11
    .D==========================eER..................................................  r7 = r7 + 0x7ff
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u8 [r7 + 449]
    ..D========================eE--------------------------R.........................  r11 = r12 & 0x20
    ..D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 562] = a0
    ...D========================eE--------------------------------------------------R  jump 11822 if r11 != 0
```

Gas simulation at offset 11778 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...............  r7 = i16 [r8 + 527]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...............  r11 = u8 [r8 + 564]
    DeE---------------------------------------R...............  r10 = r10 >>a 0x3f
    .D========================eeE-------------R...............  i32 r7 = r7 - r11
    .D==========================eE------------R...............  r7 = r7 ^ r10
    .D===========================eE-----------R...............  r7 = r7 & 0x7
    ..DeE-------------------------------------R...............  r9 = r9 << 0x4
    ..D===========================eE----------R...............  r7 = r7 | r9
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R...............  r9 = i16 [r8 + 529]
    ..D=========================eE------------R...............  r9 = r9 + 0x1
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u16 [r8 + 529] = r9
    ...D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 539] = a0
    ...DeeeeeeeeeeeeeeeeeeeeeeE------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 11822 with total cost of 64:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER........................  unlikely
    DeeeE-------------------------------------R........................  r7 = r10 <s 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R........................  r10 = i16 [r8 + 527]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R........................  r11 = u8 [r8 + 564]
    .DeE--------------------------------------R........................  r9 = r9 & 0xe
    .DeE--------------------------------------R........................  r12 = 0xfffffffffffffff8
    ..DeE-------------------------------------R........................  r2 = 0x7
    ..D========================eeE------------R........................  i32 r10 = r10 - r11
    ..D==========================eE-----------R........................  r10 = r10 & 0xf
    ...D==========================eeeE--------R........................  r11 = r10 <u 0x8
    ....D============================eeE------R........................  r12 = 0 if r11 != 0
    ....D============================eE-------R........................  r11 = r11 ^ r7
    .....D=============================eE-----R........................  r10 = r10 + r12
    .....D============================eE------R........................  r11 = r11 ^ 0x1
    .....D=============================eE-----R........................  r9 = r9 | r11
    ......D=============================eE----R........................  r11 = r2 - r10
    ......D==============================eeE--R........................  r11 = r10 if r7 == 0
    .......D============================eE----R........................  r7 = r9 << 0x4
    .......D===============================eE-R........................  r7 = r7 + r11
    .......DeeeeeeeeeeeeeeeeeeeeeeeeeE--------R........................  r9 = i16 [r8 + 529]
    ........D========================eE-------R........................  r9 = r9 + 0x1
    ........D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......  u16 [r8 + 529] = r9
    ........D===============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 539] = a0
    ........DeeeeeeeeeeeeeeeeeeeeeeE----------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 11894 with total cost of 79:

```
    DeER..............................................................................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u64 [r1 + 0] = r6
    .D................................................................................  r5 = r7
    .DeE------------------------R.....................................................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r9 = u8 [r6 + 561]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r7 = u8 [r6 + 550]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u8 [r6 + 563]
    ..D=========================eE-----------------------R............................  r9 = r9 + r5
    ..D==========================eE----------------------R............................  r9 = r9 + 0x7ff
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r9 = u8 [r9 + 449]
    ...D================================================eE--R.........................  r10 = r7 & 0x20
    ...D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 562] = a2
    ....D===============================================eE---------------------------R  r9 = r8 << 0x4
    ....D================================================eE--------------------------R  jump 12004 if r10 != 0
```

Gas simulation at offset 11947 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r7 = r7 & 0x8
    D=eE--------------------------------------R  r7 = r7 << 0x9
    D==eE-------------------------------------R  r7 = r7 | r9
    .D==eE------------------------------------R  r7 = r7 >> 0x8
    .D===eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R  u8 [r6 + 540] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  r8 = u16 [r6 + 539]
    ..D========================eE-------------R  r7 = r8 >> 0x8
    ..DeE-------------------------------------R  r9 = 0x3f
    ..D=========================eE------------R  jump 12033 if r7 <u r9
```

Gas simulation at offset 11977 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r8 = r8 & 0x1f
    D=eE--------------------------------------R.......  r8 = r8 + r5
    .D=eE-------------------------------------R.......  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R.......  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r8 = u8 [r6 + 565]
    ..D========================eE-------------R.......  r8 = r8 & 0x40
    ..D=========================eeeeeeeeeeeeeeeeeeeeER  jump 12075 if r8 != 0
```

Gas simulation at offset 12002 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 12122
```

Gas simulation at offset 12004 with total cost of 29:

```
    DeER............................  r8 = r8 << 0xc
    D=eER...........................  r8 = r8 | r9
    D==eER..........................  r7 = r8 << 0x33
    .D==eER.........................  r7 = r7 >> 0x3b
    .D===eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 540] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE---R  r8 = u16 [r6 + 539]
    ..D========================eE--R  r7 = r8 >> 0x8
    ..DeE--------------------------R  r9 = 0x3f
    ..D=========================eE-R  jump 11977 if r7 >=u r9
```

Gas simulation at offset 12033 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 298, jump [r10 + 0]
```

Gas simulation at offset 12065 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r6 + 565]
    D=========================eER.  r8 = r8 & 0x40
    D==========================eER  jump 12122 if r8 == 0
```

Gas simulation at offset 12075 with total cost of 11:

```
    DeER..........  r8 = r7 & 0xff
    DeER..........  r9 = r7 << 0xb
    .DeER.........  r10 = r8 << 0x1
    .D=eER........  r9 = r9 | r10
    .DeE-R........  r10 = 0x22110
    ..DeER........  r7 = r7 << 0xf
    ..DeER........  r8 = r8 << 0x5
    ..D=eER.......  r7 = r7 | r8
    ..D=eER.......  r9 = r9 & r10
    ...D=eER......  r7 = r7 & 0x88440
    ...D==eER.....  r7 = r7 | r9
    ...D===eeeER..  r7 = r7 * 0x10101
    ....D=====eeER  i32 r7 = r7 >> 0x10
    ....DeeE-----R  fallthrough
```

Gas simulation at offset 12122 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r6 + 566]
    D=========================eE--------------R.............  r8 = r8 << 0x2
    D==========================eE-------------R.............  r8 = r8 + r5
    .D==========================eE------------R.............  r8 = r8 + 0x7ff
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 481] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R  r7 = i16 [r6 + 529]
    .D=========================eE--------------------------R  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  u16 [r6 + 529] = r7
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r0 = u64 [r1 + 16]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r5 = u64 [r1 + 8]
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  r6 = u64 [r1 + 0]
    ...D========================eE-------------------------R  r1 = r1 + 0x18
    ...D========================eeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 12165 with total cost of 78:

```
    DeER.............................................................................  r8 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r11 = u8 [r8 + 561]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r12 = u8 [r8 + 550]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r9 = u8 [r8 + 563]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r10 = i8 [r8 + 565]
    .D=========================eER...................................................  r7 = r7 + r11
    .D==========================eER..................................................  r7 = r7 + 0x7ff
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u8 [r7 + 449]
    ..D========================eE--------------------------R.........................  r11 = r12 & 0x20
    ..D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 562] = a0
    ...D========================eE--------------------------------------------------R  jump 12253 if r11 != 0
```

Gas simulation at offset 12206 with total cost of 56:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R................  r7 = i16 [r8 + 527]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R................  r11 = u8 [r8 + 564]
    DeE---------------------------------------R................  r10 = r10 >>a 0x3f
    .D========================eeE-------------R................  i32 r7 = r7 - r11
    .D==========================eE------------R................  r7 = r7 ^ r10
    .D===========================eE-----------R................  r7 = r7 & 0x7
    ..DeE-------------------------------------R................  r9 = r9 << 0x4
    ..D===========================eE----------R................  r7 = r7 | r9
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R................  r9 = i16 [r8 + 529]
    ..D============================eE---------R................  r7 = r7 + 0x8
    ...D========================eE------------R................  r9 = r9 + 0x1
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...  u16 [r8 + 529] = r9
    ...D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 539] = a0
    ...DeeeeeeeeeeeeeeeeeeeeeeE-------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 12253 with total cost of 65:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  unlikely
    DeeeE-------------------------------------R.........................  r7 = r10 <s 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.........................  r10 = i16 [r8 + 527]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.........................  r11 = u8 [r8 + 564]
    .DeE--------------------------------------R.........................  r9 = r9 & 0xe
    .DeE--------------------------------------R.........................  r12 = 0xfffffffffffffff8
    ..DeE-------------------------------------R.........................  r2 = 0x7
    ..D========================eeE------------R.........................  i32 r10 = r10 - r11
    ..D==========================eE-----------R.........................  r10 = r10 & 0xf
    ...D==========================eeeE--------R.........................  r11 = r10 <u 0x8
    ....D============================eeE------R.........................  r12 = 0 if r11 != 0
    ....D============================eE-------R.........................  r11 = r11 ^ r7
    .....D=============================eE-----R.........................  r10 = r10 + r12
    .....D============================eE------R.........................  r11 = r11 ^ 0x1
    .....D=============================eE-----R.........................  r9 = r9 | r11
    ......D=============================eE----R.........................  r11 = r2 - r10
    ......D==============================eeE--R.........................  r11 = r10 if r7 == 0
    .......D============================eE----R.........................  r7 = r9 << 0x4
    .......D===============================eE-R.........................  r7 = r7 + r11
    .......DeeeeeeeeeeeeeeeeeeeeeeeeeE--------R.........................  r9 = i16 [r8 + 529]
    ........D===============================eER.........................  r7 = r7 + 0x8
    ........D========================eE-------R.........................  r9 = r9 + 0x1
    ........D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.......  u16 [r8 + 529] = r9
    ........D================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 539] = a0
    .........DeeeeeeeeeeeeeeeeeeeeeeE----------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 12328 with total cost of 79:

```
    DeER..............................................................................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  u64 [r1 + 0] = r6
    .D................................................................................  r5 = r7
    .DeE------------------------R.....................................................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r9 = u8 [r6 + 561]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u8 [r6 + 550]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r7 = u8 [r6 + 563]
    ..D=========================eE-----------------------R............................  r10 = r5 + r9
    ...D=========================eE----------------------R............................  r10 = r10 + 0x7ff
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r10 = u8 [r10 + 449]
    ...D========================eE--------------------------R.........................  r9 = r9 + 0x1
    ....D===============================================eE--R.........................  r11 = r8 & 0x20
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.........................  u8 [r6 + 561] = a2
    ....D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 562] = a3
    .....D===============================================eeeeeeeeeeeeeeeeeeeeE-------R  jump 12399 if r11 != 0
```

Gas simulation at offset 12385 with total cost of 16:

```
    DeER...............  r8 = r8 & 0x8
    D=eER..............  r8 = r8 << 0x9
    DeE-R..............  r7 = r7 << 0x4
    D==eER.............  r7 = r7 | r8
    .DeeeeeeeeeeeeeeeER  jump 12468
```

Gas simulation at offset 12399 with total cost of 39:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............  r8 = i16 [r6 + 527]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............  r9 = u8 [r6 + 564]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............  r10 = i8 [r6 + 565]
    .DeE-----------------------R..............  r11 = r7 & 0x1
    .D=eE----------------------R..............  r7 = r7 & 0xfe
    .DeE-----------------------R..............  r12 = 0xfffffffffffffff8
    ..DeE----------------------R..............  r2 = 0x7
    ..D=eE---------------------R..............  r11 = r11 << 0xc
    ...D======================eeeER...........  r10 = r10 <s 0
    ....D=====================eeE-R...........  i32 r8 = r8 - r9
    ....D=======================eER...........  r8 = r8 & 0xf
    .....D=======================eeeER........  r9 = r8 <u 0x8
    ......D=========================eeER......  r12 = 0 if r9 != 0
    ......D=========================eE-R......  r9 = r9 ^ r10
    .......D==========================eER.....  r8 = r8 + r12
    .......D=========================eE-R.....  r9 = r9 ^ 0x1
    .......D==========================eER.....  r7 = r7 | r9
    ........D==========================eER....  r9 = r2 - r8
    ........D===========================eeER..  r9 = r8 if r10 == 0
    .........D=========================eE--R..  r7 = r7 << 0x4
    .........D============================eER.  r9 = r9 + r11
    .........D=============================eER  r7 = r7 + r9
    .........DeeE----------------------------R  fallthrough
```

Gas simulation at offset 12468 with total cost of 27:

```
    DeER..........................  r7 = r7 + 0x8
    D=eER.........................  r7 = r7 >> 0x8
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 540] = a0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE--R  r8 = u16 [r6 + 539]
    .D========================eE-R  r7 = r8 >> 0x8
    .DeE-------------------------R  r9 = 0x3f
    .D=========================eER  jump 12535 if r7 >=u r9
```

Gas simulation at offset 12491 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 304, jump [r10 + 0]
```

Gas simulation at offset 12523 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r8 = u8 [r6 + 565]
    D=========================eER....................  r8 = r8 & 0x40
    D==========================eeeeeeeeeeeeeeeeeeeeER  jump 12560 if r8 != 0
```

Gas simulation at offset 12533 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 12607
```

Gas simulation at offset 12535 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r8 = r8 & 0x1f
    D=eE--------------------------------------R  r8 = r8 + r5
    .D=eE-------------------------------------R  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  r8 = u8 [r6 + 565]
    ..D========================eE-------------R  r8 = r8 & 0x40
    ..D=========================eE------------R  jump 12607 if r8 == 0
```

Gas simulation at offset 12560 with total cost of 11:

```
    DeER..........  r8 = r7 & 0xff
    DeER..........  r9 = r7 << 0xb
    .DeER.........  r10 = r8 << 0x1
    .D=eER........  r9 = r9 | r10
    .DeE-R........  r10 = 0x22110
    ..DeER........  r7 = r7 << 0xf
    ..DeER........  r8 = r8 << 0x5
    ..D=eER.......  r7 = r7 | r8
    ..D=eER.......  r9 = r9 & r10
    ...D=eER......  r7 = r7 & 0x88440
    ...D==eER.....  r7 = r7 | r9
    ...D===eeeER..  r7 = r7 * 0x10101
    ....D=====eeER  i32 r7 = r7 >> 0x10
    ....DeeE-----R  fallthrough
```

Gas simulation at offset 12607 with total cost of 77:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.....................................  r8 = u8 [r6 + 566]
    D=========================eE--------------R.....................................  r8 = r8 << 0x2
    D==========================eE-------------R.....................................  r8 = r8 + r5
    .D==========================eE------------R.....................................  r8 = r8 + 0x7ff
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u8 [r8 + 482] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R........................  r7 = u8 [r6 + 566]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R........................  r8 = i16 [r6 + 529]
    ..D========================eE--------------------------R........................  r7 = r7 + 0x1
    ..D========================eE--------------------------R........................  r8 = r8 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R........................  u16 [r6 + 529] = r8
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R........................  u8 [r6 + 566] = a0
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R........................  r0 = u64 [r1 + 16]
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  r5 = u64 [r1 + 8]
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ...D=================================================eE------------------------R  r1 = r1 + 0x18
    ....D========================eeeeeeeeeeeeeeeeeeeeeeE---------------------------R  jump [r0 + 0]
```

Gas simulation at offset 12661 with total cost of 78:

```
    DeER.............................................................................  r8 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r9 = u16 [r8 + 521]
    DeE-------------------------R....................................................  r10 = 0x2000
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r11 = i16 [r8 + 529]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r12 = u8 [r8 + 561]
    .D=========================eER...................................................  r9 = r9 << 0x34
    .D==========================eER..................................................  r9 = r9 >> 0x34
    ..D==========================eER.................................................  r9 = r9 | r10
    ..D========================eE--R.................................................  r7 = r7 + r12
    ..D========================eE--R.................................................  r12 = r12 + 0x1
    ..D========================eE--R.................................................  r11 = r11 + 0x1
    ...D========================eE-R.................................................  r7 = r7 + 0x7ff
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u8 [r7 + 449]
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.........................  u16 [r8 + 529] = r11
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r8 + 539] = r9
    ....D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE--R........................  u8 [r8 + 561] = a5
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 562] = a0
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 564] = a0
    ....DeeeeeeeeeeeeeeeeeeeeeeE----------------------------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 12729 with total cost of 79:

```
    DeER..............................................................................  r7 = r7 + 0x7ff
    DeER..............................................................................  r2 = 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r3 = u16 [r7 + 521]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r4 = i16 [r7 + 529]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r11 = i16 [r7 + 531]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r12 = i16 [r7 + 533]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = i16 [r7 + 535]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r9 = i16 [r7 + 537]
    ..D========================eE------------------------R............................  r3 = r3 << 0x34
    ..D=========================eE-----------------------R............................  r10 = r3 >> 0x34
    ..D==========================eE----------------------R............................  r10 = r10 | r2
    ...D================================================eER...........................  r9 = r9 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u16 [r7 + 537] = r9
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------R..  u16 [r7 + 539] = r10
    ...D=======================eE--------------------------------------------------R..  r11 = r11 << 0x1
    ....D=======================eE-------------------------------------------------R..  r12 = r12 << 0x1
    ....D===============================================eE-------------------------R..  r8 = r8 << 0x1
    ....D========================eE------------------------------------------------R..  r4 = r4 + 0x1
    ....D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------R..  u16 [r7 + 529] = r4
    .....D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u16 [r7 + 531] = r11
    .....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 533] = r12
    .....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 535] = r8
    .....DeeeeeeeeeeeeeeeeeeeeeeE----------------------------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 12811 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 12868 if r9 >=u 63
```

Gas simulation at offset 12834 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 312, jump [r10 + 0]
```

Gas simulation at offset 12866 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 12883
```

Gas simulation at offset 12868 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 12883 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r5 + 537]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r5 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r5 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r11 = i16 [r5 + 533]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r12 = i16 [r5 + 535]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................  u16 [r5 + 537] = r8
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.................................................  u8 [r5 + 554] = a0
    ..D=======================eE-------------------------R.................................................  r10 = r10 << 0x1
    ..D========================eE------------------------R.................................................  r11 = r11 << 0x1
    ..D================================================eER.................................................  r12 = r12 << 0x1
    ..D=========================eE-----------------------R.................................................  r9 = r9 + 0x1
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u16 [r5 + 529] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r5 + 531] = r10
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r5 + 533] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r5 + 535] = r12
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x10
    ....D==========================================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 12952 with total cost of 48:

```
    DeER...............................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r2 = u16 [r7 + 529]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r9 = u16 [r7 + 521]
    .D=========================eER.....................  r10 = r2 + 0xfffffffffffffeff
    .D=========================eER.....................  r12 = r9 >> 0x4
    ..D=========================eER....................  r8 = zext16 r10
    ..DeE-------------------------R....................  r3 = 0x40
    ..D=========================eER....................  r10 = r12 & 0x38
    ...D=========================eeeeeeeeeeeeeeeeeeeeER  jump 12995 if r8 >=u r3
```

Gas simulation at offset 12982 with total cost of 16:

```
    DeER...............  r8 = r9 & 0xcff
    D=eER..............  r8 = r8 | 0x2000
    .D=eER.............  r9 = r10 + r8
    .DeeeeeeeeeeeeeeeER  jump 13016
```

Gas simulation at offset 12995 with total cost of 4:

```
    DeER...  r11 = r9 & 0xc00
    DeER...  r9 = r9 << 0x3b
    D=eER..  r9 = r9 >> 0x3d
    .D=eER.  r9 = r9 | r11
    .DeE-R.  r8 = r10 | 0x23c0
    .D==eER  r9 = r9 | r8
    ..DeeER  fallthrough
```

Gas simulation at offset 13016 with total cost of 76:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r8 = i16 [r7 + 537]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r10 = i16 [r7 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r11 = i16 [r7 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r12 = i16 [r7 + 535]
    .D========================eER..................................................  r8 = r8 << 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r7 + 537] = r8
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.........................  u16 [r7 + 539] = r9
    .D========================eE-------------------------R.........................  r2 = r2 + 0x1
    ..D=======================eE-------------------------R.........................  r10 = r10 << 0x1
    ..D========================eE------------------------R.........................  r11 = r11 << 0x1
    ..D========================eE------------------------R.........................  r12 = r12 << 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r7 + 529] = r2
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r7 + 531] = r10
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r7 + 533] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 535] = r12
    ...DeeeeeeeeeeeeeeeeeeeeeeE---------------------------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 13073 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 13130 if r9 >=u 63
```

Gas simulation at offset 13096 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 318, jump [r10 + 0]
```

Gas simulation at offset 13128 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 13145
```

Gas simulation at offset 13130 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 13145 with total cost of 123:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................................................................  r10 = u8 [r5 + 521]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................................................................  r2 = i16 [r5 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................................................................  r3 = i16 [r5 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................................................................  r11 = i16 [r5 + 533]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r12 = i16 [r5 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r9 = i16 [r5 + 537]
    .D========================eE------------------------R.........................................................................  r8 = r10 & 0x2
    ..D=======================eE------------------------R.........................................................................  r10 = r10 >> 0x4
    ..D========================eE-----------------------R.........................................................................  r10 = r10 & 0x4
    ..D=========================eE----------------------R.........................................................................  r8 = r8 | r10
    ..D========================eE-----------------------R.........................................................................  r7 = r7 & 0xff
    ...D=========================eE---------------------R.........................................................................  r7 = r7 >> r8
    ...D===============================================eER........................................................................  r9 = r9 << 0x1
    ...D==========================eE---------------------R........................................................................  r7 = r7 & 0x3
    ....D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u16 [r5 + 537] = r9
    ....D==========================eeeeeeeeeeeeeeeeeeeeeeeeeE---------------------R...............................................  u8 [r5 + 555] = a0
    ....D=======================eE------------------------------------------------R...............................................  r3 = r3 << 0x1
    ....D========================eE-----------------------------------------------R...............................................  r11 = r11 << 0x1
    .....D=============================================eE-------------------------R...............................................  r12 = r12 << 0x1
    .....D========================eE----------------------------------------------R...............................................  r2 = r2 + 0x1
    .....D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE---------------------R...............................................  u16 [r5 + 529] = r2
    .....D==============================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u16 [r5 + 531] = r3
    ......D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................  u16 [r5 + 533] = r11
    ......D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................  u16 [r5 + 535] = r12
    ......D======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 8]
    ......D======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 0]
    .......D=========================================================================eE--------------------R......................  r1 = r1 + 0x10
    .......D==============================================================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 13240 with total cost of 104:

```
    DeER.......................................................................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................  r8 = u8 [r7 + 550]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................  r9 = u8 [r7 + 554]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................  r2 = i16 [r7 + 535]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................  r3 = i16 [r7 + 537]
    .D=========================eER.............................................................................  r8 = r8 & 0x10
    .D=========================eER.............................................................................  r9 = r9 << 0x4
    .D==========================eER............................................................................  r8 = r8 << 0x8
    ..D==========================eER...........................................................................  r8 = r8 | r9
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r9 = i16 [r7 + 521]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r12 = i16 [r7 + 529]
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r10 = i16 [r7 + 531]
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r11 = i16 [r7 + 533]
    ...D================================================eE--R..................................................  r9 = r9 << 0x31
    ...D=================================================eE-R..................................................  r9 = r9 >> 0x3d
    ...D==================================================eER..................................................  r8 = r8 | r9
    ....D===============================================eE--R..................................................  r3 = r3 << 0x1
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u16 [r7 + 537] = r3
    ....D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r7 + 539] = r8
    ....D================================================eE--------------------------R.........................  r10 = r10 << 0x1
    .....D=================================================eE------------------------R.........................  r11 = r11 << 0x1
    .....D================================================eE-------------------------R.........................  r2 = r2 << 0x1
    .....D=================================================eE------------------------R.........................  r12 = r12 + 0x1
    .....D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r7 + 529] = r12
    ......D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r7 + 531] = r10
    ......D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u16 [r7 + 533] = r11
    ......D=========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 535] = r2
    ......DeeeeeeeeeeeeeeeeeeeeeeE----------------------------------------------------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 13338 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 13395 if r9 >=u 63
```

Gas simulation at offset 13361 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 324, jump [r10 + 0]
```

Gas simulation at offset 13393 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 13410
```

Gas simulation at offset 13395 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 13410 with total cost of 100:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r5 + 537]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r9 = i16 [r5 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r10 = i16 [r5 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r11 = i16 [r5 + 533]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r12 = i16 [r5 + 535]
    .D========================eE------------------------R..................................................  r8 = r8 << 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................  u16 [r5 + 537] = r8
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.................................................  u8 [r5 + 556] = a0
    ..D=======================eE-------------------------R.................................................  r10 = r10 << 0x1
    ..D========================eE------------------------R.................................................  r11 = r11 << 0x1
    ..D================================================eER.................................................  r12 = r12 << 0x1
    ..D=========================eE-----------------------R.................................................  r9 = r9 + 0x1
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u16 [r5 + 529] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r5 + 531] = r10
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r5 + 533] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r5 + 535] = r12
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 8]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 0]
    ....D========================================================================eE-----------------------R  r1 = r1 + 0x10
    ....D==========================================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 13479 with total cost of 104:

```
    DeER.......................................................................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................  r2 = i16 [r7 + 535]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................  r4 = i16 [r7 + 537]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................  r10 = u8 [r7 + 550]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................  r11 = u8 [r7 + 554]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r12 = u16 [r7 + 521]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r3 = i16 [r7 + 529]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r8 = i16 [r7 + 531]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r9 = i16 [r7 + 533]
    ..D=================================================eER....................................................  r11 = r11 << 0x4
    ..D=================================================eER....................................................  r12 = r12 >> 0xc
    ..D==================================================eER...................................................  r11 = r11 | r12
    ...D================================================eE-R...................................................  r10 = r10 & 0x10
    ...D=================================================eER...................................................  r10 = r10 << 0x8
    ...D==================================================eER..................................................  r10 = r10 | r11
    ...D================================================eE--R..................................................  r4 = r4 << 0x1
    ....D==================================================eER.................................................  r10 = r10 | 0x8
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u16 [r7 + 537] = r4
    ....D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r7 + 539] = r10
    ....D================================================eE---------------------------R........................  r8 = r8 << 0x1
    .....D================================================eE--------------------------R........................  r9 = r9 << 0x1
    .....D================================================eE--------------------------R........................  r2 = r2 << 0x1
    .....D=================================================eE-------------------------R........................  r3 = r3 + 0x1
    .....D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r7 + 529] = r3
    ......D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R........................  u16 [r7 + 531] = r8
    ......D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u16 [r7 + 533] = r9
    ......D=========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 535] = r2
    ......DeeeeeeeeeeeeeeeeeeeeeeE----------------------------------------------------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 13577 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 13648 if r9 >=u 63
```

Gas simulation at offset 13600 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 330, jump [r10 + 0]
```

Gas simulation at offset 13632 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r5 + 551]
    D=========================eER.  r8 = r8 & 0x18
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.  u8 [r5 + 557] = a0
    D==========================eER  jump 13677 if r8 != 0
```

Gas simulation at offset 13646 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 13713
```

Gas simulation at offset 13648 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeE---------------------------------------R.............  r8 = r8 & 0x1f
    D=eE--------------------------------------R.............  r7 = r7 + r8
    D==eE-------------------------------------R.............  r7 = r7 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R.............  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.............  r8 = u8 [r5 + 551]
    .D=========================eE-------------R.............  r8 = r8 & 0x18
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = a0
    ..D=========================eE-------------------------R  jump 13713 if r8 == 0
```

Gas simulation at offset 13677 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......  r8 = u16 [r5 + 521]
    D=========================eE--------------R......  r9 = r8 & 0x1f
    .D========================eE--------------R......  r8 = r8 & 0xffffffffffffffe0
    .D=========================eeeeeeeeeeeeeeeeeeeeER  jump 13702 if r9 != 31
```

Gas simulation at offset 13692 with total cost of 26:

```
    DeER.........................  r8 = r8 ^ 0x400
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r8
    DeeeeeeeeeeeeeeeE-----------R  jump 13713
```

Gas simulation at offset 13702 with total cost of 27:

```
    DeER..........................  r8 = r8 | r9
    D=eER.........................  r8 = r8 + 0x1
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r8
    DeeE-------------------------R  fallthrough
```

Gas simulation at offset 13713 with total cost of 124:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R....................................................................................  r2 = i16 [r5 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R....................................................................................  r9 = u16 [r5 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R....................................................................................  r3 = u16 [r5 + 537]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R....................................................................................  r11 = u8 [r5 + 555]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................  r12 = u8 [r5 + 556]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................  r8 = u16 [r5 + 533]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................  r10 = u16 [r5 + 535]
    ..D========================eE-----------------------R..........................................................................  r9 = r9 & 0xffffffffffffff00
    ..D================================================eER.........................................................................  r9 = r9 | r12
    ..D=========================eE-----------------------R.........................................................................  r7 = r7 & 0xff
    ..D================================================eER.........................................................................  r8 = r8 & 0xffffffffffffff00
    ...D===============================================eER.........................................................................  r10 = r10 & 0xffffffffffffff00
    ...D================================================eER........................................................................  r7 = r7 | r8
    ...D=========================eE-----------------------R........................................................................  r8 = r11 << 0x3f
    ....D=========================eE----------------------R........................................................................  r8 = r8 >>a 0x3f
    ....D==========================eE---------------------R........................................................................  r8 = r8 & 0xff
    ....D===============================================eER........................................................................  r8 = r8 | r10
    .....D==========================eE--------------------R........................................................................  r10 = r3 & 0xffffffffffffff00
    .....D===========================eE-------------------R........................................................................  r11 = r11 << 0x6
    .....D============================eE------------------R........................................................................  r11 = sext8 r11
    ......D============================eE-----------------R........................................................................  r11 = r11 << 0x31
    ......D=============================eE----------------R........................................................................  r11 = r11 >> 0x38
    ......D==============================eE---------------R........................................................................  r10 = r10 | r11
    ......D===============================eE--------------R........................................................................  r2 = r2 + 0x1
    .......D============================================eER........................................................................  r9 = r9 << 0x1
    .......D=============================================eER.......................................................................  r7 = r7 << 0x1
    .......D=============================================eER.......................................................................  r8 = r8 << 0x1
    .......D===============================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................  u16 [r5 + 529] = r2
    ........D============================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u16 [r5 + 531] = r9
    ........D=============================================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u16 [r5 + 533] = r7
    ........D=============================================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u16 [r5 + 535] = r8
    ...........................................D====================eE--------------R..............................................  r10 = r10 << 0x1
    ...........................................D=====================eeeeeeeeeeeeeeeeeeeeeeeeeER...................................  u16 [r5 + 537] = r10
    ...........................................D==================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 8]
    ...........................................D===================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r5 = u64 [r1 + 0]
    ............................................D==================================eE------------------------R.....................  r1 = r1 + 0x10
    .....................................................D=================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 13840 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 13911 if r9 >=u 63
```

Gas simulation at offset 13863 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 334, jump [r10 + 0]
```

Gas simulation at offset 13895 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r5 + 551]
    D=========================eER.  r8 = r8 & 0x18
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.  u8 [r5 + 557] = a0
    D==========================eER  jump 13940 if r8 != 0
```

Gas simulation at offset 13909 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 13976
```

Gas simulation at offset 13911 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeE---------------------------------------R.............  r8 = r8 & 0x1f
    D=eE--------------------------------------R.............  r7 = r7 + r8
    D==eE-------------------------------------R.............  r7 = r7 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R.............  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.............  r8 = u8 [r5 + 551]
    .D=========================eE-------------R.............  r8 = r8 & 0x18
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = a0
    ..D=========================eE-------------------------R  jump 13976 if r8 == 0
```

Gas simulation at offset 13940 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......  r8 = u16 [r5 + 521]
    D=========================eE--------------R......  r9 = r8 & 0x1f
    .D========================eE--------------R......  r8 = r8 & 0xffffffffffffffe0
    .D=========================eeeeeeeeeeeeeeeeeeeeER  jump 13965 if r9 != 31
```

Gas simulation at offset 13955 with total cost of 26:

```
    DeER.........................  r8 = r8 ^ 0x400
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r8
    DeeeeeeeeeeeeeeeE-----------R  jump 13976
```

Gas simulation at offset 13965 with total cost of 27:

```
    DeER..........................  r8 = r8 | r9
    D=eER.........................  r8 = r8 + 0x1
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r8
    DeeE-------------------------R  fallthrough
```

Gas simulation at offset 13976 with total cost of 98:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........................................................  r8 = u8 [r5 + 555]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........................................................  r9 = i16 [r5 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........................................................  r10 = u8 [r5 + 556]
    .D========================eE--------------R..........................................................  r11 = r8 << 0x3f
    .D========================eE--------------R..........................................................  r8 = r8 << 0x6
    .D========================eE--------------R..........................................................  r9 = r9 + 0x1
    ..D========================eE-------------R..........................................................  r11 = r11 >>a 0x3f
    ..D========================eE-------------R..........................................................  r8 = sext8 r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u16 [r5 + 529] = r9
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u8 [r5 + 531] = a3
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R..............................................  u8 [r5 + 533] = a0
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u8 [r5 + 535] = a4
    ...D=========================eE-----------------------R..............................................  r8 = r8 >> 0x7
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER............................................  u8 [r5 + 537] = a1
    ....D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 8]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r5 = u64 [r1 + 0]
    ....D================================================eE------------------------R.....................  r1 = r1 + 0x10
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 14036 with total cost of 54:

```
    DeER.....................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u16 [r7 + 521]
    DeE-------------------------R............................  r9 = 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r10 = i16 [r7 + 529]
    .D=========================eER...........................  r8 = r8 << 0x34
    .D==========================eER..........................  r8 = r8 >> 0x34
    .D===========================eER.........................  r8 = r8 | r9
    .D=========================eE--R.........................  r10 = r10 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u16 [r7 + 529] = r10
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 539] = r8
    ..DeeeeeeeeeeeeeeeeeeeeeeE------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 14074 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..DeE-------------------------R.  r10 = 0x3f
    ..D==========================eER  jump 14133 if r9 >=u r10
```

Gas simulation at offset 14099 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 340, jump [r10 + 0]
```

Gas simulation at offset 14131 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 14148
```

Gas simulation at offset 14133 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 14148 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = i16 [r5 + 529]
    D=========================eER.........................  r8 = r8 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 529] = r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u8 [r5 + 554] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r0 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r5 = u64 [r1 + 0]
    .D========================eE-------------------------R  r1 = r1 + 0x10
    .D=========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 14173 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..DeE-------------------------R.  r10 = 0x3f
    ..D==========================eER  jump 14232 if r9 >=u r10
```

Gas simulation at offset 14198 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 344, jump [r10 + 0]
```

Gas simulation at offset 14230 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 14247
```

Gas simulation at offset 14232 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 14247 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = i16 [r5 + 527]
    D=========================eER.........................  r8 = r8 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 527] = r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u16 [r5 + 529] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u8 [r5 + 554] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r0 = u64 [r1 + 8]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  r5 = u64 [r1 + 0]
    .D=========================eE------------------------R  r1 = r1 + 0x10
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 14276 with total cost of 76:

```
    DeER...........................................................................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r1 + 0] = r5
    .DeE------------------------R..................................................  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................  r9 = u8 [r5 + 551]
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................  r10 = u8 [r5 + 575]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r5 + 560] = 0
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r5 + 567] = 0
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u8 [r5 + 573] = 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u8 [r5 + 574] = a3
    ...D================================================eER........................  r9 = r9 & 0x10
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 575] = 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeE----R  jump 14338 if r9 == 0
```

Gas simulation at offset 14323 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 548] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 566] = 0
    DeE------------------------R  r0 = 0x15c
    DeeeeeeeeeeeeeeeE----------R  jump 6010
```

Gas simulation at offset 14338 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 566] = 0
    DeeeeeeeeeeeeeeeE----------R  r0 = 348, jump 6010
```

Gas simulation at offset 14348 with total cost of 98:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r7 = i16 [r5 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r8 = i16 [r5 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r9 = i16 [r5 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r10 = i16 [r5 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  r11 = i16 [r5 + 537]
    .D========================eE------------------------R................................................  r8 = r8 << 0x1
    .D========================eE------------------------R................................................  r9 = r9 << 0x1
    .D========================eE------------------------R................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u16 [r5 + 529] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R..............................................  u16 [r5 + 531] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R..............................................  u16 [r5 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r5 + 535] = r10
    ...D================================================eE-----------------------R.......................  r11 = r11 << 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  u16 [r5 + 537] = r11
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................  r0 = u64 [r1 + 8]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r5 = u64 [r1 + 0]
    ....D=======================================================================eE-R.....................  r1 = r1 + 0x10
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 14413 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r6
    .D...........................  r5 = r7
    .DeE------------------------R  r6 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeE----------R  r0 = 352, jump 6819
```

Gas simulation at offset 14436 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r7 = u8 [r6 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r8 = u8 [r6 + 554]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................  r9 = u16 [r6 + 521]
    D=========================eER............................  r7 = r7 & 0x10
    .D========================eER............................  r8 = r8 << 0x4
    .D========================eER............................  r9 = r9 >> 0xc
    .D=========================eER...........................  r7 = r7 << 0x8
    .D=========================eER...........................  r8 = r8 | r9
    ..D=========================eER..........................  r7 = r7 | r8
    ..D==========================eER.........................  r7 = r7 | 0x8
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 539] = r7
    ..D......................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE------------------------------------R  r0 = 354, jump 7101
```

Gas simulation at offset 14481 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 356, jump 6010
```

Gas simulation at offset 14489 with total cost of 122:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................................  r7 = i16 [r6 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................................  r8 = i16 [r6 + 531]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................................  r9 = i16 [r6 + 533]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................................  r10 = i16 [r6 + 535]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................................  r11 = i16 [r6 + 537]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................................  r12 = i32 [r6 + 597]
    .D========================eE------------------------R........................................................................  r8 = r8 << 0x1
    .D========================eE------------------------R........................................................................  r9 = r9 << 0x1
    ..D========================eE-----------------------R........................................................................  r10 = r10 << 0x1
    ..D========================eE-----------------------R........................................................................  r7 = r7 + 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................  u16 [r6 + 529] = r7
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................  u16 [r6 + 531] = r8
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u16 [r6 + 533] = r9
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u16 [r6 + 535] = r10
    ...D=================================================eE----------------------R...............................................  r11 = r11 << 0x1
    ...D=================================================eE----------------------R...............................................  r12 = r12 + 0x1
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER............................................  u16 [r6 + 537] = r11
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER............................................  u32 [r6 + 597] = r12
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 16]
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 8]
    .....D=========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...................  r6 = u64 [r1 + 0]
    .....D=========================================================================eE------------------------R...................  r1 = r1 + 0x18
    .....D===============================================================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 14568 with total cost of 52:

```
    DeER...................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = i16 [r7 + 529]
    D==========================eER.........................  r8 = r8 + 0x1
    D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 529] = r8
    .DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 14585 with total cost of 52:

```
    DeER...................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = i16 [r7 + 527]
    D==========================eER.........................  r8 = r8 + 0x1
    D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 527] = r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u16 [r7 + 529] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u8 [r7 + 569] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 14610 with total cost of 27:

```
    DeER..........................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u8 [r7 + 569]
    D==========================eER  jump 14635 if r8 != 0
```

Gas simulation at offset 14621 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = u8 [r7 + 552]
    D=========================eE--------------R...........  r8 = r8 | 0x80
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 552] = a1
    .DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 14635 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = i16 [r7 + 529]
    D=========================eE--------------R...........  r8 = r8 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 529] = r8
    .DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 14649 with total cost of 54:

```
    DeER.....................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u8 [r7 + 550]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r9 = u8 [r7 + 552]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r10 = i16 [r7 + 529]
    .D=========================eER...........................  r8 = r8 & r9
    .D=========================eER...........................  r10 = r10 + 0x1
    .D==========================eER..........................  r8 = r8 << 0x38
    .D===========================eER.........................  r8 = r8 >> 0x3f
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u16 [r7 + 529] = r10
    ..DeeeeeeeeeeeeeeeeeeeeeeE------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 14687 with total cost of 54:

```
    DeER.....................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u8 [r7 + 550]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r9 = u8 [r7 + 552]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r10 = i16 [r7 + 527]
    .D=========================eER...........................  r8 = r8 & r9
    .D=========================eER...........................  r10 = r10 + 0x1
    .D==========================eER..........................  r8 = r8 << 0x38
    .D===========================eER.........................  r8 = r8 >> 0x3f
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u16 [r7 + 527] = r10
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R  u16 [r7 + 529] = 0
    ..DeeeeeeeeeeeeeeeeeeeeeeE------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 14729 with total cost of 54:

```
    DeER.....................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u8 [r7 + 550]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r9 = u8 [r7 + 552]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r10 = u8 [r7 + 568]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r11 = i16 [r7 + 527]
    .D=========================eER...........................  r8 = r8 & r9
    .D=========================eER...........................  r9 = r10 ^ 0x1
    ..D========================eER...........................  r11 = r11 + 0x1
    ..D=========================eER..........................  r8 = r8 << 0x38
    ..D==========================eER.........................  r8 = r8 >> 0x3f
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u16 [r7 + 527] = r11
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE-R..  u16 [r7 + 529] = 0
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u8 [r7 + 568] = a2
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a1
    ...DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 14782 with total cost of 102:

```
    DeER.....................................................................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................................................................  r2 = i16 [r7 + 537]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................................................................  r3 = u8 [r7 + 550]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................................................................  r10 = u8 [r7 + 552]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER............................................................................  r11 = i16 [r7 + 529]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r12 = i16 [r7 + 531]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r8 = i16 [r7 + 533]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r9 = i16 [r7 + 535]
    ..D========================eE------------------------R...................................................  r10 = r3 & r10
    ..D=================================================eER..................................................  r12 = r12 << 0x1
    ..D=================================================eER..................................................  r8 = r8 << 0x1
    ..D=================================================eER..................................................  r9 = r9 << 0x1
    ...D========================eE------------------------R..................................................  r11 = r11 + 0x1
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................  u16 [r7 + 529] = r11
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r7 + 531] = r12
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r7 + 533] = r8
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r7 + 535] = r9
    ....D=================================================eE-----------------------R.........................  r2 = r2 << 0x1
    ....D==================================================eE----------------------R.........................  r10 = r10 << 0x38
    ....D===================================================eE---------------------R.........................  r10 = r10 >> 0x3f
    .....D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  u16 [r7 + 537] = r2
    .....D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 552] = 0
    .....D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 566] = 0
    .....D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a3
    ......DeeeeeeeeeeeeeeeeeeeeeeE--------------------------------------------------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 14872 with total cost of 105:

```
    DeER........................................................................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................  r2 = u16 [r7 + 521]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................  r9 = i16 [r7 + 529]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................  r10 = i16 [r7 + 531]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................  r11 = i16 [r7 + 533]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................  r12 = i16 [r7 + 535]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................  r3 = i16 [r7 + 537]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................  r4 = u8 [r7 + 550]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................  r8 = u8 [r7 + 552]
    ..D=================================================eER.....................................................  r10 = r10 << 0x1
    ..D=================================================eER.....................................................  r11 = r11 << 0x1
    ..D=================================================eER.....................................................  r12 = r12 << 0x1
    ...D================================================eER.....................................................  r9 = r9 + 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER............................  u16 [r7 + 529] = r9
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER............................  u16 [r7 + 531] = r10
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER............................  u16 [r7 + 533] = r11
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER............................  u16 [r7 + 535] = r12
    ....D=========================================================================eER...........................  r2 = r2 << 0x34
    ....D==========================================================================eER..........................  r10 = r2 >> 0x34
    .....D==========================================================================eER.........................  r9 = r10 | 0x2000
    .....D========================================================================eE--R.........................  r10 = r4 & r8
    ......D=======================================================================eE--R.........................  r8 = r8 & 0xbf
    ......D=======================================================================eE--R.........................  r3 = r3 << 0x1
    ......D========================================================================eE-R.........................  r10 = r10 >> 0x7
    ......D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u16 [r7 + 537] = r3
    .......D=========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 539] = r9
    .......D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u8 [r7 + 552] = a1
    .......D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  u8 [r7 + 625] = a3
    .......DeeeeeeeeeeeeeeeeeeeeeeE----------------------------------------------------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 14977 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 15034 if r9 >=u 63
```

Gas simulation at offset 15000 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 376, jump [r10 + 0]
```

Gas simulation at offset 15032 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 15049
```

Gas simulation at offset 15034 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 15049 with total cost of 124:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................................................................  r8 = u8 [r5 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................................................................  r9 = u8 [r5 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................................................................  r10 = i16 [r5 + 537]
    .D========================eER..................................................................................................  r2 = r8 & r9
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................................................................  r9 = i16 [r5 + 529]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................  r11 = i16 [r5 + 531]
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................  r12 = i16 [r5 + 533]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r8 = i16 [r5 + 535]
    ..D========================eE------------------------R.........................................................................  r10 = r10 << 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................................  u16 [r5 + 537] = r10
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................  u8 [r5 + 554] = a0
    ...D===============================================eE------------------------R.................................................  r11 = r11 << 0x1
    ...D================================================eE-----------------------R.................................................  r12 = r12 << 0x1
    ...D================================================eE-----------------------R.................................................  r8 = r8 << 0x1
    ....D================================================eE----------------------R.................................................  r9 = r9 + 0x1
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u16 [r5 + 529] = r9
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R..............................................  u16 [r5 + 531] = r11
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R..............................................  u16 [r5 + 533] = r12
    .....D======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r5 + 535] = r8
    .....D========================================================================eE----------------------R........................  r2 = r2 << 0x38
    .....D=========================================================================eE---------------------R........................  r7 = r2 >> 0x3f
    ......D=========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................  u8 [r5 + 625] = a0
    ......D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE--R....................  r0 = u64 [r1 + 8]
    ......D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R....................  r5 = u64 [r1 + 0]
    ......D==============================================================================================eE---R....................  r1 = r1 + 0x10
    .......D===============================================================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 15139 with total cost of 48:

```
    DeER...............................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r2 = u16 [r7 + 529]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r9 = u16 [r7 + 521]
    .D=========================eER.....................  r10 = r2 + 0xfffffffffffffeff
    .D=========================eER.....................  r12 = r9 >> 0x4
    ..D=========================eER....................  r8 = zext16 r10
    ..D=========================eER....................  r10 = r12 & 0x38
    ..D==========================eeeeeeeeeeeeeeeeeeeeER  jump 15180 if r8 >=u 64
```

Gas simulation at offset 15167 with total cost of 16:

```
    DeER...............  r8 = r9 & 0xcff
    D=eER..............  r8 = r8 | 0x2000
    .D=eER.............  r3 = r10 + r8
    .DeeeeeeeeeeeeeeeER  jump 15201
```

Gas simulation at offset 15180 with total cost of 4:

```
    DeER...  r11 = r9 & 0xc00
    DeER...  r9 = r9 << 0x3b
    D=eER..  r9 = r9 >> 0x3d
    .D=eER.  r9 = r9 | r11
    .DeE-R.  r8 = r10 | 0x23c0
    ..D=eER  r3 = r9 | r8
    ..DeeER  fallthrough
```

Gas simulation at offset 15201 with total cost of 103:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................  r8 = i16 [r7 + 537]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................  r10 = u8 [r7 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................  r11 = u8 [r7 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................  r12 = i16 [r7 + 531]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r9 = i16 [r7 + 533]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r4 = i16 [r7 + 535]
    .D========================eE------------------------R.....................................................  r10 = r10 & r11
    .D========================eE------------------------R.....................................................  r8 = r8 << 0x1
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  u16 [r7 + 537] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  u16 [r7 + 539] = r3
    ..D================================================eER....................................................  r2 = r2 + 0x1
    ..D================================================eER....................................................  r12 = r12 << 0x1
    ...D================================================eER...................................................  r9 = r9 << 0x1
    ...D================================================eER...................................................  r4 = r4 << 0x1
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u16 [r7 + 529] = r2
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u16 [r7 + 531] = r12
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u16 [r7 + 533] = r9
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u16 [r7 + 535] = r4
    ....D========================================================================eER..........................  r10 = r10 << 0x38
    ....D=========================================================================eER.........................  r10 = r10 >> 0x3f
    .....D=========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a3
    .....DeeeeeeeeeeeeeeeeeeeeeeE----------------------------------------------------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 15279 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 15336 if r9 >=u 63
```

Gas simulation at offset 15302 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 382, jump [r10 + 0]
```

Gas simulation at offset 15334 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 15351
```

Gas simulation at offset 15336 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 15351 with total cost of 127:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................  r3 = i16 [r5 + 535]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................  r2 = i16 [r5 + 537]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................  r4 = u8 [r5 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................  r11 = u8 [r5 + 552]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................  r12 = i16 [r5 + 531]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................  r8 = i16 [r5 + 533]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................  r9 = u8 [r5 + 521]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................  r10 = i16 [r5 + 529]
    ..D================================================eER............................................................................  r11 = r4 & r11
    ..D================================================eER............................................................................  r12 = r12 << 0x1
    ..D================================================eER............................................................................  r8 = r8 << 0x1
    ..D================================================eER............................................................................  r3 = r3 << 0x1
    ...D================================================eER...........................................................................  r10 = r10 + 0x1
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u16 [r5 + 529] = r10
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R..................................................  u16 [r5 + 531] = r12
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R..................................................  u16 [r5 + 533] = r8
    ....D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R..................................................  u16 [r5 + 535] = r3
    ....D========================================================================eER..................................................  r8 = r9 & 0x2
    ....D========================================================================eER..................................................  r9 = r9 >> 0x4
    .....D========================================================================eER.................................................  r9 = r9 & 0x4
    .....D=========================================================================eER................................................  r8 = r8 | r9
    .....D=======================================================================eE--R................................................  r7 = r7 & 0xff
    ......D=========================================================================eER...............................................  r7 = r7 >> r8
    ......D=======================================================================eE--R...............................................  r2 = r2 << 0x1
    ......D=======================================================================eE--R...............................................  r11 = r11 << 0x38
    .......D=======================================================================eE-R...............................................  r11 = r11 >> 0x3f
    .......D=========================================================================eER..............................................  r7 = r7 & 0x3
    .......D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r5 + 537] = r2
    .......D==========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  u8 [r5 + 555] = a0
    ........D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE--R.....................  u8 [r5 + 625] = a4
    ........D=====================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE----R.....................  r0 = u64 [r1 + 8]
    ........D==============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 0]
    ............................D===========================================================================eE-----------------------R  r1 = r1 + 0x10
    ............................D==========================================================================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 15467 with total cost of 126:

```
    DeER.............................................................................................................................  r1 = r1 + 0xfffffffffffffff8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u64 [r1 + 0] = r5
    DeE-------------------------R....................................................................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  r3 = u8 [r7 + 554]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  r2 = i16 [r7 + 521]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  r10 = i16 [r7 + 529]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r11 = i16 [r7 + 531]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r12 = i16 [r7 + 533]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r8 = i16 [r7 + 535]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  r4 = i16 [r7 + 537]
    ..D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r9 = u8 [r7 + 550]
    ..D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r5 = u8 [r7 + 552]
    ...D================================================eE------------------------R..................................................  r11 = r11 << 0x1
    ...D================================================eE------------------------R..................................................  r12 = r12 << 0x1
    ...D=================================================eE-----------------------R..................................................  r8 = r8 << 0x1
    ...D=================================================eE-----------------------R..................................................  r10 = r10 + 0x1
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r7 + 529] = r10
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r7 + 531] = r11
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r7 + 533] = r12
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r7 + 535] = r8
    .....D=========================================================================eE----------------------R.........................  r5 = r5 & r9
    .....D=========================================================================eE----------------------R.........................  r9 = r9 & 0x10
    .....D==========================================================================eE---------------------R.........................  r3 = r3 << 0x4
    .....D==========================================================================eE---------------------R.........................  r9 = r9 << 0x8
    ......D==========================================================================eE--------------------R.........................  r8 = r9 | r3
    ......D==========================================================================eE--------------------R.........................  r2 = r2 << 0x31
    ......D===========================================================================eE-------------------R.........................  r4 = r4 << 0x1
    .......D==========================================================================eE-------------------R.........................  r9 = r2 >> 0x3d
    .......D===========================================================================eE------------------R.........................  r5 = r5 >> 0x7
    .......D===========================================================================eE------------------R.........................  r8 = r8 | r9
    ........D===========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................  u16 [r7 + 537] = r4
    ........D===========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................  u16 [r7 + 539] = r8
    ........D=============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = s0
    .............................D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 0]
    .............................D===============================================================================eE-----------------R  r1 = r1 + 0x8
    .............................DeeeeeeeeeeeeeeeeeeeeeeE---------------------------------------------------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 15589 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 15646 if r9 >=u 63
```

Gas simulation at offset 15612 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 388, jump [r10 + 0]
```

Gas simulation at offset 15644 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 15661
```

Gas simulation at offset 15646 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 15661 with total cost of 124:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................................................................  r8 = u8 [r5 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................................................................  r9 = u8 [r5 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................................................................  r10 = i16 [r5 + 537]
    .D========================eER..................................................................................................  r2 = r8 & r9
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................................................................  r9 = i16 [r5 + 529]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................  r11 = i16 [r5 + 531]
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................  r12 = i16 [r5 + 533]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r8 = i16 [r5 + 535]
    ..D========================eE------------------------R.........................................................................  r10 = r10 << 0x1
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................................  u16 [r5 + 537] = r10
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................  u8 [r5 + 556] = a0
    ...D===============================================eE------------------------R.................................................  r11 = r11 << 0x1
    ...D================================================eE-----------------------R.................................................  r12 = r12 << 0x1
    ...D================================================eE-----------------------R.................................................  r8 = r8 << 0x1
    ....D================================================eE----------------------R.................................................  r9 = r9 + 0x1
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u16 [r5 + 529] = r9
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R..............................................  u16 [r5 + 531] = r11
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R..............................................  u16 [r5 + 533] = r12
    .....D======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r5 + 535] = r8
    .....D========================================================================eE----------------------R........................  r2 = r2 << 0x38
    .....D=========================================================================eE---------------------R........................  r7 = r2 >> 0x3f
    ......D=========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................  u8 [r5 + 625] = a0
    ......D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE--R....................  r0 = u64 [r1 + 8]
    ......D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R....................  r5 = u64 [r1 + 0]
    ......D==============================================================================================eE---R....................  r1 = r1 + 0x10
    .......D===============================================================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 15751 with total cost of 107:

```
    DeER..........................................................................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................  r8 = u8 [r7 + 554]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................  r9 = u16 [r7 + 521]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................  r4 = i16 [r7 + 529]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................  r11 = i16 [r7 + 531]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................  r12 = i16 [r7 + 533]
    .D=========================eE------------------------R........................................................  r8 = r8 << 0x4
    .D=========================eE------------------------R........................................................  r9 = r9 >> 0xc
    ..D=========================eE-----------------------R........................................................  r2 = r8 | r9
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................  r9 = i16 [r7 + 535]
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................................................  r3 = i16 [r7 + 537]
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................  r8 = u8 [r7 + 550]
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r10 = u8 [r7 + 552]
    ...D================================================eE------------------------R...............................  r11 = r11 << 0x1
    ...D=================================================eE-----------------------R...............................  r12 = r12 << 0x1
    ....D================================================eE-----------------------R...............................  r9 = r9 << 0x1
    ....D=================================================eE----------------------R...............................  r4 = r4 + 0x1
    ....D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER............................  u16 [r7 + 529] = r4
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R............................  u16 [r7 + 531] = r11
    .....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R............................  u16 [r7 + 533] = r12
    .....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......  u16 [r7 + 535] = r9
    .....D=========================================================================eE----------------------R......  r10 = r10 & r8
    .....D=========================================================================eE----------------------R......  r8 = r8 & 0x10
    ......D=========================================================================eE---------------------R......  r3 = r3 << 0x1
    ......D=========================================================================eE---------------------R......  r8 = r8 << 0x8
    ......D=========================================================================eE---------------------R......  r10 = r10 >> 0x7
    ......D==========================================================================eE--------------------R......  r8 = r8 | r2
    .......D==========================================================================eE-------------------R......  r8 = r8 | 0x8
    .......D=========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u16 [r7 + 537] = r3
    .......D===========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 539] = r8
    .......D=========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u8 [r7 + 625] = a3
    ........DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------------------------------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 15863 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 15934 if r9 >=u 63
```

Gas simulation at offset 15886 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 394, jump [r10 + 0]
```

Gas simulation at offset 15918 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r5 + 551]
    D=========================eER.  r8 = r8 & 0x18
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.  u8 [r5 + 557] = a0
    D==========================eER  jump 15963 if r8 != 0
```

Gas simulation at offset 15932 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 15999
```

Gas simulation at offset 15934 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeE---------------------------------------R.............  r8 = r8 & 0x1f
    D=eE--------------------------------------R.............  r7 = r7 + r8
    D==eE-------------------------------------R.............  r7 = r7 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R.............  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.............  r8 = u8 [r5 + 551]
    .D=========================eE-------------R.............  r8 = r8 & 0x18
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = a0
    ..D=========================eE-------------------------R  jump 15999 if r8 == 0
```

Gas simulation at offset 15963 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......  r8 = u16 [r5 + 521]
    D=========================eE--------------R......  r9 = r8 & 0x1f
    .D========================eE--------------R......  r8 = r8 & 0xffffffffffffffe0
    .D=========================eeeeeeeeeeeeeeeeeeeeER  jump 15988 if r9 != 31
```

Gas simulation at offset 15978 with total cost of 26:

```
    DeER.........................  r8 = r8 ^ 0x400
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r8
    DeeeeeeeeeeeeeeeE-----------R  jump 15999
```

Gas simulation at offset 15988 with total cost of 27:

```
    DeER..........................  r8 = r8 | r9
    D=eER.........................  r8 = r8 + 0x1
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r8
    DeeE-------------------------R  fallthrough
```

Gas simulation at offset 15999 with total cost of 130:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........................................................................................  r2 = u8 [r5 + 556]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........................................................................................  r3 = u16 [r5 + 537]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........................................................................................  r10 = u8 [r5 + 550]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R..........................................................................................  r11 = u8 [r5 + 552]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................................................  r12 = u8 [r5 + 555]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................................................  r4 = i16 [r5 + 529]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................................................  r9 = u16 [r5 + 531]
    ..D========================eE-----------------------R................................................................................  r10 = r10 & r11
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................  r11 = u16 [r5 + 533]
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................................................  r8 = u16 [r5 + 535]
    ..D================================================eE------------------------R.......................................................  r9 = r9 & 0xffffffffffffff00
    ...D================================================eE-----------------------R.......................................................  r9 = r9 | r2
    ...D===============================================eE------------------------R.......................................................  r7 = r7 & 0xff
    ...D=================================================eE----------------------R.......................................................  r11 = r11 & 0xffffffffffffff00
    ...D========================================================================eER......................................................  r8 = r8 & 0xffffffffffffff00
    ....D=================================================eE----------------------R......................................................  r7 = r7 | r11
    ....D===============================================eE------------------------R......................................................  r11 = r12 << 0x3f
    ....D================================================eE-----------------------R......................................................  r11 = r11 >>a 0x3f
    .....D================================================eE----------------------R......................................................  r11 = r11 & 0xff
    .....D=======================================================================eER.....................................................  r8 = r8 | r11
    .....D===============================================eE------------------------R.....................................................  r11 = r3 & 0xffffffffffffff00
    ......D===============================================eE-----------------------R.....................................................  r12 = r12 << 0x6
    ......D================================================eE----------------------R.....................................................  r12 = sext8 r12
    ......D=================================================eE---------------------R.....................................................  r12 = r12 << 0x31
    ......D==================================================eE--------------------R.....................................................  r12 = r12 >> 0x38
    .......D==================================================eE-------------------R.....................................................  r11 = r11 | r12
    .......D===============================================eE----------------------R.....................................................  r4 = r4 + 0x1
    .......D===============================================eE----------------------R.....................................................  r10 = r10 << 0x38
    .......D================================================eE---------------------R.....................................................  r9 = r9 << 0x1
    ........D===============================================eE---------------------R.....................................................  r7 = r7 << 0x1
    ........D================================================eE--------------------R.....................................................  r10 = r10 >> 0x3f
    ...........................................D==================================eER....................................................  r8 = r8 << 0x1
    ...........................................D=============eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................  u16 [r5 + 529] = r4
    ...........................................D==============eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u16 [r5 + 531] = r9
    ...........................................D===============eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u16 [r5 + 533] = r7
    ............................................D==================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u16 [r5 + 535] = r8
    .....................................................D============================eE---------------------R...........................  r11 = r11 << 0x1
    .....................................................D=============================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u16 [r5 + 537] = r11
    .....................................................D=============================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u8 [r5 + 625] = a3
    .....................................................D==============================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 8]
    .......................................................D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..  r5 = u64 [r1 + 0]
    ..............................................................................D=============================eE--------------------R..  r1 = r1 + 0x10
    ..............................................................................D==============================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 16147 with total cost of 105:

```
    DeER........................................................................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................  r3 = i16 [r7 + 535]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................  r2 = i16 [r7 + 537]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................  r10 = u8 [r7 + 550]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................  r11 = u8 [r7 + 552]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................  r12 = i16 [r7 + 531]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................  r8 = i16 [r7 + 533]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................  r4 = u16 [r7 + 521]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................  r9 = i16 [r7 + 529]
    ..D=================================================eER.....................................................  r10 = r10 & r11
    ..D=================================================eER.....................................................  r12 = r12 << 0x1
    ..D=================================================eER.....................................................  r8 = r8 << 0x1
    ...D================================================eER.....................................................  r3 = r3 << 0x1
    ...D=================================================eER....................................................  r9 = r9 + 0x1
    ...D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u16 [r7 + 529] = r9
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R...........................  u16 [r7 + 531] = r12
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R...........................  u16 [r7 + 533] = r8
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R...........................  u16 [r7 + 535] = r3
    ....D=========================================================================eER...........................  r4 = r4 << 0x34
    .....D=========================================================================eER..........................  r9 = r4 >> 0x34
    .....D==========================================================================eER.........................  r8 = r9 | 0x2000
    ......D=======================================================================eE--R.........................  r2 = r2 << 0x1
    ......D=======================================================================eE--R.........................  r10 = r10 << 0x38
    ......D========================================================================eE-R.........................  r10 = r10 >> 0x3f
    ......D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u16 [r7 + 537] = r2
    .......D=========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 539] = r8
    .......D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  u8 [r7 + 625] = a3
    .......DeeeeeeeeeeeeeeeeeeeeeeE----------------------------------------------------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 16247 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 16318 if r9 >=u 63
```

Gas simulation at offset 16270 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 400, jump [r10 + 0]
```

Gas simulation at offset 16302 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r5 + 551]
    D=========================eER.  r8 = r8 & 0x18
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.  u8 [r5 + 557] = a0
    D==========================eER  jump 16347 if r8 != 0
```

Gas simulation at offset 16316 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 16383
```

Gas simulation at offset 16318 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeE---------------------------------------R.............  r8 = r8 & 0x1f
    D=eE--------------------------------------R.............  r7 = r7 + r8
    D==eE-------------------------------------R.............  r7 = r7 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R.............  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.............  r8 = u8 [r5 + 551]
    .D=========================eE-------------R.............  r8 = r8 & 0x18
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = a0
    ..D=========================eE-------------------------R  jump 16383 if r8 == 0
```

Gas simulation at offset 16347 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......  r9 = u16 [r5 + 521]
    D=========================eE--------------R......  r10 = r9 & 0x1f
    .D========================eE--------------R......  r9 = r9 & 0xffffffffffffffe0
    .D=========================eeeeeeeeeeeeeeeeeeeeER  jump 16372 if r10 != 31
```

Gas simulation at offset 16362 with total cost of 26:

```
    DeER.........................  r9 = r9 ^ 0x400
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r9
    DeeeeeeeeeeeeeeeE-----------R  jump 16383
```

Gas simulation at offset 16372 with total cost of 27:

```
    DeER..........................  r9 = r9 | r10
    D=eER.........................  r9 = r9 + 0x1
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r9
    DeeE-------------------------R  fallthrough
```

Gas simulation at offset 16383 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r5 + 555]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r10 = u8 [r5 + 556]
    .D========================eE--------------R.............  r11 = r9 << 0x3f
    .D========================eE--------------R.............  r9 = r9 << 0x6
    .D=========================eE-------------R.............  r11 = r11 >>a 0x3f
    ..D========================eE-------------R.............  r9 = sext8 r9
    ..D=========================eE------------R.............  r9 = r9 >> 0x7
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER...  u8 [r5 + 531] = a3
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------R...  u8 [r5 + 533] = a0
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r5 + 535] = a4
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 537] = a2
    ...DeE-------------------------------------------------R  jump 16529 if r8 == 0
```

Gas simulation at offset 16425 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r7 = u16 [r5 + 521]
    DeE---------------------------------------R.......  r10 = 0x7
    .D========================eE--------------R.......  r9 = r7 << 0x31
    .D=========================eE-------------R.......  r9 = r9 >> 0x3d
    .D==========================eeeeeeeeeeeeeeeeeeeeER  jump 16471 if r9 != r10
```

Gas simulation at offset 16442 with total cost of 22:

```
    DeER.....................  r9 = r7 >> 0x5
    D=eER....................  r10 = r9 & 0x1f
    .DeER....................  r11 = 0x1d
    .D=eeeeeeeeeeeeeeeeeeeeER  jump 16491 if r10 == r11
```

Gas simulation at offset 16454 with total cost of 21:

```
    DeER....................  r11 = 0x1f
    D=eeeeeeeeeeeeeeeeeeeeER  jump 16506 if r10 != r11
```

Gas simulation at offset 16460 with total cost of 26:

```
    DeER.........................  r7 = r7 & 0x8c1f
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r7
    DeeeeeeeeeeeeeeeE-----------R  jump 16529
```

Gas simulation at offset 16471 with total cost of 28:

```
    DeER...........................  r9 = r9 + 0x1
    DeER...........................  r7 = r7 & 0x8fff
    D=eER..........................  r9 = r9 << 0xc
    D==eER.........................  r7 = r7 | r9
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r7
    .DeeeeeeeeeeeeeeeE------------R  jump 16529
```

Gas simulation at offset 16491 with total cost of 27:

```
    DeER..........................  r7 = r7 & 0x8c1f
    D=eER.........................  r7 = r7 ^ 0x800
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r7
    DeeeeeeeeeeeeeeeE------------R  jump 16529
```

Gas simulation at offset 16506 with total cost of 29:

```
    DeER............................  r9 = r9 << 0x5
    DeER............................  r7 = r7 & 0x8c1f
    D=eER...........................  r8 = r9 + 0x20
    .D=eER..........................  r8 = r8 & 0x3e0
    .D==eER.........................  r7 = r7 | r8
    .D===eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r7
    .DeeE--------------------------R  fallthrough
```

Gas simulation at offset 16529 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r7 = u8 [r5 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r5 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = i16 [r5 + 529]
    .D========================eE--------------R.............  r7 = r7 & r8
    .D========================eE--------------R.............  r9 = r9 + 0x1
    .D=========================eE-------------R.............  r7 = r7 << 0x38
    .D==========================eE------------R.............  r7 = r7 >> 0x3f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 625] = a0
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u16 [r5 + 529] = r9
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r0 = u64 [r1 + 8]
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE---R  r5 = u64 [r1 + 0]
    ...D========================eE-------------------------R  r1 = r1 + 0x10
    ...D========================eeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 16572 with total cost of 54:

```
    DeER.....................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u16 [r7 + 521]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r10 = u8 [r7 + 551]
    .D=========================eER...........................  r11 = r8 << 0x34
    .D==========================eER..........................  r11 = r11 >> 0x34
    ..D==========================eER.........................  r9 = r11 | 0x2000
    ..D========================eE--R.........................  r10 = r10 & 0x18
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 539] = r9
    ...D========================eE--------------------------R  jump 16625 if r10 == 0
```

Gas simulation at offset 16604 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r9 = u16 [r7 + 523]
    DeE---------------------------------------R............  r8 = r8 & 0xfffffffffffffbe0
    D=========================eE--------------R............  r9 = r9 & 0x41f
    .D=========================eE-------------R............  r8 = r8 | r9
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 521] = r8
    .DeeE-------------------------------------------------R  fallthrough
```

Gas simulation at offset 16625 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r7 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r7 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r10 = i16 [r7 + 529]
    .D========================eE--------------R.............  r8 = r8 & r9
    .D========================eE--------------R.............  r10 = r10 + 0x1
    .D=========================eE-------------R.............  r8 = r8 << 0x38
    .D==========================eE------------R.............  r8 = r8 >> 0x3f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a1
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u16 [r7 + 529] = r10
    ..DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 16660 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 16717 if r9 >=u 63
```

Gas simulation at offset 16683 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 406, jump [r10 + 0]
```

Gas simulation at offset 16715 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 16732
```

Gas simulation at offset 16717 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 16732 with total cost of 72:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  r8 = u8 [r5 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  r9 = u8 [r5 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  r10 = i16 [r5 + 529]
    D=========================eER..............................................  r8 = r8 & r9
    .D========================eER..............................................  r10 = r10 + 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  u16 [r5 + 529] = r10
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.....................  u8 [r5 + 554] = a0
    .D=========================eE------------------------R.....................  r8 = r8 << 0x38
    ..D=========================eE-----------------------R.....................  r8 = r8 >> 0x3f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER...................  u8 [r5 + 625] = a1
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE---R...................  r0 = u64 [r1 + 8]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R...................  r5 = u64 [r1 + 0]
    ...D===============================================eE--R...................  r1 = r1 + 0x10
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 16778 with total cost of 48:

```
    DeER...............................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r2 = u16 [r7 + 529]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r9 = u16 [r7 + 521]
    DeE-------------------------R......................  r11 = 0xc00
    .D=========================eER.....................  r10 = r2 + 0xfffffffffffffeff
    .D=========================eER.....................  r12 = r9 >> 0x4
    ..D=========================eER....................  r8 = zext16 r10
    ..DeE-------------------------R....................  r3 = 0x40
    ..D=========================eER....................  r10 = r12 & 0x38
    ...D=========================eeeeeeeeeeeeeeeeeeeeER  jump 16825 if r8 >=u r3
```

Gas simulation at offset 16812 with total cost of 16:

```
    DeER...............  r8 = r9 & 0xcff
    D=eER..............  r8 = r8 | 0x2000
    .D=eER.............  r9 = r10 + r8
    .DeeeeeeeeeeeeeeeER  jump 16846
```

Gas simulation at offset 16825 with total cost of 4:

```
    DeER...  r11 = r9 & 0xc00
    DeER...  r9 = r9 << 0x3b
    D=eER..  r9 = r9 >> 0x3d
    .D=eER.  r9 = r9 | r11
    .DeE-R.  r8 = r10 | 0x23c0
    .D==eER  r9 = r9 | r8
    ..DeeER  fallthrough
```

Gas simulation at offset 16846 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u8 [r7 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r10 = u8 [r7 + 552]
    DeE------------------------R............................  r2 = r2 + 0x1
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u16 [r7 + 529] = r2
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u16 [r7 + 539] = r9
    .D========================eER...........................  r8 = r8 & r10
    .D=========================eER..........................  r8 = r8 << 0x38
    .D==========================eER.........................  r8 = r8 >> 0x3f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a1
    ..DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 16880 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 16937 if r9 >=u 63
```

Gas simulation at offset 16903 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 412, jump [r10 + 0]
```

Gas simulation at offset 16935 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 16952
```

Gas simulation at offset 16937 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 16952 with total cost of 76:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r8 = u8 [r5 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r9 = u8 [r5 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r10 = u8 [r5 + 521]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r11 = i16 [r5 + 529]
    .D========================eER..................................................  r8 = r8 & r9
    .D========================eER..................................................  r9 = r10 & 0x2
    .D========================eER..................................................  r10 = r10 >> 0x4
    ..D========================eER.................................................  r10 = r10 & 0x4
    ..D=========================eER................................................  r9 = r9 | r10
    ..D=======================eE--R................................................  r7 = r7 & 0xff
    ...D=========================eER...............................................  r7 = r7 >> r9
    ...D=======================eE--R...............................................  r11 = r11 + 0x1
    ...D=======================eE--R...............................................  r8 = r8 << 0x38
    ....D=======================eE-R...............................................  r8 = r8 >> 0x3f
    ....D=========================eER..............................................  r7 = r7 & 0x3
    ....D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u16 [r5 + 529] = r11
    ....D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  u8 [r5 + 555] = a0
    .....D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE--R.....................  u8 [r5 + 625] = a1
    .....D=====================eeeeeeeeeeeeeeeeeeeeeeeeeE----R.....................  r0 = u64 [r1 + 8]
    .....D==============================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 0]
    .....D===============================================eE-----------------------R  r1 = r1 + 0x10
    ......D=============================================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 17024 with total cost of 47:

```
    DeER..............................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r8 = u8 [r7 + 550]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r10 = u8 [r7 + 563]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r9 = i8 [r7 + 565]
    .D=========================eER....................  r11 = r8 & 0x20
    .D==========================eeeeeeeeeeeeeeeeeeeeER  jump 17074 if r11 != 0
```

Gas simulation at offset 17046 with total cost of 30:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....  r11 = i16 [r7 + 527]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....  r12 = u8 [r7 + 564]
    DeE------------------------R.....  r9 = r9 >>a 0x3f
    .D========================eeER...  i32 r11 = r11 - r12
    .D==========================eER..  r9 = r9 ^ r11
    .D===========================eER.  r9 = r9 & 0x7
    ..DeE--------------------------R.  r10 = r10 << 0x4
    ..D===========================eER  r9 = r9 | r10
    ..DeeeeeeeeeeeeeeeE-------------R  jump 17129
```

Gas simulation at offset 17074 with total cost of 39:

```
    DeeeER....................................  r9 = r9 <s 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............  r11 = i16 [r7 + 527]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.............  r12 = u8 [r7 + 564]
    .DeE------------------------R.............  r2 = r10 & 0xe
    .DeE------------------------R.............  r10 = 0xfffffffffffffff8
    ..DeE-----------------------R.............  r3 = 0x7
    ..D========================eeER...........  i32 r11 = r11 - r12
    ..D==========================eER..........  r11 = r11 & 0xf
    ...D==========================eeeER.......  r12 = r11 <u 0x8
    ....D============================eeER.....  r10 = 0 if r12 != 0
    ....D============================eE-R.....  r12 = r12 ^ r9
    .....D=============================eER....  r10 = r10 + r11
    .....D============================eE-R....  r11 = r12 ^ 0x1
    .....D=============================eER....  r11 = r2 | r11
    ......D=============================eER...  r12 = r3 - r10
    ......D==============================eeER.  r12 = r10 if r9 == 0
    .......D============================eE--R.  r9 = r11 << 0x4
    .......D===============================eER  r9 = r9 + r12
    .......DeeE------------------------------R  fallthrough
```

Gas simulation at offset 17129 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r10 = u8 [r7 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r11 = i16 [r7 + 529]
    D=========================eER..........................  r8 = r8 & r10
    D=========================eER..........................  r11 = r11 + 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r7 + 529] = r11
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  u8 [r7 + 539] = a2
    .D=========================eE------------------------R.  r8 = r8 >> 0x7
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a1
    ..DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 17160 with total cost of 52:

```
    DeER...................................................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 0] = r6
    .D.....................................................  r5 = r7
    .DeE------------------------R..........................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = u8 [r6 + 550]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r9 = u8 [r6 + 563]
    ..D=========================eE-----------------------R.  r10 = r8 & 0x20
    ...D================================================eER  r7 = r9 << 0x4
    ...D=========================eE-----------------------R  jump 17249 if r10 != 0
```

Gas simulation at offset 17194 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r8 = r8 & 0x8
    D=eE--------------------------------------R  r8 = r8 << 0x9
    D==eE-------------------------------------R  r7 = r7 | r8
    .D==eE------------------------------------R  r7 = r7 >> 0x8
    .D===eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R  u8 [r6 + 540] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  r8 = u16 [r6 + 539]
    ..D========================eE-------------R  r7 = r8 >> 0x8
    ..D=========================eE------------R  jump 17277 if r7 <u 63
```

Gas simulation at offset 17222 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r8 = r8 & 0x1f
    D=eE--------------------------------------R.......  r8 = r8 + r5
    .D=eE-------------------------------------R.......  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R.......  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r8 = u8 [r6 + 565]
    ..D========================eE-------------R.......  r8 = r8 & 0x40
    ..D=========================eeeeeeeeeeeeeeeeeeeeER  jump 17319 if r8 != 0
```

Gas simulation at offset 17247 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 17366
```

Gas simulation at offset 17249 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r9 = r9 << 0xc
    D=eE--------------------------------------R  r7 = r7 | r9
    D==eE-------------------------------------R  r7 = r7 << 0x33
    .D==eE------------------------------------R  r7 = r7 >> 0x3b
    .D===eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R  u8 [r6 + 540] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  r8 = u16 [r6 + 539]
    ..D========================eE-------------R  r7 = r8 >> 0x8
    ..D=========================eE------------R  jump 17222 if r7 >=u 63
```

Gas simulation at offset 17277 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 418, jump [r10 + 0]
```

Gas simulation at offset 17309 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r8 = u8 [r6 + 565]
    D=========================eER....................  r8 = r8 & 0x40
    D==========================eeeeeeeeeeeeeeeeeeeeER  jump 17366 if r8 == 0
```

Gas simulation at offset 17319 with total cost of 11:

```
    DeER..........  r8 = r7 & 0xff
    DeER..........  r9 = r7 << 0xb
    .DeER.........  r10 = r8 << 0x1
    .D=eER........  r9 = r9 | r10
    .DeE-R........  r10 = 0x22110
    ..DeER........  r7 = r7 << 0xf
    ..DeER........  r8 = r8 << 0x5
    ..D=eER.......  r7 = r7 | r8
    ..D=eER.......  r9 = r9 & r10
    ...D=eER......  r7 = r7 & 0x88440
    ...D==eER.....  r7 = r7 | r9
    ...D===eeeER..  r7 = r7 * 0x10101
    ....D=====eeER  i32 r7 = r7 >> 0x10
    ....DeeE-----R  fallthrough
```

Gas simulation at offset 17366 with total cost of 77:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r8 = u8 [r6 + 566]
    D=========================eER...................................................  r8 = r8 << 0x2
    D==========================eER..................................................  r8 = r8 + r5
    D===========================eER.................................................  r8 = r8 + 0x7ff
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u8 [r8 + 481] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R........................  r7 = u8 [r6 + 550]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R........................  r8 = u8 [r6 + 552]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R........................  r9 = i16 [r6 + 529]
    ..D========================eE--------------------------R........................  r7 = r7 & r8
    ..D========================eE--------------------------R........................  r9 = r9 + 0x1
    ..D=========================eE-------------------------R........................  r7 = r7 << 0x38
    ..D==========================eE------------------------R........................  r7 = r7 >> 0x3f
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u8 [r6 + 625] = a0
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R.......................  u16 [r6 + 529] = r9
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE---R.......................  r0 = u64 [r1 + 16]
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r5 = u64 [r1 + 8]
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D=================================================eE-----------------------R  r1 = r1 + 0x18
    ....D===============================================eeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 17429 with total cost of 47:

```
    DeER..............................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r8 = u8 [r7 + 550]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r10 = u8 [r7 + 563]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r9 = i8 [r7 + 565]
    .D=========================eER....................  r11 = r8 & 0x20
    .D==========================eeeeeeeeeeeeeeeeeeeeER  jump 17479 if r11 != 0
```

Gas simulation at offset 17451 with total cost of 30:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....  r11 = i16 [r7 + 527]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....  r12 = u8 [r7 + 564]
    DeE------------------------R.....  r9 = r9 >>a 0x3f
    .D========================eeER...  i32 r11 = r11 - r12
    .D==========================eER..  r9 = r9 ^ r11
    .D===========================eER.  r9 = r9 & 0x7
    ..DeE--------------------------R.  r10 = r10 << 0x4
    ..D===========================eER  r9 = r9 | r10
    ..DeeeeeeeeeeeeeeeE-------------R  jump 17534
```

Gas simulation at offset 17479 with total cost of 39:

```
    DeeeER....................................  r9 = r9 <s 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............  r11 = i16 [r7 + 527]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.............  r12 = u8 [r7 + 564]
    .DeE------------------------R.............  r2 = r10 & 0xe
    .DeE------------------------R.............  r10 = 0xfffffffffffffff8
    ..DeE-----------------------R.............  r3 = 0x7
    ..D========================eeER...........  i32 r11 = r11 - r12
    ..D==========================eER..........  r11 = r11 & 0xf
    ...D==========================eeeER.......  r12 = r11 <u 0x8
    ....D============================eeER.....  r10 = 0 if r12 != 0
    ....D============================eE-R.....  r12 = r12 ^ r9
    .....D=============================eER....  r10 = r10 + r11
    .....D============================eE-R....  r11 = r12 ^ 0x1
    .....D=============================eER....  r11 = r2 | r11
    ......D=============================eER...  r12 = r3 - r10
    ......D==============================eeER.  r12 = r10 if r9 == 0
    .......D============================eE--R.  r9 = r11 << 0x4
    .......D===============================eER  r9 = r9 + r12
    .......DeeE------------------------------R  fallthrough
```

Gas simulation at offset 17534 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r10 = u8 [r7 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r11 = i16 [r7 + 529]
    D=========================eER..........................  r8 = r8 & r10
    DeE-------------------------R..........................  r9 = r9 + 0x8
    .D========================eER..........................  r11 = r11 + 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r7 + 529] = r11
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  u8 [r7 + 539] = a2
    .D=========================eE------------------------R.  r8 = r8 >> 0x7
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a1
    ..DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 17568 with total cost of 51:

```
    DeER..................................................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 0] = r6
    .D....................................................  r5 = r7
    .DeE------------------------R.........................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER........................  r8 = u8 [r6 + 550]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r6 + 563]
    ..D=========================eE-----------------------R  r9 = r8 & 0x20
    ..D==========================eeeeeeeeeeeeeeeeeeeeE---R  jump 17613 if r9 != 0
```

Gas simulation at offset 17599 with total cost of 16:

```
    DeER...............  r8 = r8 & 0x8
    D=eER..............  r8 = r8 << 0x9
    DeE-R..............  r7 = r7 << 0x4
    D==eER.............  r7 = r7 | r8
    .DeeeeeeeeeeeeeeeER  jump 17682
```

Gas simulation at offset 17613 with total cost of 39:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............  r8 = i16 [r6 + 527]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............  r9 = u8 [r6 + 564]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............  r10 = i8 [r6 + 565]
    .DeE-----------------------R..............  r11 = r7 & 0x1
    .D=eE----------------------R..............  r7 = r7 & 0xfe
    .DeE-----------------------R..............  r12 = 0xfffffffffffffff8
    ..DeE----------------------R..............  r2 = 0x7
    ..D=eE---------------------R..............  r11 = r11 << 0xc
    ...D======================eeeER...........  r10 = r10 <s 0
    ....D=====================eeE-R...........  i32 r8 = r8 - r9
    ....D=======================eER...........  r8 = r8 & 0xf
    .....D=======================eeeER........  r9 = r8 <u 0x8
    ......D=========================eeER......  r12 = 0 if r9 != 0
    ......D=========================eE-R......  r9 = r9 ^ r10
    .......D==========================eER.....  r8 = r8 + r12
    .......D=========================eE-R.....  r9 = r9 ^ 0x1
    .......D==========================eER.....  r7 = r7 | r9
    ........D==========================eER....  r9 = r2 - r8
    ........D===========================eeER..  r9 = r8 if r10 == 0
    .........D=========================eE--R..  r7 = r7 << 0x4
    .........D============================eER.  r9 = r9 + r11
    .........D=============================eER  r7 = r7 + r9
    .........DeeE----------------------------R  fallthrough
```

Gas simulation at offset 17682 with total cost of 27:

```
    DeER..........................  r7 = r7 + 0x8
    D=eER.........................  r7 = r7 >> 0x8
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 540] = a0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE--R  r8 = u16 [r6 + 539]
    .D========================eE-R  r7 = r8 >> 0x8
    .D=========================eER  jump 17747 if r7 >=u 63
```

Gas simulation at offset 17703 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 424, jump [r10 + 0]
```

Gas simulation at offset 17735 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r8 = u8 [r6 + 565]
    D=========================eER....................  r8 = r8 & 0x40
    D==========================eeeeeeeeeeeeeeeeeeeeER  jump 17772 if r8 != 0
```

Gas simulation at offset 17745 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 17816
```

Gas simulation at offset 17747 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r8 = r8 & 0x1f
    D=eE--------------------------------------R.......  r8 = r8 + r5
    .D=eE-------------------------------------R.......  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R.......  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r8 = u8 [r6 + 565]
    ..D========================eE-------------R.......  r8 = r8 & 0x40
    ..D=========================eeeeeeeeeeeeeeeeeeeeER  jump 17816 if r8 == 0
```

Gas simulation at offset 17772 with total cost of 11:

```
    DeER..........  r8 = r7 & 0xff
    DeER..........  r9 = r7 << 0xb
    .DeER.........  r10 = r8 << 0x1
    .D=eER........  r9 = r9 | r10
    .DeE-R........  r7 = r7 << 0xf
    ..DeER........  r8 = r8 << 0x5
    ..D=eER.......  r7 = r7 | r8
    ..D=eER.......  r9 = r9 & 0x22110
    ..D==eER......  r7 = r7 & 0x88440
    ...D==eER.....  r7 = r7 | r9
    ...D===eeeER..  r7 = r7 * 0x10101
    ...D======eeER  i32 r7 = r7 >> 0x10
    ....DeeE-----R  fallthrough
```

Gas simulation at offset 17816 with total cost of 99:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................  r8 = u8 [r6 + 566]
    D=========================eER.........................................................................  r8 = r8 << 0x2
    D==========================eER........................................................................  r8 = r8 + r5
    D===========================eER.......................................................................  r8 = r8 + 0x7ff
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u8 [r8 + 482] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R..............................................  r7 = u8 [r6 + 550]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R..............................................  r8 = u8 [r6 + 552]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R..............................................  r9 = u8 [r6 + 566]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R..............................................  r10 = i16 [r6 + 529]
    ..D========================eE--------------------------R..............................................  r7 = r7 & r8
    ..D========================eE--------------------------R..............................................  r9 = r9 + 0x1
    ..D=================================================eE-R..............................................  r10 = r10 + 0x1
    ...D========================eE-------------------------R..............................................  r7 = r7 << 0x38
    ...D=========================eE------------------------R..............................................  r7 = r7 >> 0x3f
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  u16 [r6 + 529] = r10
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R......................  u8 [r6 + 566] = a2
    ....D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------R......................  u8 [r6 + 625] = a0
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 16]
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r5 = u64 [r1 + 8]
    ....D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................  r6 = u64 [r1 + 0]
    .....D========================================================================eE-R....................  r1 = r1 + 0x18
    .....D========================================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 17890 with total cost of 54:

```
    DeER.....................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u8 [r7 + 550]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r9 = u8 [r7 + 552]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r10 = u16 [r7 + 521]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r11 = i16 [r7 + 529]
    .D=========================eER...........................  r8 = r8 & r9
    .D=========================eER...........................  r10 = r10 << 0x34
    .D==========================eER..........................  r10 = r10 >> 0x34
    ..D==========================eER.........................  r9 = r10 | 0x2000
    ..D========================eE--R.........................  r11 = r11 + 0x1
    ..D=========================eE-R.........................  r8 = r8 << 0x38
    ...D=========================eER.........................  r8 = r8 >> 0x3f
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u16 [r7 + 529] = r11
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 539] = r9
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a1
    ....DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 17946 with total cost of 51:

```
    DeER..................................................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 0] = r6
    .D....................................................  r5 = r7
    .DeE------------------------R.........................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER........................  r8 = u8 [r6 + 550]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r6 + 563]
    ..D=========================eE-----------------------R  r9 = r8 & 0x20
    ..D==========================eeeeeeeeeeeeeeeeeeeeE---R  jump 17991 if r9 != 0
```

Gas simulation at offset 17977 with total cost of 16:

```
    DeER...............  r8 = r8 & 0x8
    D=eER..............  r8 = r8 << 0x9
    DeE-R..............  r7 = r7 << 0x4
    D==eER.............  r7 = r7 | r8
    .DeeeeeeeeeeeeeeeER  jump 18060
```

Gas simulation at offset 17991 with total cost of 39:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............  r8 = i16 [r6 + 527]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............  r9 = u8 [r6 + 564]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............  r10 = i8 [r6 + 565]
    .DeE-----------------------R..............  r11 = r7 & 0x1
    .D=eE----------------------R..............  r7 = r7 & 0xfe
    .DeE-----------------------R..............  r12 = 0xfffffffffffffff8
    ..DeE----------------------R..............  r2 = 0x7
    ..D=eE---------------------R..............  r11 = r11 << 0xc
    ...D======================eeeER...........  r10 = r10 <s 0
    ....D=====================eeE-R...........  i32 r8 = r8 - r9
    ....D=======================eER...........  r8 = r8 & 0xf
    .....D=======================eeeER........  r9 = r8 <u 0x8
    ......D=========================eeER......  r12 = 0 if r9 != 0
    ......D=========================eE-R......  r9 = r9 ^ r10
    .......D==========================eER.....  r8 = r8 + r12
    .......D=========================eE-R.....  r9 = r9 ^ 0x1
    .......D==========================eER.....  r7 = r7 | r9
    ........D==========================eER....  r9 = r2 - r8
    ........D===========================eeER..  r9 = r8 if r10 == 0
    .........D=========================eE--R..  r7 = r7 << 0x4
    .........D============================eER.  r9 = r9 + r11
    .........D=============================eER  r7 = r7 + r9
    .........DeeE----------------------------R  fallthrough
```

Gas simulation at offset 18060 with total cost of 27:

```
    DeER..........................  r7 = r7 + 0x8
    D=eER.........................  r7 = r7 >> 0x8
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 540] = a0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE--R  r8 = u16 [r6 + 539]
    .D========================eE-R  r7 = r8 >> 0x8
    .D=========================eER  jump 18125 if r7 >=u 63
```

Gas simulation at offset 18081 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 430, jump [r10 + 0]
```

Gas simulation at offset 18113 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r8 = u8 [r6 + 565]
    D=========================eER....................  r8 = r8 & 0x40
    D==========================eeeeeeeeeeeeeeeeeeeeER  jump 18150 if r8 != 0
```

Gas simulation at offset 18123 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 18197
```

Gas simulation at offset 18125 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r8 = r8 & 0x1f
    D=eE--------------------------------------R  r8 = r8 + r5
    .D=eE-------------------------------------R  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  r8 = u8 [r6 + 565]
    ..D========================eE-------------R  r8 = r8 & 0x40
    ..D=========================eE------------R  jump 18197 if r8 == 0
```

Gas simulation at offset 18150 with total cost of 11:

```
    DeER..........  r8 = r7 & 0xff
    DeER..........  r9 = r7 << 0xb
    .DeER.........  r10 = r8 << 0x1
    .D=eER........  r9 = r9 | r10
    .DeE-R........  r10 = 0x22110
    ..DeER........  r7 = r7 << 0xf
    ..DeER........  r8 = r8 << 0x5
    ..D=eER.......  r7 = r7 | r8
    ..D=eER.......  r9 = r9 & r10
    ...D=eER......  r7 = r7 & 0x88440
    ...D==eER.....  r7 = r7 | r9
    ...D===eeeER..  r7 = r7 * 0x10101
    ....D=====eeER  i32 r7 = r7 >> 0x10
    ....DeeE-----R  fallthrough
```

Gas simulation at offset 18197 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r6 + 566]
    D=========================eE--------------R.............  r8 = r8 << 0x2
    D==========================eE-------------R.............  r8 = r8 + r5
    .D==========================eE------------R.............  r8 = r8 + 0x7ff
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 482] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R  r7 = u8 [r6 + 566]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R  r8 = u8 [r6 + 551]
    ..D========================eE--------------------------R  r7 = r7 + 0x1
    ..D========================eE--------------------------R  r8 = r8 & 0x18
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  u8 [r6 + 566] = a0
    ..D=========================eE-------------------------R  jump 18266 if r8 == 0
```

Gas simulation at offset 18237 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r7 = u16 [r6 + 521]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r8 = u16 [r6 + 523]
    DeE---------------------------------------R............  r10 = 0x841f
    .D========================eE--------------R............  r7 = r7 & r10
    .D========================eE--------------R............  r8 = r8 & 0x7be0
    .D=========================eE-------------R............  r7 = r7 | r8
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 521] = r7
    ..DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 18266 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r7 = u8 [r6 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r6 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = i16 [r6 + 529]
    .D========================eE--------------R.............  r7 = r7 & r8
    .D========================eE--------------R.............  r9 = r9 + 0x1
    .D=========================eE-------------R.............  r7 = r7 << 0x38
    .D==========================eE------------R.............  r7 = r7 >> 0x3f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 625] = a0
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u16 [r6 + 529] = r9
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r0 = u64 [r1 + 16]
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE---R  r5 = u64 [r1 + 8]
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  r6 = u64 [r1 + 0]
    ...D===============================================eE--R  r1 = r1 + 0x18
    ...D========================eeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 18312 with total cost of 54:

```
    DeER.....................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u16 [r7 + 521]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r10 = u8 [r7 + 551]
    .D=========================eER...........................  r11 = r8 << 0x34
    .D==========================eER..........................  r11 = r11 >> 0x34
    ..D==========================eER.........................  r9 = r11 | 0x2000
    ..D========================eE--R.........................  r10 = r10 & 0x18
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 539] = r9
    ...D========================eE--------------------------R  jump 18369 if r10 == 0
```

Gas simulation at offset 18344 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r9 = u16 [r7 + 523]
    DeE---------------------------------------R............  r11 = 0x841f
    D=eE--------------------------------------R............  r8 = r8 & r11
    .D========================eE--------------R............  r9 = r9 & 0x7be0
    .D=========================eE-------------R............  r8 = r8 | r9
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 521] = r8
    .DeeE-------------------------------------------------R  fallthrough
```

Gas simulation at offset 18369 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r7 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r7 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r10 = i16 [r7 + 529]
    .D========================eE--------------R.............  r8 = r8 & r9
    .D========================eE--------------R.............  r10 = r10 + 0x1
    .D=========================eE-------------R.............  r8 = r8 << 0x38
    .D==========================eE------------R.............  r8 = r8 >> 0x3f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a1
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u16 [r7 + 529] = r10
    ..DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 18404 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..DeE-------------------------R.  r10 = 0x3f
    ..D==========================eER  jump 18477 if r9 >=u r10
```

Gas simulation at offset 18429 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 436, jump [r10 + 0]
```

Gas simulation at offset 18461 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r5 + 551]
    D=========================eER.  r8 = r8 & 0x18
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.  u8 [r5 + 554] = a0
    D==========================eER  jump 18506 if r8 != 0
```

Gas simulation at offset 18475 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 18535
```

Gas simulation at offset 18477 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeE---------------------------------------R.............  r8 = r8 & 0x1f
    D=eE--------------------------------------R.............  r7 = r7 + r8
    D==eE-------------------------------------R.............  r7 = r7 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R.............  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.............  r8 = u8 [r5 + 551]
    .D=========================eE-------------R.............  r8 = r8 & 0x18
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 554] = a0
    ..D=========================eE-------------------------R  jump 18535 if r8 == 0
```

Gas simulation at offset 18506 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r7 = u16 [r5 + 521]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r8 = u16 [r5 + 523]
    DeE---------------------------------------R............  r10 = 0x841f
    .D========================eE--------------R............  r7 = r7 & r10
    .D========================eE--------------R............  r8 = r8 & 0x7be0
    .D=========================eE-------------R............  r7 = r7 | r8
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r7
    ..DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 18535 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r7 = u8 [r5 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r5 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = i16 [r5 + 529]
    .D========================eE--------------R.............  r7 = r7 & r8
    .D========================eE--------------R.............  r9 = r9 + 0x1
    .D=========================eE-------------R.............  r7 = r7 << 0x38
    .D==========================eE------------R.............  r7 = r7 >> 0x3f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 625] = a0
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u16 [r5 + 529] = r9
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r0 = u64 [r1 + 8]
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE---R  r5 = u64 [r1 + 0]
    ...D========================eE-------------------------R  r1 = r1 + 0x10
    ...D========================eeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 18578 with total cost of 29:

```
    DeER............................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  r2 = u16 [r7 + 529]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  r9 = u16 [r7 + 521]
    .D=========================eER..  r10 = r2 + 0xfffffffffffffeff
    .D=========================eER..  r12 = r9 >> 0x4
    ..D=========================eER.  r8 = zext16 r10
    ..DeE-------------------------R.  r3 = 0x40
    ..D=========================eER.  r10 = r12 & 0x38
    ...D=========================eER  jump 18639 if r8 >=u r3
```

Gas simulation at offset 18608 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r8 = r9 & 0xcff
    DeE---------------------------------------R  r11 = 0x2000
    .DeE--------------------------------------R  r8 = r8 | r11
    .D=eE-------------------------------------R  r10 = r10 + r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  r8 = u8 [r7 + 551]
    .D=========================eE-------------R  r8 = r8 & 0x18
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeE------------R  u16 [r7 + 539] = r10
    ..D=========================eE------------R  jump 18677 if r8 != 0
```

Gas simulation at offset 18637 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 18705
```

Gas simulation at offset 18639 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r11 = r9 & 0xc00
    .DeE--------------------------------------R  r8 = r9 << 0x3b
    .D=eE-------------------------------------R  r8 = r8 >> 0x3d
    .D==eE------------------------------------R  r8 = r8 | r11
    ..DeE-------------------------------------R  r11 = 0x23c0
    ..D=eE------------------------------------R  r10 = r10 | r11
    ..D==eE-----------------------------------R  r10 = r10 | r8
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R  r8 = u8 [r7 + 551]
    ...D========================eE------------R  r8 = r8 & 0x18
    ...D==eeeeeeeeeeeeeeeeeeeeeeeeeE----------R  u16 [r7 + 539] = r10
    ...D=========================eE-----------R  jump 18705 if r8 == 0
```

Gas simulation at offset 18677 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r8 = u16 [r7 + 523]
    DeE---------------------------------------R............  r11 = 0x841f
    D=eE--------------------------------------R............  r9 = r9 & r11
    .DeE--------------------------------------R............  r10 = 0x7be0
    .D========================eE--------------R............  r8 = r8 & r10
    .D=========================eE-------------R............  r8 = r8 | r9
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 521] = r8
    ..DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 18705 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r7 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r7 + 552]
    DeE---------------------------------------R.............  r2 = r2 + 0x1
    .D========================eE--------------R.............  r8 = r8 & r9
    .D=========================eE-------------R.............  r8 = r8 << 0x38
    .D==========================eE------------R.............  r8 = r8 >> 0x3f
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a1
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u16 [r7 + 529] = r2
    ..DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 18736 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 18793 if r9 >=u 63
```

Gas simulation at offset 18759 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 442, jump [r10 + 0]
```

Gas simulation at offset 18791 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 18808
```

Gas simulation at offset 18793 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 18808 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r8 = u16 [r5 + 521]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r9 = u8 [r5 + 551]
    D=========================eER.............................  r10 = r8 & 0x2
    .D========================eER.............................  r11 = r8 >> 0x4
    .D=========================eER............................  r11 = r11 & 0x4
    .D==========================eER...........................  r10 = r10 | r11
    ..DeE-------------------------R...........................  r7 = r7 & 0xff
    ..D==========================eER..........................  r7 = r7 >> r10
    ..D===========================eER.........................  r7 = r7 & 0x3
    ...D======================eE----R.........................  r9 = r9 & 0x18
    ...D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 555] = a0
    ...D=======================eE----------------------------R  jump 18873 if r9 == 0
```

Gas simulation at offset 18848 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r7 = u16 [r5 + 523]
    DeE---------------------------------------R............  r10 = 0x841f
    D=eE--------------------------------------R............  r8 = r8 & r10
    .D========================eE--------------R............  r7 = r7 & 0x7be0
    .D=========================eE-------------R............  r7 = r7 | r8
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r7
    .DeeE-------------------------------------------------R  fallthrough
```

Gas simulation at offset 18873 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r7 = u8 [r5 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r5 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = i16 [r5 + 529]
    .D========================eE--------------R.............  r7 = r7 & r8
    .D========================eE--------------R.............  r9 = r9 + 0x1
    .D=========================eE-------------R.............  r7 = r7 << 0x38
    .D==========================eE------------R.............  r7 = r7 >> 0x3f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 625] = a0
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u16 [r5 + 529] = r9
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r0 = u64 [r1 + 8]
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE---R  r5 = u64 [r1 + 0]
    ...D========================eE-------------------------R  r1 = r1 + 0x10
    ...D========================eeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 18916 with total cost of 28:

```
    DeER...........................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r7 + 550]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r10 = u8 [r7 + 563]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r9 = i8 [r7 + 565]
    .D=========================eER.  r11 = r8 & 0x20
    .D==========================eER  jump 18981 if r11 != 0
```

Gas simulation at offset 18938 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...............  r11 = i16 [r7 + 527]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...............  r12 = u8 [r7 + 564]
    DeE---------------------------------------R...............  r9 = r9 >>a 0x3f
    .D========================eeE-------------R...............  i32 r11 = r11 - r12
    .D==========================eE------------R...............  r9 = r9 ^ r11
    .D===========================eE-----------R...............  r9 = r9 & 0x7
    ..DeE-------------------------------------R...............  r10 = r10 << 0x4
    ..D===========================eE----------R...............  r9 = r9 | r10
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R...............  r10 = u8 [r7 + 551]
    ..D=========================eE------------R...............  r10 = r10 & 0x18
    ...D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 539] = a2
    ...D=========================eE--------------------------R  jump 19050 if r10 != 0
```

Gas simulation at offset 18979 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 19082
```

Gas simulation at offset 18981 with total cost of 64:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER........................  unlikely
    DeeeE-------------------------------------R........................  r9 = r9 <s 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R........................  r11 = i16 [r7 + 527]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R........................  r12 = u8 [r7 + 564]
    .DeE--------------------------------------R........................  r2 = r10 & 0xe
    ..DeE-------------------------------------R........................  r10 = 0xfffffffffffffff8
    ..DeE-------------------------------------R........................  r3 = 0x7
    ..D========================eeE------------R........................  i32 r11 = r11 - r12
    ...D=========================eE-----------R........................  r11 = r11 & 0xf
    ...D==========================eeeE--------R........................  r12 = r11 <u 0x8
    ....D============================eeE------R........................  r10 = 0 if r12 != 0
    ....D============================eE-------R........................  r12 = r12 ^ r9
    .....D=============================eE-----R........................  r10 = r10 + r11
    .....D============================eE------R........................  r11 = r12 ^ 0x1
    .....D=============================eE-----R........................  r11 = r2 | r11
    ......D=============================eE----R........................  r12 = r3 - r10
    ......D==============================eeE--R........................  r12 = r10 if r9 == 0
    .......D============================eE----R........................  r9 = r11 << 0x4
    .......D===============================eE-R........................  r9 = r9 + r12
    .......DeeeeeeeeeeeeeeeeeeeeeeeeeE--------R........................  r10 = u8 [r7 + 551]
    ........D========================eE-------R........................  r10 = r10 & 0x18
    ........D===============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 539] = a2
    ........D=========================eE------------------------------R  jump 19082 if r10 == 0
```

Gas simulation at offset 19050 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r9 = u16 [r7 + 521]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r10 = u16 [r7 + 523]
    DeE---------------------------------------R............  r12 = 0x841f
    .DeE--------------------------------------R............  r11 = 0x7be0
    .D========================eE--------------R............  r9 = r9 & r12
    .D========================eE--------------R............  r10 = r10 & r11
    .D=========================eE-------------R............  r9 = r9 | r10
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 521] = r9
    ..DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 19082 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r9 = u8 [r7 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r10 = i16 [r7 + 529]
    D=========================eE--------------R............  r8 = r8 & r9
    .D========================eE--------------R............  r10 = r10 + 0x1
    .D=========================eE-------------R............  r8 = r8 >> 0x7
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  u16 [r7 + 529] = r10
    ..DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 19110 with total cost of 52:

```
    DeER...................................................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 0] = r6
    .D.....................................................  r5 = r7
    .DeE------------------------R..........................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = u8 [r6 + 550]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r9 = u8 [r6 + 563]
    ..D=========================eE-----------------------R.  r10 = r8 & 0x20
    ...D================================================eER  r7 = r9 << 0x4
    ...D=========================eE-----------------------R  jump 19199 if r10 != 0
```

Gas simulation at offset 19144 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r8 = r8 & 0x8
    D=eE--------------------------------------R  r8 = r8 << 0x9
    D==eE-------------------------------------R  r7 = r7 | r8
    .D==eE------------------------------------R  r7 = r7 >> 0x8
    .D===eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R  u8 [r6 + 540] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  r8 = u16 [r6 + 539]
    ..D========================eE-------------R  r7 = r8 >> 0x8
    ..D=========================eE------------R  jump 19227 if r7 <u 63
```

Gas simulation at offset 19172 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r8 = r8 & 0x1f
    D=eE--------------------------------------R.......  r8 = r8 + r5
    .D=eE-------------------------------------R.......  r7 = r8 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R.......  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r8 = u8 [r6 + 565]
    ..D========================eE-------------R.......  r8 = r8 & 0x40
    ..D=========================eeeeeeeeeeeeeeeeeeeeER  jump 19269 if r8 != 0
```

Gas simulation at offset 19197 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 19316
```

Gas simulation at offset 19199 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r9 = r9 << 0xc
    D=eE--------------------------------------R  r7 = r7 | r9
    D==eE-------------------------------------R  r7 = r7 << 0x33
    .D==eE------------------------------------R  r7 = r7 >> 0x3b
    .D===eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R  u8 [r6 + 540] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  r8 = u16 [r6 + 539]
    ..D========================eE-------------R  r7 = r8 >> 0x8
    ..D=========================eE------------R  jump 19172 if r7 >=u 63
```

Gas simulation at offset 19227 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r6 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r6 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r6 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 448, jump [r10 + 0]
```

Gas simulation at offset 19259 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r6 + 565]
    D=========================eER.  r8 = r8 & 0x40
    D==========================eER  jump 19316 if r8 == 0
```

Gas simulation at offset 19269 with total cost of 11:

```
    DeER..........  r8 = r7 & 0xff
    DeER..........  r9 = r7 << 0xb
    .DeER.........  r10 = r8 << 0x1
    .D=eER........  r9 = r9 | r10
    .DeE-R........  r10 = 0x22110
    ..DeER........  r7 = r7 << 0xf
    ..DeER........  r8 = r8 << 0x5
    ..D=eER.......  r7 = r7 | r8
    ..D=eER.......  r9 = r9 & r10
    ...D=eER......  r7 = r7 & 0x88440
    ...D==eER.....  r7 = r7 | r9
    ...D===eeeER..  r7 = r7 * 0x10101
    ....D=====eeER  i32 r7 = r7 >> 0x10
    ....DeeE-----R  fallthrough
```

Gas simulation at offset 19316 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r6 + 566]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = u8 [r6 + 551]
    D=========================eE--------------R.............  r8 = r8 << 0x2
    .D=========================eE-------------R.............  r8 = r8 + r5
    .D==========================eE------------R.............  r8 = r8 + 0x7ff
    .D========================eE--------------R.............  r9 = r9 & 0x18
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 481] = a0
    ..D========================eE--------------------------R  jump 19374 if r9 == 0
```

Gas simulation at offset 19345 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r7 = u16 [r6 + 521]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r8 = u16 [r6 + 523]
    DeE---------------------------------------R............  r10 = 0x841f
    .D========================eE--------------R............  r7 = r7 & r10
    .D========================eE--------------R............  r8 = r8 & 0x7be0
    .D=========================eE-------------R............  r7 = r7 | r8
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 521] = r7
    ..DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 19374 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r7 = u8 [r6 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r8 = u8 [r6 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r9 = i16 [r6 + 529]
    .D========================eE--------------R.............  r7 = r7 & r8
    .D========================eE--------------R.............  r9 = r9 + 0x1
    .D=========================eE-------------R.............  r7 = r7 << 0x38
    .D==========================eE------------R.............  r7 = r7 >> 0x3f
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 625] = a0
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE--R  u16 [r6 + 529] = r9
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r0 = u64 [r1 + 16]
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE---R  r5 = u64 [r1 + 8]
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  r6 = u64 [r1 + 0]
    ...D===============================================eE--R  r1 = r1 + 0x18
    ...D========================eeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 19420 with total cost of 28:

```
    DeER...........................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r7 + 550]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r10 = u8 [r7 + 563]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r9 = i8 [r7 + 565]
    .D=========================eER.  r11 = r8 & 0x20
    .D==========================eER  jump 19488 if r11 != 0
```

Gas simulation at offset 19442 with total cost of 56:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R................  r11 = i16 [r7 + 527]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R................  r12 = u8 [r7 + 564]
    DeE---------------------------------------R................  r9 = r9 >>a 0x3f
    .D========================eeE-------------R................  i32 r11 = r11 - r12
    .D==========================eE------------R................  r9 = r9 ^ r11
    .D===========================eE-----------R................  r9 = r9 & 0x7
    ..DeE-------------------------------------R................  r10 = r10 << 0x4
    ..D===========================eE----------R................  r9 = r9 | r10
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R................  r10 = u8 [r7 + 551]
    ..D============================eE---------R................  r9 = r9 + 0x8
    ...D========================eE------------R................  r10 = r10 & 0x18
    ...D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 539] = a2
    ...D=========================eE---------------------------R  jump 19560 if r10 != 0
```

Gas simulation at offset 19486 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 19592
```

Gas simulation at offset 19488 with total cost of 65:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  unlikely
    DeeeE-------------------------------------R.........................  r9 = r9 <s 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.........................  r11 = i16 [r7 + 527]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.........................  r12 = u8 [r7 + 564]
    .DeE--------------------------------------R.........................  r2 = r10 & 0xe
    ..DeE-------------------------------------R.........................  r10 = 0xfffffffffffffff8
    ..DeE-------------------------------------R.........................  r3 = 0x7
    ..D========================eeE------------R.........................  i32 r11 = r11 - r12
    ...D=========================eE-----------R.........................  r11 = r11 & 0xf
    ...D==========================eeeE--------R.........................  r12 = r11 <u 0x8
    ....D============================eeE------R.........................  r10 = 0 if r12 != 0
    ....D============================eE-------R.........................  r12 = r12 ^ r9
    .....D=============================eE-----R.........................  r10 = r10 + r11
    .....D============================eE------R.........................  r11 = r12 ^ 0x1
    .....D=============================eE-----R.........................  r11 = r2 | r11
    ......D=============================eE----R.........................  r12 = r3 - r10
    ......D==============================eeE--R.........................  r12 = r10 if r9 == 0
    .......D============================eE----R.........................  r9 = r11 << 0x4
    .......D===============================eE-R.........................  r9 = r9 + r12
    .......DeeeeeeeeeeeeeeeeeeeeeeeeeE--------R.........................  r10 = u8 [r7 + 551]
    ........D===============================eER.........................  r9 = r9 + 0x8
    ........D========================eE-------R.........................  r10 = r10 & 0x18
    ........D================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 539] = a2
    ........D=========================eE-------------------------------R  jump 19592 if r10 == 0
```

Gas simulation at offset 19560 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r9 = u16 [r7 + 521]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r10 = u16 [r7 + 523]
    DeE---------------------------------------R............  r12 = 0x841f
    .DeE--------------------------------------R............  r11 = 0x7be0
    .D========================eE--------------R............  r9 = r9 & r12
    .D========================eE--------------R............  r10 = r10 & r11
    .D=========================eE-------------R............  r9 = r9 | r10
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 521] = r9
    ..DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 19592 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r9 = u8 [r7 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r10 = i16 [r7 + 529]
    D=========================eE--------------R............  r8 = r8 & r9
    .D========================eE--------------R............  r10 = r10 + 0x1
    .D=========================eE-------------R............  r8 = r8 >> 0x7
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 625] = a1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  u16 [r7 + 529] = r10
    ..DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 19620 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..D==========================eER  jump 19691 if r9 >=u 63
```

Gas simulation at offset 19643 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 454, jump [r10 + 0]
```

Gas simulation at offset 19675 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r2 = u8 [r5 + 551]
    D=========================eER.  r9 = r2 & 0x18
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.  u8 [r5 + 557] = a0
    .D=========================eER  jump 19720 if r9 != 0
```

Gas simulation at offset 19689 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 19756
```

Gas simulation at offset 19691 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeE---------------------------------------R.............  r8 = r8 & 0x1f
    D=eE--------------------------------------R.............  r7 = r7 + r8
    D==eE-------------------------------------R.............  r7 = r7 + 0x7ff
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R.............  r7 = u8 [r7 + 417]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.............  r2 = u8 [r5 + 551]
    .D=========================eE-------------R.............  r9 = r2 & 0x18
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 557] = a0
    ..D=========================eE-------------------------R  jump 19756 if r9 == 0
```

Gas simulation at offset 19720 with total cost of 46:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......  r9 = u16 [r5 + 521]
    D=========================eE--------------R......  r10 = r9 & 0x1f
    .D========================eE--------------R......  r9 = r9 & 0xffffffffffffffe0
    .D=========================eeeeeeeeeeeeeeeeeeeeER  jump 19745 if r10 != 31
```

Gas simulation at offset 19735 with total cost of 26:

```
    DeER.........................  r9 = r9 ^ 0x400
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r9
    DeeeeeeeeeeeeeeeE-----------R  jump 19756
```

Gas simulation at offset 19745 with total cost of 27:

```
    DeER..........................  r9 = r9 | r10
    D=eER.........................  r9 = r9 + 0x1
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 521] = r9
    DeeE-------------------------R  fallthrough
```

Gas simulation at offset 19756 with total cost of 123:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...................................................................................  r3 = i16 [r5 + 529]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...................................................................................  r10 = u8 [r5 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...................................................................................  r11 = u8 [r5 + 552]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...................................................................................  r12 = u8 [r5 + 555]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r8 = u8 [r5 + 556]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r9 = u8 [r5 + 568]
    .D========================eE------------------------R.........................................................................  r10 = r10 & r11
    ..D========================eE-----------------------R.........................................................................  r2 = r2 << 0x3c
    ..D=========================eE----------------------R.........................................................................  r11 = r2 >> 0x3f
    ..D================================================eER........................................................................  r9 = r9 & r11
    ...D=======================eE------------------------R........................................................................  r11 = r12 << 0x3f
    ...D========================eE-----------------------R........................................................................  r3 = r3 + 0x1
    ...D=========================eE----------------------R........................................................................  r11 = r11 >>a 0x3f
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................  u16 [r5 + 529] = r3
    ....D==============================================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................  u8 [r5 + 531] = a1
    ....D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE---------------------R................................................  u8 [r5 + 533] = a0
    ....D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u8 [r5 + 535] = a4
    .....D================================================eE----------------------R...............................................  r12 = r12 << 0x6
    .....D=================================================eE---------------------R...............................................  r7 = sext8 r12
    .....D=================================================eE---------------------R...............................................  r10 = r10 << 0x38
    .....D==================================================eE--------------------R...............................................  r7 = r7 >> 0x7
    ......D=================================================eE--------------------R...............................................  r10 = r10 >> 0x3f
    ......D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................  u8 [r5 + 537] = a0
    ......D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................  u8 [r5 + 571] = a2
    ......D=====================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u8 [r5 + 625] = a3
    .......D=====================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 8]
    .......D==========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.................  r5 = u64 [r1 + 0]
    .......D==========================================================================eE------------------------R.................  r1 = r1 + 0x10
    .......D==============================================================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 19854 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 0] = r5
    .DeE------------------------R...  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u16 [r5 + 539]
    ..D=========================eER.  r9 = r8 >> 0x8
    ..DeE-------------------------R.  r10 = 0x3f
    ..D==========================eER  jump 19913 if r9 >=u r10
```

Gas simulation at offset 19879 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r9 = u64 [r5 + 577]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r5 + 585]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r9 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r10 = u64 [r10 + 72]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r9 if r9 != 0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeER  r0 = 458, jump [r10 + 0]
```

Gas simulation at offset 19911 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 19928
```

Gas simulation at offset 19913 with total cost of 28:

```
    DeER...........................  r8 = r8 & 0x1f
    D=eER..........................  r7 = r7 + r8
    D==eER.........................  r7 = r7 + 0x7ff
    D===eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 417]
    .DeeE-------------------------R  fallthrough
```

Gas simulation at offset 19928 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u8 [r5 + 550]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r9 = u8 [r5 + 552]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  u8 [r5 + 554] = a0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r7 = u8 [r5 + 571]
    .D========================eER...........................  r8 = r8 & r9
    .D=========================eER..........................  r8 = r8 << 0x38
    .D==========================eER.........................  r8 = r8 >> 0x3f
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 625] = a1
    ..D=======================eE---------------------------R  jump 19968 if r7 == 0
```

Gas simulation at offset 19960 with total cost of 26:

```
    DeER.........................  r7 = 0x1
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 572] = a0
    DeeE------------------------R  fallthrough
```

Gas simulation at offset 19968 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  u32 [r5 + 527] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 0]
    .DeE--------------------------------------R.......  r1 = r1 + 0x10
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 19983 with total cost of 22:

```
    DeER.....................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 19987 with total cost of 22:

```
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 19989 with total cost of 22:

```
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 19991 with total cost of 52:

```
    DeER...................................................  r1 = r1 + 0xffffffffffffffd0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 40] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 32] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 24] = r6
    .D.....................................................  r5 = r7
    .DeE------------------------R..........................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u8 [r6 + 613]
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r7
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  r8 = u16 [r6 + 617]
    ..D....................................................  r7 = r5
    ..DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 468, jump 22431
```

Gas simulation at offset 20028 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = i16 [r6 + 617]
    DeE------------------------R..........................  r9 = r7 << 0x8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 0] = r9
    .D========================eER.........................  r8 = r8 + 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 617] = r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r7 = u64 [r1 + 16]
    .D=========================eE------------------------R  r7 = r7 | r9
    ..D=========================eE-----------------------R  r8 = zext16 r7
    ..D...................................................  r7 = r5
    ..DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 470, jump 22431
```

Gas simulation at offset 20060 with total cost of 29:

```
    DeER............................  r7 = r7 & 0xff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R...  r7 = u64 [r1 + 16]
    D=========================eER...  r7 = r7 + 0x1
    .D=========================eER..  r7 = r7 & 0xff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R..  r8 = u64 [r1 + 0]
    .D==========================eER.  r7 = r7 | r8
    .D===========================eER  r8 = zext16 r7
    ..D.............................  r7 = r5
    ..DeeeeeeeeeeeeeeeE------------R  r0 = 472, jump 22431
```

Gas simulation at offset 20092 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u16 [r6 + 609]
    DeE------------------------R............................  r7 = r7 << 0x8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r9 = u64 [r1 + 8]
    D=========================eER...........................  r9 = r9 | r7
    .D=========================eER..........................  r7 = zext16 r9
    .D==========================eER.........................  r7 = r7 ^ r8
    ..D==========================eeeER......................  r7 = r7 <u 0x1
    ..D=======================eE-----R......................  r8 = r8 << 0x20
    ...D============================eER.....................  r7 = r7 << 0x10
    ...D=============================eER....................  r7 = r7 | r8
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u16 [r6 + 617] = r9
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------R..  r0 = u64 [r1 + 40]
    ....DeeeeeeeeeeeeeeeeeeeeeeeeeE----------------------R..  r5 = u64 [r1 + 32]
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    ....D=========================eE-----------------------R  r1 = r1 + 0x30
    ....D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 20140 with total cost of 51:

```
    DeER..................................................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 0] = r6
    .DeE------------------------R.........................  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER........................  r6 = u8 [r5 + 613]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r5 + 617]
    ..DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 476, jump 22431
```

Gas simulation at offset 20169 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u16 [r5 + 609]
    DeE------------------------R............................  r7 = r7 << 0x8
    D=eE-----------------------R............................  r6 = r6 | r7
    D==eE----------------------R............................  r7 = zext16 r6
    .D========================eER...........................  r7 = r7 ^ r8
    .D=========================eeeER........................  r7 = r7 <u 0x1
    ..D=========================eE-R........................  r8 = r8 << 0x20
    ..D===========================eER.......................  r7 = r7 << 0x10
    ..D============================eER......................  r7 = r7 | r8
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE----R......................  u16 [r5 + 617] = r6
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE---R......................  r0 = u64 [r1 + 16]
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE---R......................  r5 = u64 [r1 + 8]
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ...D=========================eE------------------------R  r1 = r1 + 0x18
    ....D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 20213 with total cost of 52:

```
    DeER...................................................  r1 = r1 + 0xffffffffffffffe0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 24] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 16] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 8] = r6
    .DeE------------------------R..........................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = u8 [r6 + 615]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r9 = u8 [r6 + 613]
    ..D=========================eE-----------------------R.  r10 = r8 & 0x7
    ..DeE------------------------------------------------R.  r2 = 0x7
    ...D================================================eER  r5 = r9 + 0x1
    ...D=========================eE-----------------------R  jump 20273 if r10 == r2
```

Gas simulation at offset 20249 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 611]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    DeeeeeeeeeeeeeeeE----------R  r0 = 480, jump 22969
```

Gas simulation at offset 20263 with total cost of 25:

```
    DeER........................  r2 = 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u8 [r6 + 615]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 20273 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r10 = u8 [r6 + 623]
    DeE---------------------------------------R.............  r11 = r5 & 0x80
    .DeE--------------------------------------R.............  r9 = r5 & 0xff
    ..DeeeE-----------------------------------R.............  r12 = r9 <u 0x1
    ..D===eE----------------------------------R.............  r12 = r12 << 0x1
    ...D======================eE--------------R.............  r10 = r10 & 0x7d
    ...D=======================eE-------------R.............  r10 = r10 | r11
    ...D========================eE------------R.............  r10 = r10 | r12
    ....DeE-----------------------------------R.............  r11 = r8 & 0x7
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 623] = a3
    ....D=eeeeeeeeeeeeeeeeeeeeE----------------------------R  jump 20340 if r11 != 7
```

Gas simulation at offset 20312 with total cost of 2:

```
    DeER.  r8 = r8 & 0x18
    D=eER  jump 20366 if r8 != 8
```

Gas simulation at offset 20319 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  u8 [r6 + 620] = s0
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 24]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 8]
    .D========================eE--------------R.......  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 20340 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 611]
    DeeeeeeeeeeeeeeeE----------R  r0 = 482, jump 22969
```

Gas simulation at offset 20350 with total cost of 47:

```
    DeER..............................................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 8]
    .DeE-----------------------R......................  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 20366 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  u8 [r6 + 621] = s0
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 24]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 8]
    .D========================eE--------------R.......  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 20387 with total cost of 58:

```
    DeER.........................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER................................  r8 = u8 [r7 + 613]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER................................  r9 = u8 [r7 + 619]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER................................  r10 = u8 [r7 + 623]
    .D=========================eER...............................  r11 = r9 - r8
    .D=========================eER...............................  r10 = r10 & 0x7c
    .D=========================eER...............................  r8 = r8 ^ r9
    ..D=========================eeeER............................  r9 = r11 <u 0x100
    ..D=========================eE--R............................  r11 = r11 & 0x80
    ...D========================eeeER............................  r8 = r8 <u 0x1
    ...D===========================eER...........................  r8 = r8 << 0x1
    ....D==========================eER...........................  r9 = r9 | r10
    ....D===========================eER..........................  r8 = r8 | r9
    ....D============================eER.........................  r8 = r8 | r11
    ....D=============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    .....DeE----------------------------------------------------R  r7 = 0
    .....DeeeeeeeeeeeeeeeeeeeeeeE-------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 20443 with total cost of 58:

```
    DeER.........................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER................................  r8 = u8 [r7 + 613]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER................................  r9 = u8 [r7 + 620]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER................................  r10 = u8 [r7 + 623]
    .D=========================eER...............................  r11 = r9 - r8
    .D=========================eER...............................  r10 = r10 & 0x7c
    .D=========================eER...............................  r8 = r8 ^ r9
    ..D=========================eeeER............................  r9 = r11 <u 0x100
    ..D=========================eE--R............................  r11 = r11 & 0x80
    ...D========================eeeER............................  r8 = r8 <u 0x1
    ...D===========================eER...........................  r8 = r8 << 0x1
    ....D==========================eER...........................  r9 = r9 | r10
    ....D===========================eER..........................  r8 = r8 | r9
    ....D============================eER.........................  r8 = r8 | r11
    ....D=============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    .....DeE----------------------------------------------------R  r7 = 0
    .....DeeeeeeeeeeeeeeeeeeeeeeE-------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 20499 with total cost of 58:

```
    DeER.........................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER................................  r8 = u8 [r7 + 613]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER................................  r9 = u8 [r7 + 621]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER................................  r10 = u8 [r7 + 623]
    .D=========================eER...............................  r11 = r9 - r8
    .D=========================eER...............................  r10 = r10 & 0x7c
    .D=========================eER...............................  r8 = r8 ^ r9
    ..D=========================eeeER............................  r9 = r11 <u 0x100
    ..D=========================eE--R............................  r11 = r11 & 0x80
    ...D========================eeeER............................  r8 = r8 <u 0x1
    ...D===========================eER...........................  r8 = r8 << 0x1
    ....D==========================eER...........................  r9 = r9 | r10
    ....D===========================eER..........................  r8 = r8 | r9
    ....D============================eER.........................  r8 = r8 | r11
    ....D=============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    .....DeE----------------------------------------------------R  r7 = 0
    .....DeeeeeeeeeeeeeeeeeeeeeeE-------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 20555 with total cost of 56:

```
    DeER.......................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r8 = u8 [r7 + 623]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r9 = u8 [r7 + 613]
    D==========================eER.............................  r8 = r8 & 0x7d
    .D=========================eER.............................  r10 = r9 & 0x80
    ..D========================eeeER...........................  r11 = r9 <u 0x1
    ..D===========================eER..........................  r11 = r11 << 0x1
    ...D========================eE--R..........................  r8 = r8 | r10
    ...D===========================eER.........................  r8 = r8 | r11
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER.....  u8 [r7 + 619] = a2
    ...D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    ....DeE---------------------------------------------------R  r7 = 0
    ....DeeeeeeeeeeeeeeeeeeeeeeE------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 20598 with total cost of 56:

```
    DeER.......................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r8 = u8 [r7 + 623]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r9 = u8 [r7 + 613]
    D==========================eER.............................  r8 = r8 & 0x7d
    .D=========================eER.............................  r10 = r9 & 0x80
    ..D========================eeeER...........................  r11 = r9 <u 0x1
    ..D===========================eER..........................  r11 = r11 << 0x1
    ...D========================eE--R..........................  r8 = r8 | r10
    ...D===========================eER.........................  r8 = r8 | r11
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER.....  u8 [r7 + 620] = a2
    ...D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    ....DeE---------------------------------------------------R  r7 = 0
    ....DeeeeeeeeeeeeeeeeeeeeeeE------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 20641 with total cost of 56:

```
    DeER.......................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r8 = u8 [r7 + 623]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r9 = u8 [r7 + 613]
    D==========================eER.............................  r8 = r8 & 0x7d
    .D=========================eER.............................  r10 = r9 & 0x80
    ..D========================eeeER...........................  r11 = r9 <u 0x1
    ..D===========================eER..........................  r11 = r11 << 0x1
    ...D========================eE--R..........................  r8 = r8 | r10
    ...D===========================eER.........................  r8 = r8 | r11
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER.....  u8 [r7 + 621] = a2
    ...D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    ....DeE---------------------------------------------------R  r7 = 0
    ....DeeeeeeeeeeeeeeeeeeeeeeE------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 20684 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xfffffffffffffff8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r0
    DeE-------------------------R  r9 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r9 + 611]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r9 = u8 [r9 + 619]
    .DeeeeeeeeeeeeeeeE----------R  r0 = 498, jump 22969
```

Gas simulation at offset 20707 with total cost of 47:

```
    DeER..............................................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 0]
    DeE------------------------R......................  r1 = r1 + 0x8
    D=========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 20716 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xfffffffffffffff8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r0
    DeE-------------------------R  r9 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r9 + 611]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r9 = u8 [r9 + 620]
    .DeeeeeeeeeeeeeeeE----------R  r0 = 502, jump 22969
```

Gas simulation at offset 20739 with total cost of 47:

```
    DeER..............................................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 0]
    DeE------------------------R......................  r1 = r1 + 0x8
    D=========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 20748 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xfffffffffffffff8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r0
    DeE-------------------------R  r9 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r9 + 611]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r9 = u8 [r9 + 621]
    .DeeeeeeeeeeeeeeeE----------R  r0 = 506, jump 22969
```

Gas simulation at offset 20771 with total cost of 47:

```
    DeER..............................................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 0]
    DeE------------------------R......................  r1 = r1 + 0x8
    D=========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 20780 with total cost of 52:

```
    DeER...................................................  r1 = r1 + 0xffffffffffffffe0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 24] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 16] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 8] = r6
    .DeE------------------------R..........................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = u8 [r6 + 615]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r9 = u8 [r6 + 613]
    ..D=========================eE-----------------------R.  r10 = r8 & 0x7
    ..DeE------------------------------------------------R.  r2 = 0x7
    ...D================================================eER  r5 = r9 + 0xffffffffffffffff
    ...D=========================eE-----------------------R  jump 20840 if r10 == r2
```

Gas simulation at offset 20816 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 611]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    DeeeeeeeeeeeeeeeE----------R  r0 = 510, jump 22969
```

Gas simulation at offset 20830 with total cost of 25:

```
    DeER........................  r2 = 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u8 [r6 + 615]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 20840 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r10 = u8 [r6 + 623]
    DeE---------------------------------------R.............  r11 = r5 & 0x80
    .DeE--------------------------------------R.............  r9 = r5 & 0xff
    ..DeeeE-----------------------------------R.............  r12 = r9 <u 0x1
    ..D===eE----------------------------------R.............  r12 = r12 << 0x1
    ...D======================eE--------------R.............  r10 = r10 & 0x7d
    ...D=======================eE-------------R.............  r10 = r10 | r11
    ...D========================eE------------R.............  r10 = r10 | r12
    ....DeE-----------------------------------R.............  r11 = r8 & 0x7
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 623] = a3
    ....D=eeeeeeeeeeeeeeeeeeeeE----------------------------R  jump 20907 if r11 != 7
```

Gas simulation at offset 20879 with total cost of 2:

```
    DeER.  r8 = r8 & 0x18
    D=eER  jump 20933 if r8 != 8
```

Gas simulation at offset 20886 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  u8 [r6 + 620] = s0
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 24]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 8]
    .D========================eE--------------R.......  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 20907 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 611]
    DeeeeeeeeeeeeeeeE----------R  r0 = 512, jump 22969
```

Gas simulation at offset 20917 with total cost of 47:

```
    DeER..............................................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 8]
    .DeE-----------------------R......................  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 20933 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  u8 [r6 + 621] = s0
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 24]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 8]
    .D========================eE--------------R.......  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 20954 with total cost of 27:

```
    DeER..........................  r1 = r1 + 0xfffffffffffffff8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 0] = r0
    DeE-------------------------R.  r8 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r9 = u8 [r8 + 619]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r10 = u8 [r8 + 620]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u16 [r8 + 611]
    .D=========================eER  r9 = r9 & r10
    ..DeeeeeeeeeeeeeeeE----------R  r0 = 516, jump 22969
```

Gas simulation at offset 20984 with total cost of 47:

```
    DeER..............................................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 0]
    DeE------------------------R......................  r1 = r1 + 0x8
    D=========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 20993 with total cost of 56:

```
    DeER.......................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r8 = u8 [r7 + 623]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................  r9 = u8 [r7 + 613]
    D==========================eER.............................  r8 = r8 & 0x7d
    .D=========================eER.............................  r10 = r9 & 0x80
    ..D========================eeeER...........................  r11 = r9 <u 0x1
    ..D===========================eER..........................  r11 = r11 << 0x1
    ...D========================eE--R..........................  r8 = r8 | r10
    ...D===========================eER.........................  r8 = r8 | r11
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER.....  u8 [r7 + 619] = a2
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER....  u8 [r7 + 620] = a2
    ....D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    ....DeE---------------------------------------------------R  r7 = 0
    ....DeeeeeeeeeeeeeeeeeeeeeeE------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 21040 with total cost of 52:

```
    DeER...................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r7 + 623]
    D==========================eER.........................  r8 = r8 & 0xfe
    D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    .DeE--------------------------------------------------R  r7 = 0
    .DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 21060 with total cost of 52:

```
    DeER...................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r7 + 623]
    D==========================eER.........................  r8 = r8 | 0x1
    D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    .DeE--------------------------------------------------R  r7 = 0
    .DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 21079 with total cost of 52:

```
    DeER...................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r7 + 623]
    D==========================eER.........................  r8 = r8 & 0xf7
    D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    .DeE--------------------------------------------------R  r7 = 0
    .DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 21099 with total cost of 52:

```
    DeER...................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r7 + 623]
    D==========================eER.........................  r8 = r8 | 0x8
    D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    .DeE--------------------------------------------------R  r7 = 0
    .DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 21118 with total cost of 52:

```
    DeER...................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r7 + 623]
    D==========================eER.........................  r8 = r8 & 0xbf
    D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    .DeE--------------------------------------------------R  r7 = 0
    .DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 21138 with total cost of 52:

```
    DeER...................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r7 + 623]
    D==========================eER.........................  r8 = r8 & 0xfb
    D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    .DeE--------------------------------------------------R  r7 = 0
    .DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 21158 with total cost of 52:

```
    DeER...................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r7 + 623]
    D==========================eER.........................  r8 = r8 | 0x4
    D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    .DeE--------------------------------------------------R  r7 = 0
    .DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 21177 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 24] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r6
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = i8 [r6 + 623]
    .D==========================eER  jump 21217 if r8 <s 0
```

Gas simulation at offset 21200 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 8]
    .DeE--------------------------------------R.......  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 21217 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 617]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeeeeeeeeeeeeeeeE----------R  r0 = 536, jump 22431
```

Gas simulation at offset 21229 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = i8 [r6 + 613]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r7 = u16 [r6 + 617]
    D=========================eER.....................  r5 = r5 + r7
    D=========================eER.....................  r7 = r7 & 0xffffffffffffff00
    .D=========================eER....................  r8 = r5 & 0xff00
    .D==========================eeeeeeeeeeeeeeeeeeeeER  jump 21267 if r7 == r8
```

Gas simulation at offset 21252 with total cost of 25:

```
    DeER........................  r8 = r5 & 0xff
    D=eER.......................  r8 = r8 | r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    .DeeeeeeeeeeeeeeeE---------R  r0 = 538, jump 22431
```

Gas simulation at offset 21267 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  u16 [r6 + 617] = r5
    DeE------------------------R......................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r6 = u64 [r1 + 8]
    .D========================eER.....................  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 21287 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xffffffffffffffe0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 24] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 16] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r6
    .DeE------------------------R...  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r6 + 623]
    .D==========================eER.  r8 = r8 & 0x2
    ..D==========================eER  jump 21368 if r8 == 0
```

Gas simulation at offset 21313 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 617]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeeeeeeeeeeeeeeeE----------R  r0 = 542, jump 22431
```

Gas simulation at offset 21325 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = i8 [r6 + 613]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r7 = u16 [r6 + 617]
    D=========================eER.....................  r5 = r5 + r7
    D=========================eER.....................  r7 = r7 & 0xffffffffffffff00
    .D=========================eER....................  r8 = r5 & 0xff00
    .D==========================eeeeeeeeeeeeeeeeeeeeER  jump 21363 if r7 == r8
```

Gas simulation at offset 21348 with total cost of 25:

```
    DeER........................  r8 = r5 & 0xff
    D=eER.......................  r8 = r8 | r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    .DeeeeeeeeeeeeeeeE---------R  r0 = 544, jump 22431
```

Gas simulation at offset 21363 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 617] = r5
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 21368 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 8]
    .DeE--------------------------------------R.......  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 21385 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xffffffffffffffe0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 24] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 16] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r6
    .DeE------------------------R...  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r6 + 623]
    .D==========================eER.  r8 = r8 & 0x1
    ..D==========================eER  jump 21466 if r8 == 0
```

Gas simulation at offset 21411 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 617]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeeeeeeeeeeeeeeeE----------R  r0 = 548, jump 22431
```

Gas simulation at offset 21423 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = i8 [r6 + 613]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r7 = u16 [r6 + 617]
    D=========================eER.....................  r5 = r5 + r7
    D=========================eER.....................  r7 = r7 & 0xffffffffffffff00
    .D=========================eER....................  r8 = r5 & 0xff00
    .D==========================eeeeeeeeeeeeeeeeeeeeER  jump 21461 if r7 == r8
```

Gas simulation at offset 21446 with total cost of 25:

```
    DeER........................  r8 = r5 & 0xff
    D=eER.......................  r8 = r8 | r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    .DeeeeeeeeeeeeeeeE---------R  r0 = 550, jump 22431
```

Gas simulation at offset 21461 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 617] = r5
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 21466 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 8]
    .DeE--------------------------------------R.......  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 21483 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 24] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r6
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = i8 [r6 + 623]
    .D==========================eER  jump 21561 if r8 <s 0
```

Gas simulation at offset 21506 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 617]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeeeeeeeeeeeeeeeE----------R  r0 = 554, jump 22431
```

Gas simulation at offset 21518 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = i8 [r6 + 613]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r7 = u16 [r6 + 617]
    D=========================eER.....................  r5 = r5 + r7
    D=========================eER.....................  r7 = r7 & 0xffffffffffffff00
    .D=========================eER....................  r8 = r5 & 0xff00
    .D==========================eeeeeeeeeeeeeeeeeeeeER  jump 21556 if r7 == r8
```

Gas simulation at offset 21541 with total cost of 25:

```
    DeER........................  r8 = r5 & 0xff
    D=eER.......................  r8 = r8 | r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    .DeeeeeeeeeeeeeeeE---------R  r0 = 556, jump 22431
```

Gas simulation at offset 21556 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 617] = r5
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 21561 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 8]
    .DeE--------------------------------------R.......  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 21578 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xffffffffffffffe0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 24] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 16] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r6
    .DeE------------------------R...  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r6 + 623]
    .D==========================eER.  r8 = r8 & 0x2
    ..D==========================eER  jump 21659 if r8 != 0
```

Gas simulation at offset 21604 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 617]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeeeeeeeeeeeeeeeE----------R  r0 = 560, jump 22431
```

Gas simulation at offset 21616 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = i8 [r6 + 613]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r7 = u16 [r6 + 617]
    D=========================eER.....................  r5 = r5 + r7
    D=========================eER.....................  r7 = r7 & 0xffffffffffffff00
    .D=========================eER....................  r8 = r5 & 0xff00
    .D==========================eeeeeeeeeeeeeeeeeeeeER  jump 21654 if r7 == r8
```

Gas simulation at offset 21639 with total cost of 25:

```
    DeER........................  r8 = r5 & 0xff
    D=eER.......................  r8 = r8 | r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    .DeeeeeeeeeeeeeeeE---------R  r0 = 562, jump 22431
```

Gas simulation at offset 21654 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 617] = r5
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 21659 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 8]
    .DeE--------------------------------------R.......  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 21676 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xffffffffffffffe0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 24] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 16] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r6
    .DeE------------------------R...  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r6 + 623]
    .D==========================eER.  r8 = r8 & 0x1
    ..D==========================eER  jump 21757 if r8 != 0
```

Gas simulation at offset 21702 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 617]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeeeeeeeeeeeeeeeE----------R  r0 = 566, jump 22431
```

Gas simulation at offset 21714 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = i8 [r6 + 613]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r7 = u16 [r6 + 617]
    D=========================eER.....................  r5 = r5 + r7
    D=========================eER.....................  r7 = r7 & 0xffffffffffffff00
    .D=========================eER....................  r8 = r5 & 0xff00
    .D==========================eeeeeeeeeeeeeeeeeeeeER  jump 21752 if r7 == r8
```

Gas simulation at offset 21737 with total cost of 25:

```
    DeER........................  r8 = r5 & 0xff
    D=eER.......................  r8 = r8 | r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    .DeeeeeeeeeeeeeeeE---------R  r0 = 568, jump 22431
```

Gas simulation at offset 21752 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 617] = r5
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 21757 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 8]
    .DeE--------------------------------------R.......  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 21774 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xffffffffffffffe0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 24] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 16] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r6
    .DeE------------------------R...  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r6 + 623]
    .D==========================eER.  r8 = r8 & 0x40
    ..D==========================eER  jump 21855 if r8 == 0
```

Gas simulation at offset 21800 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 617]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeeeeeeeeeeeeeeeE----------R  r0 = 572, jump 22431
```

Gas simulation at offset 21812 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = i8 [r6 + 613]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r7 = u16 [r6 + 617]
    D=========================eER.....................  r5 = r5 + r7
    D=========================eER.....................  r7 = r7 & 0xffffffffffffff00
    .D=========================eER....................  r8 = r5 & 0xff00
    .D==========================eeeeeeeeeeeeeeeeeeeeER  jump 21850 if r7 == r8
```

Gas simulation at offset 21835 with total cost of 25:

```
    DeER........................  r8 = r5 & 0xff
    D=eER.......................  r8 = r8 | r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    .DeeeeeeeeeeeeeeeE---------R  r0 = 574, jump 22431
```

Gas simulation at offset 21850 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 617] = r5
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 21855 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 8]
    .DeE--------------------------------------R.......  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 21872 with total cost of 29:

```
    DeER............................  r1 = r1 + 0xffffffffffffffe0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 24] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 16] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  u64 [r1 + 8] = r6
    .DeE------------------------R...  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r6 + 623]
    .D==========================eER.  r8 = r8 & 0x40
    ..D==========================eER  jump 21953 if r8 != 0
```

Gas simulation at offset 21898 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 617]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeeeeeeeeeeeeeeeE----------R  r0 = 578, jump 22431
```

Gas simulation at offset 21910 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = i8 [r6 + 613]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r7 = u16 [r6 + 617]
    D=========================eER.....................  r5 = r5 + r7
    D=========================eER.....................  r7 = r7 & 0xffffffffffffff00
    .D=========================eER....................  r8 = r5 & 0xff00
    .D==========================eeeeeeeeeeeeeeeeeeeeER  jump 21948 if r7 == r8
```

Gas simulation at offset 21933 with total cost of 25:

```
    DeER........................  r8 = r5 & 0xff
    D=eER.......................  r8 = r8 | r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    .DeeeeeeeeeeeeeeeE---------R  r0 = 580, jump 22431
```

Gas simulation at offset 21948 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 617] = r5
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 21953 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 8]
    .DeE--------------------------------------R.......  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 21970 with total cost of 22:

```
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 21972 with total cost of 51:

```
    DeER..................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = u8 [r7 + 613]
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 611] = r8
    DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 21986 with total cost of 27:

```
    DeER..........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 0] = r6
    .D............................  r5 = r7
    .DeE------------------------R.  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 617]
    ..DeeeeeeeeeeeeeeeE----------R  r0 = 588, jump 22431
```

Gas simulation at offset 22013 with total cost of 61:

```
    D...............................................................  r8 = r7
    D...............................................................  r7 = r5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................  r9 = i16 [r6 + 617]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................  r10 = u8 [r6 + 615]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................  r11 = u8 [r6 + 613]
    .D========================eER...................................  r9 = r9 + 0x1
    .D========================eER...................................  r12 = r10 & 0x18
    ..D========================eER..................................  r12 = r12 + 0xfffffffffffffff8
    ..D=========================eeeER...............................  r12 = r12 <u 0x1
    ...D===========================eER..............................  r12 = r5 - r12
    ...D============================eER.............................  r12 = r12 + 0x7ff
    ...D=============================eeeeeeeeeeeeeeeeeeeeeeeeeER....  r5 = u8 [r12 + 621]
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE------R....  u16 [r6 + 617] = r9
    ....DeE----------------------------------------------------R....  r8 = r8 << 0x8
    ....D======================eE------------------------------R....  r11 = r11 | r8
    ....D=====================================================eER...  r5 = r5 + r11
    .....D=====================================================eER..  r9 = r5 & 0xff
    .....D======================================================eER.  r8 = r8 | r9
    ......D===================eE----------------------------------R.  r9 = r10 & 0x20
    ......D======================================================eER  r8 = zext16 r8
    ......D====================eeeeeeeeeeeeeeeeeeeeE---------------R  jump 22103 if r9 != 0
```

Gas simulation at offset 22080 with total cost of 2:

```
    DeER.  r9 = zext16 r5
    D=eER  jump 22103 if r8 != r9
```

Gas simulation at offset 22085 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  u16 [r6 + 611] = r5
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 0]
    .D========================eE--------------R.......  r1 = r1 + 0x18
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 22103 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  r0 = 590, jump 22431
```

Gas simulation at offset 22109 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  u16 [r6 + 611] = r5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 0]
    .D========================eER.....................  r1 = r1 + 0x18
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 22126 with total cost of 27:

```
    DeER..........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 0] = r6
    .D............................  r5 = r7
    .DeE------------------------R.  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u8 [r6 + 613]
    ..DeeeeeeeeeeeeeeeE----------R  r0 = 594, jump 22431
```

Gas simulation at offset 22153 with total cost of 84:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................  r7 = u8 [r6 + 615]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................  r8 = u8 [r6 + 613]
    D=========================eER..........................................................  r7 = r7 & 0x18
    D==========================eER.........................................................  r7 = r7 + 0xfffffffffffffff8
    .D==========================eeeER......................................................  r7 = r7 <u 0x1
    .D=============================eER.....................................................  r5 = r5 - r7
    ..D=============================eER....................................................  r7 = r5 + 0x7ff
    ..D==============================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r7 = u8 [r7 + 621]
    ..D=======================================================eER..........................  r7 = r7 + r8
    ...D=======================================================eER.........................  r7 = r7 & 0xff
    ...D========================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 611] = r7
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------------------------------------R  r0 = u64 [r1 + 16]
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------------------------------------R  r5 = u64 [r1 + 8]
    ....D=====================eeeeeeeeeeeeeeeeeeeeeeeeeE----------------------------------R  r6 = u64 [r1 + 0]
    ....D========================eE-------------------------------------------------------R  r1 = r1 + 0x18
    ....D========================eeeeeeeeeeeeeeeeeeeeeeE----------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 22205 with total cost of 53:

```
    DeER....................................................  r1 = r1 + 0xffffffffffffffd8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 32] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 24] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 16] = r6
    .D......................................................  r5 = r7
    .DeE------------------------R...........................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r6 + 613]
    ..D=========================eER.........................  r7 = r8 + 0x1
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r7
    ..D.....................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 598, jump 22431
```

Gas simulation at offset 22241 with total cost of 26:

```
    DeER.........................  r7 = r7 & 0xff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R  r8 = u8 [r1 + 8]
    D............................  r7 = r5
    .DeeeeeeeeeeeeeeeE----------R  r0 = 600, jump 22431
```

Gas simulation at offset 22258 with total cost of 31:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......  u64 [r1 + 8] = r6
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......  r6 = u8 [r6 + 621]
    DeE------------------------R......  r7 = r7 << 0x8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......  r8 = u64 [r1 + 0]
    .D========================eER.....  r8 = r8 | r7
    .D=========================eER....  r6 = r6 + r8
    .D==========================eER...  r9 = zext16 r6
    ..D=========================eER...  r8 = r6 & 0xff
    ..D==========================eER..  r7 = r7 | r8
    ..D===========================eER.  r8 = zext16 r7
    ...D===========================eER  jump 22304 if r8 != r9
```

Gas simulation at offset 22290 with total cost of 71:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...............................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...............................  r7 = u64 [r1 + 8]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r7 = u8 [r7 + 615]
    D==================================================eER....................  r7 = r7 & 0x20
    .D==================================================eeeeeeeeeeeeeeeeeeeeER  jump 22311 if r7 == 0
```

Gas simulation at offset 22304 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 602, jump 22431
```

Gas simulation at offset 22311 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u64 [r1 + 8]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r7 + 611] = r6
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r0 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r5 = u64 [r1 + 24]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R  r6 = u64 [r1 + 16]
    .D========================eE------------------------R  r1 = r1 + 0x28
    .D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 22332 with total cost of 52:

```
    DeER...................................................  r1 = r1 + 0xffffffffffffffd8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 32] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 24] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 16] = r6
    .D.....................................................  r5 = r7
    .DeE------------------------R..........................  r7 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 8] = r7
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u8 [r7 + 613]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r7 + 620]
    ..D=================================================eER  r6 = r7 + r8
    ..D....................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 606, jump 22431
```

Gas simulation at offset 22371 with total cost of 15:

```
    DeER..............  r8 = r6 & 0xff
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 608, jump 22431
```

Gas simulation at offset 22382 with total cost of 26:

```
    DeER.........................  r7 = r7 & 0xff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeE-------------------------R  r7 = r6 + 0x1
    .DeE------------------------R  r8 = r7 & 0xff
    .D...........................  r7 = r5
    .DeeeeeeeeeeeeeeeE----------R  r0 = 610, jump 22431
```

Gas simulation at offset 22402 with total cost of 51:

```
    DeER..................................................  r7 = r7 << 0x8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u64 [r1 + 0]
    D=========================eER.........................  r7 = r7 | r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.........................  r8 = u64 [r1 + 8]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r8 + 611] = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r0 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r5 = u64 [r1 + 24]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  r6 = u64 [r1 + 16]
    ..D========================eE------------------------R  r1 = r1 + 0x28
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 22431 with total cost of 27:

```
    DeER..........................  r1 = r1 + 0xffffffffffffffa8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 80] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 72] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 64] = r6
    .D............................  r5 = r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 48] = r7
    .D=========================eER  r6 = r7 + 0x7ff
    ..DeeeeeeeeeeeeeeeE----------R  r0 = 612, jump 1045
```

Gas simulation at offset 22458 with total cost of 26:

```
    D............................  r8 = r5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r6 + 631]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 56] = 0x1
    D=========================eER  jump 22484 if r7 != 0
```

Gas simulation at offset 22471 with total cost of 45:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.....  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.....  r7 = u8 [r6 + 632]
    D=========================eeeeeeeeeeeeeeeeeeeeER  jump 22951 if r7 == 0
```

Gas simulation at offset 22480 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = 0
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 22484 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 48]
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r8
    DeeeeeeeeeeeeeeeE----------R  r0 = 614, jump 385
```

Gas simulation at offset 22498 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 616, jump 1045
```

Gas simulation at offset 22506 with total cost of 27:

```
    DeER..........................  r2 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 24] = 0
    DeE------------------------R..  r7 = r6 + 0xa1
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 0] = r7
    .DeE------------------------R.  r7 = 0xffff000000000000
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 32] = r7
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 40] = r6
    ..DeeeeeeeeeeeeeeeE----------R  jump 22592
```

Gas simulation at offset 22535 with total cost of 57:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.................  r10 = u64 [r1 + 56]
    D=========================eE--------------R.................  r8 = r10 & 0xff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.................  r9 = i16 [r6 + 629]
    .D=========================eeeE-----------R.................  r8 = r8 >u 0
    ..D===========================eE----------R.................  r8 = r8 + 0x1
    ..D============================eeE--------R.................  r10 = r8 if r7 != 0
    ..D==============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r10
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  r7 = u64 [r1 + 24]
    ...D=========================eE----------------------------R  r9 = r9 + r7
    ...D==========================eE---------------------------R  r8 = zext16 r9
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  r5 = u64 [r1 + 48]
    ....D.......................................................  r7 = r5
    ....DeeeeeeeeeeeeeeeE--------------------------------------R  r0 = 618, jump 385
```

Gas simulation at offset 22577 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r7
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeE----------R  r0 = 620, jump 1045
```

Gas simulation at offset 22588 with total cost of 2:

```
    DeER.  r2 = 0x1
    DeeER  fallthrough
```

Gas simulation at offset 22592 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r6 + 631]
    DeE---------------------------------------R  r9 = 0
    D=========================eE--------------R  jump 22621 if r7 == 0
```

Gas simulation at offset 22602 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u8 [r1 + 56]
    D=========================eE--------------R  jump 22621 if r8 != 2
```

Gas simulation at offset 22610 with total cost of 29:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER....  r8 = u8 [r6 + 593]
    D=========================eER...  r8 = r8 & 0x1
    .D=========================eeeER  r9 = r8 <u 0x1
    .DeeE--------------------------R  fallthrough
```

Gas simulation at offset 22621 with total cost of 48:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R........  r12 = u8 [r6 + 632]
    .D========================eeE-------------R........  r10 = r2 | ~r12
    .D==========================eE------------R........  r10 = r10 & 0x1
    ..D==========================eeeeeeeeeeeeeeeeeeeeER  jump 22652 if r10 == 0
```

Gas simulation at offset 22635 with total cost of 21:

```
    DeER....................  r10 = 0
    DeER....................  r11 = r2 & r12
    D=eeeeeeeeeeeeeeeeeeeeER  jump 22668 if r11 != 0
```

Gas simulation at offset 22643 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 22671 if r9 != 0
```

Gas simulation at offset 22646 with total cost of 1:

```
    DeER  jump 22535 if r10 != 0
```

Gas simulation at offset 22649 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 22799
```

Gas simulation at offset 22652 with total cost of 29:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER....  r10 = u8 [r6 + 593]
    D=========================eER...  r10 = r10 & 0x1
    .D=========================eeeER  r10 = r10 <u 0x1
    ..DeE--------------------------R  r11 = r2 & r12
    ..D=eeeeeeeeeeeeeeeeeeeeE------R  jump 22643 if r11 == 0
```

Gas simulation at offset 22668 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 22784 if r9 == 0
```

Gas simulation at offset 22671 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 627]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 48]
    D...........................  r7 = r5
    D...........................  r6 = r2
    .DeeeeeeeeeeeeeeeE---------R  r0 = 622, jump 385
```

Gas simulation at offset 22688 with total cost of 15:

```
    D.................  r8 = r5
    D.................  r5 = r7
    D.................  r7 = r8
    DeeeeeeeeeeeeeeeER  r0 = 624, jump 1045
```

Gas simulation at offset 22700 with total cost of 77:

```
    D...............................................................................  r2 = r6
    DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r6 = u64 [r1 + 40]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r7 = i16 [r6 + 135]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r8 = i16 [r6 + 133]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u8 [r6 + 631] = 0
    .D=================================================eER..........................  r7 = r7 + 0x1
    .D=================================================eER..........................  r9 = r8 << 0x30
    ..D================================================eER..........................  r8 = r8 + 0xffffffffffffffff
    ..D=================================================eER.........................  r7 = r7 | 0x8000
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.........................  r10 = u64 [r1 + 32]
    ..D=================================================eER.........................  r9 = r9 + r10
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r6 + 125] = 0x1
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r6 + 126] = s0
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 133] = r8
    ...D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 135] = r7
    ....D================================================eE------------------------R  jump 22592 if r9 != 0
```

Gas simulation at offset 22756 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r6 + 141]
    D=========================eE--------------R  jump 22857 if r7 == 0
```

Gas simulation at offset 22764 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r7 = i16 [r6 + 131]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r8 = i16 [r6 + 129]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 133] = r7
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 135] = r8
    .DeeeeeeeeeeeeeeeE----------------------------------R  jump 22592
```

Gas simulation at offset 22784 with total cost of 1:

```
    DeER  jump 22535 if r10 != 0
```

Gas simulation at offset 22788 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r9 = u32 [r6 + 593]
    D=========================eE--------------R  r9 = r9 & 0x1
    D==========================eE-------------R  jump 22874 if r9 != 0
```

Gas simulation at offset 22799 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u64 [r1 + 8]
    DeE------------------------R  jump 22809 if r7 != 0
```

Gas simulation at offset 22805 with total cost of 1:

```
    DeER  jump 22951 if r12 == 0
```

Gas simulation at offset 22809 with total cost of 57:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.................  r10 = u64 [r1 + 56]
    D=========================eE--------------R.................  r9 = r10 & 0xff
    .D=========================eeeE-----------R.................  r9 = r9 >u 0
    .D============================eE----------R.................  r9 = r9 + 0x1
    ..D============================eeE--------R.................  r10 = r9 if r7 != 0
    ..D==============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r10
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------------R  r5 = u64 [r1 + 48]
    ...D........................................................  r7 = r5
    ...D........................................................  r6 = r2
    ...DeeeeeeeeeeeeeeeE---------------------------------------R  r0 = 626, jump 385
```

Gas simulation at offset 22841 with total cost of 15:

```
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 628, jump 1045
```

Gas simulation at offset 22849 with total cost of 25:

```
    D...........................  r2 = r6
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 40]
    DeeeeeeeeeeeeeeeE----------R  jump 22592
```

Gas simulation at offset 22857 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u8 [r6 + 140]
    D=========================eE--------------R  jump 22592 if r7 == 0
```

Gas simulation at offset 22866 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 143] = 0x1
    DeeeeeeeeeeeeeeeE----------R  jump 22592
```

Gas simulation at offset 22874 with total cost of 57:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.................  r9 = u64 [r1 + 56]
    D=========================eE--------------R.................  r8 = r9 & 0xff
    .D=========================eeeE-----------R.................  r8 = r8 >u 0
    .D============================eE----------R.................  r8 = r8 + 0x1
    ..D============================eeE--------R.................  r9 = r8 if r7 != 0
    ..D==============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r9
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------------R  r5 = u64 [r1 + 24]
    ...D========================eE-----------------------------R  r7 = r5 & 0xff
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------------R  r8 = u64 [r1 + 0]
    ...D=========================eE----------------------------R  r7 = r7 + r8
    ....DeeeeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  r8 = u64 [r1 + 16]
    ....D=========================eeeeeeeeeeeeeeeeeeeeeeeeeE---R  u8 [r7 + 0] = a1
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeE----R  r7 = u64 [r1 + 48]
    ....DeeeeeeeeeeeeeeeE--------------------------------------R  r0 = 630, jump 1045
```

Gas simulation at offset 22919 with total cost of 26:

```
    DeER.........................  r2 = 0
    DeER.........................  r5 = r5 + 0x1
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 24] = r5
    D=eE------------------------R  r7 = zext16 r5
    .DeE------------------------R  r8 = 0x100
    .D=eE-----------------------R  jump 22592 if r7 != r8
```

Gas simulation at offset 22937 with total cost of 25:

```
    DeER........................  r2 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 632] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 24] = 0x100
    DeeeeeeeeeeeeeeeE----------R  jump 22592
```

Gas simulation at offset 22951 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u64 [r1 + 48]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r0 = u64 [r1 + 80]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r5 = u64 [r1 + 72]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r6 = u64 [r1 + 64]
    .D========================eER  r1 = r1 + 0x58
    .DeeeeeeeeeeeeeeeE----------R  jump 385
```

Gas simulation at offset 22969 with total cost of 53:

```
    DeER....................................................  r1 = r1 + 0xffffffffffffffd0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 40] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 32] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 24] = r6
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 16] = r9
    .D......................................................  r5 = r8
    .D......................................................  r6 = r7
    .D=========================eER..........................  r7 = r7 + 0x7ff
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 0] = r7
    ..D=========================eE------------------------R.  r7 = r7 + 0x1
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r7
    ..D.....................................................  r7 = r6
    ...DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 632, jump 1045
```

Gas simulation at offset 23008 with total cost of 51:

```
    D.....................................................  r8 = r5
    DeER..................................................  r7 = r5 >> 0xd
    D=eER.................................................  r7 = r7 << 0x2
    .DeER.................................................  r9 = 0x100a0
    .D=eER................................................  r7 = r7 + r9
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r7 = i32 [r7 + 0]
    .D===========================eER......................  r7 = r7 + r9
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r7 + 0]
```

Gas simulation at offset 23031 with total cost of 77:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r7 = u64 [r1 + 8]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r10 = u64 [r7 + 576]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r7 = u64 [r7 + 584]
    DeE-------------------------------------------------R...........................  r9 = 0x17c80
    .D=================================================eeER.........................  r9 = r7 if r10 != 0
    .D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r12 = u64 [r9 + 32]
    .DeeE--------------------------------------------------------------------------R  fallthrough
```

Gas simulation at offset 23054 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u64 [r1 + 0]
    D=========================eER.........................  r7 = r7 + 0x27f
    D==========================eeER.......................  r7 = r10 if r10 != 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--R.......................  r9 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--R.......................  r0 = u64 [r1 + 40]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--R.......................  r5 = u64 [r1 + 32]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    ..D========================eE------------------------R  r1 = r1 + 0x30
    ..DeeeeeeeeeeeeeeeeeeeeeeE---------------------------R  jump [r12 + 0]
```

Gas simulation at offset 23080 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 0]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r9 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r11 = u64 [r1 + 8]
    .DeE-----------------------R  r12 = r8 >> 0x5
    .DeE-----------------------R  r10 = 0x201
    .D=eE----------------------R  jump 23297 if r12 >=u r10
```

Gas simulation at offset 23099 with total cost of 2:

```
    D....  r7 = r6
    DeER.  r6 = r8 & 0x1f
    DeER.  r8 = 0x17
    .DeER  jump 23215 if r8 <u r6
```

Gas simulation at offset 23110 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    D....................................................  r12 = r9
    DeE---------------------------------------R..........  r6 = r6 << 0x2
    DeE---------------------------------------R..........  r9 = 0x100c0
    .DeE--------------------------------------R..........  r6 = r6 + r9
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R..........  r8 = i32 [r6 + 0]
    .D==========================eE------------R..........  r8 = r8 + r9
    .D===========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r8 + 0]
```

Gas simulation at offset 23131 with total cost of 75:

```
    DeER..........................................................................  r7 = r12 & 0xf
    DeER..........................................................................  r8 = r12 << 0x3b
    .DeER.........................................................................  r9 = r12 << 0x3a
    .DeER.........................................................................  r10 = r12 >> 0x6
    ..DeER........................................................................  r8 = r8 >> 0x3f
    ..DeER........................................................................  r9 = r9 >> 0x3f
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u8 [r11 + 0] = a1
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u8 [r11 + 1] = a2
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u8 [r11 + 3] = a0
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u8 [r11 + 10] = a2
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  u8 [r11 + 17] = a3
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 40]
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 32]
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 24]
    ....D=================================================eER.....................  r1 = r1 + 0x30
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 23177 with total cost of 77:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  r7 = u64 [r1 + 8]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r10 = u64 [r7 + 576]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r7 = u64 [r7 + 584]
    DeE-------------------------------------------------R...........................  r9 = 0x17c80
    .D=================================================eeER.........................  r9 = r7 if r10 != 0
    .D===================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r12 = u64 [r9 + 48]
    .DeeeeeeeeeeeeeeeE-------------------------------------------------------------R  jump 23054
```

Gas simulation at offset 23202 with total cost of 50:

```
    DeER.................................................  r7 = r8 & 0x7ff
    D=eER................................................  r7 = r7 + r6
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = u64 [r1 + 16]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 0] = a1
    .DeeE-----------------------------------------------R  fallthrough
```

Gas simulation at offset 23215 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 40]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 24]
    DeE------------------------R......................  r1 = r1 + 0x30
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 23229 with total cost of 51:

```
    D.....................................................  r5 = r6
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r9 = u64 [r1 + 8]
    DeE------------------------R..........................  r6 = r8 & 0x7
    .DeE-----------------------R..........................  r6 = r6 << 0x2
    .DeE-----------------------R..........................  r7 = 0x10120
    .D=eE----------------------R..........................  r6 = r6 + r7
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  r8 = i32 [r6 + 0]
    ..D==========================eER......................  r7 = r7 + r8
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--R......................  r8 = u64 [r1 + 16]
    ..D===========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r7 + 0]
```

Gas simulation at offset 23258 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r7 = u16 [r9 + 522]
    D=========================eER..........................  r7 = r7 & 0x73ff
    DeE-------------------------R..........................  r10 = r8 & 0x3
    .DeE------------------------R..........................  r10 = r10 << 0xa
    .D=========================eER.........................  r7 = r7 | r10
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r9 + 522] = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u8 [r9 + 549] = a1
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r0 = u64 [r1 + 40]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r5 = u64 [r1 + 32]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  r6 = u64 [r1 + 24]
    ..D=========================eE------------------------R  r1 = r1 + 0x30
    ...D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 23297 with total cost of 74:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r6 = u64 [r11 + 576]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..................................  r7 = u64 [r11 + 584]
    DeE---------------------------------------R..................................  r10 = 0x17c80
    .D========================eeE-------------R..................................  r10 = r7 if r6 != 0
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r12 = u64 [r10 + 64]
    ..DeE-------------------------------------------------R......................  r7 = r5 + 0x27f
    ..D=======================eeE-------------------------R......................  r7 = r6 if r6 != 0
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R......................  r0 = u64 [r1 + 40]
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R......................  r5 = u64 [r1 + 32]
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 24]
    ...D=========================eE-----------------------R......................  r1 = r1 + 0x30
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r12 + 0]
```

Gas simulation at offset 23338 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r7 = u8 [r9 + 547]
    D=========================eER...........................  r5 = r5 + r7
    D==========================eER..........................  r7 = r7 + 0x1
    .D==========================eER.........................  r10 = r5 + 0x7ff
    .D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r10 + 161] = a1
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  u8 [r9 + 547] = a0
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r0 = u64 [r1 + 40]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r5 = u64 [r1 + 32]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r6 = u64 [r1 + 24]
    ..D=========================eE-------------------------R  r1 = r1 + 0x30
    ...D========================eeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 23374 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  u8 [r9 + 550] = a1
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 40]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 24]
    .D========================eER.....................  r1 = r1 + 0x30
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 23392 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  u8 [r9 + 547] = a1
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 40]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 24]
    .D========================eER.....................  r1 = r1 + 0x30
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 23410 with total cost of 25:

```
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r0 = u64 [r1 + 40]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    .DeE-----------------------R  r1 = r1 + 0x30
    .DeeeeeeeeeeeeeeeE---------R  jump 6577
```

Gas simulation at offset 23427 with total cost of 25:

```
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r0 = u64 [r1 + 40]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    .DeE-----------------------R  r1 = r1 + 0x30
    .DeeeeeeeeeeeeeeeE---------R  jump 6729
```

Gas simulation at offset 23444 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r9 + 569]
    D=========================eER  jump 23488 if r7 == 0
```

Gas simulation at offset 23451 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r7 = u8 [r9 + 523]
    D=========================eE--------------R............  r7 = r7 << 0x8
    D==========================eE-------------R............  r7 = r7 | r8
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r9 + 520] = r7
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r9 + 522] = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u8 [r9 + 569] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r0 = u64 [r1 + 40]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r5 = u64 [r1 + 32]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  r6 = u64 [r1 + 24]
    ..D========================eE-------------------------R  r1 = r1 + 0x30
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 23488 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeE---------------------------------------R...........  r7 = r8 & 0x3f
    DeE---------------------------------------R...........  r8 = 0x1
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  u8 [r9 + 523] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  u8 [r9 + 569] = a1
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  r0 = u64 [r1 + 40]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  r5 = u64 [r1 + 32]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    ..D========================eE------------------------R  r1 = r1 + 0x30
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 23517 with total cost of 51:

```
    DeER..................................................  r7 = r12 << 0x8
    DeER..................................................  r8 = 0x1
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r11 + 628] = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r11 + 631] = a1
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r0 = u64 [r1 + 40]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r5 = u64 [r1 + 32]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    ..D========================eE------------------------R  r1 = r1 + 0x30
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 23545 with total cost of 28:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...  r7 = i32 [r11 + 592]
    DeE------------------------R...  r8 = r12 >> 0x7
    .DeE-----------------------R...  r9 = r12 << 0x39
    .D=eE----------------------R...  r9 = r9 >> 0x3f
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..  u8 [r11 + 150] = a1
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r11 + 151] = a2
    ..D=eE------------------------R  jump 23583 if r9 == 0
```

Gas simulation at offset 23569 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r9 = u8 [r11 + 142]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  u8 [r11 + 152] = 0
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r11 + 623] = a2
    .DeeE-----------------------------------------------R  fallthrough
```

Gas simulation at offset 23583 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeE---------------------------------------R..........  r7 = r7 & 0x1
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  u8 [r11 + 146] = a1
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R..........  u8 [r11 + 147] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R..........  r0 = u64 [r1 + 40]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R..........  r5 = u64 [r1 + 32]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    .D=========================eE-----------------------R  r1 = r1 + 0x30
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 23609 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r11 + 61]
    D=========================eER  jump 23633 if r7 == 0
```

Gas simulation at offset 23615 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeE---------------------------------------R............  r7 = r12 >> 0x3
    DeE---------------------------------------R............  r8 = 0x17290
    .DeE--------------------------------------R............  r7 = r7 + r8
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R............  r7 = u8 [r7 + 0]
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r11 + 62] = a0
    .DeeE-------------------------------------------------R  fallthrough
```

Gas simulation at offset 23633 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r7 = 0x1
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  u8 [r11 + 50] = a0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 40]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r5 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 24]
    .D========================eE--------------R.......  r1 = r1 + 0x30
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 23654 with total cost of 26:

```
    DeER.........................  r7 = r5 + 0x71
    D............................  r8 = r12
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r0 = u64 [r1 + 40]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    .DeE------------------------R  r1 = r1 + 0x30
    .DeeeeeeeeeeeeeeeE----------R  jump 207
```

Gas simulation at offset 23674 with total cost of 53:

```
    DeER....................................................  r7 = r12 & 0xf
    DeER....................................................  r8 = 0x172b0
    D=eER...................................................  r7 = r7 << 0x1
    .D=eER..................................................  r7 = r7 + r8
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = i16 [r7 + 0]
    .DeE--------------------------R.........................  r8 = r12 >> 0x7
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r11 + 54] = r7
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u8 [r11 + 63] = a1
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r0 = u64 [r1 + 40]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  r5 = u64 [r1 + 32]
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  r6 = u64 [r1 + 24]
    ...D========================eE-------------------------R  r1 = r1 + 0x30
    ...D========================eeeeeeeeeeeeeeeeeeeeeeE----R  jump [r0 + 0]
```

Gas simulation at offset 23713 with total cost of 25:

```
    D...........................  r8 = r12
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r0 = u64 [r1 + 40]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    .DeE-----------------------R  r1 = r1 + 0x30
    .DeeeeeeeeeeeeeeeE---------R  jump 263
```

Gas simulation at offset 23730 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  u8 [r11 + 6] = a5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 40]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 24]
    .D========================eER.....................  r1 = r1 + 0x30
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 23747 with total cost of 78:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r8 = u8 [r11 + 43]
    DeE------------------------R.....................................................  r9 = r12 >> 0x7
    .DeE-----------------------R.....................................................  r10 = r12 << 0x3c
    .D=eE----------------------R.....................................................  r10 = r10 >> 0x3f
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  u8 [r11 + 37] = a2
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  u8 [r11 + 38] = 0x1
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u8 [r11 + 39] = a3
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER............................  u8 [r11 + 42] = a1
    ...D=======================eE-----------------------R............................  r7 = r12 << 0x39
    ...D========================eE----------------------R............................  r8 = r12 & 0x7
    ....D=======================eE----------------------R............................  r7 = r7 >> 0x3d
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r11 + 44] = a0
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r11 + 45] = a1
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r0 = u64 [r1 + 40]
    .....D=============================================eeeeeeeeeeeeeeeeeeeeeeeeeER...  r5 = u64 [r1 + 32]
    .....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    .....D================================================eE------------------------R  r1 = r1 + 0x30
    .....D================================================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 23801 with total cost of 74:

```
    DeER.........................................................................  r7 = r12 << 0x3a
    DeER.........................................................................  r8 = r12 & 0xf
    .DeER........................................................................  r9 = r12 << 0x3b
    .DeER........................................................................  r7 = r7 >> 0x3f
    .D=eER.......................................................................  r9 = r9 >> 0x3f
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u8 [r11 + 48] = a2
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-R..............................................  u8 [r11 + 49] = a0
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-R..............................................  u8 [r11 + 51] = a1
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-R..............................................  u8 [r11 + 60] = a0
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 40]
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 32]
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 24]
    ...D=========================eE-----------------------R......................  r1 = r1 + 0x30
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 23842 with total cost of 78:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r8 = u8 [r11 + 19]
    DeE------------------------R.....................................................  r9 = r12 >> 0x7
    .DeE-----------------------R.....................................................  r10 = r12 << 0x3c
    .D=eE----------------------R.....................................................  r10 = r10 >> 0x3f
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  u8 [r11 + 13] = a2
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  u8 [r11 + 14] = 0x1
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u8 [r11 + 15] = a3
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER............................  u8 [r11 + 18] = a1
    ...D=======================eE-----------------------R............................  r7 = r12 << 0x39
    ...D========================eE----------------------R............................  r8 = r12 & 0x7
    ....D=======================eE----------------------R............................  r7 = r7 >> 0x3d
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r11 + 20] = a0
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r11 + 21] = a1
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r0 = u64 [r1 + 40]
    .....D=============================================eeeeeeeeeeeeeeeeeeeeeeeeeER...  r5 = u64 [r1 + 32]
    .....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    .....D================================================eE------------------------R  r1 = r1 + 0x30
    .....D================================================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 23896 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  u8 [r11 + 30] = a5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 40]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 24]
    .D========================eER.....................  r1 = r1 + 0x30
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 23913 with total cost of 26:

```
    DeER.........................  r7 = r5 + 0x19
    D............................  r8 = r12
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r0 = u64 [r1 + 40]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    .DeE------------------------R  r1 = r1 + 0x30
    .DeeeeeeeeeeeeeeeE----------R  jump 0
```

Gas simulation at offset 23933 with total cost of 55:

```
    DeER......................................................  r7 = r12 & 0xf
    DeER......................................................  r8 = 0x17270
    D=eER.....................................................  r7 = r7 << 0x1
    .D=eER....................................................  r7 = r7 + r8
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r7 = u16 [r7 + 0]
    .DeE--------------------------R...........................  r8 = r12 >> 0x7
    ..DeE-------------------------R...........................  r9 = r12 << 0x39
    ..D=eE------------------------R...........................  r9 = r9 >> 0x3f
    ..D==========================eER..........................  r7 = r7 >> 0x1
    ...D==========================eER.........................  r7 = r7 + 0xffffffffffffffff
    ...D===========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r11 + 126] = r7
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R  u8 [r11 + 139] = a1
    ...D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u8 [r11 + 140] = a2
    ....DeE--------------------------------------------------R  jump 23215 if r8 != 0
```

Gas simulation at offset 23979 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  u8 [r11 + 142] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 40]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 24]
    .D========================eE--------------R.......  r1 = r1 + 0x30
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 23998 with total cost of 47:

```
    DeER..............................................  r7 = r12 & 0x7f
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  u8 [r11 + 145] = a0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................  r0 = u64 [r1 + 40]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r5 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r6 = u64 [r1 + 24]
    .D========================eER.....................  r1 = r1 + 0x30
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 24019 with total cost of 26:

```
    D............................  r7 = r11
    D............................  r8 = r12
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r0 = u64 [r1 + 40]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r5 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    .DeE------------------------R  r1 = r1 + 0x30
    .DeeeeeeeeeeeeeeeE----------R  jump 0
```

Gas simulation at offset 24038 with total cost of 75:

```
    DeER..........................................................................  r7 = r12 & 0xf
    DeER..........................................................................  r8 = r12 << 0x3b
    .DeER.........................................................................  r9 = r12 << 0x3a
    .DeER.........................................................................  r10 = r12 >> 0x6
    ..DeER........................................................................  r8 = r8 >> 0x3f
    ..DeER........................................................................  r9 = r9 >> 0x3f
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u8 [r11 + 24] = a1
    ..D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u8 [r11 + 25] = a2
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u8 [r11 + 27] = a0
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u8 [r11 + 34] = a2
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  u8 [r11 + 41] = a3
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 40]
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 32]
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 24]
    ....D=================================================eER.....................  r1 = r1 + 0x30
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 24085 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  u8 [r11 + 112] = a5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 40]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 24]
    .D========================eER.....................  r1 = r1 + 0x30
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 24102 with total cost of 51:

```
    DeER..................................................  r7 = r12 >> 0x7
    DeER..................................................  r8 = r12 & 0x7f
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r11 + 117] = a1
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r11 + 119] = a0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r0 = u64 [r1 + 40]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r5 = u64 [r1 + 32]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    ..D========================eE------------------------R  r1 = r1 + 0x30
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 24128 with total cost of 48:

```
    DeER...............................................  r7 = r12 << 0x4
    D=eER..............................................  r7 = r7 + 0x1
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  u16 [r11 + 130] = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................  r0 = u64 [r1 + 40]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................  r5 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................  r6 = u64 [r1 + 24]
    .D=========================eER.....................  r1 = r1 + 0x30
    ..D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 24152 with total cost of 48:

```
    DeER...............................................  r7 = r12 | 0x300
    D=eER..............................................  r7 = r7 << 0x6
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  u16 [r11 + 128] = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................  r0 = u64 [r1 + 40]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................  r5 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................  r6 = u64 [r1 + 24]
    .D=========================eER.....................  r1 = r1 + 0x30
    ..D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 24177 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r11 + 643]
    D=========================eER  jump 24248 if r7 == 0
```

Gas simulation at offset 24184 with total cost of 59:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...................  r7 = u8 [r11 + 638]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...................  r8 = u8 [r11 + 639]
    .D========================eeeE------------R...................  r9 = r7 <u 0xc0
    ..D=======================eE--------------R...................  r10 = r7 & 0x3f
    ..D==========================eeE----------R...................  r10 = r7 if r9 != 0
    ...D======================eeeE------------R...................  r7 = r8 <u 0xc0
    ....D=====================eE--------------R...................  r9 = r8 & 0x3f
    ....D========================eeE----------R...................  r9 = r8 if r7 != 0
    .....D=========================eE---------R...................  r7 = r10 & 0x30
    .....D=========================eE---------R...................  r8 = r10 & 0xcf
    ......D=========================eE--------R...................  r7 = r7 + 0xffffffffffffffd0
    ......D==========================eeE------R...................  r8 = r10 if r7 != 0
    .......D=======================eE---------R...................  r7 = r9 & 0x30
    .......D=======================eE---------R...................  r10 = r9 & 0xcf
    ........D=======================eE--------R...................  r7 = r7 + 0xffffffffffffffd0
    ........D========================eeE------R...................  r10 = r9 if r7 != 0
    ........D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r11 + 640] = a1
    .........D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r11 + 641] = a3
    .........DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 24248 with total cost of 47:

```
    DeER..............................................  r7 = r12 & 0x1
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  u8 [r11 + 643] = a0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................  r0 = u64 [r1 + 40]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r5 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r6 = u64 [r1 + 24]
    .D========================eER.....................  r1 = r1 + 0x30
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 24269 with total cost of 27:

```
    DeER..........................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 0] = r5
    .DeE------------------------R.  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r5 + 617]
    .DeeeeeeeeeeeeeeeE-----------R  r0 = 706, jump 22431
```

Gas simulation at offset 24291 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r5 + 613]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r9 = i16 [r5 + 617]
    DeE------------------------R..........................  r7 = r7 << 0x8
    D=========================eER.........................  r7 = r7 | r8
    .D========================eER.........................  r9 = r9 + 0x1
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 611] = r7
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r5 + 617] = r9
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r0 = u64 [r1 + 8]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R  r5 = u64 [r1 + 0]
    ..D========================eE------------------------R  r1 = r1 + 0x10
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 24326 with total cost of 80:

```
    DeER...............................................................................  r8 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................  r9 = u8 [r8 + 615]
    D==========================eER.....................................................  r9 = r9 << 0x3b
    .D==========================eER....................................................  r9 = r9 >> 0x3e
    .D===========================eER...................................................  r7 = r7 + r9
    .D============================eER..................................................  r7 = r7 + 0x7ff
    .D=============================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u8 [r7 + 619]
    ..D=====================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 613] = a0
    ..DeeeeeeeeeeeeeeeeeeeeeeE--------------------------------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 24357 with total cost of 60:

```
    DeER...........................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..................................  r8 = u8 [r7 + 619]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..................................  r9 = u8 [r7 + 623]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..................................  r10 = u8 [r7 + 613]
    .D=========================eER.................................  r11 = r9 & 0x1
    .D=========================eER.................................  r12 = r10 + r8
    ..D========================eER.................................  r2 = r9 & 0x3c
    ..D========================eER.................................  r10 = r10 ^ r8
    ..D=========================eER................................  r11 = r11 + r12
    ...D========================eeeER..............................  r3 = r10 <u 0x80
    ....D========================eE-R..............................  r12 = r11 & 0xff
    ....D========================eE-R..............................  r9 = r11 & 0x80
    .....D=======================eeeER.............................  r10 = r11 <u 0x100
    .....D========================eE-R.............................  r8 = r8 ^ r11
    ......D=======================eeeER............................  r12 = r12 <u 0x1
    ......D=========================eER............................  r10 = r10 ^ 0x1
    .......D=======================eE-R............................  r8 = r8 << 0x38
    .......D=======================eE-R............................  r9 = r9 | r2
    .......D=========================eER...........................  r12 = r12 << 0x1
    .......D========================eE-R...........................  r8 = r8 >> 0x3f
    ........D========================eER...........................  r9 = r9 | r10
    ........D========================eER...........................  r8 = r3 & r8
    ........D=========================eER..........................  r9 = r9 | r12
    ........D=========================eER..........................  r8 = r8 << 0x6
    .........D=========================eER.........................  r8 = r8 | r9
    .........D======================eeeeeeeeeeeeeeeeeeeeeeeeeER....  u8 [r7 + 619] = a4
    .........D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    .........DeE--------------------------------------------------R  r7 = 0
    ..........DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 24452 with total cost of 57:

```
    DeER........................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r8 = u8 [r7 + 613]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r9 = u8 [r7 + 619]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r10 = u8 [r7 + 623]
    .D=========================eER..............................  r8 = r8 & r9
    .D=========================eER..............................  r9 = r10 & 0x7d
    ..D=========================eER.............................  r10 = r8 & 0x80
    ..D==========================eER............................  r9 = r9 | r10
    ...D========================eeeER...........................  r10 = r8 <u 0x1
    ...D===========================eER..........................  r10 = r10 << 0x1
    ....D===========================eER.........................  r9 = r9 | r10
    ....D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER.....  u8 [r7 + 619] = a1
    ....D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a2
    ....DeE----------------------------------------------------R  r7 = 0
    .....DeeeeeeeeeeeeeeeeeeeeeeE------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 24502 with total cost of 52:

```
    DeER...................................................  r1 = r1 + 0xffffffffffffffd8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 32] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 24] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 16] = r6
    .DeE------------------------R..........................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = u8 [r6 + 615]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r10 = u8 [r6 + 613]
    ..D=========================eE-----------------------R.  r9 = r8 & 0x7
    ..DeE------------------------------------------------R.  r3 = 0x7
    ...D================================================eER  r5 = r10 << 0x1
    ...D=========================eE-----------------------R  jump 24571 if r9 == r3
```

Gas simulation at offset 24538 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u16 [r6 + 611]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 8] = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u64 [r1 + 8]
    D............................  r9 = r10
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r10
    .DeeeeeeeeeeeeeeeE----------R  r0 = 716, jump 22969
```

Gas simulation at offset 24558 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r10 = u64 [r1 + 0]
    DeE------------------------R  r3 = 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u8 [r6 + 615]
    .DeeE----------------------R  fallthrough
```

Gas simulation at offset 24571 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r2 = u8 [r6 + 623]
    DeE---------------------------------------R.............  r10 = r10 >> 0x7
    .DeE--------------------------------------R.............  r11 = r5 & 0x80
    .DeE--------------------------------------R.............  r9 = r5 & 0xff
    ..DeeeE-----------------------------------R.............  r12 = r9 <u 0x1
    ..DeE-------------------------------------R.............  r11 = r11 | r10
    ...D==eE----------------------------------R.............  r12 = r12 << 0x1
    ...D======================eE--------------R.............  r10 = r2 & 0x7c
    ...D=======================eE-------------R.............  r10 = r10 | r11
    ....D=======================eE------------R.............  r10 = r10 | r12
    ....DeE-----------------------------------R.............  r8 = r8 & 0x7
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 623] = a3
    ....D=eE-----------------------------------------------R  jump 24637 if r8 != 7
```

Gas simulation at offset 24616 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  u8 [r6 + 619] = s0
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r5 = u64 [r1 + 24]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 16]
    .D========================eE--------------R.......  r1 = r1 + 0x28
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 24637 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 611]
    DeeeeeeeeeeeeeeeE----------R  r0 = 718, jump 22969
```

Gas simulation at offset 24647 with total cost of 47:

```
    DeER..............................................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 16]
    .DeE-----------------------R......................  r1 = r1 + 0x28
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 24663 with total cost of 59:

```
    DeER..........................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.................................  r8 = u8 [r7 + 619]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.................................  r9 = u8 [r7 + 620]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.................................  r10 = u8 [r7 + 623]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.................................  r11 = u8 [r7 + 613]
    .D=========================eER................................  r8 = r8 & r9
    .D=========================eER................................  r9 = r10 & 0x7c
    ..D=========================eER...............................  r8 = r8 - r11
    ..D==========================eeeER............................  r10 = r8 <u 0x100
    ...D=========================eE--R............................  r11 = r8 & 0xff
    ...D=========================eE--R............................  r12 = r8 & 0x80
    ....D=========================eeeER...........................  r11 = r11 <u 0x1
    ....D===========================eER...........................  r9 = r9 | r10
    .....D===========================eER..........................  r11 = r11 << 0x1
    .....D===========================eER..........................  r9 = r9 | r12
    .....D============================eER.........................  r9 = r9 | r11
    .....D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER......  u8 [r7 + 620] = a1
    ......D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a2
    ......DeE----------------------------------------------------R  r7 = 0
    ......DeeeeeeeeeeeeeeeeeeeeeeE-------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 24731 with total cost of 57:

```
    DeER........................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r8 = u8 [r7 + 613]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r9 = u8 [r7 + 619]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r10 = u8 [r7 + 623]
    .D=========================eER..............................  r9 = r9 & r8
    .D=========================eER..............................  r10 = r10 & 0x3d
    .D=========================eER..............................  r8 = r8 & 0xc0
    ..D=========================eeeER...........................  r9 = r9 <u 0x1
    ..D============================eER..........................  r9 = r9 << 0x1
    ...D========================eE---R..........................  r8 = r8 | r10
    ...D============================eER.........................  r8 = r8 | r9
    ...D=============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    ...DeE-----------------------------------------------------R  r7 = 0
    ....DeeeeeeeeeeeeeeeeeeeeeeE-------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 24777 with total cost of 53:

```
    DeER....................................................  r1 = r1 + 0xffffffffffffffd8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 32] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 24] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 16] = r6
    .D......................................................  r5 = r7
    .DeE------------------------R...........................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r6 + 623]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r6 + 622]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..  r9 = u8 [r6 + 618]
    ..D=========================eE-----------------------R..  r7 = r7 | 0x10
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 623] = a0
    ...D================================================eE-R  r8 = r8 | 0x100
    ...D....................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 726, jump 22969
```

Gas simulation at offset 24826 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r6 + 622]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r9 = u8 [r6 + 617]
    D=========================eER.........................  r7 = r7 + 0xffffffffffffffff
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 622] = a0
    .D=========================eE------------------------R  r7 = r7 & 0xff
    .D==========================eE-----------------------R  r8 = r7 | 0x100
    .D....................................................  r7 = r5
    ..DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 728, jump 22969
```

Gas simulation at offset 24857 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r7 = u8 [r6 + 622]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r9 = u8 [r6 + 623]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r11 = u8 [r6 + 625]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r11
    .DeE------------------------------------------------R..  r10 = 0xfffb
    .D========================eeE-----------------------R..  r10 = 0xffff if r11 == 0
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r10
    ..D=======================eE--------------------------R  r7 = r7 + 0xffffffffffffffff
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  u8 [r6 + 622] = a0
    ..D========================eE-------------------------R  r7 = r7 & 0xff
    ...D========================eE------------------------R  r8 = r7 | 0x100
    ...D...................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 730, jump 22969
```

Gas simulation at offset 24907 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r6 + 622]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r6 + 623]
    D=========================eER.........................  r7 = r7 + 0xffffffffffffffff
    D=========================eER.........................  r8 = r8 | 0x4
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 622] = a0
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 623] = a1
    .DeE-------------------------------------------------R  r8 = 0xfffa
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r9 = u64 [r1 + 0]
    ..D========================eeE-----------------------R  r8 = 0xfffe if r9 == 0
    ..D...................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE---------------------------------R  r0 = 732, jump 22431
```

Gas simulation at offset 24949 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 617] = a0
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeE----------R  r0 = 734, jump 22431
```

Gas simulation at offset 24964 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  u8 [r6 + 618] = a0
    DeE------------------------R......................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 24]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r6 = u64 [r1 + 16]
    .D========================eER.....................  r1 = r1 + 0x28
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 24984 with total cost of 57:

```
    DeER........................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r8 = u8 [r7 + 613]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r9 = u8 [r7 + 619]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r10 = u8 [r7 + 623]
    .D=========================eER..............................  r8 = r8 ^ r9
    .D=========================eER..............................  r9 = r10 & 0x7d
    ..D=========================eER.............................  r10 = r8 & 0x80
    ..D==========================eER............................  r9 = r9 | r10
    ...D========================eeeER...........................  r10 = r8 <u 0x1
    ...D===========================eER..........................  r10 = r10 << 0x1
    ....D===========================eER.........................  r9 = r9 | r10
    ....D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER.....  u8 [r7 + 619] = a1
    ....D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a2
    ....DeE----------------------------------------------------R  r7 = 0
    .....DeeeeeeeeeeeeeeeeeeeeeeE------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 25034 with total cost of 76:

```
    DeER...........................................................................  r1 = r1 + 0xffffffffffffffd8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r1 + 32] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r1 + 24] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r1 + 16] = r6
    .D.............................................................................  r5 = r7
    .DeE------------------------R..................................................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................  r7 = u8 [r6 + 622]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = u8 [r6 + 613]
    ..D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r8
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u16 [r6 + 617]
    ..D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r8
    ...D========================eE------------------------------------------------R  r8 = r7 | 0x100
    ...D...........................................................................  r7 = r5
    ...DeeeeeeeeeeeeeeeE----------------------------------------------------------R  r0 = 740, jump 22431
```

Gas simulation at offset 25081 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r6 + 622]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r9 = u8 [r6 + 618]
    D=========================eER  r8 = r7 | 0x100
    .D...........................  r7 = r5
    .DeeeeeeeeeeeeeeeE----------R  r0 = 742, jump 22969
```

Gas simulation at offset 25101 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r6 + 622]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r9 = u8 [r6 + 617]
    D=========================eER.........................  r7 = r7 + 0xffffffffffffffff
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 622] = a0
    .D=========================eE------------------------R  r7 = r7 & 0xff
    .D==========================eE-----------------------R  r8 = r7 | 0x100
    .D....................................................  r7 = r5
    ..DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 744, jump 22969
```

Gas simulation at offset 25132 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r6 + 622]
    D=========================eER.........................  r7 = r7 + 0xffffffffffffffff
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 622] = a0
    D.....................................................  r7 = r5
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u64 [r1 + 0]
    .DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 746, jump 22431
```

Gas simulation at offset 25153 with total cost of 51:

```
    DeER..................................................  r7 = r7 << 0x8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u64 [r1 + 8]
    D=========================eER.........................  r7 = r7 | r8
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 617] = r7
    .DeE-------------------------------------------------R  r7 = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r0 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r5 = u64 [r1 + 24]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r6 = u64 [r1 + 16]
    ..D========================eE------------------------R  r1 = r1 + 0x28
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 25182 with total cost of 51:

```
    DeER..................................................  r1 = r1 + 0xffffffffffffffe0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 24] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 16] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 8] = r6
    .DeE------------------------R.........................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER........................  r8 = u8 [r6 + 615]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u8 [r6 + 613]
    ..D=========================eE-----------------------R  r9 = r8 & 0x7
    ..DeE------------------------------------------------R  r11 = 0x7
    ..D==========================eE----------------------R  jump 25241 if r9 == r11
```

Gas simulation at offset 25215 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 611]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    D...........................  r9 = r5
    .DeeeeeeeeeeeeeeeE---------R  r0 = 750, jump 22969
```

Gas simulation at offset 25231 with total cost of 25:

```
    DeER........................  r11 = 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 0]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u8 [r6 + 615]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 25241 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.............  unlikely
    DeE---------------------------------------R.............  r9 = r5 >> 0x1
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.............  r10 = u8 [r6 + 623]
    .DeE--------------------------------------R.............  r2 = r5 & 0x1
    ..DeeeE-----------------------------------R.............  r12 = r5 <u 0x2
    ..D===eE----------------------------------R.............  r12 = r12 << 0x1
    ...D======================eE--------------R.............  r10 = r10 & 0x7c
    ...D=======================eE-------------R.............  r10 = r2 | r10
    ...D========================eE------------R.............  r10 = r10 | r12
    ...DeE------------------------------------R.............  r8 = r8 & 0x7
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 623] = a3
    ....DeE------------------------------------------------R  jump 25299 if r8 != 7
```

Gas simulation at offset 25278 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  u8 [r6 + 619] = a2
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 24]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r5 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 8]
    .D========================eE--------------R.......  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 25299 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 611]
    DeeeeeeeeeeeeeeeE----------R  r0 = 752, jump 22969
```

Gas simulation at offset 25309 with total cost of 47:

```
    DeER..............................................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 8]
    .DeE-----------------------R......................  r1 = r1 + 0x20
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 25325 with total cost of 22:

```
    DeER.....................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 25329 with total cost of 57:

```
    DeER........................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r8 = u8 [r7 + 613]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r9 = u8 [r7 + 619]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...............................  r10 = u8 [r7 + 623]
    .D=========================eER..............................  r8 = r8 | r9
    .D=========================eER..............................  r9 = r10 & 0x7d
    ..D=========================eER.............................  r10 = r8 & 0x80
    ..D==========================eER............................  r9 = r9 | r10
    ...D========================eeeER...........................  r10 = r8 <u 0x1
    ...D===========================eER..........................  r10 = r10 << 0x1
    ....D===========================eER.........................  r9 = r9 | r10
    ....D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER.....  u8 [r7 + 619] = a1
    ....D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a2
    ....DeE----------------------------------------------------R  r7 = 0
    .....DeeeeeeeeeeeeeeeeeeeeeeE------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 25379 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r5
    .DeE------------------------R..  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u8 [r5 + 622]
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r9 = u8 [r5 + 619]
    ..D=========================eER  r8 = r8 | 0x100
    ..DeeeeeeeeeeeeeeeE-----------R  r0 = 760, jump 22969
```

Gas simulation at offset 25409 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r5 + 622]
    D=========================eER.........................  r7 = r7 + 0xffffffffffffffff
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 622] = a0
    DeE--------------------------------------------------R  r7 = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r0 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r5 = u64 [r1 + 0]
    .DeE-------------------------------------------------R  r1 = r1 + 0x10
    .D=========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 25432 with total cost of 53:

```
    DeER....................................................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 0] = r5
    .DeE------------------------R...........................  r5 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r5 + 623]
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r10 = u8 [r5 + 622]
    ..D=========================eER.........................  r9 = r8 | 0x10
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 623] = a2
    ...D========================eE-------------------------R  r8 = r10 | 0x100
    ...DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 764, jump 22969
```

Gas simulation at offset 25469 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r5 + 622]
    D=========================eER.........................  r7 = r7 + 0xffffffffffffffff
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r5 + 622] = a0
    DeE--------------------------------------------------R  r7 = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r0 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r5 = u64 [r1 + 0]
    .DeE-------------------------------------------------R  r1 = r1 + 0x10
    .D=========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 25492 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r6
    .D.............................  r5 = r7
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r6 + 622]
    ..D=========================eER  r8 = r7 | 0x100
    ..D............................  r7 = r5
    ..DeeeeeeeeeeeeeeeE-----------R  r0 = 768, jump 22431
```

Gas simulation at offset 25525 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r6 + 622]
    D=========================eER.........................  r7 = r7 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 622] = a0
    D==========================eE------------------------R  r7 = r7 & 0xff
    .D==========================eE-----------------------R  r8 = r7 | 0x100
    .D....................................................  r7 = r5
    .DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 770, jump 22431
```

Gas simulation at offset 25552 with total cost of 53:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER............................  r8 = u8 [r6 + 623]
    DeE------------------------R............................  r9 = r7 & 0x80
    D=========================eER...........................  r8 = r8 & 0x7d
    .D=========================eER..........................  r8 = r8 | r9
    .DeE-------------------------R..........................  r9 = r7 & 0xff
    ..DeeeE----------------------R..........................  r9 = r9 <u 0x1
    ..D===eE---------------------R..........................  r9 = r9 << 0x1
    ...D========================eER.........................  r8 = r8 | r9
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r6 + 619] = a0
    ...D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 623] = a1
    ...DeE-------------------------------------------------R  r7 = 0
    ....DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R  r0 = u64 [r1 + 16]
    ....D==eeeeeeeeeeeeeeeeeeeeeeeeeE----------------------R  r5 = u64 [r1 + 8]
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ....D=========================eE-----------------------R  r1 = r1 + 0x18
    .....D========================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 25602 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r6
    .D.............................  r5 = r7
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r6 + 622]
    ..D=========================eER  r8 = r7 | 0x100
    ..D............................  r7 = r5
    ..DeeeeeeeeeeeeeeeE-----------R  r0 = 774, jump 22431
```

Gas simulation at offset 25635 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r6 + 622]
    D=========================eER.........................  r7 = r7 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 622] = a0
    D==========================eE------------------------R  r7 = r7 & 0xff
    .D==========================eE-----------------------R  r8 = r7 | 0x100
    .D....................................................  r7 = r5
    .DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 776, jump 22431
```

Gas simulation at offset 25662 with total cost of 47:

```
    DeER..............................................  r7 = r7 | 0x20
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  u8 [r6 + 623] = a0
    DeE-------------------------R.....................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................  r0 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r6 = u64 [r1 + 0]
    .D========================eER.....................  r1 = r1 + 0x18
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 25684 with total cost of 53:

```
    DeER....................................................  r1 = r1 + 0xffffffffffffffd0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 40] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 32] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 24] = r6
    .DeE------------------------R...........................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r9 = u8 [r6 + 623]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u8 [r6 + 615]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..  r5 = u8 [r6 + 613]
    ..D=========================eE-----------------------R..  r11 = r9 & 0x1
    ...D================================================eER.  r10 = r8 & 0x7
    ...DeE------------------------------------------------R.  r2 = 0x7
    ....D===============================================eER.  r12 = r5 << 0x1
    ....D================================================eER  jump 25771 if r10 == r2
```

Gas simulation at offset 25727 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r8 = u16 [r6 + 611]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  u64 [r1 + 16] = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r7 = u64 [r1 + 16]
    .D...................................................  r9 = r5
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R..........  u64 [r1 + 8] = r12
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r11
    .DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 780, jump 22969
```

Gas simulation at offset 25751 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r11 = u64 [r1 + 0]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r12 = u64 [r1 + 8]
    DeE------------------------R.........................  r2 = 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER........................  r8 = u8 [r6 + 615]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r9 = u8 [r6 + 623]
    .DeeE-----------------------------------------------R  fallthrough
```

Gas simulation at offset 25771 with total cost of 32:

```
    DeER...............................  r10 = r11 | r12
    DeER...............................  r11 = r9 & 0x7c
    .DeER..............................  r5 = r5 >> 0x7
    .DeER..............................  r12 = r12 & 0x80
    .DeER..............................  r9 = r10 & 0xff
    ..DeER.............................  r12 = r12 | r5
    ..DeeeER...........................  r5 = r9 <u 0x1
    ...DeE-R...........................  r11 = r11 | r12
    ...D==eER..........................  r5 = r5 << 0x1
    ...D===eER.........................  r11 = r11 | r5
    ...DeE---R.........................  r8 = r8 & 0x7
    ....D===eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 623] = a4
    ....DeE---------------------------R  jump 25835 if r8 != 7
```

Gas simulation at offset 25814 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  u8 [r6 + 619] = a3
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 40]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r5 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 24]
    .D========================eE--------------R.......  r1 = r1 + 0x30
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 25835 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 611]
    DeeeeeeeeeeeeeeeE----------R  r0 = 782, jump 22969
```

Gas simulation at offset 25845 with total cost of 47:

```
    DeER..............................................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 40]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 24]
    .DeE-----------------------R......................  r1 = r1 + 0x30
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 25861 with total cost of 72:

```
    DeER.......................................................................  r1 = r1 + 0xffffffffffffffd8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u64 [r1 + 32] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u64 [r1 + 24] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u64 [r1 + 16] = r6
    .DeE------------------------R..............................................  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................  r5 = u8 [r6 + 613]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r9 = u8 [r6 + 623]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r8 = u8 [r6 + 615]
    ..D=========================eE-----------------------R.....................  r10 = r5 >> 0x1
    ...D================================================eER....................  r11 = r9 << 0x7
    ...D================================================eER....................  r12 = r8 & 0x7
    ....DeE-----------------------------------------------R....................  r3 = 0x7
    ....D================================================eER...................  r11 = r11 | r10
    ....D================================================eeeeeeeeeeeeeeeeeeeeER  jump 25944 if r12 == r3
```

Gas simulation at offset 25907 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u16 [r6 + 611]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 8] = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u64 [r1 + 8]
    D............................  r9 = r5
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r11
    .DeeeeeeeeeeeeeeeE----------R  r0 = 786, jump 22969
```

Gas simulation at offset 25927 with total cost of 26:

```
    DeER.........................  r3 = 0x7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r11 = u64 [r1 + 0]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u8 [r6 + 615]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r9 = u8 [r6 + 623]
    .DeeE-----------------------R  fallthrough
```

Gas simulation at offset 25944 with total cost of 32:

```
    DeER...............................  r2 = r9 & 0x7c
    DeER...............................  r5 = r5 & 0x1
    .DeER..............................  r10 = r11 & 0x80
    .DeER..............................  r9 = r11 & 0xff
    ..DeeeER...........................  r12 = r9 <u 0x1
    ..DeE--R...........................  r10 = r10 | r5
    ...D==eER..........................  r12 = r12 << 0x1
    ...DeE--R..........................  r10 = r10 | r2
    ...D===eER.........................  r10 = r10 | r12
    ...DeE---R.........................  r8 = r8 & 0x7
    ....D===eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 623] = a3
    ....DeE---------------------------R  jump 26005 if r8 != 7
```

Gas simulation at offset 25984 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  u8 [r6 + 619] = a4
    DeE---------------------------------------R.......  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 32]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r5 = u64 [r1 + 24]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 16]
    .D========================eE--------------R.......  r1 = r1 + 0x28
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 26005 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 611]
    DeeeeeeeeeeeeeeeE----------R  r0 = 788, jump 22969
```

Gas simulation at offset 26015 with total cost of 47:

```
    DeER..............................................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r6 = u64 [r1 + 16]
    .DeE-----------------------R......................  r1 = r1 + 0x28
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 26031 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r6
    .D.............................  r5 = r7
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r6 + 622]
    ..D=========================eER  r8 = r7 | 0x100
    ..D............................  r7 = r5
    ..DeeeeeeeeeeeeeeeE-----------R  r0 = 792, jump 22431
```

Gas simulation at offset 26064 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r6 + 622]
    D=========================eER.........................  r7 = r7 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 622] = a0
    D==========================eE------------------------R  r7 = r7 & 0xff
    .D==========================eE-----------------------R  r8 = r7 | 0x100
    .D....................................................  r7 = r5
    .DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 794, jump 22431
```

Gas simulation at offset 26091 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r6 + 622]
    DeE------------------------R..........................  r7 = r7 | 0x20
    D=========================eER.........................  r8 = r8 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 622] = a1
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u8 [r6 + 623] = a0
    .D=========================eE------------------------R  r7 = r8 & 0xff
    ..D=========================eE-----------------------R  r8 = r7 | 0x100
    ..D...................................................  r7 = r5
    ..DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 796, jump 22431
```

Gas simulation at offset 26125 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r6 + 622]
    D=========================eER.........................  r8 = r8 + 0x1
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.........................  u8 [r6 + 617] = a0
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 622] = a1
    .D=========================eE------------------------R  r7 = r8 & 0xff
    .D==========================eE-----------------------R  r8 = r7 | 0x100
    ..D...................................................  r7 = r5
    ..DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 798, jump 22431
```

Gas simulation at offset 26156 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  u8 [r6 + 618] = a0
    DeE------------------------R......................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r6 = u64 [r1 + 0]
    .D========================eER.....................  r1 = r1 + 0x18
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 26175 with total cost of 28:

```
    DeER...........................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 0] = r6
    .D.............................  r5 = r7
    .DeE------------------------R..  r6 = r7 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u8 [r6 + 622]
    ..D=========================eER  r8 = r7 | 0x100
    ..D............................  r7 = r5
    ..DeeeeeeeeeeeeeeeE-----------R  r0 = 802, jump 22431
```

Gas simulation at offset 26208 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r6 + 622]
    D=========================eER.........................  r7 = r7 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 622] = a0
    D==========================eE------------------------R  r7 = r7 & 0xff
    .D==========================eE-----------------------R  r8 = r7 | 0x100
    .D....................................................  r7 = r5
    .DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 804, jump 22431
```

Gas simulation at offset 26235 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u8 [r6 + 622]
    D=========================eER.........................  r8 = r8 + 0x1
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.........................  u8 [r6 + 617] = a0
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 622] = a1
    .D=========================eE------------------------R  r7 = r8 & 0xff
    .D==========================eE-----------------------R  r8 = r7 | 0x100
    ..D...................................................  r7 = r5
    ..DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 806, jump 22431
```

Gas simulation at offset 26266 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 618] = a0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u16 [r6 + 617]
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeE----------R  r0 = 808, jump 22431
```

Gas simulation at offset 26282 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = i16 [r6 + 617]
    D=========================eER.........................  r7 = r7 + 0x1
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 617] = r7
    DeE--------------------------------------------------R  r7 = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r0 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r6 = u64 [r1 + 0]
    .D=========================eE------------------------R  r1 = r1 + 0x18
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 26308 with total cost of 61:

```
    DeER............................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...................................  r8 = u8 [r7 + 619]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...................................  r9 = u8 [r7 + 623]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...................................  r10 = u8 [r7 + 613]
    .D=========================eER..................................  r11 = r9 & 0x1
    .D=========================eER..................................  r12 = r8 - r10
    ..D========================eER..................................  r9 = r9 & 0x3c
    ..D========================eER..................................  r10 = r10 ^ r8
    ..D=========================eER.................................  r11 = r11 + r12
    ...D========================eeeER...............................  r2 = r10 <u 0x80
    ...D=========================eE-R...............................  r11 = r11 + 0xffffffffffffffff
    ....D=========================eER...............................  r12 = r11 & 0xff
    ....D=========================eER...............................  r10 = r11 & 0x80
    .....D========================eER...............................  r8 = r8 ^ r11
    .....D=========================eER..............................  r9 = r9 | r10
    ......D========================eeeER............................  r10 = r11 <u 0x100
    .......D=======================eeeER............................  r12 = r12 <u 0x1
    .......D=======================eE--R............................  r8 = r8 << 0x38
    ........D=========================eER...........................  r12 = r12 << 0x1
    ........D=======================eE--R...........................  r8 = r8 >> 0x3f
    ........D=========================eER...........................  r9 = r9 | r10
    .........D=======================eeER...........................  r8 = r8 & ~r2
    .........D=========================eER..........................  r9 = r9 | r12
    ..........D========================eER..........................  r8 = r8 << 0x6
    ..........D=========================eER.........................  r8 = r8 | r9
    ..........D=====================eeeeeeeeeeeeeeeeeeeeeeeeeER.....  u8 [r7 + 619] = a4
    ..........D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 623] = a1
    ...........DeE-------------------------------------------------R  r7 = 0
    ...........DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 26403 with total cost of 51:

```
    DeER..................................................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = u8 [r7 + 620]
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 622] = a1
    DeE--------------------------------------------------R  r7 = 0
    .DeeeeeeeeeeeeeeeeeeeeeeE----------------------------R  jump [r0 + 0]
```

Gas simulation at offset 26419 with total cost of 29:

```
    DeER............................  r7 = r7 + 0x7ff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  r8 = u8 [r7 + 614]
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...  r7 = u16 [r7 + 617]
    D==========================eER..  r8 = r8 << 0x20
    .D=========================eER..  r7 = r7 << 0x10
    .D==========================eER.  r7 = r7 | r8
    .D===========================eER  r7 = r7 + 0x1
    .DeeeeeeeeeeeeeeeeeeeeeeE------R  jump [r0 + 0]
```

Gas simulation at offset 26445 with total cost of 72:

```
    DeER.......................................................................  r1 = r1 + 0xffffffffffffffb8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u64 [r1 + 64] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u64 [r1 + 56] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u64 [r1 + 48] = r6
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u64 [r1 + 40] = r8
    .DeE------------------------R..............................................  r6 = 0x30a98
    .D=========================eER.............................................  r8 = r6 + 0x2000
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER....................  r8 = u64 [r8 + 1536]
    ..D==================================================eeeeeeeeeeeeeeeeeeeeER  jump 27140 if r8 == 0
```

Gas simulation at offset 26477 with total cost of 22:

```
    DeeER....................  i32 r8 = r7 >> 0x19
    D==eeeeeeeeeeeeeeeeeeeeER  jump 26820 if r8 != 0
```

Gas simulation at offset 26484 with total cost of 2:

```
    DeeER  i32 r3 = r7 + 0x1
    D....  r8 = r7
    .D...  r10 = r7
    .DeER  jump 26532 if r7 <=u 126
```

Gas simulation at offset 26495 with total cost of 12:

```
    DeER...........  i32 r8 = clz r3
    .DeeeER........  i32 r9 = 0x18 - r8
    ..DeE-R........  r8 = r8 << 0x7
    ...D=eeER......  i32 r11 = r3 >> r9
    ....DeeER......  i32 r9 = 0xffffffffffffffff << r9
    .....D=eER.....  r10 = r11 & 0x7f
    ......DeeER....  r9 = r3 & ~r9
    .......D=eeeER.  r9 = r9 >u 0
    .......DeE---R.  r10 = r10 - r8
    ........DeE--R.  r8 = r10 + 0x7ff
    ........D=eE-R.  r10 = r8 + 0x480
    .........D==eER  r8 = r10 + r9
    .........DeeE-R  fallthrough
```

Gas simulation at offset 26532 with total cost of 49:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.........  unlikely
    DeE---------------------------------------R.........  r12 = 0x2000
    D=eE--------------------------------------R.........  r9 = r6 + r12
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R.........  r11 = u64 [r9 + 1848]
    .DeeE-------------------------------------R.........  i32 r2 = r8 >> 0x6
    ..D=========================eE------------R.........  r5 = r11 >> r2
    ..D==========================eE-----------R.........  r5 = r5 & 0x1
    ...D==========================eeeeeeeeeeeeeeeeeeeeER  jump 26589 if r5 == 0
```

Gas simulation at offset 26556 with total cost of 48:

```
    DeER...............................................  r9 = r2 << 0x3
    DeER...............................................  r12 = r6 + 0x2000
    .DeER..............................................  r9 = r9 + r12
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r9 = u64 [r9 + 1544]
    .DeE-------------------------R.....................  r12 = 0xffffffffffffffff
    ..DeE------------------------R.....................  r8 = r12 << r8
    ..D=========================eER....................  r8 = r8 & r9
    ...D=========================eeeeeeeeeeeeeeeeeeeeER  jump 26589 if r8 == 0
```

Gas simulation at offset 26582 with total cost of 15:

```
    DeeER.............  r9 = ctz r8
    D==eeER...........  r12 = r9 if r8 != 0
    DeeeeeeeeeeeeeeeER  jump 26627
```

Gas simulation at offset 26589 with total cost of 23:

```
    DeER......................  r8 = r2 + 0x1
    DeER......................  r2 = 0xffffffffffffffff
    .DeER.....................  r8 = r2 << r8
    .D=eER....................  r8 = r8 & r11
    ..D=eeeeeeeeeeeeeeeeeeeeER  jump 26762 if r8 == 0
```

Gas simulation at offset 26605 with total cost of 33:

```
    DeeER...............................  r9 = ctz r8
    D==eeER.............................  r2 = r9 if r8 != 0
    .D===eER............................  r8 = r2 << 0x3
    .DeE---R............................  r9 = r6 + 0x2000
    ..D===eER...........................  r8 = r8 + r9
    ..D====eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u64 [r8 + 1544]
    ..D=============================eeER  r12 = ctz r8
    ..DeeE-----------------------------R  fallthrough
```

Gas simulation at offset 26627 with total cost of 57:

```
    DeER........................................................  r8 = r2 << 0x6
    D=eER.......................................................  r8 = r8 | r12
    D==eER......................................................  r8 = r8 << 0x20
    .D==eER.....................................................  r8 = r8 >> 0x1e
    .D===eER....................................................  r9 = r6 + r8
    .D====eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r10 = u32 [r9 + 0]
    ..D============================eeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u32 [r10 + 4]
    ..D=====================================================eER.  r8 = r8 >> 0x1
    ..D======================================================eER  jump 26820 if r7 >=u r8
```

Gas simulation at offset 26654 with total cost of 75:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...................................  u64 [r1 + 0] = r9
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...................................  u64 [r1 + 16] = r3
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...................................  u64 [r1 + 24] = r6
    .DeE--------------------------------------R...................................  r9 = r6 + 0x2000
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R...................................  r6 = i32 [r9 + 1536]
    ..D=======================eE--------------R...................................  r11 = r7 ^ 0xffffffffffffffff
    ..D========================eeE------------R...................................  i32 r8 = r8 + r11
    ...D======================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r0 = i32 [r9 + 1864]
    ...D========================eeE---------------------R.........................  i32 r5 = r10 - r6
    ....D=========================eeE-------------------R.........................  i32 r4 = r5 >> 0x5
    ....D===========================eE------------------R.........................  r4 = r4 + 0x1
    .....D===========================eE-----------------R.........................  r11 = r7 + r4
    .....D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  u64 [r1 + 32] = r8
    ......D======================eeeE----------------------R......................  r9 = r8 >u 0
    .......D==========================eeE------------------R......................  i32 r3 = r11 + r9
    .......D===========================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r0
    ........D==========================================eeeeeeeeeeeeeeeeeeeeE-----R  jump 26727 if r0 >=u r3
```

Gas simulation at offset 26707 with total cost of 2:

```
    DeER.  r9 = 0x4001
    D=eER  jump 26820 if r3 >=u r9
```

Gas simulation at offset 26714 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = u64 [r1 + 24]
    D=========================eE--------------R...........  r9 = r8 + 0x2000
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r9 + 1864] = r3
    .DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 26727 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r11 = u32 [r10 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r9 = i32 [r10 + 0]
    DeE------------------------R..........................  r8 = r5 & 0xffffffffffffffe0
    .DeE-----------------------R..........................  r10 = r8 + r6
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = u64 [r1 + 0]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 0] = r11
    ..D...................................................  r5 = r9
    ..D=======================eE-------------------------R  jump 26838 if r11 == 0
```

Gas simulation at offset 26747 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r11 + 12] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r0 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r12 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 24]
    .DeeeeeeeeeeeeeeeE---------R  jump 26898
```

Gas simulation at offset 26762 with total cost of 24:

```
    DeeER......................  i32 r2 = r10 >> 0x6
    .D=eER.....................  r8 = r11 >> r2
    .D==eER....................  r8 = r8 & 0x1
    ..D==eeeeeeeeeeeeeeeeeeeeER  jump 26804 if r8 == 0
```

Gas simulation at offset 26774 with total cost of 48:

```
    DeER...............................................  r8 = r2 << 0x3
    DeER...............................................  r9 = r6 + 0x2000
    .DeER..............................................  r8 = r8 + r9
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r8 = u64 [r8 + 1544]
    .DeE-------------------------R.....................  r9 = r10 & 0x3f
    ..DeE------------------------R.....................  r12 = 0xffffffffffffffff
    ..D=eE-----------------------R.....................  r9 = r12 << r9
    ...D========================eER....................  r8 = r8 & r9
    ...D=========================eeeeeeeeeeeeeeeeeeeeER  jump 26582 if r8 != 0
```

Gas simulation at offset 26804 with total cost of 23:

```
    DeER......................  r8 = r2 + 0x1
    DeER......................  r2 = 0xffffffffffffffff
    .DeER.....................  r8 = r2 << r8
    .D=eER....................  r8 = r8 & r11
    ..D=eeeeeeeeeeeeeeeeeeeeER  jump 26605 if r8 != 0
```

Gas simulation at offset 26820 with total cost of 2:

```
    DeER.  r7 = 0
    DeeER  fallthrough
```

Gas simulation at offset 26823 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 64]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 56]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r6 = u64 [r1 + 48]
    .DeE--------------------------------------R.......  r1 = r1 + 0x48
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 26838 with total cost of 78:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......................................  unlikely
    DeE---------------------------------------R......................................  r9 = r2 << 0x3
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......................................  r6 = u64 [r1 + 24]
    .D========================eE--------------R......................................  r11 = r6 + 0x2000
    .D=========================eE-------------R......................................  r9 = r9 + r11
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r11 = u64 [r9 + 1544]
    ..DeE-------------------------------------------------R..........................  r3 = 0xfffffffffffffffe
    ..D=eE------------------------------------------------R..........................  r12 = r3 <<r r12
    ...D=================================================eER.........................  r11 = r11 & r12
    ...D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r9 + 1544] = r11
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------------------------------R  r0 = u64 [r1 + 16]
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------------------------------R  r12 = u64 [r1 + 8]
    ....D=================================================eE------------------------R  jump 26898 if r11 != 0
```

Gas simulation at offset 26878 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeE---------------------------------------R............  r8 = r6 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r9 = u64 [r8 + 1848]
    .DeE--------------------------------------R............  r11 = r3 <<r r2
    .D=========================eE-------------R............  r9 = r9 & r11
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r8 + 1848] = r9
    ..DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 26898 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeE-------------------------------------R  r2 = r4 <u r12
    .DeE--------------------------------------R  r8 = r0 << 0x1
    .DeE--------------------------------------R  r11 = r10 << 0x20
    ..DeE-------------------------------------R  r3 = r10 + 0x20
    ...DeeE-----------------------------------R  i32 r9 = r7 << 0x5
    ...DeE------------------------------------R  r8 = r8 + 0x1
    ....DeE-----------------------------------R  r11 = r11 >> 0x20
    ....D=eeeeeeeeeeeeeeeeeeeeeeeeeE----------R  u32 [r11 + 0] = r5
    ....D=eeeeeeeeeeeeeeeeeeeeeeeeeE----------R  u32 [r11 + 4] = r8
    .....DeE----------------------------------R  r12 = r3 + r9
    .....DeeeeeeeeeeeeeeeeeeeeeeeeeE----------R  r5 = u64 [r1 + 32]
    .....D=========================eE---------R  jump 27075 if r5 == 0
```

Gas simulation at offset 26935 with total cost of 1:

```
    D...  r8 = r5
    DeER  jump 26979 if r5 <=u 127
```

Gas simulation at offset 26941 with total cost of 15:

```
    DeER..............  r7 = 0x2000000
    D=eeeER...........  r7 = minu(r5, r7)
    D====eER..........  i32 r10 = clz r7
    .D====eeeER.......  i32 r8 = 0x18 - r10
    ..D======eeER.....  i32 r7 = r7 >> r8
    ..D========eER....  r7 = r7 & 0x7f
    ...D==eE-----R....  r10 = r10 << 0x7
    ...D========eER...  r7 = r7 - r10
    ...D=========eER..  r7 = r7 + 0x7ff
    ....D=========eER.  r8 = r7 + 0x480
    ....D==========eER  r8 = r8 + 0x1
    ....DeeE---------R  fallthrough
```

Gas simulation at offset 26979 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..............  unlikely
    DeeE--------------------------------------R..............  i32 r10 = r8 + 0xffffffffffffffff
    .DeE--------------------------------------R..............  r5 = r5 << 0x1
    .DeE--------------------------------------R..............  r7 = r12 << 0x20
    ..DeE-------------------------------------R..............  r8 = r10 << 0x2
    ..D=eE------------------------------------R..............  r8 = r8 + r6
    ..D==eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R..............  r11 = u32 [r8 + 0]
    ...D=eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R..............  u32 [r8 + 0] = r12
    ...DeeE-----------------------------------R..............  i32 r8 = r10 >> 0x6
    ....DeE-----------------------------------R..............  r4 = r10 & 0x3f
    ....D=eE----------------------------------R..............  r7 = r7 >> 0x20
    ....D==eeeeeeeeeeeeeeeeeeeeeeeeeE---------R..............  u32 [r7 + 0] = r0
    .....D=eeeeeeeeeeeeeeeeeeeeeeeeeE---------R..............  u32 [r7 + 4] = r5
    .....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 8] = r11
    .....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 12] = 0
    .....D==========================eE----------------------R  jump 27026 if r11 == 0
```

Gas simulation at offset 27022 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r11 + 12] = r12
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 27026 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...............  unlikely
    DeE---------------------------------------R...............  r7 = r8 << 0x3
    .DeE--------------------------------------R...............  r11 = r6 + 0x2000
    .D=eE-------------------------------------R...............  r7 = r7 + r11
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R...............  r11 = u64 [r7 + 1544]
    ..DeE-------------------------------------R...............  r5 = 0x1 << r4
    ..D==========================eE-----------R...............  r11 = r11 | r5
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r7 + 1544] = r11
    ...DeE--------------------------------------------------R.  r0 = r6 + 0x2000
    ...D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  r7 = u64 [r0 + 1848]
    ....DeE-------------------------------------------------R.  r8 = 0x1 << r8
    ....D=========================eE------------------------R.  r7 = r7 | r8
    .....D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r0 + 1848] = r7
    .....DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r5 = u64 [r1 + 32]
    .....D....................................................  r0 = r5
    .....DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 27075 with total cost of 48:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER........  unlikely
    DeE---------------------------------------R........  r7 = r6 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R........  r8 = i32 [r7 + 1536]
    .DeE--------------------------------------R........  r7 = r5 << 0x5
    .D=eeE------------------------------------R........  i32 r7 = r7 + r12
    ..D========================eeE------------R........  i32 r10 = r8 + 0x80000
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R........  r8 = u64 [r1 + 40]
    ...D========================eE------------R........  r8 = r8 & r2
    ...D=========================eeeeeeeeeeeeeeeeeeeeER  jump 27113 if r7 >=u r10
```

Gas simulation at offset 27104 with total cost of 27:

```
    DeER..........................  r7 = r7 << 0x20
    D=eER.........................  r7 = r7 >> 0x20
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 0] = r0
    DeeE-------------------------R  fallthrough
```

Gas simulation at offset 27113 with total cost of 2:

```
    DeER.  r7 = r3 << 0x20
    D=eER  r7 = r7 >> 0x20
    DeE-R  jump 26823 if r8 == 0
```

Gas simulation at offset 27123 with total cost of 25:

```
    DeER........................  r8 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r0 = u64 [r1 + 64]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 56]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 48]
    .DeE-----------------------R  r1 = r1 + 0x48
    .DeeeeeeeeeeeeeeeE---------R  jump 27934
```

Gas simulation at offset 27140 with total cost of 15:

```
    D.................  r5 = r7
    DeeeeeeeeeeeeeeeER  r0 = 816, jump 27159
```

Gas simulation at offset 27147 with total cost of 1:

```
    D...  r9 = r7
    D...  r7 = r5
    DeER  jump 26477 if r9 != 0
```

Gas simulation at offset 27155 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeE-------------------------R  jump 26820
```

Gas simulation at offset 27159 with total cost of 28:

```
    DeER...........................  r9 = 0x30a98
    D=eER..........................  r8 = r9 + 0x2000
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u64 [r8 + 1856]
    .D==========================eER  jump 27248 if r7 == 0
```

Gas simulation at offset 27175 with total cost of 75:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...................................  u64 [r8 + 1536] = r7
    DeE---------------------------------------R...................................  r2 = 0x1
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...................................  r11 = u64 [r8 + 1664]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...................................  r10 = u64 [r8 + 1848]
    .DeE--------------------------------------R...................................  r12 = 0x8000000000000000
    .D========================eE--------------R...................................  r11 = r11 | r12
    ..DeE-------------------------------------R...................................  r9 = r9 + 0x7ff
    ..D========================eE-------------R...................................  r10 = r10 | 0x8000
    ..DeE-------------------------------------R...................................  r12 = 0x800000000000
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u64 [r8 + 1848] = r10
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R.......................  u32 [r8 + 1864] = r2
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE-R.......................  u64 [r8 + 1664] = r11
    ...D======================eeeeeeeeeeeeeeeeeeeeeeeeeE--R.......................  u64 [r7 + 0] = r12
    ....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  u64 [r7 + 8] = 0
    ....D==============================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r9 + 2045] = r7
    .....D==============================================eeeE---------------------R  r7 = r7 >u 0
    .....DeeeeeeeeeeeeeeeE-------------------------------------------------------R  jump 27147
```

Gas simulation at offset 27248 with total cost of 15:

```
    DeeeER............  r7 = r7 >u 0
    DeeeeeeeeeeeeeeeER  jump 27147
```

Gas simulation at offset 27252 with total cost of 53:

```
    DeER....................................................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u64 [r1 + 0] = r6
    .DeE------------------------R...........................  r7 = r7 + 0xffffffffffffffe0
    .DeE------------------------R...........................  r4 = 0x30a98
    .D=eE-----------------------R...........................  r10 = r7 << 0x20
    ..D=eE----------------------R...........................  r8 = r4 + 0x2000
    ..D==eeeeeeeeeeeeeeeeeeeeeeeeeER........................  r9 = u64 [r8 + 1536]
    ..D========================eE--R........................  r10 = r10 >> 0x20
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u32 [r10 + 4]
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r3 = i32 [r10 + 0]
    ....D=========================eeE---------------------R.  i32 r10 = r7 - r9
    .....D===============================================eER  r2 = r8 >> 0x1
    .....D==========================eE---------------------R  jump 27501 if r10 <u 32
```

Gas simulation at offset 27301 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeE---------------------------------------R...........  r10 = r3 << 0x5
    .DeeE-------------------------------------R...........  i32 r10 = r7 - r10
    .D==eE------------------------------------R...........  r12 = r10 << 0x20
    ..D==eE-----------------------------------R...........  r12 = r12 >> 0x20
    ..D===eeeeeeeeeeeeeeeeeeeeeeeeeE----------R...........  r0 = u32 [r12 + 4]
    ..D============================eE---------R...........  r11 = r0 & 0x1
    ...D============================eeeeeeeeeeeeeeeeeeeeER  jump 27501 if r11 != 0
```

Gas simulation at offset 27324 with total cost of 20:

```
    DeER...................  r8 = r0 >> 0x1
    DeeeeeeeeeeeeeeeeeeeeER  jump 27349 if r0 == 0
```

Gas simulation at offset 27330 with total cost of 20:

```
    DeER...................  r9 = 0x2000000
    D=eeeER................  r9 = minu(r8, r9)
    DeeeeeeeeeeeeeeeeeeeeER  jump 27353 if r0 >=u 256
```

Gas simulation at offset 27344 with total cost of 15:

```
    DeER..............  r9 = r9 + 0xffffffffffffffff
    DeeeeeeeeeeeeeeeER  jump 27379
```

Gas simulation at offset 27349 with total cost of 15:

```
    DeER..............  r9 = 0
    DeeeeeeeeeeeeeeeER  jump 27379
```

Gas simulation at offset 27353 with total cost of 10:

```
    DeER.........  i32 r11 = clz r9
    .DeeeER......  i32 r6 = 0x18 - r11
    ..D==eeER....  i32 r9 = r9 >> r6
    ..D====eER...  r9 = r9 & 0x7f
    ...DeE---R...  r11 = r11 << 0x7
    ...D====eER..  r9 = r9 - r11
    ...D=====eER.  r9 = r9 + 0x7ff
    ...D======eER  r9 = r9 + 0x480
    ....DeeE----R  fallthrough
```

Gas simulation at offset 27379 with total cost of 29:

```
    DeER............................  r11 = r9 << 0x20
    D=eER...........................  r11 = r11 >> 0x1e
    .D=eER..........................  r6 = r4 + r11
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER.  r11 = i32 [r6 + 0]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--R.  r3 = i32 [r12 + 0]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.  r5 = u32 [r12 + 8]
    ..D==========================eER  jump 27408 if r11 != r10
```

Gas simulation at offset 27398 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r6 + 0] = r5
    DeE------------------------R  jump 27423 if r5 == 0
```

Gas simulation at offset 27403 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 12] = 0
    DeeeeeeeeeeeeeeeE----------R  jump 27483
```

Gas simulation at offset 27408 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r9 = u32 [r12 + 12]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r9 + 8] = r5
    DeeeeeeeeeeeeeeeeeeeeE------------------------------R  jump 27483 if r5 == 0
```

Gas simulation at offset 27418 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 12] = r9
    DeeeeeeeeeeeeeeeE----------R  jump 27483
```

Gas simulation at offset 27423 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...............  unlikely
    DeeE--------------------------------------R...............  i32 r10 = r9 >> 0x6
    .DeE--------------------------------------R...............  r12 = 0x2000
    .D=eE-------------------------------------R...............  r11 = r10 << 0x3
    ..DeE-------------------------------------R...............  r5 = r4 + r12
    ..D=eE------------------------------------R...............  r11 = r11 + r5
    ..D==eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R...............  r5 = u64 [r11 + 1544]
    ...DeE------------------------------------R...............  r6 = r9 & 0x3f
    ...DeE------------------------------------R...............  r9 = 0xfffffffffffffffe
    ....DeE-----------------------------------R...............  r6 = r9 <<r r6
    ....D=========================eE----------R...............  r5 = r5 & r6
    .....D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r11 + 1544] = r5
    .....D=========================eE------------------------R  jump 27483 if r5 != 0
```

Gas simulation at offset 27463 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeE---------------------------------------R............  r12 = r4 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r11 = u64 [r12 + 1848]
    .DeE--------------------------------------R............  r9 = r9 <<r r10
    .D=========================eE-------------R............  r9 = r9 & r11
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r12 + 1848] = r9
    ..DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 27483 with total cost of 26:

```
    DeER.........................  r9 = r4 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  r9 = u64 [r9 + 1536]
    .DeeE-----------------------R  i32 r2 = r8 + r2
    .DeE------------------------R  r0 = r0 << 0x4
    ..DeeE----------------------R  i32 r7 = r7 - r0
    ..DeeE----------------------R  fallthrough
```

Gas simulation at offset 27501 with total cost of 5:

```
    DeeER...  i32 r11 = r9 + 0x80000
    .DeER...  r10 = r2 << 0x5
    .D=eeER.  i32 r10 = r10 + r7
    ..D==eER  jump 27738 if r10 >=u r11
```

Gas simulation at offset 27516 with total cost of 48:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER........  unlikely
    DeE---------------------------------------R........  r12 = r10 << 0x20
    D=eE--------------------------------------R........  r12 = r12 >> 0x20
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R........  r6 = u32 [r12 + 4]
    .D==========================eE------------R........  r9 = r6 & 0x1
    .D===========================eeeeeeeeeeeeeeeeeeeeER  jump 27738 if r9 != 0
```

Gas simulation at offset 27533 with total cost of 1:

```
    DeER  r0 = r6 >> 0x1
    DeER  jump 27576 if r6 == 0
```

Gas simulation at offset 27539 with total cost of 4:

```
    DeER...  r5 = 0x2000000
    D=eeeER  r5 = minu(r0, r5)
    DeE---R  jump 27609 if r6 >=u 256
```

Gas simulation at offset 27553 with total cost of 49:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.........  unlikely
    DeE---------------------------------------R.........  r9 = r5 + 0xffffffffffffffff
    .DeE--------------------------------------R.........  r5 = r9 << 0x20
    .D=eE-------------------------------------R.........  r5 = r5 >> 0x1e
    ..D=eE------------------------------------R.........  r6 = r4 + r5
    ..D==eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R.........  r8 = i32 [r6 + 0]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R.........  r5 = u32 [r12 + 8]
    ...D==========================eeeeeeeeeeeeeeeeeeeeER  jump 27595 if r8 == r10
```

Gas simulation at offset 27574 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 27652
```

Gas simulation at offset 27576 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r9 = 0
    DeE---------------------------------------R  r6 = 0x30a98
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = i32 [0x30a98]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R  r5 = u32 [r12 + 8]
    .D========================eE--------------R  jump 27652 if r8 != r10
```

Gas simulation at offset 27595 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r6 + 0] = r5
    DeE------------------------R  jump 27670 if r5 == 0
```

Gas simulation at offset 27600 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 12] = 0
    DeeE-----------------------R  i32 r2 = r0 + r2
    DeeeeeeeeeeeeeeeE----------R  jump 27738
```

Gas simulation at offset 27609 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  i32 r8 = clz r5
    .DeeeE------------------------------------R  i32 r9 = 0x18 - r8
    ..D==eeE----------------------------------R  i32 r9 = r5 >> r9
    ...D===eE---------------------------------R  r9 = r9 & 0x7f
    ...DeE------------------------------------R  r8 = r8 << 0x7
    ...D====eE--------------------------------R  r9 = r9 - r8
    ....D====eE-------------------------------R  r8 = r9 + 0x7ff
    ....D=====eE------------------------------R  r9 = r8 + 0x480
    .....D=====eE-----------------------------R  r5 = r9 << 0x20
    .....D======eE----------------------------R  r5 = r5 >> 0x1e
    ......D======eE---------------------------R  r6 = r4 + r5
    ......D=======eeeeeeeeeeeeeeeeeeeeeeeeeE--R  r8 = i32 [r6 + 0]
    ......DeeeeeeeeeeeeeeeeeeeeeeeeeE---------R  r5 = u32 [r12 + 8]
    .......D===============================eE-R  jump 27595 if r8 == r10
```

Gas simulation at offset 27652 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r9 = u32 [r12 + 12]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r9 + 8] = r5
    DeeeeeeeeeeeeeeeeeeeeE------------------------------R  jump 27734 if r5 == 0
```

Gas simulation at offset 27662 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 12] = r9
    DeeE-----------------------R  i32 r2 = r0 + r2
    DeeeeeeeeeeeeeeeE----------R  jump 27738
```

Gas simulation at offset 27670 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...............  unlikely
    DeeE--------------------------------------R...............  i32 r10 = r9 >> 0x6
    .DeE--------------------------------------R...............  r12 = 0x2000
    .D=eE-------------------------------------R...............  r8 = r10 << 0x3
    ..DeE-------------------------------------R...............  r5 = r4 + r12
    ..D=eE------------------------------------R...............  r8 = r8 + r5
    ..D==eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R...............  r5 = u64 [r8 + 1544]
    ...DeE------------------------------------R...............  r6 = r9 & 0x3f
    ...DeE------------------------------------R...............  r9 = 0xfffffffffffffffe
    ....DeE-----------------------------------R...............  r6 = r9 <<r r6
    ....D=========================eE----------R...............  r5 = r5 & r6
    .....D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r8 + 1544] = r5
    .....D=========================eE------------------------R  jump 27734 if r5 != 0
```

Gas simulation at offset 27710 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeE---------------------------------------R............  r12 = r4 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r8 = u64 [r12 + 1848]
    .DeE--------------------------------------R............  r9 = r9 <<r r10
    .D=========================eE-------------R............  r8 = r8 & r9
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r12 + 1848] = r8
    ..DeeE------------------------------------------------R  i32 r2 = r0 + r2
    ..DeeeeeeeeeeeeeeeE-----------------------------------R  jump 27738
```

Gas simulation at offset 27734 with total cost of 2:

```
    DeeER  i32 r2 = r0 + r2
    DeeER  fallthrough
```

Gas simulation at offset 27738 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 27877 if r2 == 0
```

Gas simulation at offset 27742 with total cost of 1:

```
    D...  r9 = r2
    DeER  jump 27786 if r2 <=u 127
```

Gas simulation at offset 27748 with total cost of 15:

```
    DeER..............  r8 = 0x2000000
    D=eeeER...........  r8 = minu(r2, r8)
    D====eER..........  i32 r10 = clz r8
    .D====eeeER.......  i32 r9 = 0x18 - r10
    ..D======eeER.....  i32 r8 = r8 >> r9
    ..D========eER....  r8 = r8 & 0x7f
    ...D==eE-----R....  r10 = r10 << 0x7
    ...D========eER...  r8 = r8 - r10
    ...D=========eER..  r8 = r8 + 0x7ff
    ....D=========eER.  r9 = r8 + 0x480
    ....D==========eER  r9 = r9 + 0x1
    ....DeeE---------R  fallthrough
```

Gas simulation at offset 27786 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..............  unlikely
    DeeE--------------------------------------R..............  i32 r10 = r9 + 0xffffffffffffffff
    .DeE--------------------------------------R..............  r8 = r2 << 0x1
    .DeE--------------------------------------R..............  r5 = r7 << 0x20
    ..DeE-------------------------------------R..............  r9 = r10 << 0x2
    ..D=eE------------------------------------R..............  r9 = r9 + r4
    ..D==eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R..............  r12 = u32 [r9 + 0]
    ...D=eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R..............  u32 [r9 + 0] = r7
    ...DeeE-----------------------------------R..............  i32 r9 = r10 >> 0x6
    ....DeE-----------------------------------R..............  r10 = r10 & 0x3f
    ....D=eE----------------------------------R..............  r5 = r5 >> 0x20
    ....D==eeeeeeeeeeeeeeeeeeeeeeeeeE---------R..............  u32 [r5 + 0] = r3
    ....D==eeeeeeeeeeeeeeeeeeeeeeeeeE---------R..............  u32 [r5 + 4] = r8
    .....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 8] = r12
    .....D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 12] = 0
    .....D==========================eE----------------------R  jump 27833 if r12 == 0
```

Gas simulation at offset 27829 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r12 + 12] = r7
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 27833 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...............  unlikely
    DeE---------------------------------------R...............  r8 = r9 << 0x3
    .DeE--------------------------------------R...............  r12 = r4 + 0x2000
    .D=eE-------------------------------------R...............  r8 = r8 + r12
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R...............  r12 = u64 [r8 + 1544]
    ..DeE-------------------------------------R...............  r10 = 0x1 << r10
    ..D==========================eE-----------R...............  r10 = r10 | r12
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r8 + 1544] = r10
    ...DeE--------------------------------------------------R.  r4 = r4 + 0x2000
    ...D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  r8 = u64 [r4 + 1848]
    ....DeE-------------------------------------------------R.  r9 = 0x1 << r9
    ....D=========================eE------------------------R.  r8 = r8 | r9
    .....D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r4 + 1848] = r8
    .....DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 27877 with total cost of 4:

```
    DeER...  r8 = r2 << 0x5
    D=eeER.  i32 r7 = r7 + r8
    .D==eER  jump 27895 if r7 >=u r11
```

Gas simulation at offset 27886 with total cost of 27:

```
    DeER..........................  r7 = r7 << 0x20
    D=eER.........................  r7 = r7 >> 0x20
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 0] = r2
    DeeE-------------------------R  fallthrough
```

Gas simulation at offset 27895 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r6 = u64 [r1 + 0]
    .DeE--------------------------------------R.......  r1 = r1 + 0x18
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 27909 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 27932 if r9 == 0
```

Gas simulation at offset 27912 with total cost of 2:

```
    DeER.  r9 = r9 + r7
    D....  r10 = r7
    DeeER  fallthrough
```

Gas simulation at offset 27918 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r11 = u8 [r8 + 0]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r10 + 0] = a4
    DeE-------------------------------------------------R  r10 = r10 + 0x1
    .DeE------------------------------------------------R  r8 = r8 + 0x1
    .DeE------------------------------------------------R  jump 27918 if r10 != r9
```

Gas simulation at offset 27932 with total cost of 22:

```
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 27934 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 27951 if r9 == 0
```

Gas simulation at offset 27937 with total cost of 2:

```
    DeER.  r9 = r9 + r7
    D....  r10 = r7
    DeeER  fallthrough
```

Gas simulation at offset 27943 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r10 + 0] = a1
    DeE------------------------R  r10 = r10 + 0x1
    D=eeeeeeeeeeeeeeeeeeeeE----R  jump 27943 if r10 != r9
```

Gas simulation at offset 27951 with total cost of 22:

```
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 27953 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r8 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r9 = i32 [r7 + 0]
    .D=========================eE-------------R............  r4 = r9 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r9 = r9 & 0xff
    ..D=========================eE------------------------R  jump 27953 if r9 != 0
```

Gas simulation at offset 27984 with total cost of 15:

```
    DeER..............  r7 = 0x1e00
    DeER..............  r8 = 0x1
    DeER..............  r6 = 0x1
    DeeeeeeeeeeeeeeeER  r0 = 818, jump 26445
```

Gas simulation at offset 28000 with total cost of 27:

```
    DeER..........................  r10 = 0x2000
    D=eER.........................  r8 = r5 + r10
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 1872] = 0
    .DeE-------------------------R  r8 = 0x30008
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 40] = r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R  r8 = u64 [0x30008]
    .D............................  r9 = r5
    ..D...........................  r5 = r7
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r9
    ..D========================eER  jump 28097 if r8 == 0
```

Gas simulation at offset 28034 with total cost of 2:

```
    DeER.  r7 = r9 + 0x2750
    D=eER  r7 = r7 & 0xfffffffffffffffc
    DeeER  fallthrough
```

Gas simulation at offset 28042 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r6 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r9 = i32 [r7 + 0]
    .D=========================eE-------------R............  r4 = r9 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r9 = r9 & 0xff
    ..D=========================eE------------------------R  jump 28042 if r9 != 0
```

Gas simulation at offset 28073 with total cost of 15:

```
    D.................  r7 = r8
    DeeeeeeeeeeeeeeeER  r0 = 820, jump 27252
```

Gas simulation at offset 28081 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r9 = u64 [r1 + 56]
    D=========================eER.........................  r7 = r9 + 0x2000
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 1872] = 0
    .DeE-------------------------------------------------R  r10 = 0x2000
    .DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 28097 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r7 = u64 [r1 + 40]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r7 + 0] = r5
    .DeE------------------------------------------------R  r7 = r9 + 0x2750
    .D=eE-----------------------------------------------R  r7 = r7 & 0xfffffffffffffffc
    .DeeE-----------------------------------------------R  fallthrough
```

Gas simulation at offset 28111 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r6 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r8 = i32 [r7 + 0]
    .D=========================eE-------------R............  r4 = r8 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r8 = r8 & 0xff
    ..D=========================eE------------------------R  jump 28111 if r8 != 0
```

Gas simulation at offset 28142 with total cost of 15:

```
    DeER..............  r7 = 0x200
    DeeeeeeeeeeeeeeeER  r0 = 822, jump 26445
```

Gas simulation at offset 28152 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r5 = u64 [r1 + 56]
    D=========================eER.........................  r8 = r5 + 0x2000
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 1872] = 0
    .DeE-------------------------------------------------R  jump 32020 if r7 == 0
```

Gas simulation at offset 28167 with total cost of 26:

```
    DeER.........................  r6 = 0x10240
    D=eER........................  r8 = r6 + 0x10
    DeE-R........................  r9 = 0x4000
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 32] = r7
    .DeeeeeeeeeeeeeeeE----------R  r0 = 824, jump 27909
```

Gas simulation at offset 28188 with total cost of 3:

```
    DeER..  r7 = r5 + 0x2750
    D=eER.  r7 = r7 & 0xfffffffffffffffc
    DeE-R.  r8 = 0x1
    .DeeER  fallthrough
```

Gas simulation at offset 28199 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r8 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r9 = i32 [r7 + 0]
    .D=========================eE-------------R............  r4 = r9 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r9 = r9 & 0xff
    ..D=========================eE------------------------R  jump 28199 if r9 != 0
```

Gas simulation at offset 28230 with total cost of 15:

```
    DeER..............  r7 = 0x100
    DeER..............  r8 = 0
    DeeeeeeeeeeeeeeeER  r0 = 826, jump 26445
```

Gas simulation at offset 28242 with total cost of 51:

```
    D.....................................................  r10 = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u64 [r1 + 56]
    D=========================eER.........................  r7 = r7 + 0x2000
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 1872] = 0
    .DeE-------------------------------------------------R  jump 32020 if r10 == 0
```

Gas simulation at offset 28259 with total cost of 26:

```
    DeER.........................  r5 = 0x4000
    DeER.........................  r8 = r6 + 0x4010
    DeER.........................  r9 = 0x2000
    .D...........................  r7 = r10
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 24] = r10
    .DeeeeeeeeeeeeeeeE----------R  r0 = 828, jump 27909
```

Gas simulation at offset 28282 with total cost of 175:

```
    DeER..............................................................................................................................................................................  r6 = 0x1
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................................................................  r7 = i16 [r1 + 672]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................................................................  u64 [r1 + 64] = r5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................................................................  r8 = u64 [r1 + 32]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................................................................  u64 [r1 + 72] = r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R.............................................................................................................................  u64 [r1 + 80] = r5
    .DeE------------------------------------------------R.............................................................................................................................  r5 = 0x2000
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................................................................  u64 [r1 + 88] = r5
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................................................................  u64 [r1 + 764] = 0
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER............................................................................................................................  u64 [r1 + 772] = 0
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u8 [r1 + 780] = 0
    ...DeE-----------------------------------------------------------------------R....................................................................................................  r8 = 0xfffffc0000000000
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u64 [r1 + 672] = 0
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u64 [r1 + 680] = r6
    ....D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER...................................................................................................  u64 [r1 + 688] = 0
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  u64 [r1 + 696] = r8
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  u16 [r1 + 118] = r7
    .....DeE----------------------------------------------------------------------------------------------R...........................................................................  r10 = 0xffff8000ffffa000
    .....DeE----------------------------------------------------------------------------------------------R...........................................................................  r12 = 0xffff4000ffff6000
    ......DeE---------------------------------------------------------------------------------------------R...........................................................................  r7 = 0xffffd400ffffd800
    ......D=====================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  u64 [r1 + 736] = r7
    ......D======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................  u64 [r1 + 744] = r10
    .......D=============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r1 + 752] = r12
    .......D=============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u32 [r1 + 760] = 0xffffffffffff2000
    .......D=============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r9 = u64 [r1 + 24]
    .......D======================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 96] = r9
    ........D=============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R.........................  u64 [r1 + 104] = r5
    ........D=====================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u32 [r1 + 112] = r5
    ........D=====================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r1 + 116] = r6
    .........DeE--------------------------------------------------------------------------------------------------------------------------------------------R.........................  r2 = 0xfffff40100000000
    .........DeE--------------------------------------------------------------------------------------------------------------------------------------------R.........................  r9 = 0xfffff400fffff800
    ..........DeE-------------------------------------------------------------------------------------------------------------------------------------------R.........................  r11 = 0xffffec00fffff000
    ..........DeE-------------------------------------------------------------------------------------------------------------------------------------------R.........................  r8 = 0xffffe400ffffe800
    ............................DeE-------------------------------------------------------------------------------------------------------------------------R.........................  r7 = 0xffffdc00ffffe000
    ............................D==================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u64 [r1 + 704] = r9
    ............................D==========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 712] = r11
    .....................................................D=================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 720] = r8
    .....................................................D=================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 728] = r7
    .....................................................D==================================================================================================eE-----------------------R  r7 = r1 + 0x2a0
    ......................................................DeE------------------------------------------------------------------------------------------------------------------------R  r9 = 0x2000
    ......................................................DeE------------------------------------------------------------------------------------------------------------------------R  r8 = 0
    ......................................................DeeeeeeeeeeeeeeeE----------------------------------------------------------------------------------------------------------R  r0 = 830, jump 32021
```

Gas simulation at offset 28495 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u64 [r1 + 680]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u64 [r1 + 688]
    D=========================eE------------------------R  r7 = r7 + r8
    .D========================eE------------------------R  r5 = r5 + r8
    .DeE------------------------------------------------R  r9 = 0x2000
    .DeE------------------------------------------------R  r8 = 0
    .DeeeeeeeeeeeeeeeE----------------------------------R  r0 = 832, jump 27934
```

Gas simulation at offset 28524 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r1 + 776]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u64 [r1 + 672]
    D=========================eER.........................  r7 = r7 | 0x3
    D=========================eER.........................  r8 = r8 - r5
    .D=========================eER........................  r8 = r8 >> 0xe
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R........................  u64 [r1 + 688] = r5
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R........................  u32 [r1 + 744] = 0xffffffffffffa000
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r1 + 776] = a0
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 8]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r5
    ..D=========================eeeeeeeeeeeeeeeeeeeeE----R  jump 30495 if r8 == 0
```

Gas simulation at offset 28565 with total cost of 25:

```
    DeER........................  r7 = r7 + r5
    DeER........................  r9 = 0x4000
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeE----------R  r0 = 834, jump 27909
```

Gas simulation at offset 28581 with total cost of 128:

```
    DeER...............................................................................................................................  r5 = r5 + 0x4000
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.......................................................................................................  r9 = u64 [r1 + 16]
    D=========================eER......................................................................................................  r7 = r9 + 0xffffffffffff8000
    .D=========================eER.....................................................................................................  r8 = r9 + 0xffffffffffff4000
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................................................................................................  r9 = u8 [r1 + 777]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................................................................................................  r10 = u8 [r1 + 778]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................................................................  r11 = u8 [r1 + 779]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................  r12 = u8 [r1 + 780]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................  u64 [r1 + 688] = r5
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER............................................................................  u32 [r1 + 748] = r7
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER............................................................................  u32 [r1 + 752] = r7
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................  u32 [r1 + 756] = r8
    ...D================================================eE------------------------R....................................................  r7 = r9 | 0x1
    ....D================================================eE-----------------------R....................................................  r9 = r10 | 0x1
    ....D================================================eE-----------------------R....................................................  r10 = r11 | 0x1
    .....D===============================================eE-----------------------R....................................................  r11 = r12 | 0x1
    .....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u32 [r1 + 760] = r8
    .....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u8 [r1 + 777] = a0
    ......D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u8 [r1 + 778] = a2
    ......D======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  u8 [r1 + 779] = a3
    ......D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r1 + 780] = a4
    .......D=======================================================================eE------------------------R.........................  r7 = r1 + 0x2a0
    .......DeE-----------------------------------------------------------------------------------------------R.........................  r9 = 0x2000
    .......D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = u64 [r1 + 24]
    ........DeE----------------------------------------------------------------------------------------------R.........................  r0 = 0x344
    ........D=======================================================================eE-----------------------R.........................  r1 = r1 + 0xffffffffffffffd0
    ........D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................  u64 [r1 + 40] = r0
    ........D=============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..  u64 [r1 + 32] = r9
    .........D==============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 24] = r6
    .........D.........................................................................................................................  r6 = r7
    .........D==============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r7 + 16]
    .........DeeeeeeeeeeeeeeeE--------------------------------------------------------------------------------------------------------R  jump 32360
```

Gas simulation at offset 28696 with total cost of 76:

```
    DeER...........................................................................  r7 = r1 + 0x2a0
    DeER...........................................................................  r0 = 0x346
    DeER...........................................................................  r1 = r1 + 0xffffffffffffffc8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r1 + 48] = r0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r1 + 40] = r5
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r1 + 32] = r6
    .DeE------------------------R..................................................  r6 = 0x1
    ..D............................................................................  r5 = r7
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeER.................................................  r7 = u64 [r7 + 0]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r10 = u64 [r5 + 16]
    ..D=================================================eER........................  r7 = r7 - r10
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 24] = r10
    ...DeeeeeeeeeeeeeeeE----------------------------------------------------------R  jump 32553
```

Gas simulation at offset 28735 with total cost of 27:

```
    DeeER.........................  i32 r7 = r5 + 0x750
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u64 [r1 + 56]
    .D========================eER.  r7 = r7 + r8
    .D=========================eER  r7 = r7 & 0xfffffffffffffffc
    .DeeE------------------------R  fallthrough
```

Gas simulation at offset 28749 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r6 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r8 = i32 [r7 + 0]
    .D=========================eE-------------R............  r4 = r8 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r8 = r8 & 0xff
    ..D=========================eE------------------------R  jump 28749 if r8 != 0
```

Gas simulation at offset 28780 with total cost of 15:

```
    DeER..............  r7 = 0x4
    DeeeeeeeeeeeeeeeER  r0 = 840, jump 26445
```

Gas simulation at offset 28789 with total cost of 51:

```
    D.....................................................  r5 = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u64 [r1 + 56]
    D=========================eER.........................  r7 = r8 + 0x2000
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 1872] = 0
    .DeE-------------------------------------------------R  jump 32020 if r5 == 0
```

Gas simulation at offset 28806 with total cost of 16:

```
    DeER...............  r8 = r1 + 0x2a0
    DeER...............  r9 = 0x70
    D..................  r7 = r5
    .DeeeeeeeeeeeeeeeER  r0 = 842, jump 27909
```

Gas simulation at offset 28821 with total cost of 50:

```
    DeER.................................................  r7 = 0x18d48
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r9 = u64 [r1 + 64]
    DeE------------------------R.........................  r8 = 0x8000000000000000
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER........................  u64 [r1 + 224] = r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER........................  u64 [r1 + 232] = r5
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER........................  u64 [r1 + 240] = r7
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 56]
    ..D========================eE-----------------------R  jump 28917 if r9 == 0
```

Gas simulation at offset 28857 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 72]
    DeE------------------------R  r8 = r5 + 0x2750
    D=eE-----------------------R  r8 = r8 & 0xfffffffffffffffc
    .DeE-----------------------R  r9 = 0x1
    .DeeE----------------------R  fallthrough
```

Gas simulation at offset 28871 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r9 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r10 = i32 [r8 + 0]
    .D=========================eE-------------R............  r4 = r10 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r10 = r10 & 0xff
    ..D=========================eE------------------------R  jump 28871 if r10 != 0
```

Gas simulation at offset 28902 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  r0 = 844, jump 27252
```

Gas simulation at offset 28908 with total cost of 26:

```
    DeER.........................  r7 = r5 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 1872] = 0
    DeeE------------------------R  fallthrough
```

Gas simulation at offset 28917 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u64 [r1 + 88]
    D=========================eE--------------R  jump 28984 if r7 == 0
```

Gas simulation at offset 28924 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 96]
    DeE------------------------R  r8 = r5 + 0x2750
    D=eE-----------------------R  r8 = r8 & 0xfffffffffffffffc
    .DeE-----------------------R  r9 = 0x1
    .DeeE----------------------R  fallthrough
```

Gas simulation at offset 28938 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r9 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r10 = i32 [r8 + 0]
    .D=========================eE-------------R............  r4 = r10 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r10 = r10 & 0xff
    ..D=========================eE------------------------R  jump 28938 if r10 != 0
```

Gas simulation at offset 28969 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  r0 = 846, jump 27252
```

Gas simulation at offset 28975 with total cost of 26:

```
    DeER.........................  r7 = r5 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 1872] = 0
    DeeE------------------------R  fallthrough
```

Gas simulation at offset 28984 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u64 [r1 + 224]
    DeE---------------------------------------R  r8 = 0x8000000000000000
    .D========================eE--------------R  jump 30494 if r7 != r8
```

Gas simulation at offset 29003 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r7 = u64 [r1 + 40]
    D=========================eE--------------R............  r6 = r7 + 0x7ff
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r10 = u64 [r6 + 585]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  r7 = u64 [r1 + 232]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 32] = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  r7 = u64 [r1 + 240]
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 48] = r7
    ..D=================================================eER  jump 29125 if r10 == 0
```

Gas simulation at offset 29032 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r5 = u64 [r6 + 593]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u64 [r5 + 0]
    D==================================================eER  jump 29056 if r8 == 0
```

Gas simulation at offset 29042 with total cost of 25:

```
    D...........................  r7 = r10
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 24] = r10
    DeeeeeeeeeeeeeeeeeeeeeeE---R  r0 = 848, jump [r8 + 0]
```

Gas simulation at offset 29052 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r10 = u64 [r1 + 24]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 29056 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u64 [r5 + 8]
    D=========================eE--------------R  jump 29125 if r7 == 0
```

Gas simulation at offset 29063 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r5 = u64 [r1 + 56]
    D=========================eER.  r7 = r5 + 0x2750
    D==========================eER  r7 = r7 & 0xfffffffffffffffc
    .DeE-------------------------R  r8 = 0x1
    .DeeE------------------------R  fallthrough
```

Gas simulation at offset 29077 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r8 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r9 = i32 [r7 + 0]
    .D=========================eE-------------R............  r4 = r9 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r9 = r9 & 0xff
    ..D=========================eE------------------------R  jump 29077 if r9 != 0
```

Gas simulation at offset 29108 with total cost of 15:

```
    D.................  r7 = r10
    DeeeeeeeeeeeeeeeER  r0 = 850, jump 27252
```

Gas simulation at offset 29116 with total cost of 26:

```
    DeER.........................  r7 = r5 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 1872] = 0
    DeeE------------------------R  fallthrough
```

Gas simulation at offset 29125 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  u64 [r6 + 585] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r7 = u64 [r1 + 48]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r6 + 593] = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R  u8 [r6 + 651] = 0x1
    .DeE------------------------------------------------R  r5 = 0x800
    .DeE------------------------------------------------R  r7 = r1 + 0x2a0
    ..DeE-----------------------------------------------R  r8 = 0
    ..DeE-----------------------------------------------R  r9 = 0x800
    ..DeeeeeeeeeeeeeeeE---------------------------------R  r0 = 852, jump 27934
```

Gas simulation at offset 29162 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 208] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 214] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 192] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r1 + 200] = 0
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 136] = 0
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 141] = 0
    .D========================eE------------------------R  r7 = r1 + 0xe5
    ..DeE-----------------------------------------------R  r9 = 0x16e
    ..DeE-----------------------------------------------R  r8 = 0
    ..DeeeeeeeeeeeeeeeE---------------------------------R  r0 = 854, jump 27934
```

Gas simulation at offset 29202 with total cost of 152:

```
    DeER.......................................................................................................................................................  r7 = r1 + 0x2a0
    D=eER......................................................................................................................................................  r5 = r5 + r7
    .DeER......................................................................................................................................................  r8 = r7 + 0x7ff
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................................................................  u64 [r1 + 176] = 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................................................................  u64 [r1 + 184] = 0
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................................................................  u32 [r1 + 664] = 0
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................................................................  u16 [r1 + 668] = 0
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................................................................  u64 [r1 + 654] = 0
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................................................................  u16 [r1 + 662] = 0
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u64 [r1 + 608] = 0
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u64 [r1 + 616] = 0
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER............................................................................  u64 [r1 + 624] = 0
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER............................................................................  u64 [r1 + 632] = 0
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  u64 [r1 + 640] = 0
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  u32 [r1 + 647] = 0
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  u32 [r1 + 600] = 0
    ....D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  u8 [r1 + 604] = 0
    .....D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r7 = u64 [r6 + 521]
    .....D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r5 + 8] = 0
    .....D================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r5 + 15] = 0
    .....D================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r8 + 25] = 0
    ......D================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r8 + 1] = 0
    ......D================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r8 + 33] = 0
    ......D========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 160] = 0
    ......D========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 168] = 0
    .......D========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r1 + 130] = 0
    .......D========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r1 + 134] = 0
    .......D================================================================================================================================================eER  jump 29463 if r7 == 0
```

Gas simulation at offset 29308 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r5 = u64 [r1 + 56]
    D=========================eER.  r8 = r5 + 0x2750
    D==========================eER  r8 = r8 & 0xfffffffffffffffc
    .DeE-------------------------R  r10 = 0x1
    .DeeE------------------------R  fallthrough
```

Gas simulation at offset 29322 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r10 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r9 = i32 [r8 + 0]
    .D=========================eE-------------R............  r4 = r9 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r9 = r9 & 0xff
    ..D=========================eE------------------------R  jump 29322 if r9 != 0
```

Gas simulation at offset 29353 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  r0 = 856, jump 27252
```

Gas simulation at offset 29359 with total cost of 26:

```
    DeER.........................  r7 = r5 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 1872] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R  r7 = u64 [r6 + 585]
    .D========================eER  jump 29463 if r7 == 0
```

Gas simulation at offset 29374 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r5 = u64 [r6 + 593]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u64 [r5 + 0]
    D==================================================eER  jump 29396 if r8 == 0
```

Gas simulation at offset 29384 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 24] = r7
    DeeeeeeeeeeeeeeeeeeeeeeE---R  r0 = 858, jump [r8 + 0]
```

Gas simulation at offset 29392 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 24]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 29396 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u64 [r5 + 8]
    D=========================eE--------------R  jump 29463 if r8 == 0
```

Gas simulation at offset 29403 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r5 = u64 [r1 + 56]
    D=========================eER.  r8 = r5 + 0x2750
    .D=========================eER  r10 = r8 & 0xfffffffffffffffc
    .DeE-------------------------R  r8 = 0x1
    .DeeE------------------------R  fallthrough
```

Gas simulation at offset 29417 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r8 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r9 = i32 [r10 + 0]
    .D=========================eE-------------R............  r4 = r9 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r10 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r9 = r9 & 0xff
    ..D=========================eE------------------------R  jump 29417 if r9 != 0
```

Gas simulation at offset 29448 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  r0 = 860, jump 27252
```

Gas simulation at offset 29454 with total cost of 26:

```
    DeER.........................  r7 = r5 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 1872] = 0
    DeeE------------------------R  fallthrough
```

Gas simulation at offset 29463 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = u64 [r1 + 40]
    D=========================eE--------------R...........  r7 = r7 + 0x8
    DeE---------------------------------------R...........  r9 = 0x828
    .DeE--------------------------------------R...........  r8 = r1 + 0x2a0
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 40] = r7
    .DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 862, jump 27909
```

Gas simulation at offset 29487 with total cost of 275:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................................................................................................................................................................................................  r11 = i32 [r1 + 664]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................................................................................................................................................................................................  r4 = i16 [r1 + 668]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................................................................................................................................................................................................  r0 = u64 [r1 + 653]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................................................................................................................................................................................................  r7 = i32 [r1 + 660]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................................................................................................................................................................  u64 [r1 + 24] = r7
    .DeE------------------------------------------------R.................................................................................................................................................................................................................................  r3 = 0x17bf4
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................................................................................................................................................................  r8 = u64 [r1 + 608]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................................................................................................................................................................  r7 = u64 [r1 + 616]
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................................................................................................................................................................  r9 = u64 [r1 + 624]
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................................................................................................................................................................  r12 = u64 [r1 + 632]
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................................................................................................................................................................  r5 = u64 [r1 + 640]
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................................................................................................................................................................  r2 = i32 [r1 + 647]
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................................................................................................................................................................  u8 [r6 + 49] = 0x1
    ...D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................................................................................................................  u32 [r6 + 50] = r11
    ...DeE------------------------------------------------------------------------------------------------R...............................................................................................................................................................................  r10 = 0x7
    ...D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................................................................................................................  u16 [r6 + 54] = r4
    ....DeE-----------------------------------------------------------------------------------------------R...............................................................................................................................................................................  r4 = 0xc000
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................................................................................................................  u64 [r6 + 56] = r0
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................................................................................................................  u64 [r6 + 81] = 0x9
    ....D================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................................................................  u64 [r6 + 89] = r8
    .....D===============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................................................................  r8 = i32 [r1 + 600]
    .....D===============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................................................................  r11 = u8 [r1 + 604]
    .....D===============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................................................................  u64 [r6 + 97] = r7
    .....D========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................................................................  u64 [r6 + 105] = r9
    ......D=======================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................................................................  u64 [r6 + 113] = r12
    ......D=======================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................................................................  u64 [r6 + 121] = r5
    ......D=======================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................................................................  u8 [r6 + 133] = 0
    ......D================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u16 [r6 + 143] = r4
    .......DeE-----------------------------------------------------------------------------------------------------------------------------------------------------------------------R....................................................................................................  r0 = 0x1c0000000
    .......D===============================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u32 [r6 + 128] = r2
    .......D===============================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u64 [r6 + 135] = r0
    ........D==============================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u32 [r6 + 145] = r8
    ............................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  u8 [r6 + 149] = a4
    ............................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  u64 [r1 + 16] = 0x8000001
    ............................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  u32 [r6 + 150] = 0x8000001
    ............................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  u16 [r6 + 154] = 0x200
    .....................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u16 [r6 + 157] = 0x1
    .....................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u32 [r6 + 159] = 0x2000000
    .....................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  r8 = u64 [r1 + 24]
    .....................................................D============================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u32 [r6 + 63] = r8
    ......................................................D==================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.........................  u16 [r6 + 67] = 0x1
    ..............................................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u32 [r6 + 69] = 0
    ..............................................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 24] = r3
    ..............................................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r6 + 73] = r3
    ..............................................................................D============================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 163] = 0
    .......................................................................................................D===================================================================================================================================================eE------------------------R  r7 = r6 + 0xa4
    .......................................................................................................D===================================================================================================================================================eE------------------------R  r8 = r1 + 0xe0
    ........................................................................................................DeE--------------------------------------------------------------------------------------------------------------------------------------------------------------------------R  r9 = 0x173
    ........................................................................................................DeeeeeeeeeeeeeeeE------------------------------------------------------------------------------------------------------------------------------------------------------------R  r0 = 864, jump 27909
```

Gas simulation at offset 29692 with total cost of 251:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................................................................................................................................................................................................  r9 = u64 [r1 + 208]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................................................................................................................................................................................................  r2 = u64 [r1 + 214]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................................................................................................................................................................................................  r10 = u64 [r1 + 192]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................................................................................................................................................................................................  r3 = i16 [r1 + 200]
    .DeE-----------------------R..................................................................................................................................................................................................................................  r4 = 0x2000
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................................................................................................................................................  r11 = u64 [r1 + 176]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................................................................................................................................................  r12 = u64 [r1 + 184]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................................................................................................................................................  u16 [r6 + 535] = 0x105
    ..D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................................................................................................................................................  u64 [r6 + 537] = r9
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................................................................................................................................................  u32 [r6 + 551] = 0xc10000
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................................................................................................................................................  u64 [r6 + 556] = r10
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................................................................................................................................................  u64 [r6 + 568] = r11
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................................................................................................................................................  r9 = u64 [r1 + 152]
    ...D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................................................................................................................................................  r10 = u64 [r1 + 160]
    ...D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................................................................................................................................................  r11 = u64 [r1 + 168]
    ...D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................................................................................................................................................  u64 [r6 + 576] = r12
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................................................................................................................................................  u64 [r6 + 585] = 0
    ....D================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................................................................  u64 [r6 + 593] = r9
    ....D================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................................................................  r9 = u64 [r1 + 136]
    ....D================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................................................................  r12 = u64 [r1 + 141]
    .....D===============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................................................................  r7 = u64 [r1 + 32]
    .....D========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................................................................  u64 [r6 + 585] = r7
    .....D========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................................................................  r7 = u64 [r1 + 48]
    .....D=================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER............................................................................  u64 [r6 + 593] = r7
    ......D=======================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R............................................................................  r5 = u64 [r1 + 126]
    ......D=======================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R............................................................................  r7 = i16 [r1 + 134]
    ......D================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER............................................................................  u64 [r6 + 601] = r10
    ......D================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER............................................................................  u64 [r6 + 609] = r11
    .......DeE-----------------------------------------------------------------------------------------------------------------------------------------------------------------------R............................................................................  r10 = 0x24fd
    .......D===============================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER............................................................................  u64 [r6 + 543] = r2
    .......D========================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  u8 [r6 + 555] = 0
    .......D========================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  u16 [r6 + 564] = r3
    ............................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  u64 [r1 + 48] = 0x2107
    ............................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  u16 [r6 + 566] = 0x2107
    ............................D============================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r6 + 622] = r12
    ............................D============================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r6 + 632] = 0
    .............................D===========================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r6 + 617] = r9
    .....................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u16 [r6 + 630] = r10
    .....................................................D============================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u32 [r6 + 639] = 0
    .....................................................D============================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u16 [r6 + 651] = r7
    .....................................................D============================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r6 + 643] = r5
    ..............................................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u8 [r6 + 651] = 0x1
    ..............................................................................D============================================================================================================================================================================eER  r7 = r1 + 0x2a0
    ..............................................................................DeE----------------------------------------------------------------------------------------------------------------------------------------------------------------------------R  r9 = 0x16e
    ...............................................................................DeE---------------------------------------------------------------------------------------------------------------------------------------------------------------------------R  r8 = 0
    .......................................................................................................DeeeeeeeeeeeeeeeE-------------------------------------------------------------------------------------------------------------------------------------R  r0 = 866, jump 27934
```

Gas simulation at offset 29883 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u64 [r6 + 521]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 224] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 230] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 608] = 0
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r1 + 616] = 0
    .D========================eeeeeeeeeeeeeeeeeeeeE-----R  jump 29966 if r7 == 0
```

Gas simulation at offset 29906 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r5 = u64 [r1 + 56]
    D=========================eER.  r8 = r5 + 0x2750
    D==========================eER  r8 = r8 & 0xfffffffffffffffc
    .DeE-------------------------R  r9 = 0x1
    .DeeE------------------------R  fallthrough
```

Gas simulation at offset 29920 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r9 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r10 = i32 [r8 + 0]
    .D=========================eE-------------R............  r4 = r10 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r10 = r10 & 0xff
    ..D=========================eE------------------------R  jump 29920 if r10 != 0
```

Gas simulation at offset 29951 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  r0 = 868, jump 27252
```

Gas simulation at offset 29957 with total cost of 26:

```
    DeER.........................  r7 = r5 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 1872] = 0
    DeeE------------------------R  fallthrough
```

Gas simulation at offset 29966 with total cost of 16:

```
    DeER...............  r7 = r6 + 0xa9
    DeER...............  r8 = r1 + 0x2a0
    .DeER..............  r9 = 0x16e
    .DeeeeeeeeeeeeeeeER  r0 = 870, jump 27909
```

Gas simulation at offset 29984 with total cost of 300:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................................................................................................................................................................................................................................................  r8 = u64 [r1 + 224]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................................................................................................................................................................................................................................................  r7 = u64 [r1 + 230]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................................................................................................................................................................................................................................................  r10 = u64 [r1 + 608]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................................................................................................................................................................................................................................................  r9 = i16 [r1 + 616]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................................................................................................................................................................................................  u64 [r6 + 9] = 0
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................................................................................................................................................................................................  u64 [r6 + 17] = 0
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................................................................................................................................................................................................  u32 [r6 + 128] = 0
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................................................................................................................................................................................................................................................  u16 [r6 + 135] = 0
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................................................................................................................................................................  u32 [r6 + 145] = 0
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................................................................................................................................................................  r11 = u64 [r1 + 16]
    ..D=========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................................................................................................................................................................  u32 [r6 + 150] = r11
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R........................................................................................................................................................................................................  u64 [r6 + 57] = 0
    ...D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R........................................................................................................................................................................................................  u64 [r6 + 65] = 0x10000
    ...D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................................................................................................................................................................  r11 = u64 [r1 + 24]
    ...D=================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................................................................................................................  u64 [r6 + 73] = r11
    ...D========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R...............................................................................................................................................................................  u64 [r6 + 81] = 0x9
    ....DeE------------------------------------------------------------------------------------------------------------------------R...............................................................................................................................................................................  r11 = 0xc00000000001c000
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R...............................................................................................................................................................................  u64 [r6 + 24] = 0
    ....D================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................................................................................................................  u64 [r6 + 41] = 0
    .....D===============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................................................................................................................  u32 [r6 + 50] = 0
    .....D===============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................................................................................................................................................  u16 [r6 + 54] = 0
    .....D========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................................................................  u64 [r6 + 89] = 0
    .....D========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................................................................  u64 [r6 + 97] = 0
    ......D=======================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................................................................  u64 [r6 + 105] = 0
    ......D=======================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................................................................................................................................................  u64 [r6 + 113] = 0
    ......D================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................................................................  u64 [r6 + 33] = 0
    ......D================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................................................................  u8 [r6 + 49] = 0x1
    .......D===============================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................................................................  u16 [r6 + 154] = 0x200
    .......D===============================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................................................................................................  u16 [r6 + 157] = 0x1
    .......DeE-----------------------------------------------------------------------------------------------------------------------------------------------------------------------R.............................................................................................................................  r12 = 0x2000000
    .......D========================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u32 [r6 + 159] = r12
    ........D=======================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u8 [r6 + 163] = 0
    ............................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u64 [r6 + 121] = 0
    ............................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................................................................................................  u8 [r6 + 133] = 0
    ............................D============================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  u64 [r6 + 137] = r11
    ............................D============================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  u8 [r6 + 149] = 0
    .....................................................DeE---------------------------------------------------------------------------------------------------------------------------------------------------------------------------R...........................................................................  r11 = 0x105
    .....................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  u16 [r6 + 535] = r11
    .....................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................  u64 [r6 + 537] = r8
    .....................................................D============================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u32 [r6 + 551] = 0xc10000
    ..............................................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r6 + 556] = r10
    ..............................................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u64 [r6 + 543] = r7
    .......................................................................................................D==========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u8 [r6 + 555] = 0
    .......................................................................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u16 [r6 + 564] = r9
    .......................................................................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u64 [r1 + 48]
    .......................................................................................................D============================================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 566] = r7
    ................................................................................................................................D==========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u64 [r6 + 568] = 0
    ................................................................................................................................D==========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u64 [r6 + 576] = 0
    ................................................................................................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r6 + 635] = 0
    ................................................................................................................................D===================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 639] = 0
    .................................................................................................................................DeE--------------------------------------------------------------------------------------------------------------------------------------------------------------------------R  r8 = 0xff
    .................................................................................................................................D==================================================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 40]
    .................................................................................................................................D.............................................................................................................................................................................  r7 = r5
    .................................................................................................................................DeeeeeeeeeeeeeeeE------------------------------------------------------------------------------------------------------------------------------------------------------------R  r0 = 872, jump 22431
```

Gas simulation at offset 30199 with total cost of 15:

```
    DeER..............  r8 = 0xff
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 874, jump 22431
```

Gas simulation at offset 30211 with total cost of 15:

```
    DeER..............  r8 = 0xff
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 876, jump 22431
```

Gas simulation at offset 30223 with total cost of 15:

```
    DeER..............  r8 = 0x100
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 878, jump 22431
```

Gas simulation at offset 30235 with total cost of 15:

```
    DeER..............  r8 = 0x1ff
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 880, jump 22431
```

Gas simulation at offset 30247 with total cost of 15:

```
    DeER..............  r8 = 0x1fe
    D.................  r7 = r5
    DeeeeeeeeeeeeeeeER  r0 = 882, jump 22431
```

Gas simulation at offset 30259 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 630] = 0xfffffffffffffffd
    DeE------------------------R  r8 = 0xfffc
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeE----------R  r0 = 884, jump 22431
```

Gas simulation at offset 30277 with total cost of 26:

```
    DeER.........................  r7 = r7 & 0xff
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r7
    DeE-------------------------R  r8 = 0xfffd
    D............................  r7 = r5
    .DeeeeeeeeeeeeeeeE----------R  r0 = 886, jump 22431
```

Gas simulation at offset 30297 with total cost of 51:

```
    DeER..................................................  r7 = r7 << 0x8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u64 [r1 + 56]
    D=========================eER.........................  r7 = r7 | r8
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u16 [r6 + 625] = r7
    .DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 888, jump 5372
```

Gas simulation at offset 30316 with total cost of 2:

```
    DeER.  r7 = r7 & 0x1
    D=eER  jump 30494 if r7 != 0
```

Gas simulation at offset 30323 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  r0 = 890, jump 5372
```

Gas simulation at offset 30329 with total cost of 2:

```
    DeER.  r7 = r7 & 0x1
    D=eER  jump 30494 if r7 != 0
```

Gas simulation at offset 30336 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  r0 = 892, jump 5372
```

Gas simulation at offset 30342 with total cost of 2:

```
    DeER.  r7 = r7 & 0x1
    D=eER  jump 30494 if r7 != 0
```

Gas simulation at offset 30349 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  r0 = 894, jump 5372
```

Gas simulation at offset 30355 with total cost of 2:

```
    DeER.  r7 = r7 & 0x1
    D=eER  jump 30494 if r7 != 0
```

Gas simulation at offset 30362 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = u8 [r6 + 647]
    D=========================eE--------------R...........  r7 = r7 | 0x4
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 647] = a0
    .DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 896, jump 5372
```

Gas simulation at offset 30380 with total cost of 2:

```
    DeER.  r7 = r7 & 0x1
    D=eER  jump 30494 if r7 != 0
```

Gas simulation at offset 30386 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = u8 [r6 + 647]
    D=========================eE--------------R...........  r7 = r7 & 0xfb
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 647] = a0
    .DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 898, jump 5372
```

Gas simulation at offset 30405 with total cost of 2:

```
    DeER.  r7 = r7 & 0x1
    D=eER  jump 30494 if r7 != 0
```

Gas simulation at offset 30411 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  r0 = 900, jump 5372
```

Gas simulation at offset 30417 with total cost of 2:

```
    DeER.  r7 = r7 & 0x1
    D=eER  jump 30494 if r7 != 0
```

Gas simulation at offset 30423 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  r0 = 902, jump 5372
```

Gas simulation at offset 30429 with total cost of 2:

```
    DeER.  r7 = r7 & 0x1
    D=eER  jump 30494 if r7 != 0
```

Gas simulation at offset 30435 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = u8 [r6 + 647]
    D=========================eE--------------R...........  r7 = r7 | 0x4
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 647] = a0
    .DeeeeeeeeeeeeeeeE-----------------------------------R  r0 = 904, jump 5372
```

Gas simulation at offset 30453 with total cost of 2:

```
    DeER.  r7 = r7 & 0x1
    D=eER  jump 30494 if r7 != 0
```

Gas simulation at offset 30459 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r7 = u8 [r6 + 647]
    D=========================eE--------------R...........  r7 = r7 & 0xfb
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r6 + 647] = a0
    .DeE-------------------------------------------------R  r1 = r1 + 0x2e8
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R  r0 = u64 [r1 + 2032]
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R  r5 = u64 [r1 + 2024]
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R  r6 = u64 [r1 + 2016]
    ..D=========================eE-----------------------R  r1 = r1 + 0x7f8
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 30494 with total cost of 2:

```
    DeeER  trap
```

Gas simulation at offset 30495 with total cost of 25:

```
    DeER........................  r7 = r1 + 0x2a0
    DeER........................  r9 = 0x4000
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeE---------R  r0 = 906, jump 32021
```

Gas simulation at offset 30512 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r1 + 680]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 688]
    DeeeeeeeeeeeeeeeE----------R  jump 28565
```

Gas simulation at offset 30523 with total cost of 52:

```
    DeER...................................................  r1 = r1 + 0xfffffffffffffff8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  u64 [r1 + 0] = r0
    DeE-------------------------R..........................  r0 = 0x38c
    D=eE------------------------R..........................  r1 = r1 + 0xfffffffffffff808
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 2032] = r0
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 2024] = r5
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u64 [r1 + 2016] = r6
    .D=========================eER.........................  r1 = r1 + 0xfffffffffffffd18
    ..DeE------------------------R.........................  r8 = 0xb3200
    ..DeE------------------------R.........................  r5 = 0x30a98
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 48] = r8
    ...D========================eE------------------------R  r7 = r5 + 0x2750
    ...D=========================eE-----------------------R  r7 = r7 & 0xfffffffffffffffc
    ...DeE------------------------------------------------R  r8 = 0x1
    ....DeeeeeeeeeeeeeeeE---------------------------------R  jump 27953
```

Gas simulation at offset 30578 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 0]
    DeE------------------------R......................  r1 = r1 + 0x8
    D=========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 30585 with total cost of 2:

```
    DeER.  r7 = r7 & 0x1
    D=eER  jump 30779 if r7 != 0
```

Gas simulation at offset 30592 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r6 = 0x30008
    D=eE--------------------------------------R  r7 = r6 + 0x7ff
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R  r5 = u64 [r7 + 521]
    .D==========================eE------------R  jump 30712 if r5 != 0
```

Gas simulation at offset 30609 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 0] = r7
    DeE------------------------R.  r8 = 0x30a98
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r8
    .DeE------------------------R  r7 = r8 + 0x2750
    .D=eE-----------------------R  r7 = r7 & 0xfffffffffffffffc
    .DeE------------------------R  r8 = 0x1
    ..DeeE----------------------R  fallthrough
```

Gas simulation at offset 30630 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r8 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r9 = i32 [r7 + 0]
    .D=========================eE-------------R............  r4 = r9 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r7 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r9 = r9 & 0xff
    ..D=========================eE------------------------R  jump 30630 if r9 != 0
```

Gas simulation at offset 30661 with total cost of 15:

```
    DeER..............  r7 = 0xf00
    DeER..............  r8 = 0
    DeeeeeeeeeeeeeeeER  r0 = 912, jump 26445
```

Gas simulation at offset 30673 with total cost of 51:

```
    D.....................................................  r5 = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u64 [r1 + 8]
    D=========================eER.........................  r7 = r8 + 0x2000
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 1872] = 0
    .DeE-------------------------------------------------R  jump 32020 if r5 == 0
```

Gas simulation at offset 30690 with total cost of 15:

```
    DeER..............  r9 = 0x1e000
    D.................  r7 = r5
    DeER..............  r8 = 0
    DeeeeeeeeeeeeeeeER  r0 = 914, jump 27934
```

Gas simulation at offset 30705 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r7 = u64 [r1 + 0]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r7 + 521] = r5
    DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 30712 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r8 = u64 [r6 + 0]
    D=========================eE--------------R  jump 30780 if r8 == 0
```

Gas simulation at offset 30718 with total cost of 2:

```
    DeER.  r11 = 0x3bffc
    DeER.  r9 = 0x200
    DeER.  r10 = 0x173f4
    DeeER  fallthrough
```

Gas simulation at offset 30733 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u16 [r5 + 0]
    D=========================eE--------------R  jump 30781 if r7 >=u r9
```

Gas simulation at offset 30739 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    D......................................................  r12 = r11
    DeE---------------------------------------R............  r7 = r7 << 0x2
    D=eE--------------------------------------R............  r7 = r7 + r10
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R............  r7 = i32 [r7 + 0]
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 0] = r7
    .DeE--------------------------------------------------R  r11 = r11 + 0xfffffffffffffffc
    .DeE--------------------------------------------------R  r8 = r8 + 0x4
    ..DeE-------------------------------------------------R  r5 = r5 + 0x2
    ..DeE-------------------------------------------------R  jump 30733 if r12 != 0
```

Gas simulation at offset 30764 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 32]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r6 = u64 [r1 + 16]
    .DeE--------------------------------------R.......  r1 = r1 + 0x28
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 30779 with total cost of 2:

```
    DeeER  trap
```

Gas simulation at offset 30780 with total cost of 2:

```
    DeeER  trap
```

Gas simulation at offset 30781 with total cost of 2:

```
    DeeER  trap
```

Gas simulation at offset 30782 with total cost of 27:

```
    DeER..........................  r1 = r1 + 0xfffffffffffffff8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 0] = r0
    DeE-------------------------R.  r0 = 0x394
    D=eE------------------------R.  r1 = r1 + 0xffffffffffffffd8
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 32] = r0
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 24] = r5
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r6
    .DeE-------------------------R  r0 = 0x38e
    ..DeeeeeeeeeeeeeeeE----------R  jump 5372
```

Gas simulation at offset 30810 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 0]
    DeE------------------------R......................  r1 = r1 + 0x8
    D=========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 30817 with total cost of 21:

```
    DeER....................  r9 = 0x1
    DeER....................  r10 = 0x1fffffffe0
    D=eeeeeeeeeeeeeeeeeeeeER  jump 30838 if r10 >=u r8
```

Gas simulation at offset 30833 with total cost of 15:

```
    DeER..............  r7 = 0
    DeeeeeeeeeeeeeeeER  jump 32329
```

Gas simulation at offset 30838 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xffffffffffffffa8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 80] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 72] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 64] = r6
    .DeE------------------------R  r5 = 0x30a98
    .D=eE-----------------------R  r10 = r5 + 0x2750
    .D==eE----------------------R  r10 = r10 & 0xfffffffffffffffc
    ..DeeE----------------------R  fallthrough
```

Gas simulation at offset 30863 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r9 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r11 = i32 [r10 + 0]
    .D=========================eE-------------R............  r4 = r11 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r10 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r11 = r11 & 0xff
    ..D=========================eE------------------------R  jump 30863 if r11 != 0
```

Gas simulation at offset 30894 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r9 = u32 [r7 - 28]
    DeE---------------------------------------R.......  r8 = r8 + 0x1f
    .DeE--------------------------------------R.......  r3 = r8 >> 0x5
    ..DeeE------------------------------------R.......  i32 r8 = r3 + 0
    ..D=======================eE--------------R.......  r9 = r9 >> 0x1
    ...D=======================eE-------------R.......  r6 = r9 + 0xffffffffffffffff
    ...D========================eeeeeeeeeeeeeeeeeeeeER  jump 31120 if r6 == r8
```

Gas simulation at offset 30916 with total cost of 1:

```
    DeER  jump 31031 if r8 >=u r6
```

Gas simulation at offset 30919 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r2 = r7 + 0xffffffffffffffe0
    .DeE--------------------------------------R  r11 = r2 << 0x20
    .D=eE-------------------------------------R  r11 = r11 >> 0x20
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R  r10 = u32 [r11 + 4]
    ..DeeE------------------------------------R  i32 r9 = r3 + 0x1
    ..D==========================eE-----------R  r10 = r10 >> 0x1
    ...D==========================eE----------R  jump 31120 if r9 >=u r10
```

Gas simulation at offset 30942 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r12 = r9 << 0x1
    D=eE--------------------------------------R  r12 = r12 + 0x1
    .DeE--------------------------------------R  r6 = r5 + 0x2000
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R  u32 [r11 + 4] = r12
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R  r11 = i32 [r6 + 1536]
    ..DeE-------------------------------------R  r12 = 0x80000
    ..DeE-------------------------------------R  r6 = r10 << 0x5
    ...D========================eeE-----------R  i32 r4 = r11 + r12
    ....DeeE----------------------------------R  i32 r6 = r6 + r2
    .....DeeE---------------------------------R  i32 r0 = r10 - r9
    .....D========================eE----------R  jump 31483 if r6 >=u r4
```

Gas simulation at offset 30981 with total cost of 48:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER........  unlikely
    D..................................................  r8 = r5
    DeE---------------------------------------R........  r5 = r6 << 0x20
    .DeE--------------------------------------R........  r5 = r5 >> 0x20
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R........  r11 = u32 [r5 + 4]
    .D==========================eE------------R........  r12 = r11 & 0x1
    ..D==========================eeeeeeeeeeeeeeeeeeeeER  jump 31317 if r12 != 0
```

Gas simulation at offset 31000 with total cost of 26:

```
    DeER.........................  r10 = r11 >> 0x1
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r10
    DeeeeeeeeeeeeeeeeeeeeE------R  jump 31322 if r11 == 0
```

Gas simulation at offset 31010 with total cost of 20:

```
    DeER...................  r3 = 0x2000000
    D=eeeER................  r3 = minu(r10, r3)
    DeeeeeeeeeeeeeeeeeeeeER  jump 31326 if r11 >=u 256
```

Gas simulation at offset 31025 with total cost of 15:

```
    DeER..............  r3 = r3 + 0xffffffffffffffff
    DeeeeeeeeeeeeeeeER  jump 31352
```

Gas simulation at offset 31031 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r5
    DeE------------------------R  r9 = 0xffffffff
    D=eE-----------------------R  jump 31097 if r3 != r9
```

Gas simulation at offset 31047 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 48] = r7
    D...........................  r7 = r8
    DeE------------------------R  r8 = 0
    DeeeeeeeeeeeeeeeE----------R  r0 = 918, jump 26445
```

Gas simulation at offset 31060 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 31116 if r7 == 0
```

Gas simulation at offset 31063 with total cost of 26:

```
    DeER.........................  r9 = r6 << 0x25
    D=eER........................  r9 = r9 >> 0x20
    D............................  r5 = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 48]
    .D...........................  r8 = r6
    .DeeeeeeeeeeeeeeeE----------R  r0 = 920, jump 27909
```

Gas simulation at offset 31082 with total cost of 15:

```
    D.................  r7 = r6
    DeeeeeeeeeeeeeeeER  r0 = 922, jump 27252
```

Gas simulation at offset 31090 with total cost of 25:

```
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 56]
    DeeeeeeeeeeeeeeeE----------R  jump 31120
```

Gas simulation at offset 31097 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r9 = r7 + 0xffffffffffffffe0
    .DeE--------------------------------------R  r5 = r9 << 0x20
    .D=eE-------------------------------------R  r5 = r5 >> 0x20
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R  r10 = u32 [r5 + 4]
    ..D==========================eE-----------R  r2 = r10 >> 0x1
    ..D===========================eE----------R  jump 31142 if r8 >=u r2
```

Gas simulation at offset 31116 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 56]
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 31120 with total cost of 47:

```
    DeER..............................................  r8 = r5 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  u8 [r8 + 1872] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................  r0 = u64 [r1 + 80]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r5 = u64 [r1 + 72]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r6 = u64 [r1 + 64]
    .D========================eER.....................  r1 = r1 + 0x58
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 31142 with total cost of 78:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER......................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R......................................  r11 = u64 [r1 + 56]
    D=========================eE--------------R......................................  r10 = r11 + 0x2000
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r4 = u64 [r10 + 1536]
    .DeE-------------------------------------------------R...........................  r11 = r2 << 0x5
    ..D=================================================eeER.........................  i32 r10 = r4 + 0x80000
    ...DeeE------------------------------------------------R.........................  i32 r11 = r11 + r9
    ...D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 48] = r10
    ...D==================================================eE------------------------R  jump 31047 if r11 >=u r10
```

Gas simulation at offset 31171 with total cost of 48:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER........  unlikely
    DeE---------------------------------------R........  r12 = r11 << 0x20
    D=eE--------------------------------------R........  r12 = r12 >> 0x20
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R........  r0 = u32 [r12 + 4]
    .D==========================eE------------R........  r10 = r0 & 0x1
    .D===========================eeeeeeeeeeeeeeeeeeeeER  jump 31047 if r10 != 0
```

Gas simulation at offset 31188 with total cost of 26:

```
    DeER.........................  r10 = r0 >> 0x1
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 32] = r10
    .DeeE-----------------------R  i32 r10 = r10 + r2
    .D==eeeeeeeeeeeeeeeeeeeeE---R  jump 31047 if r8 >=u r10
```

Gas simulation at offset 31201 with total cost of 97:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER........................................................................  u64 [r1 + 0] = r12
    DeeE-----------------------R........................................................................  i32 r12 = r3 + 0x1
    .D=eE----------------------R........................................................................  r3 = r12 << 0x5
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................................  u64 [r1 + 16] = r3
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--R.....................................................................  u64 [r1 + 8] = r10
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................................................................  u64 [r1 + 40] = r12
    ..D=======================eE--R.....................................................................  r10 = r10 ^ r12
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u64 [r1 + 24] = r10
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  r10 = u64 [r1 + 56]
    ...DeE-----------------------------------------------R..............................................  r12 = 0x2000
    ...D================================================eER.............................................  r10 = r10 + r12
    ...D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.............................................  r2 = u64 [r1 + 16]
    ...D=================================================eER............................................  r2 = r2 + r9
    ....D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER....................  r3 = i32 [r10 + 1864]
    ....D=================================================eeE----------------------R....................  i32 r10 = r2 - r4
    .....D..............................................................................................  r4 = r2
    .....D==================================================eeE--------------------R....................  i32 r2 = r10 >> 0x5
    ......D======================eeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R....................  r10 = u64 [r1 + 24]
    ......D===============================================eeeE---------------------R....................  r10 = r10 >u 0
    .......D==================================================eE-------------------R....................  r2 = r2 + r10
    .......D======================================================================eeeeeeeeeeeeeeeeeeeeER  jump 31284 if r3 >=u r2
```

Gas simulation at offset 31263 with total cost of 2:

```
    DeER.  r10 = 0x4001
    D=eER  jump 31047 if r2 >=u r10
```

Gas simulation at offset 31271 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r10 = u64 [r1 + 56]
    D=========================eE--------------R...........  r8 = r10 + 0x2000
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 1864] = r2
    .DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 31284 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r4
    DeeeeeeeeeeeeeeeeeeeeE-----R  jump 31662 if r0 == 0
```

Gas simulation at offset 31291 with total cost of 28:

```
    DeER...........................  r8 = 0x2000000
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...  r6 = u64 [r1 + 32]
    D=========================eeeER  r8 = minu(r6, r8)
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--R  r12 = u64 [r1 + 0]
    .DeeeeeeeeeeeeeeeeeeeeE-------R  jump 31668 if r0 >=u 256
```

Gas simulation at offset 31311 with total cost of 15:

```
    DeER..............  r3 = r8 + 0xffffffffffffffff
    DeeeeeeeeeeeeeeeER  jump 31694
```

Gas simulation at offset 31317 with total cost of 15:

```
    D.................  r5 = r8
    DeeeeeeeeeeeeeeeER  jump 31483
```

Gas simulation at offset 31322 with total cost of 15:

```
    DeER..............  r3 = 0
    DeeeeeeeeeeeeeeeER  jump 31352
```

Gas simulation at offset 31326 with total cost of 10:

```
    DeER.........  i32 r10 = clz r3
    .DeeeER......  i32 r11 = 0x18 - r10
    ..D==eeER....  i32 r11 = r3 >> r11
    ...D===eER...  r11 = r11 & 0x7f
    ...DeE---R...  r10 = r10 << 0x7
    ...D====eER..  r11 = r11 - r10
    ....D====eER.  r10 = r11 + 0x7ff
    ....D=====eER  r3 = r10 + 0x480
    .....DeeE---R  fallthrough
```

Gas simulation at offset 31352 with total cost of 29:

```
    DeER............................  r10 = r3 << 0x20
    D=eER...........................  r10 = r10 >> 0x1e
    .D=eER..........................  r11 = r8 + r10
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER.  r10 = i32 [r11 + 0]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--R.  r12 = u32 [r5 + 8]
    ..D==========================eER  jump 31387 if r10 != r6
```

Gas simulation at offset 31369 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r11 + 0] = r12
    DeE------------------------R  jump 31410 if r12 == 0
```

Gas simulation at offset 31374 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  u32 [r12 + 12] = 0
    D.............................  r5 = r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u64 [r1 + 56]
    .D========================eeER  i32 r0 = r8 + r0
    .DeeeeeeeeeeeeeeeE-----------R  jump 31483
```

Gas simulation at offset 31387 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r11 = u32 [r5 + 12]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r11 + 8] = r12
    D....................................................  r5 = r8
    .DeeeeeeeeeeeeeeeeeeeeE-----------------------------R  jump 31476 if r12 == 0
```

Gas simulation at offset 31399 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  u32 [r12 + 12] = r11
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u64 [r1 + 56]
    D=========================eeER  i32 r0 = r8 + r0
    .DeeeeeeeeeeeeeeeE-----------R  jump 31483
```

Gas simulation at offset 31410 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...............  unlikely
    DeeE--------------------------------------R...............  i32 r6 = r3 >> 0x6
    .D=eE-------------------------------------R...............  r10 = r6 << 0x3
    .DeE--------------------------------------R...............  r11 = r8 + 0x2000
    ..D=eE------------------------------------R...............  r10 = r10 + r11
    ..D==eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R...............  r5 = u64 [r10 + 1544]
    ..DeE-------------------------------------R...............  r12 = r3 & 0x3f
    ...DeE------------------------------------R...............  r11 = 0xfffffffffffffffe
    ...D=eE-----------------------------------R...............  r12 = r11 <<r r12
    ....D=========================eE----------R...............  r12 = r12 & r5
    ....D.....................................................  r5 = r8
    ....D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r10 + 1544] = r12
    ....D==========================eE------------------------R  jump 31476 if r12 != 0
```

Gas simulation at offset 31449 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeE---------------------------------------R............  r10 = r5 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r12 = u64 [r10 + 1848]
    .DeE--------------------------------------R............  r11 = r11 <<r r6
    .D=========================eE-------------R............  r11 = r11 & r12
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r10 + 1848] = r11
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r8 = u64 [r1 + 56]
    ..D=========================eeE-----------------------R  i32 r0 = r8 + r0
    ..DeeeeeeeeeeeeeeeE-----------------------------------R  jump 31483
```

Gas simulation at offset 31476 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r8 = u64 [r1 + 56]
    D=========================eeER  i32 r0 = r8 + r0
    DeeE-------------------------R  fallthrough
```

Gas simulation at offset 31483 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 31638 if r0 == 0
```

Gas simulation at offset 31487 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r4
    DeE------------------------R  r12 = r9 << 0x5
    .DeE-----------------------R  r3 = r12 + r2
    .D..........................  r11 = r0
    .DeE-----------------------R  jump 31540 if r0 <=u 127
```

Gas simulation at offset 31502 with total cost of 15:

```
    DeER..............  r8 = 0x2000000
    D=eeeER...........  r8 = minu(r0, r8)
    D====eER..........  i32 r11 = clz r8
    .D====eeeER.......  i32 r10 = 0x18 - r11
    ..D======eeER.....  i32 r8 = r8 >> r10
    ..D========eER....  r8 = r8 & 0x7f
    ...D==eE-----R....  r11 = r11 << 0x7
    ...D========eER...  r8 = r8 - r11
    ...D=========eER..  r8 = r8 + 0x7ff
    ....D=========eER.  r11 = r8 + 0x480
    ....D==========eER  r11 = r11 + 0x1
    ....DeeE---------R  fallthrough
```

Gas simulation at offset 31540 with total cost of 54:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..............  unlikely
    DeeE--------------------------------------R..............  i32 r8 = r11 + 0xffffffffffffffff
    .DeE--------------------------------------R..............  r10 = r0 << 0x1
    .DeE--------------------------------------R..............  r12 = r3 << 0x20
    ..DeE-------------------------------------R..............  r11 = r8 << 0x2
    ..D......................................................  r4 = r5
    ..D=eE------------------------------------R..............  r11 = r11 + r5
    ...D=eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R..............  r5 = u32 [r11 + 0]
    ...D=eeeeeeeeeeeeeeeeeeeeeeeeeE-----------R..............  u32 [r11 + 0] = r3
    ....DeeE----------------------------------R..............  i32 r6 = r8 >> 0x6
    .....DeE----------------------------------R..............  r11 = r8 & 0x3f
    .....D=eE---------------------------------R..............  r12 = r12 >> 0x20
    .....D==eeeeeeeeeeeeeeeeeeeeeeeeeE--------R..............  u32 [r12 + 0] = r9
    ......D=eeeeeeeeeeeeeeeeeeeeeeeeeE--------R..............  u32 [r12 + 4] = r10
    ......D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r12 + 8] = r5
    ......D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r12 + 12] = 0
    ......D==========================eE---------------------R  jump 31589 if r5 == 0
```

Gas simulation at offset 31585 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 12] = r3
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 31589 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...............  unlikely
    DeE---------------------------------------R...............  r8 = r6 << 0x3
    .DeE--------------------------------------R...............  r12 = r4 + 0x2000
    .D=eE-------------------------------------R...............  r8 = r8 + r12
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeE------------R...............  r12 = u64 [r8 + 1544]
    ..DeE-------------------------------------R...............  r11 = 0x1 << r11
    ..D==========================eE-----------R...............  r11 = r11 | r12
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r8 + 1544] = r11
    ...DeE--------------------------------------------------R.  r10 = r4 + 0x2000
    ...D=eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  r8 = u64 [r10 + 1848]
    ....DeE-------------------------------------------------R.  r11 = 0x1 << r6
    ....D.....................................................  r5 = r4
    .....D========================eE------------------------R.  r8 = r8 | r11
    .....D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r10 + 1848] = r8
    .....DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [r1 + 56]
    .....DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 31638 with total cost of 24:

```
    DeER.......................  r9 = r9 + r0
    D=eER......................  r9 = r9 << 0x5
    .D=eeER....................  i32 r8 = r9 + r2
    .D===eeeeeeeeeeeeeeeeeeeeER  jump 31120 if r8 >=u r4
```

Gas simulation at offset 31651 with total cost of 27:

```
    DeER..........................  r8 = r8 << 0x20
    D=eER.........................  r8 = r8 >> 0x20
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 0] = r0
    DeeeeeeeeeeeeeeeE------------R  jump 31120
```

Gas simulation at offset 31662 with total cost of 25:

```
    DeER........................  r3 = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r12 = u64 [r1 + 0]
    DeeeeeeeeeeeeeeeE----------R  jump 31694
```

Gas simulation at offset 31668 with total cost of 10:

```
    DeER.........  i32 r10 = clz r8
    .DeeeER......  i32 r6 = 0x18 - r10
    ..D==eeER....  i32 r8 = r8 >> r6
    ..D====eER...  r8 = r8 & 0x7f
    ...DeE---R...  r10 = r10 << 0x7
    ...D====eER..  r8 = r8 - r10
    ...D=====eER.  r8 = r8 + 0x7ff
    ....D=====eER  r3 = r8 + 0x480
    ....DeeE----R  fallthrough
```

Gas simulation at offset 31694 with total cost of 52:

```
    DeER...................................................  r8 = r3 << 0x20
    D=eER..................................................  r8 = r8 >> 0x1e
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...........................  r10 = u64 [r1 + 56]
    .D========================eER..........................  r8 = r8 + r10
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER.  r4 = i32 [r8 + 0]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  r6 = u32 [r12 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  r0 = u64 [r1 + 8]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R.  r10 = u64 [r1 + 40]
    ..D=========================eeE----------------------R.  i32 r2 = r0 - r10
    ...D================================================eER  jump 31733 if r4 != r11
```

Gas simulation at offset 31723 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 0] = r6
    DeE------------------------R  jump 31748 if r6 == 0
```

Gas simulation at offset 31728 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r6 + 12] = 0
    DeeeeeeeeeeeeeeeE----------R  jump 31811
```

Gas simulation at offset 31733 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r8 = u32 [r12 + 12]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 8] = r6
    DeE-------------------------------------------------R  jump 31811 if r6 == 0
```

Gas simulation at offset 31743 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r6 + 12] = r8
    DeeeeeeeeeeeeeeeE----------R  jump 31811
```

Gas simulation at offset 31748 with total cost of 79:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......................................  unlikely
    DeeE--------------------------------------R.......................................  i32 r11 = r3 >> 0x6
    .D=eE-------------------------------------R.......................................  r8 = r11 << 0x3
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......................................  r10 = u64 [r1 + 56]
    .D=========================eE-------------R.......................................  r10 = r10 + 0x2000
    ..D=========================eE------------R.......................................  r8 = r8 + r10
    ..D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r6 = u64 [r8 + 1544]
    ..DeE--------------------------------------------------R..........................  r12 = r3 & 0x3f
    ...DeE-------------------------------------------------R..........................  r10 = 0xfffffffffffffffe
    ...D=eE------------------------------------------------R..........................  r12 = r10 <<r r12
    ....D=================================================eER.........................  r12 = r12 & r6
    ....D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r8 + 1544] = r12
    ....D==================================================eE------------------------R  jump 31811 if r12 != 0
```

Gas simulation at offset 31788 with total cost of 77:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.....................................  r8 = u64 [r1 + 56]
    D=========================eE--------------R.....................................  r4 = r8 + 0x2000
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r8 = u64 [r4 + 1848]
    .DeE-------------------------------------------------R..........................  r10 = r10 <<r r11
    .D==================================================eER.........................  r8 = r8 & r10
    ..D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r4 + 1848] = r8
    ..DeeE-------------------------------------------------------------------------R  fallthrough
```

Gas simulation at offset 31811 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r4 = u64 [r1 + 40]
    D=========================eE--------------R............  r8 = r4 << 0x1
    .D=========================eE-------------R............  r8 = r8 + 0x1
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 4] = r8
    .DeeeeeeeeeeeeeeeeeeeeE-------------------------------R  jump 31974 if r2 == 0
```

Gas simulation at offset 31828 with total cost of 1:

```
    D...  r10 = r2
    DeER  jump 31872 if r2 <=u 127
```

Gas simulation at offset 31834 with total cost of 15:

```
    DeER..............  r8 = 0x2000000
    D=eeeER...........  r8 = minu(r2, r8)
    D====eER..........  i32 r11 = clz r8
    .D====eeeER.......  i32 r10 = 0x18 - r11
    ..D======eeER.....  i32 r8 = r8 >> r10
    ..D========eER....  r8 = r8 & 0x7f
    ...D==eE-----R....  r11 = r11 << 0x7
    ...D========eER...  r8 = r8 - r11
    ...D=========eER..  r8 = r8 + 0x7ff
    ....D=========eER.  r10 = r8 + 0x480
    ....D==========eER  r10 = r10 + 0x1
    ....DeeE---------R  fallthrough
```

Gas simulation at offset 31872 with total cost of 79:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......................................  unlikely
    DeeE--------------------------------------R.......................................  i32 r8 = r10 + 0xffffffffffffffff
    .DeE--------------------------------------R.......................................  r3 = r2 << 0x1
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......................................  r6 = u64 [r1 + 16]
    ..D========================eE-------------R.......................................  r5 = r6 << 0x20
    ..DeE-------------------------------------R.......................................  r10 = r8 << 0x2
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeE------------R.......................................  r11 = u64 [r1 + 56]
    ...D=========================eE-----------R.......................................  r10 = r10 + r11
    ...D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r12 = u32 [r10 + 0]
    ...D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.  u32 [r10 + 0] = r6
    ....DeeE------------------------------------------------------------------------R.  i32 r10 = r8 >> 0x6
    .....DeE------------------------------------------------------------------------R.  r11 = r8 & 0x3f
    .....D======================eE--------------------------------------------------R.  r5 = r5 >> 0x20
    .....D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  u32 [r5 + 0] = r4
    ......D======================eeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R.  u32 [r5 + 4] = r3
    ......D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 8] = r12
    ......D======================eeeeeeeeeeeeeeeeeeeeeeeeeE--------------------------R  u32 [r5 + 12] = 0
    ......D================================================eeeeeeeeeeeeeeeeeeeeE-----R  jump 31925 if r12 == 0
```

Gas simulation at offset 31921 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r12 + 12] = r6
    DeeE-----------------------R  fallthrough
```

Gas simulation at offset 31925 with total cost of 78:

```
    DeER.............................................................................  r8 = r10 << 0x3
    DeER.............................................................................  r3 = 0x2000
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................  r6 = u64 [r1 + 56]
    .D========================eER....................................................  r12 = r6 + r3
    .D=========================eER...................................................  r8 = r8 + r12
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r12 = u64 [r8 + 1544]
    ..DeE-------------------------------------------------R..........................  r11 = 0x1 << r11
    ..D==================================================eER.........................  r11 = r11 | r12
    ...D==================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r8 + 1544] = r11
    ...D======================eE----------------------------------------------------R  r6 = r6 + r3
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeE---------------------------R  r8 = u64 [r6 + 1848]
    ....DeE-------------------------------------------------------------------------R  r10 = 0x1 << r10
    ....D===============================================eE--------------------------R  r8 = r8 | r10
    .....D===============================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R  u64 [r6 + 1848] = r8
    .....DeeeeeeeeeeeeeeeE----------------------------------------------------------R  jump 31977
```

Gas simulation at offset 31974 with total cost of 2:

```
    D....  r2 = r4
    DeeER  fallthrough
```

Gas simulation at offset 31977 with total cost of 46:

```
    DeER.............................................  r8 = r0 << 0x5
    D=eeER...........................................  i32 r8 = r8 + r9
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................  r9 = u64 [r1 + 48]
    .D=========================eeeeeeeeeeeeeeeeeeeeER  jump 31116 if r8 >=u r9
```

Gas simulation at offset 31990 with total cost of 27:

```
    DeER..........................  r8 = r8 << 0x20
    D=eER.........................  r8 = r8 >> 0x20
    D==eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 0] = r2
    DeeeeeeeeeeeeeeeeeeeeeeeeeE--R  r5 = u64 [r1 + 56]
    .DeeeeeeeeeeeeeeeE-----------R  jump 31120
```

Gas simulation at offset 32004 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u64 [0x30008]
    D=========================eER  jump 32014 if r7 == 0
```

Gas simulation at offset 32012 with total cost of 22:

```
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 32014 with total cost of 2:

```
    DeeER  trap
```

Gas simulation at offset 32015 with total cost of 1:

```
    DeER  jump 32019 if r7 != 0
```

Gas simulation at offset 32018 with total cost of 2:

```
    DeeER  trap
```

Gas simulation at offset 32019 with total cost of 2:

```
    DeeER  trap
```

Gas simulation at offset 32020 with total cost of 2:

```
    DeeER  trap
```

Gas simulation at offset 32021 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xffffffffffffffb8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 64] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 56] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 48] = r6
    .DeE------------------------R  r9 = r9 + r8
    .D=eE-----------------------R  jump 32119 if r9 <u r8
```

Gas simulation at offset 32039 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    D..........................................  r5 = r7
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u64 [r7 + 0]
    DeE---------------------------------------R  r8 = 0x8
    .D========================eE--------------R  r10 = r7 << 0x1
    .DeeeE------------------------------------R  r8 = maxu(r9, r8)
    ..D========================eeeE-----------R  r6 = maxu(r8, r10)
    ..D===========================eE----------R  jump 32119 if r6 <s 0
```

Gas simulation at offset 32059 with total cost of 1:

```
    DeER  jump 32076 if r7 == 0
```

Gas simulation at offset 32062 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r8 = u64 [r5 + 8]
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 24] = r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  u64 [r1 + 40] = r7
    .DeE------------------------------------------------R  r7 = 0x1
    .DeeE-----------------------------------------------R  fallthrough
```

Gas simulation at offset 32076 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 32] = r7
    D...........................  r7 = r1
    DeE------------------------R  r9 = r1 + 0x18
    .D..........................  r8 = r6
    .DeeeeeeeeeeeeeeeE---------R  r0 = 924, jump 32130
```

Gas simulation at offset 32091 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u64 [r1 + 0]
    D=========================eER  jump 32124 if r7 != 0
```

Gas simulation at offset 32096 with total cost of 50:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER..........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  r7 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R..........  u64 [r5 + 0] = r6
    D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r5 + 8] = r7
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R  r0 = u64 [r1 + 64]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE------------------------R  r5 = u64 [r1 + 56]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 48]
    .D=========================eE-----------------------R  r1 = r1 + 0x48
    ..D========================eeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 32119 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeE---------------------------------------R  r7 = 0
    DeeeeeeeeeeeeeeeE-------------------------R  jump 32015
```

Gas simulation at offset 32124 with total cost of 40:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R  r7 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeE-------------------------R  jump 32015
```

Gas simulation at offset 32130 with total cost of 27:

```
    DeER..........................  r1 = r1 + 0xffffffffffffffe0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 24] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 16] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 8] = r6
    .D............................  r5 = r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r8 = u64 [r9 + 8]
    .D............................  r6 = r7
    .D=========================eER  jump 32172 if r8 == 0
```

Gas simulation at offset 32152 with total cost of 45:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.....  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.....  r7 = u64 [r9 + 16]
    D=========================eeeeeeeeeeeeeeeeeeeeER  jump 32236 if r7 == 0
```

Gas simulation at offset 32159 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u64 [r9 + 0]
    D...........................  r8 = r5
    DeeeeeeeeeeeeeeeE----------R  r0 = 926, jump 30817
```

Gas simulation at offset 32169 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 32329
```

Gas simulation at offset 32172 with total cost of 21:

```
    DeER....................  r7 = 0x1
    DeER....................  r8 = 0x1fffffffe0
    D=eeeeeeeeeeeeeeeeeeeeER  jump 32252 if r8 <u r5
```

Gas simulation at offset 32188 with total cost of 26:

```
    DeER.........................  r9 = 0x30a98
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r9
    D=eE------------------------R  r8 = r9 + 0x2750
    .D=eE-----------------------R  r8 = r8 & 0xfffffffffffffffc
    .DeeE-----------------------R  fallthrough
```

Gas simulation at offset 32203 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r7 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r9 = i32 [r8 + 0]
    .D=========================eE-------------R............  r4 = r9 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r9 = r9 & 0xff
    ..D=========================eE------------------------R  jump 32203 if r9 != 0
```

Gas simulation at offset 32234 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  jump 32302
```

Gas simulation at offset 32236 with total cost of 21:

```
    DeER....................  r7 = 0x1
    DeER....................  r8 = 0x1fffffffe0
    D=eeeeeeeeeeeeeeeeeeeeER  jump 32256 if r8 >=u r5
```

Gas simulation at offset 32252 with total cost of 15:

```
    DeER..............  r7 = 0
    DeeeeeeeeeeeeeeeER  jump 32329
```

Gas simulation at offset 32256 with total cost of 26:

```
    DeER.........................  r9 = 0x30a98
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r9
    D=eE------------------------R  r8 = r9 + 0x2750
    .D=eE-----------------------R  r8 = r8 & 0xfffffffffffffffc
    .DeeE-----------------------R  fallthrough
```

Gas simulation at offset 32271 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r7 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r9 = i32 [r8 + 0]
    .D=========================eE-------------R............  r4 = r9 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r9 = r9 & 0xff
    ..D=========================eE------------------------R  jump 32271 if r9 != 0
```

Gas simulation at offset 32302 with total cost of 16:

```
    DeER...............  r7 = r5 + 0x1f
    D=eER..............  r7 = r7 >> 0x5
    .D=eeER............  i32 r7 = r7 + 0
    .DeE--R............  r8 = 0
    .DeeeeeeeeeeeeeeeER  r0 = 928, jump 26445
```

Gas simulation at offset 32318 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r9 = u64 [r1 + 0]
    D=========================eER.........................  r8 = r9 + 0x2000
    D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r8 + 1872] = 0
    .DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 32329 with total cost of 52:

```
    DeeeER.................................................  r8 = r7 <u 0x1
    DeE--R.................................................  r9 = 0x1
    .DeeER.................................................  r9 = r7 if r7 != 0
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u64 [r6 + 0] = r8
    .D==eeeeeeeeeeeeeeeeeeeeeeeeeER........................  u64 [r6 + 8] = r9
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-R........................  u64 [r6 + 16] = r5
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-R........................  r0 = u64 [r1 + 24]
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 16]
    ..D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 8]
    ...D=========================eE-----------------------R  r1 = r1 + 0x20
    ...D========================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 32360 with total cost of 46:

```
    D................................................  r10 = r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r7 = u64 [r6 + 0]
    D=========================eER....................  r7 = r7 - r5
    D................................................  r8 = r5
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER....................  u64 [r1 + 8] = 0x2000
    .D=========================eeeeeeeeeeeeeeeeeeeeER  jump 32525 if r7 <u 8192
```

Gas simulation at offset 32380 with total cost of 26:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 0] = r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r7 = u64 [r6 + 8]
    D=========================eER  r7 = r7 + r8
    D............................  r8 = r10
    .DeeeeeeeeeeeeeeeE----------R  r0 = 930, jump 27909
```

Gas simulation at offset 32396 with total cost of 224:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.......................................................................................................................................................................................................  r8 = u8 [r6 + 92]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.......................................................................................................................................................................................................  r7 = u8 [r6 + 93]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.......................................................................................................................................................................................................  r12 = u8 [r6 + 94]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.......................................................................................................................................................................................................  r11 = u8 [r6 + 95]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................................................................................................................  r2 = u8 [r6 + 96]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................................................................................................................  r0 = u8 [r6 + 97]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................................................................................................................  r3 = u8 [r6 + 98]
    .D========================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................................................................................................................................................  r9 = u8 [r6 + 99]
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................................................................................................................  u64 [r1 + 16] = r9
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................................................................................................................  r9 = u64 [r1 + 0]
    ..D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................................................................................................................................................  r10 = u64 [r1 + 8]
    ..D=========================================================================eER....................................................................................................................................................  r9 = r9 + r10
    ...D=========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...........................................................................................................................  u64 [r6 + 16] = r9
    ...D===============================================eE--------------------------------------------------R...........................................................................................................................  r4 = r8 | 0x1
    ...D================================================eE-------------------------------------------------R...........................................................................................................................  r7 = r7 | 0x1
    ....D================================================eE------------------------------------------------R...........................................................................................................................  r9 = r12 | 0x1
    ....D=================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-----------------------R...........................................................................................................................  u32 [r6 + 24] = r5
    ....D=======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R...........................................................................................................................  u32 [r6 + 28] = r5
    .....D======================================================================eeeeeeeeeeeeeeeeeeeeeeeeeE-R...........................................................................................................................  u32 [r6 + 32] = r5
    .....D=========================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................................................................  u32 [r6 + 36] = r5
    .....D===============================================================================================eE--R.........................................................................................................................  r11 = r11 | 0x1
    ......D==============================================================================================eE--R.........................................................................................................................  r10 = r2 | 0x1
    ......D===============================================================================================eE-R.........................................................................................................................  r0 = r0 | 0x1
    .......D==============================================================================================eE-R.........................................................................................................................  r8 = r3 | 0x1
    .......D==============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..................................................................................................  u32 [r6 + 40] = r5
    .......D===============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................................  u32 [r6 + 44] = r5
    ........D==============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.................................................................................................  u32 [r6 + 48] = r5
    ........D===============================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER................................................................................................  u32 [r6 + 52] = r5
    ........D======================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................................................................  r12 = u64 [r1 + 16]
    ........D===============================================================================================================================================eER........................................................................  r12 = r12 | 0x1
    .........D======================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................................  u8 [r6 + 92] = t2
    .........D======================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER........................................................................  u8 [r6 + 93] = a0
    ............................D====================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.......................................................................  u8 [r6 + 94] = a2
    ............................D============================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u8 [r6 + 95] = a4
    ............................D============================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u8 [r6 + 96] = a3
    ............................D============================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER...............................................  u8 [r6 + 97] = ra
    .....................................................D====================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER..............................................  u8 [r6 + 98] = a1
    .....................................................D============================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  u8 [r6 + 99] = a5
    .....................................................D.............................................................................................................................................................................  r7 = r5
    .....................................................D============================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 40]
    ......................................................D===========================================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER......................  r5 = u64 [r1 + 32]
    ..............................................................................D====================================================================================================eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r6 = u64 [r1 + 24]
    ..............................................................................D============================================================================================================================eER.....................  r1 = r1 + 0x30
    ..............................................................................D============================================================================================================================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 32525 with total cost of 25:

```
    D...........................  r7 = r6
    D...........................  r8 = r5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r9 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 16] = r10
    .DeeeeeeeeeeeeeeeE---------R  r0 = 932, jump 32021
```

Gas simulation at offset 32541 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r10 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r9 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u64 [r6 + 16]
    DeeeeeeeeeeeeeeeE----------R  jump 32380
```

Gas simulation at offset 32553 with total cost of 20:

```
    D......................  r8 = r10
    DeeeeeeeeeeeeeeeeeeeeER  jump 32702 if r7 <=u 2047
```

Gas simulation at offset 32561 with total cost of 27:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..  r7 = u64 [r5 + 8]
    DeE------------------------R..  r9 = 0x800
    DeE------------------------R..  r10 = 0xffffffffffffd800
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.  u64 [r1 + 16] = r10
    .D========================eER.  r7 = r7 + r8
    .DeE------------------------R.  r8 = r8 + r9
    .D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r8
    .DeE-------------------------R  r8 = 0
    ..DeeeeeeeeeeeeeeeE----------R  r0 = 934, jump 27934
```

Gas simulation at offset 32592 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r7 = u8 [r5 + 100]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER..........................  r12 = u64 [r1 + 24]
    D=========================eER.........................  r10 = r12 + 0xffffffffffffe000
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r8 = u64 [r1 + 8]
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r5 + 16] = r8
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 56] = r10
    .DeE-------------------------------------------------R  jump 32680 if r6 == 0
```

Gas simulation at offset 32614 with total cost of 51:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...........  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r9 = u8 [r5 + 101]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R...........  r8 = u64 [r1 + 16]
    D=========================eE--------------R...........  r8 = r8 + r12
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...........  u32 [r5 + 60] = r10
    .D=========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 64] = r8
    .DeeE------------------------------------------------R  fallthrough
```

Gas simulation at offset 32631 with total cost of 76:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r10 = u8 [r5 + 102]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER...................................................  r11 = u8 [r5 + 103]
    DeE------------------------R...................................................  r7 = r7 | 0x3
    DeE------------------------R...................................................  r9 = r9 | 0x3
    .D========================eER..................................................  r10 = r10 | 0x3
    .D========================eER..................................................  r11 = r11 | 0x3
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u32 [r5 + 68] = r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER..................................................  u8 [r5 + 100] = a0
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r5 + 101] = a2
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r5 + 102] = a3
    ..D========================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  u8 [r5 + 103] = a4
    ..D............................................................................  r7 = r12
    ...D=======================eeeeeeeeeeeeeeeeeeeeeeeeeER.........................  r0 = u64 [r1 + 48]
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 40]
    ...D================================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 32]
    ...D================================================eE------------------------R  r1 = r1 + 0x38
    ....D===============================================eeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 32680 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r8 = u64 [r1 + 16]
    D=========================eE--------------R............  r8 = r8 + r12
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  r9 = u8 [r5 + 101]
    .D=========================eE-------------R............  r10 = r8 + 0x400
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 60] = r10
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r5 + 64] = r10
    ..DeeeeeeeeeeeeeeeE-----------------------------------R  jump 32631
```

Gas simulation at offset 32702 with total cost of 25:

```
    DeER........................  r9 = 0x800
    D...........................  r7 = r5
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u64 [r1 + 24]
    DeeeeeeeeeeeeeeeE----------R  r0 = 936, jump 32021
```

Gas simulation at offset 32717 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r8 = u64 [r5 + 16]
    DeeeeeeeeeeeeeeeE----------R  jump 32561
```

Gas simulation at offset 32723 with total cost of 45:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER....................  r8 = u64 [r7 + 0]
    D=========================eeeeeeeeeeeeeeeeeeeeER  jump 32810 if r8 == 0
```

Gas simulation at offset 32728 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r5
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R  r7 = u64 [r7 + 8]
    .DeE------------------------R  r5 = 0x30a98
    .D=eE-----------------------R  r8 = r5 + 0x2750
    .D==eE----------------------R  r8 = r8 & 0xfffffffffffffffc
    ..DeE-----------------------R  r9 = 0x1
    ..DeeE----------------------R  fallthrough
```

Gas simulation at offset 32755 with total cost of 52:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER............  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R............  u64 [0x30000] = r4
    DeE---------------------------------------R............  r4 = r9 << 0x20
    .DeE--------------------------------------R............  r4 = r4 >>a 0x20
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R............  r10 = i32 [r8 + 0]
    .D=========================eE-------------R............  r4 = r10 | r4
    .D==========================eeeeeeeeeeeeeeeeeeeeeeeeeER  u32 [r8 + 0] = r4
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------------------R  r4 = u64 [0x30000]
    ..D========================eE-------------------------R  r10 = r10 & 0xff
    ..D=========================eE------------------------R  jump 32755 if r10 != 0
```

Gas simulation at offset 32786 with total cost of 15:

```
    DeeeeeeeeeeeeeeeER  r0 = 940, jump 27252
```

Gas simulation at offset 32792 with total cost of 47:

```
    DeER..............................................  r7 = r5 + 0x2000
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER.....................  u8 [r7 + 1872] = 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeE-R.....................  r0 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r5 = u64 [r1 + 0]
    .DeE------------------------R.....................  r1 = r1 + 0x10
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 32810 with total cost of 22:

```
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 32812 with total cost of 57:

```
    DeER........................................................  r9 = r8 + 0xffffffffffffa000
    DeER........................................................  r10 = 0xe000
    D=eER.......................................................  r9 = r9 & r10
    .D=eER......................................................  r9 = r9 >> 0xb
    .D==eER.....................................................  r9 = r9 + r7
    .D===eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r9 = i32 [r9 + 72]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE---R............................  r7 = u64 [r7 + 8]
    ..D===========================eeER..........................  i32 r8 = r8 + r9
    ..D=============================eER.........................  r7 = r7 + r8
    ..D==============================eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 0]
    ...DeeeeeeeeeeeeeeeeeeeeeeE--------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 32846 with total cost of 31:

```
    DeER..............................  r10 = r8 + 0xffffffffffffa000
    D=eER.............................  r10 = r10 << 0x30
    D==eER............................  r10 = r10 >> 0x3d
    .D==eER...........................  r11 = r7 + r10
    .D===eeeeeeeeeeeeeeeeeeeeeeeeeER..  r11 = u8 [r11 + 104]
    .D============================eER.  r11 = r11 & 0x2
    ..D============================eER  jump 32891 if r11 == 0
```

Gas simulation at offset 32868 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...............  unlikely
    DeE---------------------------------------R...............  r10 = r10 << 0x2
    D=eE--------------------------------------R...............  r10 = r10 + r7
    D==eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R...............  r10 = i32 [r10 + 72]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...............  r7 = u64 [r7 + 8]
    .D==========================eeE-----------R...............  i32 r8 = r8 + r10
    .D============================eE----------R...............  r7 = r7 + r8
    ..D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 0] = a2
    ..DeeeeeeeeeeeeeeeeeeeeeeE-------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 32891 with total cost of 22:

```
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 32893 with total cost of 22:

```
    DeER.....................  r7 = 0
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 32897 with total cost of 22:

```
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 32899 with total cost of 63:

```
    DeER..............................................................  r9 = r8 >> 0xc
    .DeeeER...........................................................  r9 = r9 <u 0x3
    .DeE--R...........................................................  r10 = 0xfffffffffffff000
    ..D==eeER.........................................................  r10 = 0 if r9 != 0
    ..D====eER........................................................  r8 = r8 + r10
    ...D====eER.......................................................  r9 = r8 >> 0x8
    ...D=====eER......................................................  r9 = r9 & 0xfc
    ...D======eER.....................................................  r9 = r9 + r7
    ....D======eeeeeeeeeeeeeeeeeeeeeeeeeER............................  r9 = i32 [r9 + 24]
    ....DeeeeeeeeeeeeeeeeeeeeeeeeeE------R............................  r7 = u64 [r7 + 8]
    ....D===eE---------------------------R............................  r8 = zext16 r8
    .....D==============================eeER..........................  i32 r8 = r8 + r9
    .....D================================eER.........................  r7 = r7 + r8
    .....D=================================eeeeeeeeeeeeeeeeeeeeeeeeeER  r7 = u8 [r7 + 0]
    ......DeeeeeeeeeeeeeeeeeeeeeeE-----------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 32942 with total cost of 37:

```
    DeER....................................  r10 = r8 >> 0xc
    .DeeeER.................................  r10 = r10 <u 0x3
    .DeE--R.................................  r11 = 0xfffffffffffff000
    ..D==eeER...............................  r11 = 0 if r10 != 0
    ..D====eER..............................  r8 = r8 + r11
    ...D====eER.............................  r10 = r8 << 0x30
    ...D=====eER............................  r10 = r10 >> 0x3a
    ....D=====eER...........................  r11 = r7 + r10
    ....D======eeeeeeeeeeeeeeeeeeeeeeeeeER..  r11 = u8 [r11 + 92]
    ....D===============================eER.  r11 = r11 & 0x2
    .....D===============================eER  jump 33000 if r11 == 0
```

Gas simulation at offset 32975 with total cost of 55:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER...............  unlikely
    DeE---------------------------------------R...............  r10 = r10 << 0x2
    D=eE--------------------------------------R...............  r10 = r10 + r7
    D==eeeeeeeeeeeeeeeeeeeeeeeeeE-------------R...............  r10 = i32 [r10 + 24]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R...............  r7 = u64 [r7 + 8]
    .DeE--------------------------------------R...............  r8 = zext16 r8
    .D==========================eeE-----------R...............  i32 r8 = r8 + r10
    ..D===========================eE----------R...............  r7 = r7 + r8
    ..D============================eeeeeeeeeeeeeeeeeeeeeeeeeER  u8 [r7 + 0] = a2
    ..DeeeeeeeeeeeeeeeeeeeeeeE-------------------------------R  jump [r0 + 0]
```

Gas simulation at offset 33000 with total cost of 22:

```
    DeeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 33002 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r6
    .DeE------------------------R  r5 = 0x7fffffffffffffff
    .DeE------------------------R  r12 = 0x8010000000000000
    ..DeE-----------------------R  r11 = r7 & r5
    ..D=eE----------------------R  r10 = r11 + r12
    ...DeE----------------------R  r6 = 0x8010000000000001
    ...DeE----------------------R  r9 = r8 & r5
    ....DeeeeeeeeeeeeeeeeeeeeE--R  jump 33149 if r10 <u r6
```

Gas simulation at offset 33052 with total cost of 21:

```
    DeER....................  r12 = r12 + r9
    D=eeeeeeeeeeeeeeeeeeeeER  jump 33149 if r12 <u r6
```

Gas simulation at offset 33058 with total cost of 27:

```
    DeeeER........................  r9 = r11 <u r9
    D.............................  r10 = r7
    .D............................  r12 = r8
    .DeE-R........................  r2 = 0xfffffffffffff
    ..D=eeER......................  r10 = r8 if r9 == 0
    ..D=eeER......................  r12 = r7 if r9 == 0
    ...D==eER.....................  r9 = r12 << 0x1
    ...D==eER.....................  r11 = r10 << 0x1
    ....D==eER....................  r3 = r9 >> 0x35
    ....D==eER....................  r9 = r11 >> 0x35
    .....DeE-R....................  r4 = r12 & r2
    .....D==eeeeeeeeeeeeeeeeeeeeER  jump 33268 if r3 == 0
```

Gas simulation at offset 33100 with total cost of 20:

```
    DeER...................  r6 = r10 & r2
    DeeeeeeeeeeeeeeeeeeeeER  jump 33286 if r9 == 0
```

Gas simulation at offset 33107 with total cost of 22:

```
    DeER.....................  r11 = 0x8000000000000000
    DeER.....................  r8 = r8 ^ r7
    DeER.....................  r4 = r4 << 0x3
    .DeER....................  r10 = 0x1
    .DeER....................  r5 = 0x80000000000000
    ..DeER...................  r7 = r6 << 0x3
    ..D=eER..................  r7 = r7 | r5
    ..DeeeeeeeeeeeeeeeeeeeeER  jump 33188 if r3 != r9
```

Gas simulation at offset 33145 with total cost of 15:

```
    D.................  r10 = r7
    DeeeeeeeeeeeeeeeER  jump 33209
```

Gas simulation at offset 33149 with total cost of 21:

```
    DeER....................  r12 = 0x7ff0000000000000
    D=eeeeeeeeeeeeeeeeeeeeER  jump 33241 if r12 >=u r11
```

Gas simulation at offset 33162 with total cost of 3:

```
    DeER..  r7 = 0x8000000000000
    D=eER.  r8 = r11 | r7
    .DeeER  fallthrough
```

Gas simulation at offset 33176 with total cost of 25:

```
    D...........................  r7 = r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    DeE------------------------R  r1 = r1 + 0x10
    .DeeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 33188 with total cost of 21:

```
    DeER....................  r9 = r3 - r9
    D=eeeeeeeeeeeeeeeeeeeeER  jump 33209 if r9 >u 63
```

Gas simulation at offset 33195 with total cost of 8:

```
    DeeeER.....  i32 r10 = 0 - r9
    .D==eER....  r10 = r7 << r10
    ..D==eeeER.  r10 = r10 >u 0
    ...DeE---R.  r7 = r7 >> r9
    ...D====eER  r10 = r10 | r7
    ...DeeE---R  fallthrough
```

Gas simulation at offset 33209 with total cost of 21:

```
    DeER....................  r7 = r12 & r11
    DeER....................  r9 = r4 | r5
    .DeeeeeeeeeeeeeeeeeeeeER  jump 33300 if r8 <s 0
```

Gas simulation at offset 33218 with total cost of 22:

```
    DeER.....................  r8 = r10 + r9
    D=eER....................  r9 = r8 << 0x7
    .D=eeeeeeeeeeeeeeeeeeeeER  jump 33325 if r9 >=s 0
```

Gas simulation at offset 33227 with total cost of 16:

```
    DeER...............  r10 = r10 & 0x1
    DeER...............  r8 = r8 >> 0x1
    D=eER..............  r8 = r8 | r10
    DeE-R..............  r3 = r3 + 0x1
    .DeeeeeeeeeeeeeeeER  jump 33325
```

Gas simulation at offset 33241 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 33426 if r12 >=u r9
```

Gas simulation at offset 33245 with total cost of 26:

```
    DeER.........................  r7 = 0x8000000000000
    D=eER........................  r7 = r7 | r9
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    .DeE------------------------R  r1 = r1 + 0x10
    .DeeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 33268 with total cost of 23:

```
    DeER......................  r11 = clz r4
    D=eER.....................  r6 = r11 + 0x35
    .DeeER....................  r3 = 0xc - r11
    ..DeER....................  r4 = r4 << r6
    ..DeER....................  r6 = r10 & r2
    ...DeeeeeeeeeeeeeeeeeeeeER  jump 33107 if r9 != 0
```

Gas simulation at offset 33286 with total cost of 17:

```
    DeER................  r9 = clz r6
    D=eER...............  r11 = r9 + 0x35
    .DeeER..............  r9 = 0xc - r9
    ..DeER..............  r6 = r6 << r11
    ..DeeeeeeeeeeeeeeeER  jump 33107
```

Gas simulation at offset 33300 with total cost of 21:

```
    DeER....................  r8 = r9 - r10
    D=eeeeeeeeeeeeeeeeeeeeER  jump 33176 if r8 == 0
```

Gas simulation at offset 33306 with total cost of 21:

```
    DeER....................  r9 = r8 >> 0x37
    D=eeeeeeeeeeeeeeeeeeeeER  jump 33325 if r9 != 0
```

Gas simulation at offset 33312 with total cost of 16:

```
    DeER...............  r9 = clz r8
    D=eER..............  r9 = r9 + 0xfffffffffffffff8
    D==eER.............  r8 = r8 << r9
    .D=eER.............  r3 = r3 - r9
    .DeeeeeeeeeeeeeeeER  jump 33355
```

Gas simulation at offset 33325 with total cost of 21:

```
    DeER....................  r9 = 0x7fe
    D=eeeeeeeeeeeeeeeeeeeeER  jump 33355 if r9 >=s r3
```

Gas simulation at offset 33332 with total cost of 26:

```
    DeER.........................  r8 = 0x7ff0000000000000
    D=eER........................  r7 = r7 | r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    .DeE------------------------R  r1 = r1 + 0x10
    .DeeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 33355 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 33377 if r3 >s 0
```

Gas simulation at offset 33358 with total cost of 11:

```
    DeeeER........  i32 r9 = 0x1 - r3
    .DeE-R........  r3 = 0
    ..D=eeeER.....  i32 r10 = 0 - r9
    ...D===eER....  r10 = r8 << r10
    ....DeE--R....  r8 = r8 >> r9
    .....D==eeeER.  r9 = r10 >u 0
    .....D=====eER  r8 = r8 | r9
    ......DeeE---R  fallthrough
```

Gas simulation at offset 33377 with total cost of 29:

```
    DeER............................  r9 = r8 & 0x7
    DeER............................  r8 = r8 >> 0x3
    DeER............................  r3 = r3 << 0x34
    .DeER...........................  r8 = r8 & r2
    .DeeeER.........................  r10 = r9 <u 0x5
    ..DeE-R.........................  r7 = r3 | r7
    ..DeE-R.........................  r9 = r9 + 0xfffffffffffffffc
    ..D==eER........................  r10 = r10 ^ 0x1
    ..D=eE-R........................  r7 = r7 | r8
    ...D==eER.......................  r7 = r7 + r10
    ...DeeeER.......................  r8 = r9 <u 0x1
    ....D==eER......................  r8 = r8 & r7
    ....D===eER.....................  r7 = r7 + r8
    ....DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 8]
    ....DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    .....D=eE----------------------R  r1 = r1 + 0x10
    .....DeeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 33426 with total cost of 21:

```
    DeER....................  r12 = 0x7ff0000000000000
    D=eeeeeeeeeeeeeeeeeeeeER  jump 33480 if r11 != r12
```

Gas simulation at offset 33439 with total cost of 27:

```
    DeER..........................  r8 = r8 ^ r7
    DeER..........................  r9 = 0x8000000000000000
    D=eER.........................  r9 = r9 ^ r8
    .DeER.........................  r8 = 0x7ff8000000000000
    .D=eeER.......................  r8 = r7 if r9 != 0
    ..D...........................  r7 = r8
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 8]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ..DeE------------------------R  r1 = r1 + 0x10
    ...DeeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 33480 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 33176 if r9 == r12
```

Gas simulation at offset 33484 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 33501 if r11 == 0
```

Gas simulation at offset 33487 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 33058 if r9 != 0
```

Gas simulation at offset 33491 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    DeE------------------------R  r1 = r1 + 0x10
    DeeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 33501 with total cost of 26:

```
    DeER.........................  r10 = 0xffffffffffffffff
    D=eeER.......................  r7 = r10 if r9 != 0
    D===eER......................  r7 = r7 & r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    .DeE------------------------R  r1 = r1 + 0x10
    .DeeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 33520 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xfffffffffffffff8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r5
    DeE-------------------------R  r10 = r7 << 0x21
    .DeE------------------------R  r9 = 0xffffffff80000000
    .DeE------------------------R  r5 = r10 >> 0x21
    ..DeeE----------------------R  i32 r10 = r5 + 0xffffffff80800000
    ..DeE-----------------------R  r12 = 0xffffffff80800001
    ...DeeE---------------------R  r9 = r8 & ~r9
    ...D=eeeeeeeeeeeeeeeeeeeeE--R  jump 33704 if r10 <u r12
```

Gas simulation at offset 33556 with total cost of 22:

```
    DeeER....................  i32 r11 = r9 + 0xffffffff80800000
    D==eeeeeeeeeeeeeeeeeeeeER  jump 33704 if r11 <u -2139095039
```

Gas simulation at offset 33570 with total cost of 27:

```
    DeER..........................  r2 = 0x7fffff
    DeeeER........................  r9 = r5 <u r9
    .D............................  r10 = r7
    .D............................  r11 = r8
    .D==eeER......................  r10 = r8 if r9 == 0
    ..D=eeER......................  r11 = r7 if r9 == 0
    ..D===eER.....................  r9 = r11 << 0x21
    ...D==eER.....................  r12 = r10 << 0x21
    ...D===eER....................  r3 = r9 >> 0x38
    ....D==eER....................  r12 = r12 >> 0x38
    ....D=eE-R....................  r9 = r11 & r2
    ....D===eeeeeeeeeeeeeeeeeeeeER  jump 33751 if r3 == 0
```

Gas simulation at offset 33607 with total cost of 20:

```
    DeER...................  r5 = r10 & 0x7fffff
    DeeeeeeeeeeeeeeeeeeeeER  jump 33771 if r12 == 0
```

Gas simulation at offset 33616 with total cost of 22:

```
    DeER.....................  r4 = 0xffffffff80000000
    DeER.....................  r8 = r8 ^ r7
    DeER.....................  r7 = r9 << 0x3
    .DeER....................  r10 = 0x4000000
    .DeER....................  r9 = r5 << 0x3
    .D=eER...................  r9 = r9 | r10
    ..DeeeeeeeeeeeeeeeeeeeeER  jump 33665 if r3 == r12
```

Gas simulation at offset 33643 with total cost of 21:

```
    DeER....................  r12 = r3 - r12
    D=eeeeeeeeeeeeeeeeeeeeER  jump 33785 if r12 >u 31
```

Gas simulation at offset 33651 with total cost of 9:

```
    DeeeER......  i32 r5 = 0 - r12
    .D==eeER....  i32 r5 = r9 << r5
    ..D===eeeER.  r5 = r5 >u 0
    ...DeeE---R.  i32 r9 = r9 >> r12
    ...D=====eER  r9 = r9 | r5
    ....DeeE---R  fallthrough
```

Gas simulation at offset 33665 with total cost of 20:

```
    DeER...................  r11 = r11 & 0xffffffff80000000
    DeER...................  r7 = r7 | 0x4000000
    DeeeeeeeeeeeeeeeeeeeeER  jump 33803 if r8 <s 0
```

Gas simulation at offset 33680 with total cost of 23:

```
    DeeER.....................  i32 r8 = r9 + r7
    .D=eER....................  r7 = r8 << 0x24
    .D==eeeeeeeeeeeeeeeeeeeeER  jump 33828 if r7 >=s 0
```

Gas simulation at offset 33690 with total cost of 16:

```
    DeER...............  r9 = r9 & 0x1
    DeeER..............  i32 r8 = r8 >> 0x1
    D==eER.............  r8 = r8 | r9
    .DeE-R.............  r3 = r3 + 0x1
    .DeeeeeeeeeeeeeeeER  jump 33828
```

Gas simulation at offset 33704 with total cost of 21:

```
    DeER....................  r11 = 0x7f800000
    D=eeeeeeeeeeeeeeeeeeeeER  jump 33728 if r11 >=u r5
```

Gas simulation at offset 33713 with total cost of 2:

```
    DeER.  r8 = r5 | 0x400000
    DeeER  fallthrough
```

Gas simulation at offset 33719 with total cost of 25:

```
    D...........................  r7 = r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 0]
    DeE------------------------R  r1 = r1 + 0x8
    DeeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 33728 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 33920 if r9 <=u 2139095040
```

Gas simulation at offset 33736 with total cost of 25:

```
    DeER........................  r8 = 0x400000
    D=eER.......................  r7 = r9 | r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 0]
    .DeE-----------------------R  r1 = r1 + 0x8
    .DeeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 33751 with total cost of 23:

```
    DeER......................  i32 r5 = clz r9
    D=eER.....................  r4 = r5 + 0x18
    .DeeER....................  r3 = 0x9 - r5
    ..DeeER...................  i32 r9 = r9 << r4
    ...DeER...................  r5 = r10 & 0x7fffff
    ...DeeeeeeeeeeeeeeeeeeeeER  jump 33616 if r12 != 0
```

Gas simulation at offset 33771 with total cost of 17:

```
    DeER................  i32 r10 = clz r5
    D=eER...............  r4 = r10 + 0x18
    .DeeER..............  r12 = 0x9 - r10
    ..DeeER.............  i32 r5 = r5 << r4
    ..DeeeeeeeeeeeeeeeER  jump 33616
```

Gas simulation at offset 33785 with total cost of 20:

```
    DeER...................  r9 = 0x1
    DeER...................  r11 = r11 & 0xffffffff80000000
    DeER...................  r7 = r7 | 0x4000000
    DeeeeeeeeeeeeeeeeeeeeER  jump 33680 if r8 >=s 0
```

Gas simulation at offset 33803 with total cost of 22:

```
    DeeER....................  i32 r8 = r7 - r9
    D==eeeeeeeeeeeeeeeeeeeeER  jump 33719 if r8 == 0
```

Gas simulation at offset 33809 with total cost of 22:

```
    DeeER....................  i32 r7 = r8 >> 0x1a
    D==eeeeeeeeeeeeeeeeeeeeER  jump 33828 if r7 != 0
```

Gas simulation at offset 33815 with total cost of 17:

```
    DeER................  i32 r7 = clz r8
    D=eER...............  r7 = r7 + 0xfffffffffffffffb
    .D=eeER.............  i32 r8 = r8 << r7
    .D=eE-R.............  r3 = r3 - r7
    ..DeeeeeeeeeeeeeeeER  jump 33849
```

Gas simulation at offset 33828 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 33849 if r3 <=s 254
```

Gas simulation at offset 33833 with total cost of 25:

```
    DeER........................  r8 = 0x7f800000
    D=eER.......................  r7 = r11 | r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 0]
    .DeE-----------------------R  r1 = r1 + 0x8
    .DeeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 33849 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 33872 if r3 >s 0
```

Gas simulation at offset 33852 with total cost of 8:

```
    DeeeER.....  i32 r7 = 0x1 - r3
    .DeE-R.....  r3 = r3 + 0xffffffffffffffff
    ..DeeER....  i32 r9 = r8 << r3
    ...D=eeeER.  r9 = r9 >u 0
    ....DeeE-R.  i32 r8 = r8 >> r7
    ....D===eER  r8 = r8 | r9
    .....DeE--R  r3 = 0
    .....DeeE-R  fallthrough
```

Gas simulation at offset 33872 with total cost of 30:

```
    DeER.............................  r7 = r8 & 0x7
    DeER.............................  r8 = r8 >> 0x3
    DeER.............................  r3 = r3 << 0x17
    .DeER............................  r8 = r8 & 0x7fffff
    .DeeeER..........................  r9 = r7 <u 0x5
    ..DeE-R..........................  r10 = r3 | r11
    ..DeE-R..........................  r7 = r7 + 0xfffffffffffffffc
    ..D==eER.........................  r9 = r9 ^ 0x1
    ...DeE-R.........................  r8 = r8 | r10
    ...D==eER........................  r8 = r8 + r9
    ....DeeeER.......................  r7 = r7 <u 0x1
    ....D===eER......................  r7 = r7 & r8
    .....D===eeER....................  i32 r7 = r7 + r8
    .....DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 0]
    .....DeE------------------------R  r1 = r1 + 0x8
    ......DeeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 33920 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 33954 if r5 != 2139095040
```

Gas simulation at offset 33927 with total cost of 26:

```
    DeER.........................  r8 = r8 ^ r7
    D=eER........................  r9 = r8 ^ 0xffffffff80000000
    DeE-R........................  r8 = 0x7fc00000
    .D=eeER......................  r8 = r7 if r9 != 0
    .D...........................  r7 = r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 0]
    ..DeE-----------------------R  r1 = r1 + 0x8
    ..DeeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 33954 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 33719 if r9 == 2139095040
```

Gas simulation at offset 33962 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 33976 if r5 == 0
```

Gas simulation at offset 33965 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 33570 if r9 != 0
```

Gas simulation at offset 33969 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 0]
    DeE------------------------R  r1 = r1 + 0x8
    DeeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 33976 with total cost of 26:

```
    DeER.........................  r10 = 0xffffffffffffffff
    D=eeER.......................  r7 = r10 if r9 != 0
    D===eER......................  r7 = r7 & r8
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 0]
    .DeE------------------------R  r1 = r1 + 0x8
    .DeeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 33992 with total cost of 30:

```
    DeER.............................  r1 = r1 + 0xffffffffffffffe8
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....  u64 [r1 + 16] = r0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER....  u64 [r1 + 0] = r6
    .D...............................  r9 = r7
    .DeE------------------------R....  r2 = 0x7fffff
    .DeE------------------------R....  r12 = r7 << 0x21
    ..DeE-----------------------R....  r6 = r8 << 0x21
    ..D=eE----------------------R....  r7 = r7 ^ r8
    ..DeE-----------------------R....  r5 = 0xffffffff80000000
    ...D=eE---------------------R....  r4 = r12 >> 0x38
    ...D==eE--------------------R....  r0 = r6 >> 0x38
    ....D==eE-------------------R....  r7 = r7 & r5
    ....D===eE------------------R....  r11 = r9 & r2
    .....D===eE-----------------R....  r10 = r4 + 0xffffffffffffff01
    .....D====eE----------------R....  r3 = r8 & r2
    ......D====eeeeeeeeeeeeeeeeeeeeER  jump 34142 if r10 <u -254
```

Gas simulation at offset 34049 with total cost of 21:

```
    DeER....................  r10 = r0 + 0xffffffffffffff01
    D=eeeeeeeeeeeeeeeeeeeeER  jump 34142 if r10 <u -254
```

Gas simulation at offset 34058 with total cost of 2:

```
    D....  r10 = r11
    DeER.  r5 = 0
    DeeER  fallthrough
```

Gas simulation at offset 34063 with total cost of 29:

```
    DeER............................  r3 = r3 << 0x8
    DeER............................  r8 = r10 | 0x800000
    .DeER...........................  r9 = r3 | 0xffffffff80000000
    .DeER...........................  r8 = r8 << 0x20
    .D=eER..........................  r9 = r9 << 0x20
    ..D=eeeeER......................  r8 = r8 mulhu r9
    ...D====eER.....................  r9 = r8 >> 0x20
    ...DeE----R.....................  r11 = r0 + r4
    ....D====eER....................  r10 = r9 << 0x28
    ....DeE----R....................  r4 = r11 + r5
    .....D====eeeeeeeeeeeeeeeeeeeeER  jump 34174 if r10 <s 0
```

Gas simulation at offset 34102 with total cost of 4:

```
    DeER...  r11 = r4 + 0xffffffffffffff81
    .DeeER.  i32 r10 = r8 >> 0x1f
    .DeE-R.  r9 = r9 << 0x1
    ..D=eER  r9 = r9 | r10
    ..DeE-R  r8 = r8 << 0x1
    ..DeE-R  r10 = 0xfe
    ..D=eER  jump 34184 if r10 <s r11
```

Gas simulation at offset 34124 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 34274 if r11 <=s 0
```

Gas simulation at offset 34128 with total cost of 15:

```
    DeER..............  r9 = r9 & 0x7fffff
    DeER..............  r11 = r11 << 0x17
    D=eER.............  r9 = r9 | r11
    DeeeeeeeeeeeeeeeER  jump 34302
```

Gas simulation at offset 34142 with total cost of 21:

```
    DeER....................  r12 = r12 >> 0x21
    DeER....................  r6 = 0x7f800000
    D=eeeeeeeeeeeeeeeeeeeeER  jump 34207 if r6 >=u r12
```

Gas simulation at offset 34154 with total cost of 2:

```
    DeER.  r7 = r9 | 0x400000
    DeeER  fallthrough
```

Gas simulation at offset 34160 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 16]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r5 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r6 = u64 [r1 + 0]
    .DeE--------------------------------------R.......  r1 = r1 + 0x18
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 34174 with total cost of 2:

```
    DeER.  r11 = r4 + 0xffffffffffffff82
    DeER.  r10 = 0xfe
    D=eER  jump 34124 if r10 >=s r11
```

Gas simulation at offset 34184 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r8 = 0x7f800000
    D=eE--------------------------------------R.......  r7 = r7 | r8
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 0]
    .D=eE-------------------------------------R.......  r1 = r1 + 0x18
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 34207 with total cost of 3:

```
    DeeER.  r9 = r8 & ~r5
    D==eER  jump 34236 if r9 <=u 2139095040
```

Gas simulation at offset 34217 with total cost of 47:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER.......  unlikely
    DeE---------------------------------------R.......  r7 = r8 | 0x400000
    DeeeeeeeeeeeeeeeeeeeeeeeeeE---------------R.......  r0 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R.......  r6 = u64 [r1 + 0]
    .DeE--------------------------------------R.......  r1 = r1 + 0x18
    .D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 34236 with total cost of 2:

```
    DeER.  r8 = 0x7f800000
    D=eER  jump 34344 if r12 != r8
```

Gas simulation at offset 34245 with total cost of 48:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER........  unlikely
    DeE---------------------------------------R........  r8 = r7 | 0x7f800000
    DeE---------------------------------------R........  r7 = 0x7fc00000
    .DeeE-------------------------------------R........  r7 = r8 if r9 != 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R........  r0 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R........  r5 = u64 [r1 + 8]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R........  r6 = u64 [r1 + 0]
    ..D=eE------------------------------------R........  r1 = r1 + 0x18
    ..D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 34274 with total cost of 3:

```
    DeeER.  r10 = 0x1 - r11
    DeE-R.  r12 = 0x1f
    .D=eER  jump 34160 if r12 <u r10
```

Gas simulation at offset 34283 with total cost of 6:

```
    DeER.....  r11 = r11 + 0xffffffffffffffff
    .DeeER...  i32 r12 = r8 >> r10
    ..DeER...  r8 = r8 | r9
    ..D=eeER.  i32 r8 = r8 << r11
    ...D==eER  r8 = r8 | r12
    ...DeeE-R  i32 r9 = r9 >> r10
    ....DeeER  fallthrough
```

Gas simulation at offset 34302 with total cost of 50:

```
    DeER.................................................  r7 = r7 | r9
    DeeER................................................  i32 r8 = r8 + 0
    DeE-R................................................  r9 = 0xffffffff80000000
    .D=eeeER.............................................  r10 = r9 <u r8
    .D=eE--R.............................................  r8 = r8 ^ r9
    ..D===eER............................................  r7 = r7 + r10
    ..D=eeeER............................................  r8 = r8 <u 0x1
    ...D===eER...........................................  r8 = r8 & r7
    ...D====eeER.........................................  i32 r7 = r7 + r8
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeER......................  r0 = u64 [r1 + 16]
    ....DeeeeeeeeeeeeeeeeeeeeeeeeeER.....................  r5 = u64 [r1 + 8]
    ....D==eeeeeeeeeeeeeeeeeeeeeeeeeER...................  r6 = u64 [r1 + 0]
    ....D=====eE---------------------R...................  r1 = r1 + 0x18
    ....D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 34344 with total cost of 1:

```
    DeER  jump 34380 if r9 != 2139095040
```

Gas simulation at offset 34351 with total cost of 48:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER........  unlikely
    DeE---------------------------------------R........  r8 = r7 | 0x7f800000
    DeE---------------------------------------R........  r7 = 0x7fc00000
    .DeeE-------------------------------------R........  r7 = r8 if r12 != 0
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R........  r0 = u64 [r1 + 16]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeE--------------R........  r5 = u64 [r1 + 8]
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeE-------------R........  r6 = u64 [r1 + 0]
    ..D=eE------------------------------------R........  r1 = r1 + 0x18
    ..D========================eeeeeeeeeeeeeeeeeeeeeeER  jump [r0 + 0]
```

Gas simulation at offset 34380 with total cost of 1:

```
    DeER  jump 34160 if r12 == 0
```

Gas simulation at offset 34384 with total cost of 1:

```
    DeER  jump 34160 if r9 == 0
```

Gas simulation at offset 34388 with total cost of 21:

```
    DeER....................  r12 = r12 >> 0x17
    D=eeeeeeeeeeeeeeeeeeeeER  jump 34407 if r12 != 0
```

Gas simulation at offset 34394 with total cost of 18:

```
    DeER.................  i32 r8 = clz r11
    D=eER................  r12 = r8 + 0x18
    .DeeER...............  r5 = 0x9 - r8
    ..DeeER..............  i32 r10 = r11 << r12
    ...DeeeeeeeeeeeeeeeER  jump 34412
```

Gas simulation at offset 34407 with total cost of 2:

```
    D....  r10 = r11
    DeER.  r5 = 0
    DeeER  fallthrough
```

Gas simulation at offset 34412 with total cost of 21:

```
    DeER....................  r9 = r9 >> 0x17
    D=eeeeeeeeeeeeeeeeeeeeER  jump 34063 if r9 != 0
```

Gas simulation at offset 34419 with total cost of 17:

```
    DeER................  i32 r8 = clz r3
    D=eER...............  r9 = r8 + 0x18
    D=eER...............  r5 = r5 - r8
    .D=eeER.............  i32 r3 = r3 << r9
    .D=eE-R.............  r5 = r5 + 0x9
    ..DeeeeeeeeeeeeeeeER  jump 34063
```

Gas simulation at offset 34436 with total cost of 26:

```
    DeER.........................  r1 = r1 + 0xfffffffffffffff0
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 8] = r5
    D=eeeeeeeeeeeeeeeeeeeeeeeeeER  u64 [r1 + 0] = r6
    D............................  r9 = r7
    .DeE------------------------R  r3 = 0x7fffff
    .DeeE-----------------------R  i32 r12 = r7 >> 0x17
    ..DeE-----------------------R  r10 = r8 << 0x21
    ..D=eE----------------------R  r11 = r10 >> 0x38
    ...DeE----------------------R  r7 = r8 & 0xffffffff80000000
    ...D=eE---------------------R  r2 = r9 & r3
    ....DeE---------------------R  r4 = r8 & r3
    ....D=eeeeeeeeeeeeeeeeeeeeE-R  jump 34650 if r12 == 0
```

Gas simulation at offset 34476 with total cost of 21:

```
    DeER....................  r5 = r11 + 0xffffffffffffff01
    DeER....................  r6 = 0xffffffffffffff02
    D=eeeeeeeeeeeeeeeeeeeeER  jump 34650 if r5 <u r6
```

Gas simulation at offset 34488 with total cost of 2:

```
    DeER.  r9 = 0
    DeeER  fallthrough
```

Gas simulation at offset 34491 with total cost of 76:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeER....................................  unlikely
    DeE---------------------------------------R....................................  r12 = r12 - r11
    DeE---------------------------------------R....................................  r4 = r4 | 0x800000
    D=eE--------------------------------------R....................................  r9 = r9 + r12
    .DeE--------------------------------------R....................................  r8 = r2 | 0x800000
    ..DeeE------------------------------------R....................................  i32 r10 = r4 << 0x8
    ...D=eeE----------------------------------R....................................  r11 = 0x7504f333 - r10
    ....DeE-----------------------------------R....................................  r12 = r10 << 0x20
    ....D=eE----------------------------------R....................................  r10 = r12 >> 0x20
    .....D=eeeE-------------------------------R....................................  r10 = r11 * r10
    .....D====eE------------------------------R....................................  r10 = r10 >> 0x20
    ......D====eeeE---------------------------R....................................  i32 r10 = 0 - r10
    .......D======eE--------------------------R....................................  r10 = r10 << 0x20
    .......D=======eE-------------------------R....................................  r10 = r10 >> 0x20
    .......D========eeeE----------------------R....................................  r10 = r10 * r11
    .......D===========eE---------------------R....................................  r10 = r10 >> 0x1f
    ........D===========eE--------------------R....................................  r10 = r10 << 0x20
    .........D===========eeeeE----------------R....................................  r11 = r10 mulhu r12
    ..........D==============eE---------------R....................................  r11 = r11 >> 0x20
    ...........D==============eeeE------------R....................................  i32 r11 = 0 - r11
    ............D================eE-----------R....................................  r11 = r11 << 0x20
    .............D================eeeeE-------R....................................  r11 = r11 mulhu r10
    ..............DeE-------------------------R....................................  r10 = r8 << 0x1
    ..............D===================eE------R....................................  r11 = r11 >> 0x1f
    ..............D====================eE-----R....................................  r11 = r11 << 0x20
    ...............D====================eeeeE-R....................................  r12 = r11 mulhu r12
    ................D=======================eER....................................  r12 = r12 >> 0x20
    .................D=======================eeeER.................................  i32 r12 = 0 - r12
    ..................D=========================eER................................  r12 = r12 << 0x20
    ...................D=========================eeeeER............................  r11 = r12 mulhu r11
    ....................D============================eER...........................  r11 = r11 >> 0x1f
    ....................D=============================eER..........................  r11 = r11 + 0xfffffffffffffff4
    ...........................................D=======eER.........................  r11 = r11 << 0x20
    ...........................................DeE-------R.........................  r12 = r10 << 0x20
    ............................................D=======eeeeER.....................  r11 = r11 mulhu r12
    .............................................D==========eER....................  r12 = r11 >> 0x38
    .............................................D==========eER....................  r11 = r11 >> 0x20
    .............................................D===========eeeeeeeeeeeeeeeeeeeeER  jump 34677 if r12 != 0
```

Gas simulation at offset 34609 with total cost of 23:

```
    DeER......................  r2 = r2 << 0x18
    DeeeER....................  r8 = r4 * r11
    .D==eeER..................  i32 r12 = r2 - r8
    .DeE---R..................  r9 = r9 + 0x7e
    ..D.......................  r8 = r10
    ..DeE--R..................  r10 = 0xfe
    ..D=eeeeeeeeeeeeeeeeeeeeER  jump 34699 if r10 <s r9
```

Gas simulation at offset 34630 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 34748 if r9 <=s 0
```

Gas simulation at offset 34633 with total cost of 16:

```
    DeER...............  r8 = r11 & 0x7fffff
    DeER...............  r9 = r9 << 0x17
    D=eER..............  r9 = r9 | r8
    .DeER..............  r12 = r12 << 0x1
    .DeeeeeeeeeeeeeeeER  jump 34776
```

Gas simulation at offset 34650 with total cost of 21:

```
    DeER....................  r10 = r10 >> 0x21
    DeER....................  r5 = 0x7f800000
    D=eeeeeeeeeeeeeeeeeeeeER  jump 34719 if r5 >=u r10
```

Gas simulation at offset 34662 with total cost of 25:

```
    DeER........................  r7 = r8 | 0x400000
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    .DeE-----------------------R  r1 = r1 + 0x10
    .DeeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 34677 with total cost of 23:

```
    DeER......................  r9 = r9 + 0x7f
    DeER......................  r11 = r11 >> 0x1
    DeER......................  r2 = r2 << 0x17
    .DeeeER...................  r10 = r11 * r4
    ..D==eeER.................  i32 r12 = r2 - r10
    ..DeE---R.................  r10 = 0xfe
    ...DeeeeeeeeeeeeeeeeeeeeER  jump 34630 if r10 >=s r9
```

Gas simulation at offset 34699 with total cost of 2:

```
    DeER.  r8 = 0x7f800000
    D=eER  r7 = r7 | r8
    DeeER  fallthrough
```

Gas simulation at offset 34709 with total cost of 25:

```
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    DeE------------------------R  r1 = r1 + 0x10
    DeeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 34719 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 34709 if r10 == 2139095040
```

Gas simulation at offset 34726 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 34801 if r9 == 0
```

Gas simulation at offset 34729 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 34820 if r10 == 0
```

Gas simulation at offset 34732 with total cost of 20:

```
    DeeeeeeeeeeeeeeeeeeeeER  jump 34836 if r12 != 0
```

Gas simulation at offset 34735 with total cost of 17:

```
    DeER................  i32 r8 = clz r2
    D=eER...............  r5 = r8 + 0x18
    .DeeER..............  r9 = 0x9 - r8
    ..DeeER.............  i32 r2 = r2 << r5
    ..DeeeeeeeeeeeeeeeER  jump 34839
```

Gas simulation at offset 34748 with total cost of 21:

```
    DeER....................  r10 = 0xffffffffffffffe9
    D=eeeeeeeeeeeeeeeeeeeeER  jump 34709 if r9 <s r10
```

Gas simulation at offset 34754 with total cost of 12:

```
    DeER...........  r10 = r9 + 0x17
    .DeeeER........  i32 r12 = 0x1 - r9
    ..D==eeER......  i32 r9 = r11 >> r12
    ...DeeE-R......  i32 r8 = r8 << r10
    ....D==eeeER...  r10 = r4 * r9
    ....D=====eER..  r10 = r10 << 0x1
    .....D=====eeER  i32 r12 = r8 - r10
    .....DeeE-----R  fallthrough
```

Gas simulation at offset 34776 with total cost of 28:

```
    DeER...........................  r8 = r9 & 0x1
    D=eeER.........................  i32 r8 = r8 + r12
    .D==eeeER......................  r8 = r4 <u r8
    ..D====eeER....................  i32 r8 = r8 + r9
    ..D======eER...................  r7 = r7 | r8
    ..DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r5 = u64 [r1 + 8]
    ...DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    ...DeE------------------------R  r1 = r1 + 0x10
    ...DeeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 34801 with total cost of 26:

```
    DeER.........................  r8 = 0x7fc00000
    D=eeER.......................  r7 = r8 if r10 == 0
    DeeeeeeeeeeeeeeeeeeeeeeeeeER.  r5 = u64 [r1 + 8]
    .DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    .DeE------------------------R  r1 = r1 + 0x10
    .DeeeeeeeeeeeeeeeeeeeeeeE---R  jump [r0 + 0]
```

Gas simulation at offset 34820 with total cost of 25:

```
    DeER........................  r7 = r8 | 0x7f800000
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r5 = u64 [r1 + 8]
    DeeeeeeeeeeeeeeeeeeeeeeeeeER  r6 = u64 [r1 + 0]
    .DeE-----------------------R  r1 = r1 + 0x10
    .DeeeeeeeeeeeeeeeeeeeeeeE--R  jump [r0 + 0]
```

Gas simulation at offset 34836 with total cost of 2:

```
    DeER.  r9 = 0
    DeeER  fallthrough
```

Gas simulation at offset 34839 with total cost of 2:

```
    DeER.  r10 = r10 >> 0x17
    D=eER  jump 34491 if r10 != 0
```

Gas simulation at offset 34846 with total cost of 17:

```
    DeER................  i32 r8 = clz r4
    D=eER...............  r10 = r8 + 0x18
    D=eER...............  r8 = r8 + r9
    .D=eeER.............  i32 r4 = r4 << r10
    ..DeE-R.............  r9 = r8 + 0xfffffffffffffff7
    ..DeeeeeeeeeeeeeeeER  jump 34491
```

