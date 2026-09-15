# @ohos.util.LightWeightSet.d.ts

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
 * LightWeightSet stores a set of values, each of which must be unique.
 * LightWeightSet is based on generics and uses a lightweight structure. Its default initial capacity is 8, and it has
 * the capacity doubled in each expansion.
 * The values in such a set are searched using hash values, which are stored in an array.
 * Compared with [HashSet]{@link @ohos.util.HashSet}, which can also store values, LightWeightSet occupies less memory.
 * **Recommended use case**: Use LightWeightSet when you need a set that has only unique elements or need to deduplicate
 * a set.
 * This topic uses the following to identify the use of generics:
 *
 * - T: Type
 *
 * > **NOTE**
 * >
 * > - Container classes, implemented in static languages, have restrictions on storage locations and properties, and do
 * > not support custom properties or methods.
 *
 * @file
 * @kit ArkTS
 */
/**
 * LightWeightSet stores a set of values, each of which must be unique.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 12]
 * @since 8
 */
declare class LightWeightSet<T> {
    /**
     * A constructor used to create a **LightWeightSet** instance.
     *
     * @throws { BusinessError } 10200012 - The LightWeightSet's constructor cannot be directly invoked.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    constructor();
    /**
     * Number of elements in a LightWeightSet.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    length: number;
    /**
     * Adds an element to this LightWeightSet.
     *
     * @param { T } obj - Target element.
     * @returns { boolean } Operation result. The value **true** is returned if the element is added; otherwise, **false**
     *     is returned.
     * @throws { BusinessError } 10200011 - The add method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    add(obj: T): boolean;
    /**
     * Adds all elements in a LightWeightSet to this LightWeightSet.
     *
     * @param { LightWeightSet<T> } set - LightWeightSet whose elements are to be added to the current LightWeightSet.
     * @returns { boolean } Operation result. The value **true** is returned if the element is added; otherwise, **false**
     *     is returned.
     * @throws { BusinessError } 10200011 - The addAll method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    addAll(set: LightWeightSet<T>): boolean;
    /**
     * Checks whether this LightWeightSet contains all elements of the specified LightWeightSet.
     *
     * @param { LightWeightSet<T> } set - **LightWeightSet** instance to be used for comparison.
     * @returns { boolean } Check result. The value **true** is returned if all the elements in the specified
     *     LightWeightSet are contained; otherwise, **false** is returned.
     * @throws { BusinessError } 10200011 - The hasAll method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    hasAll(set: LightWeightSet<T>): boolean;
    /**
     * Checks whether this LightWeightSet has the specified key.
     *
     * @param { T } key - Target key.
     * @returns { boolean } Check result. The value **true** is returned if the specified key is contained; otherwise,
     *     **false** is returned.
     * @throws { BusinessError } 10200011 - The has method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    has(key: T): boolean;
    /**
     * Checks whether the elements of this LightWeightSet are the same as those of **obj**.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 8 and deprecated since API version 12. There is no substitute API.
     *
     * @param { Object } obj - **LightWeightSet** instance to be used for comparison.
     * @returns { boolean } Returns **true** if **obj** is a LightWeightSet or an array containing only strings or numbers
     *     and the elements in them are the same; returns **false** in other cases.
     * @throws { BusinessError } 10200011 - The equal method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @since 8
     * @deprecated since 12
     */
    equal(obj: Object): boolean;
    /**
     * Increases the capacity of this LightWeightSet. If the passed-in capacity is greater than or equal to the number of
     * elements in this LightWeightSet, the capacity is changed to the new capacity. If the passed-in capacity is less
     * than the number of elements in this LightWeightSet, the capacity is not changed.
     *
     * @param { number } minimumCapacity - Minimum number of elements to accommodate in this LightWeightSet.
     * @throws { BusinessError } 10200011 - The increaseCapacityTo method cannot be bound.
     * @throws { BusinessError } 10200001 - The value of minimumCapacity is out of range.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    increaseCapacityTo(minimumCapacity: number): void;
    /**
     * Obtains the position index of the element with the specified key in this LightWeightSet.
     *
     * @param { T } key - Key of the target element.
     * @returns { number } Position index of the element. If the element does not exist, a negative value is returned. The
     *     negative value consists of a minus sign and the position where the element (if available) should be. The
     *     position starts from 1.
     * @throws { BusinessError } 10200011 - The getIndexOf method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    getIndexOf(key: T): number;
    /**
     * Removes an element of the specified key from this LightWeightSet.
     *
     * @param { T } key - Key of the target element.
     * @returns { T } Value of the element removed.
     * @throws { BusinessError } 10200011 - The remove method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    remove(key: T): T;
    /**
     * Removes the element at the specified position from this LightWeightSet.
     *
     * @param { number } index - Position index of the element. The value must be less than or equal to int32_max, that is, 2
     *     147483647.
     * @returns { boolean } Operation result. The value **true** is returned if the element is removed; otherwise,
     *     **false** is returned.
     * @throws { BusinessError } 10200011 - The removeAt method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    removeAt(index: number): boolean;
    /**
     * Clears this LightWeightSet and sets its length to **0**.
     *
     * @throws { BusinessError } 10200011 - The clear method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    clear(): void;
    /**
     * Uses a callback to traverse the elements in this LightWeightSet and obtain their position indexes.
     *
     * @param { function } callbackFn - Callback invoked to traverse the elements in the LightWeightSet.
     * @param { Object } [thisArg] - Value of **this** to use when **callbackFn** is invoked. The default value is this
     *     instance.
     * @throws { BusinessError } 10200011 - The forEach method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    forEach(callbackFn: (value?: T, key?: T, set?: LightWeightSet<T>) => void, thisArg?: Object): void;
    /**
     * returns an ES6 iterator.Each item of the iterator is a Javascript Object
     *
     * @returns { IterableIterator<T> }
     * @throws { BusinessError } 10200011 - The Symbol.iterator method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    [Symbol.iterator](): IterableIterator<T>;
    /**
     * Obtains a string that contains all elements in this LightWeightSet.
     *
     * @returns { String } String obtained.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    toString(): String;
    /**
     * Obtains an array that contains all objects in this LightWeightSet.
     *
     * @returns { Array<T> } Array obtained.
     * @throws { BusinessError } 10200011 - The toArray method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    toArray(): Array<T>;
    /**
     * Obtains the value of the element at the specified position in this LightWeightSet.
     *
     * @param { number } index - Position index of the element. The value must be less than or equal to int32_max, that is
     *     , 2147483647.
     * @returns { T } Value obtained.
     * @throws { BusinessError } 10200011 - The getValueAt method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    getValueAt(index: number): T;
    /**
     * Returns an iterator that contains all the values in this LightWeightSet.
     *
     * @returns { IterableIterator<T> } Iterator obtained.
     * @throws { BusinessError } 10200011 - The values method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    values(): IterableIterator<T>;
    /**
     * Returns an iterator that contains all the elements in this LightWeightSet.
     *
     * @returns { IterableIterator<[T, T]> } Iterator obtained.
     * @throws { BusinessError } 10200011 - The entries method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    entries(): IterableIterator<[
        T,
        T
    ]>;
    /**
     * Checks whether this LightWeightSet is empty (contains no element).
     *
     * @returns { boolean } Check result. The value **true** is returned if the LightWeightSet is empty; otherwise,
     *     **false** is returned.
     * @throws { BusinessError } 10200011 - The isEmpty method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    isEmpty(): boolean;
}
export default LightWeightSet;

```
