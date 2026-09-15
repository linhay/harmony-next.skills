# @ohos.app.ability.appRecovery.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2023 Huawei Device Co., Ltd.
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
 * @kit AbilityKit
 */
import UIAbilityContext from './application/UIAbilityContext';
import Want from './@ohos.app.ability.Want';
/**
 * The appRecovery module provides APIs for recovering faulty applications.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace appRecovery {
    /**
     * Enumerates the application restart flags. This enum is used as an input parameter of
     * [enableAppRecovery]{@link appRecovery.enableAppRecovery}.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    enum RestartFlag {
        /**
         * The application is restarted in all cases.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 11]
         * @since 9
         */
        ALWAYS_RESTART = 0,
        /**
         * The application is restarted in the case of JS_CRASH.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 11]
         * @since 9
         */
        RESTART_WHEN_JS_CRASH = 0x0001,
        /**
         * The application is restarted in the case of APP_FREEZE.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 11]
         * @since 9
         */
        RESTART_WHEN_APP_FREEZE = 0x0002,
        /**
         * The application is not restarted in any case.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 11]
         * @since 9
         */
        NO_RESTART = 0xFFFF,
        /**
         * Restart if the current app process encounters a cppcrash
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        RESTART_WHEN_CPP_CRASH = 0x0004
    }
    /**
     * Enumerates the scenarios for saving the application state. This enum is used as an input parameter of
     * [enableAppRecovery]{@link appRecovery.enableAppRecovery}.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    enum SaveOccasionFlag {
        /**
         * Saving the application state when an application fault occurs.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 11]
         * @since 9
         */
        SAVE_WHEN_ERROR = 0x0001,
        /**
         * Saving the application state when the application is switched to the background.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 11]
         * @since 9
         */
        SAVE_WHEN_BACKGROUND = 0x0002
    }
    /**
     * Enumerates the application state saving modes. This enum is used as an input parameter of
     * [enableAppRecovery]{@link appRecovery.enableAppRecovery}.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    enum SaveModeFlag {
        /**
         * The application state is saved and written to the local file cache.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 11]
         * @since 9
         */
        SAVE_WITH_FILE = 0x0001,
        /**
         * The application state is saved in the memory. When the application exits due to a fault, it is written to the
         * local file cache.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 11]
         * @since 9
         */
        SAVE_WITH_SHARED_MEMORY = 0x0002
    }
    /**
     * Enables application recovery. After this API is called, the first ability that is displayed when the application is
     * started from the initiator can be restored.
     *
     * @param { RestartFlag } [restart] - Whether the application is restarted upon a fault. By default, the application
     *     is restarted.
     * @param { SaveOccasionFlag } [saveOccasion] - Scenario for saving the application state. By default, the state is
     *     saved when a fault occurs.
     * @param { SaveModeFlag } [saveMode] - Application state saving mode. By default, the application state is written to
     *     the local file cache.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @StageModelOnly
     * @atomicservice [since 11]
     * @since 9
     */
    function enableAppRecovery(restart?: RestartFlag, saveOccasion?: SaveOccasionFlag, saveMode?: SaveModeFlag): void;
    /**
     * Restarts the current process and starts the first ability that is displayed when the application is started. If the
     * state of this ability is saved, the saved state data is passed into the **wantParam** property in the **want**
     * parameter of the **onCreate** lifecycle callback of the ability.
     *
     * In API version 10, the ability specified by [setRestartWant]{@link appRecovery.setRestartWant} is started. If no
     * ability is specified, the following rules are used:
     *
     * If the ability of the current application running in the foreground supports recovery, that ability is started.
     *
     * If multiple abilities that support recovery is running in the foreground, only the last ability is started.
     *
     * If no ability is running in the foreground, none of them is started.
     *
     * This API can be used together with the APIs of [errorManager]{@link @ohos.app.ability.errorManager:errorManager}.
     * The interval between two restarts must be greater than one minute. If this API is called repeatedly within one
     * minute, the application exits but does not restart. The behavior of automatic restart is the same as that of
     * proactive restart.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @StageModelOnly
     * @atomicservice [since 11]
     * @since 9
     */
    function restartApp(): void;
    /**
     * Sets an ability that will be recovered. The ability must be a UIAbility in the current bundle.
     *
     * @param { Want } want - Want of the target ability. You can set the **bundleName** and **abilityName** fields in
     *     **Want** to specify the ability.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @StageModelOnly
     * @atomicservice [since 11]
     * @since 10
     */
    function setRestartWant(want: Want): void;
    /**
     * Saves the application state. This API can be used together with the APIs of
     * [errorManager]{@link @ohos.app.ability.errorManager:errorManager}.
     *
     * @returns { boolean } Whether the application state is saved. **true** if saved, **false** otherwise.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @StageModelOnly
     * @atomicservice [since 11]
     * @since 9
     */
    function saveAppState(): boolean;
    /**
     * Saves the ability state, which will be used for recovery. This API can be used together with the APIs of
     * [errorManager]{@link @ohos.app.ability.errorManager:errorManager}.
     *
     * @param { UIAbilityContext } [context] - Context of the target ability.
     * @returns { boolean } Whether the application state is saved. **true** if saved, **false** otherwise.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @StageModelOnly
     * @atomicservice [since 11]
     * @since 10
     */
    function saveAppState(context?: UIAbilityContext): boolean;
}
export default appRecovery;

```
