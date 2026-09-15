# @ohos.net.ethernet.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2022-2024 Huawei Device Co., Ltd.
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
 * @file Ethernet Connection Management
 * @kit NetworkKit
 */
import type connection from './@ohos.net.connection';
/**
 * The **ethernet** module provides Ethernet management functions such as configuring a network proxy and obtaining the
 * network IP address.
 *
 * @syscap SystemCapability.Communication.NetManager.Ethernet
 * @since 9
 */
declare namespace ethernet {
    /**
     * Defines the network proxy configuration.
     *
     * @syscap SystemCapability.Communication.NetManager.Ethernet
     * @since 10
     */
    type HttpProxy = connection.HttpProxy;
    /**
     * Obtains the names and MAC addresses of all Ethernet NICs. This API uses a promise to return the result.
     *
     * **Required permission**: ohos.permission.GET_ETHERNET_LOCAL_MAC
     *
     * @permission ohos.permission.GET_ETHERNET_LOCAL_MAC
     * @returns { Promise<Array<MacAddressInfo>> } Promise used to return the result.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 2200002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 2201005 - Device information does not exist.
     * @syscap SystemCapability.Communication.NetManager.Ethernet
     * @since 14
     */
    function getMacAddress(): Promise<Array<MacAddressInfo>>;
    /**
     * Defines the name and MAC address of an Ethernet NIC.
     *
     * @syscap SystemCapability.Communication.NetManager.Ethernet
     * @since 14
     */
    export interface MacAddressInfo {
        /**
         * Name of the Ethernet NIC.
         *
         * @syscap SystemCapability.Communication.NetManager.Ethernet
         * @since 14
         */
        iface: string;
        /**
         * MAC address of the Ethernet NIC.
         *
         * @syscap SystemCapability.Communication.NetManager.Ethernet
         * @since 14
         */
        macAddress: string;
    }
}
export default ethernet;

```
