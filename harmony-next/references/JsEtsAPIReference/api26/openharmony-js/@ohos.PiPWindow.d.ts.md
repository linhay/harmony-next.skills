# @ohos.PiPWindow.d.ts

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
 * @file
 * @kit ArkUI
 */
import type BaseContext from './application/BaseContext';
import type { Callback } from './@ohos.base';
import { NodeController } from './arkui/NodeController';
import { typeNode } from './arkui/FrameNode';
/**
 * The module provides basic APIs for manipulating Picture in Picture (PiP). For example, you can use the APIs to check
 * whether the PiP feature is supported and create a PiP controller to start or stop a PiP window. PiP is mainly used in
 * video playback, video calls, or video meetings.
 *
 * > **NOTE**
 * >
 * > - Before <!--RP2-->OpenHarmony 6.0<!--RP2End-->, the PiP feature was supported only on phones and tablets. Starting
 * > from <!--RP2-->OpenHarmony 6.0<!--RP2End-->, the PiP feature is supported on phones, PCs/2-in-1 devices, tablets,
 * > but is unavailable on all other devices.
 * >
 * > - For the system capability SystemCapability.Window.SessionManager, use
 * > [canIUse()]{@link canIUse} to check whether the device supports this system
 * > capability and the corresponding APIs.
 *
 * @syscap SystemCapability.Window.SessionManager
 * @atomicservice [since 12]
 * @since 11
 */
