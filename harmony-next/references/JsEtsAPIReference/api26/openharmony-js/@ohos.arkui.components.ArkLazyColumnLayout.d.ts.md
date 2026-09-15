# @ohos.arkui.components.ArkLazyColumnLayout.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
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
/**
 * Defines the lazy column layout component.
 *
 * @interface LazyColumnLayoutInterface
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export interface LazyColumnLayoutInterface {
    /**
     * Construct the lazy column layout attribute.
     *
     * @returns { LazyColumnLayoutAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    (): LazyColumnLayoutAttribute;
}
/**
 * Defines the lazy column layout attribute.
 *
 * @extends CommonMethod<LazyColumnLayoutAttribute>
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare class LazyColumnLayoutAttribute extends CommonMethod<LazyColumnLayoutAttribute> {
    /**
     * The spacing between rows.
     *
     * @param { LengthMetrics | undefined } space - the spacing between rows.
     *     <br>Default value: 0. <br>Range: [0, +∞).
     * @returns { LazyColumnLayoutAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    space(space: LengthMetrics | undefined): LazyColumnLayoutAttribute;
    /**
     * Sets the horizontal alignment of the row content.
     *
     * @param { HorizontalAlign | undefined } value - the horizontal alignment of the row content.
     *     <br>Default value HorizontalAlign.Center.
     * @returns { LazyColumnLayoutAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    alignItems(value: HorizontalAlign | undefined): LazyColumnLayoutAttribute;
    /**
     * Sets the header of the lazy column layout.
     *
     * @param { CustomBuilder | undefined } builder - The header builder function
     *     <br>Passing undefined will remove the header.
     * @returns { LazyColumnLayoutAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    header(builder: CustomBuilder | undefined): LazyColumnLayoutAttribute;
    /**
     * Sets the footer of the lazy column layout.
     *
     * @param { CustomBuilder | undefined } builder - The footer builder function
     *     <br>Passing undefined will remove the footer.
     * @returns { LazyColumnLayoutAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    footer(builder: CustomBuilder | undefined): LazyColumnLayoutAttribute;
    /**
     * Sets sticky style for header and footer.
     *
     * @param { StickyStyle | undefined } sticky - The sticky style for header and footer.
     * @returns { LazyColumnLayoutAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    sticky(sticky: StickyStyle | undefined): LazyColumnLayoutAttribute;
    /**
     * Triggered when the index of child components in the visible area changes.
     *
     * @param { OnVisibleIndexesChangeCallback | undefined } callback - callback function, triggered
     *     when the index of child components in the visible area changes.
     *     <br>Passing undefined will unregister the callback.
     * @returns { LazyColumnLayoutAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): LazyColumnLayoutAttribute;
}
/**
 * Defines the lazy column layout component.
 *
 * @type { LazyColumnLayoutInterface }
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @uicomponent
 * @since 26.0.0
 */
export declare const LazyColumnLayout: LazyColumnLayoutInterface;
/**
 * Defines the lazy column layout component instance.
 *
 * @type { LazyColumnLayoutAttribute }
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare const LazyColumnLayoutInstance: LazyColumnLayoutAttribute;

```
