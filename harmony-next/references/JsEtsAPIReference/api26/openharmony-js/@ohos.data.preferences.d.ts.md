# @ohos.data.preferences.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2025 Huawei Device Co., Ltd.
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
import Context from './application/BaseContext';
/**
 * The **Preferences** module provides APIs for processing data in the form of key-value (KV) pairs, including querying,
 * modifying, and persisting KV pairs.
 * The key is of string type, and the value can be a number, string, boolean value, or an array of numbers, strings, or
 * boolean values.
 * The user preference persistent files are stored in the
 * [preferencesDir](docroot://application-models/application-context-stage.md#obtaining-application-file-paths)
 * directory. Before creating a preferences object, ensure that the **preferencesDir** directory is readable and
 * writeable. The [encryption level]{@link @ohos.app.ability.contextConstant:contextConstant.AreaMode} of the persistent
 * file directory determines the access to the files. For details, see
 * [Application File Directory and Application File Path](docroot://file-management/app-sandbox-directory.md#application-file-directory-and-application-file-path)
 * .
 *
 * > **NOTE**
 * >
 * > Preferences are not thread-safe and may cause file damage and data loss when used in multi-process scenarios. Do
 * > not use preferences in multi-process scenarios.
 *
 * @syscap SystemCapability.DistributedDataManager.Preferences.Core
 * @name preferences
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace preferences {
    /**
     * Enumerates the value types.
     *
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @unionmember { number } The value is a number.
     * @unionmember { string } The value is a string.
     * @unionmember { boolean } The value is true or false.
     * @unionmember { Array<number> } The value is an array of numbers.
     * @unionmember { Array<string> } The value is an array of strings.
     * @unionmember { Array<boolean> } The value is a boolean array.
     * @unionmember { Uint8Array } The value is an array of 8-bit unsigned integers. [since 11]
     * @unionmember { object } The value is an object. [since 12]
     * @unionmember { bigint } The value is an integer in any format. [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    type ValueType = number | string | boolean | Array<number> | Array<string> | Array<boolean> | Uint8Array | object | bigint;
    /**
     * Maximum key length, which is 1,024 bytes.
     *
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    const MAX_KEY_LENGTH: number;
    /**
     * Maximum value length, which is 16 MB.
     *
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    const MAX_VALUE_LENGTH: number;
    /**
     * Enumerates the storage types of preferences.
     *
     * > **NOTE**
     * >
     * > - Before using this mode, you are advised to call **isStorageTypeSupported** to check whether this storage type
     * > is supported.
     * >
     * > - Once the storage type is selected and data instances are obtained via **getPreferences()**, the storage type
     * > cannot be changed.
     * >
     * > - Data cannot be directly migrated between the **Preferences** instances that use different storage types. To
     * > migrate data between them, you need to read the data to be migrated and then write the data.
     * >
     * > - If you need to change the storage directory of preferences, you cannot move or overwrite files. Instead, you
     * > need to read the data and then write the data.
     *
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @atomicservice
     * @since 18
     */
    enum StorageType {
        /**
         * [XML](docroot://database/data-persistence-by-preferences.md#xml) format, which is the default storage type of
         * **Preferences**.
         *
         * In this mode, data is stored in XML format. Data operations are performed in the memory. To persist data, call
         * **flush()**.
         *
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @atomicservice
         * @since 18
         */
        XML = 0,
        /**
         * [GSKV](docroot://database/data-persistence-by-preferences.md#gskv) format.
         *
         * Data is stored in GSKV mode. Data operations are flushed on a real-time basis without calling **flush()**.
         *
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @atomicservice
         * @since 18
         */
        GSKV
    }
    /**
     * Represents the configuration of a **Preferences** instance.
     *
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    interface Options {
        /**
         * Name of the **Preferences** instance. It must be longer than 0 bytes and less than or equal to 255 bytes, and
         * cannot contain or end with slashes (/).
         *
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        name: string;
        /**
         * Application group ID. <!--RP1-->Currently, this parameter is not supported.<!--RP1End-->
         *
         * This parameter is optional. A **Preferences** instance will be created in the sandbox path corresponding to the
         * specified **dataGroupId**. If this parameter is not specified, the **Preferences** instance is created in the
         * sandbox directory of the application.
         *
         * This attribute can be used only in the stage model.
         *
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @StageModelOnly
         * @atomicservice [since 11]
         * @since 10
         */
        dataGroupId?: string | null | undefined;
        /**
         * Storage mode to be used by the **Preferences** instance. This parameter is optional. If this parameter is left
         * blank, the XML storage type is used by default. After the storage type is set for a **Preferences** instance, it
         * cannot be changed.
         *
         * This API can be used in atomic services since API version 18.
         *
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @atomicservice
         * @since 18
         */
        storageType?: StorageType | null | undefined;
    }
    /**
     * Obtains a **Preferences** instance. This API uses an asynchronous callback to return the result.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { string } name - Name of the **Preferences** instance.
     * @param { AsyncCallback<Preferences> } callback - Callback used to return the result. If the operation is successful
     *     , **err** is **undefined** and the **Preferences** instance obtained is returned. Otherwise, **err** is an
     *     error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>): void;
    /**
     * Obtains a **Preferences** instance. This API uses an asynchronous callback to return the result.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { Options } options - Configuration options of the **Preferences** instance.
     * @param { AsyncCallback<Preferences> } callback - Callback used to return the result. If the operation is successful
     *     , **err** is **undefined** and the **Preferences** instance obtained is returned. Otherwise, **err** is an
     *     error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 15501001 - The operations is supported in stage mode only.
     * @throws { BusinessError } 15501002 - Invalid dataGroupId.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function getPreferences(context: Context, options: Options, callback: AsyncCallback<Preferences>): void;
    /**
     * Obtains a **Preferences** instance. This API uses a promise to return the result.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { string } name - Name of the **Preferences** instance.
     * @returns { Promise<Preferences> } Promise used to return the **Preferences** instance obtained.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function getPreferences(context: Context, name: string): Promise<Preferences>;
    /**
     * Obtains a **Preferences** instance. This API uses a promise to return the result.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { Options } options - Configuration options of the **Preferences** instance.
     * @returns { Promise<Preferences> } Promise used to return the **Preferences** instance obtained.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 15501001 - The operations is supported in stage mode only.
     * @throws { BusinessError } 15501002 - Invalid dataGroupId.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function getPreferences(context: Context, options: Options): Promise<Preferences>;
    /**
     * Obtains a **Preferences** instance. This API returns the result synchronously.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { Options } options - Configuration options of the **Preferences** instance.
     * @returns { Preferences } **Preferences** instance obtained.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 15501001 - The operations is supported in stage mode only.
     * @throws { BusinessError } 15501002 - Invalid dataGroupId.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function getPreferencesSync(context: Context, options: Options): Preferences;
    /**
     * Checks whether the specified storage type is supported. This API returns the result synchronously. If the storage
     * type is supported, **true** is returned. Otherwise, **false** is returned.
     *
     * @param { StorageType } type - Storage type to check.
     * @returns { boolean } Returns **true** if the storage type is supported; returns **false** otherwise.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @atomicservice
     * @since 18
     */
    function isStorageTypeSupported(type: StorageType): boolean;
    /**
     * Deletes a specified **Preferences** instance from the cache. If the **Preferences** instance has a corresponding
     * persistent file, the persistent file is also deleted. This API uses an asynchronous callback to return the result.
     * Avoid using a removed **Preferences** instance to perform data operations, which may cause data inconsistency.
     * Instead, set the removed **Preferences** instance to null. The system will reclaim them in a unified manner.
     * This API cannot be called concurrently with other **preferences** APIs.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { string } name - Name of the **Preferences** instance.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 15500010 - Failed to delete the user preferences persistence file.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function deletePreferences(context: Context, name: string, callback: AsyncCallback<void>): void;
    /**
     * Deletes a specified **Preferences** instance from the cache. If the **Preferences** instance has a corresponding
     * persistent file, the persistent file is also deleted. This API uses an asynchronous callback to return the result.
     * Avoid using a removed **Preferences** instance to perform data operations, which may cause data inconsistency.
     * Instead, set the removed **Preferences** instance to null. The system will reclaim them in a unified manner.
     * This API cannot be called concurrently with other **preferences** APIs.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { Options } options - Configuration options of the **Preferences** instance.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 15500010 - Failed to delete the user preferences persistence file.
     * @throws { BusinessError } 15501001 - The operations is supported in stage mode only.
     * @throws { BusinessError } 15501002 - Invalid dataGroupId.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function deletePreferences(context: Context, options: Options, callback: AsyncCallback<void>): void;
    /**
     * Deletes a specified **Preferences** instance from the cache. If the **Preferences** instance has a corresponding
     * persistent file, the persistent file is also deleted. This API uses a promise to return the result.
     * Avoid using a removed **Preferences** instance to perform data operations, which may cause data inconsistency.
     * Instead, set the removed **Preferences** instance to null. The system will reclaim them in a unified manner.
     * This API cannot be called concurrently with other **preferences** APIs.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { string } name - Name of the **Preferences** instance.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 15500010 - Failed to delete the user preferences persistence file.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function deletePreferences(context: Context, name: string): Promise<void>;
    /**
     * Deletes a specified **Preferences** instance from the cache. If the **Preferences** instance has a corresponding
     * persistent file, the persistent file is also deleted. This API uses a promise to return the result.
     * Avoid using a removed **Preferences** instance to perform data operations, which may cause data inconsistency.
     * Instead, set the removed **Preferences** instance to null. The system will reclaim them in a unified manner.
     * This API cannot be called concurrently with other **preferences** APIs.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { Options } options - Configuration options of the **Preferences** instance.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 15500010 - Failed to delete the user preferences persistence file.
     * @throws { BusinessError } 15501001 - The operations is supported in stage mode only.
     * @throws { BusinessError } 15501002 - Invalid dataGroupId.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function deletePreferences(context: Context, options: Options): Promise<void>;
    /**
     * Removes a **Preferences** instance from the cache. This API uses an asynchronous callback to return the result.
     * After an application calls
     * [getPreferences]{@link preferences.getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>)}
     * for the first time to obtain a **Preferences** instance, the obtained **Preferences** instance is cached. When the
     * application calls
     * [getPreferences]{@link preferences.getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>)}
     * again, the **Preferences** instance will be read from the cache instead of from the persistent file. After this API
     * is called to remove the instance from the cache, calling **getPreferences** again will read data from the
     * persistent file and create a **Preferences** instance.
     * Avoid using a removed **Preferences** instance to perform data operations, which may cause data inconsistency.
     * Instead, set the removed **Preferences** instance to null. The system will reclaim them in a unified manner.
     * If [GSKV](docroot://database/data-persistence-by-preferences.md#gskv) is used, you are advised to manually call
     * this API once when the process exits. This operation writes the data cache page to the disk, which can reduce the
     * time required for calling the **getPreferences** API next time. Otherwise, data restoration is required at the
     * bottom layer when the **getPreferences** API is called. The time required for data restoration depends on the
     * number of data cache pages that are not written to the disk.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { string } name - Name of the **Preferences** instance.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function removePreferencesFromCache(context: Context, name: string, callback: AsyncCallback<void>): void;
    /**
     * Removes a **Preferences** instance from the cache. This API uses an asynchronous callback to return the result.
     * After an application calls
     * [getPreferences]{@link preferences.getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>)}
     * for the first time to obtain a **Preferences** instance, the obtained **Preferences** instance is cached. When the
     * application calls
     * [getPreferences]{@link preferences.getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>)}
     * again, the **Preferences** instance will be read from the cache instead of from the persistent file. After this API
     * is called to remove the instance from the cache, calling **getPreferences** again will read data from the
     * persistent file and create a **Preferences** instance.
     * Avoid using a removed **Preferences** instance to perform data operations, which may cause data inconsistency.
     * Instead, set the removed **Preferences** instance to null. The system will reclaim them in a unified manner.
     * If [GSKV](docroot://database/data-persistence-by-preferences.md#gskv) is used, you are advised to manually call
     * this API once when the process exits. This operation writes the data cache page to the disk, which can reduce the
     * time required for calling the **getPreferences** API next time. Otherwise, data restoration is required at the
     * bottom layer when the **getPreferences** API is called. The time required for data restoration depends on the
     * number of data cache pages that are not written to the disk.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { Options } options - Configuration options of the **Preferences** instance.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 15501001 - The operations is supported in stage mode only.
     * @throws { BusinessError } 15501002 - Invalid dataGroupId.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function removePreferencesFromCache(context: Context, options: Options, callback: AsyncCallback<void>): void;
    /**
     * Removes a **Preferences** instance from the cache. This API uses a promise to return the result.
     * After an application calls
     * [getPreferences]{@link preferences.getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>)}
     * for the first time to obtain a **Preferences** instance, the obtained **Preferences** instance is cached. When the
     * application calls
     * [getPreferences]{@link preferences.getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>)}
     * again, the **Preferences** instance will be read from the cache instead of from the persistent file. After this API
     * is called to remove the instance from the cache, calling **getPreferences** again will read data from the
     * persistent file and create a **Preferences** instance.
     * Avoid using a removed **Preferences** instance to perform data operations, which may cause data inconsistency.
     * Instead, set the removed **Preferences** instance to null. The system will reclaim them in a unified manner.
     * If [GSKV](docroot://database/data-persistence-by-preferences.md#gskv) is used, you are advised to manually call
     * this API once when the process exits. This operation writes the data cache page to the disk, which can reduce the
     * time required for calling the **getPreferences** API next time. Otherwise, data restoration is required at the
     * bottom layer when the **getPreferences** API is called. The time required for data restoration depends on the
     * number of data cache pages that are not written to the disk.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { string } name - Name of the **Preferences** instance.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function removePreferencesFromCache(context: Context, name: string): Promise<void>;
    /**
     * Removes a **Preferences** instance from the cache. This API uses a promise to return the result.
     * After an application calls
     * [getPreferences]{@link preferences.getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>)}
     * for the first time to obtain a **Preferences** instance, the obtained **Preferences** instance is cached. When the
     * application calls
     * [getPreferences]{@link preferences.getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>)}
     * again, the **Preferences** instance will be read from the cache instead of from the persistent file. After this API
     * is called to remove the instance from the cache, calling **getPreferences** again will read data from the
     * persistent file and create a **Preferences** instance.
     * Avoid using a removed **Preferences** instance to perform data operations, which may cause data inconsistency.
     * Instead, set the removed **Preferences** instance to null. The system will reclaim them in a unified manner.
     * If [GSKV](docroot://database/data-persistence-by-preferences.md#gskv) is used, you are advised to manually call
     * this API once when the process exits. This operation writes the data cache page to the disk, which can reduce the
     * time required for calling the **getPreferences** API next time. Otherwise, data restoration is required at the
     * bottom layer when the **getPreferences** API is called. The time required for data restoration depends on the
     * number of data cache pages that are not written to the disk.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { Options } options - Configuration options of the **Preferences** instance.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 15501001 - The operations is supported in stage mode only.
     * @throws { BusinessError } 15501002 - Invalid dataGroupId.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function removePreferencesFromCache(context: Context, options: Options): Promise<void>;
    /**
     * Removes a **Preferences** instance from the cache. This API returns the result synchronously.
     * After an application calls
     * [getPreferences]{@link preferences.getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>)}
     * for the first time to obtain a **Preferences** instance, the obtained **Preferences** instance is cached. When the
     * application calls
     * [getPreferences]{@link preferences.getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>)}
     * again, the **Preferences** instance will be read from the cache instead of from the persistent file. After this API
     * is called to remove the instance from the cache, calling **getPreferences** again will read data from the
     * persistent file and create a **Preferences** instance.
     * Avoid using a removed **Preferences** instance to perform data operations, which may cause data inconsistency.
     * Instead, set the removed **Preferences** instance to null. The system will reclaim them in a unified manner.
     * If [GSKV](docroot://database/data-persistence-by-preferences.md#gskv) is used, you are advised to manually call
     * this API once when the process exits. This operation writes the data cache page to the disk, which can reduce the
     * time required for calling the **getPreferences** API next time. Otherwise, data restoration is required at the
     * bottom layer when the **getPreferences** API is called. The time required for data restoration depends on the
     * number of data cache pages that are not written to the disk.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { string } name - Name of the **Preferences** instance.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function removePreferencesFromCacheSync(context: Context, name: string): void;
    /**
     * Removes a **Preferences** instance from the cache. This API returns the result synchronously.
     * After an application calls
     * [getPreferences]{@link preferences.getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>)}
     * for the first time to obtain a **Preferences** instance, the obtained **Preferences** instance is cached. When the
     * application calls
     * [getPreferences]{@link preferences.getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>)}
     * again, the **Preferences** instance will be read from the cache instead of from the persistent file. After this API
     * is called to remove the instance from the cache, calling **getPreferences** again will read data from the
     * persistent file and create a **Preferences** instance.
     * Avoid using a removed **Preferences** instance to perform data operations, which may cause data inconsistency.
     * Instead, set the removed **Preferences** instance to null. The system will reclaim them in a unified manner.
     * If [GSKV](docroot://database/data-persistence-by-preferences.md#gskv) is used, you are advised to manually call
     * this API once when the process exits. This operation writes the data cache page to the disk, which can reduce the
     * time required for calling the **getPreferences** API next time. Otherwise, data restoration is required at the
     * bottom layer when the **getPreferences** API is called. The time required for data restoration depends on the
     * number of data cache pages that are not written to the disk.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { Options } options - Configuration options of the **Preferences** instance.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 15501001 - The operations is supported in stage mode only.
     * @throws { BusinessError } 15501002 - Invalid dataGroupId.
     * @throws { BusinessError } 15500000 - Inner error. [since 11]
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function removePreferencesFromCacheSync(context: Context, options: Options): void;
    /**
     * Provides APIs for obtaining and modifying the stored data.
     * Before calling any API of **Preferences**, you must obtain a **Preferences** instance by using
     * [preferences.getPreferences]{@link preferences.getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>)}
     * .
     *
     * @syscap SystemCapability.DistributedDataManager.Preferences.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    interface Preferences {
        /**
         * Obtains the value of a key from this **Preferences** instance. This API uses an asynchronous callback to return
         * the result. If the value is null or is not of the default value type, **defValue** is returned.
         *
         * @param { string } key - Key to be obtained. The value cannot be empty. For details about its maximum length, see
         *     [MAX_KEY_LENGTH](docroot://reference/apis-arkdata/js-apis-data-preferences.md#constants).
         * @param { ValueType } defValue - Default value to be returned.
         * @param { AsyncCallback<ValueType> } callback - Callback used to return the result. If the operation is successful
         *     , **err** is **undefined** and **data** is the value obtained. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void;
        /**
         * Obtains the value of a key from this **Preferences** instance. This API uses a promise to return the result. If
         * the value is null or is not of the default value type, **defValue** is returned.
         *
         * @param { string } key - Key to be obtained. The value cannot be empty. For details about its maximum length, see
         *     [MAX_KEY_LENGTH](docroot://reference/apis-arkdata/js-apis-data-preferences.md#constants).
         * @param { ValueType } defValue - Default value to be returned.
         * @returns { Promise<ValueType> } Promise used to return the value obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        get(key: string, defValue: ValueType): Promise<ValueType>;
        /**
         * Obtains the value of a key from this **Preferences** instance. This API returns the result synchronously. If the
         * value is null or is not of the default value type, **defValue** is returned.
         *
         * @param { string } key - Key to be obtained. The value cannot be empty. For details about its maximum length, see
         *     [MAX_KEY_LENGTH](docroot://reference/apis-arkdata/js-apis-data-preferences.md#constants).
         * @param { ValueType } defValue - Default value to be returned.
         * @returns { ValueType } Returns the value obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        getSync(key: string, defValue: ValueType): ValueType;
        /**
         * Obtains all KV pairs from a **Preferences** instance. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<Object> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **value** provides all KV pairs obtained. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Mandatory parameters are left unspecified.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getAll(callback: AsyncCallback<Object>): void;
        /**
         * Obtains all KV pairs from this **Preferences** instance. This API uses a promise to return the result.
         *
         * @returns { Promise<Object> } Promise used to return the KV pairs obtained.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getAll(): Promise<Object>;
        /**
         * Obtains all KV pairs from this **Preferences** instance. This API returns the result synchronously.
         *
         * @returns { Object } Returns all KV pairs obtained.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        getAllSync(): Object;
        /**
         * Checks whether this **Preferences** instance contains the KV pair of the given key. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { string } key - Key to be checked. The value cannot be empty. For details about its maximum length, see
         *     [MAX_KEY_LENGTH](docroot://reference/apis-arkdata/js-apis-data-preferences.md#constants).
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the **Preferences** instance
         *     contains the KV pair, **true** will be returned. Otherwise, **false** will be returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        has(key: string, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether this **Preferences** instance contains the KV pair of the given key. This API uses a promise to
         * return the result.
         *
         * @param { string } key - Key to be checked. The value cannot be empty. For details about its maximum length, see
         *     [MAX_KEY_LENGTH](docroot://reference/apis-arkdata/js-apis-data-preferences.md#constants).
         * @returns { Promise<boolean> } Promise used to return the result. If the **Preferences** instance contains the KV
         *     pair, **true** will be returned. Otherwise, **false** will be returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        has(key: string): Promise<boolean>;
        /**
         * Checks whether this **Preferences** instance contains the KV pair of the given key. This API returns the result
         * synchronously.
         *
         * @param { string } key - Key to be checked. The value cannot be empty. For details about its maximum length, see
         *     [MAX_KEY_LENGTH](docroot://reference/apis-arkdata/js-apis-data-preferences.md#constants).
         * @returns { boolean } If the **Preferences** instance contains the KV pair, **true** will be returned. Otherwise,
         *     **false** will be returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        hasSync(key: string): boolean;
        /**
         * Writes data to this **Preferences** instance. This API uses an asynchronous callback to return the result. You
         * can use [flush]{@link preferences.Preferences.flush(callback: AsyncCallback<void>)} to persist the
         * **Preferences** instance.
         *
         * @param { string } key - Key to be modified. The value cannot be empty. For details about its maximum length, see
         *     [MAX_KEY_LENGTH](docroot://reference/apis-arkdata/js-apis-data-preferences.md#constants).
         * @param { ValueType } value - Value to write.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        put(key: string, value: ValueType, callback: AsyncCallback<void>): void;
        /**
         * Writes data to this **Preferences** instance. This API uses a promise to return the result. You can use
         * [flush]{@link preferences.Preferences.flush(callback: AsyncCallback<void>)} to persist the **Preferences**
         * instance.
         *
         * @param { string } key - Key to be modified. The value cannot be empty. For details about its maximum length, see
         *     [MAX_KEY_LENGTH](docroot://reference/apis-arkdata/js-apis-data-preferences.md#constants).
         * @param { ValueType } value - Value to write.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        put(key: string, value: ValueType): Promise<void>;
        /**
         * Writes data to this **Preferences** instance. This API returns the result synchronously. You can use
         * [flush]{@link preferences.Preferences.flush(callback: AsyncCallback<void>)} to persist the **Preferences**
         * instance.
         *
         * @param { string } key - Key to be modified. The value cannot be empty. For details about its maximum length, see
         *     [MAX_KEY_LENGTH](docroot://reference/apis-arkdata/js-apis-data-preferences.md#constants).
         * @param { ValueType } value - Value to write.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        putSync(key: string, value: ValueType): void;
        /**
         * Deletes a KV pair from this **Preferences** instance. This API uses an asynchronous callback to return the
         * result. You can use [flush]{@link preferences.Preferences.flush(callback: AsyncCallback<void>)} to persist the
         * **Preferences** instance.
         *
         * @param { string } key - Key to be deleted. The value cannot be empty. For details about its maximum length, see
         *     [MAX_KEY_LENGTH](docroot://reference/apis-arkdata/js-apis-data-preferences.md#constants).
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        delete(key: string, callback: AsyncCallback<void>): void;
        /**
         * Deletes a KV pair from this **Preferences** instance. This API uses a promise to return the result. You can use
         * [flush]{@link preferences.Preferences.flush(callback: AsyncCallback<void>)} to persist the **Preferences**
         * instance.
         *
         * @param { string } key - Key to be deleted. The value cannot be empty. For details about its maximum length, see
         *     [MAX_KEY_LENGTH](docroot://reference/apis-arkdata/js-apis-data-preferences.md#constants).
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        delete(key: string): Promise<void>;
        /**
         * Deletes a KV pair from this **Preferences** instance. This API returns the result synchronously. You can use
         * [flush]{@link preferences.Preferences.flush(callback: AsyncCallback<void>)} to persist the **Preferences**
         * instance.
         *
         * @param { string } key - Key to be deleted. The value cannot be empty. For details about its maximum length, see
         *     [MAX_KEY_LENGTH](docroot://reference/apis-arkdata/js-apis-data-preferences.md#constants).
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        deleteSync(key: string): void;
        /**
         * Clears this **Preferences** instance. This API uses an asynchronous callback to return the result. You can use
         * [flush]{@link preferences.Preferences.flush(callback: AsyncCallback<void>)} to persist the **Preferences**
         * instance.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Mandatory parameters are left unspecified.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        clear(callback: AsyncCallback<void>): void;
        /**
         * Clears this **Preferences** instance. This API uses a promise to return the result. You can use
         * [flush]{@link preferences.Preferences.flush(callback: AsyncCallback<void>)} to persist the **Preferences**
         * instance.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        clear(): Promise<void>;
        /**
         * Clears this **Preferences** instance. This API returns the result synchronously. You can use
         * [flush]{@link preferences.Preferences.flush(callback: AsyncCallback<void>)} to persist the **Preferences**
         * instance.
         *
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        clearSync(): void;
        /**
         * Flushes the data in this **Preferences** instance to the persistent file. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Mandatory parameters are left unspecified.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        flush(callback: AsyncCallback<void>): void;
        /**
         * Flushes the data in this **Preferences** instance to the persistent file. This API uses a promise to return the
         * result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        flush(): Promise<void>;
        /**
         * Flushes the data in the cached **Preferences** instance to the persistent file.
         *
         * @throws { BusinessError } 15500000 - Inner error.
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        flushSync(): void;
        /**
         * Subscribes to data changes. The registered callback will be invoked to return the new value if the data change is
         * [flushed]{@link preferences.Preferences.flush(callback: AsyncCallback<void>)}.
         *
         * @param { 'change' } type - Event type. The value is **'change'**, which indicates data changes.
         * @param { Callback<{ key: string }> } callback - Callback used to return the data change. [since 9 - 9]
         * @param { Function } callback - Callback used to return the data change. [since 10 - 10]
         * @param { Callback<string> } callback - Callback used to return the data change. [since 11]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        on(type: 'change', callback: Callback<string>): void;
        /**
         * Subscribes to data changes between processes. When multiple processes hold the same preference file, calling
         * [flush]{@link preferences.Preferences.flush(callback: AsyncCallback<void>)} in any process (including the current
         * process) will trigger the callback in this API.
         * This API is provided for applications that have applied for [dataGroupId]{@link preferences.Options}. Avoid using
         * this API for the applications that have not applied for **dataGroupId** because calling it in multiple process
         * may damage the persistent files and cause data loss.
         *
         * @param { 'multiProcessChange' } type - Event type. The value is **'multiProcessChange'**, which indicates inter-
         *     process data changes.
         * @param { Function } callback - Callback used to return the data change. [since 10 - 10]
         * @param { Callback<string> } callback - Callback used to return the data change. [since 11]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500019 - Failed to obtain the subscription service.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @atomicservice [since 11]
         * @since 10
         */
        on(type: 'multiProcessChange', callback: Callback<string>): void;
        /**
         * Subscribes to changes of specific data. The registered callback will be invoked only after the values of the
         * specified keys are changed and [flushed]{@link preferences.Preferences.flush(callback: AsyncCallback<void>)}.
         *
         * @param { 'dataChange' } type - Event type. The value is **'dataChange'**, which indicates data changes.
         * @param { Array<string> } keys - Array of the keys to be observed.
         * @param { Callback<Record<string, ValueType>> } callback - Callback used to return the changed data, in an array
         *     of KV pairs. The keys identify the data changed, and the values are the new values. The values support the
         *     following data types: number, string, boolean, Array<number>, Array<string>, Array< boolean>, Uint8Array, and
         *     object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types;
         *     3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error.
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 20]
         * @atomicservice
         * @since 12
         */
        on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void;
        /**
         * Unsubscribes from data changes.
         *
         * @param { 'change' } type - Event type. The value is **'change'**, which indicates data changes.
         * @param { Callback<{ key: string }> } callback - Callback to unregister. If this parameter is not specified, this
         *     API unregisters all callbacks for data changes. [since 9 - 9]
         * @param { Function } callback - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for data changes. [since 10 - 10]
         * @param { Callback<string> } callback - Callback to unregister. If this parameter is not specified, this API
         *     unregisters all callbacks for data changes. [since 11]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        off(type: 'change', callback?: Callback<string>): void;
        /**
         * Unsubscribes from inter-process data changes.
         * This API is provided for applications that have applied for [dataGroupId]{@link preferences.Options}. Avoid using
         * this API for the applications that have not applied for **dataGroupId** because calling it in multiple process
         * may damage the persistent files and cause data loss.
         *
         * @param { 'multiProcessChange' } type - Event type. The value is **'multiProcessChange'**, which indicates inter-
         *     process data changes.
         * @param { Function } callback - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for data changes. [since 10 - 10]
         * @param { Callback<string> } callback - Callback to unregister. If this parameter is not specified, this API
         *     unregisters all callbacks for data changes. [since 11]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error. [since 11]
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @atomicservice [since 11]
         * @since 10
         */
        off(type: 'multiProcessChange', callback?: Callback<string>): void;
        /**
         * Unsubscribes from changes of specific data.
         *
         * @param { 'dataChange' } type - Event type. The value is **'dataChange'**, which indicates data changes.
         * @param { Array<string> } keys - Array of keys to be unsubscribed from. If this parameter is left empty, all keys
         *     are unsubscribed from.
         * @param { Callback<Record<string, ValueType>> } callback - Callback to unregister. If this parameter is not
         *     specified, this API unregisters all callbacks for the changes of the specified data.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 15500000 - Inner error.
         * @syscap SystemCapability.DistributedDataManager.Preferences.Core
         * @crossplatform [since 20]
         * @atomicservice
         * @since 12
         */
        off(type: 'dataChange', keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void;
    }
}
export default preferences;

```
