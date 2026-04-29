# Scan_ScannerOptions

```ets
typedef struct {...} Scan_ScannerOptions
```

#### 概述

表示一个扫描仪的所有参数选项

**起始版本：** 12

**相关模块：**[OH_Scan](OH_Scan.md)

所在头文件： [ohscan.h](ohscan.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| char** titles | 选项标题 |
| char** descriptions | 选项描述 |
| char** ranges | 选项可设置的范围 |
| int32_t optionCount | 可设置的参数选项数量 |