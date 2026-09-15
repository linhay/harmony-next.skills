# @ohos.screenshot.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022 Huawei Device Co., Ltd.
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
import image from './@ohos.multimedia.image';
/**
 * Provides the screen capture capability.
 *
 * @syscap SystemCapability.WindowManager.WindowManager.Core
 * @atomicservice
 * @since 12
 */
declare namespace screenshot {
    /**
     * Takes a screenshot of the entire screen. This API uses a promise to return the result.
     *
     * This API allows you to take screenshots of different screens by setting various **displayId** values, but only full
     * -screen captures are supported. The [pick]{@link screenshot.pick} API allows you to take screenshots of a specified
     * region.
     *
     * @permission ohos.permission.CUSTOM_SCREEN_CAPTURE [since 14 - 21]
     * @permission ohos.permission.CUSTOM_SCREEN_CAPTURE or ohos.permission.CUSTOM_SCREEN_RECORDING [since 22]
     * @param { CaptureOption } options - Capture options. If this parameter is left blank, the display with ID 0 is
     *     captured by default. [since 14 - 21]
     * @param { CaptureOption } [options] - Capture options. If this parameter is left blank, the display with ID 0 is
     *     captured by default. [since 22]
     * @returns { Promise<image.PixelMap> } Promise used to return a PixelMap object.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Incorrect parameter types.
     *     2.Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 1400003 - This display manager service works abnormally.
     * @syscap SystemCapability.WindowManager.WindowManager.Core
     * @atomicservice
     * @since 14
     */
    function capture(options?: CaptureOption): Promise<image.PixelMap>;
    /**
     * Obtains this screenshot. Currently, only the screenshot of the display whose ID is **0** can be obtained. (If a
     * screenshot of the extended screen is needed, you can use the [capture]{@link screenshot.capture} API.) This API
     * uses a promise to return the result.
     *
     * @returns { Promise<PickInfo> } Promise used to return the PickInfo object.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 1400003 - This display manager service works abnormally.
     * @syscap SystemCapability.WindowManager.WindowManager.Core
     * @atomicservice
     * @since 12
     */
    function pick(): Promise<PickInfo>;
    /**
     * Describes the screenshot options.
     *
     * @syscap SystemCapability.WindowManager.WindowManager.Core
     * @atomicservice
     * @since 12
     */
    interface PickInfo {
        /**
         * Region of the screen to capture.
         *
         * @syscap SystemCapability.WindowManager.WindowManager.Core
         * @atomicservice
         * @since 12
         */
        pickRect: Rect;
        /**
         * PixelMap object of the captured image.
         *
         * @syscap SystemCapability.WindowManager.WindowManager.Core
         * @atomicservice
         * @since 12
         */
        pixelMap: image.PixelMap;
    }
    /**
     * Describes the region of the screen to capture.
     *
     * @syscap SystemCapability.WindowManager.WindowManager.Core
     * @atomicservice
     * @since 12
     */
    interface Rect {
        /**
         * Left boundary of the screen region to capture, in px. The value must be a non-negative integer.
         *
         * @syscap SystemCapability.WindowManager.WindowManager.Core
         * @atomicservice
         * @since 12
         */
        left: number;
        /**
         * Top boundary of the screen region to capture, in px. The value must be a non-negative integer.
         *
         * @syscap SystemCapability.WindowManager.WindowManager.Core
         * @atomicservice
         * @since 12
         */
        top: number;
        /**
         * Width of the screen region to capture, in px. The value must be a positive integer.
         *
         * @syscap SystemCapability.WindowManager.WindowManager.Core
         * @atomicservice
         * @since 12
         */
        width: number;
        /**
         * Height of the screen region to capture, in px. The value must be a positive integer.
         *
         * @syscap SystemCapability.WindowManager.WindowManager.Core
         * @atomicservice
         * @since 12
         */
        height: number;
    }
    /**
     * Describes the capture options.
     *
     * @syscap SystemCapability.WindowManager.WindowManager.Core
     * @atomicservice
     * @since 14
     */
    interface CaptureOption {
        /**
         * ID of the [display]{@link @ohos.display:display.DisplayState} to capture. The default value is **0**. The value
         * must be an integer greater than or equal to 0. If a non-integer is passed, error code 401 is reported.
         *
         * @syscap SystemCapability.WindowManager.WindowManager.Core
         * @atomicservice
         * @since 14
         */
        displayId?: number;
        /**
         * List of window IDs that are not displayed during screen capture. By default, this list is empty. Valid window IDs
         * must be positive integers. Currently, this parameter applies only to
         * [floating ball windows]{@link @ohos.window.floatingBall:floatingBall}. If a window ID does not correspond to a
         * floating ball window, is not a positive integer, or does not exist, error code 401 is reported. You are advised
         * to call
         * [getFloatingBallWindowInfo()]{@link @ohos.window.floatingBall:floatingBall.FloatingBallController.getFloatingBallWindowInfo}
         * to obtain the window ID of a floating ball window.
         *
         * @syscap SystemCapability.WindowManager.WindowManager.Core
         * @atomicservice
         * @since 21
         */
        blackWindowIds?: Array<number>;
    }
}
export default screenshot;

```
