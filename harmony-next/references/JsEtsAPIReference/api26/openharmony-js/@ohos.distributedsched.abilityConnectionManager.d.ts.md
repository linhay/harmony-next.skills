# @ohos.distributedsched.abilityConnectionManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024-2026 Huawei Device Co., Ltd.
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
 * @kit DistributedServiceKit
 */
import { Callback } from './@ohos.base';
import Context from './application/Context';
/**
 * The **abilityConnectionManager** module provides APIs for cross-device connection management. After successful
 * networking between devices (login with the same account and enabling of Bluetooth on the devices), a system
 * application and a third-party application can start a [UIAbility]{@link @ohos.app.ability.UIAbility} of the same
 * application across these devices to establish a Bluetooth connection. This way, data (specifically, text) can be
 * transmitted across the devices over the connection.
 *
 * @syscap SystemCapability.DistributedSched.AppCollaboration
 * @stagemodelonly
 * @since 18
 */
declare namespace abilityConnectionManager {
    /**
     * Defines the application collaboration information.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    interface PeerInfo {
        /**
         * Peer device ID.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        deviceId: string;
        /**
         * Bundle name of the application.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        bundleName: string;
        /**
         * Module name of the peer application.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        moduleName: string;
        /**
         * Ability name of the peer application.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        abilityName: string;
        /**
         * Service name for the application.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        serviceName?: string;
    }
    /**
     * Connection options for the application.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    interface ConnectOptions {
        /**
         * Whether to send data. The value **true** indicates that data needs to be sent, and the value **false** indicates
         * the opposite.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        needSendData?: boolean;
        /**
         * Application startup options.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        startOptions?: StartOptionParams;
        /**
         * Additional configuration for the connection.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        parameters?: Record<string, string>;
    }
    /**
     * Defines the connection result.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    interface ConnectResult {
        /**
         * Whether the connection is successful. The value **true** indicates that the connection is successful, and the
         * value **false** indicates the opposite.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        isConnected: boolean;
        /**
         * Connection error code.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        errorCode?: ConnectErrorCode;
        /**
         * Connection rejection reason.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        reason?: string;
    }
    /**
     * Enumerates connection error codes.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    export enum ConnectErrorCode {
        /**
         * A session already exists between applications.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        CONNECTED_SESSION_EXISTS = 0,
        /**
         * The peer application rejects the collaboration request.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        PEER_APP_REJECTED = 1,
        /**
         * Wi-Fi is disabled at the local end.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        LOCAL_WIFI_NOT_OPEN = 2,
        /**
         * Wi-Fi is disabled at the peer end.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        PEER_WIFI_NOT_OPEN = 3,
        /**
         * The **onCollaborate** callback is not implemented.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        PEER_ABILITY_NO_ONCOLLABORATE = 4,
        /**
         * An internal system error occurs.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        SYSTEM_INTERNAL_ERROR = 5
    }
    /**
     * Enumerates application start options.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    export enum StartOptionParams {
        /**
         * Start of the peer application in the foreground.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        START_IN_FOREGROUND = 0
    }
    /**
     * Defines the event callback information.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    interface EventCallbackInfo {
        /**
         * Collaboration session ID.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        sessionId: number;
        /**
         * Disconnection reason.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        reason?: DisconnectReason;
        /**
         * Received message.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        msg?: string;
        /**
         * Received byte stream.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        data?: ArrayBuffer;
    }
    /**
     * Collaboration event information.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    interface CollaborateEventInfo {
        /**
         * Collaboration event type.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        eventType: CollaborateEventType;
        /**
         * Content of a collaboration event.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        eventMsg?: string;
    }
    /**
     * Enumerates collaboration event types.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    enum CollaborateEventType {
        /**
         * Task sending failure.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        SEND_FAILURE = 0,
        /**
         * Color space conversion failure.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        COLOR_SPACE_CONVERSION_FAILURE = 1
    }
    /**
     * Enumerates the disconnection reasons.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    enum DisconnectReason {
        /**
         * The peer application proactively disables collaboration.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        PEER_APP_CLOSE_COLLABORATION = 0,
        /**
         * The peer application exits.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        PEER_APP_EXIT = 1,
        /**
         * The network is disconnected.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        NETWORK_DISCONNECTED = 2
    }
    /**
     * Enables listening for **connect** events. This API uses an asynchronous callback to return the result.
     *
     * @param { 'connect' } type - Event type. This field has a fixed value of **connect**. This event is triggered when
     *     [abilityConnectionManager.connect()]{@link abilityConnectionManager.connect(sessionId: number)} is called.
     * @param { number } sessionId - ID of the collaboration session.
     * @param { Callback<EventCallbackInfo> } callback - Registered callback function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function on(type: 'connect', sessionId: number, callback: Callback<EventCallbackInfo>): void;
    /**
     * Disables listening for **connect** events.
     *
     * @param { 'connect' } type - Event type. This field has a fixed value of **connect**.
     * @param { number } sessionId - ID of the collaboration session.
     * @param { Callback<EventCallbackInfo> } callback - Registered callback function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function off(type: 'connect', sessionId: number, callback?: Callback<EventCallbackInfo>): void;
    /**
     * Enables listening for **disconnect** events.
     *
     * @param { 'disconnect' } type - Event type. This field has a fixed value of **disconnect**. This event is triggered when
     *     [abilityConnectionManager.disconnect()]{@link abilityConnectionManager.disconnect(sessionId: number)} is called.
     * @param { number } sessionId - ID of the collaboration session.
     * @param { Callback<EventCallbackInfo> } callback - Registered callback function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function on(type: 'disconnect', sessionId: number, callback: Callback<EventCallbackInfo>): void;
    /**
     * Disables listening for **disconnect** events.
     *
     * @param { 'disconnect' } type - Event type. This field has a fixed value of **disconnect**.
     * @param { number } sessionId - ID of the collaboration session.
     * @param { Callback<EventCallbackInfo> } callback - Registered callback function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function off(type: 'disconnect', sessionId: number, callback?: Callback<EventCallbackInfo>): void;
    /**
     * Enables listening for **receiveMessage** events.
     *
     * @param { 'receiveMessage' } type - Event type. This field has a fixed value of **receiveMessage**. This event is
     *     triggered when
     *     [abilityConnectionManager.sendMessage()]{@link abilityConnectionManager.sendMessage(sessionId: number, msg: string)} is
     *     called.
     * @param { number } sessionId - ID of the collaboration session.
     * @param { Callback<EventCallbackInfo> } callback - Registered callback function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function on(type: 'receiveMessage', sessionId: number, callback: Callback<EventCallbackInfo>): void;
    /**
     * Disables listening for **receiveMessage** events.
     *
     * @param { 'receiveMessage' } type - Event type. This field has a fixed value of **receiveMessage**.
     * @param { number } sessionId - ID of the collaboration session.
     * @param { Callback<EventCallbackInfo> } callback - Registered callback function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function off(type: 'receiveMessage', sessionId: number, callback?: Callback<EventCallbackInfo>): void;
    /**
     * Enables listening for **receiveData** events.
     *
     * @param { 'receiveData' } type - Event type. This field has a fixed value of **receiveData**. This event is triggered
     *     when
     *     [abilityConnectionManager.sendData()]{@link abilityConnectionManager.sendData(sessionId: number, data: ArrayBuffer)} is
     *     called.
     * @param { number } sessionId - ID of the collaboration session.
     * @param { Callback<EventCallbackInfo> } callback - Registered callback function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function on(type: 'receiveData', sessionId: number, callback: Callback<EventCallbackInfo>): void;
    /**
     * Disables listening for **receiveData** events.
     *
     * @param { 'receiveData' } type - Event type. This field has a fixed value of **receiveData**.
     * @param { number } sessionId - ID of the collaboration session.
     * @param { Callback<EventCallbackInfo> } callback - Registered callback function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function off(type: 'receiveData', sessionId: number, callback?: Callback<EventCallbackInfo>): void;
    /**
     * Creates a collaboration session between applications.
     *
     * @permission ohos.permission.INTERNET and ohos.permission.GET_NETWORK_INFO and ohos.permission.SET_NETWORK_INFO and
     *     ohos.permission.DISTRIBUTED_DATASYNC
     * @param { string } serviceName - Service name for the application. The service name must be the same on the local end and
     *     peer end. The value contains a maximum of 256 characters.
     * @param { Context } context - Application context.
     * @param { PeerInfo } peerInfo - Collaboration information of the peer end.
     * @param { ConnectOptions } connectOptions - Connection options for the application.
     * @returns { number} ID of the collaboration session.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function createAbilityConnectionSession(serviceName: string, context: Context, peerInfo: PeerInfo, connectOptions: ConnectOptions): number;
    /**
     * Destroys a collaboration session between applications.
     *
     * @param { number } sessionId - Collaboration session ID.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function destroyAbilityConnectionSession(sessionId: number): void;
    /**
     * Obtains information about the peer application in the specified session.
     *
     * @param { number } sessionId - ID of the collaboration session.
     * @returns { PeerInfo | undefined } Information about the peer application if the corresponding **peerInfo** exists;
     *     **undefined** if the session ID is not found.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function getPeerInfoById(sessionId: number): PeerInfo | undefined;
    /**
     * Sets up a UIAbility connection after a collaboration session is created and the session ID is obtained. This API
     * uses a promise to return the result.
     *
     * @param { number } sessionId - ID of the collaboration session.
     * @returns { Promise<ConnectResult> } Promise used to return the
     *     [connection result]{@link abilityConnectionManager.ConnectResult}.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function connect(sessionId: number): Promise<ConnectResult>;
    /**
     * Disconnects the UIAbility connection to end the collaboration session.
     *
     * @param { number } sessionId - ID of the collaboration session.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function disconnect(sessionId: number): void;
    /**
     * Accepts the UIAbility connection after a collaboration session is set up and the session ID is obtained.
     *
     * @param { number } sessionId - ID of the collaboration session.
     * @param { string } token - Token value passed by the application on device A.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function acceptConnect(sessionId: number, token: string): Promise<void>;
    /**
     * Rejects a connection request in a cross-device collaboration session. After a connection request sent from the peer
     *  application is rejected, a rejection reason is returned.
     *
     * @param { string } token - Token used for application collaboration management.
     * @param { string } reason - Reason why the connection is rejected.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function reject(token: string, reason: string): void;
    /**
     * Sends text messages after a collaboration session is set up.
     *
     * @param { number } sessionId - ID of the collaboration session.
     * @param { string } msg - Text content. The maximum size of the text content is 1 KB.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function sendMessage(sessionId: number, msg: string): Promise<void>;
    /**
     * Sends [ArrayBuffer](docroot://arkts-utils/arraybuffer-object.md) byte streams from one device to another after a
     * connection is successfully established.
     *
     * @param { number } sessionId - ID of the collaboration session.
     * @param { ArrayBuffer } data - Byte stream information.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    function sendData(sessionId: number, data: ArrayBuffer): Promise<void>;
    /**
     * Enumerates application collaboration key values.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    export enum CollaborationKeys {
        /**
         * Key value of the peer device information.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        PEER_INFO = 'ohos.collaboration.key.peerInfo',
        /**
         * Key value of the connection option.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        CONNECT_OPTIONS = 'ohos.collaboration.key.connectOptions',
        /**
         * Key value of the collaboration type.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        COLLABORATE_TYPE = 'ohos.collaboration.key.abilityCollaborateType'
    }
    /**
     * Enumerates application collaboration key values.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 18
     */
    export enum CollaborationValues {
        /**
         * Default collaboration.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        ABILITY_COLLABORATION_TYPE_DEFAULT = 'ohos.collaboration.value.abilityCollab',
        /**
         * Collaboration via connection proxy.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 18
         */
        ABILITY_COLLABORATION_TYPE_CONNECT_PROXY = 'ohos.collaboration.value.connectProxy'
    }
}
export default abilityConnectionManager;

```
