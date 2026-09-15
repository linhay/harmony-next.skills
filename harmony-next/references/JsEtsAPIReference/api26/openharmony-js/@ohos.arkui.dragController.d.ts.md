# @ohos.arkui.dragController.d.ts

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
 * @file
 * @kit ArkUI
 */
import type { AsyncCallback, Callback } from './@ohos.base';
import type unifiedDataChannel from './@ohos.data.unifiedDataChannel';
/**
 * This module provides APIs for initiating drag actions. When receiving a gesture event, such as a touch or long-press
 * event, an application can initiate a drag action and carry drag information therein.
 *
 * > **NOTE**
 * >
 * > - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used
 * > where [the UI context is ambiguous](docroot://ui/arkts-global-interface.md#ambiguous-ui-context). For details, see
 * > [UIContext]{@link @ohos.arkui.UIContext}.
 * >
 * > - You can preview how this component looks on a real device, but not in DevEco Studio Previewer.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform [since 18]
 * @atomicservice [since 12]
 * @since 10
 */
declare namespace dragController {
    /**
     * Describes the dragging start and end states.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 18]
     * @atomicservice [since 12]
     * @since 11
     */
    const enum DragStatus {
        /**
         * Dragging is started.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        STARTED = 0,
        /**
         * Dragging ends.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        ENDED = 1
    }
    /**
     * Provides the data reported when the state changes during dragging.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 18]
     * @atomicservice [since 12]
     * @since 11
     */
    interface DragAndDropInfo {
        /**
         * Current dragging state (started or ended).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        status: DragStatus;
        /**
         * Drag event corresponding to the current state. The drag event initiated by **dragController** only supports the
         * APIs for obtaining the result and behavior, and is used exclusively for the dragging end state.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        event: DragEvent;
        /**
         * Additional information about the drag action. Not supported currently. The default value is null.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        extraParams?: string;
    }
    /**
     * Implements a **DragAction** object to subscribe to drag state changes and start the drag service.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 18]
     * @atomicservice [since 12]
     * @since 11
     */
    interface DragAction {
        /**
         * Starts the drag service. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 100001 - Internal handling failed.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        startDrag(): Promise<void>;
        /**
         * Subscribes to drag state changes.
         *
         * @param { 'statusChange' } type for status changing
         * @param { Callback<DragAndDropInfo> } callback with drag event and status information
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'statusChange', callback: Callback<DragAndDropInfo>): void;
        /**
         * Unsubscribes from drag state changes.
         *
         * @param { 'statusChange' } type for status changing
         * @param { Callback<DragAndDropInfo> } callback with drag event and status information
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'statusChange', callback?: Callback<DragAndDropInfo>): void;
    }
    /**
     * Defines the attributes required for initiating a drag action and information carried in the dragging process.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 18]
     * @atomicservice [since 12]
     * @since 10
     */
    interface DragInfo {
        /**
         * ID of the touch point on the screen when dragging is started. The value is an integer in the [0, 9] range.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 10
         */
        pointerId: number;
        /**
         * Data carried in the dragging process.
         *
         * The default value is null.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 10
         */
        data?: unifiedDataChannel.UnifiedData;
        /**
         * Additional information about the drag action. Not supported currently.
         *
         * The default value is null.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 10
         */
        extraParams?: string;
        /**
         * Coordinates of the touch point. If this parameter is not set, the touch point is centered horizontally and
         * shifted downward by 20% from the top.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        touchPoint?: TouchPoint;
        /**
         * Processing mode of the drag preview and the display of the number badge during dragging.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        previewOptions?: DragPreviewOptions;
        /**
         * Unique ID of the component that is automatically hidden by the system during proactive dragging. A single unique
         * ID or an array of unique IDs can be passed.
         *
         * After the proactive dragging is successfully initiated, the system automatically hides the target component
         * before displaying the drag preview window.
         *
         * If the proactive dragging source also needs to be hidden, its unique ID must be passed as well.
         *
         * The unique ID of a component can be obtained by using [UIContext.getFrameNodeById()]{@link @ohos.arkui.UIContext:UIContext#getFrameNodeById}
         * together with [FrameNode.getUniqueId()]{@link FrameNode:FrameNode#getUniqueId}.
         *
         * You need to restore the component display status as required in the drag end callback.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        autoHideComponentUniqueIds?: number | number[];
        /**
         * Parameters for deferred data loading from the drag source. This API provides data loading parameters to the
         * system instead of directly providing complete data objects. When the user drops data on the target application,
         * the system will use these parameters to request the actual data from the drag source. If set together with
         * **data**, **dataLoadParams** takes effect.
         *
         * The default value is null.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 20
         */
        dataLoadParams?: unifiedDataChannel.DataLoadParams;
    }
    /**
     * Defines parameters related to drag-and-drop animation effects.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 18]
     * @atomicservice [since 12]
     * @since 11
     */
    interface AnimationOptions {
        /**
         * Animation duration, in ms.
         *
         * Default value: **1000**
         *
         * **NOTE**
         *
         * - If this parameter is set to a value less than 0, the value **0** is used.
         * - Floating-point values will be rounded down to integers. For example, if the value set is 1.2, **1** will be
         * used.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        duration?: number;
        /**
         * Animation curve.
         *
         * Default value: **Curve.EaseInOut**
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        curve?: Curve | ICurve;
    }
    /**
     * Implements a **DragPreview** object. This API does not work in the **OnDrop** and **OnDragEnd** callbacks.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 18]
     * @atomicservice [since 12]
     * @since 11
     */
    export class DragPreview {
        /**
         * Sets the foreground color of the drag preview. This API does not work in the **OnDrop** and **OnDragEnd**
         * callbacks. It can only be used on the object obtained through the
         * [getDragPreview()]{@link @ohos.arkui.UIContext:DragController#getDragPreview} API.
         *
         * @param { ResourceColor } color - Foreground color of the drag preview.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        setForegroundColor(color: ResourceColor): void;
        /**
         * Applies a foreground color animation to the drag preview. This API does not work in the **OnDrop** and
         * **OnDragEnd** callbacks. It can only be used on the object obtained through the
         * [getDragPreview()]{@link @ohos.arkui.UIContext:DragController#getDragPreview} API.
         *
         * @param { AnimationOptions } options - Animation settings.
         * @param { function } handler - Callback used to change attributes such as the background mask color.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 11
         */
        animate(options: AnimationOptions, handler: () => void): void;
    }
    /**
     * Callback used to return the result.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 18]
     * @atomicservice
     * @since 12
     */
    interface DragEventParam {
        /**
         * Drag event information that includes only the drag result.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 10
         */
        event: DragEvent;
        /**
         * Additional information about the drag action. Not supported currently.
         *
         * The default value is null.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 18]
         * @atomicservice [since 12]
         * @since 10
         */
        extraParams: string;
    }
    /**
     * Initiates a drag action, with the object to be dragged and the drag information passed in. This API uses an
     * asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > Since API version 11, you can use the [getDragController]{@link @ohos.arkui.UIContext:UIContext#getDragController} API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [DragController]{@link @ohos.arkui.UIContext:DragController} object
     * > associated with the current UI context.
     *
     * @param { CustomBuilder | DragItemInfo } custom - Object to be dragged.<br>**NOTE**<br>The global builder is not
     *     supported. If the [Image]{@link image} component is used in the builder, enable synchronous loading, that is,
     *     set the [syncLoad]{@link ImageAttribute#syncLoad} attribute of the component to **true**. The builder is used
     *     only to generate the image displayed during the current dragging. If the root component of the builder has zero
     *     width or height, it will cause failure in drag image generation, which in turn breaks the entire drag
     *     operation. Changes to the builder, if any, apply to the next dragging, but not to the current dragging.
     * @param { DragInfo } dragInfo - Drag information.
     * @param { AsyncCallback<{ event: DragEvent, extraParams: string }> } callback - Callback function. If the operation
     *     is successful, **err** is **undefined** and **data** is the **DragEventParam** object obtained. Otherwise,
     *     **err** is an error object. [since 10 - 11]
     * @param { AsyncCallback<DragEventParam> } callback - Callback function. If the operation is successful, **err** is
     *     **undefined** and **data** is the **DragEventParam** object obtained. Otherwise, **err** is an error
     *     object. [since 12]
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal handling failed.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 18]
     * @atomicservice [since 12]
     * @since 10
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.DragController#executeDrag
     */
    function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo, callback: AsyncCallback<DragEventParam>): void;
    /**
     * Initiates a drag action, with the object to be dragged and the drag information passed in. This API uses a promise
     * to return the result.
     *
     * > **NOTE**
     * >
     * > Since API version 11, you can use the [getDragController]{@link @ohos.arkui.UIContext:UIContext#getDragController} API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [DragController]{@link @ohos.arkui.UIContext:DragController} object
     * > associated with the current UI context.
     *
     * @param { CustomBuilder | DragItemInfo } custom - Object to be dragged.
     * @param { DragInfo } dragInfo - Drag information.
     * @returns { Promise<{ event: DragEvent, extraParams: string }> } Promise used to return the result. [since 10 - 11]
     * @returns { Promise<DragEventParam> } A Promise with the drag event information. [since 12]
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal handling failed.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 18]
     * @atomicservice [since 12]
     * @since 10
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.DragController#executeDrag
     */
    function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo): Promise<DragEventParam>;
    /**
     * Initiates a drag action, with the object to be dragged and the drag information passed in. This API uses a promise
     * to return the result.
     *
     * > **NOTE**
     * >
     * > - Since API version 11, you can use the
     * > [getDragController]{@link @ohos.arkui.UIContext:UIContext#getDragController} API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the
     * > [DragController]{@link @ohos.arkui.UIContext:DragController} object associated with the current UI context.
     * >
     * > - For optimal drag and drop performance, limit the number of drag previews.
     *
     * @param { Array<CustomBuilder | DragItemInfo> } customArray - Object to be dragged.
     * @param { DragInfo } dragInfo - Drag information.
     * @returns { DragAction } **DragAction** object, which is used to subscribe to drag state changes and start the
     *     drag service.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal handling failed.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 18]
     * @atomicservice [since 12]
     * @since 11
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.DragController#createDragAction
     */
    function createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: DragInfo): DragAction;
    /**
     * Obtains the **DragPreview** object, which represents the preview displayed during a drag operation.
     *
     * > **NOTE**
     * >
     * > Since API version 11, you can use the [getDragController]{@link @ohos.arkui.UIContext:UIContext#getDragController} API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [DragController]{@link @ohos.arkui.UIContext:DragController} object
     * > associated with the current UI context.
     *
     * @returns { DragPreview } **DragPreview** object. It provides the API for setting the preview style. It does not
     *     work in the **OnDrop** and **OnDragEnd** callbacks.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 18]
     * @atomicservice [since 12]
     * @since 11
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.DragController#getDragPreview
     */
    function getDragPreview(): DragPreview;
    /**
     * Enumerates the states defining whether an application can initiate a drag operation. This API is effective only
     * when [onDragStart]{@link CommonMethod#onDragStart} is called.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 18
     */
    const enum DragStartRequestStatus {
        /**
         * The application is preparing data and cannot initiate a drag operation yet.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 18
         */
        WAITING = 0,
        /**
         * The application has completed data preparation and is ready to initiate a drag operation.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 18
         */
        READY = 1
    }
    /**
     * Enumerates hover detection states during drag operations.
     * Under default system configuration, if no CANCEL occurs, the state reporting is as follows:
     * Hover still-->500ms-->BEGIN-->100ms-->UPDATE-->100ms-->UPDATE-->100ms-->UPDATE-->100ms-->END
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    const enum DragSpringLoadingState {
        /**
         * Initial state when a dragged item enters the component boundary and remains stationary for the specified
         * duration. This state enables preparation operations.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        BEGIN,
        /**
         * Periodic notification state during sustained hover detection. In this state, periodic updates refresh UI effects
         * to highlight the hover state.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        UPDATE,
        /**
         * Final state indicating completion of the hover detection cycle, which is triggered when the dragged item remains
         * stationary after the last update notification. Hover detection will only restart after the dragged item exits and
         * re-enters the component boundary or enters a child component. In this state, the application can perform cleanup,
         * navigation, or view switching operations.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        END,
        /**
         * Interruption state of hover detection triggered by termination events, which include the following: finger or
         * mouse release, window switching, screen off, exiting the component boundary, entering child components, or
         * exceeding the movement threshold within the component. The application will restore the UI style and cancel
         * pending navigation and view switching operations.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        CANCEL
    }
    /**
     * Defines the configuration parameters for drag hover detection. The default settings typically suffice. These
     * settings can be customized through [onDragSpringLoading]{@link CommonMethod#onDragSpringLoading} binding or
     * dynamically updated during BEGIN state using
     * [updateConfiguration]{@link dragController.SpringLoadingContext#updateConfiguration}.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    interface DragSpringLoadingConfiguration {
        /**
         * Time (in ms) required to remain stationary to enter the BEGIN state of hover detection. Value range: integer in
         * the [0, 2<sup>31</sup>-1] range. Floating-point number inputs will be truncated to integers. Invalid values (
         * negative numbers, **null**, **undefined**, **NaN**) are treated as the default value **500**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        stillTimeLimit?: number;
        /**
         * Time interval (in ms) at which update notifications are sent after hover detection enters the UPDATE state. Value
         * range: integer in the [0, 2<sup>31</sup>-1] range. Floating-point number inputs will be truncated to integers.
         * Invalid values (negative numbers, **null**, **undefined**, **NaN**) are treated as the default value **100**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        updateInterval?: number;
        /**
         * Maximum number of update notifications after hover detection enters the UPDATE state. Value range: integer in the
         * [0, 2<sup>31</sup>-1] range. Floating-point number inputs will be truncated to integers. Invalid values (negative
         * numbers, **null**, **undefined**, **NaN**) are treated as the default value **3**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        updateNotifyCount?: number;
        /**
         * Maximum waiting time (in ms) from the UPDATE state to the END state. Value range: integer in the
         * [0, 2<sup>31</sup>-1] range. Floating-point number inputs will be truncated to integers. Invalid values (negative
         * numbers, **null**, **undefined**, **NaN**) are treated as the default value **100**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        updateToFinishInterval?: number;
    }
    /**
     * Defines the drag event information when hover detection is triggered. This API provides drag data summaries and
     * additional drag event information, allowing applications to decide whether to respond to hover detection
     * callbacks.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    interface SpringLoadingDragInfos {
        /**
         * Summary of the dragged data. The default value is null.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        dataSummary?: unifiedDataChannel.Summary;
        /**
         * Additional information about the drag event. The default value is an empty string.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        extraInfos?: string;
    }
    /**
     * Defines callback context information passed to applications during hover detection. It enables access to drag
     * states, dynamic UI effect updates, and drag data for operation handling decisions.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    class SpringLoadingContext {
        /**
         * Current state of hover detection.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        state: DragSpringLoadingState;
        /**
         * Callback notification sequence number in the current hover detection cycle. The value is zero-based.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        currentNotifySequence: number;
        /**
         * Drag information. Omitted in CANCEL state; uses the
         * [SpringLoadingDragInfos]{@link dragController.SpringLoadingDragInfos} default value when **undefined**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        dragInfos?: SpringLoadingDragInfos;
        /**
         * Configuration information in the current callback. Omitted in CANCEL state; uses the
         * [DragSpringLoadingConfiguration]{@link dragController.DragSpringLoadingConfiguration} default value when
         * **undefined**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        currentConfig?: DragSpringLoadingConfiguration;
        /**
         * Terminates subsequent hover detection. This API does not trigger CANCEL state notifications, and the application
         * needs to perform state cleanup when executing this API.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        abort(): void;
        /**
         * Updates the hover detection configuration. This API is effective only when the hover detection state is BEGIN.
         * Applications typically set the hover detection configuration when binding
         * [onDragSpringLoading]{@link CommonMethod#onDragSpringLoading} or use the default configuration. This API does not
         * modify the original configuration set during binding, but updates dynamic configuration information for
         * subsequent hover detection. Use this API with caution, as different drag data types may require different UX
         * timing.
         *
         * @param { DragSpringLoadingConfiguration } config - New configuration for hover detection.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        updateConfiguration(config: DragSpringLoadingConfiguration): void;
    }
}
export default dragController;

```
