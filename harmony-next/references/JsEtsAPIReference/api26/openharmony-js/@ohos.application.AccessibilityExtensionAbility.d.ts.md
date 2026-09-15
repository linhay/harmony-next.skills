# @ohos.application.AccessibilityExtensionAbility.d.ts

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
 * The **AccessibilityExtensionAbility** module provides accessibility extension capabilities based on the
 * ExtensionAbility framework.
 *
 * @file
 * @kit AccessibilityKit
 */
import type accessibility from './@ohos.accessibility';
import type { KeyEvent } from './@ohos.multimodalInput.keyEvent';
import type { AccessibilityElement as _AccessibilityElement, ElementAttributeValues as _ElementAttributeValues, FocusDirection as _FocusDirection, FocusType as _FocusType, WindowType as _WindowType, Rect as _Rect } from './application/AccessibilityExtensionContext';
import type * as _AccessibilityExtensionContext from './application/AccessibilityExtensionContext';
/**
 * Indicates an accessibility element. For details, see
 * [AccessibilityElement]{@link ./application/AccessibilityExtensionContext:AccessibilityElement}.
 *
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @since 10
 */
export type AccessibilityElement = _AccessibilityElement;
/**
 * Provides attribute names and value types of a node element. For details, see
 * [ElementAttributeValues]{@link ./application/AccessibilityExtensionContext:ElementAttributeValues}.
 *
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @since 10
 */
export type ElementAttributeValues = _ElementAttributeValues;
/**
 * Enumerates the focus directions. For details, see
 * [FocusDirection]{@link ./application/AccessibilityExtensionContext:FocusDirection}.
 *
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @since 10
 */
export type FocusDirection = _FocusDirection;
/**
 * Describes the attribute name of
 * [ElementAttributeValues]{@link ./application/AccessibilityExtensionContext:ElementAttributeValues}.
 *
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @since 10
 */
export type ElementAttributeKeys = keyof ElementAttributeValues;
/**
 * Enumerates the focus types. For details, see [FocusType]{@link ./application/AccessibilityExtensionContext:FocusType}
 * .
 *
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @since 10
 */
export type FocusType = _FocusType;
/**
 * Enumerates the window types. For details, see
 * [WindowType]{@link ./application/AccessibilityExtensionContext:WindowType}.
 *
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @since 10
 */
export type WindowType = _WindowType;
/**
 * Defines a rectangle. For details, see [Rect]{@link ./application/AccessibilityExtensionContext:Rect}.
 *
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @since 10
 */
export type Rect = _Rect;
/**
 * Defines the context of the accessibility extension. For details, see
 * [AccessibilityExtensionContext]{@link ./application/AccessibilityExtensionContext}.
 *
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @since 10
 */
export type AccessibilityExtensionContext = _AccessibilityExtensionContext.default;
/**
 * The **AccessibilityExtensionAbility** module provides accessibility extension capabilities based on the
 * ExtensionAbility framework.
 *
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @since 9
 */
declare class AccessibilityExtensionAbility {
    /**
     * Context of the accessibility extension ability.
     *
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 9
     */
    context: AccessibilityExtensionContext;
    /**
     * Called when the **AccessibilityExtensionAbility** is enabled and connected to the system service. In this API, you
     * can have the service logic initialized. This API can be overridden as required.
     *
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 9
     * @deprecated since 12
     */
    onConnect(): void;
    /**
     * Called when the **AccessibilityExtensionAbility** is disabled and disconnected from the system service. In this API
     * , you can implement the service logic of resource release and exit. This API can be overridden as required.
     *
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 9
     * @deprecated since 12
     */
    onDisconnect(): void;
    /**
     * Called when an event that matches the specified bundle and event type occurs. In this API, you can implement event-
     * specific service logic. Generally, this API needs to be overridden.
     *
     * @param { AccessibilityEvent } event - Accessibility event. No return value.
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 9
     * @deprecated since 12
     */
    onAccessibilityEvent(event: AccessibilityEvent): void;
    /**
     * Called when a physical key is pressed. In this API, you can determine whether to consume the event based on the
     * service.
     *
     * @param { KeyEvent } keyEvent - Key event. If **true** is returned, the key is consumed.
     * @returns { boolean } Returns **true** if the event is consumed and will not be transferred;<br>returns **false** if
     *     the event is not consumed and will be transferred.
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 9
     * @deprecated since 12
     */
    onKeyEvent(keyEvent: KeyEvent): boolean;
}
export default AccessibilityExtensionAbility;
/**
 * Defines an accessibility event.
 *
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @since 9
 */
