# Region

```ets
typedef struct {...} Region
```

#### 概述

表示本地窗口OHNativeWindow需要更新内容的矩形区域（脏区）。

**起始版本：** 8

**相关模块：**[NativeWindow](NativeWindow.md)

**所在头文件：**[external_window.h](../../capi/headers/external_window.h.md)

#### 汇总

#### 成员变量

名称描述* rects如果rects是空指针nullptr，默认Buffer大小为脏区。int32_t rectNumber如果rectNumber为0，默认Buffer大小为脏区。