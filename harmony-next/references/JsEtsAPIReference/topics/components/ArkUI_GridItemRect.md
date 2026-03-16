# ArkUI_GridItemRect

```ets
typedef struct {...} ArkUI_GridItemRect
```

#### 概述

定义Grid布局选项onGetRectByIndex回调返回值结构体。

**起始版本：** 22

**相关模块：**[ArkUI_NativeModule](../system-services/ArkUI_NativeModule.md)

**所在头文件：**[native_type.h](../../capi/headers/native_type.h.md)

**相关示例：**[native_type_sample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUIKit/NativeTypeSample)

#### 汇总

#### 成员变量

名称描述uint32_t rowStartGridItem行起始位置。uint32_t columnStartGridItem列起始位置。uint32_t rowSpanGridItem占用的行数。uint32_t columnSpanGridItem占用的列数。