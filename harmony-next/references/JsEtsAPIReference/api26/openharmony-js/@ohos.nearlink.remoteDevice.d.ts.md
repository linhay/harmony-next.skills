# @ohos.nearlink.remoteDevice.d.ts

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
import nearlinkConstant from '@ohos.nearlink.constant';
/**
 * Provides interaction methods such as pairing and connection with remote devices.
 *
 * @syscap SystemCapability.Communication.NearLink.Base
 * @stagemodelonly
 * @since 26.0.0
 */
declare namespace remoteDevice {
    /**
     * Indicates the pairing state.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    type PairingState = nearlinkConstant.PairingState;
    /**
     * Indicates the connection state.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    type ConnectionState = nearlinkConstant.ConnectionState;
    /**
     * Indicates the device class.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    type DeviceClass = nearlinkConstant.DeviceClass;
    /**
     * Indicates the ACB(Asynchronous Connection-Oriented Bidirectional) connection status.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    type AcbState = nearlinkConstant.AcbState;
    /**
     * Creates a remote device instance.
     *
     * @param { string } address - Indicates the device address.
     *     <br>The length must be 17, The value consists of hexadecimal digits and colons (:),
     *     for example, 11:22:33:AA:BB:FF.
     * @returns { RemoteDevice } Returns a near link remote device instance.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100041 - Invalid address.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function createRemoteDevice(address: string): RemoteDevice;
    /**
     * Subscribes to NearLink pairing state change events.
     *
     * This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.
     * If the application is granted the ohos.permission.GET_NEARLINK_PEER_MAC permission,
     * the callback returns the real device address; otherwise, a random device address is returned.
     *
     * @param { Callback<PairingStateParam> } callback - Callback function used to listen for the pairing state event.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function onPairingStateChange(callback: Callback<PairingStateParam>): void;
    /**
     * Unsubscribes from NearLink pairing state change events.
     *
     * @param { Callback<PairingStateParam> } [callback] - Callback function used to listen for the pairing state event.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function offPairingStateChange(callback?: Callback<PairingStateParam>): void;
    /**
     * Subscribes to NearLink connection state change events.
     *
     * This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.
     * If the application is granted the ohos.permission.GET_NEARLINK_PEER_MAC permission,
     * the callback returns the real device address; otherwise, a random device address is returned.
     *
     * @param { Callback<ConnectionStateParam> } callback - Callback used to listen for the connection state changed event.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function onConnectionStateChange(callback: Callback<ConnectionStateParam>): void;
    /**
     * Unsubscribes from NearLink connection state change events.
     *
     * @param { Callback<ConnectionStateParam> } [callback] - Callback used to listen for the connection state changed event.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function offConnectionStateChange(callback?: Callback<ConnectionStateParam>): void;
    /**
     * Subscribes to the NearLink ACB connection status change event.
     *
     * This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.
     * If the application is granted the ohos.permission.GET_NEARLINK_PEER_MAC permission,
     * the callback returns the real device address; otherwise, a random device address is returned.
     *
     * @param { Callback<AcbStateParam> } callback - Callback of the event to be listened to.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function onAcbStateChange(callback: Callback<AcbStateParam>): void;
    /**
     * Unsubscribes from the NearLink ACB connection status change event.
     *
     * @param { Callback<AcbStateParam> } [callback] - Callback of the event to be listened to.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function offAcbStateChange(callback?: Callback<AcbStateParam>): void;
    /**
     * Remote device operation methods.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface RemoteDevice {
        /**
         * Initiate pairing to remote NearLink device.
         *
         * @permission ohos.permission.ACCESS_NEARLINK
         * @returns { Promise<void> } Returns the promise object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 36100003 - NearLink disabled.
         * @throws { BusinessError } 36100099 - Operation failed.
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        startPairing(): Promise<void>;
        /**
         * Gets the pairing state.
         *
         * @permission ohos.permission.ACCESS_NEARLINK
         * @returns { PairingState } Returns the pairing state.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 36100003 - NearLink disabled.
         * @throws { BusinessError } 36100099 - Operation failed.
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        getPairingState(): PairingState;
        /**
         * Gets the name of the NearLink device.
         *
         * @permission ohos.permission.ACCESS_NEARLINK
         * @returns { string } Returns the device name.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 36100003 - NearLink disabled.
         * @throws { BusinessError } 36100099 - Operation failed.
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        getDeviceName(): string;
        /**
         * Gets the type of the NearLink device.
         *
         * @permission ohos.permission.ACCESS_NEARLINK
         * @returns { DeviceClass } Indicates the type of the NearLink device.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 36100003 - NearLink disabled.
         * @throws { BusinessError } 36100099 - Operation failed.
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        getDeviceClass(): DeviceClass;
        /**
         * Gets the profile connection state.
         *
         * @permission ohos.permission.ACCESS_NEARLINK
         * @returns { ConnectionState } Returns the connection state.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 36100003 - NearLink disabled.
         * @throws { BusinessError } 36100099 - Operation failed.
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        getConnectionState(): ConnectionState;
        /**
         * Gets the ACB connection state.
         *
         * @permission ohos.permission.ACCESS_NEARLINK
         * @returns { AcbState } Returns the ACB connection state.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 36100003 - NearLink disabled.
         * @throws { BusinessError } 36100099 - Operation failed.
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        getAcbState(): AcbState;
        /**
         * Obtains the remote device information.
         *
         * @permission ohos.permission.ACCESS_NEARLINK
         * @returns { DeviceInformation } Returns the remote device information.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 36100003 - NearLink disabled.
         * @throws { BusinessError } 36100099 - Operation failed.
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        getDeviceInformation(): DeviceInformation;
    }
    /**
     * Describes the pairing state parameters.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface PairingStateParam {
        /**
         * Indicates the device address.
         * The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        address: string;
        /**
         * Indicates the previous pairing state.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        preState: PairingState;
        /**
         * Indicates the current pairing state.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        state: PairingState;
        /**
         * Indicates the pairing state reason.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        reason: PairingReason;
        /**
         * Indicates reason message. This field is intended for log information only
         * and should not be used for logic processing.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        reasonMsg?: string;
    }
    /**
     * Enum for the pairing reason.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    enum PairingReason {
        /**
         * Pairing succeed.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        PAIRING_REASON_SUCCESS = 0,
        /**
         * Pairing failed.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        PAIRING_REASON_FAILURE = 1,
        /**
         * Pairing failed: ACB connection failed. The remote device may be powered off or out of range.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        PAIRING_REASON_ACB_CONNECTION_FAIL = 2,
        /**
         * Pairing failed: ACB connection limit exceeded.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        PAIRING_REASON_EXCEED_ACB_MAX = 3,
        /**
         * Pairing failed: Cancelled by remote device.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        PAIRING_REASON_REMOTE_CANCELED = 4,
        /**
         * Pairing failed: Cancelled by local device.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        PAIRING_REASON_LOCAL_CANCELED = 5,
        /**
         * Pairing failed: Authentication failed.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        PAIRING_REASON_AUTH_FAIL = 6
    }
    /**
     * Describes pairing request parameters.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface PairingRequestParam {
        /**
         * Indicates the device address.
         * The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        address: string;
        /**
         * Key for the device pairing.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        passkey: string;
        /**
         * Indicates the pairing type.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        pairingType: PairingType;
    }
    /**
     * Enum for the pairing type.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    enum PairingType {
        /**
         * Without passkey, the user needs to accept or reject the pairing request.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        NO_PASSKEY_CONFIRMATION = 0,
        /**
         * The user needs to enter the passcode displayed on the peer device.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        PAIRING_TYPE_PASSCODE = 1,
        /**
         * The user needs to compare the number displayed on both devices.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        PAIRING_TYPE_NUMBER_COMPARE = 2
    }
    /**
     * Describes the connection state parameters.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface ConnectionStateParam {
        /**
         * Indicates the device address.
         * The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        address: string;
        /**
         * Indicates the previous connection state.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        preState: ConnectionState;
        /**
         * Indicates the current connection state.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        state: ConnectionState;
        /**
         * Connection reason.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        connectionReason: ConnectionReason;
        /**
         * Indicates reason message. This field is intended for log information only
         * and should not be used for logic processing.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        reasonMsg?: string;
    }
    /**
     * Enum for the connection reason.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    enum ConnectionReason {
        /**
         * Connection succeeded.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        CONNECTION_SUCCESS = 0,
        /**
         * Connection failed.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        CONNECTION_FAILURE = 1,
        /**
         * Local device initiated disconnection.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        CONNECTION_LOCAL_DISCONNECT = 2,
        /**
         * Remote device initiated disconnection.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        CONNECTION_REMOTE_DISCONNECT = 3,
        /**
         * Connection failed: ACB connection failed. The remote device may be powered off or out of range.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        CONNECTION_FAIL_ACB_CONNECTION = 4,
        /**
         * Connection failed: Service discovery failed.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        CONNECTION_FAIL_SERVICE_DISCOVERY = 5,
        /**
         * Connection failed: No available services found on the remote device.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        CONNECTION_FAIL_NO_AVAILABLE_SERVICE = 6,
        /**
         * Connection failed: Connection limit exceeded.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        CONNECTION_FAIL_CONNECTION_NUM_LIMITED = 7
    }
    /**
     * ACB connection status parameter.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AcbStateParam {
        /**
         * Indicates the device address.
         * The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        address: string;
        /**
         * ACB connection status.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        state: AcbState;
    }
    /**
     * Describes the remote device information.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface DeviceInformation {
        /**
         * The manufacturer data of the remote device.
         * The maximum length is 255.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        manufacturerData: string;
        /**
         * The model data of the remote device.
         * The maximum length is 255.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        modelData: string;
    }
}
export default remoteDevice;

```
