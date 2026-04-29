# @ohos.intl (国际化-Intl)

本模块提供基础的应用国际化能力，包括时间日期格式化、数字格式化、排序等，相关接口在ECMA 402标准中定义。

[I18N模块](@ohos.i18n (国际化-I18n).md)提供其他非ECMA 402定义的国际化接口，与本模块共同使用可提供完整的国际化支持能力。

-

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块接口基于[CLDR](https://cldr.unicode.org)国际化数据库实现，随着CLDR标准的迭代演进，接口处理结果可能会相应调整。例如[数字格式化接口](#ZH-CN_TOPIC_0000002522081288__numberformat)，其返回值仅适用于界面展示场景，开发者请勿对返回格式进行硬编码或假设性判断，否则可能导致版本兼容问题。其中，API version 12 对应[CLDR 42](https://cldr.unicode.org/index/downloads/cldr-42)版本，具体数据变更详情可查阅CLDR官方文档。

-

从API version 11开始，本模块部分接口支持在ArkTS卡片中使用。

-

从API version 12开始，本模块全接口支持在元服务中使用。

#### 导入模块

```ets
import { intl } from '@kit.LocalizationKit';
```

#### Locale(deprecated)

#### 属性

从API version 6开始支持，从API version 20开始废弃，建议使用[Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)替代。

**卡片能力**：从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| language | string | 否 | 否 | 与区域设置相关的语言，如：zh。取值遵循ISO 639标准。 |
| script | string | 否 | 否 | 区域语言的书写方式（脚本），如：Hans。取值遵循Unicode ISO 15924标准。 |
| region | string | 否 | 否 | 与区域设置相关的国家地区，如：CN。取值遵循ISO 3166标准。 |
| baseName | string | 否 | 否 | 区域对象的基本信息，由语言、脚本、国家地区组成，如：zh-Hans-CN。 |
| caseFirst | string | 否 | 否 | 区域的排序规则是否考虑大小写，取值包括： "upper"：大写排前面。 "lower"：小写排前面。 "false"：使用区域默认的大小写排序规则。 |
| calendar | string | 否 | 否 | 区域的日历信息，取值包括： "buddhist", "chinese", "coptic","dangi", "ethioaa", "ethiopic", "gregory", "hebrew", "indian", "islamic", "islamic-umalqura", "islamic-tbla", "islamic-civil", "islamic-rgsa", "iso8601", "japanese", "persian", "roc", "islamicc"。 不同取值表示的含义请参考设置日历和历法表1。 |
| collation | string | 否 | 否 | 区域的排序规则，取值包括： "big5han"：拉丁字母使用的拼音排序。 "compat"：兼容性排序，仅用于阿拉伯语。 "dict"：词典风格排序，仅用于僧伽罗语。 "direct"：二进制码点排序。 "ducet"：按Unicode排序元素表排序。 "eor"：按欧洲排序规则排序。 "gb2312"：拼音排序，仅用于中文排序。 "phonebk"：电话本风格排序。 "phonetic"：发音排序。 "pinyin"：拼音排序。 "reformed"：瑞典语排序。 "searchjl"：韩语初始辅音搜索的特殊排序。 "stroke"：汉语的笔画排序。 "trad"：传统风格排序，如西班牙语。 "unihan"：统一汉字排序，用于日语、韩语、中文等汉字排序。 "zhuyin"：注音排序，仅用于中文排序。 |
| hourCycle | string | 否 | 否 | 区域的时制信息，取值包括： "h11"、"h12"、"h23"、"h24"。 不同取值的显示效果可参考附录表5。 |
| numberingSystem | string | 否 | 否 | 区域使用的数字系统，取值包括： "adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide", "gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham", "laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong", "mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment", "shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii", "wara", "wcho"。 |
| numeric | boolean | 否 | 否 | true表示对数字字符进行特殊的排序规则处理，false表示不对数字字符进行特殊的排序规则处理。 默认值：false。 |

#### constructor(deprecated)

constructor()

从API version 8开始支持，从API version 20开始废弃，建议使用[i18n.System.getSystemLocaleInstance](@ohos.i18n (国际化-I18n).md#ZH-CN_TOPIC_0000002553201253__getsystemlocaleinstance20)替代。

创建区域对象。

**卡片能力**：从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 默认构造函数使用系统当前区域ID创建
let locale = new intl.Locale();
// 返回系统当前区域ID
let localeID = locale.toString();
```

#### constructor(deprecated)

constructor(locale: string, options?: LocaleOptions)

从API version 6开始支持，从API version 20开始废弃，建议使用[Intl.Locale.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)替代。

创建区域对象。

**卡片能力**：从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | string | 是 | 表示区域ID的字符串，由语言、脚本、国家地区组成。 |
| options | LocaleOptions | 否 | 创建区域对象的选项。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 创建zh-CN区域对象
let locale = new intl.Locale('zh-CN');
let localeID = locale.toString(); // localeID = 'zh-CN'
```

#### toString(deprecated)

toString(): string

从API version 6开始支持，从API version 20开始废弃，建议使用[Intl.Locale.toString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/toString)替代。

获取区域对象的字符串。

**卡片能力**：从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 区域对象的字符串。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 创建en-GB区域对象
let locale = new intl.Locale('en-GB');
let localeID = locale.toString(); // localeID = 'en-GB'
```

#### maximize(deprecated)

maximize(): Locale

从API version 6开始支持，从API version 20开始废弃，建议使用[Intl.Locale.maximize](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/maximize)替代。

最大化区域信息，补齐区域对象中缺少的脚本、国家地区信息。

**卡片能力**：从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Locale | 补齐完脚本、国家地区信息后的区域对象。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 创建zh区域对象
let locale = new intl.Locale('zh');
// 补齐区域对象的脚本和地区
let maximizedLocale = locale.maximize();
let localeID = maximizedLocale.toString(); // localeID = 'zh-Hans-CN'

// 创建en-US区域对象
locale = new intl.Locale('en-US');
// 补齐区域对象的脚本
maximizedLocale = locale.maximize();
localeID = maximizedLocale.toString(); // localeID = 'en-Latn-US'
```

#### minimize(deprecated)

minimize(): Locale

从API version 6开始支持，从API version 20开始废弃，建议使用[Intl.Locale.minimize](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/minimize)替代。

最小化区域信息，移除区域对象中的脚本、国家地区信息。

**卡片能力**：从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Locale | 移除完脚本、国家地区信息后的区域对象。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 创建zh-Hans-CN区域对象
let locale = new intl.Locale('zh-Hans-CN');
// 移除区域对象的脚本和地区
let minimizedLocale = locale.minimize();
let localeID = minimizedLocale.toString(); // localeID = 'zh'

// 创建en-US区域对象
locale = new intl.Locale('en-US');
// 移除区域对象的地区
minimizedLocale = locale.minimize();
localeID = minimizedLocale.toString(); // localeID = 'en'
```

#### LocaleOptions(deprecated)

从API version 6开始支持，从API version 20开始废弃，以calendar为例，建议使用[Intl.LocaleOptions.calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/calendar)替代。

区域初始化选项。从API version 9开始，LocaleOptions属性由必填改为可选。

**卡片能力**：从API version 11开始，该类型支持在ArkTS卡片中使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| calendar | string | 否 | 是 | 历法参数，取值包括： "buddhist", "chinese", "coptic", "dangi", "ethioaa", "ethiopic", "gregory", "hebrew", "indian", "islamic", "islamic-umalqura", "islamic-tbla", "islamic-civil", "islamic-rgsa", "iso8601", "japanese", "persian", "roc", "islamicc"。 |
| collation | string | 否 | 是 | 区域的排序规则，取值包括： "big5han"：拉丁字母使用的拼音排序。 "compat"：兼容性排序，仅用于阿拉伯语。 "dict"：词典风格排序，仅用于僧伽罗语。 "direct"：二进制码点排序。 "ducet"：按Unicode排序元素表排序。 "eor"：按欧洲排序规则排序。 "gb2312"：拼音排序，仅用于中文排序。 "phonebk"：电话本风格排序。 "phonetic"：发音排序。 "pinyin"：拼音排序。 "reformed"：瑞典语排序。 "searchjl"：韩语初始辅音搜索的特殊排序。 "stroke"：汉语的笔画排序。 "trad"：传统风格排序，如西班牙语。 "unihan"：统一汉字排序，用于日语、韩语、中文等汉字排序。 "zhuyin"：注音排序，仅用于中文排序。 |
| hourCycle | string | 否 | 是 | 时制格式，取值包括： "h11", "h12", "h23", "h24"。 |
| numberingSystem | string | 否 | 是 | 数字系统，取值包括： "adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide", "gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham", "laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong", "mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment", "shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii", "wara", "wcho"。 |
| numeric | boolean | 否 | 是 | true表示将数字字符视为数字进行排序处理，false表示将数字字符视为普通字符进行排序处理。例如设置为true时，字符串“21”和字符串“123”比较，相当于数字21和123比较。默认值：false。 |
| caseFirst | string | 否 | 是 | 区域的排序规则是否考虑大小写，取值包括： "upper"：大写排前面。 "lower"：小写排前面。 "false"：使用区域默认的大小写排序规则。 |


- calendar：不同取值的含义请参考[设置日历和历法表1](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-calendar)。

#### DateTimeFormat(deprecated)

从API version 6开始支持，从API version 20开始废弃，建议使用[Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)替代。

提供日期格式化的能力。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

#### constructor(deprecated)

constructor()

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.DateTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat)替代。

创建时间、日期格式化对象。

**卡片能力**：从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用系统当前区域ID创建DateTimeFormat对象
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat();
```

#### constructor(deprecated)

constructor(locale: string | Array<string>, options?: DateTimeOptions)

从API version 6开始支持，从API version 20开始废弃，建议使用[Intl.DateTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat)替代。

创建时间、日期格式化对象。

**卡片能力**：从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | string | Array<string> | 是 | 区域ID或区域ID数组。输入是区域ID数组时，使用第一个有效的区域ID。 |
| options | DateTimeOptions | 否 | 创建时间、日期格式化对象时可设置的配置项。 若所有选项均未设置时，year、month、day三个属性的默认值为numeric。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用zh-CN区域ID创建DateTimeFormat对象，日期风格为full，时间风格为medium
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('zh-CN', { dateStyle: 'full', timeStyle: 'medium' });

// 使用区域ID列表创建DateTimeFormat对象，因为ban为非法区域ID，因此使用zh区域ID创建DateTimeFormat对象
formatter = new intl.DateTimeFormat(['ban', 'zh'], { dateStyle: 'full', timeStyle: 'medium' });
```

#### format(deprecated)

format(date: Date): string

从API version 6开始支持，从API version 20开始废弃，建议使用[Intl.DateTimeFormat.format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/format)替代。

对时间、日期进行格式化。

**卡片能力**：从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | Date | 是 | 时间、日期。说明：月份从0开始计数，例如0表示一月。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的时间、日期字符串。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

let date: Date = new Date(2021, 11, 17, 3, 24, 0); // 时间日期为2021.12.17 03:24:00
// 使用en-GB区域ID创建DateTimeFormat对象
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('en-GB');
let formattedDate: string = formatter.format(date); // formattedDate "17/12/2021"

// 使用en-GB区域ID创建DateTimeFormat对象，dateStyle设置为full，timeStyle设置为medium
formatter = new intl.DateTimeFormat('en-GB', { dateStyle: 'full', timeStyle: 'medium' });
formattedDate = formatter.format(date); // formattedDate "Friday, 17 December 2021, 03:24:00"
```

#### formatRange(deprecated)

formatRange(startDate: Date, endDate: Date): string

从API version 6开始支持，从API version 20开始废弃，建议使用[Intl.DateTimeFormat.formatRange](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/formatRange)替代。

对时间段、日期段进行格式化。

**卡片能力**：从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startDate | Date | 是 | 时间、日期的开始。说明：月份从0开始计数，例如0表示一月。 |
| endDate | Date | 是 | 时间、日期的结束。说明：月份从0开始计数，例如0表示一月。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的时间段、日期段字符串。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

let startDate: Date = new Date(2021, 11, 17, 3, 24, 0); // 时间日期为2021.12.17 03:24:00
let endDate: Date = new Date(2021, 11, 18, 3, 24, 0);
// 使用en-GB区域ID创建DateTimeFormat对象
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('en-GB');
let formattedDateRange: string = formatter.formatRange(startDate, endDate); // formattedDateRange = '17/12/2021 - 18/12/2021'
```

#### resolvedOptions(deprecated)

resolvedOptions(): DateTimeOptions

从API version 6开始支持，从API version 20开始废弃，建议使用[Intl.DateTimeFormat.resolvedOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions)替代。

获取创建时间、日期格式化对象时设置的配置项。

**卡片能力**：从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DateTimeOptions | 时间、日期格式化对象设置的配置项。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('en-GB', { dateStyle: 'full', timeStyle: 'medium' });
// 返回DateTimeFormat对象的配置项
let options: intl.DateTimeOptions = formatter.resolvedOptions();
let dateStyle: string | undefined = options.dateStyle; // dateStyle = 'full'
let timeStyle: string | undefined = options.timeStyle; // timeStyle = 'medium'
```

#### DateTimeOptions(deprecated)

从API version 6开始支持，从API version 20开始废弃，建议使用Intl.DateTimeFormatOptions和Intl.ResolvedDateTimeFormatOptions替代。用法参考[Intl.DateTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat)和[Intl.DateTimeFormat.resolvedOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions)。

时间、日期格式化时可设置的配置项。从API version 9开始，DateTimeOptions的属性由必填改为可选。

**卡片能力**：从API version 11开始，该类型支持在ArkTS卡片中使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| locale | string | 否 | 是 | 合法的区域ID，如：zh-Hans-CN。 默认值：系统当前区域ID。 |
| dateStyle | string | 否 | 是 | 日期显示格式，取值包括： "long", "short", "medium", "full", "auto"。 不同取值的显示效果请参考附录表1。 |
| timeStyle | string | 否 | 是 | 时间显示格式，取值包括： "long", "short", "medium", "full", "auto"。 不同取值的显示效果请参考附录表2。 |
| hourCycle | string | 否 | 是 | 时制格式，取值包括： "h11", "h12", "h23", "h24"。 不设置dateStyle或timeStyle参数时的显示效果请参考附录表5。 设置dateStyle或timeStyle参数时的显示效果请参考附录表6。 |
| timeZone | string | 否 | 是 | 使用的时区，取值为合法的IANA时区ID。 |
| numberingSystem | string | 否 | 是 | 数字系统，取值包括： "adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide", "gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham", "laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong", "mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment", "shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii", "wara", "wcho"。 |
| hour12 | boolean | 否 | 是 | true表示使用12小时制，false表示使用24小时制。 同时设置hour12和hourCycle时，hourCycle不生效。 若hour12和hourCycle未设置且系统24小时开关打开时，hour12属性的默认值为false。 |
| weekday | string | 否 | 是 | 星期的显示格式，取值包括： "long", "short", "narrow", "auto"。 不同取值的显示效果请参考附录表4。 |
| era | string | 否 | 是 | 纪元的显示格式，取值包括： "long", "short", "narrow", "auto"。 不同取值的显示效果请参考附录表9。 |
| year | string | 否 | 是 | 年份的显示格式，取值包括： "numeric", "2-digit"。 不同取值的显示效果请参考附录表3。 |
| month | string | 否 | 是 | 月份的显示格式，取值包括： "numeric", "2-digit", "long", "short", "narrow", "auto"。 不同取值的显示效果请参考附录表7。 |
| day | string | 否 | 是 | 日期的显示格式，取值包括： "numeric", "2-digit"。 |
| hour | string | 否 | 是 | 小时的显示格式，取值包括： "numeric", "2-digit"。 |
| minute | string | 否 | 是 | 分钟的显示格式，取值包括： "numeric", "2-digit"。 |
| second | string | 否 | 是 | 秒钟的显示格式，取值包括： "numeric", "2-digit"。 |
| timeZoneName | string | 否 | 是 | 时区名称的本地化表示，取值包括： "long", "short", "auto"。 不同取值的显示效果请参考附录表8。 |
| dayPeriod | string | 否 | 是 | 时段的显示格式，取值包括： "long", "short", "narrow", "auto"。 不同取值的显示效果请参考附录表10。 |
| localeMatcher | string | 否 | 是 | 要使用的区域匹配算法，取值包括： "lookup"：精确匹配。 "best fit"：最佳匹配。 |
| formatMatcher | string | 否 | 是 | 要使用的格式匹配算法，取值包括： "basic"：精确匹配。 "best fit"：最佳匹配。 |

#### NumberFormat

提供标准的数字格式化的能力。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

#### constructor8+

constructor()

使用当前系统区域创建数字格式化对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用系统当前区域ID创建NumberFormat对象
let formatter: intl.NumberFormat = new intl.NumberFormat();
```

#### constructor

constructor(locale: string | Array<string>, options?: NumberOptions)

根据指定的区域和配置项创建数字格式化对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | string | Array<string> | 是 | 区域ID或区域ID数组。输入是区域ID数组时，使用第一个有效的区域ID。 |
| options | NumberOptions | 否 | 创建数字格式化对象时可设置的配置项。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用en-GB区域ID创建NumberFormat对象，style设置为decimal，notation设置为scientific
let formatter: intl.NumberFormat = new intl.NumberFormat('en-GB', { style: 'decimal', notation: 'scientific' });
```

#### format

format(num: number): string

格式化数字。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| num | number | 是 | 数字对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的数字字符串。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用区域ID列表创建NumberFormat对象，因为en-GB为合法的区域ID，因此使用en-GB创建NumberFormat对象
let formatter: intl.NumberFormat = new intl.NumberFormat(['en-GB', 'zh'], { style: 'decimal', notation: 'scientific' });
let formattedNumber: string = formatter.format(1223); // formattedNumber = 1.223E3
let options: intl.NumberOptions = {
  roundingPriority: 'lessPrecision',
  maximumFractionDigits: 3,
  maximumSignificantDigits: 3
}
formatter = new intl.NumberFormat('en', options);
let result: string = formatter.format(1.23456); // result = 1.23
```

#### formatRange18+

formatRange(startRange: number, endRange: number): string

对数字范围进行格式化。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startRange | number | 是 | 开始数字。 |
| endRange | number | 是 | 结束数字。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的数字范围字符串。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

let formatter: intl.NumberFormat = new intl.NumberFormat('en-US', { style: 'unit', unit: 'meter' });
let formattedRange: string = formatter.formatRange(0, 3); // formattedRange: 0–3 m
```

#### resolvedOptions

resolvedOptions(): NumberOptions

获取创建数字格式化对象时设置的配置项。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**返回值：**

| 类型 | 说明 |
| --- | --- |
| NumberOptions | 创建数字格式化对象时设置的配置项。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

let formatter: intl.NumberFormat = new intl.NumberFormat(['en-GB', 'zh'], { style: 'decimal', notation: 'scientific' });
// 获取NumberFormat对象配置项
let options: intl.NumberOptions = formatter.resolvedOptions();
let style: string | undefined = options.style; // style = 'decimal'
let notation: string | undefined = options.notation; // notation = 'scientific'
```

#### NumberOptions

创建数字格式化对象时可设置的配置项。从API version 9开始，NumberOptions的属性由必填改为可选。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| locale | string | 否 | 是 | 合法的区域ID， 如："zh-Hans-CN"。 默认值：系统当前区域ID。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| currency | string | 否 | 是 | 货币单位， 取值符合ISO-4217标准，如："EUR"，"CNY"，"USD"等。 从API version 12开始支持三位数字代码，如："978"，"156"，"840"等。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| currencySign | string | 否 | 是 | 货币单位的符号显示，取值包括： "standard"，"accounting"。 默认值：standard。 元服务API：从API version 12开始，该接口支持在元服务中使用。 不同取值的显示效果请参考附录表19。 |
| currencyDisplay | string | 否 | 是 | 货币的显示方式，取值包括："symbol", "narrowSymbol", "code", "name"。 默认值：symbol。 元服务API：从API version 12开始，该接口支持在元服务中使用。 不同取值的显示效果请参考附录表20。 |
| unit | string | 否 | 是 | 单位名称，如："meter"，"inch"，“hectare”等。 从API version 18开始新增支持的组合单位有： "beat-per-minute", "body-weight-per-second", "breath-per-minute", "foot-per-hour", "jump-rope-per-minute", "meter-per-hour", "milliliter-per-minute-per-kilogram", "rotation-per-minute", "step-per-minute", "stroke-per-minute"。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| unitDisplay | string | 否 | 是 | 单位的显示格式，取值包括："long", "short", "narrow"。 默认值：short。 元服务API：从API version 12开始，该接口支持在元服务中使用。 不同取值的显示效果请参考附录表21。 |
| unitUsage8+ | string | 否 | 是 | 单位的使用场景，取值包括："default", "area-land-agricult", "area-land-commercl", "area-land-residntl", "length-person", "length-person-small", "length-rainfall", "length-road", "length-road-small", "length-snowfall", "length-vehicle", "length-visiblty", "length-visiblty-small", "length-person-informal", "length-person-small-informal", "length-road-informal", "speed-road-travel", "speed-wind", "temperature-person", "temperature-weather", "volume-vehicle-fuel", "elapsed-time-second", "size-file-byte", "size-shortfile-byte"。 默认值：default。 元服务API：从API version 12开始，该接口支持在元服务中使用。 不同取值的显示效果请参考附录表22。 |
| signDisplay | string | 否 | 是 | 数字符号的显示格式，取值包括： "auto"：自动判断是否显示正负符号。 "never"：不显示正负号。 "always"：总是显示正负号。 "exceptZero"：除了0都显示正负号。 默认值："auto"。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| compactDisplay | string | 否 | 是 | 紧凑显示格式，取值包括："long", "short"。 默认值：short。 元服务API：从API version 12开始，该接口支持在元服务中使用。 不同取值的显示效果请参考附录表18。 |
| notation | string | 否 | 是 | 数字的表示方法，取值包括："standard", "scientific", "engineering", "compact"。 默认值：standard。 元服务API：从API version 12开始，该接口支持在元服务中使用。 不同取值的显示效果请参考附录表17。 |
| localeMatcher | string | 否 | 是 | 要使用的区域匹配算法，取值包括："lookup", "best fit"。 默认值：best fit。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| style | string | 否 | 是 | 数字的显示格式，取值包括："decimal", "currency", "percent", "unit"。 默认值：decimal。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| numberingSystem | string | 否 | 是 | 数字系统，取值包括： "adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide", "gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham", "laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong", "mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment", "shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii", "wara", "wcho"。 默认值：区域的默认数字系统。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| useGrouping | boolean | 否 | 是 | true表示分组显示，false表示不分组显示。 默认值：true。 元服务API：从API version 12开始，该接口支持在元服务中使用。 不同取值的显示效果请参考附录表16。 |
| minimumIntegerDigits | number | 否 | 是 | 表示要使用的最小整数位数，取值范围：1~21。 默认值：1。 元服务API：从API version 12开始，该接口支持在元服务中使用。 不同取值的显示效果请参考附录表11。 |
| minimumFractionDigits | number | 否 | 是 | 表示要使用的最小分数位数，取值范围：0~20。 默认值：0。 元服务API：从API version 12开始，该接口支持在元服务中使用。 不同取值的显示效果请参考附录表12。 |
| maximumFractionDigits | number | 否 | 是 | 表示要使用的最大分数位数，取值范围：1~21。 默认值：3。 元服务API：从API version 12开始，该接口支持在元服务中使用。 不同取值的显示效果请参考附录表13。 |
| minimumSignificantDigits | number | 否 | 是 | 表示要使用的最小有效位数，取值范围：1~21。 默认值：1。 元服务API：从API version 12开始，该接口支持在元服务中使用。 不同取值的显示效果请参考附录表14。 |
| maximumSignificantDigits | number | 否 | 是 | 表示要使用的最大有效位数，取值范围：1~21。 默认值：21。 元服务API：从API version 12开始，该接口支持在元服务中使用。 不同取值的显示效果请参考附录表15。 |
| roundingPriority18+ | string | 否 | 是 | 最大分数位数和最大有效位数同时设置时的舍入优先级，取值包括："auto"，"morePrecision" 取最大分数位数，"lessPrecision" 取最大有效位数。 默认值：auto。 元服务API：从API version 18开始，该接口支持在元服务中使用。 |
| roundingIncrement18+ | number | 否 | 是 | 表示舍入增量，取值范围：1，2，5，10，20，25，50，100，200，250，500，1000，2000，2500，5000。 默认值：1。 元服务API：从API version 18开始，该接口支持在元服务中使用。 |
| roundingMode18+ | string | 否 | 是 | 表示舍入模式，取值包括： "ceil"：向上取整。 "floor"：向下取整。 "expand"：远离零取整。 "trunc"：向零取整。 "halfCeil"：半向上取整，大于等于增量的一半时向上取整，小于增量的一半时向下取整。 "halfFloor"：半向下取整，大于增量的一半时向上取整，小于等于增量的一半时向下取整。 "halfExpand"：半远离零取整，大于等于增量的一半时远离零取整，小于增量的一半时向零取整。 "halfTrunc"：半向零取整，大于增量的一半时远离零取整，小于等于增量的一半时向零取整。 "halfEven"：半向偶数取整，大于增量的一半时 远离零取整，小于增量的一半时向零取整，等于增量的一半时向最近的偶数位舍入。 默认值：halfExpand。 元服务API：从API version 18开始，该接口支持在元服务中使用。 |

#### Collator8+

提供字符串排序的能力。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

#### constructor8+

constructor()

使用当前系统区域创建排序对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用系统区域创建Collator对象
let collator = new intl.Collator();
```

#### constructor8+

constructor(locale: string | Array<string>, options?: CollatorOptions)

根据指定的区域和配置项创建排序对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | string | Array<string> | 是 | 区域ID或区域ID数组。输入是区域ID数组时，使用第一个有效的区域ID。 |
| options | CollatorOptions | 否 | 创建排序对象时可设置的配置项。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用zh-CN区域ID创建Collator对象，localeMatcher设置为lookup，usage设置为sort
let collator = new intl.Collator('zh-CN', {localeMatcher: 'lookup', usage: 'sort'});
```

#### compare8+

compare(first: string, second: string): number

根据配置项的排序规则，比较两个字符串。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| first | string | 是 | 进行比较的第一个字符串。 |
| second | string | 是 | 进行比较的第二个字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 比较结果。 - number为负数时，表示first排序在second之前。 - number为0时，表示first与second排序相同。 - number为正数，表示first排序在second之后。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用en-GB区域ID创建Collator对象
let collator = new intl.Collator('en-GB');
// 比较first和second的先后顺序
let compareResult = collator.compare('first', 'second'); // compareResult = -1
```

#### resolvedOptions8+

resolvedOptions(): CollatorOptions

获取创建排序对象时设置的配置项。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CollatorOptions | 返回排序对象的属性。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

let collator = new intl.Collator('zh-Hans', { usage: 'sort', ignorePunctuation: true });
// 获取Collator对象的配置项
let options = collator.resolvedOptions();
let usage = options.usage; // usage = 'sort'
let ignorePunctuation = options.ignorePunctuation; // ignorePunctuation = true
```

#### CollatorOptions8+

创建排序对象时可设置的配置项。

从API version 9中，CollatorOptions中的属性改为可选。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| localeMatcher | string | 否 | 是 | 区域匹配算法，取值范围： "lookup"：模糊匹配。 "best fit"：准确匹配。 默认值："best fit"。 |
| usage | string | 否 | 是 | 比较的用途，取值范围： "sort"：用作排序。 "search"：用作查找匹配的字符串。 默认值："sort"。 |
| sensitivity | string | 否 | 是 | 表示字符串中的哪些差异会导致非零结果值，取值范围： "base"：不同的字母比较不相等，比如：'a' ≠ 'b', 'a' = 'á', 'a' = 'A'。 "accent"：不同的字母或不同读音的相同字母比较不相等，比如'a' ≠ 'b', 'a' ≠ 'á', 'a' = 'A'。 "case"：不同的字母或相同字母大小写比较不相等，比如：'a' ≠ 'b', 'a' = 'á', 'a' ≠ 'A'。 "variant"：不同的字母或读音及其它有区别的标志或大小写都是不相等的，比如：'a' ≠ 'b', 'a' ≠ 'á', 'a' ≠ 'A'。 默认值："variant"。 |
| ignorePunctuation | boolean | 否 | 是 | true表示忽略标点符号，false表示考虑标点符号。 默认值：false。 |
| collation | string | 否 | 是 | 区域的排序规则，取值包括： "big5han"：拉丁字母使用的拼音排序。 "compat"：兼容性排序，仅用于阿拉伯语。 "dict"：词典风格排序，仅用于僧伽罗语。 "direct"：二进制码点排序。 "ducet"：按Unicode排序元素表排序。 "eor"：按欧洲排序规则排序。 "gb2312"：拼音排序，仅用于中文排序。 "phonebk"：电话本风格排序。 "phonetic"：发音排序。 "pinyin"：拼音排序。 "reformed"：瑞典语排序。 "searchjl"：韩语初始辅音搜索的特殊排序。 "stroke"：汉语的笔画排序。 "trad"：传统风格排序，如西班牙语。 "unihan"：统一汉字排序，用于日语、韩语、中文等汉字排序。 "zhuyin"：注音排序，仅用于中文排序。 默认值："default"。 |
| numeric | boolean | 否 | 是 | 数字排序，取值包括： true：使用数字排序，比如：'1' < '2' < '10' < '11'。 false：不使用数字排序，比如：'1' < '10' < '11' < '2'。 默认值：false。 |
| caseFirst | string | 否 | 是 | 区域的排序规则是否考虑大小写，取值包括： "upper"：大写排前面。 "lower"：小写排前面。 "false"：使用区域默认的大小写排序规则。 默认值："false"。 |

#### PluralRules(deprecated)

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules)替代。

提供获取单复数类型的能力。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

#### constructor(deprecated)

constructor()

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules)替代。

创建单复数对象来计算数字的单复数类别。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用系统区域创建PluralRules对象
let pluralRules = new intl.PluralRules();
```

#### constructor(deprecated)

constructor(locale: string | Array<string>, options?: PluralRulesOptions)

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules)替代。

创建单复数对象来计算数字的单复数类别。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | string | Array<string> | 是 | 区域ID或区域ID数组。输入是区域ID数组时，使用第一个有效的区域ID。 |
| options | PluralRulesOptions | 否 | 创建单复数对象时设置的配置项。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用zh-CN区域ID创建PluralRules对象，localeMatcher设置为lookup，type设置为cardinal
let pluralRules: intl.PluralRules = new intl.PluralRules('zh-CN', { localeMatcher: 'lookup', type: 'cardinal' });
```

#### select(deprecated)

select(n: number): string

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.PluralRules.select](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/select)替代。

获取数字的单复数类别。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | number | 是 | 待获取单复数类别的数字。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 单复数类别，取值包括："zero"，"one"，"two", "few", "many", "others"。 不同取值的含义请参考语言单复数规则。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用zh-Hans区域ID创建PluralRules对象
let zhPluralRules = new intl.PluralRules('zh-Hans');
// 计算zh-Hans区域中数字1对应的单复数类别
let plural = zhPluralRules.select(1); // plural = 'other'

// 使用en-US区域ID创建PluralRules对象
let enPluralRules = new intl.PluralRules('en-US');
// 计算en-US区域中数字1对应的单复数类别
plural = enPluralRules.select(1); // plural = 'one'
```

#### PluralRulesOptions(deprecated)

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.PluralRulesOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules)替代。

