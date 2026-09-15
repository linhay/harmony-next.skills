# @ohos.util.LinkedList.d.ts

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
 * LinkedList is implemented based on the doubly linked list. Each node of the doubly linked list has references
 * pointing to the previous element and the next element. When querying an element, the system traverses the list from
 * the beginning or end. LinkedList offers efficient insertion and removal operations but supports low query efficiency.
 * LinkedList allows null elements.
 * Unlike [List]{@link @ohos.util.List}, which is a singly linked list, LinkedList is a doubly linked list that supports
 * insertion and removal at both ends.
 * LinkedList is more efficient in data insertion than [ArrayList]{@link @ohos.util.ArrayList}, but less efficient in
 * data access.
 *
 * > **NOTE**
 * >
 * > Accessing elements in a LinkedList using the \[index\] syntax may lead to undefined results. You are advised to use
 * > **get()** instead.
 * > **Recommended use case**: Use LinkedList for frequent insertion and removal operations when a doubly linked list is
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
 * LinkedList is implemented based on the doubly linked list. Each node of the doubly linked list has
 * references pointing to the previous element and the next element. When querying an element,
 * the system traverses the list from the beginning or end.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 12]
 * @since 8
 */
declare class LinkedList<T> {
    /**
     * A constructor used to create a **LinkedList** instance.
     *
     * @throws { BusinessError } 10200012 - The LinkedList's constructor cannot be directly invoked.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    constructor();
    /**
     * Number of elements in a LinkedList.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    length: number;
    /**
     * Adds an element at the end of this LinkedList.
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
     * Inserts an element at the specified position in this LinkedList.
     *
     * @param { number } index - Index of the position where the element is to be inserted. The value must be less than or
     *     equal to int32_max, that is, 2147483647.
     * @param { T } element - Target element.
     * @throws { BusinessError } 10200011 - The insert method cannot be bound.
     * @throws { BusinessError } 10200001 - The value of index is out of range.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    insert(index: number, element: T): void;
    /**
     * Obtains an element at the specified position in this LinkedList.
     *
     * @param { number } index - Position index of the target element. The value must be less than or equal to int32_max,
     *     that is, 2147483647.
     * @returns { T } Element obtained. If the element does not exist, **undefined** is returned.
     * @throws { BusinessError } 10200011 - The get method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    get(index: number): T;
    /**
     * Adds an element at the top of this LinkedList.
     *
     * @param { T } element - Target element.
     * @throws { BusinessError } 10200011 - The addFirst method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    addFirst(element: T): void;
    /**
     * Removes the first element from this LinkedList.
     *
     * @returns { T } Element removed.
     * @throws { BusinessError } 10200011 - The removeFirst method cannot be bound.
     * @throws { BusinessError } 10200010 - Container is empty.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    removeFirst(): T;
    /**
     * Removes the last element from this LinkedList.
     *
     * @returns { T } Element removed.
     * @throws { BusinessError } 10200011 - The removeLast method cannot be bound.
     * @throws { BusinessError } 10200010 - Container is empty.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    removeLast(): T;
    /**
     * Checks whether this LinkedList has the specified element.
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
     * Obtains the index of the first occurrence of the specified element in this LinkedList.
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
     * @returns { T } Element removed. If the element does not exist, **undefined** is returned.
     * @throws { BusinessError } 10200011 - The removeByIndex method cannot be bound.
     * @throws { BusinessError } 10200001 - The value of index is out of range.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    removeByIndex(index: number): T;
    /**
     * Removes the first occurrence of the specified element from this LinkedList.
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
     * Removes the first occurrence of the specified element from this LinkedList.
     *
     * @param { T } element - Target element.
     * @returns { boolean } Returns **true** if the element is removed; returns **false** if the element fails to be
     *     removed or does not exist.
     * @throws { BusinessError } 10200011 - The removeFirstFound method cannot be bound.
     * @throws { BusinessError } 10200010 - Container is empty.
     * @throws { BusinessError } 10200017 - The element does not exist in this container.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    removeFirstFound(element: T): boolean;
    /**
     * Removes the last occurrence of the specified element from this LinkedList.
     *
     * @param { T } element - Target element.
     * @returns { boolean } Returns **true** if the element is removed; returns **false** if the element fails to be
     *     removed or does not exist.
     * @throws { BusinessError } 10200011 - The removeLastFound method cannot be bound.
     * @throws { BusinessError } 10200010 - Container is empty.
     * @throws { BusinessError } 10200017 - The element does not exist in this container.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    removeLastFound(element: T): boolean;
    /**
     * Obtains the index of the last occurrence of the specified element in this LinkedList.
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
     * Obtains the first element in this LinkedList.
     *
     * @returns { T } Element obtained. If the element is empty, **undefined** is returned.
     * @throws { BusinessError } 10200011 - The getFirst method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    getFirst(): T;
    /**
     * Obtains the last element in this LinkedList.
     *
     * @returns { T } Element obtained. If the element is empty, **undefined** is returned.
     * @throws { BusinessError } 10200011 - The getLast method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    getLast(): T;
    /**
     * Replaces an element at the specified position in this LinkedList with a given element.
     *
     * @param { number } index - Position index of the target element. The value must be less than or equal to int32_max,
     *     that is, 2147483647.
     * @param { T } element - Element to be used for replacement.
     * @returns { T } New element. If the element is empty, **undefined** is returned.
     * @throws { BusinessError } 10200011 - The set method cannot be bound.
     * @throws { BusinessError } 10200001 - The value of index is out of range.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    set(index: number, element: T): T;
    /**
     * Uses a callback to traverse the elements in this LinkedList and obtain their indexes.
     *
     * @param { function } callbackFn - Callback invoked to traverse the elements in the LinkedList.
     * @param { Object } [thisArg] - Value of **this** to use when **callbackFn** is invoked. The default value is this
     *     instance.
     * @throws { BusinessError } 10200011 - The forEach method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    forEach(callbackFn: (value: T, index?: number, LinkedList?: LinkedList<T>) => void, thisArg?: Object): void;
    /**
     * Clears this LinkedList and sets its length to **0**.
     *
     * @throws { BusinessError } 10200011 - The clear method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    clear(): void;
    /**
     * Clones an instance identical to this **LinkedList** and returns it. The modification to the copy does not affect
     * the original instance.
     *
     * @returns { LinkedList<T> } New **LinkedList** instance obtained.
     * @throws { BusinessError } 10200011 - The clone method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    clone(): LinkedList<T>;
    /**
     * Converts this LinkedList into an array and returns the array.
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
export default LinkedList;

```
