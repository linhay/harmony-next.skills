# @ohos.multimodalInput.inputEvent.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022 Huawei Device Co., Ltd.
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
 * @file Input Event
 * @kit InputKit
 */
/**
 * The **inputEvent** module provides the basic events reported by the device.
 *
 * @interface InputEvent [since 9 - 11]
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @atomicservice [since 12]
 * @since 9
 */
export declare interface InputEvent {
    /**
     * Enumerates event IDs.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    id: number;
    /**
     * Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    deviceId: number;
    /**
     * Time when an input event is reported, in microseconds (μs) since the system starts.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    actionTime: number;
    /**
     * Target screen ID.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    screenId: number;
    /**
     * Target window ID.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    windowId: number;
}

```
