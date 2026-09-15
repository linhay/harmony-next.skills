# @ohos.url.d.ts

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
 * The url module provides APIs for parsing URL strings and constructing URL instances to process URL strings.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 7
 */
declare namespace url {
    /**
     * The URLSearchParams interface defines some practical methods to process URL query strings.
     *
     * @syscap SystemCapability.Utils.Lang
     * @name URLSearchParams
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.url.URLParams
     */
    class URLSearchParams {
        /**
         * A parameterized constructor used to create an URLSearchParams instance.
         * As the input parameter of the constructor function, init supports four types.
         * The input parameter is a character string two-dimensional array.
         * The input parameter is the object list.
         * The input parameter is a character string.
         * The input parameter is the URLSearchParams object.
         *
         * @param { string[][] | Record<string, string> | string | URLSearchParams } init - init init
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.constructor
         */
        constructor(init?: string[][] | Record<string, string> | string | URLSearchParams);
        /**
         * Appends a specified key/value pair as a new search parameter.
         *
         * @param { string } name - The key name of the search parameter to insert
         * @param { string } value - The value of the search parameter to insert
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.append
         */
        append(name: string, value: string): void;
        /**
         * Deletes the given search parameter and its associated value,from the list of all search parameters.
         *
         * @param { string } name - The name of the key-value pair to delete
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.delete
         */
        delete(name: string): void;
        /**
         * Returns all key-value pairs associated with a given search parameter as an array.
         *
         * @param { string } name - The name of the key-value pairs to retrieve
         * @returns { string[] } Returns all key-value pairs with the specified name
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.getAll
         */
        getAll(name: string): string[];
        /**
         * Returns an ES6 iterator. Each item of the iterator is a JavaScript Array.
         * The first item of Array is name, and the second item of Array is value.
         *
         * @returns { IterableIterator<[string, string]> } Returns an iterator for ES6.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.entries
         */
        entries(): IterableIterator<[
            string,
            string
        ]>;
        /**
         * Callback functions are used to traverse key-value pairs on the URLSearchParams instance object.
         *
         * @param { function } callbackFn - The callback function to execute for each key-value pair
         * @param { Object } thisArg - The value to use as this when executing callbackFn
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.forEach
         */
        forEach(callbackFn: (value: string, key: string, searchParams: URLSearchParams) => void, thisArg?: Object): void;
        /**
         * Returns the first value associated to the given search parameter.
         *
         * @param { string } name - The name of the key-value pair to get
         * @returns { string | null } Returns the first value found by name. If no value is found, null is returned.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.get
         */
        get(name: string): string | null;
        /**
         * Returns a Boolean that indicates whether a parameter with the specified name exists.
         *
         * @param { string } name - The name of the key-value pair to check
         * @returns { boolean } Returns a Boolean value that indicates whether a found
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.has
         */
        has(name: string): boolean;
        /**
         * Sets the value associated with a given search parameter to the
         * given value. If there were several matching values, this method
         * deletes the others. If the search parameter doesn't exist, this
         * method creates it.
         *
         * @param { string } name - The key name of the parameter to set
         * @param { string } value - The value to set for the parameter
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.set
         */
        set(name: string, value: string): void;
        /**
         * Sort all key/value pairs contained in this object in place and return undefined.
         *
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.sort
         */
        sort(): void;
        /**
         * Returns an iterator allowing to go through all keys contained in this object.
         *
         * @returns { IterableIterator<string> } Returns an ES6 Iterator over the names of each name-value pair.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.keys
         */
        keys(): IterableIterator<string>;
        /**
         * Returns an iterator allowing to go through all values contained in this object.
         *
         * @returns { IterableIterator<string> } Returns an ES6 Iterator over the values of each name-value pair.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.values
         */
        values(): IterableIterator<string>;
        /**
         * Returns an iterator allowing to go through all key/value
         * pairs contained in this object.
         *
         * @returns { IterableIterator<[string, string]> } Returns an ES6 iterator. Each item of the iterator is a
         *     JavaScript Array.
         *     The first item of Array is name, and the second item of Array is value.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.[Symbol.iterator]
         */
        [Symbol.iterator](): IterableIterator<[
            string,
            string
        ]>;
        /**
         * Returns a query string suitable for use in a URL.
         *
         * @returns { string } Returns a search parameter serialized as a string, percent-encoded if necessary.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URLParams.toString
         */
        toString(): string;
    }
    /**
     * The URLParams interface defines some practical methods to process URL query strings.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @name URLParams
     * @atomicservice [since 11]
     * @since 9
     */
    class URLParams {
        /**
         * A constructor used to create a URLParams instance.
         *
         * @param { string[][] | Record<string, string> | string | URLParams } [init] - Input parameter objects, which
         *     include the following:
         *     - string[][]: two-dimensional string array.
         *     - Record<string, string>: list of objects.
         *     - string: string.
         *     - URLParams: object.
         *     The default value is null.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        constructor(init?: string[][] | Record<string, string> | string | URLParams);
        /**
         * Appends a key-value pair into the query string.
         *
         * @param { string } name - Key of the key-value pair to append.
         * @param { string } value - Value of the key-value pair to append.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        append(name: string, value: string): void;
        /**
         * Deletes key-value pairs of the specified key.
         *
         * @param { string } name - Key of the key-value pairs to delete.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        delete(name: string): void;
        /**
         * Obtains all the values based on the specified key.
         *
         * @param { string } name - Target key.
         * @returns { string[] } string[] Returns all key-value pairs with the specified name.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getAll(name: string): string[];
        /**
         * Obtains an ES6 iterator. Each item of the iterator is a JavaScript array, and the first and second fields of
         * each array are the key and value respectively.
         *
         * @returns { IterableIterator<[string, string]> } Returns an iterator for ES6.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        entries(): IterableIterator<[
            string,
            string
        ]>;
        /**
         * Callback functions are used to traverse key-value pairs on the URLParams instance object.
         *
         * @param { function } callbackFn - callbackFn value Current traversal key value,
         *     key Indicates the name of the key that is traversed.
         * @param { Object } [thisArg] - thisArg to be used as this value for when callbackFn is called
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        forEach(callbackFn: (value: string, key: string, searchParams: URLParams) => void, thisArg?: Object): void;
        /**
         * Obtains the value of the first key-value pair based on the specified key.
         *
         * @param { string } name - Key specified to obtain the value.
         * @returns { string | null } Returns the first value found by name. If no value is found, null is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        get(name: string): string | null;
        /**
         * Checks whether a key has a value.
         *
         * @param { string } name - Key specified to search for its value.
         * @returns { boolean } Returns a Boolean value that indicates whether a found
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        has(name: string): boolean;
        /**
         * Sets the value for a key. If key-value pairs matching the specified key exist, the value of the first key-
         * value
         * pair will be set to the specified value and other key-value pairs will be deleted. Otherwise, the key-value
         * pair
         * will be appended to the query string.
         *
         * @param { string } name - Key of the value to set.
         * @param { string } value - Value to set.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        set(name: string, value: string): void;
        /**
         * Sorts all key-value pairs contained in this object based on the Unicode code points of the keys and returns
         * undefined. This method uses a stable sorting algorithm, that is, the relative order between key-value pairs
         * with equal keys is retained.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        sort(): void;
        /**
         * Obtains an ES6 iterator that contains the keys of all the key-value pairs.
         *
         * @returns { IterableIterator<string> } Returns an ES6 Iterator over the names of each name-value pair.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        keys(): IterableIterator<string>;
        /**
         * Obtains an ES6 iterator that contains the values of all the key-value pairs.
         *
         * @returns { IterableIterator<string> } Returns an ES6 Iterator over the values of each name-value pair.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        values(): IterableIterator<string>;
        /**
         * Obtains an ES6 iterator. Each item of the iterator is a JavaScript array, and the first and second fields
         * ofeach array are
         * the key and value respectively.
         *
         * @returns { IterableIterator<[string, string]> } Returns an ES6 iterator. Each item of the iterator is a
         *     JavaScript Array.
         *     The first item of Array is name, and the second item of Array is value.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        [Symbol.iterator](): IterableIterator<[
            string,
            string
        ]>;
        /**
         * Obtains search parameters that are serialized as a string and, if necessary, percent-encodes the characters
         * in the string.
         *
         * @returns { string } Returns a search parameter serialized as a string, percent-encoded if necessary.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        toString(): string;
    }
    /**
     * The interface of URL is used to parse, construct, normalize, and encode URLs.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @name URL
     * @atomicservice [since 11]
     * @since 7
     */
    class URL {
        /**
         * URL constructor, which is used to instantiate a URL object.
         * url: Absolute or relative input URL to resolve. Base is required if input is relative.
         * If input is an absolute value, base ignores the value.
         * base: Base URL to parse if input is not absolute.
         *
         * @param { string } url - url url
         * @param { string | URL } base - base base
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URL.parseURL
         */
        constructor(url: string, base?: string | URL);
        /**
         * A no-argument constructor used to create a URL. It returns a URL object after parseURL is called.
         * It is not used independently.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        constructor();
        /**
         * Parses a URL.
         *
         * @param { string } url - A string representing an absolute or a relative URL.
         *     In the case of a relative URL, you must specify base to parse the final URL.
         *     In the case of an absolute URL, the passed base will be ignored.
         * @param { string | URL } [base] - Either a string or an object. The default value is undefined.
         *     - string: string.
         *     - URL: URL object.
         *     This parameter is used when url is a relative URL.
         * @returns { URL }
         * @throws { BusinessError } 10200002 - Invalid url string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        static parseURL(url: string, base?: string | URL): URL;
        /**
         * Converts the parsed URL into a string.
         *
         * @returns { string } Returns the serialized URL as a string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        toString(): string;
        /**
         * Converts the parsed URL into a JSON string.
         *
         * @returns { string } Returns the serialized URL as a string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        toJSON(): string;
        /**
         * Gets and sets the fragment portion of the URL.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        hash: string;
        /**
         * Gets and sets the host portion of the URL.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        host: string;
        /**
         * Gets and sets the host name portion of the URL，not include the port.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        hostname: string;
        /**
         * Gets and sets the serialized URL.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        href: string;
        /**
         * Gets the read-only serialization of the URL's origin.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        readonly origin: string;
        /**
         * Gets and sets the password portion of the URL.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        password: string;
        /**
         * Gets and sets the path portion of the URL.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        pathname: string;
        /**
         * Gets and sets the port portion of the URL.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        port: string;
        /**
         * Gets and sets the protocol portion of the URL.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        protocol: string;
        /**
         * Gets and sets the serialized query portion of the URL.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        search: string;
        /**
         * Gets the URLSearchParams object that represents the URL query parameter.
         * This property is read-only, but URLSearchParams provides an object that can be used to change
         * the URL instance. To replace the entire query parameter for a URL, use url.searchsetter.
         *
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.url.URL.params
         */
        readonly searchParams: URLSearchParams;
        /**
         * Gets the URLParams object that represents the URL query parameter.
         * This property is read-only, but URLParams provides an object that can be used to change
         * the URL instance. To replace the entire query parameter for a URL, use url.searchsetter.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readonly params: URLParams;
        /**
         * Gets and sets the username portion of the URL.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        username: string;
    }
}
export default url;

```
