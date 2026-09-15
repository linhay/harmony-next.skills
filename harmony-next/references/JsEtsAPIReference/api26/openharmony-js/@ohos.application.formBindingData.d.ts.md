# @ohos.application.formBindingData.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2026 Huawei Device Co., Ltd.
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
/**
 * The **FormBindingData** module provides APIs for widget data binding. You can use the APIs to create a
 * **FormBindingData** object and obtain related information.
 *
 * @syscap SystemCapability.Ability.Form
 * @since 8
 * @deprecated since 9
 * @useinstead @ohos.app.form.formBindingData:formBindingData
 */
declare namespace formBindingData {
    /**
     * Creates a **FormBindingData** object.
     *
     * @param { Object | string } [obj] - Data to be displayed on the JS widget. The value can be an object containing multiple
     *     key-value pairs or a string in JSON format. The image data is identified by **'formImages'**, and the content is
     *     multiple key-value pairs, each of which consists of an image identifier and image file descriptor. The final format
     *     is {'formImages': {'key1': fd1, 'key2': fd2}}.
     * @returns { FormBindingData } **FormBindingData** object created based on the passed data.
     * @syscap SystemCapability.Ability.Form
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.app.form.formBindingData:formBindingData#createFormBindingData
     */
    function createFormBindingData(obj?: Object | string): FormBindingData;
    /**
     * Describes a **FormBindingData** object.
     *
     * @syscap SystemCapability.Ability.Form
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.app.form.formBindingData:formBindingData#FormBindingData
     */
    interface FormBindingData {
        /**
         * Data to be displayed on the JS widget. The value can be an object containing multiple key-value pairs or a string
         *  in JSON format.
         *
         * @syscap SystemCapability.Ability.Form
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.app.form.formBindingData:formBindingData#FormBindingData
         */
        data: Object;
    }
}
export default formBindingData;

```
