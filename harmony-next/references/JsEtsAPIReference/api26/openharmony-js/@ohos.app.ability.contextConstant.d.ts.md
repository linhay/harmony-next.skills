# @ohos.app.ability.contextConstant.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2024 Huawei Device Co., Ltd.
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
 * @kit AbilityKit
 */
/**
 * The ContextConstant module defines context-related enums, including the file encryption partition level and process
 * mode of the UIAbility after it is started.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace contextConstant {
    /**
     * Enumerates the file encryption levels, which are used to ensure data security for applications across different
     * scenarios. You can select the appropriate encryption level based on the application requirements to protect user
     * data.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    export enum AreaMode {
        /**
         * Device-level encryption. Directories with this encryption level are accessible after the device is powered on.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice [since 11]
         * @since 9
         */
        EL1 = 0,
        /**
         * User-level encryption. Directories with this encryption level are accessible only after the device is powered on
         * and the password is entered (for the first time).
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice [since 11]
         * @since 9
         */
        EL2 = 1,
        /**
         * User-level encryption. The file permissions vary according to their scenarios.
         *
         * - An open file is always readable and writable regardless of whether the screen is locked.
         * - When the screen is locked, a closed file cannot be opened, read, or written. When the screen is unlocked, such
         * a file can be opened, read, and written.
         * - When the screen is locked, a file can be created and then opened and written but not read. When the screen is
         * unlocked, a file can be created and then opened, read, and written.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 11
         */
        EL3 = 2,
        /**
         * User-level encryption. The file permissions vary according to their scenarios.
         *
         * - When the screen is locked, an open file is not readable or writable. When the screen is unlocked, such a file
         * is readable and writable.
         * - When the screen is locked, a closed file cannot be opened, read, or written. When the screen is unlocked, such
         * a file can be opened, read, and written.
         * - When the screen is locked, a file cannot be created. When the screen is unlocked, a file can be created and
         * then opened, read, and written.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 11
         */
        EL4 = 3,
        /**
         * Application-level encryption. The file permissions vary according to their scenarios.
         *
         * - An open file is always readable and writable regardless of whether the screen is locked.
         *
         * When the screen is locked, a closed file can be opened, read, and written only if the reserved key is obtained by
         *  calling [Access](js-apis-screenLockFileManager.md#screenlockfilemanageracquireaccess). When the screen is
         * unlocked, such a file can be opened, read, and written.
         *
         * A file can be created and then opened, read, and written regardless of whether the screen is locked.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        EL5 = 4
    }
    /**
     * Enumerates the process modes of the UIAbility after it is started.
     * As a property of [StartOptions]{@link @ohos.app.ability.StartOptions:StartOptions}, **ProcessMode** takes effect
     * only in
     * [UIAbilityContext.startAbility]{@link ./application/UIAbilityContext:UIAbilityContext.startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>)}
     *  and is used to specify the process mode of the target UIAbility.
     * This value takes effect only on 2-in-1 devices and tablets. If it is used on other devices, error code 801 is
     * returned.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 12
     */
    export enum ProcessMode {
        /**
         * A new process is created, the UIAbility is started on the process, and the process exits along with the parent
         * process.
         *
         * **Constraints**:
         *
         * In this mode, the target UIAbility and caller must be in the same application.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 12
         */
        NEW_PROCESS_ATTACH_TO_PARENT = 1,
        /**
         * A new process is created, the UIAbility is started on the process, and the process is bound to the status bar
         * icon.
         *
         * **Constraints**:
         *
         * In this mode, the target UIAbility and caller must be in the same application, and the application must have an
         * icon in the status bar.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 12
         */
        NEW_PROCESS_ATTACH_TO_STATUS_BAR_ITEM = 2,
        /**
         * The UIAbility is started, and the process of the UIAbility is bound to the status bar icon.
         *
         * **Constraints**:
         *
         * In this mode, the target UIAbility and caller must be in the same application, and the application must have an
         * icon in the status bar.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 12
         */
        ATTACH_TO_STATUS_BAR_ITEM = 3
    }
    /**
     * Enumerates the visibility statuses of the UIAbility after it is started.
     * If the target UIAbility is set to invisible, the window of the target UIAbility is not displayed in the foreground,
     *  there is no icon in the dock, and the **onForeground** lifecycle of the target UIAbility is not triggered.
     * As a property of [StartOptions]{@link @ohos.app.ability.StartOptions:StartOptions}, **StartupVisibility** takes
     * effect only in
     * [UIAbilityContext.startAbility]{@link ./application/UIAbilityContext:UIAbilityContext.startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>)}
     *  and specifies the visibility of the target UIAbility after it is started.
     * This value takes effect only on 2-in-1 devices and tablets. If it is used on other devices, error code 801 is
     * returned.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 12
     */
    export enum StartupVisibility {
        /**
         * The target UIAbility is hidden after it is started in the new process. The **onForeground** lifecycle of the
         * UIAbility is not invoked.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 12
         */
        STARTUP_HIDE = 0,
        /**
         * The target UIAbility is displayed normally after it is started in the new process.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 12
         */
        STARTUP_SHOW = 1
    }
    /**
     * Enumerates the scenarios where the [onNewWant]{@link @ohos.app.ability.UIAbility:UIAbility#onNewWant} lifecycle
     * callback is not triggered. It is used in the
     * [setOnNewWantSkipScenarios]{@link ./application/UIAbilityContext:UIAbilityContext.setOnNewWantSkipScenarios} API.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    export enum Scenarios {
        /**
         * <!--RP1-->A scenario where the system API [missionManager.moveMissionToFront](./js-apis-app-ability-missionManager-sys.md#missionmanagermovemissiontofront-2) is called to move the UIAbility to the foreground.<!--RP1End-->
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 20
         */
        SCENARIO_MOVE_MISSION_TO_FRONT = 0x00000001,
        /**
         * A scenario where the [showAbility]{@link ./application/UIAbilityContext:UIAbilityContext.showAbility} API is called
         *  to move the UIAbility to the foreground.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 20
         */
        SCENARIO_SHOW_ABILITY = 0x00000002,
        /**
         * A scenario where the
         * [backToCallerAbilityWithResult]{@link ./application/UIAbilityContext:UIAbilityContext.backToCallerAbilityWithResult}
         *  API is called to move the UIAbility to the foreground.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 20
         */
        SCENARIO_BACK_TO_CALLER_ABILITY_WITH_RESULT = 0x00000004
    }
    /**
     * Context type
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export enum ContextType {
        /**
         * Application context type.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        APPLICATION_CONTEXT = 0,
        /**
         * Ability stage context type.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ABILITY_STAGE_CONTEXT = 1,
        /**
         * UI ability context type.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        UIABILITY_CONTEXT = 2,
        /**
         * Form extension context type.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        FORM_EXTENSION_CONTEXT = 3,
        /**
         * App service extension context type.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        APP_SERVICE_EXTENSION_CONTEXT = 4
    }
}
export default contextConstant;

```
