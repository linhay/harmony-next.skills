# RawFileDescriptor64

```ets
typedef struct {...} RawFileDescriptor64
```

#### 概述

提供较大rawfile文件描述符信息。RawFileDescriptor64是[OH_ResourceManager_GetRawFileDescriptor64](../../capi/headers/raw_file.h.md#ZH-CN_TOPIC_0000002529445289__oh_resourcemanager_getrawfiledescriptor64)的输出参数,涵盖了rawfile文件的文件描述符以及在HAP包中的起始位置和长度。

**起始版本：** 11

**相关模块：**[rawfile](rawfile.md)

**所在头文件：**[raw_file.h](../../capi/headers/raw_file.h.md)

#### 汇总

#### 成员变量

名称描述int fdrawfile文件描述符，单位为int。int64_t startrawfile在HAP包中的起始位置，单位为int64_t。int64_t lengthrawfile在HAP包中的长度，单位为int64_t。