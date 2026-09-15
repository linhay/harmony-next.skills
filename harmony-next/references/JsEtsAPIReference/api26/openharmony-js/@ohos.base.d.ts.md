# @ohos.base.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2025 Huawei Device Co., Ltd.
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
 * The **Base** module defines the public callback types of ArkTS APIs, including the common and error callbacks. These
 * callbacks provide a unified asynchronous processing mechanism for processing asynchronous operation results and error
 * messages. They can help developers simplify the asynchronous programming model and improve code readability and
 * maintainability.
 *
 * > **NOTE**
 * >
 * > - The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a
 * >   superscript to indicate their earliest API version.
 * > - Since API version 12, the APIs of this module are supported in ArkTS widgets.
 *
 * @file Public Callback Information
 * @kit BasicServicesKit
 */
/**
 * Defines a common callback used to return the processing result when an asynchronous operation is successful.
 * You need to define the callback type.
 *
 * @typedef { Callback } [since 6 - 11]
 * @typedef { Callback<T> } [since 12]
 * @syscap SystemCapability.Base
 * @crossplatform [since 10]
 * @form [since 12]
 * @atomicservice [since 11]
 * @since 6
 */
export interface Callback<T> {
    /**
     *
     * @param { T } data - Common callback information. The type is defined by the developer.
     *     The callback is used to return data of the corresponding type. No data is returned if the callback fails.
     * @syscap SystemCapability.Base
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 6
     */
    (data: T): void;
}
/**
 * Defines a common callback that carries an error parameter.
 * It is used to return error information when an asynchronous operation fails.
 * The specific error code is defined by each API.
 * For details, please refer to the error code description of the corresponding API.
 *
 * The information returned by the callback is an error parameter of the [BusinessError]{@link BusinessError} type.
 *
 * @typedef ErrorCallback [since 6 - 10]
 * @typedef ErrorCallback<T extends Error = BusinessError> [since 11]
 * @syscap SystemCapability.Base
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 6
 */
export interface ErrorCallback<T extends Error = BusinessError> {
    /**
     *
     * @param { T } err - Common error information returned when the API fails to be called.
     *     The default type is **BusinessError**, including the error code (**code**)
     *     and optional additional data (**data**).
     * @syscap SystemCapability.Base
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    (err: T): void;
}
/**
 * Defines a common callback that carries an error parameter and asynchronous return value. It is used to return error
 * information or success data when an asynchronous operation is complete.
 *
 * The error parameter is of the [BusinessError]{@link BusinessError} type.
 *
 * The type of the asynchronous return value is defined by the developer.
 *
 * @typedef AsyncCallback [since 6 - 11]
 * @typedef AsyncCallback<T, E = void> [since 12]
 * @syscap SystemCapability.Base
 * @crossplatform [since 10]
 * @form [since 12]
 * @atomicservice [since 11]
 * @since 6
 */
export interface AsyncCallback<T, E = void> {
    /**
     *
     * @param { BusinessError<E> } err - Common error information returned when the API fails to be called,
     *     including the error code and optional additional data.
     *     If the **E** parameter is not specified, the default value **void** is used.
     *     In this case, **BusinessError** contains only the error code.
     *     If the API call succeeds, this parameter returns **null**.
     * @param { T } data - Data returned asynchronously when the API is successfully called. The data type is defined by
     *     the developer. This parameter is unavailable when the API fails to be called.
     * @syscap SystemCapability.Base
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 6
     */
    (err: BusinessError<E>, data: T): void;
}
/**
 * Defines an error parameter. This API inherits from the **Error** class and is used to pass standard error
 * information, including the error code and optional additional information.
 *
 * @typedef BusinessError [since 6 - 11]
 * @typedef BusinessError<T = void> [since 12]
 * @syscap SystemCapability.Base
 * @crossplatform [since 10]
 * @form [since 12]
 * @atomicservice [since 11]
 * @since 6
 */
export interface BusinessError<T = void> extends Error {
    /**
     * Error code returned when the API fails to be called. The specific error code is defined by each API. For details,
     * see the error code description of the corresponding API.
     *
     * @syscap SystemCapability.Base
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 6
     */
    code: number;
    /**
     * Error message returned when the API fails to be called. If this parameter is left empty, the error object does not
     * contain additional data.
     *
     * @syscap SystemCapability.Base
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    data?: T;
}

```
