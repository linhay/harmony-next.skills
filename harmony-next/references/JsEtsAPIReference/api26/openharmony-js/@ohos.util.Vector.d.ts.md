# @ohos.util.Vector.d.ts

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
 * Vector is a linear data structure that is implemented based on arrays. When the memory of a vector is used up, a
 * larger contiguous memory area is automatically allocated, all the elements are copied to the new memory area, and the
 * current memory area is reclaimed. Vector can be used to efficiently access elements.
 * Both Vector and [ArrayList]{@link @ohos.util.ArrayList} are implemented based on arrays, but Vector provides more
 * interfaces for operating the arrays. Both of them can dynamically adjust the capacity. Vector doubles the capacity
 * each time, whereas ArrayList increases the capacity by 50%.
 * **Recommended use case**: Use Vector when the data volume is large.
 * This topic uses the following to identify the use of generics:
 *
 * - T: Type
 *
 * > **NOTE**
 * >
 * > - The APIs provided by this module are deprecated since API version 9. You are advised to use
 * > [@ohos.util.ArrayList]{@link @ohos.util.ArrayList}.
 *
 * @syscap SystemCapability.Utils.Lang
 * @since 8
 * @deprecated since 9
 * @useinstead ohos.util.ArrayList
 */
declare class Vector<T> {
    /**
     * A constructor used to create a **Vector** instance.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    constructor();
    /**
     * Number of elements in a Vector.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    length: number;
    /**
     * Adds an element at the end of this Vector.
     *
     * @param { T } element - Target element.
     * @returns { boolean } Operation result. The value **true** is returned if the element is added; otherwise, **false**
     *     is returned.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    add(element: T): boolean;
    /**
     * Inserts an element within the length range and moves its subsequent elements rightwards.
     *
     * @param { T } element - Target element.
     * @param { number } index - Index of the position where the element is to be inserted.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    insert(element: T, index: number): void;
    /**
     * Checks whether this Vector has the specified element.
     *
     * @param { T } element - Target element.
     * @returns { boolean } Check result. The value **true** is returned if the Vector has the specified element;
     *     otherwise, **false** is returned.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    has(element: T): boolean;
    /**
     * Obtains an element at the specified position in this Vector.
     *
     * @param { number } index - Position index of the target element.
     * @returns { T } Element obtained.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    get(index: number): T;
    /**
     * Obtains the index of the first occurrence of the specified element in this Vector.
     *
     * @param { T } element - Target element.
     * @returns { number } Index of the element. If no match is found, **-1** is returned.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    getIndexOf(element: T): number;
    /**
     * Obtains the first element in this Vector.
     *
     * @returns { T } The first element obtained.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    getFirstElement(): T;
    /**
     * Obtains the last element in this Vector.
     *
     * @returns { T } The last element obtained.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    getLastElement(): T;
    /**
     * Searches for an element based on its index, removes the element after returning it, and moves its subsequent
     * elements leftwards.
     *
     * @param { number } index - Position index of the target element.
     * @returns { T } Element removed. If the Vector is empty, **undefined** is returned. If the index is out of range, an
     *     exception is thrown.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    removeByIndex(index: number): T;
    /**
     * Removes the first occurrence of the specified element from this Vector.
     *
     * @param { T } element - Target element.
     * @returns { boolean } Operation result. The value **true** is returned if the element is removed; otherwise,
     *     **false** is returned.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    remove(element: T): boolean;
    /**
     * Replaces an element at the specified position in this Vector with a given element.
     *
     * @param { number } index - Position index of the target element.
     * @param { T } element - Element to be used for replacement.
     * @returns { T } New element.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    set(index: number, element: T): T;
    /**
     * Obtains the index of the last occurrence of the specified element in this Vector.
     *
     * @param { T } element - Target element.
     * @returns { number } Index of the element. If no match is found, **-1** is returned.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    getLastIndexOf(element: T): number;
    /**
     * Searches for an element backward from the specified position index and returns the position index of the element.
     *
     * @param { T } element - Target element.
     * @param { number } index - Position index where the search starts.
     * @returns { number } Index of the element. If no match is found, **-1** is returned.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    getLastIndexFrom(element: T, index: number): number;
    /**
     * Searches for an element forward from the specified position index and returns the position index of the element.
     *
     * @param { T } element - Target element.
     * @param { number } index - Position index where the search starts.
     * @returns { number } Index of the element. If no match is found, **-1** is returned.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    getIndexFrom(element: T, index: number): number;
    /**
     * Removes from this Vector all of the elements within a range, including the element at the start position but not
     * that at the end position.
     *
     * @param { number } fromIndex - Index of the start position.
     * @param { number } toIndex - Index of the end position.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    removeByRange(fromIndex: number, toIndex: number): void;
    /**
     * Replaces all elements in this Vector with new elements, and returns the new ones.
     *
     * @param { function } callbackFn - Callback invoked for replacement.
     * @param { Object } thisArg - Value of **this** to use when **callbackFn** is invoked. The default value is this
     *     instance.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    replaceAllElements(callbackFn: (value: T, index?: number, vector?: Vector<T>) => T, thisArg?: Object): void;
    /**
     * Uses a callback to traverse the elements in this Vector and obtain their position indexes.
     *
     * @param { function } callbackFn - Callback invoked for replacement.
     * @param { Object } thisArg - Value of **this** to use when **callbackFn** is invoked. The default value is this
     *     instance.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    forEach(callbackFn: (value: T, index?: number, vector?: Vector<T>) => void, thisArg?: Object): void;
    /**
     * Sorts elements in this Vector.
     *
     * @param { function } comparator - Callback invoked for sorting. The default value is this instance.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    sort(comparator?: (firstValue: T, secondValue: T) => number): void;
    /**
     * Obtains elements within a range in this Vector, including the element at the start position but not that at the end
     * position, and returns these elements as a new **Vector** instance.
     *
     * @param { number } fromIndex - Index of the start position.
     * @param { number } toIndex - Index of the end position.
     * @returns { Vector<T> } New **Vector** instance obtained.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    subVector(fromIndex: number, toIndex: number): Vector<T>;
    /**
     * Clears all elements in this Vector and sets its length to **0**.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    clear(): void;
    /**
     * Clones this Vector and returns a copy. The modification to the copy does not affect the original instance.
     *
     * @returns { Vector<T> } New **Vector** instance obtained.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    clone(): Vector<T>;
    /**
     * Sets a new length for this Vector.
     *
     * @param { number } newSize - New length to set.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    setLength(newSize: number): void;
    /**
     * Obtains the capacity of this Vector.
     *
     * @returns { number } Capacity obtained.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    getCapacity(): number;
    /**
     * Converts this Vector into an array.
     *
     * @returns { Array<T> } Array obtained.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    convertToArray(): Array<T>;
    /**
     * Checks whether this Vector is empty (contains no elements).
     *
     * @returns { boolean } Check result. The value **true** is returned if the Vector is empty; otherwise, **false** is
     *     returned.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    isEmpty(): boolean;
    /**
     * Increases the capacity of this Vector.
     *
     * @param { number } newCapacity - New capacity.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    increaseCapacityTo(newCapacity: number): void;
    /**
     * Uses commas (,) to concatenate elements in this Vector into a string.
     *
     * @returns { string } String obtained.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    toString(): string;
    /**
     * Trims the capacity of this Vector into its current length.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    trimToCurrentLength(): void;
    /**
     * Copies elements in this Vector into an array to overwrite elements of the same position indexes.
     *
     * @param { Array<T> } array - Array to which the elements in the Vector will be copied.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    copyToArray(array: Array<T>): void;
    /**
     * returns an ES6 iterator.Each item of the iterator is a Javascript Object
     *
     * @returns { IterableIterator<T> }
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     */
    [Symbol.iterator](): IterableIterator<T>;
}
export default Vector;

```
