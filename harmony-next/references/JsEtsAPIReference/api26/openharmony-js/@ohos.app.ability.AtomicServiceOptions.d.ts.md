# @ohos.app.ability.AtomicServiceOptions.d.ts

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
 * @file
 * @kit AbilityKit
 */
import CompletionHandlerForAtomicService from './@ohos.app.ability.CompletionHandlerForAtomicService';
import StartOptions from './@ohos.app.ability.StartOptions';
/**
 * **AtomicServiceOptions** is used as an input parameter of
 * [openAtomicService()]{@link ./application/UIAbilityContext:UIAbilityContext.openAtomicService} to carry arguments. It
 * inherits from [StartOptions]{@link @ohos.app.ability.StartOptions:StartOptions}.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 12
 */
export default class AtomicServiceOptions extends StartOptions {
    /**
     * Mode in which the system processes the startup. For example, **wantConstant.Flags.FLAG_INSTALL_ON_DEMAND**
     * indicates that the installation-free capability is used.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    flags?: number;
    /**
     * Additional parameters. For details, see the **parameters** field in [Want]{@link @ohos.app.ability.Want:Want}.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    parameters?: Record<string, Object>;
    /**
     * Operation class for receiving the result of opening an atomic service.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    completionHandlerForAtomicService?: CompletionHandlerForAtomicService;
}

```
