# @ohos.multimedia.systemSoundManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2026 Huawei Device Co., Ltd.
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
 * @kit AudioKit
 */
import type { SystemSoundPlayer as _SystemSoundPlayer } from './multimedia/SystemSoundPlayer';
/**
 * This module provides basic capabilities for managing system sound effects, including defining system sound effect
 * types and obtaining system sound effect players.
 *
 * @syscap SystemCapability.Multimedia.SystemSound.Core
 * @since 23
 */
declare namespace systemSoundManager {
    /**
    * Enumerates the system sound effect types.
    *
    * @syscap SystemCapability.Multimedia.SystemSound.Core
    * @stagemodelonly
    * @since 23
    */
    enum SystemSoundType {
        /**
         * The sound indicates image capture.
         *
         * @syscap SystemCapability.Multimedia.SystemSound.Core
         * @stagemodelonly
         * @since 23
         */
        PHOTO_SHUTTER = 0,
        /**
         * The sound indicates the beginning of video recording.
         *
         * @syscap SystemCapability.Multimedia.SystemSound.Core
         * @stagemodelonly
         * @since 23
         */
        VIDEO_RECORDING_BEGIN = 1,
        /**
         * The sound indicates the end of video recording.
         *
         * @syscap SystemCapability.Multimedia.SystemSound.Core
         * @stagemodelonly
         * @since 23
         */
        VIDEO_RECORDING_END = 2
    }
    /**
     * Creates a SystemSoundPlayer instance. This function uses a promise to return the result.
     * This player can be used to play some system sounds for media or camera actions.
     *
     * @returns { Promise<SystemSoundPlayer | null> } Promise used to return the result.
     *     If the operation is successful, a SystemSoundPlayer instance is returned.
     *     Otherwise, null is returned. The instance is used for loading and playback.
     * @throws { BusinessError } 5400101 - No memory. Return by promise.
     * @syscap SystemCapability.Multimedia.SystemSound.Core
     * @since 23
     */
    function createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>;
    /**
     * Represents the system sound effect player object.
     *
     * @syscap SystemCapability.Multimedia.SystemSound.Core
     * @since 23
     */
    type SystemSoundPlayer = _SystemSoundPlayer;
}
export default systemSoundManager;

```
