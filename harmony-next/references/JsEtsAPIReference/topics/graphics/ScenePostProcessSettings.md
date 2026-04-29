# ScenePostProcessSettings

本模块提供3D图形中的色调映射等图像后处理方法。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标标记接口的起始版本。

**导入模块**

```ets
import { ToneMappingType, ToneMappingSettings, BloomSettings, PostProcessSettings } from '@kit.ArkGraphics3D';
```

**ToneMappingType**

色调映射类型枚举。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACES | 0 | ACES类型。 |
| ACES_2020 | 1 | ACES_2020类型。 |
| FILMIC | 2 | FILMIC类型。 |

**ToneMappingSettings**

色调映射设置。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | ToneMappingType | 否 | 是 | 色调映射类型，默认值为undefined。 |
| exposure | number | 否 | 是 | 曝光度，取值大于0，默认值为undefined。 |

**BloomSettings18+**

泛光设置。当[RenderingPipelineType](SceneType.md#ZH-CN_TOPIC_0000002522242228__renderingpipelinetype21)为FORWARD_LIGHTWEIGHT时，此功能不可用。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| thresholdHard | number | 否 | 是 | 硬阈值，取值范围是非负数，默认值为1.0。 |
| thresholdSoft | number | 否 | 是 | 软阈值，取值范围是非负数，默认值为2.0。 |
| scaleFactor | number | 否 | 是 | 缩放因子，取值范围大于0，默认值为1.0。 |
| scatter | number | 否 | 是 | 扩散量，取值范围大于0，默认值为1.0。 |

**VignetteSettings22+**

边缘暗角设置。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| roundness | number | 否 | 是 | 作用范围，取值范围为0到1之间，取值为1时作用范围为全局，默认值为sqrt(0.5)。 |
| intensity | number | 否 | 是 | 作用强度，默认值为0.4。 |

**ColorFringeSettings22+**

色晕设置。当[RenderingPipelineType](SceneType.md#ZH-CN_TOPIC_0000002522242228__renderingpipelinetype21)为FORWARD_LIGHTWEIGHT时，此功能不可用。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| intensity | number | 否 | 是 | 作用强度，取值范围为0到1之间，默认值为0.2。 |

**PostProcessSettings**

后处理设置。

系统能力： SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| toneMapping | ToneMappingSettings | 否 | 是 | 色调映射，默认值为undefined。 |
| bloom18+ | BloomSettings | 否 | 是 | 泛光，默认值为undefined。 |
| vignette22+ | VignetteSettings | 否 | 是 | 边缘暗角，默认值为undefined。 |
| colorFringe22+ | ColorFringeSettings | 否 | 是 | 色晕，默认值为undefined。 |