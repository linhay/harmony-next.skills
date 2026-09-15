# @ohos.arkui.inspector.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
 * @file Layout Callback
 * @kit ArkUI
 */
import { Callback } from './@ohos.base';
/**
 * Used to do observer layout and draw event for component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice [since 12]
 * @since 10
 */
declare namespace inspector {
    /**
     * The ComponentObserver is used to listen for layout, draw and drawChildren events.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 10
     */
    interface ComponentObserver {
        /**
         * Registers a callback with the corresponding query condition by using the handle.
         * This callback is triggered when the component layout complete.
         *
         * @param { string } type - type of the listened event. [since 10 - 11]
         * @param { ()=>void } callback - callback of the listened event. [since 10 - 11]
         * @param { 'layout' } type - type of the listened event. [since 12]
         * @param { function } callback - callback of the listened event. [since 12]
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'layout', callback: () => void): void;
        /**
         * Deregisters a callback with the corresponding query condition by using the handle.
         * This callback is not triggered when the component layout complete.
         *
         * @param { string } type - type of the listened event. [since 10 - 11]
         * @param { ()=>void } callback - callback of the listened event. [since 10 - 11]
         * @param { 'layout' } type - type of the listened event. [since 12]
         * @param { function } callback - callback of the listened event. [since 12]
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'layout', callback?: () => void): void;
        /**
         * Registers a callback with the corresponding query condition by using the handle.
         * This callback is triggered when the component draw complete.
         *
         * @param { string } type - type of the listened event. [since 10 - 11]
         * @param { ()=>void } callback - callback of the listened event. [since 10 - 11]
         * @param { 'draw' } type - type of the listened event. [since 12]
         * @param { function } callback - callback of the listened event. [since 12]
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'draw', callback: () => void): void;
        /**
         * Deregisters a callback with the corresponding query condition by using the handle.
         * This callback is not triggered when the component draw complete.
         *
         * @param { string } type - type of the listened event. [since 10 - 11]
         * @param { ()=>void } callback - callback of the listened event. [since 10 - 11]
         * @param { 'draw' } type - type of the listened event. [since 12]
         * @param { function } callback - callback of the listened event. [since 12]
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'draw', callback?: () => void): void;
        /**
         * Registers a callback with the corresponding query condition by using the handle.
         * This callback is triggered when the child of component draw complete.
         *
         * @param { 'drawChildren' } type - type of the listened event.
         * @param { Callback<void> } callback - callback of the listened event.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        on(type: 'drawChildren', callback: Callback<void>): void;
        /**
         * Deregisters a callback with the corresponding query condition by using the handle.
         * This callback is not triggered when the child of component draw complete.
         *
         * @param { 'drawChildren' } type - type of the listened event.
         * @param { Callback<void> } callback - callback of the listened event.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        off(type: 'drawChildren', callback?: Callback<void>): void;
        /**
         * Registers a callback with the corresponding query condition by using the handle.
         * This callback is triggered when the child of component draw complete.
         *
         * @param { Callback<number[]> } callback - callback of the listened event.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 24
         */
        onDrawChildren(callback: Callback<number[]>): void;
        /**
         * Deregisters a callback with the corresponding query condition by using the handle.
         * This callback is not triggered when the child of component draw complete.
         *
         * @param { Callback<number[]> } [callback] - callback of the listened event.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 24
         */
        offDrawChildren(callback?: Callback<number[]>): void;
        /**
         * Registers a callback with the corresponding query condition by using the handle.
         * This callback will be triggered when the child of component layout is complete.
         *
         * @param { Callback<void> } callback - callback of the listened event.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 23
         */
        onLayoutChildren(callback: Callback<void>): void;
        /**
         * Deregisters a callback with the corresponding query condition by using the handle.
         * This callback will not be triggered when the child of component layout is complete.
         *
         * @param { Callback<void> } [callback] - callback of the listened event.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 23
         */
        offLayoutChildren(callback?: Callback<void>): void;
    }
    /**
     * Sets the component after layout or draw criteria and returns the corresponding listening handle
     *
     * @param { string } id - component id.
     * @returns { ComponentObserver } create listener for observer component event.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 10
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.UIInspector#createComponentObserver
     */
    function createComponentObserver(id: string): ComponentObserver;
}
export default inspector;

```
