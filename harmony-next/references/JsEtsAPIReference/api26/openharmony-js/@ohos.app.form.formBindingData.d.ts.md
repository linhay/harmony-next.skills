# @ohos.app.form.formBindingData.d.ts

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
 * @kit FormKit
 */
/**
 * The **FormBindingData** module provides APIs for widget data binding. You can use the APIs to create a
 * **FormBindingData** object and obtain related information.
 *
 * @syscap SystemCapability.Ability.Form
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace formBindingData {
    /**
     * Creates a **FormBindingData** object.
     *
     * @param { Object | string } [obj] - Data to be displayed on the widget. The value can be an object containing multiple
     *     key-value pairs or a JSON string. The image data is identified by **'formImages'**, and the content is multiple key-
     *     value pairs, each of which consists of an image identifier and image file descriptor. The final format is {'
     *     formImages': {'key1': fd1, 'key2': fd2}}.<br>**NOTE**<br>During
     *     [widget update](docroot://form/arkts-ui-widget-interaction-overview.md), when the widget UI receives widget data
     *     through @LocalStorageProp, the **FormBindingData** object is serialized, that is, the widget data is converted into
     *     the string type. Since API version 20, if the widget data is updated using shared memory, the total size of the
     *     updated data cannot exceed 10 MB, and the number of updated images cannot exceed 20. In API version 19 and earlier
     *     versions, the maximum number of image files is 5, and the maximum memory size of each image is 2 MB. Exceeding this
     *     2 MB limit for any image will result in abnormal display.
     * @returns { FormBindingData } **FormBindingData** object created based on the passed data.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
     * @syscap SystemCapability.Ability.Form
     * @atomicservice [since 11]
     * @since 9
     */
    function createFormBindingData(obj?: Object | string): FormBindingData;
    /**
     * Defines the createFormBindingData result interface.
     *
     * @typedef FormBindingData
     * @syscap SystemCapability.Ability.Form
     * @atomicservice [since 11]
     * @since 9
     */
    interface FormBindingData {
        /**
         * Data for updating.
         *
         * @syscap SystemCapability.Ability.Form
         * @atomicservice [since 11]
         * @since 9
         */
        data: Object;
        /**
         * proxies for updating.
         *
         * @syscap SystemCapability.Ability.Form
         * @StageModelOnly
         * @atomicservice [since 11]
         * @since 10
         */
        proxies?: Array<ProxyData>;
    }
    /**
     * Defines the form proxy data.
     *
     * @typedef ProxyData
     * @syscap SystemCapability.Ability.Form
     * @StageModelOnly
     * @atomicservice [since 11]
     * @since 10
     */
    interface ProxyData {
        /**
         * Key for proxy. The value depends on the data publisher.
         *
         * @syscap SystemCapability.Ability.Form
         * @StageModelOnly
         * @atomicservice [since 11]
         * @since 10
         */
        key: string;
        /**
         * SubscriberId. The value depends on the data publisher. The default value is current formId.
         *
         * @syscap SystemCapability.Ability.Form
         * @StageModelOnly
         * @atomicservice [since 11]
         * @since 10
         */
        subscriberId?: string;
    }
}
export default formBindingData;

```
