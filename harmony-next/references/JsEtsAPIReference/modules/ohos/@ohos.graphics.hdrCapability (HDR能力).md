# @ohos.graphics.hdrCapability (HDR能力)

本模块提供HDR（高动态显示范围）能力涉及到的相关枚举类型。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { hdrCapability } from '@kit.ArkGraphics2D';
```

#### HDRFormat

HDR格式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不支持HDR类型。 |
| VIDEO_HLG | 1 | 支持视频的HLG格式。 |
| VIDEO_HDR10 | 2 | 支持视频的HDR10格式。 |
| VIDEO_HDR_VIVID | 3 | 支持视频的HDR_VIVID格式。 |
| IMAGE_HDR_VIVID_DUAL | 4 | 支持图片的HDR_VIVID格式，以dual JPEG格式存储。 |
| IMAGE_HDR_VIVID_SINGLE | 5 | 支持图片的HDR_VIVID格式，以single HEIF格式存储。 |
| IMAGE_HDR_ISO_DUAL | 6 | 支持图片的HDR_ISO格式，以dual JPEG格式存储。 |
| IMAGE_HDR_ISO_SINGLE | 7 | 支持图片的HDR_ISO格式，以single HEIF格式存储。 |