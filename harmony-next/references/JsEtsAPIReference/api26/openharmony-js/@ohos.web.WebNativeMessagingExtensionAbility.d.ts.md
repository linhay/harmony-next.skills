# @ohos.web.WebNativeMessagingExtensionAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
 * @kit ArkWeb
 */
import ExtensionAbility from './@ohos.app.ability.ExtensionAbility';
import type WebNativeMessagingExtensionContext from './@ohos.web.WebNativeMessagingExtensionContext';
/**
 * Represents the information object of the web native messaging connection.
 *
 * @typedef ConnectionInfo
 * @syscap SystemCapability.Web.Webview.Core
 * @since 21
 */
export interface ConnectionInfo {
    /**
     * Connection ID.
     *
     * @type { number }
     * @syscap SystemCapability.Web.Webview.Core
     * @since 21
     */
    connectionId: number;
    /**
     * Application bundle name of the caller.
     *
     * @type { string }
     * @syscap SystemCapability.Web.Webview.Core
     * @since 21
     */
    bundleName: string;
    /**
     * Original URL of the caller extension.
     *
     * @type { string }
     * @syscap SystemCapability.Web.Webview.Core
     * @since 21
     */
    extensionOrigin: string;
    /**
     * Pipe file descriptor used to read data.
     *
     * @type { number }
     * @syscap SystemCapability.Web.Webview.Core
     * @since 21
     */
    fdRead: number;
    /**
     * Pipe file descriptor used to write data.
     *
     * @type { number }
     * @syscap SystemCapability.Web.Webview.Core
     * @since 21
     */
    fdWrite: number;
}
/**
 * class of web native messaging extension ability.
 *
 * @extends ExtensionAbility
 * @syscap SystemCapability.Web.Webview.Core
 * @stagemodelonly
 * @since 21
 */
export default class WebNativeMessagingExtensionAbility extends ExtensionAbility {
    /**
     * Indicates web native messaging extension ability context.
     *
     * @type { WebNativeMessagingExtensionContext }
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 21
     */
    context: WebNativeMessagingExtensionContext;
    /**
     * Called when a web native messaging connection is established.
     *
     * @param { ConnectionInfo } info - Indicates connection information about new native connection.
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 21
     */
    onConnectNative(info: ConnectionInfo): void;
    /**
     * Called when a web native messaging connection is disconnected.
     *
     * @param { ConnectionInfo } info - Indicates connection information about new native connection.
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 21
     */
    onDisconnectNative(info: ConnectionInfo): void;
    /**
     * Called when the WebNativeMessagingExtensionAbility is destroyed.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 21
     */
    onDestroy(): void;
}

```
