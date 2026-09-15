# @ohos.mediaquery.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
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
import { Callback } from './@ohos.base';
/**
 * The **mediaquery** module provides different styles for different media types.
 *
 * > **NOTE**
 * >
 * > - This module cannot be used in the file declaration of the [UIAbility]{@link @ohos.app.ability.UIAbility}. In
 * > other words, the APIs of this module can be used only after a component instance is created; they cannot be called
 * > in the lifecycle of the UIAbility.
 * >
 * > - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used
 * > where [the UI context is ambiguous](docroot://ui/arkts-global-interface.md#ambiguous-ui-context). For details, see
 * > [UIContext]{@link @ohos.arkui.UIContext}.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @crossplatform [since 10]
 * @form [since 12]
 * @atomicservice [since 11]
 * @since 7
 */
declare namespace mediaquery {
    /**
     * Provides the media query result.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 7
     */
    interface MediaQueryResult {
        /**
         * Whether the media query condition is met. The value **true** means that the
         * query conditions are met, and **false** means the opposite.
         * This parameter is read-only.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        readonly matches: boolean;
        /**
         * Matching condition of a media event.
         * This parameter is read-only.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        readonly media: string;
    }
    /**
     * Implements the media query listener, including the first query result when the listener is applied for. The
     * specified media query condition, for example, **'(width <= 600vp)'**, is compared system information. If related
     * information is not initialized during the first query, **matches** returns **false**.
     *
     * Inherits from [MediaQueryResult]{@link mediaquery.MediaQueryResult}.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 7
     */
    interface MediaQueryListener extends MediaQueryResult {
        /**
         * Registers a media query listener. The callback is triggered when the media attributes change.
         *
         * > **NOTE**
         * >
         * > The **on** or **off** function cannot be called in the registered callback.
         *
         * @param { 'change' } type - Listener type. The value is fixed at **'change'**.
         * @param { Callback<MediaQueryResult> } callback - Callback registered with media query.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        on(type: 'change', callback: Callback<MediaQueryResult>): void;
        /**
         * Deregisters a media query listener, so that no callback is triggered when the media attributes change.
         *
         * @param { 'change' } type - Listener type. The value is fixed at **'change'**.
         * @param { Callback<MediaQueryResult> } callback - Callback to unregister. If this parameter is not specified, all
         *     callbacks under this handle are unregistered.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @form [since 12]
         * @atomicservice [since 11]
         * @since 7
         */
        off(type: 'change', callback?: Callback<MediaQueryResult>): void;
    }
    /**
     * Sets the media query condition. This API returns the corresponding media query listener.
     *
     * > **NOTE**
     * >
     * > - This API is supported since API version 7 and deprecated since API version 18. You are advised to use
     * > [matchMediaSync](@link @ohos.arkui.UIContext:MediaQuery#matchMediaSync) instead. Before calling this API, you
     * > need to obtain the [MediaQuery](@link @ohos.arkui.UIContext:MediaQuery) object using the
     * > [getMediaQuery](@link @ohos.arkui.UIContext:UIContext#getMediaQuery) method in
     * > [UIContext](@link @ohos.arkui.UIContext).
     * >
     * > - Since API version 10, you can use the
     * > [getMediaQuery](@link @ohos.arkui.UIContext:UIContext#getMediaQuery) API in
     * > [UIContext]{@link @ohos.arkui.UIContext:UIContext} to obtain the
     * > [MediaQuery]{@link @ohos.arkui.UIContext:MediaQuery} object associated with the current UI context.
     *
     * @param { string } condition - Media query condition. For details, see
     *     [Syntax](docroot://ui/arkts-layout-development-media-query.md#syntax).
     * @returns { MediaQueryListener } Media query listener, which is used to register or deregister the listening
     *     callback.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @form [since 12]
     * @atomicservice [since 11]
     * @since 7
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.MediaQuery#matchMediaSync
     */
    function matchMediaSync(condition: string): MediaQueryListener;
}
export default mediaquery;

```
