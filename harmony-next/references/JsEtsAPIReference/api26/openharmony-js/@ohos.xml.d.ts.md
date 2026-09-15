# @ohos.xml.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021 Huawei Device Co., Ltd.
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
import stream from './@ohos.util.stream';
/**
 * The xml module provides utilities for converting XML text to Javascript object, XML generation and parsing.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 8
 */
declare namespace xml {
    /**
     * The XmlDynamicSerializer interface is used to dynamically generate an xml file.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @name XmlDynamicSerializer
     * @atomicservice
     * @since 20
     */
    class XmlDynamicSerializer {
        /**
         * A parameterized constructor used to create a new XmlDynamicSerializer instance.
         * The input parameter is an encoding format of string type.
         *
         * @param { string } [encoding] - [encoding='utf8']  this is its encoding, only support utf-8.
         * @throws { BusinessError } 10200066 - Incorrect encoding format, only support utf-8.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        constructor(encoding?: string);
        /**
         * Write an attribute to xml element.
         *
         * @param { string } name - Key name of the attribute. Cannot be an empty string.
         * @param { string } value - Values of attribute.
         * @throws { BusinessError } 10200062 - The cumulative length of xml has exceeded the upper limit 100000.
         * @throws { BusinessError } 10200063 - Illegal position for xml.
         * @throws { BusinessError } 10200064 - Cannot be an empty string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        setAttributes(name: string, value: string): void;
        /**
         * Add an empty element.
         *
         * @param { string } name - Name of the element.
         * @throws { BusinessError } 10200062 - The cumulative length of xml has exceeded the upper limit 100000.
         * @throws { BusinessError } 10200064 - Cannot be an empty string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        addEmptyElement(name: string): void;
        /**
         * Writes xml declaration with encoding. For example: <?xml version="1.0" encoding="utf-8"?>.
         *
         * @throws { BusinessError } 10200062 - The cumulative length of xml has exceeded the upper limit 100000.
         * @throws { BusinessError } 10200063 - Illegal position for xml.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        setDeclaration(): void;
        /**
         * Writes a element start tag with the given name.
         *
         * @param { string } name - Name of the element.
         * @throws { BusinessError } 10200062 - The cumulative length of xml has exceeded the upper limit 100000.
         * @throws { BusinessError } 10200064 - Cannot be an empty string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        startElement(name: string): void;
        /**
         * Writes end tag of the element.
         *
         * @throws { BusinessError } 10200062 - The cumulative length of xml has exceeded the upper limit 100000.
         * @throws { BusinessError } 10200065 - There is no match between the startElement and the endElement.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        endElement(): void;
        /**
         * Writes the namespace of the current element tag.
         *
         * @param { string } prefix - Values name of the prefix. Cannot be an empty string.
         * @param { string } namespace - Values of namespace. Cannot be an empty string.
         * @throws { BusinessError } 10200062 - The cumulative length of xml has exceeded the upper limit 100000.
         * @throws { BusinessError } 10200064 - Cannot be an empty string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        setNamespace(prefix: string, namespace: string): void;
        /**
         * Writes the comment to xml.
         *
         * @param { string } text - Values of comment. Cannot be an empty string.
         * @throws { BusinessError } 10200062 - The cumulative length of xml has exceeded the upper limit 100000.
         * @throws { BusinessError } 10200064 - Cannot be an empty string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        setComment(text: string): void;
        /**
         * Writes the CDATA.
         *
         * @param { string } text - Values of CDATA. Cannot be an empty string.
         * @throws { BusinessError } 10200062 - The cumulative length of xml has exceeded the upper limit 100000.
         * @throws { BusinessError } 10200064 - Cannot be an empty string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        setCdata(text: string): void;
        /**
         * Writes the text to xml element.
         *
         * @param { string } text - Values of text. Cannot be an empty string.
         * @throws { BusinessError } 10200062 - The cumulative length of xml has exceeded the upper limit 100000.
         * @throws { BusinessError } 10200064 - Cannot be an empty string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        setText(text: string): void;
        /**
         * Writes the DOCTYPE.
         *
         * @param { string } text - Values of docType. Cannot be an empty string.
         * @throws { BusinessError } 10200062 - The cumulative length of xml has exceeded the upper limit 100000.
         * @throws { BusinessError } 10200064 - Cannot be an empty string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        setDocType(text: string): void;
        /**
         * Get an ArrayBuffer from a XmlDynamicSerializer instance.
         *
         * @returns { ArrayBuffer } - Returns ArrayBuffer result from a XmlDynamicSerializer instance.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        getOutput(): ArrayBuffer;
    }
    /**
     * The XmlSerializer interface is used to generate an xml file.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @name XmlSerializer
     * @atomicservice [since 11]
     * @since 8
     */
    class XmlSerializer {
        /**
         * A constructor used to create an XmlSerializer instance.
         *
         * @param { ArrayBuffer | DataView } buffer - ArrayBuffer or DataView for storing the XML information to set.
         * @param { string } [encoding] - Encoding format. The default value is 'utf-8' (the only format currently supported
         *     ).
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        constructor(buffer: ArrayBuffer | DataView, encoding?: string);
        /**
         * Sets an attribute.
         *
         * @param { string } name - Key of the attribute.
         * @param { string } value - Value of the attribute.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        setAttributes(name: string, value: string): void;
        /**
         * Adds an empty element.
         *
         * @param { string } name - Name of the empty element to add.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        addEmptyElement(name: string): void;
        /**
         * Sets a file declaration with encoding.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        setDeclaration(): void;
        /**
         * Writes the start tag based on the given element name.
         *
         * @param { string } name - Name of the element.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        startElement(name: string): void;
        /**
         * Writes the end tag of the element.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        endElement(): void;
        /**
         * Sets the namespace for an element tag.
         *
         * @param { string } prefix - Prefix of the element and its child elements.
         * @param { string } namespace - Namespace to set.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        setNamespace(prefix: string, namespace: string): void;
        /**
         * Sets a comment.
         *
         * @param { string } text - Comment to set.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        setComment(text: string): void;
        /**
         * Adds data to the CDATA tag. The structure of the generated CDATA tag is "<! <![CDATA["+ Data added + "]]>".
         *
         * @param { string } text - CDATA data to set.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        setCDATA(text: string): void;
        /**
         * Sets a tag value.
         *
         * @param { string } text - Tag value to set, which is the content of the text attribute.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        setText(text: string): void;
        /**
         * Sets a document type.
         *
         * @param { string } text - Content of DocType to set.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        setDocType(text: string): void;
    }
    /**
     * The event types represented by XML elements.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     */
    enum EventType {
        /**
         * Start a document.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        START_DOCUMENT,
        /**
         * End a document.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        END_DOCUMENT,
        /**
         * Start a tag.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        START_TAG,
        /**
         * End a tag.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        END_TAG,
        /**
         * Character data.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        TEXT,
        /**
         * A CDATA sections.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        CDSECT,
        /**
         * An XML comment.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        COMMENT,
        /**
         * An XML document type declaration.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        DOCDECL,
        /**
         * An XML processing instruction declaration.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        INSTRUCTION,
        /**
         * An entity reference.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        ENTITY_REFERENCE,
        /**
         * A whitespace.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        WHITESPACE
    }
    /**
     * The current parse info.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     */
    interface ParseInfo {
        /**
         * Obtains the current column number, starting from 1.
         *
         * @returns { number }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        getColumnNumber(): number;
        /**
         * Obtains the depth of this element.
         *
         * @returns { number }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        getDepth(): number;
        /**
         * Obtains the current line number, starting from 1.
         *
         * @returns { number }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        getLineNumber(): number;
        /**
         * Obtains the name of this element.
         *
         * @returns { string }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        getName(): string;
        /**
         * Obtains the namespace of this element.
         *
         * @returns { string }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        getNamespace(): string;
        /**
         * Obtains the prefix of this element.
         *
         * @returns { string }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        getPrefix(): string;
        /**
         * Obtains the text of the current event.
         *
         * @returns { string }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        getText(): string;
        /**
         * Checks whether the current element is empty.
         *
         * @returns { boolean }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        isEmptyElementTag(): boolean;
        /**
         * Checks whether the current event contains only whitespace characters.
         *
         * @returns { boolean }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        isWhitespace(): boolean;
        /**
         * Obtains the number of attributes for the current start tag.
         *
         * @returns { number }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        getAttributeCount(): number;
    }
    /**
     * Parse options for XmlPullParser.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     */
    interface ParseOptions {
        /**
         * Whether to parsing Doctype of the elements.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        supportDoctype?: boolean;
        /**
         * Whether to ignore parsing texts of the elements.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        ignoreNameSpace?: boolean;
        /**
         * Tag value callback function.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        tagValueCallbackFunction?: (name: string, value: string) => boolean;
        /**
         * Attribute value callback function.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        attributeValueCallbackFunction?: (name: string, value: string) => boolean;
        /**
         * Attribute value and tag callback function.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        attributeWithTagCallbackFunction?: AttributeWithTagCb;
        /**
         * Token value callback function.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        tokenValueCallbackFunction?: (eventType: EventType, value: ParseInfo) => boolean;
    }
    /**
     * The type of ParseOptions attributeWithTagCallbackFunction.
     *
     * @param { string } tagName - The tag in xml parse node
     * @param { string } key - The key in xml parse node
     * @param { string } value - The value in xml parse node
     * @returns { boolean } - whether continue to parse xml data
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 22]
     * @atomicservice
     * @since 20
     */
    type AttributeWithTagCb = (tagName: string, key: string, value: string) => boolean;
    /**
     * The XmlPullParser interface is used to parse the existing xml file.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @name XmlPullParser
     * @atomicservice [since 11]
     * @since 8
     */
    class XmlPullParser {
        /**
         * Creates and returns an XmlPullParser object.
         *
         * @param { ArrayBuffer | DataView } buffer - A instance, the new XmlPullParser with.
         * @param { string } [encoding] - [encoding='utf8']  this is its encoding.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        constructor(buffer: ArrayBuffer | DataView, encoding?: string);
        /**
         * Starts parsing the XML file.
         *
         * @param { ParseOptions } option - Parse options for XmlPullParser, the interface including
         *     two Boolean variables and three callback functions.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         * @deprecated since 14
         * @useinstead ohos.xml.XmlPullParser.parseXml
         */
        parse(option: ParseOptions): void;
        /**
         * Parses XML information.
         *
         * @param { ParseOptions } option - XML parsing options.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        parseXml(option: ParseOptions): void;
    }
    /**
     * The XmlSAXParser provides the capability of parsing XML in a streaming manner.
     *
     * @syscap SystemCapability.Utils.Lang
     * @stagemodelonly
     * @crossplatform
     * @name XmlSAXParser
     * @atomicservice
     * @since 24
     */
    class XmlSAXParser {
        /**
         * Creates and returns an XmlSAXParser instance.
         *
         * @param { stream.Readable } inputStream - An instance, of stream.Readable for the new XmlSAXParser.
         * @param { string } [encoding] - [encoding='utf8']  this is its encoding.
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 24
         */
        constructor(inputStream: stream.Readable, encoding?: string);
        /**
         * Creates and returns an XmlSAXParser instance.
         *
         * @param { XmlSAXHandler } xmlSAXHandler - The simple API for XML handler.
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 24
         */
        parse(xmlSAXHandler: XmlSAXHandler): void;
    }
    /**
     * A simple API for XML handling
     *
     * @syscap SystemCapability.Utils.Lang
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 24
     */
    interface XmlSAXHandler {
        /**
         * CallBack function triggered at the beginning of the document
         *
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 24
         */
        startDocument(): void;
        /**
         * CallBack function triggered at the end of the document
         *
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 24
         */
        endDocument(): void;
        /**
         * CallBack function triggered at the beginning of the element
         *
         * @param { string } elementName - Name of the element
         * @param { string | undefined } namespaceURI - URI of the namespace
         * @param { string | undefined } qName - Fully qualified name with namespace
         * @param { Map<string,string> } attributes - attributes mapping
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 24
         */
        startElement(elementName: string, namespaceURI: string | undefined, qName: string | undefined, attributes: Map<string, string>): void;
        /**
         * CallBack function triggered at the end of the element
         *
         * @param { string } elementName - Name of the element
         * @param { string | undefined } namespaceURI - URI of the namespace
         * @param { string | undefined } qName - Fully qualified name with namespace
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 24
         */
        endElement(elementName: string, namespaceURI: string | undefined, qName: string | undefined): void;
        /**
         * CallBack function triggered by the text content
         *
         * @param { string } content - literal content
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 24
         */
        characters(content: string): void;
    }
}
export default xml;

```
