# @system.configuration (应用配置)

-

从API Version 7 开始，该接口不再维护，推荐使用新接口[@ohos.i18n](../ohos/@ohos.i18n (国际化-I18n).md)和[@ohos.intl](../ohos/@ohos.intl (国际化-Intl).md)。

-

本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import Configuration from '@system.configuration';
```

#### configuration.getLocale

static getLocale(): LocaleResponse

获取应用当前的语言和地区。默认与系统的语言和地区同步。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**返回值：**

类型说明LocaleResponse应用当前Locale相关信息。

**示例：**

```ets
export default {
  getLocale() {
    const localeInfo = configuration.getLocale();
    console.info(localeInfo.language);
  }
}
```

#### LocaleResponse

表示应用当前Locale的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Lite

名称类型可读可写说明languagestring是否语言。例如：zh。countryOrRegionstring是否国家或地区。例如：CN。dirstring是否

文字布局方向。取值范围：

- ltr：从左到右。

- rtl：从右到左。