# @ohos.file.fileAccess.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2023 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
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
 * The **fileAccess** module provides a framework for accessing and operating user files based on
 * [extension](docroot://application-models/extensionability-overview.md). This module interacts with a variety of file
 * management services, such as the storage management service, and provides a set of unified file access and management
 * APIs for system applications. The storage management service manages both the directories of the built-in storage and
 * resources on external devices, such as shared disks, USB flash drives, and SD cards.
 *
 * > **NOTE**
 * >
 * > - Currently, the APIs of this module can be called only by **FilePicker** and **FileManager**.
 *
 * @syscap SystemCapability.FileManagement.UserFileService
 * @since 9
 * @deprecated since 23
 * @useinstead @ohos.file.fs:fileIo
 */
declare namespace fileAccess {
}
export default fileAccess;

```
