# @ohos.telephony.sms.d.ts

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
 * @file SMS
 * @kit TelephonyKit
 */
import type { AsyncCallback } from './@ohos.base';
/**
 * The **sms** module provides basic SMS management functions. With the APIs provided by this module, you can create and
 * send SMS messages, and obtain the ID of the default SIM card used to send and receive SMS messages, and check whether
 * the current device can send and receive SMS messages.
 *
 * @syscap SystemCapability.Telephony.SmsMms
 * @since 6
 */
declare namespace sms {
    /**
     * Creates an SMS instance based on the protocol data unit (PDU) and specified SMS protocol. This API uses an
     * asynchronous callback to return the result.
     *
     * @param { Array<number> } pdu - Protocol data unit, which is obtained from the received SMS message.
     * @param { string } specification - SMS protocol type.
     *     <br>- **3gpp**: GSM/UMTS/LTE SMS
     *     <br>- **3gpp2**: CDMA SMS
     * @param { AsyncCallback<ShortMessage> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 6
     */
    function createMessage(pdu: Array<number>, specification: string, callback: AsyncCallback<ShortMessage>): void;
    /**
     * Creates an SMS instance based on the protocol data unit (PDU) and specified SMS protocol. This API uses a promise
     * to return the result.
     *
     * @param { Array<number> } pdu - Protocol data unit, which is obtained from the received SMS message.
     * @param { string } specification - SMS protocol type.
     *     <br>- **3gpp**: GSM/UMTS/LTE SMS
     *     <br>- **3gpp2**: CDMA SMS
     * @returns { Promise<ShortMessage> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 6
     */
    function createMessage(pdu: Array<number>, specification: string): Promise<ShortMessage>;
    /**
     * Sends an SMS message.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 6 and deprecated since API version 10. You are advised to use
     * > [sendShortMessage]{@link sms.sendShortMessage}.
     *
     * @permission ohos.permission.SEND_MESSAGES
     * @param { SendMessageOptions } options - Options (including the callback) for sending SMS messages. For details, see
     *     [SendMessageOptions]{@link sms.SendMessageOptions}.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 6
     * @deprecated since 10
     * @useinstead telephony.sms#sendShortMessage
     */
    function sendMessage(options: SendMessageOptions): void;
    /**
     * Sends an SMS message. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.SEND_MESSAGES
     * @param { SendMessageOptions } options - Options (including the callback) for sending SMS messages. For details, see
     *     [SendMessageOptions]{@link sms.SendMessageOptions}.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 10
     */
    function sendShortMessage(options: SendMessageOptions, callback: AsyncCallback<void>): void;
    /**
     * Sends an SMS message. This API uses a promise to return the result.
     *
     * @permission ohos.permission.SEND_MESSAGES
     * @param { SendMessageOptions } options - Options (including the callback) for sending SMS messages. For details, see
     *     [SendMessageOptions]{@link sms.SendMessageOptions}.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 10
     */
    function sendShortMessage(options: SendMessageOptions): Promise<void>;
    /**
     * Obtains the default slot ID of the SIM card used to send SMS messages. This API uses an asynchronous callback to
     * return the result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the result.
     *     <br>- **0**: card slot 1.
     *     <br>- **1**: card slot 2
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 7
     */
    function getDefaultSmsSlotId(callback: AsyncCallback<number>): void;
    /**
     * Obtains the default slot ID of the SIM card used to send SMS messages. This API uses a promise to return the
     * result.
     *
     * @returns { Promise<number> } Promise used to return the result.
     *     <br>- **0**: card slot 1.
     *     <br>- **1**: card slot 2
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 7
     */
    function getDefaultSmsSlotId(): Promise<number>;
    /**
     * Checks whether the current device can send and receive SMS messages. This API works in synchronous mode.
     *
     * @returns { boolean } - **true**: The device can send and receive SMS messages.
     *     <br>- **false**: The device cannot send or receive SMS messages.
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 7
     */
    function hasSmsCapability(): boolean;
    /**
     * Obtains the default ID of the SIM card used to send SMS messages. This API uses an asynchronous callback to return
     * the result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the result.
     *     <br>The return value is bound to the SIM card and increases from 1.
     *     <br>The return value is **-1** if no SIM card is detected.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300004 - Do not have sim card.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @throws { BusinessError } 8301001 - SIM card is not activated.
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 10
     */
    function getDefaultSmsSimId(callback: AsyncCallback<number>): void;
    /**
     * Obtains the default ID of the SIM card used to send SMS messages. This API uses a promise to return the result.
     *
     * @returns { Promise<number> } Promise used to return the result.
     *     <br>The return value is bound to the SIM card and increases from 1.
     *     <br>The return value is **-1** if no SIM card is detected.
     * @throws { BusinessError } 8300001 - Invalid parameter value.
     * @throws { BusinessError } 8300002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 8300003 - System internal error.
     * @throws { BusinessError } 8300004 - Do not have sim card.
     * @throws { BusinessError } 8300999 - Unknown error code.
     * @throws { BusinessError } 8301001 - SIM card is not activated.
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 10
     */
    function getDefaultSmsSimId(): Promise<number>;
    /**
     * Defines an SMS message instance.
     *
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 6
     */
    export interface ShortMessage {
        /**
         * SMS message body.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        visibleMessageBody: string;
        /**
         * Sender address.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        visibleRawAddress: string;
        /**
         * Enumerates SMS message types.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        messageClass: ShortMessageClass;
        /**
         * Protocol identifier used for delivering the SMS message.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        protocolId: number;
        /**
         * SMSC address.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        scAddress: string;
        /**
         * SMSC timestamp.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        scTimestamp: number;
        /**
         * Whether the received SMS message is a **replace short message**. The default value is **false**.
         *
         * - **true**: yes
         * - **false**: no
         *
         * For details, see [3GPP TS 23.040 9.2.3.9](https://www.3gpp.org/ftp/specs/archive/23_series/23.040).
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        isReplaceMessage: boolean;
        /**
         * Whether the received SMS contains **TP-Reply-Path**. The default value is **false**.
         *
         * - **true**: yes
         * - **false**: no
         *
         * **TP-Reply-Path**: The device returns a response based on the SMSC that sends the SMS message.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        hasReplyPath: boolean;
        /**
         * PDU in the SMS message.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        pdu: Array<number>;
        /**
         * SMS message status sent by the SMSC in the **SMS-STATUS-REPORT** message.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        status: number;
        /**
         * Whether the received SMS message is an SMS delivery report. The default value is **false**.
         *
         * - **true**: yes
         * - **false**: no
         *
         * SMS delivery report: a message sent from the SMSC to show the current status of the SMS message you delivered.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        isSmsStatusReportMessage: boolean;
    }
    /**
     * Enumerates SMS message types.
     *
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 6
     */
    export enum ShortMessageClass {
        /**
         * Unknown type.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        UNKNOWN,
        /**
         * Instant message, which is displayed immediately after being received.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        INSTANT_MESSAGE,
        /**
         * Message stored in the device or SIM card.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        OPTIONAL_MESSAGE,
        /**
         * Message containing SIM card information, which is to be stored in the SIM card.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        SIM_MESSAGE,
        /**
         * Message to be forwarded to another device.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        FORWARD_MESSAGE
    }
    /**
     * Provides the options (including callbacks) for sending SMS messages. For example, you can specify the SMS message
     * type by the optional parameter **content**.
     *
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 6
     */
    export interface SendMessageOptions {
        /**
         * Slot ID of the SIM card used for sending SMS messages.
         *
         * - **0**: card slot 1.
         * - **1**: card slot 2
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        slotId: number;
        /**
         * Destination address of the SMS message.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        destinationHost: string;
        /**
         * SMSC address. By default, the SMSC address in the SIM card is used.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        serviceCenter?: string;
        /**
         * SMS message type. If the content is composed of character strings, the SMS message is a text message. If the
         * content is composed of byte arrays, the SMS message is a data message.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        content: string | Array<number>;
        /**
         * Destination port of the SMS message. This field is mandatory only for a data message. Otherwise, it is optional.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        destinationPort?: number;
        /**
         * Callback used to return the SMS message sending result. For details, see
         * [ISendShortMessageCallback]{@link sms.ISendShortMessageCallback}. This parameter is mandatory for sending an SMS
         * message.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        sendCallback?: AsyncCallback<ISendShortMessageCallback>;
        /**
         * Callback used to return the SMS message delivery report. For details, see
         * [IDeliveryShortMessageCallback]{@link sms.IDeliveryShortMessageCallback}. This parameter is mandatory for sending
         * an SMS message.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        deliveryCallback?: AsyncCallback<IDeliveryShortMessageCallback>;
    }
    /**
     * Provides the callback for the SMS message sending result. It consists of three parts: SMS message sending result,
     * URI for storing the sent SMS message, and whether the SMS message is the last part of a long SMS message.
     *
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 6
     */
    export interface ISendShortMessageCallback {
        /**
         * SMS message sending result.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        result: SendSmsResult;
        /**
         * URI for storing the sent SMS message.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        url: string;
        /**
         * Whether this SMS message is the last part of a long SMS message. The default value is **false**.
         *
         * - **true**: yes
         * - **false**: no
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        isLastPart: boolean;
    }
    /**
     * Provides the callback for the SMS message delivery report.
     *
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 6
     */
    export interface IDeliveryShortMessageCallback {
        /**
         * SMS message delivery report.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        pdu: Array<number>;
    }
    /**
     * Enumerates SMS message sending results.
     *
     * @syscap SystemCapability.Telephony.SmsMms
     * @since 6
     */
    export enum SendSmsResult {
        /**
         * The SMS message is sent successfully.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        SEND_SMS_SUCCESS = 0,
        /**
         * Failed to send the SMS message due to an unknown reason.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        SEND_SMS_FAILURE_UNKNOWN = 1,
        /**
         * Failed to send the SMS message because the modem is shut down.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        SEND_SMS_FAILURE_RADIO_OFF = 2,
        /**
         * Failed to send the SMS message because the network is unavailable or SMS message sending or receiving is not
         * supported.
         *
         * @syscap SystemCapability.Telephony.SmsMms
         * @since 6
         */
        SEND_SMS_FAILURE_SERVICE_UNAVAILABLE = 3
    }
}
export default sms;

```
