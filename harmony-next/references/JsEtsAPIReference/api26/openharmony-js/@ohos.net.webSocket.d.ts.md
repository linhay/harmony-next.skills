# @ohos.net.webSocket.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2026 Huawei Device Co., Ltd.
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
 * @file WebSocket Connection
 * @kit NetworkKit
 */
import type { AsyncCallback, ErrorCallback, Callback } from './@ohos.base';
import type connection from './@ohos.net.connection';
/**
 * Provides WebSocket clients and servers for third-party applications to implement bidirectional connections between
 * the client and server.
 *
 * On the WebSocket client: You can use WebSocket to establish a bidirectional connection between the server and client.
 * Before doing this, you need to use the [createWebSocket]{@link webSocket.createWebSocket} API to create a
 * [WebSocket]{@link webSocket.WebSocket} object and then use the
 * [connect]{@link webSocket.WebSocket.connect(url: string, callback: AsyncCallback<boolean>)} API to connect to the
 * server. If the connection is successful, the client will receive a callback of the
 * [open]{@link webSocket.WebSocket.on(type: 'open', callback: AsyncCallback<Object>)} event. Then, the client can
 * communicate with the server using the
 * [send]{@link webSocket.WebSocket.send(data: string | ArrayBuffer, callback: AsyncCallback<boolean>)} API. When the
 * server sends a message to the client, the client will receive a callback of the
 * [message]{@link webSocket.WebSocket.on(type: 'message', callback: AsyncCallback<string | ArrayBuffer>)} event. If the
 * connection is no longer needed, the client can call the
 * [close]{@link webSocket.WebSocket.close(callback: AsyncCallback<boolean>)} API to close the connection. After
 * successful disconnection, the client will receive a callback of the
 * [close]{@link webSocket.WebSocket.on(type: 'close', callback: AsyncCallback<CloseResult>)} event. If an error occurs
 * in any of the preceding processes, the client will receive a callback of the
 * [error]{@link webSocket.WebSocket.on(type: 'error', callback: ErrorCallback)} event.
 *
 * On the WebSocket server: Use the [createWebSocketServer]{@link webSocket.createWebSocketServer} method to create a
 * [WebSocketServer]{@link webSocket.WebSocketServer} object, and then use the
 * [start]{@link webSocket.WebSocketServer.start} method to start the server and listen to the link setup request
 * message from the client. (The API version 23 and later versions support all devices. In earlier versions, only TV
 * devices are supported.) If the connection is successful, the server receives the callback of the
 * [connect]{@link webSocket.WebSocketServer.on(type: 'connect', callback: Callback<WebSocketConnection>)} event. The
 * server can then communicate with the client by using the [send]{@link webSocket.WebSocketServer.send} API or obtain
 * information about all connected clients by using the
 * [listAllConnections]{@link webSocket.WebSocketServer.listAllConnections} API. When the client sends a message to the
 * server, the server receives the callback of the
 * [messageReceive]{@link webSocket.WebSocketServer.on(type: 'messageReceive', callback: Callback<WebSocketMessage>)}
 * event. If the connection is no longer needed, the server can call the [close]{@link webSocket.WebSocketServer.close}
 * API to close the connection. After successful disconnection, the server will receive a callback of the
 * [close]{@link webSocket.WebSocketServer.on(type: 'close', callback: ClientConnectionCloseCallback)} event. To stop
 * the service, the server can use the [stop]{@link webSocket.WebSocketServer.stop} API. If an error occurs in any of
 * the preceding processes, the server will receive a callback of the
 * [error]{@link webSocket.WebSocketServer.on(type: 'error', callback: ErrorCallback)} event.
 *
 * @syscap SystemCapability.Communication.NetStack
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 6
 */
