# VkNativeBufferFormatPropertiesOHOS

```ets
typedef struct VkNativeBufferFormatPropertiesOHOS {...} VkNativeBufferFormatPropertiesOHOS
```

#### 概述

包含了NativeBuffer的一些格式属性。

**起始版本：** 10

相关模块： [Vulkan](Vulkan.md)

所在头文件： [vulkan_ohos.h](vulkan_ohos.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| void* pNext | 下一级结构体指针。 |
| VkFormat format | 格式说明。 |
| uint64_t externalFormat | 外部定义的格式标识符。 |
| VkFormatFeatureFlags formatFeatures | 描述了与externalFormat对应的能力。 |
| VkComponentMapping samplerYcbcrConversionComponents | 表示一组VkComponentSwizzle。 |
| VkSamplerYcbcrModelConversion suggestedYcbcrModel | 色彩模型。 |
| VkSamplerYcbcrRange suggestedYcbcrRange | 色彩数值范围。 |
| VkChromaLocation suggestedXChromaOffset | X色度偏移。 |
| VkChromaLocation suggestedYChromaOffset | Y色度偏移。 |