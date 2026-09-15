# @ohos.i18n.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * @file
 * @kit LocalizationKit
 */
import intl from './@ohos.intl';
/**
 * This module provides system-related and enhanced [i18n](docroot://internationalization/i18n-l10n.md) capabilities,
 * such as locale management, phone number formatting, and calendar, through supplementary i18n APIs that are not
 * defined in [ECMA 402](https://dev.ecma-international.org/publications-and-standards/standards/ecma-402/). The
 * [intl]{@link @ohos.intl:intl} module provides basic i18n capabilities through the standard i18n APIs defined in ECMA
 * 402. It works with the **i18n** module to provide a complete suite of i18n capabilities. The terms used in the APIs
 * are defined as follows:
 *
 * - Pattern string, which is a string consisting of
 * [Unicode date field symbols](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table) and custom
 * text enclosed by single quotation marks.
 * - Skeleton string: a string that consists of
 * [Unicode date field symbols](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table) and does
 * not support custom text.
 *
 * > **NOTE**
 * >
 * > - The APIs of this module are based on the [CLDR](https://cldr.unicode.org) internationalization database. The
 * > processing results of the APIs may be adjusted as the CLDR standard evolves. For example, the return value of the
 * > [date and time formatting API]{@link i18n.SimpleNumberFormat} is used only for UI display. Do not hardcode the
 * > return value or make assumptions about the return value. Otherwise, version compatibility problems may occur. API
 * > version 12 corresponds to [CLDR 42](https://cldr.unicode.org/index/downloads/cldr-42). For details about data
 * > changes, see the official CLDR documentation.
 * >
 * > - Since API version 11, some APIs of this module are supported in ArkTS widgets.
 *
 * @syscap SystemCapability.Global.I18n
 * @crossplatform [since 11]
 * @form [since 11]
 * @atomicservice [since 11]
 * @since 7
 */