declare namespace webSocket {
    /**
     * Defines the global HTTP proxy configuration of the network.
     *
     * @syscap SystemCapability.Communication.NetManager.Core
     * @crossplatform [since 24]
     * @since 12
     */
    type HttpProxy = connection.HttpProxy;
    /**
     * Creates a **WebSocket** object, which provides methods to create or close a WebSocket connection, send data over
     * the connection, and enable or disable listening for the **open**, **close**, **message**, and **error** events.
     *
     * @returns { WebSocket } A **WebSocket** object, which contains the **connect**, **send**, **close**, **on**, or
     *     **off** method.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    function createWebSocket(): WebSocket;
    /**
     * Defines the optional parameters carried in the request for establishing a WebSocket connection.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export interface WebSocketRequestOptions {
        /**
         * Header carrying optional parameters in the request for establishing a WebSocket connection. You can customize the
         * parameter or leave it unspecified.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        header?: Object;
        /**
         * Path of CA certificates. If a path is set, the system uses the CA certificates in this path. If a path is not
         * set, the system uses the preset CA certificate, namely, **\/etc/ssl/certs/cacert.pem**. This path is the sandbox
         * mapping path, which can be obtained by using **UIAbilityContext** APIs. Currently, only text certificates in PEM
         * format are supported.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        caPath?: string;
        /**
         * Whether to skip server certificate verification. The value **true** means to skip server certificate
         * verification, and the value **false** means the opposite. Default value: **false**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 20
         */
        skipServerCertVerification?: boolean;
        /**
         * Client certificate.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        clientCert?: ClientCert;
        /**
         * Proxy configuration. By default, the system network proxy is used.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        proxy?: ProxyConfiguration;
        /**
         * Custom **Sec-WebSocket-Protocol** field. The default value is "".
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        protocol?: string;
        /**
         * Custom [heartbeat detection interval](docroot://network/websocket-connection.md). The default value is 30s.
         * Heartbeat detection is initiated at the specified interval. If the value is set to **0**, heartbeat detection is
         * disabled. The maximum value is 30000s, and the minimum value is 0s.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 21
         */
        pingInterval?: number;
        /**
         * Timeout interval for disconnecting a connection after heartbeat detection is initiated. The default value is 30s.
         * If no response is received during the specified interval, the connection is disconnected. The maximum value is 30
         * 000s, and the minimum value is 0s. **pongTimeout** must be less than or equal to **pingInterval**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 21
         */
        pongTimeout?: number;
        /**
         * Custom minimum TLS version supported. For example, if this parameter is set to **TLS_V_1_1**, the client supports
         * TLS 1.1, TLS 1.2, and TLS 1.3.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        minSupportTlsProtocol?: TlsProtocol;
        /**
         * The option of supporting origin port.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        supportOriginPort?: boolean;
    }
    /**
     * Represents the HTTP proxy configuration.
     *
     * @unionmember { 'system' } The default network proxy is used.
     * @unionmember { 'no-proxy' } No network proxy is used.
     * @unionmember { HttpProxy } The specified network proxy is used.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 12
     */
    export type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy;
    /**
     * Defines the client certificate type.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    export interface ClientCert {
        /**
         * Path of the certificate file.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        certPath: string;
        /**
         * Path of the certificate key file.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        keyPath: string;
        /**
         * Password of the certificate key file. The default value is an empty string.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        keyPassword?: string;
    }
    /**
     * Defines the optional parameters carried in the request for closing a WebSocket connection.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export interface WebSocketCloseOptions {
        /**
         * Error code. Set this parameter based on the actual situation. The value must be a positive integer ranging from 1
         * 000 to 1015. If no error code is specified or the input value is not within the preceding range, the code will be
         * set to the default value **1000**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        code?: number;
        /**
         * Error cause. Set this parameter based on the actual situation. If no reason value is specified, the reason value
         * is set to the default value **CLOSE_NORMAL**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        reason?: string;
    }
    /**
     * Represents the result obtained from the **close** event reported when the WebSocket connection is closed.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    export interface CloseResult {
        /**
         * Error code for closing the connection.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        code: number;
        /**
         * Error cause for closing the connection.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        reason: string;
    }
    /**
     * The result for open info of a WebSocket connection.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @stagemodelonly
     * @since 26.0.0
     */
    export interface WebSocketOpenInfo {
        /**
         * result status.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        status: number;
        /**
         * result message.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        message: string;
        /**
         * Negotiated protocol.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        protocol?: string;
    }
    /**
     * Enumerates the response headers sent by the server.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 12
     */
    export type ResponseHeaders = {
        [k: string]: string | string[] | undefined;
    };
    /**
     * Defines a **WebSocket** object. Before invoking WebSocket APIs, you need to call
     * [webSocket.createWebSocket]{@link webSocket.createWebSocket} to create a **WebSocket** object.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export interface WebSocket {
        /**
         * Initiates a WebSocket request to establish a WebSocket connection to a given URL. This API uses an asynchronous
         * callback to return the result.
         *
         * > **NOTE**
         * >
         * > The boolean value returned in the callback indicates only whether the connection request is created
         * > successfully. To detect whether the WebSocket connection is successful, you need to subscribe to the **open**
         * > event via [on('open')]{@link webSocket.WebSocket.on(type: 'open', callback: AsyncCallback<Object>)} before
         * > calling this API.
         * > > **NOTE**
         * >
         * > The URL cannot contain more than 1024 characters. Otherwise, the connection fails. Since API version 15, the
         * > maximum length of URLs is changed from 1024 characters to 2048 characters. Since API version 26, the maximum
         * > length of URLs is changed from 2048 characters to 8196 characters.
         *
         * @permission ohos.permission.INTERNET
         * @param { string } url - URL for establishing a WebSocket connection.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** indicates
         *     that the operation is successful, and the value **false** indicates the opposite.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2302999 - Websocket other unknown error. [since 10]
         * @throws { BusinessError } 2302001 - Websocket url error. [since 12]
         * @throws { BusinessError } 2302002 - Websocket certificate file does not exist. [since 12]
         * @throws { BusinessError } 2302003 - Websocket connection already exists. [since 12]
         * @throws { BusinessError } 2302998 - It is not allowed to access this domain. [since 12]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        connect(url: string, callback: AsyncCallback<boolean>): void;
        /**
         * Initiates a WebSocket request to establish a WebSocket connection to a given URL. This API uses an asynchronous
         * callback to return the result.
         *
         * > **NOTE**
         * >
         * > The boolean value returned in the callback indicates only whether the connection request is created
         * > successfully. To detect whether the WebSocket connection is successful, you need to subscribe to the **open**
         * > event via [on('open')]{@link webSocket.WebSocket.on(type: 'open', callback: AsyncCallback<Object>)} before
         * > calling this API.
         * > > **NOTE**
         * >
         * > The URL cannot contain more than 1024 characters. Otherwise, the connection fails. Since API version 15, the
         * > maximum length of URLs is changed from 1024 characters to 2048 characters. Since API version 26, the maximum
         * > length of URLs is changed from 2048 characters to 8196 characters.
         *
         * @permission ohos.permission.INTERNET
         * @param { string } url - URL for establishing a WebSocket connection.
         * @param { WebSocketRequestOptions } options - Request options. For details, see
         *     [WebSocketRequestOptions]{@link webSocket.WebSocketRequestOptions}.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** indicates
         *     that the operation is successful, and the value **false** indicates the opposite.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2302999 - Websocket other unknown error. [since 10]
         * @throws { BusinessError } 2302001 - Websocket url error. [since 12]
         * @throws { BusinessError } 2302002 - Websocket certificate file does not exist. [since 12]
         * @throws { BusinessError } 2302003 - Websocket connection already exists. [since 12]
         * @throws { BusinessError } 2302998 - It is not allowed to access this domain. [since 12]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void;
        /**
         * Establishes a WebSocket connection to a given URL. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > The boolean value returned in the callback indicates only whether the connection request is created
         * > successfully. To detect whether the WebSocket connection is successful, you need to subscribe to the **open**
         * > event via [on('open')]{@link webSocket.WebSocket.on(type: 'open', callback: AsyncCallback<Object>)} before
         * > calling this API.
         * > > **NOTE**
         * >
         * > The URL cannot contain more than 1024 characters. Otherwise, the connection fails. Since API version 15, the
         * > maximum length of URLs is changed from 1024 characters to 2048 characters. Since API version 26, the maximum
         * > length of URLs is changed from 2048 characters to 8196 characters.
         *
         * @permission ohos.permission.INTERNET
         * @param { string } url - URL for establishing a WebSocket connection.
         * @param { WebSocketRequestOptions } options - Request options. For details, see
         *     [WebSocketRequestOptions]{@link webSocket.WebSocketRequestOptions}.
         * @returns { Promise<boolean> } Callback used to return the result. The value **true** indicates that the operation
         *     is successful, and the value **false** indicates the opposite.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2302999 - Websocket other unknown error. [since 10]
         * @throws { BusinessError } 2302001 - Websocket url error. [since 12]
         * @throws { BusinessError } 2302002 - Websocket certificate file does not exist. [since 12]
         * @throws { BusinessError } 2302003 - Websocket connection already exists. [since 12]
         * @throws { BusinessError } 2302998 - It is not allowed to access this domain. [since 12]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>;
        /**
         * Sends data through a WebSocket connection. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @param { string | ArrayBuffer } data - Data to send.
         *     <br>Only the string type is supported for API version 6 or earlier. Both the string and ArrayBuffer types are
         *     supported for API version 8 or later. A maximum of 5,242,864 bytes (that is, 5 x 1024 x 1024 - 16) can be
         *     sent. If the data size exceeds the upper limit, error code 401 will be returned.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** indicates
         *     that the operation is successful, and the value **false** indicates the opposite.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        send(data: string | ArrayBuffer, callback: AsyncCallback<boolean>): void;
        /**
         * Sends data through the WebSocket connection. This API uses a promise to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @param { string | ArrayBuffer } data - Data to send.
         *     <br>Only the string type is supported for API version 6 or earlier. Both the string and ArrayBuffer types are
         *     supported for API version 8 or later. A maximum of 5,242,864 bytes (that is, 5 x 1024 x 1024 - 16) can be
         *     sent. If the data size exceeds the upper limit, error code 401 will be returned.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the operation
         *     is successful, and the value **false** indicates the opposite.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        send(data: string | ArrayBuffer): Promise<boolean>;
        /**
         * Closes the WebSocket connection. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** indicates
         *     that the operation is successful, and the value **false** indicates the opposite.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        close(callback: AsyncCallback<boolean>): void;
        /**
         * Closes the WebSocket connection based on the options parameter. This API uses an asynchronous callback to return
         * the result.
         *
         * @permission ohos.permission.INTERNET
         * @param { WebSocketCloseOptions } options - Request options. For details, see
         *     [WebSocketCloseOptions]{@link webSocket.WebSocketCloseOptions}.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** indicates
         *     that the operation is successful, and the value **false** indicates the opposite.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        close(options: WebSocketCloseOptions, callback: AsyncCallback<boolean>): void;
        /**
         * Closes a WebSocket connection based on the specified options. This API uses a promise to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @param { WebSocketCloseOptions } options - Request options. For details, see
         *     [WebSocketCloseOptions]{@link webSocket.WebSocketCloseOptions}.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the operation
         *     is successful, and the value **false** indicates the opposite.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        close(options?: WebSocketCloseOptions): Promise<boolean>;
        /**
         * Subscribes to WebSocket open events. This API uses an asynchronous callback to return the result. This event
         * indicates whether the WebSocket connection is successful. This API must be called before
         * [connect]{@link webSocket.WebSocket.connect(url: string, callback: AsyncCallback<boolean>)} is called to initiate
         * a connection request.
         *
         * @param { 'open' } type - Event type.<br/> **open**: event indicating that a WebSocket connection has been opened.
         * @param { AsyncCallback<Object> } callback - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        on(type: 'open', callback: AsyncCallback<Object>): void;
        /**
         * Unsubscribes from WebSocket open events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
         * > If you do not pass the callback, you will cancel listening for all events.
         *
         * @param { 'open' } type - Event type.<br /> **open**: event indicating that a WebSocket connection has been
         *     opened.
         * @param { AsyncCallback<Object> } callback - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        off(type: 'open', callback?: AsyncCallback<Object>): void;
        /**
         * Subscribes to WebSocket server message receiving events. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > The data in **AsyncCallback** can be in the format of string (API version 6) or ArrayBuffer (API version 8).
         *
         * @param { 'message' } type - Event type.<br/> **message**: event indicating that a message has been received from
         *     the server.
         * @param { AsyncCallback<string | ArrayBuffer> } callback - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        on(type: 'message', callback: AsyncCallback<string | ArrayBuffer>): void;
        /**
         * Enables listening for the open info events of a WebSocket connection.
         *
         * @param { 'openInfo' } type - event indicating that the open info of a WebSocket connection is returned.
         * @param { AsyncCallback<WebSocketOpenInfo> } callback - the callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        on(type: 'openInfo', callback: AsyncCallback<WebSocketOpenInfo>): void;
        /**
         * Cancels listening for the open info events of a WebSocket connection.
         *
         * @param { 'openInfo' } type - event indicating that the open info of a WebSocket connection is returned.
         * @param { AsyncCallback<WebSocketOpenInfo> } [callback] - the callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        off(type: 'openInfo', callback?: AsyncCallback<WebSocketOpenInfo>): void;
        /**
         * Unsubscribes from WebSocket server message receiving events. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > The data in **AsyncCallback** can be in the format of string (API version 6) or ArrayBuffer (API version 8).
         * >
         * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
         * > If you do not pass the callback, you will cancel listening for all events.
         *
         * @param { 'message' } type - Event type.<br /> **message**: event indicating that a message has been received from
         *     the server.
         * @param { AsyncCallback<string | ArrayBuffer> } callback - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        off(type: 'message', callback?: AsyncCallback<string | ArrayBuffer>): void;
        /**
         * Subscribes to WebSocket close events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'close' } type - Event type.<br/> **close**: event indicating that a WebSocket connection has been
         *     closed.
         * @param { AsyncCallback<CloseResult> } callback - Callback used to return the result.
         *     <br>**close** and **reason** indicate the error code and error cause for closing the connection,
         *     respectively.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        on(type: 'close', callback: AsyncCallback<CloseResult>): void;
        /**
         * Unsubscribes from WebSocket close events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
         * > If you do not pass the callback, you will cancel listening for all events.
         *
         * @param { 'close' } type - Event type.<br /> **close**: event indicating that a WebSocket connection has been
         *     closed.
         * @param { AsyncCallback<CloseResult> } callback - Callback used to return the result.
         *     <br>**close** and **reason** indicate the error code and error cause for closing the connection,
         *     respectively.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        off(type: 'close', callback?: AsyncCallback<CloseResult>): void;
        /**
         * Subscribes to WebSocket error events. This API uses an asynchronous callback to return the result.
         *
         * The error code of the [error]{@link webSocket.WebSocket.on(type: 'error', callback: ErrorCallback)} event
         * callback is described as follows: WebSocket is essentially an HTTP protocol upgrade. If the server agrees to the
         * upgrade, the server returns 101. The status code indicates that the protocol is switched from HTTP to WebSocket (
         * the **open** callback is triggered). If the server rejects the upgrade or other exceptions occur, the server
         * returns 200, indicating that the server only processes the request as a common HTTP request.
         *
         * @param { 'error' } type - Event type.<br/> **error**: event indicating the WebSocket connection has encountered
         *     an error.
         * @param { ErrorCallback } callback - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from WebSocket error events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
         * > If you do not pass the callback, you will cancel listening for all events.
         *
         * @param { 'error' } type - Event type.<br /> **error**: event indicating the WebSocket connection has encountered
         *     an error.
         * @param { ErrorCallback } callback - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Subscribes to the WebSocket data receiving end event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'dataEnd' } type - Event type.<br/> **dataEnd**: event indicating the data receiving over the WebSocket
         *     connection has ended.
         * @param { Callback<void> } callback - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'dataEnd', callback: Callback<void>): void;
        /**
         * Unsubscribes from WebSocket data receiving end events. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
         * > If you do not pass the callback, you will cancel listening for all events.
         *
         * @param { 'dataEnd' } type - Event type.<br /> **dataEnd**: event indicating the data receiving over the WebSocket
         *     connection has ended.
         * @param { Callback<void> } [ callback ] - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'dataEnd', callback?: Callback<void>): void;
        /**
         * Subscribes to HTTP response header events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'headerReceive'} type - Event type.<br/> Event type. The value is **headerReceive**.
         * @param { Callback<ResponseHeaders> } callback - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        on(type: 'headerReceive', callback: Callback<ResponseHeaders>): void;
        /**
         * Unsubscribes from HTTP response header events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
         * > If you do not pass the callback, you will cancel listening for all events.
         *
         * @param { 'headerReceive' } type - Event type.<br /> Event type. The value is **headerReceive**.
         * @param { Callback<ResponseHeaders> } [callback] - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        off(type: 'headerReceive', callback?: Callback<ResponseHeaders>): void;
    }
    /**
     * Creates a **WebSocketServer** object, which provides methods to start or stop the WebSocketServer service, send
     * data over the connection, close the connection, list all connections, and enable or disable listening for the
     * **open**, **close**, **message**, and **error** events.
     *
     * > **NOTE**
     * >
     * > Supported on all devices since API version 23. In earlier versions, this method is supported only on TV devices.
     *
     * @returns { WebSocketServer } **WebSocketServer** object, which provides the **start**, **listAllConnections**,
     *     **send**, **close**, **stop**, **on**, and **off** methods.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 23]
     * @since 19
     */
    function createWebSocketServer(): WebSocketServer;
    /**
     * Defines the WebSocketServer configuration.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 19
     */
    export interface WebSocketServerConfig {
        /**
         * Maximum number of connections for each client. The default value is **10**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        maxConnectionsForOneClient: number;
        /**
         * Maximum number of concurrent clients. When the number of concurrent clients reaches the maximum, the server
         * rejects new connections. The default value is **10**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        maxConcurrentClientsNumber: number;
        /**
         * Port of the WebSocketServer.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        serverPort: number;
        /**
         * IP address of the WebSocketServer. The default value is **0.0.0.0**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        serverIP?: string;
        /**
         * Certificate information, which includes the paths of the WebSocketServer certificate file and private key file.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        serverCert?: ServerCert;
        /**
         * Custom protocol.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        protocol?: string;
    }
    /**
     * Certificate information, which includes the paths of the WebSocketServer certificate file and private key file.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 19
     */
    export interface ServerCert {
        /**
         * Path of the server certificate file.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        certPath: string;
        /**
         * Path of the private key file of the server certificate.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        keyPath: string;
    }
    /**
     * Client information, including the IP address and port number.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 19
     */
    export interface WebSocketConnection {
        /**
         * IP address of the client.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        clientIP: string;
        /**
         * Port number of the client.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        clientPort: number;
    }
    /**
     * Callback used to return the result, which contains:
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 19
     */
    export interface WebSocketMessage {
        /**
         * Client information, including the IP address and port number.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        clientConnection: WebSocketConnection;
        /**
         * Message data sent by the client.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        data: string | ArrayBuffer;
    }
    /**
     * Callback invoked when the WebSocketServer connection is closed.
     *
     * @param { WebSocketConnection } clientConnection - the connection which is closed.
     * @param { CloseResult } closeReason - the error code and reason why the connection is closed.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 19
     */
    export type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason: CloseResult) => void;
    /**
     * Defines a **WebSocketServer** object. You need to use
     * [webSocket.createWebSocketServer]{@link webSocket.createWebSocketServer} to create a **WebSocketServer** object
     * before using its methods.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 19
     */
    export interface WebSocketServer {
        /**
         * Starts the WebSocketServer service based on the specified **config**. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > You are advised not to listen for the same port when calling this API multiple times.
         * > **Required permission**: ohos.permission.INTERNET
         *
         * @permission ohos.permission.INTERNET
         * @param { WebSocketServerConfig } config - Starts the WebSocket server.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the operation
         *     is successful, and the value **false** indicates the opposite.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2302002 - Websocket certificate file does not exist.
         * @throws { BusinessError } 2302004 - Can't listen on the given NIC.
         * @throws { BusinessError } 2302005 - Can't listen on the given Port.
         * @throws { BusinessError } 2302999 - Websocket other unknown error.
         * @throws { BusinessError } 2302007 - Websocket port already occupied. [since 24]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        start(config: WebSocketServerConfig): Promise<boolean>;
        /**
         * Stops the WebSocketServer service. This API uses a promise to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the operation
         *     is successful, and the value **false** indicates the opposite.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        stop(): Promise<boolean>;
        /**
         * Obtains information about all clients connected to the server.
         *
         * **Required permission**: ohos.permission.INTERNET
         *
         * > **NOTE**
         * >
         * > This API is called asynchronously. The **await** keyword needs to be used to wait until the asynchronous
         * > operation is complete, ensuring that information about all clients connected to the server can be correctly
         * > obtained.
         *
         * @permission ohos.permission.INTERNET
         * @returns { WebSocketConnection[] } an array consists connections from all clients.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        listAllConnections(): WebSocketConnection[];
        /**
         * Sends data through the WebSocket connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > The **send** API can be called only after a **connect** event is listened.
         * > **Required permission**: ohos.permission.INTERNET
         *
         * @permission ohos.permission.INTERNET
         * @param { string | ArrayBuffer } data - Data to send, which can be of the string or ArrayBuffer type. A maximum of
         *     5,242,864 bytes (that is, 5 x 1024 x 1024 - 16) can be sent. If the data size exceeds the upper limit, error
         *     code 401 will be returned.
         * @param { WebSocketConnection } connection - Client information.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the operation
         *     is successful, and the value **false** indicates the opposite.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2302006 - websocket connection does not exist.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        send(data: string | ArrayBuffer, connection: WebSocketConnection): Promise<boolean>;
        /**
         * Closes a WebSocket connection. This API uses a promise to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @param { WebSocketConnection } connection - Client information, including the IP address and port number.
         * @param { webSocket.WebSocketCloseOptions } options - Optional parameters carried in the request for closing a
         *     WebSocket connection.
         *     <br>By default, the error code is 200, and the cause is **Websocket connect failed**.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the operation
         *     is successful, and the value **false** indicates the opposite.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2302006 - websocket connection does not exist.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        close(connection: WebSocketConnection, options?: webSocket.WebSocketCloseOptions): Promise<boolean>;
        /**
         * Subscribes to the WebSocketServer connection event (the connection between the client and server is successfully
         * established). This API uses an asynchronous callback to return the result.
         *
         * @param { 'connect' } type - Event type, which has a fixed value of **connect**. Successful calling of
         *     **onconnect()** indicates that a connection is established between the client and server.
         * @param { Callback<WebSocketConnection> } callback - Callback used to return the information about connected
         *     clients.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        on(type: 'connect', callback: Callback<WebSocketConnection>): void;
        /**
         * Unsubscribes from WebSocketServer connection events (the connection between the client and server is successfully
         * established). This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
         * > If you do not pass the callback, you will cancel listening for all events.
         *
         * @param { 'connect' } type - Event type, which has a fixed value of **connect**. Successful calling of
         *     **offconnect()** indicates that listening for connection events is canceled successful.
         * @param { Callback<WebSocketConnection> } callback - Callback used to return the information about connected
         *     clients.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        off(type: 'connect', callback?: Callback<WebSocketConnection>): void;
        /**
         * Subscribes to the WebSocketServer event of receiving client messages. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'messageReceive' } type - Event type, which has a fixed value of **messageReceive**. Successful calling
         *     of **onmessageReceive()** indicates that a message is received from the client.
         * @param { Callback<WebSocketMessage> } callback - Callback used to return the result.
         *     <br>**clientconnection** indicates the client information and **data** indicates the data message sent by the
         *     client.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        on(type: 'messageReceive', callback: Callback<WebSocketMessage>): void;
        /**
         * Unsubscribes from the WebSocketServer event of receiving client messages. This API uses an asynchronous callback
         * to return the result.
         *
         * > **NOTE**
         * >
         * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
         * > If you do not pass the callback, you will cancel listening for all events.
         *
         * @param { 'messageReceive' } type - Event type, which has a fixed value of **messageReceive**. Successful calling
         *     of **offmessageReceive()** indicates that listening for **messageReceive** events is canceled successfully.
         * @param { Callback<WebSocketMessage> } callback - Callback used to return the result, which contains:
         *     <br>- **clientconnection**: client information.
         *     <br>- **data**: data sent by the client.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        off(type: 'messageReceive', callback?: Callback<WebSocketMessage>): void;
        /**
         * Subscribes to WebSocketServer close events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'close' } type - Event type, which has a fixed value of **close**. Successful calling of **onclose()**
         *     indicates that the connection is closed successfully.
         * @param { ClientConnectionCloseCallback } callback - Callback used to return the result.
         *     <br>**close** and **reason** indicate the error code and error cause for closing the connection,
         *     respectively.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        on(type: 'close', callback: ClientConnectionCloseCallback): void;
        /**
         * Unsubscribes from WebSocketServer close events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
         * > If you do not pass the callback, you will cancel listening for all events.
         *
         * @param { 'close' } type - Event type, which has a fixed value of **close**. Successful calling of **offclose()**
         *     indicates that listening for the **close** events is canceled successfully.
         * @param { ClientConnectionCloseCallback } callback - Callback used to return the result.
         *     <br>**close** and **reason** indicate the error code and error cause for closing the connection,
         *     respectively.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        off(type: 'close', callback?: ClientConnectionCloseCallback): void;
        /**
         * Subscribes to WebSocketServer error events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'error' } type - Event type, which has a fixed value of **error**. Successful calling of **onerror()**
         *     indicates that an error has occurred.
         * @param { ErrorCallback } callback - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from WebSocketServer error events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event.
         * > If you do not pass the callback, you will cancel listening for all events.
         *
         * @param { 'error' } type - Event type, which has a fixed value of **error**. Successful calling of **offerror()**
         *     indicates that listening for the **error** events is canceled successfully.
         * @param { ErrorCallback } callback - Callback used to return the error code (default value: **200**).
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 19
         */
        off(type: 'error', callback?: ErrorCallback): void;
    }
    /**
     * Enumerates the TLS protocol types.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @stagemodelonly
     * @since 26.0.0
     */
    export enum TlsProtocol {
        /**
         * TLS version 1.0.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        TLS_V_1_0 = 0,
        /**
         * TLS version 1.1.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        TLS_V_1_1 = 1,
        /**
         * TLS version 1.2.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        TLS_V_1_2 = 2,
        /**
         * TLS version 1.3.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        TLS_V_1_3 = 3
    }
}
export default webSocket;

```
