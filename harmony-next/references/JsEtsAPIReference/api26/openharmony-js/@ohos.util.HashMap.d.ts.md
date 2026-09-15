# @ohos.util.HashMap.d.ts

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
 * HashMap is implemented using an array, linked lists, and red-black trees as its core, supporting efficient querying,
 * insertion and deletion operations. It stores data as key-value pairs where duplicate keys are not allowed - each key
 * can only map to a single value.
 * HashMap is faster in accessing data than [TreeMap]{@link @ohos.util.TreeMap}, because the former accesses the keys
 * based on the hash codes, whereas the latter stores and accesses the keys in sorted order.
 * [HashSet]{@link @ohos.util.HashSet} is implemented based on HashMap. The input parameter of HashMap consists of
 * **key** and **value**. In HashSet, only the **value** object is processed.
 * **Recommended use case**: Use HashMap when you need to quickly access, remove, and insert key-value pairs.
 * This topic uses the following to identify the use of generics:<br>
 *
 * - K: Key<br>
 * - V: Value
 *
 * > **NOTE**
 * >
 * > Container classes, implemented in static languages, have restrictions on storage locations and properties, and do
 * > not support custom properties or methods.
 *
 * @file
 * @kit ArkTS
 */
/**
 * HashMap is a map implemented based on the array, linked list, and red-black tree. It provides efficient data query, insertion,
 * and removal. The elements in a HashMap instance are mappings of key-value pairs. Each key must be unique and have only one value.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 12]
 * @since 8
 */
declare class HashMap<K, V> {
    /**
     * A constructor used to create a **HashMap** instance.
     *
     * @throws { BusinessError } 10200012 - The HashMap's constructor cannot be directly invoked.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    constructor();
    /**
     * Number of elements in a HashMap.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    length: number;
    /**
     * Checks whether this HashMap is empty (contains no element).
     *
     * @returns { boolean } Check result. The value **true** is returned if the HashMap is empty; otherwise, **false** is
     *     returned.
     * @throws { BusinessError } 10200011 - The isEmpty method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    isEmpty(): boolean;
    /**
     * Checks whether this HashMap has the specified key.
     *
     * @param { K } key - Target key.
     * @returns { boolean } Check result. The value **true** is returned if the specified key is contained; otherwise,
     *     **false** is returned.
     * @throws { BusinessError } 10200011 - The hasKey method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    hasKey(key: K): boolean;
    /**
     * Checks whether this HashMap has the specified value.
     *
     * @param { V } value - Target value.
     * @returns { boolean } Check result. The value **true** is returned if the specified value is contained; otherwise,
     *     **false** is returned.
     * @throws { BusinessError } 10200011 - The hasValue method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    hasValue(value: V): boolean;
    /**
     * Obtains the value of the specified key in this HashMap. If nothing is obtained, **undefined** is returned.
     *
     * @param { K } key - Target key.
     * @returns { V } Value obtained.
     * @throws { BusinessError } 10200011 - The get method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    get(key: K): V;
    /**
     * Adds all elements in a **HashMap** instance to this HashMap.
     *
     * @param { HashMap<K, V> } map - **HashMap** instance whose elements are to be added to the current HashMap.
     * @throws { BusinessError } 10200011 - The setAll method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    setAll(map: HashMap<K, V>): void;
    /**
     * Adds or updates an element in this HashMap.
     *
     * @param { K } key - Key of the target element.
     * @param { V } value - Value of the target element.
     * @returns { Object } HashMap that contains the new element.
     * @throws { BusinessError } 10200011 - The set method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    set(key: K, value: V): Object;
    /**
     * Removes an element with the specified key from this HashMap.
     *
     * @param { K } key - Key of the target element.
     * @returns { V } Value of the element.
     * @throws { BusinessError } 10200011 - The remove method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    remove(key: K): V;
    /**
     * Clears this HashMap and sets its length to **0**.
     *
     * @throws { BusinessError } 10200011 - The clear method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    clear(): void;
    /**
     * Returns an iterator that contains all the keys in this HashMap.
     *
     * @returns { IterableIterator<K> } Iterator obtained.
     * @throws { BusinessError } 10200011 - The keys method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    keys(): IterableIterator<K>;
    /**
     * Returns an iterator that contains all the values in this HashMap.
     *
     * @returns { IterableIterator<V> } Iterator obtained.
     * @throws { BusinessError } 10200011 - The values method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    values(): IterableIterator<V>;
    /**
     * Replaces the value of a specified key.
     *
     * @param { K } key - Key of the target element.
     * @param { V } newValue - New value of the element.
     * @returns { boolean } Operation result. The value **true** is returned if the element is replaced; otherwise,
     *     **false** is returned.
     * @throws { BusinessError } 10200011 - The replace method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    replace(key: K, newValue: V): boolean;
    /**
     * Uses a callback to traverse each element.
     *
     * @param { function } callbackFn - Callback invoked to traverse the elements in the HashMap.
     * @param { Object } [thisArg] - Value of **this** to use when **callbackFn** is invoked. The default value is this
     *     instance.
     * @throws { BusinessError } 10200011 - The forEach method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    forEach(callbackFn: (value?: V, key?: K, map?: HashMap<K, V>) => void, thisArg?: Object): void;
    /**
     * Returns an iterator that contains all the elements in this HashMap.
     *
     * @returns { IterableIterator<[K, V]> } Iterator obtained.
     * @throws { BusinessError } 10200011 - The entries method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    entries(): IterableIterator<[
        K,
        V
    ]>;
    /**
     * Obtains an iterator, each item of which is a JavaScript object.
     *
     * @returns { IterableIterator<[K, V]> }
     * @throws { BusinessError } 10200011 - The Symbol.iterator method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    [Symbol.iterator](): IterableIterator<[
        K,
        V
    ]>;
}
export default HashMap;

```
