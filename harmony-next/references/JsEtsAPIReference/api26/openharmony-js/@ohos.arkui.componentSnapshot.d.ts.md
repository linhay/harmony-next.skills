# @ohos.arkui.componentSnapshot.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
import image from './@ohos.multimedia.image';
import colorSpaceManager from './@ohos.graphics.colorSpaceManager';
/**
 * The **componentSnapshot** module provides APIs for obtaining component snapshots, including snapshots of components
 * that have been loaded and snapshots of components that have not been loaded yet. Snapshots are strictly limited to
 * the component's layout bounds. Content drawn outside the area of the owning component or the parent component is not
 * visible in the snapshots. In addition, sibling components stacked in the component's area are not displayed in the
 * snapshot.
 *
 * Transformation attributes such as scaling, translation, and rotation only apply to the child components of the target
 * component. Applying these transformation attributes directly to the target component itself has no effect; the
 * snapshot will still display the component as it appears before any transformations are applied.
 *
 * For typical use cases (for example, long screenshots) and best practices of component snapshots, see
 * [Using Component Snapshot (ComponentSnapshot)](docroot://ui/arkts-uicontext-component-snapshot.md).
 *
 * > **NOTE**
 * >
 * > - In scenarios where [XComponent]{@link xcomponent} is used to, for example, display video or camera streams,
 * > obtain images through
 * > [createPixelMapFromSurface]{@link @ohos.multimedia.image:image.createPixelMapFromSurface(surfaceId: string, region: Region)},
 * > instead of through an API in this module.
 * >
 * > - If the content of a component does not fill the entire area allocated for it, any remaining space in the snapshot
 * > will be rendered as transparent pixels. In addition, if the component uses [image effects]{@link common} or other
 * > effect-related attributes, the resulting snapshot may not be as expected. To address these potential issues, check
 * > whether the component's transparent content area needs to be filled, or use the window screenshot API
 * > [snapshot]{@link @ohos.window:window.Window#snapshot(callback: AsyncCallback<image.PixelMap>)} instead.
 * >
 * > - You can preview how this component looks on a real device, but not in DevEco Studio Previewer.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice [since 12]
 * @since 10
 */
