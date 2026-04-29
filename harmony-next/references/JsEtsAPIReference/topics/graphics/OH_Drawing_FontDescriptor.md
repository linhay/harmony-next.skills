# OH_Drawing_FontDescriptor

```ets
typedef struct OH_Drawing_FontDescriptor {...} OH_Drawing_FontDescriptor
```

#### 概述

描述系统字体详细信息的结构体。

**起始版本：** 12

**相关模块：**[Drawing](Drawing.md)

所在头文件： [drawing_text_typography.h](drawing_text_typography.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| char* path | 系统字体的文件路径。 |
| char* postScriptName | 唯一标识字体的名称。 |
| char* fullName | 系统字体的名称。 |
| char* fontFamily | 系统字体的字体家族。 |
| char* fontSubfamily | 系统字体的子字体家族。 |
| int weight | 系统字体的粗细程度。 |
| int width | 系统字体的宽窄风格属性。 |
| int italic | 系统字体倾斜度。 |
| bool monoSpace | 系统字体是否紧凑。true表示字体紧凑，false表示字体非紧凑。 |
| bool symbolic | 系统字体是否支持符号字体。true表示支持符号字体，false表示不支持符号字体。 |