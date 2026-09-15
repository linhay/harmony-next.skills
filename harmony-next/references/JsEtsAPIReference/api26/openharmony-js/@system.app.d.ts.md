# @system.app.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2020 Huawei Device Co., Ltd.
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
 * @kit ArkUI
 */
/**
 * Defines the application response information.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Lite
 * @FaAndStageModel
 * @atomicservice [since 12]
 * @since 3
 */
export interface AppResponse {
    /**
     * Bundle name of an application. It uniquely identifies the application.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @atomicservice [since 12]
     * @since 6
     */
    appID: string;
    /**
     * Application name.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Lite
     * @FaAndStageModel
     * @atomicservice [since 12]
     * @since 3
     */
    appName: string;
    /**
     * Application version name.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Lite
     * @FaAndStageModel
     * @atomicservice [since 12]
     * @since 3
     */
    versionName: string;
    /**
     * Application version number.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Lite
     * @FaAndStageModel
     * @atomicservice [since 12]
     * @since 3
     */
    versionCode: number;
}
/**
 * Defines the options of the visible interface on the screen.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @FaAndStageModel
 * @atomicservice [since 11]
 * @since 3
 */
export interface ScreenOnVisibleOptions {
    /**
     * Whether to keep the application visible. The default value is **false**.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @atomicservice [since 11]
     * @since 3
     */
    visible?: boolean;
    /**
     * Callback upon success.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @atomicservice [since 11]
     * @since 3
     */
    success?: () => void;
    /**
     * Callback upon failure.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @atomicservice [since 11]
     * @since 3
     */
    fail?: (data: string, code: number) => void;
    /**
     * Called when the API call is complete.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @atomicservice [since 11]
     * @since 3
     */
    complete?: () => void;
}
/**
 * Defines the option of RequestFullWindow interface.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @FaAndStageModel
 * @atomicservice [since 11]
 * @since 3
 */
export interface RequestFullWindowOptions {
    /**
     * Defines the number of animation options.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @atomicservice [since 11]
     * @since 3
     */
    duration: number;
}
/**
 * Defines static functions of App class
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Lite
 * @FaAndStageModel
 * @atomicservice [since 12]
 * @since 3
 */
export default class App {
    /**
     * Obtains the declared information in the **config.json** file of an application. In the stage model, this API
     * returns **null**.
     *
     * This API is deprecated since API version 9. You are advised to use
     * [bundleManager.getBundleInfoForSelf]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoForSelf(bundleFlags: number)}
     * instead.
     *
     * @returns { AppResponse } Application response information.
     * @syscap SystemCapability.ArkUI.ArkUI.Lite
     * @FaAndStageModel
     * @atomicservice [since 12]
     * @since 3
     */
    static getInfo(): AppResponse;
    /**
     * Terminates the current ability. In the stage model, this API has no effect.
     *
     * This API is deprecated since API version 7. You are advised to use
     * [@ohos.ability.featureAbility]{@link @ohos.ability.featureAbility:featureAbility} instead.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Lite
     * @FaAndStageModel
     * @atomicservice [since 12]
     * @since 3
     */
    static terminate(): void;
    /**
     * Defines whether to keep the application visible when the screen is woken up.
     *
     * This API is deprecated since API version 8.
     *
     * @param { ScreenOnVisibleOptions } options - With keep-alive, the system is prevented from returning to the home
     *     screen when the screen is locked, so that the application is visible when the screen is woken up.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 3
     * @deprecated since 8
     */
    static screenOnVisible(options?: ScreenOnVisibleOptions): void;
    /**
     * Requests the application to run in full window.
     * In some scenarios, such as semi-modal FA, the FA runs in non-full window.
     * In this case, you can call this API.
     * This API is invalid for an application already in full-window mode.
     *
     * @param { RequestFullWindowOptions } options Transition time from non-full window to full window, in milliseconds.
     * By default, the value is in direct proportion to the distance between the non-full window and the full window.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 3
     * @deprecated since 8
     * @useinstead startAbility
     */
    static requestFullWindow(options?: RequestFullWindowOptions): void;
    /**
     * Set image cache capacity of decoded image count.
     * if not set, the application will not cache any decoded image.
     *
     * @param { number } value - capacity of decoded image count.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @atomicservice [since 12]
     * @since 7
     */
    static setImageCacheCount(value: number): void;
    /**
     * Set image cache capacity of raw image data size in bytes before decode.
     * if not set, the application will not cache any raw image data.
     *
     * @param { number } value - capacity of raw image data size in bytes.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @atomicservice [since 12]
     * @since 7
     */
    static setImageRawDataCacheSize(value: number): void;
    /**
     * Set image file cache size in bytes on disk before decode.
     * if not set, the application will cache 100MB image files on disk.
     *
     * @param { number } value - capacity of raw image data size in bytes.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @atomicservice [since 12]
     * @since 7
     */
    static setImageFileCacheSize(value: number): void;
}

```
