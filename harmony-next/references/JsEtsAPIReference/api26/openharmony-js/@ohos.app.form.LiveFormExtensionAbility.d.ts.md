# @ohos.app.form.LiveFormExtensionAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025-2026 Huawei Device Co., Ltd.
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
 * The **LiveFormExtensionAbility** module, inherited from
 * [ExtensionAbility]{@link @ohos.app.ability.ExtensionAbility:ExtensionAbility}, provides interactive widget functions,
 *  including creating and destroying interactive widgets.
 *
 * > **NOTE**
 *
 * > Exceptions may occur if some APIs are called. For details about the API list, see
 * > [Appendix](docroot://reference/apis-form-kit/js-apis-app-form-LiveFormExtensionAbility.md#appendix).
 *
 * @file
 * @kit FormKit
 */
import ExtensionAbility from './@ohos.app.ability.ExtensionAbility';
import LiveFormExtensionContext from './application/LiveFormExtensionContext';
import type UIExtensionContentSession from './@ohos.app.ability.UIExtensionContentSession';
import formInfo from './@ohos.app.form.formInfo';
/**
 * Provides information about a live form.
 * @typedef { LiveFormInfo }
 * @syscap SystemCapability.Ability.Form
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
export interface LiveFormInfo {
    /**
     * The form id of the live form.
     *
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    formId: string;
    /**
     * The live form display area.
     *
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    rect: formInfo.Rect;
    /**
     * The form border radius.
     * Unit: vp, The value must be greater than or equal to 0.
     *
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    borderRadius: number;
}
/**
 * Interactive widget extension class. It provides APIs for the widget provider to receive notifications about widget
 * creation and destruction.
 *
 * @syscap SystemCapability.Ability.Form
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
declare class LiveFormExtensionAbility extends ExtensionAbility {
    /**
     * Context of the **LiveFormExtensionAbility**. This context is inherited from
     * [ExtensionContext]{@link ./application/ExtensionContext:ExtensionContext}.
     *
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    context: LiveFormExtensionContext;
    /**
     * Called after the UI content of **LiveFormExtensionAbility** is created.
     *
     * @param { LiveFormInfo } liveFormInfo - Interactive widget information, including the widget ID.
     * @param { UIExtensionContentSession } session - UI information.
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void;
    /**
     * Called to clear resources when this **LiveFormExtensionAbility** is destroyed.
     *
     * @param { LiveFormInfo } liveFormInfo - Interactive widget information, including the widget ID.
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onLiveFormDestroy(liveFormInfo: LiveFormInfo): void;
}
export default LiveFormExtensionAbility;

```
