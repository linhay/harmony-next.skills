# @ohos.bundleState.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2026  Huawei Device Co., Ltd.
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
 * @file Device Usage Statistics
 * @kit BackgroundTasksKit
 */
import { AsyncCallback } from './@ohos.base';
/**
 * This module provides APIs for collecting statistics on device usage.
 *
 * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
 * @since 7
 * @deprecated since 9
 */
declare namespace bundleState {
    /**
     *
     * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
     * @since 7
     * @deprecated since 9
     */
    interface BundleStateInfo {
        /**
         * The identifier of BundleStateInfo.
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        id: number;
        /**
         * The total duration, in milliseconds.
         * <br> Unit:ms
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        abilityInFgTotalTime?: number;
        /**
         * The last time when the application was accessed, in milliseconds.
         * <br> Unit:ms
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        abilityPrevAccessTime?: number;
        /**
         * The last time when the application was visible in the foreground, in milliseconds.
         * <br> Unit:ms
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        abilityPrevSeenTime?: number;
        /**
         * The total duration when the application was visible in the foreground, in milliseconds.
         * <br> Unit:ms
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        abilitySeenTotalTime?: number;
        /**
         * The bundle name of the application.
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        bundleName?: string;
        /**
         * The total duration when the foreground application was accessed, in milliseconds.
         * <br> Unit:ms
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        fgAbilityAccessTotalTime?: number;
        /**
         * The last time when the foreground application was accessed, in milliseconds.
         * <br> Unit:ms
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        fgAbilityPrevAccessTime?: number;
        /**
         * The time of the first bundle usage record in this {@code BundleActiveInfo} object,
         * in milliseconds.
         * <br> Unit:ms
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        infosBeginTime?: number;
        /**
         * The time of the last bundle usage record in this {@code BundleActiveInfo} object,
         * in milliseconds.
         * <br> Unit:ms
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        infosEndTime?: number;
        /**
         * Merges a specified {@link BundleActiveInfo} object with this {@link BundleActiveInfo} object.
         * The bundle name of both objects must be the same.
         *
         * @param { BundleStateInfo } toMerge Indicates the {@link BundleActiveInfo} object to merge.
         *     If the bundle names of the two {@link BundleActiveInfo} objects are different.
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        merge(toMerge: BundleStateInfo): void;
    }
    /**
     *
     * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
     * @since 7
     * @deprecated since 9
     */
    interface BundleActiveState {
        /**
         * The usage priority group of the application.
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        appUsagePriorityGroup?: number;
        /**
         * The bundle name.
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        bundleName?: string;
        /**
         * The shortcut ID.
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        indexOfLink?: string;
        /**
         * The class name.
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        nameOfClass?: string;
        /**
         * The time when this state occurred, in milliseconds.
         * <br> Unit:ms
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        stateOccurredTime?: number;
        /**
         * The state type.
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        stateType?: number;
    }
    /**
     * Checks whether the application specified by **bundleName** is in the idle state. A third-party application can only
     * check the idle state of itself. A system application can check the idle state of other applications only when it is
     * granted with the ohos.permission.BUNDLE_ACTIVE_INFO permission. This API uses an asynchronous callback to return
     * the result.
     *
     * @param { string } bundleName - Bundle name of an application.
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the specified **bundleName** is
     *     valid, the idle state of the application is returned; otherwise, **null** is returned.
     * @syscap SystemCapability.ResourceSchedule.UsageStatistics.AppGroup
     * @since 7
     * @deprecated since 9
     */
    function isIdleState(bundleName: string, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether the application specified by **bundleName** is in the idle state. A third-party application can only
     * check the idle state of itself. A system application can check the idle state of other applications only when it is
     * granted with the ohos.permission.BUNDLE_ACTIVE_INFO permission. This API uses a promise to return the result.
     *
     * @param { string } bundleName - Bundle name of an application.
     * @returns { Promise<boolean> } Promise used to return the result. If the specified **bundleName** is valid, the idle
     *     state of the application is returned; otherwise, **null** is returned.
     * @syscap SystemCapability.ResourceSchedule.UsageStatistics.AppGroup
     * @since 7
     * @deprecated since 9
     */
    function isIdleState(bundleName: string): Promise<boolean>;
    /**
     * Queries the usage priority group of the calling application.
     *
     * The priority defined in a priority group restricts the resource usage of an application,
     * for example, restricting the running of background tasks.
     *
     * @param { AsyncCallback<number> } callback - the callback of queryAppUsagePriorityGroup.
     *     Returns the app group of the calling application.
     * @syscap SystemCapability.ResourceSchedule.UsageStatistics.AppGroup
     * @since 7
     * @deprecated since 9
     */
    function queryAppUsagePriorityGroup(callback: AsyncCallback<number>): void;
    /**
     * Queries the usage priority group of the calling application.
     *
     * The priority defined in a priority group restricts the resource usage of an application,
     * for example, restricting the running of background tasks.
     *
     * @returns { Promise<number> } the promise returned by queryAppUsagePriorityGroup.
     *     Returns the app group of the calling application.
     * @syscap SystemCapability.ResourceSchedule.UsageStatistics.AppGroup
     * @since 7
     * @deprecated since 9
     */
    function queryAppUsagePriorityGroup(): Promise<number>;
    /**
     *
     * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
     * @since 7
     * @deprecated since 9
     */
    interface BundleActiveInfoResponse {
        /**
         * the struct of BundleActiveInfoResponse.
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        [key: string]: BundleStateInfo;
    }
    /**
     * Declares interval type.
     *
     * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
     * @since 7
     * @deprecated since 9
     */
    export enum IntervalType {
        /**
         * Indicates the interval type that will determine the optimal interval based on the start and end time.
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        BY_OPTIMIZED = 0,
        /**
         * Indicates the daily interval.
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        BY_DAILY = 1,
        /**
         * Indicates the weekly interval.
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        BY_WEEKLY = 2,
        /**
         * Indicates the monthly interval.
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        BY_MONTHLY = 3,
        /**
         * Indicates the annually interval.
         *
         * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
         * @since 7
         * @deprecated since 9
         */
        BY_ANNUALLY = 4
    }
    /**
     * Queries state data of the current bundle within a specified period.
     *
     * @param { number } begin Indicates the start time of the query period, in milliseconds.
     *     <br> Unit:ms
     * @param { number } end Indicates the end time of the query period, in milliseconds.
     *     <br> Unit:ms
     * @param { AsyncCallback<Array<BundleActiveState>> } callback - the state data of the current bundle.
     * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
     * @since 7
     * @deprecated since 9
     */
    function queryCurrentBundleActiveStates(begin: number, end: number, callback: AsyncCallback<Array<BundleActiveState>>): void;
    /**
     * Queries state data of the current bundle within a specified period.
     *
     * @param { number } begin Indicates the start time of the query period, in milliseconds.
     *     <br> Unit:ms
     * @param { number } end Indicates the end time of the query period, in milliseconds.
     *     <br> Unit:ms
     * @returns { Promise<Array<BundleActiveState>> } the state data of the current bundle.
     * @syscap SystemCapability.ResourceSchedule.UsageStatistics.App
     * @since 7
     * @deprecated since 9
     */
    function queryCurrentBundleActiveStates(begin: number, end: number): Promise<Array<BundleActiveState>>;
}
export default bundleState;

```
