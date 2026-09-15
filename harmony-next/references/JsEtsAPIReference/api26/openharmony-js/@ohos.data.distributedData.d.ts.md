# @ohos.data.distributedData.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021 Huawei Device Co., Ltd.
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
/**
 * The distributed data management module implements collaboration between databases of different devices for
 * applications. The APIs provided by distributed data management can be used to save data to distributed databases and
 * perform operations such as adding, deleting, modifying, querying, and synchronizing data in distributed databases.
 * This module provides the following functions:
 *
 * - [KVManager]{@link distributedData.KVManagerConfig}: provides a **KVManager** instance to manage key-value (KV)
 * stores.
 * - [KvStoreResultSet<sup>8+</sup>]{@link distributedData.KvStoreResultSet}: provides APIs to obtain the KV store
 * result set and query or move the data read position.
 * - [Query<sup>8+</sup>]{@link distributedData.Query}: provides APIs to query data from the database through a
 * **Query** instance by using predicates.
 * - [KVStore]{@link distributedData.KVStoreType}: provides APIs to add data, delete data, and observe data changes and
 * data sync through a **KVStore** instance.
 * - [SingleKVStore]{@link distributedData.SingleKVStore}: provides APIs to query and synchronize data in a single KV
 * store. This class inherits from [KVStore]{@link distributedData.KVStoreType}, and data is not distinguished by
 * device.
 * - [DeviceKVStore<sup>8+</sup>]{@link distributedData.DeviceKVStore}: provides APIs to query and synchronize data in a
 *  device KV store. This class inherits from [KVStore]{@link distributedData.KVStoreType}, and data is distinguished by
 *  device.
 *
 * [@ohos.data.distributedKVStore]{@link @ohos.data.distributedKVStore:distributedKVStore}.
 *
 * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
 * @since 7
 * @deprecated since 9
 * @useinstead ohos.data.distributedKVStore
 */
