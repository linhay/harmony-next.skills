# @ohos.app.ability.DriverExtensionAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
 * @kit DriverDevelopmentKit
 */
import type rpc from './@ohos.rpc';
import type Want from './@ohos.app.ability.Want';
import _DriverExtensionContext from './application/DriverExtensionContext';
/**
 * Define a DriverExtensionContext for store context.
 *
 * @typedef { _DriverExtensionContext }
 * @syscap SystemCapability.Driver.ExternalDevice
 * @since 10
 */
export type DriverExtensionContext = _DriverExtensionContext;
/**
 * The **DriverExtensionAbility** module provides the ExtensionAbility related to drivers. It provides lifecycle
 * callbacks to be invoked when a driver is created, destroyed, connected, or disconnected.
 *
 * @syscap SystemCapability.Driver.ExternalDevice
 * @StageModelOnly
 * @since 10
 */
declare class DriverExtensionAbility {
    /**
     * Context of the **DriverExtension**. This context is inherited from **ExtensionContext**.
     *
     * @syscap SystemCapability.Driver.ExternalDevice
     * @StageModelOnly
     * @since 10
     */
    context: DriverExtensionContext;
    /**
     * Called when a DriverExtensionAbility is created to initialize the service logic.
     *
     * @param { Want } want - Want information related to this DriverExtensionAbility, including the ability name and bundle
     *     name.
     * @syscap SystemCapability.Driver.ExternalDevice
     * @StageModelOnly
     * @since 10
     */
    onInit(want: Want): void;
    /**
     * Called when this DriverExtensionAbility is destroyed to clear resources.
     *
     * @syscap SystemCapability.Driver.ExternalDevice
     * @StageModelOnly
     * @since 10
     */
    onRelease(): void;
    /**
     * Called following **onCreate()** when a DriverExtensionAbility is started by calling **connectAbility()**. A
     * **RemoteObject** object is returned for communication between the server and client.
     *
     * @param { Want } want - Want information related to this DriverExtensionAbility, including the ability name and
     *     bundle name.
     * @returns { rpc.RemoteObject | Promise<rpc.RemoteObject> } **RemoteObject** object used for communication between
     *     the server and client, or promise used to return the value.
     * @syscap SystemCapability.Driver.ExternalDevice
     * @StageModelOnly
     * @since 10
     */
    onConnect(want: Want): rpc.RemoteObject | Promise<rpc.RemoteObject>;
    /**
     * Called when a client is disconnected from this DriverExtensionAbility.
     *
     * @param { Want } want - Want information related to this DriverExtensionAbility, including the ability name and
     *     bundle name.
     * @returns { void | Promise<void> } Empty value, or promise used to return the value.
     * @syscap SystemCapability.Driver.ExternalDevice
     * @StageModelOnly
     * @since 10
     */
    onDisconnect(want: Want): void | Promise<void>;
    /**
     * Dumps client information. It is recommended that developers don't DUMP sensitive information.
     *
     * @param { Array<string> } params - Parameters in the form of a command.
     * @returns { Array<string> } String array used to dump client information.
     * @syscap SystemCapability.Driver.ExternalDevice
     * @StageModelOnly
     * @since 10
     */
    onDump(params: Array<string>): Array<string>;
}
/**
 * class of driver extension ability.
 * @syscap SystemCapability.Driver.ExternalDevice
 * @stagemodelonly
 * @since 10
 */
export default DriverExtensionAbility;

```
