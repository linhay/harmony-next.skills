# @ohos.data.storage.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
* Copyright (c) 2021 Huawei Device Co., Ltd.
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/
/**
 * @file
 * @kit ArkData
 */
import { AsyncCallback, Callback } from './@ohos.base';
/**
 * Lightweight storage provides applications with data processing capability and allows applications to perform
 * lightweight data storage and query. Data is stored in key-value (KV) pairs. Keys are of the string type, and values
 * can be of the number, string, or Boolean type.
 *
 * > **NOTE**
 *
 * > -  The APIs of this module are no longer maintained since API version 9. You are advised to use
 * > [@ohos.data.preferences]{@link @ohos.data.preferences:preferences}.
 *
 * @syscap SystemCapability.DistributedDataManager.Preferences.Core
 * @since 6
 * @deprecated since 9
 * @useinstead ohos.preferences.preferences
 * @name storage
 */
declare namespace storage {
    /**
     * Reads the specified file and loads its data to the **Storage** instance for data operations.
     *
     * @param { string } path - Path of the target file.
     * @returns { Storage } **Storage** instance used for data storage operations.
     * @throws BusinessError if invoked failed
     * @since 6
     * @deprecated since 9
     * @useinstead ohos.preferences.preferences.getPreferences
     */
    function getStorageSync(path: string): Storage;
    /**
     * Reads the specified file and loads its data to the **Storage** instance for data operations. This API uses an
     * asynchronous callback to return the result.
     *
     * @param { string } path - Path of the target file.
     * @param { AsyncCallback<Storage> } callback - Callback used to return the result.
     * @returns { Storage } The {@link Storage} instance matching the specified storage file name.
     * @throws BusinessError if invoked failed
     * @since 6
     * @deprecated since 9
     * @useinstead ohos.preferences.preferences.getPreferences
     */
    function getStorage(path: string, callback: AsyncCallback<Storage>): void;
    /**
     * Reads the specified file and loads its data to the **Storage** instance for data operations. This API uses a
     * promise to return the result.
     *
     * @param { string } path - Path of the target file.
     * @returns { Promise<Storage> } Promise used to return the result.
     * @throws BusinessError if invoked failed
     * @since 6
     * @deprecated since 9
     * @useinstead ohos.preferences.preferences.getPreferences
     */
    function getStorage(path: string): Promise<Storage>;
    /**
     * Deletes the singleton **Storage** instance of a file from the memory, and deletes the specified file, its backup
     * file, and damaged files. After the specified files are deleted, the **Storage** instance cannot be used for data
     * operations. Otherwise, data inconsistency will occur.
     *
     * @param { string } path - Path of the target file.
     * @throws BusinessError if invoked failed
     * @since 6
     * @deprecated since 9
     * @useinstead ohos.preferences.preferences.deletePreferences
     */
    function deleteStorageSync(path: string): void;
    /**
     * Deletes the singleton **Storage** instance of a file from the memory, and deletes the specified file, its backup
     * file, and damaged files. After the specified files are deleted, the **Storage** instance cannot be used for data
     * operations. Otherwise, data inconsistency will occur. This API uses an asynchronous callback to return the result.
     *
     * @param { string } path - Path of the target file.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws BusinessError if invoked failed
     * @since 6
     * @deprecated since 9
     * @useinstead ohos.preferences.preferences.deletePreferences
     */
    function deleteStorage(path: string, callback: AsyncCallback<void>): void;
    /**
     * Deletes the singleton **Storage** instance of a file from the memory, and deletes the specified file, its backup
     * file, and damaged files. After the specified files are deleted, the **Storage** instance cannot be used for data
     * operations. Otherwise, data inconsistency will occur. This API uses a promise to return the result.
     *
     * @param { string } path - Path of the target file.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws BusinessError if invoked failed
     * @since 6
     * @deprecated since 9
     * @useinstead ohos.preferences.preferences.deletePreferences
     */
    function deleteStorage(path: string): Promise<void>;
    /**
     * Removes the singleton **Storage** instance of a file from the cache. The removed instance cannot be used for data
     * operations. Otherwise, data inconsistency will occur.
     *
     * @param { string } path - Indicates the path of storage file.
     * @throws BusinessError if invoked failed
     * @since 6
     * @deprecated since 9
     * @useinstead ohos.preferences.preferences.removePreferencesFromCache
     */
    function removeStorageFromCacheSync(path: string): void;
    /**
     * Removes the singleton **Storage** instance of a file from the cache. The removed instance cannot be used for data
     * operations. Otherwise, data inconsistency will occur. This API uses an asynchronous callback to return the result.
     *
     * @param { string } path - Path of the target file.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws BusinessError if invoked failed
     * @since 6
     * @deprecated since 9
     * @useinstead ohos.preferences.preferences.removePreferencesFromCache
     */
    function removeStorageFromCache(path: string, callback: AsyncCallback<void>): void;
    /**
     * Removes the singleton **Storage** instance of a file from the cache. The removed instance cannot be used for data
     * operations. Otherwise, data inconsistency will occur. This API uses a promise to return the result.
     *
     * @param { string } path - Path of the target file.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws BusinessError if invoked failed
     * @since 6
     * @deprecated since 9
     * @useinstead ohos.preferences.preferences.removePreferencesFromCache
     */
    function removeStorageFromCache(path: string): Promise<void>;
    /**
     * Provides APIs for obtaining and modifying storage data.
     *
     * Before calling the following APIs, use [data_storage.getStorage]{@link storage.getStorageSync} or
     * [data_storage.getStorageSync]{@link storage.getStorageSync} to obtain the **Storage** instance.
     *
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @since 6
     * @deprecated since 9
     * @useinstead ohos.preferences.preferences
     */
    interface Storage {
        /**
         * Obtains the value corresponding to a key. If the value is null or not of the default value type, **defValue** is
         * returned.
         *
         * @param { string } key - Key of the data. It cannot be empty.
         * @param { ValueType } defValue - Default value to be returned if the value of the specified key does not exist. It
         *     can be a number, string, or Boolean value.
         * @returns { ValueType } Value corresponding to the specified key. If the value is null or not in the default value
         *     format, the default value is returned.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.get
         */
        getSync(key: string, defValue: ValueType): ValueType;
        /**
         * Obtains the value corresponding to a key. If the value is null or not of the default value type, **defValue** is
         * returned. This API uses an asynchronous callback to return the result.
         *
         * @param { string } key - Key of the data. It cannot be empty.
         * @param { ValueType } defValue - Default value to be returned. It can be a number, string, or Boolean value.
         * @param { AsyncCallback<ValueType> } callback - Callback used to return the result.
         * @returns { ValueType } The value matching the specified key if it is found; returns the default value otherwise.
        * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.get
         */
        get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void;
        /**
         * Obtains the value corresponding to a key. If the value is null or not of the default value type, **defValue** is
         * returned. This API uses a promise to return the result.
         *
         * @param { string } key - Key of the data. It cannot be empty.
         * @param { ValueType } defValue - Default value to be returned. It can be a number, string, or Boolean value.
         * @returns { Promise<ValueType> } Promise used to return the result.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.get
         */
        get(key: string, defValue: ValueType): Promise<ValueType>;
        /**
         * Checks whether the storage object contains data with a given key.
         *
         * @param { string } key - Key of the data. It cannot be empty.
         * @returns { boolean } Returns **true** if the storage object contains data with the specified key; returns
         *     **false** otherwise.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.has
         */
        hasSync(key: string): boolean;
        /**
         * Checks whether the storage object contains data with a given key. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { string } key - Key of the data. It cannot be empty.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result.
         * @returns { boolean } Returns **true** if the storage object contains data with the specified key; returns
         *     **false** otherwise.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.has
         */
        has(key: string, callback: AsyncCallback<boolean>): boolean;
        /**
         * Checks whether the storage object contains data with a given key. This API uses a promise to return the result.
         *
         * @param { string } key - Key of the data. It cannot be empty.
         * @returns { Promise<boolean> } Promise used to return the result.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.has
         */
        has(key: string): Promise<boolean>;
        /**
         * Obtains the **Storage** instance corresponding to the specified file, writes data to the **Storage** instance
         * using a **Storage** API, and saves the modification using **flush()** or **flushSync()**.
         *
         * @param { string } key - Key of the data. It cannot be empty.
         * @param { ValueType } value - New value to store. It can be a number, string, or Boolean value.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.put
         */
        putSync(key: string, value: ValueType): void;
        /**
         * Obtains the **Storage** instance corresponding to the specified file, writes data to the **Storage** instance
         * using a **Storage** API, and saves the modification using **flush()** or **flushSync()**. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { string } key - Key of the data. It cannot be empty.
         * @param { ValueType } value - New value to store. It can be a number, string, or Boolean value.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.put
         */
        put(key: string, value: ValueType, callback: AsyncCallback<void>): void;
        /**
         * Obtains the **Storage** instance corresponding to the specified file, writes data to the **Storage** instance
         * using a **Storage** API, and saves the modification using **flush()** or **flushSync()**. This API uses a promise
         * to return the result.
         *
         * @param { string } key - Key of the data. It cannot be empty.
         * @param { ValueType } value - New value to store. It can be a number, string, or Boolean value.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.put
         */
        put(key: string, value: ValueType): Promise<void>;
        /**
         * Deletes data with the specified key from this storage object.
         *
         * @param { string } key - Key of the data. It cannot be empty.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.delete
         */
        deleteSync(key: string): void;
        /**
         * Deletes data with the specified key from this storage object. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { string } key - Key of the data. It cannot be empty.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.delete
         */
        delete(key: string, callback: AsyncCallback<void>): void;
        /**
         * Deletes data with the specified key from this storage object. This API uses a promise to return the result.
         *
         * @param { string } key - Key of the data.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.delete
         */
        delete(key: string): Promise<void>;
        /**
         * Clears this **Storage** object.
         *
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.clear
         */
        clearSync(): void;
        /**
         * Clears this **Storage** object. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.clear
         */
        clear(callback: AsyncCallback<void>): void;
        /**
         * Clears this **Storage** object. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } A promise object.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.clear
         */
        clear(): Promise<void>;
        /**
         * Saves the modification of this object to the **Storage** instance and synchronizes the modification to the file.
         *
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.flush
         */
        flushSync(): void;
        /**
         * Saves the modification of this object to the **Storage** instance and synchronizes the modification to the file.
         * This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.flush
         */
        flush(callback: AsyncCallback<void>): void;
        /**
         * Saves the modification of this object to the **Storage** instance and synchronizes the modification to the file.
         * This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise used to return the result.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.flush
         */
        flush(): Promise<void>;
        /**
         * Subscribes to data changes. The **StorageObserver** needs to be implemented. When the value of the key subscribed
         * to is changed, a callback will be invoked after **flush()** or **flushSync()** is executed.
         *
         * @param { string } type - Event type. The value **change** indicates data change events.
         * @param { Callback<StorageObserver> } callback - Callback used to return the result.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.on
         */
        on(type: 'change', callback: Callback<StorageObserver>): void;
        /**
         * Unsubscribes from data changes.
         *
         * @param { string } type - Event type. The value **change** indicates data change events.
         * @param { Callback<StorageObserver> } callback - Callback for the data change.
         * @throws BusinessError if invoked failed
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.preferences.preferences.off
         */
        off(type: 'change', callback: Callback<StorageObserver>): void;
    }
    /**
     * Enumerates the value types.
     *
     * @unionmember { number } The value is a number.
     * @unionmember { string } The value is a string.
     * @unionmember { boolean } The value is of Boolean type.
     * @since 6
     * @deprecated since 9
     */
    type ValueType = number | string | boolean;
    /**
     * Define the change data information object.
     *
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     *
     * @since 6
     * @deprecated since 9
     */
    interface StorageObserver {
        /**
         * Data changed.
         *
         * @since 6
         * @deprecated since 9
         */
        key: string;
    }
    /**
     * Indicates the maximum length of a key (80 characters).
     *
     * @since 6
     * @deprecated since 9
     */
    const MAX_KEY_LENGTH: 80;
    /**
     * Indicates the maximum length of a string (8192 characters).
     *
     * @since 6
     * @deprecated since 9
     */
    const MAX_VALUE_LENGTH: 8192;
}
/**
 * Provides interfaces to obtain and modify storage data.
 * @since 6
 * @deprecated since 9
 * @syscap SystemCapability.DistributedDataManager.Preferences.Core
 */
export default storage;

```
