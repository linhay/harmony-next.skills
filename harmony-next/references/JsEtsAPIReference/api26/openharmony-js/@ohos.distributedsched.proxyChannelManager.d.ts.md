# @ohos.distributedsched.proxyChannelManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
 * @kit DistributedServiceKit
 */
import { Callback } from './@ohos.base';
/**
 * # Instructions
 *
 * Before calling the APIs of this module, complete the following configurations:
 *
 * 1. Apply for the **ohos.permission.ACCESS_BLUETOOTH** permission. For details about how to configure and apply for
 * permissions, see [Declaring Permissions](docroot://security/AccessToken/declare-permissions.md)
 * and [Requesting User Authorization](docroot://security/AccessToken/request-user-authorization.md).
 * 2. For application processes that need to be started by proxy, set the **action** field to
 * **action.ohos.pull.listener** in the **module.json5** file.
 */
/**
 * DSoftBus provides stable and reliable underlying channels for cross-device communication. This module is developed
 * based on DSoftBus. It supports efficient data exchange between phones and wearables, providing users with a seamless
 * device interconnection experience. During collaboration between the phone application and watch application, if the
 * phone application is not running in the foreground, its downlink messages are forwarded to the notification server
 * and then sent to the watch through the proxy module. The core functions of this module include proxy channel
 * management, data route management, application state awareness and wakeup, and link state monitoring.
 *
 * - Proxy channel management: Manages bidirectional data channels established between phones and wearables via the
 * Bluetooth Basic Rate (BR) protocol.
 * - Data route management: Accurately forwards data of wearables based on the specified service UUID.
 * - Application state awareness and wakeup: After a proxy channel is enabled, dynamically analyzes and wakes up the
 * corresponding application process on the phone after receiving data sent by the wearable.
 * - Link state monitoring: Monitors the channel connection state in real time through callback.
 *
 * @syscap SystemCapability.DistributedSched.AppCollaboration
 * @stagemodelonly
 * @since 20
 */
