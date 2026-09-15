# @ohos.hiAppEvent.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2026 Huawei Device Co., Ltd.
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
 * @file Application Event Logging
 * @kit API10LessDeprecatedModules
 */
import type { AsyncCallback } from './@ohos.base';
/**
 * ###### How to Use
 *
 * Before using application event logging, you need to understand the requirements for related parameters.
 *
 * **Event Name**
 *
 * An event name is a string that contains a maximum of 48 characters, including the dollar sign ($), digits (0 to 9),
 * letters (a to z)(A to Z), and underscore (_). It must start with a letter or dollar sign ($) and end with a digit or
 * letter.
 *
 * **Event Type**
 *
 * An event type is an enumerated value of [EventType]{@link hiAppEvent.EventType}.
 *
 * **Event Parameter**
 *
 * An event parameter is an object in key-value pair format, where the key is the parameter name and the value is the
 * parameter value. The requirements are as follows:
 *
 * - A parameter name is a string that contains a maximum of 32 characters, including the dollar sign ($), digits (0 to
 * 9), letters (a to z)(A to Z), and underscore (_). It must start with a letter or dollar sign ($) and end with a digit
 * or letter.
 * - A parameter value can be of the string, number, boolean, or array type.
 * - If the parameter value is a string, its maximum length is 8*1024 characters. If this limit is exceeded, excess
 * characters will be discarded.
 * - If the parameter value is a number, the value must be within the range of **Number.MIN_SAFE_INTEGER** to
 * **Number.MAX_SAFE_INTEGER**. Otherwise, uncertain values may be generated.
 * - If the parameter value is an array, the elements in the array must be of the same type, which can only be string,
 * number, or boolean. In addition, the number of elements must be less than 100. If this limit is exceeded, excess
 * elements will be discarded.
 * - The maximum number of parameters is 32. If this limit is exceeded, excess parameters will be discarded.
 *
 * **Event Callback**
 *
 * Event callback can be a callback or promise that carries the return value obtained by invoking the event logging API.
 * You can add the processing of the return value in the event callback as follows:
 *
 * - If the return value is **0**, the event verification is successful, and the event will be directly written to the
 * event file.
 * - If the return value is greater than **0**, invalid parameters are present in the event, and the event will be
 * written to the event file after the invalid parameters are ignored.
 * - If the return value is smaller than **0**, the event parameter verification fails, and the event will not be
 * written to the event file.
 */
/**
 * The **hiAppEvent** module provides the application event logging functions, such as writing application events to the
 * event file and managing the event logging configuration.
 *
 * > **NOTE**
 * >
 * > - The APIs provided by this module are deprecated since API version 9. You are advised to use
 * > [@ohos.hiviewdfx.hiAppEvent]{@link @ohos.hiviewdfx.hiAppEvent:hiAppEvent}.
 *
 * @syscap SystemCapability.HiviewDFX.HiAppEvent
 * @since 7
 * @deprecated since 9
 * @useinstead ohos.hiviewdfx.hiAppEvent
 */
