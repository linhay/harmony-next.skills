# @ohos.intelligentScene.d.ts

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
 * @kit BasicServicesKit
 */
/**
 * This module provides system focus modes and Do Not Disturb data access abilities.
 *
 * @namespace intelligentScene
 * @syscap SystemCapability.Applications.IntelligentScene
 * @stagemodelonly
 * @since 23
 */
declare namespace intelligentScene {
    /**
     * Checks whether Do Not Disturb is enabled on this device.
     * The Do Not Disturb state defines if notifications are allowed to interrupt
     * the user (e.g. via sound & vibration) and is applied globally.
     *
     * @permission ohos.permission.GET_DONOTDISTURB_STATE
     * @returns { Promise<boolean> } Returns whether Do Not Disturb is enabled.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 35200001 - Internal error.
     * @syscap SystemCapability.Applications.IntelligentScene
     * @stagemodelonly
     * @since 23
     */
    function isDoNotDisturbEnabled(): Promise<boolean>;
    /**
     * Checks whether calling bundle is allow notify(e.g. sound & vibration) when system
     * Do Not Disturb is on.
     *
     * @permission ohos.permission.GET_DONOTDISTURB_STATE
     * @returns { Promise<boolean> } Returns whether notify in Do Not Disturb mode is Allowed.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 35200001 - Internal error.
     * @syscap SystemCapability.Applications.IntelligentScene
     * @stagemodelonly
     * @since 23
     */
    function isNotifyAllowedInDoNotDisturb(): Promise<boolean>;
}
export default intelligentScene;

```
