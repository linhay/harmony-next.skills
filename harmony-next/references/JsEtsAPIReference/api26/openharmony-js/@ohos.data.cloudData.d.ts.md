# @ohos.data.cloudData.d.ts

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
 * @file
 * @kit ArkData
 */
import { Callback } from './@ohos.base';
import commonType from './@ohos.data.commonType';
/**
 * The **cloudData** module provides APIs for implementing device-cloud synergy and device-cloud sharing, and setting
 * the device-cloud sync strategy.
 *
 * Device-cloud synergy enables sync of the structured data (in RDB stores) between devices and the cloud. The cloud
 * serves as a data hub to implement data backup in the cloud and data consistency between the devices with the same
 * account.
 * This module also provides the capability of setting the device-cloud sync strategy.
 *
 * @syscap SystemCapability.DistributedDataManager.CloudSync.Config
 * @since 10
 */
declare namespace cloudData {
    /**
     * Enumerates the types of the cloud-device sync strategy.
     *
     * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
     * @since 12
     */
    enum StrategyType {
        /**
         * Sync over the network.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 12
         */
        NETWORK
    }
    /**
     * Enumerates the network sync options.
     *
     * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
     * @since 12
     */
    enum NetWorkStrategy {
        /**
         * Sync over Wi-Fi.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 12
         */
        WIFI = 1,
        /**
         * Sync over the cellular network.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 12
         */
        CELLULAR = 2
    }
    /**
     * Sets the cloud sync strategy of an application. This API uses a promise to return the result.
     *
     * @param { StrategyType } strategy - Type of the strategy to set.
     * @param { Array<commonType.ValueType> } param - Strategy parameters to set.
     *     Currently, only network strategies can be set. By default, Wi-Fi and cellular network are supported.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types;
     *     3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
     * @since 12
     */
    function setCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>;
    /**
     * Indicates automatic synchronization triggering method for Device-Cloud data.
     *
     * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
     * @stagemodelonly
     * @since 26.0.0
     */
    enum AutoSyncTriggerMode {
        /**
         * Indicates account login trigger method.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @stagemodelonly
         * @since 26.0.0
         */
        ACCOUNT_LOGIN = 0,
        /**
         * Indicates the synchronization switch trigger mode.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @stagemodelonly
         * @since 26.0.0
         */
        CLOUD_SWITCH_ON = 1,
        /**
         * Indicates the trigger mode for network reconnection after recovery.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @stagemodelonly
         * @since 26.0.0
         */
        NETWORK_RECOVER = 2,
        /**
         * Indicates the cloud-side data change trigger mode.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @stagemodelonly
         * @since 26.0.0
         */
        CLOUD_DATA_CHANGE = 3,
        /**
         * Indicates the user change trigger method.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @stagemodelonly
         * @since 26.0.0
         */
        USER_CHANGE = 4
    }
    /**
     * Describes information about the automatic synchronization trigger mode.
     *
     * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AutoSyncTriggerInfo {
        /**
         * Describes the automatic synchronization triggering mode.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @stagemodelonly
         * @since 26.0.0
         */
        mode: AutoSyncTriggerMode;
    }
    /**
     * Describes the triggering method for automatic device-cloud synchronization subscription.
     *
     * @param { Callback<AutoSyncTriggerInfo> } observer - Callback for automatic synchronization trigger interception.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
     * @stagemodelonly
     * @since 26.0.0
     */
    function onAutoSyncTrigger(observer: Callback<AutoSyncTriggerInfo>): void;
    /**
     * Describes unsubscribing from the device-cloud automatic synchronization trigger mode.
     *
     * @param { Callback<AutoSyncTriggerInfo> } [observer] - Callback for automatic synchronization trigger interception.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
     * @stagemodelonly
     * @since 26.0.0
     */
    function offAutoSyncTrigger(observer?: Callback<AutoSyncTriggerInfo>): void;
}
export default cloudData;

```
