# @ohos.hiviewdfx.FaultLogExtensionContext.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
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
 * @file Delayed Fault Notification Context
 * @kit PerformanceAnalysisKit
 */
import ExtensionContext from './application/ExtensionContext';
/**
 * # How to Use
 *
 * You can obtain a **FaultLogExtensionContext** object through a **FaultLogExtensionAbility** child class instance.
 *
 * ```ts
 * import { FaultLogExtensionAbility } from '@kit.PerformanceAnalysisKit';
 * export default class MyFaultLogExtension extends FaultLogExtensionAbility {
 *     onFaultReportReady() {
 *         let context = this.context; // Obtain FaultLogExtensionContext.
 *         console.info('cache dir is ' + context.cacheDir); // Access the members in the context.
 *     }
 * }
 * ```
 */
/**
 * FaultLogExtensionContext is the context of
 * [FaultLogExtensionAbility]{@link @ohos.hiviewdfx.FaultLogExtensionAbility:FaultLogExtensionAbility} and inherits from
 * [ExtensionContext]{@link ./application/ExtensionContext:ExtensionContext}.
 *
 * This module provides APIs for accessing resources of a specific
 * [FaultLogExtensionAbility]{@link @ohos.hiviewdfx.FaultLogExtensionAbility:FaultLogExtensionAbility}. An
 * ExtensionAbility can use the context directly provided by ExtensionContext or that extended from ExtensionContext.
 *
 * > **NOTE**
 * >
 * > - The APIs of this module can be used only in the stage model.
 *
 * @extends ExtensionContext
 * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
 * @stagemodelonly
 * @since 21
 */
export default class FaultLogExtensionContext extends ExtensionContext {
}

```
