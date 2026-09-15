# @ohos.net.socket.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2026 Huawei Device Co., Ltd.
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
 * @file Socket Connection
 * @kit NetworkKit
 */
import type { AsyncCallback, Callback, ErrorCallback } from './@ohos.base';
import connection from "./@ohos.net.connection";
import type cert from './@ohos.security.cert';
/**
 * The **socket** module implements data transfer over TCP, UDP, Web, and TLS socket connections.
 *
 * > **NOTE**
 * >
 * > You are advised to call the APIs of this module in the worker thread or taskpool to perform network-related
 * > operations. Otherwise, the UI thread may be suspended.
 *
 * @syscap SystemCapability.Communication.NetStack
 * @crossplatform [since 10]
 * @since 7
 */
declare namespace socket {
    /**
     * Define a network address.
     * @syscap SystemCapability.Communication.NetStack
     * @stagemodelonly
     * @crossplatform [since 24]
     * @since 8
     */
    export import NetAddress = connection.NetAddress;
    /**
     * Defines the certificate raw data.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 9
     */
    export type X509CertRawData = cert.EncodingBlob;
    /**
     * Creates a **UDPSocket** object.
     *
     * @returns { UDPSocket } **UDPSocket** object.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 7
     */
    function constructUDPSocketInstance(): UDPSocket;
    /**
     * Creates a **MulticastSocket** object.
     *
     * @returns { MulticastSocket } **MulticastSocket** object.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    function constructMulticastSocketInstance(): MulticastSocket;
    /**
     * Creates a **TCPSocket** object.
     *
     * @returns { TCPSocket } **TCPSocket** object.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 7
     */
    function constructTCPSocketInstance(): TCPSocket;
    /**
     * Creates a **TLSSocket** object.
     *
     * @returns { TLSSocket } **TLSSocket** object.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 9
     */
    function constructTLSSocketInstance(): TLSSocket;
    /**
     * Upgrades a **TCPSocket** connection to a **TLSSocket** connection.
     *
     * > **NOTE**
     * >
     * > Before calling **constructTLSSocketInstance**, ensure that a **TCPSocket** connection has been established and no
     * > data is transmitted. After a successful upgrade, you do not need to call the **close** API for the **TCPSocket**
     * > object.
     *
     * @param { TCPSocket } tcpSocket - **TCPSocket** connection to be upgraded.
     * @returns { TLSSocket } **TLSSocket** object.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2300002 - System internal error.
     * @throws { BusinessError } 2303601 - Invalid socket FD.
     * @throws { BusinessError } 2303602 - Socket is not connected.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 12
     */
    function constructTLSSocketInstance(tcpSocket: TCPSocket): TLSSocket;
    /**
     * Creates a **TCPSocketServer** object.
     *
     * @returns { TCPSocketServer } **TCPSocketServer** object.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 10
     */
    function constructTCPSocketServerInstance(): TCPSocketServer;
    /**
     * Creates a **TLSSocketServer** object.
     *
     * @returns { TLSSocketServer } **TLSSocketServer** object.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 10
     */
    function constructTLSSocketServerInstance(): TLSSocketServer;
    /**
     * Creates a **LocalSocket** object.
     *
     * @returns { LocalSocket } **LocalSocket** object.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    function constructLocalSocketInstance(): LocalSocket;
    /**
     * Creates a **LocalSocketServer** object.
     *
     * @returns { LocalSocketServer } **LocalSocketServer** object.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    function constructLocalSocketServerInstance(): LocalSocketServer;
    /**
     * Defines the parameters for sending data over a UDP socket connection.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 7
     */
    export interface UDPSendOptions {
        /**
         * Data to send.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        data: string | ArrayBuffer;
        /**
         * Destination address.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        address: NetAddress;
        /**
         * Proxy option. By default, no proxy is used.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @since 18
         */
        proxy?: ProxyOptions;
    }
    /**
     * Enumerates socket proxy types.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform
     * @since 18
     */
    export enum ProxyTypes {
        /**
         * No proxy.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @since 18
         */
        NONE = 0,
        /**
         * SOCKS5 proxy.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @since 18
         */
        SOCKS5 = 1
    }
    /**
     * Defines the socket proxy information.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform
     * @since 18
     */
    export interface ProxyOptions {
        /**
         * Proxy type.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @since 18
         */
        type: ProxyTypes;
        /**
         * Proxy address.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @since 18
         */
        address: NetAddress;
        /**
         * User name. This field must be specified if the user password authentication mode is used.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @since 18
         */
        username?: string;
        /**
         * Password. This field must be specified if the user password authentication mode is used.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @since 18
         */
        password?: string;
    }
    /**
     * Defines base properties of the **LocalSocket** object.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 7
     */
    export interface ExtraOptionsBase {
        /**
         * Size of the RX buffer, in bytes. The value ranges from 0 to 262144. If this parameter is left unspecified or the
         * unspecified value exceeds the value range, the default value **8192** is used.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        receiveBufferSize?: number;
        /**
         * Size of the TX buffer, in bytes. The value ranges from 0 to 262144. If this parameter is left unspecified or the
         * unspecified value exceeds the value range, the default value **8192** is used.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        sendBufferSize?: number;
        /**
         * Whether to reuse addresses. The value **true** means to reuse addresses, and the value **false** means the
         * opposite.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        reuseAddress?: boolean;
        /**
         * Timeout duration of the local socket connection, in ms.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        socketTimeout?: number;
    }
    /**
     * Defines other properties of the **UDPSocket** object. This object is inherited from
     * [ExtraOptionsBase]{@link socket.ExtraOptionsBase}.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 7
     */
    export interface UDPExtraOptions extends ExtraOptionsBase {
        /**
         * Whether to send broadcast messages. The value **true** indicates that broadcast messages can be sent, and the
         * value **false** indicates the opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        broadcast?: boolean;
    }
    /**
     * Defines the status of the socket connection.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 7
     */
    export interface SocketStateBase {
        /**
         * Whether the connection is in the bound state. The value **true** indicates that the connection is in the bound
         * state, and the value **false** indicates the opposite.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        isBound: boolean;
        /**
         * Whether the connection is in the closed state. The value **true** indicates that the connection is in the closed
         * state, and the value **false** indicates the opposite.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        isClose: boolean;
        /**
         * Whether the connection is in the connected state. The value **true** indicates that the connection is in the
         * connected state, and the value **false** indicates the opposite.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        isConnected: boolean;
    }
    /**
     * Defines information about the socket connection.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 7
     */
    export interface SocketRemoteInfo {
        /**
         * Peer IP address.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        address: string;
        /**
         * Network protocol type.
         *
         * - IPv4
         * - IPv6
         *
         * The default value is **IPv4**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        family: 'IPv4' | 'IPv6';
        /**
         * Port number. The value ranges from **0** to **65535**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        port: number;
        /**
         * Length of the server response message, in bytes.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        size: number;
    }
    /**
     * Defines the data received by the client over a local socket connection.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    export interface LocalSocketMessageInfo {
        /**
         * Data received.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        message: ArrayBuffer;
        /**
         * Local socket connection address.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        address: string;
        /**
         * Data length.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        size: number;
    }
    /**
     * Defines the address of a local socket file. When the address is passed for binding, a socket file is created at
     * this address.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    export interface LocalAddress {
        /**
         * Address of the local socket file.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        address: string;
    }
    /**
     * Defines local socket connection parameters.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    export interface LocalConnectOptions {
        /**
         * Address of the local socket file.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        address: LocalAddress;
        /**
         * Timeout duration of the local socket connection, in ms. **Default value**: 0 You need to manually set this
         * parameter for your application. The recommended value is **5000**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        timeout?: number;
    }
    /**
     * Defines the request parameters for the **LocalSocket** object.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    export interface LocalSendOptions {
        /**
         * Data to be transmitted.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        data: string | ArrayBuffer;
        /**
         * Encoding format of the string.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        encoding?: string;
    }
    /**
     * Defines a UDP socket connection. Before calling UDPSocket APIs, you need to call
     * [socket.constructUDPSocketInstance]{@link socket.constructUDPSocketInstance} to create a **UDPSocket** object.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 7
     */
    export interface UDPSocket {
        /**
         * Binds the IP address and port number. The port number can be customized or randomly allocated by the system. This
         * API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @param { NetAddress } address - Local address. For details, see
         *     [NetAddress](docroot://reference/apis-network-kit/js-apis-socket.md#netaddress).
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, no
         *     value is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        bind(address: NetAddress, callback: AsyncCallback<void>): void;
        /**
         * Binds the IP address and port number. The port number can be customized or randomly allocated by the system. This
         * API uses a promise to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @param { NetAddress } address - Local address. For details, see
         *     [NetAddress](docroot://reference/apis-network-kit/js-apis-socket.md#netaddress).
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        bind(address: NetAddress): Promise<void>;
        /**
         * Obtains the local socket address of a **UDPSocket** connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** is successfully called.
         *
         * @returns { Promise<NetAddress> } Promise used to return the result.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        getLocalAddress(): Promise<NetAddress>;
        /**
         * Sends data over a UDP socket connection. This API uses an asynchronous callback to return the result.
         *
         * Before sending data, call
         * [UDPSocket.bind()]{@link socket.UDPSocket.bind(address: NetAddress, callback: AsyncCallback<void>)} to bind the
         * IP address and port. Call the API in the worker thread or taskpool thread as this operation is time-consuming.
         *
         * @permission ohos.permission.INTERNET
         * @param { UDPSendOptions } options - Parameters for sending data over a UDP socket connection. For details, see
         *     [UDPSendOptions]{@link socket.UDPSendOptions}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, no
         *     value is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2301206 - Socks5 failed to connect to the proxy server. [since 18]
         * @throws { BusinessError } 2301207 - Socks5 username or password is invalid. [since 18]
         * @throws { BusinessError } 2301208 - Socks5 failed to connect to the remote server. [since 18]
         * @throws { BusinessError } 2301209 - Socks5 failed to negotiate the authentication method. [since 18]
         * @throws { BusinessError } 2301210 - Socks5 failed to send the message. [since 18]
         * @throws { BusinessError } 2301211 - Socks5 failed to receive the message. [since 18]
         * @throws { BusinessError } 2301212 - Socks5 serialization error. [since 18]
         * @throws { BusinessError } 2301213 - Socks5 deserialization error. [since 18]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        send(options: UDPSendOptions, callback: AsyncCallback<void>): void;
        /**
         * Sends data over a UDP socket connection. This API uses a promise to return the result.
         *
         * Before sending data, call
         * [UDPSocket.bind()]{@link socket.UDPSocket.bind(address: NetAddress, callback: AsyncCallback<void>)} to bind the
         * IP address and port. Call the API in the worker thread or taskpool thread as this operation is time-consuming.
         *
         * @permission ohos.permission.INTERNET
         * @param { UDPSendOptions } options - Parameters for sending data over a UDP socket connection. For details, see
         *     [UDPSendOptions]{@link socket.UDPSendOptions}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2301206 - Socks5 failed to connect to the proxy server. [since 18]
         * @throws { BusinessError } 2301207 - Socks5 username or password is invalid. [since 18]
         * @throws { BusinessError } 2301208 - Socks5 failed to connect to the remote server. [since 18]
         * @throws { BusinessError } 2301209 - Socks5 failed to negotiate the authentication method. [since 18]
         * @throws { BusinessError } 2301210 - Socks5 failed to send the message. [since 18]
         * @throws { BusinessError } 2301211 - Socks5 failed to receive the message. [since 18]
         * @throws { BusinessError } 2301212 - Socks5 serialization error. [since 18]
         * @throws { BusinessError } 2301213 - Socks5 deserialization error. [since 18]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        send(options: UDPSendOptions): Promise<void>;
        /**
         * Closes a UDP socket connection. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        close(callback: AsyncCallback<void>): void;
        /**
         * Closes a UDP socket connection. This API uses a promise to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        close(): Promise<void>;
        /**
         * Obtains the status of the UDP socket connection. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @param { AsyncCallback<SocketStateBase> } callback - Callback used to return the result. If the operation is
         *     successful, the status of the UDP socket connection is returned. If the operation fails, an error message is
         *     returned.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        getState(callback: AsyncCallback<SocketStateBase>): void;
        /**
         * Obtains the status of the UDP socket connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<SocketStateBase> } Promise used to return the result.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        getState(): Promise<SocketStateBase>;
        /**
         * Sets other properties of the **UDPSocket** object. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @param { UDPExtraOptions } options - Other properties of the **UDPSocket** object. For details, see
         *     [UDPExtraOptions]{@link socket.UDPExtraOptions}.
         * @param { AsyncCallback<void> }callback - Callback used to return the result. If the operation is successful, no
         *     value is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        setExtraOptions(options: UDPExtraOptions, callback: AsyncCallback<void>): void;
        /**
         * Sets other properties of the **UDPSocket** object. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @param { UDPExtraOptions } options - Other properties of the **UDPSocket** object. For details, see
         *     [UDPExtraOptions]{@link socket.UDPExtraOptions}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        setExtraOptions(options: UDPExtraOptions): Promise<void>;
        /**
         * Subscribes to **message** events of the **UDPSocket** object. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<{ message: ArrayBuffer, remoteInfo: SocketRemoteInfo }> } callback - Callback used to return
         *     the result. [since 7 - 10]
         * @param { Callback<SocketMessageInfo> } callback - Callback used to return the result. [since 11]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        on(type: 'message', callback: Callback<SocketMessageInfo>): void;
        /**
         * Unsubscribes from **message** events of the **UDPSocket** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<{ message: ArrayBuffer, remoteInfo: SocketRemoteInfo }> } callback - Callback used to return
         *     the result. You can pass the callback of the **on** function if you want to cancel listening for a certain
         *     type of events. If you do not pass the callback, you will cancel listening for all events. [since 7 - 10]
         * @param { Callback<SocketMessageInfo> } callback - Callback used to return the result. You can pass the callback
         *     of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the
         *     callback, you will cancel listening for all events. [since 11]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        off(type: 'message', callback?: Callback<SocketMessageInfo>): void;
        /**
         * Subscribes to **listening** events or **close** events of the **UDPSocket** object. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'listening' | 'close' } type - Event type.<br/>
         *     <br>- **listening**: data packet message event.
         *     <br>- **close**: close event.
         * @param { Callback<void> } callback - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        on(type: 'listening' | 'close', callback: Callback<void>): void;
        /**
         * Unsubscribes from **listening** events or **close** events of the **UDPSocket** object. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { 'listening' | 'close' } type - Event type.
         *     <br>- **listening**: data packet message event.
         *     <br>- **close**: close event.
         * @param { Callback<void> } callback - Callback used to return the result. You can pass the callback of the **on**
         *     function if you want to cancel listening for a certain type of events. If you do not pass the callback, you
         *     will cancel listening for all events.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        off(type: 'listening' | 'close', callback?: Callback<void>): void;
        /**
         * Subscribes to **error** events of the **UDPSocket** object. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from **error** events of the **UDPSocket** object. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result. You can pass the callback of the **on**
         *     function if you want to cancel listening for a certain type of events. If you do not pass the callback, you
         *     will cancel listening for all events.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Obtains the UDPSocket file descriptor. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - This API can be called only after
         * > [bind]{@link socket.UDPSocket.bind(address: NetAddress, callback: AsyncCallback<void>)} is successfully called.
         * >
         * > - This API returns **-1** in abnormal cases such as bind exceptions or socket closed (for example, after close
         * > is called).
         * >
         * > - The lifecycle of the file descriptor is managed by the system. The application can use the
         * > [close]{@link socket.UDPSocket.close(callback: AsyncCallback<void>)} method to close the socket connection,
         * > instead of directly operating the file descriptor.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<number> } Promise used to return the socket file descriptor.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 23
         */
        getSocketFd(): Promise<number>;
    }
    /**
     * Defines a **MulticastSocket** connection. Before calling MulticastSocket APIs, you need to call
     * [socket.constructMulticastSocketInstance]{@link socket.constructMulticastSocketInstance} to create a
     * **MulticastSocket** object.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    export interface MulticastSocket extends UDPSocket {
        /**
         * Adds a member to a multicast group. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The IP addresses used for multicast belong to a specific range, for example, 224.0.0.0 to 239.255.255.255.
         * >
         * > A member in a multicast group can serve as a sender or a receiver. Data is transmitted in broadcast mode,
         * > regardless of the client or server.
         *
         * @permission ohos.permission.INTERNET
         * @param { NetAddress } multicastAddress - Destination address. For details, see
         *     [NetAddress](docroot://reference/apis-network-kit/js-apis-socket.md#netaddress).
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301022 - Invalid argument.
         * @throws { BusinessError } 2301088 - Not a socket.
         * @throws { BusinessError } 2301098 - Address in use.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void;
        /**
         * Adds a member to a multicast group. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > The IP addresses used for multicast belong to a specific range, for example, 224.0.0.0 to 239.255.255.255.
         * >
         * > A member in a multicast group can serve as a sender or a receiver. Data is transmitted in broadcast mode,
         * > regardless of the client or server.
         *
         * @permission ohos.permission.INTERNET
         * @param { NetAddress } multicastAddress - Destination address. For details, see
         *     [NetAddress](docroot://reference/apis-network-kit/js-apis-socket.md#netaddress).
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301088 - Not a socket.
         * @throws { BusinessError } 2301098 - Address in use.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        addMembership(multicastAddress: NetAddress): Promise<void>;
        /**
         * Drops a member from a multicast group. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The IP addresses used for multicast belong to a specific range, for example, 224.0.0.0 to 239.255.255.255.
         * >
         * > You can drop only a member that has been added to a multicast group by using
         * > [addMembership]{@link socket.MulticastSocket.addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>)}.
         *
         * @permission ohos.permission.INTERNET
         * @param { NetAddress } multicastAddress - Destination address. For details, see
         *     [NetAddress](docroot://reference/apis-network-kit/js-apis-socket.md#netaddress).
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301088 - Not a socket.
         * @throws { BusinessError } 2301098 - Address in use.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        dropMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void;
        /**
         * Drops a member from a multicast group. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > The IP addresses used for multicast belong to a specific range, for example, 224.0.0.0 to 239.255.255.255.
         * >
         * > You can drop only a member that has been added to a multicast group by using
         * > [addMembership]{@link socket.MulticastSocket.addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>)}.
         *
         * @permission ohos.permission.INTERNET
         * @param { NetAddress } multicastAddress - Destination address. For details, see
         *     [NetAddress](docroot://reference/apis-network-kit/js-apis-socket.md#netaddress).
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301088 - Not a socket.
         * @throws { BusinessError } 2301098 - Address in use.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        dropMembership(multicastAddress: NetAddress): Promise<void>;
        /**
         * Sets the time to live (TTL) for multicast packets. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > TTL is used to limit the maximum number of router hops for packet transmission on a network.
         * >
         * > The value ranges from 0 to 255. The default value is **1**.
         * >
         * > If the TTL value is **1**, multicast packets can be transmitted only to the host directly connected to the
         * > sender. If the TTL is set to a large value, multicast packets can be transmitted over a longer distance.
         * >
         * > This API is effective only after
         * > [addMembership]{@link socket.MulticastSocket.addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>)}
         * > is called.
         *
         * @param { number } ttl - TTL value. The value is of the number type.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301022 - Invalid argument.
         * @throws { BusinessError } 2301088 - Not a socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        setMulticastTTL(ttl: number, callback: AsyncCallback<void>): void;
        /**
         * Sets the TTL for multicast packets. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > TTL is used to limit the maximum number of router hops for packet transmission on a network.
         * >
         * > The value ranges from 0 to 255. The default value is **1**.
         * >
         * > If the TTL value is **1**, multicast packets can be transmitted only to the host directly connected to the
         * > sender. If the TTL is set to a large value, multicast packets can be transmitted over a longer distance.
         * >
         * > This API is effective only after
         * > [addMembership]{@link socket.MulticastSocket.addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>)}
         * > is called.
         *
         * @param { number } ttl - TTL value. The value is of the number type.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301022 - Invalid argument.
         * @throws { BusinessError } 2301088 - Not a socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        setMulticastTTL(ttl: number): Promise<void>;
        /**
         * Obtains the TTL for multicast packets. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > TTL is used to limit the maximum number of router hops for packet transmission on a network.
         * >
         * > The value ranges from 0 to 255. The default value is **1**.
         * >
         * > If the TTL value is **1**, multicast packets can be transmitted only to the host directly connected to the
         * > sender. If the TTL is set to a large value, multicast packets can be transmitted over a longer distance.
         * >
         * > This API is effective only after
         * > [addMembership]{@link socket.MulticastSocket.addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>)}
         * > is called.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301088 - Not a socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        getMulticastTTL(callback: AsyncCallback<number>): void;
        /**
         * Obtains the TTL for multicast packets. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > TTL is used to limit the maximum number of router hops for packet transmission on a network.
         * >
         * > The value ranges from 0 to 255. The default value is **1**.
         * >
         * > If the TTL value is **1**, multicast packets can be transmitted only to the host directly connected to the
         * > sender. If the TTL is set to a large value, multicast packets can be transmitted over a longer distance.
         * >
         * > This API is effective only after
         * > [addMembership]{@link socket.MulticastSocket.addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>)}
         * > is called.
         *
         * @returns { Promise<number> } Promise used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301088 - Not a socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        getMulticastTTL(): Promise<number>;
        /**
         * Sets the loopback mode flag for multicast communication. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > Use this API to enable or disable the loopback mode. By default, the loopback mode is enabled.
         * >
         * > The value **true** indicates that the host is allowed to receive the multicast packets sent by itself, and the
         * > value **false** indicates the opposite.
         * >
         * > This API is effective only after
         * > [addMembership]{@link socket.MulticastSocket.addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>)}
         * > is called.
         *
         * @param { boolean } flag - Whether to enable the loopback mode. The value **true** means to enable the loopback
         *     mode, and the value **false** means the opposite.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301088 - Not a socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        setLoopbackMode(flag: boolean, callback: AsyncCallback<void>): void;
        /**
         * Sets the loopback mode flag for multicast communication. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > Use this API to enable or disable the loopback mode. By default, the loopback mode is enabled.
         * >
         * > The value **true** indicates that the host is allowed to receive the multicast packets sent by itself, and the
         * > value **false** indicates the opposite.
         * >
         * > This API is effective only after
         * > [addMembership]{@link socket.MulticastSocket.addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>)}
         * > is called.
         *
         * @param { boolean } flag - Whether to enable the loopback mode. The value **true** means to enable the loopback
         *     mode, and the value **false** means the opposite.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301088 - Not a socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        setLoopbackMode(flag: boolean): Promise<void>;
        /**
         * Obtains the loopback mode flag for multicast communication. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > Use this API to check whether the loopback mode is enabled.
         * >
         * > The value **true** indicates that the loopback mode is enabled, and the value **false** indicates the opposite.
         * > When the loopback mode is disabled, the host does not receive the multicast packets sent by itself.
         * >
         * > This API is effective only after
         * > [addMembership]{@link socket.MulticastSocket.addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>)}
         * > is called.
         *
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** indicates
         *     that the loopback mode is enabled, and the value **false** indicates the opposite.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301088 - Not a socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        getLoopbackMode(callback: AsyncCallback<boolean>): void;
        /**
         * Obtains the loopback mode flag for multicast communication. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > Use this API to check whether the loopback mode is enabled.
         * >
         * > The value **true** indicates that the loopback mode is enabled, and the value **false** indicates the opposite.
         * > When the loopback mode is disabled, the host does not receive the multicast packets sent by itself.
         * >
         * > This API is effective only after
         * > [addMembership]{@link socket.MulticastSocket.addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>)}
         * > is called.
         *
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the loopback
         *     mode is enabled, and the value **false** indicates the opposite.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301088 - Not a socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        getLoopbackMode(): Promise<boolean>;
        /**
         * Obtains the file descriptor of the MulticastSocket. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - This API can be called only after
         * > [bind]{@link socket.UDPSocket.bind(address: NetAddress, callback: AsyncCallback<void>)} is successfully called.
         * >
         * > - This API returns **-1** in abnormal cases such as bind exceptions or socket closed (for example, after close
         * > is called).
         * >
         * > - The lifecycle of the file descriptor is managed by the system. The application can use the
         * > [close]{@link socket.UDPSocket.close(callback: AsyncCallback<void>)} method to close the socket connection,
         * > instead of directly operating the file descriptor.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<number> } Promise used to return the socket file descriptor.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @crossplatform [since 24]
         * @since 23
         */
        getSocketFd(): Promise<number>;
        /**
         * Sets whether the multicast socket supports address reuse. This API is called in synchronous mode.
         *
         * > **NOTE**
         * >
         * > This API is used to control whether to enable address reuse when a multicast socket is bound to a port.
         * >
         * > To bind an occupied port, ensure that the address reuse capability is enabled for the party that occupies the
         * > port. In addition, the service needs to call this API before calling
         * > [bind]{@link socket.UDPSocket.bind(address: NetAddress, callback: AsyncCallback<void>)} to enable the address
         * > reuse capability.
         *
         * @param { boolean } reuse - Whether to enable address reuse. **true** to enable, **false** otherwise.
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        setReuseAddress(reuse: boolean): void;
    }
    /**
     * Defines a **LocalSocket** object. Before calling LocalSocket APIs, you need to call
     * [socket.constructLocalSocketInstance]{@link socket.constructLocalSocketInstance} to create a **LocalSocket**
     * object.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    export interface LocalSocket {
        /**
         * Binds the address of a local socket file. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API explicitly binds the client to a local socket file based on the specified address.
         * >
         * > It is not mandatory in local socket communication.
         *
         * @param { LocalAddress } address - Local address. For details, see [LocalAddress]{@link socket.LocalAddress}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301013 - Insufficient permissions.
         * @throws { BusinessError } 2301022 - Invalid argument.
         * @throws { BusinessError } 2301098 - Address already in use.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        bind(address: LocalAddress): Promise<void>;
        /**
         * Connects to the specified socket file. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API allows you to connect to the TCP server without first executing **localsocket.bind**.
         *
         * @param { LocalConnectOptions } options - Local socket connection parameters. For details, see
         *     [LocalConnectOptions]{@link socket.LocalConnectOptions}.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301013 - Insufficient permissions.
         * @throws { BusinessError } 2301022 - Invalid argument.
         * @throws { BusinessError } 2301111 - Connection refused.
         * @throws { BusinessError } 2301099 - Cannot assign requested address.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        connect(options: LocalConnectOptions): Promise<void>;
        /**
         * Sends data over a local socket connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **connect** is successfully called.
         *
         * @param { LocalSendOptions } options - Parameters for sending data over a local socket connection. For details,
         *     see [LocalSendOptions]{@link socket.LocalSendOptions}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301011 - Operation would block.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        send(options: LocalSendOptions): Promise<void>;
        /**
         * Closes a local socket connection. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        close(): Promise<void>;
        /**
         * Obtains the local socket connection status. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** or **connect** is successfully called.
         *
         * @returns { Promise<SocketStateBase> } Promise used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        getState(): Promise<SocketStateBase>;
        /**
         * Obtains the file descriptor of the **LocalSocket** object. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - This API can be called only after **bind** or **connect** is successfully called.
         * >
         * > - The file descriptor is allocated by the system kernel to uniquely identify the local socket in use.
         * >
         * > - The lifecycle of the file descriptor is managed by the system. The application can use the
         * > [close]{@link socket.LocalSocket.close} method to close the socket connection, instead of directly operating
         * > the file descriptor.
         *
         * @returns { Promise<number> } Promise used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        getSocketFd(): Promise<number>;
        /**
         * Sets the properties of the **LocalSocket** object. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** or **connect** is successfully called.
         *
         * @param { ExtraOptionsBase } options - Other properties of the LocalSocket connection. For details, see
         *     [ExtraOptionsBase]{@link socket.ExtraOptionsBase}.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        setExtraOptions(options: ExtraOptionsBase): Promise<void>;
        /**
         * Obtains the socket properties of the **LocalSocket** object. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** or **connect** is successfully called.
         *
         * @returns { Promise<ExtraOptionsBase> } Promise used to return the result.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        getExtraOptions(): Promise<ExtraOptionsBase>;
        /**
         * Obtains the local socket address of a **LocalSocket** connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** is successfully called.
         *
         * @returns { Promise<string> } Promise used to return the result.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        getLocalAddress(): Promise<string>;
        /**
         * Subscribes to **message** events of the **LocalSocket** object. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<LocalSocketMessageInfo> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'message', callback: Callback<LocalSocketMessageInfo>): void;
        /**
         * Unsubscribes from **message** events of the **LocalSocket** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<LocalSocketMessageInfo> } callback - Callback used to return the result. You can pass the
         *     callback of the **on** function if you want to cancel listening for a certain type of events. If you do not
         *     pass the callback, you will cancel listening for all events.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'message', callback?: Callback<LocalSocketMessageInfo>): void;
        /**
         * Subscribes to **connect** events of the **LocalSocket** object. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'connect' } type - Event type.<br/>
         * @param { Callback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'connect', callback: Callback<void>): void;
        /**
         * Unsubscribes from **connect** events of the **LocalSocket** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'connect' } type - Event type.<br/> 'connect': connection event.
         * @param { Callback<void> } callback - Callback used to return the result. You can pass the callback of the **on**
         *     function if you want to cancel listening for a certain type of events. If you do not pass the callback, you
         *     will cancel listening for all events.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'connect', callback?: Callback<void>): void;
        /**
         * Subscribes to **close** events of the **LocalSocket** object. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'close' } type - Event type.
         * @param { Callback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'close', callback: Callback<void>): void;
        /**
         * Unsubscribes from **close** events of the **LocalSocket** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'close' } type - Event type.<br/> **close**: close event.
         * @param { Callback<void> } callback - Callback used to return the result. You can pass the callback of the **on**
         *     function if you want to cancel listening for a certain type of events. If you do not pass the callback, you
         *     will cancel listening for all events.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'close', callback?: Callback<void>): void;
        /**
         * Subscribes to **error** events of the **LocalSocket** object. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'error' } type - Event type.
         * @param { ErrorCallback } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from **error** events of the **LocalSocket** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'error' } type - Event type.<br/> 'error': error event.
         * @param { ErrorCallback } callback - Callback used to return the result. You can pass the callback of the **on**
         *     function if you want to cancel listening for a certain type of events. If you do not pass the callback, you
         *     will cancel listening for all events.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'error', callback?: ErrorCallback): void;
    }
    /**
     * Defines a local socket connection, that is, the session between the local socket client and the server. Before
     * calling LocalSocketConnection APIs, you need to obtain a **LocalSocketConnection** object.
     *
     * > **NOTE**
     * >
     * > The LocalSocketConnection client can call related APIs through the **LocalSocketConnection** object only after a
     * > connection is successfully established between the local socket client and the server.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    export interface LocalSocketConnection {
        /**
         * ID of the session between the client and the server.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        clientId: number;
        /**
         * Sends data through a local socket connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be used only after the server obtains a **LocalSocketConnection** object through the **callback**
         * > of the **connect** event.
         *
         * @param { LocalSendOptions } options - Parameters for sending data over a local socket connection.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301011 - Operation would block.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        send(options: LocalSendOptions): Promise<void>;
        /**
         * Closes a local socket connection. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        close(): Promise<void>;
        /**
         * Obtains the local socket address of a **LocalSocketConnection** connection. This API uses a promise to return the
         * result.
         *
         * @returns { Promise<string> } Promise used to return the result.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        getLocalAddress(): Promise<string>;
        /**
         * Subscribes to **message** events of the **LocalSocketConnection** object. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<LocalSocketMessageInfo> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'message', callback: Callback<LocalSocketMessageInfo>): void;
        /**
         * Unsubscribes from **message** events of the **LocalSocketConnection** object. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<LocalSocketMessageInfo> } callback - Callback used to return the result. You can pass the
         *     callback of the **on** function if you want to cancel listening for a certain type of events. If you do not
         *     pass the callback, you will cancel listening for all events.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'message', callback?: Callback<LocalSocketMessageInfo>): void;
        /**
         * Unsubscribes from **close** events of the **LocalSocketConnection** object. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'close' } type - Event type.<br/> **close**: close event.
         * @param { Callback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'close', callback: Callback<void>): void;
        /**
         * Unsubscribes from **close** events of the **LocalSocketConnection** object. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'close' } type - Event type.<br/> **close**: close event.
         * @param { Callback<void> } callback - Callback used to return the result. You can pass the callback of the **on**
         *     function if you want to cancel listening for a certain type of events. If you do not pass the callback, you
         *     will cancel listening for all events.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'close', callback?: Callback<void>): void;
        /**
         * Subscribes to **error** events of the **LocalSocketConnection** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from **error** events of the **LocalSocketConnection** object. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result. You can pass the callback of the **on**
         *     function if you want to cancel listening for a certain type of events. If you do not pass the callback, you
         *     will cancel listening for all events.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Obtains the file descriptor of a LocalSocketConnection connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - This method can be called only after a connection is set up.
         * >
         * > - This API returns **-1** in abnormal cases such as disconnection and socket closed (for example, after the
         * > close API is called).
         * >
         * > - The lifecycle of the file descriptor is managed by the system. The application can use the
         * > [close]{@link socket.LocalSocket.close} method to close the socket connection, instead of directly operating
         * > the file descriptor.
         *
         * @returns { Promise<number> } Promise used to return the socket file descriptor.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 23
         */
        getSocketFd(): Promise<number>;
    }
    /**
     * Defines a local socket server connection. Before calling LocalSocketServer APIs, you need to call
     * [socket.constructLocalSocketServerInstance]{@link socket.constructLocalSocketServerInstance} to create a
     * **LocalSocketServer** object.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    export interface LocalSocketServer {
        /**
         * Binds the address of the local socket file. The server listens to and accepts local socket connections
         * established over the socket. Multiple threads are used to process client data concurrently. This API uses a
         * promise to return the result.
         *
         * > **NOTE**
         * >
         * > The server uses this API to complete the **bind**, **listen**, and **accept** operations. If the address of the
         * > local socket file is passed for binding, a socket file is automatically created when this API is called.
         *
         * @param { LocalAddress } address - Destination address.
         * @returns { Promise<void> } Promise used to return the result. If the operation is successful, no value is
         *     returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303109 - Bad file number.
         * @throws { BusinessError } 2301013 - Insufficient permissions.
         * @throws { BusinessError } 2301022 - Invalid argument.
         * @throws { BusinessError } 2301098 - Address already in use.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        listen(address: LocalAddress): Promise<void>;
        /**
         * Obtains the status of a local socket server connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @returns { Promise<SocketStateBase> } Promise used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        getState(): Promise<SocketStateBase>;
        /**
         * Sets the socket properties of the **LocalSocketServer** object. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @param { ExtraOptionsBase } options - Other properties of the **LocalSocketServer** object.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        setExtraOptions(options: ExtraOptionsBase): Promise<void>;
        /**
         * Obtains the socket properties of the **LocalSocketServer** object. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @returns { Promise<ExtraOptionsBase> } Promise used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        getExtraOptions(): Promise<ExtraOptionsBase>;
        /**
         * Obtains the local socket address of a **LocalSocketServer** connection. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @returns { Promise<string> } Promise used to return the result.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        getLocalAddress(): Promise<string>;
        /**
         * Stops listening for events of the **LocalSocketServer** object and releases the port bound by
         * [listen]{@link socket.LocalSocketServer.listen}. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API does not close existing connections. To close the connection, call the [close] (#close11-1) API of
         * > [LocalSocketConnection] (#localsocketconnection11).
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 20
         */
        close(): Promise<void>;
        /**
         * Subscribes to **connect** events of the **LocalSocketServer** object. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @param { 'connect' } type - Event type.<br/> **connect**: connection event.
         * @param { Callback<LocalSocketConnection> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'connect', callback: Callback<LocalSocketConnection>): void;
        /**
         * Unsubscribes from **connect** events of the **LocalSocketServer** object. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { 'connect' } type - Event type.<br/> 'connect': connection event.
         * @param { Callback<LocalSocketConnection> } callback - Callback used to return the result. You can pass the
         *     callback of the **on** function if you want to cancel listening for a certain type of events. If you do not
         *     pass the callback, you will cancel listening for all events.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'connect', callback?: Callback<LocalSocketConnection>): void;
        /**
         * Subscribes to **error** events of the **LocalSocketServer** object. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from **error** events of the **LocalSocketServer** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result. You can pass the callback of the **on**
         *     function if you want to cancel listening for a certain type of events. If you do not pass the callback, you
         *     will cancel listening for all events.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Obtains the file descriptor bound to the LocalSocketServer listening port. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > - This method can be called only after the [listen]{@link socket.LocalSocketServer.listen} method is
         * > successfully called.
         * >
         * > - This API returns **-1** in abnormal cases such as listening exceptions or socket closed (for example, after
         * > close is called).
         * >
         * > - The lifecycle of the file descriptor is managed by the system. The application can use the
         * > [close]{@link socket.TCPSocketServer.close} method to close the socket connection, instead of directly
         * > operating the file descriptor.
         *
         * @returns { Promise<number> } Promise used to return the socket file descriptor.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 23
         */
        getSocketFd(): Promise<number>;
    }
    /**
     * Defines TCP socket connection parameters.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 7
     */
    export interface TCPConnectOptions {
        /**
         * Bound IP address and port number.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        address: NetAddress;
        /**
         * Timeout duration of the TCP socket connection, in ms. The default value is **5000**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        timeout?: number;
        /**
         * Proxy option. By default, no proxy is used.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @since 18
         */
        proxy?: ProxyOptions;
    }
    /**
     * Defines the parameters for sending data over a TCP socket connection.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 7
     */
    export interface TCPSendOptions {
        /**
         * Data to send.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        data: string | ArrayBuffer;
        /**
         * Character encoding format. The options are as follows: **UTF-8**, **UTF-16BE**, **UTF-16LE**, **UTF-16**,
         * **US-ASCII**, and **ISO-8859-1**. The default value is **UTF-8**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        encoding?: string;
    }
    /**
     * Defines other properties of the **TCPSocket** object. This object is inherited from
     * [ExtraOptionsBase]{@link socket.ExtraOptionsBase}.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 7
     */
    export interface TCPExtraOptions extends ExtraOptionsBase {
        /**
         * Whether to keep the connection alive. The default value is **false**. The value **true** means to keep the
         * connection alive, and the value **false** indicates the opposite.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        keepAlive?: boolean;
        /**
         * Whether to enable OOBInline. The default value is **false**. The value **true** means to enable OOBInline, and
         * the value **false** indicates the opposite.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        OOBInline?: boolean;
        /**
         * Whether to enable no-delay on the TCP socket connection. The default value is **false**. The value **true** means
         * to enable no-delay on the TCP socket connection, and the value **false** indicates the opposite.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        TCPNoDelay?: boolean;
        /**
         * Socket linger.
         *
         * - **on**: whether to enable socket linger. The value true means to enable socket linger and false means the
         * opposite.
         * - **linger**: linger time, in ms. The value ranges from **0** to **65535**.
         *
         * Specify this parameter only when **on** is set to **true**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @since 7
         */
        socketLinger?: {
            on: boolean;
            linger: number;
        };
        /**
         * Whether to enable TCP Fast Open (TFO) in the TCP socket connection. This function allows the client to carry data
         * during the first handshake, reducing the connection setup delay and improving the performance in high-frequency
         * short connection scenarios. The default value is **false**. **true**: yes; **false**: no.
         *
         * Currently, this parameter can be configured only on the client.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 24
         */
        tcpFastOpen?: boolean;
    }
    /**
     * Defines a TCP socket connection. Before calling TCPSocket APIs, you need to call
     * [socket.constructTCPSocketInstance]{@link socket.constructTCPSocketInstance} to create a **TCPSocket** object.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 7
     */
    export interface TCPSocket {
        /**
         * Binds an IP address and a port number. The port number can be customized or randomly allocated by the system.
         * This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > If the bind operation fails due to a port conflict, the system will randomly allocate a port number.
         * >
         * > The TCP client can call **tcp.bind** to explicitly bind the IP address and port number, and then call
         * > **tcp.connect** to connect to the server. Alternatively, the TCP client can directly call **tcp.connect** to
         * > automatically bind the IP address and port number to connect to the server.
         * >
         * > If the IP address is **localhost** or **127.0.0.1**, only local loopback access is allowed; that is, the TCP
         * > client and the server are deployed on the same device.
         *
         * @permission ohos.permission.INTERNET
         * @param { NetAddress } address - Local address. For details, see
         *     [NetAddress](docroot://reference/apis-network-kit/js-apis-socket.md#netaddress).
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        bind(address: NetAddress, callback: AsyncCallback<void>): void;
        /**
         * Binds an IP address and a port number. The port number can be customized or randomly allocated by the system.
         * This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > If the bind operation fails due to a port conflict, the system will randomly allocate a port number.
         * >
         * > The TCP client can call **tcp.bind** to explicitly bind the IP address and port number, and then call
         * > **tcp.connect** to connect to the server. Alternatively, the TCP client can directly call **tcp.connect** to
         * > automatically bind the IP address and port number to connect to the server.
         * >
         * > If the IP address is **localhost** or **127.0.0.1**, only local loopback access is allowed; that is, the TCP
         * > client and the server are deployed on the same device.
         *
         * @permission ohos.permission.INTERNET
         * @param { NetAddress } address - Local address. For details, see
         *     [NetAddress](docroot://reference/apis-network-kit/js-apis-socket.md#netaddress).
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        bind(address: NetAddress): Promise<void>;
        /**
         * Sets up a connection to the specified IP address and port number. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API allows you to connect to the TCP server without first executing **tcp.bind**.
         *
         * @permission ohos.permission.INTERNET
         * @param { TCPConnectOptions } options - TCP socket connection parameters. For details, see
         *     [TCPConnectOptions]{@link socket.TCPConnectOptions}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2301206 - Socks5 failed to connect to the proxy server. [since 18]
         * @throws { BusinessError } 2301207 - Socks5 username or password is invalid. [since 18]
         * @throws { BusinessError } 2301208 - Socks5 failed to connect to the remote server. [since 18]
         * @throws { BusinessError } 2301209 - Socks5 failed to negotiate the authentication method. [since 18]
         * @throws { BusinessError } 2301210 - Socks5 failed to send the message. [since 18]
         * @throws { BusinessError } 2301211 - Socks5 failed to receive the message. [since 18]
         * @throws { BusinessError } 2301212 - Socks5 serialization error. [since 18]
         * @throws { BusinessError } 2301213 - Socks5 deserialization error. [since 18]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        connect(options: TCPConnectOptions, callback: AsyncCallback<void>): void;
        /**
         * Sets up a connection to the specified IP address and port number. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API allows you to connect to the TCP server without first executing **tcp.bind**.
         *
         * @permission ohos.permission.INTERNET
         * @param { TCPConnectOptions } options - TCP socket connection parameters. For details, see
         *     [TCPConnectOptions]{@link socket.TCPConnectOptions}.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2301206 - Socks5 failed to connect to the proxy server. [since 18]
         * @throws { BusinessError } 2301207 - Socks5 username or password is invalid. [since 18]
         * @throws { BusinessError } 2301208 - Socks5 failed to connect to the remote server. [since 18]
         * @throws { BusinessError } 2301209 - Socks5 failed to negotiate the authentication method. [since 18]
         * @throws { BusinessError } 2301210 - Socks5 failed to send the message. [since 18]
         * @throws { BusinessError } 2301211 - Socks5 failed to receive the message. [since 18]
         * @throws { BusinessError } 2301212 - Socks5 serialization error. [since 18]
         * @throws { BusinessError } 2301213 - Socks5 deserialization error. [since 18]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        connect(options: TCPConnectOptions): Promise<void>;
        /**
         * Sends data over a TCP socket connection. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **connect** is successfully called. Call the API in the worker thread or
         * > taskpool thread as this operation is time-consuming.
         *
         * @permission ohos.permission.INTERNET
         * @param { TCPSendOptions } options - Parameters for sending data over a TCP socket connection. For details, see
         *     [TCPSendOptions]{@link socket.TCPSendOptions}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        send(options: TCPSendOptions, callback: AsyncCallback<void>): void;
        /**
         * Sends data over a TCP socket connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **connect** is successfully called. Call the API in the worker thread or
         * > taskpool thread as this operation is time-consuming.
         *
         * @permission ohos.permission.INTERNET
         * @param { TCPSendOptions } options - Parameters for sending data over a TCP socket connection. For details, see
         *     [TCPSendOptions]{@link socket.TCPSendOptions}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        send(options: TCPSendOptions): Promise<void>;
        /**
         * Closes a TCP socket connection. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        close(callback: AsyncCallback<void>): void;
        /**
         * Closes a TCP socket connection. This API uses a promise to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        close(): Promise<void>;
        /**
         * Obtains the remote address of a socket connection. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **connect** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @param { AsyncCallback<NetAddress> } callback - Callback used to return the result. If the operation is
         *     successful, the remote address is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        getRemoteAddress(callback: AsyncCallback<NetAddress>): void;
        /**
         * Obtains the remote address of a socket connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **connect** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<NetAddress> } Promise used to return the result.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        getRemoteAddress(): Promise<NetAddress>;
        /**
         * Obtains the status of the TCP socket connection. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** or **connect** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @param { AsyncCallback<SocketStateBase> } callback - Callback used to return the result. If the operation is
         *     successful, the status of the TCP socket is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        getState(callback: AsyncCallback<SocketStateBase>): void;
        /**
         * Obtains the status of the TCP socket connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** or **connect** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<SocketStateBase> } Promise used to return the result.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        getState(): Promise<SocketStateBase>;
        /**
         * Obtains the file descriptor of the **TCPSocket** object. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > - This API can be called only after **bind** or **connect** is successfully called.
         * >
         * > - The lifecycle of the file descriptor is managed by the system. The application can use the
         * > [close]{@link socket.UDPSocket.close(callback: AsyncCallback<void>)} method to close the socket connection,
         * > instead of directly operating the file descriptor.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful, the
         *     file descriptor of the socket is returned. Otherwise, **undefined** is returned.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getSocketFd(callback: AsyncCallback<number>): void;
        /**
         * Obtains the file descriptor of the **TCPSocket** object. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - This API can be called only after **bind** or **connect** is successfully called.
         * >
         * > - The lifecycle of the file descriptor is managed by the system. The application can use the
         * > [close]{@link socket.UDPSocket.close(callback: AsyncCallback<void>)} method to close the socket connection,
         * > instead of directly operating the file descriptor.
         *
         * @returns { Promise<number> } Promise used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getSocketFd(): Promise<number>;
        /**
         * Sets other properties of the **TCPSocket** object. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** or **connect** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @param { TCPExtraOptions } options - Other properties of the **TCPSocket** object. For details, see
         *     [TCPExtraOptions]{@link socket.TCPExtraOptions}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void;
        /**
         * Sets other properties of the **TCPSocket** object. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** or **connect** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @param { TCPExtraOptions } options - Other properties of the **TCPSocket** object. For details, see
         *     [TCPExtraOptions]{@link socket.TCPExtraOptions}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        setExtraOptions(options: TCPExtraOptions): Promise<void>;
        /**
         * Obtains the local socket address of a **TCPSocket** connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** is successfully called.
         *
         * @returns { Promise<NetAddress> } Promise used to return the result.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        getLocalAddress(): Promise<NetAddress>;
        /**
         * Subscribes to **message** events of the **TCPSocket** object. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<{ message: ArrayBuffer, remoteInfo: SocketRemoteInfo }> } callback - Callback used to return
         *     the result. [since 7 - 10]
         * @param { Callback<SocketMessageInfo> } callback - Callback used to return the result. [since 11]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        on(type: 'message', callback: Callback<SocketMessageInfo>): void;
        /**
         * Unsubscribes from **message** events of the **TCPSocket** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<{ message: ArrayBuffer, remoteInfo: SocketRemoteInfo }> } callback - Callback used to return
         *     the result. You can pass the callback of the **on** function if you want to cancel listening for a certain
         *     type of events. If you do not pass the callback, you will cancel listening for all events. [since 7 - 10]
         * @param { Callback<SocketMessageInfo> } callback - Callback used to return the result. You can pass the callback
         *     of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the
         *     callback, you will cancel listening for all events. [since 11]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        off(type: 'message', callback?: Callback<SocketMessageInfo>): void;
        /**
         * Subscribes to **connect** or **close** events of the **TCPSocket** object. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { 'connect' | 'close' } type - Event type.<br/>
         *     <br>- **connect**: connection event.
         *     <br>- **close**: close event.
         * @param { Callback<void> } callback - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        on(type: 'connect' | 'close', callback: Callback<void>): void;
        /**
         * Unsubscribes from **connect** or **close** events of the **TCPSocket** object. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'connect' | 'close' } type - Event type.<br/>
         *     <br>- **connect**: connection event.
         *     <br>- **close**: close event.
         * @param { Callback<void> } callback - Callback used to return the result. You can pass the callback of the **on**
         *     function if you want to cancel listening for a certain type of events. If you do not pass the callback, you
         *     will cancel listening for all events.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        off(type: 'connect' | 'close', callback?: Callback<void>): void;
        /**
         * Subscribes to **error** events of the **TCPSocket** object. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from **error** events of the **TCPSocket** object. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result. You can pass the callback of the **on**
         *     function if you want to cancel listening for a certain type of events. If you do not pass the callback, you
         *     will cancel listening for all events.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 7
         */
        off(type: 'error', callback?: ErrorCallback): void;
    }
    /**
     * Defines a TLS socket connection. Before calling TLSSocket APIs, you need to call
     * [socket.constructTLSSocketInstance]{@link socket.constructTLSSocketInstance} to create a **TLSSocket** object.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 9
     */
    export interface TLSSocket {
        /**
         * Binds the IP address and port number. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > If the **TLSSocket** object is upgraded from a **TCPSocket** object, you do not need to execute the **bind**
         * > API.
         *
         * @permission ohos.permission.INTERNET
         * @param { NetAddress } address - Local address. For details, see
         *     [NetAddress](docroot://reference/apis-network-kit/js-apis-socket.md#netaddress).
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, the
         *     result of binding the local IP address and port number is returned. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2303198 - Address already in use.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        bind(address: NetAddress, callback: AsyncCallback<void>): void;
        /**
         * Binds the IP address and port number. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > If the **TLSSocket** object is upgraded from a **TCPSocket** object, you do not need to execute the **bind**
         * > API.
         *
         * @permission ohos.permission.INTERNET
         * @param { NetAddress } address - Local address. For details, see
         *     [NetAddress](docroot://reference/apis-network-kit/js-apis-socket.md#netaddress).
         * @returns { Promise<void> } Promise used to return the result. If the operation fails, an error message is
         *     returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2303198 - Address already in use.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        bind(address: NetAddress): Promise<void>;
        /**
         * Obtains the remote address of a TLS socket connection. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<NetAddress> } callback - Callback used to return the result. If the operation is
         *     successful, the remote address is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getRemoteAddress(callback: AsyncCallback<NetAddress>): void;
        /**
         * Obtains the remote address of a TLS socket connection. This API uses a promise to return the result.
         *
         * @returns { Promise<NetAddress> } Promise used to return the result. If the operation fails, an error message is
         *     returned.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getRemoteAddress(): Promise<NetAddress>;
        /**
         * Obtains the status of the TLS socket connection. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<SocketStateBase> } callback - Callback used to return the result. If the operation is
         *     successful, the status of the TLS socket connection is returned. If the operation fails, an error message is
         *     returned.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getState(callback: AsyncCallback<SocketStateBase>): void;
        /**
         * Obtains the status of the TLS socket connection. This API uses a promise to return the result.
         *
         * @returns { Promise<SocketStateBase> } Promise used to return the result. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getState(): Promise<SocketStateBase>;
        /**
         * Sets other properties of the **TCPSocket** object after **bind** is successfully called. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { TCPExtraOptions } options - Other properties of the **TCPSocket** object. For details, see
         *     [TCPExtraOptions]{@link socket.TCPExtraOptions}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, the
         *     result of setting other properties of the **TCPSocket** object is returned. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void;
        /**
         * Sets other properties of the **TCPSocket** object after **bind** is successfully called. This API uses a promise
         * to return the result.
         *
         * @param { TCPExtraOptions } options - Other properties of the **TCPSocket** object. For details, see
         *     [TCPExtraOptions]{@link socket.TCPExtraOptions}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        setExtraOptions(options: TCPExtraOptions): Promise<void>;
        /**
         * Obtains the local socket address of a **TLSSocket** connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > Call this API only after the **TLSSocketServer** connection is successfully established.
         *
         * @returns { Promise<NetAddress> } Promise used to return the result.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        getLocalAddress(): Promise<NetAddress>;
        /**
         * Subscribes to **message** events of the **TLSSocket** object. This API uses an asynchronous callback to return
         * the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** is successfully called.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<{ message: ArrayBuffer, remoteInfo: SocketRemoteInfo }> } callback - Callback used to return
         *     the result. [since 9 - 10]
         * @param { Callback<SocketMessageInfo> } callback - Callback used to return the result. [since 11]
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        on(type: 'message', callback: Callback<SocketMessageInfo>): void;
        /**
         * Unsubscribes from **message** events of the **TLSSocket** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<{ message: ArrayBuffer, remoteInfo: SocketRemoteInfo }> } callback - Callback used to return
         *     the result. [since 9 - 10]
         * @param { Callback<SocketMessageInfo> } callback - Callback used to return the result. [since 11]
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        off(type: 'message', callback?: Callback<SocketMessageInfo>): void;
        /**
         * Subscribes to **connect** or **close** events of the **TLSSocket** object. This API uses an asynchronous callback
         * to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** is successfully called.
         *
         * @param { 'connect' | 'close' } type - Event type.<br/>
         *     <br>- **connect**: connection event.
         *     <br>- **close**: close event.
         * @param {Callback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        on(type: 'connect' | 'close', callback: Callback<void>): void;
        /**
         * Unsubscribes from **connect** or **close** events of the **TLSSocket** object. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'connect' | 'close' } type - Event type.<br/>
         *     <br>- **connect**: connection event.
         *     <br>- **close**: close event.
         * @param {Callback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        off(type: 'connect' | 'close', callback?: Callback<void>): void;
        /**
         * Subscribes to **error** events of the **TLSSocket** object. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **bind** is successfully called.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from **error** events of the **TLSSocket** object. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Obtains the local digital certificate after a **TLSSocket** connection is established. This API is applicable to
         * two-way authentication. It uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<X509CertRawData> } callback - Callback used to return the result. If the operation is
         *     successful, the local certificate is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303504 - An error occurred when verifying the X.509 certificate.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getCertificate(callback: AsyncCallback<X509CertRawData>): void;
        /**
         * Obtains the local digital certificate after a **TLSSocket** connection is established. This API is applicable to
         * two-way authentication. It uses a promise to return the result.
         *
         * @returns { Promise<X509CertRawData> } Promise used to return the result. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303504 - An error occurred when verifying the X.509 certificate.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getCertificate(): Promise<X509CertRawData>;
        /**
         * Obtains the digital certificate of the server after a **TLSSocket** connection is established. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { AsyncCallback<X509CertRawData> } callback - Callback used to return the result. If the operation fails,
         *     an error message is returned.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getRemoteCertificate(callback: AsyncCallback<X509CertRawData>): void;
        /**
         * Obtains the digital certificate of the server after a **TLSSocket** connection is established. This API uses a
         * promise to return the result.
         *
         * @returns { Promise<X509CertRawData> } Promise used to return the result. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getRemoteCertificate(): Promise<X509CertRawData>;
        /**
         * Obtains the communication protocol version after a **TLSSocket** connection is established. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getProtocol(callback: AsyncCallback<string>): void;
        /**
         * Obtains the communication protocol version after a **TLSSocket** connection is established. This API uses a
         * promise to return the result.
         *
         * @returns { Promise<string> } Promise used to return the result. If the operation fails, an error message is
         *     returned.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getProtocol(): Promise<string>;
        /**
         * Obtains the cipher suite negotiated by both communication parties after a **TLSSocket** connection is
         * established. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<Array<string>> } callback - Callback used to return the result. If the operation fails, an
         *     error message is returned.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303502 - An error occurred when reading data on the TLS socket.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getCipherSuite(callback: AsyncCallback<Array<string>>): void;
        /**
         * Obtains the cipher suite negotiated by both communication parties after a **TLSSocket** connection is
         * established. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<string>> } Promise used to return the result. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303502 - An error occurred when reading data on the TLS socket.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getCipherSuite(): Promise<Array<string>>;
        /**
         * Obtains the signing algorithm negotiated by both communication parties after a **TLSSocket** connection is
         * established. This API is applicable to two-way authentication. It uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<Array<string>> } callback - Callback used to return the result.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getSignatureAlgorithms(callback: AsyncCallback<Array<string>>): void;
        /**
         * Obtains the signing algorithm negotiated by both communication parties after a **TLSSocket** connection is
         * established. This API is applicable to two-way authentication. It uses a promise to return the result.
         *
         * @returns { Promise<Array<string>> } Promise used to return the result.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        getSignatureAlgorithms(): Promise<Array<string>>;
        /**
         * Obtains the file descriptor of the **TLSSocket** object. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - This API can be called only after **bind** is successfully called.
         * >
         * > - The lifecycle of the file descriptor is managed by the system. The application can use the
         * > [close]{@link socket.TLSSocket.close(callback: AsyncCallback<void>)} method to close the socket connection,
         * > instead of directly operating the file descriptor.
         *
         * @returns { Promise<number> } Promise used to return the result.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 16
         */
        getSocketFd(): Promise<number>;
        /**
         * Sets up a **TLSSocket** connection, and creates and initializes a TLS session after **bind** is successfully
         * called. During this process, a TLS/SSL handshake is performed between the application and the server to implement
         * data transmission. This API uses an asynchronous callback to return the result. Note that **ca** in
         * **secureOptions** of the **options** parameter is mandatory in API version 11 or earlier. You need to enter the
         * CA certificate of the server for certificate authentication. The certificate content starts with "-----BEGIN
         * CERTIFICATE-----" and ends with "-----END CERTIFICATE-----". This field is optional since API version 12.
         *
         * @param { TLSConnectOptions } options - Parameters required for the TLS socket connection.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, no
         *     value is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303104 - Interrupted system call.
         * @throws { BusinessError } 2303109 - Bad file number.
         * @throws { BusinessError } 2303111 - Resource temporarily unavailable. Try again.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @throws { BusinessError } 2303191 - Incorrect socket protocol type.
         * @throws { BusinessError } 2303198 - Address already in use.
         * @throws { BusinessError } 2303199 - Cannot assign requested address.
         * @throws { BusinessError } 2303210 - Connection timed out.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303502 - An error occurred when reading data on the TLS socket.
         * @throws { BusinessError } 2303503 - An error occurred when writing data on the TLS socket.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2303506 - Failed to close the TLS connection.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2301206 - Socks5 failed to connect to the proxy server. [since 18]
         * @throws { BusinessError } 2301207 - Socks5 username or password is invalid. [since 18]
         * @throws { BusinessError } 2301208 - Socks5 failed to connect to the remote server. [since 18]
         * @throws { BusinessError } 2301209 - Socks5 failed to negotiate the authentication method. [since 18]
         * @throws { BusinessError } 2301210 - Socks5 failed to send the message. [since 18]
         * @throws { BusinessError } 2301211 - Socks5 failed to receive the message. [since 18]
         * @throws { BusinessError } 2301212 - Socks5 serialization error. [since 18]
         * @throws { BusinessError } 2301213 - Socks5 deserialization error. [since 18]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        connect(options: TLSConnectOptions, callback: AsyncCallback<void>): void;
        /**
         * Sets up a **TLSSocket** connection, and creates and initializes a TLS session after **bind** is successfully
         * called. During this process, a TLS/SSL handshake is performed between the application and the server to implement
         * data transmission. Both two-way and one-way authentication modes are supported. This API uses a promise to return
         * the result. Note that **ca** in **secureOptions** of the **options** parameter is mandatory in API version 11 or
         * earlier. You need to enter the CA certificate of the server for certificate authentication. The certificate
         * content starts with "-----BEGIN CERTIFICATE-----" and ends with "-----END CERTIFICATE-----". This field is
         * optional since API version 12.
         *
         * @param { TLSConnectOptions } options - Parameters required for the connection.
         * @returns { Promise<void> } Promise used to return the result. If the operation is successful, no value is
         *     returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303104 - Interrupted system call.
         * @throws { BusinessError } 2303109 - Bad file number.
         * @throws { BusinessError } 2303111 - Resource temporarily unavailable. Try again.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @throws { BusinessError } 2303191 - Incorrect socket protocol type.
         * @throws { BusinessError } 2303198 - Address already in use.
         * @throws { BusinessError } 2303199 - Cannot assign requested address.
         * @throws { BusinessError } 2303210 - Connection timed out.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303502 - An error occurred when reading data on the TLS socket.
         * @throws { BusinessError } 2303503 - An error occurred when writing data on the TLS socket.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2303506 - Failed to close the TLS connection.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2301206 - Socks5 failed to connect to the proxy server. [since 18]
         * @throws { BusinessError } 2301207 - Socks5 username or password is invalid. [since 18]
         * @throws { BusinessError } 2301208 - Socks5 failed to connect to the remote server. [since 18]
         * @throws { BusinessError } 2301209 - Socks5 failed to negotiate the authentication method. [since 18]
         * @throws { BusinessError } 2301210 - Socks5 failed to send the message. [since 18]
         * @throws { BusinessError } 2301211 - Socks5 failed to receive the message. [since 18]
         * @throws { BusinessError } 2301212 - Socks5 serialization error. [since 18]
         * @throws { BusinessError } 2301213 - Socks5 deserialization error. [since 18]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        connect(options: TLSConnectOptions): Promise<void>;
        /**
         * Sends a message to the server after a **TLSSocket** connection is established. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { string } data - Data content of the message to send. [since 9 - 11]
         * @param { string | ArrayBuffer } data - Data content of the message to send. [since 12]
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303503 - An error occurred when writing data on the TLS socket.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2303506 - Failed to close the TLS connection.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        send(data: string | ArrayBuffer, callback: AsyncCallback<void>): void;
        /**
         * Sends a message to the server after a **TLSSocket** connection is established. This API uses a promise to return
         * the result.
         *
         * @param { string } data - Data content of the message to send. [since 9 - 11]
         * @param { string | ArrayBuffer } data - Data content of the message to send. [since 12]
         * @returns { Promise<void> } Promise used to return the result. If the operation fails, an error message is
         *     returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303503 - An error occurred when writing data on the TLS socket.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2303506 - Failed to close the TLS connection.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        send(data: string | ArrayBuffer): Promise<void>;
        /**
         * Closes a **TLSSocket** connection. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2303506 - Failed to close the TLS connection.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        close(callback: AsyncCallback<void>): void;
        /**
         * Closes a **TLSSocket** connection. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise used to return the result. If the operation fails, an error message is
         *     returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2303506 - Failed to close the TLS connection.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        close(): Promise<void>;
    }
    /**
     * TLS security options. When **cert** (local certificate) and **key** (private key) are not empty, the two-way
     * authentication mode is enabled. If **cert** or **key** is empty, one-way authentication is enabled.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 9
     */
    export interface TLSSecureOptions {
        /**
         * CA certificate of the server, which is used to authenticate the digital certificate of the server. The default
         * value is the preset CA certificate<sup>12+</sup>. A maximum of 1000 certificates can be set.
         *
         * @type {string | Array<string>} [since 9 - 11]
         * @type {?(string | Array<string>)} [since 12]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        ca?: string | Array<string>;
        /**
         * Digital certificate of the local client. An array can be passed since API version 24. A maximum of 1000
         * certificates can be set.
         *
         * @type {?string} [since 9 - 23]
         * @type {?(string | Array<string>)} [since 24]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        cert?: string | Array<string>;
        /**
         * Private key of the local digital certificate.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        key?: string;
        /**
         * Password for reading the private key.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        password?: string;
        /**
         * TLS protocol version. The default value is **TLSv1.2**.
         *
         * @type {?Protocol | Array<Protocol>} [since 9 - 9]
         * @type {?(Protocol | Array<Protocol>)} [since 10]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        protocols?: Protocol | Array<Protocol>;
        /**
         * Whether to use the remote cipher suite preferentially. The value **true** means to use the remote cipher suite
         * preferentially, and the value **false** means the opposite.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        useRemoteCipherPrefer?: boolean;
        /**
         * Signing algorithm used during communication. The default value is **""**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        signatureAlgorithms?: string;
        /**
         * Cipher suite used during communication. The default value is **""**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        cipherSuite?: string;
        /**
         * Two-way authentication. The default value is **false**. The value **true** means to enable two-way
         * authentication, and the value **false** means the opposite.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        isBidirectionalAuthentication?: boolean;
    }
    /**
     * Defines TLS connection options.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 9
     */
    export interface TLSConnectOptions {
        /**
         * Gateway address.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        address: NetAddress;
        /**
         * TLS security options.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        secureOptions: TLSSecureOptions;
        /**
         * ALPN protocol. The value range is ["spdy/1", "http/1.1"]. The default value is **[]**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        ALPNProtocols?: Array<string>;
        /**
         * Whether to skip certificate authentication on the server. The default value is **false**. The value **true**
         * means to skip certificate authentication on the server, and the value **false** means the opposite.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        skipRemoteValidation?: boolean;
        /**
         * Proxy option. By default, no proxy is used.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @since 18
         */
        proxy?: ProxyOptions;
        /**
         * Connection timeout interval, in milliseconds. The default value is **0**. The input value must be an integer
         * ranging from 0 to 4294967295. The TLS socket connection fails after the timeout interval.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @since 22
         */
        timeout?: number;
    }
    /**
     * Enumerates TLS protocol versions.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @since 9
     */
    export enum Protocol {
        /**
         * TLSv1.2.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        TLSv12 = "TLSv1.2",
        /**
         * TLSv1.3.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @since 9
         */
        TLSv13 = "TLSv1.3"
    }
    /**
     * Defines a **TCPSocketConnection** object, that is, the connection between the TCPSocket client and the server.
     * Before calling TCPSocketConnection APIs, you need to obtain a **TCPSocketConnection** object.
     *
     * > **NOTE**
     * >
     * > The TCPSocket client can call related APIs through the **TCPSocketConnection** object only after a connection is
     * > successfully established between the TCPSocket client and the server.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 10
     */
    export interface TCPSocketConnection {
        /**
         * ID of the connection between the client and TCPSocketServer.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        clientId: number;
        /**
         * Sends data over a **TCPSocketConnection** object. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after a connection with the client is set up.
         *
         * @permission ohos.permission.INTERNET
         * @param { TCPSendOptions } options - Defines the parameters for sending data over a TCP socket connection.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        send(options: TCPSendOptions, callback: AsyncCallback<void>): void;
        /**
         * Sends data over a **TCPSocketConnection** object. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after a connection with the client is set up.
         *
         * @permission ohos.permission.INTERNET
         * @param { TCPSendOptions } options - Defines the parameters for sending data over a TCP socket connection.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        send(options: TCPSendOptions): Promise<void>;
        /**
         * Closes a TCP socket connection. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        close(callback: AsyncCallback<void>): void;
        /**
         * Closes a TCP socket connection. This API uses a promise to return the result.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        close(): Promise<void>;
        /**
         * Obtains the remote address of a socket connection. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after a connection with the client is set up.
         *
         * @permission ohos.permission.INTERNET
         * @param { AsyncCallback<NetAddress> } callback - Callback used to return the result. If the operation fails, an
         *     error message is returned.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getRemoteAddress(callback: AsyncCallback<NetAddress>): void;
        /**
         * Obtains the remote address of a socket connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after a connection with the client is set up.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<NetAddress> } Promise used to return the result.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getRemoteAddress(): Promise<NetAddress>;
        /**
         * Obtains the local socket address of a **TCPSocketConnection** connection. This API uses a promise to return the
         * result.
         *
         * @returns { Promise<NetAddress> } Promise used to return the result.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        getLocalAddress(): Promise<NetAddress>;
        /**
         * Subscribes to **message** events of the **TCPSocketConnection** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<{ message: ArrayBuffer, remoteInfo: SocketRemoteInfo }> } callback - Callback used to return
         *     the result. If the operation fails, an error message is returned. [since 10 - 10]
         * @param { Callback<SocketMessageInfo> } callback - Callback used to return the result. If the operation fails, an
         *     error message is returned. [since 11]
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 10
         */
        on(type: 'message', callback: Callback<SocketMessageInfo>): void;
        /**
         * Unsubscribes from **message** events of the **TCPSocketConnection** object. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<{ message: ArrayBuffer, remoteInfo: SocketRemoteInfo }> } callback - Callback used to return
         *     the result. You can pass the callback of the **on** function if you want to cancel listening for a certain
         *     type of events. If you do not pass the callback, you will cancel listening for all events. [since 10 - 10]
         * @param { Callback<SocketMessageInfo> } callback - Callback used to return the result. You can pass the callback
         *     of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the
         *     callback, you will cancel listening for all events. [since 11]
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 10
         */
        off(type: 'message', callback?: Callback<SocketMessageInfo>): void;
        /**
         * Subscribes to **close** events of the **TCPSocketConnection** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'close' } type - Event type.<br/> **close**: close event.
         * @param { Callback<void> } callback - Callback used to return the result. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        on(type: 'close', callback: Callback<void>): void;
        /**
         * Unsubscribes from **close** events of the **TCPSocketConnection** object. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { 'close' } type - Event type.<br/> **close**: close event.
         * @param { Callback<void> } callback - Callback used to return the result. You can pass the callback of the **on**
         *     function if you want to cancel listening for a certain type of events. If you do not pass the callback, you
         *     will cancel listening for all events.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        off(type: 'close', callback?: Callback<void>): void;
        /**
         * Subscribes to **error** events of the **TCPSocketConnection** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @since 10
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from **error** events of the **TCPSocketConnection** object. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result. You can pass the callback of the **on**
         *     function if you want to cancel listening for a certain type of events. If you do not pass the callback, you
         *     will cancel listening for all events.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @since 10
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Obtains the file descriptor of a TCPSocketConnection connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - This API can be called only after a connection with the client is set up.
         * >
         * > - This API returns **-1** in abnormal cases such as disconnection and socket closed (for example, after the
         * > close API is called).
         * >
         * > - The lifecycle of the file descriptor is managed by the system. The application can use the
         * > [close]{@link socket.TCPSocketConnection.close(callback: AsyncCallback<void>)} method to close the socket
         * > connection, instead of directly operating the file descriptor.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<number> } Promise used to return the socket file descriptor.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 23
         */
        getSocketFd(): Promise<number>;
    }
    /**
     * Defines a TCP socket server connection. Before calling TCPSocketServer APIs, you need to call
     * [socket.constructTCPSocketServerInstance]{@link socket.constructTCPSocketServerInstance} to create a
     * **TCPSocketServer** object.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 10
     */
    export interface TCPSocketServer {
        /**
         * Binds the IP address and port number. The port number can be specified or randomly allocated by the system. The
         * server listens to and accepts TCP socket connections established over the socket. Multiple threads are used to
         * process client data concurrently. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The server uses this API to perform the **bind**, **listen**, and **accept** operations. If the **bind**
         * > operation fails, the system randomly allocates a port number.
         *
         * @permission ohos.permission.INTERNET
         * @param { NetAddress } address - Destination address.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2303109 - Bad file number.
         * @throws { BusinessError } 2303111 - Resource temporarily unavailable. Try again.
         * @throws { BusinessError } 2303198 - Address already in use.
         * @throws { BusinessError } 2303199 - Cannot assign requested address.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        listen(address: NetAddress, callback: AsyncCallback<void>): void;
        /**
         * Binds the IP address and port number. The port number can be specified or randomly allocated by the system. The
         * server listens to and accepts TCP socket connections established over the socket. Multiple threads are used to
         * process client data concurrently. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > The server uses this API to perform the **bind**, **listen**, and **accept** operations. If the **bind**
         * > operation fails, the system randomly allocates a port number.
         *
         * @permission ohos.permission.INTERNET
         * @param { NetAddress } address - Destination address.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2303109 - Bad file number.
         * @throws { BusinessError } 2303111 - Resource temporarily unavailable. Try again.
         * @throws { BusinessError } 2303198 - Address already in use.
         * @throws { BusinessError } 2303199 - Cannot assign requested address.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        listen(address: NetAddress): Promise<void>;
        /**
         * Stops listening for events of the **TCPSocketServer** object and releases the port bound by
         * [listen]{@link socket.TCPSocketServer.listen(address: NetAddress, callback: AsyncCallback<void>)}. If
         * [listen]{@link socket.TCPSocketServer.listen(address: NetAddress, callback: AsyncCallback<void>)} has been called
         * for multiple times, all listening ports of the **TCPSocketServer** object are released when this API is called.
         * This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API does not close existing connections. To close connections, call the
         * > [close]{@link socket.TCPSocketConnection.close(callback: AsyncCallback<void>)} API of
         * > [TCPSocketConnection]{@link socket.TCPSocketConnection}.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 20
         */
        close(): Promise<void>;
        /**
         * Obtains the status of a TCP socket server connection. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @param { AsyncCallback<SocketStateBase> } callback - Callback used to return the result. If the operation fails,
         *     an error message is returned.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getState(callback: AsyncCallback<SocketStateBase>): void;
        /**
         * Obtains the status of a TCP socket server connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<SocketStateBase> } Promise used to return the result.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getState(): Promise<SocketStateBase>;
        /**
         * Sets other properties of the **TCPSocketServer** object. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @param { TCPExtraOptions } options - Other properties of the **TCPSocketServer** object.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void;
        /**
         * Sets other properties of the **TCPSocketServer** object. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @permission ohos.permission.INTERNET
         * @param { TCPExtraOptions } options - Other properties of the **TCPSocketServer** object.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        setExtraOptions(options: TCPExtraOptions): Promise<void>;
        /**
         * Obtains the local socket address of a **TCPSocketServer** connection. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @returns { Promise<NetAddress> } Promise used to return the result.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        getLocalAddress(): Promise<NetAddress>;
        /**
         * Subscribes to **connect** events of the **TCPSocketServer** object. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @param { 'connect' } type - Event type.<br/> **connect**: connection event.
         * @param { Callback<TCPSocketConnection> } callback - Callback used to return the result. If the operation fails,
         *     an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        on(type: 'connect', callback: Callback<TCPSocketConnection>): void;
        /**
         * Unsubscribes from **connect** events of the **TCPSocketServer** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'connect' } type - Event type.<br/> **connect**: connection event.
         * @param { Callback<TCPSocketConnection> } callback - Callback used to return the result. You can pass the callback
         *     of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the
         *     callback, you will cancel listening for all events.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        off(type: 'connect', callback?: Callback<TCPSocketConnection>): void;
        /**
         * Subscribes to **error** events of the **TCPSocketServer** object. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @since 10
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from **error** events of the **TCPSocketServer** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result. You can pass the callback of the **on**
         *     function if you want to cancel listening for a certain type of events. If you do not pass the callback, you
         *     will cancel listening for all events.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @since 10
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Obtains the file descriptor bound to the TCPSocketServer listening port. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > - This method can be called only after the
         * > [listen]{@link socket.TCPSocketServer.listen(address: NetAddress, callback: AsyncCallback<void>)} method is
         * > successfully called. When listen is called for multiple times, the file descriptor bound to the latest
         * > listening port is obtained.
         * >
         * > - This API returns **-1** in abnormal cases such as listening exceptions or socket closed (for example, after
         * > close is called).
         * >
         * > - The lifecycle of the file descriptor is managed by the system. The application can use the
         * > [close]{@link socket.TCPSocketServer.close} method to close the socket connection, instead of directly
         * > operating the file descriptor.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<number> } Promise used to return the socket file descriptor.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 23
         */
        getSocketFd(): Promise<number>;
    }
    /**
     * Defines a **TLSSocketConnection** object, that is, the connection between the TLSSocket client and the server.
     * Before calling TLSSocketConnection APIs, you need to obtain a **TLSSocketConnection** object.
     *
     * > **NOTE**
     * >
     * > The TLSSocket client can call related APIs through the **TLSSocketConnection** object only after a connection is
     * > successfully established between the TLSSocket client and the server.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 10
     */
    export interface TLSSocketConnection {
        /**
         * ID of the connection between the client and TLSSocketServer.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        clientId: number;
        /**
         * Sends a message to the client after a **TLSSocketServer** connection is established. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { string } data - Parameters for sending data over a TLS socket server connection. [since 10 - 11]
         * @param { string | ArrayBuffer } data - Parameters for sending data over a TLS socket server connection. [since 12]
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, no
         *     value is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303503 - An error occurred when writing data on the TLS socket.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2303506 - Failed to close the TLS connection.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        send(data: string | ArrayBuffer, callback: AsyncCallback<void>): void;
        /**
         * Sends a message to the server after a **TLSSocketServer** connection is established. This API uses a promise to
         * return the result.
         *
         * @param { string } data - Parameters for sending data over a TLS socket server connection. [since 10 - 11]
         * @param { string | ArrayBuffer } data - Parameters for sending data over a TLS socket server connection. [since 12]
         * @returns { Promise<void> } Promise used to return the result. If the operation is successful, no value is
         *     returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303503 - An error occurred when writing data on the TLS socket.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2303506 - Failed to close the TLS connection.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        send(data: string | ArrayBuffer): Promise<void>;
        /**
         * Closes a **TLSSocketServer** connection. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, no
         *     value is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2303506 - Failed to close the TLS connection.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        close(callback: AsyncCallback<void>): void;
        /**
         * Closes a **TLSSocketServer** connection. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise used to return the result. If the operation is successful, no value is
         *     returned. If the operation fails, an error message is returned. If the operation fails, an error message is
         *     returned.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2303506 - Failed to close the TLS connection.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        close(): Promise<void>;
        /**
         * Obtains the remote address of a TLS socket server connection. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { AsyncCallback<NetAddress> } callback - Callback used to return the result. If the operation is
         *     successful, the remote address is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getRemoteAddress(callback: AsyncCallback<NetAddress>): void;
        /**
         * Obtains the remote address of a TLS socket server connection. This API uses a promise to return the result.
         *
         * @returns { Promise<NetAddress> } Promise used to return the result. If the operation fails, an error message is
         *     returned.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getRemoteAddress(): Promise<NetAddress>;
        /**
         * Obtains the digital certificate of the peer end after a **TLSSocketServer** connection is established. This API
         * uses an asynchronous callback to return the result. It applies only to the scenario where the client sends a
         * certificate to the server.
         *
         * @param { AsyncCallback<X509CertRawData> } callback - Callback used to return the result. If the operation fails,
         *     an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getRemoteCertificate(callback: AsyncCallback<X509CertRawData>): void;
        /**
         * Obtains the digital certificate of the peer end after a **TLSSocketServer** connection is established. This API
         * uses a promise to return the result. It applies only to the scenario where the client sends a certificate to the
         * server.
         *
         * @returns { Promise<X509CertRawData> } Promise used to return the result. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getRemoteCertificate(): Promise<X509CertRawData>;
        /**
         * Obtains the cipher suite negotiated by both communication parties after a **TLSSocketServer** connection is
         * established. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<Array<string>> } callback - Callback used to return the result. If the operation fails, an
         *     error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303502 - An error occurred when reading data on the TLS socket.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getCipherSuite(callback: AsyncCallback<Array<string>>): void;
        /**
         * Obtains the cipher suite negotiated by both communication parties after a **TLSSocketServer** connection is
         * established. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<string>> } Promise used to return the result. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303502 - An error occurred when reading data on the TLS socket.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getCipherSuite(): Promise<Array<string>>;
        /**
         * Obtains the signing algorithm negotiated by both communication parties after a **TLSSocketServer** connection is
         * established. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<Array<string>> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getSignatureAlgorithms(callback: AsyncCallback<Array<string>>): void;
        /**
         * Obtains the signing algorithm negotiated by both communication parties after a **TLSSocketServer** connection is
         * established. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<string>> } Promise used to return the result.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getSignatureAlgorithms(): Promise<Array<string>>;
        /**
         * Obtains the local socket address of a **TLSSocketConnection** connection. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > Call this API only after the **TLSSocketServer** connection is successfully established.
         *
         * @returns { Promise<NetAddress> } Promise used to return the result.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        getLocalAddress(): Promise<NetAddress>;
        /**
         * Subscribes to **message** events of the **TLSSocketConnection** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<{ message: ArrayBuffer, remoteInfo: SocketRemoteInfo }> } callback - Callback used to return
         *     the result. If the operation is successful, the TLS socket connection information is returned. If the
         *     operation fails, an error message is returned. [since 10 - 10]
         * @param { Callback<SocketMessageInfo> } callback - Callback used to return the result. If the operation is
         *     successful, the TLS socket connection information is returned. If the operation fails, an error message is
         *     returned. [since 11]
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 10
         */
        on(type: 'message', callback: Callback<SocketMessageInfo>): void;
        /**
         * Unsubscribes from **message** events of the **TLSSocketConnection** object. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'message' } type - Event type.<br/> **message**: message receiving event.
         * @param { Callback<{ message: ArrayBuffer, remoteInfo: SocketRemoteInfo }> } callback - Callback used to return
         *     the result. If the operation is successful, the TLS socket connection information is returned. If the
         *     operation fails, an error message is returned. [since 10 - 10]
         * @param { Callback<SocketMessageInfo> } callback - Callback used to return the result. If the operation is
         *     successful, the TLS socket connection information is returned. If the operation fails, an error message is
         *     returned. [since 11]
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 10
         */
        off(type: 'message', callback?: Callback<SocketMessageInfo>): void;
        /**
         * Subscribes to **close** events of the **TLSSocketConnection** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'close' } type - Event type.<br/> **close**: close event.
         * @param { Callback<void> } callback - Callback used to return the result. If the operation is successful, no value
         *     is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        on(type: 'close', callback: Callback<void>): void;
        /**
         * Unsubscribes from **close** events of the **TLSSocketConnection** object. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { 'close' } type - Event type.<br/> **close**: close event.
         * @param { Callback<void> } callback - Callback used to return the result. If the operation is successful, no value
         *     is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        off(type: 'close', callback?: Callback<void>): void;
        /**
         * Subscribes to **error** events of the **TLSSocketConnection** object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result. If the operation is successful, no value
         *     is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @since 10
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from **error** events of the **TLSSocketConnection** object. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result. If the operation is successful, no value
         *     is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @since 10
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Obtains the file descriptor of a TLSSocketConnection connection. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - Call this API only after the **TLSSocketServer** connection is successfully established.
         * >
         * > - This API returns **-1** in abnormal cases such as disconnection and socket closed (for example, after the
         * > close API is called).
         * >
         * > - The lifecycle of the file descriptor is managed by the system. The application can use the
         * > [close]{@link socket.TCPSocketConnection.close(callback: AsyncCallback<void>)} method to close the socket
         * > connection, instead of directly operating the file descriptor.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<number> } Promise used to return the socket file descriptor.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 23
         */
        getSocketFd(): Promise<number>;
    }
    /**
     * Defines the socket connection information.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform
     * @since 11
     */
    export interface SocketMessageInfo {
        /**
         * Received **message** event.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @since 11
         */
        message: ArrayBuffer;
        /**
         * Socket connection information.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @since 11
         */
        remoteInfo: SocketRemoteInfo;
    }
    /**
     * Defines a TLS socket server connection. Before calling TLSSocketServer APIs, you need to call
     * [socket.constructTLSSocketServerInstance]{@link socket.constructTLSSocketServerInstance} to create a
     * **TLSSocketServer** object.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 24]
     * @since 10
     */
    export interface TLSSocketServer {
        /**
         * Listens for client connections after **bind** is successfully called to bind the IP address and port of
         * **TLSSocketServer**. This API uses an asynchronous callback to return the result. After a connection is
         * established, a TLS session will be created and initialized and a certificate key will be loaded and verified.
         *
         * > **NOTE**
         * >
         * > If the IP address is set to 0.0.0.0, all local IP addresses can be listened on.
         *
         * @permission ohos.permission.INTERNET
         * @param { TLSConnectOptions } options - Parameters required for the connection.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, no
         *     value is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2303109 - Bad file number.
         * @throws { BusinessError } 2303111 - Resource temporarily unavailable. Try again.
         * @throws { BusinessError } 2303198 - Address already in use.
         * @throws { BusinessError } 2303199 - Cannot assign requested address.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303502 - An error occurred when reading data on the TLS socket.
         * @throws { BusinessError } 2303503 - An error occurred when writing data on the TLS socket.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2303506 - Failed to close the TLS connection.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        listen(options: TLSConnectOptions, callback: AsyncCallback<void>): void;
        /**
         * Listens for client connections after **bind** is successfully called to bind the IP address and port of
         * **TLSSocketServer**. This API uses an asynchronous callback to return the result. After a connection is
         * established, a TLS session will be created and initialized and a certificate key will be loaded and verified.
         *
         * @permission ohos.permission.INTERNET
         * @param { TLSConnectOptions } options - Parameters required for the connection.
         * @returns { Promise<void> } Promise used to return the result. If the operation is successful, no value is
         *     returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2303109 - Bad file number.
         * @throws { BusinessError } 2303111 - Resource temporarily unavailable. Try again.
         * @throws { BusinessError } 2303198 - Address already in use.
         * @throws { BusinessError } 2303199 - Cannot assign requested address.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303502 - An error occurred when reading data on the TLS socket.
         * @throws { BusinessError } 2303503 - An error occurred when writing data on the TLS socket.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2303506 - Failed to close the TLS connection.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        listen(options: TLSConnectOptions): Promise<void>;
        /**
         * Stops listening for events of the **TLSSocketServer** object and releases the port bound by
         * [listen]{@link socket.TCPSocketServer.listen}. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API does not close existing connections. To close the connection, call the
         * > [close]{@link socket.TCPSocketConnection.close(callback: AsyncCallback<void>)} API of
         * > [TLSSocketConnection]{@link socket.TLSSocketConnection}.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 20
         */
        close(): Promise<void>;
        /**
         * Obtains the status of the TLS socket server connection upon successful listening. This API uses an asynchronous
         * callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @param { AsyncCallback<SocketStateBase> } callback - Callback used to return the result. If the operation is
         *     successful, the status of the TLS socket server connection is returned. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getState(callback: AsyncCallback<SocketStateBase>): void;
        /**
         * Obtains the status of the TLS socket server connection upon successful listening. This API uses a promise to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @returns { Promise<SocketStateBase> } Promise used to return the result. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getState(): Promise<SocketStateBase>;
        /**
         * Sets other properties of the **TLSSocketServer** object after **listen** is successfully called. This API uses an
         * asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @param { TCPExtraOptions } options - Other properties of the **TLSSocketServer** object.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, no
         *     value is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void;
        /**
         * Sets other properties of the **TLSSocketServer** object after **listen** is successfully called. This API uses a
         * promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @param { TCPExtraOptions } options - Other properties of the **TLSSocketServer** object.
         * @returns { Promise<void> } Promise used to return the result. If the operation is successful, no value is
         *     returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        setExtraOptions(options: TCPExtraOptions): Promise<void>;
        /**
         * Obtains the local digital certificate after a **TLSSocketServer** connection is established. This API uses an
         * asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @param { AsyncCallback<X509CertRawData> } callback - Callback used to return the result. If the operation is
         *     successful, the local certificate is returned. If the operation fails, an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303504 - An error occurred when verifying the X.509 certificate.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getCertificate(callback: AsyncCallback<X509CertRawData>): void;
        /**
         * Obtains the local digital certificate after a **TLSSocketServer** connection is established. This API uses a
         * promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @returns { Promise<X509CertRawData> } Promise used to return the result. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303504 - An error occurred when verifying the X.509 certificate.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getCertificate(): Promise<X509CertRawData>;
        /**
         * Obtains the communication protocol version after a **TLSSocketServer** connection is established. This API uses
         * an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation fails, an error
         *     message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getProtocol(callback: AsyncCallback<string>): void;
        /**
         * Obtains the communication protocol version after a **TLSSocketServer** connection is established. This API uses a
         * promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @returns { Promise<string> } Promise used to return the result. If the operation fails, an error message is
         *     returned.
         * @throws { BusinessError } 2303501 - SSL is null.
         * @throws { BusinessError } 2303505 - An error occurred in the TLS system call.
         * @throws { BusinessError } 2300002 - System internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        getProtocol(): Promise<string>;
        /**
         * Obtains the local socket address of a **TLSSocketServer** connection. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > Call this API only after the **TLSSocketServer** connection is successfully established.
         *
         * @returns { Promise<NetAddress> } Promise used to return the result.
         * @throws { BusinessError } 2300002 - System internal error.
         * @throws { BusinessError } 2301009 - Bad file descriptor.
         * @throws { BusinessError } 2303188 - Socket operation on non-socket.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 12
         */
        getLocalAddress(): Promise<NetAddress>;
        /**
         * Subscribes to TLS socket server connection events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @param { 'connect' } type - Event type.<br/> **connect**: connection event.
         * @param { Callback<TLSSocketConnection> } callback - Callback used to return the result. If the operation fails,
         *     an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        on(type: 'connect', callback: Callback<TLSSocketConnection>): void;
        /**
         * Unsubscribes from **connect** events of the **TLSSocketServer** object. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         * >
         * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of events.
         * > If you do not pass the callback, you will cancel listening for all events.
         *
         * @param { 'connect' } type - Event type.<br/> **connect**: connection event.
         * @param { Callback<TLSSocketConnection> } callback - Callback used to return the result. If the operation fails,
         *     an error message is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        off(type: 'connect', callback?: Callback<TLSSocketConnection>): void;
        /**
         * Subscribes to **error** events of the **TLSSocketServer** object. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from **error** events of the **TLSSocketServer** object. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only after **listen** is successfully called.
         * >
         * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of events.
         * > If you do not pass the callback, you will cancel listening for all events.
         *
         * @param { 'error' } type - Event type.<br/> **error**: error event.
         * @param { ErrorCallback } callback - Callback used to return the result. If the operation fails, an error message
         *     is returned.
         * @throws { BusinessError } 401 - Parameter error.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 10
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Obtains the file descriptor bound to the TLSSocketServer listening port. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > - This method can be called only after the [listen]{@link socket.TCPSocketServer.listen} method is successfully
         * > called. When listen is called for multiple times, the file descriptor bound to the latest listening port is
         * > obtained.
         * >
         * > - This API returns **-1** in abnormal cases such as listening exceptions or socket closed (for example, after
         * > close is called).
         * >
         * > - The lifecycle of the file descriptor is managed by the system. The application can use the
         * > [close]{@link socket.TCPSocketServer.close} method to close the socket connection, instead of directly
         * > operating the file descriptor.
         *
         * @permission ohos.permission.INTERNET
         * @returns { Promise<number> } Promise used to return the socket file descriptor.
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 24]
         * @since 23
         */
        getSocketFd(): Promise<number>;
    }
}
export default socket;

```
