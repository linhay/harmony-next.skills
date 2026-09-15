# @ohos.faultLogger.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
* Copyright (C) 2021-2026 Huawei Device Co., Ltd.
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
 * @file FaultLogger
 * @kit PerformanceAnalysisKit
 */
import type { AsyncCallback } from './@ohos.base';
/**
 * The **faultLogger** APIs can be used to query fault logs of an application cached on the system. The APIs use the
 * application bundle name and the UID allocated by the system as the unique key value.
 *
 * The number of application fault logs stored in the system is limited by the system log pressure. You are advised to
 * use [@ohos.hiviewdfx.hiAppEvent]{@link @ohos.hiviewdfx.hiAppEvent:hiAppEvent} to subscribe to fault events such as
 * **APP_CRASH** and **APP_FREEZE**.
 *
 * > **NOTE**
 * >
 * > The APIs of this module are no longer maintained since API version 18. You are advised to use
 * > [@ohos.hiviewdfx.hiAppEvent]{@link @ohos.hiviewdfx.hiAppEvent:hiAppEvent} to subscribe to the **APP_CRASH** and
 * > **APP_FREEZE** events in later versions.
 * >
 * > For details about how to use HiAppEvent to subscribe to the **APP_CRASH** event, see
 * > [Migrating Crash Events from the FaultLogger API](docroot://dfx/hiappevent-watcher-crash-events-arkts.md#migrating-crash-events-from-the-faultlogger-api)
 * > .
 * >
 * > For details about how to use HiAppEvent to subscribe to the **APP_FREEZE** event, see
 * > [Migrating Application Freeze Events from the Faultlogger API](docroot://dfx/hiappevent-watcher-freeze-events-arkts.md#migrating-application-freeze-events-from-the-faultlogger-api)
 * > .
 *
 * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
 * @since 8
 * @deprecated since 18
 * @useinstead ohos.hiviewdfx.hiAppEvent
 */
declare namespace FaultLogger {
    /**
     * Enumerates the fault types.
     *
     * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
     * @since 8
     * @deprecated since 18
     * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent.event
     */
    enum FaultType {
        /**
         * No specific fault type.
         *
         * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
         * @since 8
         * @deprecated since 18
         */
        NO_SPECIFIC = 0,
        /**
         * C++ program crash.
         *
         * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
         * @since 8
         * @deprecated since 18
         */
        CPP_CRASH = 2,
        /**
         * JS program crash.
         *
         * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
         * @since 8
         * @deprecated since 18
         */
        JS_CRASH = 3,
        /**
         * Application freezing.
         *
         * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
         * @since 8
         * @deprecated since 18
         */
        APP_FREEZE = 4
    }
    /**
     * Obtains the fault information about the current application. This API uses an asynchronous callback to return the
     * fault information array obtained, which contains a maximum of 10 pieces of fault information.
     *
     * @param { FaultType } faultType - Fault type.
     * @param { AsyncCallback<Array<FaultLogInfo>> } callback - Callback used to return the fault information array.<br>
     *     **value** is the fault information array obtained. If **value** is **undefined**, an exception occurs during
     *     the information retrieval. In this case, an error string will be returned.
     * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.faultlogger/FaultLogger#query
     */
    function querySelfFaultLog(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void;
    /**
     * Obtains the fault information about the current application. This API uses a promise to return the fault
     * information array obtained, which contains a maximum of 10 pieces of fault information.
     *
     * @param { FaultType } faultType - Fault type.
     * @returns { Promise<Array<FaultLogInfo>> } Promise used to return the fault information array. You can obtain the
     *     fault information instance in its **then()** method or use **await**.
     *     <br>**value** is the fault information array obtained. If **value** is **undefined**, an exception occurs
     *     during the information retrieval.
     * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.faultlogger/FaultLogger#query
     */
    function querySelfFaultLog(faultType: FaultType): Promise<Array<FaultLogInfo>>;
    /**
     * Obtains the fault information about the current application. This API uses an asynchronous callback to return the
     * fault information array obtained, which contains a maximum of 10 pieces of fault information.
     *
     * @param { FaultType } faultType - Fault type.
     * @param { AsyncCallback<Array<FaultLogInfo>> } callback - Callback used to return the fault information array.<br>
     *     **value** is the fault information array obtained. If **value** is **undefined**, an exception occurs during
     *     the information retrieval. In this case, an error string will be returned.
     * @throws { BusinessError } 401 - The parameter check failed, Parameter type error
     * @throws { BusinessError } 801 - The specified SystemCapability name was not found
     * @throws { BusinessError } 10600001 - The service is not started or is faulty
     * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
     * @since 9
     * @deprecated since 18
     * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent#addWatcher
     */
    function query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void;
    /**
     * Obtains the fault information about the current application. This API uses a promise to return the fault
     * information array obtained, which contains a maximum of 10 pieces of fault information.
     *
     * @param { FaultType } faultType - Fault type.
     * @returns { Promise<Array<FaultLogInfo>> } Promise used to return the fault information array. You can obtain the
     *     fault information instance in its **then()** method or use **await**.
     *     <br>**value** is the fault information array obtained. If **value** is **undefined**,
     *     an exception occurs during the information retrieval.
     * @throws { BusinessError } 401 - The parameter check failed, Parameter type error
     * @throws { BusinessError } 801 - The specified SystemCapability name was not found
     * @throws { BusinessError } 10600001 - The service is not started or is faulty
     * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
     * @since 9
     * @deprecated since 18
     * @useinstead ohos.hiviewdfx.hiAppEvent/hiAppEvent#addWatcher
     */
    function query(faultType: FaultType): Promise<Array<FaultLogInfo>>;
    /**
     * Defines the data structure of the fault log information.
     *
     * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
     * @since 8
     * @deprecated since 18
     */
    interface FaultLogInfo {
        /**
         * Process ID of the faulty process.
         *
         * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
         * @since 8
         * @deprecated since 18
         */
        pid: number;
        /**
         * User ID of the faulty process.
         *
         * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
         * @since 8
         * @deprecated since 18
         */
        uid: number;
        /**
         * Fault type.
         *
         * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
         * @since 8
         * @deprecated since 18
         */
        type: FaultType;
        /**
         * Millisecond-level timestamp when the log was generated.
         *
         * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
         * @since 8
         * @deprecated since 18
         */
        timestamp: number;
        /**
         * Reason for the fault.
         *
         * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
         * @since 8
         * @deprecated since 18
         */
        reason: string;
        /**
         * Module on which the fault occurred.
         *
         * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
         * @since 8
         * @deprecated since 18
         */
        module: string;
        /**
         * Summary of the fault.
         *
         * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
         * @since 8
         * @deprecated since 18
         */
        summary: string;
        /**
         * Full log text.
         *
         * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
         * @since 8
         * @deprecated since 18
         */
        fullLog: string;
    }
}
export default FaultLogger;

```
