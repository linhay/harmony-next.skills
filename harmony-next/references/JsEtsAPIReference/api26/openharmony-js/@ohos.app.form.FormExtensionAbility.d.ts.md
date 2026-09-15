# @ohos.app.form.FormExtensionAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2026 Huawei Device Co., Ltd.
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
 * The **FormExtensionAbility** module provides lifecycle callbacks invoked when a widget is created, destroyed, or
 * updated.
 *
 * > **NOTE**
 *
 * > - The formExtensionAbility is cleared after 10 seconds of inactivity.
 *
 * > - The following modules cannot be referenced in the FormExtensionAbility, as doing so may cause the program to exit
 * >  abnormally:
 * >   - @ohos.ability.particleAbility (ParticleAbility)
 * >   - @ohos.multimedia.audio (Audio Management)
 * >   - @ohos.multimedia.camera (Camera Management)
 * >   - @ohos.multimedia.media (Media)
 * >   - @ohos.resourceschedule.backgroundTaskManager (Background Task Management)
 *
 * @file
 * @kit FormKit
 */
import formBindingData from './@ohos.app.form.formBindingData';
import formInfo from './@ohos.app.form.formInfo';
import FormExtensionContext from './application/FormExtensionContext';
import Want from './@ohos.app.ability.Want';
import { Configuration } from './@ohos.app.ability.Configuration';
/**
 * Widget extension class. It provides APIs to notify the widget provider that a widget is being created or the widget
 * visibility status is being changed.
 *
 * @syscap SystemCapability.Ability.Form
 * @stagemodelonly
 * @atomicservice [since 11]
 * @since 9
 */
declare class FormExtensionAbility {
    /**
     * Context of the FormExtensionAbility. This context is inherited from
     * [ExtensionContext]{@link ./application/ExtensionContext:ExtensionContext}.
     *
     * This API can be used in atomic services since API version 11.
     *
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    context: FormExtensionContext;
    /**
     * Called to notify the widget provider that a widget is being created.
     *
     * @param { Want } want - Want information of the widget. You can set the **parameters** field to one or more values
     *     enumerated in [widget parameters]{@link @ohos.app.form.formInfo:formInfo.FormParam}, such as widget ID, widget name,
     *     and widget style. The information must be managed as persistent data to facilitate subsequent widget update and
     *     deletion.
     * @returns { formBindingData.FormBindingData } A **formBindingData.FormBindingData** object containing the data to be
     *     displayed on the widget.
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onAddForm(want: Want): formBindingData.FormBindingData;
    /**
     * Called to notify the widget provider that a temporary widget has been converted to a normal one. Temporary widgets
     * and normal widgets are concepts of the widget host. Temporary widgets have a brief existence, appearing following
     * particular events or user interactions and vanishing automatically upon task completion. Normal widgets maintain a
     * lasting presence, continuing to exist unless explicitly removed or altered by the user. Function widgets developed
     * in normal cases are normal widgets. Currently, the widget host does not use temporary widgets.
     *
     * @param { string } formId - ID of the widget that requests to be converted to a normal one.
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onCastToNormalForm(formId: string): void;
    /**
     * Called to notify the widget provider that a widget is being updated, with update parameters carried. After
     * obtaining the latest data, your application should call
     * [updateForm]{@link @ohos.app.form.formProvider:formProvider.updateForm( formId: string, formBindingData: formBindingData.FormBindingData, callback: AsyncCallback<void> )}
     *  of **formProvider** to update the widget data.
     *
     * @param { string } formId - ID of the widget that requests to be updated.
     * @param { Record<string, Object> } [wantParams] - Parameters used for the update.
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onUpdateForm(formId: string, wantParams?: Record<string, Object>): void;
    /**
     * Called to notify the widget provider that the widget visibility status is being changed.
     * This API is valid only for system applications when **formVisibleNotify** is set to **true**.
     *
     * @param { object } newStatus - ID and visibility status of the widget to be changed. [since 9 - 10]
     * @param { Record<string, number> } newStatus - ID and visibility status of the widget to be changed. [since 11]
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @since 9
     */
    onChangeFormVisibility(newStatus: Record<string, number>): void;
    /**
     * Called to instruct the widget provider to process the widget event.
     *
     * @param { string } formId - ID of the widget that requests the event.
     * @param { string } message - Event message.
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onFormEvent(formId: string, message: string): void;
    /**
     * Called to notify the widget provider that a widget is being destroyed.
     *
     * @param { string } formId - ID of the widget to be destroyed.
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onRemoveForm(formId: string): void;
    /**
     * Called when system configuration items change. The **onConfigurationUpdate** callback is triggered only when the
     * FormExtensionAbility is alive. <!--Del-->Since API version 20, for system applications, the
     * **onConfigurationUpdate** callback within the FormExtensionAbility will be triggered when the system language
     * changes.<!--DelEnd-->
     *
     * @param { Configuration } newConfig - New configuration.
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onConfigurationUpdate(newConfig: Configuration): void;
    /**
     * Called to notify the widget provider that the widget host is requesting the widget state. By default, the initial
     * widget state is returned. (You can override this API as required.)
     *
     * @param { Want } want - Description of the widget state, including the bundle name, ability name, module name, and widget
     *     name.
     * @returns { formInfo.FormState } Enumerated values of the current widget status.
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onAcquireFormState?(want: Want): formInfo.FormState;
    /**
     * Called when the widget process of the widget provider exits.
     *
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onStop?(): void;
    /**
     * Called when the widget size changes.
     *
     * @param { string } formId - Widget ID.
     * @param { formInfo.FormDimension } newDimension - Widget dimension. For example, **Dimension_1_2** indicates a 1 x 2
     *     widget.
     * @param { formInfo.Rect } newRect - Widget position information, including the X and Y coordinates of the widget's top-
     *     left corner, as well as its width and height.
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void;
    /**
     * Called when the widget location changes.
     *
     * @param { string } formId - Widget ID.
     * @param { formInfo.FormLocation } newFormLocation - Enumerated value of the latest widget location.
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation): void;
}
export default FormExtensionAbility;

```
