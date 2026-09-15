# @ohos.pasteboard.d.ts

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
 * @kit BasicServicesKit
 */
import { AsyncCallback } from './@ohos.base';
import Want from './@ohos.app.ability.Want';
import image from './@ohos.multimedia.image';
import unifiedDataChannel from './@ohos.data.unifiedDataChannel';
/**
 * This module provides the capabilities of managing the system pasteboard to support the copy and paste functions. You
 * can use the APIs of this module to operate pasteboard content of the plain text, HTML, URI, Want, PixelMap, and
 * other types.
 *
 * @syscap SystemCapability.MiscServices.Pasteboard
 * @crossplatform [since 24]
 * @atomicservice [since 11]
 * @since 6
 */
declare namespace pasteboard {
    /**
     * Maximum number of records in a **PasteData** object. In versions earlier than API version 10, the value is 512,
     * indicating that no more records can be added once the number of records reaches 512.
     *
     * Since API version 10, no limit is placed on the number of records in a **PasteData** object.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @atomicservice [since 11]
     * @since 7
     */
    const MAX_RECORD_NUM = 512;
    /**
     * MIME type of the HTML content.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @atomicservice [since 11]
     * @since 7
     */
    const MIMETYPE_TEXT_HTML = 'text/html';
    /**
     * MIME type of the Want content.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @atomicservice [since 11]
     * @since 7
     */
    const MIMETYPE_TEXT_WANT = 'text/want';
    /**
     * MIME type of the plain text content.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @atomicservice [since 11]
     * @since 7
     */
    const MIMETYPE_TEXT_PLAIN = 'text/plain';
    /**
     * MIME type of the URI content.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @atomicservice [since 11]
     * @since 7
     */
    const MIMETYPE_TEXT_URI = 'text/uri';
    /**
     * MIME type of the PixelMap content.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @atomicservice [since 11]
     * @since 9
     */
    const MIMETYPE_PIXELMAP = 'pixelMap';
    /**
     * Indicates type of value.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @unionmember { string } The value is of the string type.
     * @unionmember { image.PixelMap } The value is of the [image.PixelMap]{@link @ohos.multimedia.image:image.PixelMap} type.
     * @unionmember { Want } The value is of the [Want]{@link @ohos.app.ability.Want:Want} type.
     * @unionmember { ArrayBuffer } The value is of the **ArrayBuffer** type.
     * @crossplatform [since 24]
     * @atomicservice [since 11]
     * @since 9
     */
    type ValueType = string | image.PixelMap | Want | ArrayBuffer;
    /**
     * Creates a **PasteData** object of the HTML type.
     *
     * @param { string } htmlText - HTML content.
     * @returns { PasteData } **PasteData** object.
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @since 7
     * @deprecated since 9
     * @useinstead pasteboard.createData(mimeType: string, value: ValueType)
     */
    function createHtmlData(htmlText: string): PasteData;
    /**
     * Creates a **PasteData** object of the Want type.
     *
     * @param { Want } want - Want content.
     * @returns { PasteData } **PasteData** object.
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @since 7
     * @deprecated since 9
     * @useinstead pasteboard.createData(mimeType: string, value: ValueType)
     */
    function createWantData(want: Want): PasteData;
    /**
     * Creates a **PasteData** object of the plain text type.
     *
     * @param { string } text - Plain text.
     * @returns { PasteData } **PasteData** object.
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @since 6
     * @deprecated since 9
     * @useinstead pasteboard.createData(mimeType: string, value: ValueType)
     */
    function createPlainTextData(text: string): PasteData;
    /**
     * Creates a **PasteData** object of the URI type.
     *
     * @param { string } uri - URI content.
     * @returns { PasteData } **PasteData** object.
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @since 7
     * @deprecated since 9
     * @useinstead pasteboard.createData(mimeType: string, value: ValueType)
     */
    function createUriData(uri: string): PasteData;
    /**
     * Creates a **PasteData** object of the specified type.
     *
     * @param { string } mimeType - Type of PasteData. The value can be a predefined MIME type listed in
     *     [Constants](docroot://reference/apis-basic-services-kit/js-apis-pasteboard.md#constants), including HTML, Want,
     *     plain text, URI, and PixelMap, or a custom type. The value of **mimeType** cannot exceed 1024 bytes.
     * @param { ValueType } value - Content of PasteData.
     * @returns { PasteData } **PasteData** object.
     * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     *     3. Parameter verification failed.
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @atomicservice [since 11]
     * @since 9
     */
    function createData(mimeType: string, value: ValueType): PasteData;
    /**
     * Creates a **PasteData** object that contains multiple types of data.
     *
     * @param { Record<string, ValueType> } data - The key of **Record** can be the MIME type corresponding to the
     *     PasteData, including HTML, Want, plain text, URI, and PixelMap defined in
     *     [Constants](docroot://reference/apis-basic-services-kit/js-apis-pasteboard.md#constants). Alternatively,
     *     the key could be a custom type, whose parameter, the length of **mimeType**,
     *     cannot exceed 1024 bytes. The value of **Record** is the data corresponding to the type specified
     *     in the key. The first type specified by the key-value in **Record** is used as the default type
     *     of the first **PasteDataRecord** in the **PasteData** object. Data of non-default types can be read only by
     *     using the [getData]{@link pasteboard.PasteDataRecord.getData(type: string)} API.
     * @returns { PasteData } **PasteData** object.
     * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     *     3. Parameter verification failed.
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @since 14
     */
    function createData(data: Record<string, ValueType>): PasteData;
    /**
     * Creates a **PasteDataRecord** object of the HTML text type.
     *
     * @param { string } htmlText - HTML content.
     * @returns { PasteDataRecord } **PasteDataRecord** object of the HTML text type.
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @since 7
     * @deprecated since 9
     * @useinstead pasteboard.createRecord(mimeType: string, value: ValueType)
     */
    function createHtmlTextRecord(htmlText: string): PasteDataRecord;
    /**
     * Creates a **PasteDataRecord** object of the Want type.
     *
     * @param { Want } want - Want content.
     * @returns { PasteDataRecord } New **PasteDataRecord** object of the Want type.
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @since 7
     * @deprecated since 9
     * @useinstead pasteboard.createRecord(mimeType: string, value: ValueType)
     */
    function createWantRecord(want: Want): PasteDataRecord;
    /**
     * Creates a **PasteDataRecord** object of the plain text type.
     *
     * @param { string } text - Plain text.
     * @returns { PasteDataRecord } New **PasteDataRecord** object of the plain text type.
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @since 7
     * @deprecated since 9
     * @useinstead pasteboard.createRecord(mimeType: string, value: ValueType)
     */
    function createPlainTextRecord(text: string): PasteDataRecord;
    /**
     * Creates a **PasteDataRecord** object of the URI type.
     *
     * @param { string } uri - URI content.
     * @returns { PasteDataRecord } New **PasteDataRecord** object of the URI type.
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @since 7
     * @deprecated since 9
     * @useinstead pasteboard.createRecord(mimeType: string, value: ValueType)
     */
    function createUriRecord(uri: string): PasteDataRecord;
    /**
     * Creates a **PasteDataRecord** object of the specified type.
     *
     * @param { string } mimeType - The type of custom data. The value can be a predefined MIME type listed in
     *     [Constants](docroot://reference/apis-basic-services-kit/js-apis-pasteboard.md#constants), including HTML, Want,
     *     plain text, URI, and PixelMap, or a custom type. The value of **mimeType** cannot exceed 1024 bytes.
     * @param { ValueType } value - Data content of the specified type.
     * @returns { PasteDataRecord } A new paste data record of a specified type.
     * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types;
     *     3. Parameter verification failed.
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @atomicservice [since 11]
     * @since 9
     */
    function createRecord(mimeType: string, value: ValueType): PasteDataRecord;
    /**
     * Obtains **SystemPasteboard** object.
     *
     * @returns { SystemPasteboard } **SystemPasteboard** object.
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @atomicservice [since 11]
     * @since 6
     */
    function getSystemPasteboard(): SystemPasteboard;
    /**
     * Enumerates the pasteable ranges of PasteData.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @atomicservice [since 11]
     * @since 9
     */
    enum ShareOption {
        /**
         * Only intra-application pasting is allowed.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice [since 11]
         * @since 9
         */
        INAPP = 0,
        /**
         * Paste is allowed in any application.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice [since 11]
         * @since 9
         */
        LOCALDEVICE = 1,
        /**
         * Paste is allowed in any application across devices.
         *
         * This API is deprecated since API version 12 without any alternative API or method.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 12
         */
        CROSSDEVICE = 2
    }
    /**
     * Describes the patterns supported by the pasteboard.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @since 13
     */
    enum Pattern {
        /**
         * URL.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 13
         */
        URL = 0,
        /**
         * Number.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 13
         */
        NUMBER = 1,
        /**
         * Email address.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 13
         */
        EMAIL_ADDRESS = 2,
        /**
         * HTTP URL.
         * This API can be used only in the stage model.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @stagemodelonly
         * @since 24
         */
        HTTP_URL = 3,
        /**
         * Flight number.
         * This API can be used only in the stage model.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @stagemodelonly
         * @since 24
         */
        FLIGHT_NUMBER = 4
    }
    /**
     * Defines the properties of PasteData in the pasteboard, including the timestamp, data types, pasteable range,
     * and additional data. The defined properties can be applied to the pasteboard only with the
     * [setProperty]{@link pasteboard.PasteData.setProperty(property: PasteDataProperty)} method.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @atomicservice [since 11]
     * @since 7
     */
    interface PasteDataProperty {
        /**
         * Additional property data. It does not allow for dynamic adding of properties. Properties can be added only by re-
         * assigning values. This parameter is left empty by default. For details, see the example of **setProperty**.
         *
         * @type { object } [since 7 - 22]
         * @type { Record<string, object> } [since 23]
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        additions: Record<string, object>;
        /**
         * Data types of all records in PasteData.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        readonly mimeTypes: Array<string>;
        /**
         * Custom tag. This parameter is left empty by default.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        tag: string;
        /**
         * Timestamp when data is written to the pasteboard (unit: nanoseconds since the device is powered on).
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        readonly timestamp: number;
        /**
         * Whether the pasteboard content is for local access only. The default value is **false**. The value will be
         * overwritten by the value of the **shareOption** attribute. You are advised to use the
         * [ShareOption]{@link pasteboard.ShareOption} attribute instead.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice [since 11]
         * @since 7
         */
        localOnly: boolean;
        /**
         * Pasteable ranges of PasteData. The default value is **CROSSDEVICE**.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice [since 11]
         * @since 9
         */
        shareOption: ShareOption;
    }
    /**
     * Provides **PasteDataRecord** APIs. A **PasteDataRecord** is an abstract definition of the content in the
     * pasteboard. The pasteboard content consists of one or more plain text, HTML, URI, or Want records.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @atomicservice [since 11]
     * @since 7
     */
    interface PasteDataRecord {
        /**
         * HTML content.
         * This parameter is read-only and does not support assignment operations.
         * To assign a value, please use [createData]{@link pasteboard.createData(mimeType: string, value: ValueType)}
         * ** or ** [addEntry]{@link pasteboard.PasteDataRecord.addEntry(type: string, value: ValueType)}**
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        htmlText: string;
        /**
         * Want content.
         * This parameter is read-only and does not support assignment operations.
         * To assign a value, please use [createData]{@link pasteboard.createData(mimeType: string, value: ValueType)}
         * ** or ** [addEntry]{@link pasteboard.PasteDataRecord.addEntry(type: string, value: ValueType)}**
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        want: Want;
        /**
         * Default type of PasteDataRecord.
         * This parameter is read-only and does not support assignment operations.
         * To assign a value, please use [createData]{@link pasteboard.createData(mimeType: string, value: ValueType)}
         * ** or ** [addEntry]{@link pasteboard.PasteDataRecord.addEntry(type: string, value: ValueType)}**
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        mimeType: string;
        /**
         * Plain text.
         * This parameter is read-only and does not support assignment operations.
         * To assign a value, please use [createData]{@link pasteboard.createData(mimeType: string, value: ValueType)}
         * ** or ** [addEntry]{@link pasteboard.PasteDataRecord.addEntry(type: string, value: ValueType)}**
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        plainText: string;
        /**
         * URI content.
         * This parameter is read-only and does not support assignment operations.
         * To assign a value, please use [createData]{@link pasteboard.createData(mimeType: string, value: ValueType)}
         * ** or ** [addEntry]{@link pasteboard.PasteDataRecord.addEntry(type: string, value: ValueType)}**
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        uri: string;
        /**
         * PixelMap content.
         * This parameter is read-only and does not support assignment operations.
         * To assign a value, please use [createData]{@link pasteboard.createData(mimeType: string, value: ValueType)}
         * ** or ** [addEntry]{@link pasteboard.PasteDataRecord.addEntry(type: string, value: ValueType)}**
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        pixelMap: image.PixelMap;
        /**
         * Content of custom data.
         * This parameter is read-only and does not support assignment operations.
         * To assign a value, please use [createData]{@link pasteboard.createData(mimeType: string, value: ValueType)}
         * ** or ** [addEntry]{@link pasteboard.PasteDataRecord.addEntry(type: string, value: ValueType)}**
         *
         * @type { object } [since 9 - 22]
         * @type { Record<string, ArrayBuffer> } [since 23]
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        data: Record<string, ArrayBuffer>;
        /**
         * Forcibly converts the content in a **PasteData** object to text. This API uses an asynchronous callback to return
         *  the result.
         *
         * @param { AsyncCallback<string> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Possible causes: Incorrect parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.PasteDataRecord.toPlainText()
         */
        convertToText(callback: AsyncCallback<string>): void;
        /**
         * Forcibly converts the content in a **PasteData** object to text. This API uses a promise to return the result.
         *
         * @returns { Promise<string> } Promise used to return the text obtained from the conversion.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.PasteDataRecord.toPlainText()
         */
        convertToText(): Promise<string>;
        /**
         * Forcibly converts HTML, plain, and URI content in a **PasteDataRecord** to the plain text.
         *
         * @returns { string } Plain text.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        toPlainText(): string;
        /**
         * Adds PasteData of an extra type to **PasteDataRecord**. The type added using this method is not the
         * default type of **Record**. You can only use the
         * [getData]{@link pasteboard.PasteDataRecord.getData(type: string)} API to read the corresponding data.
         *
         * @param { string } type - Type of extra data. The value can be a predefined MIME type listed in
         *     [Constants](docroot://reference/apis-basic-services-kit/js-apis-pasteboard.md#constants),
         *     including HTML, Want, plain text, URI, and PixelMap, or a custom type.
         *     The value of **mimeType** cannot exceed 1024 bytes.
         * @param { ValueType } value - Content of extra data.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types;
         *     3. Parameter verification failed.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @since 14
         */
        addEntry(type: string, value: ValueType): void;
        /**
         * Obtains the intersection of the input types and the types of the PasteData.
         *
         * @param { Array<string> } types - List of the types.
         * @returns { Array<string> } Intersection of the input types and the types of the PasteData obtained.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types;
         *     3. Parameter verification failed.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @since 14
         */
        getValidTypes(types: Array<string>): Array<string>;
        /**
         * Obtains data of the specified type from **PasteDataRecord**.
         *
         * @param { string } type - type of PasteData, which cannot exceed 1024 bytes.
         * @returns { Promise<ValueType> } Promise used to return the data of the specified type in
         *     **PasteDataRecord**.
         *     If **PasteDataRecord** contains data of multiple types,
         *     the non-**PasteDataRecord** data of the default
         *     type can be obtained only through this API.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types;
         *     3. Parameter verification failed.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @since 14
         */
        getData(type: string): Promise<ValueType>;
    }
    /**
     * Implements a **PasteData** object. PasteData contains one or more data records (
     * [PasteDataRecord]{@link pasteboard.PasteDataRecord}) and property description objects (
     * [PasteDataProperty]{@link pasteboard.PasteDataProperty}).
     * Before calling any API in **PasteData**, you must use **
     * [createData()]{@link pasteboard.createData(mimeType: string, value: ValueType)}** or **
     * [getData()]{@link pasteboard.SystemPasteboard.getData(callback: AsyncCallback<PasteData>)}** to create a
     * **PasteData** object.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @atomicservice [since 11]
     * @since 6
     */
    interface PasteData {
        /**
         * Adds an HTML record to the PasteData, and adds **MIMETYPE_TEXT_HTML** to **mimeTypes** in
         * [PasteDataProperty]{@link pasteboard.PasteDataProperty}. The parameters cannot be empty. Otherwise, the operation
         *  fails.
         *
         * @param { string } htmlText - HTML content.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.PasteData.addRecord(mimeType: string, value: ValueType)
         */
        addHtmlRecord(htmlText: string): void;
        /**
         * Adds a Want record to the PasteData, and adds **MIMETYPE_TEXT_WANT** to **mimeTypes** in
         * [PasteDataProperty]{@link pasteboard.PasteDataProperty}. The parameters cannot be empty. Otherwise, the operation
         *  fails.
         *
         * @param { Want } want - Want object.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.PasteData.addRecord(mimeType: string, value: ValueType)
         */
        addWantRecord(want: Want): void;
        /**
         * Adds a data record to the PasteData, and adds its type to **mimeTypes** in
         * [PasteDataProperty]{@link pasteboard.PasteDataProperty}. The parameters cannot be empty. Otherwise, the operation
         *  fails.
         *
         * @param { PasteDataRecord } record - Record to add.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        addRecord(record: PasteDataRecord): void;
        /**
         * Adds a plain text record to the PasteData, and adds **MIMETYPE_TEXT_PLAIN** to **mimeTypes** in
         * [PasteDataProperty]{@link pasteboard.PasteDataProperty}. The parameters cannot be empty. Otherwise, the operation
         *  fails.
         *
         * @param { string } text - Plain text.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.PasteData.addRecord(mimeType: string, value: ValueType)
         */
        addTextRecord(text: string): void;
        /**
         * Adds a URI record to the PasteData, and adds **MIMETYPE_TEXT_URI** to **mimeTypes** in
         * [PasteDataProperty]{@link pasteboard.PasteDataProperty}. The parameters cannot be empty. Otherwise, the operation
         *  fails.
         *
         * @param { string } uri - URI content.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.PasteData.addRecord(mimeType: string, value: ValueType)
         */
        addUriRecord(uri: string): void;
        /**
         * Adds a data record to the PasteData, and adds its type to **mimeTypes** in
         * [PasteDataProperty]{@link pasteboard.PasteDataProperty}. The parameters cannot be empty. Otherwise, the operation
         *  fails.
         *
         * @param { string } mimeType - MIME type of PasteData. The length cannot exceed 1024 bytes.
         * @param { ValueType } value - Data content.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types;
         *     3. Parameter verification failed.
         * @throws { BusinessError } 12900002 - The number of records exceeds the upper limit. [since 9 - 9]
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        addRecord(mimeType: string, value: ValueType): void;
        /**
         * Obtains types of [PasteDataProperty]{@link pasteboard.PasteDataProperty} of the PasteData.
         *
         * @returns { Array<string> } Data types of the PasteData.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        getMimeTypes(): Array<string>;
        /**
         * Obtains the HTML content of the primary record.
         *
         * @returns { string } HTML content.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        getPrimaryHtml(): string;
        /**
         * Obtains the **Want** object of the primary record.
         *
         * @returns { Want } Want object.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        getPrimaryWant(): Want;
        /**
         * Obtains the data type of the primary record in the pasteboard.
         *
         * @returns { string } Data type of the primary record.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        getPrimaryMimeType(): string;
        /**
         * Obtains the plain text of the primary record.
         *
         * @returns { string } Plain text.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 6
         */
        getPrimaryText(): string;
        /**
         * Obtains the URI of the primary record.
         *
         * @returns { string } URI content.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        getPrimaryUri(): string;
        /**
         * Obtains the PixelMap of the primary record.
         *
         * @returns { image.PixelMap } PixelMap.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        getPrimaryPixelMap(): image.PixelMap;
        /**
         * Obtains the property of the PasteData.
         *
         * @returns { PasteDataProperty } Property of the PasteData.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        getProperty(): PasteDataProperty;
        /**
         * Sets a [PasteDataProperty]{@link pasteboard.PasteDataProperty} object.
         *
         * @param { PasteDataProperty } property - Property of the PasteData.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        setProperty(property: PasteDataProperty): void;
        /**
         * Obtains the record with a specific index in PasteData.
         *
         * @param { number } index - Index of the target record.
         * @returns { PasteDataRecord } Record with the specified index.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.PasteData.getRecord(index: int)
         */
        getRecordAt(index: number): PasteDataRecord;
        /**
         * Obtains the record with a specific index in PasteData.
         *
         * @param { number } index - Index of the target record.
         * @returns { PasteDataRecord } Record with the specified index.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         *     3. Parameter verification failed.
         * @throws { BusinessError } 12900001 - The index is out of the record.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        getRecord(index: number): PasteDataRecord;
        /**
         * Obtains the number of records in a PasteData object.
         *
         * @returns { number } Number of records.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        getRecordCount(): number;
        /**
         * Obtains the custom tag from the PasteData. If no custom tag is set, an empty string is returned.
         *
         * @returns { string } Custom tag. If no custom tag is set, an empty string is returned.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 7
         */
        getTag(): string;
        /**
         * Checks whether the PasteData contains data of the specified type.
         *
         * @param { string } mimeType - Type of the data to query.
         * @returns { boolean } Returns **true** if the specified data type exists; returns **false** otherwise.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.PasteData.hasType(mimeType: string)
         */
        hasMimeType(mimeType: string): boolean;
        /**
         * Checks whether the PasteData contains data of the specified MIME type.
         *
         * @param { string } mimeType - Type of the data to query. The value can be a predefined type listed in
         *     [Constants](docroot://reference/apis-basic-services-kit/js-apis-pasteboard.md#constants),
         *     including HTML, Want, plain text, URI, and PixelMap, or a custom type.
         * @returns { boolean } Returns **true** if the specified data type exists; returns **false** otherwise.
         * @throws { BusinessError } 401 - Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        hasType(mimeType: string): boolean;
        /**
         * Removes the record with a specific index in PasteData.
         *
         * @param { number } index - Specified index.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.PasteData.removeRecord(index: int)
         */
        removeRecordAt(index: number): boolean;
        /**
         * Removes the record with a specific index in PasteData.
         *
         * @param { number } index - Specified index.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         *     3. Parameter verification failed.
         * @throws { BusinessError } 12900001 - The index is out of the record.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        removeRecord(index: number): void;
        /**
         * Replaces the record with a specific index in PasteData.
         *
         * @param { number } index - Specified index.
         * @param { PasteDataRecord } record - New record.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.PasteData.replaceRecord(index: int, record: PasteDataRecord)
         */
        replaceRecordAt(index: number, record: PasteDataRecord): boolean;
        /**
         * Replaces the record with a specific index in PasteData.
         *
         * @param { number } index - Specified index.
         * @param { PasteDataRecord } record - New record.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types.
         *     3. Parameter verification failed.
         * @throws { BusinessError } 12900001 - The index is out of the record.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        replaceRecord(index: number, record: PasteDataRecord): void;
        /**
         * Notifies the pasteboard service to retain the cross-device channel before reading data from the pasteboard.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 12
         */
        pasteStart(): void;
        /**
         * Invoked to notify pasteboard service the utilization of PasteData has completed and occupied resources can be released for further usage
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 12
         */
        pasteComplete(): void;
    }
    /**
     * Enumerates options for file copy conflicts.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @atomicservice
     * @since 15
     */
    enum FileConflictOptions {
        /**
         * Overwrites the file with the same name in the destination path.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 15
         */
        OVERWRITE = 0,
        /**
         * Skips the file with the same name in the destination path. If **SKIP** is set, the copied data of the skipped
         * file is not pasted to the application.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 15
         */
        SKIP = 1
    }
    /**
     * Enumerates options for the progress indicator. You can choose whether to use the default progress indicator.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @atomicservice
     * @since 15
     */
    enum ProgressIndicator {
        /**
         * Getting data without system default progress indicator.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 15
         */
        NONE = 0,
        /**
         * Getting data with system default progress indicator.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 15
         */
        DEFAULT = 1
    }
    /**
     * Defines the progress information. This information is reported only when
     * [ProgressIndicator]{@link pasteboard.ProgressIndicator} is set to **NONE**.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @atomicservice
     * @since 15
     */
    interface ProgressInfo {
        /**
         * If the progress indicator provided by the system is not used, the system reports the progress percentage of the
         * paste task.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 15
         */
        progress: number;
    }
    /**
     * Defines a listener for progress data changes. If the default progress indicator is not used, you can set this API
     * to obtain the paste progress.
     *
     * @param { ProgressInfo } progress - Defines the progress information. This information is reported only when
     *     [ProgressIndicator]{@link pasteboard.ProgressIndicator} is set to **NONE**.
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @atomicservice
     * @since 15
     */
    type ProgressListener = (progress: ProgressInfo) => void;
    /**
     * Defines a function for canceling the paste task. This parameter is valid only when
     * [ProgressIndicator]{@link pasteboard.ProgressIndicator} is set to **NONE**.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @class ProgressSignal
     * @atomicservice
     * @since 15
     */
    export class ProgressSignal {
        /**
         * Cancels an ongoing paste task.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 15
         */
        cancel(): void;
    }
    /**
     * Defines parameters when an application obtains the Data from the pasteboard, including the
     * destination path, file conflict options, and progress indicator types.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @atomicservice
     * @since 15
     */
    interface GetDataParams {
        /**
         * Destination path for copying files. If file processing is not supported, this parameter is not required. If the
         * application involves complex file processing policies or needs to distinguish file multipathing storage, you are
         * advised not to set this parameter but let the application copy files by itself. This parameter is left empty by
         * default.
         *
         * @default -
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 15
         */
        destUri?: string;
        /**
         * File conflict options for a paste task. The default value is **OVERWRITE**.
         *
         * @default FileConflictOptions.OVERWRITE
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 15
         */
        fileConflictOptions?: FileConflictOptions;
        /**
         * Progress indicator options. You can choose whether to use the default progress indicator.
         *
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 15
         */
        progressIndicator: ProgressIndicator;
        /**
         * Defines a listener for progress data changes. If the default progress indicator is not used, you can set this
         * type to obtain the paste progress. This parameter is left empty by default.
         *
         * @default -
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 15
         */
        progressListener?: ProgressListener;
        /**
         * Function for canceling the paste task. This parameter is valid only when
         * [ProgressIndicator]{@link pasteboard.ProgressIndicator} is set to **NONE**. This parameter is left empty by
         * default.
         *
         * @default -
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 15
         */
        progressSignal?: ProgressSignal;
    }
    /**
     * Callback to be invoked when the pasteboard content changes.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @since 22
     */
    type UpdateCallback = () => void;
    /**
     * Provides **SystemPasteboard** APIs.
     * Before calling any **SystemPasteboard** API, you must obtain a **SystemPasteboard** object using
     * [getSystemPasteboard]{@link pasteboard.getSystemPasteboard()}.
     *
     * @syscap SystemCapability.MiscServices.Pasteboard
     * @crossplatform [since 24]
     * @atomicservice [since 11]
     * @since 6
     */
    interface SystemPasteboard {
        /**
         * Subscribes the content change event of the system pasteboard.
         *
         * @param { 'update' } type - Event type. The value **'update'** indicates changes in the pasteboard content.
         * @param { function } callback - Callback invoked when the pasteboard content changes.
         * @throws { BusinessError }  401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @since 7
         */
        on(type: 'update', callback: () => void): void;
        /**
         * Add a callback invoked when remote pasteboard content changes.
         *
         * @param { UpdateCallback } callback - the callback to add.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 22
         */
        onRemoteUpdate(callback: UpdateCallback): void;
        /**
         * Unsubscribes the content change event of the system pasteboard.
         *
         * @param { 'update' } type - Event type. The value **'update'** indicates changes in the pasteboard content.
         * @param { function } [callback] - the callback to remove.
         *     If this parameter is not filled in, it indicates that all callbacks for this application will be cleared.
         *     Otherwise, it indicates that the specified callback will be cleared.
         * @throws { BusinessError }  401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @since 7
         */
        off(type: 'update', callback?: () => void): void;
        /**
         * Remove a callback invoked when remote pasteboard content changes.
         *
         * @param { UpdateCallback } [callback] - the callback to remove. If this parameter is not filled in, it indicates
         *     that all callbacks for this application will be cleared. Otherwise, it indicates that the specified callback
         *     will be cleared.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 22
         */
        offRemoteUpdate(callback?: UpdateCallback): void;
        /**
         * Checks whether the data in the pasteboard is from another device.
         *
         * @returns { boolean } Returns **true** if the data in the pasteboard is from another device;
         *     returns **false** otherwise.
         * @throws { BusinessError } 12900005 - Excessive processing time for internal data.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 11
         */
        isRemoteData(): boolean;
        /**
         * Checks whether the PasteData is on a remote device. Transferring data across devices takes time. If the
         * PasteData is in a remote device, do not check for custom data types or read the PasteData on the UI
         * thread.
         *
         * @returns { boolean } Returns the check result. The value **true** indicates that the PasteData
         *     is in a remote device, and **false** indicates the opposite. Default value: **false**.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 24
         */
        hasRemoteData(): boolean;
        /**
         * Obtains the name of the application that provides data.
         *
         * @returns { string } Application name.
         * @throws { BusinessError } 12900005 - Excessive processing time for internal data.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 11
         */
        getDataSource(): string;
        /**
         * Checks whether the pasteboard contains data of the specified type.
         *
         * @param { string } mimeType - Data type.
         * @returns { boolean } Returns **true** if the pasteboard contains data of the specified type; returns **false**
         *     otherwise.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types.
         * @throws { BusinessError } 12900005 - Excessive processing time for internal data.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice
         * @since 11
         */
        hasDataType(mimeType: string): boolean;
        /**
         * Clears the system pasteboard. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.SystemPasteboard.clearData(callback: AsyncCallback<void>)
         */
        clear(callback: AsyncCallback<void>): void;
        /**
         * Clears the system pasteboard. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.SystemPasteboard.clearData()
         */
        clear(): Promise<void>;
        /**
         * Clears the system pasteboard. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        clearData(callback: AsyncCallback<void>): void;
        /**
         * Clears the system pasteboard. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        clearData(): Promise<void>;
        /**
         * Clears the system pasteboard. This API returns the result synchronously.
         *
         * @throws { BusinessError } 12900005 - Excessive processing time for internal data.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice
         * @since 11
         */
        clearDataSync(): void;
        /**
         * Obtains a **PasteData** object from the pasteboard. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<PasteData> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect  parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 6
         * @deprecated since 9
         * @useinstead pasteboard.SystemPasteboard.getData(callback: AsyncCallback<PasteData>)
         */
        getPasteData(callback: AsyncCallback<PasteData>): void;
        /**
         * Obtains a **PasteData** object from the pasteboard. This API uses a promise to return the result.
         *
         * @returns { Promise<PasteData> } Promise used to return the system PasteData.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 6
         * @deprecated since 9
         * @useinstead pasteboard.SystemPasteboard.getData()
         */
        getPasteData(): Promise<PasteData>;
        /**
         * Obtains a **PasteData** object from the pasteboard. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.READ_PASTEBOARD [since 12]
         * @param { AsyncCallback<PasteData> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect  parameters types.
         * @throws { BusinessError } 27787277 - Another copy or paste operation is in progress.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
         *     permission required to call the API. [since 12]
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        getData(callback: AsyncCallback<PasteData>): void;
        /**
         * Obtains a **PasteData** object from the pasteboard. This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_PASTEBOARD [since 12]
         * @returns { Promise<PasteData> } Promise used to return the system PasteData.
         * @throws { BusinessError } 27787277 - Another copy or paste operation is in progress.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
         *     permission required to call the API. [since 12]
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        getData(): Promise<PasteData>;
        /**
         * Obtains a **PasteData** object from the pasteboard. This API returns the result synchronously.
         *
         * @permission ohos.permission.READ_PASTEBOARD [since 12]
         * @returns { PasteData } Data in the system pasteboard.
         * @throws { BusinessError } 12900005 - Excessive processing time for internal data.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
         *     permission required to call the API. [since 12]
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice
         * @since 11
         */
        getDataSync(): PasteData;
        /**
         * Checks whether the system pasteboard contains data. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. Returns **true** if the system
         *     pasteboard contains data; returns **false** otherwise.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect  parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.SystemPasteboard.hasData(callback: AsyncCallback<boolean>)
         */
        hasPasteData(callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether the system pasteboard contains data. This API uses a promise to return the result.
         *
         * @returns { Promise<boolean> } Callback used to return the result.
         *     Returns **true** if the system pasteboard contains data; returns **false** otherwise.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 7
         * @deprecated since 9
         * @useinstead pasteboard.SystemPasteboard.hasData()
         */
        hasPasteData(): Promise<boolean>;
        /**
         * Checks whether the system pasteboard contains data. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. Returns **true** if the system
         *     pasteboard contains data; returns **false** otherwise.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect  parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        hasData(callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether the system pasteboard contains data. This API uses a promise to return the result.
         *
         * @returns { Promise<boolean> } Callback used to return the result.
         *     Returns **true** if the system pasteboard contains data; returns **false** otherwise.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        hasData(): Promise<boolean>;
        /**
         * Checks whether the system pasteboard contains data. This API returns the result synchronously.
         *
         * @returns { boolean } Callback used to return the result. Returns **true** if the system pasteboard contains data;
         *     returns **false** otherwise.
         * @throws { BusinessError } 12900005 - Excessive processing time for internal data.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice
         * @since 11
         */
        hasDataSync(): boolean;
        /**
         * Writes a **PasteData** object to the system pasteboard. This API uses an asynchronous callback to return the result.
         *
         * @param { PasteData } data - **PasteData** object.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Possible causes: 1.  Mandatory parameters are left unspecified;
         *     2. Incorrect  parameters types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 6
         * @deprecated since 9
         * @useinstead pasteboard.SystemPasteboard.setData(data: PasteData, callback: AsyncCallback<void>)
         */
        setPasteData(data: PasteData, callback: AsyncCallback<void>): void;
        /**
         * Writes a **PasteData** object to the system pasteboard. This API uses a promise to return the result.
         *
         * @param { PasteData } data - **PasteData** object.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 6
         * @deprecated since 9
         * @useinstead pasteboard.SystemPasteboard.setData(data: PasteData)
         */
        setPasteData(data: PasteData): Promise<void>;
        /**
         * Writes a **PasteData** object to the pasteboard. This API uses an asynchronous callback to return the result.
         *
         * @param { PasteData } data - **PasteData** object.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types.
         * @throws { BusinessError } 27787277 - Another copy or paste operation is in progress.
         * @throws { BusinessError } 27787278 - Replication is prohibited.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        setData(data: PasteData, callback: AsyncCallback<void>): void;
        /**
         * Writes a **PasteData** object to the system pasteboard. This API uses a promise to return the result.
         *
         * @param { PasteData } data - **PasteData** object.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect  parameters types.
         * @throws { BusinessError } 27787277 - Another copy or paste operation is in progress.
         * @throws { BusinessError } 27787278 - Replication is prohibited.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice [since 11]
         * @since 9
         */
        setData(data: PasteData): Promise<void>;
        /**
         * Writes data to the system system pasteboard. This API returns the result synchronously.
         *
         * @param { PasteData } data - Data to be written to the pasteboard.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameters types.
         * @throws { BusinessError } 12900005 - Excessive processing time for internal data.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice
         * @since 11
         */
        setDataSync(data: PasteData): void;
        /**
         * Obtains a **PasteData** object from the system pasteboard. This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_PASTEBOARD
         * @returns { Promise<unifiedDataChannel.UnifiedData> } Promise used to return the system PasteData.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
         *     permission required to call the API.
         * @throws { BusinessError } 27787277 - Another copy or paste operation is in progress.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice
         * @since 12
         */
        getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>;
        /**
         * Obtains a **UnifiedData** object from the system pasteboard. This API returns the result synchronously.
         *
         * @permission ohos.permission.READ_PASTEBOARD
         * @returns { unifiedDataChannel.UnifiedData } Data in the system pasteboard.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
         *     permission required to call the API.
         * @throws { BusinessError } 12900005 - Excessive processing time for internal data.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice
         * @since 12
         */
        getUnifiedDataSync(): unifiedDataChannel.UnifiedData;
        /**
         * Writes a **PasteData** object to the system pasteboard. This API uses a promise to return the result.
         *
         * @param { unifiedDataChannel.UnifiedData } data - Data to be written to the pasteboard.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect  parameters types.
         * @throws { BusinessError } 27787277 - Another copy or paste operation is in progress.
         * @throws { BusinessError } 27787278 - Replication is prohibited.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice
         * @since 12
         */
        setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>;
        /**
         * Writes data to the system pasteboard. This API returns the result synchronously.
         *
         * @param { unifiedDataChannel.UnifiedData } data - Data to be written to the pasteboard.
         * @throws { BusinessError } 401 - Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect  parameters types.
         * @throws { BusinessError } 12900005 - Excessive processing time for internal data.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice
         * @since 12
         */
        setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void;
        /**
         * Sets pasteable range of PasteData for application.
         *
         * @permission ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION
         * @param { ShareOption } shareOptions - Pasteable range. Only **pasteboard.ShareOption.INAPP** is allowed.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types;
         *     3. Parameter verification failed.
         * @throws { BusinessError } 12900006 - Settings already exist.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
         *     permission required to call the API.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 14
         */
        setAppShareOptions(shareOptions: ShareOption): void;
        /**
         * Deletes the global pasteable range of the application.
         *
         * @permission ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
         *     permission required to call the API.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 14
         */
        removeAppShareOptions(): void;
        /**
         * Detects [patterns]{@link pasteboard.Pattern} in the system pasteboard. This API uses a promise to return the
         * result.
         *
         * @param { Array<Pattern> } patterns - Pattern to be detected in the system pasteboard.
         * @returns { Promise<Array<Pattern>> } Promise used to return the detected patterns.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types;
         *     3. Parameter verification failed.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @since 13
         */
        detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>;
        /**
         * Obtains the types of PasteData in the system pasteboard. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<string>> } Promise used to return the types.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice
         * @since 14
         */
        getMimeTypes(): Promise<Array<string>>;
        /**
         * Obtains the number of pasteboard content changes.
         * Returns the number of pasteboard content changes if this API is called successfully; returns **0** otherwise.
         * Even though the PasteData expires, or the data becomes empty because of the called
         * [clearDataSync]{@link pasteboard.SystemPasteboard.clearDataSync()} API, the number of data changes remains.
         * When the system is restarted, or the pasteboard service is restarted due to an exception, the number of
         * PasteData changes counts from 0. In addition, copying the same data repeatedly is considered to change the
         * data for multiple times. Therefore, each time the data is copied, the number of data changes increases.
         *
         * @returns { number } The number of pasteboard content changes obtained.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @crossplatform [since 24]
         * @atomicservice
         * @since 18
         */
        getChangeCount(): number;
        /**
         * Obtains the PasteData from the system pasteboard with system progress.
         * This API uses a promise to return the result. Folders cannot be copied.
         *
         * @permission ohos.permission.READ_PASTEBOARD
         * @param { GetDataParams } params - Parameters required when an application obtains the Data from the
         * system pasteboard, including the destination path, file conflict options, and progress indicator types.
         * @returns { Promise<PasteData> } Promise used to return the system PasteData.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
         *     permission required to call the API.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 12900003 - Another copy or paste operation is in progress.
         * @throws { BusinessError } 12900007 - Invalid destUri or file system error.
         * @throws { BusinessError } 12900008 - Failed to start progress.
         * @throws { BusinessError } 12900009 - Progress exits abnormally.
         * @throws { BusinessError } 12900010 - System error occurred during paste execution.
         * @syscap SystemCapability.MiscServices.Pasteboard
         * @atomicservice
         * @since 15
         */
        getDataWithProgress(params: GetDataParams): Promise<PasteData>;
    }
}
export default pasteboard;

```
