# @ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义)

ConfigurationConstant模块提供了[Configuration](@ohos.app.ability.Configuration (环境变量).md)操作相关的系统预置枚举。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { ConfigurationConstant } from '@kit.AbilityKit';
```

#### ColorMode

表示深浅色模式的枚举，用于[Configuration.colorMode](@ohos.app.ability.Configuration (环境变量).md#ZH-CN_TOPIC_0000002522240556__configuration)字段。开发者可以使用这些预置枚举设置或获取系统/应用的深浅色模式。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLOR_MODE_NOT_SET | -1 | 表示未设置颜色模式。 |
| COLOR_MODE_DARK | 0 | 表示深色模式。 |
| COLOR_MODE_LIGHT | 1 | 表示浅色模式。 |

#### Direction

表示屏幕方向的枚举，用于[Configuration.direction](@ohos.app.ability.Configuration (环境变量).md#ZH-CN_TOPIC_0000002522240556__configuration)字段。开发者可以使用这些预置枚举设置或获取系统/应用的显示方向。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DIRECTION_NOT_SET | -1 | 表示未设置方向。 |
| DIRECTION_VERTICAL | 0 | 表示垂直方向。 |
| DIRECTION_HORIZONTAL | 1 | 表示水平方向。 |

#### ScreenDensity

表示屏幕像素密度的枚举，用于[Configuration.screenDensity](@ohos.app.ability.Configuration (环境变量).md#ZH-CN_TOPIC_0000002522240556__configuration)字段。开发者可以使用这些预置枚举设置或获取屏幕的像素密度。

字体显示大小与屏幕像素密度呈正相关关系。通过监听屏幕像素密度变化，可以感知字体显示大小的调整。通常情况下，对于相同的物理尺寸，屏幕像素密度越高，字体显示效果越大。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCREEN_DENSITY_NOT_SET | 0 | 表示未设置屏幕像素密度。 |
| SCREEN_DENSITY_SDPI | 120 | 表示屏幕像素密度为'SDPI'。 |
| SCREEN_DENSITY_MDPI | 160 | 表示屏幕像素密度为'MDPI'。 |
| SCREEN_DENSITY_LDPI | 240 | 表示屏幕像素密度为'LDPI'。 |
| SCREEN_DENSITY_XLDPI | 320 | 表示屏幕像素密度为'XLDPI'。 |
| SCREEN_DENSITY_XXLDPI | 480 | 表示屏幕像素密度为'XXLDPI'。 |
| SCREEN_DENSITY_XXXLDPI | 640 | 表示屏幕像素密度为'XXXLDPI'。 |