# @ohos.distributedHardware.mechanicManager.d.ts

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
 * @kit MechanicKit
 */
import type { Callback } from './@ohos.base';
/**
 * Provides capabilities for controlling and interacting with mechanical devices connected to this device.
 * The capabilities cover connection management, control, and monitoring.
 *
 * @namespace mechanicManager
 * @syscap SystemCapability.Mechanic.Core
 * @since 20
 */
declare namespace mechanicManager {
    /**
     * Subscribes to device attachment state change events.
     * @param { 'attachStateChange' } type Event type.
     * @param { Callback<AttachStateChangeInfo> } callback Callback used to return the state change.
     * @throws { BusinessError } 33300001 - Service exception.
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    function on(type: 'attachStateChange', callback: Callback<AttachStateChangeInfo>): void;
    /**
     * Unsubscribes from device attachment state change events.
     * @param { 'attachStateChange' } type Event type.
     * @param { Callback<AttachStateChangeInfo> } [callback] Callback used to return the state change.
     * @throws { BusinessError } 33300001 - Service exception.
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    function off(type: 'attachStateChange', callback?: Callback<AttachStateChangeInfo>): void;
    /**
     * Obtain the list of connected mechanical devices.
     * @returns { MechInfo[] } List of connected mechanical devices.
     * @throws { BusinessError } 33300001 - Service exception.
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    function getAttachedMechDevices(): MechInfo[];
    /**
     * Enables or disables camera tracking.
     * @param { boolean } isEnabled Whether to enable camera tracking.
     * @throws { BusinessError } 33300001 - Service exception.
     * @throws { BusinessError } 33300002 - Device not connected.
     * @throws { BusinessError } 33300003 - Feature not supported.
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    function setCameraTrackingEnabled(isEnabled: boolean): void;
    /**
     * Checks whether camera tracking is enabled for this mechanical device.
     * @returns { boolean } Enabled status. The value true means that camera tracking is enabled, and false means
     * the opposite.
     * @throws { BusinessError } 33300001 - Service exception.
     * @throws { BusinessError } 33300002 - Device not connected.
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    function getCameraTrackingEnabled(): boolean;
    /**
     * Subscribes to tracking events.
     * @param { 'trackingStateChange' } type Event type.
     * @param { Callback<TrackingEventInfo> } callback Callback used to return the tracking event information.
     * @throws { BusinessError } 33300001 - Service exception.
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    function on(type: 'trackingStateChange', callback: Callback<TrackingEventInfo>): void;
    /**
     * Unsubscribes from tracking events.
     * @param { 'trackingStateChange' } type Event type.
     * @param { Callback<TrackingEventInfo> } [callback] Callback used to return the tracking event information.
     * @throws { BusinessError } 33300001 - Service exception.
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    function off(type: 'trackingStateChange', callback?: Callback<TrackingEventInfo>): void;
    /**
     * Obtains the camera tracking layout of this mechanical device.
     * @returns { CameraTrackingLayout } Camera tracking layout obtained.
     * @throws { BusinessError } 33300001 - Service exception.
     * @throws { BusinessError } 33300002 - Device not connected.
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    function getCameraTrackingLayout(): CameraTrackingLayout;
    /**
     * Checks whether the current device supports embodied control for a specific type of device.
     *
     * @param { MechDeviceType } [mechDeviceType]  - Associated device type.
     *     <br>Default: If this parameter is not provided, it represents all device types. As long as one or more types
     * are supported, the result returned will be supported.
     * @returns { boolean } Returns whether embodied control is supported.
     * @syscap SystemCapability.Mechanic.Core
     * @since 26.0.0
     */
    function isControlSupported(mechDeviceType?: MechDeviceType): boolean;
    /**
     * Mechanical device information.
     * @typedef MechInfo
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    export interface MechInfo {
        /**
         * ID of the mechanical device.
         * @type { number }
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        mechId: number;
        /**
         * Type of the mechanical device.
         * @type { MechDeviceType }
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        mechDeviceType: MechDeviceType;
        /**
         * Name of the mechanical device.
         * @type { string }
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        mechName: string;
    }
    /**
     * Tracking event callback info.
     *
     * @typedef TrackingEventInfo
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    export interface TrackingEventInfo {
        /**
         * Tracking event.
         * @type { TrackingEvent } Tracking event.
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        event: TrackingEvent;
    }
    /**
     * Callback information about the device attachment state change.
     * @typedef AttachStateChangeInfo
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    export interface AttachStateChangeInfo {
        /**
         * Device attachment state.
         * @type { AttachState }
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        state: AttachState;
        /**
         * Mechanical device information.
         * @type { MechInfo }
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        mechInfo: MechInfo;
    }
    /**
     * Enumerates the tracking events.
     * @enum { number }
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    export enum TrackingEvent {
        /**
         * Camera tracking enabled by user.
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        CAMERA_TRACKING_USER_ENABLED = 0,
        /**
         * Camera tracking disabled by user.
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        CAMERA_TRACKING_USER_DISABLED = 1,
        /**
         * Camera tracking layout changed. You can call getCameraTrackingLayout to obtain the new layout.
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        CAMERA_TRACKING_LAYOUT_CHANGED = 2
    }
    /**
     * Enumerates the mechanical device types.
     * @enum { number }
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    export enum MechDeviceType {
        /**
         * Gimbal device.
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        GIMBAL_DEVICE = 0
    }
    /**
     * Device attach states.
     *
     * @enum { number }
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    export enum AttachState {
        /**
         * Device attached.
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        ATTACHED = 0,
        /**
         * Device detached.
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        DETACHED = 1
    }
    /**
     * Enumerates the camera tracking layouts.
     * @enum { number }
     * @syscap SystemCapability.Mechanic.Core
     * @since 20
     */
    export enum CameraTrackingLayout {
        /**
         * Default layout.
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        DEFAULT = 0,
        /**
         * Left-side layout.
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        LEFT = 1,
        /**
         * Middle layout.
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        MIDDLE = 2,
        /**
         * Right-side layout.
         * @syscap SystemCapability.Mechanic.Core
         * @since 20
         */
        RIGHT = 3
    }
}
export default mechanicManager;

```
