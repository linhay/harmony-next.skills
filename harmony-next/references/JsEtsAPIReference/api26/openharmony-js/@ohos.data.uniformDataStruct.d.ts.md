# @ohos.data.uniformDataStruct.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024-2026 Huawei Device Co., Ltd.
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
 * @kit ArkData
 */
import image from './@ohos.multimedia.image';
/**
 * As a part of the Unified Data Management Framework (UDMF), the **uniformDataStruct** module provides data structs
 * corresponding to certain
 * [UniformDataTypes]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor.UniformDataType} for service
 * scenarios of many-to-many data sharing across applications. It helps simplify data interaction and reduce the data
 * type adaptation workload.
 *
 * @syscap SystemCapability.DistributedDataManager.UDMF.Core
 * @stagemodelonly
 * @since 12
 */
declare namespace uniformDataStruct {
    /**
     * Represents data of the plain text type.
     *
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @since 12
     */
    interface PlainText {
        /**
         * Uniform data type, which has a fixed value of **general.plain-text**. For details, see
         * [UniformDataType]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor.UniformDataType}.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        readonly uniformDataType: 'general.plain-text';
        /**
         * Plaintext content.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        textContent: string;
        /**
         * Text abstract. It is an empty string by default.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        abstract?: string;
        /**
         * Object of the dictionary type used to describe the attributes of the text content. Both the key and value of the
         * object are of the string type. For example, the following is a **details** object used to describe the properties
         * of a file:
         *
         * {
         *
         * "title":"Title of the file",
         *
         * "content":"Content of the file"
         *
         * }
         *
         * By default, it is an empty dictionary object.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        details?: Record<string, string>;
    }
    /**
     * Represents data of the hyperlink type.
     *
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @since 12
     */
    interface Hyperlink {
        /**
         * Uniform data type, which has a fixed value of **general.hyperlink**. For details, see
         * [UniformDataType]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor.UniformDataType}.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        readonly uniformDataType: 'general.hyperlink';
        /**
         * URL.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        url: string;
        /**
         * Description of the linked content. This parameter is optional. By default, it is an empty string.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        description?: string;
        /**
         * Object of the dictionary type used to describe the attributes of the hyperlink. Both the key and value of the
         * object are of the string type. For example, the following is a **details** object used to describe the properties
         * of a file:
         *
         * {
         *
         * "title":"Title of the file",
         *
         * "content":"Content of the file"
         *
         * }
         *
         * By default, it is an empty dictionary object.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        details?: Record<string, string>;
    }
    /**
     * Represents data of the HTML type.
     *
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @since 12
     */
    interface HTML {
        /**
         * Uniform data type, which has a fixed value of **general.html**. For details, see
         * [UniformDataType]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor.UniformDataType}.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        readonly uniformDataType: 'general.html';
        /**
         * Content in HTML format.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        htmlContent: string;
        /**
         * Plaintext without HTML tags. This parameter is optional. By default, it is an empty string.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        plainContent?: string;
        /**
         * Object of the dictionary type used to describe the attributes of the HTML content. Both the key and value of the
         * object are of the string type. For example, the following is a **details** object used to describe the properties
         * of a file:
         *
         * {
         *
         * "title":"Title of the file",
         *
         * "content":"Content of the file"
         *
         * }
         *
         * By default, it is an empty dictionary object.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        details?: Record<string, string>;
        /**
         * Defines URI authorization policies for drag intention.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        uriAuthorizationPolicies?: Array<number>;
    }
    /**
     * Represents data of the home screen icon type defined by the system.
     *
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @since 12
     */
    interface OpenHarmonyAppItem {
        /**
         * Uniform data type, which has a fixed value of **openharmony.app-item**. For details, see
         * [UniformDataType]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor.UniformDataType}.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        readonly uniformDataType: 'openharmony.app-item';
        /**
         * ID of the application, for which the icon is used.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        appId: string;
        /**
         * Name of the application, for which the icon is used.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        appName: string;
        /**
         * Image ID of the icon.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        appIconId: string;
        /**
         * Label ID corresponding to the icon name.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        appLabelId: string;
        /**
         * Bundle name corresponding to the icon.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        bundleName: string;
        /**
         * Application ability name corresponding to the icon.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        abilityName: string;
        /**
         * Object of the dictionary type used to describe the icon. The key is of the string type, and the value can be a
         * number, a string, or a Uint8Array. By default, it is an empty dictionary object.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 12
         */
        details?: Record<string, number | string | Uint8Array>;
    }
    /**
     * Represents data of the content widget type.
     *
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @since 14
     */
    interface ContentForm {
        /**
         * Uniform data type, which has a fixed value of **general.content-form**.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 14
         */
        readonly uniformDataType: 'general.content-form';
        /**
         * Image data in the content widget.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 14
         */
        thumbData?: Uint8Array;
        /**
         * Description of the content widget.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 14
         */
        description?: string;
        /**
         * Title of the content widget.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 14
         */
        title: string;
        /**
         * Application icon data in the content widget.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 14
         */
        appIcon?: Uint8Array;
        /**
         * Application name in the content widget.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 14
         */
        appName?: string;
        /**
         * Hyperlink in the content widget.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 14
         */
        linkUri?: string;
    }
    /**
     * Represents data of the widget type defined by the system.
     *
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @since 15
     */
    interface Form {
        /**
         * Uniform data type, which has a fixed value of **openharmony.form**. For details, see
         * [UniformDataType]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor.UniformDataType}.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        readonly uniformDataType: 'openharmony.form';
        /**
         * Widget ID.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        formId: number;
        /**
         * Widget name.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        formName: string;
        /**
         * Bundle to which the widget belongs.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        bundleName: string;
        /**
         * Ability name corresponding to the widget.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        abilityName: string;
        /**
         * Module to which the widget belongs.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        module: string;
        /**
         * Object of the dictionary type used to describe the icon. The key is of the string type, and the value can be a
         * number, a string, or a Uint8Array. By default, it is an empty dictionary object.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        details?: Record<string, number | string | Uint8Array>;
    }
    /**
     * Represents data of the file URI type.
     *
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @since 15
     */
    interface FileUri {
        /**
         * Uniform data type, which has a fixed value of **general.file-uri**. For details, see
         * [UniformDataType]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor.UniformDataType}.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        readonly uniformDataType: 'general.file-uri';
        /**
         * File path.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        oriUri: string;
        /**
         * File type, which must be UTD. For details, see [Prebuilt UTDs]. The
         * maximum length of the value is 1024 bytes.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        fileType: string;
        /**
         * Object of the dictionary type used to describe the icon. The key is of the string type, and the value can be a
         * number, a string, or a Uint8Array. By default, it is an empty dictionary object.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        details?: Record<string, number | string | Uint8Array>;
        /**
         * Defines URI authorization policies for drag intention.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        uriAuthorizationPolicies?: Array<number>;
    }
    /**
     * Represents data of the pixel map type defined by the system.
     *
     * @syscap SystemCapability.DistributedDataManager.UDMF.Core
     * @stagemodelonly
     * @since 15
     */
    interface PixelMap {
        /**
         * Uniform data type, which has a fixed value of **openharmony.pixel-map**. For details, see
         * [UniformDataType]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor.UniformDataType}.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        readonly uniformDataType: 'openharmony.pixel-map';
        /**
         * Binary data of the pixel map.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        pixelMap: image.PixelMap;
        /**
         * Object of the dictionary type used to describe the icon. The key is of the string type, and the value can be a
         * number, a string, or a Uint8Array. By default, it is an empty dictionary object.
         *
         * @syscap SystemCapability.DistributedDataManager.UDMF.Core
         * @stagemodelonly
         * @since 15
         */
        details?: Record<string, number | string | Uint8Array>;
    }
}
export default uniformDataStruct;

```
