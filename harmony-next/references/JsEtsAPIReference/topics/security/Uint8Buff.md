# Uint8Buff

**概述**

定义uint8_t字节流。

起始版本： 6.0.0(20)

相关模块： [FIDO2](通行密钥.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t length | 字节流的长度。 |
| uint8_t * val | 字节流的值。 |

**结构体成员变量说明**

**length**

```ets
uint32_t Uint8Buff::length
```

描述

字节流的长度。

**val**

```ets
uint8_t* Uint8Buff::val
```

描述

字节流的值。