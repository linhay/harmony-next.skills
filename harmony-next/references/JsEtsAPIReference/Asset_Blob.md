# Asset_Blob

```ets
typedef struct {...} Asset_Blob
```

#### 概述

二进制数组类型，即不定长的字节数组。

**起始版本：** 11

**相关模块：**[AssetType](AssetType.md)

**所在头文件：**[asset_type.h](asset_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t size表示字节数组的大小。uint8_t *data指向字节数组的指针。