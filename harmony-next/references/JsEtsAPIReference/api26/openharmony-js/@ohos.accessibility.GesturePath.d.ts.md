# @ohos.accessibility.GesturePath.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2025 Huawei Device Co., Ltd.
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
 * @kit AccessibilityKit
 */
import type { GesturePoint } from './@ohos.accessibility.GesturePoint';
/**
 * The **GesturePath** module provides APIs for creating gesture path information required for an accessibility
 * application to inject gestures.
 *
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @since 9
 */
export declare class GesturePath {
    /**
     * Defines a constructor used to create a **GesturePath** instance.
     *
     * @param { number } durationTime - Total gesture duration, in milliseconds.
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 9
     * @deprecated since 12
     */
    constructor(durationTime: number);
    /**
     * Gesture touch point.
     *
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 9
     */
    points: Array<GesturePoint>;
    /**
     * Total gesture duration, in milliseconds.
     *
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 9
     */
    durationTime: number;
}

```
