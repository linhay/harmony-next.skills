# JSVM_VMInfo

```ets
typedef struct {...} JSVM_VMInfo
```

#### 概述

JavaScript虚拟机信息。

**起始版本：** 11

**相关模块：**[JSVM](JSVM.md)

所在头文件： [jsvm_types.h](jsvm_types.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32_t apiVersion | 此虚拟机支持的最高API版本。 |
| const char* engine | 实现虚拟机的引擎名称。 |
| const char* version | 虚拟机的版本。 |
| uint32_t cachedDataVersionTag | 缓存数据版本标签。 |