# Print_PrinterInfo

```ets
typedef struct {...} Print_PrinterInfo
```

**概述**

表示打印机信息。

起始版本： 12

相关模块： [OH_Print](OH_Print.md)

所在头文件： [ohprint.h](ohprint.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Print_PrinterState printerState | 打印机状态。 |
| Print_PrinterCapability capability | 打印机能力。 |
| Print_DefaultValue defaultValue | 打印机当前属性。 |
| bool isDefaultPrinter | 默认打印机。 |
| char *printerId | 打印机 ID。 |
| char *printerName | 打印机名称。 |
| char *description | 打印机描述。 |
| char *location | 打印机位置。 |
| char *makeAndModel | 打印机品牌和型号信息。 |
| char *printerUri | 打印机 URI。 |
| char *detailInfo | JSON 格式的详细信息。 |