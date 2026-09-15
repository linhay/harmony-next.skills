# @ohos.vibrator.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2025 Huawei Device Co., Ltd.
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
 * @kit SensorServiceKit
 */
import { AsyncCallback, Callback } from './@ohos.base';
/**
 * The **vibrator** module allows precise control over the vibration of device vibrators. With the APIs provided by this
 * module, you can start vibration in various modes such as specified duration, preset effect, and custom effect and
 * stop any or all of them.
 *
 * @syscap SystemCapability.Sensors.MiscDevice
 * @crossplatform [since 22]
 * @atomicservice [since 11]
 * @since 8
 */
declare namespace vibrator {
    /**
     * Triggers vibration based on a specified duration. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.VIBRATE
     * @param { number } duration - Vibration duration, in ms. The value range is (0,1800000]. The maximum vibration
     *     duration varies with devices due to different component protection design specifications of drivers provided by
     *     different vendors. It is recommended that a single vibration duration be less than or equal to 10s to maximize
     *     user experience.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the vibration starts, **err** is
     *     **undefined**; otherwise, **err** is an error object.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @since 8
     * @deprecated since 9
     * @useinstead vibrator.startVibration(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback<void>)
     */
    function vibrate(duration: number, callback?: AsyncCallback<void>): void;
    /**
     * Triggers vibration based on a specified duration. This API uses a promise to return the result.
     *
     * @permission ohos.permission.VIBRATE
     * @param { number } duration - Vibration duration, in ms. The value range is (0,1800000]. The maximum vibration
     *     duration varies with devices due to different component protection design specifications of drivers provided by
     *     different vendors. It is recommended that a single vibration duration be less than or equal to 10s to maximize
     *     user experience.
     * @returns { Promise<void> } Promise that returns the result.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @since 8
     * @deprecated since 9
     * @useinstead vibrator.startVibration(effect: VibrateEffect, attribute: VibrateAttribute)
     */
    function vibrate(duration: number): Promise<void>;
    /**
     * Triggers vibration based on a specified effect. This API uses a promise to return the result.
     *
     * @permission ohos.permission.VIBRATE
     * @param { EffectId } effectId - Effect ID. The value is a string of a maximum of 64 characters. If the length
     *     exceeds 64 characters, the first 64 characters are used. You are advised to check whether the effect ID is
     *     supported.
     * @returns { Promise<void> } Promise that returns the result.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @since 8
     * @deprecated since 9
     * @useinstead vibrator.startVibration(effect: VibrateEffect, attribute: VibrateAttribute)
     */
    function vibrate(effectId: EffectId): Promise<void>;
    /**
     * Triggers vibration based on a specified effect. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.VIBRATE
     * @param { EffectId } effectId - Effect ID. The value is a string of a maximum of 64 characters. If the length
     *     exceeds 64 characters, the first 64 characters are used. You are advised to check whether the effect ID is
     *     supported.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the vibration starts, **err** is
     *     **undefined**; otherwise, **err** is an error object.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @since 8
     * @deprecated since 9
     * @useinstead vibrator.startVibration(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback<void>)
     */
    function vibrate(effectId: EffectId, callback?: AsyncCallback<void>): void;
    /**
     * Starts vibration based on a specified effect and attribute. This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.VIBRATE
     * @param { VibrateEffect } effect - Vibration effect. The following options are supported:<br>1.
     *     [VibratePreset]{@link vibrator.VibratePreset}: triggers vibration according to preset vibration effects. This
     *     mode is suitable for short vibration scenarios in interactive feedback (such as tapping, long-pressing, sliding
     *     , dragging, etc.). This API is recommended to maintain consistency with the system's overall vibration feedback
     *     experience.<br>2. [VibrateFromFile]{@link vibrator.VibrateFromFile}: triggers vibration according to custom
     *     vibration configuration file. This mode is suitable for interactive feedback in complex scenarios requiring
     *     precise vibration patterns (such as realistic effects triggered by emoji packs, or feedback for in-game actions
     *     /mechanics).<br>3. [VibrateTime]{@link vibrator.VibrateTime}: triggers vibration of the specified duration,
     *     providing basic control over the start and stop of vibration. This mode does not support customization of
     *     vibration intensity, frequency, or other parameters. As a result, the vibration adjustment is relatively coarse
     *     and not suitable for delivering a refined experience.<br>4.
     *     [VibrateFromPattern<sup>18+</sup>]{@link vibrator.VibrateFromPattern}: starts vibration according to a custom
     *     vibration pattern. The usage scenario is the same as **VibrateFromFile**. **VibrateFromFile** utilizes
     *     predefined effects in a custom configuration file, passing specific vibration events to the API via file
     *     descriptors. By contrast, **VibrateFromPattern** enables more flexible vibration event combinations, delivering
     *     them to the API as a vibration event array.<br>
     * @param { VibrateAttribute } attribute - Vibration attribute.
     * @param { AsyncCallback<void> } callback - Callback used to return the operation result. If the operation is
     *     successful, **err** is **undefined**; otherwise, **err** is an error object, which contains the error code and
     *     error information.
     * @throws { BusinessError } 201 - Permission denied
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported
     * @throws { BusinessError } 14600101 - Device operation failed
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    function startVibration(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback<void>): void;
    /**
     * Starts vibration based on a specified effect and attribute. This API uses a promise to return the result.
     *
     * @permission ohos.permission.VIBRATE
     * @param { VibrateEffect } effect - Vibration effect. The following options are supported:<br>1.
     *     [VibrateTime]{@link vibrator.VibrateTime}: triggers vibration according to preset vibration effects. This mode
     *     is suitable for short vibration scenarios in interactive feedback (such as tapping, long-pressing, sliding,
     *     dragging, etc.). This API is recommended to maintain consistency with the system's overall vibration feedback
     *     experience.<br>2. [VibratePreset]{@link vibrator.VibratePreset}: triggers vibration according to custom
     *     vibration configuration file. This mode is suitable for interactive feedback in complex scenarios requiring
     *     precise vibration patterns (such as realistic effects triggered by emoji packs, or feedback for in-game actions
     *     /mechanics).<br>3. [VibrateFromFile]{@link vibrator.VibrateFromFile}: triggers vibration of the specified
     *     duration, providing basic control over the start and stop of vibration. This mode does not support
     *     customization of vibration intensity, frequency, or other parameters. As a result, the vibration adjustment is
     *     relatively coarse and not suitable for delivering a refined experience.<br>4.
     *     [VibrateFromPattern<sup>18+</sup>]{@link vibrator.VibrateFromPattern}: starts vibration according to a custom
     *     vibration pattern. The usage scenario is the same as **VibrateFromFile**. **VibrateFromFile** utilizes
     *     predefined effects in a custom configuration file, passing specific vibration events to the API via file
     *     descriptors. By contrast, **VibrateFromPattern** enables more flexible vibration event combinations, delivering
     *     them to the API as a vibration event array.
     * @param { VibrateAttribute } attribute - Vibration attribute.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 14600101 - Device operation failed.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    function startVibration(effect: VibrateEffect, attribute: VibrateAttribute): Promise<void>;
    /**
     * Stops vibration in the specified mode. This API uses a promise to return the result.
     *
     * @permission ohos.permission.VIBRATE
     * @param { VibratorStopMode } stopMode - Vibration stop mode:<br>- **VIBRATOR_STOP_MODE_TIME**: used to stop
     *     vibration of the specified duration.<br>- **VIBRATOR_STOP_MODE_PRESET**: used to stop vibration of the preset
     *     effect.<br>To stop custom vibration, use [vibrator.stopVibration<sup>10+</sup>]{@link vibrator.stopVibration()}
     *     .
     * @returns { Promise<void> } Promise that returns the result.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 9
     */
    function stopVibration(stopMode: VibratorStopMode): Promise<void>;
    /**
     * Stops vibration in the specified mode. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.VIBRATE
     * @param { VibratorStopMode } stopMode - Mode to stop the vibration. The options are as follows:<br>-
     *     **VIBRATOR_STOP_MODE_TIME**: used to stop vibration of the specified duration.<br>-
     *     **VIBRATOR_STOP_MODE_PRESET**: used to stop vibration of the preset effect.<br>To stop custom vibration, use
     *     [vibrator.stopVibration<sup>10+</sup>]{@link vibrator.stopVibration(callback: AsyncCallback<void>)}.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the vibration stops, **err** is
     *     **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 9
     */
    function stopVibration(stopMode: VibratorStopMode, callback: AsyncCallback<void>): void;
    /**
     * Stops vibration in all modes. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.VIBRATE
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the vibration stops, **err** is
     *     **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 10
     */
    function stopVibration(callback: AsyncCallback<void>): void;
    /**
     * Stops vibration in all modes. This API uses a promise to return the result.
     *
     * @permission ohos.permission.VIBRATE
     * @returns { Promise<void> } Promise that returns the result.
     * @throws { BusinessError } 201 - Permission denied.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 10
     */
    function stopVibration(): Promise<void>;
    /**
     * Stops any form of motor vibration.
     *
     * @permission ohos.permission.VIBRATE
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 14600101 - Device operation failed.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @atomicservice
     * @since 12
     */
    function stopVibrationSync(): void;
    /**
     * Stops vibration based on the specified vibrator parameters. If no parameters are passed, this API stops all
     * vibrators of the local device by default. This API uses a promise to return the result.
     *
     * @permission ohos.permission.VIBRATE
     * @param { VibratorInfoParam } [param] - Vibrator parameters, such as the specified device and vibrator. If this
     *     parameter is left unspecified, this API applies to all vibrators of the local device by default.
     * @returns { Promise<void> } Promise that returns the result.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 14600101 - Device operation failed.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 19
     */
    function stopVibration(param?: VibratorInfoParam): Promise<void>;
    /**
     * Checks whether an effect ID is supported. This API uses an asynchronous callback to return the result.
     *
     * @param { string } effectId - Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds
     *     64 characters, the first 64 characters are used.
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** means that the
     *     effect ID is supported, and the value **false** means the opposite.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 10
     */
    function isSupportEffect(effectId: string, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether an effect ID is supported. This API uses a promise to return the result.
     *
     * @param { string } effectId - Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds
     *     64 characters, the first 64 characters are used.
     * @returns { Promise<boolean> } Promise that returns the result. The value **true** means that the effect ID is
     *     supported, and the value **false** means the opposite.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 10
     */
    function isSupportEffect(effectId: string): Promise<boolean>;
    /**
     * Checks whether the preset vibration effect is supported.
     *
     * @param { string } effectId - Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds
     *     64 characters, the first 64 characters are used.
     * @returns { boolean } Returned object. The value **true** means that the effect ID is supported, and the value
     *     **false** means the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14600101 - Device operation failed.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 12
     */
    function isSupportEffectSync(effectId: string): boolean;
    /**
     * Obtains the preset vibration effect based on the device ID and vibrator ID to determine whether the preset
     * vibration effect is supported.
     *
     * @param { string } effectId - Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds
     *     64 characters, the first 64 characters are used.
     * @param { VibratorInfoParam } [param] - Device ID and vibrator ID. If this parameter is left unspecified, this API
     *     applies to the local device by default.
     * @returns { EffectInfo } Whether the preset vibration effect is supported.
     * @throws { BusinessError } 14600101 - Device operation failed.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 19
     */
    function getEffectInfoSync(effectId: string, param?: VibratorInfoParam): EffectInfo;
    /**
     * Defines the preset effect.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 19
     */
    interface EffectInfo {
        /**
         * Whether the preset effect is supported. The value **true** indicates that the preset effect is supported, and the
         * value **false** indicates the opposite.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 19
         */
        isEffectSupported: boolean;
    }
    /**
     * Stops vibration in the specified mode. This API uses a promise to return the result.
     *
     * @permission ohos.permission.VIBRATE
     * @param { VibratorStopMode } stopMode - Mode to stop the vibration.
     * @returns { Promise<void> } Promise that returns the result.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @since 8
     * @deprecated since 9
     * @useinstead vibrator.stopVibration(stopMode: VibratorStopMode)
     */
    function stop(stopMode: VibratorStopMode): Promise<void>;
    /**
     * Stops vibration in the specified mode. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.VIBRATE
     * @param { VibratorStopMode } stopMode - Mode to stop the vibration.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the vibration stops, **err** is
     *     **undefined**; otherwise, **err** is an error object.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @since 8
     * @deprecated since 9
     * @useinstead vibrator.stopVibration(stopMode: VibratorStopMode, callback: AsyncCallback<void>)
     */
    function stop(stopMode: VibratorStopMode, callback?: AsyncCallback<void>): void;
    /**
     * Checks whether HD vibration is supported.
     *
     * @returns { boolean } Boolean value indicating whether HD vibration is supported. The value **true** indicates that
     *     HD vibration is supported, and the value **false** indicates the opposite.
     * @throws { BusinessError } 14600101 - Device operation failed.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 12
     */
    function isHdHapticSupported(): boolean;
    /**
     * Enumerates the preset vibration effect IDs. This parameter is needed when you call
     * [vibrator.startVibration9+]{@link vibrator.startVibration(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback<void>)}
     * or [vibrator.stopVibration9+]{@link vibrator.stopVibration(stopMode: VibratorStopMode)} to deliver the vibration
     * effect specified by [VibratePreset]{@link vibrator.VibratePreset}. This parameter supports a variety of values,
     * such as **haptic.clock.timer**. [HapticFeedback<sup>12+</sup>]{@link vibrator.HapticFeedback} provides several
     * frequently used **EffectId** values.
     *
     * > **NOTE**
     * >
     * > Preset effects vary according to devices. You are advised to call
     * > [vibrator.isSupportEffect]{@link vibrator.isSupportEffect(effectId: string)}<sup>10+</sup> to check whether the
     * > device supports the preset effect before use.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 8
     */
    enum EffectId {
        /**
         * Vibration effect when a user adjusts the timer.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 8
         */
        EFFECT_CLOCK_TIMER = 'haptic.clock.timer'
    }
    /**
     * Defines the vibration effect. The frequency of the same vibration effect may vary depending on the vibrator, but
     * the frequency trend remains consistent. These vibration effects correspond to the specific **EffectId** values. For
     * details, see the sample code that demonstrates how to use
     * [vibrator.startVibration9+]{@link vibrator.startVibration(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback<void>)}
     * or [vibrator.stopVibration9+]{@link vibrator.stopVibration(stopMode: VibratorStopMode)} to deliver the vibration
     * effect defined by [VibratePreset]{@link vibrator.VibratePreset}.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 12
     */
    enum HapticFeedback {
        /**
         * Soft vibration, low frequency.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 12
         */
        EFFECT_SOFT = 'haptic.effect.soft',
        /**
         * Hard vibration, medium frequency.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 12
         */
        EFFECT_HARD = 'haptic.effect.hard',
        /**
         * Sharp vibration, high frequency.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 12
         */
        EFFECT_SHARP = 'haptic.effect.sharp',
        /**
         * Vibration for a success notification.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        EFFECT_NOTICE_SUCCESS = 'haptic.notice.success',
        /**
         * Vibration for a failure notification.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        EFFECT_NOTICE_FAILURE = 'haptic.notice.fail',
        /**
         * Vibration for an alert.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        EFFECT_NOTICE_WARNING = 'haptic.notice.warning'
    }
    /**
     * Enumerates vibration stop modes. This parameter is required for
     * [vibrator.stopVibration9+]{@link vibrator.stopVibration(stopMode: VibratorStopMode, callback: AsyncCallback<void>)}
     * or [vibrator.stopVibration9+]{@link vibrator.stopVibration(stopMode: VibratorStopMode)}. The stop mode must match
     * that delivered in [VibrateEffect9+]{@link vibrator.VibrateEffect}.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 8
     */
    enum VibratorStopMode {
        /**
         * The vibration to stop is in **duration** mode.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 8
         */
        VIBRATOR_STOP_MODE_TIME = 'time',
        /**
         * The vibration to stop is in **EffectId** mode.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 8
         */
        VIBRATOR_STOP_MODE_PRESET = 'preset'
    }
    /**
     * Enumerates the vibration scenarios.
     *
     * <!--RP1End-->
     *
     * @unionmember { 'unknown' } Unknown scenario, with the lowest priority. This parameter has a fixed value of
     *     **unknown**.
     * @unionmember { 'alarm' } Vibration for alarms. This parameter has a fixed value of **alarm**.
     * @unionmember { 'ring' } Vibration for ringing. This parameter has a fixed value of **ring**.
     * @unionmember { 'notification' } Vibration for notification. This parameter has a fixed value of **notification**.
     * @unionmember { 'communication' } Vibration for communication. This parameter has a fixed value of
     *     **communication**.
     * @unionmember { 'touch' } Vibration for touch. This parameter has a fixed value of **touch**.
     * @unionmember { 'media' } Vibration for media. This parameter has a fixed value of **media**.
     * @unionmember { 'physicalFeedback' } Vibration for physical feedback. This parameter has a fixed value of
     *     **physicalFeedback**.
     * @unionmember { 'simulateReality' } Vibration for simulated reality. This parameter has a fixed value of
     *     **simulateReality**.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    type Usage = 'unknown' | 'alarm' | 'ring' | 'notification' | 'communication' | 'touch' | 'media' | 'physicalFeedback' | 'simulateReality';
    /**
     * Describes the vibration attribute.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    interface VibrateAttribute {
        /**
         * Vibrator ID. The default value is **0**.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        id?: number;
        /**
         * Device ID. The default value is **-1**, indicating the local device. Since API version 19, you can use
         * [getVibratorInfoSync]{@link vibrator.getVibratorInfoSync} or [on]{@link vibrator.on} to query the device ID.
         *
         * This API can be used in atomic services since API version 19.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @atomicservice
         * @since 19
         */
        deviceId?: number;
        /**
         * Vibration scenario. The default value is **unknown**. The value must be an enum defined in
         * [Usage]{@link vibrator.Usage}.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        usage: Usage;
    }
    /**
     * Enumerates vibration effects of the vibrator. You can specify the vibration effect when calling
     * [vibrator.startVibration9+]{@link vibrator.startVibration(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback<void>)}
     * or [vibrator.startVibration9+]{@link vibrator.startVibration(effect: VibrateEffect, attribute: VibrateAttribute)}.
     *
     * @unionmember { VibrateTime } Triggers vibration based on a specified duration.
     *     <br>
     *      This API can be used in atomic services since API version 11.
     * @unionmember { VibratePreset } Triggers vibration based on a preset effect.
     * @unionmember { VibrateFromFile } Triggers vibration based on a custom vibration configuration file. [since 10]
     * @unionmember { VibrateFromPattern } Triggers vibration based on a custom effect. [since 18]
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    type VibrateEffect = VibrateTime | VibratePreset | VibrateFromFile | VibrateFromPattern;
    /**
     * Represents vibration of the specified duration.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    interface VibrateTime {
        /**
         * The value is **time**, indicating vibration of the specified duration.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        type: 'time';
        /**
         * Vibration duration, in ms. The value range is (0,1800000]. The maximum vibration duration varies with devices due
         * to different component protection design specifications of drivers provided by different vendors. It is
         * recommended that a single vibration duration be less than or equal to 10s to maximize user experience.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        duration: number;
    }
    /**
     * Represents the preset vibration effect. You can pass **VibratePreset** to
     * [VibrateEffect9+]{@link vibrator.VibrateEffect} to specify a preset vibration effect when calling
     * [vibrator.startVibration9+]{@link vibrator.startVibration(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback<void>)}
     * or [vibrator.startVibration9+]{@link vibrator.startVibration(effect: VibrateEffect, attribute: VibrateAttribute)}.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 9
     */
    interface VibratePreset {
        /**
         * The value **preset** means that vibration is triggered based on the specified effect.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 9
         */
        type: 'preset';
        /**
         * Effect ID. The value is a string of a maximum of 64 characters. If the length exceeds 64 characters, the first 64
         * characters are used.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 9
         */
        effectId: string;
        /**
         * Number of repeated vibrations. This parameter is optional. The default value is **1**.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 9
         */
        count?: number;
        /**
         * Vibration intensity. This parameter is optional. The value range is [0, 100]. The default value is **100**. If
         * vibration intensity adjustment is not supported, the default vibration intensity will be used.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 12
         */
        intensity?: number;
    }
    /**
     * Represents a custom vibration pattern. It is supported only by certain devices. An error code will be returned if a
     * device does not support this vibration mode. You can pass **VibrateFromFile** to
     * [VibrateEffect9+]{@link vibrator.VibrateEffect} to specify a custom vibration pattern when calling
     * [vibrator.startVibration9+]{@link vibrator.startVibration(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback<void>)}
     * or [vibrator.startVibration9+]{@link vibrator.startVibration(effect: VibrateEffect, attribute: VibrateAttribute)}.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 10
     */
    interface VibrateFromFile {
        /**
         * The value **file** means vibration according to a vibration configuration file.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 10
         */
        type: 'file';
        /**
         * File descriptor (FD) of the vibration configuration file.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 10
         */
        hapticFd: HapticFileDescriptor;
    }
    /**
     * Describes the FD of a custom vibration configuration file. Ensure that the file is available, and the parameters in
     * it can be obtained from the sandbox path through the
     * [fileIo.open](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#fileioopen) API or from the HAP resource
     * through the
     * [getRawFd]{@link @ohos.resourceManager:resourceManager.ResourceManager.getRawFd(path: string, callback: _AsyncCallback<RawFileDescriptor>)}
     * API. The application scenario is as follows: The vibration sequence is stored in a file and vibration needs to be
     * triggered based on the offset and length. For details about the storage format of the vibration sequence, see
     * [Vibration Effect Description](docroot://device/sensor/vibrator-guidelines.md#vibration-effect-description).
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 10
     */
    interface HapticFileDescriptor {
        /**
         * FD of the custom vibration configuration file.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 10
         */
        fd: number;
        /**
         * Offset from the start position of the file, in bytes. The default value is the start position of the file, and
         * the value cannot exceed the valid range of the file.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 10
         */
        offset?: number;
        /**
         * Resource length, in bytes. The default value is the length from the offset position to the end of the file, and
         * the value cannot exceed the valid range of the file.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 10
         */
        length?: number;
    }
    /**
     * Vibration event type.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 18
     */
    enum VibratorEventType {
        /**
         * Long vibration.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        CONTINUOUS = 0,
        /**
         * Short vibration.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        TRANSIENT = 1
    }
    /**
     * Defines the gain relative to the vibration intensity.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 18
     */
    interface VibratorCurvePoint {
        /**
         * Start time offset, in ms.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        time: number;
        /**
         * Gain relative to the vibration intensity. This parameter is optional. The value range is [0,100%]. If this
         * parameter is left empty, the default value is **1**.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        intensity?: number;
        /**
         * Change relative to the vibration frequency. This parameter is optional. The value range is [-100,100]. If this
         * parameter is left empty, the default value is **0**.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        frequency?: number;
    }
    /**
     * Vibration event.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 18
     */
    interface VibratorEvent {
        /**
         * Vibration event type.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        eventType: VibratorEventType;
        /**
         * Vibration start time, in ms. The value range is [0,1800000].
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        time: number;
        /**
         * Vibration duration. This parameter is optional, in ms. The value range is (0,5000]. The default value is **48**
         * for short vibration and **1000** for long vibration.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        duration?: number;
        /**
         * Vibration intensity. This parameter is optional. The value range is [0,100]. If this parameter is left empty, the
         * default value is **100**.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        intensity?: number;
        /**
         * Vibration frequency. This parameter is optional. The value range is [0,100]. If this parameter is left empty, the
         * default value is **50**.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        frequency?: number;
        /**
         * Channel number. This parameter is optional. The value range is [0,2]. If this parameter is left empty, the
         * default value is **0**.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        index?: number;
        /**
         * Adjustment points of the vibration curve.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        points?: Array<VibratorCurvePoint>;
    }
    /**
     * Defines the vibration sequence.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 18
     */
    interface VibratorPattern {
        /**
         * Absolute vibration start time, in ms.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        time: number;
        /**
         * Vibration event array, which is the **VibratorPattern** object returned by **build() **.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        events: Array<VibratorEvent>;
    }
    /**
     * Defines the parameters for continuous vibration.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 18
     */
    interface ContinuousParam {
        /**
         * Vibration intensity. This parameter is optional. The value range is [0,100]. If this parameter is left empty, the
         * default value is **100**.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        intensity?: number;
        /**
         * Vibration frequency. This parameter is optional. The value range is [0,100]. If this parameter is left empty, the
         * default value is **50**.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        frequency?: number;
        /**
         * Adjustment points of the vibration curve.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        points?: VibratorCurvePoint[];
        /**
         * Channel number. This parameter is optional. The value range is [0,2]. If this parameter is left empty, the
         * default value is **0**.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        index?: number;
    }
    /**
     * Defines the parameters for transient vibration.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 18
     */
    interface TransientParam {
        /**
         * Vibration intensity. This parameter is optional. The value range is [0,100]. If this parameter is left empty, the
         * default value is **100**.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        intensity?: number;
        /**
         * Vibration frequency. This parameter is optional. The value range is [0,100]. If this parameter is left empty, the
         * default value is **50**.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        frequency?: number;
        /**
         * Channel number. This parameter is optional. The value range is [0,2]. If this parameter is left empty, the
         * default value is **0**.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        index?: number;
    }
    /**
     * Provide methods for adding long or short vibration events and generate VibratorPattern objects.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @name VibratorPatternBuilder
     * @since 18
     */
    class VibratorPatternBuilder {
        /**
         * Adds a long vibration event as a **VibratorPattern** object.
         *
         * @param { number } time - Start time of the long vibration event, in ms. The value range is [0, 1800000].
         * @param { number } duration - Duration of the long vibration event, in ms. The value range is (0,5000].
         * @param { ContinuousParam } [options] - Optional parameters.
         * @returns { VibratorPatternBuilder } **VibratorPatternBuilder** object representing a long vibration event.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        addContinuousEvent(time: number, duration: number, options?: ContinuousParam): VibratorPatternBuilder;
        /**
         * Adds a short vibration event as a **VibratorPattern** object.
         *
         * @param { number } time - Start time of the short vibration event, in ms. The value range is [0, 1800000].
         * @param { TransientParam } [options] - Optional parameters.
         * @returns { VibratorPatternBuilder } **VibratorPatternBuilder** object representing a short vibration event.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        addTransientEvent(time: number, options?: TransientParam): VibratorPatternBuilder;
        /**
         * Constructor used to create a **VibratorPattern** object, which determines the vibration sequence of short or long
         * events.
         *
         * @returns { VibratorPattern } **VibratorPattern** object.
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        build(): VibratorPattern;
    }
    /**
     * Defines the custom vibration effect.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 18
     */
    interface VibrateFromPattern {
        /**
         * If the value is **pattern**, the vibrator vibrates based on the specified pattern.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        type: 'pattern';
        /**
         * Vibration event array, which is the **VibratorPattern** object returned by **build() **.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 18
         */
        pattern: VibratorPattern;
    }
    /**
     * Defines the vibrator parameters. If **VibratorInfoParam** is left unspecified, an API applies to all vibrators of
     * the local device by default.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 19
     */
    interface VibratorInfoParam {
        /**
         * Device ID. The default value is **-1**, indicating the local device. Since API version 19, you can use
         * [getVibratorInfoSync]{@link vibrator.getVibratorInfoSync} or [on]{@link vibrator.on} to query the device ID.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 19
         */
        deviceId?: number;
        /**
         * Vibrator ID. The default value is **0**, which indicates all vibrators of the local device. Since API version 19,
         * you can use [getVibratorInfoSync]{@link vibrator.getVibratorInfoSync} or [on]{@link vibrator.on} to query the
         * vibrator ID.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 19
         */
        vibratorId?: number;
    }
    /**
     * Defines the vibrator information.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 19
     */
    interface VibratorInfo {
        /**
         * Device ID.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 19
         */
        deviceId: number;
        /**
         * Vibrator ID.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 19
         */
        vibratorId: number;
        /**
         * Device name.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 19
         */
        deviceName: string;
        /**
         * Whether HD vibration is supported. The value **true** indicates that HD vibration is supported, and the value
         * **false** indicates the opposite.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 19
         */
        isHdHapticSupported: boolean;
        /**
         * Whether the device is a local device. The value **true** indicates that the device is a local device, and the
         * value **false** indicates the opposite.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @crossplatform [since 22]
         * @since 19
         */
        isLocalVibrator: boolean;
    }
    /**
     * Queries the vibrator list of one or all devices.
     *
     * @param { VibratorInfoParam } [param] - Vibrator parameters, such as the specified device and vibrator. If this
     *     parameter is left unspecified, this API applies to all vibrators of the local device by default.
     * @returns { Array<VibratorInfo> } Vibrator information.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @crossplatform [since 22]
     * @since 19
     */
    function getVibratorInfoSync(param?: VibratorInfoParam): Array<VibratorInfo>;
    /**
     * Enables listening for vibrator status changes.
     *
     * @param { 'vibratorStateChange' } type - Event type. The value **vibratorStateChange** indicates a vibrator online/
     *     offline event.
     * @param { Callback<VibratorStatusEvent> } callback - Callback used to return the vibrator status change event.
     * @throws { BusinessError } 14600101 - Device operation failed.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @since 19
     */
    function on(type: 'vibratorStateChange', callback: Callback<VibratorStatusEvent>): void;
    /**
     * Disables listening for vibrator status changes.
     *
     * @param { 'vibratorStateChange' } type - Event type. The value **vibratorStateChange** indicates a vibrator online/
     *     offline event.
     * @param { Callback<VibratorStatusEvent> } [callback] - Callback used to return the vibrator status change event. If
     *     this parameter is not specified, all callbacks of vibrator status change events will be unregistered.
     * @throws { BusinessError } 14600101 - Device operation failed.
     * @syscap SystemCapability.Sensors.MiscDevice
     * @since 19
     */
    function off(type: 'vibratorStateChange', callback?: Callback<VibratorStatusEvent>): void;
    /**
     * Defines the vibrator status change event.
     *
     * @syscap SystemCapability.Sensors.MiscDevice
     * @since 19
     */
    interface VibratorStatusEvent {
        /**
         * Event timestamp, in ms.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @since 19
         */
        timestamp: number;
        /**
         * Device ID.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @since 19
         */
        deviceId: number;
        /**
         * Number of vibrators on the device.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @since 19
         */
        vibratorCount: number;
        /**
         * Vibrator status. The value **true** indicates that the device is online, and the value **false** indicates the
         * opposite.
         *
         * @syscap SystemCapability.Sensors.MiscDevice
         * @since 19
         */
        isVibratorOnline: boolean;
    }
}
export default vibrator;

```
