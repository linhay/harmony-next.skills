# @ohos.telephony.observer.d.ts

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
 * @file Telephony Status Observer
 * @kit TelephonyKit
 */
import type { Callback } from './@ohos.base';
import type radio from './@ohos.telephony.radio';
import type data from './@ohos.telephony.data';
import type call from './@ohos.telephony.call';
import type sim from './@ohos.telephony.sim';
/**
 * The **observer** module provides event subscription management functions. You can register or unregister an observer
 * that listens for the following events: network status change, signal status change, call status change, cellular data
 * connection status, uplink and downlink data flow status of cellular data services, and SIM status change.
 *
 * @syscap SystemCapability.Telephony.StateRegistry
 * @since 6
 */
declare namespace observer {
    /**
     * Defines the network status.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    type NetworkState = radio.NetworkState;
    /**
     * Defines the signal strength.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    type SignalInformation = radio.SignalInformation;
    /**
     * Describes the connection status of a cellular data link.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    type DataConnectState = data.DataConnectState;
    /**
     * Enumerates the radio access technologies.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    type RatType = radio.RadioTechnology;
    /**
     * Defines the cellular data flow type.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    type DataFlowType = data.DataFlowType;
    /**
     * Enumerates call states.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    type CallState = call.CallState;
    /**
     * Enumerates SIM card types.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    type CardType = sim.CardType;
    /**
     * SIM card state.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    type SimState = sim.SimState;
    /**
     * Enumerates call states.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 21
     */
    type TelCallState = call.TelCallState;
    /**
     * Enumerates carrier call states.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 23
     */
    type CCallState = call.CCallState;
    /**
     * Registers an observer for network status change events. This API uses an asynchronous callback to return the
     * execution result.
     *
     * **Required permission**: ohos.permission.GET_NETWORK_INFO
     *
     * @permission ohos.permission.GET_NETWORK_INFO
     * @param { 'networkStateChange' } type - Network status change event. This field has a fixed value of
     *     **networkStateChange**.
     * @param { Callback<NetworkState> } callback - Callback used to return the network status object. For details, see
     *     [NetworkState]{@link @ohos.telephony.radio:radio.NetworkState}.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    function on(type: 'networkStateChange', callback: Callback<NetworkState>): void;
    /**
     * Registers an observer for network status change events of the SIM card in the specified slot. This API uses an
     * asynchronous callback to return the execution result.
     *
     * **Required permission**: ohos.permission.GET_NETWORK_INFO
     *
     * @permission ohos.permission.GET_NETWORK_INFO
     * @param { 'networkStateChange' } type - Network status change event. This field has a fixed value of
     *     **networkStateChange**.
     * @param { ObserverOptions } options - Event subscription parameters.
     * @param { Callback<NetworkState> } callback - Callback used to return the network status object. For details, see
     *     [NetworkState]{@link @ohos.telephony.radio:radio.NetworkState}.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    function on(type: 'networkStateChange', options: ObserverOptions, callback: Callback<NetworkState>): void;
    /**
     * Unregisters the observer for network status change events. This API uses an asynchronous callback to return the
     * execution result.
     *
     * > **NOTE**
     * >
     * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
     * > you do not pass the callback, you will cancel listening for all events.
     *
     * @param { 'networkStateChange' } type - Network status change event. This field has a fixed value of
     *     **networkStateChange**.
     * @param { Callback<NetworkState> } callback - Callback used to return the network status object. which is the
     *     [NetworkState]{@link @ohos.telephony.radio:radio.NetworkState} object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    function off(type: 'networkStateChange', callback?: Callback<NetworkState>): void;
    /**
     * Registers an observer for signal status change events. This API uses an asynchronous callback to return the
     * execution result.
     *
     * @param { 'signalInfoChange' } type - Signal status change event. This field has a fixed value of
     *     **signalInfoChange**.
     * @param { Callback<Array<SignalInformation>> } callback - Callback used to return the signal strength object. For
     *     details, see [SignalInformation]{@link @ohos.telephony.radio:radio.SignalInformation}.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    function on(type: 'signalInfoChange', callback: Callback<Array<SignalInformation>>): void;
    /**
     * Registers an observer for signal status change events of the SIM card in the specified slot. This API uses an
     * asynchronous callback to return the execution result.
     *
     * @param { 'signalInfoChange' } type - Signal status change event. This field has a fixed value of
     *     **signalInfoChange**.
     * @param { ObserverOptions } options - Event subscription parameters.
     * @param { Callback<Array<SignalInformation>> } callback - Callback used to return the signal strength object. For
     *     details, see [SignalInformation]{@link @ohos.telephony.radio:radio.SignalInformation}.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    function on(type: 'signalInfoChange', options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void;
    /**
     * Unregisters the observer for signal status change events. This API uses an asynchronous callback to return the
     * execution result.
     *
     * > **NOTE**
     * >
     * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
     * > you do not pass the callback, you will cancel listening for all events.
     *
     * @param { 'signalInfoChange' } type - Signal status change event. This field has a fixed value of
     *     **signalInfoChange**.
     * @param { Callback<Array<SignalInformation>> } callback - Callback used to return the signal strength object. For
     *     details, see [SignalInformation]{@link @ohos.telephony.radio:radio.SignalInformation}.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    function off(type: 'signalInfoChange', callback?: Callback<Array<SignalInformation>>): void;
    /**
     * Registers an observer for connection status change events of the cellular data link. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { 'cellularDataConnectionStateChange' } type - Cellular data connection status event. This field has a fixed
     *     value of **cellularDataConnectionStateChange**.
     * @param { Callback<DataConnectionStateInfo> } callback - Callback function used to return the cellular data
     *     connection status information object. For details, see
     *     [DataConnectState]{@link @ohos.telephony.data:data.DataConnectState} of **data** and
     *     [RadioTechnology]{@link @ohos.telephony.radio:radio.RadioTechnology} of **radio**.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 7
     */
    function on(type: 'cellularDataConnectionStateChange', callback: Callback<DataConnectionStateInfo>): void;
    /**
     * Registers an observer for connection status change events of the cellular data link over the SIM card in the
     * specified slot. This API uses an asynchronous callback to return the result.
     *
     * @param { 'cellularDataConnectionStateChange' } type - Cellular data connection status event. This field has a fixed
     *     value of **cellularDataConnectionStateChange**.
     * @param { ObserverOptions } options - Event subscription parameters.
     * @param { Callback<DataConnectionStateInfo> } callback - Callback function used to return the cellular data
     *     connection status information object. For details, see
     *     [DataConnectState]{@link @ohos.telephony.data:data.DataConnectState} of **data** and
     *     [RadioTechnology]{@link @ohos.telephony.radio:radio.RadioTechnology} of **radio**.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 7
     */
    function on(type: 'cellularDataConnectionStateChange', options: ObserverOptions, callback: Callback<DataConnectionStateInfo>): void;
    /**
     * Unregisters the observer for connection status change events of the cellular data link. This API uses an
     * asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
     * > you do not pass the callback, you will cancel listening for all events.
     *
     * @param { 'cellularDataConnectionStateChange' } type - Cellular data connection status event. This field has a fixed
     *     value of **cellularDataConnectionStateChange**.
     * @param { Callback<DataConnectionStateInfo> } callback - Callback function used to return the cellular data
     *     connection status information object. For details, see
     *     [DataConnectState]{@link @ohos.telephony.data:data.DataConnectState} of **data** and
     *     [RadioTechnology]{@link @ohos.telephony.radio:radio.RadioTechnology} of **radio**.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 7
     */
    function off(type: 'cellularDataConnectionStateChange', callback?: Callback<DataConnectionStateInfo>): void;
    /**
     * Registers an observer for the uplink and downlink data flow status change events of the cellular data service. This
     * API uses an asynchronous callback to return the result.
     *
     * @param { 'cellularDataFlowChange' } type - Cellular data flow change event. This field has a fixed value of
     *     **cellularDataFlowChange**.
     * @param { Callback<DataFlowType> } callback - Callback function used to return the data flow status object. For
     *     details, see [DataFlowType]{@link @ohos.telephony.data:data.DataFlowType} in **data**.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 7
     */
    function on(type: 'cellularDataFlowChange', callback: Callback<DataFlowType>): void;
    /**
     * Registers an observer for the uplink and downlink data flow status change events of the cellular data service on
     * the SIM card in the specified slot. This API uses an asynchronous callback to return the result.
     *
     * @param { 'cellularDataFlowChange' } type - Cellular data flow change event. This field has a fixed value of
     *     **cellularDataFlowChange**.
     * @param { ObserverOptions } options - Event subscription parameters.
     * @param { Callback<DataFlowType> } callback - Callback function used to return the data flow status object. For
     *     details, see [DataFlowType]{@link @ohos.telephony.data:data.DataFlowType} in **data**.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 7
     */
    function on(type: 'cellularDataFlowChange', options: ObserverOptions, callback: Callback<DataFlowType>): void;
    /**
     * Unregisters the observer for the uplink and downlink data flow status change events of the cellular data service.
     * This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
     * > you do not pass the callback, you will cancel listening for all events.
     *
     * @param { 'cellularDataFlowChange' } type - Cellular data flow change event. This field has a fixed value of
     *     **cellularDataFlowChange**.
     * @param { Callback<DataFlowType> } callback - Callback function used to return the data flow status object. For
     *     details, see [DataFlowType]{@link @ohos.telephony.data:data.DataFlowType} in **data**.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 7
     */
    function off(type: 'cellularDataFlowChange', callback?: Callback<DataFlowType>): void;
    /**
     * Registers an observer for call status change events. This API uses an asynchronous callback to return the execution
     * result.
     *
     * @param { 'callStateChange' } type - Call status change event. This field has a fixed value of **callStateChange**.
     * @param { Callback<CallStateInfo> } callback - Callback function used to return the result,
     *     <br>which is the **CallStateInfo** object. In this object:
     *     <br>- Only **state** is accessible to third-party applications. - **number** is only accessible to system
     *     applications.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    function on(type: 'callStateChange', callback: Callback<CallStateInfo>): void;
    /**
     * Registers an observer for call status change events. This API uses an asynchronous callback to return the execution
     * result.
     *
     * @param { 'callStateChange' } type - Call status change event. This field has a fixed value of **callStateChange**.
     * @param { ObserverOptions } options - Event subscription parameters.
     * @param { Callback<CallStateInfo> } callback - Callback function used to return the call status information object.
     *     <br>The application can obtain the **CallStateInfo** object. In this object:
     *     <br>- Only **state** is accessible to third-party applications. - **number** is only accessible to system
     *     applications.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    function on(type: 'callStateChange', options: ObserverOptions, callback: Callback<CallStateInfo>): void;
    /**
     * Unregisters the observer for call status change events. This API uses an asynchronous callback to return the
     * execution result.
     *
     * > **NOTE**
     * >
     * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
     * > you do not pass the callback, you will cancel listening for all events.
     *
     * @param { 'callStateChange' } type - Call status change event. This field has a fixed value of **callStateChange**.
     * @param { Callback<CallStateInfo> } callback - Callback function used to return the call status information object.
     *     For details, see [CallState]{@link @ohos.telephony.call:call.CallState}.
     *     <br>**number**: phone number.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 6
     */
    function off(type: 'callStateChange', callback?: Callback<CallStateInfo>): void;
    /**
     * Registers an observer for extended call status change events. This API uses an asynchronous callback to return the
     * execution result.
     *
     * @param { 'callStateChangeEx' } type - Extended call status change event. This field has a fixed value of
     *     **callStateChangeEx**.
     * @param { Callback<TelCallState> } callback - Callback function used to return the call status information object.
     *     <br>The application can obtain **TelCallState**.
     *     <br>
     * @param { ObserverOptions } [options] - Event subscription parameters.
     * @throws { BusinessError } 8800001 - Invalid parameter value.
     * @throws { BusinessError } 8800002 - Service connection failed.
     * @throws { BusinessError } 8800003 - System internal error.
     * @throws { BusinessError } 8800999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 21
     */
    function on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void;
    /**
     * Unregisters the observer for extended call status change events. This API uses an asynchronous callback to return
     * the execution result.
     *
     * > **NOTE**
     * >
     * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
     * > you do not pass the callback, you will cancel listening for all events.
     *
     * @param { 'callStateChangeEx' } type - Call status change event. This field has a fixed value of
     *     **callStateChange**.
     * @param { Callback<TelCallState> } [callback] - Callback function used to return the call status information object.
     *     For details, see [TelCallState]{@link @ohos.telephony.call:call.TelCallState} in **call**.
     *     <br>
     * @throws { BusinessError } 8800001 - Invalid parameter value.
     * @throws { BusinessError } 8800002 - Service connection failed.
     * @throws { BusinessError } 8800003 - System internal error.
     * @throws { BusinessError } 8800999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 21
     */
    function off(type: 'callStateChangeEx', callback?: Callback<TelCallState>): void;
    /**
     * Subscribes to the carrier call state changes and obtains the call number. This method uses an asynchronous callback
     * to return the execution result.
     *
     * @permission ohos.permission.MANAGE_CALL_FOR_DEVICES
     * @param { Callback<CCallStateInfo> } callback - Callback function used to return the call status information object.
     *     <br>The application can obtain CCallState.
     *     <br>
     * @param { ObserverOptions } [options] - Event subscription parameters.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 8800001 - Invalid parameter value.
     * @throws { BusinessError } 8800002 - Service connection failed.
     * @throws { BusinessError } 8800003 - System internal error.
     * @throws { BusinessError } 8800999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @FaAndStageModel
     * @since 23
     */
    function onCCallStateChange(callback: Callback<CCallStateInfo>, options?: ObserverOptions): void;
    /**
     * Cancels the listening on the carrier call status and obtaining of the call number by a third-party application.
     * This method uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.MANAGE_CALL_FOR_DEVICES
     * @param { Callback<CCallStateInfo> } [callback] - Callback function used to return the call status information
     *     object.
     *     <br>The application can obtain CCallState.
     *     <br>
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 8800001 - Invalid parameter value.
     * @throws { BusinessError } 8800002 - Service connection failed.
     * @throws { BusinessError } 8800003 - System internal error.
     * @throws { BusinessError } 8800999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @FaAndStageModel
     * @since 23
     */
    function offCCallStateChange(callback?: Callback<CCallStateInfo>): void;
    /**
     * Registers an observer for SIM card status change events. This API uses an asynchronous callback to return the
     * result.
     *
     * > **NOTE**
     * >
     * > The return result of this API does not contain the activation status of the SIM card. For details, see
     * > [sim.isSimActive]{@link @ohos.telephony.sim:sim.isSimActive}.
     *
     * @param { 'simStateChange' } type - SIM status change event. This field has a fixed value of **simStateChange**.
     * @param { Callback<SimStateData> } callback - Callback function used to return the SIM status data object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 7
     */
    function on(type: 'simStateChange', callback: Callback<SimStateData>): void;
    /**
     * Registers an observer for status change events of the SIM card in the specified slot. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { 'simStateChange' } type - SIM status change event. This field has a fixed value of **simStateChange**.
     * @param { ObserverOptions } options - Event subscription parameters.
     * @param { Callback<SimStateData> } callback - Callback function used to return the SIM status data object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 7
     */
    function on(type: 'simStateChange', options: ObserverOptions, callback: Callback<SimStateData>): void;
    /**
     * This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.GET_NETWORK_INFO
     * @param { Callback<boolean> } callback - Callback used to return the result.
     *     The value **true** indicates 5A state, and **false** indicates not 5A state.
     * @param { ObserverOptions } [options] - Indicates the options for observer.
     * @throws { BusinessError } 201 - Permission denied.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @stagemodelonly
     * @since 26.0.0
     */
    function onCommunicationStateChange(callback: Callback<boolean>, options?: ObserverOptions): void;
    /**
     * Unsubscribes from the callback for listening to the 5A state.
     *
     * @permission ohos.permission.GET_NETWORK_INFO
     * @param { Callback<boolean> } callback - Callback used to return the result.
     *     The value **true** indicates 5A state, and **false** indicates not 5A state.
     * @param { ObserverOptions } [options] - Indicates the options for observer.
     * @throws { BusinessError } 201 - Permission denied.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @stagemodelonly
     * @since 26.0.0
     */
    function offCommunicationStateChange(callback: Callback<boolean>, options?: ObserverOptions): void;
    /**
     * Unregisters the observer for SIM card status change events. This API uses an asynchronous callback to return the
     * result.
     *
     * > **NOTE**
     * >
     * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
     * > you do not pass the callback, you will cancel listening for all events.
     *
     * @param { 'simStateChange' } type - SIM status change event. This field has a fixed value of **simStateChange**.
     * @param { Callback<SimStateData> } callback - Callback function used to return the SIM status data object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 7
     */
    function off(type: 'simStateChange', callback?: Callback<SimStateData>): void;
    /**
     * Registers an observer for account information change events of the SIM card. This API uses an asynchronous callback
     * to return the result.
     *
     * @param { 'iccAccountInfoChange' } type - Account information change event. This field has a fixed value of
     *     **iccAccountInfoChange**.
     * @param { Callback<void> } callback - Callback used to return the result. If the account is successfully changed,
     *     the value of **err** is **undefined**. Otherwise, the value is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 10
     */
    function on(type: 'iccAccountInfoChange', callback: Callback<void>): void;
    /**
     * Unregisters the observer for account information change events of the SIM card. This API uses an asynchronous
     * callback to return the result.
     *
     * > **NOTE**
     * >
     * > You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
     * > you do not pass the callback, you will cancel listening for all events.
     *
     * @param { 'iccAccountInfoChange' } type - Account information change event. This field has a fixed value of
     *     **iccAccountInfoChange**.
     * @param { Callback<void> } callback - Callback used to return the result. If the account is successfully changed,
     *     the value of **err** is **undefined**. Otherwise, the value is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 10
     */
    function off(type: 'iccAccountInfoChange', callback?: Callback<void>): void;
    /**
     * Enumerates SIM card types and states.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 7
     */
    export interface SimStateData {
        /**
         * SIM card type.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 7
         */
        type: CardType;
        /**
         * SIM card state.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 7
         */
        state: SimState;
        /**
         * SIM card lock type.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        reason: LockReason;
    }
    /**
     * Defines information about the call status.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 11
     */
    export interface CallStateInfo {
        /**
         * Call type.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 11
         */
        state: CallState;
        /**
         * Phone number.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 11
         */
        number: string;
    }
    /**
     * Defines information about the call status.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 23
     */
    export interface CCallStateInfo {
        /**
         * Call type.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 23
         */
        state: CCallState;
        /**
         * Phone number.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 23
         */
        teleNumber: string;
    }
    /**
     * Defines information about the data connection status.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 11
     */
    export interface DataConnectionStateInfo {
        /**
         * Data connection status.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 11
         */
        state: DataConnectState;
        /**
         * Network type.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 11
         */
        network: RatType;
    }
    /**
     * Defines event subscription parameters.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 11
     */
    export interface ObserverOptions {
        /**
         * Card slot ID.
         *
         * - **0**: card slot 1.
         * - **1**: card slot 2.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 11
         */
        slotId: number;
    }
    /**
     * Enumerates SIM card lock types.
     *
     * @syscap SystemCapability.Telephony.StateRegistry
     * @since 8
     */
    export enum LockReason {
        /**
         * No lock.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        SIM_NONE = 0,
        /**
         * PIN lock.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        SIM_PIN = 1,
        /**
         * PUK lock.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        SIM_PUK = 2,
        /**
         * Network PIN lock.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        SIM_PN_PIN = 3,
        /**
         * Network PUK lock.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        SIM_PN_PUK = 4,
        /**
         * Subnet PIN lock.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        SIM_PU_PIN = 5,
        /**
         * Subnet PUK lock.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        SIM_PU_PUK = 6,
        /**
         * Service provider PIN lock.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        SIM_PP_PIN = 7,
        /**
         * Service provider PUK lock.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        SIM_PP_PUK = 8,
        /**
         * Organization PIN lock.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        SIM_PC_PIN = 9,
        /**
         * Organization PUK lock.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        SIM_PC_PUK = 10,
        /**
         * SIM PIN lock.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        SIM_SIM_PIN = 11,
        /**
         * SIM PUK lock.
         *
         * @syscap SystemCapability.Telephony.StateRegistry
         * @since 8
         */
        SIM_SIM_PUK = 12
    }
    /**
     * Registers an observer for SIM card activation state changes. This API uses an asynchronous callback to return the
     * execution result.
     *
     * **Required permission**: ohos.permission.GET_TELEPHONY_STATE
     *
     * @permission ohos.permission.GET_TELEPHONY_STATE
     * @param { number } slotId - Card slot ID.
     *     <br>- **0**: card slot 1.
     *     <br>- **1**: card slot 2.
     * @param { Callback< boolean> } callback - Callback function used to return whether the SIM card is activated.
     *     <br>- **true**: activated.
     *     <br>- **false**: not activated.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @FaAndStageModel
     * @since 23
     */
    function onGetSimActiveState(slotId: number, callback: Callback<boolean>): void;
    /**
     * Unregisters an observer for SIM card activation state changes. This API uses an asynchronous callback to return the
     * execution result.
     *
     * **Required permission**: ohos.permission.GET_TELEPHONY_STATE
     *
     * @permission ohos.permission.GET_TELEPHONY_STATE
     * @param { Callback<boolean> } [callback] - Callback function used to return whether the SIM card is activated.
     *     <br>- **true**: activated.
     *     <br>- **false**: not activated.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Service connection failed.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error.
     * @syscap SystemCapability.Telephony.StateRegistry
     * @FaAndStageModel
     * @since 23
     */
    function offGetSimActiveState(callback?: Callback<boolean>): void;
}
export default observer;

```
