# @ohos.app.ability.hyperSnapManager.d.ts

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
 * @kit AbilityKit
 */
/**
 * This module provides the capability to manage HyperSnap.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @since 24
 */
declare namespace hyperSnapManager {
    /**
     * Enables or disables the Hyper Snap performance optimization for the application.
     *
     * When enabled, the system will create a snapshot of the application process at an appropriate time.
     * Subsequent launched resume directly from this snapshot, bypassing the full cold start sequence,
     * resulting in significantly improved application launch performance.
     *
     * **Notes:**
     * - The system ultimately determines whether to create or use snapshots based on
     *   application compatibility, resource availability, and system policies. Enabling this feature only
     *   indicates the application's readiness for optimization.
     * - Hyper Snap is enabled by default for applications meeting system compatibility requirements.
     * - If issues arise after enabling Hyper Snap, disable this feature to revert
     *   to standard cold start processes.
     * - Settings persist across reboots.
     *
     * @param { boolean } enableFlag - Indicates the desired optimization state:
     *     - `true`: Indicates the application's compatibility with Hyper Snap optimization (system may
     *               apply when appropriate)
     *     - `false`: Disables Hyper Snap; uses standard cold-start process.
     * @throws { BusinessError } 16000150 - Failed to send request to system service.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 24
     */
    function setHyperSnapEnabled(enableFlag: boolean): void;
    /**
     * Requests the recreation of the Hyper Snap process snapshot for the application.
     *
     * When compatibility issues arise with an existing snapshot, this method triggers destruction of the current
     * snapshot process. The system will subsequently generate a new snapshot at an optimal time to resolve
     * compatibility problems while maintaining launch performance benefits.
     *
     * **Notes:**
     * - The system ultimately determines whether and when to recreate the snapshot. Invoking this method only submits
     *   a request; actual snapshot recreation depends on system policies and resource availability.
     * - Recreation occurs during optimal system idle periods to minimize performance impact.
     * - Primarily for resolving specific compatibility issues identified after initial snapshot creation.
     *   Most applications don't require manual intervention for snapshot management.
     *
     * @throws { BusinessError } 16000150 -  Failed to send request to system service.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 24
     */
    function requestRebuildHyperSnap(): void;
}
export default hyperSnapManager;

```
