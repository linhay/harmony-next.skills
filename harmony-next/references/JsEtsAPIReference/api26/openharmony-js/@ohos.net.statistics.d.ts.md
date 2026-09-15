# @ohos.net.statistics.d.ts

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
 * @file Traffic Management
 * @kit NetworkKit
 */
import type { AsyncCallback } from './@ohos.base';
import type connection from './@ohos.net.connection';
/**
 * The Traffic Management module provides the capability to obtain device network traffic data. This module supports
 * querying packet traffic usage from multiple dimensions, for example:
 *
 * - Obtaining the uplink/downlink traffic data of a specified NIC.
 * - Obtaining the total traffic data of all NICs, facilitating the viewing of overall device network usage.
 * - Obtaining the traffic data of a specified application based on the application UID, helping you monitor the network
 * resource consumption of applications.
 * - Obtaining traffic statistics for a specified socket, providing a data foundation for fine-grained network
 * performance analysis.
 * - Obtaining the historical traffic usage of an application within a specified time period, facilitating the analysis
 * of long-term network usage trends of the application.
 *
 * @syscap SystemCapability.Communication.NetManager.Core
 * @atomicservice [since 15]
 * @since 10
 */
declare namespace statistics {
    /**
     * Defines the network type.
     *
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 12
     */
    type NetBearType = connection.NetBearType;
    /**
     * Obtains the total downlink traffic of the specified NIC from the last startup to the time when this API is called (
     * in bytes). This API uses an asynchronous callback to return the result.
     *
     * @param { string } nic - NIC name.
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the traffic data is successfully
     *     obtained, **error** is **undefined**; otherwise, it is an error object.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @throws { BusinessError } 2103012 - Failed to obtain the NIC name.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    function getIfaceRxBytes(nic: string, callback: AsyncCallback<number>): void;
    /**
     * Obtains the total downlink traffic (in bytes) of the specified NIC from the last startup to the time when this API
     * is called. This API uses a promise to return the result.
     *
     * @param { string } nic - NIC name.
     * @returns { Promise<number> } Promise used to return the total downlink traffic (in bytes) of the specified NIC from
     *     the last startup to the current moment.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @throws { BusinessError } 2103012 - Failed to obtain the NIC name.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    function getIfaceRxBytes(nic: string): Promise<number>;
    /**
     * Obtains the total uplink traffic (in bytes) of the specified NIC from the last startup to the time when this API is
     * called. This API uses an asynchronous callback to return the result.
     *
     * @param { string } nic - NIC name.
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the traffic data is successfully
     *     obtained, **error** is **undefined**; otherwise, it is an error object.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @throws { BusinessError } 2103012 - Failed to obtain the NIC name.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    function getIfaceTxBytes(nic: string, callback: AsyncCallback<number>): void;
    /**
     * Obtains the total uplink traffic (in bytes) of the specified NIC from the last startup to the time when this API is
     * called. This API uses a promise to return the result.
     *
     * @param { string } nic - NIC name.
     * @returns { Promise<number> } Promise used to return the total uplink traffic (in bytes) of the specified NIC from the
     *     last startup to the time when the API is called.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @throws { BusinessError } 2103012 - Failed to obtain the NIC name.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    function getIfaceTxBytes(nic: string): Promise<number>;
    /**
     * Obtains the total downlink traffic (in bytes) of the NIC corresponding to the currently connected cellular network
     * from the last startup to the time when this API is called. This API uses an asynchronous callback to return the
     * result.
     *
     * > **NOTE**
     * >
     * > It is recommended to call this API when the cellular network is in the connected state. Otherwise, error code 210
     * > 3012 will be thrown.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the traffic data is successfully
     *     obtained, **error** is **undefined**; otherwise, it is an error object.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @throws { BusinessError } 2103012 - Failed to obtain the NIC name.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    function getCellularRxBytes(callback: AsyncCallback<number>): void;
    /**
     * Obtains the total downlink traffic (in bytes) of the NIC corresponding to the currently connected cellular network
     * from the last startup to the time when this API is called. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > It is recommended to call this API when the cellular network is in the connected state. Otherwise, error code 210
     * > 3012 will be thrown.
     *
     * @returns { Promise<number> } Promise used to return the total downlink traffic (in bytes) of the specified NIC from
     *     the last startup to the time when the API is called.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @throws { BusinessError } 2103012 - Failed to obtain the NIC name.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    function getCellularRxBytes(): Promise<number>;
    /**
     * Obtains the total uplink traffic (in bytes) of the NIC corresponding to the currently connected cellular network
     * from the last startup to the time when this API is called. This API uses an asynchronous callback to return the
     * result.
     *
     * > **NOTE**
     * >
     * > It is recommended to call this API when the cellular network is in the connected state. Otherwise, error code 210
     * > 3012 will be thrown.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the traffic data is successfully
     *     obtained, **error** is **undefined**; otherwise, it is an error object.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @throws { BusinessError } 2103012 - Failed to obtain the NIC name.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    function getCellularTxBytes(callback: AsyncCallback<number>): void;
    /**
     * Obtains the total uplink traffic (in bytes) of the NIC corresponding to the currently connected cellular network
     * from the last startup to the time when this API is called. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > It is recommended to call this API when the cellular network is in the connected state. Otherwise, error code 210
     * > 3012 will be thrown.
     *
     * @returns { Promise<number> } Promise used to return the total uplink traffic (in bytes) consumed on the cellular
     *     network since the last startup to the current moment.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @throws { BusinessError } 2103012 - Failed to obtain the NIC name.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    function getCellularTxBytes(): Promise<number>;
    /**
     * Obtains the total downlink traffic (in bytes) of all NICs from the last startup to the time when this API is
     * called. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the traffic data is successfully
     *     obtained, **error** is **undefined**; otherwise, it is an error object.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @atomicservice [since 15]
     * @since 10
     */
    function getAllRxBytes(callback: AsyncCallback<number>): void;
    /**
     * Obtains the total downlink traffic (in bytes) of all NICs from the last startup to the time when this API is
     * called. This API uses a promise to return the result.
     *
     * @returns { Promise<number> } Promise used to return the total downlink traffic (in bytes) of all NICs from the last
     *     startup to the current moment.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @atomicservice [since 15]
     * @since 10
     */
    function getAllRxBytes(): Promise<number>;
    /**
     * Obtains the total uplink traffic of all NICs (in bytes) from the last startup to the time when this API is called.
     * This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the traffic data is successfully
     *     obtained, **error** is **undefined**; otherwise, it is an error object.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @atomicservice [since 15]
     * @since 10
     */
    function getAllTxBytes(callback: AsyncCallback<number>): void;
    /**
     * Obtains the total uplink traffic (in bytes) of all NICs from the last startup to the time when this API is called.
     * This API uses a promise to return the result.
     *
     * @returns { Promise<number> } Promise used to return the real-time uplink traffic (in bytes) of all NICs.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @atomicservice [since 15]
     * @since 10
     */
    function getAllTxBytes(): Promise<number>;
    /**
     * Obtains the total downlink traffic (in bytes) of the specified application from the last startup to the time when
     * this API is called. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > If the application has not generated any traffic consumption after the restart, error code 2103005 will be
     * > thrown.
     *
     * @permission ohos.permission.GET_NETWORK_STATS [since 26.0.0]
     * @param { number } uid - Application UID.
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the traffic data is successfully
     *     obtained, **error** is **undefined**; otherwise, it is an error object.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @throws { BusinessError } 201 - Permission denied. [since 26.0.0]
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    function getUidRxBytes(uid: number, callback: AsyncCallback<number>): void;
    /**
     * Obtains the total downlink traffic (in bytes) of the specified application from the last startup to the time when
     * this API is called. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > If the application has not generated any traffic consumption after the restart, error code 2103005 will be
     * > thrown.
     *
     * @permission ohos.permission.GET_NETWORK_STATS [since 26.0.0]
     * @param { number } uid - Application UID.
     * @returns { Promise<number> } Promise used to return the total downlink traffic (in bytes) of the specified
     *     application from the last startup to the current moment.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @throws { BusinessError } 201 - Permission denied. [since 26.0.0]
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    function getUidRxBytes(uid: number): Promise<number>;
    /**
     * Obtains the total uplink traffic (in bytes) of the specified application from the last startup to the time when
     * this API is called. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > If the application has not generated any traffic consumption after the restart, error code 2103005 will be
     * > thrown.
     *
     * @permission ohos.permission.GET_NETWORK_STATS [since 26.0.0]
     * @param { number } uid - Application UID.
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the application's real-time uplink
     *     traffic is successfully obtained, **error** is **undefined** and **stats** is the obtained application uplink
     *     traffic (in bytes). Otherwise, it is an error object.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @throws { BusinessError } 201 - Permission denied. [since 26.0.0]
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    function getUidTxBytes(uid: number, callback: AsyncCallback<number>): void;
    /**
     * Obtains the total uplink traffic of the specified application from the last startup to the time when this API is
     * called (in bytes). This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > If the application has not generated any traffic consumption after the restart, error code 2103005 will be
     * > thrown.
     *
     * @permission ohos.permission.GET_NETWORK_STATS [since 26.0.0]
     * @param { number } uid - Application UID.
     * @returns { Promise<number> } Promise used to return the total uplink traffic (in bytes) of the specified application
     *     from the last startup to the time when the API is called.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103005 - Failed to read the system map.
     * @throws { BusinessError } 2103011 - Failed to create a system map.
     * @throws { BusinessError } 201 - Permission denied. [since 26.0.0]
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 10
     */
    function getUidTxBytes(uid: number): Promise<number>;
    /**
     * Obtains the downlink traffic (in bytes) of the specified socket. This API uses an asynchronous callback to return
     * the result.
     *
     * > **NOTE**
     * >
     * > It is recommended to use this API when the socket is connected. Otherwise, the corresponding traffic data cannot
     * > be queried after the socket is closed.
     *
     * @param { number } sockfd - File description (FD) of the socket to query.
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the downlink traffic of the socket
     *     is obtained successfully, **error** is **undefined**; otherwise, it is an error object.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100001 - Invalid parameter value.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 11
     */
    function getSockfdRxBytes(sockfd: number, callback: AsyncCallback<number>): void;
    /**
     * Obtains the downlink traffic (in bytes) of the specified socket. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > It is recommended to use this API when the socket is connected. Otherwise, the corresponding traffic data cannot
     * > be queried after the socket is closed.
     *
     * @param { number } sockfd - FD of the socket to query.
     * @returns { Promise<number> } Promise used to return the downlink traffic (in bytes) of the socket.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100001 - Invalid parameter value.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 11
     */
    function getSockfdRxBytes(sockfd: number): Promise<number>;
    /**
     * Obtains the uplink traffic of the specified socket (in bytes). This API uses an asynchronous callback to return the
     * result.
     *
     * > **NOTE**
     * >
     * > It is recommended to use this API when the socket is connected. Otherwise, the corresponding traffic data cannot
     * > be queried after the socket is closed.
     *
     * @param { number } sockfd - FD of the socket to query.
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the uplink traffic of the socket
     *     is obtained successfully, **error** is **undefined**; otherwise, it is an error object.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100001 - Invalid parameter value
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 11
     */
    function getSockfdTxBytes(sockfd: number, callback: AsyncCallback<number>): void;
    /**
     * Obtains the uplink traffic (in bytes) of the specified socket. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > It is recommended to use this API when the socket is connected. Otherwise, the corresponding traffic data cannot
     * > be queried after the socket is closed.
     *
     * @param { number } sockfd - FD of the socket to query.
     * @returns { Promise<number> } Promise used to return the uplink traffic (in bytes) of the socket.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100001 - Invalid parameter value
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 11
     */
    function getSockfdTxBytes(sockfd: number): Promise<number>;
    /**
     * Defines the historical traffic information.
     *
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 22
     */
    export interface NetStatsInfo {
        /**
         * Downlink traffic data (unit: bytes).
         *
         * @syscap SystemCapability.Communication.NetManager.Core
         * @since 22
         */
        rxBytes: number;
        /**
         * Uplink traffic data (unit: bytes).
         *
         * @syscap SystemCapability.Communication.NetManager.Core
         * @since 22
         */
        txBytes: number;
        /**
         * Number of downlink packets.
         *
         * @syscap SystemCapability.Communication.NetManager.Core
         * @since 22
         */
        rxPackets: number;
        /**
         * Number of uplink packets.
         *
         * @syscap SystemCapability.Communication.NetManager.Core
         * @since 22
         */
        txPackets: number;
    }
    /**
     * Defines the network information.
     *
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 22
     */
    export interface NetworkInfo {
        /**
         * Network type.
         *
         * **Note**: If **type** is set to **cellular**, the **simId** field must be specified.
         *
         * @syscap SystemCapability.Communication.NetManager.Core
         * @since 22
         */
        type: NetBearType;
        /**
         * Start timestamp, in seconds.
         *
         * @syscap SystemCapability.Communication.NetManager.Core
         * @since 22
         */
        startTime: number;
        /**
         * End timestamp, in seconds.
         *
         * @syscap SystemCapability.Communication.NetManager.Core
         * @since 22
         */
        endTime: number;
        /**
         * SIM card ID. The default value is the maximum value of the uint32_t type.
         *
         * **Note**: If **type** is set to **cellular**, this field must be specified.
         *
         * @syscap SystemCapability.Communication.NetManager.Core
         * @since 22
         */
        simId?: number;
    }
    /**
     * Obtains the traffic statistics of the specified application on the specified network within the specified period.
     * This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - Currently, only cellular and Wi-Fi traffic usage can be obtained.
     *
     * > - Currently, only traffic usage within the last 31 days can be obtained. If the timestamp passed in the parameter
     * > is earlier than 31 days before the current system time, error code 2103019 will be returned.
     * >
     * > - This API may take some time to execute. Do not call it frequently.
     *
     * @param { NetworkInfo } networkInfo - Network information.
     * @returns { Promise<NetStatsInfo> } Promise used to return the historical traffic statistics of the application.
     * @throws { BusinessError } 2100001 - Invalid parameter value.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2103017 - Failed to read the database.
     * @throws { BusinessError } 2103019 - The timestamp in param is invalid.
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 22
     */
    function getSelfTrafficStats(networkInfo: NetworkInfo): Promise<NetStatsInfo>;
}
export default statistics;

```