export declare interface AccessibilityEvent {
    /**
     * Event type.
     *
     * **EventType**: accessibility event type.
     *
     * **WindowUpdateType**: window update type.
     *
     * **TouchGuideType**: touch guide type.
     *
     * **GestureType**: gesture type.
     *
     * **PageUpdateType**: page update type.
     *
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 9
     */
    eventType: accessibility.EventType | accessibility.WindowUpdateType | TouchGuideType | GestureType | PageUpdateType;
    /**
     * Target component where the event occurs.
     *
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 9
     */
    target?: AccessibilityElement;
    /**
     * Timestamp of the event, in milliseconds. The default value is **0**.
     *
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 9
     */
    timeStamp?: number;
    /**
     * Component ID for auto-focusing. The default value is **0**.
     *
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 12
     */
    elementId?: number;
    /**
     * Content for auto-broadcasting. Set the broadcast content based on the actual scenario. No special restrictions.
     *
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 12
     */
    textAnnouncedForAccessibility?: string;
    /**
     * Added or deleted text content carried by the **TextArea**, **TextInput**, **SearchField**, or **RichEdit**
     * component. Set this parameter based on site requirements. No special restrictions.
     *
     * @syscap SystemCapability.BarrierFree.Accessibility.Core
     * @since 20
     */
    extraInfo?: string;
}
/**
 * Enumerates gesture types.
 *
 * @unionmember { 'left' } Left gesture.
 * @unionmember { 'leftThenRight' } Left-then-right gesture.
 * @unionmember { 'leftThenUp' } Left-then-up gesture.
 * @unionmember { 'leftThenDown' } Left-then-down gesture.
 * @unionmember { 'right' } Right gesture.
 * @unionmember { 'rightThenLeft' } Right-then-left gesture.
 * @unionmember { 'rightThenUp' } Right-then-up gesture.
 * @unionmember { 'rightThenDown' } Right-then-down gesture.
 * @unionmember { 'up' } Up gesture.
 * @unionmember { 'upThenLeft' } Up-then-left gesture.
 * @unionmember { 'upThenRight' } Up-then-right gesture.
 * @unionmember { 'upThenDown' } Up-then-down gesture.
 * @unionmember { 'down' } Down gesture.
 * @unionmember { 'downThenLeft' } Down-then-left gesture.
 * @unionmember { 'downThenRight' } Down-then-right gesture.
 * @unionmember { 'downThenUp' } Down-then-up gesture.
 * @unionmember { 'twoFingerSingleTap' } Two-finger single-tap gesture. [since 11]
 * @unionmember { 'twoFingerDoubleTap' } Two-finger double-tap gesture. [since 11]
 * @unionmember { 'twoFingerDoubleTapAndHold' } Two-finger double-tap-and-hold gesture. [since 11]
 * @unionmember { 'twoFingerTripleTap' } Two-finger triple-tap gesture. [since 11]
 * @unionmember { 'twoFingerTripleTapAndHold' } Two-finger triple-tap-and-hold gesture. [since 11]
 * @unionmember { 'threeFingerSingleTap' } Three-finger single-tap gesture. [since 11]
 * @unionmember { 'threeFingerDoubleTap' } Three-finger double-tap gesture. [since 11]
 * @unionmember { 'threeFingerDoubleTapAndHold' } Three-finger double-tap-and-hold gesture. [since 11]
 * @unionmember { 'threeFingerTripleTap' } Three-finger triple-tap gesture. [since 11]
 * @unionmember { 'threeFingerTripleTapAndHold' } Three-finger triple-tap-and-hold gesture. [since 11]
 * @unionmember { 'fourFingerSingleTap' } Four-finger single-tap gesture. [since 11]
 * @unionmember { 'fourFingerDoubleTap' } Four-finger double-tap gesture. [since 11]
 * @unionmember { 'fourFingerDoubleTapAndHold' } Four-finger double-tap-and-hold gesture. [since 11]
 * @unionmember { 'fourFingerTripleTap' } Four-finger triple-tap gesture. [since 11]
 * @unionmember { 'fourFingerTripleTapAndHold' } Four-finger triple-tap-and-hold gesture. [since 11]
 * @unionmember { 'threeFingerSwipeUp' } Three-finger swipe-up gesture. [since 11]
 * @unionmember { 'threeFingerSwipeDown' } Three-finger swipe-down gesture. [since 11]
 * @unionmember { 'threeFingerSwipeLeft' } Three-finger swipe-left gesture. [since 11]
 * @unionmember { 'threeFingerSwipeRight' } Three-finger swipe-right gesture. [since 11]
 * @unionmember { 'fourFingerSwipeUp' } Four-finger swipe-up gesture. [since 11]
 * @unionmember { 'fourFingerSwipeDown' } Four-finger swipe-down gesture. [since 11]
 * @unionmember { 'fourFingerSwipeLeft' } Four-finger swipe-left gesture. [since 11]
 * @unionmember { 'fourFingerSwipeRight' } Four-finger swipe-right gesture. [since 11]
 * @unionmember {'oneFingerDoubleTap'} [since 26.0.0]
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @stagemodelonly
 * @since 9
 */
