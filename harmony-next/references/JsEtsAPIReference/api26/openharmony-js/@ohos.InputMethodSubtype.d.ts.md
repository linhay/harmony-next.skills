# @ohos.InputMethodSubtype.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2025 Huawei Device Co., Ltd.
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
 * @kit IMEKit
 */
/**
 * The **InputMethodSubtype** module provides APIs for managing the attributes of input method subtypes. The input
 * method subtype allows the input method to switch to a specific mode or language, for example, the Chinese or English
 * keyboard.
 *
 * @syscap SystemCapability.MiscServices.InputMethodFramework
 * @since 9
 */
export default interface InputMethodSubtype {
    /**
     * Optional. Label of the input method subtype.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    readonly label?: string;
    /**
     * Optional. Label ID of the input method subtype.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    readonly labelId?: number;
    /**
     * Mandatory. Bundle name of the application to which the input method subtype belongs.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    readonly name: string;
    /**
     * Mandatory. ID of the input method subtype.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    readonly id: string;
    /**
     * Optional. Mode of the input method subtype, including **upper** (uppercase) and **lower** (lowercase).
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    readonly mode?: 'upper' | 'lower';
    /**
     * Mandatory. Locale of the input method subtype.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    readonly locale: string;
    /**
     * Mandatory. Language of the input method subtype.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    readonly language: string;
    /**
     * Optional. Icon of the input method subtype. It can be obtained by using **iconId**. This parameter is reserved.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    readonly icon?: string;
    /**
     * Optional. Icon ID of the input method subtype.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    readonly iconId?: number;
    /**
     * Mandatory. Extra information of the input method subtype.
     *
     * **NOTE**
     *
     * - This parameter is optional since API version 10.
     * - This parameter is reserved and currently has no specific meaning.
     *
     * @type { object } [since 9 - 9]
     * @type { ?object } [since 10]
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    extra?: object;
}

```