declare namespace proxyChannelManager {
    /**
     * Opens a proxy channel. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { ChannelInfo } channelInfo - Channel information, including the MAC address and service UUID of the peer
     *     device.
     * @returns { Promise<number> } Proxy channel ID. The value range is [1, 2147483647]. The lifecycle of **channelId** is
     *     the same as that of the proxy channel. If the proxy is not closed, the returned **channelId** is the same as
     *     that passed in the API.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because bluetooth proxy function has
     *     been trimmed. [since 26.0.0]
     * @throws { BusinessError } 32390001 - BR is disabled.
     * @throws { BusinessError } 32390002 - Device not paired.
     * @throws { BusinessError } 32390006 - Parameter error.
     * @throws { BusinessError } 32390100 - Internal error.
     * @throws { BusinessError } 32390101 - Call is restricted.
     * @throws { BusinessError } 32390102 - Operation failed or Connection timed out.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    function openProxyChannel(channelInfo: ChannelInfo): Promise<number>;
    /**
     * Closes a proxy channel that has been opened.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { number } channelId - Channel ID obtained when the proxy channel is opened.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because bluetooth proxy function has
     *     been trimmed. [since 26.0.0]
     * @throws { BusinessError } 32390004 - ChannelId is invalid or unavailable.
     * @throws { BusinessError } 32390006 - Parameter error.
     * @throws { BusinessError } 32390100 - Internal error.
     * @throws { BusinessError } 32390101 - Call is restricted.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    function closeProxyChannel(channelId: number): void;
    /**
     * Sends data to the peer end. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { number } channelId - Channel ID obtained when the proxy channel is opened.
     * @param { ArrayBuffer } data - Byte message sent to the peer end. The maximum length is 4096 bytes.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because bluetooth proxy function has
     *     been trimmed. [since 26.0.0]
     * @throws { BusinessError } 32390004 - ChannelId is invalid or unavailable.
     * @throws { BusinessError } 32390006 - Parameter error.
     * @throws { BusinessError } 32390100 - Internal error.
     * @throws { BusinessError } 32390101 - Call is restricted.
     * @throws { BusinessError } 32390103 - Data too long.
     * @throws { BusinessError } 32390104 - Send failed.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    function sendData(channelId: number, data: ArrayBuffer): Promise<void>;
    /**
     * Subscribes to data receiving events. This API returns the result asynchronously through a callback.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { 'receiveData' } type - Event type. The value **receiveData** indicates the data receiving event.
     * @param { number } channelId - Channel ID obtained when the proxy channel is opened.
     * @param { Callback<DataInfo> } callback - Callback used to return the received data. If the callback function is
     *     registered multiple times, only the last registered one takes effect.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 32390004 - ChannelId is invalid or unavailable.
     * @throws { BusinessError } 32390006 - Parameter error.
     * @throws { BusinessError } 32390100 - Internal error.
     * @throws { BusinessError } 32390101 - Call is restricted.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    function on(type: 'receiveData', channelId: number, callback: Callback<DataInfo>): void;
    /**
     * Unsubscribes from data receiving events.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { 'receiveData' } type - Event type. The value **receiveData** indicates the data receiving event.
     * @param { number } channelId - Channel ID obtained when the proxy channel is opened.
     * @param { Callback<DataInfo> } [callback] - Registered callback, If the value is empty, **undefined**, or **null**,
     *     all callbacks of data receiving events are unregistered. If the value is not empty, the last registered
     *     callback is used.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 32390004 - ChannelId is invalid or unavailable.
     * @throws { BusinessError } 32390006 - Parameter error.
     * @throws { BusinessError } 32390100 - Internal error.
     * @throws { BusinessError } 32390101 - Call is restricted.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    function off(type: 'receiveData', channelId: number, callback?: Callback<DataInfo>): void;
    /**
     * Subscribes to channel state change events. This API returns the result asynchronously through a callback.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { 'channelStateChange' } type - Event type. The value **channelStateChange** indicates the channel state
     *     change event.
     * @param { number } channelId - Channel ID obtained when the proxy channel is opened.
     * @param { Callback<ChannelStateInfo> } callback - Callback used to return the received channel state. If the
     *     callback function is registered multiple times, only the last registered one takes effect.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 32390004 - ChannelId is invalid or unavailable.
     * @throws { BusinessError } 32390006 - Parameter error.
     * @throws { BusinessError } 32390100 - Internal error.
     * @throws { BusinessError } 32390101 - Call is restricted.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    function on(type: 'channelStateChange', channelId: number, callback: Callback<ChannelStateInfo>): void;
    /**
     * Unsubscribes from channel state change events.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { 'channelStateChange' } type - Event type. The value **channelStateChange** indicates the channel state
     *     change event.
     * @param { number } channelId - Channel ID obtained when the proxy channel is opened.
     * @param { Callback<ChannelStateInfo> } [callback] - Registered callback, If the value is empty, **undefined**, or
     *     **null**, all callbacks of data receiving events are unregistered. If the value is not empty, the last
     *     registered callback is used.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 32390004 - ChannelId is invalid or unavailable.
     * @throws { BusinessError } 32390006 - Parameter error.
     * @throws { BusinessError } 32390100 - Internal error.
     * @throws { BusinessError } 32390101 - Call is restricted.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    function off(type: 'channelStateChange', channelId: number, callback?: Callback<ChannelStateInfo>): void;
    /**
     * Represents the received data, including the channel ID and data.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    interface DataInfo {
        /**
         * Proxy channel ID.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        channelId: number;
        /**
         * Received byte array.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        data: ArrayBuffer;
    }
    /**
     * Enumerates the link types.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    enum LinkType {
        /**
         * Bluetooth.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        LINK_BR = 0
    }
    /**
     * Represents the proxy channel information, including the MAC address and service UUID of the peer device.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    interface ChannelInfo {
        /**
         * Link type of the proxy channel.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        linkType: LinkType;
        /**
         * MAC address of the peer device.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        peerDevAddr: string;
        /**
         * Service UUID of the peer device.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        peerUuid: string;
    }
    /**
     * Enumerates the connection states of the proxy channel.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    enum ChannelState {
        /**
         * The connection is disconnected, and the channel is unavailable.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        CHANNEL_WAIT_RESUME = 0,
        /**
         * The connection is restored, and the channel is available.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        CHANNEL_RESUME = 1,
        /**
         * The channel is unavailable due to other software errors.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        CHANNEL_EXCEPTION_SOFTWARE_FAILED = 2,
        /**
         * The Bluetooth pairing relationship is deleted, and the channel is unavailable.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        CHANNEL_BR_NO_PAIRED = 3
    }
    /**
     * Represents the connection state information of the proxy channel.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    interface ChannelStateInfo {
        /**
         * Proxy channel ID.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        channelId: number;
        /**
         * Connection state of the proxy channel.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        state: ChannelState;
    }
}
export default proxyChannelManager;

```
