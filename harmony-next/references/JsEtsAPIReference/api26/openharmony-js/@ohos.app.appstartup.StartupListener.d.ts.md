# @ohos.app.appstartup.StartupListener.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
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
 * The module defines the task listener used in [App Startup](docroot://application-models/app-startup.md).
 *
 * @file
 * @kit AbilityKit
 */
import { BusinessError } from './@ohos.base';
/**
 * The module defines the task listener used in [App Startup](docroot://application-models/app-startup.md).
 *
 * @syscap SystemCapability.Ability.AppStartup
 * @stagemodelonly
 * @since 12
 */
declare class StartupListener {
    /**
     * Called when all startup tasks complete.
     *
     * @param { BusinessError<void> } error - Indicates the error during execution.
     * @syscap SystemCapability.Ability.AppStartup
     * @stagemodelonly
     * @since 12
     */
    onCompleted?(error: BusinessError<void>): void;
}
export default StartupListener;

```
