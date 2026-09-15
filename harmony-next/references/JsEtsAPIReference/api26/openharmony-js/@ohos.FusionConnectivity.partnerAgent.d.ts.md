# @ohos.FusionConnectivity.partnerAgent.d.ts

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
import type common from './@ohos.bluetooth.common';
/**
 * Provides APIs for managing partner agents.
 *
 * @namespace partnerAgent
 * @syscap SystemCapability.Communication.FusionConnectivity.Core
 * @stagemodelonly
 * @since 23
 */
declare namespace partnerAgent {
    /**
     * Checks whether the current device supports the partner agent feature.
     *
     * @returns { boolean } Check result for the support of the partner agent feature.
     * @syscap SystemCapability.Communication.FusionConnectivity.Core
     * @stagemodelonly
     * @since 23
     */
    function isPartnerAgentSupported(): boolean;
    /**
     * Bind the partner device.
     * After successfully binding the device, if the device meets the discovery requirements,
     * the {@link PartnerAgentExtensionAbility} of the application will be launched.
     * - If the {@link DeviceCapability.supportBR} in the capability variable is set to true,
     *   the application's ability will be launched when the device is connected via Bluetooth.
     * - If the {@link DeviceCapability.supportBleAdvertiser} in the capability variable is set to true,
     *   the application's ability will be launched when the device is detected via Bluetooth scanning.
     *
     * Note: The device must be paired first.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { PartnerDeviceAddress } deviceAddress - The address of partner device.
     * @param { DeviceCapability } deviceCapability - The capability of partner device.
     * @param { BusinessCapability } businessCapability - The business capability of application.
     * @param { string } partnerAgentExtensionAbilityName - The name of PartnerAgentExtensionAbility.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 34900003 - The device is not paired.
     * @throws { BusinessError } 34900004 - The device has already been bound to the PartnerAgentExtensionAbility.
     * @throws { BusinessError } 34900005 - Bluetooth disabled.
     * @throws { BusinessError } 34900099 - Internal error.
     * @syscap SystemCapability.Communication.FusionConnectivity.Core
     * @stagemodelonly
     * @since 23
     */
    function bindDevice(deviceAddress: PartnerDeviceAddress, deviceCapability: DeviceCapability, businessCapability: BusinessCapability, partnerAgentExtensionAbilityName: string): Promise<void>;
    /**
     * Unbinds a partner device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { PartnerDeviceAddress } deviceAddress - The address of partner device.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 34900001 - The device is not bound.
     * @throws { BusinessError } 34900099 - Internal error.
     * @syscap SystemCapability.Communication.FusionConnectivity.Core
     * @stagemodelonly
     * @since 23
     */
    function unbindDevice(deviceAddress: PartnerDeviceAddress): Promise<void>;
    /**
     * Checks whether a device is bound to this application.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { PartnerDeviceAddress } deviceAddress - The address of partner device.
     * @returns { boolean } Returns whether the device is bound.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 34900099 - Internal error.
     * @syscap SystemCapability.Communication.FusionConnectivity.Core
     * @stagemodelonly
     * @since 23
     */
    function isDeviceBound(deviceAddress: PartnerDeviceAddress): boolean;
    /**
     * Gets the list of addresses of the bound partner device for this application.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @returns { PartnerDeviceAddress[] } Returns the list of addresses of partner device.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 34900099 - Internal error.
     * @syscap SystemCapability.Communication.FusionConnectivity.Core
     * @stagemodelonly
     * @since 23
     */
    function getBoundDevices(): PartnerDeviceAddress[];
    /**
     * Checks whether device control is enabled.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { PartnerDeviceAddress } deviceAddress - The address of partner device.
     * @returns { boolean } Returns whether the device control is enabled.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 34900099 - Internal error.
     * @syscap SystemCapability.Communication.FusionConnectivity.Core
     * @stagemodelonly
     * @since 23
     */
    function isDeviceControlEnabled(deviceAddress: PartnerDeviceAddress): boolean;
    /**
     * Describes the capability of a partner device.
     *
     * @typedef DeviceCapability
     * @syscap SystemCapability.Communication.FusionConnectivity.Core
     * @stagemodelonly
     * @since 23
     */
    interface DeviceCapability {
        /**
         * Whether the partner device supports the Bluetooth Basic Rate (BR) capability.
         *
         * @type { ?boolean }
         * @syscap SystemCapability.Communication.FusionConnectivity.Core
         * @stagemodelonly
         * @since 23
         */
        supportBR?: boolean;
        /**
         * Whether the partner device supports the Bluetooth Low Energy (BLE) advertiser capability.
         *
         * @type { ?boolean }
         * @syscap SystemCapability.Communication.FusionConnectivity.Core
         * @stagemodelonly
         * @since 23
         */
        supportBleAdvertiser?: boolean;
    }
    /**
     * Describes the business capabilities of the application.
     *
     * @typedef BusinessCapability
     * @syscap SystemCapability.Communication.FusionConnectivity.Core
     * @stagemodelonly
     * @since 23
     */
    interface BusinessCapability {
        /**
         * Indicates whether the application supports media control capability.
         *
         * @type { ?boolean }
         * @syscap SystemCapability.Communication.FusionConnectivity.Core
         * @stagemodelonly
         * @since 23
         */
        supportMediaControl?: boolean;
        /**
         * Indicates whether the application supports telephony control capability.
         *
         * @type { ?boolean }
         * @syscap SystemCapability.Communication.FusionConnectivity.Core
         * @stagemodelonly
         * @since 23
         */
        supportTelephonyControl?: boolean;
    }
    /**
     * Describes the partner device address.
     *
     * @typedef PartnerDeviceAddress
     * @syscap SystemCapability.Communication.FusionConnectivity.Core
     * @stagemodelonly
     * @since 23
     */
    export interface PartnerDeviceAddress {
        /**
         * Bluetooth address of the partner device.
         *
         * @type { ?common.BluetoothAddress }
         * @syscap SystemCapability.Communication.FusionConnectivity.Core
         * @stagemodelonly
         * @since 23
         */
        bluetoothAddress?: common.BluetoothAddress;
    }
    /**
     * The enum of reasons for destroying partner agent extension ability.
     *
     * @enum { number }
     * @syscap SystemCapability.Communication.FusionConnectivity.Core
     * @stagemodelonly
     * @since 23
     */
    export enum PartnerAgentExtensionAbilityDestroyReason {
        /**
         * Unknown reason.
         *
         * @syscap SystemCapability.Communication.FusionConnectivity.Core
         * @stagemodelonly
         * @since 23
         */
        UNKNOWN_REASON = 0,
        /**
         * The user actively disables this ability feature.
         *
         * @syscap SystemCapability.Communication.FusionConnectivity.Core
         * @stagemodelonly
         * @since 23
         */
        USER_CLOSED_ABILITY = 1,
        /**
         * The device is unpaired.
         *
         * @syscap SystemCapability.Communication.FusionConnectivity.Core
         * @stagemodelonly
         * @since 23
         */
        DEVICE_UNPAIRED = 2,
        /**
         * The device is lost.
         *
         * @syscap SystemCapability.Communication.FusionConnectivity.Core
         * @stagemodelonly
         * @since 23
         */
        DEVICE_LOST = 3,
        /**
         * Bluetooth is disabled.
         *
         * @syscap SystemCapability.Communication.FusionConnectivity.Core
         * @stagemodelonly
         * @since 23
         */
        BLUETOOTH_DISABLED = 4
    }
}
export default partnerAgent;

```
