# ArkUI_AccessibleGridItemInfo

```ets
typedef struct {...} ArkUI_AccessibleGridItemInfo
```

#### 概述

用于配置特定组件（如List、Flex、Select、Swiper组件）的属性值。

**起始版本：** 13

**相关模块：**[ArkUI_Accessibility](../security/ArkUI_Accessibility.md)

**所在头文件：**[native_interface_accessibility.h](../../capi/headers/native_interface_accessibility.h.md)

#### 汇总

#### 成员变量

名称描述bool heading是否是标题。true表示是标题，false表示不是标题。bool selected是否被选中。true表示被选中，false表示未被选中。int32_t columnIndex列下标。int32_t rowIndex行下标。int32_t columnSpan列跨度。int32_t rowSpan行跨度。