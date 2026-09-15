# @ohos.util.HashSet.d.ts

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
 * HashSet is implemented based on [HashMap]{@link @ohos.util.HashMap}. In HashSet, only the **value** object is
 * processed.
 * Unlike [TreeSet]{@link @ohos.util.TreeSet}, which stores and accesses data in sorted order, HashSet sorts data by
 * hash value. This means that HashSet may use a different order when storing and accessing elements. Both of them allow
 * only unique elements. However, null values are allowed in HashSet, but not in TreeSet, because null values may affect
 * the order of elements in the container.
 * **Recommended use case**: Use HashSet when you need a set that has only unique elements or need to deduplicate a set.
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
 * HashSet is implemented based on HashMap. In HashSet, only the value object is processed.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 12]
 * @since 8
 */
declare class HashSet<T> {
    /**
     * A constructor used to create a **HashSet** instance.
     *
     * @throws { BusinessError } 10200012 - The HashSet's constructor cannot be directly invoked.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    constructor();
    /**
     * Number of elements in a HashSet.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    length: number;
    /**
     * Checks whether this HashSet is empty (contains no element).
     *
     * @returns { boolean } Check result. The value **true** is returned if the HashSet is empty; otherwise, **false** is
     *     returned.
     * @throws { BusinessError } 10200011 - The isEmpty method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    isEmpty(): boolean;
    /**
     * Checks whether this HashSet has the specified element.
     *
     * @param { T } value - Target element.
     * @returns { boolean } Operation result. The value **true** is returned if the specified element is contained;
     *     otherwise, **false** is returned.
     * @throws { BusinessError } 10200011 - The has method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    has(value: T): boolean;
    /**
     * Adds elements to this HashSet.
     *
     * @param { T } value - Target element.
     * @returns { boolean } Operation result. The value **true** is returned if the element is added; otherwise, **false**
     *     is returned.
     * @throws { BusinessError } 10200011 - The add method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    add(value: T): boolean;
    /**
     * Removes an element from this HashSet.
     *
     * @param { T } value - Target element.
     * @returns { boolean } Operation result. The value **true** is returned if the element is removed; otherwise,
     *     **false** is returned.
     * @throws { BusinessError } 10200011 - The remove method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    remove(value: T): boolean;
    /**
     * Clears this HashSet and sets its length to **0**.
     *
     * @throws { BusinessError } 10200011 - The clear method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    clear(): void;
    /**
     * Uses a callback to traverse each element.
     *
     * @param { function } callbackFn - Callback invoked to traverse the elements in the HashSet.
     * @param { Object } [thisArg] - Value of **this** to use when **callbackFn** is invoked. The default value is this
     *     instance.
     * @throws { BusinessError } 10200011 - The forEach method cannot be bound.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    forEach(callbackFn: (value?: T, key?: T, set?: HashSet<T>) => void, thisArg?: Object): void;
    /**
     * Returns an iterator that contains all the values in this HashSet.
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
     * Returns an iterator that contains all the elements in this HashSet.
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
export default HashSet;

```
