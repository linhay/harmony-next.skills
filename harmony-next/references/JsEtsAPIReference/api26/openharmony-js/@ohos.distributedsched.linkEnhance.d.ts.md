# @ohos.distributedsched.linkEnhance.d.ts

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
 * @kit DistributedServiceKit
 */
import { Callback } from './@ohos.base';
/**
 * The **linkEnhance** module delivers highly efficient Bluetooth connectivity and data transmission capabilities,
 * significantly enhancing the cross-device connection stability. By employing a multi-channel merging algorithm, it not
 * only increases the number of available cross-device connections but also strengthens cross-device data transmission
 * capabilities, thereby improving the overall user experience.
 *
 * @syscap SystemCapability.DistributedSched.AppCollaboration
 * @stagemodelonly
 * @since 20
 */
declare namespace linkEnhance {
    /**
     * Represents the connection result, which is returned after the client calls **connect()**.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    interface ConnectResult {
        /**
         * ID of the peer device. If the connection is successful, the device ID of the peer device is returned. If the
         * connection fails, an empty string is returned.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        deviceId: string;
        /**
         * Connection result. The value **true** indicates that the connection is successful, and the value **false**
         * indicates the opposite.
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        success: boolean;
        /**
         * Number indicating the result code. If the connection is successful, **0** is returned. If the connection fails,
         * an error code is returned:
         *
         * - 32390200: The client connection times out.
         * - 32390201: The server service is not started.
         * - 32390300: Internal error.
         *
         * For details about the error codes, see
         * [Link Enhancement Error Codes](docroot://reference/apis-distributedservice-kit/errorcode-link-enhance.md).
         *
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        reason: number;
    }
    /**
     * Represents a **Server** object, which provides methods for starting, stopping, and closing the server, and
     * registering or unregistering event callbacks.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    interface Server {
        /**
         * Starts a server so that it can be connected by the client. A maximum of 10 servers are supported.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 32390202 - The number of servers exceeds the limit.
         * @throws { BusinessError } 32390300 - Internal error.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        start(): void;
        /**
         * Stops the server. After the server is stopped, you can call `start` to start it again.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        stop(): void;
        /**
         * Destroys the **Server** object to release related resources. To interact with the peer device again, create a new
         * **Server** object.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        close(): void;
        /**
         * Registers a callback listener for **connectionAccepted** events. This API uses an asynchronous callback to return
         * the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'connectionAccepted' } type - Event type, which is **connectionAccepted**. This event is triggered when
         *      a connection from the peer end is received.
         * @param { Callback<Connection> } callback - Registered callback, which is used to return the
         *     [Connection]{@link linkEnhance.Connection} object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 32390206 - Parameter invalid.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        on(type: 'connectionAccepted', callback: Callback<Connection>): void;
        /**
         * Unregisters the callback listener for **connectionAccepted** events. This API uses an asynchronous callback to
         * return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'connectionAccepted' } type - Event type, which is **connectionAccepted**. This event is triggered when
         *     a connection from the peer end is received.
         * @param { Callback<Connection> } [callback] - Registered callback, which is used to return the
         *     [Connection]{@link linkEnhance.Connection} object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 32390206 - Parameter invalid.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        off(type: 'connectionAccepted', callback?: Callback<Connection>): void;
        /**
         * Registers a callback listener for **serverStopped** events. This API uses an asynchronous callback to return the
         * result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'serverStopped' } type - Event type, which is **serverStopped**. This event is triggered when the server
         *     is stopped abnormally.
         * @param { Callback<number> } callback - Registered callback, where **number** indicates the returned error code.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 32390206 - Parameter invalid.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        on(type: 'serverStopped', callback: Callback<number>): void;
        /**
         * Unregisters the callback listener for **serverStopped** events. This API uses an asynchronous callback to return
         * the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'serverStopped' } type - Event type, which is **serverStopped**. This event is triggered when the server
         *     is stopped abnormally.
         * @param { Callback<number> } [callback] - Registered callback, where **number** indicates the returned error code.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 32390206 - Parameter invalid.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        off(type: 'serverStopped', callback?: Callback<number>): void;
    }
    /**
     * Creates a **Server** object. After **start()** is called, the device can be connected to other devices as a server.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { string } name - **Server** object name. The value is a string of up to 255 bytes. It cannot be empty.
     * @returns { Server } **Server** object created.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported
     *     because the linkEnhance function has been trimmed. [since 26.0.0]
     * @throws { BusinessError } 32390206 - Invalid parameter.
     * @throws { BusinessError } 32390203 - Duplicate server name.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    function createServer(name: string): Server;
    /**
     * Represents a **Connection** object, which provides methods for connecting to and disconnecting from a peer device,
     * obtaining the device's ID, sending data, and registering or unregistering event callbacks.
     *
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    interface Connection {
        /**
         * Connects to the server on the client. A maximum number of 10 connections are supported.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 32390204 - The number of connection exceeds the limit.
         * @throws { BusinessError } 32390300 - Internal error.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        connect(): void;
        /**
         * Disconnects from the peer device. The created **Connection** object remains valid after this API is called. You
         * can call **connect()** to reconnect to the peer device if necessary.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        disconnect(): void;
        /**
         * Destroys the **Connection** object to release resources. If the device needs to interact with the peer device
         * again, create a **Connection** object again and call `connect()` to initiate a connection.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        close(): void;
        /**
         * Obtains the device ID of the peer device. This API is called when the connection is established successfully
         * either by initiating a connection or accepting an incoming connection.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @returns { string } Device ID of the peer device, that is, the BLE MAC address of the peer device. An empty
         *     string is returned if no device ID is obtained.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        getPeerDeviceId(): string;
        /**
         * Sends data to the server after a connection is established successfully. When the server receives the connection
         * callback, it can also send data to the client.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { ArrayBuffer } data - Data to send. The maximum length is 1024 bytes.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 32390206 - Invalid parameter.
         * @throws { BusinessError } 32390205 - Connection is not ready.
         * @throws { BusinessError } 32390300 - Internal error.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        sendData(data: ArrayBuffer): void;
        /**
         * Registers a listener for **connectResult** events. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'connectResult' } type - Event type, which is **connectResult**. This event is triggered when `connect()
         *     ` is called.
         * @param { Callback<ConnectResult> } callback - Registered callback.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 32390206 - Invalid parameter.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        on(type: 'connectResult', callback: Callback<ConnectResult>): void;
        /**
         * Unregisters the listener for **connectResult** events.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'connectResult' } type - Event type, which is **connectResult**. This event is triggered when `connect()
         *     ` is called.
         * @param { Callback<ConnectResult> } [callback] - Registered callback.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 32390206 - Invalid parameter.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        off(type: 'connectResult', callback?: Callback<ConnectResult>): void;
        /**
         * Registers a listener for **disconnected** events. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'disconnected' } type - Event type, which is **disconnected**. This event is triggered when the
         *     connection is passively terminated or encounters an exception.
         * @param { Callback<number> } callback - Registered callback, where **number** indicates the returned error code.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 32390206 - Invalid parameter.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        on(type: 'disconnected', callback: Callback<number>): void;
        /**
         * Unregisters the listener for **disconnected** events. This API uses an asynchronous callback to return the
         * result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'disconnected' } type - Event type, which is **disconnected**. This event is triggered when the
         *     connection is passively terminated or encounters an exception.
         * @param { Callback<number> } [callback] - Registered callback, where **number** indicates the returned error code.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 32390206 - Invalid parameter.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        off(type: 'disconnected', callback?: Callback<number>): void;
        /**
         * Registers a listener for the **dataReceived** events. This API uses an asynchronous callback to return the
         * result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'dataReceived' } type - Event type, which is **dataReceived**. This event is triggered when data is
         *     received.
         * @param { Callback<ArrayBuffer> } callback - Registered callback.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 32390206 - Invalid parameter.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        on(type: 'dataReceived', callback: Callback<ArrayBuffer>): void;
        /**
         * Unregisters the listener for **dataReceived** events.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'dataReceived' } type - Event type, which is **dataReceived**. This event is triggered when data is
         *     received.
         * @param { Callback<ArrayBuffer> } [callback] - Registered callback.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 32390206 - Invalid parameter.
         * @syscap SystemCapability.DistributedSched.AppCollaboration
         * @stagemodelonly
         * @since 20
         */
        off(type: 'dataReceived', callback?: Callback<ArrayBuffer>): void;
    }
    /**
     * Creates a **Connection** object on the device that functions as the client. The device can then initiate connection
     * requests to the device that functions as the server.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { string } deviceId - Device ID of the peer device, that is, the BLE MAC address of the peer device. For
     *     details about how to obtain the BLE MAC address, see
     *     [BLE Advertising and Scanning](docroot://connectivity/bluetooth/ble-development-guide.md).
     * @param { string } name - Server name of the device to be connected. The value is a string of up to 255 bytes. It
     *     cannot be empty.
     * @returns { Connection } **Connection** object created.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported
     *     because the linkEnhance function has been trimmed. [since 26.0.0]
     * @throws { BusinessError } 32390206 - Invalid parameter.
     * @syscap SystemCapability.DistributedSched.AppCollaboration
     * @stagemodelonly
     * @since 20
     */
    function createConnection(deviceId: string, name: string): Connection;
}
export default linkEnhance;

```
