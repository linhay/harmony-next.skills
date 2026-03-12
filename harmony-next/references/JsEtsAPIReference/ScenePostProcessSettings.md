# ScenePostProcessSettings

本模块提供3D图形中的色调映射等图像后处理方法。

- 本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标标记接口的起始版本。

#### 导入模块

```ets
import { ToneMappingType, ToneMappingSettings, BloomSettings, PostProcessSettings } from '@kit.ArkGraphics3D';
```

#### ToneMappingType

色调映射类型枚举。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称值说明ACES0ACES类型。ACES_20201ACES_2020类型。FILMIC2FILMIC类型。

#### ToneMappingSettings

色调映射设置。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明type[ToneMappingType](#ZH-CN_TOPIC_0000002529446041__tonemappingtype)否是色调映射类型，默认值为undefined。exposurenumber否是曝光度，取值大于0，默认值为undefined。

#### BloomSettings18+

泛光设置。当[RenderingPipelineType](SceneType.md#ZH-CN_TOPIC_0000002497446096__renderingpipelinetype21)为FORWARD_LIGHTWEIGHT时，此功能不可用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明thresholdHardnumber否是硬阈值，取值范围是非负数，默认值为1.0。thresholdSoftnumber否是软阈值，取值范围是非负数，默认值为2.0。scaleFactornumber否是缩放因子，取值范围大于0，默认值为1.0。scatternumber否是扩散量，取值范围大于0，默认值为1.0。

#### VignetteSettings22+

边缘暗角设置。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明roundnessnumber否是作用范围，取值范围为0到1之间，取值为1时作用范围为全局，默认值为sqrt(0.5)。intensitynumber否是作用强度，默认值为0.4。

#### ColorFringeSettings22+

色晕设置。当[RenderingPipelineType](SceneType.md#ZH-CN_TOPIC_0000002497446096__renderingpipelinetype21)为FORWARD_LIGHTWEIGHT时，此功能不可用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明intensitynumber否是作用强度，取值范围为0到1之间，默认值为0.2。

#### PostProcessSettings

后处理设置。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明toneMapping[ToneMappingSettings](#ZH-CN_TOPIC_0000002529446041__tonemappingsettings)否是色调映射，默认值为undefined。bloom18+[BloomSettings](#ZH-CN_TOPIC_0000002529446041__bloomsettings18)否是泛光，默认值为undefined。vignette22+[VignetteSettings](#ZH-CN_TOPIC_0000002529446041__vignettesettings22)否是边缘暗角，默认值为undefined。colorFringe22+[ColorFringeSettings](#ZH-CN_TOPIC_0000002529446041__colorfringesettings22)否是色晕，默认值为undefined。