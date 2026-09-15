# @ohos.util.List.d.ts

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
 * List is implemented based on the singly linked list. Each node has a reference pointing to the next element. Elements
 * must be traversed from the beginning, making querying inefficient. However, insertion and deletion operations are
 * highly efficient. List allows null elements.
 * Unlike [LinkedList]{@link @ohos.util.LinkedList}, which is a doubly linked list, List is a singly linked list that
 * does not support insertion or removal at both ends.
 *
 * > **NOTE**
 * >
 * > Accessing elements in a List using the \[index\] syntax may lead to undefined results. You are advised to use
 * > **get()** instead.
 * > **Recommended use case**: Use List for frequent insertion and removal operations when a singly linked list is
 * > required.
 * > This topic uses the following to identify the use of generics:
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
 * List is implemented based on the singly linked list. Each node has a reference pointing to the next element.
 * When querying an element, the system traverses the list from the beginning.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 12]
 * @since 8
 */
declare class List<T> {
    /**
     * A constructor used to create a **List** instance.
     *
     * @throws { BusinessError } 10200012 - The List's constructor cannot be directly invoked.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    constructor();
    /**
     * Number of elements in a List.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    length: number;
    /**
     * Adds an element at the end of this List.
     *
     * @param { T } element - Target element.
     * @returns { boolean } Operation result. The value **true** is returned if the element is added; otherwise, **false**
     *     is returned.
     * @throws { BusinessError } 10200011 - The add method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    add(element: T): boolean;
    /**
     * Inserts an element at the specified position in this List.
     *
     * @param { T } element - Target element.
     * @param { number } index - Index of the position where the element is to be inserted. The value must be less than or
     *     equal to int32_max, that is, 2147483647.
     * @throws { BusinessError } 10200011 - The insert method cannot be bound.
     * @throws { BusinessError } 10200001 - The value of index is out of range.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    insert(element: T, index: number): void;
    /**
     * Obtains the element at the specified position in this List.
     *
     * @param { number } index - Position index of the target element. The value must be less than or equal to int32_max,
     *     that is, 2147483647.
     * @returns { T } Element obtained.
     * @throws { BusinessError } 10200011 - The get method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    get(index: number): T;
    /**
     * Checks whether this List has the specified element.
     *
     * @param { T } element - Target element.
     * @returns { boolean } Operation result. The value **true** is returned if the specified element is contained;
     *     otherwise, **false** is returned.
     * @throws { BusinessError } 10200011 - The has method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    has(element: T): boolean;
    /**
     * Obtains the index of the first occurrence of the specified element in this List.
     *
     * @param { T } element - Target element.
     * @returns { number } Index of the element. If no match is found, **-1** is returned.
     * @throws { BusinessError } 10200011 - The getIndexOf method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    getIndexOf(element: T): number;
    /**
     * Searches for an element based on its index and then removes it.
     *
     * @param { number } index - Position index of the target element. The value must be less than or equal to int32_max,
     *     that is, 2147483647.
     * @returns { T } Element removed.
     * @throws { BusinessError } 10200011 - The removeByIndex method cannot be bound.
     * @throws { BusinessError } 10200001 - The value of index is out of range.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    removeByIndex(index: number): T;
    /**
     * Removes the first occurrence of the specified element from this List.
     *
     * @param { T } element - Target element.
     * @returns { boolean } Operation result. The value **true** is returned if the element is removed; otherwise,
     *     **false** is returned.
     * @throws { BusinessError } 10200011 - The remove method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    remove(element: T): boolean;
    /**
     * Obtains the index of the last occurrence of the specified element in this List.
     *
     * @param { T } element - Target element.
     * @returns { number } Index of the element. If no match is found, **-1** is returned.
     * @throws { BusinessError } 10200011 - The getLastIndexOf method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    getLastIndexOf(element: T): number;
    /**
     * Obtains the first element in this List.
     *
     * @returns { T } The first element obtained.
     * @throws { BusinessError } 10200011 - The getFirst method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    getFirst(): T;
    /**
     * Obtains the last element in this List.
     *
     * @returns { T } The last element obtained.
     * @throws { BusinessError } 10200011 - The getLast method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    getLast(): T;
    /**
     * Replaces an element at the specified position in this List with a given element.
     *
     * @param { number } index - Position index of the target element. The value must be less than or equal to int32_max,
     *     that is, 2147483647.
     * @param { T } element - Element to be used for replacement.
     * @returns { T } New element.
     * @throws { BusinessError } 10200011 - The set method cannot be bound.
     * @throws { BusinessError } 10200001 - The value of index is out of range.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    set(index: number, element: T): T;
    /**
     * Compares whether a specified object is equal to this List.
     *
     * @param { Object } obj - Object used for comparison.
     * @returns { boolean } Check result. The value **true** is returned if the two are equal; otherwise, **false** is
     *     returned.
     * @throws { BusinessError } 10200011 - The equal method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    equal(obj: Object): boolean;
    /**
     * Uses a callback to traverse each element in the **List** instance.
     *
     * @param { function } callbackFn - Callback used to return the result.
     * @param { Object } [thisArg] - Value of **this** to use when **callbackFn** is invoked. The default value is this
     *     instance.
     * @throws { BusinessError } 10200011 - The forEach method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    forEach(callbackFn: (value: T, index?: number, List?: List<T>) => void, thisArg?: Object): void;
    /**
     * Sorts elements in this List.
     *
     * @param { function } comparator - Callback used to return the result.<br> There has been a compatibility change
     *     since API version 23. In API version 22 and earlier versions, the type is `(firstValue: T, secondValue: T) =>
     *     number`. [since 8 - 22]
     * @param { ListComparatorFn<T> } comparator - Callback used to return the result.<br> There has been a compatibility
     *     change since API version 23. In API version 22 and earlier versions, the type is `(firstValue: T, secondValue:
     *     T) => number`. [since 23]
     * @throws { BusinessError } 10200011 - The sort method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    sort(comparator: ListComparatorFn<T>): void;
    /**
     * Clears this List and sets its length to **0**.
     *
     * @throws { BusinessError } 10200011 - The clear method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    clear(): void;
    /**
     * Obtains elements within a range in this List, including the element at the start position but not that at the end
     * position, and returns these elements as a new **List** instance.
     *
     * @param { number } fromIndex - Index of the start position.
     * @param { number } toIndex - Index of the end position.
     * @returns { List<T> } New **List** instance obtained.
     * @throws { BusinessError } 10200011 - The getSubList method cannot be bound.
     * @throws { BusinessError } 10200001 - The value of fromIndex or toIndex is out of range.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    getSubList(fromIndex: number, toIndex: number): List<T>;
    /**
     * Replaces all elements in this List with new elements, and returns the new ones.
     *
     * @param { function } callbackFn - Callback invoked for the replacement.
     * @param { Object } [thisArg] - Value of **this** to use when **callbackFn** is invoked. The default value is this
     *     instance.
     * @throws { BusinessError } 10200011 - The replaceAllElements method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    replaceAllElements(callbackFn: (value: T, index?: number, list?: List<T>) => T, thisArg?: Object): void;
    /**
     * Converts this List into an array and returns the array.
     *
     * @returns { Array<T> } Array obtained.
     * @throws { BusinessError } 10200011 - The convertToArray method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    convertToArray(): Array<T>;
    /**
     * Checks whether this List is empty (contains no element).
     *
     * @returns { boolean } Check result. The value **true** is returned if the List is empty; otherwise, **false** is
     *     returned.
     * @throws { BusinessError } 10200011 - The isEmpty method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    isEmpty(): boolean;
    /**
     * returns an iterator.Each item of the iterator is a Javascript Object
     *
     * @returns { IterableIterator<T> }
     * @throws { BusinessError } 10200011 - The Symbol.iterator method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    [Symbol.iterator](): IterableIterator<T>;
}
/**
 * This type specifies the comparator of sort in comparation.
 *
 * @param { T } firstValue - firstValue (required) previous element.
 * @param { T } secondValue - secondValue (required) next element.
 * @returns { number } the number type
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform
 * @atomicservice
 * @since 23
 */
export type ListComparatorFn<T> = (firstValue: T, secondValue: T) => number;
export default List;

```