type GestureType = 'left' | 'leftThenRight' | 'leftThenUp' | 'leftThenDown' | 'right' | 'rightThenLeft' | 'rightThenUp' | 'rightThenDown' | 'up' | 'upThenLeft' | 'upThenRight' | 'upThenDown' | 'down' | 'downThenLeft' | 'downThenRight' | 'downThenUp' | 'twoFingerSingleTap' | 'twoFingerDoubleTap' | 'twoFingerDoubleTapAndHold' | 'twoFingerTripleTap' | 'twoFingerTripleTapAndHold' | 'threeFingerSingleTap' | 'threeFingerDoubleTap' | 'threeFingerDoubleTapAndHold' | 'threeFingerTripleTap' | 'threeFingerTripleTapAndHold' | 'fourFingerSingleTap' | 'fourFingerDoubleTap' | 'fourFingerDoubleTapAndHold' | 'fourFingerTripleTap' | 'fourFingerTripleTapAndHold' | 'threeFingerSwipeUp' | 'threeFingerSwipeDown' | 'threeFingerSwipeLeft' | 'threeFingerSwipeRight' | 'fourFingerSwipeUp' | 'fourFingerSwipeDown' | 'fourFingerSwipeLeft' | 'fourFingerSwipeRight' | 'oneFingerDoubleTap';
/**
 * Enumerates the page update types.
 *
 * @unionmember { 'pageContentUpdate' } Update of the page content.
 * @unionmember { 'pageStateUpdate' } Update of the page status.
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @since 9
 */
type PageUpdateType = 'pageContentUpdate' | 'pageStateUpdate';
/**
 * Enumerates the touch guide event types.
 *
 * @unionmember { 'touchBegin' } Start of touch.
 * @unionmember { 'touchEnd' } End of touch.
 * @unionmember { 'touchGuideGesture' } Event indicating the touchGuide gesture. [since 26.0.0]
 * @syscap SystemCapability.BarrierFree.Accessibility.Core
 * @since 9
 */
type TouchGuideType = 'touchBegin' | 'touchEnd' | 'touchGuideGesture';

```
