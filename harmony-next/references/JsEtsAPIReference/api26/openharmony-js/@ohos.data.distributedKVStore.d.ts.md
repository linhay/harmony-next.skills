# @ohos.data.distributedKVStore.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022 Huawei Device Co., Ltd.
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
 * @kit ArkData
 */
import { AsyncCallback, Callback } from './@ohos.base';
import BaseContext from './application/BaseContext';
/**
 * The **distributedKVStore** module implements collaboration between databases for different devices that form a Super
 * Device. You can use the APIs provided by this module to save application data to a distributed key-value (KV) store
 * and perform operations, such as adding, deleting, modifying, and querying data, and synchronizing data across
 * devices.
 * The **distributedKVStore** module provides the following functionalities:
 *
 * - [KVManager]{@link distributedKVStore.KVManagerConfig}: provides a **KVManager** instance to obtain KV store
 * information.
 * - [KVStoreResultSet]{@link distributedKVStore.KVStoreResultSet}: provides APIs for accessing the results obtained
 * from a KV store.
 * - [Query]{@link distributedKVStore.Query}: provides APIs for setting predicates for data query.
 * - [SingleKVStore]{@link distributedKVStore.SingleKVStore}: provides APIs for querying data in single KV stores and
 * synchronizing data across devices. The single KV stores manage data without distinguishing devices.
 * - [DeviceKVStore]{@link distributedKVStore.DeviceKVStore}: provides APIs for querying data in device KV stores and
 * synchronizing data across devices. This class inherits from [SingleKVStore]{@link distributedKVStore.SingleKVStore}.
 * The device KV stores manage data by device.
 *
 * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
 * @crossplatform [since 24]
 * @since 9
 */