创建单复数对象时可设置的配置项。从API version 9开始，PluralRulesOptions的属性由必填改为可选。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| localeMatcher(deprecated) | string | 否 | 是 | 从API version 8开始支持，从API version 20开始废弃，建议使用Intl.PluralRulesOptions.localeMatcher替代，用法参考Intl.PluralRules。 区域匹配算法，取值包括："best fit", "lookup"。 默认值：best fit。 |
| type(deprecated) | string | 否 | 是 | 从API version 8开始支持，从API version 20开始废弃，建议使用Intl.PluralRulesOptions.type替代，用法参考Intl.PluralRules。 排序的类型，取值包括："cardinal", "ordinal", 默认值：cardinal。 - cardinal：基数词，ordinal：序数词。 |
| minimumIntegerDigits(deprecated) | number | 否 | 是 | 从API version 8开始支持，从API version 20开始废弃，建议使用Intl.PluralRulesOptions.minimumIntegerDigits替代，用法参考Intl.PluralRules。 表示要使用的最小整数位数，取值范围：1~21。 默认值：1。 |
| minimumFractionDigits(deprecated) | number | 否 | 是 | 从API version 8开始支持，从API version 20开始废弃，建议使用Intl.PluralRulesOptions.minimumFractionDigits替代，用法参考Intl.PluralRules。 表示要使用的最小分数位数，取值范围：0~20。 默认值：0。 |
| maximumFractionDigits(deprecated) | number | 否 | 是 | 从API version 8开始支持，从API version 20开始废弃，建议使用Intl.PluralRulesOptions.maximumFractionDigits替代，用法参考Intl.PluralRules。 表示要使用的最大分数位数，取值范围：1~21。 默认值：3。 |
| minimumSignificantDigits(deprecated) | number | 否 | 是 | 从API version 8开始支持，从API version 20开始废弃，建议使用Intl.PluralRulesOptions.minimumSignificantDigits替代，用法参考Intl.PluralRules。 表示要使用的最小有效位数，取值范围：1~21。 默认值：1。 |
| maximumSignificantDigits(deprecated) | number | 否 | 是 | 从API version 8开始支持，从API version 20开始废弃，建议使用Intl.PluralRulesOptions.maximumSignificantDigits替代，用法参考Intl.PluralRules。 表示要使用的最大有效位数，取值范围：1~21。 默认值：21。 |

