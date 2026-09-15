# @ohos.bluetooth.hid.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2023 Huawei Device Co., Ltd.
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
import type baseProfile from './@ohos.bluetooth.baseProfile';
import { Callback } from './@ohos.base';
import type common from './@ohos.bluetooth.common';
/**
 * Provides methods to accessing bluetooth HID(Human Interface Device)-related capabilities.
 *
 * @syscap SystemCapability.Communication.Bluetooth.Core
 * @since 10
 */
declare namespace hid {
    /**
     * Base interface of profile.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    type BaseProfile = baseProfile.BaseProfile;
    /**
     * Bluetooth device address.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    type BluetoothAddress = common.BluetoothAddress;
    /**
     * create the instance of hid profile.
     *
     * @returns { HidHostProfile } Returns the instance of hid profile.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    function createHidHostProfile(): HidHostProfile;
    /**
     * Manager hid host profile.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    interface HidHostProfile extends BaseProfile {
    }
    /**
     * Creates the instance of HID device profile.
     *
     * @returns { HidDeviceProfile } Returns the instance of HID device profile.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    function createHidDeviceProfile(): HidDeviceProfile;
    /**
     * Manager HID device profile.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    interface HidDeviceProfile extends BaseProfile {
        /**
         * Application registers the HID Device capability.
         * The application will only successfully call this API when it's in the foreground.
         * If the application that has registered the HID Device capability is switched to the background, the system
         * automatically cancels the HID Device capability registration. The application can listen to the appStatusChange
         * callback to detect the status change.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { HidDeviceSdp } sdp - Describe the hid device capability fields of this endpoint being queried.
         * @param { HidDeviceQos } inQos - Describe the In Quality of Service (QoS) settings
         *     for the Bluetooth HID device application.
         * @param { HidDeviceQos } outQos - Describe the Out Quality of Service (QoS) settings
         *     for the Bluetooth HID device application.
         * @param { Callback<boolean> } callback - Callback for HID device registration status changes,
         *     {@code true} indicates register success or {@code false} otherwise.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 2900003 - Bluetooth disabled.
         * @throws { BusinessError } 2900099 - Operation failed.
         * @throws { BusinessError } 2903050 - Application is not in the foreground.
         * @throws { BusinessError } 2903051 - Any app has been registered.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        registerHidDevice(sdp: HidDeviceSdp, inQos: HidDeviceQos, outQos: HidDeviceQos, callback: Callback<boolean>): void;
        /**
         * Application unregisters the HID Device capability.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 2900003 - Bluetooth disabled.
         * @throws { BusinessError } 2900099 - Operation failed.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        unregisterHidDevice(): void;
        /**
         * Initiate an HID connection to a remote HID host device.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { BluetoothAddress } deviceId -  Indicates the address of the remote Bluetooth device.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 2900003 - Bluetooth disabled.
         * @throws { BusinessError } 2900004 - Remote Device profile not supported.
         * @throws { BusinessError } 2900099 - Operation failed.
         * @throws { BusinessError } 2903052 - App not register.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        connect(deviceId: BluetoothAddress): void;
        /**
         * Disconnect the HID connection with the remote device.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 2900003 - Bluetooth disabled.
         * @throws { BusinessError } 2900099 - Operation failed.
         * @throws { BusinessError } 2903052 - App not register.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        disconnect(): void;
        /**
         * Send report to a remote HID host device.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { number } id  - Report ID defined in the descriptor.
         * @param { Uint8Array } reportData  - Report data sent to the host device.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 2900003 - Bluetooth disabled.
         * @throws { BusinessError } 2900099 - Operation failed.
         * @throws { BusinessError } 2903052 - App not register.
         * @throws { BusinessError } 2903053 - Device not connected.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        sendReport(id: number, reportData: Uint8Array): void;
        /**
         * Reply report to a remote HID host device.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { ReportType } type - Report type for reply
         * @param { number } id - Report Id, as defined in descriptor.
         *     It can be 0 in case Report Id are not defined in descriptor.
         * @param { Uint8Array } reportData - Report Data send to host.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 2900003 - Bluetooth disabled.
         * @throws { BusinessError } 2900099 - Operation failed.
         * @throws { BusinessError } 2903052 - App not register.
         * @throws { BusinessError } 2903053 - Device not connected.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        replyReport(type: ReportType, id: number, reportData: Uint8Array): void;
        /**
         * Report error to a remote HID host device.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { ErrorReason } error - error reason to send.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 2900003 - Bluetooth disabled.
         * @throws { BusinessError } 2900099 - Operation failed.
         * @throws { BusinessError } 2903052 - App not register.
         * @throws { BusinessError } 2903053 - Device not connected.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        reportError(error: ErrorReason): void;
        /**
         * Subscribe to the event reported when GET_REPORT message is received from the remote.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { Callback<GetReportData> } callback - Callback used to listen for event.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        onGetReport(callback: Callback<GetReportData>): void;
        /**
         * Unsubscribe from the event that a GET_REPORT message is received from the peer device.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { Callback<GetReportData> } [callback] - Callback used to listen for event.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        offGetReport(callback?: Callback<GetReportData>): void;
        /**
         * Subscribe to the event reported when SET_REPORT message is received from the remote.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { Callback<SetReportData> } callback - Callback used to listen for event.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        onSetReport(callback: Callback<SetReportData>): void;
        /**
         * Unsubscribe from the event that a SET_REPORT message is received from the peer device.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { Callback<SetReportData> } [callback] - Callback used to listen for event.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        offSetReport(callback?: Callback<SetReportData>): void;
        /**
         * Subscribe to the event reported when InterruptData is received from the remote.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { Callback<InterruptData> } callback - Callback used to listen for event.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        onInterruptDataReceived(callback: Callback<InterruptData>): void;
        /**
         * Unsubscribe from the event reported when InterruptData is received from the remote.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { Callback<InterruptData> } [callback] - Callback used to listen for event.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        offInterruptDataReceived(callback?: Callback<InterruptData>): void;
        /**
         * Subscribe to the event reported when SET_PROTOCOL message is received from the remote.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { Callback<ProtocolData> } callback - Callback used to listen for event.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        onSetProtocol(callback: Callback<ProtocolData>): void;
        /**
         * Unsubscribe from the event that a SET_PROTOCOL message is received from the peer device.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { Callback<ProtocolData> } [callback] - Callback used to listen for event.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        offSetProtocol(callback?: Callback<ProtocolData>): void;
        /**
         * Subscribe to the event reported when virtual Cable is removed.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { Callback<void> } callback - Callback used to listen for event.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        onVirtualCableUnplug(callback: Callback<void>): void;
        /**
         * Unsubscribe from the event reported when virtual Cable is removed.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { Callback<void> } [callback] - Callback used to listen for event.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        offVirtualCableUnplug(callback?: Callback<void>): void;
    }
    /**
     * Describe the HID device capability fields of this endpoint being queried.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    interface HidDeviceSdp {
        /**
         * name of this Bluetooth hid device. Maximum length is 50 bytes.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        name: string;
        /**
         * description for this Bluetooth hid device. Maximum length is 50 bytes.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        description: string;
        /**
         * provider of this Bluetooth hid device. Maximum length is 50 bytes.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        provider: string;
        /**
         * Subclass of this Bluetooth HID device. Subclass represents the specific HID device type.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        subclass: Subclass;
        /**
         * descriptors identifies the descriptors associated with the bluetooth hid device.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        descriptors: Uint8Array;
    }
    /**
     * Represents the Quality of Service (QoS) settings for a bluetooth hid device application.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    interface HidDeviceQos {
        /**
         * L2CAP service type, default = SERVICE_BEST_EFFORT.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        serviceType?: ServiceType;
        /**
         * L2CAP tokenRate, means transmission rate, default = 0.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        tokenRate?: number;
        /**
         * L2CAP token bucket size, default = 0.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        tokenBucketSize?: number;
        /**
         * L2CAP peak bandwidth, default = 0.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        peakBandwidth?: number;
        /**
         * L2CAP latency, default = -1.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        latency?: number;
        /**
         * L2CAP delay variation, default = -1.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        delayVariation?: number;
    }
    /**
     * Describe the GET_REPORT data is received from remote host.
     *
     * @typedef GetReportData
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    interface GetReportData {
        /**
         * reportType of GET_REPORT data.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        type: ReportType;
        /**
         * id of GET_REPORT data.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        id: number;
        /**
         * bufferSize of GET_REPORT data, maximum number of octets to transfer during data phase.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        bufferSize: number;
    }
    /**
     * Describe the SET_REPORT data is received from remote host.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    interface SetReportData {
        /**
         * reportType of SET_REPORT data.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        type: ReportType;
        /**
         * id of SET_REPORT data.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        id: number;
        /**
         * data of SET_REPORT data.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        data: Uint8Array;
    }
    /**
     * Describe the interrupt data is received from remote host.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    interface InterruptData {
        /**
         * id of interrupt data.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        id: number;
        /**
         * data of interrupt data.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        data: Uint8Array;
    }
    /**
     * Describe the protocol data is received from remote host.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    interface ProtocolData {
        /**
         * protocol of protocol data.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        protocol: ProtocolType;
    }
    /**
     * Describe the subclass.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    enum Subclass {
        /**
         * Uncategorized subclass.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        SUBCLASS_UNCATEGORIZED = 0,
        /**
         * Joystick subclass.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        SUBCLASS_JOYSTICK = 1,
        /**
         * Gamepad subclass.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        SUBCLASS_GAMEPAD = 2,
        /**
         * Remote control subclass.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        SUBCLASS_REMOTE_CONTROL = 3,
        /**
         * Sensing device subclass.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        SUBCLASS_SENSING_DEVICE = 4,
        /**
         * digitizer tablet subclass.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        SUBCLASS_DIGITIZER_TABLET = 5,
        /**
         * Card reader subclass.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        SUBCLASS_CARD_READER = 6,
        /**
         * Keyboard subclass.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        SUBCLASS_KEYBOARD = 64,
        /**
         * Mouse subclass.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        SUBCLASS_MOUSE = 128,
        /**
         * Combo subclass.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        SUBCLASS_COMBO = 192
    }
    /**
     * Describe the report type.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    enum ReportType {
        /**
         * Report type input.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        REPORT_TYPE_INPUT = 1,
        /**
         * Report type output.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        REPORT_TYPE_OUTPUT = 2,
        /**
         * Report type feature.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        REPORT_TYPE_FEATURE = 3
    }
    /**
     * Describe the l2cap service type.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    enum ServiceType {
        /**
         * Service type no traffic.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        SERVICE_NO_TRAFFIC = 0,
        /**
         * Service type best effort.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        SERVICE_BEST_EFFORT = 1,
        /**
         * Service type guaranteed.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        SERVICE_GUARANTEED = 2
    }
    /**
     * Describe the error reason.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    enum ErrorReason {
        /**
         * Constant representing success response for set report.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        RSP_SUCCESS = 0,
        /**
         * Constant representing error response for set report due to not ready.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        RSP_NOT_READY = 1,
        /**
         * Constant representing error response for set report due to invalid report ID.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        RSP_INVALID_REPORT_ID = 2,
        /**
         * Constant representing error response for set report due to unsupported request.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        RSP_UNSUPPORTED_REQ = 3,
        /**
         * Constant representing error response for set report due to invalid parameter.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        RSP_INVALID_PARAM = 4,
        /**
         * Constant representing error response for Set Report with unknown reason.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        RSP_UNKNOWN = 14
    }
    /**
     * Describe the protocol type.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    enum ProtocolType {
        /**
         * Protocol type boot mode.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        PROTOCOL_BOOT_MODE = 0,
        /**
         * Protocol type report mode.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 23
         */
        PROTOCOL_REPORT_MODE = 1
    }
}
export default hid;

```
