# @ohos.bluetooth.socket.d.ts

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
import type { AsyncCallback, Callback } from './@ohos.base';
/**
 * Provides methods to operate or manage bluetooth socket connection.
 *
 * @syscap SystemCapability.Communication.Bluetooth.Core
 * @since 10
 */
declare namespace socket {
    /**
     * Creates a Bluetooth server listening socket.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } name - Indicates the service name.
     * @param { SppOptions } options - Indicates the listen parameters.
     * @param { AsyncCallback<number> } callback - Callback used to return a server socket ID.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900004 - Profile not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    function sppListen(name: string, options: SppOptions, callback: AsyncCallback<number>): void;
    /**
     * Get l2cap socket psm.
     *
     * @param { number } serverSocket - Indicates the server socket ID, returned by {@link sppListen}.
     * @returns { number } Returns the l2cap socket psm
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 20
     */
    function getL2capPsm(serverSocket: number): number;
    /**
     * Waits for a remote device to connect.
     *
     * @param { number } serverSocket - Indicates the server socket ID, returned by {@link sppListen}.
     * @param { AsyncCallback<number> } callback - Callback used to return a client socket ID.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900004 - Profile not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    function sppAccept(serverSocket: number, callback: AsyncCallback<number>): void;
    /**
     * Connects to a remote device over the socket.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @param { SppOptions } options - Indicates the connect parameters {@link SppOptions}.
     * @param { AsyncCallback<number> } callback - Callback used to return a client socket ID.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900004 - Profile not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    function sppConnect(deviceId: string, options: SppOptions, callback: AsyncCallback<number>): void;
    /**
     * Obtain the device id in the client socket.
     *
     * @param { number } clientSocket - Indicates client socket.
     * @returns { string } Returns the connected device id
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     * 1. Mandatory parameters are left unspecified;
     * 2. Incorrect parameter types;
     * 3. Parameter verification failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 17
     */
    function getDeviceId(clientSocket: number): string;
    /**
     * Obtain the maximum data size that can be received through this socket channel.
     *
     * @param { number } clientSocket - Indicates the client socket ID, returned by {@link sppAccept} or {@link sppConnect}.
     * @returns { number } Maximum received data size
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 22
     */
    function getMaxReceiveDataSize(clientSocket: number): number;
    /**
     * Obtain the maximum data size that can be transmitted through this socket channel.
     *
     * @param { number } clientSocket - Indicates the client socket ID, returned by {@link sppAccept} or {@link sppConnect}.
     * @returns { number } Maximum transmitted data size
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 22
     */
    function getMaxTransmitDataSize(clientSocket: number): number;
    /**
     * Check whether the current socket connection has been established.
     *
     * @param { number } clientSocket - Indicates client socket.
     * @returns { boolean } Indicates whether or not it is connected.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 22
     */
    function isConnected(clientSocket: number): boolean;
    /**
     * Disables an spp server socket and releases related resources.
     *
     * @param { number } socket - Indicates the server socket ID, returned by {@link sppListen}.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    function sppCloseServerSocket(socket: number): void;
    /**
     * Disables an spp client socket and releases related resources.
     *
     * @param { number } socket - Indicates the client socket ID, returned by {@link sppAccept} or {@link sppConnect}.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    function sppCloseClientSocket(socket: number): void;
    /**
     * Write data through the socket.
     *
     * @param { number } clientSocket - Indicates the client socket ID, returned by {@link sppAccept} or {@link sppConnect}.
     * @param { ArrayBuffer } data - Indicates the data to write.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2901054 - IO error.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    function sppWrite(clientSocket: number, data: ArrayBuffer): void;
    /**
     * Subscribe the event reported when data is read from the socket.
     *
     * @param { 'sppRead' } type - Type of the spp read event to listen for.
     * @param { number } clientSocket - Client socket ID, which is obtained by sppAccept or sppConnect.
     * @param { Callback<ArrayBuffer> } callback - Callback used to listen for the spp read event.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2901054 - IO error.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    function on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void;
    /**
     * Unsubscribe the event reported when data is read from the socket.
     *
     * @param { 'sppRead' } type - Type of the spp read event to listen for.
     * @param { number } clientSocket - Client socket ID, which is obtained by sppAccept or sppConnect.
     * @param { Callback<ArrayBuffer> } callback - Callback used to listen for the spp read event.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    function off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void;
    /**
     * Asynchronous interface for writing data to the socket.
     *
     * @param { number } clientSocket - Indicates the client socket ID, returned by {@link sppAccept} or {@link sppConnect}.
     * @param { ArrayBuffer } data - Indicates the data to write.
     * @returns { Promise<void> } Returns the promise object.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2901054 - IO error.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 18
     */
    function sppWriteAsync(clientSocket: number, data: ArrayBuffer): Promise<void>;
    /**
     * Asynchronous interface for reading data from the socket.
     *
     * @param { number } clientSocket - Indicates the client socket ID, returned by {@link sppAccept} or {@link sppConnect}.
     * @returns { Promise<ArrayBuffer> } Returns the promise object, used to get the spp read data.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2901054 - IO error.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 18
     */
    function sppReadAsync(clientSocket: number): Promise<ArrayBuffer>;
    /**
     * Describes the spp parameters.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    interface SppOptions {
        /**
         * Indicates the UUID in the SDP record.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 10
         */
        uuid: string;
        /**
         * Indicates secure channel or not
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 10
         */
        secure: boolean;
        /**
         * Spp link type
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 10
         */
        type: SppType;
        /**
         * l2cap protocol service multiplexer
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 20
         */
        psm?: number;
    }
    /**
     * The enum of SPP type.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    enum SppType {
        /**
         * RFCOMM
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 10
         */
        SPP_RFCOMM = 0,
        /**
         * L2CAP of the BR type
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 20
         */
        SPP_L2CAP = 1,
        /**
         * L2CAP of the BLE type
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 20
         */
        SPP_L2CAP_BLE = 2
    }
}
export default socket;

```
