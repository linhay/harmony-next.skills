# @ohos.convertxml.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2022 Huawei Device Co., Ltd.
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
 * @kit ArkTS
 */
/**
 * The convertxml module provides APIs for converting XML text into JavaScript objects.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 8
 */
declare namespace xml {
    /**
     * Options for conversion.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     */
    interface ConvertOptions {
        /**
         * Whether to trim the whitespace characters before and after the text. The value **true** means to trim the
         * whitespace characters before and after the text, and **false** means to keep them.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        trim: boolean;
        /**
         * Whether to ignore the XML declaration. The value **true** means to ignore the XML declaration, and **false**
         * means the opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        ignoreDeclaration?: boolean;
        /**
         * Whether to ignore the XML processing instruction. The value **true** means to ignore the XML processing
         * instruction, and **false** means the opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        ignoreInstruction?: boolean;
        /**
         * Whether to ignore the element's attribute information. The value **true** means to ignore the element's attribute
         * information, and **false** means the opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        ignoreAttributes?: boolean;
        /**
         * Whether to ignore element comments. The value **true** means to ignore element comments, and **false** means the
         * opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        ignoreComment?: boolean;
        /**
         * Whether to ignore the element's CDATA information. The value **true** means to ignore the element's CDATA
         * information, and **false** means the opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        ignoreCDATA?: boolean;
        /**
         * Whether to ignore the element's Doctype information. The value **true** means to ignore the element's Doctype
         * information, and **false** means the opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        ignoreDoctype?: boolean;
        /**
         * Whether to ignore the element's text information. The value **true** means to ignore the element's text
         * information, and **false** means the opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        ignoreText?: boolean;
        /**
         * Name of the attribute key for **declaration** in the output object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        declarationKey: string;
        /**
         * Name of the attribute key for **instruction** in the output object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        instructionKey: string;
        /**
         * Name of the attribute key for **attributes** in the output object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        attributesKey: string;
        /**
         * Name of the attribute key for **text** in the output object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        textKey: string;
        /**
         * Name of the attribute key for **cdata** in the output object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        cdataKey: string;
        /**
         * Name of the attribute key for **doctype** in the output object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        doctypeKey: string;
        /**
         * Name of the attribute key for **comment** in the output object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        commentKey: string;
        /**
         * Name of the attribute key for **parent** in the output object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        parentKey: string;
        /**
         * Name of the attribute key for **type** in the output object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        typeKey: string;
        /**
         * Name of the attribute key for **name** in the output object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        nameKey: string;
        /**
         * Name of the attribute key for **elements** in the output object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        elementsKey: string;
    }
    /**
     * ConvertXML representation refers to extensible markup language.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     */
    class ConvertXML {
        /**
         * Converts an XML text to a JavaScript object.
         *
         * @param { string } xml - Input XML text.
         * @param { ConvertOptions } options - Options for conversion. The default value is a **ConvertOptions** object,
         *     which consists of the default values of the attributes in the object.
         * @returns { Object } JavaScript object.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead xml.ConvertXML#fastConvertToJSObject
         */
        convert(xml: string, options?: ConvertOptions): Object;
        /**
         * Converts an XML text to an object of the object type.
         *
         * @param { string } xml - If the XML text to convert contains the ampersand (&), replace it with the entity
         *     reference **&amp;**.
         * @param { ConvertOptions } [options] - Options for conversion. The default value is a **ConvertOptions** object,
         *     which consists of the default values of the attributes in the object.
         * @returns { Object } JavaScript object.
         * @throws { BusinessError } 10200002 - Invalid xml string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 14
         * @useinstead xml.ConvertXML#fastConvertToJSObject
         */
        convertToJSObject(xml: string, options?: ConvertOptions): Object;
        /**
         * Converts an XML text to an object of the object type.
         *
         * > **NOTE**
         * >
         * > - This API cannot parse XML files with a large amount of data. If the text content of a single element exceeds
         * > 10 MB, an error message is displayed and an object that contains only the XML tag header will be returned.
         * >
         * > - In Windows, a newline is usually represented by the carriage return (CR) followed by the line feed (LF).
         * > However, the object obtained by calling this API uses only the LF to indicate a new line.
         *
         * @param { string } xml - XML text to convert. If the XML text contains the ampersand (&), replace it with the
         *     entity reference **&amp;**.
         * @param { ConvertOptions } [options] - Options for conversion. The default value is a **ConvertOptions** object,
         *     which consists of the default values of the attributes in the object.
         * @returns { Object } JavaScript object.
         * @throws { BusinessError } 10200002 - Invalid xml string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        fastConvertToJSObject(xml: string, options?: ConvertOptions): Object;
        /**
         * Convert XML text to JavaScript objects, this method supports parsing large XML texts
         * with a single node size exceeding 10M.
         *
         * @param { string } xml - XML text to convert. If the XML text contains the ampersand (&), replace it with the
         *     entity reference &amp;.
         * @param { ConvertOptions } [options] - Options for conversion. The default value is a ConvertOptions object,
         *     which consists of the default values of the attributes in the object.
         * @returns { Object } Returns a JavaScript object converting from XML text.
         * @throws { BusinessError } 10200002 - Invalid xml string.
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 23
         */
        largeConvertToJSObject(xml: string, options?: ConvertOptions): Object;
    }
}
export default xml;

```
