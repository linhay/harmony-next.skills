# @ohos.app.ability.Configuration (环境变量)

定义了应用运行时的环境变量，包含语言、深浅色、屏幕方向、字体等。开发者可以通过订阅环境变量，适配不同用户偏好，提升交互体验。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { Configuration } from '@kit.AbilityKit';
```

#### Configuration

**系统能力**：SystemCapability.Ability.AbilityBase

名称类型只读可选说明languagestring否是

表示应用当前语言，例如“zh"(中文)，“en”（英文）。

支持开发者[设置应用语言](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-system-environment-variable-changes#设置应用语言)。

取值范围参考[获取系统支持的语言列表](@ohos.i18n (国际化-I18n).md#ZH-CN_TOPIC_0000002529445281__getsystemlanguages9)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

colorMode[ConfigurationConstant.ColorMode](@ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义).md#ZH-CN_TOPIC_0000002497604608__colormode)否是

表示应用深浅色模式，默认为浅色。

支持开发者[设置应用或组件深浅色](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-system-environment-variable-changes#设置深浅色模式)。

取值范围：

- COLOR_MODE_NOT_SET：未设置

- COLOR_MODE_LIGHT：浅色模式

- COLOR_MODE_DARK：深色模式

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

direction[ConfigurationConstant.Direction](@ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义).md#ZH-CN_TOPIC_0000002497604608__direction)否是

表示应用屏幕方向。

取值范围：

- DIRECTION_NOT_SET：未设置

- DIRECTION_HORIZONTAL：水平方向

- DIRECTION_VERTICAL：垂直方向

该环境变量支持在[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)组件和[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)组件中订阅，不支持在[ApplicationContext](ApplicationContext (应用上下文).md)和[AbilityStage](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md)组件容器中订阅。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

screenDensity[ConfigurationConstant.ScreenDensity](@ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义).md#ZH-CN_TOPIC_0000002497604608__screendensity)否是

表示屏幕显示密度。

取值范围：

- SCREEN_DENSITY_NOT_SET：未设置

- SCREEN_DENSITY_SDPI：120

- SCREEN_DENSITY_MDPI：160

- SCREEN_DENSITY_LDPI：240

- SCREEN_DENSITY_XLDPI：320

- SCREEN_DENSITY_XXLDPI：480

- SCREEN_DENSITY_XXXLDPI：640

字体显示大小与屏幕像素密度呈正相关关系。通过监听屏幕像素密度变化，可以感知字体显示大小的调整。通常情况下，对于相同的物理尺寸，屏幕像素密度越高，字体显示效果越大。

该环境变量支持在[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)组件和[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)组件中订阅，不支持在[ApplicationContext](ApplicationContext (应用上下文).md)和[AbilityStage](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md)组件容器中订阅。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

displayIdnumber否是

表示应用所在的物理屏幕ID。

该环境变量支持在[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)组件和[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)组件中订阅，不支持在[ApplicationContext](ApplicationContext (应用上下文).md)和[AbilityStage](@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md)组件容器中订阅。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

hasPointerDeviceboolean否是

表示指针设备是否已连接，如键鼠、触控板等。true表示设备已连接，false表示设备未连接。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

fontId14+string否是

表示应用字体的唯一ID。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

fontSizeScale12+number否是

表示字体大小缩放比例，取值为非负数，默认值为1。

支持开发者[设置应用字体大小](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-system-environment-variable-changes#设置字体大小)。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

fontWeightScale12+number否是

表示字体粗细缩放比例，取值为非负数，默认值为1。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

mcc12+string否是

表示移动设备国家代码。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

mnc12+string否是

表示移动设备网络代码。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

locale20+[Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)否是

表示区域设置。

应用会根据当前的区域设置自动调整其行为，以符合用户的本地化需求。该属性可以通过设置系统语言、设置系统地区和设置应用偏好语言等方式设置。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**示例：**

```ets
import { UIAbility, AbilityConstant, EnvironmentCallback, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let envCallback: EnvironmentCallback = {
      onConfigurationUpdated(config) {
        console.info(`envCallback onConfigurationUpdated success: ${JSON.stringify(config)}`);
        let language = config.language;
        let colorMode = config.colorMode;
        let direction = config.direction;
        let screenDensity = config.screenDensity;
        let displayId = config.displayId;
        let hasPointerDevice = config.hasPointerDevice;
        let fontId = config.fontId;
        let fontSizeScale = config.fontSizeScale;
        let fontWeightScale = config.fontWeightScale;
        let mcc = config.mcc;
        let mnc = config.mnc;
        let locale = config.locale;
      },
      onMemoryLevel(level) {
        console.info(`onMemoryLevel level: ${level}`);
      }
    };
    try {
      let applicationContext = this.context.getApplicationContext();
      let callbackId = applicationContext.on('environment', envCallback);
      console.info(`callbackId: ${callbackId}`);
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
  }
}
```