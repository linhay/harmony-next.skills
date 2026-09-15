# @ohos.web.webNativeMessagingExtensionManager.d.ts

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
import type UIAbilityContext from './application/UIAbilityContext';
import type Want from './@ohos.app.ability.Want';
/**
 * The webNativeMessagingExtensionManager module provides the capability of managing message extensions based on web
 * standards.
 *
 * @namespace webNativeMessagingExtensionManager
 * @syscap SystemCapability.Web.Webview.Core
 * @stagemodelonly
 * @since 21
 */
declare namespace webNativeMessagingExtensionManager {
    /**
     * Represents the information about the web native message connection.
     * @typedef ConnectionNativeInfo
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 21
     */
    interface ConnectionNativeInfo {
        /**
         * Connection ID.
         * The value range is all integers.
         *
         * @type { number }
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 21
         */
        connectionId: number;
        /**
         * Bundle name of the web native message extension application.
         *
         * @type { string }
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 21
         */
        bundleName: string;
        /**
         * Source URL of the browser extension.
         *
         * @type { string }
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 21
         */
        extensionOrigin: string;
        /**
         * Process ID of the web native message extension.
         * The value range is all integers.
         *
         * @type { number }
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 21
         */
        extensionPid: number;
    }
    /**
     * Provides the native messaging error codes.
     *
     * @enum { number }
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 21
     */
    export enum NmErrorCode {
        /**
         * Permission denied due to missing ohos.permission.WEB_NATIVE_MESSAGING.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 21
         */
        PERMISSION_DENY = 17100203,
        /**
         * The want content is invalid.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 21
         */
        WANT_CONTENT_ERROR = 17100202,
        /**
         * Inner error for native messaging.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 21
         */
        INNER_ERROR = 17100201
    }
    /**
     * As an input parameter when connecting a web native messaging extension, it is used to receive
     * state changes during the connection.
     * @typedef WebExtensionConnectionCallback
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 21
     */
    interface WebExtensionConnectionCallback {
        /**
         * Called when a connection is set up.
         *
         * @param { ConnectionNativeInfo } connection - Connection information.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 21
         */
        onConnect(connection: ConnectionNativeInfo): void;
        /**
         * Called when a connection is interrupted.
         *
         * @param { ConnectionNativeInfo } connection - Connection information.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 21
         */
        onDisconnect(connection: ConnectionNativeInfo): void;
        /**
         * Called when the connection fails.
         *
         * @param { NmErrorCode } code - Error code.
         * @param { string } errMsg - Error message.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 21
         */
        onFailed(code: NmErrorCode, errMsg: string): void;
    }
    /**
     * Connects the current ability to the specified web native message extension ability.
     *
     * @permission ohos.permission.WEB_NATIVE_MESSAGING
     * @param { UIAbilityContext } context - Context of the web native message extension.
     * @param { Want } want - Want information about the target ability.
     * @param { WebExtensionConnectionCallback } callback - Callback object of the WebExtensionConnection status.
     * @returns { number } Connection ID.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 21
     */
    function connectNative(context: UIAbilityContext, want: Want, callback: WebExtensionConnectionCallback): number;
    /**
     * Disconnects the connection of a specified web native message extension.
     *
     * @permission ohos.permission.WEB_NATIVE_MESSAGING
     * @param { number } connectionId - Connection ID
     *     <br>The value range is all integers.
     * @returns { Promise<void> } The promise returned by the function.
     * @throws { BusinessError } 201 - Permission verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 16000011 - The context does not exist.
     * @throws { BusinessError } 16000050 - Internal error. Possible causes: 1. Failed to connect to the system service;
     *     2. The system service failed to communicate with dependency module.
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 21
     */
    function disconnectNative(connectionId: number): Promise<void>;
}
export default webNativeMessagingExtensionManager;

```