declare namespace componentSnapshot {
    /**
     * Defines the rectangular region for capturing the component snapshot.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 15
     */
    interface SnapshotRegion {
        /**
         * X-coordinate of the upper left corner of the rectangular region.
         *
         * Unit: px.
         *
         * Value range: [0, Component width].
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        left: number;
        /**
         * X-coordinate of the lower right corner of the rectangular region.
         *
         * Unit: px.
         *
         * Value range: [0, Component width].
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        right: number;
        /**
         * Y-coordinate of the upper left corner of the rectangular region.
         *
         * Unit: px.
         *
         * Value range: [0, Component height].
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        top: number;
        /**
         * Y-coordinate of the lower right corner of the rectangular region.
         *
         * Unit: px.
         *
         * Value range: [0, Component height].
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        bottom: number;
    }
    /**
     * Defines the rectangular region for capturing the component snapshot, with coordinates adjusted based on the layout
     * direction (LTR or RTL).
     *
     * > **NOTE**
     * >
     * > Directly using **componentSnapshot** can lead to the issue of
     * > [ambiguous UI context](docroot://ui/arkts-global-interface.md#ambiguous-ui-context). To avoid this, obtain a
     * > **UIContext** instance using **getUIContext()**, and then obtain the associated **componentSnapshot** object
     * > using
     * > [getComponentSnapshot](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getcomponentsnapshot12).
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 15
     */
    interface LocalizedSnapshotRegion {
        /**
         * For LTR layouts: X-coordinate of the upper left corner of the rectangular region.
         *
         * For RTL layouts: X-coordinate of the upper right corner of the rectangular region.
         *
         * Unit: px.
         *
         * Value range: [0, Component width].
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        start: number;
        /**
         * For LTR layouts: X-coordinate of the lower right corner of the rectangular region.
         *
         * For RTL layouts: X-coordinate of the lower left corner of the rectangular region.
         *
         * Unit: px.
         *
         * Value range: [0, Component width].
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        end: number;
        /**
         * For LTR layouts: Y-coordinate of the upper left corner of the rectangular region.
         *
         * For RTL layouts: Y-coordinate of the upper right corner of the rectangular region.
         *
         * Unit: px.
         *
         * Value range: [0, Component height].
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        top: number;
        /**
         * Y-coordinate of the lower right corner of the rectangular region.
         *
         * Unit: px.
         *
         * Value range: [0, Component height].
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        bottom: number;
    }
    /**
     * Defines the snapshot region rect type.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 15
     */
    type SnapshotRegionType = SnapshotRegion | LocalizedSnapshotRegion;
    /**
     * Defines the color space used for the snapshot.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    interface ColorModeOptions {
        /**
         * Color space used for the snapshot.
         *
         * If the target component's color space is known, specify it through **colorSpace** and set **isAuto** to **false**
         * to achieve optimal snapshot quality.
         *
         * The value can be **DISPLAY_P3**, **SRGB**, or **DISPLAY_BT2020_SRGB** in
         * [colorSpaceManager.ColorSpace]{@link @ohos.graphics.colorSpaceManager:colorSpaceManager.ColorSpace}.
         *
         * Default value: **SRGB**
         *
         * If the value is **undefined**, **null**, or not set, the default value is used. If an abnormal value is used,
         * snapshot capture fails and the error code 160003 is returned.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        colorSpace?: colorSpaceManager.ColorSpace;
        /**
         * Whether the system automatically determines the color space to be used.
         *
         * The value **true** means to allow the system to automatically determine the color space to be used, and **false**
         * means to manually set the color space through **colorSpace**. If an invalid value is used, the default value
         * **false** is used.
         *
         * Default value: **false**
         *
         * For offscreen snapshots, this parameter can only be set to **false**. Otherwise, the error code 160004 will be
         * returned.
         *
         * If `isAuto` is set to **true**, you are advised to set `waitUntilRenderFinished` in
         * [SnapshotOptions]{@link componentSnapshot.SnapshotOptions} to **true** to ensure that the system can properly
         * detect the used color space.
         *
         * If the color space used by the component is uncertain, you are advised to set **isAuto** to **true** so that the
         * system can automatically determine the color space to be used.
         *
         * When **isAuto** is set to true, the value of **colorSpace** is ignored. In this case, if the target component
         * contains child components in different color spaces, the color space with the highest priority is used for the
         * snapshot. The priority order of the color space is as follows: **DISPLAY_BT2020_SRGB** > **DISPLAY_P3** >
         * **SRGB**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        isAuto?: boolean;
    }
    /**
     * Defines the dynamic range mode used for the snapshot.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    interface DynamicRangeModeOptions {
        /**
         * Dynamic range mode used for the snapshot.
         *
         * By default, the system snapshots in [STANDARD]{@link ImageAttribute#dynamicRangeMode} mode. If the dynamic range
         * mode used by the target component is known, you can specify the dynamic range mode using the **dynamicRangeMode**
         * field and set **isAuto** to **false** to achieve the expected snapshot effect.
         *
         * There are three dynamic range modes available. HDR is applied for **HIGH** and **CONSTRAINT** modes, and SDR is
         * applied for **STANDARD** mode.
         *
         * After a valid dynamic range mode is specified, the dynamic range to be used for the snapshot is determined by
         * both the target component and the specified mode. The details are as follows:
         *
         * 1. If SDR is used for the component, SDR is applied for the snapshot even if the dynamic range mode is set to **HIGH**.
         * 2. If HDR is used for the component, the specified dynamic range mode is applied for the screenshot.
         * 3. If the [color space]{@link componentSnapshot.ColorModeOptions} is set to **SRGB** or **DISPLAY_P3**, SDR is applied for the snapshot.
         * 4. If both SDR and HDR are used for the child components, HDR is applied for the snapshot.
         * 5. If both conditions 3 and 4 are met, SDR is applied for the snapshot.
         *
         * For details about the enum values, see [DynamicRangeMode]{@link ImageAttribute#dynamicRangeMode}.
         *
         * Default value: **STANDARD**
         *
         * If the value is **undefined**, **null**, or not set, the default value is used. If an abnormal value is used,
         * snapshot capture fails and the error code 160003 is returned.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        dynamicRangeMode?: DynamicRangeMode;
        /**
         * Whether the system automatically determines the dynamic range mode to be used.
         *
         * The value **true** means to allow the system to automatically determine the dynamic range mode to be used, and
         * **false** means to manually set the dynamic range mode through **dynamicRangeMode**. If an invalid value is used,
         * the default value **false** is used.
         *
         * Default value: **false**
         *
         * For offscreen snapshots, this parameter can only be set to **false**. Otherwise, the error code 160004 will be
         * returned.
         *
         * If `isAuto` is set to **true**, you are advised to set `waitUntilRenderFinished` in
         * [SnapshotOptions]{@link componentSnapshot.SnapshotOptions} to **true** to ensure that the system can properly
         * detect the used dynamic range mode.
         *
         * If the dynamic range mode used by the component is uncertain, you are advised to set **isAuto** to **true** so
         * that the system can automatically determine the dynamic range mode to be used.
         *
         * When **isAuto** is set to true, the value of **dynamicRangeMode** is ignored.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        isAuto?: boolean;
    }
    /**
     * Defines the size limit of a component screenshot.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    interface SnapshotSizeLimitation {
        /**
         * Maximum width of a component screenshot.
         *
         * Value range: (-∞, +∞)
         *
         * Unit: px.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        maxWidth: number;
        /**
         * Maximum height of a component screenshot.
         *
         * Value range: (-∞, +∞)
         *
         * Unit: px.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        maxHeight: number;
    }
    /**
     * Defines the extra options for snapshot taking.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    interface SnapshotOptions {
        /**
         * Scale ratio for rendering pixel maps during a snapshot. Note that a high scale ratio may increase the time taken
         * for the snapshot or even result in a snapshot failure.
         *
         * Value range: [0, +∞). If the value is less than or equal to 0, the default value is used.
         *
         * Default value: **1**
         *
         * **NOTE**
         *
         * Avoid capturing images that are excessively large, ideally not larger than the screen size. If the size of the
         * image to capture exceeds device-specific underlying limits, the capture will fail.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        scale?: number;
        /**
         * Whether to force the system to wait for all rendering commands to complete before taking the snapshot. The value
         * **true** means to force the system to wait for all rendering commands to complete before taking the snapshot, and
         * **false** means the opposite. This option ensures the snapshot reflects the most up-to-date content and should be
         * enabled whenever possible. Note that enabling this option may increase the time required for the snapshot to
         * complete, which depends on the size of the area that needs to be redrawn at the time.
         *
         * Default value: **false**
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        waitUntilRenderFinished?: boolean;
        /**
         * Rectangular region for the snapshot. The default region is the entire component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        region?: SnapshotRegionType;
        /**
         * Color space used for the snapshot.
         *
         * Default value: **{colorSpace: SRGB, isAuto: false}**
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        colorMode?: ColorModeOptions;
        /**
         * Dynamic range mode used for the snapshot.
         *
         * Default value: **{dynamicRangeMode: STANDARD, isAuto: false}**
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        dynamicRangeMode?: DynamicRangeModeOptions;
    }
    /**
     * Obtains the snapshot of a component that has been loaded based on the provided [component ID]{@link common}. This
     * API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > - Since API version 12, you can use the [getComponentSnapshot]{@link @ohos.arkui.UIContext:UIContext#getComponentSnapshot}
     * > API in [UIContext]{@link @ohos.arkui.UIContext} to obtain the [ComponentSnapshot]{@link @ohos.arkui.UIContext:ComponentSnapshot}
     * > object associated with the current UI context.
     * >
     * > - The snapshot captures content rendered in the last frame. If this API is called when the component triggers an
     * > update, the re-rendered content will not be included in the obtained snapshot.
     *
     * @param { string } id - [ID]{@link common} of the target component.
     * @param { AsyncCallback<image.PixelMap> } callback - Callback used to return the result.
     * @param { SnapshotOptions } [options] - Custom settings of the snapshot. [since 12]
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Invalid ID.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 10
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.ComponentSnapshot#get
     */
    function get(id: string, callback: AsyncCallback<image.PixelMap>, options?: SnapshotOptions): void;
    /**
     * Obtains the snapshot of a component that has been loaded based on the provided [component ID]{@link common}. This
     * API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - Since API version 12, you can use the [getComponentSnapshot]{@link @ohos.arkui.UIContext:UIContext#getComponentSnapshot}
     * > API in [UIContext]{@link @ohos.arkui.UIContext} to obtain the [ComponentSnapshot]{@link @ohos.arkui.UIContext:ComponentSnapshot}
     * > object associated with the current UI context.
     * >
     * > - The snapshot captures content rendered in the last frame. If this API is called when the component triggers an
     * > update, the re-rendered content will not be included in the obtained snapshot.
     *
     * @param { string } id - [ID]{@link common} of the target component.
     * @param { SnapshotOptions } [options] - Custom settings of the snapshot. [since 12]
     * @returns { Promise<image.PixelMap> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Invalid ID.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 10
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.ComponentSnapshot#get
     */
    function get(id: string, options?: SnapshotOptions): Promise<image.PixelMap>;
    /**
     * Renders a custom component in the application background and outputs its snapshot. This API uses an asynchronous
     * callback to return the result. The coordinates and size of the offscreen component's drawing area can be obtained
     * through the callback.
     *
     * > **NOTE**
     * >
     * > - Since API version 12, you can use the [getComponentSnapshot]{@link @ohos.arkui.UIContext:UIContext#getComponentSnapshot}
     * > API in [UIContext]{@link @ohos.arkui.UIContext} to obtain the [ComponentSnapshot]{@link @ohos.arkui.UIContext:ComponentSnapshot}
     * > object associated with the current UI context.
     * >
     * > - To account for the time spent in awaiting component building and rendering, the callback of offscreen snapshots
     * > has a delay of less than 500 ms.
     * >
     * > - Components in the builder do not support the setting of animation-related attributes, such as
     * > [transition]{@link common}.
     * >
     * > - If a component is on a time-consuming task, for example, an [Image]{@link image} or [Web]{@link web} component
     * > that is loading online images, its loading may be still in progress when this API is called. In this case, the
     * > output snapshot does not represent the component in the way it looks when the loading is successfully completed.
     *
     * @param { CustomBuilder } builder - Builder of the custom component.<br>Note: The global builder is not supported.<
     *     br>If the root component of the builder has a width or height of zero, the snapshot operation will fail with
     *     error code 100001.
     * @param { AsyncCallback<image.PixelMap> } callback - Callback used to return the result. The coordinates and size of
     *     the offscreen component's drawing area can be obtained through the callback.
     * @param { number } [delay] - Delay time for triggering the screenshot command. When the layout includes an image
     *     component, it is necessary to set a delay time to allow the system to decode the image resources. The decoding
     *     time is subject to the resource size. In light of this, whenever possible, use pixel map resources that do not
     *     require decoding.<br> When pixel map resources are used or when **syncLoad** to **true** for the **Image**
     *     component, you can set **delay** to **0** to forcibly capture snapshots without waiting. This delay time does
     *     not refer to the time from the API call to the return: As the system needs to temporarily construct the passed-
     *     in **builder** offscreen, the return time is usually longer than this delay.<br>Note: In the **builder** passed
     *     in, state variables should not be used to control the construction of child components. If they are used, they
     *     should not change when the API is called, so as to avoid unexpected snapshot results.<br> Default value:
     *     **300**<br> Unit: ms<br> Value range:
     *     [0, +∞). If the value is less than 0, the default value is used. [since 12]
     * @param { boolean } [checkImageStatus] - Whether to verify the image decoding status before taking a snapshot. <br>
     *     **true**: Check whether all Image components have been decoded. <br>**false**: Skip verification. If the
     *     verification is not completed, snapshot capture will be canceled and an exception will be returned.<br>Default
     *     value: **false** [since 12]
     * @param { SnapshotOptions } [options] - Custom settings of the snapshot. [since 12]
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - The builder is not a valid build function.
     * @throws { BusinessError } 160001 - An image component in builder is not ready for taking a snapshot. The check for
     *     the ready state is required when the checkImageStatus option is enabled. [since 12]
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 10
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.ComponentSnapshot#createFromBuilder
     */
    function createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>, delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): void;
    /**
     * Renders a custom component in the application background and outputs its snapshot. This API uses a promise to
     * return the result. The coordinates and size of the offscreen component's drawing area can be obtained through the
     * callback.
     *
     * > **NOTE**
     * >
     * > - Since API version 12, you can use the [getComponentSnapshot]{@link @ohos.arkui.UIContext:UIContext#getComponentSnapshot}
     * > API in [UIContext]{@link @ohos.arkui.UIContext} to obtain the [ComponentSnapshot]{@link @ohos.arkui.UIContext:ComponentSnapshot}
     * > object associated with the current UI context.
     * >
     * > - To account for the time spent in awaiting component building and rendering, the callback of offscreen snapshots
     * > has a delay of less than 500 ms.
     * >
     * > - Components in the builder do not support the setting of animation-related attributes, such as
     * > [transition]{@link common}.
     * >
     * > - If a component is on a time-consuming task, for example, an [Image]{@link image} or [Web]{@link web} component
     * > that is loading online images, its loading may be still in progress when this API is called. In this case, the
     * > output snapshot does not represent the component in the way it looks when the loading is successfully completed.
     *
     * @param { CustomBuilder } builder - Builder of the custom component.<br>Note: The global builder is not supported.<
     *     br>If the root component of the builder has a width or height of zero, the snapshot operation will fail with
     *     error code 100001.
     * @param { number } [delay] - Delay time for triggering the screenshot command. When the layout includes an image
     *     component, it is necessary to set a delay time to allow the system to decode the image resources. The decoding
     *     time is subject to the resource size. In light of this, whenever possible, use pixel map resources that do not
     *     require decoding.<br> When pixel map resources are used or when **syncLoad** to **true** for the **Image**
     *     component, you can set **delay** to **0** to forcibly capture snapshots without waiting. This delay time does
     *     not refer to the time from the API call to the return: As the system needs to temporarily construct the passed-
     *     in **builder** offscreen, the return time is usually longer than this delay.<br>Note: In the **builder** passed
     *     in, state variables should not be used to control the construction of child components. If they are used, they
     *     should not change when the API is called, so as to avoid unexpected snapshot results.<br> Default value:
     *     **300**<br> Unit: ms [since 12]
     * @param { boolean } [checkImageStatus] - Whether to verify the image decoding status before taking a snapshot. <br>
     *     **true**: Check whether all Image components have been decoded. <br>**false**: Skip verification. If the
     *     verification is not completed, snapshot capture will be canceled and an exception will be returned.<br>Default
     *     value: **false** [since 12]
     * @param { SnapshotOptions } [options] - Custom settings of the snapshot. [since 12]
     * @returns { Promise<image.PixelMap> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - The builder is not a valid build function.
     * @throws { BusinessError } 160001 - An image component in builder is not ready for taking a snapshot. The check for
     *     the ready state is required when the checkImageStatus option is enabled. [since 12]
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 10
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.ComponentSnapshot#createFromBuilder
     */
    function createFromBuilder(builder: CustomBuilder, delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): Promise<image.PixelMap>;
    /**
     * Obtains the snapshot of a component that has been loaded based on the provided [component ID]{@link common}. This
     * API synchronously waits for the snapshot to complete and returns a
     * [PixelMap]{@link @ohos.multimedia.image:image.PixelMap} object.
     *
     * > **NOTE**
     * >
     * > The snapshot captures content rendered in the last frame. If this API is called when the component triggers an
     * > update, the re-rendered content will not be included in the obtained snapshot.
     *
     * @param { string } id - [ID]{@link common} of the target component.
     * @param { SnapshotOptions } [options] - Custom settings of the snapshot.
     * @returns { image.PixelMap } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Invalid ID.
     * @throws { BusinessError } 160002 - Timeout.
     * @throws { BusinessError } 160003 - Unsupported color space or dynamic range mode in snapshot options. [since 23]
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function getSync(id: string, options?: SnapshotOptions): image.PixelMap;
}
export default componentSnapshot;

```
