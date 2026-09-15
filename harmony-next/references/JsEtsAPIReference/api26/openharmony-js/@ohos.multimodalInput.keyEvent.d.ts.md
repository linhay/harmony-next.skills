# @ohos.multimodalInput.keyEvent.d.ts

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
 * The **keyEvent** module provides key events reported by a device. It is inherited from
 * [InputEvent]{@link @ohos.multimodalInput.inputEvent:InputEvent}.
 *
 * @file Key Event
 * @kit InputKit
 */
import type { InputEvent } from './@ohos.multimodalInput.inputEvent';
import type { KeyCode } from './@ohos.multimodalInput.keyCode';
/**
 * Key event type.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @atomicservice [since 12]
 * @since 9
 */
export declare enum Action {
    /**
     * Cancellation of a key action.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    CANCEL = 0,
    /**
     * Key press.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    DOWN = 1,
    /**
     * Key release.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    UP = 2
}
/**
 * Defines a key.
 *
 * @interface Key [since 9 - 11]
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @atomicservice [since 12]
 * @since 9
 */
export declare interface Key {
    /**
     * Key code.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    code: KeyCode;
    /**
     * Time when the key is pressed, in microseconds (μs) since the system starts.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    pressedTime: number;
    /**
     * Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    deviceId: number;
}
/**
 * Key event.
 *
 * @interface KeyEvent [since 9 - 11]
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @atomicservice [since 12]
 * @since 9
 */
export declare interface KeyEvent extends InputEvent {
    /**
     * Key event type.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    action: Action;
    /**
     * Defines a key.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    key: Key;
    /**
     * Unicode character corresponding to the key.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    unicodeChar: number;
    /**
     * List of pressed keys.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    keys: Key[];
    /**
     * Whether ctrlKey is being pressed.
     *
     * The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    ctrlKey: boolean;
    /**
     * Whether altKey is being pressed.
     *
     * The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    altKey: boolean;
    /**
     * Whether shiftKey is being pressed.
     *
     * The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    shiftKey: boolean;
    /**
     * Whether logoKey is being pressed.
     *
     * The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    logoKey: boolean;
    /**
     * Whether fnKey is being pressed.
     *
     * The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    fnKey: boolean;
    /**
     * Whether capsLock is enabled.
     *
     * The value **true** indicates that capsLock is enabled, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    capsLock: boolean;
    /**
     * Whether numLock is enabled.
     *
     * The value **true** indicates that numLock is enabled, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    numLock: boolean;
    /**
     * Whether scrollLock is enabled.
     *
     * The value **true** indicates that scrollLock is enabled, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @atomicservice [since 12]
     * @since 9
     */
    scrollLock: boolean;
}

```