#### RelativeTimeFormat(deprecated)

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.RelativeTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)替代。

提供相对时间格式化的能力。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

#### constructor(deprecated)

constructor()

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.RelativeTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)替代。

创建相对时间格式化对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用系统区域创建RelativeTimeFormat对象
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat();
```

#### constructor(deprecated)

constructor(locale: string | Array<string>, options?: RelativeTimeFormatInputOptions)

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.RelativeTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)替代。

创建相对时间格式化对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | string | Array<string> | 是 | 区域ID或区域ID数组。输入是区域ID数组时，使用第一个有效的区域ID。 |
| options | RelativeTimeFormatInputOptions | 否 | 创建相对时间格式化对象时可配置的选项。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用zh-CN区域ID创建RelativeTimeFormat对象，localeMatcher设置为lookup，numeric设置为always，style设置为long
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('zh-CN', {
  localeMatcher: 'lookup',
  numeric: 'always',
  style: 'long'
});
```

#### format(deprecated)

format(value: number, unit: string): string

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.RelativeTimeFormat.format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format)替代。

对相对时间进行格式化。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 相对时间格式化的数值。 |
| unit | string | 是 | 相对时间格式化的单位， 取值包括："year", "quarter", "month", "week", "day", "hour", "minute", "second"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的相对时间。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用zh-CN区域ID创建RelativeTimeFormat对象
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('zh-CN');
// 计算zh-CN区域中数字3，单位quarter的本地化表示
let formatResult: string = formatter.format(3, 'quarter'); // formatResult = '3个季度后'
```

#### formatToParts(deprecated)

formatToParts(value: number, unit: string): Array<object>

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.RelativeTimeFormat.formatToParts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/formatToParts)替代。

对相对时间进行格式化，获取格式化结果中各个部分的对象数组。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 相对时间格式化的数值。 |
| unit | string | 是 | 相对时间格式化的单位， 取值包括："year", "quarter", "month", "week", "day", "hour", "minute", "second"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<object> | 格式化结果中各个部分的对象数组。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用en区域ID创建RelativeTimeFormat对象，numeric设置为auto
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('en', { numeric: 'auto' });
let parts: Array<object> = formatter.formatToParts(10, 'seconds'); // parts = [ {type: 'literal', value: 'in'}, {type: 'integer', value: 10, unit: 'second'}, {type: 'literal', value: 'seconds'} ]
```

