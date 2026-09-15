# @ohos.FusionConnectivity.PartnerAgentExtensionAbility.d.ts

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
 * @kit ConnectivityKit
 */
import type PartnerAgentExtensionContext from './@ohos.FusionConnectivity.PartnerAgentExtensionContext';
import ExtensionAbility from './@ohos.app.ability.ExtensionAbility';
/**
 * Partner device address.
 *
 * @typedef { partnerAgent.PartnerDeviceAddress } PartnerDeviceAddress
 * @syscap SystemCapability.Communication.FusionConnectivity.Core
 * @stagemodelonly
 * @since 23
 */
type PartnerDeviceAddress = partnerAgent.PartnerDeviceAddress;
/**
 * The reasons for destroying partner agent extension ability.
 *
 * @typedef { partnerAgent.PartnerAgentExtensionAbilityDestroyReason } PartnerAgentExtensionAbilityDestroyReason
 * @syscap SystemCapability.Communication.FusionConnectivity.Core
 * @stagemodelonly
 * @since 23
 */
type PartnerAgentExtensionAbilityDestroyReason = partnerAgent.PartnerAgentExtensionAbilityDestroyReason;
/**
 * Class for the PartnerAgentExtensionAbility.
 * Applications can use this ability to discover devices.
 *
 * @extends ExtensionAbility
 * @syscap SystemCapability.Communication.FusionConnectivity.Core
 * @stagemodelonly
 * @since 23
 */
export default class PartnerAgentExtensionAbility extends ExtensionAbility {
    /**
     * Context of the PartnerAgentExtensionAbility.
     *
     * @type { PartnerAgentExtensionContext }
     * @syscap SystemCapability.Communication.FusionConnectivity.Core
     * @stagemodelonly
     * @since 23
     */
    context: PartnerAgentExtensionContext;
    /**
     * Called when the PartnerAgentExtensionAbility is to be destroyed.
     * Applications can clean up resources in this callback function.
     *
     * @param { PartnerAgentExtensionAbilityDestroyReason } reason - The reason for Ability destruction.
     * @syscap SystemCapability.Communication.FusionConnectivity.Core
     * @stagemodelonly
     * @since 23
     */
    onDestroyWithReason(reason: PartnerAgentExtensionAbilityDestroyReason): void;
    /**
     * Called when a device is discovered.
     *
     * @param { PartnerDeviceAddress } deviceAddress Address of the discovered device.
     * @syscap SystemCapability.Communication.FusionConnectivity.Core
     * @stagemodelonly
     * @since 23
     */
    onDeviceDiscovered(deviceAddress: PartnerDeviceAddress): void;
}

```
