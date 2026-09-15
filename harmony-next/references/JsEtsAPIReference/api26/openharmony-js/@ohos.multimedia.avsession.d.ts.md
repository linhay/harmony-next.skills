# @ohos.multimedia.avsession.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
* Copyright (c) 2022-2024 Huawei Device Co., Ltd.
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
 * @kit AVSessionKit
 */
import type { ErrorCallback, AsyncCallback, Callback } from './@ohos.base';
import { WantAgent } from './@ohos.app.ability.wantAgent';
import { KeyEvent } from './@ohos.multimodalInput.keyEvent';
import { ElementName } from './bundleManager/ElementName';
import image from './@ohos.multimedia.image';
import audio from './@ohos.multimedia.audio';
import { AVCastPickerState, AVCastPickerStyle } from './@ohos.multimedia.avCastPickerParam';
import type media from './@ohos.multimedia.media';
import type Context from './application/BaseContext';
import type hdrCapability from './@ohos.graphics.hdrCapability';
/**
 *
 * @syscap SystemCapability.Multimedia.AVSession.Core
 * @atomicservice [since 12]
 * @since 9
 */
declare namespace avSession {
    /**
     * Create an AVSession instance. An ability can only create one AVSession
     *
     * @param { Context } context - The context of application
     * @param { string } tag - A user-defined name for this session
     * @param { AVSessionType } type - The type of session {@link AVSessionType}
     * @param { AsyncCallback<AVSession> } callback - async callback for AVSession.
     * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
     *     2.Parameter verification failed.
     * @throws { BusinessError } 6600101 - Session service exception.
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @since 10
     */
    function createAVSession(context: Context, tag: string, type: AVSessionType, callback: AsyncCallback<AVSession>): void;
    /**
     * Create an AVSession instance. An ability can only create one AVSession
     *
     * @param { Context } context - The context of application
     * @param { string } tag - A user-defined name for this session
     * @param { AVSessionType } type - The type of session {@link AVSessionType}
     * @returns { Promise<AVSession> } Promise for AVSession
     * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
     *     2.Parameter verification failed.
     * @throws { BusinessError } 6600101 - Session service exception.
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    function createAVSession(context: Context, tag: string, type: AVSessionType): Promise<AVSession>;
    /**
     * Get an AVSession instance if already created.
     *
     * @param { Context } context - The context of application
     * @returns { Promise<AVSession> } Promise for AVSession
     * @throws { BusinessError } 6600101 - Session service exception.
     * @throws { BusinessError } 6600102 - The session does not exist.
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice
     * @since 22
     */
    function getAVSession(context: Context): Promise<AVSession>;
    /**
     * Get all avsession descriptors which can be shown on system entrance.
     *
     * @permission ohos.permission.MANAGE_MEDIA_RESOURCES or ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC
     * @returns { Promise<Array<Readonly<AVSessionDescriptor>>> } Promise for an array of AVSessionDescriptors
     * @throws { BusinessError } 201 - permission denied
     * @throws { BusinessError } 6600101 - Session service exception.
     * @syscap SystemCapability.Multimedia.AVSession.Manager
     * @since 23
     */
    function getAllSessionDescriptors(): Promise<Array<Readonly<AVSessionDescriptor>>>;
    /**
     * Create an avsession controller
     *
     * @permission ohos.permission.MANAGE_MEDIA_RESOURCES or ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC
     * @param { string } sessionId - Specifies the sessionId to create the controller.
     *     If provided 'default', the system will create a default controller, Used to control the system default session
     * @returns { Promise<AVSessionController> } Promise for AVSessionController
     * @throws { BusinessError } 201 - Permission denied
     * @throws { BusinessError } 6600101 - Session service exception.
     * @throws { BusinessError } 6600102 - The session does not exist.
     * @syscap SystemCapability.Multimedia.AVSession.Manager
     * @since 23
     */
    function createController(sessionId: string): Promise<AVSessionController>;
    /**
     * Whether desktop lyric feature is supported.
     *
     * @returns { Promise<boolean> } - result returned to indicate desktop lyric is supported.
     * @throws { BusinessError } 6600101 - Session service exception.
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @stagemodelonly
     * @since 23
     */
    function isDesktopLyricSupported(): Promise<boolean>;
    /**
     * Desktop lyric state definition.
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @stagemodelonly
     * @since 23
     */
    interface DesktopLyricState {
        /**
         * Desktop lyric lock state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        isLocked: boolean;
    }
    /**
     * Register session create callback
     *
     * @permission ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC
     * @param { Callback<AVSessionDescriptor> } callback - Used to handle ('sessionCreate' command)
     * @throws { BusinessError } 201 - permission denied.
     * @throws { BusinessError } 6600101 - Session service exception.
     * @syscap SystemCapability.Multimedia.AVSession.Manager
     * @since 23
     */
    function onSessionCreate(callback: Callback<AVSessionDescriptor>): void;
    /**
     * Register session destroy callback
     *
     * @permission ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC
     * @param { Callback<AVSessionDescriptor> } callback - Used to handle ('sessionDestroy' command)
     * @throws { BusinessError } 201 - permission denied.
     * @throws { BusinessError } 6600101 - Session service exception.
     * @syscap SystemCapability.Multimedia.AVSession.Manager
     * @since 23
     */
    function onSessionDestroy(callback: Callback<AVSessionDescriptor>): void;
    /**
     * Register top session changed callback
     *
     * @permission ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC
     * @param { Callback<AVSessionDescriptor> } callback - Used to handle ('topSessionChange' command)
     * @throws { BusinessError } 201 - permission denied.
     * @throws { BusinessError } 6600101 - Session service exception.
     * @syscap SystemCapability.Multimedia.AVSession.Manager
     * @since 23
     */
    function onTopSessionChange(callback: Callback<AVSessionDescriptor>): void;
    /**
     * Unregister session create callback
     *
     * @permission ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC
     * @param { Callback<AVSessionDescriptor> } [callback] - Used to unregister listener for ('sessionCreate') command
     * @throws { BusinessError } 201 - permission denied.
     * @throws { BusinessError } 6600101 - Session service exception.
     * @syscap SystemCapability.Multimedia.AVSession.Manager
     * @since 23
     */
    function offSessionCreate(callback?: Callback<AVSessionDescriptor>): void;
    /**
     * Unregister session destroy callback
     *
     * @permission ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC
     * @param { Callback<AVSessionDescriptor> } [callback] - Used to unregister listener for ('sessionDestroy') command
     * @throws { BusinessError } 201 - permission denied.
     * @throws { BusinessError } 6600101 - Session service exception.
     * @syscap SystemCapability.Multimedia.AVSession.Manager
     * @since 23
     */
    function offSessionDestroy(callback?: Callback<AVSessionDescriptor>): void;
    /**
     * Unregister top session changed callback
     *
     * @permission ohos.permission.MANAGE_MEDIA_RESOURCES_FOR_PUBLIC
     * @param { Callback<AVSessionDescriptor> } [callback] - Used to unregister listener for ('topSessionChange') command
     * @throws { BusinessError } 201 - permission denied.
     * @throws { BusinessError } 6600101 - Session service exception.
     * @syscap SystemCapability.Multimedia.AVSession.Manager
     * @since 23
     */
    function offTopSessionChange(callback?: Callback<AVSessionDescriptor>): void;
    /**
     * Defines the basic callback.
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @since 22
     */
    type NoParamCallback = () => void;
    /**
     * Defines the callback type including two parameters.
     *
     * @param { T } data1
     * @param { G } data2
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @since 22
     */
    type TwoParamCallback<T, G> = (data1: T, data2: G) => void;
    /**
     * Define different protocol capability
     *
     * @syscap SystemCapability.Multimedia.AVSession.AVCast
     * @atomicservice [since 12]
     * @since 11
     */
    enum ProtocolType {
        /**
         * The default cast type "local", media can be routed on the same device,
         * including internal speakers or audio jack on the device itself, A2DP devices.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 11
         */
        TYPE_LOCAL = 0,
        /**
         * The Cast+ Stream indicating the media is presenting on a different device
         * the application need get an AVCastController to control remote playback.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 11
         */
        TYPE_CAST_PLUS_STREAM = 2,
        /**
         * The DLNA type indicates the device supports DLNA protocol,
         * the application needs to get an AVCastController to control remote playback.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 12
         */
        TYPE_DLNA = 4,
        /**
         * This type indicates the device supports audio casting with high definition to get a better sound quality.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        TYPE_CAST_PLUS_AUDIO = 8
    }
    /**
     * Session type supports audio & video, voice_call, video_call, photo
     *
     * @unionmember { 'audio' } audio type
     * @unionmember { 'video' } video type
     * @unionmember { 'voice_call' } voice call type [since 11]
     * @unionmember { 'video_call' } video call type [since 12]
     * @unionmember { 'photo' } photo type [since 22]
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    type AVSessionType = 'audio' | 'video' | 'voice_call' | 'video_call' | 'photo';
    /**
     * AVSession object.
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface AVSession {
        /**
         * unique session Id
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        readonly sessionId: string;
        /**
         * Get current session type
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        readonly sessionType: AVSessionType;
        /**
         * Current session tag.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice
         * @since 22
         */
        readonly sessionTag: string;
        /**
         * Set the metadata of this session.
         * In addition to the required properties, users can fill in partially supported properties
         *
         * @param { AVMetadata } data {@link AVMetadata}
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        setAVMetadata(data: AVMetadata, callback: AsyncCallback<void>): void;
        /**
         * Set the metadata of this session.
         * In addition to the required properties, users can fill in partially supported properties
         *
         * @param { AVMetadata } data {@link AVMetadata}
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        setAVMetadata(data: AVMetadata): Promise<void>;
        /**
         * Set the metadata related with current call.
         *
         * @param { CallMetadata } data - {@link CallMetadata}
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        setCallMetadata(data: CallMetadata, callback: AsyncCallback<void>): void;
        /**
         * Set the metadata related with current call.
         *
         * @param { CallMetadata } data - {@link CallMetadata}
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        setCallMetadata(data: CallMetadata): Promise<void>;
        /**
         * Set the playback state of this session.
         *
         * @param { AVPlaybackState } state {@link AVPlaybackState}
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        setAVPlaybackState(state: AVPlaybackState, callback: AsyncCallback<void>): void;
        /**
         * Set the playback state of this session.
         *
         * @param { AVPlaybackState } state {@link AVPlaybackState}
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        setAVPlaybackState(state: AVPlaybackState): Promise<void>;
        /**
         * Set the call state of this session.
         *
         * @param { AVCallState } state - {@link AVCallState}
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        setAVCallState(state: AVCallState, callback: AsyncCallback<void>): void;
        /**
         * Set the call state of this session.
         *
         * @param { AVCallState } state - {@link AVCallState}
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        setAVCallState(state: AVCallState): Promise<void>;
        /**
         * Set the ability to start the session corresponding to
         *
         * @param { WantAgent } ability - The WantAgent for launch the ability
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        setLaunchAbility(ability: WantAgent, callback: AsyncCallback<void>): void;
        /**
         * Set the ability to start the session corresponding to
         *
         * @param { WantAgent } ability - The WantAgent for launch the ability
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        setLaunchAbility(ability: WantAgent): Promise<void>;
        /**
         * Dispatch the session event of this session.
         *
         * @param { string } event - Session event name to dispatch
         * @param { object } args - The parameters of session event
         * @param { AsyncCallback<void>} callback - The asyncCallback triggered when the command is executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @since 10
         */
        dispatchSessionEvent(event: string, args: {
            [key: string]: Object;
        }, callback: AsyncCallback<void>): void;
        /**
         * Dispatch the session event of this session.
         *
         * @param { string } event - Session event name to dispatch
         * @param { object } args - The parameters of session event
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        dispatchSessionEvent(event: string, args: {
            [key: string]: Object;
        }): Promise<void>;
        /**
         * Set the playlist of queueItem. Identifies the content of the playlist presented by this session.
         *
         * @param { Array<AVQueueItem> } items - An array of the AVQueueItem
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        setAVQueueItems(items: Array<AVQueueItem>, callback: AsyncCallback<void>): void;
        /**
         * Set the playlist of queueItem. Identifies the content of the playlist presented by this session.
         *
         * @param { Array<AVQueueItem> } items - An array of the AVQueueItem
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        setAVQueueItems(items: Array<AVQueueItem>): Promise<void>;
        /**
         * Set the name of the playlist presented by this session.
         *
         * @param { string } title - The name of the playlist
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        setAVQueueTitle(title: string, callback: AsyncCallback<void>): void;
        /**
         * Set the name of the playlist presented by this session.
         *
         * @param { string } title - The name of the playlist
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        setAVQueueTitle(title: string): Promise<void>;
        /**
         * Set the custom media packets for this session.
         *
         * @param { object } extras - The custom media packets
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @since 10
         */
        setExtras(extras: {
            [key: string]: Object;
        }, callback: AsyncCallback<void>): void;
        /**
         * Set the custom media packets for this session.
         *
         * @param { object } extras - The custom media packets
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        setExtras(extras: {
            [key: string]: Object;
        }): Promise<void>;
        /**
         * Set supported speeds supplied by application.
         *
         * @param { Array<number> } speeds - supported speeds
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        setSupportedPlaySpeeds(speeds: Array<number>): Promise<void>;
        /**
         * Set supported loop modes supplied by application.
         *
         * @param { Array<LoopMode> } loopModes - supported loop modes
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        setSupportedLoopModes(loopModes: Array<LoopMode>): Promise<void>;
        /**
         * Enable desktop lyric for this session.
         *
         * @param { boolean } enable - The enable status indicating to using system desktop lyric feature or not
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600111 - The desktop lyrics feature is not supported.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        enableDesktopLyric(enable: boolean): Promise<void>;
        /**
         * Set desktop lyric visible state for this session.
         *
         * @param { boolean } visible - make desktop lyric window visible or not
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600110 - The desktop lyrics feature of this application is not enabled.
         * @throws { BusinessError } 6600111 - The desktop lyrics feature is not supported.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        setDesktopLyricVisible(visible: boolean): Promise<void>;
        /**
         * Query desktop lyric visible state for this session.
         *
         * @returns { Promise<boolean> } return desktop lyric visible state
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600110 - The desktop lyrics feature of this application is not enabled.
         * @throws { BusinessError } 6600111 - The desktop lyrics feature is not supported.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        isDesktopLyricVisible(): Promise<boolean>;
        /**
         * Register desktop lyric visible state change callback.
         *
         * @param { Callback<boolean> } callback - a callback to receive desktop lyric window visible state.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void;
        /**
         * Unregister desktop lyric visible state change callback.
         *
         * @param { Callback<boolean> } [callback] - a callback to receive desktop lyric window visible state.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void;
        /**
         * Set desktop lyric state such as lock state for this session.
         *
         * @param { DesktopLyricState } state - The desktop lyric state
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600110 - The desktop lyrics feature of this application is not enabled.
         * @throws { BusinessError } 6600111 - The desktop lyrics feature is not supported.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        setDesktopLyricState(state: DesktopLyricState): Promise<void>;
        /**
         * Get desktop lyric state such as lock state for this session.
         *
         * @returns { Promise<DesktopLyricState> } void promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600110 - The desktop lyrics feature of this application is not enabled.
         * @throws { BusinessError } 6600111 - The desktop lyrics feature is not supported.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        getDesktopLyricState(): Promise<DesktopLyricState>;
        /**
         * Register desktop lyric state changed callback.
         *
         * @param { Callback<DesktopLyricState> } callback - a callback to receive desktop lyric state.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void;
        /**
         * Unregister desktop lyric state changed callback.
         *
         * @param { Callback<DesktopLyricState> } [callback] - a callback to receive desktop lyric state.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void;
        /**
         * Set the background playback mode.
         * It is recommended that you associate it with the background playback switch in the app.
         * If not set, the default value for 'audio' session is {@link ENABLE_BACKGROUND_PLAY} and
         * the default value for 'video' session is {@link DISENABLE_BACKGROUND_PLAY}.
         *
         * @param { BackgroundPlayMode } mode - Background play mode
         * @returns { Promise<void> } void promise when executed successfully.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 24
         */
        setBackgroundPlayMode(mode: BackgroundPlayMode): Promise<void>;
        /**
         * Set media control types that can be displayed on the media center.
         *
         * @param { Array<AVMediaCenterControlType> } type - The control types that can be displayed on the media center.
         *     If the priority of control type is not set, the media center will display based on {@link AVSessionType}.
         *     The control type set must be registered by {@link on}, the media center prioritizes displaying
         *     the set control type.
         * @returns { Promise<void> } void promise when executed successfully.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        setMediaCenterControlType(type: Array<AVMediaCenterControlType>): Promise<void>;
        /**
         * Get the current session's own controller
         *
         * @param { AsyncCallback<AVSessionController> } callback - async callback for the AVSessionController.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        getController(callback: AsyncCallback<AVSessionController>): void;
        /**
         * Get the current session's own controller
         *
         * @returns { Promise<AVSessionController> } Promise for the AVSessionController
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getController(): Promise<AVSessionController>;
        /**
         * Get the cast controller when the session is casted to remote device.
         * If the avsession is not under casting state, the controller will return null.
         *
         * @param { AsyncCallback<AVCastController> } callback - async callback for the AVCastController.
         * @throws {BusinessError} 6600102 - The session does not exist
         * @throws {BusinessError} 6600109 - The remote connection is not established
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 10
         */
        getAVCastController(callback: AsyncCallback<AVCastController>): void;
        /**
         * Get the cast controller when the session is casted to remote device.
         * If the avsession is not under casting state, the controller will return null.
         *
         * @returns { Promise<AVCastController> } Promise for the AVCastController
         * @throws {BusinessError} 6600102 - The session does not exist
         * @throws {BusinessError} 6600109 - The remote connection is not established
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        getAVCastController(): Promise<AVCastController>;
        /**
         * Get output device information
         *
         * @param { AsyncCallback<OutputDeviceInfo> } callback - async callback for the OutputDeviceInfo.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void;
        /**
         * Get output device information
         *
         * @returns { Promise<OutputDeviceInfo> } Promise for the OutputDeviceInfo
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getOutputDevice(): Promise<OutputDeviceInfo>;
        /**
         * Get output device information
         *
         * @returns { OutputDeviceInfo } the OutputDeviceInfo
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getOutputDeviceSync(): OutputDeviceInfo;
        /**
         * Get all the current virtual display information for extended display.
         *
         * @returns { Promise<Array<CastDisplayInfo>> } Promise for the CastDisplayInfo
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.ExtendedDisplayCast
         * @atomicservice
         * @since 12
         */
        getAllCastDisplays(): Promise<Array<CastDisplayInfo>>;
        /**
         * Register play command callback.
         * As long as it is registered, it means that the ability supports this command.
         * If you cancel the callback, you need to call off {@link off}
         * When canceling the callback, need to update the supported commands list.
         * Each playback command only supports registering one callback,
         * and the new callback will replace the previous one.
         *
         * @param { 'play' } type - Command to register 'play'.
         * @param { function } callback - Used to handle ('play') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'play', callback: () => void): void;
        /**
         * Register play command callback.
         * The application will receive {@link CommandInfo} from a controller.
         *
         * @param { Callback<CommandInfo> } callback - Used to handle ('play') command
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        onPlay(callback: Callback<CommandInfo>): void;
        /**
         * Register pause command callback.
         * As long as it is registered, it means that the ability supports this command.
         * If you cancel the callback, you need to call off {@link off}
         * When canceling the callback, need to update the supported commands list.
         * Each playback command only supports registering one callback,
         * and the new callback will replace the previous one.
         *
         * @param { 'pause' } type - Command to register 'pause'.
         * @param { function } callback - Used to handle ('pause') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'pause', callback: () => void): void;
        /**
         * Register stop command callback.
         * As long as it is registered, it means that the ability supports this command.
         * If you cancel the callback, you need to call off {@link off}
         * When canceling the callback, need to update the supported commands list.
         * Each playback command only supports registering one callback,
         * and the new callback will replace the previous one.
         *
         * @param { 'stop' } type - Command to register 'stop'.
         * @param { function } callback - Used to handle ('stop') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'stop', callback: () => void): void;
        /**
         * Register playNext command callback.
         * As long as it is registered, it means that the ability supports this command.
         * If you cancel the callback, you need to call off {@link off}
         * When canceling the callback, need to update the supported commands list.
         * Each playback command only supports registering one callback,
         * and the new callback will replace the previous one.
         *
         * @param { 'playNext' } type - Command to register 'playNext'.
         * @param { function } callback - Used to handle ('playNext') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'playNext', callback: () => void): void;
        /**
         * Register playNext command callback.
         * The application will receive {@link CommandInfo} from a controller.
         *
         * @param { Callback<CommandInfo> } callback - Used to handle ('playNext') command
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        onPlayNext(callback: Callback<CommandInfo>): void;
        /**
         * Register playPrevious command callback.
         * As long as it is registered, it means that the ability supports this command.
         * If you cancel the callback, you need to call off {@link off}
         * When canceling the callback, need to update the supported commands list.
         * Each playback command only supports registering one callback,
         * and the new callback will replace the previous one.
         *
         * @param { 'playPrevious' } type - Command to register 'playPrevious'.
         * @param { function } callback - Used to handle ('playPrevious') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'playPrevious', callback: () => void): void;
        /**
         * Register playPrevious command callback.
         * The application will receive {@link CommandInfo} from a controller.
         *
         * @param { Callback<CommandInfo> } callback - Used to handle ('playPrevious') command
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice
         * @since 22
         */
        onPlayPrevious(callback: Callback<CommandInfo>): void;
        /**
         * Register fastForward command callback.
         * As long as it is registered, it means that the ability supports this command.
         * If you cancel the callback, you need to call off {@link off}
         * When canceling the callback, need to update the supported commands list.
         * Each playback command only supports registering one callback,
         * and the new callback will replace the previous one.
         *
         * @param { 'fastForward' } type - Command to register 'fastForward'.
         * @param { function } callback - Used to handle ('fastForward') command, described by milliseconds.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'fastForward', callback: (time?: number) => void): void;
        /**
         * Register fastForward command callback.
         * The application will receive forward time and {@link CommandInfo} from a controller.
         *
         * @param { TwoParamCallback<number, CommandInfo> } callback - Used to handle ('fastForward') command, described by
         *     milliseconds.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        onFastForward(callback: TwoParamCallback<number, CommandInfo>): void;
        /**
         * Register rewind command callback.
         * As long as it is registered, it means that the ability supports this command.
         * If you cancel the callback, you need to call off {@link off}
         * When canceling the callback, need to update the supported commands list.
         * Each playback command only supports registering one callback,
         * and the new callback will replace the previous one.
         *
         * @param { 'rewind' } type - Command to register 'rewind'.
         * @param { function } callback - Used to handle ('rewind') command, described by milliseconds.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'rewind', callback: (time?: number) => void): void;
        /**
         * Register rewind command callback.
         * The application will receive rewind time and {@link CommandInfo} from a controller.
         *
         * @param { TwoParamCallback<number, CommandInfo> } callback - Used to handle ('rewind') command, described by
         *     milliseconds.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        onRewind(callback: TwoParamCallback<number, CommandInfo>): void;
        /**
         * Unregister play command callback.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { 'play' } type - Command to register 'play'.
         * @param { function } callback - Used to handle ('play') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'play', callback?: () => void): void;
        /**
         * Unregister play command callback.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { Callback<CommandInfo> } [callback] - Used to handle ('play') command
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        offPlay(callback?: Callback<CommandInfo>): void;
        /**
         * Unregister pause command callback.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { 'pause' } type - Command to register 'pause'.
         * @param { function } callback - Used to handle ('pause') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'pause', callback?: () => void): void;
        /**
         * Unregister stop command callback.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { 'stop' } type - Command to register 'stop'.
         * @param { function } callback - Used to handle ('stop') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'stop', callback?: () => void): void;
        /**
         * Unregister playNext command callback.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { 'playNext' } type - Command to register 'playNext'.
         * @param { function } callback - Used to handle ('playNext') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'playNext', callback?: () => void): void;
        /**
         * Unregister playNext command callback.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { Callback<CommandInfo> } [callback] - Used to handle ('playNext') command
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        offPlayNext(callback?: Callback<CommandInfo>): void;
        /**
         * Unregister playPrevious command callback.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { 'playPrevious' } type - Command to register 'playPrevious'.
         * @param { function } callback - Used to handle ('playPrevious') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'playPrevious', callback?: () => void): void;
        /**
         * Unregister playPrevious command callback.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { Callback<CommandInfo> } [callback] - Used to handle ('playPrevious') command
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        offPlayPrevious(callback?: Callback<CommandInfo>): void;
        /**
         * Unregister fastForward command callback.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { 'fastForward' } type - Command to register 'fastForward'.
         * @param { function } callback - Used to handle ('fastForward') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'fastForward', callback?: () => void): void;
        /**
         * Unregister fastForward command callback.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { TwoParamCallback<number, CommandInfo> } [callback] - Used to handle ('fastForward') command
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        offFastForward(callback?: TwoParamCallback<number, CommandInfo>): void;
        /**
         * Unregister rewind command callback.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { 'rewind' } type - Command to register 'rewind'.
         * @param { function } callback - Used to handle ('rewind') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'rewind', callback?: () => void): void;
        /**
         * Unregister rewind command callback.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { TwoParamCallback<number, CommandInfo> } [callback] - Used to handle ('rewind') command
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        offRewind(callback?: TwoParamCallback<number, CommandInfo>): void;
        /**
         * Register playFromAssetId command callback.
         * As long as it is registered, it means that the ability supports this command.
         * If you cancel the callback, you need to call off {@link off}
         * When canceling the callback, need to update the supported commands list.
         * Each playback command only supports registering one callback,
         * and the new callback will replace the previous one.
         *
         * @param { 'playFromAssetId' } type - Command to register 'playFromAssetId'.
         * @param { function } callback - Used to handle ('playFromAssetId') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         * @deprecated since 20
         * @useinstead ohos.multimedia.avsession.AVSession#on
         */
        on(type: 'playFromAssetId', callback: (assetId: number) => void): void;
        /**
         * Unregister playFromAssetId command callback.
         *
         * @param { 'playFromAssetId' } type - Command to register 'playFromAssetId'.
         * @param { function } callback - Used to handle ('playFromAssetId') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         * @deprecated since 20
         * @useinstead ohos.multimedia.avsession.AVSession#off
         */
        off(type: 'playFromAssetId', callback?: (assetId: number) => void): void;
        /**
         * Subscribes to playWithAssetId events.
         *
         * @param { 'playWithAssetId' } type - Event type.
         * @param { Callback<string> } callback - Callback used to handle the 'playWithAssetId' command.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice
         * @since 20
         */
        on(type: 'playWithAssetId', callback: Callback<string>): void;
        /**
         * Unsubscribes from playWithAssetId events.
         *
         * @param { 'playWithAssetId' } type - Event type.
         * @param { Callback<string> } callback - Callback used to handle the 'playWithAssetId' command.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice
         * @since 20
         */
        off(type: 'playWithAssetId', callback?: Callback<string>): void;
        /**
         * Register seek command callback
         *
         * @param { 'seek' } type - Registration Type 'seek'
         * @param { function } callback - Used to handle seek command.The callback provides the seek time(ms)
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'seek', callback: (time: number) => void): void;
        /**
         * Unregister seek command callback
         *
         * @param { 'seek' } type - Registration Type 'seek'
         * @param { function } callback - Used to handle seek command.The callback provides the seek time(ms)
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'seek', callback?: (time: number) => void): void;
        /**
         * Register setSpeed command callback
         *
         * @param { 'setSpeed' } type - Registration Type 'setSpeed'
         * @param { function } callback - Used to handle setSpeed command.The callback provides the speed value
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'setSpeed', callback: (speed: number) => void): void;
        /**
         * Unregister setSpeed command callback
         *
         * @param { 'setSpeed' } type - Registration Type 'setSpeed'
         * @param { function } callback - Used to handle setSpeed command.The callback provides the speed value
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'setSpeed', callback?: (speed: number) => void): void;
        /**
         * Register setLoopMode command callback
         *
         * @param { 'setLoopMode' } type - Registration Type 'setLoopMode'
         * @param { function } callback - Used to handle setLoopMode command.The callback provides the {@link LoopMode}
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'setLoopMode', callback: (mode: LoopMode) => void): void;
        /**
         * Unregister setLoopMode command callback
         *
         * @param { 'setLoopMode' } type - Registration Type 'setLoopMode'
         * @param { function } callback - Used to handle setLoopMode command.The callback provides the {@link LoopMode}
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'setLoopMode', callback?: (mode: LoopMode) => void): void;
        /**
         * Register setTargetLoopMode command callback
         * Application should change playmode to the loopmode which is requested.
         *
         * @param { 'setTargetLoopMode' } type - Registration Type 'setTargetLoopMode'
         * @param { Callback<LoopMode> } callback - Used to handle setTargetLoopMode command.The callback provides the {@
         *     link LoopMode}
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice
         * @since 18
         */
        on(type: 'setTargetLoopMode', callback: Callback<LoopMode>): void;
        /**
         * Unregister setTargetLoopMode command callback
         *
         * @param { 'setTargetLoopMode' } type - Registration Type 'setTargetLoopMode'
         * @param { Callback<LoopMode> } callback - Used to handle setTargetLoopMode command.The callback provides the {@
         *     link LoopMode}
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice
         * @since 18
         */
        off(type: 'setTargetLoopMode', callback?: Callback<LoopMode>): void;
        /**
         * Register toggle favorite command callback
         *
         * @param { 'toggleFavorite' } type - Registration Type 'toggleFavorite'
         * @param { function } callback - Used to handle toggleFavorite command.The callback provides
         *     the assetId for which the favorite status needs to be switched.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'toggleFavorite', callback: (assetId: string) => void): void;
        /**
         * Unregister toggle favorite command callback
         *
         * @param { 'toggleFavorite' } type - Registration Type 'toggleFavorite'
         * @param { function } callback - Used to handle toggleFavorite command.The callback provides
         *     the assetId for which the favorite status needs to be switched.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'toggleFavorite', callback?: (assetId: string) => void): void;
        /**
         * Register media key handling callback
         *
         * @param { 'handleKeyEvent' } type - Registration Type 'handleKeyEvent'
         * @param { function } callback - Used to handle key events.The callback provides the KeyEvent
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'handleKeyEvent', callback: (event: KeyEvent) => void): void;
        /**
         * Unregister media key handling callback
         *
         * @param { 'handleKeyEvent' } type - Registration Type 'handleKeyEvent'
         * @param { function } callback - Used to handle key events.The callback provides the KeyEvent
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'handleKeyEvent', callback?: (event: KeyEvent) => void): void;
        /**
         * Register session output device change callback
         *
         * @param { 'outputDeviceChange' } type - Registration Type 'outputDeviceChange'
         * @param { function } callback - Used to handle output device changed.
         *     The callback provide the new device info {@link OutputDeviceInfo} and related connection state {@link
         *     ConnectionState}.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600102 - The session does not exist
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void;
        /**
         * Unregister session output device change callback
         *
         * @param { 'outputDeviceChange' } type - Registration Type 'outputDeviceChange'
         * @param { function } callback - Used to handle output device changed.
         *     The callback provide the new device info {@link OutputDeviceInfo} and related connection state {@link
         *     ConnectionState}.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600102 - The session does not exist
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void;
        /**
         * Register session custom command change callback
         *
         * @param { 'commonCommand' } type - Registration Type 'commonCommand'
         * @param { function } callback - Used to handle event when the common command is received
         *     The callback provide the command name and command args
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'commonCommand', callback: (command: string, args: {
            [key: string]: Object;
        }) => void): void;
        /**
         * Unregister session custom command change callback
         *
         * @param { 'commonCommand' } type - Registration Type 'commonCommand'
         * @param { function } callback - Used to cancel a specific listener
         *     The callback provide the command name and command args
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'commonCommand', callback?: (command: string, args: {
            [key: string]: Object;
        }) => void): void;
        /**
         * Register the item to play from the playlist change callback
         *
         * @param { 'skipToQueueItem' } type - Registration Type 'skipToQueueItem'
         * @param { function } callback - Used to handle the item to be played.
         *     The callback provide the new device info {@link OutputDeviceInfo}
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'skipToQueueItem', callback: (itemId: number) => void): void;
        /**
         * Unregister the item to play from the playlist change callback
         *
         * @param { 'skipToQueueItem' } type - Registration Type 'skipToQueueItem'
         * @param { function } callback - Used to handle the item to be played.
         *     The callback provide the new device info {@link OutputDeviceInfo}
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'skipToQueueItem', callback?: (itemId: number) => void): void;
        /**
         * Register answer command callback.
         * As long as it is registered, it means that the ability supports this command.
         * If you cancel the callback, you need to call off {@link off}
         *
         * @param { 'answer' } type - Command to register 'answer'.
         * @param { Callback<void> } callback - Used to handle ('answer') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'answer', callback: Callback<void>): void;
        /**
         * Unregister answer command callback.
         *
         * @param { 'answer' } type - Command to register 'answer'.
         * @param { Callback<void> } callback - Used to handle ('answer') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'answer', callback?: Callback<void>): void;
        /**
         * Register hangUp command callback.
         * As long as it is registered, it means that the ability supports this command.
         * If you cancel the callback, you need to call off {@link off}
         *
         * @param { 'hangUp' } type - Command to register 'hangUp'.
         * @param { Callback<void> } callback - Used to handle ('hangUp') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'hangUp', callback: Callback<void>): void;
        /**
         * Unregister hangUp command callback.
         *
         * @param { 'hangUp' } type - Command to register 'hangUp'.
         * @param { Callback<void> } callback - Used to handle ('hangUp') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'hangUp', callback?: Callback<void>): void;
        /**
         * Register toggleCallMute command callback.
         * As long as it is registered, it means that the ability supports this command.
         * If you cancel the callback, you need to call off {@link off}
         *
         * @param { 'toggleCallMute' } type - Command to register 'toggleCallMute'.
         * @param { Callback<void> } callback - Used to handle ('toggleCallMute') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'toggleCallMute', callback: Callback<void>): void;
        /**
         * Unregister toggleCallMute command callback.
         *
         * @param { 'toggleCallMute' } type - Command to register 'toggleCallMute'.
         * @param { Callback<void> } callback - Used to handle ('toggleCallMute') command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect
         *     parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'toggleCallMute', callback?: Callback<void>): void;
        /**
         * Register listener for cast display information changed.
         *
         * @param { 'castDisplayChange' } type - Type of the 'castDisplayChange' to listen for.
         * @param { Callback<CastDisplayInfo> } callback - Callback used to return cast display information.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600102 - The session does not exist
         * @syscap SystemCapability.Multimedia.AVSession.ExtendedDisplayCast
         * @atomicservice
         * @since 12
         */
        on(type: 'castDisplayChange', callback: Callback<CastDisplayInfo>): void;
        /**
         * Unregister listener for cast display information changed.
         *
         * @param { 'castDisplayChange' } type - Type of the 'castDisplayChange' to listen for.
         * @param { Callback<CastDisplayInfo> } callback - Callback used to return cast display information.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600102 - The session does not exist
         * @syscap SystemCapability.Multimedia.AVSession.ExtendedDisplayCast
         * @atomicservice
         * @since 12
         */
        off(type: 'castDisplayChange', callback?: Callback<CastDisplayInfo>): void;
        /**
         * Register listener for custom data sent from remote device.
         *
         * @param { 'customDataChange' } type - Type of the 'customDataChange' to listen for.
         * @param { Callback<Record<string, Object>> } callback - Callback used to retrieve custom data.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void;
        /**
         * Unsubscribes from custom data changes.
         *
         * @param { 'customDataChange' } type Custom data type.
         * @param { Callback<Record<string, Object>> } [callback] Callback used to return the custom data.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void;
        /**
         * Sends custom data to a remote device.
         *
         * @param { Record<string, Object> } data Custom data populated by the application.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 6600101 - Session service exception.
         *     You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        sendCustomData(data: Record<string, Object>): Promise<void>;
        /**
         * Stop current cast and disconnect device connection.
         *
         * @param { AsyncCallback<void> } callback A callback instance used to return when cast stopped completed.
         * @throws { BusinessError } 6600109 - The remote connection is not established
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 10
         */
        stopCasting(callback: AsyncCallback<void>): void;
        /**
         * Stop current cast and disconnect device connection.
         *
         * @returns { Promise<void> } void result promise when executed successfully
         * @throws { BusinessError } 6600109 - The remote connection is not established
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        stopCasting(): Promise<void>;
        /**
         * Activate the session, indicating that the session can accept control commands
         *
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the session is activated.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        activate(callback: AsyncCallback<void>): void;
        /**
         * Activate the session, indicating that the session can accept control commands
         *
         * @returns { Promise<void> } void result promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        activate(): Promise<void>;
        /**
         * Deactivate the session, indicating that the session not ready to accept control commands
         *
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the session is deactivated.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        deactivate(callback: AsyncCallback<void>): void;
        /**
         * Deactivate the session, indicating that the session not ready to accept control commands
         *
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        deactivate(): Promise<void>;
        /**
         * Destroy this session, the server will clean up the session resources
         *
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        destroy(callback: AsyncCallback<void>): void;
        /**
         * Destroy this session, the server will clean up the session resources
         *
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        destroy(): Promise<void>;
    }
    /**
     * The type of control command
     *
     * @unionmember { 'play' } Play the current media.
     * @unionmember { 'pause' } Pause the current media.
     * @unionmember { 'stop' } Stop the current media.
     * @unionmember { 'playNext' } Play the next media in the queue.
     * @unionmember { 'playPrevious' } Play the previous media in the queue.
     * @unionmember { 'fastForward' } Fast forward the current media.
     * @unionmember { 'rewind' } Rewind the current media.
     * @unionmember { 'seek' } Seek to a specific position in the media.
     * @unionmember { 'setVolume' } Adjust volume for the media.
     * @unionmember { 'setSpeed' } Set the playback speed..
     * @unionmember { 'setLoopMode' } Set the loop mode for the media.
     * @unionmember { 'toggleFavorite' } Toggle the favorite status of the current media.
     * @unionmember { 'toggleMute' } Toggle the mute status of the media.
     * @syscap SystemCapability.Multimedia.AVSession.AVCast
     * @atomicservice [since 12]
     * @since 10
     */
    type AVCastControlCommandType = 'play' | 'pause' | 'stop' | 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' | 'seek' | 'setVolume' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite' | 'toggleMute';
    /**
     * The definition of cast command to be sent to the session
     *
     * @syscap SystemCapability.Multimedia.AVSession.AVCast
     * @atomicservice [since 12]
     * @since 10
     */
    interface AVCastControlCommand {
        /**
         * The command value {@link AVCastControlCommandType}
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        command: AVCastControlCommandType;
        /**
         * Parameter carried in the command.
         * The seek command must carry the number parameter.
         * The setVolume command must carry the number parameter.
         * The toggleFavorite command must carry the {@link AVMediaDescription.assetId} parameter.
         * The setSpeed command must carry the {@link #media.PlaybackSpeed} parameter.
         * The setLoopMode command must carry the {@link LoopMode} parameter.
         * Other commands do not need to carry parameters.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        parameter?: media.PlaybackSpeed | number | string | LoopMode;
    }
    /**
     * AVCastController definition used to implement a remote control when a cast is connected
     *
     * @syscap SystemCapability.Multimedia.AVSession.AVCast
     * @atomicservice [since 12]
     * @since 10
     */
    interface AVCastController {
        /**
         * Get the playback status of the current player
         *
         * @param { AsyncCallback<AVPlaybackState> } callback - The triggered asyncCallback when (getAVPlaybackState).
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 10
         */
        getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void;
        /**
         * Get the playback status of the current player
         *
         * @returns { Promise<AVPlaybackState> } (AVPlaybackState) returned through promise
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        getAVPlaybackState(): Promise<AVPlaybackState>;
        /**
         * Get supported decoders of remote player.
         *
         * @returns { Promise<Array<DecoderType>> } (DecoderType) returned through promise
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 19
         */
        getSupportedDecoders(): Promise<Array<DecoderType>>;
        /**
         * Get recommended resolution of remote player based on each decoder.
         *
         * @param { DecoderType } decoderType - The decoder type.
         * @returns { Promise<ResolutionLevel> } ResolutionLevel returned through promise
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 19
         */
        getRecommendedResolutionLevel(decoderType: DecoderType): Promise<ResolutionLevel>;
        /**
         * Get supported hdr capabilities of remote player.
         *
         * @returns { Promise<Array<hdrCapability.HDRFormat>> } HDRFormat returned through promise
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 19
         */
        getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>;
        /**
         * Get supported speed of remote player.
         *
         * @returns { Promise<Array<number>> } supported speed returned through promise
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 19
         */
        getSupportedPlaySpeeds(): Promise<Array<number>>;
        /**
         * Send control commands to remote player
         *
         * @param { AVCastControlCommand } command The command to be send.
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600105 - Invalid session command
         * @throws { BusinessError } 6600109 - The remote connection is not established
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 10
         */
        sendControlCommand(command: AVCastControlCommand, callback: AsyncCallback<void>): void;
        /**
         * Send control commands to remote player
         *
         * @param { AVCastControlCommand } command The command to be send.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600105 - Invalid session command
         * @throws { BusinessError } 6600109 - The remote connection is not established
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        sendControlCommand(command: AVCastControlCommand): Promise<void>;
        /**
         * Play the current item, should contain mediaUri otherwise the playback will fail.
         *
         * @param { AVQueueItem } item media item info.
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully
         * @throws {BusinessError} 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws {BusinessError} 6600101 - Session service exception
         * @throws {BusinessError} 6600109 - The remote connection is not established
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 10
         */
        start(item: AVQueueItem, callback: AsyncCallback<void>): void;
        /**
         * Play the current item, should contain mediaUri otherwise the playback will fail.
         *
         * @param { AVQueueItem } item media item info.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws {BusinessError} 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws {BusinessError} 6600101 - Session service exception
         * @throws {BusinessError} 6600109 - The remote connection is not established
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        start(item: AVQueueItem): Promise<void>;
        /**
         * Load the current item and mediaUri can be null, this is needed for sink media information displaying
         *
         * @param { AVQueueItem } item media item info.
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully
         * @throws {BusinessError} 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws {BusinessError} 6600101 - Session service exception
         * @throws {BusinessError} 6600109 - The remote connection is not established
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 10
         */
        prepare(item: AVQueueItem, callback: AsyncCallback<void>): void;
        /**
         * Load the current item and mediaUri can be null, this is needed for sink media information displaying
         *
         * @param { AVQueueItem } item media item info.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws {BusinessError} 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws {BusinessError} 6600101 - Session service exception
         * @throws {BusinessError} 6600109 - The remote connection is not established
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        prepare(item: AVQueueItem): Promise<void>;
        /**
         * Get the current playing item
         *
         * @param { AsyncCallback<AVQueueItem> } callback - The triggered asyncCallback.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 10
         */
        getCurrentItem(callback: AsyncCallback<AVQueueItem>): void;
        /**
         * Get the current playing item
         *
         * @returns { Promise<AVQueueItem> } (AVQueueItem) returned through promise
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        getCurrentItem(): Promise<AVQueueItem>;
        /**
         * Get commands supported by the current cast controller
         *
         * @param { AsyncCallback<Array<AVCastControlCommandType>> } callback - The triggered asyncCallback when (
         *     getValidCommands).
         * @throws { BusinessError } 6600101 - Session service exception.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 11
         */
        getValidCommands(callback: AsyncCallback<Array<AVCastControlCommandType>>): void;
        /**
         * Get commands supported by the current cast controller
         *
         * @returns { Promise<Array<AVCastControlCommandType>> } array of AVCastControlCommandType promise
         * @throws { BusinessError } 6600101 - Session service exception.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 11
         */
        getValidCommands(): Promise<Array<AVCastControlCommandType>>;
        /**
         * Process the response corresponding to the media key request obtained by the application.
         *
         * @param { string } assetId - The assetId of resource which provides the response.
         * @param { Uint8Array } response - Response corresponding to the request.
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 12
         */
        processMediaKeyResponse(assetId: string, response: Uint8Array): Promise<void>;
        /**
         * Sends custom data to a remote device.
         *
         * @param { Record<string, Object> } data Custom data populated by the application.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 6600101 - Session service exception.
         *     You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        sendCustomData(data: Record<string, Object>): Promise<void>;
        /**
         * Destroy the controller
         *
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 11
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Destroy the controller
         *
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 11
         */
        release(): Promise<void>;
        /**
         * Register playback state changed callback
         *
         * @param { 'playbackStateChange' } type
         * @param { Array<keyof AVPlaybackState> | 'all' } filter - The properties of {@link AVPlaybackState} that you cared
         *     about
         * @param { function } callback - The callback used to handle playback state changed event.
         *     The callback function provides the {@link AVPlaybackState} parameter.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void): void;
        /**
         * Unregister playback state changed callback
         *
         * @param { 'playbackStateChange' } type
         * @param { function } callback - The callback used to handle playback state changed event.
         *     The callback function provides the {@link AVPlaybackState} parameter.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void): void;
        /**
         * Register listener for current media item playback events.
         *
         * @param { 'mediaItemChange' } type Type of the playback event to listen for.
         * @param { Callback<AVQueueItem> } callback Callback used to listen for current item changed.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'mediaItemChange', callback: Callback<AVQueueItem>): void;
        /**
         * Unregister listener for current media item playback events.
         *
         * @param { 'mediaItemChange' } type Type of the playback event to listen for.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'mediaItemChange'): void;
        /**
         * Register playback command callback sent by remote side or media center.
         * Application needs update the new media resource when receive these commands by using playItem.
         *
         * @param { 'playNext' } type - Type of the 'playNext' event to listen for.
         * @param { Callback<void> } callback - Used to handle 'playNext' command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'playNext', callback: Callback<void>): void;
        /**
         * Unregister playback command callback sent by remote side or media center.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { 'playNext' } type - Type of the 'playNext' event to listen for.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'playNext'): void;
        /**
         * Register playback command callback sent by remote side or media center.
         * Application needs update the new media resource when receive these commands by using playItem.
         *
         * @param { 'playPrevious' } type - Type of the 'playPrevious' to listen for.
         * @param { Callback<void> } callback - Used to handle 'playPrevious' command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'playPrevious', callback: Callback<void>): void;
        /**
         * Unregister playback command callback sent by remote side or media center.
         * When canceling the callback, need to update the supported commands list.
         *
         * @param { 'playPrevious' } type - Type of the 'playPrevious' to listen for.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'playPrevious'): void;
        /**
         * Register requested playback command callback sent by remote side or media center.
         * The AVQueueItem may include the requested assetId, starting position and other configurations.
         *
         * @param { 'requestPlay' } type - Type of the 'requestPlay' to listen for.
         * @param { Callback<AVQueueItem> } callback - Used to handle 'requestPlay' command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 11
         */
        on(type: 'requestPlay', callback: Callback<AVQueueItem>): void;
        /**
         * Unregister requested playback command callback sent by remote side or media center.
         *
         * @param { 'requestPlay' } type - Type of the 'requestPlay' to listen for.
         * @param { Callback<AVQueueItem> } callback - Used to handle 'requestPlay' command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 11
         */
        off(type: 'requestPlay', callback?: Callback<AVQueueItem>): void;
        /**
         * Register endOfStream state callback.
         * Application needs update the new media resource when receive these commands by using playItem.
         *
         * @param { 'endOfStream' } type - Type of the 'endOfStream' to listen for.
         * @param { Callback<void> } callback - Used to handle 'endOfStream' command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 11
         */
        on(type: 'endOfStream', callback: Callback<void>): void;
        /**
         * Unregister endOfStream state callback.
         *
         * @param { 'endOfStream' } type - Type of the 'endOfStream' to listen for.
         * @param { Callback<void> } callback - Used to handle 'endOfStream' command
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 11
         */
        off(type: 'endOfStream', callback?: Callback<void>): void;
        /**
         * Register listens for playback events.
         *
         * @param { 'seekDone' } type - Type of the 'seekDone' to listen for.
         * @param { Callback<number> } callback - Callback used to listen for the playback seekDone event.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'seekDone', callback: Callback<number>): void;
        /**
         * Unregister listens for playback events.
         *
         * @param { 'seekDone' } type - Type of the 'seekDone' to listen for.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'seekDone'): void;
        /**
         * Register the valid commands of the casted session changed callback
         *
         * @param { 'validCommandChange' } type - 'validCommandChange'
         * @param { Callback<Array<AVCastControlCommandType>> } callback - The callback used to handle the changes.
         *     The callback function provides an array of AVCastControlCommandType.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @FaAndStageModel
         * @since 11
         */
        on(type: 'validCommandChange', callback: Callback<Array<AVCastControlCommandType>>);
        /**
         * Unregister the valid commands of the casted session changed callback
         *
         * @param { 'validCommandChange' } type - 'validCommandChange'
         * @param { Callback<Array<AVCastControlCommandType>> } callback - The callback used to handle the changes.
         *     The callback function provides an array of AVCastControlCommandType.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @FaAndStageModel
         * @since 11
         */
        off(type: 'validCommandChange', callback?: Callback<Array<AVCastControlCommandType>>);
        /**
         * Register listener for video size change event, used at remote side.
         *
         * @param { 'videoSizeChange' } type - Type of the 'videoSizeChange' to listen for.
         * @param { function } callback - Callback used to return video size.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 12
         */
        on(type: 'videoSizeChange', callback: (width: number, height: number) => void): void;
        /**
         * Unregister listener for video size change event, used at remote side.
         *
         * @param { 'videoSizeChange' } type - Type of the 'videoSizeChange' to listen for.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 12
         */
        off(type: 'videoSizeChange'): void;
        /**
         * Register listeners for playback error events.
         *
         * @param { 'error' } type Type of the 'error' to listen for.
         * @param { ErrorCallback } callback Callback used to listen for the playback error event.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 5400101 - No memory.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @throws { BusinessError } 5400103 - I/O error.
         * @throws { BusinessError } 5400104 - Time out.
         * @throws { BusinessError } 5400105 - Service died.
         * @throws { BusinessError } 5400106 - Unsupport format.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unregister listens for playback error events.
         *
         * @param { 'error' } type Type of the 'error' to listen for.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 5400101 - No memory.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @throws { BusinessError } 5400103 - I/O error.
         * @throws { BusinessError } 5400104 - Time out.
         * @throws { BusinessError } 5400105 - Service died.
         * @throws { BusinessError } 5400106 - Unsupport format.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'error'): void;
        /**
         * Register listeners for cast control generic error events.
         *
         * @param { 'castControlGenericError' } type Type of the 'castControlGenericError' to listen for.
         * @param { ErrorCallback } callback Callback used to listen for the cast control error event.
         * @throws { BusinessError } 401 - Parameter check failed. 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 6611000 - The error code for cast control is unspecified.
         * @throws { BusinessError } 6611001 - An unspecified error occurs in the remote player.
         * @throws { BusinessError } 6611002 - The playback position falls behind the live window.
         * @throws { BusinessError } 6611003 - The process of cast control times out.
         * @throws { BusinessError } 6611004 - The runtime check failed.
         * @throws { BusinessError } 6611100 - Cross-device data transmission is locked.
         * @throws { BusinessError } 6611101 - The specified seek mode is not supported.
         * @throws { BusinessError } 6611102 - The position to seek to is out of the range of the media asset
         *     or the specified seek mode is not supported.
         * @throws { BusinessError } 6611103 - The specified playback mode is not supported.
         * @throws { BusinessError } 6611104 - The specified playback speed is not supported.
         * @throws { BusinessError } 6611105 - The action failed because either the media source device or the media sink
         *     device has been revoked.
         * @throws { BusinessError } 6611106 - The parameter is invalid, for example, the url is illegal to play.
         * @throws { BusinessError } 6611107 - Allocation of memory failed.
         * @throws { BusinessError } 6611108 - Operation is not allowed.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        on(type: 'castControlGenericError', callback: ErrorCallback): void;
        /**
         * Unregister listeners for cast control generic error events.
         *
         * @param { 'castControlGenericError' } type Type of the 'castControlGenericError' to listen for.
         * @param { ErrorCallback } callback Callback used to listen for the cast control error event.
         * @throws { BusinessError } 401 - Parameter check failed. 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        off(type: 'castControlGenericError', callback?: ErrorCallback): void;
        /**
         * Register listeners for cast control input/output error events.
         *
         * @param { 'castControlIoError' } type Type of the 'castControlIoError' to listen for.
         * @param { ErrorCallback } callback Callback used to listen for the cast control error event.
         * @throws { BusinessError } 401 - Parameter check failed. 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 6612000 - An unspecified input/output error occurs.
         * @throws { BusinessError } 6612001 - Network connection failure.
         * @throws { BusinessError } 6612002 - Network timeout.
         * @throws { BusinessError } 6612003 - Invalid "Content-Type" HTTP header.
         * @throws { BusinessError } 6612004 - The HTTP server returns an unexpected HTTP response status code.
         * @throws { BusinessError } 6612005 - The file does not exist.
         * @throws { BusinessError } 6612006 - No permission is granted to perform the IO operation.
         * @throws { BusinessError } 6612007 - Access to cleartext HTTP traffic is not allowed by the app's network security
         *     configuration.
         * @throws { BusinessError } 6612008 - Reading data out of the data bound.
         * @throws { BusinessError } 6612100 - The media does not contain any contents that can be played.
         * @throws { BusinessError } 6612101 - The media cannot be read, for example, because of dust or scratches.
         * @throws { BusinessError } 6612102 - This resource is already in use.
         * @throws { BusinessError } 6612103 - The content using the validity interval has expired.
         * @throws { BusinessError } 6612104 - Using the requested content to play is not allowed.
         * @throws { BusinessError } 6612105 - The use of the allowed content cannot be verified.
         * @throws { BusinessError } 6612106 - The number of times this content has been used as requested has reached the
         *     maximum allowed number of uses.
         * @throws { BusinessError } 6612107 - An error occurs when sending packet from source device to sink device.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        on(type: 'castControlIoError', callback: ErrorCallback): void;
        /**
         * Unregister listeners for cast control input/output error events.
         *
         * @param { 'castControlIoError' } type Type of the 'castControlIoError' to listen for.
         * @param { ErrorCallback } callback Callback used to listen for the cast control error event.
         * @throws { BusinessError } 401 - Parameter check failed. 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        off(type: 'castControlIoError', callback?: ErrorCallback): void;
        /**
         * Register listeners for cast control parsing error events.
         *
         * @param { 'castControlParsingError' } type Type of the 'castControlParsingError' to listen for.
         * @param { ErrorCallback } callback Callback used to listen for the cast control error event.
         * @throws { BusinessError } 401 - Parameter check failed. 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 6613000 - Unspecified error related to content parsing.
         * @throws { BusinessError } 6613001 - Parsing error associated with media container format bit streams.
         * @throws { BusinessError } 6613002 - Parsing error associated with the media manifest.
         * @throws { BusinessError } 6613003 - An error occurs when attempting to extract a file with an unsupported media
         *     container format
         *     or an unsupported media container feature.
         * @throws { BusinessError } 6613004 - Unsupported feature in the media manifest.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        on(type: 'castControlParsingError', callback: ErrorCallback): void;
        /**
         * Unregister listeners for cast control parsing error events.
         *
         * @param { 'castControlParsingError' } type Type of the 'castControlParsingError' to listen for.
         * @param { ErrorCallback } callback Callback used to listen for the cast control error event.
         * @throws { BusinessError } 401 - Parameter check failed. 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        off(type: 'castControlParsingError', callback?: ErrorCallback): void;
        /**
         * Register listeners for cast control decoding error events.
         *
         * @param { 'castControlDecodingError' } type Type of the 'castControlDecodingError' to listen for.
         * @param { ErrorCallback } callback Callback used to listen for the cast control error event.
         * @throws { BusinessError } 401 - Parameter check failed. 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 6614000 - Unspecified decoding error.
         * @throws { BusinessError } 6614001 - Decoder initialization failed.
         * @throws { BusinessError } 6614002 - Decoder query failed.
         * @throws { BusinessError } 6614003 - Decoding the media samples failed.
         * @throws { BusinessError } 6614004 - The format of the content to decode exceeds the capabilities of the device.
         * @throws { BusinessError } 6614005 - The format of the content to decode is not supported.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        on(type: 'castControlDecodingError', callback: ErrorCallback): void;
        /**
         * Unregister listeners for cast control decoding error events.
         *
         * @param { 'castControlDecodingError' } type Type of the 'castControlDecodingError' to listen for.
         * @param { ErrorCallback } callback Callback used to listen for the cast control error event.
         * @throws { BusinessError } 401 - Parameter check failed. 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        off(type: 'castControlDecodingError', callback?: ErrorCallback): void;
        /**
         * Register listeners for cast control audio renderer error error events.
         *
         * @param { 'castControlAudioRendererError' } type Type of the 'castControlAudioRendererError' to listen for.
         * @param { ErrorCallback } callback Callback used to listen for the cast control error event.
         * @throws { BusinessError } 401 - Parameter check failed. 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 6615000 - Unspecified errors related to the audio renderer.
         * @throws { BusinessError } 6615001 - Initializing the audio renderer failed.
         * @throws { BusinessError } 6615002 - The audio renderer fails to write data.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        on(type: 'castControlAudioRendererError', callback: ErrorCallback): void;
        /**
         * Unregister listeners for cast control audio renderer error events.
         *
         * @param { 'castControlAudioRendererError' } type Type of the 'castControlAudioRendererError' to listen for.
         * @param { ErrorCallback } callback Callback used to listen for the cast control error event.
         * @throws { BusinessError } 401 - Parameter check failed. 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        off(type: 'castControlAudioRendererError', callback?: ErrorCallback): void;
        /**
         * Register listeners for cast control drm error events.
         *
         * @param { 'castControlDrmError' } type Type of the 'castControlDrmError' to listen for.
         * @param { ErrorCallback } callback Callback used to listen for the cast control error event.
         * @throws { BusinessError } 401 - Parameter check failed. 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 6616000 - Unspecified error related to DRM.
         * @throws { BusinessError } 6616001 - The chosen DRM protection scheme is not supported by the device.
         * @throws { BusinessError } 6616002 - Device provisioning failed.
         * @throws { BusinessError } 6616003 - The DRM-protected content to play is incompatible.
         * @throws { BusinessError } 6616004 - Failed to obtain a license.
         * @throws { BusinessError } 6616005 - The operation is disallowed by the license policy.
         * @throws { BusinessError } 6616006 - An error occurs in the DRM system.
         * @throws { BusinessError } 6616007 - The device has revoked DRM privileges.
         * @throws { BusinessError } 6616008 - The DRM license being loaded into the open DRM session has expired.
         * @throws { BusinessError } 6616100 - An error occurs when the DRM processes the key response.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        on(type: 'castControlDrmError', callback: ErrorCallback): void;
        /**
         * Unregister listeners for cast control drm error events.
         *
         * @param { 'castControlDrmError' } type Type of the 'castControlDrmError' to listen for.
         * @param { ErrorCallback } callback Callback used to listen for the cast control error event.
         * @throws { BusinessError } 401 - Parameter check failed. 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        off(type: 'castControlDrmError', callback?: ErrorCallback): void;
        /**
         * Register listener for drm key request.
         *
         * @param { 'keyRequest' } type - Type of the 'keyRequest' to listen for.
         * @param { KeyRequestCallback } callback - Callback used to request drm key.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 12
         */
        on(type: 'keyRequest', callback: KeyRequestCallback): void;
        /**
         * Unregister listener for drm key request.
         *
         * @param { 'keyRequest' } type - Type of the 'keyRequest' to listen for.
         * @param { KeyRequestCallback } callback - Callback used to request drm key.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 12
         */
        off(type: 'keyRequest', callback?: KeyRequestCallback): void;
        /**
         * Register listener for custom data sent from remote device.
         *
         * @param { 'customDataChange' } type - Type of the 'customDataChange' to listen for.
         * @param { Callback<Record<string, Object>> } callback - Callback used to retrieve custom data.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void;
        /**
         * Unregister listener for custom data sent from remote device.
         *
         * @param { 'customDataChange' } type - Type of the 'customDataChange' to listen for.
         * @param { Callback<Record<string, Object>> } [callback] - Callback used to retrieve custom data.
         * @throws { BusinessError } 6600101 - Session service exception
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void;
    }
    /**
     * A helper to enable a picker to select output devices
     *
     * @syscap SystemCapability.Multimedia.AVSession.AVCast
     * @atomicservice
     * @since 14
     */
    class AVCastPickerHelper {
        /**
         * The constructor used to create a AVCastPickerHelper object.
         *
         * @param { Context } context - represents the context.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 14
         */
        constructor(context: Context);
        /**
         * Pull up the avcastpicker based on the options.
         *
         * @param { AVCastPickerOptions } [options] - represents the options provided to  the picker.
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 14
         */
        select(options?: AVCastPickerOptions): Promise<void>;
        /**
         * Reset audio device to be default set by the platform which is used for communication use cases
         * including voice or video calls.
         * For example, the audio output device will be switched to earpiece for voice call and
         * to speaker for video call on phone.
         *
         * @returns { Promise<void> } void promise when executed successfully
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 21
         */
        resetCommunicationDevice(): Promise<void>;
        /**
         * Register picker state change callback.
         *
         * @param { 'pickerStateChange' } type - 'pickerStateChange'
         * @param { Callback<AVCastPickerState> } callback - The callback used to handle picker state changed event.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 14
         */
        on(type: 'pickerStateChange', callback: Callback<AVCastPickerState>): void;
        /**
         * Unregister picker state change callback.
         *
         * @param { 'pickerStateChange' } type - 'pickerStateChange'
         * @param { Callback<AVCastPickerState> } callback - The callback used to handle picker state changed event.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 14
         */
        off(type: 'pickerStateChange', callback?: Callback<AVCastPickerState>): void;
    }
    /**
     * Audio capabilities.
     *
     * @syscap SystemCapability.Multimedia.AVSession.AVCast
     * @atomicservice
     * @since 20
     */
    interface AudioCapabilities {
        /**
         * Audio stream information.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        readonly streamInfos: Array<audio.AudioStreamInfo>;
    }
    /**
     * Position definition of one component on which the menu will bind and popup.
     *
     * @syscap SystemCapability.Multimedia.AVSession.AVCast
     * @atomicservice
     * @since 22
     */
    interface MenuPosition {
        /**
         * Coordinate x of the position of the component, uint is vp.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 22
         */
        x: number;
        /**
         * Coordinate y of the position of the component, uint is vp.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 22
         */
        y: number;
        /**
         * Component width, uint is vp.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 22
         */
        width: number;
        /**
         * Component height, uint is vp.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 22
         */
        height: number;
    }
    /**
     * An option to make different picker usage
     *
     * @syscap SystemCapability.Multimedia.AVSession.AVCast
     * @atomicservice
     * @since 14
     */
    interface AVCastPickerOptions {
        /**
         * Indicates current session type to show different picker ui.
         * If not set, default value is 'audio'.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 14
         */
        sessionType?: AVSessionType;
        /**
         * Set the picker style.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 22
         */
        pickerStyle?: AVCastPickerStyle;
        /**
         * Set the popup menu position if pickerstyple is set to STYLE_MENU.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @since 22
         */
        menuPosition?: MenuPosition;
    }
    /**
     * The callback of key request.
     *
     * @param { string } assetId - request key for current assetId
     * @param { Uint8Array } requestData - media key request data sent to media key server
     * @syscap SystemCapability.Multimedia.AVSession.AVCast
     * @atomicservice
     * @since 12
     */
    type KeyRequestCallback = (assetId: string, requestData: Uint8Array) => void;
    /**
     * Enumerates the cast display states.
     *
     * @syscap SystemCapability.Multimedia.AVSession.ExtendedDisplayCast
     * @atomicservice
     * @since 12
     */
    enum CastDisplayState {
        /**
         * Screen off.
         *
         * @syscap SystemCapability.Multimedia.AVSession.ExtendedDisplayCast
         * @atomicservice
         * @since 12
         */
        STATE_OFF = 1,
        /**
         * Screen on.
         *
         * @syscap SystemCapability.Multimedia.AVSession.ExtendedDisplayCast
         * @atomicservice
         * @since 12
         */
        STATE_ON = 2
    }
    /**
     * Define the information for extended display screen.
     *
     * @syscap SystemCapability.Multimedia.AVSession.ExtendedDisplayCast
     * @atomicservice
     * @since 12
     */
    interface CastDisplayInfo {
        /**
         * Display ID.
         * The application can get more display information based on the same id from display interface.
         *
         * @syscap SystemCapability.Multimedia.AVSession.ExtendedDisplayCast
         * @atomicservice
         * @since 12
         */
        id: number;
        /**
         * Display name.
         *
         * @syscap SystemCapability.Multimedia.AVSession.ExtendedDisplayCast
         * @atomicservice
         * @since 12
         */
        name: string;
        /**
         * The state of display.
         *
         * @syscap SystemCapability.Multimedia.AVSession.ExtendedDisplayCast
         * @atomicservice
         * @since 12
         */
        state: CastDisplayState;
        /**
         * Display width, in pixels.
         *
         * @syscap SystemCapability.Multimedia.AVSession.ExtendedDisplayCast
         * @atomicservice
         * @since 12
         */
        width: number;
        /**
         * Display height, in pixels.
         *
         * @syscap SystemCapability.Multimedia.AVSession.ExtendedDisplayCast
         * @atomicservice
         * @since 12
         */
        height: number;
    }
    /**
     * Define the device connection state.
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    enum ConnectionState {
        /**
         * A connection state indicating the device is in the process of connecting.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        STATE_CONNECTING = 0,
        /**
         * A connection state indicating the device is connected.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        STATE_CONNECTED = 1,
        /**
         * The default connection state indicating the device is disconnected.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        STATE_DISCONNECTED = 6
    }
    /**
     * The pre-defined display tag by system.
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @since 11
     */
    enum DisplayTag {
        /**
         * Indicate the AUDIO VIVID property of current media resource.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        TAG_AUDIO_VIVID = 1
    }
    /**
     * The defination of decoder type.
     *
     * @syscap SystemCapability.Multimedia.AVSession.AVCast
     * @atomicservice
     * @since 19
     */
    enum DecoderType {
        /**
         * Defination of avc codec type.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 19
         */
        OH_AVCODEC_MIMETYPE_VIDEO_AVC = 'video/avc',
        /**
         * Defination of hevc codec type.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 19
         */
        OH_AVCODEC_MIMETYPE_VIDEO_HEVC = 'video/hevc',
        /**
         * Defination of audio vivid codec type.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 19
         */
        OH_AVCODEC_MIMETYPE_AUDIO_VIVID = 'audio/av3a'
    }
    /**
     * The defination of suggested resolution.
     *
     * @syscap SystemCapability.Multimedia.AVSession.AVCast
     * @atomicservice
     * @since 19
     */
    enum ResolutionLevel {
        /**
         * Defination of 480P which typically resolution is 640*480.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 19
         */
        RESOLUTION_480P = 0,
        /**
         * Defination of 720P which typically resolution is 1280*720.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 19
         */
        RESOLUTION_720P = 1,
        /**
         * Defination of 1080P which typically resolution is 1920*1080.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 19
         */
        RESOLUTION_1080P = 2,
        /**
         * Defination of 2K which typically resolution is 2560*1440.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 19
         */
        RESOLUTION_2K = 3,
        /**
         * Defination of 4K which typically resolution is 4096*3840.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 19
         */
        RESOLUTION_4K = 4
    }
    /**
     * Define some common extra keys used in different scenarios.
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    enum ExtraKey {
        /**
         * Set required abilities to the system.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        REQUIRE_ABILITY_LIST = 'requireAbilityList',
        /**
         * Informs the system that the app supports URL casting.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        SUPPORT_URL_CASTING = 'url-cast',
        /**
         * Key for DLNA CurrentURIMetadata extra parameter.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        DLNA_CURRENT_URI_METADATA = 'CurrentURIMetadata',
        /**
         * Key for DLNA DIDL-Lite extra parameter.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        DLNA_DIDL_LITE = 'DIDL-Lite'
    }
    /**
     * The metadata of the current media.Used to set the properties of the current media file
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface AVMetadata {
        /**
         * Unique ID used to represent this media.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        assetId: string;
        /**
         * The title of this media, for display in media center.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        title?: string;
        /**
         * The artist of this media
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        artist?: string;
        /**
         * The author of this media
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        author?: string;
        /**
         * The name of play list which current media belongs to
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 12
         */
        avQueueName?: string;
        /**
         * The id of play list which current media belongs to, it should be an unique identifier in the application.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        avQueueId?: string;
        /**
         * The artwork of play list as a {@link PixelMap} or an uri formatted String,
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        avQueueImage?: image.PixelMap | string;
        /**
         * The album of this media
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        album?: string;
        /**
         * The writer of this media
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        writer?: string;
        /**
         * The composer of this media
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        composer?: string;
        /**
         * The duration of this media, used to automatically calculate playback position, described by milliseconds.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        duration?: number;
        /**
         * The image of the media as a {@link PixelMap} or an uri formatted String,
         * used to display in media center.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        mediaImage?: image.PixelMap | string;
        /**
         * The image of the bundle icon as a {@link PixelMap}, no need to be set by application.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 18
         */
        readonly bundleIcon?: image.PixelMap;
        /**
         * The publishDate of the media
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        publishDate?: Date;
        /**
         * The subtitle of the media, used for display
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        subtitle?: string;
        /**
         * The description of the media, used for display
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        description?: string;
        /**
         * The lyric of the media, it should be in standard lyric format
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        lyric?: string;
        /**
         * The single lyric text of the media, not including time prefix
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice
         * @since 17
         */
        singleLyricText?: string;
        /**
         * The previous playable media id.
         * Used to tell the controller if there is a previous playable media
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        previousAssetId?: string;
        /**
         * The next playable media id.
         * Used to tell the controller if there is a next playable media
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        nextAssetId?: string;
        /**
         * The protocols supported by this session, if not set, the default is {@link TYPE_CAST_PLUS_STREAM}.
         * See {@link ProtocolType}
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        filter?: number;
        /**
         * The drm schemes supported by this session which are represented by uuid.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 12
         */
        drmSchemes?: Array<string>;
        /**
         * The supported skipIntervals when doing fast forward and rewind operation, the default is {@link SECONDS_15}.
         * See {@link SkipIntervals}
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        skipIntervals?: SkipIntervals;
        /**
         * The display tags supported by application to be displayed on media center
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        displayTags?: number;
        /**
         * The supported skipIntervals when doing rewind operation, the default is {@link SECONDS_15}.
         * The system will use this value for rewind skip intervals instead of {@link skipIntervals}.
         * If not set, the rewind skip intervals still use {@link skipIntervals}.
         * See {@link SkipIntervals}
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        rewindSkipIntervals?: SkipIntervals;
        /**
         * The supported skipIntervals when doing fast forward operation, the default is {@link SECONDS_15}.
         * The system will use this value for fastforward skip intervals instead of {@link skipIntervals}.
         * If not set, the fast forward skip intervals still use {@link skipIntervals}.
         * See {@link SkipIntervals}
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        fastForwardSkipIntervals?: SkipIntervals;
    }
    /**
     * The description of the media for an item in the playlist of the session
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface AVMediaDescription {
        /**
         * Unique ID used to represent this media.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        assetId: string;
        /**
         * The title of this media, for display in media center.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        title?: string;
        /**
         * The subtitle of the media, used for display
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        subtitle?: string;
        /**
         * The description of this media
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        description?: string;
        /**
         * The image of this media asset displayed in the media center.
         * It can be a {@link PixelMap} or a URI formatted string,
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        mediaImage?: image.PixelMap | string;
        /**
         * Any additional attributes that can be represented as key-value pairs
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @since 10
         */
        extras?: {
            [key: string]: Object;
        };
        /**
         * The type of this media, such as video, audio and so on.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        mediaType?: string;
        /**
         * The size of this media.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        mediaSize?: number;
        /**
         * The album title of this media
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        albumTitle?: string;
        /**
         * The album cover uri of this media
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        albumCoverUri?: string;
        /**
         * The lyric content of the media, it should be in standard lyric format
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        lyricContent?: string;
        /**
         * The lyric uri of the media.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        lyricUri?: string;
        /**
         * The artist of this media.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        artist?: string;
        /**
         * The uri of the media, used to locate the media in some special cases
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        mediaUri?: string;
        /**
         * Media file descriptor.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        fdSrc?: media.AVFileDescriptor;
        /**
         * DataSource descriptor. The caller ensures the fileSize and callback are valid.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 12
         */
        dataSrc?: media.AVDataSrcDescriptor;
        /**
         * Source type that supports PCM casting.
         * The application can send PCM data directly to the system through audio APIs, without using AVSession to set data.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice
         * @since 20
         */
        pcmSrc?: boolean;
        /**
         * The drm scheme supported by this resource which is represented by uuid.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 12
         */
        drmScheme?: string;
        /**
         * The duration of this media, described by milliseconds.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        duration?: number;
        /**
         * Media start position, described by milliseconds.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        startPosition?: number;
        /**
         * Media credits position, described by milliseconds.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        creditsPosition?: number;
        /**
         * Application name.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        appName?: string;
        /**
         * The display tags supported by application to be displayed on media center
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        displayTags?: number;
        /**
         * Custom data sent by the application to the receiver during casting.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        launchClientData?: string;
    }
    /**
     * The item in the playlist of the session
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface AVQueueItem {
        /**
         * Sequence number of the item in the playlist.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        itemId: number;
        /**
         * The media description of the item in the playlist.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        description?: AVMediaDescription;
    }
    /**
     * Used to indicate the playback state of the current media.
     * If the playback state of the media changes, it needs to be updated synchronously
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface AVPlaybackState {
        /**
         * Current playback state. See {@link PlaybackState}
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        state?: PlaybackState;
        /**
         * Current playback speed
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        speed?: number;
        /**
         * Current playback position of this media. See {@link PlaybackPosition}
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        position?: PlaybackPosition;
        /**
         * The current buffered time, the maximum playable position, described by milliseconds.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        bufferedTime?: number;
        /**
         * Current playback loop mode. See {@link LoopMode}
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        loopMode?: LoopMode;
        /**
         * Current Favorite Status
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        isFavorite?: boolean;
        /**
         * Current active item id
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        activeItemId?: number;
        /**
         * Current player volume
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        volume?: number;
        /**
         * maximum  volume
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        maxVolume?: number;
        /**
         * Current muted status
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        muted?: boolean;
        /**
         * The duration of this media asset, described by milliseconds.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        duration?: number;
        /**
         * The video width of this media asset.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        videoWidth?: number;
        /**
         * The video height of this media asset.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        videoHeight?: number;
        /**
         * Current custom media packets
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        extras?: {
            [key: string]: Object;
        };
    }
    /**
     * Playback position definition
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface PlaybackPosition {
        /**
         * Elapsed time(position) of this media set by the app, described by milliseconds.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        elapsedTime: number;
        /**
         * Record the system time when elapsedTime is set, described by milliseconds.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        updateTime: number;
    }
    /**
     * The metadata of the current call.
     *
     * @interface CallMetadata [since 11 - 11]
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 11
     */
    interface CallMetadata {
        /**
         * The displayed user name of current call.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        name?: string;
        /**
         * The phone number of current call.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        phoneNumber?: string;
        /**
         * The displayed picture that represents a particular user.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        avatar?: image.PixelMap;
    }
    /**
     * Used to indicate the call state of the current call.
     *
     * @interface AVCallState [since 11 - 11]
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 11
     */
    interface AVCallState {
        /**
         * Current call state. See {@link CallState}
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        state: CallState;
        /**
         * Current muted status.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        muted: boolean;
    }
    /**
     * Enumeration of current call state
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 11
     */
    enum CallState {
        /**
         * Idle state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        CALL_STATE_IDLE = 0,
        /**
         * Incoming state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        CALL_STATE_INCOMING = 1,
        /**
         * Active state in calling.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        CALL_STATE_ACTIVE = 2,
        /**
         * Dialing state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        CALL_STATE_DIALING = 3,
        /**
         * Waiting state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        CALL_STATE_WAITING = 4,
        /**
         * Holding state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        CALL_STATE_HOLDING = 5,
        /**
         * Disconnecting state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        CALL_STATE_DISCONNECTING = 6
    }
    /**
     * cast category indicating different playback scenes
     *
     * @syscap SystemCapability.Multimedia.AVSession.AVCast
     * @atomicservice [since 12]
     * @since 10
     */
    enum AVCastCategory {
        /**
         * The default cast type "local", media can be routed on the same device,
         * including internal speakers or audio jack on the device itself, A2DP devices.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        CATEGORY_LOCAL = 0,
        /**
         * The remote category indicating the media is presenting on a remote device,
         * the application needs to get an AVCastController to control remote playback.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        CATEGORY_REMOTE = 1
    }
    /**
     * Device type definition
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    enum DeviceType {
        /**
         * A device type indicating the route is on internal speakers or audio jack on the device itself.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        DEVICE_TYPE_LOCAL = 0,
        /**
         * A device type indicating the route is on a TV.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        DEVICE_TYPE_TV = 2,
        /**
         * A device type indicating the route is on a smart speaker.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 10
         */
        DEVICE_TYPE_SMART_SPEAKER = 3,
        /**
         * The device type is a car.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        DEVICE_TYPE_CAR = 4,
        /**
         * The device type is a pad.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        DEVICE_TYPE_PAD = 6,
        /**
         * A default device which supports Cast+ Stream protocol.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        DEVICE_TYPE_DEFAULT_CAST_PLUS_STREAM = 7,
        /**
         * The device type is a 2in1.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        DEVICE_TYPE_2IN1 = 8,
        /**
         * A device type indicating the route is on a bluetooth device.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        DEVICE_TYPE_BLUETOOTH = 10,
        /**
         * The device which supports HiPlay protocol.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        DEVICE_TYPE_HIPLAY = 15
    }
    /**
     * Device Information Definition
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface DeviceInfo {
        /**
         * The playback type supported by the device. See {@link AVCastCategory}
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        castCategory: AVCastCategory;
        /**
         * Audio device id.The length of the audioDeviceId array is greater than 1
         * if output to multiple devices at the same time.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        deviceId: string;
        /**
         * Device name. The length of the deviceName array is greater than 1
         * if output to multiple devices at the same time.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        deviceName: string;
        /**
         * device type.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        deviceType: DeviceType;
        /**
         * Device manufacturer.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        manufacturer?: string;
        /**
         * Device model name.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        modelName?: string;
        /**
         * The protocols supported by current device, can be union of {@link ProtocolType}.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice [since 12]
         * @since 11
         */
        supportedProtocols?: number;
        /**
         * The drm capability supported by current device, each drm is represented by uuid.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 12
         */
        supportedDrmCapabilities?: Array<string>;
        /**
         * Whether the device supports pull-end playback, including a collection of pull-end client IDs.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        supportedPullClients?: Array<number>;
        /**
         * Audio capabilities supported by the device.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        audioCapabilities?: AudioCapabilities;
    }
    /**
     * Target Device Information Definition
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface OutputDeviceInfo {
        /**
         * Arrays of device information
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        devices: Array<DeviceInfo>;
    }
    /**
     * Loop Play Mode Definition
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    enum LoopMode {
        /**
         * The default mode is sequential playback
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        LOOP_MODE_SEQUENCE = 0,
        /**
         * Single loop mode
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        LOOP_MODE_SINGLE = 1,
        /**
         * List loop mode
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        LOOP_MODE_LIST = 2,
        /**
         * Shuffle playback mode
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        LOOP_MODE_SHUFFLE = 3,
        /**
         * Custom playback mode supported by application
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        LOOP_MODE_CUSTOM = 4
    }
    /**
     * Supported skip intervals definition
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @since 11
     */
    enum SkipIntervals {
        /**
         * 10 seconds
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        SECONDS_10 = 10,
        /**
         * 15 seconds
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        SECONDS_15 = 15,
        /**
         * 30 seconds
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        SECONDS_30 = 30
    }
    /**
     * Supported background play mode definitions.
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @stagemodelonly
     * @since 24
     */
    enum BackgroundPlayMode {
        /**
         * Enable background playback
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 24
         */
        ENABLE_BACKGROUND_PLAY = 0,
        /**
         * Disable background playback
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 24
         */
        DISABLE_BACKGROUND_PLAY = 1
    }
    /**
     * Definition of current playback state
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    enum PlaybackState {
        /**
         * Initial state. The initial state of media file
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        PLAYBACK_STATE_INITIAL = 0,
        /**
         * Preparing state. Indicates that the media file is not ready to play,
         * the media is loading or buffering
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        PLAYBACK_STATE_PREPARE = 1,
        /**
         * Playing state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        PLAYBACK_STATE_PLAY = 2,
        /**
         * Paused state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        PLAYBACK_STATE_PAUSE = 3,
        /**
         * Fast forwarding state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        PLAYBACK_STATE_FAST_FORWARD = 4,
        /**
         * Rewinding state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        PLAYBACK_STATE_REWIND = 5,
        /**
         * Stopped state.The server will clear the media playback position and other information.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        PLAYBACK_STATE_STOP = 6,
        /**
         * Completed state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        PLAYBACK_STATE_COMPLETED = 7,
        /**
         * Released state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        PLAYBACK_STATE_RELEASED = 8,
        /**
         * error state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        PLAYBACK_STATE_ERROR = 9,
        /**
         * Idle state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        PLAYBACK_STATE_IDLE = 10,
        /**
         * Buffering state.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        PLAYBACK_STATE_BUFFERING = 11
    }
    /**
     * The description of the session
     *
     * @syscap SystemCapability.Multimedia.AVSession.Manager
     * @since 23
     */
    interface AVSessionDescriptor {
        /**
         * Unique ID of the session
         *
         * @syscap SystemCapability.Multimedia.AVSession.Manager
         * @since 23
         */
        sessionId: string;
        /**
         * Session type, currently supports audio or video
         *
         * @syscap SystemCapability.Multimedia.AVSession.Manager
         * @since 23
         */
        type: AVSessionType;
        /**
         * The session tag set by the application
         *
         * @syscap SystemCapability.Multimedia.AVSession.Manager
         * @since 23
         */
        sessionTag: string;
        /**
         * The elementName of the ability that created this session. See {@link ElementName} in bundle/elementName.d.ts
         *
         * @syscap SystemCapability.Multimedia.AVSession.Manager
         * @since 23
         */
        elementName: ElementName;
        /**
         * Session active state
         *
         * @syscap SystemCapability.Multimedia.AVSession.Manager
         * @since 23
         */
        isActive: boolean;
        /**
         * Is it the top priority session
         *
         * @syscap SystemCapability.Multimedia.AVSession.Manager
         * @since 23
         */
        isTopSession: boolean;
    }
    /**
     * The extra info object.
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @since 18
     */
    type ExtraInfo = {
        [key: string]: Object;
    };
    /**
     * Session controller,used to control media playback and get media information
     *
     * @interface AVSessionController [since 10 - 11]
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface AVSessionController {
        /**
         * Unique session Id
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        readonly sessionId: string;
        /**
         * Get the playback status of the current session
         *
         * @param { AsyncCallback<AVPlaybackState> } callback - The triggered asyncCallback when (getAVPlaybackState).
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void;
        /**
         * Get the playback status of the current session
         *
         * @returns { Promise<AVPlaybackState> } (AVPlaybackState) returned through promise
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getAVPlaybackState(): Promise<AVPlaybackState>;
        /**
         * Get the playback status of the current session
         *
         * @returns { AVPlaybackState } (AVPlaybackState) returned
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getAVPlaybackStateSync(): AVPlaybackState;
        /**
         * Get the metadata of the current session
         *
         * @param { AsyncCallback<AVMetadata> } callback - The triggered asyncCallback when (getAVMetadata).
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        getAVMetadata(callback: AsyncCallback<AVMetadata>): void;
        /**
         * Get the metadata of the current session
         *
         * @returns { Promise<AVMetadata> } (AVMetadata) returned through promise
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getAVMetadata(): Promise<AVMetadata>;
        /**
         * Get the metadata of the current session
         *
         * @returns { AVMetadata } (AVMetadata) returned
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getAVMetadataSync(): AVMetadata;
        /**
         * Get the call status of the current session
         *
         * @param { AsyncCallback<AVCallState> } callback - The triggered asyncCallback when (getAVCallState).
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        getAVCallState(callback: AsyncCallback<AVCallState>): void;
        /**
         * Get the call status of the current session
         *
         * @returns { Promise<AVCallState> } (AVCallState) returned through promise
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        getAVCallState(): Promise<AVCallState>;
        /**
         * Get the call metadata of the current session
         *
         * @param { AsyncCallback<CallMetadata> } callback - The triggered asyncCallback when (getCallMetadata).
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        getCallMetadata(callback: AsyncCallback<CallMetadata>): void;
        /**
         * Get the call metadata of the current session
         *
         * @returns { Promise<CallMetadata> } (CallMetadata) returned through promise
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 11
         */
        getCallMetadata(): Promise<CallMetadata>;
        /**
         * Get the name of the playlist of the current session
         *
         * @param { AsyncCallback<string> } callback - The triggered asyncCallback when (getAVQueueTitle).
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        getAVQueueTitle(callback: AsyncCallback<string>): void;
        /**
         * Get the name of the playlist of the current session
         *
         * @returns { Promise<string> } (string) returned through promise
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getAVQueueTitle(): Promise<string>;
        /**
         * Get the name of the playlist of the current session
         *
         * @returns { string } (string) returned
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getAVQueueTitleSync(): string;
        /**
         * Get the playlist of the current session
         *
         * @param { AsyncCallback<Array<AVQueueItem>> } callback - The triggered asyncCallback when (getAVQueueItems).
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        getAVQueueItems(callback: AsyncCallback<Array<AVQueueItem>>): void;
        /**
         * Get the playlist of the current session
         *
         * @returns { Promise<Array<AVQueueItem>> } (Array<AVQueueItem>) returned through promise
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getAVQueueItems(): Promise<Array<AVQueueItem>>;
        /**
         * Get the playlist of the current session
         *
         * @returns { Array<AVQueueItem> } (Array<AVQueueItem>) returned
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getAVQueueItemsSync(): Array<AVQueueItem>;
        /**
         * Set the item in the playlist to be played
         *
         * @param { number } itemId - The serial number of the item to be played
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        skipToQueueItem(itemId: number, callback: AsyncCallback<void>): void;
        /**
         * Set the item in the playlist to be played
         *
         * @param { number } itemId - The serial number of the item to be played
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        skipToQueueItem(itemId: number): Promise<void>;
        /**
         * Get output device information
         *
         * @param { AsyncCallback<OutputDeviceInfo> } callback - The triggered asyncCallback when (getOutputDevice).
         * @throws { BusinessError } 600101 - Session service exception.
         * @throws { BusinessError } 600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void;
        /**
         * Get output device information
         *
         * @returns { Promise<OutputDeviceInfo> } (OutputDeviceInfo) returned through promise
         * @throws { BusinessError } 600101 - Session service exception.
         * @throws { BusinessError } 600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getOutputDevice(): Promise<OutputDeviceInfo>;
        /**
         * Get output device information
         *
         * @returns { OutputDeviceInfo } (OutputDeviceInfo) returned
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getOutputDeviceSync(): OutputDeviceInfo;
        /**
         * Get supported speeds supplied by application.
         *
         * @returns { Promise<Array<number>> } Promise that returns no value.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getSupportedPlaySpeeds(): Promise<Array<number>>;
        /**
         * Get supported loop modes supplied by application.
         *
         * @returns { Promise<Array<LoopMode>> } supported loop modes returned through promise
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getSupportedLoopModes(): Promise<Array<LoopMode>>;
        /**
         * Send media key event to this session
         *
         * @param { KeyEvent } event - The KeyEvent
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 600101 - Session service exception.
         * @throws { BusinessError } 600102 - The session does not exist.
         * @throws { BusinessError } 600103 - The session controller does not exist.
         * @throws { BusinessError } 600105 - Invalid session command.
         * @throws { BusinessError } 600106 - The session is not activated.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        sendAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void;
        /**
         * Send media key event to this session
         *
         * @param { KeyEvent } event - The KeyEvent
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 600101 - Session service exception.
         * @throws { BusinessError } 600102 - The session does not exist.
         * @throws { BusinessError } 600103 - The session controller does not exist.
         * @throws { BusinessError } 600105 - Invalid session command.
         * @throws { BusinessError } 600106 - The session is not activated.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        sendAVKeyEvent(event: KeyEvent): Promise<void>;
        /**
         * Get the {@link WantAgent} of this session that can launch the session ability
         *
         * @param { AsyncCallback<WantAgent> } callback - The asyncCallback triggered when getting the WantAgent.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        getLaunchAbility(callback: AsyncCallback<WantAgent>): void;
        /**
         * Get the {@link WantAgent} of this session that can launch the session ability
         *
         * @returns { Promise<WantAgent> } WantAgent promise
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getLaunchAbility(): Promise<WantAgent>;
        /**
         * Get the adjusted playback position. The time automatically calculated by the system
         * taking into account factors such as playback status, playback speed, and application update time.
         *
         * @returns { number } current playback position in ms.Note that the returns value of each call will be different.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getRealPlaybackPositionSync(): number;
        /**
         * Check if the current session is active
         *
         * @param { AsyncCallback<boolean> } callback - The triggered asyncCallback when (isActive).
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        isActive(callback: AsyncCallback<boolean>): void;
        /**
         * Check if the current session is active
         *
         * @returns { Promise<boolean> } boolean promise
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        isActive(): Promise<boolean>;
        /**
         * Check if the current session is active
         *
         * @returns { boolean } boolean
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        isActiveSync(): boolean;
        /**
         * Destroy the server controller
         *
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        destroy(callback: AsyncCallback<void>): void;
        /**
         * Destroy the server controller
         *
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        destroy(): Promise<void>;
        /**
         * Get commands supported by the current session
         *
         * @param { AsyncCallback<Array<AVControlCommandType>> } callback - The triggered asyncCallback when (
         *     getValidCommands).
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        getValidCommands(callback: AsyncCallback<Array<AVControlCommandType>>): void;
        /**
         * Get commands supported by the current session
         *
         * @returns { Promise<Array<AVControlCommandType>> } array of AVControlCommandType promise
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getValidCommands(): Promise<Array<AVControlCommandType>>;
        /**
         * Get commands supported by the current session
         *
         * @returns {Array<AVControlCommandType> } array of AVControlCommandType
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        getValidCommandsSync(): Array<AVControlCommandType>;
        /**
         * Send control commands to this session
         *
         * @param { AVControlCommand } command - The command to be sent. See {@link AVControlCommand}
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @throws { BusinessError } 6600105 - Invalid session command.
         * @throws { BusinessError } 6600106 - The session is not activated.
         * @throws { BusinessError } 6600107 - Too many commands or events.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 10
         */
        sendControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void;
        /**
         * Send control commands to this session
         *
         * @param { AVControlCommand } command - The command to be sent. See {@link AVControlCommand}
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @throws { BusinessError } 6600105 - Invalid session command.
         * @throws { BusinessError } 6600106 - The session is not activated.
         * @throws { BusinessError } 6600107 - Too many commands or events.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        sendControlCommand(command: AVControlCommand): Promise<void>;
        /**
         * Send common commands to this session
         *
         * @param { string } command - The command name to be sent.
         * @param { object } args - The parameters of session event
         * @param { AsyncCallback<void> } callback - The asyncCallback triggered when the command is executed successfully.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @throws { BusinessError } 6600105 - Invalid session command.
         * @throws { BusinessError } 6600106 - The session is not activated.
         * @throws { BusinessError } 6600107 - Too many commands or events.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @since 10
         */
        sendCommonCommand(command: string, args: {
            [key: string]: Object;
        }, callback: AsyncCallback<void>): void;
        /**
         * Send common commands to this session
         *
         * @param { string } command - The command name to be sent.
         * @param { object } args - The parameters of session event
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @throws { BusinessError } 6600105 - Invalid session command.
         * @throws { BusinessError } 6600106 - The session is not activated.
         * @throws { BusinessError } 6600107 - Too many commands or events.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        sendCommonCommand(command: string, args: {
            [key: string]: Object;
        }): Promise<void>;
        /**
         * Get custom media packets provided by the corresponding session
         *
         * @param { AsyncCallback<{[key: string]: Object}> } callback - The triggered asyncCallback when (getExtras).
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @throws { BusinessError } 6600105 - Invalid session command.
         * @throws { BusinessError } 6600107 - Too many commands or events.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @since 10
         */
        getExtras(callback: AsyncCallback<{
            [key: string]: Object;
        }>): void;
        /**
         * Get custom media packets provided by the corresponding session
         *
         * @returns { Promise<{[key: string]: Object}> } the parameters of extras
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @throws { BusinessError } 6600105 - Invalid session command.
         * @throws { BusinessError } 6600107 - Too many commands or events.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        getExtras(): Promise<{
            [key: string]: Object;
        }>;
        /**
         * Get extra information for remote device, such as volume level, connected devices.
         *
         * @param { string } extraEvent - the event name to get
         * @returns { Promise<ExtraInfo> } the value returned for such event
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @throws { BusinessError } 6600105 - Invalid session command.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 18
         */
        getExtrasWithEvent(extraEvent: string): Promise<ExtraInfo>;
        /**
         * Query desktop lyric enabled state for this session.
         *
         * @returns { Promise<boolean> } return the enabled status
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @throws { BusinessError } 6600111 - The desktop lyrics feature is not supported.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        isDesktopLyricEnabled(): Promise<boolean>;
        /**
         * Register desktop lyric enable state change callback.
         *
         * @param { Callback<boolean> } callback - a callback to receive desktop lyric enable state.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        onDesktopLyricEnabled(callback: Callback<boolean>): void;
        /**
         * Unregister desktop lyric enable state change callback.
         *
         * @param { Callback<boolean> } [callback] - a callback to receive desktop lyric enable state.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        offDesktopLyricEnabled(callback?: Callback<boolean>): void;
        /**
         * Set desktop lyric visible state for this session.
         *
         * @param { boolean } visible - make desktop lyric window visible or not
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @throws { BusinessError } 6600110 - The desktop lyrics feature of this application is not enabled.
         * @throws { BusinessError } 6600111 - The desktop lyrics feature is not supported.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        setDesktopLyricVisible(visible: boolean): Promise<void>;
        /**
         * Query desktop lyric visible state for this session.
         *
         * @returns { Promise<boolean> } return desktop lyric visible state
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @throws { BusinessError } 6600110 - The desktop lyrics feature of this application is not enabled.
         * @throws { BusinessError } 6600111 - The desktop lyrics feature is not supported.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        isDesktopLyricVisible(): Promise<boolean>;
        /**
         * Register desktop lyric visible state change callback.
         *
         * @param { Callback<boolean> } callback - a callback to receive desktop lyric window visible state.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void;
        /**
         * Unregister desktop lyric visible state change callback.
         *
         * @param { Callback<boolean> } [callback] - a callback to receive desktop lyric window visible state.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void;
        /**
         * Set desktop lyric state such as lock state for this session.
         *
         * @param { DesktopLyricState } state - The desktop lyric state
         * @returns { Promise<void> } void promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @throws { BusinessError } 6600110 - The desktop lyrics feature of this application is not enabled.
         * @throws { BusinessError } 6600111 - The desktop lyrics feature is not supported.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        setDesktopLyricState(state: DesktopLyricState): Promise<void>;
        /**
         * Get desktop lyric state such as lock state for this session.
         *
         * @returns { Promise<DesktopLyricState> } void promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @throws { BusinessError } 6600110 - The desktop lyrics feature of this application is not enabled.
         * @throws { BusinessError } 6600111 - The desktop lyrics feature is not supported.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        getDesktopLyricState(): Promise<DesktopLyricState>;
        /**
         * Register desktop lyric state changed callback.
         *
         * @param { Callback<DesktopLyricState> } callback - a callback to receive desktop lyric state.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void;
        /**
         * Unregister desktop lyric state changed callback.
         *
         * @param { Callback<DesktopLyricState> } [callback] - a callback to receive desktop lyric state.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 23
         */
        offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void;
        /**
         * Get media control type that the can be displayed on the media center.
         *
         * @returns { Promise<Array<AVMediaCenterControlType>> } The control types that the app sets to be displayed
         *     on the media center. The default value is empty, indicating that the types of the customized
         *     display control is not set.
         * @param { Callback<DesktopLyricState> } callback - a callback to receive desktop lyric state.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        getMediaCenterControlType(): Promise<Array<AVMediaCenterControlType>>;
        /**
         * Register media center control type changed callback.
         *
         * @param { Callback<Array<AVMediaCenterControlType>> } callback - Callback to receive the changed control types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        onMediaCenterControlTypeChanged(callback: Callback<Array<AVMediaCenterControlType>>): void;
        /**
         * Unregister media center control type changed callback.
         *
         * @param { Callback<Array<AVMediaCenterControlType>> } [callback] - Callback to receive the changed control types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        offMediaCenterControlTypeChanged(callback?: Callback<Array<AVMediaCenterControlType>>): void;
        /**
         * Register metadata changed callback
         *
         * @param { 'metadataChange' } type
         * @param { Array<keyof AVMetadata> | 'all' } filter - The properties of {@link AVMetadata} that you cared about
         * @param { function } callback - The callback used to handle metadata changed event.
         *     The callback function provides the {@link AVMetadata} parameter.
         *     It only contains the properties set in the filter.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'metadataChange', filter: Array<keyof AVMetadata> | 'all', callback: (data: AVMetadata) => void);
        /**
         * Unregister metadata changed callback
         *
         * @param { 'metadataChange' } type
         * @param { function } callback - The callback used to handle metadata changed event.
         *     The callback function provides the {@link AVMetadata} parameter.
         *     It only contains the properties set in the filter.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'metadataChange', callback?: (data: AVMetadata) => void);
        /**
         * Register playback state changed callback
         *
         * @param { 'playbackStateChange' } type
         * @param { Array<keyof AVPlaybackState> | 'all' } filter - The properties of {@link AVPlaybackState}
         *     that you cared about
         * @param { function } callback - The callback used to handle playback state changed event.
         *     The callback function provides the {@link AVPlaybackState} parameter.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void);
        /**
         * Unregister playback state changed callback
         *
         * @param { 'playbackStateChange' } type
         * @param { function } callback - The callback used to handle playback state changed event.
         *     The callback function provides the {@link AVPlaybackState} parameter.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void);
        /**
         * Register call metadata changed callback
         *
         * @param { 'callMetadataChange' } type - 'callMetadataChange'
         * @param { Array<keyof CallMetadata> | 'all' } filter - The properties of {@link CallMetadata} that you cared about
         * @param { Callback<CallMetadata> } callback - The callback used to handle call metadata changed event.
         *     The callback function provides the {@link CallMetadata} parameter.
         *     It only contains the properties set in the filter.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'callMetadataChange', filter: Array<keyof CallMetadata> | 'all', callback: Callback<CallMetadata>): void;
        /**
         * Unregister call metadata changed callback
         *
         * @param { 'callMetadataChange' } type - 'callMetadataChange'
         * @param { Callback<CallMetadata> } callback - The callback used to handle call metadata changed event.
         *     The callback function provides the {@link CallMetadata} parameter.
         *     It only contains the properties set in the filter.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'callMetadataChange', callback?: Callback<CallMetadata>): void;
        /**
         * Register call state changed callback
         *
         * @param { 'callStateChange' } type - 'callStateChange'
         * @param { Array<keyof AVCallState> | 'all' } filter - The properties of {@link AVCallState} that you cared about
         * @param { Callback<AVCallState> } callback - The callback used to handle call state changed event.
         *     The callback function provides the {@link AVCallState} parameter.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'callStateChange', filter: Array<keyof AVCallState> | 'all', callback: Callback<AVCallState>): void;
        /**
         * Unregister playback state changed callback
         *
         * @param { 'callStateChange' } type - 'callStateChange'
         * @param { Callback<AVCallState> } callback - The callback used to handle call state changed event.
         *     The callback function provides the {@link AVCallState} parameter.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'callStateChange', callback?: Callback<AVCallState>): void;
        /**
         * Register current session destroyed callback
         *
         * @param { 'sessionDestroy' } type
         * @param { function } callback - The callback used to handle current session destroyed event.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'sessionDestroy', callback: () => void);
        /**
         * Unregister current session destroyed callback
         *
         * @param { 'sessionDestroy' } type - 'sessionDestroy'
         * @param { function } callback - The callback used to handle current session destroyed event.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'sessionDestroy', callback?: () => void);
        /**
         * Register the active state of this session changed callback
         *
         * @param { 'activeStateChange' } type - 'activeStateChange'
         * @param { function } callback - The callback used to handle the active state of this session changed event.
         *     The callback function provides the changed session state.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'activeStateChange', callback: (isActive: boolean) => void);
        /**
         * Unregister the active state of this session changed callback
         *
         * @param { 'activeStateChange' } type - 'activeStateChange'
         * @param { function } callback - The callback used to handle the active state of this session changed event.
         *     The callback function provides the changed session state.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'activeStateChange', callback?: (isActive: boolean) => void);
        /**
         * Register the valid commands of the session changed callback
         *
         * @param { 'validCommandChange' } type - 'validCommandChange'
         * @param { function } callback - The callback used to handle the changes.
         *     The callback function provides an array of AVControlCommandType.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'validCommandChange', callback: (commands: Array<AVControlCommandType>) => void);
        /**
         * Unregister the valid commands of the session changed callback
         *
         * @param { 'validCommandChange' } type - 'validCommandChange'
         * @param { function } callback - The callback used to handle the changes.
         *     The callback function provides an array of AVControlCommandType.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'validCommandChange', callback?: (commands: Array<AVControlCommandType>) => void);
        /**
         * Register session output device change callback
         *
         * @param { 'outputDeviceChange' } type - Registration Type 'outputDeviceChange'
         * @param { function } callback - Used to handle output device changed.
         *     The callback provide the new device info {@link OutputDeviceInfo} and related connection state {@link
         *     ConnectionState}.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600103 - The session controller does not exist
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void;
        /**
         * Unregister session output device change callback
         *
         * @param { 'outputDeviceChange' } type - Registration Type 'outputDeviceChange'
         * @param { function } callback - Used to handle output device changed.
         *     The callback provide the new device info {@link OutputDeviceInfo} and related connection state {@link
         *     ConnectionState}.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600103 - The session controller does not exist
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void;
        /**
         * Register session event callback
         *
         * @param { 'sessionEvent' } type - 'sessionEvent'
         * @param { function } callback - The callback used to handle session event changed event.
         *     The callback function provides the event string and key-value pair parameters.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'sessionEvent', callback: (sessionEvent: string, args: {
            [key: string]: Object;
        }) => void): void;
        /**
         * Unregister session event callback
         *
         * @param { 'sessionEvent' } type - 'sessionEvent'
         * @param { function } callback - Used to cancel a specific listener
         *     The callback function provides the event string and key-value pair parameters.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'sessionEvent', callback?: (sessionEvent: string, args: {
            [key: string]: Object;
        }) => void): void;
        /**
         * Register session playlist change callback
         *
         * @param { 'queueItemsChange' } type - Registration Type 'queueItemsChange'
         * @param { function } callback - Used to handle playlist changed.
         *     The callback provides the new array of AVQueueItem {@link AVQueueItem}
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'queueItemsChange', callback: (items: Array<AVQueueItem>) => void): void;
        /**
         * Unregister session playlist change callback
         *
         * @param { 'queueItemsChange' } type - Registration Type 'queueItemsChange'
         * @param { function } callback - Used to handle playlist changed.
         *     The callback provides the new array of AVQueueItem {@link AVQueueItem}
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'queueItemsChange', callback?: (items: Array<AVQueueItem>) => void): void;
        /**
         * Register the name of session playlist change callback
         *
         * @param { 'queueTitleChange' } type - Registration Type 'queueTitleChange'
         * @param { function } callback - Used to handle name of playlist changed.
         *     The callback provides the new name.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'queueTitleChange', callback: (title: string) => void): void;
        /**
         * Unregister the name of session playlist change callback
         *
         * @param { 'queueTitleChange' } type - Registration Type 'queueTitleChange'
         * @param { function } callback - Used to handle name of playlist changed.
         *     The callback provides the new name.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'queueTitleChange', callback?: (title: string) => void): void;
        /**
         * Register the custom media packets change callback
         *
         * @param { 'extrasChange' } type - Registration Type 'extrasChange'
         * @param { function } callback - Used to handle custom media packets changed.
         *     The callback provides the new media packets.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        on(type: 'extrasChange', callback: (extras: {
            [key: string]: Object;
        }) => void): void;
        /**
         * Unregister the custom media packets change callback
         *
         * @param { 'extrasChange' } type - Registration Type 'extrasChange'
         * @param { function } callback - Used to handle custom media packets changed.
         *     The callback provides the new media packets.
         * @throws { BusinessError } 401 - parameter check failed. 1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6600101 - Session service exception.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @FaAndStageModel
         * @atomicservice [since 12]
         * @since 10
         */
        off(type: 'extrasChange', callback?: (extras: {
            [key: string]: Object;
        }) => void): void;
        /**
         * Send custom data to this avsession.
         *
         * @param { Record<string, Object> } data - The custom data populated by application.
         * @returns { Promise<void> } void result promise when executed successfully
         * @throws { BusinessError } 6600101 - Session service exception.
         *     You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it.
         * @throws { BusinessError } 6600102 - The session does not exist.
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        sendCustomData(data: Record<string, Object>): Promise<void>;
        /**
         * Register listener for custom data.
         *
         * @param { 'customDataChange' } type - Type of the 'customDataChange' to listen for.
         * @param { Callback<Record<string, Object>> } callback - Callback used to retrieve custom data.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void;
        /**
         * Unregister listener for custom data.
         *
         * @param { 'customDataChange' } type - Type of the 'customDataChange' to listen for.
         * @param { Callback<Record<string, Object>> } [callback] - Callback used to retrieve custom data.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 20
         */
        off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void;
        /**
         * Register listener for supported play speeds.
         *
         * @param { Callback<Array<number>> } callback - Callback used to retrieve supported play speeds.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        onSupportedPlaySpeedsChange(callback: Callback<Array<number>>): void;
        /**
         * Unregister listener for supported play speeds.
         *
         * @param { Callback<Array<number>> } [callback] - Callback used to retrieve supported play speeds.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        offSupportedPlaySpeedsChange(callback?: Callback<Array<number>>): void;
        /**
         * Register listener for supported loop modes.
         *
         * @param { Callback<Array<LoopMode>> } callback - Callback used to retrieve supported loop modes.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        onSupportedLoopModesChange(callback: Callback<Array<LoopMode>>): void;
        /**
         * Unregister listener for supported loop modes.
         *
         * @param { Callback<Array<number>> } [callback] - Callback used to retrieve supported loop modes.
         * @throws { BusinessError } 6600101 - Session service exception
         * @throws { BusinessError } 6600103 - The session controller does not exist.
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        offSupportedLoopModesChange(callback?: Callback<Array<LoopMode>>): void;
    }
    /**
     * The type of control command.
     *
     * @unionmember { 'play' } Play the current media.
     * @unionmember { 'pause' } Pause the current media.
     * @unionmember { 'stop' } Stop the current media.
     * @unionmember { 'playNext' } Play the next media in the queue.
     * @unionmember { 'playPrevious' } Play the previous media in the queue.
     * @unionmember { 'fastForward' } Fast forward the current media.
     * @unionmember { 'rewind' } Rewind the current media.
     * @unionmember { 'seek' } Seek to a specific position in the media.
     * @unionmember { 'setSpeed' } Set the playback speed.
     * @unionmember { 'setLoopMode' } Set the loop mode for the media.
     * @unionmember { 'toggleFavorite' } Toggle the favorite status of the current media.
     * @unionmember { 'playFromAssetId' } Play media specified by an asset ID. [since 11]
     * @unionmember { 'playWithAssetId' } Play media with an asset ID (dynamic support). [since 20]
     * @unionmember { 'answer' } Answer an incoming call. [since 11]
     * @unionmember { 'hangUp' } Hang up the current call. [since 11]
     * @unionmember { 'toggleCallMute' } Toggle the mute status of the call. [since 11]
     * @unionmember { 'setTargetLoopMode' } Set the target loop mode. [since 18]
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    type AVControlCommandType = 'play' | 'pause' | 'stop' | 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' | 'seek' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite' | 'playFromAssetId' | 'playWithAssetId' | 'answer' | 'hangUp' | 'toggleCallMute' | 'setTargetLoopMode';
    /**
     * The type of media center control command, which can be used to determine the button displayed on the media center.
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    type AVMediaCenterControlType = 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite';
    /**
     * The definition of command to be sent to the session
     *
     * @interface AVControlCommand [since 10 - 11]
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    interface AVControlCommand {
        /**
         * The command value {@link AVControlCommandType}
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        command: AVControlCommandType;
        /**
         * parameter of the command. Whether this command requires parameters, see {@link AVSessionCommand}
         * seek command requires a number parameter
         * setSpeed command requires a number parameter
         * setLoopMode command requires a {@link LoopMode} parameter.
         * toggleFavorite command requires assetId {@link AVMetadata.assetId} parameter
         * other commands need no parameter
         *
         * @type { ?(LoopMode | string | number) } [since 10 - 11]
         * @type { ?(LoopMode | string | number) } [since 12]
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        parameter?: LoopMode | string | number;
        /**
         * The command value {@link CommandInfo}
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        commandInfo?: CommandInfo;
    }
    /**
     * The definition of command information to be sent to the session
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @since 22
     */
    interface CommandInfo {
        /**
         * Caller bundle name.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        callerBundleName?: string;
        /**
         * Caller module name.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        callerModuleName?: string;
        /**
         * Caller device id.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        callerDeviceId?: string;
        /**
         * Caller type.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        callerType?: CallerType;
    }
    /**
     * Enumerates CallerType including caller source type.
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @since 22
     */
    enum CallerType {
        /**
         * The control command comes from cast service.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        TYPE_CAST = 'cast',
        /**
         * The control command comes from bluetooth.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        TYPE_BLUETOOTH = 'bluetooth',
        /**
         * The control command comes from nearlink device.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @since 22
         */
        TYPE_NEARLINK = 'nearlink',
        /**
         * The control command comes from an application.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @since 22
         */
        TYPE_APP = 'app'
    }
    /**
     * Enumerates ErrorCode types, returns in BusinessError.code.
     *
     * @syscap SystemCapability.Multimedia.AVSession.Core
     * @atomicservice [since 12]
     * @since 10
     */
    enum AVSessionErrorCode {
        /**
         * Session service exception.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        ERR_CODE_SERVICE_EXCEPTION = 6600101,
        /**
         * The session does not exist
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        ERR_CODE_SESSION_NOT_EXIST = 6600102,
        /**
         * The session controller does not exist.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        ERR_CODE_CONTROLLER_NOT_EXIST = 6600103,
        /**
         * The remote session connection failed.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        ERR_CODE_REMOTE_CONNECTION_ERR = 6600104,
        /**
         * Invalid session command.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        ERR_CODE_COMMAND_INVALID = 6600105,
        /**
         * The session is not activated.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        ERR_CODE_SESSION_INACTIVE = 6600106,
        /**
         * Too many commands or events.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        ERR_CODE_MESSAGE_OVERLOAD = 6600107,
        /**
         * Device connecting failed.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        ERR_CODE_DEVICE_CONNECTION_FAILED = 6600108,
        /**
         * The remote connection is not established.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @atomicservice [since 12]
         * @since 10
         */
        ERR_CODE_REMOTE_CONNECTION_NOT_EXIST = 6600109,
        /**
         * The desktop lyrics feature of this application is not enabled.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        ERR_CODE_DESKTOP_LYRIC_NOT_ENABLED = 6600110,
        /**
         * The desktop lyrics feature is not supported.
         *
         * @syscap SystemCapability.Multimedia.AVSession.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        ERR_CODE_DESKTOP_LYRIC_NOT_SUPPORTED = 6600111,
        /**
         * The error code for cast control is unspecified.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_UNSPECIFIED = 6611000,
        /**
         * An unspecified error occurs in the remote player.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_REMOTE_ERROR = 6611001,
        /**
         * The playback position falls behind the live window.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_BEHIND_LIVE_WINDOW = 6611002,
        /**
         * The process of cast control times out.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_TIMEOUT = 6611003,
        /**
         * The runtime check failed.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_RUNTIME_CHECK_FAILED = 6611004,
        /**
         * Cross-device data transmission is locked.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_PLAYER_NOT_WORKING = 6611100,
        /**
         * The specified seek mode is not supported.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_SEEK_MODE_UNSUPPORTED = 6611101,
        /**
         * The position to seek to is out of the range of the media asset or the specified seek mode is not supported.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_ILLEGAL_SEEK_TARGET = 6611102,
        /**
         * The specified playback mode is not supported.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_PLAY_MODE_UNSUPPORTED = 6611103,
        /**
         * The specified playback speed is not supported.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_PLAY_SPEED_UNSUPPORTED = 6611104,
        /**
         * The action failed because either the media source device or the media sink device has been revoked.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DEVICE_MISSING = 6611105,
        /**
         * The parameter is invalid, for example, the url is illegal to play.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_INVALID_PARAM = 6611106,
        /**
         * Allocation of memory failed.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_NO_MEMORY = 6611107,
        /**
         * Operation is not allowed.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_OPERATION_NOT_ALLOWED = 6611108,
        /**
         * An unspecified input/output error occurs.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_UNSPECIFIED = 6612000,
        /**
         * Network connection failure.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_NETWORK_CONNECTION_FAILED = 6612001,
        /**
         * Network timeout.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_NETWORK_CONNECTION_TIMEOUT = 6612002,
        /**
         * Invalid "Content-Type" HTTP header.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_INVALID_HTTP_CONTENT_TYPE = 6612003,
        /**
         * The HTTP server returns an unexpected HTTP response status code.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_BAD_HTTP_STATUS = 6612004,
        /**
         * The file does not exist.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_FILE_NOT_FOUND = 6612005,
        /**
         * No permission is granted to perform the IO operation.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_NO_PERMISSION = 6612006,
        /**
         * Access to cleartext HTTP traffic is not allowed by the app's network security configuration.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_CLEARTEXT_NOT_PERMITTED = 6612007,
        /**
         * Reading data out of the data bound.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_READ_POSITION_OUT_OF_RANGE = 6612008,
        /**
         * The media does not contain any contents that can be played.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_NO_CONTENTS = 6612100,
        /**
         * The media cannot be read, for example, because of dust or scratches.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_READ_ERROR = 6612101,
        /**
         * This resource is already in use.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_CONTENT_BUSY = 6612102,
        /**
         * The content using the validity interval has expired.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_CONTENT_EXPIRED = 6612103,
        /**
         * Using the requested content to play is not allowed.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_USE_FORBIDDEN = 6612104,
        /**
         * The use of the allowed content cannot be verified.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_NOT_VERIFIED = 6612105,
        /**
         * The number of times this content has been used as requested has reached the maximum allowed number of uses.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_EXHAUSTED_ALLOWED_USES = 6612106,
        /**
         * An error occurs when sending packet from source device to sink device.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_IO_NETWORK_PACKET_SENDING_FAILED = 6612107,
        /**
         * Unspecified error related to content parsing.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_PARSING_UNSPECIFIED = 6613000,
        /**
         * Parsing error associated with media container format bit streams.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_PARSING_CONTAINER_MALFORMED = 6613001,
        /**
         * Parsing error associated with the media manifest.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_PARSING_MANIFEST_MALFORMED = 6613002,
        /**
         * An error occurs when attempting to extract a file with an unsupported media container format
         * or an unsupported media container feature.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_PARSING_CONTAINER_UNSUPPORTED = 6613003,
        /**
         * Unsupported feature in the media manifest.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_PARSING_MANIFEST_UNSUPPORTED = 6613004,
        /**
         * Unspecified decoding error.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DECODING_UNSPECIFIED = 6614000,
        /**
         * Decoder initialization failed.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DECODING_INIT_FAILED = 6614001,
        /**
         * Decoder query failed.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DECODING_QUERY_FAILED = 6614002,
        /**
         * Decoding the media samples failed.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DECODING_FAILED = 6614003,
        /**
         * The format of the content to decode exceeds the capabilities of the device.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DECODING_FORMAT_EXCEEDS_CAPABILITIES = 6614004,
        /**
         * The format of the content to decode is not supported.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DECODING_FORMAT_UNSUPPORTED = 6614005,
        /**
         * Unspecified errors related to the audio renderer.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_AUDIO_RENDERER_UNSPECIFIED = 6615000,
        /**
         * Initializing the audio renderer failed.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_AUDIO_RENDERER_INIT_FAILED = 6615001,
        /**
         * The audio renderer fails to write data.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_AUDIO_RENDERER_WRITE_FAILED = 6615002,
        /**
         * Unspecified error related to DRM.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DRM_UNSPECIFIED = 6616000,
        /**
         * The chosen DRM protection scheme is not supported by the device.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DRM_SCHEME_UNSUPPORTED = 6616001,
        /**
         * Device provisioning failed.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DRM_PROVISIONING_FAILED = 6616002,
        /**
         * The DRM-protected content to play is incompatible.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DRM_CONTENT_ERROR = 6616003,
        /**
         * Failed to obtain a license.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DRM_LICENSE_ACQUISITION_FAILED = 6616004,
        /**
         * The operation is disallowed by the license policy.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DRM_DISALLOWED_OPERATION = 6616005,
        /**
         * An error occurs in the DRM system.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DRM_SYSTEM_ERROR = 6616006,
        /**
         * The device has revoked DRM privileges.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DRM_DEVICE_REVOKED = 6616007,
        /**
         * The DRM license being loaded into the open DRM session has expired.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DRM_LICENSE_EXPIRED = 6616008,
        /**
         * An error occurs when the DRM processes the key response.
         *
         * @syscap SystemCapability.Multimedia.AVSession.AVCast
         * @atomicservice
         * @since 13
         */
        ERR_CODE_CAST_CONTROL_DRM_PROVIDE_KEY_RESPONSE_ERROR = 6616100
    }
}
export default avSession;

```
