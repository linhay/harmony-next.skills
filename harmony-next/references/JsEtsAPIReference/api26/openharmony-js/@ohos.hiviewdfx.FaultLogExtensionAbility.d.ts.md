# @ohos.hiviewdfx.FaultLogExtensionAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
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
 * @file Delayed Fault Notification
 * @kit PerformanceAnalysisKit
 */
import type FaultLogExtensionContext from './@ohos.hiviewdfx.FaultLogExtensionContext';
/**
 * # Appendix
 *
 * The following table lists the APIs that cannot be called by this module.
 * | Kit| Module|
 * | ------- | ------- |
 * | AVSessionKit | [@ohos.multimedia.avsession (AVSession Management)]{@link @ohos.multimedia.avsession:avSession}|
 * | AbilityKit | [@ohos.UIAbilityContext]{@link ./application/UIAbilityContext:UIAbilityContext} |
 * | ArkUI | [@ohos.window (Window)]{@link @ohos.window}|
 * | AudioKit | [@ohos.multimedia.audio (Audio Management)]{@link @ohos.multimedia.audio:audio}|
 * | BackgroundTasksKit |
 * [@ohos.backgroundTaskManager (Background Task Management)]{@link @ohos.backgroundTaskManager:backgroundTaskManager}|
 * | BackgroundTasksKit | [@ohos.reminderAgent (reminderAgent)]{@link @ohos.reminderAgent:reminderAgent}|
 * | BackgroundTasksKit |
 * [@ohos.reminderAgentManager (Agent-Powered Reminders)]{@link @ohos.reminderAgentManager:reminderAgentManager}|
 * | BackgroundTasksKit |
 * [@ohos.resourceschedule.backgroundTaskManager (Background Task Management)]{@link @ohos.resourceschedule.backgroundTaskManager:backgroundTaskManager}
 * |
 * | BasicServicesKit | [@ohos.power (System Power Management)]{@link @ohos.power:power}|
 * | BasicServicesKit | [@ohos.wallpaper (Wallpaper)]{@link @ohos.wallpaper:wallpaper}|
 * | CameraKit | [@ohos.multimedia.camera (Camera Management)]{@link @ohos.multimedia.camera:camera}|
 * | CameraKit | [@ohos.multimedia.cameraPicker (Camera Picker)]{@link @ohos.multimedia.cameraPicker:cameraPicker}|
 * | ConnectivityKit | [@ohos.wifiManager (WLAN)]{@link @ohos.wifiManager:wifiManager} |
 * | ConnectivityKit | [@ohos.wifiManagerExt (WLAN Extension)]{@link @ohos.wifiManagerExt:wifiManagerExt}|
 * | ConnectivityKit | [@ohos.wifiext (WLAN Extension)]{@link @ohos.wifiext:wifiext}|
 * | IMEKit | [@ohos.inputMethod (Input Method Framework)]{@link @ohos.inputMethod:inputMethod}|
 * | MediaLibraryKit | [@ohos.multimedia.movingphotoview (MovingPhotoView)]{@link @ohos.multimedia.movingphotoview}|
 * | NotificationKit | [@ohos.notification (Notification)]{@link @ohos.notification:notification}|
 * | NotificationKit |
 * [@ohos.notificationManager (NotificationManager)]{@link @ohos.notificationManager:notificationManager}|
 * | <!--DelRow--> NotificationKit |
 * [@ohos.notificationSubscribe (NotificationSubscribe)]{@link @ohos.notificationSubscribe:notificationSubscribe}|
 * | SensorServiceKit | [@ohos.vibrator (Vibrator)]{@link @ohos.vibrator:vibrator}|
 * | TelephonyKit | [@ohos.telephony.call (Call)]{@link @ohos.telephony.call:call}|
 * | TelephonyKit | [@ohos.telephony.sim (SIM Management)]{@link @ohos.telephony.sim:sim}|
 * | TelephonyKit | [@ohos.telephony.sms (SMS)]{@link @ohos.telephony.sms:sms}|
 * | <!--DelRow--> UserAuthenticationKit |
 * [@ohos.userIAM.faceAuth (Facial Authentication)]{@link @ohos.userIAM.faceAuth:faceAuth}|
 * | UserAuthenticationKit | [@ohos.userIAM.userAuth (User Authentication)]{@link @ohos.userIAM.userAuth:userAuth}|
 */
/**
 * This module implements the delayed fault notification feature.
 *
 * When the crash and freeze events are subscribed by [HiAppEvent]{@link @ohos.hiviewdfx.hiAppEvent:hiAppEvent}, the
 * previous event can be received only after the application restarts. If the application fails to start or remains
 * unresponsive for a long time, the fault may not be reported in time.
 *
 * > **NOTE**
 * >
 * > - The APIs of this module can be used only in the stage model.
 * >
 * > - Exceptions may occur if some APIs are called by this module. For details, see
 * > [Appendix](docroot://reference/apis-performance-analysis-kit/js-apis-hiviewdfx-FaultLogExtensionAbility.md#appendix)
 * > .
 *
 * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
 * @stagemodelonly
 * @since 21
 */
declare class FaultLogExtensionAbility {
    /**
     * Context of the FaultLogExtensionAbility. This context is inherited from
     * [ExtensionContext]{@link ./application/ExtensionContext:ExtensionContext}.
     *
     * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
     * @stagemodelonly
     * @since 21
     */
    context: FaultLogExtensionContext;
    /**
     * Called to subscribe to and process fault events when the system service notifies the FaultLogExtensionAbility to
     * process faults.
     *
     * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
     * @stagemodelonly
     * @since 21
     */
    onFaultReportReady(): void;
    /**
     * Called to perform the initialization operation when the system service completes the connection. This API can be
     * overridden selectively.
     *
     * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
     * @stagemodelonly
     * @since 21
     */
    onConnect(): void;
    /**
     * Called to release resources and clear the running status when the system service completes the disconnection. This
     * API can be overridden selectively.
     *
     * @syscap SystemCapability.HiviewDFX.Hiview.FaultLogger
     * @stagemodelonly
     * @since 21
     */
    onDisconnect(): void;
}
export default FaultLogExtensionAbility;

```