declare namespace PiPWindow {
    /**
     * Checks whether the current device supports the PiP feature.
     *
     * @returns { boolean } Check result for whether the PiP feature is supported. **true** if supported, **false**
     *     otherwise.
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice [since 12]
     * @since 11
     */
    function isPiPEnabled(): boolean;
    /**
     * Creates a PiP controller. This API uses a promise to return the result.
     *
     * @param { PiPConfiguration } config - Options for creating the PiP controller. This parameter cannot be empty, and
     *     **context** and **componentController** that are used to construct this parameter cannot be empty. When
     *     constructing this parameter, **templateType** (if specified) must be a value defined in
     *     [PiPTemplateType]{@link PiPWindow.PiPTemplateType}, and **controlGroups** (if specified) must match the value
     *     of **templateType**. For details, see [PiPControlGroup]{@link PiPWindow.PiPControlGroup}.
     * @returns { Promise<PiPController> } Promise used to return the PiP controller.
     * @throws { BusinessError } 401 - Params error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified.
     *     <br>2. Incorrect parameter types.
     *     <br>3. Parameter verification failed
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities.
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice [since 12]
     * @since 11
     */
    function create(config: PiPConfiguration): Promise<PiPController>;
    /**
     * Creates a PiP controller. This API uses **typeNode** to add a custom UI node for PiP. This API uses a promise to
     * return the result.
     *
     * @param { PiPConfiguration } config - Options for creating the PiP controller. This parameter cannot be empty, and
     *     **context** that is used to construct this parameter cannot be empty. When constructing this parameter,
     *     **templateType** (if specified) must be a value defined in [PiPTemplateType]{@link PiPWindow.PiPTemplateType},
     *     and **controlGroups** (if specified) must match the value of **templateType**. For details, see
     *     [PiPControlGroup]{@link PiPWindow.PiPControlGroup}.
     * @param { typeNode.XComponent } contentNode - Content to be rendered in the PiP window. The parameter value cannot
     *     be empty.
     * @returns { Promise<PiPController> } Promise used to return the PiP controller.
     * @throws { BusinessError } 401 - Params error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified.
     *     <br>2. Incorrect parameter types.
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities.
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice
     * @since 12
     */
    function create(config: PiPConfiguration, contentNode: typeNode.XComponent): Promise<PiPController>;
    /**
     * Defines the parameters for creating a PiP controller.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice [since 12]
     * @since 11
     */
    interface PiPConfiguration {
        /**
         * Context environment.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        context: BaseContext;
        /**
         * Original [XComponent]{@link XComponent} controller.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        componentController: XComponentController;
        /**
         * ID of the **Navigation** component. If no value is passed, the page does not need to be cached.
         *
         * 1. When the UIAbility uses [Navigation]{@link Navigation} to manage pages,
         * set the ID of the **Navigation** component for the PiP controller.
         * This ensures that the original page can be restored from the PiP window.
         * 2. When the UIAbility uses [Router]{@link @ohos.router:router} to manage pages,
         * you do not need to set the ID of the **Navigation** component for the PiP controller.
         * 3. If the UIAbility has only one page, you do not need to set the navigation ID.
         * The original page can be restored from the PiP window.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        navigationId?: string;
        /**
         * ID of the subpage under the **Navigation** component. After the Full-screen Window button is touched,
         * the specified page is restored. This parameter applies only in scenarios where the UIAbility
         * uses [Navigation]{@link Navigation} to manage pages. It can be set to any subpage ID
         * within the Navigation hierarchy. The default value is **-1**, indicating that the topmost page in the Navigation
         * stack is restored. You are advised to use [getUniqueId()]{@link BaseCustomComponent#getUniqueId} to obtain the
         * page ID. When you use page routing provided by [Navigation]{@link Navigation}, you are
         * advised to use the [system routing table](docroot://ui/arkts-navigation-cross-package.md#system-routing-table).
         * Otherwise, the page ID obtained by calling [getUniqueId()]{@link BaseCustomComponent#getUniqueId}
         * may be incorrect.
         *
         * @default -1
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 22
         */
        handleId?: number;
        /**
         * Template type, which is used to distinguish video playback, video call, video meeting, and live broadcast
         * scenarios. If no value is passed, the video playback template is used by default.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        templateType?: PiPTemplateType;
        /**
         * Width of the original content, in px. It is used to determine the aspect ratio of the PiP window. When the PiP
         * controller is created in
         * [typeNode mode]{@link PiPWindow.create(config: PiPConfiguration, contentNode: typeNode.XComponent)}, the default
         * value is 1920. When the PiP controller is created
         * [not in typeNode mode]{@link PiPWindow.create(config: PiPConfiguration)}, the default value is the width of the
         * [XComponent]{@link XComponent}.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        contentWidth?: number;
        /**
         * Height of the original content, in px. It is used to determine the aspect ratio of the PiP window. When the PiP
         * controller is created in
         * [typeNode mode]{@link PiPWindow.create(config: PiPConfiguration, contentNode: typeNode.XComponent)}, the default
         * value is 1080. When the PiP controller is created
         * [not in typeNode mode]{@link PiPWindow.create(config: PiPConfiguration)}, the default value is the height of the
         * [XComponent]{@link XComponent}.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        contentHeight?: number;
        /**
         * A list of optional component groups of the PiP controller. An application can configure whether to display these
         * optional components. If this parameter is not set for the application, the panel displays basic components (such
         * as the play/pause component of the video playback component group). If this parameter is set for the application,
         * a maximum of three components can be selected. If more than three controls are selected, error code 401 is
         * reported by the API.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        controlGroups?: Array<PiPControlGroup>;
        /**
         * Custom UI controller, which is used to implement the custom UI features on the PiP page. If this parameter is
         * left empty, the custom UI features are not used by default.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        customUIController?: NodeController;
        /**
         * A page-level UI state storage unit. In multi-instance scenarios, it can be used to track the UI state storage
         * object of the main window instance. If no value is passed, you cannot retrieve the main window's UI storage
         * object through the PiP window.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 17
         */
        localStorage?: LocalStorage;
        /**
         * Size of the PiP window that the current app starts for the first time.
         *
         * **0**: no size is set. The PiP window is started based on the size before the PiP window of the previous
         * application is closed.
         *
         * **1**: small window.
         *
         * **2**: large window.
         *
         * If no value is passed, **0** is used.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 19
         */
        defaultWindowSizeType?: number;
        /**
         * Whether the PiP window automatically snaps to screen corners. When this feature is enabled, the screen is divided
         * into four hot zones (top-left, top-right, bottom-left, and bottom-right). When users lift their finger while
         * dragging the PiP window within a hot zone, the PiP window is automatically snapped to the nearest corner.
         *
         * **true**: enables corner snapping.
         *
         * **false**: disables corner snapping.
         *
         * The default value is **true**.
         *
         * This API can be properly called on phones and tablets. If it is called on other device types, it has no effect.
         *
         * @default true
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 22
         */
        cornerAdsorptionEnabled?: boolean;
    }
    /**
     * Describes the size of a PiP window.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice
     * @since 15
     */
    interface PiPWindowSize {
        /**
         * Window width, in px. The value must be a positive integer and cannot be greater than the screen width.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 15
         */
        width: number;
        /**
         * Window height, in px. The value must be a positive integer and cannot be greater than the screen height.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 15
         */
        height: number;
        /**
         * Scale factor of the window, representing the display size relative to the width and height. The value is a
         * floating-point number in the range (0.0, 1.0]. The value **1** means that the window matches the specified width
         * and height.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 15
         */
        scale: number;
    }
    /**
       * Describes the PiP window information.
       *
       * @syscap SystemCapability.Window.SessionManager
       * @atomicservice
       * @since 15
       */
    interface PiPWindowInfo {
        /**
         * ID of the PiP window.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 15
         */
        windowId: number;
        /**
         * Size of the PiP window.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 15
         */
        size: PiPWindowSize;
    }
    /**
     * Enumerates the PiP template types.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice [since 12]
     * @since 11
     */
    enum PiPTemplateType {
        /**
         * Video playback template. A PiP window will be started during video playback, and the video playback template will
         * be loaded. The template contains the play/pause component by default.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        VIDEO_PLAY = 0,
        /**
         * Video call template. A PiP window will be started during a video call, and the video call template will be
         * loaded.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        VIDEO_CALL = 1,
        /**
         * Video meeting template. A PiP window will be started during a video meeting, and the video meeting template will
         * be loaded.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        VIDEO_MEETING = 2,
        /**
         * Live template. A PiP window will be started during a live, and the live template is loaded.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        VIDEO_LIVE = 3
    }
    /**
     * Enumerates the PiP states.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice [since 12]
     * @since 11
     */
    enum PiPState {
        /**
         * PiP is about to start.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        ABOUT_TO_START = 1,
        /**
         * PiP is started.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        STARTED = 2,
        /**
         * PiP is about to stop.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        ABOUT_TO_STOP = 3,
        /**
         * PiP is stopped.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        STOPPED = 4,
        /**
         * The original page is about to restore.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        ABOUT_TO_RESTORE = 5,
        /**
         * An error occurs during the execution of the PiP lifecycle.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        ERROR = 6
    }
    /**
     * Describes the optional component groups of the PiP controller. An application can configure whether to display
     * these optional components. This API must match [PiPTemplateType]{@link PiPWindow.PiPTemplateType} when being used.
     * Otherwise, the [create]{@link PiPWindow.create(config: PiPConfiguration)} API returns error code 401.
     *
     * @unionmember { VideoPlayControlGroup } Video playback component group.
     * @unionmember { VideoCallControlGroup } Video call component group.
     * @unionmember { VideoMeetingControlGroup } Video meeting component group.
     * @unionmember { VideoLiveControlGroup } Live video component group.
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice
     * @since 12
     */
    type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup | VideoLiveControlGroup;
    /**
     * Enumerates the video playback component groups. They are used only when
     * [PiPTemplateType]{@link PiPWindow.PiPTemplateType} is set to **VIDEO_PLAY**.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice
     * @since 12
     */
    enum VideoPlayControlGroup {
        /**
         * Previous/Next component group for video playback.
         *
         * This component group is mutually exclusive with the fast-forward/rewind component group. It cannot be added if
         * the fast-forward/rewind component group is added.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        VIDEO_PREVIOUS_NEXT = 101,
        /**
         * Fast-forward/Rewind component group for video playback.
         *
         * This component group is mutually exclusive with the previous/next component group. It cannot be added if the
         * previous/next component group is added.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        FAST_FORWARD_BACKWARD = 102
    }
    /**
     * Enumerates the video call component groups. They are used only when
     * [PiPTemplateType]{@link PiPWindow.PiPTemplateType} is set to **VIDEO_CALL**.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice
     * @since 12
     */
    enum VideoCallControlGroup {
        /**
         * Microphone on/off component group.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        MICROPHONE_SWITCH = 201,
        /**
         * Hang-up component group.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        HANG_UP_BUTTON = 202,
        /**
         * Camera on/off component group.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        CAMERA_SWITCH = 203,
        /**
         * Mute/Unmute component group.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        MUTE_SWITCH = 204
    }
    /**
     * Enumerates the video meeting component groups. They are used only when
     * [PiPTemplateType]{@link PiPWindow.PiPTemplateType} is set to **VIDEO_MEETING**.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice
     * @since 12
     */
    enum VideoMeetingControlGroup {
        /**
         * Hang-up component group.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        HANG_UP_BUTTON = 301,
        /**
         * Camera on/off component group.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        CAMERA_SWITCH = 302,
        /**
         * Mute/Unmute component group.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        MUTE_SWITCH = 303,
        /**
         * Microphone on/off component group.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        MICROPHONE_SWITCH = 304
    }
    /**
     * Enumerates the live video component groups. They are used only when
     * [PiPTemplateType]{@link PiPWindow.PiPTemplateType} is set to **VIDEO_LIVE**.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice
     * @since 12
     */
    enum VideoLiveControlGroup {
        /**
         * Play/Pause component group for live video.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        VIDEO_PLAY_PAUSE = 401,
        /**
         * Mute/Unmute component group.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        MUTE_SWITCH = 402
    }
    /**
     * Enumerates the statuses of components displayed on the PiP controller.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice
     * @since 12
     */
    enum PiPControlStatus {
        /**
         * Play.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        PLAY = 1,
        /**
         * Pause.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        PAUSE = 0,
        /**
         * Open.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        OPEN = 1,
        /**
         * Close.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        CLOSE = 0
    }
    /**
     * Enumerates the types of components displayed on the PiP controller.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice
     * @since 12
     */
    enum PiPControlType {
        /**
         * Play/Pause component group for live video.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        VIDEO_PLAY_PAUSE = 0,
        /**
         * Previous component in video scenarios.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        VIDEO_PREVIOUS = 1,
        /**
         * Next component in video scenarios.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        VIDEO_NEXT = 2,
        /**
         * Fast-forward component in video scenarios.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        FAST_FORWARD = 3,
        /**
         * Rewind component in video scenarios.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        FAST_BACKWARD = 4,
        /**
         * Hang-up component.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        HANG_UP_BUTTON = 5,
        /**
         * Microphone on/off component.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        MICROPHONE_SWITCH = 6,
        /**
         * Camera on/off component.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        CAMERA_SWITCH = 7,
        /**
         * Mute/Unmute component.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        MUTE_SWITCH = 8
    }
    /**
     * Enumerates the types of action events of the PiP controller.
     *
     * @unionmember { PiPVideoActionEvent } Action event for components displayed on the video playback controller.
     * @unionmember { PiPCallActionEvent } Action event for components displayed on the video call controller.
     * @unionmember { PiPMeetingActionEvent } Action event for components displayed on the video meeting controller.
     * @unionmember { PiPLiveActionEvent } Action event for components displayed on the live video controller.
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice [since 12]
     * @since 11
     */
    type PiPActionEventType = PiPVideoActionEvent | PiPCallActionEvent | PiPMeetingActionEvent | PiPLiveActionEvent;
    /**
     * Defines the PiP action event during video playback.
     *
     * @unionmember { 'playbackStateChanged' } The playback status changes.
     * @unionmember { 'nextVideo' } Plays the next video.
     * @unionmember { 'previousVideo' } Plays the previous video.
     * @unionmember { 'fastForward' } Fast forwards the video. This value is supported since API version 12. [since 12]
     * @unionmember { 'fastBackward' } Rewinds the video. This value is supported since API version 12. [since 12]
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice [since 12]
     * @since 11
     */
    type PiPVideoActionEvent = 'playbackStateChanged' | 'nextVideo' | 'previousVideo' | 'fastForward' | 'fastBackward';
    /**
     * Defines the PiP action event in a video call.
     *
     * @unionmember { 'hangUp' } The video call is hung up.
     * @unionmember { 'micStateChanged' } The microphone is muted or unmuted.
     * @unionmember { 'videoStateChanged' } The camera is turned on or off.
     * @unionmember { 'voiceStateChanged' } The speaker is muted or unmuted. [since 12]
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice [since 12]
     * @since 11
     */
    type PiPCallActionEvent = 'hangUp' | 'micStateChanged' | 'videoStateChanged' | 'voiceStateChanged';
    /**
     * Defines the PiP action event in a video meeting.
     *
     * @unionmember { 'hangUp' } The video meeting is hung up.
     * @unionmember { 'voiceStateChanged' } The speaker is muted or unmuted.
     * @unionmember { 'videoStateChanged' } The camera is turned on or off.
     * @unionmember { 'micStateChanged' } The microphone is muted or unmuted. [since 12]
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice [since 12]
     * @since 11
     */
    type PiPMeetingActionEvent = 'hangUp' | 'voiceStateChanged' | 'videoStateChanged' | 'micStateChanged';
    /**
     * Defines the PiP action event in a live.
     *
     * @unionmember { 'playbackStateChanged' } The live is played or paused.
     * @unionmember { 'voiceStateChanged' } The speaker is muted or unmuted. [since 12]
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice [since 12]
     * @since 11
     */
    type PiPLiveActionEvent = 'playbackStateChanged' | 'voiceStateChanged';
    /**
     * Describes the action event callback of the PiP controller.
     *
     * @param { PiPActionEventType } event - Type of the action event of the PiP controller.
     *     <br>The application performs processing based on the action event. For example,
     *     if the **'playbackStateChanged'** event is triggered, the application starts or stops the video.
     * @param { number } [status] - Status of a component that can be switched. For example, for a microphone on/off
     *     component group, a camera on/off component group, and a mute/unmute component group, the value **1** means that
     *     the component is enabled and **0** means that the component is disabled. For other components, the default
     *     value **-1** is used.
     *     The value should be an integer.
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice
     * @since 12
     */
    type ControlPanelActionEventCallback = (event: PiPActionEventType, status?: number) => void;
    /**
     * Describes the parameters in the callback of the action event of the PiP controller.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice
     * @since 12
     */
    interface ControlEventParam {
        /**
         * Type of the action event of the PiP controller. The application performs processing based on the component type.
         * For example, if the video play/pause component is touched, the application starts or stops the video.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        controlType: PiPControlType;
        /**
         * Status of a component that can be switched. For example, for a microphone on/off component group, a camera on/off
         * component group, and a mute/unmute component group, the value **PiPControlStatus.PLAY** means that the component
         * is enabled and **PiPControlStatus.PAUSE** means that the component is disabled. For the hang-up component, the
         * default value is **-1**.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        status?: PiPControlStatus;
    }
    /**
     * Implements a PiP controller that starts, stops, or updates a PiP window and registers callbacks.
     *
     * Before calling any of the following APIs, you must use
     * [PiPWindow.create()]{@link PiPWindow.create(config: PiPConfiguration)} to create a PiPController instance.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @atomicservice [since 12]
     * @since 11
     */
    interface PiPController {
        /**
         * Starts a PiP window. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 1300012 - The PiP window state is abnormal.
         * @throws { BusinessError } 1300013 - Failed to create the PiP window.
         * @throws { BusinessError } 1300014 - PiP internal error.
         * @throws { BusinessError } 1300015 - Repeated PiP operation.
         * @throws { BusinessError } 1300034 - This operation conflicts with other floating windows. Possible cause:
         *     App has already started float view. [since 26.0.0]
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        startPiP(): Promise<void>;
        /**
         * Stops a PiP window. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 1300011 - Failed to destroy the PiP window.
         * @throws { BusinessError } 1300012 - The PiP window state is abnormal.
         * @throws { BusinessError } 1300015 - Repeated PiP operation.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        stopPiP(): Promise<void>;
        /**
         * Sets whether to automatically start the PiP window when the application's main window which can start the
         * PiP window transitions to the background. By default, the PiP window is not automatically started.
         *
         * If the XComponent approach is used to implement PiP and the **Navigation** component is used for route management
         * , the system caches the top stack information with the specified navigation ID upon the first call of
         * **setAutoStartEnabled(true)**.
         *
         * @param { boolean } enable - If the PiP window needs to be automatically started when the application's
         *     main window transitions to the background, set this parameter to **true**. Otherwise,
         *     set this parameter to **false**. If the PiP feature under **Settings** > **System** > **Multi-window**
         *     is disabled, the PiP window will not be automatically started when the application's main window transitions
         *     to the background even if this parameter is set to **true**.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        setAutoStartEnabled(enable: boolean): void;
        /**
         * Updates the media content size when the media content changes.
         *
         * @param { number } width - Width of the media content, in px. The value must be an integer greater than 0. It is used
         *     to update the aspect ratio of the PiP window.
         * @param { number } height - Height of the media content, in px. The value must be an integer greater than 0. It is
         *     used to update the aspect ratio of the PiP window.
         * @throws { BusinessError } 401 - Params error. Possible causes: The PiPController is not created or destroyed.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        updateContentSize(width: number, height: number): void;
        /**
         * Updates the PiP controller status.
         *
         * @param { PiPControlType } controlType - Type of the component displayed on the PiP controller. Currently, only
         *     the **VIDEO_PLAY_PAUSE**, **MICROPHONE_SWITCH**, **CAMERA_SWITCH**, and **MUTE_SWITCH** component types are
         *     supported. If other component types are passed, they do not take effect and no error is reported.
         * @param { PiPControlStatus } status - Status of the component displayed on the PiP controller.
         * @throws { BusinessError } 401 - Params error. Possible causes: The PiPController is not created or destroyed.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        updatePiPControlStatus(controlType: PiPControlType, status: PiPControlStatus): void;
        /**
         * Updates the PiP node content. This API uses a promise to return the result.
         *
         * @param { typeNode.XComponent } contentNode - Content to be rendered in the PiP window. The parameter value cannot
         *     be empty.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Params error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
         *     capabilities.
         * @throws { BusinessError } 1300014 - PiP internal error.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 18
         */
        updateContentNode(contentNode: typeNode.XComponent): Promise<void>;
        /**
         * Sets the enabled status for a component displayed on the PiP controller.
         *
         * @param { PiPControlType } controlType - Type of the component displayed on the PiP controller.
         * @param { boolean } enabled - Enabled status of the component displayed on the PiP controller. **true** if enabled
         *     , **false** otherwise.
         * @throws { BusinessError } 401 - Params error. Possible causes: The PiPController is not created or destroyed.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        setPiPControlEnabled(controlType: PiPControlType, enabled: boolean): void;
        /**
         * Obtains the PIP window information. This API uses a promise to return the result.
         *
         * @returns { Promise<PiPWindowInfo> } Promise used to return the information about the current PIP window.
         * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
         *     capabilities.
         * @throws { BusinessError } 1300014 - PiP internal error.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 15
         */
        getPiPWindowInfo(): Promise<PiPWindowInfo>;
        /**
         * Obtains the status of the auto-start PiP switch in Settings. This API uses a promise to return the result.
         *
         * @returns { Promise<boolean> } Promise used to return the auto-start PiP switch status. **true** if enabled,
         *     **false** otherwise.
         * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
         *     capabilities.
         * @throws { BusinessError } 1300014 - PiP internal error.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 20
         */
        getPiPSettingSwitch(): Promise<boolean>;
        /**
         * Check whether the PiP window is active. This API uses a promise to return the result.
         *
         * @returns { Promise<boolean> } Promise used to return the PiP window status. **true** is returned if the PiP
         *     window is visible, and **false** is returned if the PiP window is invisible (hidden in the sidebar). If this
         *     API is called when the PiP lifecycle is not [STARTED]{@link PiPWindow.PiPState}, **false** is always
         *     returned.
         * @throws { BusinessError } 1300014 - PiP internal error.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 23
         */
        isPiPActive(): Promise<boolean>;
        /**
         * Subscribes to PiP state events. To avoid potential memory leaks, you are advised to stop listening when it is no
         * longer needed.
         *
         * @param { 'stateChange' } type - Event type. The value is fixed at **'stateChange'**, indicating that the PiP
         *     state changes.
         * @param { function } callback - Callback used to return the result, which includes the following information:<br>-
         *     **state**: [PiPState]{@link PiPWindow.PiPState}, indicating the new PiP state.
         *     <br>- **reason**: a string indicating the reason for the state change.
         *     <br>Before <!--RP1-->OpenHarmony 6.1<!--RP1End-->, the value of **reason** is always **0**,
         *     which can be ignored.<br>Since <!--RP1-->OpenHarmony 6.1<!--RP1End-->, **reason**
         *     indicates the reason for switching the current lifecycle. The options are as follows:
         *     <br>**"requestStart"**: An application calls the **startPip** API.
         *     <br>**"autoStart"**: The application is automatically started in PiP mode
         *      when it is switched to the background.
         *     <br>**"requestDelete"**: The application calls the **stopPip** API.
         *     <br>**"panelActionDelete"**: The user taps the close button in the PiP window.
         *     <br>**"dragDelete"**: The user drags the PiP window to delete.
         *     <br>**"panelActionRestore"**: The user taps the restore button in the PiP
         *     window (or taps the PiP window if there is no restore button) to restore the PiP window.
         *     <br>**"other"**: Other reasons, such as the current window or application's main window being closed
         *     due to the startup of a new PiP window.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'stateChange', callback: (state: PiPState, reason: string) => void): void;
        /**
         * Unsubscribes from PiP state events.
         *
         * @param { 'stateChange' } type - Event type. The value is fixed at **'stateChange'**, indicating that the PiP
         *     state changes.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'stateChange'): void;
        /**
         * Subscribes to PiP action events. To avoid potential memory leaks, you are advised to stop listening when it is no
         * longer needed. The
         * [on('controlEvent')]{@link PiPWindow.PiPController.on(type: 'controlEvent', callback: Callback<ControlEventParam>)}
         * API is preferred.
         *
         * @param { 'controlPanelActionEvent' } type - Event type. The value is fixed at **'controlPanelActionEvent'**,
         *     indicating the action event of the PiP controller.
         * @param { function } callback - Action event callback of the PiP controller. [since 11 - 11]
         * @param { ControlPanelActionEventCallback } callback - Action event callback of the PiP controller. [since 12]
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'controlPanelActionEvent', callback: ControlPanelActionEventCallback): void;
        /**
         * Unsubscribes from PiP action events. The
         * **[off('controlEvent')]{@link PiPWindow.PiPController.off(type: 'controlEvent', callback?: Callback<ControlEventParam>)}**
         * API is preferred.
         *
         * @param { 'controlPanelActionEvent' } type - Event type. The value is fixed at **'controlPanelActionEvent'**,
         *     indicating the action event of the PiP controller.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'controlPanelActionEvent'): void;
        /**
         * Subscribes to PiP action events. To avoid potential memory leaks, you are advised to stop listening when it is no
         * longer needed.
         *
         * @param { 'controlEvent' } type - Event type. The value is fixed at **'controlEvent'**, indicating the action
         *     event of the PiP controller.
         * @param { Callback<ControlEventParam> } callback - Action event callback of the PiP controller.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        on(type: 'controlEvent', callback: Callback<ControlEventParam>): void;
        /**
         * Unsubscribes from PiP action events.
         *
         * @param { 'controlEvent' } type - Event type. The value is fixed at **'controlEvent'**, indicating the action
         *     event of the PiP controller.
         * @param { Callback<ControlEventParam> } callback - Describes the action event callback of the PiP controller. If
         *     no value is passed in, all subscriptions to the specified event are canceled.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 12
         */
        off(type: 'controlEvent', callback?: Callback<ControlEventParam>): void;
        /**
         * Subscribes to PiP window size change events. To avoid potential memory leaks, you are advised to stop listening
         * when it is no longer needed.
         *
         * @param { 'pipWindowSizeChange' } type - Event type. The value is fixed at **'pipWindowSizeChange'**, indicating
         *     that the PiP window size changes.
         * @param { Callback<PiPWindowSize> } callback - Callback used to return the size of the current PiP window.
         * @throws { BusinessError } 401 - Params error. Possible causes: Callback is already registered.
         * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
         *     capabilities.
         * @throws { BusinessError } 1300014 - PiP internal error.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 15
         */
        on(type: 'pipWindowSizeChange', callback: Callback<PiPWindowSize>): void;
        /**
         * Unsubscribes from the PiP window size change event.
         *
         * @param { 'pipWindowSizeChange' } type - Event type. The value is fixed at **'pipWindowSizeChange'**, indicating
         *     that the PiP window size changes.
         * @param { Callback<PiPWindowSize> } callback - Callback used to return the size of the current PiP window. If a
         *     value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions
         *     to the specified event are canceled.
         * @throws { BusinessError } 401 - Params error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types.
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
         *     capabilities.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 15
         */
        off(type: 'pipWindowSizeChange', callback?: Callback<PiPWindowSize>): void;
        /**
         * Subscribes to PiP window active status change events. To avoid potential memory leaks, you are advised to stop
         * listening when it is no longer needed.
         *
         * @param { 'activeStatusChange' } type - Event type. The value is fixed at **'activeStatusChange'**, indicating
         *     that the PiP window active status changes.
         * @param { Callback<boolean> } callback - PiP window active status. **true** is returned if the PiP window is
         *     visible, and **false** is returned if the PiP window is invisible (hidden in the sidebar).
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 22
         */
        on(type: 'activeStatusChange', callback: Callback<boolean>): void;
        /**
         * Unsubscribes from PiP window active status change events.
         *
         * @param { 'activeStatusChange' } type - Event type. The value is fixed at **'activeStatusChange'**, indicating
         *     that the PiP window active status changes.
         * @param { Callback<boolean> } [callback] - PiP window active status. **true** is returned if the PiP window is
         *     visible, and **false** is returned if the PiP window is invisible (hidden in the sidebar). If no value is
         *     passed in, all subscriptions to the specified event are canceled.
         * @syscap SystemCapability.Window.SessionManager
         * @atomicservice
         * @since 22
         */
        off(type: 'activeStatusChange', callback?: Callback<boolean>): void;
    }
}
export default PiPWindow;

```
