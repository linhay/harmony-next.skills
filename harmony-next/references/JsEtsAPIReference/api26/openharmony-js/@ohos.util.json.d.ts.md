# @ohos.util.json.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
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
 * The JSON module provides a series of APIs for converting JSON text into JSON objects or values and converting objects
 * into JSON text.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform
 * @atomicservice
 * @since 12
 */
declare namespace json {
    /**
     * Defines the type of the conversion result function.
     *
     * When used as a parameter of [JSON.parse]{@link json.parse}, the function is called by each member of the object,
     * allowing for custom data processing or conversion during parsing.
     *
     * When used as a parameter of
     * [JSON.stringify]{@link json.stringify(value: Object, replacer?: Transformer, space?: string | number)}, the
     * function is used to transfer and handle each property during serialization.
     *
     * @param { Object } this - Object to which the key-value pair to parse belongs.
     * @param { string } key - Key to parse.
     * @param { Object } value - Value of the key.
     * @returns { Object | undefined | null } Return an Object, undefined or null value
     * @syscap SystemCapability.Utils.Lang
     * @atomicservice
     * @since 12
     */
    type Transformer = (this: Object, key: string, value: Object) => Object | undefined | null;
    /**
     * Parses a JSON string into an ArkTS object or null.
     *
     * @param { string } text - Valid JSON string.
     * @param { Transformer } [reviver] - Conversion function. This parameter can be used to modify the value generated
     *     after parsing. The default value is undefined.
     * @param {ParseOptions} options - Parsing options. This parameter is used to control the type of the parsing result.
     *     The default value is undefined.
     * @returns { Object | null } Return an Object, array, string, number, boolean, or null value corresponding to JSON
     *     text.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null;
    /**
     * Converts an ArkTS object or array into a JSON string. In the case of a container, linear containers are supported,
     * but non-linear containers are not.
     *
     * @param { Object } value - ArkTS object or array. In the case of a container, linear containers are supported, but
     *     non-linear containers are not.
     * @param { (number | string)[] | null } [replacer] - If an array is passed in, only the keys in the array are
     *     serialized to the final JSON string. If null is passed in, all keys of the object are serialized. The default
     *     value is undefined.
     * @param { string | number } [space] - White spaces or strings inserted into the output JSON string for readability
     *     purposes. If the parameter is a number, it represents the number of indentation spaces; if it is a string, it
     *     represents the indentation characters. If no parameter is provided, there will be no indentation. The default
     *     value is an empty string.
     * @returns { string } Return a JSON text.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function stringify(value: Object, replacer?: (number | string)[] | null, space?: string | number): string;
    /**
     * Converts an ArkTS object or array into a JSON string. In the case of a container, linear containers are supported,
     * but non-linear containers are not.
     *
     * @param { Object } value - ArkTS object or array. In the case of a container, linear containers are supported, but
     *     non-linear containers are not.
     * @param { Transformer } [replacer] - During serialization, each key of the serialized value is converted and
     *     processed by this function. The default value is undefined.
     * @param { string | number } [space] - Indentation, white space, or line break characters inserted into the output
     *     JSON string for readability purposes. If a number is passed in, it indicates the number of space characters to
     *     be used as indentation. If a string is passed in, the string is inserted before the output JSON string. If null
     *     is passed in, no white space is used. The default value is an empty string.
     * @returns { string } Return a JSON text.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function stringify(value: Object, replacer?: Transformer, space?: string | number): string;
    /**
     * Checks whether an ArkTS object contains a key. This API can be used for related operations after
     * [JSON.parse]{@link json.parse} is called to parse a JSON string. This API supports only valid JSON strings whose
     * outermost layer is in dictionary format (in braces instead of square brackets).
     *
     * @param { object } obj - ArkTS object.
     * @param { string } property - Key to check.
     * @returns { boolean } Return true if the key is in the object, otherwise return false.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function has(obj: object, property: string): boolean;
    /**
     * Removes a key from an ArkTS object. This API can be used for related operations after
     * [JSON.parse]{@link json.parse} is called to parse a JSON string. This API supports only valid JSON strings whose
     * outermost layer is in dictionary format (in braces instead of square brackets).
     *
     * @param { object } obj - ArkTS object.
     * @param { string } property - Key to remove.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function remove(obj: object, property: string): void;
    /**
     * Enumerates the modes for processing BigInt.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    const enum BigIntMode {
        /**
         * BigInt is not supported.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        DEFAULT = 0,
        /**
         * Parses an integer that is less than -(2^53-1) or greater than (2^53-1) as BigInt.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        PARSE_AS_BIGINT = 1,
        /**
         * Parses all integers as BigInt.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ALWAYS_PARSE_AS_BIGINT = 2
    }
    /**
     * Describes the parsing options, which can define the mode for processing BigInt.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    interface ParseOptions {
        /**
         * Mode for processing BigInt.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        bigIntMode: BigIntMode;
    }
}
export default json;

```
