# @ohos.app.ability.autoStartupManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2025 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
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
 * @kit AbilityKit
 */
/**
 * The autoStartupManager module provides APIs for an application to query whether it is configured to start
 * automatically at boot time.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @since 21
 */
declare namespace autoStartupManager {
    /**
     * Checks whether the current application is enabled for automatic startup at boot time. This API uses a promise to
     * return the result.
     * This API can be properly called only on phones, PC/2-in-1 devices, tablets, and wearables. On other devices, it
     * returns the error code 801.
     *
     * @returns { Promise<boolean> } Promise used to return the auto-startup status. **true** if enabled for automatic
     *     startup at boot time, **false** otherwise.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 16000050 - Internal error. Possible causes: 1. Connect to system service failed;
     *     2.System service failed to communicate with dependency module.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 21
     */
    function getAutoStartupStatusForSelf(): Promise<boolean>;
    /**
     * Check whether the current device supports auto startup on this device.
     *
     * @returns { boolean }
     *     - `true`: Device supports auto startup.
     *     - `false`: Device do not support auto startup.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function isAutoStartupSupported(): boolean;
}
export default autoStartupManager;

```
