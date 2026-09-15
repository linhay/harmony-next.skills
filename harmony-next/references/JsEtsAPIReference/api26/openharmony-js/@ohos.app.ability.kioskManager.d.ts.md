# @ohos.app.ability.kioskManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
import UIAbilityContext from './application/UIAbilityContext';
import { KioskStatus as _KioskStatus } from './application/KioskStatus';
/**
 * The KioskManager module provides APIs to manage kiosk mode, including entering/exiting kiosk mode and querying the
 * kiosk mode status.
 *
 * Kiosk mode is a dedicated device lockdown mode that ensures the device UI serves only specific interaction scenarios.
 * In this mode, device usage is confined to predetermined applications. A typical example is a bank ATM, where users
 * can only interact with the ATM software and cannot exit it or access any other functions.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @since 20
 */
declare namespace kioskManager {
    /**
     * Enters kiosk mode. This API uses a promise to return the result.
     * This API can be properly called only on phones, PC/2-in-1 devices, and tablets. On other devices, it returns the
     * error code 801.
     *
     * @param { UIAbilityContext } context - Context of the UIAbility that needs to enter kiosk mode.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 16000050 - Failed to connect to the system service.
     * @throws { BusinessError } 16000110 - The current application is not in Kiosk app list and cannot enter Kiosk mode.
     * @throws { BusinessError } 16000111 - The system is already in Kiosk mode and cannot enter Kiosk mode again.
     * @throws { BusinessError } 16000113 - Current ability is not in foreground.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 20
     */
    function enterKioskMode(context: UIAbilityContext): Promise<void>;
    /**
     * Exits kiosk mode. This API uses a promise to return the result.
     * This API takes effect only for applications that have entered kiosk mode.
     * This API can be properly called only on phones, PC/2-in-1 devices, and tablets. On other devices, it returns the
     * error code 801.
     *
     * @param { UIAbilityContext } context - Context of the UIAbility that needs to exit kiosk mode.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 16000050 - Failed to connect to the system service.
     * @throws { BusinessError } 16000110 - The current application is not in Kiosk app list and cannot enter Kiosk mode.
     * @throws { BusinessError } 16000112 - The current application is not in Kiosk mode and cannot exit Kiosk mode.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 20
     */
    function exitKioskMode(context: UIAbilityContext): Promise<void>;
    /**
     * Defines the kiosk status information, including whether the system is in kiosk mode and the information about the
     * application in kiosk mode.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 20
     */
    export type KioskStatus = _KioskStatus;
}
export default kioskManager;

```
