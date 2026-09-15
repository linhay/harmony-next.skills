# @ohos.router.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2025 Huawei Device Co., Ltd.
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
 * @kit ArkUI
 */
import { AsyncCallback } from './@ohos.base';
/**
 * The **Router** module provides APIs to access pages through URLs. You can use the APIs to navigate to a specified
 * page in an application, replace the current page with another one in the same application, and return to the previous
 * page or a specified page.
 *
 * For routing management, it is recommended that you use the
 * [Navigation](docroot://ui/arkts-navigation-architecture.md) component instead as your application routing framework.
 *
 * > **NOTE**
 * >
 * > - Page routing APIs can be invoked only after page rendering is complete. Do not call these APIs in **onInit** and
 * > **onReady** when the page is still in the rendering phase.
 * >
 * > - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used
 * > where [the UI context is ambiguous](docroot://ui/arkts-global-interface.md#ambiguous-ui-context). For details, see
 * > [UIContext]{@link @ohos.arkui.UIContext}.
 * >
 * > - When using
 * > [pushUrl]{@link @ohos.arkui.UIContext:Router#pushUrl(options: router.RouterOptions, callback: AsyncCallback<void>)}
 * > or
 * > [pushNamedRoute]{@link @ohos.arkui.UIContext:Router#pushNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>)}
 * > with a callback to return the result, be aware that the stack information obtained through the callback using APIs
 * > such as [getLength]{@link @ohos.arkui.UIContext:Router#getLength} represents an intermediate state during the
 * > navigation operation. This temporary state might differ from the final stack information available after the stack
 * > operation is complete.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 8
 */