declare namespace distributedKVStore {
    /**
     * Provides the **KVManager** instance configuration, including the bundle name of the invoker and the application
     * context.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @crossplatform [since 24]
     * @since 9
     */
    interface KVManagerConfig {
        /**
         * Bundle name.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        bundleName: string;
        /**
         * Application context.
         *
         * For details about the application context of the FA model, see
         * [Context](../apis-ability-kit/js-apis-inner-app-context.md).
         *
         * For details about the application context of the stage model, see
         * [Context](../apis-ability-kit/js-apis-inner-application-uiAbilityContext.md).
         *
         * Since API version 10, the parameter type of context is
         * [BaseContext](../apis-ability-kit/js-apis-inner-application-baseContext.md).
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         *     if swap the area, you should close all the KV store and use the new Context to create the KVManager [since 9 - 23]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         *     if swap the area, you should close all the KV store and use the new BaseContext to create the KVManager [since 10]
         * @crossplatform [since 24]
         * @since 9
         */
        context: BaseContext;
    }
    /**
     * Provides constants of the distributed KV store.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @crossplatform [since 24]
     * @since 9
     */
    interface Constants {
        /**
         * Maximum length of a key in the database, which is 1024 bytes.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        readonly MAX_KEY_LENGTH: number;
        /**
         * Maximum length of a value in the database, which is 4194303 bytes.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        readonly MAX_VALUE_LENGTH: number;
        /**
         * Maximum length of a key in a device KV store, which is 896 bytes.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        readonly MAX_KEY_LENGTH_DEVICE: number;
        /**
         * Maximum length of a KV store ID, which is 128 bytes.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        readonly MAX_STORE_ID_LENGTH: number;
        /**
         * Maximum query length, which is 512000 bytes.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        readonly MAX_QUERY_LENGTH: number;
        /**
         * Maximum number of batch operations allowed, which is 128.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        readonly MAX_BATCH_SIZE: number;
    }
    /**
     * Indicates the {@code ValueType}.
     *
     * <p>{@code ValueType} is obtained based on the value.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @crossplatform [since 24]
     * @since 9
     */
    enum ValueType {
        /**
         * Indicates that the value type is string.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        STRING = 0,
        /**
         * Indicates that the value type is int.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        INTEGER = 1,
        /**
         * Indicates that the value type is float.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        FLOAT = 2,
        /**
         * Indicates that the value type is byte array.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        BYTE_ARRAY = 3,
        /**
         * Indicates that the value type is boolean.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        BOOLEAN = 4,
        /**
         * Indicates that the value type is double.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        DOUBLE = 5
    }
    /**
     * Defines the **value** object in a KV store.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @crossplatform [since 24]
     * @since 9
     */
    interface Value {
        /**
         * Type of the value.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         * @see ValueType
         */
        type: ValueType;
        /**
         * Value of the KV pair.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        value: Uint8Array | string | number | boolean;
    }
    /**
     * Provides key-value pairs stored in the distributedKVStore.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @crossplatform [since 24]
     * @since 9
     */
    interface Entry {
        /**
         * Indicates the key
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        key: string;
        /**
         * Indicates the value
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        value: Value;
    }
    /**
     * Defines the content of a data change notification, including inserted data, updated data, deleted data, and device
     * ID.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 9
     */
    interface ChangeNotification {
        /**
         * Data inserted.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        insertEntries: Entry[];
        /**
         * Data updated.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        updateEntries: Entry[];
        /**
         * Data deleted.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        deleteEntries: Entry[];
        /**
         * UUID of the device.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        deviceId: string;
    }
    /**
     * Enumerates the sync modes.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 9
     */
    enum SyncMode {
        /**
         * Indicates that data is only pulled from the remote end.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        PULL_ONLY,
        /**
         * Indicates that data is only pushed from the local end.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        PUSH_ONLY,
        /**
         * Indicates that data is pushed from the local end, and then pulled from the remote end.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        PUSH_PULL
    }
    /**
     * Enumerates the subscription types.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 9
     */
    enum SubscribeType {
        /**
         * Subscription to local data changes
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        SUBSCRIBE_TYPE_LOCAL,
        /**
         * Subscription to remote data changes
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        SUBSCRIBE_TYPE_REMOTE,
        /**
         * Subscription to both local and remote data changes
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        SUBSCRIBE_TYPE_ALL
    }
    /**
     * Enumerates the distributed KV store types.
     * | Name                | Value| Description                                                        |
     * | -------------------- | - | ------------------------------------------------------------ |
     * | DEVICE_COLLABORATION | 0 | Device KV store.<br>The device KV store manages data by device, which eliminates
     * conflicts. Data can be queried by device.<br>**System capability**:
     * SystemCapability.DistributedDataManager.KVStore.DistributedKVStore|
     * | SINGLE_VERSION       | 1 | Single KV store.<br>The single KV store does not differentiate data by device. If
     * entries with the same key are modified on different devices, the value will be overwritten.<br>**System
     * capability**: SystemCapability.DistributedDataManager.KVStore.Core|
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @crossplatform [since 24]
     * @since 9
     */
    enum KVStoreType {
        /**
         * Device-collaboration database, as specified by {@code DeviceKVStore}
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        DEVICE_COLLABORATION,
        /**
         * Single-version database, as specified by {@code SingleKVStore}
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        SINGLE_VERSION
    }
    /**
     * Enumerates the KV store security levels.
     *
     * > **NOTE**
     * >
     * > For the scenarios involving a single device, you can upgrade the security level of a KV store by modifying the
     * > **securityLevel** parameter. When upgrading the database security level, observe the following:
     * >
     * > * This operation does not apply to the databases that require cross-device sync. Data cannot be synced between
     * > databases of different security levels. If you want to upgrade the security level of a database, you are advised
     * > to create a database of a higher security level.
     * >
     * > * You need to close the database before modifying the **securityLevel** parameter, and open it after the security
     * >  level is upgraded.
     * >
     * > * You cannot downgrade the database security level. For example, you can change the database security level from
     * > S2 to S3, but cannot change it from S3 to S2.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @crossplatform [since 24]
     * @since 9
     */
    enum SecurityLevel {
        /**
         * S1: means the db is in the low security level
         * There are some low impact when the data is leaked.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        S1,
        /**
         * S2: means the db is in the middle security level
         * There are some major impact when the data is leaked.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        S2,
        /**
         * S3: means the db is in the high security level
         * There are some severity impact when the data is leaked.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        S3,
        /**
         * S4: means the db is in the critical security level
         * There are some critical impact when the data is leaked.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        S4
    }
    /**
     * Provides KV store configuration.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @crossplatform [since 24]
     * @since 9
     */
    interface Options {
        /**
         * Whether to create a database when database files do not exist. The value **true** means to create a database, and
         *  the value **false** means the opposite. The default value is **true**.
         *
         * SystemCapability.DistributedDataManager.KVStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        createIfMissing?: boolean;
        /**
         * Whether to encrypt the database files. The value **true** means to encrypt the database files, and the value
         * **false** means the opposite. The default value is **false**.
         *
         * SystemCapability.DistributedDataManager.KVStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        encrypt?: boolean;
        /**
         * Whether to back up the database files. The value **true** means to back up the database files, and the value
         * **false** means the opposite. The default value is **true**.
         *
         * SystemCapability.DistributedDataManager.KVStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        backup?: boolean;
        /**
         * Whether to enable auto sync across devices. The default value is **false**, indicating that only manual sync is
         * supported. If this parameter is set to **true**, <!--RP1-->it takes effect only in
         * [device collaboration using cross-device calls](docroot://application-models/hop-multi-device-collaboration.md#using-cross-device-call)
         * .<!--RP1End-->
         *
         * SystemCapability.DistributedDataManager.KVStore.Core
         *
         * ohos.permission.DISTRIBUTED_DATASYNC
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        autoSync?: boolean;
        /**
         * Type of the KV store to create. The default value is **DEVICE_COLLABORATION**, which indicates a device KV store.
         *
         * SystemCapability.DistributedDataManager.KVStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        kvStoreType?: KVStoreType;
        /**
         * Security level of the KV store.
         *
         * SystemCapability.DistributedDataManager.KVStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        securityLevel: SecurityLevel;
        /**
         * Schema that defines the values stored in the KV store. The default value is **undefined**, which means no schema
         * is used.
         *
         * SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        schema?: Schema;
        /**
         * Specifies the root directory relative to the database
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 24
         */
        rootDir?: string;
    }
    /**
     * Provides backup config to backup or restore KVStore.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 24
     */
    interface BackupConfig {
        /**
         * Specifies the file name to the backup database
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 24
         */
        fileName: string;
        /**
         * Specifies the root directory relative to the backup database
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 24
         */
        filePath: string;
    }
    /**
     * Defines the schema of a KV store. You can create a **Schema** object and pass it in
     * [Options]{@link distributedKVStore.Options} when creating or opening a KV store.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
     * @crossplatform [since 24]
     * @since 9
     */
    class Schema {
        /**
         * Defines a constructor used to create a **Schema** instance.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        constructor();
        /**
         * Get the root json object.
         *
         * @returns { FieldNode } returns the root json object.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        get root(): FieldNode;
        /**
         * Set the root json object.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        set root(root: FieldNode);
        /**
         * Get the string array of json.
         *
         * @returns { Array<string> } returns the string array of json.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        get indexes(): Array<string>;
        /**
         * Set the string array of json.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        set indexes(indexes: Array<string>);
        /**
         * Get the mode of schema.
         *
         * @returns { number } returns the mode of schema.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        get mode(): number;
        /**
         * Set the mode of schema.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        set mode(mode: number);
        /**
         * Get the skip size of schema.
         *
         * @returns { number } returns the skip size of schema.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        get skip(): number;
        /**
         * Set the skip size of schema.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        set skip(skip: number);
    }
    /**
     * Represents a **Schema** instance, which provides the methods for defining the values stored in a KV store.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
     * @crossplatform [since 24]
     * @since 9
     */
    class FieldNode {
        /**
         * Defines a constructor used to create a **FieldNode** instance with a string field.
         *
         * @param { string } name - Value of **FieldNode**, with a maximum of 64 characters. This parameter cannot be left blank.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        constructor(name: string);
        /**
         * Appends a child node to this **FieldNode**.
         *
         * @param { FieldNode } child - Child node to append.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        appendChild(child: FieldNode): boolean;
        /**
         * Indicates the default value of field node.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        default: string;
        /**
         * Get the nullable of database field.
         *
         * @returns { boolean } returns the nullable of database field.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        get nullable(): boolean;
        /**
         * Set the nullable of database field.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        set nullable(isnullable: boolean);
        /**
         * Get the type of value.
         *
         * @returns { number } returns the type of value.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        get type(): number;
        /**
         * Set the type of value.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @crossplatform [since 24]
         * @since 9
         */
        set type(type: number);
    }
    /**
     * Provides APIs for obtaining the distributed KV store result sets. A maximum of eight result sets can be opened at a
     *  time.
     * The **KVStoreResultSet** instance is not refreshed in real time. After using the result set, if the data in the
     * database is changed (by being added, deleted, or modified), you need to query the result set again to obtain the
     * latest data.
     * Before calling any API in **KVStoreResultSet**, you must use **
     * [getKVStore]{@link distributedKVStore.KVManager.getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>)}
     * ** to construct a **SingleKVStore** or **DeviceKVStore** instance.
     *
     * > **NOTE**
     * >
     * > The cursor start position of **KVStoreResultSet** is **-1**.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @crossplatform [since 24]
     * @since 9
     */
    interface KVStoreResultSet {
        /**
         * Obtains the total number of rows in the result set.
         *
         * @returns { number } Total number of rows obtained.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getCount(): number;
        /**
         * Obtains the current data read position (position from which data is read) in the result set. The read position
         * changes with the operations, such as [moveToFirst]{@link distributedKVStore.KVStoreResultSet.moveToFirst} and
         * [moveToLast]{@link distributedKVStore.KVStoreResultSet.moveToLast}.
         *
         * @returns { number } Current data read position obtained. The value must be greater than or equal to **-1**. The value **-1
         *     ** means no data is read; the value **0** indicates the first row.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getPosition(): number;
        /**
         * Moves the data read position to the first row. If the result set is empty, **false** will be returned.
         *
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        moveToFirst(): boolean;
        /**
         * Moves the data read position to the last row. If the result set is empty, **false** will be returned.
         *
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        moveToLast(): boolean;
        /**
         * Moves the data read position to the next row. If the result set is empty, **false** will be returned. This API
         * applies when the whole result set is obtained.
         *
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        moveToNext(): boolean;
        /**
         * Moves the data read position to the previous row. If the result set is empty, **false** will be returned. This
         * API applies when the whole result set is obtained.
         *
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        moveToPrevious(): boolean;
        /**
         * Moves the data read position with the specified offset from the current position. That is, moves the number of
         * rows specified by **offset** from the current position.
         *
         * @param { number } offset - Offset to move the data read position. A positive value means to move forward; a negative value
         *     means to move backward. If the cursor is beyond the start or end position of the result set, **false** is returned.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        move(offset: number): boolean;
        /**
         * Moves the data read position from 0 to an absolute position.
         *
         * @param { number } position - Absolute position to move to. If the absolute position exceeds the start or end position of
         *     the result set, **false** is returned.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        moveToPosition(position: number): boolean;
        /**
         * Checks whether the data read position is the first row.
         *
         * @returns { boolean } Returns **true** if the first row is being read; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        isFirst(): boolean;
        /**
         * Checks whether the data read position is the last row.
         *
         * @returns { boolean } Returns **true** if the last row is being read; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        isLast(): boolean;
        /**
         * Checks whether the data read position is before the first row.
         *
         * @returns { boolean } Returns **true** if the data read position is before the first row; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        isBeforeFirst(): boolean;
        /**
         * Checks whether the data read position is after the last row.
         *
         * @returns { boolean } Returns **true** if the data read position is after the last row; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        isAfterLast(): boolean;
        /**
         * Obtains the KV pair from the current position.
         *
         * @returns { Entry } KV pair obtained.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getEntry(): Entry;
    }
    /**
     * Provides methods to create a **Query** object, which defines different data query criteria. A **Query** object
     * supports a maximum of 256 predicates.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @crossplatform [since 24]
     * @since 9
     */
    class Query {
        /**
         * Defines a constructor used to create a **Query** instance.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        constructor();
        /**
         * Resets the **Query** object.
         *
         * @returns { Query } **Query** object reset.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        reset(): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is equal to the given value.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @param { number | string | boolean } value - Value specified.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        equalTo(field: string, value: number | string | boolean): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is not equal to the specified value.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @param { number | string | boolean } value - Value specified.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        notEqualTo(field: string, value: number | string | boolean): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is greater than the specified value.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Indicates the field, which cannot contain ^.
         * @param { number | string | boolean } value - Indicates the value to be compared.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        greaterThan(field: string, value: number | string | boolean): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is less than the specified value.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @param { number | string } value - Value specified.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        lessThan(field: string, value: number | string): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is greater than or equal to the specified
         * value.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @param { number | string } value - Value specified.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        greaterThanOrEqualTo(field: string, value: number | string): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is less than or equal to the specified value.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @param { number | string } value - Value specified.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        lessThanOrEqualTo(field: string, value: number | string): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is **null**.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        isNull(field: string): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is within the specified list of numbers.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @param { number[] } valueList - List of numbers.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        inNumber(field: string, valueList: number[]): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is within the specified list of strings.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @param { string[] } valueList - List of strings.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        inString(field: string, valueList: string[]): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is not within the specified list of numbers.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @param { number[] } valueList - List of numbers.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        notInNumber(field: string, valueList: number[]): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is not within the specified list of strings.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @param { string[] } valueList - List of strings.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        notInString(field: string, valueList: string[]): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is similar to the specified string.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @param { string } value - String specified.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        like(field: string, value: string): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is not similar to the specified string.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @param { string } value - String specified.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        unlike(field: string, value: string): Query;
        /**
         * Creates a **Query** object with the AND condition.
         *
         * @returns { Query } **Query** object created.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        and(): Query;
        /**
         * Creates a **Query** object with the OR condition.
         *
         * @returns { Query } **Query** object created.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        or(): Query;
        /**
         * Creates a **Query** object to sort the query results in ascending order.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        orderByAsc(field: string): Query;
        /**
         * Creates a **Query** object to sort the query results in descending order.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        orderByDesc(field: string): Query;
        /**
         * Creates a **Query** object to specify the number of records of the query result and where to start. This API must
         *  be called after the invocation of the **orderByAsc()**, **orderByDesc()**, and the query APIs of the **Query**
         * object.
         *
         * @param { number } total - Maximum number of results to query. The value must be a non-negative integer.<br>If the value is
         *     a negative number, the entire result set is queried.
         * @param { number } offset - Start position of the query result. The value must be a non-negative integer.<br>If the value is
         *     a negative number, the entire result set is queried.<br>If **offset** exceeds the end of the result set, the query
         *     result is empty.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        limit(total: number, offset: number): Query;
        /**
         * Creates a **Query** object to match the specified field whose value is not **null**.
         *
         * > **NOTE**
         * >
         * > This API should be used together with [Schema]{@link distributedKVStore.Schema}.
         * >
         * > For details about how to use **Schema** to create a database, see the example of creating and obtaining a KV
         * > store using the **getKVStore()** method in
         * > [Persisting KV Store Data](docroot://database/data-persistence-by-kv-store.md#how-to-develop).
         *
         * @param { string } field - Field to match. It cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        isNotNull(field: string): Query;
        /**
         * Creates a **Query** object for a query condition group with a left parenthesis.
         *
         * @returns { Query } **Query** object created.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        beginGroup(): Query;
        /**
         * Creates a **Query** object for a query condition group with a right parenthesis.
         *
         * @returns { Query } **Query** object created.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        endGroup(): Query;
        /**
         * Creates a **Query** object with a specified key prefix.
         *
         * @param { string } prefix - Key prefix, which cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        prefixKey(prefix: string): Query;
        /**
         * Creates a **Query** object with an index preferentially used for query.
         *
         * @param { string } index - Index to set, which cannot contain '^'. If the value contains '^', the predicate becomes
         *     invalid and all data in the KV store will be returned.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        setSuggestIndex(index: string): Query;
        /**
         * Creates a **Query** object with the device ID as the key prefix.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - ID of the device to be queried. This parameter cannot be left empty.
         * @returns { Query } **Query** object created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        deviceId(deviceId: string): Query;
        /**
         * Obtains the query statement of the **Query** object.
         *
         * @returns { string } Returns the query statement obtained.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getSqlLike(): string;
    }
    /**
     * Provides APIs for data management in a single KV store, such as adding data, deleting data, and subscribing to data
     *  changes or across-device data sync completion events.
     * Before calling any method in **SingleKVStore**, you must use
     * [getKVStore]{@link distributedKVStore.KVManager.getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>)}
     *  to obtain a **SingleKVStore** instance.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @crossplatform [since 24]
     * @since 9
     */
    interface SingleKVStore {
        /**
         * Adds a KV pair of the specified type to this KV store. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { string } key - Key of the KV pair to add. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @param { Uint8Array | string | number | boolean } value - Value of the KV pair to add. The value type can be Uint
         *     8Array, long , double, string, or boolean. A value of the Uint8Array or string type cannot exceed
         *     [MAX_VALUE_LENGTH]{@link distributedKVStore.Constants}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void;
        /**
         * Adds a KV pair of the specified type to this KV store. This API uses a promise to return the result.
         *
         * @param { string } key - Key of the KV pair to add. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @param { Uint8Array | string | number | boolean } value - Value of the KV pair to add. The value type can be Uint
         *     8Array, long , double, string, or boolean. A value of the Uint8Array or string type cannot exceed
         *     [MAX_VALUE_LENGTH]{@link distributedKVStore.Constants}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        put(key: string, value: Uint8Array | string | number | boolean): Promise<void>;
        /**
         * Batch inserts KV pairs to this single KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { Entry[] } entries - KV pairs to insert, which cannot exceed 512 MB.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        putBatch(entries: Entry[], callback: AsyncCallback<void>): void;
        /**
         * Batch inserts KV pairs to this single KV store. This API uses a promise to return the result.
         *
         * @param { Entry[] } entries - KV pairs to insert, which cannot exceed 512 MB.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        putBatch(entries: Entry[]): Promise<void>;
        /**
         * Deletes a KV pair from this KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { string } key - Key of the KV pair to delete. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        delete(key: string, callback: AsyncCallback<void>): void;
        /**
         * Deletes a KV pair from this KV store. This API uses a promise to return the result.
         *
         * @param { string } key - Key of the KV pair to delete. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        delete(key: string): Promise<void>;
        /**
         * Batch deletes KV pairs from this single KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { string[] } keys - KV pairs to delete. This parameter cannot be empty.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        deleteBatch(keys: string[], callback: AsyncCallback<void>): void;
        /**
         * Batch deletes KV pairs from this single KV store. This API uses a promise to return the result.
         *
         * @param { string[] } keys - KV pairs to delete. This parameter cannot be empty.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        deleteBatch(keys: string[]): Promise<void>;
        /**
         * Deletes data of a device. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > **deviceId** is **networkId** in
         * > [DeviceBasicInfo]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceBasicInfo}, which can be
         * > obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - Network ID of the target device.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void;
        /**
         * Deletes data of a device. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > **deviceId** is **networkId** in
         * > [DeviceBasicInfo]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceBasicInfo}, which can be
         * > obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - Network ID of the target device.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        removeDeviceData(deviceId: string): Promise<void>;
        /**
         * Obtains the value of the specified key. This API uses an asynchronous callback to return the result.
         *
         * @param { string } key - Key of the value to obtain. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @param { AsyncCallback<boolean | string | number | Uint8Array> } callback - Callback used to return the value
         *     obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void;
        /**
         * Obtains the value of the specified key. This API uses a promise to return the result.
         *
         * @param { string } key - Key of the value to obtain. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @returns { Promise<boolean | string | number | Uint8Array> } Promise used to return the value obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        get(key: string): Promise<boolean | string | number | Uint8Array>;
        /**
         * Obtains all KV pairs that match the specified key prefix. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { string } keyPrefix - Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and
         *     all data in the RDB store will be returned.
         * @param { AsyncCallback<Entry[]> } callback - Callback used to return the KV pairs that match the specified prefix.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getEntries(keyPrefix: string, callback: AsyncCallback<Entry[]>): void;
        /**
         * Obtains all KV pairs that match the specified key prefix. This API uses a promise to return the result.
         *
         * @param { string } keyPrefix - Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and
         *     all data in the RDB store will be returned.
         * @returns { Promise<Entry[]> } Promise used to return the KV pairs that match the specified prefix.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getEntries(keyPrefix: string): Promise<Entry[]>;
        /**
         * Obtains the KV pairs that match the specified **Query** object. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { Query } query - Key prefix to match.
         * @param { AsyncCallback<Entry[]> } callback - Callback used to return the KV pairs that match the specified **Query**
         *     object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getEntries(query: Query, callback: AsyncCallback<Entry[]>): void;
        /**
         * Obtains the KV pairs that match the specified **Query** object. This API uses a promise to return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<Entry[]> } Promise used to return the KV pairs that match the specified **Query** object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getEntries(query: Query): Promise<Entry[]>;
        /**
         * Obtains a result set with the specified prefix from this single KV store. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { string } keyPrefix - Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and
         *     all data in the RDB store will be returned.
         * @param { AsyncCallback<KVStoreResultSet> } callback - Callback used to return the result set with the specified prefix.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 15100001 - Over max limits. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void;
        /**
         * Obtains a result set with the specified prefix from this single KV store. This API uses a promise to return the
         * result.
         *
         * @param { string } keyPrefix - Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and
         *     all data in the RDB store will be returned.
         * @returns { Promise<KVStoreResultSet> } Promise used to return the result set with the specified prefix.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 15100001 - Over max limits. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getResultSet(keyPrefix: string): Promise<KVStoreResultSet>;
        /**
         * Obtains a **KVStoreResultSet** object that matches the specified **Query** object. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<KVStoreResultSet> } callback - Callback used to return the **KVStoreResultSet** object obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 15100001 - Over max limits. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getResultSet(query: Query, callback: AsyncCallback<KVStoreResultSet>): void;
        /**
         * Obtains a **KVStoreResultSet** object that matches the specified **Query** object. This API uses a promise to
         * return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<KVStoreResultSet> } Promise used to return the **KVStoreResultSet** object obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 15100001 - Over max limits. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getResultSet(query: Query): Promise<KVStoreResultSet>;
        /**
         * Closes the **KVStoreResultSet** object returned by
         * [SingleKvStore.getResultSet]{@link distributedKVStore.SingleKVStore.getResultSet(keyPrefix: string)}. This API
         * uses an asynchronous callback to return the result.
         *
         * @param { KVStoreResultSet } resultSet - **KVStoreResultSet** object to close.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        closeResultSet(resultSet: KVStoreResultSet, callback: AsyncCallback<void>): void;
        /**
         * Closes the **KVStoreResultSet** object returned by
         * [SingleKvStore.getResultSet]{@link distributedKVStore.SingleKVStore.getResultSet(keyPrefix: string)}. This API
         * uses a promise to return the result.
         *
         * @param { KVStoreResultSet } resultSet - **KVStoreResultSet** object to close.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        closeResultSet(resultSet: KVStoreResultSet): Promise<void>;
        /**
         * Obtains the number of results that match the specified **Query** object. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<number> } callback - Callback used to return the number of results obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getResultSize(query: Query, callback: AsyncCallback<number>): void;
        /**
         * Obtains the number of results that match the specified **Query** object. This API uses a promise to return the
         * result.
         *
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<number> } Promise used to return the number of results obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getResultSize(query: Query): Promise<number>;
        /**
         * Backs up a distributed KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { string } file - Name of the KV store. The value cannot be empty or exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        backup(file: string, callback: AsyncCallback<void>): void;
        /**
         * Backs up an RDB store. This API uses a promise to return the result.
         *
         * @param { string } file - Name of the KV store. The value cannot be empty or exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        backup(file: string): Promise<void>;
        /**
         * Backs up a database by specifying {@code BackupConfig}.
         *
         * @param { BackupConfig } backupConfig - Indicates the {@code BackupConfig} object for backup database.
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 15100000 - Input parameters do not meet the API requirements, such as invalid value
         *     ranges, length limits, or incorrect formats.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 24
         */
        backupEx(backupConfig: BackupConfig): Promise<void>;
        /**
         * Restores a distributed KV store from a database file. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { string } file - Name of the database file. The value cannot be empty or exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        restore(file: string, callback: AsyncCallback<void>): void;
        /**
         * Restores a distributed KV store from a database file. This API uses a promise to return the result.
         *
         * @param { string } file - Name of the database file. The value cannot be empty or exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        restore(file: string): Promise<void>;
        /**
         * Restores a database by specifying {@code BackupConfig}.
         *
         * @param { BackupConfig } backupConfig - Indicates the {@code BackupConfig} object for restore database.
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 15100000 - Input parameters do not meet the API requirements, such as invalid value
         *     ranges, length limits, or incorrect formats.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 24
         */
        restoreEx(backupConfig: BackupConfig): Promise<void>;
        /**
         * Deletes a backup file. This API uses an asynchronous callback to return the result.
         *
         * @param { Array<string> } files - Name of the backup file to delete. The value cannot be empty or exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @param { AsyncCallback<Array<[ string, number ]>> } callback - Callback used to return the name of the backup file deleted
         *     and the operation result.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        deleteBackup(files: Array<string>, callback: AsyncCallback<Array<[
            string,
            number
        ]>>): void;
        /**
         * Deletes a backup file. This API uses a promise to return the result.
         *
         * @param { Array<string> } files - Name of the backup file to delete. The value cannot be empty or exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @returns { Promise<Array<[ string, number ]>> } Promise used to return the name of the backup file deleted and the operation
         *     result.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        deleteBackup(files: Array<string>): Promise<Array<[
            string,
            number
        ]>>;
        /**
         * Delete database backup file by specifying {@code BackupConfig}.
         *
         * @param { BackupConfig } backupConfig - Indicates the {@code BackupConfig} object for delete backup file.
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 15100000 - Input parameters do not meet the API requirements, such as invalid value
         *     ranges, length limits, or incorrect formats.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 24
         */
        deleteBackupEx(backupConfig: BackupConfig): Promise<void>;
        /**
         * Starts the transaction in this single KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        startTransaction(callback: AsyncCallback<void>): void;
        /**
         * Starts the transaction in this single KV store. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        startTransaction(): Promise<void>;
        /**
         * Commits the transaction in this single KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        commit(callback: AsyncCallback<void>): void;
        /**
         * Commits the transaction in this single KV store. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        commit(): Promise<void>;
        /**
         * Rolls back the transaction in this single KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        rollback(callback: AsyncCallback<void>): void;
        /**
         * Rolls back the transaction in this single KV store. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        rollback(): Promise<void>;
        /**
         * Sets cross-device data sync, which can be enabled or disabled. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { boolean } enabled - Whether to enable data sync across devices. The value **true** means to enable data sync
         *     across devices, and the value **false** means the opposite.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        enableSync(enabled: boolean, callback: AsyncCallback<void>): void;
        /**
         * Sets cross-device data sync, which can be enabled or disabled. This API uses a promise to return the result.
         *
         * @param { boolean } enabled - Whether to enable data sync across devices. The value **true** means to enable data sync
         *     across devices, and the value **false** means the opposite.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        enableSync(enabled: boolean): Promise<void>;
        /**
         * Sets the data sync range. This API uses an asynchronous callback to return the result.
         *
         * @param { string[] } localLabels - Sync labels set for the local device.
         * @param { string[] } remoteSupportLabels - Sync labels set for remote devices.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        setSyncRange(localLabels: string[], remoteSupportLabels: string[], callback: AsyncCallback<void>): void;
        /**
         * Sets the data sync range. This API uses a promise to return the result.
         *
         * @param { string[] } localLabels - Sync labels set for the local device.
         * @param { string[] } remoteSupportLabels - Sync labels set for remote devices.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        setSyncRange(localLabels: string[], remoteSupportLabels: string[]): Promise<void>;
        /**
         * Sets the default delay for cross-device data sync. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > After the default delay is set, calling [sync]{@link distributedKVStore.SyncMode} will not trigger the cross-
         * > device data sync immediately. Instead, the data sync will be executed only after the specified delay duration.
         *
         * @param { number } defaultAllowedDelayMs - Delay time to set, in ms. The value can be **0** or ranges from 100 to 86400000.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        setSyncParam(defaultAllowedDelayMs: number, callback: AsyncCallback<void>): void;
        /**
         * Sets the default delay for cross-device data sync. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > After the default delay is set, calling [sync]{@link distributedKVStore.SyncMode} will not trigger the cross-
         * > device data sync immediately. Instead, the data sync will be executed only after the specified delay duration.
         *
         * @param { number } defaultAllowedDelayMs - Delay time to set, in ms. The value can be **0** or ranges from 100 to 86400000.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        setSyncParam(defaultAllowedDelayMs: number): Promise<void>;
        /**
         * Starts cross-device data sync manually. For details about the sync modes of KV stores, see
         * [Cross-Device Synchronization of KV Stores](docroot://database/data-sync-of-kv-store.md).
         *
         * > **NOTE**
         * >
         * > **deviceIds** is **networkId** in
         * > [DeviceBasicInfo]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceBasicInfo}, which can be
         * > obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string[] } deviceIds - List of **networkId**s of the devices in the same networking environment to be
         *     synchronized.
         * @param { SyncMode } mode - Sync mode.
         * @param { number } delayMs - Delay time allowed, in ms. The default value is **0**. If **delayMs** is set, data sync will be
         *     executed **delayMs** after **sync()** is called. If **delayMs** is not set, the delay set in
         *     [setSyncParam]{@link distributedKVStore.SingleKVStore.setSyncParam(defaultAllowedDelayMs: number, callback: AsyncCallback<void>)}
         *     is used.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void;
        /**
         * Starts cross-device data sync manually. This API returns the result synchronously. For details about the sync
         * modes of KV stores, see [Cross-Device Synchronization of KV Stores](docroot://database/data-sync-of-kv-store.md).
         *
         * > **NOTE**
         * >
         * > **deviceIds** is **networkId** in
         * > [DeviceBasicInfo]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceBasicInfo}, which can be
         * > obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string[] } deviceIds - List of **networkId**s of the devices in the same networking environment to be
         *     synchronized.
         * @param { Query } query - **Query** object to match.
         * @param { SyncMode } mode - Sync mode.
         * @param { number } delayMs - Delay time allowed, in ms. The default value is **0**. If **delayMs** is set, data sync will be
         *     executed **delayMs** after **sync()** is called. If **delayMs** is not set, the delay set in
         *     [setSyncParam]{@link distributedKVStore.SingleKVStore.setSyncParam(defaultAllowedDelayMs: number, callback: AsyncCallback<void>)}
         *     is used.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        sync(deviceIds: string[], query: Query, mode: SyncMode, delayMs?: number): void;
        /**
         * Subscribes to data changes of the specified type.
         *
         * @param { 'dataChange' } event - Event type. The value is **dataChange**, which indicates a data change event.
         * @param { SubscribeType } type - Type of data change.
         * @param { Callback<ChangeNotification> } listener - Callback used to return the object to be notified when the data
         *     changes.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100001 - Over max limits.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void;
        /**
         * Subscribes to the cross-device data sync completion events.
         *
         * @param { 'syncComplete' } event - Event type. The value is **syncComplete**, which indicates the sync completion event.
         * @param { Callback<Array<[ string, number ]>> } syncCallback - Callback used to return the sync completion event.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        on(event: 'syncComplete', syncCallback: Callback<Array<[
            string,
            number
        ]>>): void;
        /**
         * Unsubscribes from data changes.
         *
         * @param { 'dataChange' } event - Event type. The value is **dataChange**, which indicates a data change event.
         * @param { Callback<ChangeNotification> } listener - Callback to unregister. If this parameter is not specified, this API
         *     unregisters all callbacks for data changes.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        off(event: 'dataChange', listener?: Callback<ChangeNotification>): void;
        /**
         * Unsubscribes from the cross-device data sync completion events.
         *
         * @param { 'syncComplete' } event - Event type. The value is **syncComplete**, which indicates a sync completion event.
         * @param { Callback<Array<[ string, number ]>> } syncCallback - Callback to unregister. If this parameter is not set, all
         *     callbacks used to listen for the data sync completion event are unregistered. When multiple ArkTS instances (
         *     obtained through the
         *     [getKVStore]{@link distributedKVStore.KVManager.getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>)}
         *     API) of the same database all register the callback used to listen for the sync completion event, if all these
         *     callbacks are unregistered by one of the ArkTS instances, then the callbacks of the others are also unregistered.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        off(event: 'syncComplete', syncCallback?: Callback<Array<[
            string,
            number
        ]>>): void;
        /**
         * Obtains the security level of this KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<SecurityLevel> } callback - Callback used to return the security level of the KV store.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getSecurityLevel(callback: AsyncCallback<SecurityLevel>): void;
        /**
         * Obtains the security level of this KV store. This API uses a promise to return the result.
         *
         * @returns { Promise<SecurityLevel> } Promise used to return the security level of the KV store.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getSecurityLevel(): Promise<SecurityLevel>;
        /**
         * Update the key used to encrypt the database.
         *
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 15100006 - Failed to update the key.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        rekey(): Promise<void>;
    }
    /**
     * Provides APIs for querying data in a device KV store and performing cross-device data sync. This class inherits
     * from **SingleKVStore**. The **SingleKVStore** APIs such as **put** and **putBatch** can be used.
     * Data is distinguished by device in a device KV store. Each device can only write and modify its own data. Data of
     * other devices is read-only and cannot be modified.
     * For example, a device KV store can be used to implement image sharing between devices. The images of other devices
     * can be viewed, but not be modified or deleted.
     * Before calling any method in **DeviceKVStore**, you must use
     * [getKVStore]{@link distributedKVStore.KVManager.getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>)}
     *  to obtain a **DeviceKVStore** object.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
     * @since 9
     */
    interface DeviceKVStore extends SingleKVStore {
        /**
         * Obtains the value of the specified key for this device. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { string } key - Key of the value to obtain. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @param { AsyncCallback<boolean | string | number | Uint8Array> } callback - Callback used to return the value
         *     obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void;
        /**
         * Obtains the value of the specified key for this device. This API uses a promise to return the result.
         *
         * @param { string } key - Key of the value to obtain. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @returns { Promise<boolean | string | number | Uint8Array> } Promise used to return the value obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        get(key: string): Promise<boolean | string | number | Uint8Array>;
        /**
         * Obtains a string value that matches the specified device ID and key. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { string } key - Key of the value to obtain. It cannot be empty or exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @param { AsyncCallback<boolean | string | number | Uint8Array> } callback - Callback used to return the value
         *     obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        get(deviceId: string, key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void;
        /**
         * Obtains a string value that matches the specified device ID and key. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { string } key - Key of the value to obtain. It cannot be empty or exceed
         *     [MAX_KEY_LENGTH]{@link distributedKVStore.Constants}.
         * @returns { Promise<boolean | string | number | Uint8Array> } Promise used to return the string value that matches
         *     the given condition.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        get(deviceId: string, key: string): Promise<boolean | string | number | Uint8Array>;
        /**
         * Obtains all KV pairs that match the specified key prefix for this device. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { string } keyPrefix - Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and
         *     all data in the RDB store will be returned.
         * @param { AsyncCallback<Entry[]> } callback - Callback used to return the KV pairs that match the specified prefix.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getEntries(keyPrefix: string, callback: AsyncCallback<Entry[]>): void;
        /**
         * Obtains all KV pairs that match the specified key prefix for this device. This API uses a promise to return the
         * result.
         *
         * @param { string } keyPrefix - Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and
         *     all data in the RDB store will be returned.
         * @returns { Promise<Entry[]> } Promise used to return the KV pairs that match the specified prefix.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getEntries(keyPrefix: string): Promise<Entry[]>;
        /**
         * Obtains all KV pairs that match the specified device ID and key prefix. This API uses an asynchronous callback to
         *  return the result.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { string } keyPrefix - Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and
         *     all data in the RDB store will be returned.
         * @param { AsyncCallback<Entry[]> } callback - Callback used to return the KV pairs obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        getEntries(deviceId: string, keyPrefix: string, callback: AsyncCallback<Entry[]>): void;
        /**
         * Obtains all KV pairs that match the specified device ID and key prefix. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { string } keyPrefix - Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and
         *     all data in the RDB store will be returned.
         * @returns { Promise<Entry[]> } Promise used to return all the KV pairs that match the given condition.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        getEntries(deviceId: string, keyPrefix: string): Promise<Entry[]>;
        /**
         * Obtains all KV pairs that match the specified **Query** object for this device. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { Query } query - Key prefix to match.
         * @param { AsyncCallback<Entry[]> } callback - Callback used to return the KV pairs that match the specified **Query**
         *     object on the local device.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getEntries(query: Query, callback: AsyncCallback<Entry[]>): void;
        /**
         * Obtains all KV pairs that match the specified **Query** object for this device. This API uses a promise to return
         *  the result.
         *
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<Entry[]> } Promise used to return the KV pairs that match the specified **Query** object on the local
         *     device.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getEntries(query: Query): Promise<Entry[]>;
        /**
         * Obtains the KV pairs that match the specified device ID and **Query** object. This API uses an asynchronous
         * callback to return the result.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<Entry[]> } callback - Callback used to return the KV pairs that match the specified device ID and
         *     **Query** object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        getEntries(deviceId: string, query: Query, callback: AsyncCallback<Entry[]>): void;
        /**
         * Obtains the KV pairs that match the specified device ID and **Query** object. This API uses a promise to return
         * the result.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<Entry[]> } Promise used to return the KV pairs that match the specified device ID and **Query**
         *     object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        getEntries(deviceId: string, query: Query): Promise<Entry[]>;
        /**
         * Obtains a result set with the specified prefix for this device. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { string } keyPrefix - Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and
         *     all data in the RDB store will be returned.
         * @param { AsyncCallback<KVStoreResultSet> } callback - Callback used to return the result set with the specified prefix.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 15100001 - Over max limits. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void;
        /**
         * Obtains a result set with the specified prefix for this device. This API uses a promise to return the result.
         *
         * @param { string } keyPrefix - Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and
         *     all data in the RDB store will be returned.
         * @returns { Promise<KVStoreResultSet> } Promise used to return the result set with the specified prefix.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 15100001 - Over max limits. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getResultSet(keyPrefix: string): Promise<KVStoreResultSet>;
        /**
         * Obtains a **KVStoreResultSet** object that matches the specified device ID and key prefix. This API uses an
         * asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { string } keyPrefix - Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and
         *     all data in the RDB store will be returned.
         * @param { AsyncCallback<KVStoreResultSet> } callback - Callback used to return the **KVStoreResultSet** object obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 15100001 - Over max limits. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        getResultSet(deviceId: string, keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void;
        /**
         * Obtains a **KVStoreResultSet** object that matches the specified device ID and key prefix. This API uses a
         * promise to return the result.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { string } keyPrefix - Key prefix to match. It cannot contain '^'; otherwise, the predicate becomes invalid and
         *     all data in the RDB store will be returned.
         * @returns { Promise<KVStoreResultSet> } Promise used to return the **KVStoreResultSet** object obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 15100001 - Over max limits. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        getResultSet(deviceId: string, keyPrefix: string): Promise<KVStoreResultSet>;
        /**
         * Obtains a **KVStoreResultSet** object that matches the specified **Query** object for this device. This API uses
         * an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<KVStoreResultSet> } callback - Callback used to return the **KVStoreResultSet** object obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 15100001 - Over max limits. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getResultSet(query: Query, callback: AsyncCallback<KVStoreResultSet>): void;
        /**
         * Obtains a **KVStoreResultSet** object that matches the specified **Query** object for this device. This API uses
         * a promise to return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<KVStoreResultSet> } Promise used to return the **KVStoreResultSet** object obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 15100001 - Over max limits. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getResultSet(query: Query): Promise<KVStoreResultSet>;
        /**
         * Obtains a **KVStoreResultSet** object that matches the specified device ID and **Query** object. This API uses an
         *  asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - ID of the device to which the **KVStoreResultSet** object belongs.
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<KVStoreResultSet> } callback - Callback used to return the **KVStoreResultSet** object that
         *     matches the specified device ID and **Query** object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 15100001 - Over max limits. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KVStoreResultSet>): void;
        /**
         * Obtains a **KVStoreResultSet** object that matches the specified device ID and **Query** object. This API uses a
         * promise to return the result.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - ID of the device to which the **KVStoreResultSet** object belongs.
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<KVStoreResultSet> } Promise used to return the **KVStoreResultSet** object that matches the specified
         *     device ID and **Query** object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @throws { BusinessError } 15100001 - Over max limits. [since 10]
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        getResultSet(deviceId: string, query: Query): Promise<KVStoreResultSet>;
        /**
         * Obtains the number of results that match the specified **Query** object for this device. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<number> } callback - Callback used to return the number of results obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getResultSize(query: Query, callback: AsyncCallback<number>): void;
        /**
         * Obtains the number of results that match the specified **Query** object for this device. This API uses a promise
         * to return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<number> } Promise used to return the number of results obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getResultSize(query: Query): Promise<number>;
        /**
         * Obtains the number of results that match the specified device ID and **Query** object. This API uses an
         * asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - ID of the device to which the **KVStoreResultSet** object belongs.
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<number> } callback - Callback used to return the number of results obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        getResultSize(deviceId: string, query: Query, callback: AsyncCallback<number>): void;
        /**
         * Obtains the number of results that match the specified device ID and **Query** object. This API uses a promise to
         *  return the result.
         *
         * > **NOTE**
         * >
         * > **deviceId** can be obtained by
         * > [deviceManager.getAvailableDeviceListSync]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}
         * > .
         * > > For details about how to obtain **deviceId**, see [sync()]{@link distributedKVStore.SyncMode}.
         *
         * @param { string } deviceId - ID of the device to which the **KVStoreResultSet** object belongs.
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<number> } Promise used to return the number of results obtained.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @throws { BusinessError } 15100004 - Not found.
         * @throws { BusinessError } 15100005 - Database or result set already closed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        getResultSize(deviceId: string, query: Query): Promise<number>;
    }
    /**
     * Creates a **KVManager** instance for KV store management.
     *
     * @param { KVManagerConfig } config - Configuration of the **KVManager** instance, including the bundle name (cannot be
     *     empty) of the caller and user information.
     * @returns { KVManager } **KVManager** instance created.
     * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
     *     <br>2.Incorrect parameters types;
     *     <br>3.Parameter verification failed.
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @crossplatform [since 24]
     * @since 9
     */
    function createKVManager(config: KVManagerConfig): KVManager;
    /**
     * Provides an instance to obtain information about a distributed KV store. Before calling any API in **KVManager**,
     * you must use [createKVManager]{@link distributedKVStore.createKVManager} to create a **KVManager** instance.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @crossplatform [since 24]
     * @since 9
     */
    interface KVManager {
        /**
         * Creates and obtains a distributed KV store based on the specified **options** and **storeId**. This API uses an
         * asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > If the database file cannot be opened (for example, the file header is damaged) when an existing distributed KV
         * >  store is obtained, the automatic rebuild logic will be triggered to return a newly created distributed KV
         * > store instance. For important data that cannot be regenerated, you are advised to use the backup and restore
         * > feature to prevent data loss. For details, see
         * > [Database Backup and Restoration](docroot://database/data-backup-and-restore.md).
         *
         * @param { string } storeId - Unique identifier of the KV store. The KV store ID allows only letters, digits, and
         *     underscores (_), and cannot exceed [MAX_STORE_ID_LENGTH]{@link distributedKVStore.Constants} in length.
         * @param { Options } options - Configuration of the KV store to create.
         * @param { AsyncCallback<T> } callback - Callback used to return the **SingleKVStore** or **DeviceKVStore** instance
         *     created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100002 - Open existed database with changed options.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>): void;
        /**
         * Creates and obtains a distributed KV store based on the specified **options** and **storeId**. This API uses a
         * promise to return the result.
         *
         * > **NOTE**
         * >
         * > If the database file cannot be opened (for example, the file header is damaged) when an existing distributed KV
         * >  store is obtained, the automatic rebuild logic will be triggered to return a newly created distributed KV
         * > store instance. For important data that cannot be regenerated, you are advised to use the backup and restore
         * > feature to prevent data loss. For details, see
         * > [Database Backup and Restoration](docroot://database/data-backup-and-restore.md).
         *
         * @param { string } storeId - Unique identifier of the KV store. The KV store ID allows only letters, digits, and
         *     underscores (_), and cannot exceed [MAX_STORE_ID_LENGTH]{@link distributedKVStore.Constants} in length.
         * @param { Options } options - Configuration of the KV store to create.
         * @returns { Promise<T> } Promise used to return the **SingleKVStore** or **DeviceKVStore** instance created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @throws { BusinessError } 15100002 - Open existed database with changed options.
         * @throws { BusinessError } 15100003 - Database corrupted.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        getKVStore<T>(storeId: string, options: Options): Promise<T>;
        /**
         * Closes a distributed KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { string } appId - Bundle name of the application. The value cannot be empty or exceed 256 bytes.
         * @param { string } storeId - Unique identifier of the KV store to close. The KV store ID allows only letters, digits, and
         *     underscores (_), and cannot exceed [MAX_STORE_ID_LENGTH]{@link distributedKVStore.Constants} in length.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        closeKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void;
        /**
         * Closes a distributed KV store. This API uses a promise to return the result.
         *
         * @param { string } appId - Bundle name of the application. The value cannot be empty or exceed 256 bytes.
         * @param { string } storeId - Unique identifier of the KV store to close. The KV store ID allows only letters, digits, and
         *     underscores (_), and cannot exceed [MAX_STORE_ID_LENGTH]{@link distributedKVStore.Constants} in length.
         * @param { Options } [kvConfig] - Indicates the {@code Options} object used for close the KVStore database. [since 24]
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        closeKVStore(appId: string, storeId: string, kvConfig?: Options): Promise<void>;
        /**
         * Deletes a distributed KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { string } appId - Bundle name of the application. The value cannot be empty or exceed 256 bytes.
         * @param { string } storeId - Unique identifier of the KV store to delete. The KV store ID allows only letters, digits,
         *     and underscores (_), and cannot exceed [MAX_STORE_ID_LENGTH]{@link distributedKVStore.Constants} in length.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
         *     **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @throws { BusinessError } 15100004 - Not found.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void;
        /**
         * Deletes a distributed KV store. This API uses a promise to return the result.
         *
         * @param { string } appId - Bundle name of the application. The value cannot be empty or exceed 256 bytes.
         * @param { string } storeId - Unique identifier of the KV store to delete. The KV store ID allows only letters, digits,
         *     and underscores (_), and cannot exceed [MAX_STORE_ID_LENGTH]{@link distributedKVStore.Constants} in length.
         * @param { Options } [kvConfig] - Indicates the {@code Options} object used for delete the KVStore database. [since 24]
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @throws { BusinessError } 15100004 - Not found.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @crossplatform [since 24]
         * @since 9
         */
        deleteKVStore(appId: string, storeId: string, kvConfig?: Options): Promise<void>;
        /**
         * Obtains the IDs of all distributed KV stores that are created by
         * [getKVStore]{@link distributedKVStore.KVManager.getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>)}
         *  and have not been deleted by
         * [deleteKVStore]{@link distributedKVStore.KVManager.deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>)}
         * . This API uses an asynchronous callback to return the result.
         *
         * @param { string } appId - Bundle name of the application. The value cannot be empty or exceed 256 bytes.
         * @param { AsyncCallback<string[]> } callback - Callback used to return the IDs of all the distributed KV stores created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getAllKVStoreId(appId: string, callback: AsyncCallback<string[]>): void;
        /**
         * Obtains the IDs of all distributed KV stores that are created by
         * [getKVStore]{@link distributedKVStore.KVManager.getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>)}
         *  and have not been deleted by
         * [deleteKVStore]{@link distributedKVStore.KVManager.deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>)}
         * . This API uses a promise to return the result.
         *
         * @param { string } appId - Bundle name of the application. The value cannot be empty or exceed 256 bytes.
         * @returns { Promise<string[]> } Promise used to return the IDs of all the distributed KV stores created.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 9
         */
        getAllKVStoreId(appId: string): Promise<string[]>;
        /**
         * Subscribes to the termination (death) of the distributed data service. If the service is terminated, you need to
         * register the callbacks for data change notifications and cross-device sync completion notifications again. In
         * addition, an error will be returned for a sync operation.
         *
         * @param { 'distributedDataServiceDie' } event - Event type. The value is **distributedDataServiceDie**, which indicates
         *     the termination of the distributed data service.
         * @param { Callback<void> } deathCallback - Callback used to return the result. If the subscription is successful, **err**
         *     is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        on(event: 'distributedDataServiceDie', deathCallback: Callback<void>): void;
        /**
         * Unsubscribes from the termination (death) of the distributed data service. The **deathCallback** parameter must
         * be a callback registered for subscribing to the termination of the distributed data service. Otherwise, the
         * unsubscription will fail.
         *
         * @param { 'distributedDataServiceDie' } event - Event type. The value is **distributedDataServiceDie**, which indicates
         *     the termination of the distributed data service.
         * @param { Callback<void> } deathCallback - Callback to unregister. If this parameter is not specified, this API
         *     unregisters all callbacks for the **distributedDataServiceDie** event.
         * @throws { BusinessError } 401 - Parameter error.Possible causes:1.Mandatory parameters are left unspecified;
         *     <br>2.Incorrect parameters types;
         *     <br>3.Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 9
         */
        off(event: 'distributedDataServiceDie', deathCallback?: Callback<void>): void;
    }
}
export default distributedKVStore;

```
