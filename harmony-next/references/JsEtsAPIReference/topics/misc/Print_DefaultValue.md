# Print_DefaultValue

```ets
typedef struct {...} Print_DefaultValue
```

**概述**

表示当前属性。

起始版本： 12

相关模块： [OH_Print](OH_Print.md)

所在头文件： [ohprint.h](ohprint.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Print_ColorMode defaultColorMode | 默认色彩模式。 |
| Print_DuplexMode defaultDuplexMode | 默认双面模式。 |
| char *defaultMediaType | 默认介质类型。 |
| char *defaultPageSizeId | 默认纸张尺寸 ID。 |
| Print_Margin defaultMargin | 默认边距。 |
| char *defaultPaperSource | 默认纸张来源。 |
| Print_Quality defaultPrintQuality | 默认打印质量。 |
| uint32_t defaultCopies | 默认份数。 |
| Print_Resolution defaultResolution | 默认打印机分辨率。 |
| Print_OrientationMode defaultOrientation | 默认方向。 |
| char *otherDefaultValues | JSON 格式的其他默认值。 |