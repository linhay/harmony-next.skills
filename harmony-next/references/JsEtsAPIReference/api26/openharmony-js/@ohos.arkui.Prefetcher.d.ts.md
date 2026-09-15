# @ohos.arkui.Prefetcher.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
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
 * @file Prefetching
 * @kit ArkUI
 */
/**
 * Extends the [IDataSource]{@link IDataSource} API to provide a data source that can be prefetched.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export interface IDataSourcePrefetching extends IDataSource {
    /**
     * Prefetches a specified data item from the dataset. This API can be either synchronous or asynchronous. When the
     * visible area changes, the prefetching algorithm calls this API if it determines that the data item about to enter
     * the visible area needs to be prefetched.
     *
     * @param { number } index - Index of the data item to be prefetched. The value range is [0, **totalCount()** - 1].
     * @returns { Promise<void> | void } Promise when this API is executed asynchronously; no return value when this API
     *     is executed synchronously. The promise only indicates that the operation is completed and contains no actual
     *     return content.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    prefetch(index: number): Promise<void> | void;
    /**
     * Cancels the prefetching of a specified data item from the dataset. This API can be either synchronous or
     * asynchronous. This API is optional. If the data source does not implement this API, the prefetching cancellation
     * operation will not be performed.
     *
     * @param { number } index - Index of the data item whose prefetching is to be canceled. The value range is
     *     [0, **totalCount()** - 1].
     * @returns { Promise<void> | void } Promise when this API is executed asynchronously; no return value when this API
     *     is executed synchronously. The promise only indicates that the operation is completed and contains no actual
     *     return content.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    cancel?(index: number): Promise<void> | void;
}
/**
 * Provides the prefetching capability. It works with **LazyForEach** to prefetch data items when users swipe through
 * container components such as **List** and **Grid**, improving user browsing experience.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export interface IPrefetcher {
    /**
     * Sets the prefetching-capable data source to bind to the **Prefetcher**.
     *
     * @param { IDataSourcePrefetching } dataSource - Prefetching-capable data source.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    setDataSource(dataSource: IDataSourcePrefetching): void;
    /**
     * Called when the boundary of the visible area changes. It notifies **Prefetcher** of the current visible area range
     * so that **Prefetcher** can determine whether to prefetch or cancel the prefetching of data items. Before calling
     * this API, you need to set a data source using **setDataSource**. This API works with the **List**, **Grid**,
     * **WaterFlow**, and **Swiper** components.
     *
     * @param { number } minVisible - Index of the first data item in the current visible area.
     * @param { number } maxVisible - Index of the last data item in the current visible area.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    visibleAreaChanged(minVisible: number, maxVisible: number): void;
}
/**
 * **BasicPrefetcher** is a fundamental implementation of **IPrefetcher**. It offers an intelligent data prefetching
 * algorithm that decides the data items to prefetch based on real-time changes in the visible area on the screen and
 * variations in the prefetch duration. It can also determine the prefetch requests to be canceled based on the user's
 * scrolling actions.
 *
 * **BasicPrefetcher** objects do not support JSON serialization.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export class BasicPrefetcher implements IPrefetcher {
    /**
     * Passes the data source that supports prefetching and binds it to **Prefetcher** when an object is created. If no
     * data source is passed during the creation, you can use **setDataSource** to set a data source after the creation.
     *
     * @param { IDataSourcePrefetching } dataSource - Prefetching-capable data source. If this parameter is not specified,
     *     the value is empty by default. You can set a data source using **setDataSource** later.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    constructor(dataSource?: IDataSourcePrefetching);
    /**
     * Sets the prefetching-capable data source to bind to the **Prefetcher**.
     *
     * @param { IDataSourcePrefetching } dataSource - Prefetching-capable data source.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    setDataSource(dataSource: IDataSourcePrefetching): void;
    /**
     * Called when the boundary of the visible area changes. It notifies **Prefetcher** of the current visible area range
     * so that **Prefetcher** can determine whether to prefetch or cancel the prefetching of data items. Before calling
     * this API, ensure that the data source has been set using the constructor or the **setDataSource** API. This API
     * works with the **List**, **Grid**, **WaterFlow**, and **Swiper** components.
     *
     * @param { number } minVisible - Index of the first data item in the current visible area.
     * @param { number } maxVisible - Index of the last data item in the current visible area.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    visibleAreaChanged(minVisible: number, maxVisible: number): void;
}

```
