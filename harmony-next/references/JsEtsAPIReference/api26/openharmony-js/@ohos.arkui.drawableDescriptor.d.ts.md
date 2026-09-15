# @ohos.arkui.drawableDescriptor.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2024 Huawei Device Co., Ltd.
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
 * This module provides capabilities for layered icon composition (foreground, background, mask), animated image
 * control, and basic image processing.
 *
 * > **NOTE**
 * >
 * > - You can preview how this component looks on a real device, but not in DevEco Studio Previewer.
 *
 * @file DrawableDescriptor
 * @kit ArkUI
 */
import image from './@ohos.multimedia.image';
import drawing from './@ohos.graphics.drawing';
/**
 * Represents the result of loading an image resource or URI.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 21
 */
export interface DrawableDescriptorLoadedResult {
    /**
     * Image width.
     *
     * Unit: px.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    imageWidth: number;
    /**
     * Image height.
     *
     * Unit: px.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    imageHeight: number;
}
/**
 * Represents the base class providing overridable methods for [PixelMap]{@link @ohos.multimedia.image:image.PixelMap}
 * acquisition and image resource loading.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 10
 */
export class DrawableDescriptor {
    /**
     * Obtains this **PixelMap** instance.
     *
     * @returns { image.PixelMap } **PixelMap** object.
     * @throws { BusinessError } 111002 - The native memory referenced by
     *     the drawableDescriptor has been released. [since 26.0.0]
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    getPixelMap(): image.PixelMap;
    /**
     * Synchronously loads the image resource and returns the loading result.
     *
     * @returns { DrawableDescriptorLoadedResult } Image resource loading result.
     * @throws { BusinessError } 111001 - resource loading failed.
     * @throws { BusinessError } 111002 - The native memory referenced by
     *     the drawableDescriptor has been released. [since 26.0.0]
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    loadSync(): DrawableDescriptorLoadedResult;
    /**
     * Asynchronously loads the image resource and returns the loading result. This API uses a promise to return the
     * result.
     *
     * @returns { Promise<DrawableDescriptorLoadedResult> } Image resource loading result.
     * @throws { BusinessError } 111001 - resource loading failed.
     * @throws { BusinessError } 111002 - The native memory referenced by
     *     the drawableDescriptor has been released. [since 26.0.0]
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    load(): Promise<DrawableDescriptorLoadedResult>;
    /**
     * Releases the resource held by **DrawableDescriptor**. After the **release** API is called, the object becomes
     * unavailable. In this case, if you call APIs such as [getPixelMap]{@link DrawableDescriptor#getPixelMap},
     * [getForeground]{@link LayeredDrawableDescriptor#getForeground},
     * [getBackground]{@link LayeredDrawableDescriptor#getBackground}, [getMask]{@link LayeredDrawableDescriptor#getMask},
     * [loadSync]{@link DrawableDescriptor#loadSync}, and [load]{@link DrawableDescriptor#load} again, error code 111002
     * will be thrown. No crash occurs when the **release** API is called repeatedly.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    release(): void;
    /**
     * Checks whether **DrawableDescriptor** is released. If **true** is returned, the object has been released. In this
     * case, calling APIs such as [getPixelMap]{@link DrawableDescriptor#getPixelMap},
     * [getForeground]{@link LayeredDrawableDescriptor#getForeground},
     * [getBackground]{@link LayeredDrawableDescriptor#getBackground}, [getMask]{@link LayeredDrawableDescriptor#getMask},
     * [loadSync]{@link DrawableDescriptor#loadSync}, and [load]{@link DrawableDescriptor#load} will throw error code 1110
     * 02. If **false** is returned, the object has not been released and can be used normally.
     *
     * @returns { boolean } Whether **DrawableDescriptor** is released. The value **true** indicates that the object is
     *     released, and **false** indicates that the object is not released.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    isReleased(): boolean;
    /**
     * Redraws **DrawableDescriptor**. Currently, this API is supported for the
     * [PictureDrawableDescriptor]{@link PictureDrawableDescriptor} type, and does not take effect for other
     * **DrawableDescriptor** subtypes. If no component is bound to **DrawableDescriptor**, no operation is performed.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    invalidate(): void;
}
/**
 * Creates a **LayeredDrawableDescriptor** object when the passed resource ID or name belongs to a JSON file that
 * contains foreground and background resources. Inherits from
 * [DrawableDescriptor]{@link DrawableDescriptorLoadedResult}.
 *
 * The **drawable.json** file is located under **entry/src/main/resources/base/media** in the project directory. Below
 * shows the file content:
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 10
 */
export class LayeredDrawableDescriptor extends DrawableDescriptor {
    /**
     * A constructor used to create a **LayeredDrawableDescriptor** object.
     *
     * @param { DrawableDescriptor } [foreground] - Options for the foreground image of the layered drawable.
     * @param { DrawableDescriptor } [background] - Options for the background image of the layered drawable.
     * @param { DrawableDescriptor } [mask] - Options for the mask of the layered drawable.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 23]
     * @atomicservice
     * @since 12
     */
    constructor(foreground?: DrawableDescriptor, background?: DrawableDescriptor, mask?: DrawableDescriptor);
    /**
     * Obtains the **DrawableDescriptor** object of the foreground.
     *
     * @returns { DrawableDescriptor } **DrawableDescriptor** object.
     * @throws { BusinessError } 111002 - The native memory referenced by
     *     the drawableDescriptor has been released. [since 26.0.0]
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    getForeground(): DrawableDescriptor;
    /**
     * Obtains the **DrawableDescriptor** object of the background.
     *
     * @returns { DrawableDescriptor } **DrawableDescriptor** object.
     * @throws { BusinessError } 111002 - The native memory referenced by
     *     the drawableDescriptor has been released. [since 26.0.0]
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    getBackground(): DrawableDescriptor;
    /**
     * Obtains the **DrawableDescriptor** object of the mask.
     *
     * @returns { DrawableDescriptor } **DrawableDescriptor** object.
     * @throws { BusinessError } 111002 - The native memory referenced by
     *     the drawableDescriptor has been released. [since 26.0.0]
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    getMask(): DrawableDescriptor;
    /**
     * Sets the blend mode of **LayeredDrawableDescriptor**. If this API is called for multiple times on the same
     * **LayeredDrawableDescriptor** object, only the last call before the drawing completion takes effect. This API does
     * not support dynamic switching. The default drawing order of **LayeredDrawableDescriptor** is background, mask, and
     * foreground. After the blend mode is set, the drawing order changes to background, foreground, and mask. If the
     * specified value is invalid, the default drawing order is used.
     *
     * @param { drawing.BlendMode } mode - Blend mode.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 23
     */
    setBlendMode(mode: drawing.BlendMode): void;
    /**
     * Obtains the built-in clipping path parameters of the system. It is a static method of
     * **LayeredDrawableDescriptor**.
     *
     * @returns { string } String of the clipping path.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    static getMaskClipPath(): string;
}
/**
 * Implements a **PixelMapDrawableDescriptor** object, which can be created by passing in a **PixelMap** object.
 * Inherits from [DrawableDescriptor]{@link DrawableDescriptorLoadedResult}.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform [since 23]
 * @atomicservice
 * @since 12
 */
export class PixelMapDrawableDescriptor extends DrawableDescriptor {
    /**
     * A constructor used to create a **PixelMapDrawableDescriptor** object.
     *
     * @param { image.PixelMap } src - **PixelMap** image data.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 23]
     * @atomicservice
     * @since 12
     */
    constructor(src?: image.PixelMap);
    /**
     * A constructor used to create a **PixelMapDrawableDescriptor** object through the PixelMap type or **ResourceStr**.
     *
     * @param { image.PixelMap | ResourceStr } [src] - **PixelMap** image data. You can use application resources, system
     *     resources, sandbox paths (file://<bundleName>/<sandboxPath>), and Base64 strings to create
     *     **PixelMapDrawableDescriptor** objects.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    constructor(src?: image.PixelMap | ResourceStr);
}
/**
 * Enumerates the stop modes of an animation.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 24
 */
export enum AnimationStopMode {
    /**
     * The animation returns to the first frame when it stops.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 24
     */
    FIRST_FRAME = 0,
    /**
     * The animation stays at the last frame when it stops.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 24
     */
    LAST_FRAME = 1
}
/**
 * Provides the configuration options for animation playback, including the playback duration, number of playback times,
 * and autoplay behavior.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
declare interface AnimationOptions {
    /**
     * Total playback duration for the image sequence.
     *
     * For **PixelMap** arrays, the default value is 1s per image. For local or application resources, the duration is
     * determined by the playback delay embedded in the image resource.
     *
     * Unit: ms.
     *
     * Value range: [0, +∞).
     *
     * Negative values are treated as the default value.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    duration?: number;
    /**
     * Number of playback times for the image sequence.
     *
     * A value of **-1** indicates infinite playback, **0** indicates no playback, and a value greater than 0 represents
     * the number of playback times.
     *
     * The default value is **1**.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    iterations?: number;
    /**
     * Per-frame playback duration. The setting overrides **duration** if specified.
     *
     * If **duration** and **frameDurations** are set, **duration** is ignored.
     *
     * If the value of **frameDurations** is inconsistent with the image count, animation timing distributes across the
     * total duration.
     *
     * Unit: ms.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    frameDurations?: Array<number>;
    /**
     * Whether to enable autoplay.
     *
     * **true** to enable, **false** otherwise.
     *
     * The default value is **true**.
     *
     * @default true
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    autoPlay?: boolean;
    /**
     * Sets the stop mode for an animation.
     *
     * The default value is **AnimationStopMode.FIRST_FRAME**, indicating that the animation returns to the first frame
     * when it stops.
     *
     * @default AnimationStopMode.FIRST_FRAME
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 24
     */
    stopMode?: AnimationStopMode;
}
/**
 * Implements an animation controller object. It provides APIs for playing, stopping, resuming, and pausing animations,
 * as well as querying the status.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 21
 */
export interface AnimationController {
    /**
     * Starts playback from the first frame.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    start(): void;
    /**
     * Stops playback and resets to the first frame.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    stop(): void;
    /**
     * Pauses playback on the current frame.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    pause(): void;
    /**
     * Resumes playback from the current frame.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    resume(): void;
    /**
     * Obtains the current animation playback status.
     *
     * @returns { AnimationStatus } Current animation state: initial, running, paused, or stopped.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    getStatus(): AnimationStatus;
}
/**
 * Defines a descriptor object used to play animated content (for example, **PixelMap** arrays or animated image
 * resources) using the [Image]{@link ./@internal/component/ets/image} component. It inherits from
 * [DrawableDescriptor]{@link DrawableDescriptorLoadedResult}.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export class AnimatedDrawableDescriptor extends DrawableDescriptor {
    /**
     * A constructor used to create an **AnimatedDrawableDescriptor** object.
     *
     * @param { Array<image.PixelMap> } pixelMaps - **PixelMap** image data.
     * @param { AnimationOptions } [options] - Animation options.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    constructor(pixelMaps: Array<image.PixelMap>, options?: AnimationOptions);
    /**
     * A constructor used to create an **AnimatedDrawableDescriptor** object.
     *
     * @param { ResourceStr | Array<image.PixelMap> } src - Animated image source address or
     *     [PixelMap]{@link @ohos.multimedia.image:image.PixelMap} array.<br> The address (**ResourceStr**) supports the
     *     following formats: application resources (**Resource**), sandbox path (file://<bundleName>/<sandboxPath>), and
     *     Base64 string.
     * @param { AnimationOptions } [options] - Animation playback configuration.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    constructor(src: ResourceStr | Array<image.PixelMap>, options?: AnimationOptions);
    /**
     * Obtains the animation controller for playback control.
     *
     * @param { string } [id] - ID of the target component.<br>Optional when the
     *     [Image]{@link ./@internal/component/ets/image} component and **AnimatedDrawableDescriptor** object have a 1:1
     *     relationship.<br>Required when the same **AnimatedDrawableDescriptor** object is bound to multiple
     *     [Image]{@link ./@internal/component/ets/image} components (in this case, you must ensure the ID uniqueness).<br
     *     >This rule is based on the design principle of the animation system: Animation data can be shared across
     *     multiple components, but each component's animation runs independently. Correspondingly, an
     *     **AnimationController** object maintains a strict 1:1 relationship with a component, meaning one component is
     *     paired with exactly one **AnimationController** object.<br>In addition,
     *     [AnimatedDrawableDescriptor]{@link AnimatedDrawableDescriptor} supports the feature for automatically pausing
     *     animation playback when the bound component is not visible (for example, when the component is scrolled out of
     *     the screen or hidden). For specific implementation details, see [onVisibleAreaChange]
     *     {@link CommonMethod#onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback)}.
     * @returns { AnimationController | undefined } Animation controller object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    getAnimationController(id?: string): AnimationController | undefined;
}
/**
 * Provides HDR composition configuration.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @atomicservice
 * @since 26.0.0
 */
declare interface HdrCompositionConfig {
    /**
     * Rectangle area for HDR composition.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    rect: Rectangle;
}
/**
 * Creates a **PictureDrawableDescriptor** object by passing a **Picture** object. This API inherits from
 * [DrawableDescriptor]{@link DrawableDescriptorLoadedResult}.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @atomicservice
 * @since 26.0.0
 */
export class PictureDrawableDescriptor extends DrawableDescriptor {
    /**
     * A constructor used to create a **PictureDrawableDescriptor** object.
     *
     * @param { image.Picture } src - **Picture** object for creating **PictureDrawableDescriptor**.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    constructor(src: image.Picture);
    /**
     * Sets HDR composition.
     *
     * @param { HdrCompositionConfig } config - HDR composition configuration.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    setHdrComposition(config: HdrCompositionConfig): void;
}

```
