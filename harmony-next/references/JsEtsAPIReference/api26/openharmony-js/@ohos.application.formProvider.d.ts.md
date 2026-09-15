# @ohos.application.formProvider.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2023 Huawei Device Co., Ltd.
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
 * @kit API10LessDeprecatedModules
 */
import { AsyncCallback } from './@ohos.base';
import formBindingData from './@ohos.application.formBindingData';
/**
 * The **FormProvider** module provides APIs related to the widget provider. You can use the APIs to update a widget,
 * set the next refresh time for a widget, obtain widget information, and request a widget release.
 *
 * @syscap SystemCapability.Ability.Form
 * @since 8
 * @deprecated since 9
 * @useinstead @ohos.app.form.formProvider:formProvider
 */
declare namespace formProvider {
    /**
     * Sets the next refresh time for a widget. This API uses an asynchronous callback to return the result.
     *
     * @param { string } formId - Widget ID.
     * @param { number } minute - Time for the next refresh. The value must be greater than or equal to 5, in minutes.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Ability.Form
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.app.form.formProvider:formProvider#setFormNextRefreshTime
     */
    function setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void;
    /**
     * Sets the next refresh time for a widget. This API uses a promise to return the result.
     *
     * @param { string } formId - Widget ID.
     * @param { number } minute - Time for the next refresh. The value must be greater than or equal to 5, in minutes.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Ability.Form
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.app.form.formProvider:formProvider#setFormNextRefreshTime
     */
    function setFormNextRefreshTime(formId: string, minute: number): Promise<void>;
    /**
     * Updates a widget. This API uses an asynchronous callback to return the result.
     *
     * @param { string } formId - ID of the widget to update.
     * @param { formBindingData.FormBindingData } formBindingData - Data to be used for the update.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Ability.Form
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.app.form.formProvider:formProvider#updateForm
     */
    function updateForm(formId: string, formBindingData: formBindingData.FormBindingData, callback: AsyncCallback<void>): void;
    /**
     * Updates a widget. This API uses a promise to return the result.
     *
     * @param { string } formId - ID of the widget to update.
     * @param { formBindingData.FormBindingData } formBindingData - Data to be used for the update.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Ability.Form
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.app.form.formProvider:formProvider#updateForm
     */
    function updateForm(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>;
}
export default formProvider;

```