declare namespace i18n {
    /**
     * Obtains the localized name of the specified country/region.
     *
     * @param { string } country - Specified country.
     * @param { string } locale - [System locale](docroot://internationalization/i18n-locale-culture.md#how-it-works),
     *     which consists of the language, script, and country/region.
     * @param { boolean } [sentenceCase] - Whether to use sentence case to display the text. The value **true** means to
     *     display the text in title case format, and the value **false** means to display the text in the default case
     *     format of the locale. The default value is **true**.
     * @returns { string } Localized script for the specified country.
     * @syscap SystemCapability.Global.I18n
     * @since 7
     * @deprecated since 9
     * @useinstead i18n.System.getDisplayCountry
     */
    export function getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string;
    /**
     * Obtains the localized script for the specified language.
     *
     * @param { string } language - Specified language.
     * @param { string } locale - [System locale](docroot://internationalization/i18n-locale-culture.md#how-it-works),
     *     which consists of the language, script, and country/region.
     * @param { boolean } [sentenceCase] - Whether to use sentence case to display the text. The value **true** means to
     *     display the text in title case format, and the value **false** means to display the text in the default case
     *     format of the locale. The default value is **true**.
     * @returns { string } Localized script for the specified language.
     * @syscap SystemCapability.Global.I18n
     * @since 7
     * @deprecated since 9
     * @useinstead i18n.System.getDisplayLanguage
     */
    export function getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string;
    /**
     * Obtains the system language.
     *
     * @returns { string } System language ID.
     * @syscap SystemCapability.Global.I18n
     * @since 7
     * @deprecated since 9
     * @useinstead i18n.System.getSystemLanguage
     */
    export function getSystemLanguage(): string;
    /**
     * Obtains the system region.
     *
     * @returns { string } System region ID.
     * @syscap SystemCapability.Global.I18n
     * @since 7
     * @deprecated since 9
     * @useinstead i18n.System.getSystemRegion
     */
    export function getSystemRegion(): string;
    /**
     * Obtains the system locale.
     *
     * @returns { string } System locale ID.
     * @syscap SystemCapability.Global.I18n
     * @since 7
     * @deprecated since 9
     * @useinstead i18n.System.getSystemLocale
     */
    export function getSystemLocale(): string;
    /**
     * Provides system attribute configuration functions, including translating language and country/region names,
     * obtaining the list of supported languages and countries/regions, and obtaining the system language and region.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @form [since 11]
     * @atomicservice [since 11]
     * @since 9
     */
    export class System {
        /**
         * Obtains the country/region display name in the specified language.
         *
         * @param { string } country - Valid country/region code. For details, see
         *     [System Locale](docroot://internationalization/i18n-locale-culture.md#how-it-works).
         * @param { string } locale - [System locale](docroot://internationalization/i18n-locale-culture.md#how-it-works),
         *     which consists of the language, script, and country/region.
         * @param { boolean } [sentenceCase] - Whether to use sentence case to display the text. The value **true** means to
         *     display the text in title case format, and the value **false** means to display the text in the default case
         *     format of the locale. The default value is **true**.
         * @returns { string } Country/region display name in the specified language.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string;
        /**
         * Obtains the language display name in the specified language.
         *
         * @param { string } language - Valid language ID. For details, see
         *     [System Locale](docroot://internationalization/i18n-locale-culture.md#how-it-works).
         * @param { string } locale - [System locale](docroot://internationalization/i18n-locale-culture.md#how-it-works),
         *     which consists of the language, script, and country/region.
         * @param { boolean } [sentenceCase] - Whether to use sentence case to display the text. The value **true** means to
         *     display the text in title case format, and the value **false** means to display the text in the default case
         *     format of the locale. The default value is **true**.
         * @returns { string } Language display name in the specified language.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string;
        /**
         * Obtains the list of system languages.
         * Since API version 11, this API is supported in ArkTS widgets.
         *
         * @returns { Array<string> } List of system languages.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 9
         */
        static getSystemLanguages(): Array<string>;
        /**
         * Obtains the list of countries/regions supported for the specified language.
         *
         * @param { string } language -
         *     [Valid language ID](docroot://internationalization/i18n-locale-culture.md#how-it-works).
         * @returns { Array<string> } List of countries/regions supported for the specified language.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 9
         */
        static getSystemCountries(language: string): Array<string>;
        /**
         * Checks whether a language is a suggested language in the specified region. It can be used for region-based
         * language recommendation or language-based region recommendation.
         *
         * @param { string } language -
         *     [Valid language ID](docroot://internationalization/i18n-locale-culture.md#how-it-works), for example, **zh**.
         * @param { string } [region] -
         *     [Valid country/region code](docroot://internationalization/i18n-locale-culture.md#how-it-works), for example,
         *     **CN**.
         *   The default value is the country/region of the SIM card.
         * @returns { boolean } Whether a language is a suggested language. The value **true** indicates that the language
         *     is a suggested language of the region, the the value false indicates the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 9
         */
        static isSuggested(language: string, region?: string): boolean;
        /**
         * Obtains the current system language. To listen for system language changes, enable listening for
         * [COMMON_EVENT_LOCALE_CHANGED](docroot://reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed)
         * . For details, see
         * [System Language and Region](docroot://internationalization/i18n-system-language-region.md#how-to-develop).
         *
         * @returns { string } Language ID.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        static getSystemLanguage(): string;
        /**
         * Obtains the current system country/region. To listen for system region changes, enable listening for
         * [COMMON_EVENT_LOCALE_CHANGED](docroot://reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed)
         * . For details, see
         * [System Language and Region](docroot://internationalization/i18n-system-language-region.md#how-to-develop).
         *
         * @returns { string } Country/region ID.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static getSystemRegion(): string;
        /**
         * Obtains the current system locale.
         *
         * @returns { string } Locale ID.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         * @useinstead i18n.System.getSystemLocaleInstance
         */
        static getSystemLocale(): string;
        /**
         * Obtains the current system locale. To listen for system locale changes, enable listening for
         * [COMMON_EVENT_LOCALE_CHANGED](docroot://reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_locale_changed)
         * . For details, see
         * [System Language and Region](docroot://internationalization/i18n-system-language-region.md#how-to-develop).
         *
         * @returns { Intl.Locale } the locale object currently used by the system.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        static getSystemLocaleInstance(): Intl.Locale;
        /**
         * Checks whether the 24-hour clock is used. To listen for system time format changes, enable listening for
         * [COMMON_EVENT_TIME_CHANGED](docroot://reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_time_changed)
         * . For details, see [User Preference](docroot://internationalization/i18n-user-preferences.md#how-to-develop).
         *
         * @returns { boolean } Whether the 24-hour clock is used. The value **true** indicates that the 24-hour clock is
         *     used, the the value **false** means the opposite.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        static is24HourClock(): boolean;
        /**
         * Obtains the list of preferred languages.
         *
         * @returns { Array<string> } List of preferred languages.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 9
         */
        static getPreferredLanguageList(): Array<string>;
        /**
         * Obtains the first language in the preferred language list.
         *
         * @returns { string } First language in the preferred language list.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 9
         */
        static getFirstPreferredLanguage(): string;
        /**
         * Sets the preferred language of the application. Resources are loaded in the preferred language when the
         * application is launched. If the preferred language is set to **default**, the application's language will be the
         * same as the system language, and the setting will take effect upon cold starting of the application.
         *
         * @param { string } language -
         *     [Valid language ID](docroot://internationalization/i18n-locale-culture.md#how-it-works) or **default**.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 20]
         * @atomicservice [since 12]
         * @since 11
         */
        static setAppPreferredLanguage(language: string): void;
        /**
         * Obtains the preferred language of an application.
         *
         * @returns { string } Preferred language of the application.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 20]
         * @atomicservice [since 12]
         * @since 9
         */
        static getAppPreferredLanguage(): string;
        /**
         * Checks whether use of local digits is enabled.
         *
         * @returns { boolean } Whether use of local digits is enabled. The value **true** indicates that use of local
         *     digits is enabled, and the value **false** indicates the opposite.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 9
         */
        static getUsingLocalDigit(): boolean;
        /**
         * Obtains the simplified representation of a language. For example, the simplified representation of **en-Latn-US**
         * is **en**, and that of **en-Latn-GB** is **en-GB**.
         *
         * @param { string } [language] -
         *     [Valid language ID](docroot://internationalization/i18n-locale-culture.md#how-it-works). The default value is
         *     the system language.
         * @returns { string } If **language** is not passed, the application checks for dialects supported by the system
         *     based on the system language and locale. If such a dialect is found, the simplified representation of the
         *     dialect is returned. Otherwise, the simplified representation of the system language is returned.
         *     If **language** is passed, the simplified representation of the specified language is returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 15
         */
        static getSimplifiedLanguage(language?: string): string;
        /**
         * Obtains the temperature unit of the system.
         *
         * @returns { TemperatureType } Temperature unit.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        static getTemperatureType(): TemperatureType;
        /**
         * Obtains the name of a temperature unit.
         *
         * @param { TemperatureType } type - Temperature unit.
         * @returns { string } Name of the temperature unit, which can be **celsius**, **fahrenheit**, and **kelvin**.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        static getTemperatureName(type: TemperatureType): string;
        /**
         * Obtains the first day of a week in the system settings.
         *
         * @returns { WeekDay } Start day of a week.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        static getFirstDayOfWeek(): WeekDay;
    }
    /**
     * Enumerates the first day of a week. The value ranges from Monday to Sunday.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice
     * @since 18
     */
    export enum WeekDay {
        /**
         * Monday.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        MON = 1,
        /**
         * Tuesday.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        TUE = 2,
        /**
         * Wednesday.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        WED = 3,
        /**
         * Thursday.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        THU = 4,
        /**
         * Friday.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        FRI = 5,
        /**
         * Saturday.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        SAT = 6,
        /**
         * Sunday.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        SUN = 7
    }
    /**
     * Enumerates temperature units.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice
     * @since 18
     */
    export enum TemperatureType {
        /**
         * Celsius.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        CELSIUS = 1,
        /**
         * Fahrenheit.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        FAHRENHEIT = 2,
        /**
         * Kelvin.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        KELVIN = 3
    }
    /**
     * Provides util functions.
     *
     * @syscap SystemCapability.Global.I18n
     * @since 8
     * @deprecated since 9
     * @useinstead i18n.I18NUtil
     */
    export interface Util {
        /**
         * Converts one measurement unit into another and formats the unit based on the specified locale and style.
         *
         * @param { UnitInfo } fromUnit - Measurement unit to be converted.
         * @param { UnitInfo } toUnit - Measurement unit to be converted to.
         * @param { number } value - Value of the measurement unit to be converted.
         * @param { string } locale - Locale ID used for formatting, for example, **zh-Hans-CN**.
         * @param { string } [style] - Style used for formatting. The value can be **long**, **short**, or **narrow**. The
         *     default value is **short**.
         * @returns { string } String obtained after formatting based on the measurement unit specified by **toUnit**.
         * @syscap SystemCapability.Global.I18n
         * @since 8
         * @deprecated since 9
         * @useinstead i18n.I18NUtil.unitConvert
         */
        unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: number, locale: string, style?: string): string;
    }
    /**
     * Internationalization utility class, which provides the capabilities of unit conversion, date sequence retrieval,
     * time segment name retrieval, region matching, and path localization.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    export class I18NUtil {
        /**
         * Converts one measurement unit into another and formats the unit based on the specified locale and style.
         *
         * @param { UnitInfo } fromUnit - Measurement unit to be converted.
         * @param { UnitInfo } toUnit - Measurement unit to be converted to.
         * @param { number } value - Value of the measurement unit to be converted.
         * @param { string } locale - [Locale ID](docroot://internationalization/i18n-locale-culture.md#how-it-works), which
         *     consists of the language, script, and country/region, for example, **zh-Hans-CN**.
         * @param { string } [style] - Style used for formatting. The value can be **long**, **short**, or **narrow**. The
         *     default value is **short**.
         *     For details about the meaning or display effect of different values, see
         *     [Number and Unit of Measurement Formatting](docroot://internationalization/i18n-numbers-weights-measures.md).
         * @returns { string } String converted to the measurement unit after formatting.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 9
         */
        static unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: number, locale: string, style?: string): string;
        /**
         * Obtains the sequence of the year, month, and day in the specified locale.
         *
         * @param { string } locale - [Locale ID](docroot://internationalization/i18n-locale-culture.md#how-it-works), which
         *     consists of the language, script, and country/region, for example, **zh-Hans-CN**.
         * @returns { string } Sequence of the year, month, and day in the locale. **y** indicates the year, **L** indicates
         *     the month, and **d** indicates the day.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static getDateOrder(locale: string): string;
        /**
         * Obtains the localized expression of the specified time in the specified locale.
         *
         * @param { number } hour - Specified time, for example, **16**.
         * @param { string } [locale] - [System locale](docroot://internationalization/i18n-locale-culture.md#how-it-works),
         *     which consists of the language, script, and country/region. for example, **zh-Hans-CN**.
         *     The default value is the current system locale.
         * @returns { string } Localized expression of the specified time in the specified locale.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        static getTimePeriodName(hour: number, locale?: string): string;
        /**
         * Obtains the locale that best matches a region from the specified locale list.
         *
         * @param { string } locale - [Locale ID](docroot://internationalization/i18n-locale-culture.md#how-it-works), for
         *     example, **zh-Hans-CN**.
         * @param { string[] } localeList - List of locale IDs.
         * @returns { string } ID of the locale that best matches a region. If no matching locale is found, an empty string
         *     is returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        static getBestMatchLocale(locale: string, localeList: string[]): string;
        /**
         * Converts a language code from two letters to three letters.
         *
         * For example, the two-letter language code of Chinese is **zh**, and the corresponding three-letter language code
         * is **zho**. For details, see [ISO 639](https://www.iso.org/iso-639-language-code).
         *
         * @param { string } locale - Two-letter code of the language to be converted, for example, **zh**.
         * @returns { string } Language code after conversion.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 12
         */
        static getThreeLetterLanguage(locale: string): string;
        /**
         * Converts a region code from two letters to three letters.
         *
         * For example, the two-letter region code of China is **CN**, and the corresponding three-letter region code is
         * **CHN**. For details, see [ISO 3166](https://www.iso.org/iso-3166-country-codes.html).
         *
         * @param { string } locale - Two-letter country/region code to be converted, for example, **CN**.
         * @returns { string } Region code after conversion .
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 12
         */
        static getThreeLetterRegion(locale: string): string;
        /**
         * Localizes a file path for the specified locale.
         *
         * For example, "/data/out/tmp" is changed to "tmp/out/data/" after localization.
         *
         * @param { string } path - Path to mirror, for example, "/data/out/tmp".
         * @param { string } [delimiter] - Path delimiter. The default value is "/".
         * @param { Intl.Locale } [locale] - **Locale** object. The default value is the current system locale.
         * @returns { string } File path after localization. If the specified locale object corresponds to an RTL language,
         *     the processed file path contains a direction control character to ensure that the file path is displayed in
         *     mirror mode.
         * @throws { BusinessError } 8900001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 20
         */
        static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: Intl.Locale): string;
        /**
         * Localizes a file path for the specified locale.
         *
         * For example, "/data/out/tmp" is changed to "tmp/out/data/" after localization.
         *
         * @param { string } path - Path to mirror, for example, "/data/out/tmp".
         * @param { string } [delimiter] - Path delimiter. The default value is "/".
         * @param { intl.Locale } [locale] - **Locale** object. The default value is the current system locale.
         * @returns { string } File path after localization. If the specified locale object corresponds to an RTL language,
         *     the processed file path contains a direction control character to ensure that the file path is displayed in
         *     mirror mode.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 18
         * @deprecated since 20
         * @useinstead i18n.I18NUtil.getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: Intl.Locale)
         */
        static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string;
        /**
         * Adjusts a locale ID to a format that complies with the [BCP47](https://www.rfc-editor.org/info/bcp47) standard.
         *
         * @param { string } locale - Locale string to be converted, which consists of the language, script,
         *     and country/region.
         * @returns { string } If the input locale ID is valid, a locale ID that complies with the [BCP47](https://www.rfc-editor.org/info/bcp47) standard will be returned.
         *                     If the input locale ID is invalid, an empty string is returned.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        static convertCanonicalLocaleIdentifier(locale: string): string;
        /**
         * Sets the text direction for certain text within a paragraph, including RTL (right-to-left) and
         * LTR (left-to-right). NOTE: The setting does not take effect within strong characters (characters
         *  with an intrinsic, unambiguous writing direction).
         *
         * @param { string } text - Text for which the direction needs to be set.
         * @param { 'RTL' | 'LTR' } direction - The value can be "RTL" or "LTR".
         *     "RTL" indicates setting the input text direction from right to left.
         *     "LTR" indicates setting the input text direction from left to right.
         * @returns { string } Processed Text.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        static setUnicodeWrappedBidiDirection(text: string, direction: 'RTL' | 'LTR'): string;
    }
    /**
     * Defines the measurement unit information.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice [since 12]
     * @since 8
     */
    export interface UnitInfo {
        /**
         * Name of the measurement unit, for example, **meter**, **inch**, or **cup**.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        unit: string;
        /**
         * Measurement system. The value can be **SI**, **US**, or **UK**.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        measureSystem: string;
    }
    /**
     * Options for **PhoneNumberFormat** object initialization.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 8
     */
    export interface PhoneNumberFormatOptions {
        /**
         * Type of the phone number. The value can be **E164**, **INTERNATIONAL**, **NATIONAL**, **RFC3966**, or **TYPING**.
         *
         * - In API version 8, **type** is mandatory.
         * - In API version 9 or later, **type** is optional.
         * - In API version 12 or later, TYPING is supported, which indicates that the dialed number is formatted in real
         * time.
         * - In API version 23 or later, TYPING supports real-time obtaining of the home location of a dialed number.
         *
         * @type { string } [since 8 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 8
         */
        type?: string;
    }
    /**
     * Provides phone number management capabilities, such as phone number validity verification, formatting, and home
     * location retrieval.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 8
     */
    export class PhoneNumberFormat {
        /**
         * Creates a **PhoneNumberFormat** object.
         *
         * @param { string } country - Country/region to which the phone number to be formatted belongs.
         * @param { PhoneNumberFormatOptions } [options] - Options for **PhoneNumberFormat** object initialization. The
         *     default value is **NATIONAL**.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 8
         */
        constructor(country: string, options?: PhoneNumberFormatOptions);
        /**
         * Checks whether the phone number is valid for the country/region in the **PhoneNumberFormat** object.
         *
         * @param { string } number - Indicates the input phone number. [since 8 - 11]
         * @param { string } phoneNumber - Phone number to be checked. [since 12]
         * @returns { boolean } Whether the phone number is valid. The value **true** indicates that the phone number is
         *     valid, and the value **false** indicates the opposite.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 8
         */
        isValidNumber(phoneNumber: string): boolean;
        /**
         * Formats a phone number.
         *
         * > **Description**
         * > > Formatting dialed phone numbers is supported since API version 12.
         *
         * @param { string } number - Indicates the input phone number to be formatted. [since 8 - 11]
         * @param { string } phoneNumber - Phone number to be formatted. [since 12]
         * @returns { string } Formatted phone number.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 8
         */
        format(phoneNumber: string): string;
        /**
         * Obtains the home location of a phone number.
         *
         * > **Description**
         * > > This API can be used to obtain the home location of a dialed number in real time since API version 23.
         *
         * @param { string } number - input phone number. [since 9 - 11]
         * @param { string } phoneNumber - Phone number. To obtain the home location of a number in other countries/regions,
         *     you need to prefix the number with **00** and the country code. [since 12]
         * @param { string } locale - [System locale](docroot://internationalization/i18n-locale-culture.md#how-it-works),
         *     which consists of the language, script, and country/region.
         * @returns { string } Home location of the phone number. If the number is invalid, an empty string is returned.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice [since 12]
         * @since 9
         */
        getLocationName(phoneNumber: string, locale: string): string;
    }
    /**
     * Obtains the **Calendar** object for the specified locale and calendar type.
     *
     * @param { string } locale - [Locale ID](docroot://internationalization/i18n-locale-culture.md#how-it-works), which
     *     consists of the language, script, and country/region, for example, **zh-Hans-CN**.
     * @param { string } [type] - Calendar. The value can be buddhist, chinese, coptic, ethiopic, hebrew, gregory, indian,
     *      islamic_civil, islamic_tbla, islamic_umalqura, japanese,  or persian.
     *     The default value is the default calendar of the locale.
     *     For details about the meanings and application scenarios of different values, see
     *     [Calendar Setting](docroot://internationalization/i18n-calendar.md).
     * @returns { Calendar } **Calendar** object.
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    export function getCalendar(locale: string, type?: string): Calendar;
    /**
     * Provides calendar management capabilities, such as calendar name retrieval and date calculation.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 7
     */
    export class Calendar {
        /**
         * Sets the date and time for a **Calendar** object based on the input **Date** object.
         *
         * @param { Date } date - Date and time. Note: The month starts from **0**. For example, **0** indicates January.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        setTime(date: Date): void;
        /**
         * Sets the date and time for a **Calendar** object based on the input timestamp.
         *
         * @param { number } time - Unix timestamp, which indicates the number of milliseconds
         *     that have elapsed since the Unix epoch.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        setTime(time: number): void;
        /**
         * Sets the year, month, day, hour, minute, and second for this **Calendar** object.
         *
         * @param { number } year - Year to set.
         * @param { number } month - Month to set. Note: The month starts from **0**. For example, **0** indicates January.
         * @param { number } date - Day to set.
         * @param { number } hour - Hour to set. The default value is the current system time.
         * @param { number } minute - Minute to set. The default value is the current system time.
         * @param { number } second - Second to set. The default value is the current system time.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        set(year: number, month: number, date: number, hour?: number, minute?: number, second?: number): void;
        /**
         * Sets the time zone of this **Calendar** object.
         *
         * @param { string } timezone - Valid time zone ID, for example, Asia/Shanghai.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        setTimeZone(timezone: string): void;
        /**
         * Obtains the time zone ID of this **Calendar** object.
         *
         * @returns { string } Time zone ID.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        getTimeZone(): string;
        /**
         * Obtains the first day of a week for this **Calendar** object.
         *
         * @returns { number } First day of a week. The value **1** indicates Sunday, and the value **7** indicates Saturday.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        getFirstDayOfWeek(): number;
        /**
         * Sets the first day of a week for this **Calendar** object.
         *
         * @param { number } value - Start day of a week. The value **1** indicates Sunday, and the value **7** indicates
         *     Saturday.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        setFirstDayOfWeek(value: number): void;
        /**
         * Obtains the minimum number of days in the first week for this **Calendar** object.
         *
         * @returns { number } Minimum number of days in the first week of a year.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        getMinimalDaysInFirstWeek(): number;
        /**
         * Sets the minimum number of days in the first week for this **Calendar** object.
         *
         * @param { number } value - Minimum number of days in the first week of a year.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        setMinimalDaysInFirstWeek(value: number): void;
        /**
         * Obtains the values of the calendar attributes in this **Calendar** object.
         *
         * @param { string } field - Calendar attributes. The following table lists the supported attribute values.
         *     The value can be
         *         "era": Era, for example, AD or BC.
         *         "year": Year.
         *         "month": Month. Note: The month starts from **0**. For example, **0** indicates January.
         *         "date": Date.
         *         "hour": Wall-clock hour.
         *         "hour_of_day": Hour of day.
         *         "minute": Minute.
         *         "second": Second.
         *         "millisecond": Millisecond.
         *         "week_of_year": Week of year. Note that the algorithm for calculating the first week of a year varies
         *             according to regions. For example, the first seven days in a year are the first week.
         *         "year_woy": Year used with the week of year field.
         *         "week_of_month": Week of month.
         *         "day_of_week_in_month": Day of week in month.
         *         "day_of_year": Day of year.
         *         "day_of_week": Day of week.
         *         "milliseconds_in_day": Milliseconds in day.
         *         "zone_offset": Fixed time zone offset in milliseconds (excluding DST).
         *         "dst_offset": DST offset in milliseconds.
         *         "dow_local": Localized day of week.
         *         "extended_year": Extended year, which can be a negative number.
         *         "julian_day": Julian day.
         *         "is_leap_month": Whether a month is a leap month.
         * @returns { number } Value of the calendar attribute. For example, if the year of the internal date of the current
         *     **Calendar** object is 1990, **get('year')** returns **1990**.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        get(field: string): number;
        /**
         * Obtains calendar display name in the specified language.
         *
         * @param { string } locale - [System locale](docroot://internationalization/i18n-locale-culture.md#how-it-works),
         *     which consists of the language, script, and country/region.
         * @returns { string } Calendar display name in the specified language. For example, **buddhist** is displayed as
         *     **Buddhist Calendar** if the locale is **en-US**.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        getDisplayName(locale: string): string;
        /**
         * Checks whether a given date is a weekend in this **Calendar** object.
         *
         * @param { Date } [date] - Date and time. Note: The month starts from **0**. For example, **0** indicates January.
         *     The default value is current date of the **Calendar** object.
         * @returns { boolean } The value **true** indicates that the specified date is a weekend, and the value **false**
         *     indicates the opposite.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isWeekend(date?: Date): boolean;
        /**
         * Performs addition or subtraction on the calendar attributes of this **Calendar** object.
         *
         * @param { string } field - Calendar attribute. The value can be any of the following: **year**, **month**,
         *     **week_of_year**, **week_of_month**, **date**, **day_of_year**, **day_of_week**, **day_of_week_in_month**,
         *     **hour**, **hour_of_day**, **minute**, **second**, **millisecond**.
         *   For details about the values, see [get]{@link i18n.Calendar#get}.
         * @param { number } amount - Addition or subtraction amount.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        add(field: string, amount: number): void;
        /**
         * Obtains the timestamp of this **Calendar** object.
         *
         * @returns { number } Unix timestamp, which indicates the number of milliseconds that have elapsed since the Unix
         *     epoch.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getTimeInMillis(): number;
        /**
         * Compares the current date of this **Calendar** object with the specified date for the difference in the number of
         * days.
         *
         * @param { Date } date - Date and time. Note: The month starts from **0**. For example, **0** indicates January.
         * @returns { number } Difference in the number of days. A positive number indicates that the calendar date is earlier,
         *     and a negative number indicates the opposite.
         *     The value is accurate to milliseconds. If the value is less than one day, it is considered as one day.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        compareDays(date: Date): number;
    }
    /**
     * Checks whether a language is an RTL language. For an RTL language,
     * [UI mirroring](docroot://internationalization/i18n-ui-design.md#ui-mirroring) is required.
     *
     * @param { string } locale - [System locale](docroot://internationalization/i18n-locale-culture.md#how-it-works),
     *     which consists of the language, script, and country/region.
     * @returns { boolean } Whether a language is an RTL language. The value **true** indicates that the language is an
     *     RTL language, and the value **false** indicates the opposite.
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 7
     */
    export function isRTL(locale: string): boolean;
    /**
     * Obtains a **BreakIterator** object. The **BreakIterator** object maintains an internal break iterator that can be
     * used to access various line break points.
     *
     * @param { string } locale - [System locale](docroot://internationalization/i18n-locale-culture.md#how-it-works),
     *     which consists of the language, script, and country/region.
     *   The generated
     *     [BreakIterator]{@link i18n.BreakIterator} object calculates the positions of line breaks based on the rules of
     *     the specified locale.
     * @returns { BreakIterator } **BreakIterator** object.
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice [since 12]
     * @since 8
     */
    export function getLineInstance(locale: string): BreakIterator;
    /**
     * Provides text line breaking capabilities, such as obtaining, moving, and identifying break points.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice [since 12]
     * @since 8
     */
    export class BreakIterator {
        /**
         * Obtains the position of the break iterator in the text.
         *
         * @returns { number } Position of the break iterator in the text.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        current(): number;
        /**
         * Moves the break iterator to the first line break point, which is always at the beginning of the processed text.
         *
         * @returns { number } Offset of the first line break point in the processed text.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        first(): number;
        /**
         * Moves the break iterator to the last line break point, which is always the next position after the end of the
         * processed text.
         *
         * @returns { number } Offset of the last line break point in the processed text.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        last(): number;
        /**
         * Moves the break iterator backward by the specified number of line break points.
         *
         * @param { number } [index] - Number of line break points for moving the break iterator. The value is an integer.
         *  A positive number means to move the break iterator backward, and a negative number means to move the break
         *     iterator forward.
         *  The default value is **1**.
         * @returns { number } Position of the break iterator in the text after movement.
         *     The value **-1** is returned if the position of the break iterator is outside of the processed text after
         *     movement.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        next(index?: number): number;
        /**
         * Moves the break iterator foreward by one line break point.
         *
         * @returns { number } Position of the break iterator in the text after movement.
         *     The value **-1** is returned if the position of the break iterator is outside of the processed text after
         *     movement.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        previous(): number;
        /**
         * Sets the text to be processed by the **BreakIterator** object.
         *
         * @param { string } text - Input text.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        setLineBreakText(text: string): void;
        /**
         * Moves the line break iterator to the line break point after the specified position.
         *
         * @param { number } offset - Offset of the line break point.
         * @returns { number } Position of the break iterator in the text after movement. The value **-1** is returned if the
         *     position of the break iterator is outside of the processed text after movement.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        following(offset: number): number;
        /**
         * Obtains the text processed by the **BreakIterator** object.
         *
         * @returns { string } Text being processed by the **BreakIterator** object.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        getLineBreakText(): string;
        /**
         * Checks whether the specified position is a line break point.
         *
         * @param { number } offset - Specified position in the text.
         * @returns { boolean } Whether the specified position is a line break point. The value **true** indicates that the
         *     specified position is a line break point, and the value **false** indicates the opposite.
         *     If **true** is returned, the break iterator is moved to the position specified by **offset**. Otherwise, the
         *     break iterator is moved to the text line break point after the position specified by **offset**, which is
         *     equivalent to calling **following**.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        isBoundary(offset: number): boolean;
    }
    /**
     * Creates an **IndexUtil** object.
     *
     * @param { string } [locale] - [System locale](docroot://internationalization/i18n-locale-culture.md#how-it-works),
     *     which consists of the language, script, and country/region.
     *   The default value is the current system locale.
     * @returns { IndexUtil } **IndexUtil** object created based on the specified locale ID.
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice [since 12]
     * @since 8
     */
    export function getInstance(locale?: string): IndexUtil;
    /**
     * Provides index management capabilities, such as obtaining the locale index list and text index values.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice [since 12]
     * @since 8
     */
    export class IndexUtil {
        /**
         * Obtains the index list of the current locale.
         *
         * @returns { Array<string> } Index list of the current locale. The first and last elements are **...**.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        getIndexList(): Array<string>;
        /**
         * Adds the index list of a new locale to the index list of the current locale to form a composite list.
         *
         * @param { string } locale - [System locale](docroot://internationalization/i18n-locale-culture.md#how-it-works),
         *     which consists of the language, script, and country/region.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        addLocale(locale: string): void;
        /**
         * Obtains the index of the **text** object.
         *
         * @param { string } text - Input text.
         * @returns { string } Index of the **text** object. If no proper index is found, an empty string is returned.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 8
         */
        getIndex(text: string): string;
    }
    /**
     * Provides the API for accessing unicode character properties. For example, determine whether a character is a number.
     *
     * @syscap SystemCapability.Global.I18n
     * @since 8
     * @deprecated since 9
     * @useinstead i18n.Unicode
     */
    export class Character {
        /**
         * Checks whether the input character is a digit.
         *
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked.
         * @returns { boolean } **true** if the input character is a digit, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @since 8
         * @deprecated since 9
         * @useinstead i18n.Unicode.isDigit
         */
        isDigit(ch: string): boolean;
        /**
         * Checks whether the input character is a space.
         *
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked.
         * @returns { boolean } **true** if the input character is a space, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @since 8
         * @deprecated since 9
         * @useinstead i18n.Unicode.isSpaceChar
         */
        isSpaceChar(ch: string): boolean;
        /**
         * Checks whether the input character is a whitespace.
         *
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked.
         * @returns { boolean } **true** if the input character is a white space, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @since 8
         * @deprecated since 9
         * @useinstead i18n.Unicode.isWhitespace
         */
        isWhitespace(ch: string): boolean;
        /**
         * Checks whether the input character is of the right to left (RTL) language.
         *
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked.
         * @returns { boolean } **true** if the input character is of the RTL language, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @since 8
         * @deprecated since 9
         * @useinstead i18n.Unicode.isRTL
         */
        isRTL(ch: string): boolean;
        /**
         * Checks whether the input character is an ideographic character.
         *
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked.
         * @returns { boolean } **true** if the input character an ideographic character, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @since 8
         * @deprecated since 9
         * @useinstead i18n.Unicode.isIdeograph
         */
        isIdeograph(ch: string): boolean;
        /**
         * Checks whether the input character is a letter.
         *
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked.
         * @returns { boolean } **true** if the input character a letter, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @since 8
         * @deprecated since 9
         * @useinstead i18n.Unicode.isLetter
         */
        isLetter(ch: string): boolean;
        /**
         * Checks whether the input character is a lowercase letter.
         *
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked.
         * @returns { boolean } **true** if the input character a lowercase letter, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @since 8
         * @deprecated since 9
         * @useinstead i18n.Unicode.isLowerCase
         */
        isLowerCase(ch: string): boolean;
        /**
         * Checks whether the input character is an uppercase letter.
         *
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked.
         * @returns { boolean } **true** if the input character an uppercase letter, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @since 8
         * @deprecated since 9
         * @useinstead i18n.Unicode.isUpperCase
         */
        isUpperCase(ch: string): boolean;
        /**
         * Obtains the type of the input character.
         *
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked.
         * @returns { string } Type of the input character.
         * @syscap SystemCapability.Global.I18n
         * @since 8
         * @deprecated since 9
         * @useinstead i18n.Unicode.getType
         */
        getType(ch: string): string;
    }
    /**
     * Provides character attribute management capabilities, such as checking whether a character is a space, digit, or
     * letter.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    export class Unicode {
        /**
         * Checks whether the input character is a digit.
         *
         * @param { string } char - the character to be tested [since 9 - 11]
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked. [since 12]
         * @returns { boolean } **true** if the input character is a digit, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static isDigit(ch: string): boolean;
        /**
         * Checks whether the input character is a space.
         *
         * @param { string } char - the character to be tested [since 9 - 11]
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked. [since 12]
         * @returns { boolean } **true** if the input character is a space, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static isSpaceChar(ch: string): boolean;
        /**
         * Checks whether the input character is a whitespace.
         *
         * @param { string } char - the character to be tested [since 9 - 11]
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked. [since 12]
         * @returns { boolean } **true** if the input character is a white space, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static isWhitespace(ch: string): boolean;
        /**
         * Checks whether the input character is of the right to left (RTL) language.
         *
         * @param { string } char - the character to be tested [since 9 - 11]
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked. [since 12]
         * @returns { boolean } **true** if the input character is of the RTL language, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static isRTL(ch: string): boolean;
        /**
         * Checks whether the input character is an ideographic character.
         *
         * @param { string } char - the character to be tested [since 9 - 11]
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked. [since 12]
         * @returns { boolean } **true** if the input character an ideographic character, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static isIdeograph(ch: string): boolean;
        /**
         * Checks whether the input character is a letter.
         *
         * @param { string } char - the character to be tested [since 9 - 11]
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked. [since 12]
         * @returns { boolean } **true** if the input character a letter, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static isLetter(ch: string): boolean;
        /**
         * Checks whether the input character is a lowercase letter.
         *
         * @param { string } char - the character to be tested [since 9 - 11]
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked. [since 12]
         * @returns { boolean } **true** if the input character a lowercase letter, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static isLowerCase(ch: string): boolean;
        /**
         * Checks whether the input character is an uppercase letter.
         *
         * @param { string } char - the character to be tested [since 9 - 11]
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked. [since 12]
         * @returns { boolean } **true** if the input character an uppercase letter, and **false** otherwise.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static isUpperCase(ch: string): boolean;
        /**
         * Obtains the type of the input character.
         *
         * @param { string } char - the character to be tested [since 9 - 11]
         * @param { string } ch - Input character. If the input is a string, only the type of the first character is
         *     checked. [since 12]
         * @returns { string } Type of the input character.U_UNASSIGNED： Non-category for unassigned and non-character code
         *     points. The value can be
         *
         *     U_GENERAL_OTHER_TYPES： Same as **U_UNASSIGNED**.
         *
         *     U_UPPERCASE_LETTER： Uppercase letter.
         *
         *     U_LOWERCASE_LETTER： Lowercase letter.
         *
         *     U_TITLECASE_LETTER： Title case letter.
         *
         *     U_MODIFIER_LETTER： Modifier letter.
         *
         *     U_OTHER_LETTER： Letters other than the uppercase letter, lowercase letter, title case letter, and modifier
         *     letter.
         *
         *     U_NON_SPACING_MARK： Non-spacing mark, such as the accent symbol **'** and the variable symbol **#**.
         *
         *     U_ENCLOSING_MARK： Enclosing mark, for example, a circle or a box.
         *
         *     U_COMBINING_SPACING_MARK： Spacing mark, for example, the vowel symbol **[]**.
         *
         *     U_DECIMAL_DIGIT_NUMBER： Decimal number.
         *
         *     U_LETTER_NUMBER： Letter and number (including Roman numeral).
         *
         *     U_OTHER_NUMBER： Other numbers, which are used as encryption symbols, marker symbols, or non-Arabic numerals,
         *     such as **@**, **#**, **(1)**, and **①**.
         *
         *     U_SPACE_SEPARATOR： Space separator, for example, a space character, uninterrupted space character, or space
         *     character with a fixed width.
         *
         *     U_LINE_SEPARATOR： Line separator.
         *
         *     U_PARAGRAPH_SEPARATOR： Paragraph separator.
         *
         *     U_CONTROL_CHAR： Control character.
         *
         *     U_FORMAT_CHAR： Format character.
         *
         *     U_PRIVATE_USE_CHAR： Privately used character, for example, a company logo.
         *
         *     U_SURROGATE： Surrogate, which is used to represent supplementary characters in UTF-16.
         *
         *     U_DASH_PUNCTUATION： Dash punctuation.
         *
         *     U_START_PUNCTUATION： Start punctuation, for example, the left parenthesis.
         *
         *     U_END_PUNCTUATION： End punctuation, for example, the right parenthesis.
         *
         *     U_INITIAL_PUNCTUATION ： Initial punctuation, for example, the left double quotation mark or left single
         *     quotation mark.
         *
         *     U_FINAL_PUNCTUATION： Final punctuation, for example, the right double quotation mark or right single
         *     quotation mark.
         *
         *     U_CONNECTOR_PUNCTUATION： Connector punctuation.
         *
         *     U_OTHER_PUNCTUATION： Other punctuations.
         *
         *     U_MATH_SYMBOL： Mathematical symbol.
         *
         *     U_CURRENCY_SYMBOL： Currency symbol.
         *
         *     U_MODIFIER_SYMBOL： Modifier symbol.
         *
         *     U_OTHER_SYMBOL： Other symbols.
         *
         *     For details, see Unicode standard.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static getType(ch: string): string;
        /**
         * Detects the encoding information of the input byte stream.
         *
         * @param { Uint8Array } bytes - Input byte stream. To detect the encoding of a text string,
         *     convert the text to a byte stream first while preserving its original format.
         *     <br>Byte stream to be identified and encoded
         * @returns { EncodingInfo } An object containing the detected encoding name and detection confidence level.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        static detectEncoding(bytes: Uint8Array): EncodingInfo;
    }
    /**
     * Defines the detect encoding result information.
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export interface EncodingInfo {
        /**
         * Name of the detect encoding result, the value can be "UTF-8", "UTF-16BE", "UTF-16LE", "UTF-32BE",
         * "UTF-32LE", "Shift_JIS", "ISO-2022-JP", "ISO-2022-CN", "ISO-2022-KR", "GB18030", "Big5", "EUC-JP",
         * "EUC-KR", "ISO-8859-1", "ISO-8859-2", "ISO-8859-5", "ISO-8859-6", "ISO-8859-7", "ISO-8859-8",
         * "ISO-8859-9", "windows-1250", "windows-1251", "windows-1252", "windows-1253", "windows-1254",
         * "windows-1255", "windows-1256", "KOI8-R", "IBM420", "IBM424".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        encodingName: string;
        /**
         * An integer between 0 to 100, determine the accuracy of the result.
         * Higher value indicates a more reliable detection result.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        confidence: number;
    }
    /**
     * Checks whether the 24-hour clock is used.
     *
     * @returns { boolean } **true** if the 24-hour clock is used, and **false** otherwise.
     * @syscap SystemCapability.Global.I18n
     * @since 7
     * @deprecated since 9
     * @useinstead i18n.System.is24HourClock
     */
    export function is24HourClock(): boolean;
    /**
     * Sets the 24-hour clock.
     *
     * @permission ohos.permission.UPDATE_CONFIGURATION
     * @param { boolean } option - Whether to enable the 24-hour clock. The value **true** means to enable the 24-hour
     *     clock, and the value **false** means the opposite.
     * @returns { boolean } **true** if the setting is successful, and **false** otherwise.
     * @syscap SystemCapability.Global.I18n
     * @since 7
     * @deprecated since 9
     */
    export function set24HourClock(option: boolean): boolean;
    /**
     * Adds a preferred language to the specified position on the preferred language list.
     *
     * @permission ohos.permission.UPDATE_CONFIGURATION
     * @param { string } language - Preferred language to add.
     * @param { number } [index] - Position to which the preferred language is added. The default value is the length of the
     *     preferred language list.
     * @returns { boolean } **true** if the operation is successful, and **false** otherwise.
     * @syscap SystemCapability.Global.I18n
     * @since 8
     * @deprecated since 9
     */
    export function addPreferredLanguage(language: string, index?: number): boolean;
    /**
     * Removes a preferred language from the specified position on the preferred language list.
     *
     * @permission ohos.permission.UPDATE_CONFIGURATION
     * @param { number } index - Position of the preferred language to delete.
     * @returns { boolean } Whether the operation is successful. The value **true** indicates that the operation is
     *     successful, and the value **false** indicates the opposite.
     * @syscap SystemCapability.Global.I18n
     * @since 8
     * @deprecated since 9
     */
    export function removePreferredLanguage(index: number): boolean;
    /**
     * Obtains the list of preferred languages.
     *
     * @returns { Array<string> } List of preferred languages.
     * @syscap SystemCapability.Global.I18n
     * @since 8
     * @deprecated since 9
     * @useinstead i18n.System.getPreferredLanguageList
     */
    export function getPreferredLanguageList(): Array<string>;
    /**
     * Obtains the first language in the preferred language list.
     *
     * @returns { string } First language in the preferred language list.
     * @syscap SystemCapability.Global.I18n
     * @since 8
     * @deprecated since 9
     * @useinstead i18n.System.getFirstPreferredLanguage
     */
    export function getFirstPreferredLanguage(): string;
    /**
     * Obtains the **TimeZone** object corresponding to the specified time zone ID.
     *
     * @param { string } [zoneID] - Time zone ID. The default value is the system time zone.
     * @returns { TimeZone } **TimeZone** object corresponding to the time zone ID.
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 7
     */
    export function getTimeZone(zoneID?: string): TimeZone;
    /**
     * Provides time zone management capabilities, such as time zone name translation, offset retrieval, and transition
     * rule retrieval.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 7
     */
    export class TimeZone {
        /**
         * Obtains the ID of the specified **TimeZone** object.
         *
         * @returns { string } Time zone ID corresponding to the **TimeZone** object.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 7
         */
        getID(): string;
        /**
         * Obtains time zone display name in the specified language.
         *
         * @param { string } [locale] - [System locale](docroot://internationalization/i18n-locale-culture.md#how-it-works),
         *     which consists of the language, script, and country/region. The default value is the current system locale.
         * @param { boolean } [isDST] - Whether DST information is displayed. The value **true** indicates that DST
         *     information is displayed, and the value **false** indicates the opposite. The default value is **false**.
         * @returns { string } Time zone display name in the specified language.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 7
         */
        getDisplayName(locale?: string, isDST?: boolean): string;
        /**
         * Obtains the raw offset of the specified time zone.
         *
         * @returns { number } Raw offset of the time zone, in milliseconds.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 7
         */
        getRawOffset(): number;
        /**
         * Obtains the offset of the specified time zone at the specified time.
         *
         * @param { number } [date] - Specified time, in milliseconds. The default value is the system time.
         * @returns { number } Time zone offset, in milliseconds. When the DST is used, the time zone offset is the raw time
         *     zone offset plus the DST offset.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 7
         */
        getOffset(date?: number): number;
        /**
         * Obtains the list of time zone IDs supported by the system.
         *
         * @returns { Array<string> } List of time zone IDs supported by the system.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static getAvailableIDs(): Array<string>;
        /**
         * Obtains the list of time zone city IDs supported by the system.
         *
         * @returns { Array<string> } List of time zone city IDs supported by the system.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice [since 12]
         * @since 9
         */
        static getAvailableZoneCityIDs(): Array<string>;
        /**
         * Obtains time zone city display name in the specified language.
         *
         * @param { string } cityID - Time zone city ID.
         * @param { string } locale - [System locale](docroot://internationalization/i18n-locale-culture.md#how-it-works),
         *     which consists of the language, script, and country/region.
         * @returns { string } Time zone city display name in the specified language.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice [since 12]
         * @since 9
         */
        static getCityDisplayName(cityID: string, locale: string): string;
        /**
         * Creates a **TimeZone** object corresponding to the specified time zone city.
         *
         * @param { string } cityID - Time zone city ID. The value must be a time zone city ID supported by the system.
         * @returns { TimeZone } **TimeZone** object corresponding to the specified time zone city ID.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice [since 12]
         * @since 9
         */
        static getTimezoneFromCity(cityID: string): TimeZone;
        /**
         * Creates an array of **TimeZone** objects corresponding to the specified location.
         *
         * @param { number } longitude - Longitude. The value range is
         *     [-180, 179.9). A positive value is used for east longitude and a negative value is used for west longitude.
         * @param { number } latitude - Latitude. The value range is
         *     [-90, 89.9). A positive value is used for north latitude and a negative value is used for south latitude.
         * @returns { Array<TimeZone> } **TimeZone** objects corresponding to the specified location.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice [since 12]
         * @since 10
         */
        static getTimezonesByLocation(longitude: number, latitude: number): Array<TimeZone>;
        /**
         * Obtains the time zone transition rules. For details about the time zone transition logic, see
         * [DST Transition](docroot://internationalization/i18n-dst-transition.md).
         *
         * @returns { ZoneRules } Time zone transition rule, including the transition time and the offset before and after
         *     the transition.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 20
         */
        public getZoneRules(): ZoneRules;
        /**
         * Check if the given date use daylight saving time. The calculation will be based on the matched time zone rules.
         *
         * @param { Date } date - Date and time. Note: The month starts from **0**, indicating January.
         * @returns { boolean } true if the date use daylight saving time, and false otherwise.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public isDaylightSavingTime(date: Date): boolean;
        /**
         * Sets the default time zone for the current app, the value will be used on the application's runtime lifecycle.
         * When the date time formatting function is used, the default time zone ID of the app is used preferentially.
         *
         * @param { string } zoneID - Time zone ID that set default for app. for example, "Asia/Shanghai".
         *     <br> Time zone ID supported by the system
         * @throws { BusinessError } 8900001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        static setAppDefaultTimeZoneById(zoneID: string): void;
        /**
         * Obtains the default time zone object used by an application.
         * If the default time zone has been set by calling setAppDefaultTimeZoneById, the default time zone object
         * is returned. Otherwise, the system time zone object is returned.
         *
         * @returns { TimeZone } TimeZone object, first set by application, then system time zone, last GMT time zone.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        static getAppDefaultTimeZone(): TimeZone;
    }
    /**
     * Queries the time zone transition rule.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice
     * @since 20
     */
    export class ZoneRules {
        /**
         * Obtains the **nextTransition** object for the specified time.
         *
         * @param { number } [ date ] - Timestamp of next transition. It is measured as the number of milliseconds from 00:0
         *     0:00 on January 1, 1970 (UTC) to the specified time, which defaults to the current system time.
         * @returns { ZoneOffsetTransition } **ZoneOffsetTransition** object for next transition.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 20
         */
        public nextTransition(date?: number): ZoneOffsetTransition;
    }
    /**
     * Provides the API for obtaining a timezone transition information.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice
     * @since 20
     */
    export class ZoneOffsetTransition {
        /**
         * Obtains the timestamp of the time zone transition point.
         *
         * @returns { number } Timestamp of the time zone transition point. It is measured as the number of milliseconds
         *     from 00:00:00 on January 1, 1970 (UTC) to the time zone transition point, for example, 1762074000000. If the
         *     [raw offset]{@link i18n.TimeZone#getRawOffset} remains unchanged and DST is not used, **0** is returned.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 20
         */
        public getMilliseconds(): number;
        /**
         * Obtains the offset after the time zone transition.
         *
         * @returns { number } Post-transition offset, that is, the time difference between the post-transition time and UTC,
         *     measured in ms. For example, **-28800000** indicates that the time after the transition is 28800000 ms (8
         *     hours) later than UTC.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 20
         */
        public getOffsetAfter(): number;
        /**
         * Obtains the offset before the time zone transition.
         *
         * @returns { number } Pre-transition offset, that is, the time difference between the pre-transition time and UTC,
         *     measured in ms. For example, **-25200000** indicates that the pre-transition time is 25200000 ms (7 hours)
         *     slower than UTC.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice
         * @since 20
         */
        public getOffsetBefore(): number;
    }
    /**
     * Provides text transliteration capabilities, such as obtaining the supported language IDs and transliterating text.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice [since 12]
     * @since 9
     */
    export class Transliterator {
        /**
         * Obtains a list of IDs supported by the **Transliterator** object.
         *
         * @returns { string[] } List of IDs supported by the **Transliterator** object.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 9
         */
        static getAvailableIDs(): string[];
        /**
         * Creates a **Transliterator** object based on the specified ID.
         *
         * @param { string } id - ID supported by the **Transliterator** object.
         * @returns { Transliterator } **Transliterator** object.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 9
         */
        static getInstance(id: string): Transliterator;
        /**
         * Converts the input text from the source format to the target format.
         *
         * @param { string } text - Input text.
         * @returns { string } Text after conversion.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 9
         */
        transform(text: string): string;
    }
    /**
     * Enumerates text normalization modes.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice [since 12]
     * @since 10
     */
    export enum NormalizerMode {
        /**
         * Normalization form C, characters are decomposed and then re-composed by canonical equivalence
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 10
         */
        NFC = 1,
        /**
         * Normalization form D, characters are decomposed by canonical equivalence
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 10
         */
        NFD = 2,
        /**
         * Normalization form KC, characters are decomposed by compatibility, then re-composed by canonical equivalence
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 10
         */
        NFKC = 3,
        /**
         * Normalization form KD, characters are decomposed by compatibility
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 10
         */
        NFKD = 4
    }
    /**
     * Provides the text normalization capabilities.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice [since 12]
     * @since 10
     */
    export class Normalizer {
        /**
         * Obtains a **Normalizer** object.
         *
         * @param { NormalizerMode } mode - Text normalization mode.
         * @returns { Normalizer } **Normalizer** object for text normalization.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 10
         */
        static getInstance(mode: NormalizerMode): Normalizer;
        /**
         * Normalizes input strings.
         *
         * @param { string } text - Input text.
         * @returns { string } Normalized strings.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 10
         */
        normalize(text: string): string;
    }
    /**
     * Represents the holiday information.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice [since 12]
     * @since 11
     */
    export interface HolidayInfoItem {
        /**
         * Holiday name.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        baseName: string;
        /**
         * Year of the holiday.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        year: number;
        /**
         * Month of the holiday.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        month: number;
        /**
         * Day of the holiday.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        day: number;
        /**
         * Local names of the holiday.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        localNames?: Array<HolidayLocalName>;
    }
    /**
     * Represents the name of a holiday in different languages.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice [since 12]
     * @since 11
     */
    export interface HolidayLocalName {
        /**
         * Language, for example, **ar**, **en**, or **tr**.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        language: string;
        /**
         * Local name of a holiday. For example, the Turkish name of Sacrifice Feast is Kurban Bayrami.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        name: string;
    }
    /**
     * Provides holiday data parsing capabilities, such as determining holidays and obtaining the holiday list of a
     * specified year.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice [since 12]
     * @since 11
     */
    export class HolidayManager {
        /**
         * Creates a **HolidayManager** object for parsing holiday data.
         *
         * @param { String } icsPath - Path of the **.ics** file with the read permission granted for applications.
         *     iCalendar is a standard Internet calendar format for storing calendar data.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        constructor(icsPath: String);
        /**
         * Determines whether the specified date is a holiday.
         *
         * @param { Date } [date] - Date and time. Note: The month starts from **0**. For example, **0** indicates January.
         *     The default value is the current date.
         * @returns { boolean } **true** if the specified date is a holiday, and **false** otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        isHoliday(date?: Date): boolean;
        /**
         * Obtains the holiday information list of the specified year.
         *
         * @param { number } [year] - Specified year, for example, 2023.
         *   The default value is the current year.
         * @returns { Array<HolidayInfoItem> } Holiday information list.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        getHolidayInfoItemArray(year?: number): Array<HolidayInfoItem>;
    }
    /**
     * Defines a list of entities.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice [since 12]
     * @since 11
     */
    export interface EntityInfoItem {
        /**
         * Start position of the entity in the input string.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        begin: number;
        /**
         * End position of the entity the input string.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        end: number;
        /**
         * Entity type. The value can be **phone_number** or **date**. **phone_number** indicates that the entity is a phone
         * number, and **date** indicates that the entity is a date.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        type: string;
    }
    /**
     * Provides entity recognition capabilities, which can be used to obtain the type and start and end positions of an
     * entity in the text. Currently, supported entities include phone numbers, and date and time.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 24]
     * @atomicservice [since 12]
     * @since 11
     */
    export class EntityRecognizer {
        /**
         * Creates an **entityRecognizer** object. This object is used to recognize entities in the text for the specified
         * locale.
         *
         * @param { string } [locale] - [Locale ID](docroot://internationalization/i18n-locale-culture.md#how-it-works),
         *     which consists of the language, script, and country/region, for example, **zh-Hans-CN**.
         *  The default value is the current system locale.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        constructor(locale?: string);
        /**
         * Obtains entity information in the **text** object.
         *
         * @param { string } text - Input text.
         * @returns { Array<EntityInfoItem> } List of entities in the text.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 24]
         * @atomicservice [since 12]
         * @since 11
         */
        findEntityInfo(text: string): Array<EntityInfoItem>;
    }
    /**
     * Obtains a **SimpleDateTimeFormat** object based on the specified pattern string. For details about the difference
     * between the objects obtained by this API and
     * [getSimpleDateTimeFormatBySkeleton]{@link i18n.getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: Intl.Locale)}
     * , see the examples in [SimpleDateTimeFormat.format]{@link i18n.SimpleDateTimeFormat#format}.
     *
     * @param { string } pattern - Valid pattern, which supports free combinations of field patterns in
     *     [Date Field Symbol Table](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table). This
     *     parameter also supports custom text enclosed in single quotation marks (`''`).
     * @param { Intl.Locale } [locale] - **Locale** object. The default value is the current system locale.
     * @returns { SimpleDateTimeFormat } **SimpleDateTimeFormat** object.
     * @throws { BusinessError } 8900001 - Invalid parameter. Possible causes: Parameter verification failed.
     * @syscap SystemCapability.Global.I18n
     * @atomicservice
     * @since 20
     */
    export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat;
    /**
     * Obtains a **SimpleDateTimeFormat** object based on the specified pattern string. For details about the difference
     * between the objects obtained by this API and
     * [getSimpleDateTimeFormatBySkeleton]{@link i18n.getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: intl.Locale)}
     * , see the examples in [SimpleDateTimeFormat.format]{@link i18n.SimpleDateTimeFormat#format}.
     *
     * @param { string } pattern - Valid pattern, which supports free combinations of field patterns in
     *     [Date Field Symbol Table](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table). This
     *     parameter also supports custom text enclosed in single quotation marks (`''`).
     * @param { intl.Locale } [locale] - **Locale** object. The default value is the current system locale.
     * @returns { SimpleDateTimeFormat } **SimpleDateTimeFormat** object.
     * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
     * @syscap SystemCapability.Global.I18n
     * @atomicservice
     * @since 18
     * @deprecated since 20
     * @useinstead i18n.getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale)
     */
    export function getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat;
    /**
     * Obtains a **SimpleDateTimeFormat** object based on the specified skeleton. For details about the difference between
     * the objects obtained by this API and
     * [getSimpleDateTimeFormatByPattern]{@link i18n.getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale)}
     * , see the examples in [SimpleDateTimeFormat.format]{@link i18n.SimpleDateTimeFormat#format}.
     *
     * @param { string } skeleton - Valid skeleton, which supports free combinations of field patterns in
     *     [Date Field Symbol Table](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table). This
     *     parameter does not support custom text.
     * @param { Intl.Locale } [locale] - **Locale** object. The default value is the current system locale.
     * @returns { SimpleDateTimeFormat } **SimpleDateTimeFormat** object.
     * @throws { BusinessError } 8900001 - Invalid parameter. Possible causes: Parameter verification failed.
     * @syscap SystemCapability.Global.I18n
     * @atomicservice
     * @since 20
     */
    export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: Intl.Locale): SimpleDateTimeFormat;
    /**
     * Obtains a **SimpleDateTimeFormat** object based on the specified skeleton. For details about the difference between
     * the objects obtained by this API and
     * [getSimpleDateTimeFormatByPattern]{@link i18n.getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale)}
     * , see the examples in [SimpleDateTimeFormat.format]{@link i18n.SimpleDateTimeFormat#format}.
     *
     * @param { string } skeleton - Valid skeleton, which supports free combinations of field patterns in
     *     [Date Field Symbol Table](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table). This
     *     parameter does not support custom text.
     * @param { intl.Locale } [locale] - **Locale** object. The default value is the current system locale.
     * @returns { SimpleDateTimeFormat } **SimpleDateTimeFormat** object.
     * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
     * @syscap SystemCapability.Global.I18n
     * @atomicservice
     * @since 18
     * @deprecated since 20
     * @useinstead i18n.getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: Intl.Locale)
     */
    export function getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleDateTimeFormat;
    /**
     * Provide a simple date time formatting interface.
     *
     * @syscap SystemCapability.Global.I18n
     * @atomicservice
     * @since 18
     */
    export class SimpleDateTimeFormat {
        /**
         * Formats the date and time.
         *
         * @param { Date } date - Date and time. Note: The month starts from **0**. For example, **0** indicates January.
         * @returns { string } A string containing the formatted date and time.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 18
         */
        format(date: Date): string;
    }
    /**
     * Obtains a **SimpleNumberFormat** object based on the specified skeleton.
     *
     * @param { string } skeleton - Valid skeleton. For details about the supported characters and their meanings, see
     *     [Number Skeletons](https://unicode-org.github.io/icu/userguide/format_parse/numbers/skeletons.html#number-skeletons)
     *     .
     * @param { Intl.Locale } [locale] - **Locale** object. The default value is the current system locale.
     * @returns { SimpleNumberFormat } **SimpleNumberFormat** object.
     * @throws { BusinessError } 8900001 - Invalid parameter. Possible causes: Parameter verification failed.
     * @syscap SystemCapability.Global.I18n
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    export function getSimpleNumberFormatBySkeleton(skeleton: string, locale?: Intl.Locale): SimpleNumberFormat;
    /**
     * Obtains a **SimpleNumberFormat** object based on the specified skeleton.
     *
     * @param { string } skeleton - Valid skeleton. For details about the supported characters and their meanings, see
     *     [Number Skeletons](https://unicode-org.github.io/icu/userguide/format_parse/numbers/skeletons.html#number-skeletons)
     *     .
     * @param { intl.Locale } [locale] - **Locale** object. The default value is the current system locale.
     * @returns { SimpleNumberFormat } **SimpleNumberFormat** object.
     * @throws { BusinessError } 890001 - Invalid parameter. Possible causes: Parameter verification failed.
     * @syscap SystemCapability.Global.I18n
     * @crossplatform
     * @atomicservice
     * @since 18
     * @deprecated since 20
     * @useinstead i18n.getSimpleNumberFormatBySkeleton(skeleton: string, locale?: Intl.Locale)
     */
    export function getSimpleNumberFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleNumberFormat;
    /**
     * Formats a number based on the specified skeleton string.
     *
     * @syscap SystemCapability.Global.I18n
     * @atomicservice
     * @since 18
     */
    export class SimpleNumberFormat {
        /**
         * Formats a number.
         *
         * @param { number } value - Number to be formatted.
         * @returns { string } Formatted number.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 18
         */
        format(value: number): string;
    }
    /**
     * Provide a number formatting interface which could format number to StyleString.
     *
     * @syscap SystemCapability.Global.I18n
     * @atomicservice
     * @since 18
     */
    export class StyledNumberFormat {
        /**
         * Creates a **NumberFormat** object for rich text display.
         *
         * @param { Intl.NumberFormat | SimpleNumberFormat } numberFormat - **NumberFormat** object.
         * @param { StyledNumberFormatOptions } [ options ] - Configuration options of the **NumberFormat** object. The
         *     default value is the default text style.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 20
         */
        constructor(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions);
        /**
         * Creates a **NumberFormat** object for rich text display.
         *
         * @param { intl.NumberFormat | SimpleNumberFormat } numberFormat - **NumberFormat** object.
         * @param { StyledNumberFormatOptions } [ options ] - Configuration options of the **NumberFormat** object. The
         *     default value is the default text style.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 18
         * @deprecated since 20
         * @useinstead i18n.StyledNumberFormat.constructor(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)
         */
        constructor(numberFormat: intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions);
        /**
         * Formats a number as a rich text object.
         *
         * @param { number } value - Number to be formatted.
         * @returns { StyledString } Rich text object after formatting.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 18
         */
        format(value: number): StyledString;
    }
    /**
     * Represents optional configuration items for the **NumberFormat** object.
     *
     * @syscap SystemCapability.Global.I18n
     * @atomicservice
     * @since 18
     */
    export interface StyledNumberFormatOptions {
        /**
         * Text style for the integer part. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 18
         */
        integer?: TextStyle;
        /**
         * Text style for the decimal point. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 18
         */
        decimal?: TextStyle;
        /**
         * Text style for the fraction part. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 18
         */
        fraction?: TextStyle;
        /**
         * Text style for the unit. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 18
         */
        unit?: TextStyle;
    }
    /**
     * Provide a DateTime formatting interface which could format DateTime to StyleString.
     *
     * @syscap SystemCapability.Global.I18n
     * @atomicservice
     * @since 23
     */
    export class StyledDateTimeFormat {
        /**
         * Creates an object for formatting the time and date that need to be displayed in rich text.
         *
         * @param { Intl.DateTimeFormat | SimpleDateTimeFormat } dateTimeFormat - Object used to format the date and time.
         * @param { StyledDateTimeFormatOptions } [ options ] - Specifies the configuration items of the time and date
         *     formatting object. The default value is the default text style.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 23
         */
        constructor(dateTimeFormat: Intl.DateTimeFormat | SimpleDateTimeFormat, options?: StyledDateTimeFormatOptions);
        /**
         * Formats the date and time as a rich text object.
         *
         * @param { Date } date - Date and time to be formatted.
         * @returns { StyledString } Rich text object after formatting.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 23
         */
        format(date: Date): StyledString;
    }
    /**
     * Optional configuration items for creating the time and date formatting object for rich text display.
     *
     * @syscap SystemCapability.Global.I18n
     * @atomicservice
     * @since 23
     */
    export interface StyledDateTimeFormatOptions {
        /**
         * Specifies the text style of the year. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 23
         */
        year?: TextStyle;
        /**
         * Specifies the text style of the month. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 23
         */
        month?: TextStyle;
        /**
         * Specifies the text style of the day. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 23
         */
        day?: TextStyle;
        /**
         * Specifies the text style of the hour. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 23
         */
        hour?: TextStyle;
        /**
         * Specifies the text style of the minute. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 23
         */
        minute?: TextStyle;
        /**
         * Specifies the text style of the second. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 23
         */
        second?: TextStyle;
        /**
         * Specifies the text style of the period. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 23
         */
        dayPeriod?: TextStyle;
        /**
         * Specifies the text style of the week. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 23
         */
        weekday?: TextStyle;
        /**
         * Specifies the text style of the era. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 23
         */
        era?: TextStyle;
        /**
         * Specifies the text style of the time zone name. The default value is the default text style of StyledString.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 23
         */
        timeZoneName?: TextStyle;
    }
    /**
     * Provides the number formatting capability, supporting automatic unit conversion based on
     * specific application scenarios.
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    export class AdvancedMeasureFormat {
        /**
         * Creates a **NumberFormat** object for the specified locale.
         *
         * @param { Intl.NumberFormat } numberFormat - Indicates the number format object that used to format number.
         * @param { AdvancedMeasureFormatOptions } [ options ] - Indicates the options for AdvancedMeasureFormat.
         *     When no options are provided, the formatting result is consistent with that of NumberFormat.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        constructor(numberFormat: Intl.NumberFormat, options?: AdvancedMeasureFormatOptions);
        /**
         * Formats a number by appropriate measure for usage scenarios. For instance, when formatting the value 12.3
         *     for rainfall in the English locale, the output is "12.3 mm".
         *
         * @param { number } num - Number to be formatted.
         * @returns { string } Formatted text.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        format(num: number): string;
    }
    /**
     * Represents optional configuration items for AdvancedMeasureFormat object.
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    export interface AdvancedMeasureFormatOptions {
        /**
         * Scenarios for MeasureFormat.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        unitUsage?: UnitUsage;
    }
    /**
     * Enumerates unit formatting scenarios.
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    export enum UnitUsage {
        /**
         * Area land agricult scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        AREA_LAND_AGRICULT = 1,
        /**
         * Area land commercl scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        AREA_LAND_COMMERCL = 2,
        /**
         * Area land residntl scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        AREA_LAND_RESIDNTL = 3,
        /**
         * Length person scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        LENGTH_PERSON = 4,
        /**
         * Length person small scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        LENGTH_PERSON_SMALL = 5,
        /**
         * Length rainfall scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        LENGTH_RAINFALL = 6,
        /**
         * Length road scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        LENGTH_ROAD = 7,
        /**
         * Length road small scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        LENGTH_ROAD_SMALL = 8,
        /**
         * Length snowfall scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        LENGTH_SNOWFALL = 9,
        /**
         * Length vehicle scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        LENGTH_VEHICLE = 10,
        /**
         * Length visiblty scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        LENGTH_VISIBLTY = 11,
        /**
         * Length visiblty small scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        LENGTH_VISIBLTY_SMALL = 12,
        /**
         * Length person informal scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        LENGTH_PERSON_INFORMAL = 13,
        /**
         * Length person small informal scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        LENGTH_PERSON_SMALL_INFORMAL = 14,
        /**
         * Length road informal scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        LENGTH_ROAD_INFORMAL = 15,
        /**
         * Speed road travel scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        SPEED_ROAD_TRAVEL = 16,
        /**
         * Speed wind scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        SPEED_WIND = 17,
        /**
         * Temperature person scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        TEMPERATURE_PERSON = 18,
        /**
         * Temperature weather scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        TEMPERATURE_WEATHER = 19,
        /**
         * Volume vehicle fuel scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        VOLUME_VEHICLE_FUEL = 20,
        /**
         * Elapsed time second scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        ELAPSED_TIME_SECOND = 21,
        /**
         * Size file byte scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        SIZE_FILE_BYTE = 22,
        /**
         * Size shortfile byte scenario.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        SIZE_SHORTFILE_BYTE = 23
    }
    /**
     * Provide a DateTime formatting interface that supports custom symbols.
     * This interface formats date time values into strings with custom symbols,
     * and can replace variable symbols in the formatted result with custom fixed symbols
     * (e.g., replacing "2:23 PM" with "2:23 afternoon").
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export class SymbolDateTimeFormat extends Intl.DateTimeFormat {
        /**
         * A constructor used to create a SymbolDateTimeFormat object.
         *
         * @param { Intl.Locale } [locale] - Locale object used for formatting the date time value.
         *     The default value is the current system locale.
         * @param { SymbolDateTimeFormatOptions } [options] - Indicates the symbols used to replace.
         *     The symbols that support replacement are "AM" and "PM".
         * @throws { BusinessError } 8900001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public constructor(locale?: Intl.Locale, options?: SymbolDateTimeFormatOptions);
        /**
         * Formats the date and time.
         *
         * @param { Date | number } [date] - Date and time. Note: The month starts from 0. For example, 0 indicates January.
         * @returns { string } The formatted date and time string.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public format(date?: Date | number): string;
        /**
         * Formats date and time ranges.
         *
         * @param { Date | number | bigint } startDate - Start date and time, represented as a Date object or timestamp.
         *      Note: The month starts from 0. For example, 0 indicates January.
         * @param { Date | number | bigint } endDate - End date and time, represented as a Date object or timestamp.
         *      Note: The month starts from 0. For example, 0 indicates January.
         * @returns { string } A date string formatted based on the specified locale.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public formatRange(startDate: Date | number | bigint, endDate: Date | number | bigint): string;
        /**
         * Formats a date time range to Parts.
         *
         * @param { Date | number | bigint } startDate - Start date and time, represented as a Date object or timestamp.
         *      Note: The month starts from 0. For example, 0 indicates January.
         * @param { Date | number | bigint } endDate - End date and time, represented as a Date object or timestamp.
         *      Note: The month starts from 0. For example, 0 indicates January.
         * @returns { Intl.DateTimeRangeFormatPart[] } Locale formatted DateTimeRangeFormatPart array.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public formatRangeToParts(startDate: Date | number | bigint, endDate: Date | number | bigint): Intl.DateTimeRangeFormatPart[];
        /**
         * Formats a date to parts.
         *
         * @param { Date | number } [date] - Date or timestamp. Note: The month starts from 0.
         *     For example, 0 indicates January.
         * @returns { Intl.DateTimeFormatPart[] } Locale formatted DateTimeFormatPart array.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public formatToParts(date?: Date | number): Intl.DateTimeFormatPart[];
        /**
         * Parse a date time localized string to Unix timestamp.
         * Unix timestamp, indicating the number of milliseconds elapsed since 00:00:00 on January 1, 1970 GMT.
         *
         * @param { string } text - Localized string to be parse.
         *     <br>Text to be parsed
         * @param { boolean } lenientMode - Indicates whether parsing allows any non-compliant localized strings.
         *     For example, "2023/02-25" is a invalid separator date string, it will parse failure when lenientMode
         *     is false, and will parse success with value (2023, 02, 25) when lenientMode is true. it's better set
         *     to false, ensure the data is not polluted.
         *     <br>Whether to use loose parsing rules
         * @returns { number } Unix timestamp, which indicates the number of milliseconds that have elapsed since
         *     the Unix epoch.
         * @throws { BusinessError } 8900001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public parse(text: string, lenientMode: boolean): number;
        /**
         * Obtains the options for creating a SymbolDateTimeFormat object.
         * This will allow us to check the current config symbols.
         *
         * @returns { ResolvedSymbolDateTimeFormatOptions } Symbol options for SymbolDateTimeFormat.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public resolvedOptions(): ResolvedSymbolDateTimeFormatOptions;
    }
    /**
     * Represents optional configuration items for the SymbolDateTimeFormat object.
     * Define the symbol element and value that need to be replaced.
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export interface SymbolDateTimeFormatOptions extends Intl.DateTimeFormatOptions {
        /**
         * AM and PM symbol of date time period part, such as "PM" of "2:23 PM". The parameter array
         *     must be greater than 2, If greater than 2, the first two will be selected.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        amPMSymbol?: string[] | undefined;
    }
    /**
     * Represents optional element for the ResolvedSymbolDateTimeFormatOptions object.
     * Define the resolved symbol element and value that need to get.
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export interface ResolvedSymbolDateTimeFormatOptions extends Intl.ResolvedDateTimeFormatOptions {
        /**
         * AM and PM symbol of date time period part, such as "PM" of "2:23 PM". First parameter is AM,
         *     second parameter is PM.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        amPMSymbol?: string[];
    }
    /**
     * Provide a Number formatting interface that supports custom symbols.
     * This interface formats number values into strings with custom symbols,
     * and can replace variable symbols in the formatted result with custom fixed symbols
     * (e.g., replacing "null" to "NA").
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export class SymbolNumberFormat implements Intl.NumberFormat {
        /**
         * A constructor used to create a SymbolNumberFormat object.
         *
         * @param { Intl.Locale } [locale] - Locale object used for formatting the date time value.
         *     The default value is the current system locale.
         *     <br>Default value:The default is the current system locale.
         *     <br>Default Value: System Locale.
         *     <br>Region object.
         * @param { SymbolNumberFormatOptions } [options] - Indicates the symbols used to replace.
         *     Such as zero, nan, positiveInfinity, etc.
         *     <br>Symbol Number Formatting Options.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public constructor(locale?: Intl.Locale, options?: SymbolNumberFormatOptions);
        /**
         * Formats a number with give locale and SymbolNumberFormatOptions.
         *
         * @param { number | bigint } value - Number to be formatted.
         * @returns { string } Formatted number.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public format(value: number | bigint): string;
        /**
         * Formats a number range.
         *
         * @param { number } startRange - Start number of the range.
         * @param { number } endRange - End number of the range.
         * @returns { string } Formatted number range.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public formatRange(startRange: number, endRange: number): string;
        /**
         * Formats a number into parts.
         *
         * @param { number | bigint } [value] - Number to be formatted.
         * @returns { Intl.NumberFormatPart[] } Locale formatted NumberFormatPart array.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public formatToParts(value?: number | bigint): Intl.NumberFormatPart[];
        /**
         * Formats a number range into parts.
         *
         * @param { number } startRange - Start number of the range.
         * @param { number } endRange - End number of the range.
         * @returns { Intl.NumberFormatPart[] } Locale formatted NumberFormatPart array.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public formatRangeToParts(startRange: number, endRange: number): Intl.NumberFormatPart[];
        /**
         * Parse a localized string to number object. For example, "123,456" will parse to 123456.
         *
         * @param { string } text - Localized string to be parse.
         *     <br>Text to be parsed
         * @param { boolean } lenientMode - Indicates whether parsing allows any non-compliant localized strings.
         *     For example, "1,23,456" is a invalid thousand separator number string, it will parse failure
         *     when lenientMode is false, and will parse success with value 123456 when lenientMode is true.it's better
         *     set to false, ensure the data is not polluted.
         *     <br>Whether to use loose rules
         * @returns { number } The result parse with localization rules.
         * @throws { BusinessError } 8900001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public parse(text: string, lenientMode: boolean): number;
        /**
         * Represents optional element for the ResolvedSymbolDateTimeFormatOptions object.
         * Define the resolved symbol element and value that need to get.
         *
         * @returns  { ResolvedSymbolNumberFormatOptions } Symbol options for SymbolNumberFormat.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public resolvedOptions(): ResolvedSymbolNumberFormatOptions;
    }
    /**
     * Represents optional configuration items for the SymbolNumberFormat object.
     * Define the symbol element and value that need to be replaced.
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export interface SymbolNumberFormatOptions extends Intl.NumberFormatOptions {
        /**
         * Zero symbol of localized number part, such as "0".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        zero?: string | undefined;
        /**
         * NaN symbol of localized number part, such as "null".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        nan?: string | undefined;
        /**
         * Minus sign of localized number part, such as "-".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        minusSign?: string | undefined;
        /**
         * Plus sign of localized number part, such as "+".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        plusSign?: string | undefined;
        /**
         * Infinity symbol of localized number part, such as "∞".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        infinity?: string | undefined;
        /**
         * Grouping Separator symbol of localized number part, such as "," of "10,000".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        groupingSeparator?: string | undefined;
    }
    /**
     * Represents optional element for the ResolvedSymbolNumberFormatOptions object.
     * Define the resolved symbol element and value that need to get.
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export interface ResolvedSymbolNumberFormatOptions extends Intl.ResolvedNumberFormatOptions {
        /**
         * Zero symbol of localized number part, such as "0".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        zero?: string;
        /**
         * NaN symbol of localized number part, such as "null".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        nan?: string;
        /**
         * Minus sign of localized number part, such as "-".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        minusSign?: string;
        /**
         * Plus sign of localized number part, such as "+".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        plusSign?: string;
        /**
         * Infinity symbol of localized number part, such as "∞".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        infinity?: string;
        /**
         * Grouping Separator symbol of localized number part, such as "," of "10,000".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        groupingSeparator?: string;
    }
    /**
     * Provide a DateTime formatting interface which could format date to ISO 8601 standard string.
     * [ISO8601](https://iso8601.com/).
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export class ISO8601DateTimeFormat {
        /**
         * A constructor used to create a ISO8601DateTimeFormat object.
         *
         * @param { ISO8601DateTimeFormatOptions } [options] - Options for creating a date formatting object
         *     that complies with ISO 8601.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public constructor(options?: ISO8601DateTimeFormatOptions);
        /**
         * Formats a date to ISO 8601 formatted string.
         *
         * @param { Date } date - date to be formatted. Note: The month starts from 0. For example, 0 indicates January.
         * @returns { string } Date and time string that complies with ISO 8601.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public format(date: Date): string;
    }
    /**
     * Represents optional configuration items for the ISO8601DateTimeFormat object.
     * These options determine which elements need to be displayed after formatting and the corresponding format.
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export interface ISO8601DateTimeFormatOptions {
        /**
         * The ISO 8601 date format to format. The value can be: "calendar", the format is yyyy-MM-dd; "ordinal",
         * the format is yyyy-DDD; "week", the format is YYYY-Www-e. Default value is "calendar".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        dateFormat?: 'calendar' | 'ordinal' | 'week';
        /**
         * The ISO 8601 time precision to format. The value can be: "dateOnly", "hours", "minutes", "seconds",
         * "milliSeconds". Default value is "seconds".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        timePrecision?: 'dateOnly' | 'hours' | 'minutes' | 'seconds' | 'milliSeconds';
        /**
         * The date time separator style. The value can be: "extended": with -/:, "basic": compact mode.
         * Default separator style is "extended".
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        separatorStyle?: 'extended' | 'basic';
        /**
         * TimeZone object used to format date, default value UTC.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        timeZone?: TimeZone;
        /**
         * Check if need to show time zone part. Default value is true that show time zone.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        displayTimeZone?: boolean;
    }
    /**
     * Obtains the ChineseCalendar object for the specified locale.
     *
     * @param { Intl.Locale } [locale] - Locale object. The default value is the current system locale.
     * @returns { ChineseCalendar } ChineseCalendar object.
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export function getChineseCalendar(locale?: Intl.Locale): ChineseCalendar;
    /**
     * Provide a ChineseCalendar interface which could handle unique characteristics of the chinese calendar,
     * such as leap month.
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export class ChineseCalendar extends Calendar {
        /**
         * Sets the year, month, day, hour, minute, second, isLeapMonth for this ChineseCalendar object.
         *
         * @param { ChineseCalendarTime } chineseCalendarTime - Indicates the time element used to set for ChineseCalendar.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public setChineseCalendarTime(chineseCalendarTime: ChineseCalendarTime): void;
        /**
         * Checks whether a given month exist leap month in gregorianYear and cyclicalYear.
         *
         * @param { number } gregorianYear - Gregorian year to check, supported range is from 1900 to 2100.
         *     <br>The value range is all integers.
         *     <br>Year.
         * @param { number } cyclicalYear - Cyclical year to check, supported range is from 1 to 60.
         *     <br>The value range is all integers.
         *     <br>Year.
         * @param { number } month - Month to check. Note: The month starts from 0. For example, 0 indicates January.
         *     <br>The value range is all integers.
         *     <br>Month.
         * @returns { boolean } Check whether the input month is a leap month.
         * @throws { BusinessError } 8900001 - Invalid parameter. Possible causes: Parameter verification failed.
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        public static checkLeapMonth(gregorianYear: number, cyclicalYear: number, month: number): boolean;
    }
    /**
     * Represents chinese calendar time element for the ChineseCalendar object.
     *
     * @syscap SystemCapability.Global.I18n
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export interface ChineseCalendarTime {
        /**
         * The gregorian year of date.
         * If you need to convert between the chinese calendar and the Gregorian calendar,
         * the year range must be set from 1900 to 2100.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        gregorianYear: number;
        /**
         * The cyclical year of date.
         * If you need to convert between the chinese calendar and the Gregorian calendar,
         * the year range must be set from 1 to 60.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        cyclicalYear: number;
        /**
         * Month of the chinese calendar time. Note: The month starts from 0. For example, 0 indicates January.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        month: number;
        /**
         * Date of the chinese calendar time.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        date: number;
        /**
         * Determines whether the input month is a leap month.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        isLeapMonth?: boolean;
        /**
         * Hour of the chinese calendar time.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        hour?: number;
        /**
         * Minute of the chinese calendar time.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        minute?: number;
        /**
         * Second of the chinese calendar time.
         *
         * @syscap SystemCapability.Global.I18n
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        second?: number;
    }
}
export default i18n;

```
