# @ohos.file.securityLabel.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2022-2025 Huawei Device Co., Ltd.
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
 * @kit CoreFileKit
 */
import type { AsyncCallback } from './@ohos.base';
/**
 * The **securityLabel** module provides APIs for managing data security levels of files, including obtaining and
 * setting file security levels.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 9
 */
declare namespace securityLabel {
    /**
     * Represents the data security level.
     *
     * @unionmember { 's0' } Level S0
     * @unionmember { 's1' } Level S1
     * @unionmember { 's2' } Level S2
     * @unionmember { 's3' } Level S3
     * @unionmember { 's4' } Level S4
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 9
     */
    type DataLevel = 's0' | 's1' | 's2' | 's3' | 's4';
    /**
     * Sets the data security level for a file or directory. The level can only be adjusted from low to high, or set to
     * the same level. This API uses a promise to return the result.
     *
     * @param { string } path - File path.
     * @param { DataLevel } type - Data security level. The value can only be **s0**, **s1**, **s2**, **s3**, or **s4**.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900007 - Arg list too long
     * @throws { BusinessError } 13900015 - File exists
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900037 - No data available
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 9
     */
    function setSecurityLabel(path: string, type: DataLevel): Promise<void>;
    /**
     * Sets the data security level for a file or directory. The level can only be adjusted from low to high, or set to
     * the same level. This API uses an asynchronous callback to return the result.
     *
     * @param { string } path - File path.
     * @param { DataLevel } type - Data security level. The value can only be **s0**, **s1**, **s2**, **s3**, or **s4**.
     * @param { AsyncCallback<void> } [callback] - Callback used to return the security level.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900007 - Arg list too long
     * @throws { BusinessError } 13900015 - File exists
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900037 - No data available
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 9
     */
    function setSecurityLabel(path: string, type: DataLevel, callback: AsyncCallback<void>): void;
    /**
     * Sets the data security level for a file or directory in synchronous mode. The level can only be adjusted from low
     * to high, or set to the same level.
     *
     * @param { string } path - File path.
     * @param { DataLevel } type - Data security level. The value can only be **s0**, **s1**, **s2**, **s3**, or **s4**.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900007 - Arg list too long
     * @throws { BusinessError } 13900015 - File exists
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900037 - No data available
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 9
     */
    function setSecurityLabelSync(path: string, type: DataLevel): void;
    /**
     * Obtains the data security level of a file or directory. If no data security level has been set, **s3** is returned
     * by default. This API uses a promise to return the result.
     *
     * @param { string } path - File path.
     * @returns { Promise<string> } Promise used to return the data security level.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900007 - Arg list too long
     * @throws { BusinessError } 13900015 - File exists
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900037 - No data available
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 9
     */
    function getSecurityLabel(path: string): Promise<string>;
    /**
     * Obtains the data security level of a file or directory. If no data security level has been set, **s3** is returned
     * by default. This API uses an asynchronous callback to return the result.
     *
     * @param { string } path - File path.
     * @param { AsyncCallback<string> } [callback] - Callback after the data security level is obtained asynchronously.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900007 - Arg list too long
     * @throws { BusinessError } 13900015 - File exists
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900037 - No data available
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 9
     */
    function getSecurityLabel(path: string, callback: AsyncCallback<string>): void;
    /**
     * Obtains the data security level of a file or directory in synchronous mode. If no data security level has been set,
     * **s3** is returned by default.
     *
     * @param { string } path - File path.
     * @returns { string } Promise used to return the data security level.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900007 - Arg list too long
     * @throws { BusinessError } 13900015 - File exists
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900037 - No data available
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 9
     */
    function getSecurityLabelSync(path: string): string;
}
export default securityLabel;

```
