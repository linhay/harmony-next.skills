# ArkUI_ExpectedFrameRateRange

```ets
typedef struct {...} ArkUI_ExpectedFrameRateRange
```

#### 概述

设置动画的期望帧率。

**起始版本：** 12

**相关模块：**[ArkUI_NativeModule](ArkUI_NativeModule.md)

**所在头文件：**[native_animate.h](native_animate.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t min期望的最小帧率，单位为帧/秒（fps）。uint32_t max期望的最大帧率，单位为帧/秒（fps）。uint32_t expected期望的最优帧率，单位为帧/秒（fps）。