declare namespace hiAppEvent {
    /**
     * Enumerates the event types.
     *
     * @syscap SystemCapability.HiviewDFX.HiAppEvent
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.EventType
     */
    enum EventType {
        /**
         * Fault event.
         *
         * @syscap SystemCapability.HiviewDFX.HiAppEvent
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.EventType#FAULT
         */
        FAULT = 1,
        /**
         * Statistic event.
         *
         * @syscap SystemCapability.HiviewDFX.HiAppEvent
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.EventType#STATISTIC
         */
        STATISTIC = 2,
        /**
         * Security event.
         *
         * @syscap SystemCapability.HiviewDFX.HiAppEvent
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.EventType#SECURITY
         */
        SECURITY = 3,
        /**
         * User behavior event.
         *
         * @syscap SystemCapability.HiviewDFX.HiAppEvent
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.EventType#BEHAVIOR
         */
        BEHAVIOR = 4
    }
    /**
     * Provides constants that define the names of all predefined events.
     *
     * | Name                     | Type  | Readable| Writable| Description                |
     * | ------------------------- | ------ | ---- | ---- | -------------------- |
     * | USER_LOGIN                | string | Yes  | No  | User login event.      |
     * | USER_LOGOUT               | string | Yes  | No  | User logout event.      |
     * | DISTRIBUTED_SERVICE_START | string | Yes  | No  | Distributed service startup event.|
     *
     * @syscap SystemCapability.HiviewDFX.HiAppEvent
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.Event
     */
    namespace Event {
        /**
         * User login event.
         *
         * @syscap SystemCapability.HiviewDFX.HiAppEvent
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.Event#USER_LOGIN
         */
        const USER_LOGIN: string;
        /**
         * User logout event.
         *
         * @syscap SystemCapability.HiviewDFX.HiAppEvent
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.Event#USER_LOGOUT
         */
        const USER_LOGOUT: string;
        /**
         * Distributed service event.
         *
         * @syscap SystemCapability.HiviewDFX.HiAppEvent
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.Event#DISTRIBUTED_SERVICE_START
         */
        const DISTRIBUTED_SERVICE_START: string;
    }
    /**
     * Provides constants that define the names of all predefined event parameters.
     *
     * | Name                           | Type  | Readable| Writable| Description              |
     * | ------------------------------- | ------ | ---- | ---- | ------------------ |
     * | USER_ID                         | string | Yes  | No  | Custom user ID.    |
     * | DISTRIBUTED_SERVICE_NAME        | string | Yes  | No  | Distributed service name.  |
     * | DISTRIBUTED_SERVICE_INSTANCE_ID | string | Yes  | No  | Distributed service instance ID.|
     *
     * @syscap SystemCapability.HiviewDFX.HiAppEvent
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.Param
     */
    namespace Param {
        /**
         * User id.
         *
         * @syscap SystemCapability.HiviewDFX.HiAppEvent
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.Param#USER_ID
         */
        const USER_ID: string;
        /**
         * Distributed service name.
         *
         * @syscap SystemCapability.HiviewDFX.HiAppEvent
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.Param#DISTRIBUTED_SERVICE_NAME
         */
        const DISTRIBUTED_SERVICE_NAME: string;
        /**
         * Distributed service instance id.
         *
         * @syscap SystemCapability.HiviewDFX.HiAppEvent
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.Param#DISTRIBUTED_SERVICE_INSTANCE_ID
         */
        const DISTRIBUTED_SERVICE_INSTANCE_ID: string;
    }
    /**
     * Writes event information to the event file of the current day. This API uses a promise to return the result.
     *
     * @param { string } eventName Application event name.
     * @param { EventType } eventType Application event type.
     * @param { object } keyValues Application event key-value pair params.
     * @returns { Promise<void> } Promise used to asynchronously process the callback in the **then()** and **catch()**
     *     methods when event writing succeeded or failed.
     * @syscap SystemCapability.HiviewDFX.HiAppEvent
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent#write
     */
    function write(eventName: string, eventType: EventType, keyValues: object): Promise<void>;
    /**
     * Writes event information to the event file of the current day. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { string } eventName Application event name.
     * @param { EventType } eventType Application event type.
     * @param { object } keyValues Application event key-value pair params.
     * @param { AsyncCallback<void> } [callback] Callback function.
     * @syscap SystemCapability.HiviewDFX.HiAppEvent
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent#write
     */
    function write(eventName: string, eventType: EventType, keyValues: object, callback: AsyncCallback<void>): void;
    /**
     * Configures the application event logging function, such as setting the event logging switch and maximum size of the
     * directory that stores the event logging files.
     *
     * @param { ConfigOption } config - Configuration items for application event logging.
     * @returns { boolean } Returns **true** if the configuration is successful; returns **false** otherwise.
     * @syscap SystemCapability.HiviewDFX.HiAppEvent
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent#configure
     */
    function configure(config: ConfigOption): boolean;
    /**
     * Provides the configuration items for application event logging.
     *
     * @syscap SystemCapability.HiviewDFX.HiAppEvent
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.ConfigOption
     */
    interface ConfigOption {
        /**
         * Application event logging switch. The value **true** means to disable the application event logging function, and
         * the value **false** means the opposite.
         *
         * @syscap SystemCapability.HiviewDFX.HiAppEvent
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.ConfigOption#disable
         */
        disable?: boolean;
        /**
         * Maximum size of the event file storage directory. The default value is **10MB**. If the specified size is
         * exceeded, the oldest event logging files in the directory will be deleted to free up space.
         *
         * @syscap SystemCapability.HiviewDFX.HiAppEvent
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.ConfigOption#maxStorage
         */
        maxStorage?: string;
    }
}
export default hiAppEvent;

```