declare namespace router {
    /**
     * Enumerates the routing modes.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum RouterMode {
        /**
         * Multi-instance mode. It is the default routing mode.
         *
         * The target page is added to the top of the page stack, regardless of whether a page with the same URL exists in
         * the stack.
         *
         * **NOTE**
         *
         * If no routing mode is used, the navigation will be carried out according to the default multi-instance mode.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        Standard,
        /**
         * Singleton mode.
         *
         * If the URL of the target page already exists in the page stack, the page is moved to the top of the stack.
         *
         * If the URL of the target page does not exist in the page stack, the page is redirected to in multi-instance mode.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        Single
    }
    /**
     * Describes the page routing options.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Lite
     * @crossplatform [since 19]
     * @atomicservice [since 11]
     * @since 8
     */
    interface RouterOptions {
        /**
         * URL of the target page, in either of the following formats:
         *
         * - Absolute path of the page. The value is available in the pages list in the **config.json** file, for example:
         *  - pages/index/index
         *  - pages/detail/detail
         * - special value. If the value of **url** is **"/"**, the application navigates to the home page. By default, the
         * home page is set to the first item in the **src** value array.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Lite
         * @crossplatform [since 19]
         * @atomicservice [since 11]
         * @since 8
         */
        url: string;
        /**
         * Data that needs to be passed to the target page during redirection. The received data becomes invalid when the
         * page is switched to another page. The target page can use **router.getParams()** to obtain the passed parameters,
         * for example, **this.keyValue** (**keyValue** is the value of a key in **params**). In the web-like paradigm,
         * these parameters can be directly used on the target page. If the field specified by **key** already exists on the
         * target page, the passed value of the key will be displayed.
         *
         * **NOTE**
         *
         * The **params** parameter can only carry serializable data. Objects returned by methods and system APIs (for
         * example, **PixelMap** objects defined and returned by media APIs) cannot be passed. To pass such objects, extract
         * from them the basic type attributes to be passed, and then construct objects of the object type.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Lite
         * @crossplatform [since 19]
         * @atomicservice [since 11]
         * @since 8
         */
        params?: Object;
        /**
         * Whether the corresponding page is recoverable.
         *
         * Default value: **true**.
         *
         * **true**: The corresponding page is recoverable.
         *
         * **false**: The corresponding page is not recoverable.
         *
         * **NOTE**
         *
         * If an application is switched to the background and is later closed by the system due to resource constraints or
         * other reasons, a page marked as recoverable can be restored by the system when the application is brought back to
         * the foreground. For more details, see
         * [UIAbility Backup and Restore](docroot://application-models/ability-recover-guideline.md).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Lite
         * @since 14
         */
        recoverable?: boolean;
    }
    /**
     * Describes the page routing state.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     */
    interface RouterState {
        /**
         * Index of the current page in the stack. The index starts from 1 from the bottom to the top of the stack.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        index: number;
        /**
         * Name of the current page, that is, the file name.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        name: string;
        /**
         * Path of the current page.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        path: string;
        /**
         * Parameters carried on the current page.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        params: Object;
    }
    /**
     * Describes the page routing state.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     */
    interface EnableAlertOptions {
        /**
         * Content displayed in the confirm dialog box.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        message: string;
    }
    /**
     * Navigates to a specified page in the application.
     *
     * @param { RouterOptions } options - Page routing parameters.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.arkui.UIContext:Router#pushUrl(options: router.RouterOptions)
     */
    function push(options: RouterOptions): void;
    /**
     * Navigates to a specified page in the application.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { RouterOptions } options - Page routing parameters.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @throws { BusinessError } 100002 - Uri error. The URI of the page to redirect is incorrect or does not exist
     * @throws { BusinessError } 100003 - Page stack error. Too many pages are pushed.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#pushUrl(options: router.RouterOptions, callback: AsyncCallback<void>)
     */
    function pushUrl(options: RouterOptions, callback: AsyncCallback<void>): void;
    /**
     * Navigates to a specified page in the application.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { RouterOptions } options - Page routing parameters.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @throws { BusinessError } 100002 - Uri error. The URI of the page to redirect is incorrect or does not exist
     * @throws { BusinessError } 100003 - Page stack error. Too many pages are pushed.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#pushUrl(options: router.RouterOptions)
     */
    function pushUrl(options: RouterOptions): Promise<void>;
    /**
     * Navigates to a specified page in the application.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { RouterOptions } options - Page routing parameters.
     * @param { RouterMode } mode - Routing mode.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @throws { BusinessError } 100002 - Uri error. The URI of the page to redirect is incorrect or does not exist
     * @throws { BusinessError } 100003 - Page stack error. Too many pages are pushed.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#pushUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>)
     */
    function pushUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void;
    /**
     * Navigates to a specified page in the application.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { RouterOptions } options - Page routing parameters.
     * @param { RouterMode } mode - Routing mode.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @throws { BusinessError } 100002 - Uri error. The URI of the page to redirect is incorrect or does not exist
     * @throws { BusinessError } 100003 - Page stack error. Too many pages are pushed.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#pushUrl(options: router.RouterOptions, mode: router.RouterMode)
     */
    function pushUrl(options: RouterOptions, mode: RouterMode): Promise<void>;
    /**
     * Replaces the current page with another one in the application and destroys the current page.
     *
     * @param { RouterOptions } options - Description of the new page.
     * @syscap SystemCapability.ArkUI.ArkUI.Lite
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.arkui.UIContext:Router#replaceUrl(options: router.RouterOptions)
     */
    function replace(options: RouterOptions): void;
    /**
     * Replaces the current page with another one in the application and destroys the current page.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { RouterOptions } options - Description of the new page.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - The UI execution context is not found. This error code is thrown only in the
     *     standard system.
     * @throws { BusinessError } 200002 - Uri error. The URI of the page to be used for replacement is incorrect or does
     *     not exist.
     * @syscap SystemCapability.ArkUI.ArkUI.Lite
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @reserved ["liteWearable"] [since 11]
     * @useinstead @ohos.arkui.UIContext:Router#replaceUrl(options: router.RouterOptions, callback: AsyncCallback<void>)
     */
    function replaceUrl(options: RouterOptions, callback: AsyncCallback<void>): void;
    /**
     * Replaces the current page with another one in the application and destroys the current page. This API cannot be
     * used to configure page transition effects. To configure page transition effects, use the
     * [Navigation](docroot://ui/arkts-navigation-architecture.md) component.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { RouterOptions } options - Description of the new page.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - The UI execution context is not found. This error code is thrown only in the
     *     standard system.
     * @throws { BusinessError } 200002 - Uri error. The URI of the page to be used for replacement is incorrect or does
     *     not exist.
     * @syscap SystemCapability.ArkUI.ArkUI.Lite
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @reserved ["liteWearable"] [since 11]
     * @useinstead @ohos.arkui.UIContext:Router#replaceUrl(options: router.RouterOptions)
     */
    function replaceUrl(options: RouterOptions): Promise<void>;
    /**
     * Replaces the current page with another one in the application and destroys the current page.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { RouterOptions } options - Description of the new page.
     * @param { RouterMode } mode - Routing mode.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - The UI execution context is not found. This error code is thrown only in the
     *     standard system.
     * @throws { BusinessError } 200002 - Uri error. The URI of the page to be used for replacement is incorrect or does
     *     not exist.
     * @syscap SystemCapability.ArkUI.ArkUI.Lite
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @reserved ["liteWearable"] [since 11]
     * @useinstead @ohos.arkui.UIContext:Router#replaceUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>)
     */
    function replaceUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void;
    /**
     * Replaces the current page with another one in the application and destroys the current page.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { RouterOptions } options - Description of the new page.
     * @param { RouterMode } mode - Routing mode.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Failed to get the delegate. This error code is thrown only in the standard
     *     system.
     * @throws { BusinessError } 200002 - Uri error. The URI of the page to be used for replacement is incorrect or does
     *     not exist.
     * @syscap SystemCapability.ArkUI.ArkUI.Lite
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @reserved ["liteWearable"] [since 11]
     * @useinstead @ohos.arkui.UIContext:Router#replaceUrl(options: router.RouterOptions, mode: router.RouterMode)
     */
    function replaceUrl(options: RouterOptions, mode: RouterMode): Promise<void>;
    /**
     * Returns to the previous page or a specified page, which deletes all pages between the current page and the target
     * page.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { RouterOptions } options - Description of the target page. The **url** parameter indicates the URL of the
     *     page to return to. If the specified page does not exist in the navigation stack, no action is taken. If no URL
     *     is set, the application returns to the previous page, and the page is not rebuilt. Pages are only reclaimed
     *     after being popped from the navigation stack. Setting **url** to the special value **"/"** has no effect. If
     *     the named route is used, the provided URL must be the name of the named route.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#back(options?: router.RouterOptions)
     */
    function back(options?: RouterOptions): void;
    /**
     * Returns to the specified page, which deletes all pages between the current page and the target page.
     *
     * > **NOTE**
     * >
     * > - Since API version 12, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { number } index - Index of the target page to navigate to. The index starts from 1 from the bottom to the
     *     top of the stack.
     * @param { Object } [params] - Parameters carried when returning to the page.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#back(index: number, params?: Object)
     */
    function back(index: number, params?: Object): void;
    /**
     * Clears all historical pages in the stack and retains only the current page at the top of the stack.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#clear
     */
    function clear(): void;
    /**
     * Obtains the number of pages in the current stack.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @returns { string } Number of pages in the stack. The maximum value is **32**.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#getLength
     */
    function getLength(): string;
    /**
     * Obtains state information about the page at the top of the navigation stack.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @returns { RouterState } Page routing state.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#getState
     */
    function getState(): RouterState;
    /**
     * Obtains the status information about a page by its index.
     *
     * > **NOTE**
     * >
     * > - Since API version 12, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { number } index - Index of the target page. The index starts from 1 from the bottom to the top of the
     *     stack.
     * @returns { RouterState | undefined } State information about the target page; **undefined** if the specified index
     *     does not exist.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#getStateByIndex
     */
    function getStateByIndex(index: number): RouterState | undefined;
    /**
     * Obtains the status information about a page by its URL.
     *
     * > **NOTE**
     * >
     * > - Since API version 12, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { string } url - URL of the target page.
     * @returns { Array<RouterState> } Page routing state.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#getStateByUrl
     */
    function getStateByUrl(url: string): Array<RouterState>;
    /**
     * Enables the display of a confirm dialog box before returning to the previous page.
     *
     * @param { EnableAlertOptions } options - Description of the dialog box.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.arkui.UIContext:Router#showAlertBeforeBackPage
     */
    function enableAlertBeforeBackPage(options: EnableAlertOptions): void;
    /**
     * Enables the display of a confirm dialog box before returning to the previous page.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { EnableAlertOptions } options - Description of the dialog box.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#showAlertBeforeBackPage
     */
    function showAlertBeforeBackPage(options: EnableAlertOptions): void;
    /**
     * Disables the display of a confirm dialog box before returning to the previous page.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.arkui.UIContext:Router#hideAlertBeforeBackPage
     */
    function disableAlertBeforeBackPage(): void;
    /**
     * Disables the display of a confirm dialog box before returning to the previous page.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#hideAlertBeforeBackPage
     */
    function hideAlertBeforeBackPage(): void;
    /**
     * Obtains the parameters passed from the page that initiates redirection to the current page.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     * >
     * > **getParams** obtains only the parameters of the current page and does not clear the parameters associated with
     * > the page.
     *
     * @returns { Object } Parameters passed from the page that initiates redirection to the current page.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#getParams
     */
    function getParams(): Object;
    /**
     * Describes the named route options.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    interface NamedRouterOptions {
        /**
         * Name of the target named route.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        name: string;
        /**
         * Data that needs to be passed to the target page during redirection. The target page can use
         * **router.getParams()** to obtain the passed parameters, for example, **this.keyValue** (**keyValue** is the value
         * of a key in **params**). In the web-like paradigm, these parameters can be directly used on the target page. If
         * the field specified by **key** already exists on the target page, the passed value of the key will be displayed.
         *
         * **NOTE**
         *
         * The **params** parameter cannot pass objects returned by methods and system APIs, for example, **PixelMap**
         * objects defined and returned by media APIs. To pass such objects, extract from them the basic type attributes to
         * be passed, and then construct objects of the object type.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        params?: Object;
        /**
         * Whether the corresponding page is recoverable.
         *
         * Default value: **true**.
         *
         * **true**: The corresponding page is recoverable.
         *
         * **false**: The corresponding page is not recoverable.
         *
         * **NOTE**
         *
         * If an application is switched to the background and is later closed by the system due to resource constraints or
         * other reasons, a page marked as recoverable can be restored by the system when the application is brought back to
         * the foreground. For more details, see
         * [UIAbility Backup and Restore](docroot://application-models/ability-recover-guideline.md).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Lite
         * @since 14
         */
        recoverable?: boolean;
    }
    /**
     * Navigates to a page using the named route. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { NamedRouterOptions } options - Page routing parameters.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @throws { BusinessError } 100003 - Page stack error. Too many pages are pushed.
     * @throws { BusinessError } 100004 - Named route error. The named route does not exist.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#pushNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>)
     */
    function pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void;
    /**
     * Navigates to a page using the named route. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { NamedRouterOptions } options - Page routing parameters.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @throws { BusinessError } 100003 - Page stack error. Too many pages are pushed.
     * @throws { BusinessError } 100004 - Named route error. The named route does not exist.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#pushNamedRoute(options: router.NamedRouterOptions)
     */
    function pushNamedRoute(options: NamedRouterOptions): Promise<void>;
    /**
     * Navigates to a page using the named route. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { NamedRouterOptions } options - Page routing parameters.
     * @param { RouterMode } mode - Routing mode.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @throws { BusinessError } 100003 - Page stack error. Too many pages are pushed.
     * @throws { BusinessError } 100004 - Named route error. The named route does not exist.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>)
     */
    function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void;
    /**
     * Navigates to a page using the named route. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { NamedRouterOptions } options - Page routing parameters.
     * @param { RouterMode } mode - Routing mode.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @throws { BusinessError } 100003 - Page stack error. Too many pages are pushed.
     * @throws { BusinessError } 100004 - Named route error. The named route does not exist.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode)
     */
    function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>;
    /**
     * Replaces the current page with another one using the named route and destroys the current page.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { NamedRouterOptions } options - Description of the new page.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - The UI execution context is not found. This error code is thrown only in the
     *     standard system.
     * @throws { BusinessError } 100004 - Named route error. The named route does not exist.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#replaceNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>)
     */
    function replaceNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void;
    /**
     * Replaces the current page with another one using the named route and destroys the current page.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { NamedRouterOptions } options - Description of the new page.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - The UI execution context is not found. This error code is thrown only in the
     *     standard system.
     * @throws { BusinessError } 100004 - Named route error. The named route does not exist.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#replaceNamedRoute(options: router.NamedRouterOptions)
     */
    function replaceNamedRoute(options: NamedRouterOptions): Promise<void>;
    /**
     * Replaces the current page with another one using the named route and destroys the current page.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { NamedRouterOptions } options - Description of the new page.
     * @param { RouterMode } mode - Routing mode.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - The UI execution context is not found. This error code is thrown only in the
     *     standard system.
     * @throws { BusinessError } 100004 - Named route error. The named route does not exist.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>)
     */
    function replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void;
    /**
     * Replaces the current page with another one using the named route and destroys the current page.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getRouter](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Router]{@link @ohos.arkui.UIContext} object associated
     * > with the current UI context.
     *
     * @param { NamedRouterOptions } options - Description of the new page.
     * @param { RouterMode } mode - Routing mode.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Failed to get the delegate. This error code is thrown only in the standard
     *     system.
     * @throws { BusinessError } 100004 - Named route error. The named route does not exist.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 18
     * @useinstead @ohos.arkui.UIContext:Router#replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode)
     */
    function replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>;
}
export default router;

```
