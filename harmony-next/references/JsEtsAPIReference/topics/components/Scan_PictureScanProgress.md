# Scan_PictureScanProgress

```ets
typedef struct {...} Scan_PictureScanProgress
```

#### 概述

表示扫描仪扫描图片的进度

**起始版本：** 12

**相关模块：**[OH_Scan](../misc/OH_Scan.md)

**所在头文件：**[ohscan.h](../../capi/headers/ohscan.h.md)

#### 汇总

#### 成员变量

名称描述int32_t progress图片进度，从0到100int32_t fd扫描仪文件句柄bool isFinal指示该图像是否为最后扫描的图像。true表示该图像是最后扫描的图像，false表示该图像不是最后扫描的图像。