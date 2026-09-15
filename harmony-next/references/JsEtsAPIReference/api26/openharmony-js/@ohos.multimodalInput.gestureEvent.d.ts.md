# @ohos.multimodalInput.gestureEvent.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
 * Defines a pinch event.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 10
 */
export declare interface Pinch {
    /**
     * Gesture event type, for example, gesture start, gesture update, or gesture end.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 10
     */
    type: ActionType;
    /**
     * Pinch scale factor. The value is greater than or equal to 0.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 10
     */
    scale: number;
}
/**
 * Defines a rotation gesture event.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 11
 */
export declare interface Rotate {
    /**
     * Gesture event type, for example, gesture start, gesture update, or gesture end.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 11
     */
    type: ActionType;
    /**
     * Rotation angle, in degrees.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 11
     */
    angle: number;
}
/**
 * Defines a three-finger swipe gesture event.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 10
 */
export declare interface ThreeFingersSwipe {
    /**
     * Gesture event type, for example, gesture start, gesture update, or gesture end.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 10
     */
    type: ActionType;
    /**
     * X coordinate, in px.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 10
     */
    x: number;
    /**
     * Y coordinate, in px.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 10
     */
    y: number;
}
/**
 * Defines a four-finger swipe gesture event.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 10
 */
export declare interface FourFingersSwipe {
    /**
     * Gesture event type, for example, gesture start, gesture update, or gesture end.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 10
     */
    type: ActionType;
    /**
     * X coordinate, in px.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 10
     */
    x: number;
    /**
     * Y coordinate, in px.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 10
     */
    y: number;
}
/**
 * Defines a three-finger tap gesture event.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 11
 */
export declare interface ThreeFingersTap {
    /**
     * Gesture event type, for example, gesture start, gesture update, or gesture end.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 11
     */
    type: ActionType;
}
/**
 * Enumerates gesture event types.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 10
 */
export declare enum ActionType {
    /**
     * Canceled.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 10
     */
    CANCEL = 0,
    /**
     * Started.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 10
     */
    BEGIN = 1,
    /**
     * Updated.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 10
     */
    UPDATE = 2,
    /**
     * Ended.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 10
     */
    END = 3
}

```
