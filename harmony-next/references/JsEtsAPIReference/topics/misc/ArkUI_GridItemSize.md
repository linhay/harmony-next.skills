# ArkUI_GridItemSize

```ets
typedef struct {...} ArkUI_GridItemSize
```

**概述**

定义Grid布局选项onGetIrregularSizeByIndex回调返回值结构体。

起始版本： 22

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

所在头文件： [native_type.h](native_type.h.md)

相关示例： [native_type_sample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeTypeSample)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t rowSpan | GridItem占用的行数。 |
| uint32_t columnSpan | GridItem占用的列数。 |