#### resolvedOptions(deprecated)

resolvedOptions(): RelativeTimeFormatResolvedOptions

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.RelativeTimeFormat.resolvedOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions)替代。

获取相对时间格式化对象的格式化配置项。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RelativeTimeFormatResolvedOptions | 相对时间格式化对象的格式化配置项。 |

**示例：**

```ets
import { intl } from '@kit.LocalizationKit';

// 使用en-GB区域ID创建RelativeTimeFormat对象
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('en-GB', { style: 'short' });
// 获取RelativeTimeFormat对象配置项
let options: intl.RelativeTimeFormatResolvedOptions = formatter.resolvedOptions();
let style: string = options.style; // style = 'short'
```

#### RelativeTimeFormatInputOptions(deprecated)

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.RelativeTimeFormatOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#options)替代。

创建相对时间格式化对象时可设置的配置项。

从API version 9开始，RelativeTimeFormatInputOptions中的属性改为可选。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| localeMatcher | string | 否 | 是 | 区域匹配算法，取值包括："best fit", "lookup"。 默认值：best fit。 |
| numeric | string | 否 | 是 | 输出消息的格式，表示格式化结果中是否使用数字表示相对日期或时间。取值包括："always", "auto"。 默认值：always。 不同取值的显示效果请参考附录表23。 |
| style | string | 否 | 是 | 国际化消息的长度，取值包括："long", "short", "narrow"。 默认值：long。 不同取值的显示效果请参考附录表24。 |

