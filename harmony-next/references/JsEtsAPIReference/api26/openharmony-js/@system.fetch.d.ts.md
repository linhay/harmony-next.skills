# @system.fetch.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2023 Huawei Device Co., Ltd.
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
 * @kit NetworkKit
 */
/**
 * **Table 2** Mapping between responseType and data in success callback
 *
 * | responseType | data | Description|
 * | -------- | -------- | -------- |
 * | N/A| string | When the type in the header returned by the server is **text/\***, **application/json**, **application/javascript**, or **application/xml**, the value is the text content.|
 * | text | string | Text content.|
 * | json | Object | A JSON object.|
 *
 * @syscap SystemCapability.Communication.NetStack
 * @since 3
 */
export interface FetchResponse {
    /**
     * Server status code.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @since 3
     */
    code: number;
    /**
     * The type of the returned data is determined by **responseType**. For details, see the mapping between
     * **responseType** and **data** in **success** callback.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @since 3
     */
    data: string | object;
    /**
     * All headers in the response from the server.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @since 3
     */
    headers: Object;
}
/**
 * **Table 1** Mapping between data and Content-Type
 *
 * | data | Content-Type | Description|
 * | -------- | -------- | -------- |
 * | string | Left unspecified| The default value of Content-Type is **text/plain**, and the value of data is used as the request body.|
 * | string | Any type| The value of data is used as the request body.|
 * | Object | Left unspecified| The default value of **Content-Type** is **application/x-www-form-urlencoded**. The **data** value is encoded based on the URL rule and appended in the request body.|
 * | Object | application/x-www-form-urlencoded | The value of data is encoded based on the URL rule and is used as the request body.|
 *
 * @syscap SystemCapability.Communication.NetStack
 * @since 3
 */
export default class Fetch {
    /**
     * Obtains data through the network.
     *
     * @param { object } options - Options.
     * @syscap SystemCapability.Communication.NetStack
     * @since 3
     */
    static fetch(options: {
        /**
         * Resource URL.
         * @syscap SystemCapability.Communication.NetStack
         * @since 3
         */
        url: string;
        /**
         * Request parameter, which can be of the string type or a JSON object.
         * @syscap SystemCapability.Communication.NetStack
         * @since 3
         */
        data?: string | object;
        /**
         * Request header, which accommodates all attributes of the request.
         * @syscap SystemCapability.Communication.NetStack
         * @since 3
         */
        header?: Object;
        /**
         * Request methods available: OPTIONS, GET, HEAD, POST, PUT, DELETE and TRACE. The default value is GET.
         * @syscap SystemCapability.Communication.NetStack
         * @since 3
         */
        method?: string;
        /**
         * The return type can be text, or JSON. By default, the return type is determined based on Content-Type in the header returned by the server.
         * @syscap SystemCapability.Communication.NetStack
         * @since 3
         */
        responseType?: string;
        /**
         * Called when the network data is obtained successfully.
         * @syscap SystemCapability.Communication.NetStack
         * @since 3
         */
        success?: (data: FetchResponse) => void;
        /**
         * Called when the network data fails to be obtained.
         * @syscap SystemCapability.Communication.NetStack
         * @since 3
         */
        fail?: (data: any, code: number) => void;
        /**
         * Called when the execution is completed.
         * @syscap SystemCapability.Communication.NetStack
         * @since 3
         */
        complete?: () => void;
    }): void;
}

```
