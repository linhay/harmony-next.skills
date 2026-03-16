# ArkUI_AccessibleGridInfo

```ets
typedef struct {...} ArkUI_AccessibleGridInfo
```

#### 概述

用于配置特定组件（如List、Flex、Select、Swiper组件）的网格布局属性。

**起始版本：** 13

**相关模块：**[ArkUI_Accessibility](../security/ArkUI_Accessibility.md)

**所在头文件：**[native_interface_accessibility.h](../../capi/headers/native_interface_accessibility.h.md)

#### 汇总

#### 成员变量

名称描述int32_t rowCount组件的行数。int32_t columnCount组件的列数。int32_t selectionMode值为0时表示仅选中网格的一行，非0值时表示选中网格的多行。