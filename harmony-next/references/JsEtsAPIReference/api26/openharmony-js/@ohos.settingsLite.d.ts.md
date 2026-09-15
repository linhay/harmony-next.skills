# @ohos.settingsLite.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
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
 * @kit BasicServicesKit
 */
/**
 * Defines the lite settings capability for wearables.
 *
 * @syscap SystemCapability.Applications.Settings.Core.Lite
 * @famodelonly
 * @since 24
 */
declare namespace settingsLite {
    /**
     * Opens the password settings page.
     *
     * @syscap SystemCapability.Applications.Settings.Core.Lite
     * @famodelonly
     * @since 24
     */
    function openPinSettingPage(): void;
    /**
     * Opens the NFC settings page.
     *
     * @syscap SystemCapability.Applications.Settings.Core.Lite
     * @famodelonly
     * @since 24
     */
    function openNfcSettingsPage(): void;
    /**
     * Opens the settings page for double-pressing the function key.
     *
     * @syscap SystemCapability.Applications.Settings.Core.Lite
     * @famodelonly
     * @since 24
     */
    function openDoubleClickSettingsPage(): void;
    /**
     * Defines a callback used to return whether the application started by double-pressing the function key is the
     * application itself.
     * @syscap SystemCapability.Applications.Settings.Core.Lite
     * @famodelonly
     * @since 24
     */
    interface ClickCallback {
        /**
         * Called to determine whether the application can be started by double-pressing the function key.
         *
         * @param { boolean } result - The specified application is started by double-pressing the function key if
         *     true is returned. Otherwise, an unexpected application is started.
         * @syscap SystemCapability.Applications.Settings.Core.Lite
         * @famodelonly
         * @since 24
         */
        onResult(result: boolean): void;
    }
    /**
     * 1. Checks whether the application started by double-pressing the function key is the application itself.
     * 2. This API is triggered to check whether double-pressing the function key starts the application itself.
     *
     * @param { ClickCallback } callback - Callback used to return the execution result.
     * @syscap SystemCapability.Applications.Settings.Core.Lite
     * @famodelonly
     * @since 24
     */
    function isDoubleClickAppForSelf(callback: ClickCallback): void;
}
export default settingsLite;

```
