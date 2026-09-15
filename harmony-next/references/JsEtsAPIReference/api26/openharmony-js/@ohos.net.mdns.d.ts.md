# @ohos.net.mdns.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
 * @file MDNS Management
 * @kit NetworkKit
 */
import { AsyncCallback, Callback } from './@ohos.base';
import connection from './@ohos.net.connection';
import Context from './application/Context';
/**
 * Multicast DNS (MDNS) provides functions such as adding, removing, discovering, and resolving local services on a LAN.
 *
 * @syscap SystemCapability.Communication.NetManager.MDNS
 * @atomicservice [since 11]
 * @since 10
 */
declare namespace mdns {
    /**
     * Obtains the network address.
     *
     * @syscap SystemCapability.Communication.NetManager.Core
     * @atomicservice [since 12]
     * @since 10
     */
    type NetAddress = connection.NetAddress;
    /**
     * Adds an MDNS service. This API uses an asynchronous callback to return the result.
     *
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see [Context]{@link ./app/context}.
     *     <br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { LocalServiceInfo } serviceInfo - MDNS service information.
     * @param { AsyncCallback<LocalServiceInfo> } callback - Callback used to return the result. If the operation is
     *     successful, **error** is **undefined** and **data** is the MDNS service information.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2204003 - Callback duplicated.
     * @throws { BusinessError } 2204008 - Failed to delete the service instance.
     * @throws { BusinessError } 2204010 - Failed to send the message.
     * @syscap SystemCapability.Communication.NetManager.MDNS
     * @atomicservice [since 11]
     * @since 10
     */
    function addLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void;
    /**
     * Adds an MDNS service. This API uses a promise to return the result.
     *
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see [Context]{@link ./app/context}.
     *     <br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { LocalServiceInfo } serviceInfo - MDNS service information.
     * @returns { Promise<LocalServiceInfo> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2204003 - Callback duplicated.
     * @throws { BusinessError } 2204008 - Failed to delete the service instance.
     * @throws { BusinessError } 2204010 - Failed to send the message.
     * @syscap SystemCapability.Communication.NetManager.MDNS
     * @atomicservice [since 11]
     * @since 10
     */
    function addLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>;
    /**
     * Removes an MDNS service. This API uses an asynchronous callback to return the result.
     *
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see [Context]{@link ./app/context}.
     *     <br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { LocalServiceInfo } serviceInfo - MDNS service information.
     * @param { AsyncCallback<LocalServiceInfo> } callback - Callback used to return the result. If the operation is
     *     successful, **error** is **undefined** and **data** is the MDNS service information.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2204002 - Callback not found.
     * @throws { BusinessError } 2204008 - Failed to delete the service instance.
     * @throws { BusinessError } 2204010 - Failed to send the message.
     * @syscap SystemCapability.Communication.NetManager.MDNS
     * @atomicservice [since 11]
     * @since 10
     */
    function removeLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void;
    /**
     * Removes an MDNS service. This API uses a promise to return the result.
     *
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see [Context]{@link ./app/context}.
     *     <br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { LocalServiceInfo } serviceInfo - MDNS service information.
     * @returns { Promise<LocalServiceInfo> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2204002 - Callback not found.
     * @throws { BusinessError } 2204008 - Failed to delete the service instance.
     * @throws { BusinessError } 2204010 - Failed to send the message.
     * @syscap SystemCapability.Communication.NetManager.MDNS
     * @atomicservice [since 11]
     * @since 10
     */
    function removeLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>;
    /**
     * Creates a **DiscoveryService** object, which is used to discover MDNS services of the specified type.
     *
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see [Context]{@link ./app/context}.
     *     <br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { string } serviceType - MDNS service type.
     * @returns { DiscoveryService } **DiscoveryService** object obtained based on the specified **serviceType** and
     *     **context**.
     * @throws { BusinessError } 401 - Parameter error.
     * @syscap SystemCapability.Communication.NetManager.MDNS
     * @atomicservice [since 11]
     * @since 10
     */
    function createDiscoveryService(context: Context, serviceType: string): DiscoveryService;
    /**
     * Resolves an MDNS service. This API uses an asynchronous callback to return the result.
     *
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see [Context]{@link ./app/context}.
     *     <br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { LocalServiceInfo } serviceInfo - MDNS service information.
     * @param { AsyncCallback<LocalServiceInfo> } callback - Callback used to return the result. If the operation is
     *     successful, **error** is **undefined** and **data** is the MDNS service information.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2204003 - Callback duplicated.
     * @throws { BusinessError } 2204006 - Request timeout.
     * @throws { BusinessError } 2204010 - Failed to send the message.
     * @syscap SystemCapability.Communication.NetManager.MDNS
     * @atomicservice [since 11]
     * @since 10
     */
    function resolveLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void;
    /**
     * Resolves an MDNS service. This API uses a promise to return the result.
     *
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see [Context]{@link ./app/context}.
     *     <br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { LocalServiceInfo } serviceInfo - MDNS service information.
     * @returns { Promise<LocalServiceInfo> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100002 - Failed to connect to the service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 2204003 - Callback duplicated.
     * @throws { BusinessError } 2204006 - Request timeout.
     * @throws { BusinessError } 2204010 - Failed to send the message.
     * @syscap SystemCapability.Communication.NetManager.MDNS
     * @atomicservice [since 11]
     * @since 10
     */
    function resolveLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>;
    /**
     * Defines a **DiscoveryService** object for discovering MDNS services of the specified type.
     *
     * @syscap SystemCapability.Communication.NetManager.MDNS
     * @atomicservice [since 11]
     * @since 10
     */
    export interface DiscoveryService {
        /**
         * Enables listening for **discoveryStart** events.
         *
         * @param { 'discoveryStart' } type - Event type. This field has a fixed value of **discoveryStart**.
         *     <br>**discoveryStart**: event of starting discovery of MDNS services on the LAN.
         * @param { Callback<{ serviceInfo: LocalServiceInfo, errorCode?: MdnsError }> } callback - Callback used to return
         *     the MDNS service and error information. [since 10 - 10]
         * @param { Callback<DiscoveryEventInfo> } callback - Callback used to return the MDNS service and error
         *     information. [since 11]
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        on(type: 'discoveryStart', callback: Callback<DiscoveryEventInfo>): void;
        /**
         * Disables listening for **discoveryStart** events.
         *
         * @param { 'discoveryStart' } type - Event type. This field has a fixed value of **discoveryStart**.
         *     <br>**discoveryStart**: event of starting discovery of MDNS services on the LAN.
         * @param { Callback<{ serviceInfo: LocalServiceInfo, errorCode?: MdnsError }> } callback - Callback used to return
         *     the MDNS service and error information. You can pass the callback of the **on** function if you want to
         *     cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for
         *     all events. [since 10 - 10]
         * @param { Callback<DiscoveryEventInfo> } callback - Callback used to return the MDNS service and error
         *     information. You can pass the callback of the **on** function if you want to cancel listening for a certain
         *     type of events. If you do not pass the callback, you will cancel listening for all events. [since 11]
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        off(type: 'discoveryStart', callback?: Callback<DiscoveryEventInfo>): void;
        /**
         * Enables listening for **discoveryStop** events.
         *
         * @param { 'discoveryStop' } type - Event type. This field has a fixed value of **discoveryStop**.
         *     <br>**discoveryStop**: event of stopping discovery of MDNS services on the LAN.
         * @param { Callback<{ serviceInfo: LocalServiceInfo, errorCode?: MdnsError }> } callback - Callback used to return
         *     the MDNS service and error information. [since 10 - 10]
         * @param { Callback<DiscoveryEventInfo> } callback - Callback used to return the MDNS service and error
         *     information. [since 11]
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        on(type: 'discoveryStop', callback: Callback<DiscoveryEventInfo>): void;
        /**
         * Disables listening for **discoveryStop** events.
         *
         * @param { 'discoveryStop' } type - Event type. This field has a fixed value of **discoveryStop**.
         *     <br>**discoveryStop**: event of stopping discovery of MDNS services on the LAN.
         * @param { Callback<{ serviceInfo: LocalServiceInfo, errorCode?: MdnsError }> } callback - Callback used to return
         *     the MDNS service and error information. You can pass the callback of the **on** function if you want to
         *     cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for
         *     all events. [since 10 - 10]
         * @param { Callback<DiscoveryEventInfo> } callback - Callback used to return the MDNS service and error
         *     information. You can pass the callback of the **on** function if you want to cancel listening for a certain
         *     type of events. If you do not pass the callback, you will cancel listening for all events. [since 11]
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        off(type: 'discoveryStop', callback?: Callback<DiscoveryEventInfo>): void;
        /**
         * Enables listening for **serviceFound** events.
         *
         * @param { 'serviceFound' } type - Event type. This field has a fixed value of **serviceFound**.
         *     <br>**serviceFound**: event indicating an MDNS service is found.
         * @param { Callback<LocalServiceInfo> } callback - Callback used to return the MDNS service information. You need
         *     to call **resolveLocalService** to parse the information.
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        on(type: 'serviceFound', callback: Callback<LocalServiceInfo>): void;
        /**
         * Disables listening for **serviceFound** events.
         *
         * @param { 'serviceFound' } type - Event type. This field has a fixed value of **serviceFound**.
         *     <br>**serviceFound**: event indicating an MDNS service is found.
         * @param { Callback<LocalServiceInfo> } callback - MDNS service information. You can pass the callback of the
         *     **on** function if you want to cancel listening for a certain type of events. If you do not pass the
         *     callback, you will cancel listening for all events. [since 10 - 10]
         * @param { Callback<LocalServiceInfo> } [callback] - MDNS service information. You can pass the callback of the
         *     **on** function if you want to cancel listening for a certain type of events. If you do not pass the
         *     callback, you will cancel listening for all events. [since 11]
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        off(type: 'serviceFound', callback?: Callback<LocalServiceInfo>): void;
        /**
         * Enables listening for **serviceLost** events.
         *
         * @param { 'serviceLost' } type - Event type. This field has a fixed value of **serviceLost**.
         *     <br>**serviceLost**: event indicating that an MDNS service is removed.
         * @param { Callback<LocalServiceInfo> } callback - MDNS service information.
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        on(type: 'serviceLost', callback: Callback<LocalServiceInfo>): void;
        /**
         * Disables listening for **serviceLost** events.
         *
         * @param { 'serviceLost' } type - Event type. This field has a fixed value of **serviceLost**.
         *     <br>**serviceLost**: event indicating that an MDNS service is removed.
         * @param { Callback<LocalServiceInfo> } callback - MDNS service information. You can pass the callback of the
         *     **on** function if you want to cancel listening for a certain type of events. If you do not pass the
         *     callback, you will cancel listening for all events.
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        off(type: 'serviceLost', callback?: Callback<LocalServiceInfo>): void;
        /**
         * Searches for MDNS services on the LAN.
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        startSearchingMDNS(): void;
        /**
         * Stops searching for MDNS services on the LAN.
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        stopSearchingMDNS(): void;
    }
    /**
     * MDNS service information.
     *
     * @syscap SystemCapability.Communication.NetManager.MDNS
     * @atomicservice [since 11]
     * @since 10
     */
    export interface LocalServiceInfo {
        /**
         * MDNS service type. The value is in the format of **_<name>.<_tcp/_udp>**, where **name** contains a maximum of 63
         * characters excluding periods (.).
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        serviceType: string;
        /**
         * MDNS service name.
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        serviceName: string;
        /**
         * Service port number. The value range is [0, 65535].
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        port?: number;
        /**
         * IP address of the device that provides the MDNS service. The IP address is not effective when an MDNS service is
         * added or removed.
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        host?: NetAddress;
        /**
         * MDNS service attribute information.
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        serviceAttribute?: Array<ServiceAttribute>;
    }
    /**
     * MDNS service attribute information.
     *
     * @syscap SystemCapability.Communication.NetManager.MDNS
     * @atomicservice [since 11]
     * @since 10
     */
    export interface ServiceAttribute {
        /**
         * MDNS service attribute key. The value contains a maximum of 9 characters.
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        key: string;
        /**
         * MDNS service attribute value.
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        value: Array<number>;
    }
    /**
     * Defines the MDNS service event information.
     *
     * @syscap SystemCapability.Communication.NetManager.MDNS
     * @atomicservice
     * @since 11
     */
    export interface DiscoveryEventInfo {
        /**
         * MDNS service information.
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice
         * @since 11
         */
        serviceInfo: LocalServiceInfo;
        /**
         * MDNS error information.
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice
         * @since 11
         */
        errorCode?: MdnsError;
    }
    /**
     * Defines the MDNS error information.
     *
     * @syscap SystemCapability.Communication.NetManager.MDNS
     * @atomicservice [since 11]
     * @since 10
     */
    export enum MdnsError {
        /**
         * Operation failed because of an internal error.
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        INTERNAL_ERROR = 0,
        /**
         * Operation failed because the service already exists.
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        ALREADY_ACTIVE = 1,
        /**
         * Operation failed because the number of requests exceeds the maximum value.
         *
         * @syscap SystemCapability.Communication.NetManager.MDNS
         * @atomicservice [since 11]
         * @since 10
         */
        MAX_LIMIT = 2
    }
}
export default mdns;

```
