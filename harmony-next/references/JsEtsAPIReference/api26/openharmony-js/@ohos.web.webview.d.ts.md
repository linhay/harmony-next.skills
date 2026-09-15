# @ohos.web.webview.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2022 Huawei Device Co., Ltd.
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
import { AsyncCallback } from './@ohos.base';
import { Callback } from './@ohos.base';
import type cert from './@ohos.security.cert';
import type image from './@ohos.multimedia.image';
import type print from './@ohos.print';
import { WebNetErrorList } from './@ohos.web.netErrorList';
/**
 * This module provides the capability to manage web modules.
 *
 * @namespace webview
 * @syscap SystemCapability.Web.Webview.Core
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace webview {
    /**
     * Defines the Web's request/response header.
     *
     * @interface WebHeader [since 9 - 11]
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    interface WebHeader {
        /**
         * Gets the key of the request/response header.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        headerKey: string;
        /**
         * Gets the value of the request/response header.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        headerValue: string;
    }
    /**
     * Enumerates the cursor node types for the
     * [getLastHitTest]{@link @ohos.web.webview:webview.WebviewController#getLastHitTest} API.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice [since 11]
     * @since 9
     */
    enum WebHitTestType {
        /**
         * Editable area.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        EditText = 0,
        /**
         * Email address.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        Email = 1,
        /**
         * Hyperlink, where **src** is **http**.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        HttpAnchor = 2,
        /**
         * Image with a hyperlink, where **src** is http + HTML::img.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        HttpAnchorImg = 3,
        /**
         * HTML::img tag.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        Img = 4,
        /**
         * Geographical address.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        Map = 5,
        /**
         * Phone number.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        Phone = 6,
        /**
         * Unknown content.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        Unknown = 7
    }
    /**
     * Defines the mode for using HttpDns.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice [since 11]
     * @since 10
     */
    enum SecureDnsMode {
        /**
         * Do not use HttpDns, can be used to revoke previously used HttpDns configuration.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        OFF = 0,
        /**
         * By default, the user-settings of HttpDns is used for dns resolution, and if it fails,
         * the system dns is used for resolution.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        AUTO = 1,
        /**
         * Use the user-settings of HttpDns for dns resolution. If it fails, it will not
         * fall back to the system dns, which will directly cause the page to fail to load.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        SECURE_ONLY = 2
    }
    /**
     * For details about the ArkWeb kernel version, see
     * [Adaptation Guide for the M114 Kernel on OpenHarmony 6.0](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md)
     * .
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 20
     */
    enum ArkWebEngineVersion {
        /**
         * Default system kernel. For OpenHarmony 6.0, the default kernel is M132.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        SYSTEM_DEFAULT = 0,
        /**
         * Legacy kernel of OpenHarmony 6.0. You can select this legacy kernel. If it does not exist, the setting is
         * invalid.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        M114 = 1,
        /**
         * Evergreen kernel of OpenHarmony 6.0, which is M132 by default. If it does not exist, the setting is invalid.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        M132 = 2,
        /**
         * ArkWeb M144 version.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        M144 = 3,
        /**
         * Evergreen kernel, which is the latest kernel of the system. You can choose to use the latest kernel for each
         * system version. This setting takes effect for OpenHarmony 6.1 and later versions.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        ARKWEB_EVERGREEN = 99999
    }
    /**
     * Defines the security level for the page.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 11
     */
    enum SecurityLevel {
        /**
         * Unable to determine whether it is safe or not, the non-http/https protocol used.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        NONE = 0,
        /**
         * Indicates the HTTPS protocol used by the page and the authentication is successful.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        SECURE = 1,
        /**
         * The page is insecure. For example, the HTTP protocol is used or the HTTPS protocol
         * is used but use an legacy TLS version.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        WARNING = 2,
        /**
         * Attempted HTTPS and failed, the authentication is failed.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        DANGEROUS = 3
    }
    /**
     * Enumerates the playback states on the current web page.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    enum MediaPlaybackState {
        /**
         * No audio or video playback is started on the page.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        NONE = 0,
        /**
         * The audio and video on the page are being played.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        PLAYING = 1,
        /**
         * The audio and video on the page are paused.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        PAUSED = 2,
        /**
         * The audio and video on the page are stopped.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        STOPPED = 3
    }
    /**
     * Enumerates the memory pressure levels. When an application clears the cache occupied by the **Web** component, the
     * **Web** kernel releases the cache based on the memory pressure level.
     *
     * | Name| Value| Description|
     * | ------------------------------- | - | ---------- |
     * | MEMORY_PRESSURE_LEVEL_MODERATE | 1 | Moderate memory pressure level. At this level, the **Web** kernel attempts
     * to release the cache that has low reallocation overhead and does not need to be used immediately.|
     * | MEMORY_PRESSURE_LEVEL_CRITICAL | 2 | Critical memory pressure level. At this level, the **Web** kernel attempts
     * to release all possible memory caches.|
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 14
     */
    enum PressureLevel {
        /**
         * Modules are advised to free buffers that are cheap to re-allocate and not immediately needed.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        MEMORY_PRESSURE_LEVEL_MODERATE = 1,
        /**
         * At this level, modules are advised to free all possible memory.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        MEMORY_PRESSURE_LEVEL_CRITICAL = 2
    }
    /**
     * Provides the element information of the area being clicked. For the sample code, see
     * [getLastHitTest]{@link @ohos.web.webview:webview.WebviewController#getLastHitTest}.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice [since 11]
     * @since 9
     */
    interface HitTestValue {
        /**
         * Element type of the area being clicked.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        type: WebHitTestType;
        /**
         * Extra information of the area being clicked. If the area being clicked is an image or a link, the extra
         * information is the URL of the image or link.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        extra: string;
    }
    /**
     * Defines the configuration of web custom scheme, related to {@link customizeSchemes} method.
     *
     * @interface WebCustomScheme [since 9 - 11]
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice [since 11]
     * @since 9
     */
    interface WebCustomScheme {
        /**
         * Name of the custom scheme. The value can contain a maximum of 32 characters, including lowercase letters,
         * digits, periods (.), plus signs (+), and hyphens (-), and must start with a letter.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        schemeName: string;
        /**
         * Whether Cross-Origin Resource Sharing is supported.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        isSupportCORS: boolean;
        /**
         * Whether fetch request is supported.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        isSupportFetch: boolean;
        /**
         * If isStandard is true, the scheme will be handled as a standard scheme. The standard
         * schemes needs to comply with the URL normalization and parsing rules defined in Section 3.1 of RFC 1738,
         * which can be found in the http://www.ietf.org/rfc/rfc1738.txt.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        isStandard?: boolean;
        /**
         * If isLocal is true, the same security rules as those applied to the "file" URL will be
         * used to handle the scheme.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        isLocal?: boolean;
        /**
         * If isDisplayIsolated is true, then the scheme can only be displayed from other content
         * hosted using the same scheme.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        isDisplayIsolated?: boolean;
        /**
         * If isSecure is true, the same security rules as those applied to the "https" URL will be
         * used to handle the scheme.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        isSecure?: boolean;
        /**
         * If isCspBypassing is true, then this scheme can bypass Content Security Policy (CSP)
         * checks. In most cases, this value should not be true when isStandard is true.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        isCspBypassing?: boolean;
        /**
         * If isCodeCacheSupported is true, then the js of this scheme can generate code cache.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        isCodeCacheSupported?: boolean;
    }
    /**
     * Implements the output data stream class of **createPdf()**.
     *
     * > **NOTE**
     * >
     * > - The sample effect is subject to the actual device.
     * >
     * > - When a PDF file is generated on a web page, a data stream is returned, which is encapsulated by the **PdfData**
     * > class.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 14
     */
    class PdfData {
        /**
         * Obtains the data stream generated by a web page. For details about the sample code, see
         * [createPdf]{@link @ohos.web.webview:webview.WebviewController#createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>)}.
         *
         * @returns { Uint8Array } Data stream.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        pdfArrayBuffer(): Uint8Array;
    }
    /**
     * Specifies the input parameters of **createPdf()**.
     *
     * > **NOTE**
     * >
     * > The number of pixels is calculated as follows: Number of pixels = 96 x Number of inches.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 14
     */
    interface PdfConfiguration {
        /**
         * Page width,
         *
         * in inches.
         *
         * Recommended value: 8.27 inches of A4 paper width.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        width: number;
        /**
         * Page height,
         *
         * in inches.
         *
         * Recommended value: 11.69 inches of A4 paper height.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        height: number;
        /**
         * Top margin.
         *
         * The value range is [0.0, half of the page height). If the value is not within the value range, set it to **0.0**.
         *
         * Unit: inch.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        marginTop: number;
        /**
         * Bottom margin.
         *
         * The value range is [0.0, half of the page height). If the value is not within the value range, set it to **0.0**.
         *
         * Unit: inch.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        marginBottom: number;
        /**
         * Right margin.
         *
         * The value range is [0.0, half of the page width). If the value is not within the value range, set it to **0.0**.
         *
         * Unit: inch.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        marginRight: number;
        /**
         * Left margin.
         *
         * The value range is [0.0, half of the page width). If the value is not within the value range, set it to **0.0**.
         *
         * Unit: inch.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        marginLeft: number;
        /**
         * Scale multiple.
         *
         * The value range is [0.0, 2.0]. If the value is less than 0.0, set it to **0.0**. If the value is greater
         * than 2.0, set it to **2.0**.
         *
         * Default value: **1.0**
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        scale?: number;
        /**
         * Whether to print the background color. The value **true** means to print the background color, and **false**
         * means the opposite.
         *
         * Default value: **false**.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        shouldPrintBackground?: boolean;
    }
    /**
     * Provides usage information of the Web SQL Database.
     *
     * @interface WebStorageOrigin [since 9 - 11]
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 18]
     * @atomicservice [since 11]
     * @since 9
     */
    interface WebStorageOrigin {
        /**
         * Index of the origin.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        origin: string;
        /**
         * Storage usage of the origin.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        usage: number;
        /**
         * Storage quota of the origin.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        quota: number;
    }
    /**
     * Describes the information about the resource request sent by the **Web** component.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    interface RequestInfo {
        /**
         * URL of the request.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        url: string;
        /**
         * Method of the request.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        method: string;
        /**
         * Form data in the request body.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        formData: string;
    }
    /**
     * Represents the current scrolling offset of a web page.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 13
     */
    interface ScrollOffset {
        /**
         * Horizontal scrolling offset of a web page. The value is the difference between the x-coordinate of the left
         * boundary of the web page and that of the left boundary of the **Web** component.
         *
         * When the web page is scrolled rightwards, the value is negative.
         *
         * When the web page is not scrolled or scrolled leftwards, the value is **0** or positive.
         *
         * Unit: vp
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 13
         */
        x: number;
        /**
         * Vertical scrolling offset of a web page. The value is the difference between the y-coordinate of the upper
         * boundary of the web page and that of the upper boundary of the **Web** component.
         *
         * When the web page is scrolled downwards, the value is negative.
         *
         * When the web page is not scrolled or scrolled upwards, the value is **0** or positive.
         *
         * Unit: vp
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 13
         */
        y: number;
    }
    /**
     * Registers a one-time callback for web events of the specified type. Currently, only **webInited** is supported.
     * This callback is triggered when the Web engine initialization is complete.
     * When the first **Web** component is loaded in an application, the web engine is initialized. When other **Web**
     * components are loaded in the same application, **once()** is not triggered. When the first **Web** component is
     * loaded after the last **Web** component is destroyed in the application, the web engine will be initialized again.
     *
     * @param {string} type Web event type. The value can be **"webInited"**, indicating completion of web
     *     initialization.
     * @param {Callback<void>} callback Indicate callback used to receive the web event.
     *
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     * <br>2. Incorrect parameter types. 3.Parameter verification failed.
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice [since 11]
     * @since 9
     */
    function once(type: string, callback: Callback<void>): void;
    /**
     * Implements a **WebStorage** object to manage the Web SQL database and HTML5 Web Storage APIs. All **Web**
     * components in an application share a **WebStorage** object.
     *
     * > **NOTE**
     * >
     * > - The sample effect is subject to the actual device.
     * >
     * > - You must load the **Web** component before calling the APIs in **WebStorage**.
     * >
     * > - After the ArkWeb kernel is upgraded to M132, the Web SQL database management becomes invalid because the kernel
     * > discards Web SQL. For details about the ArkWeb kernel version, see
     * > [Constraints](docroot://web/web-component-overview.md#constraints).
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 18]
     * @atomicservice [since 11]
     * @since 9
     */
    class WebStorage {
        /**
         * Deletes all storage data used by JavaScript storage APIs, including the Web SQL Database and HTML5-supported Web
         * storage APIs.
         *
         * @param { boolean } incognito - Whether to delete all data in the Web SQL Database in incognito mode. The value
         *     **true** means to delete all data in the Web SQL Database in incognito mode, and **false** means the
         *     opposite.<br>Default value: **false**.<br>If **undefined** or **null** is passed, the value is
         *     **false**. [since 11]
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static deleteAllData(incognito?: boolean): void;
        /**
         * Deletes all data in the specified origin.
         *
         * @param { string } origin - Index of the origin, which is obtained through
         *     [getOrigins]{@link webview.WebStorage.static getOrigins(callback: AsyncCallback<Array<WebStorageOrigin>>)}.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 17100011 - Invalid origin.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static deleteOrigin(origin: string): void;
        /**
         * Obtains information about origins that are currently using the Web SQL Database and HTML5-supported Web Storage
         * APIs. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<WebStorageOrigin>> } Promise used to return the information about the origins.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100012 - Invalid web storage origin.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static getOrigins(): Promise<Array<WebStorageOrigin>>;
        /**
         * Obtains information about origins that are currently using the Web SQL Database and HTML5-supported Web Storage
         * APIs. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<Array<WebStorageOrigin>> } callback - Callback used to return the information about the
         *     origins.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100012 - Invalid web storage origin.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static getOrigins(callback: AsyncCallback<Array<WebStorageOrigin>>): void;
        /**
         * Obtains the storage quota of an origin in the Web SQL Database and HTML5-supported Web Storage APIs, in bytes.
         * This API uses a promise to return the result.
         *
         * @param { string } origin - Index of the origin.
         * @returns { Promise<number> } Promise used to return the storage quota of the origin.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100011 - Invalid origin.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static getOriginQuota(origin: string): Promise<number>;
        /**
         * Obtains the storage quota of an origin in Web SQL Database and HTML5-supported Web Storage APIs, in bytes. This
         * API uses an asynchronous callback to return the result.
         *
         * @param { string } origin - Index of the origin.
         * @param { AsyncCallback<number> } callback - Storage quota of the origin.<br>**number** is a long integer ranging
         *     from -2,147,483,648 to 2,147,483,647.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100011 - Invalid origin.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static getOriginQuota(origin: string, callback: AsyncCallback<number>): void;
        /**
         * Obtains the storage usage of an origin in the Web SQL Database and HTML5-supported Web Storage APIs, in bytes.
         * This API uses a promise to return the result.
         *
         * @param { string } origin - Index of the origin.
         * @returns { Promise<number> } Promise used to return the storage usage of the origin.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100011 - Invalid origin.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static getOriginUsage(origin: string): Promise<number>;
        /**
         * Obtains the storage usage of an origin in the Web SQL Database and HTML5-supported Web Storage APIs, in bytes.
         * This API uses an asynchronous callback to return the result.
         *
         * @param { string } origin - Index of the origin.
         * @param { AsyncCallback<number> } callback - Storage usage of the origin.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100011 - Invalid origin.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static getOriginUsage(origin: string, callback: AsyncCallback<number>): void;
    }
    /**
     * Implements a **WebDataBase** object.
     *
     * > **NOTE**
     * >
     * > - The sample effect is subject to the actual device.
     * >
     * > - You must load the **Web** component before calling the APIs in **WebDataBase**.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     */
    class WebDataBase {
        /**
         * Checks whether any saved HTTP authentication credentials exist. This API returns the result synchronously.
         *
         * @returns { boolean } Whether any saved HTTP authentication credentials exist.
         *     <br>**true** is returned if any saved HTTP authentication credentials exist; otherwise, **false** is returned.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        static existHttpAuthCredentials(): boolean;
        /**
         * Deletes all HTTP authentication credentials saved in the cache. This API returns the result synchronously.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        static deleteHttpAuthCredentials(): void;
        /**
         * Retrieves HTTP authentication credentials for a given host and realm. This API returns the result synchronously.
         *
         * @param { string } host - Host to which the HTTP authentication credential is applied.
         * @param { string } realm - Realm to which the HTTP authentication credential is applied.
         * @returns { Array<string> } Array of the matching user names and passwords is returned if the operation is
         *     successful; otherwise, an empty array is returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        static getHttpAuthCredentials(host: string, realm: string): Array<string>;
        /**
         * Saves HTTP authentication credentials for a given host and realm. This API returns the result synchronously.
         *
         * @param { string } host - Host to which the HTTP authentication credential is applied.
         * @param { string } realm - Realm to which the HTTP authentication credential is applied.
         * @param { string } username - User name.
         * @param { string } password - Password.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        static saveHttpAuthCredentials(host: string, realm: string, username: string, password: string): void;
    }
    /**
     * Implements a **GeolocationPermissions** object.
     *
     * > **NOTE**
     * >
     * > - The sample effect is subject to the actual device.
     * >
     * > - You must load the **Web** component before calling the APIs in **GeolocationPermissions**.
     * >
     * > - Required Permissions
     * > **ohos.permission.LOCATION**, **ohos.permission.APPROXIMATELY_LOCATION**, and
     * > **ohos.permission.LOCATION_IN_BACKGROUND**, which are required for accessing the location information. For details
     * > about the permissions, see
     * > [@ohos.geolocation (Geolocation)](docroot://reference/apis-location-kit/js-apis-geolocation.md).
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 18]
     * @atomicservice [since 11]
     * @since 9
     */
    class GeolocationPermissions {
        /**
         * Allows the specified origin to use the geolocation information.
         *
         * @param { string } origin - Index of the origin.
         * @param { boolean } incognito - Whether to allow the specified origin to use the geolocation information in
         *     incognito mode. The value **true** means to allow the specified origin to use the geolocation information in
         *     incognito mode, and **false** means the opposite.<br>Default value: **false**.<br>If **null** or
         *     **undefined** is passed in, the value is **false**. [since 11]
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100011 - Invalid origin. The origin format must follow defined in RFC 6454.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static allowGeolocation(origin: string, incognito?: boolean): void;
        /**
         * Clears the geolocation permission status of a specified origin.
         *
         * @param { string } origin - Index of the origin.
         * @param { boolean } incognito - Whether to clear the geolocation permission status of a specified origin in
         *     incognito mode. The value **true** means to clear the geolocation permission status of a specified origin in
         *     incognito mode, and **false** means the opposite.<br>Default value: **false**.<br>If **null** or
         *     **undefined** is passed in, the value is **false**. [since 11]
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100011 - Invalid origin. The origin format must follow defined in RFC 6454.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static deleteGeolocation(origin: string, incognito?: boolean): void;
        /**
         * Clears the geolocation permission status of all sources.
         *
         * @param { boolean } incognito - Whether to clear the geolocation permission status of all sources in incognito
         *     mode. The value **true** means to clear the geolocation permission status of all sources in incognito mode,
         *     and **false** means the opposite.<br>Default value: **false**.<br>If **null** or **undefined** is passed in,
         *     the value is **false**. [since 11]
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static deleteAllGeolocation(incognito?: boolean): void;
        /**
         * Obtains the geolocation permission status of the specified origin. This API uses a promise to return the result.
         *
         * @param { string } origin - Index of the origin.
         * @param { boolean } incognito - Whether to obtain the geolocation permission status of the specified origin in
         *     incognito mode. The value **true** means to obtain the geolocation permission status of the specified origin
         *     in incognito mode, and **false** means the opposite.<br>Default value: **false**.<br>If **null** or
         *     **undefined** is passed, error code **401** is thrown. [since 11]
         * @returns { Promise<boolean> } Promise used to return the geolocation permission status of the specified origin.
         *     <br>If the operation is successful, the value **true** means that the geolocation permission is granted, and
         *     **false** means the opposite.
         *     <br>If the operation fails, the geolocation permission status of the specified origin is not found.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100011 - Invalid origin. The origin format must follow defined in RFC 6454.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static getAccessibleGeolocation(origin: string, incognito?: boolean): Promise<boolean>;
        /**
          * Obtains the geolocation permission status of the specified origin. This API uses an asynchronous callback to
          * return the result.
          *
          * @param { string } origin - Index of the origin.
          * @param { AsyncCallback<boolean> } callback - Callback used to return the geolocation permission status of the
          *     specified origin.<br>If the operation is successful, the value **true** means that the geolocation permission
          *     is granted, and **false** means the opposite.<br>If the operation fails, the geolocation permission status of
          *     the specified origin is not found.
          * @param { boolean } incognito - Whether to obtain the geolocation permission status of the specified origin in
          *     incognito mode. The value **true** means to obtain the geolocation permission status of the specified origin
          *     in incognito mode, and **false** means the opposite.<br>Default value: **false**.<br>If **null** or
          *     **undefined** is passed, error code **401** is thrown. [since 11]
          * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
          *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
          * @throws { BusinessError } 17100011 - Invalid origin. The origin format must follow defined in RFC 6454.
          * @syscap SystemCapability.Web.Webview.Core
          * @crossplatform [since 18]
          * @atomicservice [since 11]
          * @since 9
          */
        static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void;
        /**
          * Obtains the geolocation permission status of all origins. This API uses a promise to return the result.
          *
          * @param { boolean } incognito - Whether to obtain the geolocation permission status of all origins in incognito
          *     mode. The value **true** means to obtain the geolocation permission status of all origins in incognito mode,
          *     and **false** means the opposite.<br>Default value: **false**.<br>If **null** or **undefined** is passed,
          *     error code **401** is thrown. [since 11]
          * @returns { Promise<Array<string>> } Promise used to return the geolocation permission status of all origins.
          * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
          *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
          * @syscap SystemCapability.Web.Webview.Core
          * @crossplatform [since 18]
          * @atomicservice [since 11]
          * @since 9
          */
        static getStoredGeolocation(incognito?: boolean): Promise<Array<string>>;
        /**
          * Obtains the geolocation permission status of all origins. This API uses an asynchronous callback to return the
          * result.
          *
          * @param { AsyncCallback<Array<string>> } callback - Callback used to return the geolocation permission status of
          *     all origins.
          * @param { boolean } incognito - Whether to obtain the geolocation permission status of all origins in incognito
          *     mode. The value **true** means to obtain the geolocation permission status of all origins in incognito mode,
          *     and **false** means the opposite.<br>Default value: **false**.<br>If **null** or **undefined** is passed,
          *     error code **401** is thrown. [since 11]
          * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
          *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
          * @syscap SystemCapability.Web.Webview.Core
          * @crossplatform [since 18]
          * @atomicservice [since 11]
          * @since 9
          */
        static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void;
    }
    /**
     * Provides methods for managing the web cookies.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     */
    class WebCookieManager {
        /**
         * Gets all cookies for the given URL.
         *
         * @param { string } url - The URL for which the cookies are requested.
         * @returns { string } - The cookie value for the given URL.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100002 - URL error. No valid cookie found for the specified URL.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.web.webview.WebCookieManager#fetchCookieSync
         */
        static getCookie(url: string): string;
        /**
         * Gets all cookies for the given URL.
         *
         * <p><strong>API Note</strong>:<br>
         *
         * **fetchCookieSync()** is used to obtain all cookie values. Cookie values are separated by semicolons. However,
         * a specific cookie value cannot be obtained separately.
         * </p>
         *
         * @param { string } url - The URL for which the cookies are requested.
         * @param { boolean } incognito - {@code true} gets all cookies for the given URL
         *     in incognito mode; {@code false} otherwise.
         * @returns { string } - The cookie value for the given URL.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100002 - URL error. No valid cookie found for the specified URL.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        static fetchCookieSync(url: string, incognito?: boolean): string;
        /**
         * Gets all cookies for the given URL Asynchronously.
         *
         * @param { string } url - The URL for which the cookies are requested.
         * @returns { Promise<string> } - A promise resolved after the cookies of given URL have been gotten.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100002 - URL error. No valid cookie found for the specified URL.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        static fetchCookie(url: string): Promise<string>;
        /**
         * Gets all cookies for the given URL Asynchronously.
         *
         * @param { string } url - The URL for which the cookies are requested.
         * @param { boolean } incognito - {@code true} gets all cookies for the given URL
         *     in incognito mode; {@code false} otherwise.
         * @returns { Promise<string> } - A promise resolved after the cookies of given URL have been gotten.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100002 - URL error. No valid cookie found for the specified URL.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 14
         */
        static fetchCookie(url: string, incognito: boolean): Promise<string>;
        /**
         * Gets all cookies for the given URL Asynchronously.
         *
         * @param { string } url - The URL for which the cookies are requested.
         * @param { AsyncCallback<string> } callback - Called after the cookies of given URL have been gotten.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100002 - URL error. No valid cookie found for the specified URL.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        static fetchCookie(url: string, callback: AsyncCallback<string>): void;
        /**
         * Set a single cookie (key-value pair) for the given URL.
         *
         * @param { string } url - The URL for which the cookie is to be set.
         * @param { string } value - The cookie as a string, using the format of the 'Set-Cookie' HTTP response header.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100002 - URL error. No valid cookie found for the specified URL.
         * @throws { BusinessError } 17100005 - The provided cookie value is invalid. It must follow the format specified
         *     <br>in RFC 6265.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.web.webview.WebCookieManager#configCookieSync
         */
        static setCookie(url: string, value: string): void;
        /**
         * Set a single cookie (key-value pair) for the given URL.
         *
         * > **NOTE**
         * >
         * > You can set **url** in **configCookieSync** to a domain name so that the cookie is attached to the requests on
         * > the page.
         * >
         * > Cookies are periodically saved to the disk every 30s. You can also use the
         * > **saveCookieAsync** API to forcibly save cookies to the disk.
         * >
         * > The **value** parameter must comply with the format of the Set-Cookie HTTP response header. The value is in the
         * > format of "key=value", followed by a list of cookie attributes separated by semicolons, for example,
         * > **"key=value;Max-Age=100"**.
         * >
         * > If a cookie with the same host, path, and name exists, it will be replaced by the new cookie. If the cookie has
         * > expired, it will not be stored. To set multiple cookies, call this method multiple times.
         * >
         * > If **configCookieSync()** is used to set cookies for two or more times, the cookies set each time are separated
         * > by semicolons.
         * >
         * > If the specified value contains the **Secure** attribute, the URL must use the **https://** protocol.
         * >
         * > To override HttpOnly cookies, the HttpOnly attribute must be specified in the value.
         *
         * @param { string } url - The URL for which the cookie is to be set.
         * @param { string } value - The cookie as a string, using the format of the 'Set-Cookie' HTTP response header.
         * @param { boolean } incognito - {@code true} set a single cookie (key-value pair) for the given URL
         *     in incognito mode; {@code false} otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100002 - URL error. No valid cookie found for the specified URL.
         * @throws { BusinessError } 17100005 - The provided cookie value is invalid. It must follow the format specified
         *     <br>in RFC 6265.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        static configCookieSync(url: string, value: string, incognito?: boolean): void;
        /**
         * Set a single cookie (key-value pair) for the given URL.
         *
         * > **NOTE**
         * >
         * > You can set **url** in **configCookieSync** to a domain name so that the cookie is attached to the requests on
         * > the page.
         * >
         * > It is recommended that cookie syncing be completed before the **Web** component is loaded.
         * >
         * > Cookies are periodically saved to the disk every 30s. You can also use the
         * > **saveCookieAsync** API to forcibly save cookies to the disk.
         * >
         * > The **value** parameter must comply with the format of the Set-Cookie HTTP response header. The value is in the
         * > format of "key=value", followed by a list of cookie attributes separated by semicolons, for example,
         * > **"key=value;Max-Age=100"**.
         * >
         * > If a cookie with the same host, path, and name exists, it will be replaced by the new cookie. If the cookie has
         * > expired, it will not be stored. To set multiple cookies, call this method multiple times.
         * >
         * > If **configCookieSync()** is used to set cookies for two or more times, the cookies set each time are separated
         * > by semicolons.
         * >
         * > If the specified value contains the **Secure** attribute, the URL must use the **https://** protocol.
         *
         * @param { string } url - The URL for which the cookie is to be set.
         * @param { string } value - The cookie as a string, using the format of the 'Set-Cookie' HTTP response header.
         * @param { boolean } incognito - {@code true} set a single cookie (key-value pair) for the given URL
         *     in incognito mode; {@code false} otherwise.
         * @param { boolean } includeHttpOnly - {@code true} HTTP-only cookies can also be overwritten;
         *     {@code false} otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100002 - URL error. No valid cookie found for the specified URL.
         * @throws { BusinessError } 17100005 - The provided cookie value is invalid. It must follow the format specified
         *     <br>in RFC 6265.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 14
         */
        static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void;
        /**
         * Set a single cookie (key-value pair) for the given URL Asynchronously.
         *
         * @param { string } url - The URL for which the cookie is to be set.
         * @param { string } value - The cookie as a string, using the format of the 'Set-Cookie' HTTP response header.
         * @returns { Promise<void> } - A promise resolved after the cookies of given URL have been set.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100002 - URL error. No valid cookie found for the specified URL.
         * @throws { BusinessError } 17100005 - The provided cookie value is invalid. It must follow the format specified
         *     <br>in RFC 6265.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        static configCookie(url: string, value: string): Promise<void>;
        /**
         * Set a single cookie (key-value pair) for the given URL Asynchronously.
         *
         * @param { string } url - The URL for which the cookie is to be set.
         * @param { string } value - The cookie as a string, using the format of the 'Set-Cookie' HTTP response header.
         * @param { boolean } incognito - {@code true} set a single cookie (key-value pair) for the given URL
         *     in incognito mode; {@code false} otherwise.
         * @param { boolean } includeHttpOnly - {@code true} HTTP-only cookies can also be overwritten;
         *     {@code false} otherwise.
         * @returns { Promise<void> } - A promise resolved after the cookies of given URL have been set.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100002 - URL error. No valid cookie found for the specified URL.
         * @throws { BusinessError } 17100005 - The provided cookie value is invalid. It must follow the format specified
         *     <br>in RFC 6265.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 14
         */
        static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>;
        /**
         * Set a single cookie (key-value pair) for the given URL Asynchronously.
         *
         * @param { string } url - The URL for which the cookie is to be set.
         * @param { string } value - The cookie as a string, using the format of the 'Set-Cookie' HTTP response header.
         * @param { AsyncCallback<void> } callback - Called after the cookies have been set.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100002 - URL error. No valid cookie found for the specified URL.
         * @throws { BusinessError } 17100005 - The provided cookie value is invalid. It must follow the format specified
         *     <br>in RFC 6265.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        static configCookie(url: string, value: string, callback: AsyncCallback<void>): void;
        /**
         * Save the cookies synchronously.
         *
         * <p><strong>API Note</strong>:<br>
         * **saveCookieSync** is used to forcibly write cookies that need to be persisted to disks. Session cookies are
         * not persisted on PCs, 2-in-1 devices, or tablets, even if **saveCookieSync** is invoked.
         *
         * **saveCookieSync** blocks the caller until the operation is complete. During this period, I/O operations may be
         * performed.
         * </p>
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 15
         */
        static saveCookieSync(): void;
        /**
         * Save the cookies Asynchronously.
         *
         * @returns { Promise<void> } - A promise resolved after the cookies have been saved.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        static saveCookieAsync(): Promise<void>;
        /**
         * Save the cookies Asynchronously.
         *
         * @param { AsyncCallback<void> } callback - Called after the cookies have been saved.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        static saveCookieAsync(callback: AsyncCallback<void>): void;
        /**
         * Get whether the instance can send and accept cookies.
         *
         * @returns { boolean } True if the instance can send and accept cookies else false.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        static isCookieAllowed(): boolean;
        /**
         * Set whether the instance should send and accept cookies.
         * By default this is set to be true.
         *
         * @param { boolean } accept - Whether the instance should send and accept cookies.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        static putAcceptCookieEnabled(accept: boolean): void;
        /**
         * Get whether the instance can send and accept thirdparty cookies.
         *
         * @returns { boolean } True if the instance can send and accept thirdparty cookies else false.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        static isThirdPartyCookieAllowed(): boolean;
        /**
         * Set whether the instance should send and accept thirdparty cookies.
         * By default this is set to be false.
         *
         * @param { boolean } accept - Whether the instance should send and accept thirdparty cookies.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        static putAcceptThirdPartyCookieEnabled(accept: boolean): void;
        /**
         * Check whether exists any cookies.
         *
         * @param { boolean } incognito - {@code true} check whether exists any cookies.
         *     in incognito mode; {@code false} otherwise. [since 11]
         * @returns { boolean } True if exists more than one cookie else false;
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static existCookie(incognito?: boolean): boolean;
        /**
         * Remove all cookies.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.web.webview.WebCookieManager#clearAllCookiesSync
         */
        static deleteEntireCookie(): void;
        /**
         * Remove all cookies.
         *
         * @param { boolean } incognito - {@code true} remove all cookies in incognito mode;
         *                                {@code false} otherwise.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        static clearAllCookiesSync(incognito?: boolean): void;
        /**
         * Remove all cookies Asynchronously.
         *
         * @returns { Promise<void> } - A promise resolved after the cookies have been deleted.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        static clearAllCookies(): Promise<void>;
        /**
         * Remove all cookies Asynchronously.
         *
         * @param { AsyncCallback<void> } callback - Called after the cookies have been deleted.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        static clearAllCookies(callback: AsyncCallback<void>): void;
        /**
         * Delete the session cookies.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.web.webview.WebCookieManager#clearSessionCookieSync
         */
        static deleteSessionCookie(): void;
        /**
         * Delete the session cookies.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        static clearSessionCookieSync(): void;
        /**
         * Delete the session cookies Asynchronously.
         *
         * @returns { Promise<void> } - A promise resolved after the cookies have been deleted.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        static clearSessionCookie(): Promise<void>;
        /**
         * Delete the session cookies Asynchronously.
         *
         * @param { AsyncCallback<void> } callback - Called after the cookies have been deleted.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        static clearSessionCookie(callback: AsyncCallback<void>): void;
        /**
         * Delays the initialization of the web engine. By default, the web engine is initialized when the CookieManager
         * interface is called. By setting the 'lazy' parameter to true, the web engine will not be initialized when the
         * CookieManager interface is called. Instead, the web engine will be initialized either when the web component is
         * created or when initializeWebEngine is called.
         *
         * @param { boolean } lazy - Controls whether to delay the initialization of the web engine.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 22
         */
        static setLazyInitializeWebEngine(lazy: boolean): void;
        /**
         * Fetches all stored cookies asynchronously.
         *
         * @param { boolean } incognito - {@code true} Gets all cookies in incognito context; {@code false} otherwise.
         * @returns { Promise<Array<WebHttpCookie>> } - A promise resolved after the cookies gotten.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        static fetchAllCookies(incognito: boolean): Promise<Array<WebHttpCookie>>;
        /**
         * Gets all cookies for the given URL Asynchronously.
         *
         * @param { string } url - The URL for which to fetch cookies.
         * @param { boolean } incognito - Whether to fetch cookies in incognito mode.
         * @param { boolean } includePartitionedCookies - If true, allows fetching first-party partitioned cookies.
         * @returns { Promise<string> } A promise resolved with the cookie string.
         * @throws { BusinessError } 17100002 - URL error. No valid cookie found for the specified URL.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        static fetchCookie(url: string, incognito: boolean, includePartitionedCookies: boolean): Promise<string>;
        /**
         * Gets all cookies for the given URL.
         *
         * <strong>API Note</strong>:<br>
         *
         * **fetchCookieSync()** is used to obtain all cookie values. Cookie values are separated by semicolons. However,
         * a specific cookie value cannot be obtained separately.
         *
         * @param { string } url - The URL for which the cookies are requested.
         * @param { boolean } [incognito] - {@code true} gets all cookies for the given URL
         *     in incognito mode; {@code false} otherwise. Default is false.
         * @param { boolean } [includePartitionedCookies] - If true, allows fetching first-party partitioned cookies.
         *     Default is false.
         * @returns { string } - The cookie value for the given URL.
         * @throws { BusinessError } 17100002 - URL error. No valid cookie found for the specified URL.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        static fetchCookieSync(url: string, incognito?: boolean, includePartitionedCookies?: boolean): string;
    }
    /**
     * Enum type supplied to {@link onMessageEventExt} for indicating the type of web message.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 18]
     * @atomicservice [since 11]
     * @since 10
     */
    enum WebMessageType {
        /**
         * Unsupported data type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        NOT_SUPPORT = 0,
        /**
         * The string data type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        STRING = 1,
        /**
         * The number data type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        NUMBER = 2,
        /**
         * The boolean data type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        BOOLEAN = 3,
        /**
         * The arraybuffer data type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        ARRAY_BUFFER = 4,
        /**
         * The array data type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        ARRAY = 5,
        /**
         * The error data type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        ERROR = 6
    }
    /**
     * The message received or sent from web message port.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 18]
     * @atomicservice [since 11]
     * @since 10
     */
    class WebMessageExt {
        /**
         * Get the type of the web message.
         *
         * @returns { WebMessageType } - Returns data of WebMessageType type
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        getType(): WebMessageType;
        /**
         * Get the string value of the web message.
         *
         * @returns { string } - Returns data of string type
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        getString(): string;
        /**
         * Get the number value of the web message.
         *
         * @returns { number } - Returns data of number type
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        getNumber(): number;
        /**
         * Get the boolean value of the web message.
         *
         * @returns { boolean } - Returns data of Boolean type
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        getBoolean(): boolean;
        /**
         * Get the array buffer value of the web message.
         *
         * @returns { ArrayBuffer } - Returns data of ArrayBuffer type
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        getArrayBuffer(): ArrayBuffer;
        /**
         * Get the array value of the web message.
         *
         * @returns { Array<string | number | boolean> } - Returns data of Array type
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        getArray(): Array<string | number | boolean>;
        /**
         * Get the error value of the web message.
         *
         * @returns { Error } - Returns data of Error type
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        getError(): Error;
        /**
         * Set the type of the web message.
         *
         * @param { WebMessageType } type - set WebMessageType type data
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        setType(type: WebMessageType): void;
        /**
         * Set the string value of the web message.
         *
         * @param { string } message - set string type data
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        setString(message: string): void;
        /**
         * Set the number value of the web message.
         *
         * @param { number } message - set number type data
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        setNumber(message: number): void;
        /**
         * Set the boolean value of the web message.
         *
         * @param { boolean } message - set boolean type data
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        setBoolean(message: boolean): void;
        /**
         * Set the array buffer value of the web message.
         *
         * @param { ArrayBuffer } message - set ArrayBuffer type data
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        setArrayBuffer(message: ArrayBuffer): void;
        /**
         * Set the array value of the web message.
         *
         * @param { Array<string | number | boolean> } message - set Array type data
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        setArray(message: Array<string | number | boolean>): void;
        /**
         * Set the error value of the web message.
         *
         * @param { Error } message - set Error type data
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        setError(message: Error): void;
    }
    /**
     * Defines the data types supported by {@link onMessageEventExt}.
     *
     * @unionmember { ArrayBuffer } [since 11]
     * @unionmember { string } [since 11]
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 9
     */
    type WebMessage = ArrayBuffer | string;
    /**
     * Define html web message port.
     *
     * @interface WebMessagePort [since 9 - 11]
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     */
    interface WebMessagePort {
        /**
         * The flag indicates whether more formats are supported than string and array buffers.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        isExtentionType?: boolean;
        /**
         * Close port.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        close(): void;
        /**
         * Post a message to other port.
         *
         * @param { WebMessage } message - Message to send.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100010 - Failed to post messages through the port.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        postMessageEvent(message: WebMessage): void;
        /**
         * Receive message from other port.
         *
         * @param { function } callback - Callback function for receiving messages.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100006 - Failed to register a message event for the port.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        onMessageEvent(callback: (result: WebMessage) => void): void;
        /**
         * Post a message to other port.
         *
         * @param { WebMessageExt } message - Message to send.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100010 - Failed to post messages through the port.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        postMessageEventExt(message: WebMessageExt): void;
        /**
         * Receive message from other port.
         *
         * @param { function } callback - Callback function for receiving messages.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100006 - Failed to register a message event for the port.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        onMessageEventExt(callback: (result: WebMessageExt) => void): void;
    }
    /**
     * Provides information for history item in BackForwardList.
     *
     * @interface HistoryItem [since 9 - 11]
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     */
    interface HistoryItem {
        /**
         * Pixelmap of icon.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        icon: image.PixelMap;
        /**
         * Url of this history item.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        historyUrl: string;
        /**
         * Original request url of this history item.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        historyRawUrl: string;
        /**
         * Title of this history item.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        title: string;
    }
    /**
     * Provides back and forward history list information method. related to {@link HistoryItem}.
     *
     * @interface BackForwardList [since 9 - 11]
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     */
    interface BackForwardList {
        /**
         * Current index in BackForwardList.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        currentIndex: number;
        /**
         * Size of in BackForwardList.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        size: number;
        /**
         * Get history entry at given index.
         *
         * @param { number } index Index of back forward list entry.
         * @returns { HistoryItem } HistoryItem at given index in back forward list.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        getItemAtIndex(index: number): HistoryItem;
    }
    /**
     * Provides information used to obtain a full drawing result.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    interface SnapshotInfo {
        /**
         * Snapshot ID.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        id?: string;
        /**
         * Size for web rendering. The maximum size is 16000 px × 16000 px. The length unit can be px, vp, or %. The length
         * unit must be the consistent across parameters. The default unit is vp. If the size exceeds the specifications,
         * the maximum size is returned. Example: **width: '100px', height: '200px'** or **width: '20%', height'30%'**. If
         * only digits are written, the unit is vp.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        size?: SizeOptions;
    }
    /**
    * Represents a full drawing result.
    *
    * @syscap SystemCapability.Web.Webview.Core
    * @atomicservice
    * @since 12
    */
    interface SnapshotResult {
        /**
         * Snapshot ID.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        id?: string;
        /**
         * The status of the snapshot.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        status?: boolean;
        /**
         * Size for web rendering. The maximum size is 16000 px × 16000 px. The length unit can be px, vp, or %. The length
         * unit must be the consistent across parameters. The default unit is vp. If the size exceeds the specifications,
         * the maximum size is returned. Example: **width: '100px', height: '200px'** or **width: '20%', height'30%'**. If
         * only digits are written, the unit is vp.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        size?: SizeOptions;
        /**
         * The image in PixelMap format.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        imagePixelMap?: image.PixelMap;
    }
    /**
     * Enum type supplied to {@link runJavaScriptExt} for indicating the result of JavaScript code execution.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 18]
     * @atomicservice [since 11]
     * @since 10
     */
    enum JsMessageType {
        /**
         * Unsupported data type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        NOT_SUPPORT = 0,
        /**
         * The string data type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        STRING = 1,
        /**
         * The number data type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        NUMBER = 2,
        /**
         * The boolean data type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        BOOLEAN = 3,
        /**
         * The arraybuffer data type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        ARRAY_BUFFER = 4,
        /**
         * The array data type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        ARRAY = 5
    }
    /**
     * The message for indicating the of result of JavaScript code execution.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 18]
     * @atomicservice [since 11]
     * @since 10
     */
    class JsMessageExt {
        /**
         * Get the type of the JavaScript code execution result.
         *
         * @returns { JsMessageType } - Returns data of JsMessageType type
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        getType(): JsMessageType;
        /**
         * Get the string value of the JavaScript code execution result.
         *
         * @returns { string } - Returns data of string type
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        getString(): string;
        /**
         * Get the number value of the JavaScript code execution result.
         *
         * @returns { number } - Returns data of number type
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        getNumber(): number;
        /**
         * Get the boolean value of the JavaScript code execution result.
         *
         * @returns { boolean } - Returns data of Boolean type
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        getBoolean(): boolean;
        /**
         * Get the array buffer value of the JavaScript code execution result.
         *
         * @returns { ArrayBuffer } - Returns data of ArrayBuffer
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        getArrayBuffer(): ArrayBuffer;
        /**
         * Get the array value of the the JavaScript code execution result.
         *
         * @returns { Array<string | number | boolean> } - Returns data of Array type
         * @throws { BusinessError } 17100014 - The type and value of the message do not match.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        getArray(): Array<string | number | boolean>;
        /**
         * Get the object or exception of the the JavaScript code execution result and serialize it into a string.
         *
         * @returns { string | null } - If an exception occurs, or the returned type is object, return the
         *     serialized string in the format of "Not support type: <{exception|object}>", Parts exceeding a length of
         *     2048 will be truncated; otherwise, return null.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 22
         */
        getErrorDescription(): string | null;
    }
    /**
     * Enumerates the ArkWeb render subprocess modes.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    enum RenderProcessMode {
        /**
         * ArkWeb single render subprocess mode. In this mode, multiple **Web** components share one
         * render subprocess.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        SINGLE = 0,
        /**
         * ArkWeb multi-render subprocess mode. In this mode, each **Web** component has a rendering
         * subprocess.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        MULTIPLE = 1
    }
    /**
     * Represents a configuration object for precompiling JavaScript in the **Web** component to generate bytecode cache,
     * which is designed to control the updating of the bytecode cache.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 12
     */
    interface CacheOptions {
        /**
         * Array of response headers from the server when a JavaScript file is requested. They include information such as E
         * -Tag or Last-Modified to identify the file version and determine whether the bytecode cache needs to be
         * refreshed.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        responseHeaders: Array<WebHeader>;
    }
    /**
     * Enumerates the offline resource types corresponding to the
     * [OfflineResourceMap]{@link @ohos.web.webview:webview.OfflineResourceMap} object.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 12
     */
    enum OfflineResourceType {
        /**
         * Resource of the image type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        IMAGE,
        /**
         * Resource of the CSS type.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        CSS,
        /**
         * Javascript resource loaded through the <script src="" /> tag.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        CLASSIC_JS,
        /**
         * Javascript resource loaded through the <script src="" type="module" /> tag.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        MODULE_JS
    }
    /**
     * Implements an **OfflineResourceMap** object, which is used to set information related to local offline resources
     * that will be injected into memory cache through the
     * [injectOfflineResources]{@link @ohos.web.webview:webview.WebviewController#injectOfflineResources} API. The ArkWeb
     * engine will generate resource caches based on this information and control the validity period of the cache
     * accordingly.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 12
     */
    interface OfflineResourceMap {
        /**
         * List of network addresses of the local offline resources. The first item in the list is used as the resources'
         * origin. If only one network address is provided, this single address is used for the resources' origin. The URL
         * supports only the HTTP and HTTPS protocols and contains a maximum of 2048 characters.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        urlList: Array<string>;
        /**
         * Content of a local offline resource.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        resource: Uint8Array;
        /**
         * HTTP response headers corresponding to the resources. The **Cache-Control** or **Expires** response header is
         * used to control the validity period of the resource in the memory cache. If neither of the headers is provided, a
         * default validity time of 86400 seconds (1 day) will be applied. The **Content-Type** response header is used to
         * define the MIME type of the resource. For resources of type MODULE_JS, a valid MIME type must be provided. For
         * other types, the MIME type is optional, with no default value. A non-standard MIME type can lead to the resource
         * being invalidated in the memory cache. If a **script** tag on the web page uses the **crossorigin** attribute,
         * the **Cross-Origin** response header must be set in the **responseHeaders** parameter of the API. The value for
         * this header should be **anonymous** or **use-credentials**.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        responseHeaders: Array<WebHeader>;
        /**
         * Resource type. Currently, only the JavaScript, image, and CSS types are supported.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        type: OfflineResourceType;
    }
    /**
     * Enumerates the scroll types for [setScrollable]{@link setScrollable}.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 12
     */
    enum ScrollType {
        /**
         * Scrolling event, indicating that a web page is scrolled by using a touchscreen, a touchpad, or a mouse.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        EVENT = 0
    }
    /**
     * Describes the attach status of WebViewController and the **Web** component.
     *
     * @enum { number }
     * @syscap SystemCapability.Web.Webview.Core
     * @since 20
     */
    enum ControllerAttachState {
        /**
         * Indicates webviewController is not attached a web component.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        UNATTACHED = 0,
        /**
         * Indicates webviewController is attached a web component.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        ATTACHED = 1
    }
    /**
     * Enumerates the error codes of the blankless loading.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 20
     */
    enum WebBlanklessErrorCode {
        /**
         * Operation successful.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        SUCCESS = 0,
        /**
         * Unknown error or internal status error.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        ERR_UNKNOWN = -1,
        /**
         * Invalid parameter.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        ERR_INVALID_PARAM = -2,
        /**
         * **WebViewController** is not bound to any component.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        ERR_CONTROLLER_NOT_INITED = -3,
        /**
         * No key value is matched.
         * [setBlanklessLoadingWithKey]{@link @ohos.web.webview:webview.WebviewController#setBlanklessLoadingWithKey} must
         * be used with [getBlanklessInfoWithKey]{@link @ohos.web.webview:webview.WebviewController#getBlanklessInfoWithKey}
         * and their key values must be the same. Otherwise, this error code is returned.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        ERR_KEY_NOT_MATCH = -4,
        /**
         * The similarity is low, and the system determines that the scene change is too
         * large. As a result, the
         * [setBlanklessLoadingWithKey]{@link @ohos.web.webview:webview.WebviewController#setBlanklessLoadingWithKey} API
         * does not enable frame interpolation.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        ERR_SIGNIFICANT_CHANGE = -5,
        /**
         * The frame interpolation duration set in
         * [BlanklessLoadingParam]{@link @ohos.web.webview:webview.BlanklessLoadingParam} is out of range.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        ERR_DURATION_OUT_OF_RANGE = -6,
        /**
         * The historical frame expiration time set in
         * [BlanklessLoadingParam]{@link @ohos.web.webview:webview.BlanklessLoadingParam} is out of range.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        ERR_EXPIRATION_TIME_OUT_OF_RANGE = -7
    }
    /**
     * Enumerates the current frame interpolation states.
     *
     * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
     *
     * @enum { number }
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 23
     */
    enum BlanklessFrameInterpolationState {
        /**
         * Frame interpolation succeeded.
         *
         * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        FRAME_INTERPOLATION_SUCCEEDED = 0,
        /**
         * Frame interpolation failed.
         *
         * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        FRAME_INTERPOLATION_FAILED = 1,
        /**
         * The frame interpolation is removed.
         *
         * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        FRAME_INTERPOLATION_REMOVED = 2
    }
    /**
     * Enumerates the behavior modes of the web soft keyboard.
     * @enum {number}
     * @syscap SystemCapability.Web.Webview.Core
     * @since 22
     */
    enum WebSoftKeyboardBehaviorMode {
        /**
         * When the **Web** component is focused or unfocused, or its status changes to inactive or active,
         * the system attempts to hide or display the soft keyboard. This value is used by default.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 22
         */
        DEFAULT = 0,
        /**
         * When the **Web** component's status changes between inactive and active,
         * the system does not hide or start the soft keyboard.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 22
         */
        DISABLE_AUTO_KEYBOARD_ON_ACTIVE = 1
    }
    /**
     * Describes the prediction information about blankless loading, including the first screen similarity, first screen
     * loading duration, and error code. The application determines whether to enable the blankless loading solution based
     * on the prediction information.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 20
     */
    interface BlanklessInfo {
        /**
         * Error code of blankless loading. For details, see
         * [WebBlanklessErrorCode]{@link @ohos.web.webview:webview.WebBlanklessErrorCode}.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        errCode: WebBlanklessErrorCode;
        /**
         * First screen similarity, which is calculated based on the historical first screen content. The value ranges from
         * 0 to 1.0. 1.0 indicates that the content is the same. A value closer to 1 indicates a higher similarity. This
         * value is lagging, and the similarity of local loading is displayed in the next loading. You are advised not to
         * enable the blankless loading solution when the similarity is low.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        similarity: number;
        /**
         * Loading duration estimated based on the historical first screen loading durations, in milliseconds. The value
         * must be greater than 0.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        loadingTime: number;
    }
    /**
     * Defines the frame interpolation state information in the scenario where the ArkWeb blankless loading
     * optimization is enabled.
     *
     *
     * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
     *
     * @typedef BlanklessFrameInterpolationInfo
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 23
     */
    interface BlanklessFrameInterpolationInfo {
        /**
         * Key value that uniquely identifies the page.
         *
         * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
         *
         * @type { string }
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        key: string;
        /**
         * Current frame interpolation state.
         *
         * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
         *
         * @type { BlanklessFrameInterpolationState }
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        state: BlanklessFrameInterpolationState;
        /**
         * Time when a frame is interpolated or removed.
         *
         * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
         * The value must be an integer.
         * <br>Unit: ms.
         *
         * @type { number }
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        timestamp: number;
        /**
         * Reason for the frame interpolation failure.
         *
         * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
         *
         * @type { string }
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        reason: string;
    }
    /**
     * Defines the blankless loading parameter.
     *
     * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
     *
     * @typedef BlanklessLoadingParam
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 23
     */
    interface BlanklessLoadingParam {
        /**
         * Whether to enable frame interpolation. The value true indicates to enable frame interpolation, and false
         * indicates the opposite.
         *
         * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
         *
         * @type { boolean }
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        enable: boolean;
        /**
         * Duration of the frame interpolation.
         * The valid range is the union of {0} and [200, 2000].
         *
         * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
         * The value must be an integer.
         * <br>Unit: ms.
         *
         * @type { ?number }
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        duration?: number;
        /**
         * Expiration time of the historical frame, in ms (UTC time). T indicates the current UTC time. If the
         * expiration time is 30 days, the value is 2592000000 ms. The value range is the union of (T, T + 2592000000] and
         * {0}. 0 indicates that the expiration time is not specified and the default expiration time (7 days) is used.
         *
         * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
         *
         * @type { ?number }
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        expirationTime?: number;
        /**
         * Callback for the blankless frame interpolation, which is used to return the blankless frame interpolation
         * information.
         *
         * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
         *
         * @type { ?Callback<BlanklessFrameInterpolationInfo> }
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        callback?: Callback<BlanklessFrameInterpolationInfo>;
    }
    /**
     * Security feature option configuration.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface SecurityParams {
        /**
         * Whether to disable JIT compilation. true means disabled, and false means the opposite. Default value: false.
         * To optimize performance, the V8 engine compiles hot code into machine code. Most browser vulnerabilities
         * (such as Type Confusion) are exploited by manipulating the JIT optimization process. Disabling it does not affect
         * web page functions, but the performance of complex JavaScript code decreases by about 17%. It is recommended that
         * this feature be disabled if possible. For pure display and non-computing-intensive pages (such as news and
         * documents), it is recommended that this feature not be disabled.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        disableJITCompilation?: boolean;
        /**
         * Whether to disable WebAssembly. true means disabled, and false means the opposite. Default value: false.
         * The compiled machine code is executed in WASM, which is prone to memory security vulnerabilities. It is
         * recommended that this feature be disabled if possible. For pure display and non-computing-intensive pages
         * (such as news and documents), it is recommended that this feature be disabled. Disabling it may affect web
         * page functions that depend on video encoding and decoding and complex encryption.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        disableWebAssembly?: boolean;
        /**
         * Whether to disable WebGL. true means disabled, and false means the opposite. Default value: false.
         * WebGL allows JavaScript to directly invoke the GPU driver for rendering. Attackers may exploit underlying
         * driver vulnerabilities to implement sandbox escape or remote code execution. In addition, WebGL may be used
         * for user fingerprint identification attacks. Disabling it prevents 3D rendering and causes some 2D canvases
         * to fall back to CPU rendering, which may result in a lower frame rate. It is recommended that this feature be
         * disabled for sensitive services such as financial payment, instant messaging, and government systems.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        disableWebGL?: boolean;
        /**
         * Whether to disable the PDF viewer. true means disabled, and false means the opposite. Default value: false.
         * The built-in PDF parsing engine is prone to vulnerabilities when parsing complex binary formats and embedded
         * scripts. Attackers can construct special PDF files to exploit font parsing or memory corruption vulnerabilities
         * to control the main process of the app. Disabling it prevents PDF loading in ArkWeb. It is recommended that
         * this feature be disabled for non-document office apps and users be guided to use external
         * apps to open PDF files.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        disablePDFViewer?: boolean;
        /**
         * Whether to disable MathML. true means disabled, and false means the opposite. Default value: false.
         * MathML is an outdated rendering module in the kernel and often lacks sufficient automated auditing
         * and fuzzing. It is prone to becoming a stepping stone for side-channel attacks or attribute injection XSS.
         * Disabling it prevents proper parsing and rendering of <math> tag content, which may affect formula layout
         * on a small number of science websites that have not been adapted for JavaScript. Disabling it is recommended.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        disableMathML?: boolean;
        /**
         * Whether to disable Service Worker. true means disabled, and false means the opposite. Default value: false.
         * Service Worker has persistent control and can reside in the background of web pages and intercept network
         * requests. If a web page has an XSS vulnerability, attackers can exploit it to install malicious Service
         * Worker and launch man-in-the-middle (MITM) attacks. Disabling it disables offline access, prevents Web
         * push notifications from working, and removes preloading capabilities. It is recommended that this feature
         * be disabled in industries that have high requirements on session freshness, such as banking and securities.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        disableServiceWorker?: boolean;
        /**
         * Whether to disable non-proxy UDP for WebRTC. true means disabled, and false means the opposite. Default
         * value: false. When WebRTC is enabled, it may allow malicious traffic to bypass the proxy tunnel, exposing
         * the user's real physical IP address and resulting in privacy leakage. Disabling it forces all traffic
         * through the TCP proxy, increasing latency and potentially preventing connection establishment for features
         * such as video calls and real-time intercom. It is recommended that this feature be disabled in scenarios
         * such as anonymous social networking, global services, and forcible proxy.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        disableNonProxyUDP?: boolean;
    }
    /**
     * Represents a **WebviewController** object used to control various behaviors of **Web** components, including page
     * navigation, lifecycle status, and JavaScript interaction. A **WebviewController** object can control only one
     * **Web** component, and the APIs (except static APIs) in the **WebviewController** can be invoked only after it has
     * been bound to the target **Web** component.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    class WebviewController {
        /**
         * Constructs a WebviewController object.
         *
         * @param { string } [webTag] - specified the name of the web component, Empty by default.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        constructor(webTag?: string);
        /**
         * Loads the dynamic link library (DLL) file of the web engine. This API can be called before
         * the Web component is initialized to improve the startup performance. The frequently visited
         * websites are automatically pre-connected. initializeWebEngine cannot be called in an asynchronous
         * thread. Otherwise, the system breaks down. initializeWebEngine takes effect globally and needs to
         * be called only once in an application lifecycle.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        static initializeWebEngine(): void;
        /**
         * Sets the ArkWeb kernel version. If the system does not support the specified version, the setting is invalid.
         * This API is a global static API and must be called before **initializeWebEngine** is called. If any **Web**
         * component has been loaded, the setting of this API is invalid.
         *
         * > **NOTE**
         * >
         * > - **setActiveWebEngineVersion** cannot be called in an asynchronous thread.
         * >
         * > - **setActiveWebEngineVersion** takes effect globally and needs to be called only once in an application
         * > lifecycle.
         *
         * @param {ArkWebEngineVersion} engineVersion - ArkWeb kernel version.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void;
        /**
         * Obtains the current ArkWeb kernel version.
         *
         * @returns {ArkWebEngineVersion} The ArkWeb kernel version defined by
         *     [ArkWebEngineVersion]{@link @ohos.web.webview:webview.ArkWebEngineVersion}.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        static getActiveWebEngineVersion(): ArkWebEngineVersion;
        /**
         * Checks whether the system is using the evergreen kernel, that is, the latest kernel.
         *
         * @returns {boolean} Whether the system is using the evergreen kernel. If the system is using the evergreen kernel,
         *     **true** is returned. Otherwise, **false** is returned.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        static isActiveWebEngineEvergreen(): boolean;
        /**
         * Set web engine to use HttpDns server to resolve dns.
         *
         * @param { SecureDnsMode } secureDnsMode - using HttpDns.
         * @param { string } secureDnsConfig - The configuration of the HttpDns server.
         *     Must be https protocol and only allow one server to be configured.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3. Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void;
        /**
         * Sets whether to enable web debugging. By default, web debugging is disabled.
         * For details, see Debugging Frontend Pages by Using DevTools.
         *
         * <p><strong>API Note</strong>:<br>
         * Enabling web debugging allows users to check and modify the internal status of the web page,
         * which poses security risks. Therefore, you are advised not to enable this function
         * in the officially released version of the app.
         * </p>
         *
         * @param { boolean } webDebuggingAccess - Sets whether to enable web debugging.{@code true} enable web debugging;
         *     {@code false} disable web debugging. The default value is false.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        static setWebDebuggingAccess(webDebuggingAccess: boolean): void;
        /**
         * Enable the ability to check website security risks.
         * Illegal and fraudulent websites are mandatory enabled and can't be disabled by this function.
         *
         * @param { boolean } enable - {@code true} enable check the website security risks; {@code false} otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        enableSafeBrowsing(enable: boolean): void;
        /**
         * Get whether checking website security risks is enabled.
         *
         * @returns { boolean } True if enable the ability to check website security risks else false.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        isSafeBrowsingEnabled(): boolean;
        /**
         * Checks whether the web page can go forward.
         *
         * @returns { boolean } True if the web page can go forward else false.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        accessForward(): boolean;
        /**
         * Checks whether the web page can go back.
         *
         * @returns { boolean } True if the web page can go back else false.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        accessBackward(): boolean;
        /**
         * Checks whether the web page can go back or forward the given number of steps.
         *
         * @param { number } step - The number of steps.
         * @returns { boolean } True if the web page can go back else false.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        accessStep(step: number): boolean;
        /**
         * Goes forward in the history of the web page.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        forward(): void;
        /**
         * Goes back in the history of the web page.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        backward(): void;
        /**
         * Clears the history in the Web.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        clearHistory(): void;
        /**
         * Called when the Web component enters the active state. The application can interact with
         * the user while in the active foreground state, and it remains in this state until the
         * focus is moved away from it due to some event (for example, an incoming call is received
         * or the device screen is turned off).
         *
         * @throws { BusinessError } 17100001 - Init error.
         *                           The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        onActive(): void;
        /**
         * Called when the Web component enters the inactive state. You can implement the behavior to perform
         * after the application loses focus. When this API is called, any content that can be safely paused,
         * such as animations and geographical locations, is paused as much as possible. However, the JavaScript
         * is not paused. To pause the JavaScript globally, use pauseAllTimers. To reactivate the Web component,
         * use onActive.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *                           The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        onInactive(): void;
        /**
         * Refreshes the current URL.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        refresh(): void;
        /**
         * Refreshes the current URL.
         *
         * @param { boolean } ignoreCache - If set to true, it indicates an end-to-end request with "pragma: no-cache";
         *     otherwise, it performs a normal refresh.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 24
         */
        refresh(ignoreCache: boolean): void;
        /**
         * Loads the data or URL.
         *
         * When both **baseUrl** and **historyUrl** are empty:
         *
         * If **encoding** is not base64 (including null values), ASCII encoding is used for octets within the secure URL
         * character range, and the standard %xx hexadecimal encoding of the URL is used for octets outside the secure URL
         * character range.
         *
         * @param { string } data - A string encoded according to "Base64" or "URL".
         * @param { string } mimeType - Media type. For example: "text/html".
         * @param { string } encoding - Encoding type. For example: "UTF-8".
         * @param { string } [baseUrl] - A specified URL path ("http"/"https"/"data" protocol),
         *                             which is assigned to window.origin by the Web component.
         * @param { string } [historyUrl] - History URL. When it is not empty, it can be managed by
         *                                history records to realize the back and forth function.
         *                                This property is invalid when baseUrl is empty.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2048. [since 9 - 10]
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void;
        /**
         * Loads the data or URL.
         *
         * @param { string | Resource } url - The URL to load.
         * @param { Array<WebHeader> } [headers] - Additional HTTP request header for URL.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid.
         * @throws { BusinessError } 17100003 - Invalid resource path or file type.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        loadUrl(url: string | Resource, headers?: Array<WebHeader>): void;
        /**
         * Obtains the element type of the area being clicked.
         *
         * @returns { WebHitTestType } Element type of the area being clicked.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead webview.WebviewController#getLastHitTest
         */
        getHitTest(): WebHitTestType;
        /**
         * Stores the current page as a web archive.
         *
         * @param { string } baseName - Where the generated offline webpage is stored, This value cannot be null.
         * @param { boolean } autoName - Decide whether to automatically generate the file name. If false, it is
         *     stored by the file name of baseName. If true, the file name is
         *     automatically generated based on the current URL and stored in the file
         *     directory of baseName.
         * @returns { Promise<string> } a promise resolved after the web archive has been stored. The parameter
         *     will either be the filename under which the file was stored, or empty
         *     if storing the file failed.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3. Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100003 - Invalid resource path or file type.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        storeWebArchive(baseName: string, autoName: boolean): Promise<string>;
        /**
         * Stores the current page as a web archive.
         *
         * @param { string } baseName - Where the generated offline webpage is stored, This value cannot be null.
         * @param { boolean } autoName - Decide whether to automatically generate the file name. If false, it is
         *     stored by the file name of baseName. If true, the file name is
         *     automatically generated based on the current URL and stored in the file
         *     directory of baseName.
         * @param { AsyncCallback<string> } callback - called after the web archive has been stored. The parameter
         *     will either be the filename under which the file was stored,
         *     or empty if storing the file failed.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3. Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100003 - Invalid resource path or file type.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void;
        /**
         * Zooms in or out of this web page. This API is effective only when
         * [zoomAccess]{@link @ohos.web.WebAttribute#zoomAccess} is **true**.
         *
         * @param { number } factor - Relative zoom ratio. The value must be greater than 0. The value **1** indicates that
         *     the page is not zoomed. A value smaller than **1** indicates zoom-out, and a value greater than **1**
         *     indicates zoom-in.<br>Value range: (0, 100]
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100004 - Function not enabled.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        zoom(factor: number): void;
        /**
         * Zooms in on this web page by 25%.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100004 - Function not enabled.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        zoomIn(): void;
        /**
         * Zooms out of this web page by 20%.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100004 - Function not enabled.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        zoomOut(): void;
        /**
         * Obtains the element information of the area being clicked.
         *
         * @returns { HitTestValue } Element information of the area being clicked.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead webview.WebviewController#getLastHitTest
         */
        getHitTestValue(): HitTestValue;
        /**
         * Obtains the index value of this Web component, which can be used for **Web** component management.
         * @returns { number } Returns the index value of the current Web component.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        getWebId(): number;
        /**
         * Gets the default user agent.
         *
         * @returns { string } Return user agent information.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice [since 11]
         * @since 9
         */
        getUserAgent(): string;
        /**
         * Gets the title of current Web page.
         *
         * @returns { string } Return to File Selector Title.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        getTitle(): string;
        /**
         * Obtains the height of this web page. For details, see
         * [Obtaining the Web Page Content Height](docroot://web/web-getpage-height.md).
         *
         * @returns { number } Height of the current web page. Unit: vp.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        getPageHeight(): number;
        /**
         * Goes forward or back backOrForward in the history of the web page.
         *
         * @param { number } step - Steps to go forward or backward.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        backOrForward(step: number): void;
        /**
         * Requests focus for this web page.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        requestFocus(): void;
        /**
         * Create web message ports
         *
         * @param { boolean } isExtentionType - Set whether the web message port supports extention type. [since 10]
         * @returns { Array<WebMessagePort> } An array represent 2 WebMessagePort, then can use
         *     those ports to communication with html pages.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed. [since 10]
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>;
        /**
         * Post web message port to html
         *
         * @param { string } name - Data name information to send.
         * @param { Array<WebMessagePort> } ports - Port number array information to send.
         * @param { string } uri - URI to receive this information.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void;
        /**
         * Stops the current load.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        stop(): void;
        /**
         * Registers the supplied ArkTs object into this Web component.
         * The object is registered into all frames of the web page, including all iframes, using the specified name.
         * This allows the methods of the ArkTs object to be accessed from JavaScript.
         *
         * <p><strong>API Note</strong>:<br>
         * Registed objects will not appear in JavaScript until the page is next (re)load.
         * To avoid memory leaks, registerJavaScriptProxy must be used together with deleteJavaScriptProxy.
         * To avoid security risks, it is recommended that registerJavaScriptProxy be used with trusted web components.
         * If the same method is registered repeatedly in both synchronous and asynchronous list, it will default to an
         * asynchronous method. The synchronous function list and asynchronous function list cannot be empty at the same
         * time. otherwise, this registration will fail.
         * <p>
         *
         * @param { object } jsObject - Application side JavaScript objects participating in registration.
         * @param { string } name - The name of the registered object, which is consistent with the
         *     object name called in the window.
         * @param { Array<string> } methodList - The method of the application side JavaScript object participating
         *     in the registration.
         * @param { Array<string> } [asyncMethodList] - The async method of the application side JavaScript object
         *     participating in the registration. [since 12]
         * @param { string } [permission] - permission configuration defining web page URLs that can access JavaScriptProxy
         *     methods.
         *     The configuration can be defined at two levels, object level and method level. [since 12]
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>, asyncMethodList?: Array<string>, permission?: string): void;
        /**
         * Deletes a registered JavaScript object with given name.
         *
         * @param { string } name - The name of a registered JavaScript object to be deleted.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100008 - Failed to delete JavaScriptProxy because it does not exist.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        deleteJavaScriptRegister(name: string): void;
        /**
         * Searches the web page for content that matches the keyword specified by **'searchString'** and highlights the
         * matches on the page. This API returns the result asynchronously through
         * [onSearchResultReceive]{@link @ohos.web.WebAttribute#onsearchresultreceive}
         * .
         *
         * @param { string } searchString - Search keyword.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        searchAllAsync(searchString: string): void;
        /**
         * Clears the matches found through [searchAllAsync]{@link webview.WebviewController#searchAllAsync}.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        clearMatches(): void;
        /**
         * Highlights and scrolls to the next match search.
         *
         * @param { boolean } forward - Step of search is back or forward.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        searchNext(forward: boolean): void;
        /**
         * Clears the ssl cache in the Web.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        clearSslCache(): void;
        /**
         * Clears the client authentication certificate cache in the Web.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        clearClientAuthenticationCache(): void;
        /**
         * Asynchronously execute JavaScript in the context of the currently displayed page.
         * The result of the script execution will be returned through a via Promise.
         * This method must be used on the UI thread, and the callback will also be invoked on the UI thread.
         *
         * <p><strong>API Note</strong>:<br>
         * The state of JavaScript is no longer persisted across navigations like loadUrl.
         * For example, global variables and functions defined before calling loadUrl will not exist in the loaded page.
         * It is recommended that applications use registerJavaScriptProxy to ensure that the JavaScript state can be
         * persisted across page navigations.<br>
         * If you cannot obtain the return value by executing the asynchronous method,
         * you need to determine whether to use synchronous or asynchronous mode based on the specific situation.
         * <p>
         *
         * @param { string } script - JavaScript Script.
         * @returns { Promise<string> } A promise is solved after the JavaScript script is executed.
         *     This parameter will be the result of JavaScript script execution.
         *     If the JavaScript script fails to execute or has no return value,
         *     null will be returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100003 - Calling a JS method that returns an empty ArrayBuffer via runJavaScript.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        runJavaScript(script: string): Promise<string>;
        /**
         * Asynchronously execute JavaScript in the context of the currently displayed page.
         * The result of the script execution will be returned through an asynchronous callback.
         * This method must be used on the UI thread, and the callback will also be invoked on the UI thread.
         *
         * <p><strong>API Note</strong>:<br>
         * The state of JavaScript is no longer persisted across navigations like loadUrl.
         * For example, global variables and functions defined before calling loadUrl will not exist in the loaded page.
         * It is recommended that applications use registerJavaScriptProxy to ensure that the JavaScript state can be
         * persisted across page navigations.
         * <p>
         *
         * @param { string } script - JavaScript Script.
         * @param { AsyncCallback<string> } callback - Callbacks execute JavaScript script results.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100003 - Calling a JS method that returns an empty ArrayBuffer via runJavaScript.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        runJavaScript(script: string, callback: AsyncCallback<string>): void;
        /**
         * Execute JavaScript code in the context of the currently displayed page, and return the result.
         *
         * @param { string } script - JavaScript Script. [since 10 - 11]
         * @param { string | ArrayBuffer } script - JavaScript Script. [since 12]
         * @returns { Promise<JsMessageExt> } A promise is solved after the JavaScript script is executed.
         *     This parameter will be the result of JavaScript script execution.
         *     If the JavaScript script fails to execute or has no return value,
         *     a none type value will be returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>;
        /**
         * Execute JavaScript code in the context of the currently displayed page, and return the result.
         *
         * @param { string } script - JavaScript Script. [since 10 - 11]
         * @param { string | ArrayBuffer } script - JavaScript Script. [since 12]
         * @param { AsyncCallback<JsMessageExt> } callback - Callbacks execute JavaScript script results.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 10
         */
        runJavaScriptExt(script: string | ArrayBuffer, callback: AsyncCallback<JsMessageExt>): void;
        /**
         * Obtains the data stream of a specified web page using an asynchronous callback.
         *
         * @param { PdfConfiguration } configuration - Parameters required for creating a PDF file.
         * @param { AsyncCallback<PdfData> } callback - Callback used to return the data stream of an online PDF file.
         * @throws { BusinessError } 401 - Invalid input parameter.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void;
        /**
         * Obtains the data stream of a specified web page using a promise.
         *
         * @param { PdfConfiguration } configuration - Parameters required for creating a PDF file.
         * @returns { Promise<PdfData> } Promise used to return the data stream of a web page.
         * @throws { BusinessError } 401 - Invalid input parameter.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        createPdf(configuration: PdfConfiguration): Promise<PdfData>;
        /**
         * Gets the url of current Web page.
         *
         * @returns { string } Return the url of the current page.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        getUrl(): string;
        /**
         * Scrolls the page up by half the viewport or jumps to the top of the page.
         *
         * @param { boolean } top - Whether to jump to the top of the page.<br>The value **false** means to scroll the page
         *     up by half the viewport, and the value **true** means to jump to the top of the page.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        pageUp(top: boolean): void;
        /**
         * Scrolls the page down by half the viewport or jumps to the bottom of the page.
         *
         * @param { boolean } bottom - Whether to jump to the bottom of the page.<br>The value **false** means to scroll the
         *     page down by half the viewport, and the value **true** means to jump to the bottom of the page.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        pageDown(bottom: boolean): void;
        /**
         * Gets the original url of current Web page.
         *
         * @returns { string } Return the original url of the current page.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        getOriginalUrl(): string;
        /**
         * Gets the favicon of current Web page.
         *
         * @returns { image.PixelMap } Return the favicon bitmap of the current page.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        getFavicon(): image.PixelMap;
        /**
         * Put network state for web. Which is used to set window.navigator.onLine property in
         * JavaScript.
         *
         * @param { boolean } enable - Whether enable window.navigator.onLine.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        setNetworkAvailable(enable: boolean): void;
        /**
         * Checks whether this page contains images. This API uses a promise to return the result.
         *
         * @returns { Promise<boolean> } Promise used to return the result.
         *     <br> The value **true** indicates that this page contains images, and the value **false** indicates the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        hasImage(): Promise<boolean>;
        /**
         * Checks whether this page contains images. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result.<br> The value **true** indicates
         *     that this page contains images, and the value **false** indicates the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        hasImage(callback: AsyncCallback<boolean>): void;
        /**
         * Get back forward stack list from current webview.
         *
         * <p><strong>API Note</strong>:<br>
         * onLoadIntercept is triggered when the loading starts. At this time, no entry is generated.
         * Therefore, the entries obtained by calling **getBackForwardEntries** in **onLoadIntercept**
         * does not include the page that is being loaded.
         * </p>
         *
         * @returns { BackForwardList } Back forward list for current webview.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        getBackForwardEntries(): BackForwardList;
        /**
         * Clears the cache in the application. This API will clear the cache for all webviews in the same application.
         *
         * @param { boolean } clearRom - Whether to clear the cache in the ROM and RAM at the same time.
         *     {@code true} means to clear the cache in the ROM and RAM at the same time;
         *     {@code false} means to only clear the cache in the RAM.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        removeCache(clearRom: boolean): void;
        /**
         * Remove resource cache in application. So this method will remove all cache for all web components in the
         * same application.
         *
         * @param { boolean } clearRom - Remove cache in both rom and ram if true. Otherwise only clear cache
         *     in ram.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 18
         */
        static removeAllCache(clearRom: boolean): void;
        /**
         * Scrolls the page to the specified absolute position within a specified period.
         *
         * @param { number } x - X coordinate of the absolute position. If the value is a negative number, the value 0 is
         *     used.<br>Unit: vp
         * @param { number } y - Y coordinate of the absolute position. If the value is a negative number, the value 0 is
         *     used.<br>Unit: vp
         * @param { number } [duration] - Scrolling animation duration,<br>in milliseconds.<br>If no value is input or the
         *     input value is a negative number or 0, the animation is disabled.<br>If **null** or **undefined** is passed,
         *     error code **401** is thrown. [since 14]
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        scrollTo(x: number, y: number, duration?: number): void;
        /**
         * Scrolls the page by the specified amount within a specified period.
         *
         * @param { number } deltaX - Amount to scroll by along the x-axis. The positive direction is rightward.<br>Unit: vp
         * @param { number } deltaY - Amount to scroll by along the y-axis. The positive direction is downward.<br>Unit: vp
         * @param { number } duration - Scrolling animation duration,<br>in milliseconds.<br>If no value is input or the
         *     input value is a negative number or 0, the animation is disabled.<br>If **null** or **undefined** is passed,
         *     error code **401** is thrown. [since 14]
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 9
         */
        scrollBy(deltaX: number, deltaY: number, duration?: number): void;
        /**
         * Simulates a slide-to-scroll action on the page at the specified velocity.
         *
         * @param { number } vx - Horizontal velocity component of the slide-to-scroll action, where the positive direction
         *     is rightward.<br>Unit: vp/ms.
         * @param { number } vy - Vertical velocity component of the slide-to-scroll action, where the positive direction is
         *     downward.<br>Unit: vp/ms.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        slideScroll(vx: number, vy: number): void;
        /**
         * Serialize the access stack of the web, that is, the history of access.
         * @returns { Uint8Array } Web access stack after serialization.
         * @throws { BusinessError } 17100001 - Init error.
         *                           The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        serializeWebState(): Uint8Array;
        /**
         * Restores the page status history from the serialized data of the current WebView. If the
         * value of state is too large, exceptions may occur. It is recommended that the page status
         * history be not restored when the state value is greater than 512 KB.
         * @param { Uint8Array } state - Web access stack after serialization.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         * <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *                           The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        restoreWebState(state: Uint8Array): void;
        /**
         * Grant the Web kernel the permission to initiate cross-domain requests for custom protocol URLs and to initiate
         * fetch requests for custom protocol URLs. When the Web performs a cross-domain fetch of a custom protocol URL,
         * this fetch request can be intercepted by the onInterceptRequest event interface, allowing developers to further
         * process the request. It is recommended to call this interface before any Web component is initialized.
         *
         * @param { Array<WebCustomScheme> } schemes - Configuration of web custom scheme.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100020 - Failed to register custom schemes. [since 12]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 9
         */
        static customizeSchemes(schemes: Array<WebCustomScheme>): void;
        /**
         * Grant the Web kernel the permission to initiate cross-domain requests for custom protocol URLs and to initiate
         * fetch requests for custom protocol URLs. When the Web performs a cross-domain fetch of a custom protocol URL,
         * this fetch request can be intercepted by the onInterceptRequest event interface, allowing developers to further
         * process the request. It is recommended to call this interface before any Web component is initialized.
         *
         * @param { Array<WebCustomScheme> } schemes - Configuration of web custom scheme.
         * @param { boolean } lazyInitWebEngine - When true: The interface internally skips initializing WebEngine and
         *     temporarily stores the registered schemes, which will be passed to WebEngine when it actually
         *     initializes. When false: The interface automatically performs WebEngine initialization internally
         * @throws { BusinessError } 17100020 - Failed to register custom schemes.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. The length of the schemes array is greater than 10.
         *     2. The character length of the scheme is greater than 32.
         *     3. The character in the scheme is not within the allowed range of lowercase English letters, numbers,
         *     and the symbols ".", "+", "-".
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 21
         */
        static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void;
        /**
         * Get certificate for the current website.
         *
         * @returns { Promise<Array<cert.X509Cert>> } the promise of the current website's certificate.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        getCertificate(): Promise<Array<cert.X509Cert>>;
        /**
         * Get certificate for the current website.
         *
         * @param {AsyncCallback<Array<cert.X509Cert>>} callback - the callback of getCertificate.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void;
        /**
         * Mutes this web page.
         *
         * @param { boolean } mute - Whether to mute the web page.<br>The value **true** means to mute the web page, and
         *     **false** means the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        setAudioMuted(mute: boolean): void;
        /**
         * Prefetch the resources required by the page, but will not execute js or render the page.
         * <p><strong>API Note</strong>:<br>
         * The downloaded page resources are cached for about 5 minutes. After this period, the **Web** component
         * automatically releases the resources.
         * **prefetchPage** can also prefetch 302 redirect pages.
         * When a page is loaded after **prefetchPage** is executed, the prefetched resources are directly loaded from
         * the cache.
         * The **prefetchPage** has a 500ms interval restriction. If multiple URLs are prefetched consecutively within
         * a short time, only the first one will take effect.
         * </p>
         *
         * @param { string } url - Which url to preresolve/preconnect.
         * @param { Array<WebHeader> } [additionalHeaders] - Additional HTTP request header of the URL.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2048. [since 10 - 21]
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2*1024*1024. [since 22]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void;
        /**
         * Prefetch the resources required by the page, but will not execute js or render the page.
         *
         * <p><strong>API Note</strong>:<br>
         * The downloaded page resources are cached for about 5 minutes. After this period, the **Web** component
         * automatically releases the resources.
         * **prefetchPage** can also prefetch 302 redirect pages.
         * When a page is loaded after **prefetchPage** is executed, the prefetched resources are directly loaded from
         * the cache.
         * ?prefetchPage? does not cache resources with Cache-Control: no-store by default, and only allows one prefetch
         * within 500ms.
         * Prefetch behavior can be customized via ?prefetchOptions?, including ignoring Cache-Control: no-store and
         * adjusting the throttling interval.
         *
         * @param { string } url - Which url to preresolve/preconnect.
         * @param { Array<WebHeader> } [additionalHeaders] - Additional HTTP request header of the URL.
         * @param { PrefetchOptions } [prefetchOptions] - Prefetch behavior can be customized via ?prefetchOptions?,
         *     including ignoring Cache-Control: no-store and adjusting the throttling interval.
         * @throws { BusinessError } 17100001 - Init error. The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2048. [since 21 - 21]
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2*1024*1024. [since 22]
         * @syscap SystemCapability.Web.Webview.Core
         * @since 21
         */
        prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void;
        /**
         * Preresolve or Preconnect the url. This API can be called before loading the url to make loading faster.
         *
         * @param { string } url - Which url to preresolve/preconnect.
         * @param { boolean } preconnectable - Indicates whether to preconnect.
         * @param { number } numSockets - If preconnectable is true, this parameter indicates the number of sockets
         *     to be preconnected.
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2048. [since 10 - 21]
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2*1024*1024. [since 22]
         * @throws { BusinessError } 17100013 - The number of preconnect sockets is invalid.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 11]
         * @since 10
         */
        static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: number): void;
        /**
         * Set custom user agent.
         *
         * @param { string } userAgent - User custom agent information.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        setCustomUserAgent(userAgent: string): void;
        /**
         * Get custom user agent.
         *
         * @returns { string } Get custom User agent information.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getCustomUserAgent(): string;
        /**
         * Set web engine socket connection timeout. Unit: seconds. the default timeout interval is **30** seconds.
         *
         * @param { number } timeout - Socket connection timeout.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3. Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        static setConnectionTimeout(timeout: number): void;
        /**
         * Set delegate for download.
         * Used to notify the progress of the download triggered from web.
         *
         * @param { WebDownloadDelegate } delegate - Delegate used for download triggered from web.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        setDownloadDelegate(delegate: WebDownloadDelegate): void;
        /**
         * Start a download.
         *
         * @param { string } url - The download url.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2048. [since 11 - 21]
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2*1024*1024. [since 22]
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        startDownload(url: string): void;
        /**
         * Loads the URL use "POST" method with post data.
         *
         * @param { string } url - Request the URL use "POST" method.
         * @param { ArrayBuffer } postData - This data will passed to "POST" request.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        postUrl(url: string, postData: ArrayBuffer): void;
        /**
         * Creates a **PrintDocumentAdapter** instance to provide content for printing.
         *
         * @param { string } jobName - Name of the file to print.
         * @returns { print.PrintDocumentAdapter } **PrintDocumentAdapter** instance created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 11
         */
        createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter;
        /**
         * Get the security level of the current page.
         *
         * @returns { SecurityLevel } the security level of current page.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        getSecurityLevel(): SecurityLevel;
        /**
         * Whether the incognito mode is set.
         *
         * @returns { boolean } {@code true} has been set the incognito mode; {@code false} otherwise.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        isIncognitoMode(): boolean;
        /**
         * Sets whether this web page is scrollable.
         *
         * @param { boolean } enable - Whether this web page is scrollable.<br>The value **true** indicates that this web
         *     page is scrollable, and **false** indicates the opposite.<br>Default value: **true**.
         * @param { ScrollType } type - Scrolling type supported by the web page. The default value is supported.<br> - If
         *     the value of **enable** is set to **false**, the specified **ScrollType** is disabled. If **ScrollType** is
         *     set to the default value, all scrolling types are disabled.<br> - If the value of **enable** is set to
         *     **true**, all scrolling types are enabled regardless of the value of **ScrollType**.<br>If **null** or
         *     **undefined** is passed, error code **401** is thrown.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        setScrollable(enable: boolean, type?: ScrollType): void;
        /**
         * Obtains whether this web page is scrollable.
         *
         * @returns { boolean } Whether this web page is scrollable.
         *     <br>The value **true** indicates that this web page is scrollable, and **false** indicates the opposite.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        getScrollable(): boolean;
        /**
         * Sets whether to print the background of a web page. If the setting of this API is inconsistent with that of
         * [PrintAttributes](docroot://reference/apis-basic-services-kit/js-apis-print.md#printattributes11), the setting of
         * this API takes precedence.
         *
         * @param { boolean } enable - Whether to print the web page background.<br>The value **true** means to print the
         *     web page background, and **false** means the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        setPrintBackground(enable: boolean): void;
        /**
         * Obtains whether the web page background is printed.
         *
         * @returns { boolean } Whether the web page background is printed.
         *     <br>The value **true** indicates that the web page background is printed, and **false** indicates the opposite.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        getPrintBackground(): boolean;
        /**
         * Get the url of the last frame that calls the JavaScriptProxy.
         * This should be called on the UI thread.
         *
         * @returns { string } The url of the last frame that calls the JavaScriptProxy.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        getLastJavascriptProxyCallingFrameUrl(): string;
        /**
         * Enables the camera capture of the current web page. Before using the camera, add the **ohos.permission.CAMERA**
         * permission to **module.json5**. For details about how to add the permission, see
         * [Declaring Permissions in the Configuration File](docroot://security/AccessToken/declare-permissions.md).
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        startCamera(): void;
        /**
         * Stops the camera capture of the current web page.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        stopCamera(): void;
        /**
         * Disables the camera capture of the current web page.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        closeCamera(): void;
        /**
         * Called when the Web component enters the inactive state. You can implement the behavior to
         * perform after the application loses focus. When this API is called, any content that can
         * be safely paused, such as animations and geographical locations, is paused as much as
         * possible. However, the JavaScript is not paused. To pause the JavaScript globally,
         * use pauseAllTimers. To reactivate the Web component, use onActive.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *                           The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static pauseAllTimers(): void;
        /**
         * Resume all timers suspended from the pauseAllTimers() interface.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *                           The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static resumeAllTimers(): void;
        /**
         * Stops all audio and video on a web page.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        stopAllMedia(): void;
        /**
         * Resumes the playback of the audio and video that are paused by the pauseAllMedia interface.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        resumeAllMedia(): void;
        /**
         * Pauses all audio and video on a web page.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        pauseAllMedia(): void;
        /**
         * Closes all full-screen videos on a web page.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        closeAllMediaPresentations(): void;
        /**
         * Queries the audio and video playback status of the current web page.
         *
         * @returns { MediaPlaybackState } Playback control status of the current web page. The options are **NONE**,
         *     **PLAYING**, **PAUSED**, and **STOPPED**.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        getMediaPlaybackState(): MediaPlaybackState;
        /**
         * Set web scheme handler for specific scheme. This is only used for related web component.
         *
         * @param { string } scheme - String value for url scheme.
         * @param { WebSchemeHandler } handler - Web scheme handler.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void;
        /**
         * Clear all web scheme handlers for related web component.
         *
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        clearWebSchemeHandler(): void;
        /**
         * Set web scheme handler for specific scheme. This is used for service worker.
         *
         * @param { string } scheme - String value for url scheme.
         * @param { WebSchemeHandler } handler - Web scheme handler.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void;
        /**
         * Clear all web service worker scheme handlers.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static clearServiceWorkerWebSchemeHandler(): void;
        /**
         * Enable the ability to use Intelligent Tracking Prevention; default is disabled.
         *
         * @param { boolean } enable {@code true} enable Intelligent Tracking Prevention; {@code false} otherwise.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        enableIntelligentTrackingPrevention(enable: boolean): void;
        /**
         * Get whether Intelligent Tracking Prevention is enabled.
         *
         * @returns { boolean } True if enable the Intelligent Tracking Prevention; else false.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        isIntelligentTrackingPreventionEnabled(): boolean;
        /**
         * Add bypassing hosts for Intelligent Tracking Prevention.
         *
         * @param { Array<string> } hostList - Hosts that bypass the Intelligent Tracking Prevention.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void;
        /**
         * Remove bypassing hosts for Intelligent Tracking Prevention.
         *
         * @param { Array<string> } hostList - Hosts needs to remove from bypass list.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void;
        /**
         * Clear bypassing hosts for Intelligent Tracking Prevention.
         *
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static clearIntelligentTrackingPreventionBypassingList(): void;
        /**
         * Get the default user agent.
         *
         * @returns {string} The default user agent string.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 14
         */
        static getDefaultUserAgent(): string;
        /**
         * Called when the
         * [application takes over media playback of the web page](docroot://reference/apis-arkweb/arkts-basic-components-web-attributes.md#enablenativemediaplayer12)
         * and a media file is played on the web page.
         *
         * If the application does not take over media playback on the web page, this callback is not invoked.
         *
         * @param { CreateNativeMediaPlayerCallback } callback - Callback when the application takes over media playback on
         *     the web page.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void;
        /**
         * Enables the full drawing capability for the web page. This API works only during **Web** component
         * initialization.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static enableWholeWebPageDrawing(): void;
        /**
         * Obtains the full drawing result of the web page.
         *
         * > **NOTE**
         * >
         * > Only static images and texts in the rendering process can be captured.
         * >
         * > If there is a video on the page, the placeholder image of the video is displayed when you take a snapshot. If
         * > there is no placeholder image, the page is blank.
         *
         * @param { SnapshotInfo } info - Information for obtaining the full drawing result.
         * @param { AsyncCallback<SnapshotResult> } callback - Callback used to return the result.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void;
        /**
         * Prefetches resource requests based on specified request information and additional HTTP request headers, saves
         * the requests to the memory cache, and specifies the cache key and validity period to accelerate loading.
         * Currently, only POST requests whose Content-Type is application/x-www-form-urlencoded are supported. A maximum of
         * six POST requests can be pre-obtained. To prefetch the seventh post request, call
         * [clearPrefetchedResource]{@link webview.WebviewController#clearPrefetchedResource} to clear the cache of
         * unnecessary post requests. Otherwise, the cache of the earliest prefetched POST request will be automatically
         * cleared. To use the prefetched resource cache, you need to add the key value **ArkWebPostCacheKey** to the header
         * of the POST request. The content of the key value is the cacheKey of the corresponding cache.
         *
         * Resources in the memory cache are automatically managed by the ArkWeb engine. When the injected resources are
         * excessive and cause significant memory pressure, the engine will automatically release unused resources. It is
         * advisable to avoid injecting a large number of resources into the memory cache.
         *
         * @param { RequestInfo } request - Information about the prefetched request.
         * @param { Array<WebHeader> } [additionalHeaders] - Additional HTTP request header of the prefetched request.<br>If
         *     **undefined** or **null** is passed, error code **401** will be thrown.
         * @param { string } [cacheKey] - Key used to query the cache of prefetched resources. The value can contain only
         *     letters and digits. If this parameter is not passed or is left empty, **url** is used by default.<br>If
         *     **undefined** or **null** is passed, error code **401** will be thrown.
         * @param { number } [cacheValidTime] - Validity period for caching prefetched resources.<br>Value range: (0, 214748
         *     3647]<br>Default value: **300s**<br>Unit: second.<br>If **undefined** or **null** is passed, error code
         *     **401** will be thrown.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left
         *     unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2048. [since 12 - 21]
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2\*1024\*1024. [since 22]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string, cacheValidTime?: number): void;
        /**
        * Clears the cache of prefetched resources based on the specified cache key list. The cache key in the input
        * parameter must be the prefetched resource cache key specified by
        * [prefetchResource]{@link webview.WebviewController.prefetchResource}.
        *
        * @param { Array<string> } cacheKeyList - Key used to query the cache of prefetched resources. The value can
        *     contain only letters and digits. If this parameter is not passed or is left empty, **url** is used by
        *     default.
        * @syscap SystemCapability.Web.Webview.Core
        * @atomicservice
        * @since 12
        */
        static clearPrefetchedResource(cacheKeyList: Array<string>): void;
        /**
         * Sets the ArkWeb render subprocess mode.
         *
         * @param { RenderProcessMode } mode - The render process mode for the ArkWeb.
         *        Call {@link getRenderProcessMode} to get the ArkWeb rendering subprocess mode of the current device.
         *        The enumerated value **0** indicates the single render subprocess mode,
         *        and **1** indicates the multi-render subprocess mode.
         *        If an invalid number other than the enumerated value of **RenderProcessMode** is passed,
         *        the multi-render subprocess mode is used by default.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         * <br>2. Incorrect parameter types.
         * @static
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static setRenderProcessMode(mode: RenderProcessMode): void;
        /**
         * Obtains the ArkWeb render subprocess mode.
         *
         * @returns { RenderProcessMode } mode - The render process mode of the ArkWeb.
         *          Call {@link getRenderProcessMode} to get the ArkWeb rendering subprocess mode of the current device,
         *          with an enumeration value of 0 as a single subprocess mode and an enumeration value of 1 as a multi-subprocess mode.
         *          If the obtained value is not within the range of the RenderProcessMode enumeration value,
         *          it defaults to the multi-rendering subprocess mode.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static getRenderProcessMode(): RenderProcessMode;
        /**
         * Terminates this render process.
         * Calling this API will destroy the associated render process. If the render process has not
         * been started or has been destroyed, there is no impact. In addition, destroying the render process affects
         * all other instances associated with the render process.
         *
         * @returns { boolean } true if it was possible to terminate the render process, otherwise false.
         *         Calling this on a not yet started, or an already terminated render will have no effect.
         * @throws { BusinessError } 17100001 - Init error.
         *                           The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        terminateRenderProcess(): boolean;
        /**
         * Precompiles JavaScript to generate the bytecode cache or update the existing bytecode cache based on the provided
         * parameters.
         *
         * The API determines whether to update the existing bytecode cache based on the provided file information, E-Tag
         * response header, and Last-Modified response header.
         *
         * @param { string } url - Network address corresponding to the local JavaScript file, that is, the network address
         *     used when the service web page requests the server version of the file. The network address supports only the
         *     HTTP and HTTPS protocols and contains a maximum of 2048 characters. If the cache corresponding to the network
         *     address is invalid, the service web page requests the corresponding resource through the network.
         * @param { string | Uint8Array } script - Text content of the local JavaScript. The content cannot be empty.
         * @param { CacheOptions } cacheOptions - Whether to update the bytecode cache.
         * @returns { Promise<number> } - Promise used to return the error code for generating the bytecode cache. The value
         *     **0** indicates no error, and the value **-1** indicates an internal error.
         * @throws { BusinessError } 401 - Invalid input parameter.
         *    Possible causes: 1. Mandatory parameters are left unspecified.
         *    2. Incorrect parameter types. 3. Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *    The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<number>;
        /**
         * Set IP address for host name.
         *
         * @param { string } hostName - Which host name to be resolved.
         * @param { string } address - Resolved IP address.
         * @param { number } aliveTime - The validity seconds for resolve cache.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static setHostIP(hostName: string, address: string, aliveTime: number): void;
        /**
         * Clear the host name IP address.
         *
         * @param { string } hostName - Which host name to be cleared.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static clearHostIP(hostName: string): void;
        /**
         * Warmup the registered service worker associated the url.
         *
         * @param { string } url - The url.
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2048. [since 12 - 21]
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2*1024*1024. [since 22]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static warmupServiceWorker(url: string): void;
        /**
         * Injects local offline resources to the memory cache to improve the initial page startup speed.
         *
         * Resources in the memory cache are automatically managed by the ArkWeb engine. When the injected resources are
         * excessive and cause significant memory pressure, the engine will automatically release unused resources. It is
         * advisable to avoid injecting a large number of resources into the memory cache.
         *
         * Under normal circumstances, the validity period of the resources is controlled by the provided Cache-Control or
         * Expires response header, with a default validity period of 86,400 seconds, which is one day.
         *
         * The MIME type of the resources is configured through the provided Content-Type response header. The Content-Type
         * must comply with standards; otherwise, the resources cannot be used correctly. For resources of type MODULE_JS, a
         * valid MIME type must be provided. For other types, the MIME type is optional.
         *
         * Resources injected in this mode can be loaded only through HTML tags. If a **script** tag on the web page uses
         * the **crossorigin** attribute, the **Cross-Origin** response header must be set in the **responseHeaders**
         * parameter of the API. The value for this header should be **anonymous** or **use-credentials**.
         *
         * After **webview.WebviewController.SetRenderProcessMode(webview.RenderProcessMode.MULTIPLE)** is called, the
         * application starts the multi-rendering process mode. This API does not take effect in this scenario.
         *
         * @param { Array<OfflineResourceMap> } resourceMaps - Configuration object for local offline resources. A maximum
         *     of 30 resources can be injected in a single call, with a maximum size of 10 MB per individual resource.
         * @throws { BusinessError } 401 - Parameter error.
         *    Possible causes: 1. Mandatory parameters are left unspecified.
         *    2. Incorrect parameter types. 3. Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *    The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2048. [since 12 - 21]
         * @throws { BusinessError } 17100002 - URL error. The webpage corresponding to the URL is invalid, or the URL
         *     length exceeds 2\*1024\*1024. [since 22]
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void;
        /**
         * Enable the ability to block Ads, disabled by default.
         *
         * @param { boolean } enable {@code true} Enable Ads block; {@code false} otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Parameter string is too long. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        enableAdsBlock(enable: boolean): void;
        /**
         * Get whether Ads block is enabled.
         *
         * @returns { boolean } True if the ability of AdsBlock is enabled; else false.
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        isAdsBlockEnabled(): boolean;
        /**
         * Get whether Ads block is enabled for current Webpage.
         *
         * @returns { boolean } True if the ability of AdsBlock is enabled for current Webpage; else false.
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        isAdsBlockEnabledForCurPage(): boolean;
        /**
         * Obtains the ID of the surface corresponding to ArkWeb. The ID can be used to capture a screenshot of the web
         * page.
         *
         * > **NOTE**
         * >
         * > This API is valid only when the **Web** component rendering mode is **ASYNC_RENDER**. The value of
         * > **getSurfaceId** can be obtained only after the **Web** component is initialized.
         *
         * @returns { string } ID of the surface held by ArkWeb.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        getSurfaceId(): string;
        /**
         * Set the URL trust list for the ArkWeb.
         * When the URL trust list has been set, only the URLs in the list can be accessed.
         *
         * @param { string } urlTrustList - the URL trust list in JSON format.
         *     An empty string means that all URLs are allowed to access.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         * <br>2. Parameter string is too long. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        setUrlTrustList(urlTrustList: string): void;
        /**
         * Sets the URL trust list for the ArkWeb.
         *
         * <p><strong>API Note</strong>:<br>
         * When the URL trust list is set, only the URLs in the list can be accessed.
         *
         * Example of the urlTrustList:
         *
         * {
         *   "UrlPermissionList": [
         *     {
         *       "scheme": "https",
         *       "host": "www.example1.com",
         *       "port": 443,
         *       "path": "pathA/pathB"
         *     },
         *     {
         *       "scheme": "http",
         *       "host": "*.example2.com",
         *       "port": 80,
         *       "path": "test1/test2/test3"
         *     }
         *   ]
         * }
         * </p>
         *
         * @param { string } urlTrustList - The URL trust list in JSON format.
         *     An empty string means all URLs are allowed.
         * @param { boolean } allowOpaqueOrigin - If true, loading of opaque origin URLs (e.g., javascript, data) is
         *     allowed. If false, it is not allowed.
         * @param { boolean } supportWildcard - If true, wildcard matching is supported (e.g., *.example.com matches all
         *     subdomains). If false, wildcard matching is not supported.
         * @throws { BusinessError } 401 Parameter error, possible causes:
         *     1. Mandatory parameters are left unspecified
         *     2. JSON string exceeds 10MB limit
         *     3. JSON parsing failed (syntax errors, etc.)
         *     4. UrlPermissionList field is missing
         *     5. URL rule validation failed:
         *        - scheme must be http or https
         *        - host cannot be empty
         *        - port must be between 0-65535
         *        - path length cannot exceed 65536 characters
         * @throws { BusinessError } 17100001 - Initialization error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 24
         */
        setUrlTrustList(urlTrustList: string, allowOpaqueOrigin: boolean, supportWildcard: boolean): void;
        /**
         * Sets a path list. When a file protocol accesses resources in the path list, it can access the local files across
         * domains. In addition, when a path list is set, the file protocol can access only the resources in the path list.
         * The behavior of {@link fileAccess} will be overwritten by that of this API.
         *
         * The paths in the list must be any of the following(sub path and module name must be provided):
         *
         * 1. The path of subdirectory of the application file directory, like "/data/storage/el2/base/files/example"
         * or "/data/storage/el2/base/haps/entry/files/example".
         * The application file directory is obtained using Context.filesDir in the Ability Kit.
         * 2. The path of application resource directory or its subdirectory, like "/data/storage/el1/bundle/entry/resource/resfile"
         * or "/data/storage/el1/bundle/entry/resource/resfile/example".
         * The application resource directory is obtained from Context.resourceDir in the Ability Kit.
         *
         * If a path in the list is not of the preceding paths, error code 401 is reported and the path list fails
         * to be set. When the path list is set to empty, the accessible files for the file protocol are subject to
         * the behavior of the {@link fileAccess}.
         *
         * @param { Array<string> } pathList - The path list allow universal access.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified.
         *     <br>2. Parameter string is too long.
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        setPathAllowingUniversalAccess(pathList: Array<string>): void;
        /**
         * Trim memory by different memory pressure level.
         *
         * @param { PressureLevel } level - The memory pressure level for the ArkWeb.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified.
         *     <br>2. Parameter string is too long.
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 14
         */
        static trimMemoryByPressureLevel(level: PressureLevel): void;
        /**
         * Enable the BackForwardCache and indicate features that are allowed to enter BackForwardCache.
         * Default is disabled.
         *
         * @param { BackForwardCacheSupportedFeatures } features - The features that supports BackForwardCache.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void;
        /**
         * Configure the BackForwardCache.
         *
         * @param { BackForwardCacheOptions } options - The configuration of BackForwardCache.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        setBackForwardCacheOptions(options: BackForwardCacheOptions): void;
        /**
         * Obtains the current scrolling offset (including the over-scrolling offset) of the web page.
         *
         * @returns { ScrollOffset } Current scrolling offset (including the over-scrolling offset) of the web page.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 13
         */
        getScrollOffset(): ScrollOffset;
        /**
         * Scrolls the page by the specified amount and returns value to indicate whether the scrolling is successful.
         *
         * @param { number } deltaX - Amount to scroll by along the x-axis. The positive direction is rightward.<br>Unit: vp
         * @param { number } deltaY - Amount to scroll by along the y-axis. The positive direction is downward.<br>Unit: vp
         * @returns { boolean } Whether the current web page can be scrolled. The value **true** indicates that the current
         *     web page can be scrolled, and the value **false** indicates the opposite.
         *     <br>Default value: **false**.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        scrollByWithResult(deltaX: number, deltaY: number): boolean;
        /**
         * Obtains the element information of the area being clicked last time.
         *
         * @returns { HitTestValue } Element information of the area being clicked.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 18
         */
        getLastHitTest(): HitTestValue;
        /**
         * Obtains the current scrolling offset of the web page (excluding the over-scrolling offset).
         *
         * @returns { ScrollOffset } Current scrolling offset of the web page (excluding the over-scrolling offset).
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        getPageOffset(): ScrollOffset;
        /**
         * Set the default User-Agent for the application.
         *
         * <p><strong>API Note</strong>:<br>
         * Unlike setCustomUserAgent, which only takes effect in the current web context, the
         * priority for pages loaded in the web is as follows:
         * 1. The User-Agent set by setCustomUserAgent is used first.
         * 2. If not set, it will check whether a specific User-Agent has been
         * assigned to the current page via setUserAgentForHosts.
         * 3. If no specific User-Agent is assigned, the application will fall back
         * to using the User-Agent set by setAppCustomUserAgent.
         * 4. If the app's default User-Agent is also not specified, the web's default
         * User-Agent will be used as the final fallback.
         * </p>
         *
         * @param { string } userAgent - The User-Agent string.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        static setAppCustomUserAgent(userAgent: string): void;
        /**
         * Set the User-Agent to be used for specified hosts, with a maximum of 20,000 hosts.
         *
         * <p><strong>API Note</strong>:<br>
         * Setting the same host list multiple times for the same User-Agent will override
         * the previous settings. That is, if you want to cancel certain hosts from using
         * the specified User-Agent, you need to reset the host list for that User-Agent.
         * </p>
         *
         * @param { string } userAgent - The User-Agent string.
         * @param { Array<string> } hosts - The hosts to which the User-Agent apply.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        static setUserAgentForHosts(userAgent: string, hosts: Array<string>): void;
        /**
         * Enable the UserAgent Client Hints.
         *
         * @param { boolean } enabled - UserAgent Client Hints will enabled when set true.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 24
         */
        static setUserAgentClientHintsEnabled(enabled: boolean): void;
        /**
         * Get if the UserAgent Client Hints enabled.
         *
         * @returns { boolean } If UserAgent Client Hints was enabled.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 24
         */
        static getUserAgentClientHintsEnabled(): boolean;
        /**
         * Sets the User-Agent metadata corresponding to the User-Agent.
         *
         * <p><strong>API Note</strong>:<br>
         * This User-Agent metadata will be used to populate the User-Agent client hints, They can provide the client's
         * branding and version information, the underlying  operating system's branding and major version, as well as
         * details about the underlying device.
         *
         * The User-Agent can be set with setCustomUserAgent or setAppCustomUserAgent or setUserAgentForHosts.
         *
         * If the UserAgentMetadata is not found according to the overridden User-Agent and the overridden User-Agent
         * contains the system default User-Agent, the system default value will be used.
         *
         * If the UserAgentMetadata is not found according to the overridden User-Agent but the overridden User-Agent
         * does not contain the system default User-Agent, only the low-entry User-Agent client hints will be generated.
         *
         * </p>
         *
         * @param { string } userAgent - The User-Agent string.
         * @param { UserAgentMetadata } metaData - The UserAgentMetadata for the userAgent.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 24
         */
        setUserAgentMetadata(userAgent: string, metaData: UserAgentMetadata): void;
        /**
         * Get the User-Agent metadata corresponding to the User-Agent.
         *
         * @param { string } userAgent - The UserAgent string.
         * @returns { UserAgentMetadata } The UserAgentMetadata for the userAgent.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 24
         */
        getUserAgentMetadata(userAgent: string): UserAgentMetadata;
        /**
         * Get whether webviewController is attached to a web component.
         * @returns { ControllerAttachState } the attach state of controller
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        getAttachState(): ControllerAttachState;
        /**
         * Register the callback for controller attach state change.
         *
         * @param { 'controllerAttachStateChange' } type the event of controller attach state change.
         * @param { Callback<ControllerAttachState> } callback Callback used to return the controller attach state.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        on(type: 'controllerAttachStateChange', callback: Callback<ControllerAttachState>): void;
        /**
         * Unregister the callback for controller attach state change.
         *
         * @param { 'controllerAttachStateChange' } type the event of controller attach state change.
         * @param { Callback<ControllerAttachState> } callback Callback used to return the controller attach state.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        off(type: 'controllerAttachStateChange', callback?: Callback<ControllerAttachState>): void;
        /**
         * Asynchronously waits for the WebViewController to be attached to the Web component. If the attachment is complete or times out,
         * a callback is triggered to return the current ControllerAttachState through a promise.
         *
         * @param { number } timeout - the wait timeout, if timeout reach, promise will return, the unit is millisecond.
         * @returns { Promise<ControllerAttachState> } Promise used to return the state of attach.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        waitForAttached(timeout: number): Promise<ControllerAttachState>;
        /**
         * Enables debugging of web contents.
         *
         * <p><strong>API Note</strong>:<br>
         * The port numbers from 0 to 1024 are prohibited. Ports less than 0 or greater than 65535 are considered invalid.
         * If an attempt is made to set these disabled or invalid ports, an exception will be thrown.
         * </p>
         *
         * @param { boolean } webDebuggingAccess {@code true} enables debugging of web contents; {@code false} otherwise.
         * @param { number } port Indicates the port of the devtools server. After the port is specified, a tcp server
         *     socket is created instead of a unix domain socket.
         * @throws { BusinessError } 17100023 - The port number is not within the allowed range.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        static setWebDebuggingAccess(webDebuggingAccess: boolean, port: number): void;
        /**
         * Gets the loading progress for the current page.
         *
         * @returns { number } The loading progress for the current page.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        getProgress(): number;
        /**
         * Sets the bottom avoidance height of the visible viewport on the web page.
         *
         * > **NOTE**
         * >
         * > - The valid value range of **avoidHeight** is [0, height of the **Web** component]. Values outside this range
         * > are adjusted to the nearest boundary.
         * >
         * > - When a non-zero value is specified for **avoidHeight**, the position and size of the **Web** component remain
         * > unchanged, but the visible viewport shift upwards by the specified height, lifting the web page content by the
         * > **avoidHeight**. This API is used to customize the avoidance area at the bottom of a web page. It is not
         * > recommended that this API be used when the editable area of the web page is tapped to pull up the keyboard. If
         * > this API is used in this scenario, the keyboard avoidance mode is set to **OVERLAYS_CONTENT**.
         * >
         * > - When the height of this API is set to **0**, the web page content can be restored, and the keyboard avoidance
         * > mode is specified by
         * > [keyboardAvoidMode()](docroot://reference/apis-arkweb/arkts-basic-components-web-attributes.md#keyboardavoidmode12)
         * > .
         *
         * @param { number } avoidHeight - Bottom avoidance height of the visible viewport on the web page.<br>Unit: vp.<br>
         *     Value range: [0, height of the **Web** component]<br>If the value is less than 0, the value **0** is used. If
         *     the value is greater than the height of the **Web** component, the height of the **Web** component is used.
         * @throws { BusinessError } 17100001 - Init error. The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        avoidVisibleViewportBottom(avoidHeight: number): void;
        /**
         * Obtains the prediction information about blankless loading (for details, see
         * [BlanklessInfo]{@link @ohos.web.webview:webview.BlanklessInfo}) and starts to generate the loading transition
         * frame. The application determines whether to enable blankless loading based on the information. This API must be
         * used together with the [setBlanklessLoadingWithKey]{@link webview.WebviewController#setBlanklessLoadingWithKey}
         * API before the page loading API is triggered or in **onLoadIntercept**, and after the **WebViewController** is
         * bound to the **Web** component.
         *
         * > **NOTE**
         * >
         * > - The default size of the persistent cache capacity is 30 MB (about 30 pages). You can set the cache capacity
         * > by calling [setBlanklessLoadingCacheCapacity]{@link webview.WebviewController#setBlanklessLoadingCacheCapacity}
         * > . For details, see the description of this API. When the maximum capacity is exceeded, the cache is updated
         * > based on the Least Recently Used (LRU) mechanism. The persistent cache data that has been stored for more than
         * > seven days is automatically cleared. After the cache is cleared, the optimization effect appears when the page
         * > is loaded for the third time.
         * >
         * > - If the snapshot similarity (**similarity** in [BlanklessInfo]{@link @ohos.web.webview:webview.BlanklessInfo})
         * > is extremely low, check whether the **key** value is correct.
         * >
         * > - After this API is called, page loading snapshot detection and transition frame generation calculation are
         * > enabled, which generates certain resource overhead.
         * >
         * > - Blankless loading consumes certain resources, which depends on the resolution of the **Web** component. When
         * > the width and height of the resolution are respectively **w** and **h**, the peak memory usage increases by
         * > about **12 × w × h** B in the page-opening phase. After the page is opened, the memory is reclaimed, which does
         * > not affect the stable memory usage. When the size of the solid-state application cache is increased, the
         * > increased cache of each page is about **w × h/10** B and the cache is located in the application cache.
         * >
         * > - Add the **ohos.permission.INTERNET** and **ohos.permission.GET_NETWORK_INFO** permissions to **module.json5**
         * > . For details, see
         * > [Declaring Permissions in the Configuration File](docroot://security/AccessToken/declare-permissions.md#declaring-permissions-in-the-configuration-file).
         *
         * @param { string } key  Key value that uniquely identifies the page.<br>The value cannot be empty and can contain
         *     a maximum of 2048 characters.<br>Invalid values do not take effect.
         * @returns { BlanklessInfo } Prediction information about blankless loading, including the first screen similarity
         *     and first screen loading duration. The application determines whether to enable blankless loading based on
         *     the prediction information.
         * @throws { BusinessError } 801 This functionality is not supported.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        getBlanklessInfoWithKey(key: string): BlanklessInfo;
        /**
         * Sets whether to enable blankless loading. This API must be used together with
         * [getBlanklessInfoWithKey]{@link webview.WebviewController#getBlanklessInfoWithKey}.
         *
         * > **NOTE**
         * >
         * > - This API must be called after the page loading API is triggered. Other restrictions are the same as those of
         * > [getBlanklessInfoWithKey]{@link webview.WebviewController#getBlanklessInfoWithKey}.
         * >
         * > - The page must be loaded in the component that calls this API.
         * >
         * > - When the similarity is low, the system will deem the scene change too abrupt and frame insertion will fail.
         * >
         * > - Add the **ohos.permission.INTERNET** and **ohos.permission.GET_NETWORK_INFO** permissions to **module.json5**
         * > . For details, see
         * > [Declaring Permissions in the Configuration File](docroot://security/AccessToken/declare-permissions.md#declaring-permissions-in-the-configuration-file).
         *
         * @param { string } key  Key value that uniquely identifies the page. This value must be the same as the **key**
         *     value of the **getBlanklessInfoWithKey** API.<br>The value cannot be empty and can contain a maximum of 2048
         *     characters.<br>When an invalid value is set, the error code **WebBlanklessErrorCode** is returned, and the
         *     API does not take effect.
         * @param { boolean } is_start  Whether to enable frame interpolation. The value **true** means to enable frame
         *     interpolation, and **false** means the opposite.<br>If **undefined** or **null** is passed in, the value is
         *     **false**.
         * @returns { WebBlanklessErrorCode } Whether the API is successfully called. For details, see
         *     [WebBlanklessErrorCode]{@link @ohos.web.webview:webview.WebBlanklessErrorCode}.
         * @throws { BusinessError } 801 This functionality is not supported.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        setBlanklessLoadingWithKey(key: string, is_start: boolean): WebBlanklessErrorCode;
        /**
         * Triggers frame interpolation and sets frame interpolation parameters. This API must be used in pair with the
         * getBlanklessInfoWithKey API.
         *
         * Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.
         *
         * @param { string } key - Key value that uniquely identifies the current page.
         *     <br>Value range: (0, 2048]
         *     <br>The key value must be the same as that of getBlanklessInfoWithKey.
         * @param { BlanklessLoadingParam } param - The blankless loading parameter.
         *     <br>None
         * @returns { WebBlanklessErrorCode } WebBlanklessErrorCode.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 23
         */
        setBlanklessLoadingWithParams(key: string, param: BlanklessLoadingParam): WebBlanklessErrorCode;
        /**
         * Clears the blankless loading cache of the page with a specified key value.
         *
         * In an applet or web application, when the content changes significantly during page loading, an obvious scene
         * change may occur. If you are concerned about this change, you can use this API to clear the page cache.
         *
         * > **NOTE**
         * >
         * > - After the page is cleared, the optimization effect appears when the page is loaded for the third time.
         *
         * @param { Array<string> } [keys] Key value list on the pages using the blankless optimization solution. The
         *     **key** value has been specified in
         *     [getBlanklessInfoWithKey]{@link webview.WebviewController#getBlanklessInfoWithKey}.<br>Default value: key
         *     list of all pages cached by the blankless optimization solution.<br>Valid value range: The key length cannot
         *     exceed 2048 characters, and the number of keys must be less than or equal to 100. The key value is the same
         *     as that input to the **Web** component during page loading.<br>Invalid value setting behavior: If
         *     **undefined** or **null** is passed, error code **401** is thrown. If the key length exceeds 2048, the key
         *     does not take effect. If the key length exceeds 100, the first 100 values are used. If the key is empty, the
         *     default value is used.
         * @throws { BusinessError } 801 This functionality is not supported.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        static clearBlanklessLoadingCache(keys?: Array<string>): void;
        /**
         * Sets the persistent cache capacity of the blankless loading solution and returns the value that takes effect. If
         * the API is not explicitly called, the default cache capacity is 30 MB. When this limit is exceeded, transition
         * frames that are not frequently used are eliminated.
         *
         * @param { number } capacity Persistent cache capacity, in MB. The maximum value is 100 MB.<br>The value ranges
         *     from 0 to 100. If this parameter is set to **0**, no cache capacity is available and the functionality is
         *     disabled globally.<br>When a value less than 0 is set, the value **0** takes effect. When a value greater
         *     than 100 is set, the value **100** takes effect.
         * @returns { number } Effective value that ranges from 0 MB to 100 MB.
         *     <br>When a value less than 0 is set, the value **0** takes effect. When a value greater than 100 is set, the value
         *     **100** takes effect.
         * @throws { BusinessError } 801 This functionality is not supported.
         * @static
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        static setBlanklessLoadingCacheCapacity(capacity: number): number;
        /**
          * Get whether default error page feature is enabled.
          *
          * @returns  { boolean } -  True if enable the default error page feature; else false.
          * @throws { BusinessError } 17100001 - Init error.
          *                           The WebviewController must be associated with a Web component.
          * @syscap SystemCapability.Web.Webview.Core
          * @since 20
          */
        getErrorPageEnabled(): boolean;
        /**
          * Set whether enable the error page. onOverrideErrorPage will be triggered when the page error.
          *
          * @param { boolean } enable - Whether to enable the default error page feature.
          * @throws { BusinessError } 17100001 - Init error.
          *                           The WebviewController must be associated with a Web component.
          * @syscap SystemCapability.Web.Webview.Core
          * @since 20
          */
        setErrorPageEnabled(enable: boolean): void;
        /**
         * Set whether to enable error page. onOverrideErrorPage will be triggered when the page error.
         *
         * @param { boolean } enable - Whether enable error page.
         * @param { boolean } includeSubframe - If true, error page is displayed in iframe
         *     when a subframe fails to load.
         * @throws { BusinessError } 17100001 - Init error.
         *                           The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        setErrorPageEnabled(enable: boolean, includeSubframe: boolean): void;
        /**
         * Get whether default error page feature is enabled for subframes.
         *
         * @returns { boolean } - True if the default error page function of the subframe
         *     is enabled; Otherwise, the value is false.
         * @throws { BusinessError } 17100001 - Init error.
         *     The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        getSubframeErrorPageEnabled(): boolean;
        /**
         * After enable PrivateNetworkAccess feature, ArkWeb will send a CORS preflight request before issuing any
         * sub-resource private network requests to request explicit permission from the target server. After disable
         * PrivateNetworkAccess, ArkWeb will no longer check whether the private network request is legitimate.
         * By default, PrivateNetworkAccess feature is enabled.
         *
         * @param { boolean } enable - {@code true} enable the private network acccess check; {@code false} otherwise.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        static enablePrivateNetworkAccess(enable: boolean): void;
        /**
         * Get whether PrivateNetworkAccess is enabled.
         *
         * @returns {boolean} True is enable the ability to check private network access else false.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        static isPrivateNetworkAccessEnabled(): boolean;
        /**
         * Sets the destroy mode of the Web component. The destroy mode of the Web component
         * affects the time when web kernel resources, such as the JavaScript running context
         * and rendering context, are released. The default value is WebDestroyMode.NORMAL_MODE
         * (normal mode), indicating that the system determines the destroy time. You can set
         * WebDestroyMode.FAST_MODE (fast mode) to destroy resources immediately, improving
         * performance in specific scenarios.
         * @param { WebDestroyMode } mode web destroy mode, default NORMAL_MODE.
         * @static
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        static setWebDestroyMode(mode: WebDestroyMode): void;
        /**
         * Configure whether to enable automatic pre-connection to high-frequency URLs accessed during the application's
         * previous lifecycle after web initialization.
         *
         * @param { boolean } enabled - Enable if true, disable if false.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 21
         */
        static setAutoPreconnect(enabled: boolean): void;
        /**
         * ‌Retrieve whether the automatic pre-connection feature is enabled‌.
         *
         * @returns { boolean } Return true if enabled, false if disabled.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 21
         */
        static isAutoPreconnectEnabled(): boolean;
        /**
         * Set the site isolation mode.
         *
         * @param { SiteIsolationMode } mode The site isolation mode of the application,
         *     default value depends on different devices type.
         * @throws { BusinessError } 17100001 - Init error. Possible causes:
         *     1. Site Isolation mode is already set by the developer.
         *     2. Site Isolation mode cannot be strict in single-render-process mode.
         *     3. Site Isolation mode cannot be changed while Secure Shield mode is active.
         * @static
         * @syscap SystemCapability.Web.Webview.Core
         * @since 21
         */
        static setSiteIsolationMode(mode: SiteIsolationMode): void;
        /**
         * Queries the currently effective site isolation mode.
         *
         * @returns { SiteIsolationMode } The site isolation mode of the application.
         * @static
         * @syscap SystemCapability.Web.Webview.Core
         * @since 21
         */
        static getSiteIsolationMode(): SiteIsolationMode;
        /**
         * Set web engine socket idle timeout.
         *
         * <p><strong>API Note</strong>:<br>
         * Unit: seconds, minimum 30s, maximum 5 minutes. If not set, the default is five minutes.
         * </p>
         *
         * @param { number } timeout - Socket idle timeout.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 21
         */
        static setSocketIdleTimeout(timeout: number): void;
        /**
         * Set the behavior mode of the soft keyboard. If this API is not explicitly called, the system automatically
         * hides or shows the soft keyboard when the Web component loses or gains focus, or when its status becomes
         * inactive or active.
         *
         * @param { WebSoftKeyboardBehaviorMode } mode - The WebSoftKeyboardBehaviorMode of this web.
         * @throws { BusinessError } 17100001 - Init error. The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 22
         */
        setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void;
        /**
         * Sets the global scrollbar mode in the web page. When this API is not explicitly called,
         * [ScrollbarMode.OVERLAY_LAYOUT_SCROLLBAR]{@link @ohos.web.webview:webview.ScrollbarMode} is used by default,
         * indicating that the scroll bar is not always displayed.
         *
         * > **NOTE**
         * >
         * > - You can set whether to always display the web scrollbar of the current application based on the scrollbar
         * > mode.
         * >
         * > - If the
         * > [forceDisplayScrollBar]{@link @ohos.web.WebAttribute#forcedisplayscrollbar}
         * > API is set at the same time as this API, the setting of **forceDisplayScrollBar** does not take effect.
         * >
         * > - This API must be called before WebViewController is bound to a **Web** component.
         *
         * @param { ScrollbarMode } scrollbarMode - Scroll bar mode.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        static setScrollbarMode(scrollbarMode: ScrollbarMode): void;
        /**
         * Enable the application disable some features such as PDFViewer to enhance the security level of web application
         *
         * @param { SecurityParams } securityParams - The parameters means which supported option or item will be disabled.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        static enableAdvancedSecurityMode(securityParams: SecurityParams): void;
        /**
         * Resumes microphone capture on the current web page. Before using the microphone , add the
         * **ohos.permission.MICROPHONE** permission to **module.json5**. For details about how to add the permission, see
         * [Declaring Permissions in the Configuration File](docroot://security/AccessToken/declare-permissions.md).
         *
         * @throws { BusinessError } 17100001 - Init error. The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        resumeMicrophone(): void;
        /**
         * Pauses microphone capture on the current web page.
         *
         * @throws { BusinessError } 17100001 - Init error. The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        pauseMicrophone(): void;
        /**
         * Stops microphone capture on the current web page.
         *
         * @throws { BusinessError } 17100001 - Init error. The WebviewController must be associated with a Web component.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        stopMicrophone(): void;
        /**
         * Asynchronously executes AI page command operations.
         *
         * @param { string } command - JSON-formatted command parameter.
         * @returns { Promise<string> } A promise that resolves after the command is executed.
         *                              This JSON-formatted value will be the result of command execution.
         * @throws { BusinessError } 17100001 - Init error.
         *                           The WebviewController must be associated with a Web component.
         * @throws { BusinessError } 17100024 - Command format error.
         *                           The command parameter does not conform to the JSON format requirements.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        executeAIPageCommand(command: string): Promise<string>;
    }
    /**
     * Defines the state for download.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 18]
     * @atomicservice
     * @since 11
     */
    enum WebDownloadState {
        /**
         * The web download is in progress.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        IN_PROGRESS = 0,
        /**
         * The web download has been completed.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        COMPLETED,
        /**
         * The web download was canceled.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        CANCELED,
        /**
         * The web download was interrupted.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        INTERRUPTED,
        /**
         * The web download is pending.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        PENDING,
        /**
         * The web download has been paused.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        PAUSED,
        /**
         * Unknown state.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        UNKNOWN
    }
    /**
     * Defines the error code for download.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 18]
     * @atomicservice
     * @since 11
     */
    enum WebDownloadErrorCode {
        /**
         * Unknown error.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        ERROR_UNKNOWN = 0,
        /**
         * Generic file operation failure.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        FILE_FAILED = 1,
        /**
         * The file cannot be accessed due to certain restrictions.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        FILE_ACCESS_DENIED = 2,
        /**
         * There is not enough disk space.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        FILE_NO_SPACE = 3,
        /**
         * The file name is too long.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        FILE_NAME_TOO_LONG = 5,
        /**
         * The file is too large.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        FILE_TOO_LARGE = 6,
        /**
         * Some temporary problems occurred, such as not enough memory, files in use, and too many files open at the same time.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        FILE_TRANSIENT_ERROR = 10,
        /**
         * The file is blocked from accessing because of some local policy.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        FILE_BLOCKED = 11,
        /**
         * When trying to resume the download, Found that the file is not long enough, maybe the file no longer exists.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        FILE_TOO_SHORT = 13,
        /**
         * Hash mismatch.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        FILE_HASH_MISMATCH = 14,
        /**
         * The file already exists.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        FILE_SAME_AS_SOURCE = 15,
        /**
         * Generic network error.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        NETWORK_FAILED = 20,
        /**
         * The network operation timed out.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        NETWORK_TIMEOUT = 21,
        /**
         * The network was disconnected.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        NETWORK_DISCONNECTED = 22,
        /**
         * Server down.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        NETWORK_SERVER_DOWN = 23,
        /**
         * Invalid network requests，may redirect to unsupported scheme or an invalid URL.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        NETWORK_INVALID_REQUEST = 24,
        /**
         * The server returned a generic error.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        SERVER_FAILED = 30,
        /**
         * The server does not support range requests.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        SERVER_NO_RANGE = 31,
        /**
         * The server does not have the requested data.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        SERVER_BAD_CONTENT = 33,
        /**
         * The server does not allow the file to be downloaded.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        SERVER_UNAUTHORIZED = 34,
        /**
         * Server certificate error.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        SERVER_CERT_PROBLEM = 35,
        /**
         * Server access forbidden.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        SERVER_FORBIDDEN = 36,
        /**
         * Server unreachable.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        SERVER_UNREACHABLE = 37,
        /**
         * The received data does not match content-length.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        SERVER_CONTENT_LENGTH_MISMATCH = 38,
        /**
         * An unexpected cross-origin redirect happened.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        SERVER_CROSS_ORIGIN_REDIRECT = 39,
        /**
         * User cancel.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        USER_CANCELED = 40,
        /**
         * User shut down the application.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        USER_SHUTDOWN = 41,
        /**
         * Application crash.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        CRASH = 50
    }
    /**
     * Represents a download task, You can use this object to operate the corresponding download task.
     * Currently, the maximum length of the download file name supported by **WebDownloadItem** is 255 bytes.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 18]
     * @atomicservice
     * @since 11
     */
    class WebDownloadItem {
        /**
         * Get guid.
         *
         * @returns { string } - Returns the download's guid.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        getGuid(): string;
        /**
         * Get current speed, in bytes per second.
         *
         * @returns { number } - Returns the current download speed.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        getCurrentSpeed(): number;
        /**
         * Get percent complete.
         *
         * @returns { number } - Returns -1 if progress is unknown. 100 if the download is already complete.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        getPercentComplete(): number;
        /**
         * Get total bytes.
         *
         * @returns { number } - Returns the total bytes received, -1 if the total size is unknown.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        getTotalBytes(): number;
        /**
         * Get state of the web download.
         *
         * @returns { WebDownloadState } - Returns the current download state.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        getState(): WebDownloadState;
        /**
         * Get last error code of the web download.
         *
         * @returns { WebDownloadErrorCode } - Returns the last error code.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        getLastErrorCode(): WebDownloadErrorCode;
        /**
         * Get http method of the web download request.
         *
         * @returns { string } - Returns the http request method.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        getMethod(): string;
        /**
         * Get mime type of the web download.
         *
         * @returns { string } - Returns the mimetype.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        getMimeType(): string;
        /**
         * Get url of the web download request.
         *
         * @returns { string } - Returns the url.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        getUrl(): string;
        /**
         * Get suggested file name of the web download request.
         *
         * @returns { string } - Returns the suggested file name.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        getSuggestedFileName(): string;
        /**
         * Start the web download.
         * <p><strong>API Note</strong>:<br>
         * This API must be used in the **onBeforeDownload** callback of **WebDownloadDelegate**. If it is not called in
         * the callback, the download task remains in the PENDING state and is downloaded to a temporary directory. After
         * the target path is specified by **WebDownloadItem.start**, the temporary files are renamed to the target path
         * and the unfinished files are directly downloaded to the target path. If you do not want to download the file to
         * the temporary directory before invoking **WebDownloadItem.start**, you can call **WebDownloadItem.cancel** to
         * cancel the current download task and then call **WebDownloadManager.resumeDownload** to resume the task.
         * </p>
         *
         * @param { string } downloadPath - The content will be downloaded to this file.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
         *     <br>2. Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        start(downloadPath: string): void;
        /**
         * Cancel the web download.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        cancel(): void;
        /**
         * Pause the web download.
         *
         * @throws { BusinessError } 17100019 - The download task is not started yet.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        pause(): void;
        /**
         * Resume the web download.
         * Use WebDownloadManager.resumeDownload to resume deserialized downloads.
         * WebDownloadItem.resume is only used to resume the currently paused download.
         *
         * @throws { BusinessError } 17100016 - The download task is not paused.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        resume(): void;
        /**
         * Get received bytes.
         *
         * @returns { number } - Returns the received bytes.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        getReceivedBytes(): number;
        /**
         * Get full path of the web download.
         *
         * @returns { string } - Returns the full path of the download.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        getFullPath(): string;
        /**
         * Get the original url of the web download.
         *
         * @returns { string } - Returns the original url of the download.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getOriginalUrl(): string;
        /**
         * Get the referrer url of the web download.
         *
         * @returns { string } - Returns the referrer url of the download.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getReferrerUrl(): string;
        /**
         * Serialize web download to typed array.
         *
         * @returns { Uint8Array } - Returns the serialized data.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        serialize(): Uint8Array;
        /**
         * Deserialize web download from typed array.
         *
         * @param { Uint8Array } serializedData - The serialized data.
         * @returns { WebDownloadItem } - Deserialize the serialized data into a WebDownloadItem.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
         *     <br>2. Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        static deserialize(serializedData: Uint8Array): WebDownloadItem;
    }
    /**
     * The download state is notified through this delegate.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 18]
     * @atomicservice
     * @since 11
     */
    class WebDownloadDelegate {
        /**
         * Callback will be triggered before web download start.
         *
         * @param { Callback<WebDownloadItem> } callback - The callback of download will be start.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        onBeforeDownload(callback: Callback<WebDownloadItem>): void;
        /**
         * Callback will be triggered when web download is processing.
         *
         * @param { Callback<WebDownloadItem> } callback - The callback of download did update.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        onDownloadUpdated(callback: Callback<WebDownloadItem>): void;
        /**
         * Callback will be triggered when web download is completed.
         *
         * @param { Callback<WebDownloadItem> } callback - The callback of download did finish.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        onDownloadFinish(callback: Callback<WebDownloadItem>): void;
        /**
         * Callback will be triggered when web download is interrupted or canceled.
         *
         * @param { Callback<WebDownloadItem> } callback - The callback of download did fail.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        onDownloadFailed(callback: Callback<WebDownloadItem>): void;
    }
    /**
     * You can trigger download manually through this interface, or resume failed or canceled downloads.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 18]
     * @atomicservice
     * @since 11
     */
    class WebDownloadManager {
        /**
         * Set a delegate used to receive the progress of the download triggered from WebDownloadManager.
         *
         * @param { WebDownloadDelegate } delegate - Delegate used for download triggered from WebDownloadManager.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 18]
         * @atomicservice
         * @since 11
         */
        static setDownloadDelegate(delegate: WebDownloadDelegate): void;
        /**
         * Resume the canceled or failed download.
         *
         * @param { WebDownloadItem } webDownloadItem - Download that need to be resume.
         * @throws { BusinessError } 17100018 - No WebDownloadDelegate has been set yet.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 11
         */
        static resumeDownload(webDownloadItem: WebDownloadItem): void;
    }
    /**
     * The http body stream of the request.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    class WebHttpBodyStream {
        /**
         * Initialize data stream.
         *
         * @returns { Promise<void> } The promise of data stream is initialized.
         * @throws { BusinessError } 17100022 - Failed to initialize the HTTP body stream.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        initialize(): Promise<void>;
        /**
         * Read the data stream to the buffer. Unit: bytes.
         *
         * @param { number } size - Read size.
         * @returns { Promise<ArrayBuffer> } Read array buffer of result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        read(size: number): Promise<ArrayBuffer>;
        /**
         * Get the total size of the data stream. When data is chunked, always return zero. Unit: bytes.
         *
         * @returns { number } Return size of data stream size.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        getSize(): number;
        /**
         * Get the current position of the data stream. Unit: bytes.
         *
         * @returns { number } Return position in post data stream.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        getPosition(): number;
        /**
         * Whether data stream is chunked.
         *
         * @returns { boolean } Whether data stream is chunked.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        isChunked(): boolean;
        /**
         * Whether all data stream has been consumed. For chunked uploads,
         * returns false until the first read attempt.
         *
         * @returns { boolean } Whether data stream has been consumed.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        isEof(): boolean;
        /**
         * Returns true if the upload data in the stream is entirely in memory, and all read requests will succeed
         * synchronously. Expected to return false for chunked requests.
         *
         * @returns { boolean } Whether the data stream is in memory.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        isInMemory(): boolean;
    }
    /**
     * Defines the resource type of request.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 12
     */
    enum WebResourceType {
        /**
         * Top level page.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        MAIN_FRAME = 0,
        /**
         * Frame or Iframe.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        SUB_FRAME = 1,
        /**
         * CSS stylesheet.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        STYLE_SHEET = 2,
        /**
         * External script.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        SCRIPT = 3,
        /**
         * Image (jpg/gif/png/etc).
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        IMAGE = 4,
        /**
         * Font.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        FONT_RESOURCE = 5,
        /**
         * Some other subresource. This is the default type if the actual type is unknown.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        SUB_RESOURCE = 6,
        /**
         * Object (or embed) tag for a plugin, or a resource that a plugin requested.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        OBJECT = 7,
        /**
         * Media resource.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        MEDIA = 8,
        /**
         * Main resource of a dedicated worker.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        WORKER = 9,
        /**
         * Main resource of a shared worker.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        SHARED_WORKER = 10,
        /**
         * Explicitly requested prefetch.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        PREFETCH = 11,
        /**
         * Favicon.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        FAVICON = 12,
        /**
         * XMLHttpRequest.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        XHR = 13,
        /**
         * Ping request for <a ping>/sendBeacon.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        PING = 14,
        /**
         * The main resource of a service worker.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        SERVICE_WORKER = 15,
        /**
         * Report of Content Security Policy violations.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        CSP_REPORT = 16,
        /**
         * Resource that a plugin requested.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        PLUGIN_RESOURCE = 17,
        /**
         * A main-frame service worker navigation preload request.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        NAVIGATION_PRELOAD_MAIN_FRAME = 19,
        /**
         * A sub-frame service worker navigation preload request.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        NAVIGATION_PRELOAD_SUB_FRAME = 20
    }
    /**
     * Defines the Web resource request used for scheme handler.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 23]
     * @atomicservice
     * @since 12
     */
    class WebSchemeHandlerRequest {
        /**
         * Gets request headers.
         *
         * @returns { Array<WebHeader> } Return the request headers.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        getHeader(): Array<WebHeader>;
        /**
         * Gets the request URL.
         *
         * @returns { string } Return the request URL.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        getRequestUrl(): string;
        /**
         * Get request method.
         *
         * @returns { string } Return the request method.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        getRequestMethod(): string;
        /**
         * Get referrer of request.
         *
         * @returns { string } Return referrer of request.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        getReferrer(): string;
        /**
         * Check whether the request is for getting the main frame.
         *
         * @returns { boolean } Whether request is main frame.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        isMainFrame(): boolean;
        /**
         * Check whether the request is associated with gesture.
         *
         * @returns { boolean } Whether request has user gesture.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        hasGesture(): boolean;
        /**
         * Get http body stream.
         *
         * @returns { WebHttpBodyStream | null } Return http body stream. If request has no http body stream, return null.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        getHttpBodyStream(): WebHttpBodyStream | null;
        /**
         * Get request's resource type.
         *
         * @returns { WebResourceType } Return the request's resource type.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        getRequestResourceType(): WebResourceType;
        /**
         * Gets the URL of frame which trigger this request.
         *
         * @returns { string } Return the URL of frame which trigger this request.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        getFrameUrl(): string;
    }
    /**
     * Defines the Web resource response used for scheme handler.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 23]
     * @atomicservice
     * @since 12
     */
    class WebSchemeHandlerResponse {
        /**
         * Constructor.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        constructor();
        /**
         * Set the resolved URL after redirects or changed as a result of HSTS.
         *
         * @param { string } url - Set response url for redirects.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        setUrl(url: string): void;
        /**
         * Get the resolved URL after redirects or changed as a result of HSTS.
         *
         * @returns { string } Return response url for redirects.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        getUrl(): string;
        /**
         * Set net error code.
         *
         * @param { WebNetErrorList } code - Set net error code.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        setNetErrorCode(code: WebNetErrorList): void;
        /**
         * Get net error code.
         *
         * @returns { WebNetErrorList } Return response error code.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        getNetErrorCode(): WebNetErrorList;
        /**
         * Set http status code.
         *
         * @param { number } code - Http status code.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        setStatus(code: number): void;
        /**
         * Get http status code.
         *
         * @returns { number } Return http status code.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        getStatus(): number;
        /**
         * Set status text.
         *
         * @param { string } text - Status text.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        setStatusText(text: string): void;
        /**
         * Get status text.
         *
         * @returns { string } Return http status text.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        getStatusText(): string;
        /**
         * Set mime type.
         *
         * @param { string } type - Mime type.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        setMimeType(type: string): void;
        /**
         * Get mime type.
         *
         * @returns { string } Return mime type of response.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        getMimeType(): string;
        /**
         * Set the response encoding.
         *
         * @param { string } encoding - Encoding.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        setEncoding(encoding: string): void;
        /**
         * Get the response encoding.
         *
         * @returns { string } Return encoding of response.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        getEncoding(): string;
        /**
         * Set response hander value by name.
         *
         * @param { string } name - Header name.
         * @param { string } value - Header value.
         * @param { boolean } overwrite - Whether to overwrite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        setHeaderByName(name: string, value: string, overwrite: boolean): void;
        /**
         * Get the header value by name from the response.
         *
         * @param { string } name - Header name.
         * @returns { string } Return header value by name.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        getHeaderByName(name: string): string;
    }
    /**
     * Used to intercept url requests. Response headers and body can be sent through
     * WebResourceHandler.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 23]
     * @atomicservice
     * @since 12
     */
    class WebResourceHandler {
        /**
         * Pass response headers to intercepted requests.
         *
         * @param { WebSchemeHandlerResponse } response - Set response header to intercept.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         * @throws { BusinessError } 17100021 - The resource handler is invalid.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        didReceiveResponse(response: WebSchemeHandlerResponse): void;
        /**
         * Pass response body data to intercepted requests.
         *
         * @param { ArrayBuffer } data - Set response body to intercept.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         * @throws { BusinessError } 17100021 - The resource handler is invalid.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        didReceiveResponseBody(data: ArrayBuffer): void;
        /**
         * Notify that this request should be finished and there is no more data available.
         *
         * @throws { BusinessError } 17100021 - The resource handler is invalid.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        didFinish(): void;
        /**
         * Notify that this request should be failed.
         *
         * @param { WebNetErrorList } code - Set response error code to intercept.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
         * @throws { BusinessError } 17100021 - The resource handler is invalid.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        didFail(code: WebNetErrorList): void;
        /**
         * Notify that this request should be failed.
         *
         * @param { WebNetErrorList } code - Set response error code to intercept.
         * @param { boolean } completeIfNoResponse - If completeIfNoResponse is true, when DidFailWithError is called, if
         *     DidReceiveResponse has not been called, a response is automatically
         *     constructed and the current request is terminated.
         * @throws { BusinessError } 17100101 - The errorCode is either ARKWEB_NET_OK or outside the range of error codes
         *     in WebNetErrorList.
         * @throws { BusinessError } 17100021 - The resource handler is invalid.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @since 20
         */
        didFail(code: WebNetErrorList, completeIfNoResponse: boolean): void;
    }
    /**
     * This class is used to intercept requests for a specified scheme.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @crossplatform [since 23]
     * @atomicservice
     * @since 12
     */
    class WebSchemeHandler {
        /**
         * Callback for handling the request.
         *
         * @param { function } callback - Callback of handling the request. If callback return false,
         *     it means no interception.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        onRequestStart(callback: (request: WebSchemeHandlerRequest, handler: WebResourceHandler) => boolean): void;
        /**
         * Callback when the request is completed.
         *
         * @param { Callback<WebSchemeHandlerRequest> } callback - Callback of request is completed.
         * @throws { BusinessError } 401 - Invalid input parameter.
         * @syscap SystemCapability.Web.Webview.Core
         * @crossplatform [since 23]
         * @atomicservice
         * @since 12
         */
        onRequestStop(callback: Callback<WebSchemeHandlerRequest>): void;
    }
    /**
     * Enumerates the playback statuses of the player, which is an input parameter of the
     * [handleStatusChanged]{@link @ohos.web.webview:webview.NativeMediaPlayerHandler.handleStatusChanged} API.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    enum PlaybackStatus {
        /**
         * Playing.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        PAUSED = 0,
        /**
         * Paused.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        PLAYING = 1
    }
    /**
     * Enumerates the network statuses of the player.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    enum NetworkState {
        /**
         * The player has not started downloading data.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        EMPTY = 0,
        /**
         * The player's network activity is idle. This could mean that the download of a media segment is complete, and the
         * player is waiting to start downloading the next segment.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        IDLE = 1,
        /**
         * The player is downloading media data.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        LOADING = 2,
        /**
         * A network error occurs.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        NETWORK_ERROR = 3
    }
    /**
     * Enumerates the cache states of the player.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    enum ReadyState {
        /**
         * There is no data cached.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        HAVE_NOTHING = 0,
        /**
         * Only media metadata is cached.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        HAVE_METADATA = 1,
        /**
         * Data up to the current playback position is cached.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        HAVE_CURRENT_DATA = 2,
        /**
         * Data beyond the current playback position is cached, but there might still be stutters during playback.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        HAVE_FUTURE_DATA = 3,
        /**
         * Sufficient data has been cached to ensure smooth playback.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        HAVE_ENOUGH_DATA = 4
    }
    /**
     * Enumerates the error types of the player.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    enum MediaError {
        /**
         * Network error.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        NETWORK_ERROR = 1,
        /**
         * Media format error.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        FORMAT_ERROR = 2,
        /**
         * Decoding error.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        DECODE_ERROR = 3
    }
    /**
     * Implements a **NativeMediaPlayerHandler** object used as a parameter of the
     * [CreateNativeMediaPlayerCallback]{@link @ohos.web.webview:webview.CreateNativeMediaPlayerCallback} callback. The
     * application uses this object to report the player status to the ArkWeb engine.
     *
     * > **NOTE**
     * >
     * > - The sample effect is subject to the actual device.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    interface NativeMediaPlayerHandler {
        /**
         * Called to notify the ArkWeb engine of the playback status of the player when the playback status changes.
         *
         * @param { PlaybackStatus } status - Player status.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleStatusChanged(status: PlaybackStatus): void;
        /**
         * Called to notify the ArkWeb engine of the volume of the player when the volume changes.
         *
         * @param { number } volume - Volume of the player. The value range is [0, 1.0].
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleVolumeChanged(volume: number): void;
        /**
         * Called to notify the ArkWeb engine of the muted status of the player when the muted status changes.
         *
         * @param { boolean } muted - Whether the player is muted.<br>The value **true** indicates that the player is muted,
         *     and **false** indicates the opposite.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleMutedChanged(muted: boolean): void;
        /**
         * Called to notify the ArkWeb engine of the playback rate of the player when the playback rate changes.
         *
         * @param { number } playbackRate - Playback rate. The value range is [0, +��).
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handlePlaybackRateChanged(playbackRate: number): void;
        /**
         * Called to notify the ArkWeb engine of the total duration of the media.
         *
         * @param { number } duration - Total duration of the media.<br>Unit: second. Value range: [0,+��)
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleDurationChanged(duration: number): void;
        /**
         * Called to notify the ArkWeb engine of the playback progress when the playback progress changes.
         *
         * @param { number } currentPlayTime - Current progress.<br>Unit: second. Value range: [0, duration]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleTimeUpdate(currentPlayTime: number): void;
        /**
         * Called to notify the ArkWeb engine of the buffer time when the buffer time changes.
         *
         * @param { number } bufferedEndTime - Duration of media data in the buffer.<br>Unit: second. Value range:
         *     [0, duration]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleBufferedEndTimeChanged(bufferedEndTime: number): void;
        /**
         * Called to notify the ArkWeb engine that the media playback ends.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleEnded(): void;
        /**
         * Called to notify the ArkWeb engine of the network status of the player when the network status changes.
         *
         * @param { NetworkState } state - Network status of the player.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleNetworkStateChanged(state: NetworkState): void;
        /**
         * Called to notify the ArkWeb engine of the cache status of the player when the cache status changes.
         *
         * @param { ReadyState } state - Cache status of the player.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleReadyStateChanged(state: ReadyState): void;
        /**
         * Called to notify the ArkWeb engine of the full screen status of the player when the full screen status changes.
         *
         * @param { boolean } fullscreen - Whether the player is in full screen.<br>The value **true** means that the player
         *     is in full screen, and **false** means the opposite.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleFullscreenChanged(fullscreen: boolean): void;
        /**
         * Called to notify the ArkWeb engine that the player enters the seek state.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleSeeking(): void;
        /**
         * Called to notify the ArkWeb engine that the seek operation is complete.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleSeekFinished(): void;
        /**
         * Called to notify the ArkWeb engine that an error occurs with the player.
         *
         * @param { MediaError } error - Error object type.
         * @param { string } errorMessage - Error message.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleError(error: MediaError, errorMessage: string): void;
        /**
         * Called to notify the ArkWeb engine of the video size of the player.
         *
         * @param { number } width - Video width, in pixels. Value range: [0,+��)
         * @param { number } height - Video height, in pixels. Value range: [0,+��)
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        handleVideoSizeChanged(width: number, height: number): void;
    }
    /**
     * Enumerates the suspension types of the player.
     * @enum {number}
     * @syscap SystemCapability.Web.Webview.Core
     * @since 12
     */
    enum SuspendType {
        /**
         * The page enters the BFCache.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        ENTER_BACK_FORWARD_CACHE = 0,
        /**
         * The page is displayed in the background.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        ENTER_BACKGROUND,
        /**
         * The page is automatically cleaned up by the system.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        AUTO_CLEANUP
    }
    /**
     * Instance of the API class between the web media player and the ArkWeb kernel.
     *
     * The ArkWeb kernel uses an object of this interface class to
     * control the player created by the application to take over web page media.
     *
     * > **NOTE**
     * >
     * > - The sample effect is subject to the actual device.
     *
     * @typedef NativeMediaPlayerBridge
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    interface NativeMediaPlayerBridge {
        /**
         * Updates the surface position information.
         *
         * @param { number } x - X coordinate of the surface relative to the **Web** component, Unit: px.
         * @param { number } Y coordinate of the surface relative to the **Web** component, Unit: px.
         * @param { number } width - Width of the surface, Unit: px.
         * @param { number } height - Height of the surface, Unit: px.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        updateRect(x: number, y: number, width: number, height: number): void;
        /**
         * Plays this video.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        play(): void;
        /**
         * Pauses playback.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        pause(): void;
        /**
         * Seeks to a specific time point in the media.
         *
         * @param { number } targetTime - Target time point, Unit: seconds.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        seek(targetTime: number): void;
        /**
         * Sets the playback volume.
         *
         * @param { number } volume - Playback volume.Value range: [0, 1.0].
         *  The value **0** indicates mute, and the value **1.0** indicates the maximum volume.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        setVolume(volume: number): void;
        /**
         * Sets the muted status.
         *
         * @param { boolean } muted - Whether to mute the player.
         *  The value **true** means to mute the player, and **false** means the opposite.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        setMuted(muted: boolean): void;
        /**
         * Sets the playback rate.
         *
         * @param { number } playbackRate - Playback rate.
         *  Value range: [0, 10.0]. The value **1** indicates the original speed of playback.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        setPlaybackRate(playbackRate: number): void;
        /**
         * Releases this player.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        release(): void;
        /**
         * Enables the player to enter full screen mode.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        enterFullscreen(): void;
        /**
         * Enables the player to exit full screen mode.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        exitFullscreen(): void;
        /**
         * Resumes the player and its status information.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        resumePlayer?(): void;
        /**
         * Suspends the player and save its status information.
         *
         * @param { SuspendType } type - Suspension type of the player.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        suspendPlayer?(type: SuspendType): void;
    }
    /**
     * Enumerates the media types.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    enum MediaType {
        /**
         * Video.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        VIDEO = 0,
        /**
         * Audio.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        AUDIO = 1
    }
    /**
     * Enumerates the media source types.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    enum SourceType {
        /**
         * URL.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        URL = 0,
        /**
         * Blob.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        MSE = 1
    }
    /**
     * Implements a **MediaSourceInfo** object to provide the information about the media source.
     *
     * > **NOTE**
     * >
     * > - The sample effect is subject to the actual device.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    class MediaSourceInfo {
        /**
         * Type of the media source.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        type: SourceType;
        /**
         * Address of the media source.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        source: string;
        /**
         * Format of the media source, which may be empty. You need to determine the format by yourself.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        format: string;
    }
    /**
     * Defines a rectangle.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 12
     */
    interface RectEvent {
        /**
         * X-axis coordinate of the upper left corner of the rectangle.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        x: number;
        /**
         * Y-axis coordinate of the upper left corner of the rectangle.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        y: number;
        /**
         * Width of the rectangle.
         *
         * Unit: px.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        width: number;
        /**
         * Height of the rectangle.
         *
         * Unit: px.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        height: number;
    }
    /**
     * Implements a **NativeMediaPlayerSurfaceInfo** object to provide the surface information used for same-layer
     * rendering [when the application takes over the media playback of the web page]
     * (docroot://reference/apis-arkweb/arkts-basic-components-web-attributes.md#enablenativemediaplayer12).
     *
     * > **NOTE**
     * >
     * > - The sample effect is subject to the actual device.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    class NativeMediaPlayerSurfaceInfo {
        /**
         * Surface ID, which is the **psurfaceid** of the native image used for rendering at the same layer.
         * For details, see [NativeEmbedDataInfo](./arkts-basic-components-web-i.md#nativeembeddatainfo11).
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        id: string;
        /**
         *  Position of the surface.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        rect: RectEvent;
    }
    /**
     * Enumerates how the player preloads media data.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    enum Preload {
        /**
         * No media data is preloaded.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        NONE = 0,
        /**
         * Only the metadata of the media is preloaded.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        METADATA = 1,
        /**
         * A sufficient amount of media data is preloaded to ensure smooth playback
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        AUTO = 2
    }
    /**
     * Represents a **MediaInfo** object used as a parameter of the
     * [CreateNativeMediaPlayerCallback]{@link @ohos.web.webview:webview.CreateNativeMediaPlayerCallback} callback. The
     * object contains information about media on the web page. The application may create, based on the information, a
     * player that takes over media playback of the web page.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    interface MediaInfo {
        /**
         * ID of **<video>** or **<audio>** on the web page.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        embedID: string;
        /**
         * Type of the media.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        mediaType: MediaType;
        /**
         * Source of the media. There may be multiple sources. The application needs to select a supported source to play.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        mediaSrcList: MediaSourceInfo[];
        /**
         * Surface information used for same-layer rendering.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        surfaceInfo: NativeMediaPlayerSurfaceInfo;
        /**
         * Whether the **controls** attribute exists in **<video>** or **<audio>**.
         *
         * The value **true** means that the **controls** attribute exists in **<video>** or **<audio>**, and **false**
         * means the opposite.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        controlsShown: boolean;
        /**
         * Value of the **controlslist** attribute in **<video>** or **<audio>**.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        controlList: string[];
        /**
         * Whether to mute the player.
         *
         * The value **true** means to mute the player, and **false** means the opposite.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        muted: boolean;
        /**
         * URL of a poster.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        posterUrl: string;
        /**
         * Whether preloading is required.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        preload: Preload;
        /**
         * HTTP headers that need to be included in the player's request for media resources.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        headers: Record<string, string>;
        /**
         * Attributes in **<video>** or **<audio>**.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        attributes: Record<string, string>;
    }
    /**
     * Defines a **CreateNativeMediaPlayerCallback** object used as a parameter of the
     * [onCreateNativeMediaPlayer]{@link @ohos.web.webview:webview.WebviewController#onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback)}
     * callback. This object is used to create a player to take over media playback of the web page.
     *
     * @param { NativeMediaPlayerHandler } handler - Object used to report the player status to the ArkWeb engine.
     * @param { MediaInfo } mediaInfo - Information about the media on the web page.
     * @returns { NativeMediaPlayerBridge } Instance of the interface class between the player that takes over web media
     *     and the ArkWeb kernel.
     *     <br>The application needs to implement this interface class.
     *     <br> The ArkWeb engine uses an object of this interface class to control the player created by the application to
     *     take over web page media.
     *     <br>If the application returns **null**, the application does not take over the media playback, and the media will
     *     be played by the ArkWeb engine.
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    type CreateNativeMediaPlayerCallback = (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge;
    /**
     * This class is used to set adblock config.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice
     * @since 12
     */
    class AdsBlockManager {
        /**
         * set Ads Block ruleset file, containing easylist rules.
         *
         * <p><strong>API Note</strong>:<br>
         * The ad blocking rules set by this API will be persistently stored after successful internal parsing; you do not
         * need to set them again after the application is restarted.
         * </p>
         *
         * @param {string} rulesFile - absolute file path contains app customized ads block rules.
         * @param {boolean} replace - (@code true)replace internal rules;(@code false) add to internal rules.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static setAdsBlockRules(rulesFile: string, replace: boolean): void;
        /**
         * Add items to Ads Block Disallow list.
         *
         * <p><strong>API Note</strong>:<br>
         * The domain name set by this API is not persistent; they need to be set again after the application is
         * restarted.
         *
         * The ad blocking feature matches website URLs based on the suffix. For example, if the disallowed list contains
         * **'example.com'** or **'www.example.com'**, then ad blocking will be disabled for sites
         * **https://www.example.com** and **https://m.example.com**.
         * </p>
         *
         * @param { Array<string> } domainSuffixes - list of domain suffix, if web page url matches someone in the list,
         *     Ads Block will be disallowed for the web page.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static addAdsBlockDisallowedList(domainSuffixes: Array<string>): void;
        /**
         * Add items to Ads Block Allow list.
         * By default, ads block is allowed for all pages unless they are added to the
         * disallow list. The priority of allowlist is higher than the disallowlist. It is
         * used to re-enable ads block on the page that matches disallow list.
         *
         * @param { Array<string> } domainSuffixes - list of domain suffix, if web page url matches someone in the list,
         *     Ads Block will be allowed for the web page.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static addAdsBlockAllowedList(domainSuffixes: Array<string>): void;
        /**
         * remove items from Ads Block Disallowed list.
         *
         * @param { Array<string> } domainSuffixes - list of domain suffix needed be removed from disallow list
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static removeAdsBlockDisallowedList(domainSuffixes: Array<string>): void;
        /**
         * remove items from Ads Block Allowed list.
         *
         * @param { Array<string> } domainSuffixes - list of domain suffix needed be removed from allow list
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static removeAdsBlockAllowedList(domainSuffixes: Array<string>): void;
        /**
         * clear Ads Block Disallowed list.
         *
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static clearAdsBlockDisallowedList(): void;
        /**
         * clear Ads Block Allowed list.
         *
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice
         * @since 12
         */
        static clearAdsBlockAllowedList(): void;
    }
    /**
     * This class is used to enable back forward cache supported features.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 12
     */
    class BackForwardCacheSupportedFeatures {
        /**
         * Whether cache the pages that use native embed.
         *
         * <p><strong>API Note</strong>:<br>
         * When the value is set to **true**, you need to maintain the lifecycle of system components created for the
         * same-layer rendering elements to avoid resource leak.
         * </p>
         *
         * Default is false;
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        nativeEmbed: boolean;
        /**
         * Whether cache the pages that use media take over.
         * <p><strong>API Note</strong>:<br>
         * When the value is set to **true**, you need to maintain the lifecycle of system components
         * created for video elements to avoid resource leak.
         * </p>
         *
         * Default is false;
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        mediaTakeOver: boolean;
        /**
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        constructor();
    }
    /**
     * This class is used to set back forward cache options.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 12
     */
    class BackForwardCacheOptions {
        /**
         * Set the maximum size of pages that can cache.
         * Default is 1, max is 50.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        size: number;
        /**
         * Set the lifetime in seconds in the BackForwardCache.
         * Unit: seconds. Default is 600.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        timeToLive: number;
        /**
         * @syscap SystemCapability.Web.Webview.Core
         * @since 12
         */
        constructor();
    }
    /**
     * Defines the PrefetchOptions class.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 21
     */
    class PrefetchOptions {
        /**
         * ‌Set prefetch page interval limit.
         *
         * <p><strong>API Note</strong>:<br>
         * The value should be an integer.Unit: ms. Default 500ms (ensures only one successful prefetch within 500ms).
         * The interval throttles prefetch frequency to balance performance and resource usage.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 21
         */
        minTimeBetweenPrefetchesMs: number;
        /**
         * Set whether to ignore Cache-Control: no-store‌.
         *
         * <p><strong>API Note</strong>:<br>
         * This setting controls whether prefetch operations bypass the HTTP Cache-Control: no-store directive.
         * Important‌: Default behavior (false) aligns with HTTP security standards. Overriding (true) requires explicit risk
         * assessment for non-sensitive resources.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 21
         */
        ignoreCacheControlNoStore: boolean;
        /**
         * Constructor for PrefetchOptions.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 21
         */
        constructor();
    }
    /**
     * Enum type supplied to {@link insertProxyRule} for indicating the scheme filter for proxy.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice [since 19]
     * @since 15
     */
    enum ProxySchemeFilter {
        /**
         * This indicates all the schemes will use the proxy.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        MATCH_ALL_SCHEMES = 0,
        /**
         * This indicates only the HTTP requests will use the proxy.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        MATCH_HTTP = 1,
        /**
         * This indicates only the HTTPS requests will use the proxy.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        MATCH_HTTPS = 2
    }
    /**
     * The ProxyConfig used by applyProxyOverride.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice [since 19]
     * @since 15
     */
    class ProxyConfig {
        /**
         * Insert a bypass rule that indicates URLs that should skip the override proxy and connect the server directly
         * instead.
         * These maybe URLs or IP addresses and wildcards are supported. e.g. "*.example.com" means that requests to
         * "https://www.example.com" and "http://test.example.com" will connect the server directly.
         *
         * @param { string } bypassRule - The bypass rule.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        insertBypassRule(bypassRule: string): void;
        /**
         * Insert a proxy rule that indicates URLs that match the schemeFilter will connect the server directly.
         *
         * @param { ProxySchemeFilter } schemeFilter - The scheme filter for this rule.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        insertDirectRule(schemeFilter?: ProxySchemeFilter): void;
        /**
         * Insert a proxy rule which indicates that requests matching the schemeFilter should use an override proxy, all requests will
         * use the proxy rule if schemeFilter is null.
         *
         * The format for proxy is [scheme://]host[:port]. Scheme is optional and must be HTTP, HTTPS, or SOCKS if present. Scheme defaults to HTTP.
         * Host is an IPv6 literal with brackets, an IPv4 literal or one or more labels seperated by a period. Port number is optional and defaults
         * to 80 for HTTP, 443 for HTTPS and 1080 for SOCKS.
         *
         * e.g. example.com host: example.com
         *      https://example.com  scheme: https  host: example.com
         *      example.com:8888     host: example.com  port: 8888
         *      https://example.com:8888  scheme:https  host: example.com  port:8888
         *      192.168.1.1  host: 192.168.1.1
         *      192.168.1.1:8888  host:192.168.1.1 port: 8888
         *      [10:20:30:40:50:60:70:80]
         *
         * @param { string } proxyRule - The proxy rule.
         * @param { ProxySchemeFilter } schemeFilter - The scheme filter for this rule.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        insertProxyRule(proxyRule: string, schemeFilter?: ProxySchemeFilter): void;
        /**
         * Hostnames without a period in them (and that are not IP literals) will skip the proxy and connect the server
         * directly.
         * Examples: "abc", "local", "some-domain".
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        bypassHostnamesWithoutPeriod(): void;
        /**
         * By default, certain hostnames implicitly bypass the proxy if they are link-local IPs, or localhost addresses. For instance
         * hostnames matching any of (non-exhaustive list): localhost *.localhost [::1] 127.0.0.1/8 169.254/16 [FE80::]/10
         * Call this function to override the default behavior and force localhost and link-local URLs to be sent through the proxy.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        clearImplicitRules(): void;
        /**
         * Reverse the bypass rules.
         *
         * If false all URLs will use proxy settings except URLs match the bypass rules.
         * If true only URLs in the bypass list will use proxy, and all other URLs will be connected to directly.
         *
         * @param { boolean } reverse - If reverse the bypass rule.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        enableReverseBypass(reverse: boolean): void;
        /**
         * Returns the bypass rules.
         *
         * @returns { Array<string> } The bypass rules.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        getBypassRules(): Array<string>;
        /**
         * Returns the proxy rules.
         *
         * @returns { Array<ProxyRule> } The proxy rules.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        getProxyRules(): Array<ProxyRule>;
        /**
         * Returns if reverse bypass rules.
         *
         * @returns { boolean } If reverse bypass enabled.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        isReverseBypassEnabled(): boolean;
    }
    /**
     * The ProxyRule used by insertProxyRule.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice [since 19]
     * @since 15
     */
    class ProxyRule {
        /**
         * Returns the scheme filter used for this rule.
         *
         * @returns { ProxySchemeFilter } The scheme filter used for this rule.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        getSchemeFilter(): ProxySchemeFilter;
        /**
         * Returns the proxy URL.
         *
         * @returns { string } The proxy URL.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        getUrl(): string;
    }
    /**
     * The callback for proxy changed.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice [since 19]
     * @since 15
     */
    type OnProxyConfigChangeCallback = () => void;
    /**
     * This class is used for set proxy for ArkWeb.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @atomicservice [since 19]
     * @since 15
     */
    class ProxyController {
        /**
         * Sets ProxyConfig which will be used by all Webs in the app. URLs that match patterns in the bypass list will
         * connect the server directly.
         * Instead, the request will use the proxy specified by the config. Requests are not guaranteed to use the new proxy
         * immediately; wait for
         * the listener before loading a page. This listener will be called on the UI thread.
         * Note: calling applyProxyOverride will cause any existing system wide setting to be ignored.
         *
         * @param { ProxyConfig } proxyConfig - The proxy config.
         * @param { OnProxyConfigChangeCallback } callback - Called when the proxy has been changed.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        static applyProxyOverride(proxyConfig: ProxyConfig, callback: OnProxyConfigChangeCallback): void;
        /**
         * Remove the proxy config. Requests are not guaranteed to not use the proxy; Wait for the listener before loading a
         * page. This listener
         * will be called on the UI thread.
         *
         * @param { OnProxyConfigChangeCallback } callback - Called when the proxy has been changed.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         * @syscap SystemCapability.Web.Webview.Core
         * @atomicservice [since 19]
         * @since 15
         */
        static removeProxyOverride(callback: OnProxyConfigChangeCallback): void;
    }
    /**
     * Enumerates the destroy modes of the **Web** component. When the Web component is destroyed, the destroy mode
     * affects the resource release time of the Web kernel, such as the JavaScript running context and rendering context.
     * @enum { number }
     * @syscap SystemCapability.Web.Webview.Core
     * @since 20
     */
    enum WebDestroyMode {
        /**
         * Normal mode. The system determines the destroy time of **Web** component resources.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        NORMAL_MODE = 0,
        /**
         * Quick mode. When the **Web** component is destroyed, the related internal resources are
         * destroyed immediately.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 20
         */
        FAST_MODE = 1
    }
    /**
     * Enumerates the site isolation modes. The site isolation mechanism isolates websites from different sources in
     * different render processes to reduce the cross-domain attack surface. For example, on a PC, each tab corresponds to
     * a render process. After site isolation is enabled, Iframes from different sources run in independent render
     * processes.
     * @enum {number}
     * @syscap SystemCapability.Web.Webview.Core
     * @since 21
     */
    enum SiteIsolationMode {
        /**
         * Partial site isolation. New sites are loaded in the same render process.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 21
         */
        PARTIAL = 0,
        /**
         * Strict site isolation. Iframes from different sites are switched to new render processes.
         * @syscap SystemCapability.Web.Webview.Core
         * @since 21
         */
        STRICT = 1
    }
    /**
     * Enumerates the global scrollbar modes in the web page.
     * @syscap SystemCapability.Web.Webview.Core
     * @since 23
     */
    enum ScrollbarMode {
        /**
         * The scrollbar is not always displayed.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        OVERLAY_LAYOUT_SCROLLBAR = 0,
        /**
         * The scrollbar is always displayed.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        FORCE_DISPLAY_SCROLLBAR = 1,
        /**
         * Overlay VisualViewport scrollbars: appear on scroll, hide when idle. Rendered via Visual Viewport, non-draggable.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        OVERLAY_VISUAL_SCROLLBAR = 2
    }
    /**
     * Indicates whether to restrict cookies so that only requests sent back to the same site that
     * created them can carry them.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 23
     */
    enum WebHttpCookieSameSitePolicy {
        /**
         * Cookies marked as Secure are allowed to be carried in cross-site requests.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        NONE = 0,
        /**
         * Allow specific cross-site requests to carry cookies.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        LAX = 1,
        /**
         * Prohibit cross-site requests from carrying cookies.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        STRICT = 2
    }
    /**
     * The form factors for User-Agent metadata.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 24
     */
    enum UserAgentFormFactor {
        /**
         * Form factor option: Automotive.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        AUTOMOTIVE = 'Automotive',
        /**
         * Form factor option: Desktop.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        DESKTOP = 'Desktop',
        /**
         * Form factor option: Mobile.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        MOBILE = 'Mobile',
        /**
         * Form factor option: EInk.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        EINK = 'EInk',
        /**
         * Form factor option: Tablet.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        TABLET = 'Tablet',
        /**
         * Form factor option: Watch.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        WATCH = 'Watch',
        /**
         * Form factor option: XR.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        XR = 'XR'
    }
    /**
     * Class that holds brand name, major version and full version. Brand name and major version used to generated
     * User-Agent client hints sec-cu-ua. Brand name and full version used to generated user-agent client hint
     * sec-ch-ua-full-version-list.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 24
     */
    class UserAgentBrandVersion {
        /**
         * Sets the brand. Should not be blank.
         *
         * @param { string } brand - The brand.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        setBrand(brand: string): void;
        /**
         * Get the brand info.
         *
         * @returns { string } - Returns brand info of UserAgentBrandVersion.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getBrand(): string;
        /**
         * Sets the major version. Should not be blank.
         *
         * @param { string } majorVersion - The major version.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        setMajorVersion(majorVersion: string): void;
        /**
         * Get the major version.
         *
         * @returns { string } - Returns major version of UserAgentBrandVersion.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getMajorVersion(): string;
        /**
         * Sets the full version. Should not be blank.
         *
         * @param { string } fullVersion - The full version.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        setFullVersion(fullVersion: string): void;
        /**
         * Get the full version.
         *
         * @returns { string } - Returns full version of UserAgentBrandVersion.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getFullVersion(): string;
    }
    /**
     * Holds User-Agent metadata information and uses to generate User-Agent client hints.
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 24
     */
    class UserAgentMetadata {
        /**
         * Sets User-Agent metadata brands and their versions.
         *
         * <p><strong>API Note</strong>:<br>
         * The default value is an empty list which means the system default User-Agent metadata brands and versions will be
         * used to generate the User-Agent client hints.
         * </p>
         *
         * @param { Array<UserAgentBrandVersion> } brandVersionList - The brandVersionList is used to generate User-Agent
         *     client hints sec-ch-ua-full-version-list.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        setBrandVersionList(brandVersionList: Array<UserAgentBrandVersion>): void;
        /**
         * Returns the current list of UserAgentBrandVersion which are used to generate the User-Agent client hints
         * sec-ch-ua and sec-ch-ua-full-version-list.
         *
         * @returns { Array<UserAgentBrandVersion> } - Returns the current list of UserAgentBrandVersion.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getBrandVersionList(): Array<UserAgentBrandVersion>;
        /**
         * Sets User-Agent metadata architecture.
         *
         * <p><strong>API Note</strong>:<br>
         * The default value is empty string which means the system default value will be used.
         * </p>
         *
         * @param { string } arch - The arch is used to generate User-Agent client hints sec-ch-ua-architecture.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        setArchitecture(arch: string): void;
        /**
         * Gets the value for sec-ch-ua-architecture.
         *
         * @returns { string } - Returns the value for sec-ch-ua-architecture.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getArchitecture(): string;
        /**
         * Sets User-Agent metadata bitness default is "".
         *
         * @param { string } bitness - The bitness is used to generate User-Agent client hints sec-ch-ua-bitness.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        setBitness(bitness: string): void;
        /**
         * Gets the value for the sec-ch-ua-bitness.
         *
         * @returns { string } - Returns the value for the sec-ch-ua-bitness.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getBitness(): string;
        /**
         * Sets User-Agent metadata form factors.
         *
         * <p><strong>API Note</strong>:<br>
         * The default value is empty list which means the system default value will be used.
         * Form factor value should be one or more of DESKTOP, AUTOMOTIVE, MOBILE, TABLET, XR, EINK, WATCH.
         * </p>
         *
         * @param { Array<UserAgentFormFactor> } formFactors - The formFactors is used to generate User-Agent client hints
         *     sec-ch-ua-form-factors.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        setFormFactors(formFactors: Array<UserAgentFormFactor>): void;
        /**
         * Gets the value for the sec-ch-ua-form-factors.
         *
         * @returns { Array<UserAgentFormFactor> } - Returns the form factors.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getFormFactors(): Array<UserAgentFormFactor>;
        /**
         * Sets User-Agent metadata full version.
         *
         * <p><strong>API Note</strong>:<br>
         * The default value is empty string which means the system default value will be used.
         * </p>
         *
         * @param { string } fullVersion - The fullVersion is used to generate User-Agent client hints
         *     sec-ch-ua-full-version.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        setFullVersion(fullVersion: string): void;
        /**
         * Gets the value for the sec-ch-ua-full-version.
         *
         * @returns { string } - Returns the value for the sec-ch-ua-full-version.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getFullVersion(): string;
        /**
         * Sets User-Agent metadata mobile, default is true.
         *
         * @param { boolean } isMobile - The isMobile is used to generate User-Agent client hints sec-ch-ua-mobile.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        setMobile(isMobile: boolean): void;
        /**
         * Gets the value for the sec-ch-ua-mobile.
         *
         * @returns { boolean } - Returns the value for the sec-ch-ua-mobile.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getMobile(): boolean;
        /**
         * Sets User-Agent metadata model.
         *
         * <p><strong>API Note</strong>:<br>
         * The default value is empty string which means the system default value will be used.
         * </p>
         *
         * @param { string } model - The model is used to generate User-Agent client hints sec-ch-ua-model.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        setModel(model: string): void;
        /**
         * Gets the value for the sec-ch-ua-model.
         *
         * @returns { string } - Returns the value for the sec-ch-ua-model.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getModel(): string;
        /**
         * Sets User-Agent metadata platform.
         *
         * <p><strong>API Note</strong>:<br>
         * The default value is empty string which means the system default value will be used.
         * </p>
         *
         * @param { string } platform - The platform is used to generate User-Agent client hints sec-ch-ua-platform.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        setPlatform(platform: string): void;
        /**
         * Gets the value for the sec-ch-ua-platform.
         *
         * @returns { string } - Returns the value for the sec-ch-ua-platform.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getPlatform(): string;
        /**
         * Sets User-Agent metadata platform version.
         *
         * <p><strong>API Note</strong>:<br>
         * The default value is empty string which means the system default value will be used.
         * </p>
         *
         * @param { string } platformVersion - The platformVersion is used to generate User-Agent client hints
         *     sec-ch-ua-platform-version.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        setPlatformVersion(platformVersion: string): void;
        /**
         * Gets the value for the sec-ch-ua-platform-version.
         *
         * @returns { string } - Returns the value for the sec-ch-ua-platform-version.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getPlatformVersion(): string;
        /**
         * Sets User-Agent metadata wow64, default is false.
         *
         * @param { boolean } isWow64 - The wow64 is used to generate User-Agent client hints sec-ch-ua-wow64.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        setWow64(isWow64: boolean): void;
        /**
         * Gets the value for the sec-ch-ua-wow64.
         *
         * @returns { boolean } - Returns the value for the sec-ch-ua-wow64.
         * @syscap SystemCapability.Web.Webview.Core
         * @stagemodelonly
         * @since 24
         */
        getWow64(): boolean;
    }
    /**
     * Defines the Web's HTTPCookie.
     * <p><strong>API Note</strong>:<br>
     * The maximum length allowed for each attribute value in a cookie string is 1024.
     * </p>
     *
     * @syscap SystemCapability.Web.Webview.Core
     * @since 23
     */
    interface WebHttpCookie {
        /**
         * Gets the cookie's samesite policy.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        samesitePolicy: WebHttpCookieSameSitePolicy;
        /**
         * Gets the cookie's expiration date.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        expiresDate: string;
        /**
         * Gets the cookie's name.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        name: string;
        /**
         * Gets if the cookie is session cookie.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        isSessionCookie: boolean;
        /**
         * Gets the cookie's value.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        value: string;
        /**
         * Gets the cookie's path.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        path: string;
        /**
         * Gets whether the current cookie is marked as HttpOnly.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        isHttpOnly: boolean;
        /**
         * Gets whether the current cookie is marked as Secure.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        isSecure: boolean;
        /**
         * Gets the domain of the cookie.
         *
         * @syscap SystemCapability.Web.Webview.Core
         * @since 23
         */
        domain: string;
    }
}
export default webview;

```
