# @ohos.telephony.data.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2021-2024 Huawei Device Co., Ltd.
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
 * @file Cellular Data
 * @kit TelephonyKit
 */
import type { AsyncCallback } from './@ohos.base';
import Context from './application/Context';
/**
 * The **data** module provides basic mobile data management functions. With the APIs provided by this module, you can
 * obtain the default slot of the SIM card used for mobile data, obtain the cellular data flow type and connection
 * status, and check whether cellular data and roaming are enabled.
 *
 * @syscap SystemCapability.Telephony.CellularData
 * @since 7
 */
declare namespace data {
    /**
     * Obtains the default slot of the SIM card used for mobile data. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the result.
     *     <br>- **0**: card slot 1.
     *     <br>- **1**: card slot 2
     *     <br>- **2**: slot ID of the mobile data in the eSIM and SkyTone scenarios.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 7
     */
    function getDefaultCellularDataSlotId(callback: AsyncCallback<number>): void;
    /**
     * Obtains the default slot of the SIM card used for mobile data. This API uses a promise to return the result.
     *
     * @returns { Promise<number> } Promise used to return the result.
     *     <br>- **0**: card slot 1.
     *     <br>- **1**: card slot 2
     *     <br>- **2**: slot ID of the mobile data in the eSIM and SkyTone scenarios.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 7
     */
    function getDefaultCellularDataSlotId(): Promise<number>;
    /**
     * Obtains the default SIM card used for mobile data synchronously.
     *
     * @returns { number } Card slot ID.
     *     <br>- **0**: card slot 1.
     *     <br>- **1**: card slot 2
     *     <br>- **2**: slot ID of the mobile data in the eSIM and SkyTone scenarios.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 9
     */
    function getDefaultCellularDataSlotIdSync(): number;
    /**
     * Obtains the data flow type of the cellular network (corresponding to the uplink and downlink arrows next to the
     * signal bar). This API uses an asynchronous callback to return the result.
     *
     * **Required permission**: ohos.permission.GET_NETWORK_INFO
     *
     * @permission ohos.permission.GET_NETWORK_INFO [since 22]
     * @param { AsyncCallback<DataFlowType> } callback - Callback used to return the result.
     * @throws { BusinessError } 201 - Permission denied. [since 22]
     * @syscap SystemCapability.Telephony.CellularData
     * @since 7
     */
    function getCellularDataFlowType(callback: AsyncCallback<DataFlowType>): void;
    /**
     * Obtains the data flow type of the cellular network (corresponding to the uplink and downlink arrows next to the
     * signal bar). This API uses a promise to return the result.
     *
     * **Required permission**: ohos.permission.GET_NETWORK_INFO
     *
     * @permission ohos.permission.GET_NETWORK_INFO [since 22]
     * @returns { Promise<DataFlowType> } Promise used to return the data flow type of the cellular network (corresponding
     *     to the uplink and downlink arrows next to the signal bar).
     * @throws { BusinessError } 201 - Permission denied. [since 22]
     * @syscap SystemCapability.Telephony.CellularData
     * @since 7
     */
    function getCellularDataFlowType(): Promise<DataFlowType>;
    /**
     * Obtains the cellular data connection status. This API uses an asynchronous callback to return the result.
     *
     * **Required permission**: ohos.permission.GET_NETWORK_INFO
     *
     * @permission ohos.permission.GET_NETWORK_INFO [since 22]
     * @param { AsyncCallback<DataConnectState> } callback - Callback used to return the result.
     * @throws { BusinessError } 201 - Permission denied. [since 22]
     * @syscap SystemCapability.Telephony.CellularData
     * @since 7
     */
    function getCellularDataState(callback: AsyncCallback<DataConnectState>): void;
    /**
     * Obtains the cellular data connection status. This API uses a promise to return the result.
     *
     * **Required permission**: ohos.permission.GET_NETWORK_INFO
     *
     * @permission ohos.permission.GET_NETWORK_INFO [since 22]
     * @returns { Promise<DataConnectState> } Promise used to return the result.
     * @throws { BusinessError } 201 - Permission denied. [since 22]
     * @syscap SystemCapability.Telephony.CellularData
     * @since 7
     */
    function getCellularDataState(): Promise<DataConnectState>;
    /**
     * Checks whether the cellular data service is enabled. This API uses an asynchronous callback to return the result.
     *
     * **Required permission**: ohos.permission.GET_NETWORK_INFO
     *
     * @permission ohos.permission.GET_NETWORK_INFO
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result.
     *     <br>**true**: The cellular data service is enabled.
     *     <br>**false**: The cellular data service is disabled.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 7
     */
    function isCellularDataEnabled(callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether the cellular data service is enabled. This API uses a promise to return the result.
     *
     * **Required permission**: ohos.permission.GET_NETWORK_INFO
     *
     * @permission ohos.permission.GET_NETWORK_INFO
     * @returns { Promise<boolean> } Promise used to return the result.
     *     <br>**true**: The cellular data service is enabled.
     *     <br>**false**: The cellular data service is disabled.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 7
     */
    function isCellularDataEnabled(): Promise<boolean>;
    /**
     * Checks whether the cellular data service is enabled. This API returns the result synchronously.
     *
     * **Required permission**: ohos.permission.GET_NETWORK_INFO
     *
     * @permission ohos.permission.GET_NETWORK_INFO
     * @returns { boolean } Whether the cellular data service is enabled.
     *     <br>**true**: The cellular data service is enabled.
     *     <br>**false**: The cellular data service is disabled.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 12
     */
    function isCellularDataEnabledSync(): boolean;
    /**
     * Checks whether roaming is enabled for the cellular data service. This API uses an asynchronous callback to return
     * the result.
     *
     * **Required permission**: ohos.permission.GET_NETWORK_INFO
     *
     * @permission ohos.permission.GET_NETWORK_INFO
     * @param { number } slotId - Card slot ID.
     *     <br>- **0**: card slot 1.
     *     <br>- **1**: card slot 2
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result.
     *     <br>**true**: Roaming is enabled for the cellular data service.
     *     <br>**false**: Roaming is disabled for the cellular data service.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 7
     */
    function isCellularDataRoamingEnabled(slotId: number, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether roaming is enabled for the cellular data service. This API uses a promise to return the result.
     *
     * **Required permission**: ohos.permission.GET_NETWORK_INFO
     *
     * @permission ohos.permission.GET_NETWORK_INFO
     * @param { number } slotId - Card slot ID.
     *     <br>- **0**: card slot 1.
     *     <br>- **1**: card slot 2
     * @returns { Promise<boolean> } Promise used to return the result.
     *     <br>**true**: Roaming is enabled for the cellular data service.
     *     <br>**false**: Roaming is disabled for the cellular data service.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 7
     */
    function isCellularDataRoamingEnabled(slotId: number): Promise<boolean>;
    /**
     * Checks whether roaming is enabled for the cellular data service. This API returns the result synchronously.
     *
     * **Required permission**: ohos.permission.GET_NETWORK_INFO
     *
     * @permission ohos.permission.GET_NETWORK_INFO
     * @param { number } slotId - Card slot ID.
     *     <br>- **0**: card slot 1.
     *     <br>- **1**: card slot 2
     * @returns { boolean } Whether roaming is enabled for the cellular data service.
     *     <br>**true**: Roaming is enabled for the cellular data service.
     *     <br>**false**: Roaming is disabled for the cellular data service.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 12
     */
    function isCellularDataRoamingEnabledSync(slotId: number): boolean;
    /**
     * Obtains the default ID of the SIM card used for mobile data.
     *
     * @returns { number } Obtains the default ID of the SIM card used for mobile data.
     *     <br>The return value is bound to the SIM card and increases from 1.
     *     <br>- **0**: no SIM card.
     *     <br>- **9999**: ID of the SIM card used for mobile data in the eSIM scenario.
     *     <br>- **99999**: ID of the SIM card used for mobile data in the SkyTone scenario. The default value is
     *     **99999**.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 10
     */
    function getDefaultCellularDataSimId(): number;
    /**
     * Obtains the access point name (APN) of the default SIM card used for mobile data. This API returns the result
     * asynchronously.
     *
     * @permission ohos.permission.MANAGE_APN_SETTING
     * @returns { Promise<Array<ApnInfo>> } Promise used to return the result.
     * @throws { BusinessError } 201 - Permission denied.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 16
     */
    function queryAllApns(): Promise<Array<ApnInfo>>;
    /**
     * Obtains the access point name (APN) of the default SIM card used for mobile data. This API returns the result
     * asynchronously.
     *
     * **Required permission**: ohos.permission.GET_NETWORK_INFO
     *
     * @permission ohos.permission.GET_NETWORK_INFO
     * @returns { Promise<string> } Promise used to return the result. If mobile data is not activated, an empty string is
     *     returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 20
     */
    function getActiveApnName(): Promise<string>;
    /**
     * Obtains the APN ID corresponding to the specified **ApnInfo**. This API returns the result asynchronously.
     *
     * @permission ohos.permission.MANAGE_APN_SETTING
     * @param { ApnInfo } apnInfo - APN to query.
     * @returns { Promise<Array<number>> } Promise used to return the result.
     * @throws { BusinessError } 201 - Permission denied.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 16
     */
    function queryApnIds(apnInfo: ApnInfo): Promise<Array<number>>;
    /**
     * Sets the APN corresponding to the specified **apnId** as the preferred APN. This API returns the result
     * asynchronously.
     *
     * > **NOTE**
     * >
     * > If the input APN ID is invalid, the default preferred APN configured by the carrier is used.
     *
     * @permission ohos.permission.MANAGE_APN_SETTING
     * @param { number } apnId - APN ID, which can be obtained by calling [queryApnIds]{@link data.queryApnIds}.
     * @returns { Promise<boolean> } Promise used to return the result. If no SIM card is installed, the value **false**
     *     is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @syscap SystemCapability.Telephony.CellularData
     * @since 16
     */
    function setPreferredApn(apnId: number): Promise<boolean>;
    /**
     * Open the system APN selection menu, which is presented in a semi-modal form and can
     * be used to select a specific APN. This API uses a promise to return the result.
     * If there is no SIM card or the device does not support the APN menu, the menu cannot be displayed.
     *
     * @param { Context } context - Indicates Context instance.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Telephony.CellularData
     * @stagemodelonly
     * @since 26.0.0
     */
    function showSystemApnSettings(context: Context): Promise<void>;
    /**
     * Defines the APN information.
     *
     * @syscap SystemCapability.Telephony.CellularData
     * @since 16
     */
    interface ApnInfo {
        /**
         * APN name.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 16
         */
        apnName: string;
        /**
         * APN.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 16
         */
        apn: string;
        /**
         * Mobile country code (MCC) of the SIM card.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 16
         */
        mcc: string;
        /**
         * Mobile network code (MNC) of the SIM card.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 16
         */
        mnc: string;
        /**
         * User name.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 16
         */
        user?: string;
        /**
         * APN type.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 16
         */
        type?: string;
        /**
         * Proxy address.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 16
         */
        proxy?: string;
        /**
         * Multimedia messaging service (MMS) proxy.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 16
         */
        mmsproxy?: string;
    }
    /**
     * Defines the cellular data flow type.
     *
     * @syscap SystemCapability.Telephony.CellularData
     * @since 7
     */
    export enum DataFlowType {
        /**
         * No uplink or downlink data is available.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 7
         */
        DATA_FLOW_TYPE_NONE = 0,
        /**
         * Only the downlink data is available.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 7
         */
        DATA_FLOW_TYPE_DOWN = 1,
        /**
         * Only the uplink data is available.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 7
         */
        DATA_FLOW_TYPE_UP = 2,
        /**
         * Both the uplink data and downlink data are available.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 7
         */
        DATA_FLOW_TYPE_UP_DOWN = 3,
        /**
         * No uplink or downlink data is available because the lower-layer link is in the dormant state.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 7
         */
        DATA_FLOW_TYPE_DORMANT = 4
    }
    /**
     * Describes the connection status of a cellular data link.
     *
     * @syscap SystemCapability.Telephony.CellularData
     * @since 7
     */
    export enum DataConnectState {
        /**
         * The status of the cellular data link is unknown.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 7
         */
        DATA_STATE_UNKNOWN = -1,
        /**
         * The cellular data link is disconnected.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 7
         */
        DATA_STATE_DISCONNECTED = 0,
        /**
         * The cellular data link is being connected.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 7
         */
        DATA_STATE_CONNECTING = 1,
        /**
         * The cellular data link is connected.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 7
         */
        DATA_STATE_CONNECTED = 2,
        /**
         * The cellular data link is suspended.
         *
         * @syscap SystemCapability.Telephony.CellularData
         * @since 7
         */
        DATA_STATE_SUSPENDED = 3
    }
}
export default data;

```
