# @ohos.i18n (国际化-I18n)

本模块提供系统相关的以及增强的[国际化](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-l10n)能力，包括区域管理、电话号码处理、日历等，相关接口为[ECMA 402](https://dev.ecma-international.org/publications-and-standards/standards/ecma-402/)标准中未定义的补充接口。[Intl模块](zh-cn_topic_0000002497605316.md)提供了ECMA 402标准定义的基础国际化接口，与本模块共同使用可提供完整地国际化能力。接口中使用的名词定义如下：

- 模式字符串：由[Unicode日期字段符号](https://www.unicode.org/reports/tr35/tr35-dates.md#Date_Field_Symbol_Table)和单引号包裹的自定义文本自由组合而成的字符串。
- 框架字符串：由[Unicode日期字段符号](https://www.unicode.org/reports/tr35/tr35-dates.md#Date_Field_Symbol_Table)自由组合而成的字符串，不支持自定义文本。

-

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块接口基于[CLDR](https://cldr.unicode.org)国际化数据库实现，随着CLDR标准的迭代演进，接口处理结果可能会相应调整。例如[时间日期格式化接口](#ZH-CN_TOPIC_0000002529445281__simplenumberformat18)，其返回值仅适用于界面展示场景，开发者请勿对返回格式进行硬编码或假设性判断，否则可能导致版本兼容问题。其中，API version 12 对应[CLDR 42](https://cldr.unicode.org/index/downloads/cldr-42)版本，具体数据变更详情可查阅CLDR官方文档。

-

从API version 11开始，本模块部分接口支持在ArkTS卡片中使用。

#### 导入模块

```ets
import { i18n } from '@kit.LocalizationKit';
```

#### System9+

提供系统属性相关的能力，包括语言地区名称翻译、支持的语言地区列表获取和系统语言地区获取等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### getDisplayCountry9+

static getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string

获取国家地区名称在指定语言下的翻译。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明countrystring是国家地区，要求是[合法的国家地区码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)。localestring是[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成。sentenceCaseboolean否true表示按照首字母大写的格式显示文本，false表示按照区域默认的大小写格式显示文本。默认值：true。

**返回值：**

类型说明string国家地区名称在指定语言下的翻译。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

890001的报错信息请以接口的实际报错为准。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let displayCountry: string = i18n.System.getDisplayCountry('CN', 'en-GB'); // displayCountry = 'China'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getDisplayCountry failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getDisplayLanguage9+

static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string

获取语言名称在指定语言下的翻译。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明languagestring是语言，要求是[合法的语言ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)。localestring是[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成。sentenceCaseboolean否true表示按照首字母大写的格式显示文本，false表示按照区域默认的大小写格式显示文本。默认值：true。

**返回值：**

类型说明string语言名称在指定语言下的翻译。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // 获取“中文”在英文下的翻译
  let displayLanguage: string = i18n.System.getDisplayLanguage('zh', 'en-GB'); // displayLanguage = 'Chinese'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getDisplayLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getSystemLanguages9+

static getSystemLanguages(): Array<string>

获取系统支持的语言列表。

从API version 11开始，该类型支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明Array<string>系统支持的语言列表。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

// systemLanguages = [ 'ug', 'bo', 'zh-Hant', 'en-Latn-US', 'zh-Hans' ]
let systemLanguages: Array<string> = i18n.System.getSystemLanguages();
```

#### getSystemCountries9+

static getSystemCountries(language: string): Array<string>

获取输入语言下系统支持的国家地区列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明languagestring是[合法的语言ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)。

**返回值：**

类型说明Array<string>某种特定语言下系统支持的国家地区列表。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

890001的报错信息请以接口的实际报错为准。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // systemCountries = [ 'ZW', 'YT', 'YE', ..., 'ER', 'CN', 'DE' ]
  let systemCountries: Array<string> = i18n.System.getSystemCountries('zh');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getSystemCountries failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### isSuggested9+

static isSuggested(language: string, region?: string): boolean

判断语言是否是地区的推荐语言。用于根据地区推荐语言或根据语言推荐地区。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明languagestring是[合法的语言ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，例如zh。regionstring否

[合法的国家地区码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，例如CN。

默认值：SIM卡国家地区。

**返回值：**

类型说明booleantrue表示语言是地区的推荐语言，false表示语言不是地区的推荐语言。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

890001的报错信息请以接口的实际报错为准。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let isSuggestedCountry: boolean = i18n.System.isSuggested('zh', 'CN'); // isSuggestedCountry = true
  isSuggestedCountry = i18n.System.isSuggested('en'); // 结果和系统当前地区相关
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.isSuggested failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getSystemLanguage9+

static getSystemLanguage(): string

获取系统当前设置的语言。若要监听系统语言变化，可以监听[公共事件](系统定义的公共事件.md#ZH-CN_TOPIC_0000002497605510__common_event_locale_changed)OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_LOCALE_CHANGED，具体可参考[系统语言与区域](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-system-language-region#开发步骤)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力**：从API version 11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明string表示语言ID的字符串。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let systemLanguage: string = i18n.System.getSystemLanguage(); // 如果系统语言为简体中文，systemLanguage = 'zh-Hans'
```

#### getSystemRegion9+

static getSystemRegion(): string

获取系统当前设置的国家地区。若要监听系统地区变化，可以监听[公共事件](系统定义的公共事件.md#ZH-CN_TOPIC_0000002497605510__common_event_locale_changed)OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_LOCALE_CHANGED，具体可参考[系统语言与区域](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-system-language-region#开发步骤)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明string表示国家地区ID的字符串。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let systemRegion: string = i18n.System.getSystemRegion(); // 如果系统地区为中国，systemRegion = 'CN'
```

#### getSystemLocale(deprecated)

static getSystemLocale(): string

从API version 9开始支持，从API version 20开始废弃，建议使用[System.getSystemLocaleInstance](#ZH-CN_TOPIC_0000002529445281__getsystemlocaleinstance20)代替。

获取系统当前设置的区域。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明string表示区域ID的字符串。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let systemLocale: string = i18n.System.getSystemLocale(); // 如果系统语言为简体中文、地区为中国，systemLocale = 'zh-Hans-CN'
```

#### getSystemLocaleInstance20+

static getSystemLocaleInstance(): Intl.Locale

获取系统当前设置的区域对象。若要监听系统区域变化，可以监听[公共事件](系统定义的公共事件.md#ZH-CN_TOPIC_0000002497605510__common_event_locale_changed)OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_LOCALE_CHANGED，具体可参考[系统语言与区域](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-system-language-region#开发步骤)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明[Intl.Locale](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)系统区域对象。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let systemLocale: Intl.Locale = i18n.System.getSystemLocaleInstance();
```

#### is24HourClock9+

static is24HourClock(): boolean

判断系统时制是否为24小时制。若要监听系统时制变化，可以监听[公共事件](系统定义的公共事件.md#ZH-CN_TOPIC_0000002497605510__common_event_time_changed)OHOS::EventFwk::CommonEventSupport::COMMON_EVENT_TIME_CHANGED，具体可参考[用户偏好](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-user-preferences#开发步骤)。

**卡片能力**：从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明booleantrue表示系统时制为24小时制，false表示系统时制为12小时制。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let is24HourClock: boolean = i18n.System.is24HourClock(); // 如果系统时制是24小时制，is24HourClock = true
```

#### getPreferredLanguageList9+

static getPreferredLanguageList(): Array<string>

获取系统偏好语言列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明Array<string>系统偏好语言列表。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let preferredLanguageList: Array<string> = i18n.System.getPreferredLanguageList();
```

#### getFirstPreferredLanguage9+

static getFirstPreferredLanguage(): string

获取系统偏好语言列表中的第一个语言。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明string系统偏好语言列表中的第一个语言。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let firstPreferredLanguage: string = i18n.System.getFirstPreferredLanguage();
```

#### setAppPreferredLanguage11+

static setAppPreferredLanguage(language: string): void

设置应用偏好语言。设置后，应用将优先加载应用偏好语言对应的资源。设置偏好语言为'default'后，应用语言将跟随系统语言，应用冷启动生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明languagestring是[合法的语言ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)或'default'。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  i18n.System.setAppPreferredLanguage('zh');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.setAppPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getAppPreferredLanguage9+

static getAppPreferredLanguage(): string

获取应用偏好语言。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明string应用偏好语言。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let appPreferredLanguage: string = i18n.System.getAppPreferredLanguage();
```

#### getUsingLocalDigit9+

static getUsingLocalDigit(): boolean

判断系统是否使用本地数字。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明booleantrue表示系统当前使用本地数字，false表示系统当前不使用本地数字。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let usingLocalDigit: boolean = i18n.System.getUsingLocalDigit();
```

#### getSimplifiedLanguage15+

static getSimplifiedLanguage(language?: string): string

获取语言的简化表示。例如：'en-Latn-US'的简化表示为'en'，'en-Latn-GB'的简化表示为'en-GB'。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明languagestring否[合法的语言ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)。默认值：系统语言。

**返回值：**

类型说明string

不传入language时，会根据系统语言和地区判断是否存在系统支持的方言，若存在则返回方言的简化表示；若不存在，则返回系统语言的简化表示。

传入language时，返回language的简化表示。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // simplifiedLanguage = 'zh'
  let simplifiedLanguage: string = i18n.System.getSimplifiedLanguage('zh-Hans-CN');
  // 获取当前系统语言的简化表示
  let simplifiedSystemLanguage: string = i18n.System.getSimplifiedLanguage();
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getSimplifiedLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getTemperatureType18+

static getTemperatureType(): TemperatureType

获取系统设置的温度单位。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明[TemperatureType](#ZH-CN_TOPIC_0000002529445281__temperaturetype18)温度单位。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let temperatureType: i18n.TemperatureType = i18n.System.getTemperatureType();
```

#### getTemperatureName18+

static getTemperatureName(type: TemperatureType): string

获取温度单位的名称。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明type[TemperatureType](#ZH-CN_TOPIC_0000002529445281__temperaturetype18)是温度单位。

**返回值：**

类型说明string返回温度单位的名称，包括celsius，fahrenheit，kelvin。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)。

错误码ID错误信息890001Invalid parameter. Possible causes: Parameter verification failed.

890001的报错信息请以接口的实际报错为准。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // temperatureName = 'celsius'
  let temperatureName: string = i18n.System.getTemperatureName(i18n.TemperatureType.CELSIUS);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.getTemperatureName failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getFirstDayOfWeek18+

static getFirstDayOfWeek(): WeekDay

获取系统设置的周起始日。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明[WeekDay](#ZH-CN_TOPIC_0000002529445281__weekday18)周起始日。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let firstDayOfWeek: i18n.WeekDay = i18n.System.getFirstDayOfWeek();
```

#### TemperatureType18+

温度单位的枚举。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

名称值说明CELSIUS1摄氏度。FAHRENHEIT2华氏度。KELVIN3开尔文。

#### WeekDay18+

周起始日的枚举，取值范围为周一至周日。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

名称值说明MON1周一。TUE2周二。WED3周三。THU4周四。FRI5周五。SAT6周六。SUN7周日。

#### i18n.isRTL

isRTL(locale: string): boolean

判断语言是否为镜像语言。在镜像语言下，UI界面需要[镜像显示](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-ui-design#界面镜像)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明localestring是[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成。

**返回值：**

类型说明booleantrue表示该语言是镜像语言，false表示该语言不是镜像语言。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let isZhRTL: boolean = i18n.isRTL('zh-CN'); // 中文不是镜像语言，返回false
let isArRTL: boolean = i18n.isRTL('ar-EG'); // 阿语是镜像语言，返回true
```

#### i18n.getCalendar8+

getCalendar(locale: string, type? : string): Calendar

获取指定区域和历法的日历对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明localestring是[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成，例如zh-Hans-CN。typestring否

表示历法，取值包括：buddhist, chinese, coptic, ethiopic, hebrew, gregory, indian, islamic_civil, islamic_tbla, islamic_umalqura, japanese, persian。

默认值：区域默认的历法。不同取值代表的含义和使用场景请参考[设置日历和历法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-calendar)。

**返回值：**

类型说明[Calendar](#ZH-CN_TOPIC_0000002529445281__calendar8)日历对象。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans', 'chinese'); // 获取中国农历日历对象
```

#### EntityRecognizer11+

提供实体识别相关的能力，可以获取文本中实体的类型和起止位置。当前支持识别的实体包括电话号码和时间日期。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### constructor11+

constructor(locale?: string)

创建实体识别对象。该对象根据区域规则识别文本中的实体。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明localestring否

[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成，例如zh-Hans-CN。

默认值：系统当前区域ID。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let entityRecognizer: i18n.EntityRecognizer = new i18n.EntityRecognizer('zh-CN');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call new i18n.EntityRecognizer failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### findEntityInfo11+

findEntityInfo(text: string): Array<EntityInfoItem>

获取文本中的实体信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明textstring是输入文本。

**返回值：**

类型说明Array<[EntityInfoItem](#ZH-CN_TOPIC_0000002529445281__entityinfoitem11)>文本中的实体信息列表。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let entityRecognizer: i18n.EntityRecognizer = new i18n.EntityRecognizer('zh-CN');
  let phoneNumberText: string = '如有疑问，请联系158****2312';
  // phoneNumberEntity[0].type = 'phone_number', phoneNumberEntity[0].begin = 8, phoneNumberEntity[0].end = 19
  let phoneNumberEntity: Array<i18n.EntityInfoItem> = entityRecognizer.findEntityInfo(phoneNumberText);
  let dateText: string = '我们2023年12月1日一起吃饭吧。';
  // dateEntity[0].type = 'date', dateEntity[0].begin = 2, dateEntity[0].end = 12
  let dateEntity: Array<i18n.EntityInfoItem> = entityRecognizer.findEntityInfo(dateText);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call EntityRecognizer.findEntityInfo failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### EntityInfoItem11+

实体信息属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

名称类型只读可选说明typestring否否实体的类型，当前支持phone_number和date类型。phone_number表示实体类型是电话号码，date表示实体类型是时间日期。beginnumber否否实体在输入字符串中的起始位置。endnumber否否实体在输入字符串中的终止位置。

#### Calendar8+

提供历法相关的能力，包括历法名称获取和日期计算等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### setTime8+

setTime(date: Date): void

基于传入的Date对象，设置日历对象内部的时间、日期。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明dateDate是时间、日期。说明：月份从0开始计数，例如0表示一月。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'gregory');
let date: Date = new Date(2021, 10, 7, 8, 0, 0); // 时间日期为2021.11.07 08:00:00
calendar.setTime(date);
```

#### setTime8+

setTime(time: number): void

基于传入的时间戳，设置日历对象内部的时间、日期。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明timenumber是Unix时间戳，表示从1970.1.1 00:00:00 GMT逝去的毫秒数。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'gregory');
calendar.setTime(10540800000);
```

#### set8+

set(year: number, month: number, date:number, hour?: number, minute?: number, second?: number): void

设置日历对象的年、月、日、时、分、秒。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明yearnumber是设置的年。monthnumber是设置的月。说明：月份从0开始计数，例如0表示一月。datenumber是设置的日。hournumber否设置的小时。默认值：系统当前时间。minutenumber否设置的分钟。默认值：系统当前时间。secondnumber否设置的秒。默认值：系统当前时间。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.set(2021, 10, 1, 8, 0, 0); // 设置时间日期为2021.11.1 08:00:00
```

#### setTimeZone8+

setTimeZone(timezone: string): void

设置日历对象的时区。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明timezonestring是合法的时区ID，如“Asia/Shanghai”。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setTimeZone('Asia/Shanghai');
```

#### getTimeZone8+

getTimeZone(): string

获取日历对象的时区ID。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明string表示时区ID的字符串。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setTimeZone('Asia/Shanghai');
let timezone: string = calendar.getTimeZone(); // timezone = 'Asia/Shanghai'
```

#### getFirstDayOfWeek8+

getFirstDayOfWeek(): number

获取日历对象的周起始日。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明number周起始日，1代表周日，7代表周六。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'gregory');
let firstDayOfWeek: number = calendar.getFirstDayOfWeek(); // firstDayOfWeek = 1
```

#### setFirstDayOfWeek8+

setFirstDayOfWeek(value: number): void

设置日历对象的周起始日。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明valuenumber是一周的起始日，1代表周日，7代表周六。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setFirstDayOfWeek(3);
let firstDayOfWeek: number = calendar.getFirstDayOfWeek(); // firstDayOfWeek = 3
```

#### getMinimalDaysInFirstWeek8+

getMinimalDaysInFirstWeek(): number

获取日历对象一年中第一周的最小天数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明number一年中第一周的最小天数。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
let minimalDaysInFirstWeek: number = calendar.getMinimalDaysInFirstWeek(); // minimalDaysInFirstWeek = 1
```

#### setMinimalDaysInFirstWeek8+

setMinimalDaysInFirstWeek(value: number): void

设置日历对象一年中第一周的最小天数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明valuenumber是一年中第一周的最小天数。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setMinimalDaysInFirstWeek(3);
let minimalDaysInFirstWeek: number = calendar.getMinimalDaysInFirstWeek(); // minimalDaysInFirstWeek = 3
```

#### get8+

get(field: string): number

获取日历对象中日历属性的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明fieldstring是指定的日历属性，目前支持的属性值请参考下表。属性名称说明era纪元，例如公历中的公元前或者公元后。year年。month月。说明：月份从0开始计数，例如0表示一月。date日。hour挂钟小时数。hour_of_day一天中的第几小时。minute分。second秒。millisecond毫秒。week_of_year一年中的第几周，按照星期计算周，注意：第一周的归属算法各地有区别。year_woy一年中的第几周，按照数值计算周，例如一年中前1~7日属于第一周。week_of_month一个月中的第几周，按照星期计算周。day_of_week_in_month一月中的第几周，按照数值计算周，例如1-7日属于第一周。day_of_year一年中的第几天。day_of_week一周中的第几天(星期)。milliseconds_in_day一天中的第几毫秒。zone_offset以毫秒计时的时区固定偏移量（不含夏令时）。dst_offset以毫秒计时的夏令时偏移量。dow_local本地星期。extended_year扩展的年份数值，支持负数。julian_day儒略日,与当前时区相关。is_leap_month是否为闰月。

**返回值：**

类型说明number日历属性的值，如当前Calendar对象的内部日期的年份为1990，get('year')返回1990。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.set(2021, 10, 1, 8, 0, 0); // 设置时间日期为2021.11.1 08:00:00
let hourOfDay: number = calendar.get('hour_of_day'); // hourOfDay = 8
```

#### getDisplayName8+

getDisplayName(locale: string): string

获取日历对象名称在指定语言下的翻译。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明localestring是[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成。

**返回值：**

类型说明string日历对象名称在指定语言下的翻译。如buddhist在en-US上显示的名称为“Buddhist Calendar”。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'buddhist');
let calendarName: string = calendar.getDisplayName('zh'); // calendarName = '佛历'
```

#### isWeekend8+

isWeekend(date?: Date): boolean

判断指定的日期在日历对象中是否为周末。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明dateDate否

时间、日期。说明：月份从0开始计数，例如0表示一月。

默认值：日历对象的当前日期。

**返回值：**

类型说明booleantrue表示指定的日期是周末，false表示指定的日期不是周末。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.set(2021, 11, 11, 8, 0, 0); // 设置时间为2021.12.11 08:00:00
let isWeekend: boolean = calendar.isWeekend(); // isWeekend = true
let date: Date = new Date(2011, 11, 6, 9, 0, 0); // 时间日期为2011.12.06 09:00:00
isWeekend = calendar.isWeekend(date); // isWeekend = false
```

#### add11+

add(field: string, amount: number): void

对日历对象中的表示时间日期的日历属性值进行加减操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明fieldstring是

指定的日历属性，目前支持的属性值有 year, month, week_of_year, week_of_month, date, day_of_year, day_of_week, day_of_week_in_month, hour, hour_of_day, minute, second, millisecond。

各取值代表的含义请参考[get](#ZH-CN_TOPIC_0000002529445281__get8)。

amountnumber是进行加减操作的具体数值。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
  calendar.set(2021, 11, 11, 8, 0, 0); // 设置时间日期为2021.12.11 08:00:00
  calendar.add('year', 8); // 2021 + 8
  let year: number = calendar.get('year'); // year = 2029
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call Calendar.add failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getTimeInMillis11+

getTimeInMillis(): number

获取当前日历对象的时间戳。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明numberUnix时间戳，表示从1970.1.1 00:00:00 GMT逝去的毫秒数。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setTime(5000);
let millisecond: number = calendar.getTimeInMillis(); // millisecond = 5000
```

#### compareDays11+

compareDays(date: Date): number

比较日历对象当前日期和指定日期相差的天数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明dateDate是时间、日期。说明：月份从0开始计数，例如0表示一月。

**返回值：**

类型说明number

相差的天数，正数表示日历时间更早，负数表示指定时间更早。

按毫秒级的精度，不足一天按一天计。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
  calendar.setTime(5000);
  let date: Date = new Date(6000);
  let diff: number = calendar.compareDays(date); // diff = 1
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call Calendar.compareDays failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### PhoneNumberFormat8+

提供电话号码相关的能力，包括电话号码有效性判断、格式化和归属地获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### constructor8+

constructor(country: string, options?: PhoneNumberFormatOptions)

创建电话号码格式化对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明countrystring是表示电话号码所属的国家地区代码。options[PhoneNumberFormatOptions](#ZH-CN_TOPIC_0000002529445281__phonenumberformatoptions8)否电话号码格式化时设置的配置项。默认值：NATIONAL。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let option: i18n.PhoneNumberFormatOptions = { type: 'E164' };
let phoneNumberFormat: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN', option);
```

#### isValidNumber8+

isValidNumber(phoneNumber: string): boolean

判断电话号码是否为当前电话号码格式化对象中国家的有效号码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明phoneNumberstring是待判断的电话号码。

**返回值：**

类型说明booleantrue表示电话号码有效，false表示电话号码无效。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let formatter: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN');
let isValidNumber: boolean = formatter.isValidNumber('158****2312'); // isValidNumber = true
```

#### format8+

format(phoneNumber: string): string

对电话号码进行格式化。

从API version 12开始，支持对拨号中的电话号码进行格式化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明phoneNumberstring是待格式化的电话号码。

**返回值：**

类型说明string格式化后的电话号码。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let formatter: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN');
// formattedPhoneNumber = '158 **** 2312'
let formattedPhoneNumber: string = formatter.format('158****2312');

// 拨号中的电话号码格式化
let option: i18n.PhoneNumberFormatOptions = { type: 'TYPING' };
let typingFormatter: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN', option);
let phoneNumber: string = '130493';
let formatResult: string = '';
for (let i = 0; i < phoneNumber.length; i++) {
  formatResult += phoneNumber.charAt(i);
  formatResult = typingFormatter.format(formatResult); // formatResult = '130 493'
}
```

#### getLocationName9+

getLocationName(phoneNumber: string, locale: string): string

获取电话号码归属地。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。获取其他地区电话号码的归属地时，需要在电话号码前加00+国际区号。localestring是[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成。

**返回值：**

类型说明string电话号码归属地。无效号码时返回空字符串。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let phonenumberFormat: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN');
let locationName: string = phonenumberFormat.getLocationName('158****2345', 'zh-CN'); // locationName = '广东省湛江市'
let locName: string = phonenumberFormat.getLocationName('0039312****789', 'zh-CN'); // locName = '意大利'
```

#### PhoneNumberFormatOptions8+

电话号码格式化时可设置的配置项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

名称类型只读可选说明typestring否是

表示对电话号码格式化的类型，取值包括：'E164', 'INTERNATIONAL', 'NATIONAL', 'RFC3966', 'TYPING'。

-在API version 8版本，type为必填项。

-API version 9版本开始，type为选填项。

-API version 12版本开始支持TYPING，表示对拨号中的电话号码实时格式化。

#### UnitInfo8+

度量衡单位信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

名称类型只读可选说明unitstring否否单位的名称，如：'meter', 'inch', 'cup'等。measureSystemstring否否单位的度量体系，取值包括：'SI', 'US', 'UK'。

#### i18n.getInstance8+

getInstance(locale?: string): IndexUtil

创建并返回IndexUtil对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明localestring否

[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成。

默认值：系统当前区域ID。

**返回值：**

类型说明[IndexUtil](#ZH-CN_TOPIC_0000002529445281__indexutil8)根据区域ID创建的IndexUtil对象。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let indexUtil: i18n.IndexUtil = i18n.getInstance('zh-CN');
```

#### IndexUtil8+

提供索引相关的能力，包括区域索引列表和文本索引值获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### getIndexList8+

getIndexList(): Array<string>

获取当前区域的索引列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明Array<string>当前区域的索引列表。第一个元素和最后一个元素为“...”。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let indexUtil: i18n.IndexUtil = i18n.getInstance('zh-CN');
// indexList = [ '...', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
//              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '...' ]
let indexList: Array<string> = indexUtil.getIndexList();
```

#### addLocale8+

addLocale(locale: string): void

在当前区域的索引列表中，添加新区域的索引列表，形成复合列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明localestring是[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let indexUtil: i18n.IndexUtil = i18n.getInstance('zh-CN');
indexUtil.addLocale('en-US');
```

#### getIndex8+

getIndex(text: string): string

获取输入文本对应的索引值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明textstring是输入文本。

**返回值：**

类型说明string输入文本对应的索引值。无合适索引时返回空字符串。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let indexUtil: i18n.IndexUtil = i18n.getInstance('zh-CN');
let index: string = indexUtil.getIndex('hi'); // index = 'H'
```

#### i18n.getLineInstance8+

getLineInstance(locale: string): BreakIterator

获取用于获取可换行点的BreakIterator对象。BreakIterator对象内部维护一个换行迭代器，可以用于访问各个可换行点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明localestring是

[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成。

生成的[BreakIterator](#ZH-CN_TOPIC_0000002529445281__breakiterator8)将按照指定区域的规则计算可换行点的位置。

**返回值：**

类型说明[BreakIterator](#ZH-CN_TOPIC_0000002529445281__breakiterator8)可换行点处理器。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
```

#### BreakIterator8+

提供文本换行相关的能力，包括可换行点的获取、移动和识别等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### setLineBreakText8+

setLineBreakText(text: string): void

设置BreakIterator对象要处理的文本。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明textstring是输入文本。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.'); // 设置处理文本
```

#### getLineBreakText8+

getLineBreakText(): string

获取BreakIterator对象当前处理的文本。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明stringBreakIterator对象正在处理的文本。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let breakText: string = iterator.getLineBreakText(); // breakText = 'Apple is my favorite fruit.'
```

#### current8+

current(): number

获取换行迭代器在当前处理文本中的位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明number获取换行迭代器在当前处理的文本中的位置。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let currentPos: number = iterator.current(); // currentPos = 0
```

#### first8+

first(): number

将换行迭代器移动到第一个可换行点。第一个可换行点总是在被处理文本的起始位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明number被处理文本的第一个可换行点的偏移量。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let firstPos: number = iterator.first(); // firstPos = 0
```

#### last8+

last(): number

将换行迭代器移动到最后一个可换行点。最后一个可换行点总是在被处理文本末尾的下一个位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明number被处理文本的最后一个可换行点的偏移量。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let lastPos: number = iterator.last(); // lastPos = 27
```

#### next8+

next(index?: number): number

将换行迭代器向后移动index个可换行点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明indexnumber否

换行迭代器将要移动的可换行点数，取值为整数。

正数表示向后移动index个可换行点，负数表示向前移动index个可换行点。

默认值：1。

**返回值：**

类型说明number

移动index个可换行点后，当前换行迭代器在文本中的位置。

若移动index个可换行点后超出了所处理的文本的长度范围，返回-1。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let pos: number = iterator.first(); // pos = 0
pos = iterator.next(); // pos = 6
pos = iterator.next(10); // pos = -1
```

#### previous8+

previous(): number

将换行迭代器向前移动一个可换行点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明number

移动到前一个可换行点后，当前换行迭代器在文本中的位置。

若移动后超出了所处理的文本的长度范围，返回-1。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let pos: number = iterator.first(); // pos = 0
pos = iterator.next(3); // pos = 12
pos = iterator.previous(); // pos = 9
```

#### following8+

following(offset: number): number

将换行迭代器移动到指定位置后面一个可换行点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明offsetnumber是将换行迭代器移动到文本指定位置的后面一个可换行点。

**返回值：**

类型说明number换行迭代器移动后的位置。若offset所指定位置的下一个可换行点超出了文本的范围，则返回-1。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let pos: number = iterator.following(0); // pos = 6
pos = iterator.following(100); // pos = -1
pos = iterator.current(); // pos = 27
```

#### isBoundary8+

isBoundary(offset: number): boolean

判断指定位置是否为可换行点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明offsetnumber是文本指定位置。

**返回值：**

类型说明boolean

true表示offset指定的文本位置是一个可换行点，false表示offset指定的文本位置不是一个可换行点。

返回true时，会将换行迭代器移动到offset指定的位置，否则相当于调用following。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let isBoundary: boolean = iterator.isBoundary(0); // isBoundary = true;
isBoundary = iterator.isBoundary(5); // isBoundary = false;
```

#### i18n.getTimeZone

getTimeZone(zoneID?: string): TimeZone

获取时区ID对应的时区对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明zoneIDstring否时区ID。默认值：系统时区。

**返回值：**

类型说明[TimeZone](#ZH-CN_TOPIC_0000002529445281__timezone)时区ID对应的时区对象。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
```

#### TimeZone

提供时区相关的能力，包括时区名称翻译、偏移量获取和跳变规则获取等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### getID

getID(): string

获取时区对象的ID。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明string时区对象对应的时区ID。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
let timezoneID: string = timezone.getID(); // timezoneID = 'Asia/Shanghai'
```

#### getDisplayName

getDisplayName(locale?: string, isDST?: boolean): string

获取时区对象名称在指定语言下的翻译。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明localestring否[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成。默认值：系统当前区域ID。isDSTboolean否true表示显示夏令时信息，false表示不显示夏令时信息。默认值：false。

**返回值：**

类型说明string时区对象名称在指定语言下的翻译。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
let timezoneName: string = timezone.getDisplayName('zh-CN', false); // timezoneName = '中国标准时间'
```

#### getRawOffset

getRawOffset(): number

获取时区对象所表示时区的原始偏移量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明number时区的原始偏移量，单位是毫秒。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
let offset: number = timezone.getRawOffset(); // offset = 28800000
```

#### getOffset

getOffset(date?: number): number

获取某一时刻时区对象所表示时区的偏移量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明datenumber否待计算时区偏移量的时刻，单位是毫秒。默认值：系统时间。

**返回值：**

类型说明number时区的偏移量，单位是毫秒。当处于夏令时时，时区偏移量为时区原始偏移量加夏令时偏移量。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
let offset: number = timezone.getOffset(1234567890); // offset = 28800000
```

#### getAvailableIDs9+

static getAvailableIDs(): Array<string>

获取系统支持的时区ID列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明Array<string>系统支持的时区ID列表。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

// ids = ['America/Adak', 'America/Anchorage', 'America/Bogota', 'America/Denver', 'America/Los_Angeles', 'America/Montevideo', 'America/Santiago', 'America/Sao_Paulo', 'Asia/Ashgabat', 'Asia/Hovd', 'Asia/Jerusalem', 'Asia/Magadan', 'Asia/Omsk', 'Asia/Shanghai', 'Asia/Tokyo', 'Asia/Yerevan', 'Atlantic/Cape_Verde', 'Australia/Lord_Howe', 'Europe/Dublin', 'Europe/London', 'Europe/Moscow', 'Pacific/Auckland', 'Pacific/Easter', 'Pacific/Pago-Pago']
let ids: Array<string> = i18n.TimeZone.getAvailableIDs();
```

#### getAvailableZoneCityIDs9+

static getAvailableZoneCityIDs(): Array<string>

获取系统支持的时区城市ID列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明Array<string>系统支持的时区城市ID列表。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

// cityIDs = ['Auckland', 'Magadan', 'Lord Howe Island', 'Tokyo', 'Shanghai', 'Hovd', 'Omsk', 'Ashgabat', 'Yerevan', 'Moscow', 'Tel Aviv', 'Dublin', 'London', 'Praia', 'Montevideo', 'Brasília', 'Santiago', 'Bogotá', 'Easter Island', 'Salt Lake City', 'Los Angeles', 'Anchorage', 'Adak', 'Pago Pago']
let cityIDs: Array<string> = i18n.TimeZone.getAvailableZoneCityIDs();
```

#### getCityDisplayName9+

static getCityDisplayName(cityID: string, locale: string): string

获取时区城市名称在指定语言下的翻译。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明cityIDstring是时区城市ID。localestring是[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成。

**返回值：**

类型说明string时区城市名称在指定语言下的翻译。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let displayName: string = i18n.TimeZone.getCityDisplayName('Shanghai', 'zh-CN'); // displayName = '上海 (中国)'
```

#### getTimezoneFromCity9+

static getTimezoneFromCity(cityID: string): TimeZone

创建对应时区城市的时区对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明cityIDstring是时区城市ID，要求是系统支持的时区城市ID。

**返回值：**

类型说明TimeZone时区城市对应的时区对象。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.TimeZone.getTimezoneFromCity('Shanghai');
```

#### getTimezonesByLocation10+

static getTimezonesByLocation(longitude: number, latitude: number): Array<TimeZone>

创建地理位置对应的时区对象数组。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明longitudenumber是经度，范围[-180, 179.9)，东经取正值，西经取负值。latitudenumber是纬度，范围[-90, 89.9)，北纬取正值，南纬取负值。

**返回值：**

类型说明Array<[TimeZone](#ZH-CN_TOPIC_0000002529445281__timezone)>时区对象数组，数组中对象对应的时区为该地理位置推荐的时区。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

890001的报错信息请以接口的实际报错为准。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let timezoneArray: Array<i18n.TimeZone> = i18n.TimeZone.getTimezonesByLocation(-118.1, 34.0);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call TimeZone.getTimezonesByLocation failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getZoneRules20+

getZoneRules(): ZoneRules

获取时区跳变规则，时区的跳变逻辑参考[夏令时跳变](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-dst-transition)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明[ZoneRules](#ZH-CN_TOPIC_0000002529445281__zonerules20)时区跳变规则，包含跳变的时间点、跳变前后的偏移量信息。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let tzId: string = 'America/Tijuana';
let timeZone: i18n.TimeZone = i18n.getTimeZone(tzId);
let zoneRules: i18n.ZoneRules = timeZone.getZoneRules();
let date = new Date(2025, 4, 13);
let zoneOffsetTransition: i18n.ZoneOffsetTransition =
    zoneRules.nextTransition(date.getTime()); // 获取2025年5月13日以后的下一个时区跳变对象
zoneOffsetTransition.getMilliseconds(); // 跳变点的时间戳: 1762074000000
zoneOffsetTransition.getOffsetAfter(); // 跳变后的偏移量: -28800000
zoneOffsetTransition.getOffsetBefore(); // 跳变前的偏移量: -25200000
// 将跳变点时间格式化
let dateTimeFormat: Intl.DateTimeFormat = new Intl.DateTimeFormat('en-US', {
  timeZone: tzId,
  dateStyle: 'long',
  timeStyle: 'long',
  hour12: false
});
let dateFormat: string =
  dateTimeFormat.format(new Date(zoneOffsetTransition.getMilliseconds())); // November 2, 2025, 1:00:00 PST
```

#### ZoneRules20+

提供查询时区跳变规则的能力。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### nextTransition20+

nextTransition(date?: number): ZoneOffsetTransition

获取指定时间的下一个时区跳变对象。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明datenumber否从1970年1月1日0时0分0秒到指定时间之间的毫秒数，默认到当前系统时间之间的毫秒数，单位：毫秒。

**返回值：**

类型说明[ZoneOffsetTransition](#ZH-CN_TOPIC_0000002529445281__zoneoffsettransition20)时区跳变对象。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

// 获取蒂华纳时区对象
let timeZone: i18n.TimeZone = i18n.getTimeZone('America/Tijuana');
// 获取蒂华纳时区跳变规则
let zoneRules: i18n.ZoneRules = timeZone.getZoneRules();
let date = new Date(2025, 4, 13);
// 获取蒂华纳时区2025年5月13日后的下一个跳变对象
let zoneOffsetTransition: i18n.ZoneOffsetTransition = zoneRules.nextTransition(date.getTime());
```

#### ZoneOffsetTransition20+

提供解析时区跳变规则的能力。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### getMilliseconds20+

getMilliseconds(): number

获取时区跳变点的时间戳。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明number从1970年1月1日0时0分0秒到时区跳变点之间的毫秒数，例如：1762074000000，单位：毫秒。如果当前时区[原始偏移量](#ZH-CN_TOPIC_0000002529445281__getrawoffset)保持不变并且不使用夏令时，则返回0。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let timeZone: i18n.TimeZone = i18n.getTimeZone('America/Tijuana');
let zoneRules: i18n.ZoneRules = timeZone.getZoneRules();
let date = new Date(2025, 4, 13);
let zoneOffsetTransition: i18n.ZoneOffsetTransition =
    zoneRules.nextTransition(date.getTime()); // 获取2025年5月13日以后的下一个时区跳变对象
zoneOffsetTransition.getMilliseconds(); // 跳变点的时间戳: 1762074000000
```

#### getOffsetAfter20+

getOffsetAfter(): number

获取时区跳变后的偏移量。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明number时区跳变后的偏移量，表示跳变后的时间相对于标准时间（协调世界时UTC）的时间差，单位：毫秒。例如：-28800000表示跳变后的时间比标准时间慢28800000毫秒（8小时）。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let timeZone: i18n.TimeZone = i18n.getTimeZone('America/Tijuana');
let zoneRules: i18n.ZoneRules = timeZone.getZoneRules();
let date = new Date(2025, 4, 13);
let zoneOffsetTransition: i18n.ZoneOffsetTransition =
    zoneRules.nextTransition(date.getTime()); // 获取2025年5月13日以后的下一个时区跳变对象
zoneOffsetTransition.getOffsetAfter(); // 跳变后的偏移量: -28800000
```

#### getOffsetBefore20+

getOffsetBefore(): number

获取时区跳变前的偏移量。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明number时区跳变前的偏移量，表示跳变前的时间相对于标准时间（协调世界时UTC）的时间差，单位：毫秒。例如：-25200000表示跳变前的时间比标准时间慢25200000毫秒（7小时）。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let timeZone: i18n.TimeZone = i18n.getTimeZone('America/Tijuana');
let zoneRules: i18n.ZoneRules = timeZone.getZoneRules();
let date = new Date(2025, 4, 13);
let zoneOffsetTransition: i18n.ZoneOffsetTransition =
    zoneRules.nextTransition(date.getTime()); // 获取2025年5月13日以后的下一个时区跳变对象
zoneOffsetTransition.getOffsetBefore(); // 跳变前的偏移量: -25200000
```

#### Transliterator9+

提供文本音译相关的能力，包括音译支持范围获取和文本音译等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### getAvailableIDs9+

static getAvailableIDs(): string[]

获取音译支持的转换ID列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明string[]音译支持的转换ID列表。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

// 共支持742个ID。每一个ID由使用中划线分割的两部分组成，格式为 source-destination。例如ids = ['Han-Latin','Latin-ASCII', 'Amharic-Latin/BGN','Accents-Any', ...]，Han-Latin表示汉语转为译拉丁文，Amharic-Latin表示阿姆哈拉语转为拉丁文。
// 更多使用信息可以参考ISO-15924。
let ids: string[] = i18n.Transliterator.getAvailableIDs();
```

#### getInstance9+

static getInstance(id: string): Transliterator

创建指定转换ID的音译对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明idstring是音译支持的转换ID。

**返回值：**

类型说明[Transliterator](#ZH-CN_TOPIC_0000002529445281__transliterator9)音译对象。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let transliterator: i18n.Transliterator = i18n.Transliterator.getInstance('Any-Latn');
```

#### transform9+

transform(text: string): string

将输入文本从源格式转换为目标格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明textstring是输入文本。

**返回值：**

类型说明string转换后的文本。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let transliterator: i18n.Transliterator = i18n.Transliterator.getInstance('Any-Latn');
let wordArray: string[] = ['中国', '德国', '美国', '法国']
for (let i = 0; i < wordArray.length; i++) {
  let transliterateLatn: string =
    transliterator.transform(wordArray[i]); // transliterateLatn依次为：'zhōng guó', 'dé guó', 'měi guó', 'fǎ guó'
}

// 汉语音译去声调
transliterator = i18n.Transliterator.getInstance('Any-Latn;Latin-Ascii');
let transliterateAscii: string = transliterator.transform('中国'); // transliterateAscii = 'zhong guo'

// 汉语姓氏读音
transliterator = i18n.Transliterator.getInstance('Han-Latin/Names');
let transliterateNames: string = transliterator.transform('单老师'); // transliterateNames = 'shàn lǎo shī'
transliterateNames = transliterator.transform('长孙无忌'); // transliterateNames = 'zhǎng sūn wú jì'
```

#### Unicode9+

提供字符属性相关的能力，包括判断字符是否为空格、数字和字母等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### isDigit9+

static isDigit(ch: string): boolean

判断输入的字符是否是数字。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是数字，false表示输入的字符不是数字。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let isDigit: boolean = i18n.Unicode.isDigit('1'); // isDigit = true
```

#### isSpaceChar9+

static isSpaceChar(ch: string): boolean

判断输入的字符是否是空格符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是空格符，false表示输入的字符不是空格符。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let isSpacechar: boolean = i18n.Unicode.isSpaceChar('a'); // isSpacechar = false
```

#### isWhitespace9+

static isWhitespace(ch: string): boolean

判断输入的字符是否是空白符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是空白符，false表示输入的字符不是空白符。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let isWhitespace: boolean = i18n.Unicode.isWhitespace('a'); // isWhitespace = false
```

#### isRTL9+

static isRTL(ch: string): boolean

判断输入的字符是否是从右到左语言的字符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是从右到左语言的字符，false表示输入的字符不是从右到左语言的字符。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let isRtl: boolean = i18n.Unicode.isRTL('a'); // isRtl = false
```

#### isIdeograph9+

static isIdeograph(ch: string): boolean

判断输入的字符是否是表意文字。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是表意文字，false表示输入的字符不是表意文字。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let isIdeograph: boolean = i18n.Unicode.isIdeograph('a'); // isIdeograph = false
```

#### isLetter9+

static isLetter(ch: string): boolean

判断输入的字符是否是字母。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是字母，false表示输入的字符不是字母。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let isLetter: boolean = i18n.Unicode.isLetter('a'); // isLetter = true
```

#### isLowerCase9+

static isLowerCase(ch: string): boolean

判断输入的字符是否是小写字母。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是小写字母，false表示输入的字符不是小写字母。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let isLowercase: boolean = i18n.Unicode.isLowerCase('a'); // isLowercase = true
```

#### isUpperCase9+

static isUpperCase(ch: string): boolean

判断输入的字符是否是大写字母。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是大写字母，false表示输入的字符不是大写字母。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let isUppercase: boolean = i18n.Unicode.isUpperCase('a'); // isUppercase = false
```

#### getType9+

static getType(ch: string): string

获取输入的字符的一般类别值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明string输入字符的一般类别值。

一般类别值如下，更详细的介绍可以参考Unicode标准。

名称值说明U_UNASSIGNEDU_UNASSIGNED表示未分配和非字符代码点对应类别。U_GENERAL_OTHER_TYPESU_GENERAL_OTHER_TYPES与 U_UNASSIGNED 一致。U_UPPERCASE_LETTERU_UPPERCASE_LETTER表示大写字母。U_LOWERCASE_LETTERU_LOWERCASE_LETTER表示小写字母。U_TITLECASE_LETTERU_TITLECASE_LETTER表示首字母大写。U_MODIFIER_LETTERU_MODIFIER_LETTER表示字母修饰符。U_OTHER_LETTERU_OTHER_LETTER表示其它字母，不属于大写字母、小写字母、首字母大写或修饰符字母的字母。U_NON_SPACING_MARKU_NON_SPACING_MARK表示非间距标记，例如重音符号'，变音符号#。U_ENCLOSING_MARKU_ENCLOSING_MARK表示封闭标记和能围住其它字符的标记，如圆圈、方框等。U_COMBINING_SPACING_MARKU_COMBINING_SPACING_MARK表示间距标记，例如元音符号[ ]。U_DECIMAL_DIGIT_NUMBERU_DECIMAL_DIGIT_NUMBER表示十进制数字。U_LETTER_NUMBERU_LETTER_NUMBER表示字母数字，罗马数字。U_OTHER_NUMBERU_OTHER_NUMBER表示其它作为加密符号和记号的数字，非阿拉伯数字的数字表示符，例如@、#、（1）、①等。U_SPACE_SEPARATORU_SPACE_SEPARATOR表示空白分隔符，如空格符、不间断空格、固定宽度的空白符。U_LINE_SEPARATORU_LINE_SEPARATOR表示行分隔符。U_PARAGRAPH_SEPARATORU_PARAGRAPH_SEPARATOR表示段落分割符。U_CONTROL_CHARU_CONTROL_CHAR表示控制字符。U_FORMAT_CHARU_FORMAT_CHAR表示格式字符。U_PRIVATE_USE_CHARU_PRIVATE_USE_CHAR表示私人使用区代码点类别，例如公司 logo。U_SURROGATEU_SURROGATE表示代理项，在UTF-16中用来表示补充字符的方法。U_DASH_PUNCTUATIONU_DASH_PUNCTUATION表示短划线标点。U_START_PUNCTUATIONU_START_PUNCTUATION表示开始标点，如左括号。U_END_PUNCTUATIONU_END_PUNCTUATION表示结束标点，如右括号。U_INITIAL_PUNCTUATIONU_INITIAL_PUNCTUATION表示前引号，例如左双引号、左单引号。U_FINAL_PUNCTUATIONU_FINAL_PUNCTUATION表示后引号，例如右双引号、右单引号。U_CONNECTOR_PUNCTUATIONU_CONNECTOR_PUNCTUATION表示连接符标点。U_OTHER_PUNCTUATIONU_OTHER_PUNCTUATION表示其他标点。U_MATH_SYMBOLU_MATH_SYMBOL表示数学符号。U_CURRENCY_SYMBOLU_CURRENCY_SYMBOL表示货币符号。U_MODIFIER_SYMBOLU_MODIFIER_SYMBOL表示修饰符号。U_OTHER_SYMBOLU_OTHER_SYMBOL表示其它符号。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let unicodeType: string = i18n.Unicode.getType('a'); // unicodeType = 'U_LOWERCASE_LETTER'
```

#### I18NUtil9+

国际化工具类，提供单位转换、获取日期顺序、获取时段名称、区域匹配和路径本地化等能力。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### unitConvert9+

static unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: number, locale: string, style?: string): string

将fromUnit的单位转换为toUnit的单位，并根据区域与风格进行格式化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明fromUnit[UnitInfo](#ZH-CN_TOPIC_0000002529445281__unitinfo8)是需要转换的单位。toUnit[UnitInfo](#ZH-CN_TOPIC_0000002529445281__unitinfo8)是转换成的目标单位。valuenumber是需要转换的单位的数量值。localestring是[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成，如：zh-Hans-CN。stylestring否

格式化使用的风格，取值包括：'long', 'short', 'narrow'。默认值：short。

不同取值显示效果请参考[数字与度量衡国际化](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-numbers-weights-measures)。

**返回值：**

类型说明string转换单位后的度量衡格式化结果。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let fromUnit: i18n.UnitInfo = { unit: 'cup', measureSystem: 'US' };
let toUnit: i18n.UnitInfo = { unit: 'liter', measureSystem: 'SI' };
let convertResult: string =
  i18n.I18NUtil.unitConvert(fromUnit, toUnit, 1000, 'en-US', 'long'); // convertResult = '236.588 liters'
```

#### getDateOrder9+

static getDateOrder(locale: string): string

获取某区域日期中年、月、日的排列顺序。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明localestring是[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成，如：zh-Hans-CN。

**返回值：**

类型说明string该区域年、月、日的排列顺序。“y”表示年，“L”表示月，“d”表示日。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let order: string = i18n.I18NUtil.getDateOrder('zh-CN'); // order = 'y-L-d'
```

#### getTimePeriodName11+

static getTimePeriodName(hour:number, locale?: string): string

获取指定时间在某区域的本地化表达。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明hournumber是指定的时间，例如16。localestring否

[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成。如：zh-Hans-CN。

默认值：系统当前区域ID。

**返回值：**

类型说明string指定时间在某区域的本地化表达。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let name: string = i18n.I18NUtil.getTimePeriodName(2, 'zh-CN'); // name = '凌晨'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call I18NUtil.getTimePeriodName failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getBestMatchLocale12+

static getBestMatchLocale(locale: string, localeList: string[]): string

在指定区域列表中获取与某个区域最佳匹配的区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明localestring是待匹配的[区域ID字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，如：zh-Hans-CN。localeListstring[]是指定的区域ID字符串列表。

**返回值：**

类型说明string与某个区域最佳匹配的区域ID。当指定区域列表中没有匹配的区域时，返回空字串。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let matchedLocaleId: string = i18n.I18NUtil.getBestMatchLocale('zh-Hans-CN',
    ['en-Latn-US', 'en-GB', 'zh-Hant-CN', 'zh-Hans-MO']); // matchedLocaleId = 'zh-Hans-MO'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call I18NUtil.getBestMatchLocale failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getThreeLetterLanguage12+

static getThreeLetterLanguage(locale: string): string

将语言代码由二字母转换为三字母。二字母和三字母语言代码的规格参考[ISO 639](https://www.iso.org/iso-639-language-code)。

例如，中文的二字母语言代码是zh，对应的三字母语言代码是zho。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明localestring是待转换的语言二字母代码，如：zh。

**返回值：**

类型说明string返回待转换语言二字母代码对应的三字母代码。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let language: string = i18n.I18NUtil.getThreeLetterLanguage('zh') // language = 'zho'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call I18NUtil.getThreeLetterLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getThreeLetterRegion12+

static getThreeLetterRegion(locale: string): string

将地区代码由二字母转换为三字母。二字母和三字母地区代码的规格参考[ISO 3166](https://www.iso.org/iso-3166-country-codes.md)

例如，中国的二字母地区代码是CN, 三字母是CHN。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明localestring是待转换的地区二字母代码，如：CN。

**返回值：**

类型说明string返回待转换地区二字母代码对应的三字母代码。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let region: string = i18n.I18NUtil.getThreeLetterRegion('CN') // region = 'CHN'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call I18NUtil.getThreeLetterRegion failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getUnicodeWrappedFilePath20+

static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: Intl.Locale): string

对文件路径进行本地化处理。

例如，将/data/out/tmp本地化处理后生成tmp/out/data/。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明pathstring是待处理的路径，如：/data/out/tmp。delimiterstring否路径分隔符，默认值：/。locale[Intl.Locale](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)否区域对象，默认值：系统区域对象。

**返回值：**

类型说明string本地化处理后的文件路径。如果区域对象表示的语言是镜像语言，则处理后的文件路径包含方向控制符，保证文件路径镜像显示。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)。

错误码ID错误信息8900001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let path: string = '/data/out/tmp';
  let delimiter: string = '/';
  let locale: Intl.Locale = new Intl.Locale('ar');
  let mirrorPath: string =
    i18n.I18NUtil.getUnicodeWrappedFilePath(path, delimiter, locale); // mirrorPath显示为: 'tmp/out/data/'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call I18NUtil.getUnicodeWrappedFilePath failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getUnicodeWrappedFilePath(deprecated)

static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string

从API version 18开始支持，从API version 20开始废弃，建议使用[getUnicodeWrappedFilePath](#ZH-CN_TOPIC_0000002529445281__getunicodewrappedfilepath20)替代。

对文件路径进行本地化处理。

例如，将/data/out/tmp本地化处理后生成tmp/out/data/。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明pathstring是待处理的路径，如：/data/out/tmp。delimiterstring否路径分隔符，默认值：/。locale[intl.Locale](@ohos.intl (国际化-Intl).md#ZH-CN_TOPIC_0000002497605316__localedeprecated)否区域对象，默认值：系统区域对象。

**返回值：**

类型说明string本地化处理后的文件路径。如果区域对象表示的语言是镜像语言，则处理后的文件路径包含方向控制符，保证文件路径镜像显示。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)。

错误码ID错误信息890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n, intl } from '@kit.LocalizationKit';

try {
  let path: string = '/data/out/tmp';
  let delimiter: string = '/';
  let locale: intl.Locale = new intl.Locale('ar');
  let mirrorPath: string =
    i18n.I18NUtil.getUnicodeWrappedFilePath(path, delimiter, locale); // mirrorPath显示为: 'tmp/out/data/'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call I18NUtil.getUnicodeWrappedFilePath failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### Normalizer10+

提供文本标准化的能力。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### getInstance10+

static getInstance(mode: NormalizerMode): Normalizer

获取文本标准化对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明mode[NormalizerMode](#ZH-CN_TOPIC_0000002529445281__normalizermode10)是文本标准化范式。

**返回值：**

类型说明[Normalizer](#ZH-CN_TOPIC_0000002529445281__normalizer10)返回指定范式的文本标准化对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let normalizer: i18n.Normalizer = i18n.Normalizer.getInstance(i18n.NormalizerMode.NFC);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call Normalizer.getInstance failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### normalize10+

normalize(text: string): string

对字符串进行标准化处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明textstring是输入文本。

**返回值：**

类型说明string标准化处理后的字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let normalizer: i18n.Normalizer = i18n.Normalizer.getInstance(i18n.NormalizerMode.NFC);
  let normalizedText: string = normalizer.normalize('\u1E9B\u0323'); // normalizedText = 'ẛ̣'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call Normalizer.getInstance failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### NormalizerMode10+

文本标准化范式的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

名称值说明NFC1NFC范式。NFD2NFD范式。NFKC3NFKC范式。NFKD4NFKD范式。

#### HolidayManager11+

提供解析节假日数据的能力，包括节假日判断和指定年份节假日列表获取等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### constructor11+

constructor(icsPath: String)

创建HolidayManager对象，用于解析节假日数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明icsPathString是在设备上有应用读取权限的iCalendar格式的ics文件路径。iCalendar格式是一种标准的互联网日历格式，用于存储日历数据。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // 需要将'/system/lib/US.ics'替换为实际ics文件路径
  let holidayManager = new i18n.HolidayManager('/system/lib/US.ics');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call i18n.HolidayManager failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### isHoliday11+

isHoliday(date?: Date): boolean

判断指定的日期是否是节假日。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明dateDate否

时间、日期。说明：月份从0开始计数，例如0表示一月。

默认值：当前日期。

**返回值：**

类型说明booleantrue表示指定的日期是节假日，false表示指定的日期不是节假日。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // 需要将'/system/lib/US.ics'替换为实际ics文件路径
  let holidayManager: i18n.HolidayManager = new i18n.HolidayManager('/system/lib/US.ics');
  let isHoliday: boolean = holidayManager.isHoliday();
  isHoliday = holidayManager.isHoliday(new Date(2023, 5, 25)); // 时间日期为2023.06.25
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call holidayManager.isHoliday failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### getHolidayInfoItemArray11+

getHolidayInfoItemArray(year?: number): Array<[HolidayInfoItem](#ZH-CN_TOPIC_0000002529445281__holidayinfoitem11)>

获取指定年的节假日信息列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明yearnumber否

年，例如2023。

默认值：当前年份。

**返回值：**

类型说明Array<[HolidayInfoItem](#ZH-CN_TOPIC_0000002529445281__holidayinfoitem11)>返回节假日信息列表。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // 需要将'/system/lib/US.ics'替换为实际ics文件路径
  let holidayManager: i18n.HolidayManager = new i18n.HolidayManager('/system/lib/US.ics');
  let holidayInfoItemArray: Array<i18n.HolidayInfoItem> = holidayManager.getHolidayInfoItemArray(2023);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call holidayManager.getHolidayInfoItemArray failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### HolidayInfoItem11+

节假日信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

名称类型只读可选说明baseNamestring否否节假日的英文名称。yearnumber否否节假日所在年。monthnumber否否节假日所在月。daynumber否否节假日所在日。localNamesArray<[HolidayLocalName](#ZH-CN_TOPIC_0000002529445281__holidaylocalname11)>否是节假日的本地名称列表。

#### HolidayLocalName11+

节假日名称在不同语言下的翻译。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

名称类型只读可选说明languagestring否否语言，例如ar，en，tr。namestring否否节假日的本地名称，例如Sacrifice Feast（宰牲节）的土耳其语名称为Kurban Bayrami。

#### i18n.getSimpleDateTimeFormatByPattern20+

getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat

通过模式字符串获取SimpleDateTimeFormat对象。与[getSimpleDateTimeFormatBySkeleton](#ZH-CN_TOPIC_0000002529445281__i18ngetsimpledatetimeformatbyskeleton20)接口获取的对象在格式化后显示差异请参考[SimpleDateTimeFormat.format](#ZH-CN_TOPIC_0000002529445281__format18)的示例。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明patternstring是合法的模式字符串，支持[日期字段符号表](https://www.unicode.org/reports/tr35/tr35-dates.md#Date_Field_Symbol_Table)中Field Patterns值的自由组合。同时，pattern支持传入自定义文本，文本内容以''标识。locale[Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)否区域对象。默认值：系统区域对象。

**返回值：**

类型说明[SimpleDateTimeFormat](#ZH-CN_TOPIC_0000002529445281__simpledatetimeformat18)SimpleDateTimeFormat对象。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)。

错误码ID错误信息8900001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let locale: Intl.Locale = new Intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatByPattern("'month('M')'", locale);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call i18n.getSimpleDateTimeFormatByPattern failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### i18n.getSimpleDateTimeFormatByPattern(deprecated)

getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat

从API version 18开始支持，从API version 20开始废弃，建议使用[getSimpleDateTimeFormatByPattern](#ZH-CN_TOPIC_0000002529445281__i18ngetsimpledatetimeformatbypattern20)替代。

通过模式字符串获取SimpleDateTimeFormat对象。与[getSimpleDateTimeFormatBySkeleton](#ZH-CN_TOPIC_0000002529445281__i18ngetsimpledatetimeformatbyskeletondeprecated)接口获取的对象在格式化后显示差异请参考[SimpleDateTimeFormat.format](#ZH-CN_TOPIC_0000002529445281__format18)的示例。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明patternstring是合法的模式字符串，支持[日期字段符号表](https://www.unicode.org/reports/tr35/tr35-dates.md#Date_Field_Symbol_Table)中Field Patterns值的自由组合。同时，pattern支持传入自定义文本，文本内容以''标识。locale[intl.Locale](@ohos.intl (国际化-Intl).md#ZH-CN_TOPIC_0000002497605316__localedeprecated)否区域对象。默认值：系统区域对象。

**返回值：**

类型说明[SimpleDateTimeFormat](#ZH-CN_TOPIC_0000002529445281__simpledatetimeformat18)SimpleDateTimeFormat对象。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)。

错误码ID错误信息890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n, intl } from '@kit.LocalizationKit';

try {
  let locale: intl.Locale = new intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatByPattern("'month('M')'", locale);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call i18n.getSimpleDateTimeFormatByPattern failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### i18n.getSimpleDateTimeFormatBySkeleton20+

getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: Intl.Locale): SimpleDateTimeFormat

通过框架字符串获取SimpleDateTimeFormat对象。与[getSimpleDateTimeFormatByPattern](#ZH-CN_TOPIC_0000002529445281__i18ngetsimpledatetimeformatbypattern20)接口获取的对象在格式化后显示差异请参考[SimpleDateTimeFormat.format](#ZH-CN_TOPIC_0000002529445281__format18)的示例。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明skeletonstring是合法的框架字符串，支持[日期字段符号表](https://www.unicode.org/reports/tr35/tr35-dates.md#Date_Field_Symbol_Table)中Field Patterns值的自由组合。skeleton不支持传入自定义文本。locale[Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)否区域对象。默认值：系统区域对象。

**返回值：**

类型说明[SimpleDateTimeFormat](#ZH-CN_TOPIC_0000002529445281__simpledatetimeformat18)SimpleDateTimeFormat对象。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)。

错误码ID错误信息8900001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let locale: Intl.Locale = new Intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatBySkeleton('yMd', locale);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call i18n.getSimpleDateTimeFormatBySkeleton failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### i18n.getSimpleDateTimeFormatBySkeleton(deprecated)

getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleDateTimeFormat

从API version 18开始支持，从API version 20开始废弃，建议使用[getSimpleDateTimeFormatBySkeleton](#ZH-CN_TOPIC_0000002529445281__i18ngetsimpledatetimeformatbyskeleton20)替代。

通过框架字符串获取SimpleDateTimeFormat对象。与[getSimpleDateTimeFormatByPattern](#ZH-CN_TOPIC_0000002529445281__i18ngetsimpledatetimeformatbypatterndeprecated)接口获取的对象在格式化后显示差异请参考[SimpleDateTimeFormat.format](#ZH-CN_TOPIC_0000002529445281__format18)的示例。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明skeletonstring是合法的框架字符串，支持[日期字段符号表](https://www.unicode.org/reports/tr35/tr35-dates.md#Date_Field_Symbol_Table)中Field Patterns值的自由组合。skeleton不支持传入自定义文本。locale[intl.Locale](@ohos.intl (国际化-Intl).md#ZH-CN_TOPIC_0000002497605316__localedeprecated)否区域对象。默认值：系统区域对象。

**返回值：**

类型说明[SimpleDateTimeFormat](#ZH-CN_TOPIC_0000002529445281__simpledatetimeformat18)SimpleDateTimeFormat对象。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)。

错误码ID错误信息890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n, intl } from '@kit.LocalizationKit';

try {
  let locale: intl.Locale = new intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatBySkeleton('yMd', locale);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call i18n.getSimpleDateTimeFormatBySkeleton failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### SimpleDateTimeFormat18+

提供时间日期格式化的能力。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### format18+

format(date: Date): string

对时间、日期进行格式化。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明dateDate是时间、日期。说明：月份从0开始计数，例如0表示一月。

**返回值：**

类型说明string格式化后的时间、日期字符串。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let locale : Intl.Locale = new Intl.Locale("zh-Hans-CN");
  let date : Date = new Date(2024, 11, 13); // 时间日期为2024.12.13

  let formatterWithText: i18n.SimpleDateTimeFormat =
    i18n.getSimpleDateTimeFormatByPattern("'month('M')'", locale);
  let formattedDate: string = formatterWithText.format(date); // formattedDate = 'month(12)'

  let patternFormatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatByPattern('yMd', locale);
  formattedDate = patternFormatter.format(date); // formattedDate = '20241213'

  let skeletonFormatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatBySkeleton('yMd', locale);
  formattedDate = skeletonFormatter.format(date); // formattedDate = '2024/12/13'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call SimpleDateTimeFormat.format failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### i18n.getSimpleNumberFormatBySkeleton20+

getSimpleNumberFormatBySkeleton(skeleton: string, locale?: Intl.Locale): SimpleNumberFormat

通过框架字符串获取SimpleNumberFormat对象。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明skeletonstring是合法的框架字符串，支持的字符及含义请参考[Number Skeletons](https://unicode-org.github.io/icu/userguide/format_parse/numbers/skeletons.md#number-skeletons)。locale[Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)否区域对象。默认值：系统区域对象。

**返回值：**

类型说明[SimpleNumberFormat](#ZH-CN_TOPIC_0000002529445281__simplenumberformat18)SimpleNumberFormat对象。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)。

错误码ID错误信息8900001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let locale: Intl.Locale = new Intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('%', locale);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call SimpleDateTimeFormat.getSimpleNumberFormatBySkeleton failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### i18n.getSimpleNumberFormatBySkeleton(deprecated)

getSimpleNumberFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleNumberFormat

从API version 18开始支持，从API version 20开始废弃，建议使用[getSimpleNumberFormatBySkeleton](#ZH-CN_TOPIC_0000002529445281__i18ngetsimplenumberformatbyskeleton20)替代。

通过框架字符串获取SimpleNumberFormat对象。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明skeletonstring是合法的框架字符串，支持的字符及含义请参考[Number Skeletons](https://unicode-org.github.io/icu/userguide/format_parse/numbers/skeletons.md#number-skeletons)。locale[intl.Locale](@ohos.intl (国际化-Intl).md#ZH-CN_TOPIC_0000002497605316__localedeprecated)否区域对象。默认值：系统区域对象。

**返回值：**

类型说明[SimpleNumberFormat](#ZH-CN_TOPIC_0000002529445281__simplenumberformat18)SimpleNumberFormat对象。

**错误码：**

以下错误码的详细介绍请参见[ohos.i18n错误码](I18n错误码.md)。

错误码ID错误信息890001Invalid parameter. Possible causes: Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n, intl } from '@kit.LocalizationKit';

try {
  let locale: intl.Locale = new intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('%', locale);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call SimpleDateTimeFormat.getSimpleNumberFormatBySkeleton failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### SimpleNumberFormat18+

基于框架字符串提供数字格式化的能力。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### format18+

format(value: number): string

对数字进行格式化。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明valuenumber是数字对象。

**返回值：**

类型说明string格式化后的数字字符串。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let locale: Intl.Locale = new Intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('%', locale);
  let formattedNumber: string = formatter.format(10); // formattedNumber = '10%'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call SimpleNumberFormat.format failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### StyledNumberFormat18+

提供富文本数字格式化的能力。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

#### constructor(deprecated)

constructor(numberFormat: intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)

从API version 18开始支持，从API version 20开始废弃，建议使用[constructor](#ZH-CN_TOPIC_0000002529445281__constructor20)替代。

创建需要富文本显示的数字格式化的对象。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明numberFormat[intl.NumberFormat](@ohos.intl (国际化-Intl).md#ZH-CN_TOPIC_0000002497605316__numberformat) | [SimpleNumberFormat](#ZH-CN_TOPIC_0000002529445281__simplenumberformat18)是用于格式化数字的对象。options[StyledNumberFormatOptions](#ZH-CN_TOPIC_0000002529445281__stylednumberformatoptions18)否指定数字格式化对象的配置项。默认值：默认的文本样式。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n, intl } from '@kit.LocalizationKit';

try {
  let integerTextStyle: TextStyle = new TextStyle({ fontColor: Color.Red });
  let decimalTextStyle: TextStyle = new TextStyle({ fontColor: Color.Brown });
  let fractionTextStyle: TextStyle = new TextStyle({ fontColor: Color.Blue });
  let unitTextStyle: TextStyle = new TextStyle({ fontColor: Color.Green });

  // 通过intl.NumberFormat创建StyledNumberFormat对象
  let numFmt: intl.NumberFormat = new intl.NumberFormat('zh', { style: 'unit', unit: 'percent' });
  let styledNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(numFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });

  // 通过SimpleNumberFormat创建StyledNumberFormat对象
  let locale: intl.Locale = new intl.Locale('zh');
  let simpleNumFmt: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('percent', locale);
  let styledSimpleNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(simpleNumFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call i18n.StyledNumberFormat failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### constructor20+

constructor(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)

创建需要富文本显示的数字格式化的对象。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明numberFormat[Intl.NumberFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat) | [SimpleNumberFormat](#ZH-CN_TOPIC_0000002529445281__simplenumberformat18)是用于格式化数字的对象。options[StyledNumberFormatOptions](#ZH-CN_TOPIC_0000002529445281__stylednumberformatoptions18)否指定数字格式化对象的配置项。默认值：默认的文本样式。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let integerTextStyle: TextStyle = new TextStyle({ fontColor: Color.Red });
  let decimalTextStyle: TextStyle = new TextStyle({ fontColor: Color.Brown });
  let fractionTextStyle: TextStyle = new TextStyle({ fontColor: Color.Blue });
  let unitTextStyle: TextStyle = new TextStyle({ fontColor: Color.Green });

  // 通过Intl.NumberFormat创建StyledNumberFormat对象
  let numFmt: Intl.NumberFormat = new Intl.NumberFormat('zh', { style: 'unit', unit: 'percent' });
  let styledNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(numFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });

  // 通过SimpleNumberFormat创建StyledNumberFormat对象
  let locale: Intl.Locale = new Intl.Locale('zh');
  let simpleNumFmt: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('percent', locale);
  let styledSimpleNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(simpleNumFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call i18n.StyledNumberFormat failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### format18+

format(value: number): StyledString

使用数字格式化对象对数字进行格式化，返回富文本对象。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明valuenumber是需要格式化的数字。

**返回值：**

类型说明[StyledString](属性字符串.md#ZH-CN_TOPIC_0000002497444920__styledstring)格式化后的富文本对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let integerTextStyle: TextStyle = new TextStyle({ fontColor: Color.Red });
  let decimalTextStyle: TextStyle = new TextStyle({ fontColor: Color.Brown });
  let fractionTextStyle: TextStyle = new TextStyle({ fontColor: Color.Blue });
  let unitTextStyle: TextStyle = new TextStyle({ fontColor: Color.Green });

  // 通过Intl.NumberFormat创建StyledNumberFormat对象
  let numFmt: Intl.NumberFormat = new Intl.NumberFormat('zh', { style: 'unit', unit: 'percent' });
  let styledNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(numFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
  // formattedNumber.getString() 为 '1,234.568%'。显示formattedNumber时'1,234'是红色，'.'是棕色，'568'是蓝色，'%'是绿色。
  let formattedNumber: StyledString = styledNumFmt.format(1234.5678);

  // 通过SimpleNumberFormat创建StyledNumberFormat对象
  let locale: Intl.Locale = new Intl.Locale('zh');
  let simpleNumFmt: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('percent', locale);
  let styledSimpleNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(simpleNumFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
  // formattedSimpleNumber.getString() 为 '1,234.5678%'。显示formattedSimpleNumber时'1,234'是红色，'.'是棕色，'5678'是蓝色，'%'是绿色。
  let formattedSimpleNumber: StyledString = styledSimpleNumFmt.format(1234.5678);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call StyledNumberFormat.format failed, error code: ${err.code}, message: ${err.message}.`);
}
```

#### StyledNumberFormatOptions18+

创建富文本显示的数字格式化对象时的可选配置项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.I18n

名称类型只读可选说明integer[TextStyle](属性字符串.md#ZH-CN_TOPIC_0000002497444920__textstyle)否是指定整数部分的文本样式。默认值：默认的文本样式。decimal[TextStyle](属性字符串.md#ZH-CN_TOPIC_0000002497444920__textstyle)否是指定小数点的文本样式。默认值：默认的文本样式。fraction[TextStyle](属性字符串.md#ZH-CN_TOPIC_0000002497444920__textstyle)否是指定小数部分的文本样式。默认值：默认的文本样式。unit[TextStyle](属性字符串.md#ZH-CN_TOPIC_0000002497444920__textstyle)否是指定单位部分的文本样式。默认值：默认的文本样式。

#### i18n.getDisplayCountry(deprecated)

getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string

从API version 7开始支持，从API version 9开始废弃，建议使用[System.getDisplayCountry](#ZH-CN_TOPIC_0000002529445281__getdisplaycountry9)替代。

获取指定国家的本地化名称。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明countrystring是指定国家。localestring是[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成。sentenceCaseboolean否true表示按照首字母大写的格式显示文本，false表示按照区域默认的大小写格式显示文本。默认值：true。

**返回值：**

类型说明string指定国家的本地化显示文本。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let countryName: string = i18n.getDisplayCountry('zh-CN', 'en-GB', true); // countryName = 'China'
countryName = i18n.getDisplayCountry('zh-CN', 'en-GB'); // countryName = 'China'
```

#### i18n.getDisplayLanguage(deprecated)

getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string

从API version 7开始支持，从API version 9开始废弃，建议使用[System.getDisplayLanguage](#ZH-CN_TOPIC_0000002529445281__getdisplaylanguage9)替代。

获取指定语言的本地化显示文本。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明languagestring是指定语言。localestring是[表示区域ID的字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-locale-culture#实现原理)，由语言、脚本、国家地区组成。sentenceCaseboolean否true表示按照首字母大写的格式显示文本，false表示按照区域默认的大小写格式显示文本。默认值：true。

**返回值：**

类型说明string指定语言的本地化显示文本。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let languageName: string = i18n.getDisplayLanguage('zh', 'en-GB', true); // languageName = 'Chinese'
languageName = i18n.getDisplayLanguage('zh', 'en-GB'); // languageName = 'Chinese'
```

#### i18n.getSystemLanguage(deprecated)

getSystemLanguage(): string

从API version 7开始支持，从API version 9开始废弃，建议使用[System.getSystemLanguage](#ZH-CN_TOPIC_0000002529445281__getsystemlanguage9)替代。

获取系统语言。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明string系统语言ID。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let systemLanguage: string = i18n.getSystemLanguage();
```

#### i18n.getSystemRegion(deprecated)

getSystemRegion(): string

从API version 7开始支持，从API version 9开始废弃，建议使用[System.getSystemRegion](#ZH-CN_TOPIC_0000002529445281__getsystemregion9)替代。

获取系统地区。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明string系统地区ID。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let region: string = i18n.getSystemRegion();
```

#### i18n.getSystemLocale(deprecated)

getSystemLocale(): string

从API version 7开始支持，从API version 9开始废弃，建议使用[System.getSystemLocale](#ZH-CN_TOPIC_0000002529445281__getsystemlocaledeprecated)代替。

获取系统区域ID。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明string系统区域ID。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let locale: string = i18n.getSystemLocale();
```

#### i18n.is24HourClock(deprecated)

is24HourClock(): boolean

从API version 7开始支持，从API version 9开始废弃，建议使用[System.is24HourClock](#ZH-CN_TOPIC_0000002529445281__is24hourclock9)替代。

判断系统时间是否为24小时制。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明booleantrue表示系统24小时开关开启，false表示系统24小时开关关闭。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let is24HourClock: boolean = i18n.is24HourClock();
```

#### i18n.set24HourClock(deprecated)

set24HourClock(option: boolean): boolean

从API version 7开始支持，从API version 9开始废弃，替代接口仅支持系统应用使用。

修改系统时间的24小时制设置。

**需要权限**：ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明optionboolean是true表示开启系统24小时制开关，false表示关闭系统24小时制开关。

**返回值：**

类型说明booleantrue表示修改成功，false表示修改失败。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

// 将系统时间设置为24小时制
let success: boolean = i18n.set24HourClock(true);
```

#### i18n.addPreferredLanguage(deprecated)

addPreferredLanguage(language: string, index?: number): boolean

从API version 8开始支持，从API version 9开始废弃，替代接口仅支持系统应用使用。

在系统偏好语言列表的指定位置添加偏好语言。

**需要权限**：ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明languagestring是待添加的偏好语言。indexnumber否偏好语言的添加位置。默认值：系统偏好语言列表长度。

**返回值：**

类型说明booleantrue表示添加成功，false表示添加失败。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

// 将语言zh-CN添加到系统偏好语言列表中
let language: string = 'zh-CN';
let index: number = 0;
let success: boolean = i18n.addPreferredLanguage(language, index);
```

#### i18n.removePreferredLanguage(deprecated)

removePreferredLanguage(index: number): boolean

从API version 8开始支持，从API version 9开始废弃，替代接口仅支持系统应用使用。

从系统偏好语言列表中移除指定位置的偏好语言。

**需要权限**：ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明indexnumber是待移除偏好语言在系统偏好语言列表中的位置。

**返回值：**

类型说明booleantrue表示移除成功，false表示移除失败。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

// 移除系统偏好语言列表中的第一个偏好语言
let index: number = 0;
let success: boolean = i18n.removePreferredLanguage(index);
```

#### i18n.getPreferredLanguageList(deprecated)

getPreferredLanguageList(): Array<string>

从API version 8开始支持，从API version 9开始废弃，建议使用[System.getPreferredLanguageList](#ZH-CN_TOPIC_0000002529445281__getpreferredlanguagelist9)替代。

获取系统偏好语言列表。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明Array<string>系统偏好语言列表。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let preferredLanguageList: Array<string> = i18n.getPreferredLanguageList();
```

#### i18n.getFirstPreferredLanguage(deprecated)

getFirstPreferredLanguage(): string

从API version 8开始支持，从API version 9开始废弃，建议使用[System.getFirstPreferredLanguage](#ZH-CN_TOPIC_0000002529445281__getfirstpreferredlanguage9)替代。

获取偏好语言列表中的第一个语言。

**系统能力：** SystemCapability.Global.I18n

**返回值：**

类型说明string偏好语言列表中的第一个语言。

**示例：**

```ets
import { i18n } from '@kit.LocalizationKit';

let firstPreferredLanguage: string = i18n.getFirstPreferredLanguage();
```

#### Util(deprecated)

#### unitConvert(deprecated)

unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: number, locale: string, style?: string): string

从API version 8开始支持，从API version 9开始废弃，建议使用[unitConvert](#ZH-CN_TOPIC_0000002529445281__unitconvert9)替代。

将fromUnit的单位转换为toUnit的单位，并根据区域与风格进行格式化。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明fromUnit[UnitInfo](#ZH-CN_TOPIC_0000002529445281__unitinfo8)是要被转换的单位。toUnit[UnitInfo](#ZH-CN_TOPIC_0000002529445281__unitinfo8)是要转换为的单位。valuenumber是要被转换的单位的数量值。localestring是格式化时使用的区域ID，如：zh-Hans-CN。stylestring否格式化使用的风格，取值包括：'long', 'short', 'narrow'。默认值：short。

**返回值：**

类型说明string按照toUnit的单位格式化后，得到的字符串。

#### Character(deprecated)

#### isDigit(deprecated)

isDigit(ch: string): boolean

从API version 8开始支持，从API version 9开始废弃，建议使用[isDigit](#ZH-CN_TOPIC_0000002529445281__isdigit9)替代。

判断输入的字符是否是数字。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是数字，false表示输入的字符不是数字。

#### isSpaceChar(deprecated)

isSpaceChar(ch: string): boolean

从API version 8开始支持，从API version 9开始废弃，建议使用[isSpaceChar](#ZH-CN_TOPIC_0000002529445281__isspacechar9)替代。

判断输入的字符是否是空格符。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是空格符，false表示输入的字符不是空格符。

#### isWhitespace(deprecated)

isWhitespace(ch: string): boolean

从API version 8开始支持，从API version 9开始废弃，建议使用[isWhitespace](#ZH-CN_TOPIC_0000002529445281__iswhitespace9)替代。

判断输入的字符是否是空白符。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是空白符，false表示输入的字符不是空白符。

#### isRTL(deprecated)

isRTL(ch: string): boolean

从API version 8开始支持，从API version 9开始废弃，建议使用[isRTL](#ZH-CN_TOPIC_0000002529445281__isrtl9)替代。

判断输入的字符是否是从右到左语言的字符。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是从右到左语言的字符，false表示输入的字符不是从右到左语言的字符。

#### isIdeograph(deprecated)

isIdeograph(ch: string): boolean

从API version 8开始支持，从API version 9开始废弃，建议使用[isIdeograph](#ZH-CN_TOPIC_0000002529445281__isideograph9)替代。

判断输入的字符是否是表意文字。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是表意文字，false表示输入的字符不是表意文字。

#### isLetter(deprecated)

isLetter(ch: string): boolean

从API version 8开始支持，从API version 9开始废弃，建议使用[isLetter](#ZH-CN_TOPIC_0000002529445281__isletter9)替代。

判断输入的字符是否是字母。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是字母，false表示输入的字符不是字母。

#### isLowerCase(deprecated)

isLowerCase(ch: string): boolean

从API version 8开始支持，从API version 9开始废弃，建议使用[isLowerCase](#ZH-CN_TOPIC_0000002529445281__islowercase9)替代。

判断输入的字符是否是小写字母。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是小写字母，false表示输入的字符不是小写字母。

#### isUpperCase(deprecated)

isUpperCase(ch: string): boolean

从API version 8开始支持，从API version 9开始废弃，建议使用[isUpperCase](#ZH-CN_TOPIC_0000002529445281__isuppercase9)替代。

判断输入的字符是否是大写字母。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明booleantrue表示输入的字符是大写字母，false表示输入的字符不是大写字母。

#### getType(deprecated)

getType(ch: string): string

从API version 8开始支持，从API version 9开始废弃，建议使用[getType](#ZH-CN_TOPIC_0000002529445281__gettype9)替代。

获取输入的字符的一般类别值。

**系统能力：** SystemCapability.Global.I18n

**参数：**

参数名类型必填说明chstring是输入的字符。如果输入的是字符串，则只判断首字符的类别。

**返回值：**

类型说明string输入字符的一般类别值。