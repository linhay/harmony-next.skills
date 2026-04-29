# AREngine_ARAugmentedImageSource

**概述**

图像数据。

起始版本： 5.1.0(18)

相关模块： [AR Engine](AR Engine.md)

所在头文件： [ar_engine_core.h](ar_engine_core.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| const char *imageName | 图像名，不允许为空，255个字符以内，超过255个的字符将会被丢弃。 |
| const uint8_t *imageData | 灰度图像元素数组地址。 |
| int32_t pixelWidth | 图像像素宽度。 |
| int32_t pixelHeight | 图像像素高度。 |
| int32_t stride | 图像步幅。 |
| float realWidthInMeters | 图像中对象的实际物理宽度。无限制，默认值为A4纸张尺寸。 |

**结构体成员变量说明**

**imageName**

```ets
const char* AREngine_ARAugmentedImageSource::imageName
```

描述

图像名，不允许为空，255个字符以内，超过255个的字符将会被丢弃。

**imageData**

```ets
const uint8_t* AREngine_ARAugmentedImageSource::imageData
```

描述

灰度图像元素数组地址。

**pixelWidth**

```ets
int32_t AREngine_ARAugmentedImageSource::pixelWidth
```

描述

图像像素宽度。

**pixelHeight**

```ets
int32_t AREngine_ARAugmentedImageSource::pixelHeight
```

描述

图像像素高度。

**stride**

```ets
int32_t AREngine_ARAugmentedImageSource::stride
```

描述

图像步幅。

**realWidthInMeters**

```ets
float AREngine_ARAugmentedImageSource::realWidthInMeters
```

描述

图像中对象的实际物理宽度。无限制，默认值为A4纸张尺寸。