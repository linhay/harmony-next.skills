# @ohos.nearlink.manager.d.ts

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
import type { Callback } from '@ohos.base';
/**
 * Provides methods to manage NearLink devices.
 *
 * @syscap SystemCapability.Communication.NearLink.Base
 * @stagemodelonly
 * @since 26.0.0
 */
declare namespace manager {
    /**
     * Check whether the current device supports NearLink.
     *
     * @returns { boolean } Return whether the NearLink is supported.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function isNearLinkSupported(): boolean;
    /**
     * Gets the NearLink state.
     *
     * @returns { NearlinkState } Returns the NearLink state.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function getState(): NearlinkState;
    /**
     * Gets the local device's name.
     *
     * @permission ohos.permission.ACCESS_NEARLINK
     * @returns { string } Returns the device's name.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100003 - NearLink disabled.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function getLocalName(): string;
    /**
     * Gets the list of devices that have been paired with the current device.
     * If the user has the ohos.permission.GET_NEARLINK_PEER_MAC permission, the real device address is returned.
     * Otherwise, a random device address is returned.
     *
     * @permission ohos.permission.ACCESS_NEARLINK
     * @returns { string[] } Returns a list of paired devices' address in MAC format (e.g., "11:22:33:AA:BB:FF").
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100003 - NearLink disabled.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function getPairedDevices(): string[];
    /**
     * Subscribes to state change events.
     *
     * @param { Callback<NearlinkState> } callback - Callback used to listen for the state change event.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function onStateChange(callback: Callback<NearlinkState>): void;
    /**
     * Unsubscribes from state change events.
     *
     * @param { Callback<NearlinkState> } [callback] - Callback used to listen for the state change event.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function offStateChange(callback?: Callback<NearlinkState>): void;
    /**
     * The enum of NearLink state.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    enum NearlinkState {
        /**
         * Indicates that NearLink is turning on.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        STATE_TURNING_ON = 0,
        /**
         * Indicates that NearLink is on and ready for use.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        STATE_ON = 1,
        /**
         * Indicates that NearLink is turning off.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        STATE_TURNING_OFF = 2,
        /**
         * Indicates that NearLink has turned off.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        STATE_OFF = 3
    }
}
export default manager;

```
