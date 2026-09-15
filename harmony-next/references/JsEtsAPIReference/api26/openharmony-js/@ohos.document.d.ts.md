# @ohos.document.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
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
 * @kit API10LessDeprecatedModules
 */
import { AsyncCallback } from './@ohos.base';
/**
 * document
 *
 * @syscap SystemCapability.FileManagement.UserFileService
 * @since 6
 * @deprecated since 9
 */
declare namespace document {
    export { choose };
    export { show };
}
/**
 * Chooses files of the specified types. This API uses a promise to return the result.
 *
 * @param { string[] } types - Types of the files to choose.
 * @returns { Promise<string> } Promise used to return the result. An error code is returned.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.UserFileService
 * @since 6
 * @deprecated since 9
 */
declare function choose(types?: string[]): Promise<string>;
/**
 * Chooses a file. This API uses an asynchronous callback to return the result.
 *
 * @param { AsyncCallback<string> } [callback] - Callback used to return the result. An error code is returned.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.UserFileService
 * @since 6
 * @deprecated since 9
 */
declare function choose(callback: AsyncCallback<string>): void;
/**
 * Chooses files of the specified types. This API uses an asynchronous callback to return the result.
 *
 * @param { string[] } types - Types of the files to choose.
 * @param { AsyncCallback<string> } [callback] - Callback used to return the result. An error code is returned.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.UserFileService
 * @since 6
 * @deprecated since 9
 */
declare function choose(types: string[], callback: AsyncCallback<string>): void;
/**
 * Opens a file. This API uses a promise to return the result.
 *
 * @param { string } uri - URI of the file to open.
 * @param { string } type - Type of the file to open.
 * @returns { Promise<void> } Promise used to return the result. An error code is returned.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.UserFileService
 * @since 6
 * @deprecated since 9
 */
declare function show(uri: string, type: string): Promise<void>;
/**
 * Opens a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string } uri - URI of the file to open.
 * @param { string } type - Type of the file to open.
 * @param { AsyncCallback<void> } [callback] - Callback used to return the result. An error code is returned.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.UserFileService
 * @since 6
 * @deprecated since 9
 */
declare function show(uri: string, type: string, callback: AsyncCallback<void>): void;
export default document;

```
