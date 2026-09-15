# @ohos.intl.d.ts

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
/**
 * The **intl** module provides basic i18n capabilities, such as time and date formatting, number formatting, and string
 * sorting, through the standard i18n APIs defined in ECMA 402.
 *
 * @syscap SystemCapability.Global.I18n
 * @crossplatform [since 10]
 * @form [since 11]
 * @atomicservice [since 12]
 * @since 6
 */
declare namespace intl {
    /**
     * Options for initializing the **Locale** object. Since API version 9, the **LocaleOptions** attribute is changed
     * from mandatory to optional.
     *
     * > **NOTE**
     * >
     * > - For details about **calendar**, see Table 1 in
     * > [Calendar Setting](docroot://internationalization/i18n-calendar.md).
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @form [since 11]
     * @atomicservice [since 12]
     * @since 6
     * @deprecated since 20
     * @useinstead [Intl.LocaleOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#options)
     */
    export interface LocaleOptions {
        /**
         * Calendar parameter. The value can be:
         *
         * "buddhist", "chinese", "coptic", "dangi", "ethioaa", "ethiopic", "gregory", "hebrew", "indian", "islamic", "
         * islamic-umalqura", "islamic-tbla", "islamic-civil", "islamic-rgsa", "iso8601", "japanese", "persian", "roc",
         * or "islamicc".
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#calendar)
         */
        calendar?: string;
        /**
         * Collation rules for the locale. The value can be:
         *
         * **big5han**: Pinyin sorting for Latin letters.
         *
         * **compat**: compatibility sorting, only for Arabic.
         *
         * **dict**: dictionary-style sorting, only for Singhalese.
         *
         * **direct**: binary code point sorting.
         *
         * **ducet**: sorting according to the Unicode collation element table.
         *
         * **eor**: sorting according to the European collation rules.
         *
         * **gb2312**: Pinyin sorting, only for Chinese.
         *
         * **phonebk**: phone book-style sorting.
         *
         * **phonetic**: phonetic sorting.
         *
         * **pinyin**: Pinyin sorting.
         *
         * **reformed**: reformed sorting, only for Swedish.
         *
         * **searchjl**: special sorting for Korean initial consonant search.
         *
         * **stroke**: stroke sorting for Chinese.
         *
         * **trad**: traditional-style sorting, for example, Spanish.
         *
         * **unihan**: radical-stroke sorting for Han characters, only for Chinese, Japanese, and Korean.
         *
         * **zhuyin**: Zhuyin sorting, only for Chinese.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.collation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#collation)
         */
        collation?: string;
        /**
         * Hour cycle. The value can be:
         *
         * "h11", "h12", "h23", or  "h24".
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.hourCycle](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#hourcycle)
         */
        hourCycle?: string;
        /**
         * Numbering system. The value can be:
         *
         * **adlm**, **ahom**, **arab**, **arabext**, **bali**, **beng**, **bhks**, **brah**, **cakm**, **cham**, **deva**,
         * **diak**, **fullwide**, **gong**, **gonm**, **gujr**, **guru**, **hanidec**, **hmng**, **hmnp**, **java**,
         * **kali**, **khmr**, **knda**, **lana**, **lanatham**, **laoo**, **latn**, **lepc**, **limb**, **mathbold**,
         * **mathdbl**, **mathmono**, **mathsanb**, **mathsans**, **mlym**, **modi**, **mong**, **mroo**, **mtei**, **mymr**,
         * **mymrshan**, **mymrtlng**, **newa**, **nkoo**, **olck**, **orya**, **osma**, **rohg**, **saur**, **segment**,
         * **shrd**, **sind**, **sinh**, **sora**, **sund**, **takr**, **talu**, **tamldec**, **telu**, **thai**, **tibt**,
         * **tirh**, **vaii**, **wara**, or **wcho**.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.numberingSystem](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#numberingsystem)
         */
        numberingSystem?: string;
        /**
         * Whether to treat numeric characters as numbers for sorting. The value true means to treat numeric characters as
         * numbers for sorting, and the value **false** means to treat numeric characters as ordinary characters for
         * sorting. For example, when this parameter is set to **true**, comparing the string **21** with the string **123**
         * is equivalent to comparing the number 21 with the number 123. The default value is **false**.
         *
         * @type { boolean } [since 6 - 8]
         * @type { ?boolean } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.numeric](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#numeric)
         */
        numeric?: boolean;
        /**
         * Whether case is taken into account for the locale's collation rules. The value can be:
         *
         * **upper**: Uppercase letters come first.
         *
         * **lower**: Lowercase letters come first.
         *
         * **false**: The default collation rules of the locale are used.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.caseFirst](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#casefirst)
         */
        caseFirst?: string;
    }
    /**
     * Provides APIs for obtaining locale information.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @form [since 11]
     * @atomicservice [since 12]
     * @since 6
     * @deprecated since 20
     * @useinstead [Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
     */
    export class Locale {
        /**
         * Creates a **Locale** object.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.Locale.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)
         */
        constructor();
        /**
         * Creates a **Locale** object.
         *
         * @param { string } locale - Locale information, which consists of the language, script, and country/region.
         * @param { LocaleOptions } options - Options for creating the **Locale** object. [since 6 - 11]
         * @param { LocaleOptions } [options] - Options for creating the **Locale** object. [since 12]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.Locale.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)
         */
        constructor(locale: string, options?: LocaleOptions);
        /**
         * Language associated with the locale, for example, **zh**. The value complies with the ISO 639 standard.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.language](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language)
         */
        language: string;
        /**
         * Script type of the language, for example, **Hans**. The value complies with the Unicode ISO 15924 standard.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.script](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script)
         */
        script: string;
        /**
         * Country/region associated with the locale, for example, **CN**. The value complies with the ISO 3166 standard.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.region](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/region)
         */
        region: string;
        /**
         * Locale information, which consists of the language, script, and country/region, for example, **zh-Hans-CN**.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.baseName](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/baseName)
         */
        baseName: string;
        /**
         * Whether case is taken into account for the locale's collation rules. The value can be:
         *        **upper**: Uppercase letters come first.
         *        **lower**: Lowercase letters come first.
         *        **false**: The default collation rules of the locale are used.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.caseFirst](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst)
         */
        caseFirst: string;
        /**
         * Calendar for the locale. The value can be:
         * The value can be any of the following: **buddhist**, **chinese**,
         * **coptic**, **dangi**, **ethioaa**, **ethiopic**, **gregory**, **hebrew**, **indian**, **islamic**,
         * **islamic-umalqura**, **islamic-tbla**, **islamic-civil**, **islamic-rgsa**, **iso8601**, **japanese**,
         * **persian**, **roc**, or **islamicc**.
         *  For details about their meanings, see Table 1 in
         * [Calendar Setting](docroot://internationalization/i18n-calendar.md).
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/calendar)
         */
        calendar: string;
        /**
         * Collation rules for the locale. The value can be:
         * **big5han**: Pinyin sorting for Latin letters.
         * **compat** : compatibility sorting, only for Arabic.
         * **dict**: dictionary-style sorting, only for Singhalese.
         * **direct**: binary code point sorting.
         * **ducet**: sorting according to the Unicode collation element table.
         * **eor**: sorting according to the European collation rules.
         * **gb2312**: Pinyin sorting, only for Chinese.
         * **phonebk**: phone book-style sorting.
         * **phonetic**: phonetic sorting.
         * **pinyin**: Pinyin sorting.
         * **reformed**: reformed sorting, only for Swedish.
         * **searchjl**: special sorting for Korean initial consonant search.
         * **stroke**: stroke sorting for Chinese.
         * **trad**: traditional-style sorting, for example, Spanish.
         * **unihan**: radical-stroke sorting for Han characters, only for Chinese, Japanese, and Korean.
         * **zhuyin**: Zhuyin  sorting, only for Chinese.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.collation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/collation)
         */
        collation: string;
        /**
         * Time system for the locale. The value can be:
         * "h11", "h12", "h23", or "h24".
         * For details about their
         * display effects, see [Table 5](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.hourCycle](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/hourCycle)
         */
        hourCycle: string;
        /**
         * Numbering system for the locale. The value can be:
         * **adlm**, **ahom**, **arab**, **arabext**, **bali**,
         * **beng**, **bhks**, **brah**, **cakm**, **cham**, **deva**, **diak**, **fullwide**, **gong**, **gonm**, **gujr**,
         * **guru**, **hanidec**, **hmng**, **hmnp**, **java**, **kali**, **khmr**, **knda**, **lana**, **lanatham**,
         * **laoo**, **latn**, **lepc**, **limb**, **mathbold**, **mathdbl**, **mathmono**, **mathsanb**, **mathsans**,
         * **mlym**, **modi**, **mong**, **mroo**, **mtei**, **mymr**, **mymrshan**, **mymrtlng**, **newa**, **nkoo**,
         * **olck**, **orya**, **osma**, **rohg**, **saur**, **segment**, **shrd**, **sind**, **sinh**, **sora**, **sund**,
         * **takr**, **talu**, **tamldec**, **telu**, **thai**, **tibt**, **tirh**, **vaii**, **wara**, or **wcho**.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.numberingSystem](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/numberingSystem)
         */
        numberingSystem: string;
        /**
         * Whether to use special sorting rules for digits. The value **true** means to use special sorting rules for digits,
         * and the value **false** means the opposite.The default value is **false**.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.LocaleOptions.numeric](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/numeric)
         */
        numeric: boolean;
        /**
         * Obtains the string that represents a **Locale** object.
         *
         * @returns { string } String that represents the **Locale** object.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.Locale.toString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/toString)
         */
        toString(): string;
        /**
         * Maximizes locale information by supplementing the missing script and country/region information.
         *
         * @returns { Locale } **Locale** object with the script and country/region information.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.Locale.maximize](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/maximize)
         */
        maximize(): Locale;
        /**
         * Minimizes locale information by removing the script and country/region information.
         *
         * @returns { Locale } **Locale** object without the script and country/region information.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.Locale.minimize](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/minimize)
         */
        minimize(): Locale;
    }
    /**
     * Defines the options for a **DateTimeOptions** object. Since API version 9, the **DateTimeOptions** attribute is
     * changed from mandatory to optional.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @form [since 11]
     * @atomicservice [since 12]
     * @since 6
     * @deprecated since 20
     * @useinstead [Intl.DateTimeFormatOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#options)
     */
    export interface DateTimeOptions {
        /**
         * Valid locale ID, for example, **zh-Hans-CN**.
         *
         * The default value is the current system locale.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         */
        locale?: string;
        /**
         * Date display format. The value can be:
         *
         * "long", "short", "medium", "full", or  "auto".
         *
         * For details about their display effects, see
         * [Table 1](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.dateStyle](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#datestyle)
         */
        dateStyle?: string;
        /**
         * Time display format. The value can be:
         *
         * "long", "short", "medium", "full", or  "auto".
         *
         * For details about their display effects, see
         * [Table 2](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.timeStyle](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#timestyle)
         */
        timeStyle?: string;
        /**
         * Hour cycle. The value can be:
         *
         * "h11", "h12", "h23", or  "h24".
         *
         * For the display effects when **dateStyle** or **timeStyle** is not set, see
         * [Table 5](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * For the display effects when **dateStyle** or **timeStyle** is not set, see
         * [Table 6](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.hourCycle](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#hourcycle)
         */
        hourCycle?: string;
        /**
         * Time zone in use. The value is a valid IANA time zone ID.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.timeZone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#timezone)
         */
        timeZone?: string;
        /**
         * Numbering system. The value can be:
         *
         * **adlm**, **ahom**, **arab**, **arabext**, **bali**, **beng**, **bhks**, **brah**, **cakm**, **cham**, **deva**,
         * **diak**, **fullwide**, **gong**, **gonm**, **gujr**, **guru**, **hanidec**, **hmng**, **hmnp**, **java**,
         * **kali**, **khmr**, **knda**, **lana**, **lanatham**, **laoo**, **latn**, **lepc**, **limb**, **mathbold**,
         * **mathdbl**, **mathmono**, **mathsanb**, **mathsans**, **mlym**, **modi**, **mong**, **mroo**, **mtei**, **mymr**
         * , **mymrshan**, **mymrtlng**, **newa**, **nkoo**, **olck**, **orya**, **osma**, **rohg**, **saur**, **segment**,
         * **shrd**, **sind**, **sinh**, **sora**, **sund**, **takr**, **talu**, **tamldec**, **telu**, **thai**, **tibt**,
         * **tirh**, **vaii**, **wara**, or **wcho**.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.numberingSystem](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#numberingsystem)
         */
        numberingSystem?: string;
        /**
         * Whether to use the 12-hour clock. The value **true** means to use the 12-hour clock, and the value **false**
         * means the opposite.
         *
         * If both **hour12** and **hourCycle** are set, **hourCycle** does not take effect.
         *
         * If **hour12** and **hourCycle** are not set and the 24-hour clock is turned on, the default value of **hour12**
         * is **false**.
         *
         * @type { boolean } [since 6 - 8]
         * @type { ?boolean } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.hour12](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#hour12)
         */
        hour12?: boolean;
        /**
         * Week display format. The value can be:
         *
         * "long", "short", "narrow", or  "auto".
         *
         * For details about their display effects, see
         * [Table 4](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.weekday](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#weekday)
         */
        weekday?: string;
        /**
         * Epoch display format. The value can be:
         *
         * "long", "short", "narrow", or  "auto".
         *
         * For details about their display effects, see
         * [Table 9](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.era](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#era)
         */
        era?: string;
        /**
         * Year display format. The value can be:
         *
         * "numeric" or  "2-digit".
         *
         * For details about their display effects, see
         * [Table 3](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.year](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#year)
         */
        year?: string;
        /**
         * Month display format. The value can be:
         *
         * "numeric", "2-digit", "long", "short", "narrow", or  "auto".
         *
         * For details about their display effects, see
         * [Table 7](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.month](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#month)
         */
        month?: string;
        /**
         * Day display format. The value can be:
         *
         * "numeric" or  "2-digit".
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.day](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#day)
         */
        day?: string;
        /**
         * Hour display format. The value can be:
         *
         * "numeric" or  "2-digit".
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.hour](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#hour)
         */
        hour?: string;
        /**
         * Minute display format. The value can be:
         *
         * "numeric" or  "2-digit".
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.minute](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#minute)
         */
        minute?: string;
        /**
         * Second display format. The value can be:
         *
         * "numeric" or  "2-digit".
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.second](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#second)
         */
        second?: string;
        /**
         * Localized representation of a time zone name. The value can be:
         *
         * "long", "short", or  "auto".
         *
         * For details about their display effects, see
         * [Table 8](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.timeZoneName](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#timezonename)
         */
        timeZoneName?: string;
        /**
         * Time period display format. The value can be:
         *
         * "long", "short", "narrow", or  "auto".
         *
         * For details about their display effects, see
         * [Table 10](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.dayPeriod](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#dayperiod)
         */
        dayPeriod?: string;
        /**
         * Locale matching algorithm. The value can be:
         *
         * - "lookup": exact match.
         * - "best fit": best match.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.localeMatcher](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#localematcher)
         */
        localeMatcher?: string;
        /**
         * Format matching algorithm. The value can be:
         *
         * - "basic": exact match.
         * - "best fit": best match.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormatOptions.formatMatcher](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#formatmatcher)
         */
        formatMatcher?: string;
    }
    /**
     * Performs date and time formatting.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @form [since 11]
     * @atomicservice [since 12]
     * @since 6
     * @deprecated since 20
     * @useinstead [Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)
     */
    export class DateTimeFormat {
        /**
         * Creates a **DateTimeOptions** object for the specified locale.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat)
         */
        constructor();
        /**
         * Creates a **DateTimeOptions** object for the specified locale.
         *
         * @param { string | Array<string> } locale - Locale ID or locale ID array. If the input is a locale ID array, the
         *     first valid locale ID is used.
         * @param { DateTimeOptions } [options] - Options for creating the **DateTimeOptions** object.
         * If no options are set, the default values of **year**, **month**, and **day** are **numeric**.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat)
         */
        constructor(locale: string | Array<string>, options?: DateTimeOptions);
        /**
         * Formats the date and time.
         *
         * @param { Date } date - Date and time. Note: The month starts from **0**. For example, **0** indicates January.
         * @returns { string } A string containing the formatted date and time.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormat.format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/format)
         */
        format(date: Date): string;
        /**
         * Formats date and time ranges.
         *
         * @param { Date } startDate - Start date and time. Note: The month starts from **0**. For example, **0** indicates
         *     January.
         * @param { Date } endDate - End date and time. Note: The month starts from **0**. For example, **0** indicates
         *     January.
         * @returns { string } A string containing the formatted date and time ranges.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormat.formatRange](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/formatRange)
         */
        formatRange(startDate: Date, endDate: Date): string;
        /**
         * Obtains the options for creating a **DateTimeOptions** object.
         *
         * @returns { DateTimeOptions } Options for the **DateTimeOptions** object.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @form [since 11]
         * @atomicservice [since 12]
         * @since 6
         * @deprecated since 20
         * @useinstead [Intl.DateTimeFormat.resolvedOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions)
         */
        resolvedOptions(): DateTimeOptions;
    }
    /**
     * Options for creating the **NumberFormat** object. Since API version 9, the **NumberOptions** attribute is changed
     * from mandatory to optional.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 6
     */
    export interface NumberOptions {
        /**
         * Valid locale ID, for example, **zh-Hans-CN**.
         *
         * The default value is the current system locale.
         *
         * This API can be used in atomic services since API version 12.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        locale?: string;
        /**
         * Currency unit. The value must comply with the
         * [ISO-4217 standard](https://www.iso.org/iso-4217-currency-codes.html), for example, EUR, CNY, and USD.
         *
         * From API version 12, a three-digit number is supported, for example, **978**, **156**, or **840**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        currency?: string;
        /**
         * Currency unit symbol. The value can be **standard** or **accounting**.
         *
         * The default value is **standard**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * For details about their display effects, see
         * [Table 19](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        currencySign?: string;
        /**
         * Currency display mode. The value can be **symbol**, **narrowSymbol**, **code**, or **name**.
         *
         * The default value is **symbol**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * For details about their display effects, see
         * [Table 20](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        currencyDisplay?: string;
        /**
         * Unit name, for example, **meter**, **inch**, or **hectare**.
         *
         * The combination units supported since API version 18 are as follows: beat-per-minute, body-weight-per-second,
         * breath-per-minute, foot-per-hour, jump-rope-per-minute, meter-per-hour, milliliter-per-minute-per-kilogram,
         * rotation-per-minute, step-per-minute, and stroke-per-minute.
         *
         * This API can be used in atomic services since API version 12.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        unit?: string;
        /**
         * Display format of units. The value can be **long**, **short**, or **narrow**.
         *
         * The default value is **short**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * For details about their display effects, see
         * [Table 21](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        unitDisplay?: string;
        /**
         * Application scenario of units. The value can be any of the following: **default**, **area-land-agricult**, **area-
         * land-commercl**, **area-land-residntl**, **length-person**, **length-person-small**, **length-rainfall**, **
         * length-road**, **length-road-small**, **length-snowfall**, **length-vehicle**, **length-visiblty**, **length-
         * visiblty-small**, **length-person-informal**, **length-person-small-informal**, **length-road-informal**, **speed
         * -road-travel**, **speed-wind**, **temperature-person**, **temperature-weather**, **volume-vehicle-fuel**, **
         * elapsed-time-second**, **size-file-byte**, or **size-shortfile-byte**.
         *
         * The default value is **default**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * For details about their display effects, see
         * [Table 22](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 8 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        unitUsage?: string;
        /**
         * Number sign display format. The value can be:
         *
         * - "auto": automatically determines whether to display the plus or minus sign.
         * - "never": do not display the plus or minus sign.
         * - "always": always displays the plus or minus sign.
         * - "exceptZero": displays the plus or minus sign for all values except 0.
         *
         * Default value: **"auto"**
         *
         * This API can be used in atomic services since API version 12.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        signDisplay?: string;
        /**
         * Compact display format. The value can be **long** or **short**.
         *
         * The default value is **short**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * For details about their display effects, see
         * [Table 18](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        compactDisplay?: string;
        /**
         * Number notation. The value can be **standard**, **scientific**, **engineering**, or **compact**.
         *
         * The default value is **standard**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * For details about their display effects, see
         * [Table 17](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        notation?: string;
        /**
         * Locale matching algorithm. The value can be **lookup** or **best fit**.
         *
         * The default value is **best fit**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        localeMatcher?: string;
        /**
         * Number display format. The value can be **decimal**, **currency**, **percent**, or **unit**.
         *
         * The default value is **decimal**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        style?: string;
        /**
         * Numbering system. The value can be:
         *
         * **adlm**, **ahom**, **arab**, **arabext**, **bali**, **beng**, **bhks**, **brah**, **cakm**, **cham**, **deva**,
         * **diak**, **fullwide**, **gong**, **gonm**, **gujr**, **guru**, **hanidec**, **hmng**, **hmnp**, **java**,
         * **kali**, **khmr**, **knda**, **lana**, **lanatham**, **laoo**, **latn**, **lepc**, **limb**, **mathbold**,
         * **mathdbl**, **mathmono**, **mathsanb**, **mathsans**, **mlym**, **modi**, **mong**, **mroo**, **mtei**, **mymr**
         * , **mymrshan**, **mymrtlng**, **newa**, **nkoo**, **olck**, **orya**, **osma**, **rohg**, **saur**, **segment**,
         * **shrd**, **sind**, **sinh**, **sora**, **sund**, **takr**, **talu**, **tamldec**, **telu**, **thai**, **tibt**,
         * **tirh**, **vaii**, **wara**, or **wcho**.
         *
         * The default value is the default numbering system of the locale.
         *
         * This API can be used in atomic services since API version 12.
         *
         * @type { string } [since 6 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        numberingSystem?: string;
        /**
         * Whether to enable grouping for display. The value **true** means to enable grouping for display, and the value
         * **false** means the opposite.
         *
         * The default value is **true**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * For details about their display effects, see
         * [Table 16](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { boolean } [since 6 - 8]
         * @type { ?boolean } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        useGrouping?: boolean;
        /**
         * Minimum number of digits allowed in the integer part of a number. The value ranges from **1** to **21**.
         *
         * The default value is **1**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * For details about their display effects, see
         * [Table 11](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { number } [since 6 - 8]
         * @type { ?number } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        minimumIntegerDigits?: number;
        /**
         * Minimum number of digits in the fraction part of a number. The value ranges from **0** to **20**.
         *
         * The default value is **0**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * For details about their display effects, see
         * [Table 12](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { number } [since 6 - 8]
         * @type { ?number } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        minimumFractionDigits?: number;
        /**
         * Maximum number of digits in the fraction part of a number. The value ranges from **1** to **21**.
         *
         * The default value is **3**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * For details about their display effects, see
         * [Table 13](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { number } [since 6 - 8]
         * @type { ?number } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        maximumFractionDigits?: number;
        /**
         * Minimum number of the least significant digits. The value ranges from **1** to **21**.
         *
         * The default value is **1**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * For details about their display effects, see
         * [Table 14](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { number } [since 6 - 8]
         * @type { ?number } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        minimumSignificantDigits?: number;
        /**
         * Maximum number of the least significant digits. The value ranges from **1** to **21**.
         *
         * The default value is **21**.
         *
         * This API can be used in atomic services since API version 12.
         *
         * For details about their display effects, see
         * [Table 15](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { number } [since 6 - 8]
         * @type { ?number } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        maximumSignificantDigits?: number;
        /**
         * Rounding priority used when both the maximum number of fraction digits and the maximum number of valid digits are
         * set. The value can be **auto**, **morePrecision**, or **lessPrecision**. The value **morePrecision** indicates
         * that the maximum number of fraction digits is used. The value **lessPrecision** indicates that the maximum number
         * of valid digits is used.
         *
         * The default value is **auto**.
         *
         * This API can be used in atomic services since API version 18.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 18
         */
        roundingPriority?: string;
        /**
         * Rounding increment. The value can be **1**, **2**, **5**, **10**, **20**, **25**, **50**, **100**, **200**,
         * **250**, **500**, **1000**, **2000**, **2500**, or **5000**.
         *
         * The default value is **1**.
         *
         * This API can be used in atomic services since API version 18.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 18
         */
        roundingIncrement?: number;
        /**
         * Rounding mode. The value can be:
         *
         * - **ceil**: rounding up.
         * - **floor**: rounding down.
         * - **expand**: rounding away from 0.
         * - **trunc**: rounding toward 0.
         * - **halfCeil**: half-rounding up; that is, rounding up when the decimal number is greater than or equal to half
         * of the increment, and rounding down otherwise.
         * - **halfFloor**: half-rounding down; that is, rounding up when the decimal number is greater than half of the
         * increment, and rounding down otherwise.
         * - **halfExpand**: half-rounding away from 0; that is, rounding away from 0 when the decimal number is greater
         * than or equal to half of the increment, and rounding toward 0 otherwise.
         * - **halfTrunc**: half-rounding toward 0; that is, rounding away from 0 when the decimal number is greater than
         * half of the increment, and rounding toward 0 otherwise.
         * - "halfEven": half-rounding to the nearest even number; that is, rounding away from 0 when the decimal number is
         * greater than half of the increment, rounding toward 0 when the decimal number is less than half of the increment,
         * and rounding to the nearest even number when the decimal number is exactly half of the increment.
         *
         * The default value is **halfExpand**.
         *
         * This API can be used in atomic services since API version 18.
         *
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 18
         */
        roundingMode?: string;
    }
    /**
     * Provides the API for formatting number strings.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 6
     */
    export class NumberFormat {
        /**
         * Creates a **NumberFormat** object for the current system locale.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        constructor();
        /**
         * Creates a **NumberFormat** object based on the specified locale and options.
         *
         * @param { string | Array<string> } locale - Locale ID or locale ID array. If the input is a locale ID array, the
         *     first valid locale ID is used.
         * @param { NumberOptions } [options] - Options for creating the **NumberFormat** object.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        constructor(locale: string | Array<string>, options?: NumberOptions);
        /**
         * Formats a number.
         *
         * @param { number } number Indicates the number to be formatted. [since 6 - 11]
         * @param { number } num - Number to be formatted. [since 12]
         * @returns { string } Formatted number.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        format(num: number): string;
        /**
         * Formats a number range.
         *
         * @param { number } startRange - Start number.
         * @param { number } endRange - End number.
         * @returns { string } Formatted number range.
         * @syscap SystemCapability.Global.I18n
         * @atomicservice
         * @since 18
         */
        formatRange(startRange: number, endRange: number): string;
        /**
         * Obtains the options for creating a **NumberFormat** object.
         *
         * @returns { NumberOptions } Options for creating the **NumberFormat** object.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 6
         */
        resolvedOptions(): NumberOptions;
    }
    /**
     * Defines the options for creating a **Collator** object.
     * Since API version 9, the attributes in **CollatorOptions** are optional.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    export interface CollatorOptions {
        /**
         * Locale matching algorithm. The options are as follows:
         *
         * **lookup**: fuzzy match.
         *
         * **best fit**: exact match.
         *
         * The default value is **best fit**.
         *
         * @type { string } [since 8 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        localeMatcher?: string;
        /**
         * Purpose of comparison. The options are as follows:
         *
         * - **sort**: sorting.
         * - **search**: search for matched strings.
         *
         * The default value is **sort**.
         *
         * @type { string } [since 8 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        usage?: string;
        /**
         * Differences in the strings that lead to non-zero return values. The options are as follows:
         *
         * - **base**: Different letters are considered unequal, for example, 'a' ≠ 'b', 'a' = 'á', 'a' = 'A'.
         * - **accent**: Different letters or same letters with different pronunciations are considered unequal, for example
         * , 'a' ≠ 'b', 'a' ≠ 'á', 'a' = 'A'.
         * - **case**: Different letters or same letters with different cases are considered unequal, for example, 'a' ≠ 'b'
         * , 'a' = 'á', 'a' ≠ 'A'.
         * - **variant**: Different letters, pronunciations, other distinguishing marks, or cases are all considered unequal
         * , for example, 'a' ≠ 'b', 'a' ≠ 'á', 'a' ≠ 'A'.
         *
         * The default value is **variant**.
         *
         * @type { string } [since 8 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        sensitivity?: string;
        /**
         * Whether to ignore punctuation. The value **true** means to ignore punctuation, and the value **false** means the
         * opposite.
         *
         * The default value is **false**.
         *
         * @type { boolean } [since 8 - 8]
         * @type { ?boolean } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        ignorePunctuation?: boolean;
        /**
         * Collation rules for the locale. The value can be:
         *
         * **big5han**: Pinyin sorting for Latin letters.
         *
         * **compat**: compatibility sorting, only for Arabic.
         *
         * **dict**: dictionary-style sorting, only for Singhalese.
         *
         * **direct**: binary code point sorting.
         *
         * **ducet**: sorting according to the Unicode collation element table.
         *
         * **eor**: sorting according to the European collation rules.
         *
         * **gb2312**: Pinyin sorting, only for Chinese.
         *
         * **phonebk**: phone book-style sorting.
         *
         * **phonetic**: phonetic sorting.
         *
         * **pinyin**: Pinyin sorting.
         *
         * **reformed**: reformed sorting, only for Swedish.
         *
         * **searchjl**: special sorting for Korean initial consonant search.
         *
         * **stroke**: stroke sorting for Chinese.
         *
         * **trad**: traditional-style sorting, for example, Spanish.
         *
         * **unihan**: radical-stroke sorting for Han characters, only for Chinese, Japanese, and Korean.
         *
         * **zhuyin**: Zhuyin sorting, only for Chinese.
         *
         * The default value is **default**.
         *
         * @type { string } [since 8 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        collation?: string;
        /**
         * Whether numeric sorting is used. The options are as follows:
         *
         * - **true**: Numeric sorting is used. For example, '1' < '2' < '10' < '11'.
         * - **false**: Numeric sorting is not used. For example, '1' < '10' < '11' < '2'.
         *
         * The default value is **false**.
         *
         * @type { boolean } [since 8 - 8]
         * @type { ?boolean } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        numeric?: boolean;
        /**
         * Whether case is taken into account for the locale's collation rules. The value can be:
         *
         * **upper**: Uppercase letters come first.
         *
         * **lower**: Lowercase letters come first.
         *
         * - **false**: The default collation rules of the locale are used.
         *
         * The default value is **false**.
         *
         * @type { string } [since 8 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        caseFirst?: string;
    }
    /**
     * Provides the string collation capability.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    export class Collator {
        /**
         * Creates a **Collator** object for the current system locale.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        constructor();
        /**
         * Creates a **Collator** object based on the specified locale and options.
         *
         * @param { string | Array<string> } locale - Locale ID or locale ID array. If the input is a locale ID array, the
         *     first valid locale ID is used.
         * @param { CollatorOptions } [options] - Options for creating a **Collator** object.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        constructor(locale: string | Array<string>, options?: CollatorOptions);
        /**
         * Compares two strings based on the specified collation rules.
         *
         * @param { string } first - First string to compare.
         * @param { string } second - Second string to compare.
         * @returns { number } Comparison result.
         *     - If the value is a negative number, the first string comes before the second string.
         *     - If the value is **0**, the first and second strings are in the same sequence.
         *     - If the value is a positive number, the first string is comes after the second string.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        compare(first: string, second: string): number;
        /**
         * Obtains the options for creating a **Collator** object.
         *
         * @returns { CollatorOptions } Options for creating a **Collator** object.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        resolvedOptions(): CollatorOptions;
    }
    /**
     * Defines the options for creating a **PluralRules** object. Since API version 9, the **PluralRulesOptions**
     * attribute is changed from mandatory to optional.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     * @deprecated since 20
     * @useinstead [Intl.PluralRulesOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#options)
     */
    export interface PluralRulesOptions {
        /**
         * Locale matching algorithm. The value can be **lookup** or **best fit**.
         *
         * The default value is **best fit**.
         *
         * @type { string } [since 8 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.PluralRulesOptions.localeMatcher](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#localematcher)
         */
        localeMatcher?: string;
        /**
         * Collation type. The value can be **cardinal** or **ordinal**.
         *
         * The default value is **cardinal**.
         *
         * The value **cardinal** indicates a cardinal number and the value **ordinal** indicates an ordinal number.
         *
         * @type { string } [since 8 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.PluralRulesOptions.type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#type)
         */
        type?: string;
        /**
         * Minimum number of digits allowed in the integer part of a number. The value ranges from **1** to **21**.
         *
         * The default value is **1**.
         *
         * @type { number } [since 8 - 8]
         * @type { ?number } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.PluralRulesOptions.minimumIntegerDigits](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#minimumintegerdigits)
         */
        minimumIntegerDigits?: number;
        /**
         * Minimum number of digits in the fraction part of a number. The value ranges from **0** to **20**.
         *
         * The default value is **0**.
         *
         * @type { number } [since 8 - 8]
         * @type { ?number } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.PluralRulesOptions.minimumFractionDigits](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#minimumfractiondigits)
         */
        minimumFractionDigits?: number;
        /**
         * Maximum number of digits in the fraction part of a number. The value ranges from **1** to **21**.
         *
         * The default value is **3**.
         *
         * @type { number } [since 8 - 8]
         * @type { ?number } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.PluralRulesOptions.maximumFractionDigits](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#maximumfractiondigits)
         */
        maximumFractionDigits?: number;
        /**
         * Minimum number of the least significant digits. The value ranges from **1** to **21**.
         *
         * The default value is **1**.
         *
         * @type { number } [since 8 - 8]
         * @type { ?number } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.PluralRulesOptions.minimumSignificantDigits](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#minimumsignificantdigits)
         */
        minimumSignificantDigits?: number;
        /**
         * Maximum number of the least significant digits. The value ranges from **1** to **21**.
         *
         * The default value is **21**.
         *
         * @type { number } [since 8 - 8]
         * @type { ?number } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.PluralRulesOptions.maximumSignificantDigits](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#maximumsignificantdigits)
         */
        maximumSignificantDigits?: number;
    }
    /**
     * Provides the capability for obtaining the plural rule type.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     * @deprecated since 20
     * @useinstead [Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules)
     */
    export class PluralRules {
        /**
         * Creates a **PluralRules** object to obtain the singular-plural type of numbers.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules)
         */
        constructor();
        /**
         * Creates a **PluralRules** object to obtain the singular-plural type of numbers.
         *
         * @param { string | Array<string> } locale - Locale ID or locale ID array. If the input is a locale ID array, the
         *     first valid locale ID is used.
         * @param { PluralRulesOptions } [options] - Options for creating a **PluralRules** object.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules)
         */
        constructor(locale: string | Array<string>, options?: PluralRulesOptions);
        /**
         * Obtains the singular-plural type of the specified number.
         *
         * @param { number } n - Number for which the singular-plural type is to be obtained.
         * @returns { string } Singular-plural type. The value can be any of the following: **zero**, **one**, **two**,
         *     **few**, **many**, **others**.
         *     For details about the meanings of different values, see
         *     [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.PluralRules.select](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/select)
         */
        select(n: number): string;
    }
    /**
     * Defines the configuration options for a **RelativeTimeFormat** object.
     * Since API version 9, the attributes in **RelativeTimeFormatInputOptions** are optional.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     * @deprecated since 20
     * @useinstead [Intl.RelativeTimeFormatOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#options)
     */
    export interface RelativeTimeFormatInputOptions {
        /**
         * Locale matching algorithm. The value can be **lookup** or **best fit**.
         *
         * The default value is **best fit**.
         *
         * @type { string } [since 8 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.RelativeTimeFormatOptions.localeMatcher](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#localematcher)
         */
        localeMatcher?: string;
        /**
         * Format of the output result. It determines whether numeric values are used to represent relative dates or times
         * in the formatting result. The value can be **always** or **auto**.
         *
         * The default value is **always**.
         *
         * For details about their display effects, see
         * [Table 23](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @type { string } [since 8 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.RelativeTimeFormatOptions.numeric](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#numeric)
         */
        numeric?: string;
        /**
         * Length of an internationalized message. The value can be **long**, **short**, or **narrow**.
         *
         * The default value is **long**.
         *
         * @type { string } [since 8 - 8]
         * @type { ?string } [since 9]
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.RelativeTimeFormatOptions.style](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#style)
         */
        style?: string;
    }
    /**
     * Represents the formatting options for the **RelativeTimeFormat** object.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     * @deprecated since 20
     * @useinstead [Intl.ResolvedRelativeTimeFormatOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions#return_value)
     */
    export interface RelativeTimeFormatResolvedOptions {
        /**
         * Locale ID, including the language, script, and region.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.ResolvedRelativeTimeFormatOptions.locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions#locale)
         */
        locale: string;
        /**
         * Length of an internationalized message. The value can be **long**, **short**, or **narrow**.
         *
         * For details about their display effects, see
         * [Table 24](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.ResolvedRelativeTimeFormatOptions.style](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions#style)
         */
        style: string;
        /**
         * Format of the output result. It determines whether numeric values are used to represent relative dates or times
         * in the formatting result. The value can be **always** or **auto**.
         *
         * For details about their display effects, see
         * [Table 23](docroot://reference/apis-localization-kit/js-apis-intl.md#appendix).
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.ResolvedRelativeTimeFormatOptions.numeric](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions#numeric)
         */
        numeric: string;
        /**
         * Numbering system. The value can be:
         *
         * **adlm**, **ahom**, **arab**, **arabext**, **bali**, **beng**, **bhks**, **brah**, **cakm**, **cham**, **deva**,
         * **diak**, **fullwide**, **gong**, **gonm**, **gujr**, **guru**, **hanidec**, **hmng**, **hmnp**, **java**,
         * **kali**, **khmr**, **knda**, **lana**, **lanatham**, **laoo**, **latn**, **lepc**, **limb**, **mathbold**,
         * **mathdbl**, **mathmono**, **mathsanb**, **mathsans**, **mlym**, **modi**, **mong**, **mroo**, **mtei**, **mymr**
         * , **mymrshan**, **mymrtlng**, **newa**, **nkoo**, **olck**, **orya**, **osma**, **rohg**, **saur**, **segment**,
         * **shrd**, **sind**, **sinh**, **sora**, **sund**, **takr**, **talu**, **tamldec**, **telu**, **thai**, **tibt**,
         * **tirh**, **vaii**, **wara**, or **wcho**.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.ResolvedRelativeTimeFormatOptions.numberingSystem](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions#numberingsystem)
         */
        numberingSystem: string;
    }
    /**
     * Provides the relative time formatting capability.
     *
     * @syscap SystemCapability.Global.I18n
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     * @deprecated since 20
     * @useinstead [Intl.RelativeTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)
     */
    export class RelativeTimeFormat {
        /**
         * Creates a **RelativeTimeFormat** object.
         *
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.RelativeTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat)
         */
        constructor();
        /**
         * Creates a **RelativeTimeFormat** object.
         *
         * @param { string | Array<string> } locale - Locale ID or locale ID array. If the input is a locale ID array, the
         *     first valid locale ID is used.
         * @param { RelativeTimeFormatInputOptions } [options] - Options for creating a **RelativeTimeFormat** object.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.RelativeTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat)
         */
        constructor(locale: string | Array<string>, options?: RelativeTimeFormatInputOptions);
        /**
         * Formats a relative time.
         *
         * @param { number } value - Value to format.
         * @param { string } unit - Unit of the relative time.
         *   The value can be any of the following: **year**,
         *     **quarter**, **month**, **week**, **day**, **hour**, **minute**, or **second**.
         * @returns { string } Relative time after formatting.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.RelativeTimeFormat.format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format)
         */
        format(value: number, unit: string): string;
        /**
         * Formats the relative time
         *
         * @param { number } value - Value to format.
         * @param { string } unit - Unit of the relative time.
         *     The value can be any of the following: **year**,
         *     **quarter**, **month**, **week**, **day**, **hour**, **minute**, or **second**.
         * @returns { Array<object> } Components of the formatted result.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.RelativeTimeFormat.formatToParts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/formatToParts)
         */
        formatToParts(value: number, unit: string): Array<object>;
        /**
         * Defines the formatting options for a **RelativeTimeFormat** object.
         *
         * @returns { RelativeTimeFormatResolvedOptions } Options for the **RelativeTimeFormat** object.
         * @syscap SystemCapability.Global.I18n
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 20
         * @useinstead [Intl.RelativeTimeFormat.resolvedOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions)
         */
        resolvedOptions(): RelativeTimeFormatResolvedOptions;
    }
}
export default intl;

```
