# @ohos.graphics.hdrCapability.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
* Copyright (C) 2022-2023 Huawei Device Co., Ltd.
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/
/**
 * @file HDR Capability
 * @kit ArkGraphics2D
 */
/**
 * The hdrCapability module provides enums related to the High Dynamic Range (HDR) capability. The HDR technology
 * significantly expands the dynamic range and color expressiveness of images. It is applicable to scenarios such as
 * video playback and image display. It addresses the issues of overexposure in bright areas and loss of details in dark
 * areas in traditional SDR in high-contrast scenarios, delivering a more authentic and richer visual experience.
 *
 * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
 * @atomicservice [since 12]
 * @since 11
 */
declare namespace hdrCapability {
    /**
     * Enumerates the HDR formats.
     *
     * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
     * @atomicservice [since 12]
     * @since 11
     */
    enum HDRFormat {
        /**
         * Unsupported HDR type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @atomicservice [since 12]
         * @since 11
         */
        NONE = 0,
        /**
         * Videos in Hybrid Log-Gamma (HLG) format.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @atomicservice [since 12]
         * @since 11
         */
        VIDEO_HLG = 1,
        /**
         * Videos in HDR10 format.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @atomicservice [since 12]
         * @since 11
         */
        VIDEO_HDR10 = 2,
        /**
         * Videos in HDR_VIVID format.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @atomicservice [since 12]
         * @since 11
         */
        VIDEO_HDR_VIVID = 3,
        /**
         * Images in HDR_VIVID format, stored in dual JPEG format.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @atomicservice [since 12]
         * @since 11
         */
        IMAGE_HDR_VIVID_DUAL = 4,
        /**
         * Images in HDR_VIVID format, stored in single HEIF format.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @atomicservice [since 12]
         * @since 11
         */
        IMAGE_HDR_VIVID_SINGLE = 5,
        /**
         * Images in HDR_ISO format, stored in dual JPEG format.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @atomicservice [since 12]
         * @since 11
         */
        IMAGE_HDR_ISO_DUAL = 6,
        /**
         * Images in HDR_ISO format, stored in single HEIF format.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @atomicservice [since 12]
         * @since 11
         */
        IMAGE_HDR_ISO_SINGLE = 7,
        /**
         * Videos in AIHDR format.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        VIDEO_AIHDR = 8
    }
}
export default hdrCapability;

```
