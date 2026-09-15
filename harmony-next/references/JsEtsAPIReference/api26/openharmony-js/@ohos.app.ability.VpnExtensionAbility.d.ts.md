# @ohos.app.ability.VpnExtensionAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
 * @kit NetworkKit
 */
import type VpnExtensionContext from './application/VpnExtensionContext';
import type Want from './@ohos.app.ability.Want';
/**
 * **VpnExtensionContext** represents the context of **VpnExtensionAbility** and is inherited from
 * [ExtensionContext]{@link ./application/ExtensionContext:ExtensionContext}.
 *
 * This module provides the context required for APIs to access the resources of a **VpnExtensionAbility** object.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @since 11
 */
export default class VpnExtensionAbility {
    /**
     * Specified context.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    context: VpnExtensionContext;
    /**
     * Represents the callback triggered when the extended VPN is initialized.
     *
     * > **NOTE**
     * >
     * > You are advised to call [onDestroy]{@link VpnExtensionAbility#onDestroy} to listen to the destruction of the
     * > extended VPN and clear resources in a timely manner.
     *
     * @param { Want } want - Want information.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    onCreate(want: Want): void;
    /**
     * Represents the callback triggered when the extended VPN is destroyed.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    onDestroy(): void;
}

```
