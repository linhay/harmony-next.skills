# @ohos.app.ability.AbilityLifecycleCallback.d.ts

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
 * The lifecycle of a [UIAbility]{@link ./@ohos.app.ability.UIAbility} dynamically changes from creation to
 * destruction.
 * The AbilityLifecycleCallback module provides the capability to listen for these lifecycle changes, which can be used
 * for scenarios such as tracking the runtime duration of each UIAbility and performing data loading decoupled from the
 * service logic of UIAbility.
 *
 * > **NOTE**
 * >
 * > The APIs provided by this module can listen for lifecycle changes of the UIAbility within the same process.
 *
 * @file
 * @kit AbilityKit
 */
import UIAbility from './@ohos.app.ability.UIAbility';
import window from './@ohos.window';
/**
 * The lifecycle of a [UIAbility]{@link ./@ohos.app.ability.UIAbility} dynamically changes from creation to
 * destruction.
 * The AbilityLifecycleCallback module provides the capability to listen for these lifecycle changes, which can be used
 * for scenarios such as tracking the runtime duration of each UIAbility and performing data loading decoupled from the
 * service logic of UIAbility.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
 * @stagemodelonly
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare class AbilityLifecycleCallback {
    /**
     * Called after the [onCreate]{@link ./@ohos.app.ability.UIAbility:UIAbility#onCreate} callback of the UIAbility is
     * triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onAbilityCreate(ability: UIAbility): void;
    /**
     * Called before the [onCreate]{@link ./@ohos.app.ability.UIAbility:UIAbility#onCreate} callback of the UIAbility is
     * triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onAbilityWillCreate?(ability: UIAbility): void;
    /**
     * Called after the [onWindowStageCreate]{@link ./@ohos.app.ability.UIAbility:UIAbility#onWindowStageCreate} callback of
     *  the UIAbility is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @param { window.WindowStage } windowStage - Main window manager of the UIAbility associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onWindowStageCreate(ability: UIAbility, windowStage: window.WindowStage): void;
    /**
     * Called before the [onWindowStageCreate]{@link ./@ohos.app.ability.UIAbility:UIAbility#onWindowStageCreate}
     * callback of the UIAbility is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @param { window.WindowStage } windowStage - Main window manager of the UIAbility associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onWindowStageWillCreate?(ability: UIAbility, windowStage: window.WindowStage): void;
    /**
     * Called before the [onNewWant]{@link ./@ohos.app.ability.UIAbility:UIAbility#onNewWant} callback of the UIAbility
     * is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onWillNewWant?(ability: UIAbility): void;
    /**
     * Called after the [onNewWant]{@link ./@ohos.app.ability.UIAbility:UIAbility#onNewWant} callback of the UIAbility
     * is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onNewWant?(ability: UIAbility): void;
    /**
     * Called when the main window of the UIAbility gains focus.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @param { window.WindowStage } windowStage - Main window manager of the UIAbility associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onWindowStageActive(ability: UIAbility, windowStage: window.WindowStage): void;
    /**
     * Called when the main window of the UIAbility loses focus.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @param { window.WindowStage } windowStage - Main window manager of the UIAbility associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onWindowStageInactive(ability: UIAbility, windowStage: window.WindowStage): void;
    /**
     * Called after the [onWindowStageDestroy]{@link ./@ohos.app.ability.UIAbility:UIAbility#onWindowStageDestroy}
     * callback of the UIAbility is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @param { window.WindowStage } windowStage - Main window manager of the UIAbility associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onWindowStageDestroy(ability: UIAbility, windowStage: window.WindowStage): void;
    /**
     * Called before the [onWindowStageDestroy]{@link ./@ohos.app.ability.UIAbility:UIAbility#onWindowStageDestroy}
     * callback of the UIAbility is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @param { window.WindowStage } windowStage - Main window manager of the UIAbility associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onWindowStageWillDestroy?(ability: UIAbility, windowStage: window.WindowStage): void;
    /**
     * Called after the [onDestroy]{@link ./@ohos.app.ability.UIAbility:UIAbility.onDestroy} callback of the UIAbility
     * is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onAbilityDestroy(ability: UIAbility): void;
    /**
     * Called before the [onDestroy]{@link ./@ohos.app.ability.UIAbility:UIAbility.onDestroy} callback of the UIAbility
     * is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onAbilityWillDestroy?(ability: UIAbility): void;
    /**
     * Called after the [onForeground]{@link ./@ohos.app.ability.UIAbility:UIAbility#onForeground} callback of the
     * UIAbility is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onAbilityForeground(ability: UIAbility): void;
    /**
     * Called before the [onForeground]{@link ./@ohos.app.ability.UIAbility:UIAbility#onForeground} callback of the
     * UIAbility is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onAbilityWillForeground?(ability: UIAbility): void;
    /**
     * Called after the [onBackground]{@link ./@ohos.app.ability.UIAbility:UIAbility#onBackground} callback of the
     * UIAbility is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onAbilityBackground(ability: UIAbility): void;
    /**
     * Called before the [onBackground]{@link ./@ohos.app.ability.UIAbility:UIAbility#onBackground} callback of the
     * UIAbility is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onAbilityWillBackground?(ability: UIAbility): void;
    /**
     * Called after the [onContinue]{@link ./@ohos.app.ability.UIAbility:UIAbility#onContinue} callback of the UIAbility
     * is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onAbilityContinue(ability: UIAbility): void;
    /**
     * Called before the [onContinue]{@link ./@ohos.app.ability.UIAbility:UIAbility#onContinue} callback of the UIAbility
     * is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onAbilityWillContinue?(ability: UIAbility): void;
    /**
     * Called before the [onWindowStageRestore]{@link ./@ohos.app.ability.UIAbility:UIAbility#onWindowStageRestore}
     * callback of the UIAbility is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @param { window.WindowStage } windowStage - Main window manager of the UIAbility associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onWindowStageWillRestore?(ability: UIAbility, windowStage: window.WindowStage): void;
    /**
     * Called after the [onWindowStageRestore]{@link ./@ohos.app.ability.UIAbility:UIAbility#onWindowStageRestore}
     * callback of the UIAbility is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @param { window.WindowStage } windowStage - Main window manager of the UIAbility associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onWindowStageRestore?(ability: UIAbility, windowStage: window.WindowStage): void;
    /**
     * Called before the [onSaveState]{@link ./@ohos.app.ability.UIAbility:UIAbility.onSaveState} callback of the
     * UIAbility is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onAbilityWillSaveState?(ability: UIAbility): void;
    /**
     * Called after the [onSaveState]{@link ./@ohos.app.ability.UIAbility:UIAbility.onSaveState} callback of the
     * UIAbility is triggered.
     *
     * @param { UIAbility } ability - UIAbility object associated with the callback event.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onAbilitySaveState?(ability: UIAbility): void;
}
export default AbilityLifecycleCallback;

```
