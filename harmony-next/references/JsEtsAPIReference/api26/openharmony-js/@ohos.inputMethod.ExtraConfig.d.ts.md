# @ohos.inputMethod.ExtraConfig.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
 * This module manages input method extension information. It enables the ArkUI editor to pass such information to the
 * input method application when the input method is launched. After processing the extension information, the input
 * method application can retrieve the details added by the host application. The total length of the information cannot
 * exceed 32 KB.
 *
 * @file The extra config of edit box.
 * @kit IMEKit
 */
/**
 * Represents the extension information type. The specific type of the parameter depends on its functionality.
 *
 * @unionmember { int } Number.
 * @unionmember { string } String.
 * @unionmember { boolean } Boolean.
 * @syscap SystemCapability.MiscServices.InputMethodFramework
 * @since 22
 */
export type CustomValueType = number | string | boolean;
/**
 * Represents the extension information of an input method.
 *
 * @syscap SystemCapability.MiscServices.InputMethodFramework
 * @since 22
 */
export interface InputMethodExtraConfig {
    /**
     * Input method extension information, which is used to store custom key-value pairs. These key-value pairs can be
     * any configuration information related to the input method, such as user input habits, shortcut key settings,
     * theme colors, and more. The settings are loaded when the input method application is bound to the system,
     * delivering a personalized user experience. The total length of the information cannot exceed 32 KB.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 22
     */
    customSettings: Record<string, CustomValueType>;
}

```
