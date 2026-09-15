# @ohos.app.ability.UIExtensionAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
import AbilityConstant from './@ohos.app.ability.AbilityConstant';
import type Want from './@ohos.app.ability.Want';
import ExtensionAbility from './@ohos.app.ability.ExtensionAbility';
import type UIExtensionContentSession from './@ohos.app.ability.UIExtensionContentSession';
import type UIExtensionContext from './application/UIExtensionContext';
/**
 * UIExtensionAbility is an ExtensionAbility component with a User Interface (UI). It inherits from
 * [ExtensionAbility]{@link ./@ohos.app.ability.ExtensionAbility:ExtensionAbility} and provides basic lifecycle
 * capabilities such as component creation, destruction, and foreground/background switching. Unlike the UIAbility, the
 * UIExtensionAbility does not appear as a separate mission in the mission view. The foreground/background state and
 * visibility of the UIExtensionAbility follow those of its host window.
 * You cannot directly inherit from the UIExtensionAbility. However, you can choose other components that inherit from
 * UIExtensionAbility based on specific service scenarios. For example, when handling data shared from other
 * applications, you can use the
 * [ShareExtensionAbility]{@link ./@ohos.app.ability.ShareExtensionAbility:ShareExtensionAbility}; when providing
 * widget editing functionality, you can use the
 * [FormEditExtensionAbility]{@link ./@ohos.app.form.FormEditExtensionAbility:FormEditExtensionAbility}.
 * For details about the inheritance relationship of each ability, see
 * [Inheritance Relationship](docroot://reference/apis-ability-kit/js-apis-app-ability-ability.md#ability-inheritance-relationship)
 * .
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @since 10
 */
declare class UIExtensionAbility extends ExtensionAbility {
    /**
     * Context of the UIExtensionAbility.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 10
     */
    context: UIExtensionContext;
    /**
     * Called when a UIExtensionAbility instance is created. You can execute initialization logic (such as defining
     * variables and loading resources) within this callback.
     *
     * @param { AbilityConstant.LaunchParam } launchParam - Parameters for application launch, including the reason for
     *     application launch and the reason for the last application exit. [since 12]
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 10
     */
    onCreate(launchParam: AbilityConstant.LaunchParam): void;
    /**
     * Called when a [UIExtensionContentSession]{@link ./@ohos.app.ability.UIExtensionContentSession} instance is created.
     * You can load a page through the UIExtensionContentSession instance within this callback.
     *
     * @param { Want } want - Data passed by the caller when launching the UIExtensionAbility.
     * @param { UIExtensionContentSession } session - UIExtensionContentSession instance.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 10
     */
    onSessionCreate(want: Want, session: UIExtensionContentSession): void;
    /**
     * Called when a UIExtensionContentSession is destroyed. It informs applications that the UIExtensionContentSession
     * instance is no longer available for use.
     *
     * @param { UIExtensionContentSession } session - UIExtensionContentSession instance.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 10
     */
    onSessionDestroy(session: UIExtensionContentSession): void;
    /**
     * Called when a UIExtensionAbility is initially launched into the foreground or transitions from the background to
     * the foreground. You can apply for resources when the UI becomes visible within this callback.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 10
     */
    onForeground(): void;
    /**
     * Called when a UIExtensionAbility transitions from the foreground to the background. You can release resources when
     * the UI is no longer invisible within this callback.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 10
     */
    onBackground(): void;
    /**
     * Called when a UIExtensionAbility is destroyed. You can clear resources and save data during this lifecycle. This
     * API returns the result synchronously or uses a promise to return the result.
     * After the **onDestroy()** lifecycle callback is executed, the application may exit. Consequently, the asynchronous
     * function (for example, asynchronously writing data to the database) in **onDestroy()** may fail to be executed.
     * Using a Promise for asynchronous callback is recommended to prevent such issues.
     *
     * @returns { void | Promise<void> } No return value or a Promise object that returns no value.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 10
     */
    onDestroy(): void | Promise<void>;
}
export default UIExtensionAbility;

```