#### RelativeTimeFormatResolvedOptions(deprecated)

从API version 8开始支持，从API version 20开始废弃，建议使用[Intl.RelativeTimeFormatOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions#return_value)替代。

相对时间格式化对象的格式化配置项。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.I18n

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| locale | string | 否 | 否 | 表示区域ID的字符串，包括语言以及可选的脚本和区域。 |
| numeric | string | 否 | 否 | 输出消息的格式，表示格式化结果中是否使用数字表示相对日期或时间。取值包括："always", "auto"。 不同取值的显示效果请参考附录表23。 |
| style | string | 否 | 否 | 国际化消息的长度，取值包括："long", "short", "narrow"。 不同取值的显示效果请参考附录表24。 |
| numberingSystem | string | 否 | 否 | 使用的数字系统，取值包括： "adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide", "gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham", "laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong", "mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment", "shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii", "wara", "wcho"。 |

#### 附录

**时间日期格式化选项**

下方表格以时间：2021年9月17日 13:04:00、2021年9月17日 00:25:00和区域ID: zh-CN、en为例，说明[DateTimeOptions](#ZH-CN_TOPIC_0000002522081288__datetimeoptionsdeprecated)的取值和显示结果。

**表1** 日期显示格式(dateStyle)

| 取值 | 描述 | 2021年9月17日 13:04:00，区域ID为zh-CN显示结果 | 2021年9月17日 13:04:00，区域ID为en显示结果 |
| --- | --- | --- | --- |
| full | 完整的日期显示，包含年份、月份、天数和星期。 | 2021年9月17日星期五 | Friday, September 17, 2021 |
| long | 详细的日期显示，包含年份、月份和天数。 | 2021年9月17日 | September 17, 2021 |
| short | 简短的日期显示，包含年份、月份和天数。 | 2021/9/17 | 9/17/21 |
| medium | 中等长度日期显示，包含年份、月份和天数。 | 2021年9月17日 | Sep 17, 2021 |

**表2** 时间显示格式(timeStyle)

| 取值 | 描述 | 2021年9月17日 13:04:00，区域ID为zh-CN显示结果 | 2021年9月17日 13:04:00，区域ID为en显示结果 |
| --- | --- | --- | --- |
| full | 完整的时间显示，包含时区和时间，时间精确到秒。 | 中国标准时间 13:04:00 | 13:04:00 China Standard Time |
| long | 详细的时间显示，包含时区和时间，时区以GMT+时区偏移表示，时间精确到秒。 | GMT+8 13:04:00 | 13:04:00 GMT+8 |
| short | 简短时间显示，包含小时和分钟。 | 13:04 | 13:04 |
| medium | 中等长度时间显示，包含小时、分钟和秒。 | 13:04:00 | 13:04:00 |

**表3** 年份显示格式(year)

| 取值 | 描述 | 2021年9月17日 13:04:00，区域ID为zh-CN显示结果 | 2021年9月17日 13:04:00，区域ID为en显示结果 |
| --- | --- | --- | --- |
| numeric | 完整的年份显示。 | 2021年 | 2021 |
| 2-digit | 用完整年份的后2位数字表示年份。 | 21年 | 21 |

**表4** 星期显示格式(weekday)

| 取值 | 描述 | 2021年9月17日 13:04:00，区域ID为zh-CN显示结果 | 2021年9月17日 13:04:00，区域ID为en显示结果 |
| --- | --- | --- | --- |
| long | 详细的星期显示。 | 星期五 | Friday |
| short | 简短的星期显示。 | 周五 | Fri |
| narrow | 最简短的星期显示。 | 五 | F |

**表5** 时制格式(hourCycle)

| 取值 | 描述 | 2021年9月17日 13:04:00，区域ID为zh-CN显示结果 | 2021年9月17日 00:25:00，区域ID为zh-CN显示结果 |
| --- | --- | --- | --- |
| h11 | 用0-11表示小时。 | 下午1:04 | 上午0:25 |
| h12 | 用1-12表示小时。 | 下午1:04 | 上午12:25 |
| h23 | 用0-23表示小时。 | 13:04 | 00:25 |
| h24 | 用1-24表示小时。 | 13:04 | 24:25 |


不设置dateStyle或timeStyle参数时，hourCycle不同取值的显示效果如上表格。

**表6** 时制格式(hourCycle)

| 取值 | 描述 | 2021年9月17日 13:04:00，区域ID为zh-CN显示结果 | 2021年9月17日 00:25:00，区域ID为zh-CN显示结果 |
| --- | --- | --- | --- |
| h11 | 用1-24表示小时。 | 下午13:04 | 上午24:25 |
| h12 | 用1-12表示小时。 | 下午1:04 | 上午12:25 |
| h23 | 用0-11表示小时。 | 1:04 | 0:25 |
| h24 | 用0-23表示小时。 | 13:04 | 0:25 |


设置dateStyle或timeStyle参数时，hourCycle不同取值的显示效果如上表格。

**表7** 月份格式(month)

| 取值 | 描述 | 2021年9月17日 13:04:00，区域ID为zh-CN显示结果 | 2021年9月17日 13:04:00，区域ID为en显示结果 |
| --- | --- | --- | --- |
| numeric | 以数字形式显示月份。 | 9月 | 9 |
| 2-digit | 以两位数字形式显示月份。 | 09月 | 09 |
| long | 详细的月份显示。 | 九月 | September |
| short | 简短的月份显示。 | 9月 | Sep |
| narrow | 最简短的月份显示。 | 9 | S |

**表8** 时区名称的本地化表示(timeZoneName)

| 取值 | 描述 | 2021年9月17日 13:04:00，区域ID为zh-CN显示结果 | 2021年9月17日 13:04:00，区域ID为en显示结果 |
| --- | --- | --- | --- |
| long | 详细的时区名称显示。 | 中国标准时间 | China Standard Time |
| short | 简短的时区名称显示。 | GMT+8 | GMT+8 |

**表9** 纪元的显示格式(era)

| 取值 | 描述 | 2021年9月17日 13:04:00，区域ID为zh-CN显示效果 | 2021年9月17日 13:04:00，区域ID为en显示效果 |
| --- | --- | --- | --- |
| long | 详细的纪元显示。 | 公元 | Anno Domini |
| short | 简短的纪元显示。 | 公元 | AD |
| narrow | 最简短的纪元显示。 | 公元 | A |

**表10** 时段的显示格式(dayPeriod)

| 取值 | 描述 | 2021年9月17日 13:04:00，区域ID为zh-CN显示效果 | 2021年9月17日 13:04:00，区域ID为en显示效果 |
| --- | --- | --- | --- |
| long | 详细的时段表述。 | 下午 | in the afternoon |
| short | 简短的时段表示。 | 下午 | in the afternoon |
| narrow | 最简短的时段表示。 | 下午 | in the afternoon |

**数字格式化选项**

通过数字格式化选项可以设置最小整数位数、最小小数位数、最大小数位数、最小有效位数、最大有效位数、是否分组显示、数字的表示方法、紧凑显示格式、舍入模式、舍入优先级、舍入增量以及数字的显示格式和数字系统。其中，数字的显示格式包括decimal(十进制)、percent(百分数)、currency(货币)和unit(单位)。

以123000.123为例，各选项取值和显示效果如下表所示：

**表11** 最小整数位数(minimumIntegerDigits)

| 取值 | 显示效果 |
| --- | --- |
| 6 | 123,000.123 |
| 7 | 0,123,000.123 |

**表12** 最小小数位数(minimumFractionDigits)

| 取值 | 显示效果 |
| --- | --- |
| 3 | 123,000.123 |
| 4 | 123,000.1230 |

**表13** 最大小数位数(maximumFractionDigits)

| 取值 | 显示效果 |
| --- | --- |
| 3 | 123,000.123 |
| 2 | 123,000.12 |

**表14** 最小有效位数(minimumSignificantDigits)

| 取值 | 显示效果 |
| --- | --- |
| 9 | 123,000.123 |
| 10 | 123,000.1230 |

**表15** 最大有效位数(maximumSignificantDigits)

| 取值 | 显示效果 |
| --- | --- |
| 9 | 123,000.123 |
| 8 | 123,000.12 |

**表16** 是否分组显示(useGrouping)

| 取值 | 显示效果 |
| --- | --- |
| true | 123,000.123 |
| false | 123000.123 |

**表17** 数字的表示方法(notation)

| 取值 | 显示效果 |
| --- | --- |
| standard | 123,000.123 |
| scientific | 1.230001E5 |
| engineering | 123.000123E3 |
| compact | 123K |

**表18** 紧凑显示格式(compactDisplay)

| 取值 | 显示效果 |
| --- | --- |
| short | 123K |
| long | 123 thousand |

**货币格式化选项**

以货币单位USD，数字大小-12300为例。

**表19** 货币单位的符号(currencySign)

| 取值 | 显示效果 |
| --- | --- |
| standard | -US$12,300.00 |
| accounting | (US$12,300.00) |

**表20** 货币的显示方式(currencyDisplay)

| 取值 | 显示效果 |
| --- | --- |
| symbol | -US$12,300.00 |
| narrowSymbol | -$12,300.00 |
| code | -USD 12,300.00 |
| name | -12,300.00 US dollars |

**单位格式化选项**

以单位hectare，数字大小-12300为例。

**表21** 单位的显示格式(unitDisplay)

| 取值 | 显示效果 |
| --- | --- |
| long | -12,3000 hectares |
| short | -12,300 ha |
| narrow | -12,300ha |

**表22** 单位的使用场景(unitUsage)

| 取值 | 显示效果 |
| --- | --- |
| 未设置 | -12,300 ha |
| default | -47.491 sq mi |
| area-land-agricult | -30,393.962 ac |

**相对时间格式化选项**

以相对时间：一天前，区域ID: fr-FR和en-GB为例。

**表23** 数值表示(numeric)

| 取值 | 描述 | 显示效果(fr-FR) | 显示效果(en-GB) |
| --- | --- | --- | --- |
| always | 使用数值表示相对时间。 | il y a 1 jour | 1 day ago |
| auto | 根据区域ID自适应选择短语或数值表示相对时间。 | hier | yesterday |

**表24** 相对时间样式(style)

| 取值 | 描述 | 显示效果(fr-FR) | 显示效果(en-GB) |
| --- | --- | --- | --- |
| long | 详细的相对时间显示。 | il y a 1 jour | 1 day ago |
| short | 简短的相对时间显示。 | il y a 1 j | 1 day ago |
| narrow | 最简短的相对时间显示。 | -1 j | 1 day ago |