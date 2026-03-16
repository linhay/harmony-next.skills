[]()[]()

# Types

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### HdrMetadataValue12+

type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata

PixelMap使用的HDR元数据值类型，和[HdrMetadataKey](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__hdrmetadatakey12)关键字相对应。

**系统能力：** SystemCapability.Multimedia.Image.Core

类型说明[HdrMetadataType](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__hdrmetadatatype12)[HdrMetadataKey](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__hdrmetadatakey12)中HDR_GAINMAP_METADATA关键字对应的元数据值类型。[HdrStaticMetadata](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__hdrstaticmetadata12)[HdrMetadataKey](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__hdrmetadatakey12)中HDR_STATIC_METADATA关键字对应的元数据值类型。ArrayBuffer[HdrMetadataKey](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__hdrmetadatakey12)中HDR_DYNAMIC_METADATA关键字对应的元数据值类型。[HdrGainmapMetadata](../../types/interfaces/Interfaces (其他) (arkts-apis-image-i).md#ZH-CN_TOPIC_0000002497445866__hdrgainmapmetadata12)[HdrMetadataKey](Enums (arkts-apis-image-e).md#ZH-CN_TOPIC_0000002529285837__hdrmetadatakey12)中HDR_GAINMAP_METADATA关键字对应的元数据值类型。