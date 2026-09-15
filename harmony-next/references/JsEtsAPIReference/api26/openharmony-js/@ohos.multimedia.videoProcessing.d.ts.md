# @ohos.multimedia.videoProcessing.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2025 Huawei Device Co., Ltd.
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
 * @file Provides the capability of video quality processing.
 * @kit MediaKit
 */
/**
 * Provides the VideoProcessor type, including AIHDR related functions.
 *
 * @syscap SystemCapability.Multimedia.VideoProcessingEngine
 * @stagemodelonly
 * @since 26.0.0
 */
declare namespace videoProcessing {
    /**
     * Provides the AIHDR feature status.
     *
     * @syscap SystemCapability.Multimedia.VideoProcessingEngine
     * @stagemodelonly
     * @since 26.0.0
     */
    interface VideoProcessorAiHdrStatus {
        /**
         * Whether AIHDR is enabled.
         *
         * @syscap SystemCapability.Multimedia.VideoProcessingEngine
         * @stagemodelonly
         * @since 26.0.0
         */
        enabled?: boolean;
    }
    /**
     * Provides the unified video processor status.
     *
     * @syscap SystemCapability.Multimedia.VideoProcessingEngine
     * @stagemodelonly
     * @since 26.0.0
     */
    interface VideoProcessorStatus {
        /**
         * AIHDR status.
         *
         * @syscap SystemCapability.Multimedia.VideoProcessingEngine
         * @stagemodelonly
         * @since 26.0.0
         */
        aiHdr?: VideoProcessorAiHdrStatus;
    }
    /**
     * Status change callback type for video processor notifications.
     *
     * @param { VideoProcessorStatus } status - The type of video processor status.
     * @syscap SystemCapability.Multimedia.VideoProcessingEngine
     * @stagemodelonly
     * @since 26.0.0
     */
    type VideoProcessorStatusCallback = (status: VideoProcessorStatus) => void;
    /**
     * Provides the VideoProcessor type, including AIHDR related functions.
     *
     * @syscap SystemCapability.Multimedia.VideoProcessingEngine
     * @stagemodelonly
     * @since 26.0.0
     */
    interface VideoProcessor {
        /**
         * Gets the current status of video processor features.
         *
         * @returns { Promise<VideoProcessorStatus | undefined> } Promise used to return VideoProcessorStatus or undefined.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.Multimedia.VideoProcessingEngine
         * @stagemodelonly
         * @since 26.0.0
         */
        getStatus(): Promise<VideoProcessorStatus | undefined>;
        /**
         * Registers a listener for video processor status changes.
         *
         * @param { VideoProcessorStatusCallback } [callback] - The callback function to invoke when status changes.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 29200007 - Out of memory.
         * @throws { BusinessError } 29200009 - Input value is invalid.
         * @syscap SystemCapability.Multimedia.VideoProcessingEngine
         * @stagemodelonly
         * @since 26.0.0
         */
        onStatusChange(callback: VideoProcessorStatusCallback): void;
        /**
         * Unregisters a listener for video processor status changes.
         *
         * @param { VideoProcessorStatusCallback } callback - The callback function to remove.
         *     If not provided, all callbacks for this event type will be removed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 29200006 - The operation is not permitted. This may be caused by incorrect status.
         * @throws { BusinessError } 29200009 - Input value is invalid.
         * @syscap SystemCapability.Multimedia.VideoProcessingEngine
         * @stagemodelonly
         * @since 26.0.0
         */
        offStatusChange(callback?: VideoProcessorStatusCallback): void;
    }
    /**
     * Create a video processing instance.
     *
     * @returns { VideoProcessor } Returns the VideoProcessor instance if the operation is successful;
     *     returns null otherwise.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Function createVideoProcessor can not work correctly due to limited device capabilities.
     * @throws { BusinessError } 29200003 - Failed to create video processing instance.
     *     For example, the number of instances exceeds the upper limit.
     * @throws { BusinessError } 29200007 - Out of memory.
     * @syscap SystemCapability.Multimedia.VideoProcessingEngine
     * @stagemodelonly
     * @since 26.0.0
     */
    function createVideoProcessor(): VideoProcessor;
}
export default videoProcessing;

```
