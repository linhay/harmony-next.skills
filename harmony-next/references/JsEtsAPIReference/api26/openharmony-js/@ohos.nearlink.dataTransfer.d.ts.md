# @ohos.nearlink.dataTransfer.d.ts

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
import nearlinkConstant from '@ohos.nearlink.constant';
/**
 * Provides methods to operate and manage data transfer of NearLink.
 *
 * @syscap SystemCapability.Communication.NearLink.Base
 * @stagemodelonly
 * @since 26.0.0
 */
declare namespace dataTransfer {
    /**
     * Indicates the connection state.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    type ConnectionState = nearlinkConstant.ConnectionState;
    /**
     * Creates a NearLink listening port that can receive data by UUID.
     *
     * @permission ohos.permission.ACCESS_NEARLINK
     * @param { string } uuid - Indicates application service UUID.
     *     <br>The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-), for example,
     *     FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.
     *     <br>NearLink standard UUIDs not allowed.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100003 - NearLink disabled.
     * @throws { BusinessError } 36100020 - The UUID is already registered.
     * @throws { BusinessError } 36100021 - Port exceeds the upper limit.
     * @throws { BusinessError } 36100043 - Invalid UUID.
     * @throws { BusinessError } 36100044 - NearLink standard UUID not allowed.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function createPort(uuid: string): void;
    /**
     * Destroys a listen port and releases related resources by UUID.
     *
     * @permission ohos.permission.ACCESS_NEARLINK
     * @param { string } uuid - Indicates application service UUID.
     *     <br>The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-), for example,
     *     FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.
     *     <br>NearLink standard UUIDs not allowed.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100003 - NearLink disabled.
     * @throws { BusinessError } 36100022 - The UUID is not registered.
     * @throws { BusinessError } 36100043 - Invalid UUID.
     * @throws { BusinessError } 36100044 - NearLink standard UUID not allowed.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function destroyPort(uuid: string): void;
    /**
     * Connects to a server. If the connection is successful, data can be sent to the server.
     *
     * @permission ohos.permission.ACCESS_NEARLINK
     * @param { ConnectionParams } params - Indicates the connection params.
     * @returns { Promise<void> } Returns the promise object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100003 - NearLink disabled.
     * @throws { BusinessError } 36100041 - Invalid address.
     * @throws { BusinessError } 36100043 - Invalid UUID.
     * @throws { BusinessError } 36100044 - NearLink standard UUID not allowed.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function connect(params: ConnectionParams): Promise<void>;
    /**
     * Disconnects or stops an ongoing connection to a server.
     *
     * @permission ohos.permission.ACCESS_NEARLINK
     * @param { ConnectionParams } params - Indicates the connection params.
     * @returns { Promise<void> } Returns the promise object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100003 - NearLink disabled.
     * @throws { BusinessError } 36100041 - Invalid address.
     * @throws { BusinessError } 36100043 - Invalid UUID.
     * @throws { BusinessError } 36100044 - NearLink standard UUID not allowed.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function disconnect(params: ConnectionParams): Promise<void>;
    /**
     * Subscribes to the connection state change event.
     *
     * This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.
     *
     * @param { Callback<ConnectionResult> } callback - Callback used to listen for the state change event.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function onConnectionStateChanged(callback: Callback<ConnectionResult>): void;
    /**
     * Unsubscribes from the connection state change event.
     *
     * @param { Callback<ConnectionResult> } [callback] - Callback used to listen for the state change event.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function offConnectionStateChanged(callback?: Callback<ConnectionResult>): void;
    /**
     * Writes data by address and UUID.
     *
     * @permission ohos.permission.ACCESS_NEARLINK
     * @param { DataParams } params - Indicates the send data params.
     * @returns { Promise<void> } Returns the promise object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100003 - NearLink disabled.
     * @throws { BusinessError } 36100023 - Write data congestion.
     * @throws { BusinessError } 36100041 - Invalid address.
     * @throws { BusinessError } 36100043 - Invalid UUID.
     * @throws { BusinessError } 36100044 - NearLink standard UUID not allowed.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function writeData(params: DataParams): Promise<void>;
    /**
     * Subscribes to the event reported when data is read from the port.
     *
     * This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.
     *
     * @param { Callback<DataParams> } callback - Callback used to listen for the port read event.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function onReadData(callback: Callback<DataParams>): void;
    /**
     * Unsubscribes from the event reported when data is read from the port.
     *
     * @param { Callback<DataParams> } [callback] - Callback used to listen for the port read event.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function offReadData(callback?: Callback<DataParams>): void;
    /**
     * Obtains the connection status for data transfer.
     *
     * @permission ohos.permission.ACCESS_NEARLINK
     * @param { ConnectionStateParams } params - Parameters used to obtain the connection status.
     * @returns { ConnectionState } Returns the connection status for data transfer.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100003 - NearLink disabled.
     * @throws { BusinessError } 36100041 - Invalid address.
     * @throws { BusinessError } 36100043 - Invalid UUID in connection parameters.
     * @throws { BusinessError } 36100044 - NearLink standard UUID not allowed.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function getConnectionState(params: ConnectionStateParams): ConnectionState;
    /**
     * Describes the parameters for connection.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface ConnectionParams {
        /**
         * Indicates the connected device address.
         * The length must be 17, The value consists of hexadecimal digits and colons (:),
         * for example, 11:22:33:AA:BB:FF.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        address: string;
        /**
         * Indicates the service UUID.
         * The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-),
         * for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.
         * <br>NearLink standard UUIDs are not allowed.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        uuid: string;
        /**
         * Data transfer mode. The basic transfer mode is used by default
         * Default value: BASIC.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        transferMode?: TransferMode;
    }
    /**
     * Describes the parameters for Data.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface DataParams {
        /**
         * Indicates the connected device address.
         * The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        address: string;
        /**
         * Indicates the service UUID.
         * The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-),
         * for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.
         * <br>NearLink standard UUIDs are not allowed.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        uuid: string;
        /**
         * Indicates the data buffer.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        data: ArrayBuffer;
    }
    /**
     * Describes the parameters for connection result.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface ConnectionResult {
        /**
         * Indicates the connected device address.
         * The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        address: string;
        /**
         * Indicates the service UUID.
         * The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-),
         * for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.
         * <br>NearLink standard UUIDs are not allowed.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        uuid: string;
        /**
         * Indicates the maximum channel data length.
         * Unit: Bytes, The value must be an integer within [0,65535].
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        mtu: number;
        /**
         * Connection state.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        state: ConnectionState;
    }
    /**
     * Describes the parameters required for obtaining the connection status.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface ConnectionStateParams {
        /**
         * Indicates the connected device address.
         * The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        address: string;
        /**
         * Indicates the service uuid.
         * The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-),
         * for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.
         * <br>NearLink standard UUIDs are not allowed.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        uuid: string;
    }
    /**
     * Indicates the data transfer mode.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    enum TransferMode {
        /**
         * Basic data transfer mode.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        BASIC = 0,
        /**
         * Reliable data transfer mode.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        RELIABLE = 1
    }
}
export default dataTransfer;

```
