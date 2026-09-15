# @ohos.arkui.components.ArkLazyWaterFlowLayout.d.ts

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
 * @file
 * @kit ArkUI
 */
/**
 * Defines the lazy vertical waterflow layout component.
 *
 * @interface LazyVWaterFlowLayoutInterface
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export interface LazyVWaterFlowLayoutInterface {
    /**
     * Construct the lazy vertical waterflow attribute.
     *
     * @returns { LazyVWaterFlowLayoutAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    (): LazyVWaterFlowLayoutAttribute;
}
/**
 * Defines the lazy waterflow layout attribute.
 *
 * @extends CommonMethod<T>
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare class LazyWaterFlowLayoutAttribute<T> extends CommonMethod<T> {
    /**
     * The spacing between rows.
     *
     * @param { LengthMetrics | undefined } value - The spacing between rows.
     *     <br>Default value: LengthMetrics.vp(0)
     * @returns { T }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    rowsGap(value: LengthMetrics | undefined): T;
    /**
     * The spacing between columns.
     *
     * @param { LengthMetrics | undefined } value - The spacing between columns.
     *     <br>Default value: LengthMetrics.vp(0)
     * @returns { T }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    columnsGap(value: LengthMetrics | undefined): T;
    /**
     * Sets the header of the lazy waterflow layout.
     *
     * @param { CustomBuilder | undefined } builder - The header builder function.
     *     <br>Passing undefined will remove the header.
     * @returns { T }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    header(builder: CustomBuilder | undefined): T;
    /**
     * Sets the footer of the lazy waterflow layout.
     *
     * @param { CustomBuilder | undefined } builder - The footer builder function.
     *     <br>Passing undefined will remove the footer.
     * @returns { T }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    footer(builder: CustomBuilder | undefined): T;
    /**
     * Sets the sticky style for header and footer.
     *
     * @param { StickyStyle | undefined } sticky - The sticky style for header and footer.
     * @returns { T }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    sticky(sticky: StickyStyle | undefined): T;
    /**
     * Called when the first or last item displayed in the component changes.
     * It is triggered once when the component is initialized.
     *
     * @param { OnVisibleIndexesChangeCallback | undefined } callback - callback function, triggered
     *     when the index of child components in the visible area changes.
     *     <br>Passing undefined will unregister the callback.
     * @returns { T }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): T;
}
/**
 * Defines the lazy vertical waterflow layout attribute.
 *
 * @extends LazyWaterFlowLayoutAttribute<LazyVWaterFlowLayoutAttribute>
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare class LazyVWaterFlowLayoutAttribute extends LazyWaterFlowLayoutAttribute<LazyVWaterFlowLayoutAttribute> {
    /**
     * This parameter specifies the number of columns in the current waterflow layout.
     *
     * @param { string | ItemFillPolicy | undefined } value - Number of columns in the layout.
     *     <br>Default value: '1fr'
     *     <br>When the value is a string, it sets the number of columns or the minimum column width
     *     of the current <em>LazyVWaterFlowLayout</em>. For example,
     *     <em>columnsTemplate('1fr 1fr 2fr')</em> divides the <em>LazyVWaterFlowLayout</em> into 3 columns,
     *     splitting the width into 4 equal parts: column 1 takes 1 part, column 2 takes 1 part,
     *     and column 3 takes 2 parts.
     * @returns { LazyVWaterFlowLayoutAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    columnsTemplate(value: string | ItemFillPolicy | undefined): LazyVWaterFlowLayoutAttribute;
}
/**
 * Defines LazyVWaterFlowLayout Component.
 *
 * @type { LazyVWaterFlowLayoutInterface }
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @uicomponent
 * @since 26.0.0
 */
export declare const LazyVWaterFlowLayout: LazyVWaterFlowLayoutInterface;
/**
 * Defines LazyVWaterFlowLayout Component instance.
 *
 * @type { LazyVWaterFlowLayoutAttribute }
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare const LazyVWaterFlowLayoutInstance: LazyVWaterFlowLayoutAttribute;

```
