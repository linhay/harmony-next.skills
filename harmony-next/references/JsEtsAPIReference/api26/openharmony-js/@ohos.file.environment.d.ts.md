# @ohos.file.environment.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2021-2025 Huawei Device Co., Ltd.
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
/**
 * The **Environment** module provides ArkTS APIs for obtaining the root directories of the storage and user files.
 *
 * @syscap SystemCapability.FileManagement.File.Environment
 * @since 11
 */
declare namespace Environment {
    /**
     * Obtains the sandbox path of the pre-authorized **Download** directory.
     *
     * @permission ohos.permission.READ_WRITE_DOWNLOAD_DIRECTORY [since 11 - 11]
     * @returns { string } Sandbox path of the **Download** directory obtained.
     * @throws { BusinessError } 201 - Permission verification failed, usually the result returned by VerifyAccessToken.
     *     [since 11 - 11]
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 13900042 - Unknown error.
     * @syscap SystemCapability.FileManagement.File.Environment.FolderObtain
     * @since 11
     */
    function getUserDownloadDir(): string;
    /**
     * Obtains the sandbox path of the pre-authorized **Desktop** directory.
     *
     * @permission ohos.permission.READ_WRITE_DESKTOP_DIRECTORY [since 11 - 11]
     * @returns { string } Sandbox path of the **Desktop** directory obtained.
     * @throws { BusinessError } 201 - Permission verification failed, usually the result returned by VerifyAccessToken.
     *     [since 11 - 11]
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 13900042 - Unknown error.
     * @syscap SystemCapability.FileManagement.File.Environment.FolderObtain
     * @since 11
     */
    function getUserDesktopDir(): string;
    /**
     * Obtains the sandbox path of the pre-authorized **Document** directory.
     *
     * @permission ohos.permission.READ_WRITE_DOCUMENTS_DIRECTORY [since 11 - 11]
     * @returns { string } Sandbox path of the **Documents** directory obtained.
     * @throws { BusinessError } 201 - Permission verification failed, usually the result returned by VerifyAccessToken.
     *     [since 11 - 11]
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 13900042 - Unknown error.
     * @syscap SystemCapability.FileManagement.File.Environment.FolderObtain
     * @since 11
     */
    function getUserDocumentDir(): string;
}
export default Environment;

```
