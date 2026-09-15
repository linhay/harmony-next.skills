# @ohos.telephony.call.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2021-2023 Huawei Device Co., Ltd.
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
 * @file Call
 * @kit TelephonyKit
 */
import type { AsyncCallback } from './@ohos.base';
import type Context from './application/BaseContext';
/**
 * The **call** module provides call management functions, including making calls, redirecting to the dial screen,
 * obtaining the call status, and formatting phone numbers.
 *
 * To subscribe to call status changes, use
 * [`observer.on('callStateChange')`]{@link @ohos.telephony.observer:observer.on(type: 'callStateChange', callback: Callback<CallStateInfo>)}.
 *
 * @syscap SystemCapability.Telephony.CallManager
 * @atomicservice [since 11]
 * @since 6
 */
declare namespace call {
    /**
     * Initiates a call. You can set call options as needed. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 6 and deprecated since API version 9. The substitute API is available
     * > only for system applications.
     *
     * @permission ohos.permission.PLACE_CALL
     * @param { string } phoneNumber - Phone number.
     * @param { DialOptions } options - Call option, which indicates whether the call is a voice call or video call.
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** indicates that
     *     the operation is successful, and the value **false** indicates the opposite.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 6
     * @deprecated since 9
     * @useinstead telephony.call#dialCall
     */
    function dial(phoneNumber: string, options: DialOptions, callback: AsyncCallback<boolean>): void;
    /**
     * Initiates a call. You can set call options as needed. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 6 and deprecated since API version 9. The substitute API is available
     * > only for system applications.
     *
     * @permission ohos.permission.PLACE_CALL
     * @param { string } phoneNumber - Phone number.
     * @param { DialOptions } options - Call option, which indicates whether the call is a voice call or video call.
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the operation is
     *     successful, and the value **false** indicates the opposite.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 6
     * @deprecated since 9
     * @useinstead telephony.call#dialCall
     */
    function dial(phoneNumber: string, options?: DialOptions): Promise<boolean>;
    /**
     * Initiates a call. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 6 and deprecated since API version 9. The substitute API is available
     * > only for system applications.
     *
     * @permission ohos.permission.PLACE_CALL
     * @param { string } phoneNumber - Phone number.
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** indicates that
     *     the operation is successful, and the value **false** indicates the opposite.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 6
     * @deprecated since 9
     * @useinstead telephony.call#dialCall
     */
    function dial(phoneNumber: string, callback: AsyncCallback<boolean>): void;
    /**
     * Launches the call screen and displays the dialed number. This API uses an asynchronous callback to return the
     * result. This API can be called only in a UIAbility.
     *
     * @param { string } phoneNumber - Phone number.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice [since 11]
     * @since 7
     */
    function makeCall(phoneNumber: string, callback: AsyncCallback<void>): void;
    /**
     * Launches the call screen and displays the dialed number. This API uses a promise to return the result. This API can
     * be called only in a UIAbility.
     *
     * @param { string } phoneNumber - Phone number.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice [since 11]
     * @since 7
     */
    function makeCall(phoneNumber: string): Promise<void>;
    /**
     * Launches the call screen and displays the dialed number. This API uses a promise to return the result. This API can
     * be called only in a UIAbility.
     *
     * @param { string } phoneNumber - Phone number.
     * @param { MakeCallOptions } [options] - Call options.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Applications.Contacts
     * @FaAndStageModel
     * @atomicservice
     * @since 24
     */
    function makeCall(phoneNumber: string, options?: MakeCallOptions): Promise<void>;
    /**
     * Launches the call screen and displays the dialed number. This API uses a promise to return the result. You need to
     * declare the **ohos.permission.START_ABILITIES_FROM_BACKGROUND** permission if you want to call the API in the
     * background.
     *
     * @param { Context } context - Application context.
     * @param { string } phoneNumber - Phone number.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @syscap SystemCapability.Applications.Contacts
     * @atomicservice
     * @since 12
     */
    function makeCall(context: Context, phoneNumber: string): Promise<void>;
    /**
     * Go to the dial screen and the called number is displayed.The authentication challenge value is returned.
     *
     * @param { string } phoneNumber - Indicates the called number.
     * @param { MakeCallOptions } [options] - Indicates additional information carried in the call.
     * @returns { Promise<string> } Promise used to return access token by the makeCall.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Applications.Contacts
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function makeCallWithToken(phoneNumber: string, options?: MakeCallOptions): Promise<string>;
    /**
     * Checks whether a call is in progress. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** indicates that
     *     a call is in progress, and the value **false** indicates the opposite.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 6
     */
    function hasCall(callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether a call is in progress. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that a call is in
     *     progress, and the value **false** indicates the opposite.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 6
     */
    function hasCall(): Promise<boolean>;
    /**
     * Checks whether a call is in progress.
     *
     * @returns { boolean } Promise used to return the result. The value **true** indicates that a call is in progress,
     *     and the value **false** indicates the opposite.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 10
     */
    function hasCallSync(): boolean;
    /**
     * Obtains the call status. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<CallState> } callback - Callback used to return the result.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 6
     */
    function getCallState(callback: AsyncCallback<CallState>): void;
    /**
     * Obtains the call status. This API uses a promise to return the result.
     *
     * @returns { Promise<CallState> } Promise used to return the result.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 6
     */
    function getCallState(): Promise<CallState>;
    /**
     * Obtains the call status.
     *
     * @returns { CallState } Promise used to return the result.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 10
     */
    function getCallStateSync(): CallState;
    /**
     * Checks whether a device supports voice calls.
     *
     * @returns { boolean } Result indicating whether the device supports voice calls. The value **true** indicates yes,
     *     and the value **false** indicates no.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 7
     */
    function hasVoiceCapability(): boolean;
    /**
     * Checks whether the called number is an emergency number based on the phone number. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { string } phoneNumber - Phone number.
     * @param { EmergencyNumberOptions } options - Emergency number options.
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** indicates that
     *     the called number is an emergency number, and the value **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 7
     */
    function isEmergencyPhoneNumber(phoneNumber: string, options: EmergencyNumberOptions, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether the called number is an emergency number based on the phone number. This API uses a promise to
     * return the result.
     *
     * @param { string } phoneNumber - Phone number.
     * @param { EmergencyNumberOptions } options - Emergency number options.
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the called
     *     number is an emergency number, and the value **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 7
     */
    function isEmergencyPhoneNumber(phoneNumber: string, options?: EmergencyNumberOptions): Promise<boolean>;
    /**
     * Checks whether the called number is an emergency number. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { string } phoneNumber - Phone number.
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** indicates that
     *     the called number is an emergency number, and the value **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 7
     */
    function isEmergencyPhoneNumber(phoneNumber: string, callback: AsyncCallback<boolean>): void;
    /**
     * Formats a phone number based on specified formatting options. This API uses an asynchronous callback to return the
     * result.
     *
     * A formatted phone number is a standard numeric string, for example, 555 0100.
     *
     * @param { string } phoneNumber - Phone number.
     * @param { NumberFormatOptions } options - Number formatting options, for example, country code.
     * @param { AsyncCallback<string> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 7
     */
    function formatPhoneNumber(phoneNumber: string, options: NumberFormatOptions, callback: AsyncCallback<string>): void;
    /**
     * Formats a phone number based on specified formatting options. This API uses a promise to return the result.
     *
     * A formatted phone number is a standard numeric string, for example, 555 0100.
     *
     * @param { string } phoneNumber - Phone number.
     * @param { NumberFormatOptions } options - Number formatting options, for example, country code.
     * @returns { Promise<string> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 7
     */
    function formatPhoneNumber(phoneNumber: string, options?: NumberFormatOptions): Promise<string>;
    /**
     * Formats a phone number. This API uses an asynchronous callback to return the result.
     *
     * A formatted phone number is a standard numeric string, for example, 555 0100.
     *
     * @param { string } phoneNumber - Phone number.
     * @param { AsyncCallback<string> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 7
     */
    function formatPhoneNumber(phoneNumber: string, callback: AsyncCallback<string>): void;
    /**
     * Converts a phone number into the E.164 format. This API uses an asynchronous callback to return the result.
     *
     * The phone number must match the specified country code. For example, for a China phone number, the country code
     * must be **CN**. Otherwise, **null** will be returned.
     *
     * @param { string } phoneNumber - Phone number.
     * @param { string } countryCode - Country code, for example, **CN** (China). All country codes are supported.
     * @param { AsyncCallback<string> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 7
     */
    function formatPhoneNumberToE164(phoneNumber: string, countryCode: string, callback: AsyncCallback<string>): void;
    /**
     * Converts a phone number into the E.164 format. This API uses a promise to return the result.
     *
     * The phone number must match the specified country code. For example, for a China phone number, the country code
     * must be **CN**. Otherwise, **null** will be returned.
     *
     * All country codes are supported.
     *
     * @param { string } phoneNumber - Phone number.
     * @param { string } countryCode - Country code, for example, **CN** (China). All country codes are supported.
     * @returns { Promise<string> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 7
     */
    function formatPhoneNumberToE164(phoneNumber: string, countryCode: string): Promise<string>;
    /**
     * Answers a call. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.ANSWER_CALL or ohos.permission.MANAGE_CALL_FOR_DEVICES
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the call is answered successfully,
     *     the value of **err** is **undefined**. Otherwise, the value is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 23
     */
    function answerCall(callback: AsyncCallback<void>): void;
    /**
     * Ends a call. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.ANSWER_CALL or ohos.permission.SET_TELEPHONY_STATE or
     *     ohos.permission.MANAGE_CALL_FOR_DEVICES
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the call is hung up successfully,
     *     the value of **err** is **undefined**. Otherwise, the value is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 23
     */
    function hangUpCall(callback: AsyncCallback<void>): void;
    /**
     * Rejects a call. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.ANSWER_CALL or ohos.permission.MANAGE_CALL_FOR_DEVICES
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the call is rejected successfully,
     *     the value of **err** is **undefined**. Otherwise, the value is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.CallManager
     * @since 23
     */
    function rejectCall(callback: AsyncCallback<void>): void;
    /**
     * Obtains call transfer information with the phone number. This API uses a promise to return the result.
     *
     * @permission ohos.permission.GET_CALL_TRANSFER_INFO
     * @param { CallTransferType } type - Type of call forwarding to be obtained.
     * @param { string } number - Number used to obtain the call forwarding status.
     * @returns { Promise<CallTransferResult> } Promise used to return the call forwarding result.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8401002 - Invalid input call number.
     * @throws { BusinessError } 8401003 - Operation too frequent.
     * @syscap SystemCapability.Telephony.CallManager
     * @FaAndStageModel
     * @since 26.0.0
     */
    function getCallTransferInfo(type: CallTransferType, number: string): Promise<CallTransferResult>;
    /**
     * Enumerates call transfer types.
     *
     * @syscap SystemCapability.Telephony.CallManager
     * @since 26.0.0
     */
    export enum CallTransferType {
        /**
         * Call forwarding unconditional.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 26.0.0
         */
        TRANSFER_TYPE_UNCONDITIONAL = 0,
        /**
         * Call forwarding busy.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 26.0.0
         */
        TRANSFER_TYPE_BUSY = 1,
        /**
         * Call forwarding on no reply.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 26.0.0
         */
        TRANSFER_TYPE_NO_REPLY = 2,
        /**
         * Call forwarding on no user not reachable.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 26.0.0
         */
        TRANSFER_TYPE_NOT_REACHABLE = 3
    }
    /**
     * Enumerates call states.
     *
     * @syscap SystemCapability.Telephony.CallManager
     * @since 6
     */
    export enum CallState {
        /**
         * The call status fails to be obtained and is unknown.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 6
         */
        CALL_STATE_UNKNOWN = -1,
        /**
         * No call is in progress.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 6
         */
        CALL_STATE_IDLE = 0,
        /**
         * The call is in the ringing or waiting state.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 6
         */
        CALL_STATE_RINGING = 1,
        /**
         * At least one call is in dialing, active, or on hold, and no new incoming call is ringing or waiting.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 6
         */
        CALL_STATE_OFFHOOK = 2,
        /**
         * The incoming call is answered.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 11
         */
        CALL_STATE_ANSWERED = 3
    }
    /**
     * Enumerates call states.
     *
     * @syscap SystemCapability.Telephony.CallManager
     * @since 21
     */
    export enum TelCallState {
        /**
         * The call status fails to be obtained and is unknown.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 21
         */
        TEL_CALL_STATE_UNKNOWN = -1,
        /**
         * No call is in progress.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 21
         */
        TEL_CALL_STATE_IDLE = 0,
        /**
         * The call is in the ringing or waiting state.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 21
         */
        TEL_CALL_STATE_RINGING = 1,
        /**
         * At least one call is being dialed, and no new incoming call is in the ringing or waiting state.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 21
         */
        TEL_CALL_STATE_OFFHOOK = 2,
        /**
         * The incoming call is answered.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 21
         */
        TEL_CALL_STATE_ANSWERED = 3,
        /**
         * The call is being connected or placed on hold.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 21
         */
        TEL_CALL_STATE_CONNECTED = 4
    }
    /**
     * Carrier call state code.
     *
     * @syscap SystemCapability.Telephony.CallManager
     * @since 23
     */
    export enum CCallState {
        /**
         * The call status fails to be obtained and is unknown.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 23
         */
        CCALL_STATE_UNKNOWN = -1,
        /**
         * The call is connected.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 23
         */
        CCALL_STATE_ACTIVE = 0,
        /**
         * The call is on hold.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 23
         */
        CCALL_STATE_HOLDING = 1,
        /**
         * The outgoing call is in the dialing process, and the peer end has not received the ringing.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 23
         */
        CCALL_STATE_DIALING = 2,
        /**
         * The outgoing call is in the ringing process, and the peer end is ringing.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 23
         */
        CCALL_STATE_ALERTING = 3,
        /**
         * Indicates that an incoming call is received.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 23
         */
        CCALL_STATE_INCOMING = 4,
        /**
         * Indicates that another incoming call is received when there is an ongoing call in the same card slot.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 23
         */
        CCALL_STATE_WAITING = 5,
        /**
         * Indicates that the call has been released.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 23
         */
        CCALL_STATE_DISCONNECTED = 6,
        /**
         * Indicates that the call is being released.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 23
         */
        CCALL_STATE_DISCONNECTING = 7,
        /**
         * No call is in progress.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 23
         */
        CCALL_STATE_IDLE = 8,
        /**
         * The incoming call is answered.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 23
         */
        CCALL_STATE_ANSWERED = 9
    }
    /**
     * Provides an option for determining whether a call is a video call.
     *
     * @syscap SystemCapability.Telephony.CallManager
     * @since 6
     */
    export interface DialOptions {
        /**
         * Whether the call is a video call.
         *
         * - **true**: video call
         * - **false** (default): voice call
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 6
         */
        extras?: boolean;
    }
    /**
     * Provides an option for determining whether a call is a video call.
     *
     * @syscap SystemCapability.Applications.Contacts
     * @FaAndStageModel
     * @atomicservice
     * @since 24
     */
    export interface MakeCallOptions {
        /**
         * Whether to hide the dial screen. **true**: yes; **false**: no.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @FaAndStageModel
         * @atomicservice
         * @since 24
         */
        isHideDialScreen?: boolean;
        /**
         * Whether the third-party app supports custom accessibility features.
         * Default value: false.
         *
         * @syscap SystemCapability.Applications.Contacts
         * @FaAndStageModel
         * @atomicservice
         * @since 26.0.0
         */
        isCustomAccessibility?: boolean;
    }
    /**
     * Defines the call transfer result.
     *
     * @syscap SystemCapability.Telephony.CallManager
     * @since 26.0.0
     */
    export interface CallTransferResult {
        /**
         * Enumerates call transfer states.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 26.0.0
         */
        status: TransferStatus;
        /**
         * Hour in the start time.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 26.0.0
         */
        startHour: number;
        /**
         * Minute in the start time.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 26.0.0
         */
        startMinute: number;
        /**
         * Hour in the end time.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 26.0.0
         */
        endHour: number;
        /**
         * Minute in the end time.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 26.0.0
         */
        endMinute: number;
    }
    /**
     * Enumerates call transfer states.
     *
     * @syscap SystemCapability.Telephony.CallManager
     * @since 26.0.0
     */
    export enum TransferStatus {
        /**
         * Call transfer disabled.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 26.0.0
         */
        TRANSFER_DISABLE = 0,
        /**
         * Call transfer enabled.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 26.0.0
         */
        TRANSFER_ENABLE = 1
    }
    /**
     * Provides an option for determining whether a number is an emergency number for the SIM card in the specified slot.
     *
     * @syscap SystemCapability.Telephony.CallManager
     * @since 7
     */
    export interface EmergencyNumberOptions {
        /**
         * Card slot ID.
         *
         * - **0**: card slot 1
         * - **1**: card slot 2
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 7
         */
        slotId?: number;
    }
    /**
     * Provides an option for number formatting.
     *
     * @syscap SystemCapability.Telephony.CallManager
     * @since 7
     */
    export interface NumberFormatOptions {
        /**
         * Country code, for example, **CN** (China). All country codes are supported. The default value is **CN**.
         *
         * @syscap SystemCapability.Telephony.CallManager
         * @since 7
         */
        countryCode?: string;
    }
}
export default call;

```
