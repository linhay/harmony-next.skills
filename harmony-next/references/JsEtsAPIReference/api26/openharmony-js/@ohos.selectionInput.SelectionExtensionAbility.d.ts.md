# @ohos.selectionInput.SelectionExtensionAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
 * @file SelectionExtensionAbility
 * @kit BasicServicesKit
 */
import type rpc from './@ohos.rpc';
import type Want from './@ohos.app.ability.Want';
import type SelectionExtensionContext from './@ohos.selectionInput.SelectionExtensionContext';
/**
 * This module provides APIs for word selection extension, which can implement extended interactions such as searching
 * and translating text using a mouse or touchpad. Word selection extension services can be customized by inheriting
 * SelectionExtensionAbility. You need to declare this ExtensionAbility in the project configuration. For details, see
 * [Developing a Word Selection Extension Ability](docroot://basic-services/selectionInput/selection-services-application-guide.md).
 * This module provides the following capabilities:
 *
 * - Lifecycle management: Use the [onConnect]{@link SelectionExtensionAbility#onConnect} and
 * [onDisconnect]{@link SelectionExtensionAbility#onDisconnect} callbacks to process the connection and disconnection
 * logic.
 * - **context**: You can use **context** to call
 * [startAbility]{@link @ohos.selectionInput.SelectionExtensionContext:SelectionExtensionContext#startAbility} to start
 * the target ability in the same app, or use **context** as an input parameter of
 * [createPanel]{@link @ohos.selectionInput.selectionManager:selectionManager.createPanel} to create a word selection
 * panel.
 *
 * > **NOTE**
 * >
 * > - This module is supported only on PCs/2-in-1 devices. You can use
 * > **canIUse('SystemCapability.SelectionInput.Selection')** to check whether the current device supports the
 * > capability.
 *
 * @syscap SystemCapability.SelectionInput.Selection
 * @stagemodelonly
 * @since 24
 */
declare class SelectionExtensionAbility {
    /**
     * Context of the **SelectionExtensionAbility**. This context is inherited from
     * [ExtensionContext]{@link ./application/ExtensionContext:ExtensionContext}. You can use **context** to call
     * [startAbility]{@link @ohos.selectionInput.SelectionExtensionContext:SelectionExtensionContext#startAbility} to
     * start the target ability in the same app, or use **context** as an input parameter of
     * [createPanel]{@link @ohos.selectionInput.selectionManager:selectionManager.createPanel} to create a word selection
     * panel.
     *
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    context: SelectionExtensionContext;
    /**
     * Defines a callback triggered when the client connects to the **SelectionExtensionAbility**. You can return an RPC
     * object in this callback to establish an IPC connection between the client and the server. You need to return a
     * communication stub object that inherits **rpc.RemoteObject**. The system passes the stub object to the client,
     * which then uses the stub object to communicate with the **SelectionExtensionAbility** through IPC.
     *
     * @param { Want } want - **Want** object passed by the system when the **SelectionExtensionAbility** is connected.
     *     The object contains the description information such as the ability name and bundle name. It is used to obtain
     *     the ability connection configuration in the **onConnect** callback so that the corresponding initialization
     *     logic can be executed.
     * @returns { rpc.RemoteObject } **RemoteObject** communication stub object. You need to implement the remote message
     *     processing method (for example, **onRemoteMessageRequest**) of this object. The system passes this object to
     *     the client for IPC.
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    onConnect(want: Want): rpc.RemoteObject;
    /**
     * Defines a callback triggered when the client disconnects from the **SelectionExtensionAbility** (for example, when
     * the user disables the word selection function or switches the word selection app). You can perform cleanup
     * operations for the **onConnect** callback in this callback. For example, you can
     * call [destroyPanel]{@link @ohos.selectionInput.selectionManager:selectionManager.destroyPanel} to destroy the created
     * panel, or call
     * [off('selectionCompleted')]{@link @ohos.selectionInput.selectionManager:selectionManager.off(type: 'selectionCompleted', callback?: Callback<SelectionInfo>)}
     * to unsubscribe from the word selection completion event.
     *
     * The callback is triggered only when the **SelectionExtensionAbility** is disconnected normally. It is not triggered
     * in cases of abnormal disconnection (for example, process termination due to low memory conditions).
     *
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    onDisconnect(): void;
}
export default SelectionExtensionAbility;

```
