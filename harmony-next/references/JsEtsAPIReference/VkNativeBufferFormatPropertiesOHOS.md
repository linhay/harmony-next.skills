# VkNativeBufferFormatPropertiesOHOS

```ets
typedef struct VkNativeBufferFormatPropertiesOHOS {...} VkNativeBufferFormatPropertiesOHOS
```

#### 概述

包含了NativeBuffer的一些格式属性。

**起始版本：** 10

**相关模块：**[Vulkan](Vulkan.md)

**所在头文件：**[vulkan_ohos.h](vulkan_ohos.h.md)

#### 汇总

#### 成员变量

名称描述VkStructureType sType结构体类型。void* pNext下一级结构体指针。VkFormat format格式说明。uint64_t externalFormat外部定义的格式标识符。VkFormatFeatureFlags formatFeatures描述了与externalFormat对应的能力。VkComponentMapping samplerYcbcrConversionComponents表示一组VkComponentSwizzle。VkSamplerYcbcrModelConversion suggestedYcbcrModel色彩模型。VkSamplerYcbcrRange suggestedYcbcrRange色彩数值范围。VkChromaLocation suggestedXChromaOffsetX色度偏移。VkChromaLocation suggestedYChromaOffsetY色度偏移。