declare namespace distributedData {
    /**
     * Represents the configuration of a **KVManager** instance, including the bundle name and user information of the
     * caller.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.KVManagerConfig
     */
    interface KVManagerConfig {
        /**
         * User information.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         */
        userInfo: UserInfo;
        /**
         * Bundle name of the caller.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVManagerConfig#bundleName
         */
        bundleName: string;
    }
    /**
     * Defines user information.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     */
    interface UserInfo {
        /**
         * User ID. The default value is **0**.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         */
        userId?: string;
        /**
         * User type. The default value is **0**.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         */
        userType?: UserType;
    }
    /**
     * Enumerates the user types.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     */
    enum UserType {
        /**
         * User who logs in to different devices using the same account.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         */
        SAME_USER_ID = 0
    }
    /**
     * Defines the KV store constants.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.Constants
     */
    namespace Constants {
        /**
         * max key length.
         * Maximum length of a key in the KV store, in bytes.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Constants#MAX_KEY_LENGTH
         */
        const MAX_KEY_LENGTH = 1024;
        /**
         * max value length.
         * Maximum length of a value in the KV store, in bytes.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Constants#MAX_VALUE_LENGTH
         */
        const MAX_VALUE_LENGTH = 4194303;
        /**
         * max device coordinate key length.
         * Maximum length of a device key, in bytes.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Constants#MAX_KEY_LENGTH_DEVICEs
         */
        const MAX_KEY_LENGTH_DEVICE = 896;
        /**
         * max store id length.
         * Maximum length of a KV store ID, in bytes.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Constants#MAX_STORE_ID_LENGTH
         */
        const MAX_STORE_ID_LENGTH = 128;
        /**
         * max query length.
         * Maximum query length, in bytes.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Constants#MAX_QUERY_LENGTH
         */
        const MAX_QUERY_LENGTH = 512000;
        /**
         * max batch operation size.
         * Maximum number of batch operations.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Constants#MAX_BATCH_SIZE
         */
        const MAX_BATCH_SIZE = 128;
    }
    /**
     * Enumerates the data types.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.ValueType
     */
    enum ValueType {
        /**
         * String.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.ValueType#STRING
         */
        STRING = 0,
        /**
         * Integer.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.ValueType#INTEGER
         */
        INTEGER = 1,
        /**
         * Float (single-precision floating point).
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.ValueType#FLOAT
         */
        FLOAT = 2,
        /**
         * Byte array.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.ValueType#BYTE_ARRAY
         */
        BYTE_ARRAY = 3,
        /**
         * Boolean.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.ValueType#BOOLEAN
         */
        BOOLEAN = 4,
        /**
         * Double (double-precision floating point).
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.ValueType#DOUBLE
         */
        DOUBLE = 5
    }
    /**
     * Defines the **value** object in a KV store.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.Value
     */
    interface Value {
        /**
         * Type of the value.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @memberof Value
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Value#type
         * @see ValueType
         */
        type: ValueType;
        /**
         * Value of the KV pair stored in the KV store.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Value#value
         */
        value: Uint8Array | string | number | boolean;
    }
    /**
     * Defines the KV pairs stored in the KV store.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.Entry
     */
    interface Entry {
        /**
         * Key of the KV pair stored in the KV store.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Entry#key
         */
        key: string;
        /**
         * Value of the KV pair stored in the KV store.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Entry#value
         */
        value: Value;
    }
    /**
     * Defines the content of data change notifications, including inserted data, updated data, deleted data, and device
     * ID.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.ChangeNotification
     */
    interface ChangeNotification {
        /**
         * Data inserted.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.ChangeNotification#insertEntries
         */
        insertEntries: Entry[];
        /**
         * Data updated.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.ChangeNotification#updateEntries
         */
        updateEntries: Entry[];
        /**
         * Data deleted.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.ChangeNotification#deleteEntries
         */
        deleteEntries: Entry[];
        /**
         * UUID of the device.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.ChangeNotification#deviceId
         */
        deviceId: string;
    }
    /**
     * Enumerates the sync modes.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.SyncMode
     */
    enum SyncMode {
        /**
         * Pull data from the peer end to the local end only.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SyncMode#PULL_ONLY
         */
        PULL_ONLY = 0,
        /**
         * Push data from the local end to the peer end only.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SyncMode#PUSH_ONLY
         */
        PUSH_ONLY = 1,
        /**
         * Push data from the local end to the peer end and then pull data from the peer end to the local end.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SyncMode#PUSH_PULL
         */
        PUSH_PULL = 2
    }
    /**
     * Enumerates the subscription types.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.SubscribeType
     */
    enum SubscribeType {
        /**
         * Local data changes.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SubscribeType#SUBSCRIBE_TYPE_LOCAL
         */
        SUBSCRIBE_TYPE_LOCAL = 0,
        /**
         * Remote data changes.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SubscribeType#SUBSCRIBE_TYPE_REMOTE
         */
        SUBSCRIBE_TYPE_REMOTE = 1,
        /**
         * Local and remote data changes.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SubscribeType#SUBSCRIBE_TYPE_ALL
         */
        SUBSCRIBE_TYPE_ALL = 2
    }
    /**
     * Enumerates the KV store types.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.KVStoreType
     */
    enum KVStoreType {
        /**
         * Device KV store.
         *
         * The device KV store manages data by device, which eliminates conflicts. Data can be queried by device.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreType#DEVICE_COLLABORATION
         */
        DEVICE_COLLABORATION = 0,
        /**
         * Single KV store.
         *
         * The single KV store does not differentiate data by device. If the same key is modified by different devices, the
         * data will be overwritten.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreType#SINGLE_VERSION
         */
        SINGLE_VERSION = 1,
        /**
         * Multi-version KV store. This type is not supported currently.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 7
         * @deprecated since 9
         */
        MULTI_VERSION = 2
    }
    /**
     * Enumerates the KV store security levels.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.SecurityLevel
     */
    enum SecurityLevel {
        /**
         * No security level is set for the KV store (deprecated).
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 7
         * @deprecated since 9
         */
        NO_LEVEL = 0,
        /**
         * The KV store security level is public (deprecated).
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         */
        S0 = 1,
        /**
         * Low security level. If data leakage occurs, minor impact will be caused. For example, a KV store that contains
         * system data such as wallpapers.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SecurityLevel#S1
         */
        S1 = 2,
        /**
         * Medium security level. If data leakage occurs, moderate impact will be caused. For example, a KV store that
         * contains information created by users or call records, such as audio or video clips.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SecurityLevel#S2
         */
        S2 = 3,
        /**
         * High security level. If data leakage occurs, major impact will be caused. For example, a KV store that contains
         * information such as user fitness, health, and location data.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SecurityLevel#S3
         */
        S3 = 5,
        /**
         * Critical security level. If data leakage occurs, severe impact will be caused. For example, a KV store that
         * contains information such as authentication credentials and financial data.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SecurityLevel#S4
         */
        S4 = 6
    }
    /**
     * Provides KV store configuration.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.Options
     */
    interface Options {
        /**
         * Whether to create a KV store if the database file does not exist. The default value is **true**, which means to
         * create a KV store.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Options#createIfMissing
         */
        createIfMissing?: boolean;
        /**
         * Whether to encrypt the KV store. The default value is **false**, which means the KV store is not encrypted.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Options#encrypt
         */
        encrypt?: boolean;
        /**
         * Whether to back up the KV store. The default value is **true**, which means to back up the KV store.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Options#backup
         */
        backup?: boolean;
        /**
         * Whether to automatically synchronize database files. The default value is **false**, which means the database
         * files are manually synchronized.
         *
         * ohos.permission.DISTRIBUTED_DATASYNC
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Options#autoSync
         */
        autoSync?: boolean;
        /**
         * Type of the KV store to create. The default value is **DEVICE_COLLABORATION**, which indicates a device KV store.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Options#kvStoreType
         */
        kvStoreType?: KVStoreType;
        /**
         * Security level (S1 to S4) of the KV store.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Options#securityLevel
         */
        securityLevel?: SecurityLevel;
        /**
         * Schema that defines the values stored in the KV store. The default value is **undefined**, which means no schema
         * is used.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Options#schema
         */
        schema?: Schema;
    }
    /**
     * Defines the schema of a KV store. You can create a **Schema** object and place it in
     * [Options]{@link distributedData.Options} when creating or opening a KV store.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.Schema
     */
    class Schema {
        /**
         * A constructor used to create a **Schema** instance.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Schema#constructor
         */
        constructor();
        /**
         * JSON root object.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Schema#root
         */
        root: FieldNode;
        /**
         * String array in JSON format.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Schema#indexes
         */
        indexes: Array<string>;
        /**
         * Schema mode.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Schema#mode
         */
        mode: number;
        /**
         * Size of a skip of the schema.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Schema#skip
         */
        skip: number;
    }
    /**
     * Represents a **Schema** instance, which provides the APIs for defining the values stored in a KV store.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.FieldNode
     */
    class FieldNode {
        /**
         * A constructor used to create a **FieldNode** instance with a string field.
         *
         * @param { string } name - Value of **FieldNode**.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.FieldNode#constructor
         */
        constructor(name: string);
        /**
         * Appends a child node to this **FieldNode**.
         *
         * @param { FieldNode } child - Child node to append.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.FieldNode#appendChild
         */
        appendChild(child: FieldNode): boolean;
        /**
         * Default value of a **FieldNode**.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.FieldNode#default
         */
        default: string;
        /**
         * Whether the database field can be null.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.FieldNode#nullable
         */
        nullable: boolean;
        /**
         * Value of the data type corresponding to the specified node.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.FieldNode#type
         */
        type: number;
    }
    /**
     * Provides APIs to obtain the KV store result sets, and query and move the data read position.
     * Before calling any method in **KvStoreResultSet**, you must use
     * [getKVStore]{@link distributedData.KVManager.getKVStore<T extends KVStore>(storeId: string, options: Options, callback: AsyncCallback<T>)}
     *  to obtain a **KVStore** object.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.KVStoreResultSet
     */
    interface KvStoreResultSet {
        /**
         * Obtains the total number of rows in the result set.
         *
         * @returns { number } Total number of rows obtained.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreResultSet#getCount
         */
        getCount(): number;
        /**
         * Obtains the current data read position (position from which data is read) in the result set.
         *
         * @returns { number } Current data read position obtained.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreResultSet#getPosition
         */
        getPosition(): number;
        /**
         * Moves the data read position to the first row. If the result set is empty, **false** will be returned.
         *
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreResultSet#moveToFirst
         */
        moveToFirst(): boolean;
        /**
         * Moves the data read position to the last row. If the result set is empty, **false** will be returned.
         *
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreResultSet#moveToLast
         */
        moveToLast(): boolean;
        /**
         * Moves the data read position to the next row. If the result set is empty, **false** will be returned.
         *
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreResultSet#moveToNext
         */
        moveToNext(): boolean;
        /**
         * Moves the data read position to the previous row. If the result set is empty, **false** will be returned.
         *
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreResultSet#moveToPrevious
         */
        moveToPrevious(): boolean;
        /**
         * Moves the data read position with the specified offset from the current position.
         *
         * @param { number } offset - Offset to move the data read position. A negative value means to move backward, and a
         *     positive value means to move forward.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreResultSet#move
         */
        move(offset: number): boolean;
        /**
         * Moves the data read position from 0 to an absolute position.
         *
         * @param { number } position - Absolute position to move to.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreResultSet#moveToPosition
         */
        moveToPosition(position: number): boolean;
        /**
         * Checks whether the data read position is the first row.
         *
         * @returns { boolean } Returns **true** if the first row is being read; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreResultSet#isFirst
         */
        isFirst(): boolean;
        /**
         * Checks whether the data read position is the last row.
         *
         * @returns { boolean } Returns **true** if the last row is being read; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreResultSet#isLast
         */
        isLast(): boolean;
        /**
         * Checks whether the data read position is before the first row.
         *
         * @returns { boolean } Returns **true** if the data read position is before the first row; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreResultSet#isBeforeFirst
         */
        isBeforeFirst(): boolean;
        /**
         * Checks whether the data read position is after the last row.
         *
         * @returns { boolean } Returns **true** if the data read position is after the last row; returns **false** otherwise.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreResultSet#isAfterLast
         */
        isAfterLast(): boolean;
        /**
         * Obtains the KV pair from the current position.
         *
         * @returns { Entry } KV pair obtained.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVStoreResultSet#getEntry
         */
        getEntry(): Entry;
    }
    /**
     * Provides APIs to create a **Query** object, which defines different data query criteria.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.Query
     */
    class Query {
        /**
         * Defines a constructor used to create a **Query** instance.
         *
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#constructor
         */
        constructor();
        /**
         * Resets the **Query** object.
         *
         * @returns { Query } **Query** object reset.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#reset
         */
        reset(): Query;
        /**
         * Creates a **Query** object to search for the records with the specified field that are equal to the given value.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @param { number | string | boolean } value - Value to match.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#equalTo
         */
        equalTo(field: string, value: number | string | boolean): Query;
        /**
         * Creates a **Query** object to search for the records with the specified field that are not equal to the given
         * value.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @param { number | string | boolean } value - Value to match.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#notEqualTo
         */
        notEqualTo(field: string, value: number | string | boolean): Query;
        /**
         * Creates a **Query** object to search for the records with the specified field that are greater than the given
         * value.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @param { number | string | boolean } value - Value to match.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#greaterThan
         */
        greaterThan(field: string, value: number | string | boolean): Query;
        /**
         * Creates a **Query** object to search for the records with the specified field that are less than the given value.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @param { number | string } value - Value to match.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#lessThan
         */
        lessThan(field: string, value: number | string): Query;
        /**
         * Creates a **Query** object to search for the records with the specified field that are greater than or equal to
         * the given value.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @param { number | string } value - Value to match.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#greaterThanOrEqualTo
         */
        greaterThanOrEqualTo(field: string, value: number | string): Query;
        /**
         * Creates a **Query** object to search for the records with the specified field that are less than or equal to the
         * given value.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @param { number | string } value - Value to match.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#lessThanOrEqualTo
         */
        lessThanOrEqualTo(field: string, value: number | string): Query;
        /**
         * Creates a **Query** object to search for the records with the specified field that are **null**.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#isNull
         */
        isNull(field: string): Query;
        /**
         * Creates a **Query** object to search for the records with the specified field that are within the given number
         * list.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @param { number[] } valueList - List of numbers to match.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#inNumber
         */
        inNumber(field: string, valueList: number[]): Query;
        /**
         * Creates a **Query** object to search for the records with the specified field that are within the given string
         * list.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @param { string[] } valueList - List of strings to match.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#inString
         */
        inString(field: string, valueList: string[]): Query;
        /**
         * Creates a **Query** object to search for the records with the specified field that are not within the given
         * number list.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @param { number[] } valueList - List of numbers to match.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#notInNumber
         */
        notInNumber(field: string, valueList: number[]): Query;
        /**
         * Creates a **Query** object to search for the records with the specified field that are not within the given
         * string list.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @param { string[] } valueList - List of strings to match.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#notInString
         */
        notInString(field: string, valueList: string[]): Query;
        /**
         * Creates a **Query** object to search for the records with the specified field that are similar to the given
         * string.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @param { string } value - String to match.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#like
         */
        like(field: string, value: string): Query;
        /**
         * Creates a **Query** object to search for the records with the specified field that are not similar to the given
         * string.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @param { string } value - String to match.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#unlike
         */
        unlike(field: string, value: string): Query;
        /**
         * Creates a **Query** object with the AND condition.
         *
         * @returns { Query } **Query** object created.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#and
         */
        and(): Query;
        /**
         * Creates a **Query** object with the OR condition.
         *
         * @returns { Query } **Query** object created.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#or
         */
        or(): Query;
        /**
         * Creates a **Query** object to sort the query results in ascending order.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#orderByAsc
         */
        orderByAsc(field: string): Query;
        /**
         * Creates a **Query** object to sort the query results in descending order.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#orderByDesc
         */
        orderByDesc(field: string): Query;
        /**
         * Creates a **Query** object to specify the number of records in the query result and the start position.
         *
         * @param { number } total - Number of records in the query result.
         * @param { number } offset - Start position.
         * @returns { Query } **Query** object created.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#limit
         */
        limit(total: number, offset: number): Query;
        /**
         * Creates a **Query** object to search for the records whose value is not **null**.
         *
         * @param { string } field - Field to query. It cannot contain '^'.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#isNotNull
         */
        isNotNull(field: string): Query;
        /**
         * Creates a **Query** object for a query condition group with a left parenthesis.
         *
         * @returns { Query } **Query** object created.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#beginGroup
         */
        beginGroup(): Query;
        /**
         * Creates a **Query** object for a query condition group with a right parenthesis.
         *
         * @returns { Query } **Query** object created.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#endGroup
         */
        endGroup(): Query;
        /**
         * Creates a **Query** object with a specified key prefix.
         *
         * @param { string } prefix - Key prefix.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#prefixKey
         */
        prefixKey(prefix: string): Query;
        /**
         * Creates a **Query** object with an index preferentially used for query.
         *
         * @param { string } index - Index preferentially used for query.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#setSuggestIndex
         */
        setSuggestIndex(index: string): Query;
        /**
         * Creates a **Query** object with the device ID as the key prefix.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - Device ID.
         * @returns { Query } **Query** object created.
         * @throws Throws this exception if input is invalid.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#deviceId
         */
        deviceId(deviceId: string): Query;
        /**
         * Obtains the query statement of the **Query** object.
         *
         * @returns { string } Query statement obtained.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.Query#getSqlLike
         */
        getSqlLike(): string;
    }
    /**
     * Provides APIs to manage data in a KV store, for example, adding or deleting data and subscribing to data changes or
     *  completion of data sync.
     * Before calling any method in **KVStore**, you must use
     * [getKVStore]{@link distributedData.KVManager.getKVStore<T extends KVStore>(storeId: string, options: Options, callback: AsyncCallback<T>)}
     *  to obtain a **KVStore** object.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @version 1
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.SingleKVStore
     */
    interface KVStore {
        /**
         * Adds a KV pair of the specified type to this KV store. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { string } key - Key of the KV pair to add. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedData.Constants}.
         * @param { Uint8Array | string | number | boolean } value - Value of the KV pair to add. The value type can be Uint8Array,
         *     number, string, or boolean. A value of the Uint8Array or string type cannot exceed
         *     [MAX_VALUE_LENGTH]{@link distributedData.Constants}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if any of the following errors
         *     occurs: {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#put
         */
        put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void;
        /**
         * Adds a KV pair of the specified type to this KV store. This API uses a promise to return the result.
         *
         * @param { string } key - Key of the KV pair to add. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedData.Constants}.
         * @param { Uint8Array | string | number | boolean } value - Value of the KV pair to add. The value type can be Uint8Array,
         *     number, string, or boolean. A value of the Uint8Array or string type cannot exceed
         *     [MAX_VALUE_LENGTH]{@link distributedData.Constants}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if any of the following errors
         *     occurs: {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#put
         */
        put(key: string, value: Uint8Array | string | number | boolean): Promise<void>;
        /**
         * Deletes a KV pair from this KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { string } key - Key of the KV pair to delete. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedData.Constants}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if any of the following errors
         *     occurs: {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and
         *     {@code DB_ERROR}, and {@code KEY_NOT_FOUND}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#delete
         */
        delete(key: string, callback: AsyncCallback<void>): void;
        /**
         * Deletes a KV pair from this KV store. This API uses a promise to return the result.
         *
         * @param { string } key - Key of the KV pair to delete. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedData.Constants}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if any of the following errors
         *     occurs: {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and
         *     {@code DB_ERROR}, and {@code KEY_NOT_FOUND}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#delete
         */
        delete(key: string): Promise<void>;
        /**
         * Subscribes to data changes of the specified type.
         *
         * @param { 'dataChange' } event - Event type. The value is **dataChange**, which indicates data changes.
         * @param { SubscribeType } type - Type of data change.
         * @param { Callback<ChangeNotification> } listener - Callback used to return the result.
         * @throws Throws this exception if any of the following errors
         *     occurs: {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR},
         *     {@code DB_ERROR}, and {@code STORE_ALREADY_SUBSCRIBE}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#on
         */
        on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void;
        /**
         * Subscribes to sync completion events.
         *
         * @param { 'syncComplete' } event - Event type. The value is **syncComplete**, which indicates a sync completion event.
         * @param { Callback<Array<[ string, number ]>> } syncCallback - Callback used to return a sync completion event.
         * @throws Throws this exception if any of the following errors
         *     occurs: {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR},
         *     {@code DB_ERROR}, and {@code STORE_ALREADY_SUBSCRIBE}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#on
         */
        on(event: 'syncComplete', syncCallback: Callback<Array<[
            string,
            number
        ]>>): void;
        /**
         * Unsubscribes from data changes.
         *
         * @param { 'dataChange' } event - Event type. The value is **dataChange**, which indicates data changes.
         * @param { Callback<ChangeNotification> } listener - Callback to unregister. If this parameter is not specified, all
         *     callbacks for data changes will be unregistered.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#off
         */
        off(event: 'dataChange', listener?: Callback<ChangeNotification>): void;
        /**
         * Unsubscribes from sync completion events.
         *
         * @param { 'syncComplete' } event - Event type. The value is **syncComplete**, which indicates a sync completion event.
         * @param { Callback<Array<[ string, number ]>> } syncCallback - Callback to unregister. If this parameter is not specified,
         *     all callbacks for data changes will be unregistered.
         * @throws Throws this exception if any of the following errors
         *     occurs: {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR},
         *     {@code DB_ERROR}, and {@code STORE_ALREADY_SUBSCRIBE}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#off
         */
        off(event: 'syncComplete', syncCallback?: Callback<Array<[
            string,
            number
        ]>>): void;
        /**
         * Inserts KV pairs in batches to this KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { Entry[] } entries - KV pairs to insert in batches.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if a database error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#putBatch
         */
        putBatch(entries: Entry[], callback: AsyncCallback<void>): void;
        /**
         * Inserts KV pairs in batches to this KV store. This API uses a promise to return the result.
         *
         * @param { Entry[] } entries - KV pairs to insert in batches.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if a database error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#putBatch
         */
        putBatch(entries: Entry[]): Promise<void>;
        /**
         * Deletes KV pairs in batches from this KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { string[] } keys - KV pairs to delete in batches.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if a database error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#deleteBatch
         */
        deleteBatch(keys: string[], callback: AsyncCallback<void>): void;
        /**
         * Deletes KV pairs in batches from this KV store. This API uses a promise to return the result.
         *
         * @param { string[] } keys - KV pairs to delete in batches.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if a database error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#deleteBatch
         */
        deleteBatch(keys: string[]): Promise<void>;
        /**
         * Starts the transaction in this KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if a database error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#startTransaction
         */
        startTransaction(callback: AsyncCallback<void>): void;
        /**
         * Starts the transaction in this KV store. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if a database error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#startTransaction
         */
        startTransaction(): Promise<void>;
        /**
         * Commits the transaction in this KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if a database error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#commit
         */
        commit(callback: AsyncCallback<void>): void;
        /**
         * Commits the transaction in this KV store. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if a database error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#commit
         */
        commit(): Promise<void>;
        /**
         * Rolls back the transaction in this KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if a database error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#rollback
         */
        rollback(callback: AsyncCallback<void>): void;
        /**
         * Rolls back the transaction in this KV store. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if a database error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#rollback
         */
        rollback(): Promise<void>;
        /**
         * Sets data sync, which can be enabled or disabled. This API uses an asynchronous callback to return the result.
         *
         * @param { boolean } enabled - Whether to enable data sync. The value **true** means to enable data sync, and **false**
         *     means the opposite.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if an internal service error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#enableSync
         */
        enableSync(enabled: boolean, callback: AsyncCallback<void>): void;
        /**
         * Sets data sync, which can be enabled or disabled. This API uses a promise to return the result.
         *
         * @param { boolean } enabled - Whether to enable data sync. The value **true** means to enable data sync, and **false**
         *     means the opposite.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if an internal service error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#enableSync
         */
        enableSync(enabled: boolean): Promise<void>;
        /**
         * Sets the data sync range. This API uses an asynchronous callback to return the result.
         *
         * @param { string[] } localLabels - Sync labels set for the local device.
         * @param { string[] } remoteSupportLabels - Sync labels set for remote devices.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if an internal service error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#setSyncRange
         */
        setSyncRange(localLabels: string[], remoteSupportLabels: string[], callback: AsyncCallback<void>): void;
        /**
         * Sets the data sync range. This API uses a promise to return the result.
         *
         * @param { string[] } localLabels - Sync labels set for the local device.
         * @param { string[] } remoteSupportLabels - Sync labels set for remote devices.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if an internal service error occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#setSyncRange
         */
        setSyncRange(localLabels: string[], remoteSupportLabels: string[]): Promise<void>;
    }
    /**
     * Provides APIs to query and synchronize data in a single KV store. This class inherits from
     * [KVStore]{@link distributedData.KVStoreType}.
     *
     * Data is not distinguished by device in a single KV store. The data written to different devices using the same key
     * will be overwritten. For example, a single KV store can be used to synchronize a user's calendar and contact data
     * between different devices.
     * Before calling any method in **SingleKVStore**, you must use
     * [getKVStore]{@link distributedData.KVManager.getKVStore<T extends KVStore>(storeId: string, options: Options, callback: AsyncCallback<T>)}
     *  to obtain a **SingleKVStore** instance.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @version 1
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.SingleKVStore
     */
    interface SingleKVStore extends KVStore {
        /**
         * Obtains the value of the specified key. This API uses an asynchronous callback to return the result.
         *
         * @param { string } key - Key of the value to obtain. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedData.Constants}.
         * @param { AsyncCallback<Uint8Array | string | boolean | number> } callback - Callback used to return the value obtained.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}, and {@code KEY_NOT_FOUND}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#get
         */
        get(key: string, callback: AsyncCallback<Uint8Array | string | boolean | number>): void;
        /**
         * Obtains the value of the specified key. This API uses a promise to return the result.
         *
         * @param { string } key - Key of the value to obtain. It cannot be empty, and the length cannot exceed
         *     [MAX_KEY_LENGTH]{@link distributedData.Constants}.
         * @returns { Promise<Uint8Array | string | boolean | number> } Promise used to return the value obtained.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}, and {@code KEY_NOT_FOUND}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#get
         */
        get(key: string): Promise<Uint8Array | string | boolean | number>;
        /**
         * Obtains all KV pairs that match the specified key prefix. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { string } keyPrefix - Key prefix to match.
         * @param { AsyncCallback<Entry[]> } callback - Callback used to return the KV pairs that match the specified prefix.
         * @returns { void } Returns void.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#getEntries
         */
        getEntries(keyPrefix: string, callback: AsyncCallback<Entry[]>): void;
        /**
         * Obtains all KV pairs that match the specified key prefix. This API uses a promise to return the result.
         *
         * @param { string } keyPrefix - Key prefix to match.
         * @returns { Promise<Entry[]> } Promise used to return the KV pairs that match the specified prefix.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#getEntries
         */
        getEntries(keyPrefix: string): Promise<Entry[]>;
        /**
         * Obtains the KV pairs that match the specified **Query** object. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { Query } query - Key prefix to match.
         * @param { AsyncCallback<Entry[]> } callback - Callback used to return the KV pairs that match the specified **Query**
         *     object.
         * @returns { Entry[] } Returns the list of key-value pairs matching the specified {@code Query} object.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#getEntries
         */
        getEntries(query: Query, callback: AsyncCallback<Entry[]>): void;
        /**
         * Obtains the KV pairs that match the specified **Query** object. This API uses a promise to return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<Entry[]> } Promise used to return the KV pairs that match the specified **Query** object.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#getEntries
         */
        getEntries(query: Query): Promise<Entry[]>;
        /**
         * Obtains the result set with the specified prefix. This API uses an asynchronous callback to return the result.
         *
         * @param { string } keyPrefix - Key prefix to match.
         * @param { AsyncCallback<KvStoreResultSet> } callback - Callback used to return the result set with the specified prefix.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#getResultSet
         */
        getResultSet(keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>): void;
        /**
         * Obtains the result set with the specified prefix. This API uses a promise to return the result.
         *
         * @param { string } keyPrefix - Key prefix to match.
         * @returns { Promise<KvStoreResultSet> } Promise used to return the result set with the specified prefix.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#getResultSet
         */
        getResultSet(keyPrefix: string): Promise<KvStoreResultSet>;
        /**
         * Obtains a **KvStoreResultSet** object that matches the specified **Query** object. This API uses an asynchronous
         *  callback to return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<KvStoreResultSet> } callback - Callback used to return the **KvStoreResultSet** object obtained.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#getResultSet
         */
        getResultSet(query: Query, callback: AsyncCallback<KvStoreResultSet>): void;
        /**
         * Obtains a **KvStoreResultSet** object that matches the specified **Query** object. This API uses a promise to
         * return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<KvStoreResultSet> } Promise used to return the **KvStoreResultSet** object obtained.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#getResultSet
         */
        getResultSet(query: Query): Promise<KvStoreResultSet>;
        /**
         * Closes the **KvStoreResultSet** object obtained by
         * [SingleKVStore.getResultSet]{@link distributedData.SingleKVStore.getResultSet(keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>)}
         * . This API uses an asynchronous callback to return the result.
         *
         * @param { KvStoreResultSet } resultSet - **KvStoreResultSet** object to close.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#closeResultSet
         */
        closeResultSet(resultSet: KvStoreResultSet, callback: AsyncCallback<void>): void;
        /**
         * Closes the **KvStoreResultSet** object obtained by
         * [SingleKVStore.getResultSet]{@link distributedData.SingleKVStore.getResultSet(keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>)}
         * . This API uses a promise to return the result.
         *
         * @param { KvStoreResultSet } resultSet - **KvStoreResultSet** object to close.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#closeResultSet
         */
        closeResultSet(resultSet: KvStoreResultSet): Promise<void>;
        /**
         * Obtains the number of results that match the specified **Query** object. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<number> } callback - Callback used to return the number of results that match the specified
         *     **Query** object.
         * @returns { number } Returns the number of results matching the specified {@code Query} object.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#getResultSize
         */
        getResultSize(query: Query, callback: AsyncCallback<number>): void;
        /**
         * Obtains the number of results that match the specified **Query** object. This API uses a promise to return the
         * result.
         *
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<number> } Promise used to return the number of results obtained.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#getResultSize
         */
        getResultSize(query: Query): Promise<number>;
        /**
         * Deletes data of a device. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#removeDeviceData
         */
        removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void;
        /**
         * Deletes data of a device. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#removeDeviceData
         */
        removeDeviceData(deviceId: string): Promise<void>;
        /**
         * Synchronizes the KV store manually.
         *
         * > **NOTE**
         * >
         * > **deviceIds** is **networkId** in <!--RP2-->
         * > [DeviceInfo]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceInfo}, which can be obtained by
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP2End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string[] } deviceIds - List of **networkId**s of the devices in the same networking environment to be
         *     synchronized.
         * @param { SyncMode } mode - Sync mode.
         * @param { number } delayMs - Delay time allowed, in milliseconds. The default value is **0**.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#sync
         */
        sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void;
        /**
         * Subscribes to data changes of the specified type.
         *
         * @param { 'dataChange' } event - Event type. The value is **dataChange**, which indicates data changes.
         * @param { SubscribeType } type - Type of data change.
         * @param { Callback<ChangeNotification> } listener - Callback used to return the result.
         * @throws Throws this exception if no {@code SingleKvStore} database is available.
         *     {@code DB_ERROR}, and {@code STORE_ALREADY_SUBSCRIBE}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#on
         */
        on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void;
        /**
         * Subscribes to sync completion events.
         *
         * @param { 'syncComplete' } event - Event type. The value is **syncComplete**, which indicates a sync completion event.
         * @param { Callback<Array<[ string, number ]>> } syncCallback - Callback used to return a sync completion event.
         * @throws Throws this exception if no {@code SingleKvStore} database is available.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#on
         */
        on(event: 'syncComplete', syncCallback: Callback<Array<[
            string,
            number
        ]>>): void;
        /**
         * Unsubscribes from data changes.
         *
         * @param { 'dataChange' } event - Event type. The value is **dataChange**, which indicates data changes.
         * @param { Callback<ChangeNotification> } listener - Callback to unregister. If this parameter is not specified, all
         *     callbacks for data changes will be unregistered.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#off
         */
        off(event: 'dataChange', listener?: Callback<ChangeNotification>): void;
        /**
         * Unsubscribes from sync completion events.
         *
         * @param { 'syncComplete' } event - Event type. The value is **syncComplete**, which indicates a sync completion event.
         * @param { Callback<Array<[ string, number ]>> } syncCallback - Callback to unregister. If this parameter is not specified,
         *     all callbacks for data changes will be unregistered.
         * @throws Throws this exception if no {@code SingleKvStore} database is available.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#off
         */
        off(event: 'syncComplete', syncCallback?: Callback<Array<[
            string,
            number
        ]>>): void;
        /**
         * Sets the default delay allowed for KV store sync. This API uses an asynchronous callback to return the result.
         *
         * @param { number } defaultAllowedDelayMs - Default delay allowed for database sync, in ms.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#setSyncParam
         */
        setSyncParam(defaultAllowedDelayMs: number, callback: AsyncCallback<void>): void;
        /**
         * Sets the default delay allowed for KV store sync. This API uses a promise to return the result.
         *
         * @param { number } defaultAllowedDelayMs - Default delay allowed for database sync, in ms.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if any of the following errors occurs:{@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#setSyncParam
         */
        setSyncParam(defaultAllowedDelayMs: number): Promise<void>;
        /**
         * Obtains the security level of this KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<SecurityLevel> } callback - Callback used to return the security level of the KV store.
         * @returns { SecurityLevel } {@code SecurityLevel} the security level of the database.
         * @throws Throws this exception if any of the following errors occurs:{@code SERVER_UNAVAILABLE},
         *     {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#getSecurityLevel
         */
        getSecurityLevel(callback: AsyncCallback<SecurityLevel>): void;
        /**
         * Obtains the security level of this KV store. This API uses a promise to return the result.
         *
         * @returns { Promise<SecurityLevel> } Promise used to return the security level of the KV store.
         * @throws Throws this exception if any of the following errors occurs:{@code SERVER_UNAVAILABLE},
         *     {@code IPC_ERROR}, and {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.SingleKVStore#getSecurityLevel
         */
        getSecurityLevel(): Promise<SecurityLevel>;
    }
    /**
     * Provides APIs to query and synchronize data in a device KV store. This class inherits from
     * [KVStore]{@link distributedData.KVStoreType}.
     * Data is distinguished by device in a device KV store. Each device can only write and modify its own data. Data of
     * other devices is read-only and cannot be modified.
     * For example, a device KV store can be used to implement image sharing between devices. The images of other devices
     * can be viewed, but not be modified or deleted.
     * Before calling any method in **DeviceKVStore**, you must use
     * [getKVStore]{@link distributedData.KVManager.getKVStore<T extends KVStore>(storeId: string, options: Options, callback: AsyncCallback<T>)}
     *  to obtain a **DeviceKVStore** object.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.DeviceKVStore
     */
    interface DeviceKVStore extends KVStore {
        /**
         * Obtains a string value that matches the specified device ID and key. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { string } key - Key to match.
         * @param { AsyncCallback<boolean | string | number | Uint8Array> } callback - Callback used to return the value obtained.
         * @returns { void } Returns void.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}, and {@code KEY_NOT_FOUND}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#get
         */
        get(deviceId: string, key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void;
        /**
         * Obtains a string value that matches the specified device ID and key. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { string } key - Key to match.
         * @returns { Promise<boolean | string | number | Uint8Array> } Promise used to return the string value that matches the
         *     given condition.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}, and {@code KEY_NOT_FOUND}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#get
         */
        get(deviceId: string, key: string): Promise<boolean | string | number | Uint8Array>;
        /**
         * Obtains all KV pairs that match the specified device ID and key prefix. This API uses an asynchronous callback to
         *  return the result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { string } keyPrefix - Key prefix to match.
         * @param { AsyncCallback<Entry[]> } callback - Callback used to return the KV pairs obtained.
         * @returns { void } Returns void.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getEntries
         */
        getEntries(deviceId: string, keyPrefix: string, callback: AsyncCallback<Entry[]>): void;
        /**
         * Obtains all KV pairs that match the specified device ID and key prefix. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { string } keyPrefix - Key prefix to match.
         * @returns { Promise<Entry[]> } Promise used to return all the KV pairs that match the given condition.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getEntries
         */
        getEntries(deviceId: string, keyPrefix: string): Promise<Entry[]>;
        /**
         * Obtains the KV pairs that match the specified **Query** object. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<Entry[]> } callback - Callback used to return the KV pairs obtained.
         * @returns { Entry[] } Returns the list of key-value pairs matching the specified {@code Query} object.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getEntries
         */
        getEntries(query: Query, callback: AsyncCallback<Entry[]>): void;
        /**
         * Obtains the KV pairs that match the specified **Query** object. This API uses a promise to return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<Entry[]> } Promise used to return the KV pairs that match the specified **Query** object.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getEntries
         */
        getEntries(query: Query): Promise<Entry[]>;
        /**
         * Obtains the KV pairs that match the specified device ID and **Query** object. This API uses an asynchronous
         * callback to return the result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<Entry[]> } callback - Callback used to return the KV pairs that match the specified device ID and
         *     **Query** object.
         * @returns { Entry[] } Returns the list of key-value pairs matching the specified {@code Query} object.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getEntries
         */
        getEntries(deviceId: string, query: Query, callback: AsyncCallback<Entry[]>): void;
        /**
         * Obtains the KV pairs that match the specified device ID and **Query** object. This API uses a promise to return
         * the result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<Entry[]> } Promise used to return the KV pairs that match the specified device ID and **Query**
         *     object.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getEntries
         */
        getEntries(deviceId: string, query: Query): Promise<Entry[]>;
        /**
         * Obtains a **KvStoreResultSet** object that matches the specified device ID and key prefix. This API uses an
         * asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { string } keyPrefix - Key prefix to match.
         * @param { AsyncCallback<KvStoreResultSet> } callback - Callback used to return the **KvStoreResultSet** object that
         *     matches the specified device ID and key prefix.
         * @returns { KvStoreResultSet } Returns the {@code KvStoreResultSet} objects.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getResultSet
         */
        getResultSet(deviceId: string, keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>): void;
        /**
         * Obtains a **KvStoreResultSet** object that matches the specified device ID and key prefix. This API uses a
         * promise to return the result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { string } keyPrefix - Key prefix to match.
         * @returns { Promise<KvStoreResultSet> } Promise used to return the **KvStoreResultSet** object that matches the specified
         *     device ID and key prefix.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getResultSet
         */
        getResultSet(deviceId: string, keyPrefix: string): Promise<KvStoreResultSet>;
        /**
         * Obtains a **KvStoreResultSet** object that matches the specified **Query** object. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<KvStoreResultSet> } callback - Callback used to return the **KvStoreResultSet** object obtained.
         * @returns { KvStoreResultSet } Returns the {@code KvStoreResultSet} object matching the specified {@code Query} object.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getResultSet
         */
        getResultSet(query: Query, callback: AsyncCallback<KvStoreResultSet>): void;
        /**
         * Obtains a **KvStoreResultSet** object that matches the specified **Query** object. This API uses a promise to
         * return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<KvStoreResultSet> } Promise used to return the **KvStoreResultSet** object that matches the specified
         *     **Query** object.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getResultSet
         */
        getResultSet(query: Query): Promise<KvStoreResultSet>;
        /**
         * Obtains a **KvStoreResultSet** object that matches the specified device ID and **Query** object. This API uses an
         *  asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<KvStoreResultSet> } callback - Callback used to return the **KvStoreResultSet** object that
         *     matches the specified device ID and **Query** object.
         * @returns { KvStoreResultSet } Returns the {@code KvStoreResultSet} object matching the specified {@code Query} object.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getResultSet
         */
        getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KvStoreResultSet>): void;
        /**
         * Obtains a **KvStoreResultSet** object that matches the specified device ID and **Query** object. This API uses a
         * promise to return the result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<KvStoreResultSet> } Promise used to return the **KvStoreResultSet** object that matches the specified
         *     device ID and **Query** object.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getResultSet
         */
        getResultSet(deviceId: string, query: Query): Promise<KvStoreResultSet>;
        /**
         * Closes the **KvStoreResultSet** object obtained by
         * [DeviceKVStore.getResultSet]{@link getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KvStoreResultSet>)}. This
         * API uses an asynchronous callback to return the result.
         *
         * @param { KvStoreResultSet } resultSet - **KvStoreResultSet** object to close.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#closeResultSet
         */
        closeResultSet(resultSet: KvStoreResultSet, callback: AsyncCallback<void>): void;
        /**
         * Closes the **KvStoreResultSet** object obtained by
         * [DeviceKVStore.getResultSet]{@link getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KvStoreResultSet>)}. This
         * API uses a promise to return the result.
         *
         * @param { KvStoreResultSet } resultSet - **KvStoreResultSet** object to close.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#closeResultSet
         */
        closeResultSet(resultSet: KvStoreResultSet): Promise<void>;
        /**
         * Obtains the number of results that match the specified **Query** object. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<number> } callback - Callback used to return the number of results obtained.
         * @returns { number } Returns the number of results matching the specified {@code Query} object.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getResultSize
         */
        getResultSize(query: Query, callback: AsyncCallback<number>): void;
        /**
         * Obtains the number of results that match the specified **Query** object. This API uses a promise to return the
         * result.
         *
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<number> } Promise used to return the number of results obtained.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getResultSize
         */
        getResultSize(query: Query): Promise<number>;
        /**
         * Obtains the number of results that match the specified device ID and **Query** object. This API uses an
         * asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { Query } query - **Query** object to match.
         * @param { AsyncCallback<number> } callback - Callback used to return the number of results obtained.
         * @returns { number } Returns the number of results matching the specified {@code Query} object.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getResultSize
         */
        getResultSize(deviceId: string, query: Query, callback: AsyncCallback<number>): void;
        /**
         * Obtains the number of results that match the specified device ID and **Query** object. This API uses a promise to
         *  return the result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { Query } query - **Query** object to match.
         * @returns { Promise<number> } Promise used to return the number of results obtained.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#getResultSize
         */
        getResultSize(deviceId: string, query: Query): Promise<number>;
        /**
         * Deletes data of the specified device from this KV store. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#removeDeviceData
         */
        removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void;
        /**
         * Deletes data of the specified device from this KV store. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > The value of **deviceId** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         * > For details about how to obtain **deviceId**, see [sync()]{@link distributedData.SingleKVStore.sync}.
         *
         * @param { string } deviceId - ID of the target device.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if any of the following errors occurs: {@code INVALID_ARGUMENT},
         *     {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR}, {@code DB_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#removeDeviceData
         */
        removeDeviceData(deviceId: string): Promise<void>;
        /**
         * Synchronizes the KV store manually.
         *
         * > **NOTE**
         * >
         * > **deviceIds** is **networkId** in <!--RP2-->
         * > [DeviceInfo]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceInfo}, which can be obtained by
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}.
         * > <!--RP2End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string[] } deviceIds - **networkId**s of the devices to be synchronized.
         * @param { number } delayMs - Delay time allowed, in milliseconds. The default value is **0**.
         * @param { SyncMode } mode - Sync mode.
         * @throws Throws this exception if no DeviceKVStore database is available.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#sync
         */
        sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void;
        /**
         * Subscribes to data changes of the specified type.
         *
         * @param { 'dataChange' } event - Event type. The value is **dataChange**, which indicates data changes.
         * @param { SubscribeType } type - Type of data change.
         * @param { Callback<ChangeNotification> } listener - Callback used to return the result.
         * @throws Throws this exception if any of the following errors
         *     occurs: {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR},
         *     {@code DB_ERROR}, and {@code STORE_ALREADY_SUBSCRIBE}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#on
         */
        on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void;
        /**
         * Subscribes to sync completion events.
         *
         * @param { 'syncComplete' } event - Event type. The value is **syncComplete**, which indicates a sync completion event.
         * @param { Callback<Array<[ string, number ]>> } syncCallback - Callback used to return a sync completion event.
         * @throws Throws this exception if no DeviceKVStore database is available.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#on
         */
        on(event: 'syncComplete', syncCallback: Callback<Array<[
            string,
            number
        ]>>): void;
        /**
         * Unsubscribes from data changes.
         *
         * @param { 'dataChange' } event - Event type. The value is **dataChange**, which indicates data changes.
         * @param { Callback<ChangeNotification> } listener - Callback to unregister. If this parameter is not specified, all
         *     callbacks for data changes will be unregistered.
         * @throws Throws this exception if any of the following errors
         *     occurs: {@code SERVER_UNAVAILABLE}, {@code IPC_ERROR},
         *     {@code DB_ERROR}, and {@code STORE_ALREADY_SUBSCRIBE}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#off
         */
        off(event: 'dataChange', listener?: Callback<ChangeNotification>): void;
        /**
         * Unsubscribes from sync completion events.
         *
         * @param { 'syncComplete' } event - Event type. The value is **syncComplete**, which indicates a sync completion event.
         * @param { Callback<Array<[ string, number ]>> } syncCallback - Callback to unregister. If this parameter is not specified,
         *     all callbacks for data changes will be unregistered.
         * @throws Throws this exception if no DeviceKVStore database is available.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.DeviceKVStore#off
         */
        off(event: 'syncComplete', syncCallback?: Callback<Array<[
            string,
            number
        ]>>): void;
    }
    /**
     * Creates a **KVManager** instance to manage KV stores. This API uses an asynchronous callback to return the result.
     *
     * @param { KVManagerConfig } config - Configuration of the **KVManager** instance, including the bundle name and user
     *     information of the caller.
     * @param { AsyncCallback<KVManager> } callback - Callback used to return the **KVManager** instance created.
     * @returns { void } Returns the {@code KVManager} instance.
     * @throws Throws exception if input is invalid.
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore#createKVManager
     */
    function createKVManager(config: KVManagerConfig, callback: AsyncCallback<KVManager>): void;
    /**
     * Creates a **KVManager** instance to manage KV stores. This API uses a promise to return the result.
     *
     * @param { KVManagerConfig } config - Configuration of the **KVManager** instance, including the bundle name and user
     *     information of the caller.
     * @returns { Promise<KVManager> } Promise used to return the **KVManager** instance created.
     * @throws Throws exception if input is invalid.
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore#createKVManager
     */
    function createKVManager(config: KVManagerConfig): Promise<KVManager>;
    /**
     * Creates a **KVManager** object to obtain KV store information. Before calling any method in **KVManager**, you must
     *  use
     * [createKVManager]{@link distributedData.createKVManager(config: KVManagerConfig, callback: AsyncCallback<KVManager>)}
     *  to create a **KVManager** object.
     *
     * @syscap SystemCapability.DistributedDataManager.KVStore.Core
     * @version 1
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.data.distributedKVStore.KVManager
     */
    interface KVManager {
        /**
         * Creates and obtains a KV store. This API uses a promise to return the result.
         *
         * @param { Options } options - Configuration of the KV store.
         * @param { string } storeId - Unique identifier of the KV store. The length cannot exceed
         *     [MAX_STORE_ID_LENGTH]{@link distributedData.Constants}.
         * @returns { Promise<T>, <T extends KVStore> } Promise used to return the KV store instance created.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVManager#getKVStore
         */
        getKVStore<T extends KVStore>(storeId: string, options: Options): Promise<T>;
        /**
         * Creates and obtains a KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { Options } options - Configuration of the KV store.
         * @param { string } storeId - Unique identifier of the KV store. The length cannot exceed
         *     [MAX_STORE_ID_LENGTH]{@link distributedData.Constants}.
         * @param { AsyncCallback<T> } callback - Callback used to return the KV store instance created.
         * @returns { void } Returns a {@code KVStore}, or {@code SingleKVStore}.* @syscap
         *     SystemCapability.DistributedDataManager.KVStore.Core
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVManager#getKVStore
         */
        getKVStore<T extends KVStore>(storeId: string, options: Options, callback: AsyncCallback<T>): void;
        /**
         * Closes a KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { string } appId - Bundle name of the app that invokes the KV store.
         * @param { string } storeId - Unique identifier of the KV store to close. The length cannot exceed
         *     [MAX_STORE_ID_LENGTH]{@link distributedData.Constants}.
         * @param { KVStore } kvStore - KV store to close.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if any of the following errors
         * occurs:{@code INVALID_ARGUMENT}, {@code SERVER_UNAVAILABLE},
         * {@code STORE_NOT_OPEN}, {@code STORE_NOT_FOUND}, {@code DB_ERROR},
         * {@code PERMISSION_DENIED}, and {@code IPC_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVManager#closeKVStore
         */
        closeKVStore(appId: string, storeId: string, kvStore: KVStore, callback: AsyncCallback<void>): void;
        /**
         * Closes a KV store. This API uses a promise to return the result.
         *
         * @param { string } appId - Bundle name of the app that invokes the KV store.
         * @param { string } storeId - Unique identifier of the KV store to close. The length cannot exceed
         *     [MAX_STORE_ID_LENGTH]{@link distributedData.Constants}.
         * @param { KVStore } kvStore - KV store to close.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if any of the following errors
         * occurs:{@code INVALID_ARGUMENT}, {@code SERVER_UNAVAILABLE},
         * {@code STORE_NOT_OPEN}, {@code STORE_NOT_FOUND}, {@code DB_ERROR},
         * {@code PERMISSION_DENIED}, and {@code IPC_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVManager#closeKVStore
         */
        closeKVStore(appId: string, storeId: string, kvStore: KVStore): Promise<void>;
        /**
         * Deletes a KV store. This API uses an asynchronous callback to return the result.
         *
         * @param { string } appId - Bundle name of the app that invokes the KV store.
         * @param { string } storeId - Unique identifier of the KV store to delete. The length cannot exceed
         *     [MAX_STORE_ID_LENGTH]{@link distributedData.Constants}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws Throws this exception if any of the following errors
         * occurs: {@code INVALID_ARGUMENT},
         * {@code SERVER_UNAVAILABLE}, {@code STORE_NOT_FOUND},
         * {@code DB_ERROR}, {@code PERMISSION_DENIED}, and {@code IPC_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVManager#deleteKVStore
         */
        deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void;
        /**
         * Deletes a KV store. This API uses a promise to return the result.
         *
         * @param { string } appId - Bundle name of the app that invokes the KV store.
         * @param { string } storeId - Unique identifier of the KV store to delete. The length cannot exceed
         *     [MAX_STORE_ID_LENGTH]{@link distributedData.Constants}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws Throws this exception if any of the following errors
         * occurs: {@code INVALID_ARGUMENT},
         * {@code SERVER_UNAVAILABLE}, {@code STORE_NOT_FOUND},
         * {@code DB_ERROR}, {@code PERMISSION_DENIED}, and {@code IPC_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVManager#deleteKVStore
         */
        deleteKVStore(appId: string, storeId: string): Promise<void>;
        /**
         * Obtains the IDs of all KV stores that are created by
         * [getKVStore()]{@link distributedData.KVManager.getKVStore<T extends KVStore>(storeId: string, options: Options, callback: AsyncCallback<T>)}
         *  and have not been deleted by
         * [deleteKVStore()]{@link distributedData.KVManager.deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>)}
         * . This API uses an asynchronous callback to return the result.
         *
         * @param { string } appId - Bundle name of the app that invokes the KV store.
         * @param { AsyncCallback<string[]> } callback - Callback used to return the IDs of all created KV stores.
         * @returns { void } Returns the storeId of all created {@code KvStore} databases.
         * @throws Throws this exception if any of the following errors
         * occurs: {@code SERVER_UNAVAILABLE}, {@code DB_ERROR},
         * {@code PERMISSION_DENIED}, and {@code IPC_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVManager#getAllKVStoreId
         */
        getAllKVStoreId(appId: string, callback: AsyncCallback<string[]>): void;
        /**
         * Obtains the IDs of all KV stores that are created by
         * [getKVStore()]{@link distributedData.KVManager.getKVStore<T extends KVStore>(storeId: string, options: Options, callback: AsyncCallback<T>)}
         *  and have not been deleted by
         * [deleteKVStore()]{@link distributedData.KVManager.deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>)}
         * . This API uses a promise to return the result.
         *
         * @param { string } appId - Bundle name of the app that invokes the KV store.
         * @returns { Promise<string[]> } Promise used to return the IDs of all created KV stores.
         * @throws Throws this exception if any of the following errors
         * occurs: {@code SERVER_UNAVAILABLE}, {@code DB_ERROR},
         * {@code PERMISSION_DENIED}, and {@code IPC_ERROR}.
         * @syscap SystemCapability.DistributedDataManager.KVStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVManager#getAllKVStoreId
         */
        getAllKVStoreId(appId: string): Promise<string[]>;
        /**
         * Subscribes to service status changes.
         *
         * @param { 'distributedDataServiceDie' } event - Event type. The value is **distributedDataServiceDie**, which indicates
         *     service status changes.
         * @param { Callback<void> } deathCallback - Callback used to return the result.
         * @throws    exception maybe occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVManager#on
         */
        on(event: 'distributedDataServiceDie', deathCallback: Callback<void>): void;
        /**
         * Unsubscribes from service status changes.
         *
         * @param { 'distributedDataServiceDie' } event - Event type. The value is **distributedDataServiceDie**, which indicates
         *     service status changes.
         * @param { Callback<void> } deathCallback - Callback to unregister. If this parameter is not specified, all callbacks for
         *     service status changes will be unregistered.
         * @throws exception maybe occurs.
         * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.data.distributedKVStore.KVManager#off
         */
        off(event: 'distributedDataServiceDie', deathCallback?: Callback<void>): void;
    }
}
/**
 * Providers interfaces to creat a {@link KVManager} instance.
 * @syscap SystemCapability.DistributedDataManager.KVStore.DistributedKVStore
 * @since 7
 * @deprecated since 9
 */
export default distributedData;

```
