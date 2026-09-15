# @ohos.arkui.WithEnv.d.ts

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
 * @file Define the WithEnv component that allows setting environment properties for child components.
 * @kit ArkUI
 */
/**
 * Define the WithEnv attribute functions.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare class WithEnvAttribute {
    /**
     * Defining System Environment Variables
     *
     * @param { WritableSystemEnvKey<T> } key - Key for system environment variables.
     * @param { T } value - Value of system environment variables.
     * @returns { WithEnvAttribute } WithEnvAttribute object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    env<T>(key: WritableSystemEnvKey<T>, value: T): WithEnvAttribute;
    /**
     * Defining Custom Environment Variables
     *
     * @param { CustomEnvKey<T> } key - Key for custom environment variables.
     * @param { T } value - Value of custom environment variables.
     * @returns { WithEnvAttribute } WithEnvAttribute object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    customEnv<T>(key: CustomEnvKey<T>, value: T): WithEnvAttribute;
}
/**
 * Define the WithEnv component's type.
 *
 * @typedef { function }
 * @returns { WithEnvAttribute } WithEnvAttribute object
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare type WithEnvInterface = () => WithEnvAttribute;
/**
 * Define the WithEnv component that allows setting environment properties for child components.
 *
 * @type { WithEnvInterface }
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @uicomponent
 * @since 26.0.0
 */
export declare const WithEnv: WithEnvInterface;
/**
 * Define WithEnv Logic Component Instance.
 *
 * @type { WithEnvAttribute }
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @uicomponent
 * @since 26.0.0
 */
export declare const WithEnvInstance: WithEnvAttribute;

```
