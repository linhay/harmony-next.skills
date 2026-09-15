# @ohos.net.sharing.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2022-2023 Huawei Device Co., Ltd.
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
 * @file Network Sharing
 * @kit NetworkKit
 */
import type connection from './@ohos.net.connection';
/**
 * This module allows you to share your device's network connectivity with other connected devices.
 *
 * @syscap SystemCapability.Communication.NetManager.NetSharing
 * @since 9
 */
declare namespace sharing {
    /**
     * Defines the handle of the data network. Before calling the **NetHandle** function, call the **getNetHandle**
     * function to obtain a **NetHandle** object.
     *
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 9
     */
    type NetHandle = connection.NetHandle;
}
export default sharing;

```
