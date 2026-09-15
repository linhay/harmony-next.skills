# @ohos.util.PlainArray.d.ts

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
 * PlainArray stores key-value (KV) pairs. Each key must be unique, be of the number type, and have only one value.
 * PlainArray is based on generics and uses a lightweight structure. Keys in the array are searched using binary search
 * and are mapped to values in other arrays.
 * Both PlainArray and [LightWeightMap]{@link @ohos.util.LightWeightMap} are used to store KV pairs in the lightweight
 * structure. However, the keys of PlainArray can only be of the number type.
 * **Recommended use case**: Use PlainArray when you need to store KV pairs whose keys are of the **number** type.
 * This topic uses the following to identify the use of generics:
 *
 * - T: Type
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
 * PlainArray stores key-value (KV) pairs. Each key must be unique, be of the number type, and have only one value.
 * PlainArray is based on generics and uses a lightweight structure.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 12]
 * @since 8
 */
declare class PlainArray<T> {
    /**
     * A constructor used to create a **PlainArray** instance.
     *
     * @throws { BusinessError } 10200012 - The PlainArray's constructor cannot be directly invoked.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    constructor();
    /**
     * Number of elements in a PlainArray.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    length: number;
    /**
     * Adds an element to this PlainArray.
     *
     * @param { number } key - Key of the target element. The value must be less than or equal to int32_max, that is, 2147483
     *     647.
     * @param { T } value - Value of the target element.
     * @throws { BusinessError } 10200011 - The add method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    add(key: number, value: T): void;
    /**
     * Clears this PlainArray and sets its length to **0**.
     *
     * @throws { BusinessError } 10200011 - The clear method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    clear(): void;
    /**
     * Clones this PlainArray and returns a copy. The modification to the copy does not affect the original instance.
     *
     * @returns { PlainArray<T> } New **PlainArray** instance obtained.
     * @throws { BusinessError } 10200011 - The clone method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    clone(): PlainArray<T>;
    /**
     * Checks whether PlainArray has the specified key.
     *
     * @param { number } key - Target key. The value must be less than or equal to int32_max, that is, 2147483647.
     * @returns { boolean } Check result. The value **true** is returned if the specified key is contained; otherwise,
     *     **false** is returned.
     * @throws { BusinessError } 10200011 - The has method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    has(key: number): boolean;
    /**
     * Obtains the value of the specified key in this PlainArray.
     *
     * @param { number } key - Target key. The value must be less than or equal to int32_max, that is, 2147483647.
     * @returns { T } Value of the key.
     * @throws { BusinessError } 10200011 - The get method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    get(key: number): T;
    /**
     * Obtains the index of the element with the specified key in this PlainArray.
     *
     * @param { number } key - Target key. The value must be less than or equal to int32_max, that is, 2147483647.
     * @returns { number } Index of the element. If no match is found, **-1** is returned.
     * @throws { BusinessError } 10200011 - The getIndexOfKey method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    getIndexOfKey(key: number): number;
    /**
     * Obtains the index of the first occurrence of an element with the specified value in this PlainArray.
     *
     * @param { T } value - Value of the target element.
     * @returns { number } Index of the element. If no match is found, **-1** is returned.
     * @throws { BusinessError } 10200011 - The getIndexOfValue method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    getIndexOfValue(value: T): number;
    /**
     * Checks whether this PlainArray is empty.
     *
     * @returns { boolean } Check result. The value **true** is returned if the PlainArray is empty; otherwise, **false**
     *     is returned.
     * @throws { BusinessError } 10200011 - The isEmpty method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    isEmpty(): boolean;
    /**
     * Obtains the key of the element at the specified position in this PlainArray.
     *
     * @param { number } index - Position index of the target element. The value must be less than or equal to int32_max,
     *     that is, 2147483647.
     * @returns { number } Key of the element. If no match is found, **-1** is returned.
     * @throws { BusinessError } 10200011 - The getKeyAt method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    getKeyAt(index: number): number;
    /**
     * Removes a key-value pair with the specified key.
     *
     * @param { number } key - Target key. The value must be less than or equal to int32_max, that is, 2147483647.
     * @returns { T } Value in the key-value pair removed.
     * @throws { BusinessError } 10200011 - The remove method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    remove(key: number): T;
    /**
     * Removes an element at the specified position from this PlainArray.
     *
     * @param { number } index - Position index of the target element. The value must be less than or equal to int32_max,
     *     that is, 2147483647.
     * @returns { T } Element removed.
     * @throws { BusinessError } 10200011 - The removeAt method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    removeAt(index: number): T;
    /**
     * Removes elements within the specified range.
     *
     * @param { number } index - Start position of the elements to remove. The value must be less than or equal to int32_max,
     *     that is, 2147483647.
     * @param { number } size - Number of elements to remove. The value must be less than or equal to int32_max, that is, 214
     *     7483647.
     * @returns { number } Number of elements removed.
     * @throws { BusinessError } 10200011 - The removeRangeFrom method cannot be bound.
     * @throws { BusinessError } 10200001 - The value of index is out of range.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    removeRangeFrom(index: number, size: number): number;
    /**
     * Sets a value for an element at the specified position in this PlainArray.
     *
     * @param { number } index - Position index of the target element. The value must be less than or equal to int32_max,
     *     that is, 2147483647.
     * @param { T } value - Value of the target element.
     * @throws { BusinessError } 10200011 - The setValueAt method cannot be bound.
     * @throws { BusinessError } 10200001 - The value of index is out of range.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    setValueAt(index: number, value: T): void;
    /**
     * Obtains a string that contains all elements in this PlainArray.
     *
     * @returns { String } String obtained.
     * @throws { BusinessError } 10200011 - The toString method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    toString(): String;
    /**
     * Obtains the value of an element at the specified position in this PlainArray.
     *
     * @param { number } index - Position index of the target element. The value must be less than or equal to int32_max,
     *     that is, 2147483647.
     * @returns { T } Value of the element. If no match is found, **undefined** is returned.
     * @throws { BusinessError } 10200011 - The getValueAt method cannot be bound.
     * @throws { BusinessError } 10200001 - The value of index is out of range.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    getValueAt(index: number): T;
    /**
     * Uses a callback to traverse each element in the **PlainArray** instance.
     *
     * @param { function } callbackFn - Callback invoked to traverse the elements in the PlainArray.
     * @param { Object } [thisArg] - Value of **this** to use when **callbackFn** is invoked. The default value is this
     *     instance.
     * @throws { BusinessError } 10200011 - The forEach method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    forEach(callbackFn: (value: T, index?: number, PlainArray?: PlainArray<T>) => void, thisArg?: Object): void;
    /**
     * returns an iterator.Each item of the iterator is a Javascript Object
     *
     * @returns { IterableIterator<[ number, T ]> }
     * @throws { BusinessError } 10200011 - The Symbol.iterator method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    [Symbol.iterator](): IterableIterator<[
        number,
        T
    ]>;
}
export default PlainArray;

```
