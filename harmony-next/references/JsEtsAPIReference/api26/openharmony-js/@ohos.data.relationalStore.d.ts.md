# @ohos.data.relationalStore.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2025 Huawei Device Co., Ltd.
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
import Context from './application/BaseContext';
import sendableRelationalStore from './@ohos.data.sendableRelationalStore';
/**
 * The relational database (RDB) manages data based on relational models. The **relationalStore** module provides a
 * complete mechanism for managing local databases based on the underlying SQLite. You can use the APIs to perform
 * operations such as adding, deleting, modifying, and querying data, and directly run SQL statements. In addition, you
 * can obtain sendable data using
 * [ResultSet.getSendableRow]{@link @ohos.data.relationalStore:relationalStore.ResultSet.getSendableRow} and transfer
 * the data across threads.
 *
 * To ensure successful data access, limit the size of a data record to 2 MB. If a data record exceeds 2 MB, it can be
 * inserted successfully but cannot be read.
 *
 * Querying data from a large amount of data may take time or even cause application suspension. In this case, you can
 * perform batch operations. For details, see
 * [Batch Database Operations](docroot://arkts-utils/batch-database-operations-guide.md). Moreover, observe the
 * following:
 *
 * - The number of data records to be queried at a time should not exceed 5000.
 * - Use [TaskPool]{@link @ohos.taskpool:taskpool} if there is a large amount of data needs to be queried.
 * - Keep concatenated SQL statements as concise as possible.
 * - Query data in batches.
 *
 * The **relationalStore** module provides the following functionalities:
 *
 * - [RdbPredicates]{@link @ohos.data.relationalStore:relationalStore}: provides predicates indicating the nature,
 * feature, or relationship of a data entity in an RDB store. It is used to define the operation conditions for an RDB
 * store.
 * - [RdbStore]{@link @ohos.data.relationalStore:relationalStore}: provides APIs for managing data in an RDB store.
 * - [ResultSet]{@link @ohos.data.relationalStore:relationalStore}: provides APIs for accessing the result set obtained
 * from the RDB store.
 * - [LiteResultSet]{@link @ohos.data.relationalStore:relationalStore}: provides APIs for accessing the result set
 * obtained from the RDB store, such as
 * [queryWithoutRowCount]{@link @ohos.data.relationalStore:relationalStore.RdbStore.queryWithoutRowCount} and
 * [querySqlWithoutRowCount]{@link @ohos.data.relationalStore:relationalStore.RdbStore.querySqlWithoutRowCount}. Unlike
 * [ResultSet]{@link @ohos.data.relationalStore:relationalStore}, **LiteResultSet** does not include the total number of
 * rows in the query result.
 * - [Transaction]{@link @ohos.data.relationalStore:relationalStore}: provides APIs for managing transaction objects.
 *
 * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
 * @crossplatform [since 10]
 * @since 9
 */
declare namespace relationalStore {
    /**
     * Enumerates the asset statuses. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 10
     */
    enum AssetStatus {
        /**
         * The asset is in normal status.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        ASSET_NORMAL,
        /**
         * The asset is to be inserted to the cloud.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        ASSET_INSERT,
        /**
         * The asset is to be updated to the cloud.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        ASSET_UPDATE,
        /**
         * The asset is to be deleted from the cloud.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        ASSET_DELETE,
        /**
         * The asset is in abnormal status.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        ASSET_ABNORMAL,
        /**
         * The asset is being downloaded to a local device.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        ASSET_DOWNLOADING,
        /**
         * ASSET_TO_DOWNLOAD: means the asset will be downloaded.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        ASSET_TO_DOWNLOAD
    }
    /**
     * Represents the asset (such as a document, image, or video).
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 10
     */
    interface Asset {
        /**
         * Asset name.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        name: string;
        /**
         * Asset URI, which is an absolute path in the system.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        uri: string;
        /**
         * Path of an asset in the application sandbox.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        path: string;
        /**
         * Time when an asset is created.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        createTime: string;
        /**
         * Time when an asset is last modified.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        modifyTime: string;
        /**
         * Asset size. In the device-cloud sync mechanism, this field is one of the key bases for determining whether an
         * asset is changed. Ensure that the storage format and value logic are consistent across the end-to-end link. It is
         * recommended that all system nodes use the standard processing format (unit: byte; value: a non-negative integer)
         * to avoid sync exceptions or misjudgment caused by format differences.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        size: string;
        /**
         * Asset status.
         *
         * Default value: **ASSET_NORMAL**.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        status?: AssetStatus;
    }
    /**
     * Indicates several assets in one column
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 10
     */
    type Assets = Asset[];
    /**
     * Indicates possible value types
     *
     * @unionmember { null } The value is a null
     * @unionmember { long } The value is a long
     * @unionmember { double } The value is a double
     * @unionmember { string } The value is a string
     * @unionmember { boolean } The value is a boolean
     * @unionmember { Uint8Array } The value is an array of the Uint8
     * @unionmember { Asset } The value is an asset [since 10]
     * @unionmember { Assets } The value is an array of the asset [since 10]
     * @unionmember { Float32Array } The value is an array of the float32 [since 12]
     * @unionmember { bigint } The value is an integer of any length [since 12]
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 10]
     * @since 9
     */
    type ValueType = null | number | string | boolean | Uint8Array | Asset | Assets | Float32Array | bigint;
    /**
     * Values in buckets are stored in key-value pairs, change {[key: string]: ValueType;} to Record<string, ValueType>
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 10]
     * @since 9
     */
    type ValuesBucket = Record<string, ValueType>;
    /**
     * The type of the priority key can be number or string
     *
     * @unionmember { long } The value is a long
     * @unionmember { double } The value is a double
     * @unionmember { string } The value is a string
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @FaAndStageModel
     * @since 10
     */
    type PRIKeyType = number | string;
    /**
     * The time is in UTC format.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 10
     */
    type UTCTime = Date;
    /**
     * Indicates the primary key and UTC time of the modified rows.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 10
     */
    type ModifyTime = Map<PRIKeyType, UTCTime>;
    /**
     * Indicates a row of data with an array.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @stagemodelonly
     * @crossplatform
     * @since 23
     */
    type RowData = Array<ValueType>;
    /**
     * Indicates multiple rows of data with an array.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @stagemodelonly
     * @crossplatform
     * @since 23
     */
    type RowsData = Array<RowData>;
    /**
     * Defines the RDB store configuration.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 10]
     * @since 9
     */
    interface StoreConfig {
        /**
         * Database file name, which is the unique identifier of the RDB store. Creating two databases with the same name in
         * the same process is prohibited; otherwise, functions such as device-device sync, device-cloud sync, silent access
         * , and key backup may malfunction.
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        name: string;
        /**
         * Security level of the RDB store.
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 9
         */
        securityLevel: SecurityLevel;
        /**
         * Whether to encrypt the RDB store. After the database is created, this parameter cannot be modified directly. To
         * change the database encryption status, call the
         * [rekeyEx]{@link @ohos.data.relationalStore:relationalStore.RdbStore.rekeyEx} API.
         *
         * **true**: encrypt the RDB store.
         *
         * **false** (default): not encrypt the RDB store.
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        encrypt?: boolean;
        /**
         * Application group ID. <!--RP1-->Currently, this parameter is not supported.<!--RP1End-->
         *
         * **Model restriction**: This parameter can be used only in the stage model.
         *
         * This parameter is supported since API version 10. If **dataGroupId** is specified, the **RdbStore** instance will
         * be created in the sandbox directory of the specified **dataGroupId**. However, the encrypted RDB store in this
         * sandbox directory does not support multi-process access. If this parameter is left blank, the **RdbStore**
         * instance will be created in the sandbox directory of the application by default.
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @StageModelOnly
         * @since 10
         */
        dataGroupId?: string;
        /**
         * Custom database path.
         *
         * **Constraints**: The maximum length of the database path is 128 bytes. If the database path exceeds 128 bytes,
         * the RDB store fails to be opened and an error is returned.
         *
         * This parameter is supported since API version 11. The database is created in the following directory structure:
         * **context.databaseDir** + **"/rdb/"** + **customDir**, where **context.databaseDir** indicates the path of the
         * application sandbox, **"/rdb/"** indicates the relational database created, and **customDir** indicates a user-
         * defined path. If this parameter is left blank, the **RdbStore** instance will be created in the sandbox directory
         * of the application by default. Since API version 18, if the **rootDir** parameter is also configured, the
         * database in the following path will be opened or deleted: **rootDir** + "/" + **customDir** + "/" + **name**.
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 11
         */
        customDir?: string;
        /**
         * Root path of the database.
         *
         * This parameter is supported since API version 18. The database in the **rootDir** + "/" + **customDir** directory
         * will be opened or deleted. The database opened is read-only. Writing data to a read-only database will trigger
         * error 801. If this parameter is set when you want to open or delete an RDB store, ensure that the database file
         * exists in the corresponding path and the caller has the read permission. Otherwise, error 14800010 will be
         * returned.
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        rootDir?: string;
        /**
         * Whether to automatically clear the dirty data (data that has been deleted from the cloud) from the local device.
         * The value **true** means to clear the dirty data automatically; **false** means to clear the data manually.
         *
         * Default value: **true**.
         *
         * For a database with device-cloud synergy, this parameter can be used to set whether to automatically clear the
         * data deleted from the cloud on the device. You can manually clear the data by calling
         * [cleanDirtyData<sup>11+</sup>]{@link @ohos.data.relationalStore:relationalStore.RdbStore.
         *  cleanDirtyData(table: string,cursor: number, callback: AsyncCallback<void>)}
         * .
         *
         * This parameter is supported since API version 11.
         *
         * SystemCapability.DistributedDataManager.CloudSync.Client
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 11
         */
        autoCleanDirtyData?: boolean;
        /**
         * Whether to automatically delete the RDB store and create an empty table in the case of an exception.
         *
         * **true**: delete the RDB store and create an empty table in the case of an exception.
         *
         * **false** (default): not delete the RDB store in the case of an exception.
         *
         * This parameter is supported since API version 12.
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 12
         */
        allowRebuild?: boolean;
        /**
         * Whether the RDB store is a vector store. The value **true** means the RDB store is a vector store, and the value
         * **false** means the opposite.
         *
         * Default value: **false**.
         *
         * The vector store is ideal for storing and managing high-dimensional vector data, while the RDB store is optimal
         * for storing and processing structured data.
         *
         * Before calling **deleteRdbStore**, ensure that the **RdbStore** and **ResultSet** of the vector store have been
         * closed.
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 18
         */
        vector?: boolean;
        /**
         * Whether the RDB store is read-only.
         *
         * **true**: The RDB store is read-only. Writing data to the RDB store will result in error code 801.
         *
         * **false** (default): The RDB store is readable and writeable.
         *
         * This parameter is supported since API version 12.
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 12
         */
        isReadOnly?: boolean;
        /**
         * Loads custom dynamic libraries. Multiple dynamic library names can be passed in the array. For details, see
         * [Constraints and Examples of pluginLibs]
         * (docroot://reference/apis-arkdata/arkts-apis-data-relationalStore-i.md#constraints-and-examples-of-pluginlibs).
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 12
         */
        pluginLibs?: Array<string>;
        /**
         * Custom encryption parameters.
         *
         * If this parameter is left empty, the default encryption parameters are used. For details, see default values of
         * [CryptoParam]{@link relationalStore.CryptoParam}.
         *
         * This parameter is valid only when **encrypt** is set to **true** or the key is not empty.
         *
         * This parameter is supported since API version 14.
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        cryptoParam?: CryptoParam;
        /**
         * Type of the tokenizer to be used for FTS.
         *
         * If this parameter is left blank, English tokenization is supported if FTS does not support Chinese or multi-
         * language tokenization.
         *
         * If you want to use a custom tokenizer, you can configure it through the **pluginLibs** parameter. For details,
         * see [Restrictions and Examples of pluginLibs]
         * (docroot://reference/apis-arkdata/arkts-apis-data-relationalStore-i.md#constraints-and-examples-of-pluginlibs).
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 17
         */
        tokenizer?: Tokenizer;
        /**
         * Whether to persist an RDB store. The value **true** means to persist the RDB store; **false** means the opposite
         * (using an in-memory database). The default value is **true**.
         *
         * An in-memory database does not support encryption, backup, restore, cross-process access, and distributed
         * capabilities, with the **securityLevel** property ignored.
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 18
         */
        persist?: boolean;
        /**
         * Whether to enable the semantic index processing feature for the database. The value **true** means to enable the
         * semantic index processing feature; **false** means the opposite. The default value is **false**.
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 20
         */
        enableSemanticIndex?: boolean;
    }
    /**
     * Represents the configuration of database encryption parameters. This configuration is valid only when **encrypt**
     * of **StoreConfig** is set to **true** or the key is not empty.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 20]
     * @since 14
     */
    interface CryptoParam {
        /**
         * Key used for database encryption and decryption.
         *
         * If this parameter is not specified, the RDB store generates a key, saves the key, and uses the key to open the
         * database file.
         *
         * If the key is not required, you need to set the key to **0**.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        encryptionKey: Uint8Array;
        /**
         * Number of iterations of the PBKDF2 algorithm used in the RDB store. The value is an integer.
         *
         * Default value: **10000**.
         *
         * The value must be an integer greater than 0. If it is not an integer, the value is rounded down.
         *
         * If this parameter is not specified or is set to **0**, the default value **10000** and the default encryption
         * algorithm **AES_256_GCM** are used.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        iterationCount?: number;
        /**
         * Algorithm used for database encryption and decryption.
         *
         * Default value: **AES_256_GCM**.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        encryptionAlgo?: EncryptionAlgo;
        /**
         * HMAC algorithm used for database encryption and decryption.
         *
         * Default value: **SHA256**.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        hmacAlgo?: HmacAlgo;
        /**
         * PBKDF2 algorithm used for database encryption and decryption.
         *
         * Default value: the same as the HMAC algorithm used.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        kdfAlgo?: KdfAlgo;
        /**
         * Page size used for database encryption and decryption. The value is an integer. Unit: byte
         *
         * Default value: **1024**.
         *
         * The value must be an integer within the range of 1,024 to 65,536 and must be 2<sup>n</sup>. If the specified
         * value is not an integer, the value is rounded down.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        cryptoPageSize?: number;
    }
    /**
     * Enumerates the encryption algorithms for the database. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 20]
     * @since 14
     */
    enum EncryptionAlgo {
        /**
         * AES_256_GCM: Database is encrypted using AES_256_GCM.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        AES_256_GCM = 0,
        /**
         * AES_256_CBC: Database is encrypted using AES_256_CBC.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        AES_256_CBC = 1,
        /**
         * PLAIN_TEXT: Database is unencrypted.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 22
         */
        PLAIN_TEXT = 2
    }
    /**
     * Enumerates the HMAC algorithms for the database. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 20]
     * @since 14
     */
    enum HmacAlgo {
        /**
         * SHA1: HMAC_SHA1 algorithm.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        SHA1 = 0,
        /**
         * SHA256: HMAC_SHA256 algorithm.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        SHA256 = 1,
        /**
         * SHA512: HMAC_SHA512 algorithm.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        SHA512 = 2
    }
    /**
     * Enumerates the PBKDF2 algorithms for the database. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 20]
     * @since 14
     */
    enum KdfAlgo {
        /**
         * KDF_SHA1: PBKDF2_HMAC_SHA1 algorithm.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        KDF_SHA1 = 0,
        /**
         * KDF_SHA256: PBKDF2_HMAC_SHA256 algorithm.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        KDF_SHA256 = 1,
        /**
         * KDF_SHA512: PBKDF2_HMAC_SHA512 algorithm.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        KDF_SHA512 = 2
    }
    /**
     * Enumerates tokenizers that can be used for FTS. Use the enum name rather than the enum value.
     *
     * The table creation statement varies with the tokenizer in use.
     *
     * For details about the definition of **this.context** in the sample code, see the application
     * [context]{@link ./application/Context:Context} of the stage model.
     *
     * The following is an example of the table creation statement when **ICU_TOKENIZER** is used:
     *
     * The following is an example of the table creation statement when **CUSTOM_TOKENIZER** is used:
     *
     * The following is an example of the table creation statement when **CUSTOM_TOKENIZER** is used:
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 17
     */
    enum Tokenizer {
        /**
         * NONE_TOKENIZER: not use tokenizer
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 17
         */
        NONE_TOKENIZER = 0,
        /**
         * The ICU tokenizer is used, which supports Chinese and multiple languages. If the ICU tokenizer is used, you can
         * set the language to use, for example, **zh_CN** for Chinese and **tr_TR** for Turkish. For details about the
         * supported languages, see
         * [ICU tokenizer](https://gitcode.com/openharmony/third_party_icu/blob/master/icu4c/source/data/lang/en.txt). For
         * details about the language abbreviations, see
         * [locales](https://gitcode.com/openharmony/third_party_icu/tree/master/icu4c/source/data/locales).
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 17
         */
        ICU_TOKENIZER = 1,
        /**
         * A custom tokenizer is used. Chinese (simplified and traditional), English, and Arabic numerals are supported.
         * Compared with **ICU_TOKENIZER**, **CUSTOM_TOKENIZER** has advantages in tokenization accuracy and resident memory
         * usage. The self-developed tokenizer supports two modes: default tokenization mode and short word tokenization
         * mode (short_words). You can use the cut_mode parameter to specify the mode. If no mode is specified, the default
         * mode is used.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 18
         */
        CUSTOM_TOKENIZER = 2
    }
    /**
     * Enumerates the stages in the device-cloud sync progress. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 10
     */
    enum Progress {
        /**
         * SYNC_BEGIN: means the sync process begin.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        SYNC_BEGIN = 0,
        /**
         * SYNC_BEGIN: means the sync process is in progress
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        SYNC_IN_PROGRESS = 1,
        /**
         * SYNC_BEGIN: means the sync process is finished
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        SYNC_FINISH = 2
    }
    /**
     * Defines a struct for the device-cloud sync statistics of a database table.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 10
     */
    interface Statistic {
        /**
         * Total number of rows to be synced between the device and cloud in the database table.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        total: number;
        /**
         * Number of rows that are successfully synced between the device and cloud in the database table.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        successful: number;
        /**
         * Number of rows that failed to be synced between the device and cloud in the database table.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        failed: number;
        /**
         * Number of rows that are not executed for device-cloud sync in the database table.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        remained: number;
    }
    /**
     * Defines a struct for statistics of device-cloud upload and download tasks of a database table.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 10
     */
    interface TableDetails {
        /**
         * Describes the {@code Statistic} details of the upload process.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        upload: Statistic;
        /**
         * Describes the {@code Statistic} details of the download process.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        download: Statistic;
    }
    /**
     * Describes the status of {@code Progress}.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 10
     */
    enum ProgressCode {
        /**
         * The device-cloud sync is successful.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        SUCCESS = 0,
        /**
         * An unknown error occurs during the device-cloud sync.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        UNKNOWN_ERROR = 1,
        /**
         * A network error occurs during the device-cloud sync.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        NETWORK_ERROR = 2,
        /**
         * The cloud is unavailable.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        CLOUD_DISABLED = 3,
        /**
         * The device-cloud sync of another device is being performed.
         *
         * The sync of the local device can be performed only when the cloud resources are available.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        LOCKED_BY_OTHERS = 4,
        /**
         * The number of records or size of the data to be synced exceeds the maximum. The maximum value is configured on
         * the cloud.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        RECORD_LIMIT_EXCEEDED = 5,
        /**
         * The remaining cloud space is less than the size of the data to be synced.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        NO_SPACE_FOR_ASSET = 6,
        /**
         * The device-cloud sync is blocked due to the network strategy.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 12
         */
        BLOCKED_BY_NETWORK_STRATEGY = 7,
        /**
         * STOP_CLOUD_SYNC: means cloud synchronization has been stopped.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        STOP_CLOUD_SYNC = 8
    }
    /**
     * Describes detail of the cloud sync {@code Progress}.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 10
     */
    interface ProgressDetails {
        /**
         * Describes the status of data sync progress.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        schedule: Progress;
        /**
         * Describes the code of data sync progress.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        code: ProgressCode;
        /**
         * Indicates the code message.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        message?: string;
        /**
         * Statistics of each table.
         *
         * The key indicates the table name, and the value indicates the device-cloud sync statistics of the table.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        details: Record<string, TableDetails>;
    }
    /**
     * Represents statistics about SQL statements executed by the database.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 20]
     * @since 12
     */
    interface SqlExecutionInfo {
        /**
         * SQL statements executed. If the value of [batchInsert]
         * {@link @ohos.data.relationalStore:relationalStore.RdbStore.batchInsert(table: string)} is too large, multiple
         * SQL statements may be executed.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 12
         */
        sql: Array<string>;
        /**
         * Total time used to execute the SQL statements, in μs.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 12
         */
        totalTime: number;
        /**
         * Time used to obtain the handle, in μs.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 12
         */
        waitTime: number;
        /**
         * Time used to get the SQL statements ready and bind parameters, in μs.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 12
         */
        prepareTime: number;
        /**
         * Time used to execute the SQL statements, in μs.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 12
         */
        executeTime: number;
    }
    /**
     * Represents an exception message about the SQL statement executed by the database.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 20
     */
    interface ExceptionMessage {
        /**
         * Error code returned by the executed SQL statement. For details about the values and meanings, see
         * [SQLite Error Codes](https://www.sqlite.org/rescode.html).
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 20
         */
        code: number;
        /**
         * Exception message returned by the executed SQL statement.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 20
         */
        message: string;
        /**
         * SQL statement that reports the error.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 20
         */
        sql: string;
    }
    /**
     * Represents details about the SQL statement executed by the database.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 20
     */
    interface SqlInfo {
        /**
         * SQL statements to be executed.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 20
         */
        sql: string;
        /**
         * Parameters in the SQL statements to be executed.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 20
         */
        args: Array<ValueType>;
    }
    /**
     * Enumerates the KV store security levels. Use the enum name rather than the enum value. You cannot change the
     * security level of an RDB store from a higher level to a lower one.
     *
     * > **NOTE**
     * >
     * > To perform data sync operations, the RDB store security level must be lower than or equal to that of the peer
     * > device. For details, see [Access Control Mechanism in Cross-Device Sync]
     * > (docroot://database/sync-app-data-across-devices-overview.md#access-control-mechanism-in-cross-device-sync).
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 9
     */
    enum SecurityLevel {
        /**
         * The RDB store security level is low. If data leakage occurs, minor impact will be caused on the database. An
         * example would be a graph store containing non-sensitive system data such as wallpapers.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 9
         */
        S1 = 1,
        /**
         * The RDB store security level is medium. If data leakage occurs, moderate impact will be caused on the database.
         * An example would be a graph store containing audio and video data created by users or call logs.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 9
         */
        S2 = 2,
        /**
         * The RDB store security level is high. If data leakage occurs, major impact will be caused on the database. An
         * example would be a graph store containing user fitness, health, and location data.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 9
         */
        S3 = 3,
        /**
         * The RDB store security level is critical. If data leakage occurs, severe impact will be caused on the database.
         * An example would be a graph store containing authentication credentials and financial data.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 9
         */
        S4 = 4
    }
    /**
     * Defines the database synchronization mode. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 9
     */
    enum SyncMode {
        /**
         * Data is pushed from a local device to a remote device.
    
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        SYNC_MODE_PUSH = 0,
        /**
         * Data is pulled from a remote device to a local device.
    
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        SYNC_MODE_PULL = 1,
        /**
         * Synchronize with the data with the latest modification time.
    
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 10
         */
        SYNC_MODE_TIME_FIRST,
        /**
         * Synchronize data from a local device to the cloud.
    
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 10
         */
        SYNC_MODE_NATIVE_FIRST,
        /**
         * Synchronize data from the cloud to a local device.
    
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 10
         */
        SYNC_MODE_CLOUD_FIRST
    }
    /**
     * Enumerates the subscription types. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 9
     */
    enum SubscribeType {
        /**
         * Subscribe to remote data changes.
    
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        SUBSCRIBE_TYPE_REMOTE = 0,
        /**
         * Subscribe to cloud data changes.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC [since 10 - 11]
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 10
         */
        SUBSCRIBE_TYPE_CLOUD = 1,
        /**
         * Subscribe to detailed information about cloud data changes.
    
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC [since 10 - 11]
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 10
         */
        SUBSCRIBE_TYPE_CLOUD_DETAILS = 2,
        /**
         * Subscribe to detailed information about local data changes.
    
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 12
         */
        SUBSCRIBE_TYPE_LOCAL_DETAILS
    }
    /**
     * Enumerates data change types. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 10
     */
    enum ChangeType {
        /**
         * Data change.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC [since 10 - 11]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        DATA_CHANGE = 0,
        /**
         * Asset change.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC [since 10 - 11]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        ASSET_CHANGE = 1
    }
    /**
     * Defines a struct for the details about the device-cloud sync process.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 10
     */
    interface ChangeInfo {
        /**
         * Name of the table with data changes.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        table: string;
        /**
         * Type of the data changed, which can be data or asset.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        type: ChangeType;
        /**
         * Location where data is inserted. If the primary key of the table is of the string type, it is the value of the
         * primary key. Otherwise, it is the row number of the inserted data.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        inserted: Array<string> | Array<number>;
        /**
         * Location where data is updated. If the primary key of the table is of the string type, it is the value of the
         * primary key. Otherwise, it is the row number of the updated data.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        updated: Array<string> | Array<number>;
        /**
         * Location where data is deleted. If the primary key of the table is of the string type, it is the value of the
         * primary key. Otherwise, it is the row number of the deleted data.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        deleted: Array<string> | Array<number>;
    }
    /**
     * Enumerates the distributed table types. Use the enum name rather than the enum value. This item is a database-level
     * configuration. If a database contains multiple distributed tables, all tables must use the same distributed table
     * type; switching the table type or upgrade tables is not supported.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 23
     */
    enum DistributedTableType {
        /**
         * Multi-device collaboration table. Data on each device is stored in an independent distributed table in an
         * isolated manner instead of being written to the local table. The name of the distributed table is formed by
         * prepending the peer device's device ID to the original table name.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 23
         */
        DEVICE_COLLABORATION = 0,
        /**
         * Single version table. Data is directly written to the local table of the peer device through the distributed data
         * management framework.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 23
         */
        SINGLE_VERSION = 1
    }
    /**
     * Enumerates the distributed database table types. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 10
     */
    enum DistributedType {
        /**
         * Distributed database table synced between devices.
         *
         * SystemCapability.DistributedDataManager.RelationalStore.Core
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        DISTRIBUTED_DEVICE = 0,
        /**
         * Distributed database table synced between a device and the cloud.
         *
         * SystemCapability.DistributedDataManager.CloudSync.Client
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC [since 10 - 11]
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 10
         */
        DISTRIBUTED_CLOUD = 1
    }
    /**
     * Describes the asset conflict policy.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    enum AssetConflictPolicy {
        /**
         * Indicates the default conflict policy.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        CONFLICT_POLICY_DEFAULT = 0,
        /**
         * Indicates the time-first conflict policy.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        CONFLICT_POLICY_TIME_FIRST = 1,
        /**
         * Indicates the temporary path conflict policy.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        CONFLICT_POLICY_TEMP_PATH = 2
    }
    /**
     * Defines a struct for distributed configuration of a table.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 10
     */
    interface DistributedConfig {
        /**
         * Whether the table supports automatic device-cloud synchronization. If the value is **true**, the system can
         * automatically trigger device-cloud sync. If the value is **false**, the system cannot automatically trigger
         * device-cloud sync, and the [cloudSync]
         * {@link @ohos.data.relationalStore:relationalStore.RdbStore.cloudSync(mode: SyncMode, tables: string[])}
         * API needs to be called to trigger device-cloud sync.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        autoSync: boolean;
        /**
         * Whether to download assets synchronously or asynchronously when device-cloud sync is being performed for the
         * current RDB store. The value **true** means to use an asynchronous task to download assets after all data is
         * downloaded; **false** means to download assets synchronously.
         *
         * Default value: **false**.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 18
         */
        asyncDownloadAsset?: boolean;
        /**
         * Whether to enable device-cloud sync for this RDB store. The value **true** means to enable device-cloud sync;
         * **false** means the opposite. The default value is **true**.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 18
         */
        enableCloud?: boolean;
        /**
         * Distributed table type. **DEVICE_COLLABORATION** indicates the device collaboration table, and **SINGLE_VERSION**
         * indicates the single version table. For cross-device data sync, the default value is **DEVICE_COLLABORATION**.
         * For device-cloud data sync, the default value is **SINGLE_VERSION**, and **DEVICE_COLLABORATION** is not
         * supported.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 23
         */
        tableType?: DistributedTableType;
        /**
         * Specifies the asset conflict policy.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        assetConflictPolicy?: AssetConflictPolicy;
        /**
         * Specifies the asset temp path.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        assetTempPath?: string;
        /**
         * Specifies whether to download assets on demand.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        assetDownloadOnDemand?: boolean;
        /**
         * Specifies the auto synchronization switch.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        autoSyncSwitch?: boolean;
    }
    /**
     * Cloud sync configuration.
     *
     * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
     * @stagemodelonly
     * @since 26.0.0
     */
    interface CloudSyncConfig {
        /**
         * Indicates the database synchronization mode.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @stagemodelonly
         * @since 26.0.0
         */
        mode: SyncMode;
        /**
         * Indicates the table-level synchronization switch.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @stagemodelonly
         * @since 26.0.0
         */
        enablePredicate?: boolean;
        /**
         * Indicates the table-level synchronization predicate.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @stagemodelonly
         * @since 26.0.0
         */
        predicate?: RdbPredicates;
    }
    /**
     * Enumerates the resolutions used when a conflict occurs during data insertion or modification. Use the enum name
     * rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 10
     */
    enum ConflictResolution {
        /**
         * No operation is performed.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        ON_CONFLICT_NONE = 0,
        /**
         * Abort the SQL statement and roll back the current transaction.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        ON_CONFLICT_ROLLBACK = 1,
        /**
         * Abort the current SQL statement and revert any changes made by the current SQL statement. However, the changes
         * made by the previous SQL statement in the same transaction are retained and the transaction remains active.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        ON_CONFLICT_ABORT = 2,
        /**
         * Abort the current SQL statement. The **FAIL** resolution does not revert previous changes made by the failed SQL
         * statement or end the transaction.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        ON_CONFLICT_FAIL = 3,
        /**
         * Skip the rows that contain constraint violations and continue to process the subsequent rows of the SQL
         * statement.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        ON_CONFLICT_IGNORE = 4,
        /**
         * Delete pre-existing rows that cause the constraint violation before inserting or updating the current row, and
         * continue to execute the command normally.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        ON_CONFLICT_REPLACE = 5
    }
    /**
     * Enumerates the data sources. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
     * @since 11
     */
    enum Origin {
        /**
         * Indicates the data source is local.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 11
         */
        LOCAL = 0,
        /**
         * Indicates the data source is cloud.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 11
         */
        CLOUD = 1,
        /**
         * Indicates the data source is remote.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 11
         */
        REMOTE = 2
    }
    /**
     * Enumerates predicates used as query conditions. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
     * @crossplatform [since 20]
     * @since 11
     */
    enum Field {
        /**
         * Field name used for cursor-based search.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @crossplatform [since 20]
         * @since 11
         */
        CURSOR_FIELD = '#_cursor',
        /**
         * Field name used to specify the data source in cursor-based search.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @crossplatform [since 20]
         * @since 11
         */
        ORIGIN_FIELD = '#_origin',
        /**
         * Whether the dirty data (data deleted from the cloud) is cleared from the local device. It fills in the result set
         * returned upon the cursor-based search.
         *
         * The value **true** means the dirty data is cleared; the value **false** means the opposite.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @crossplatform [since 20]
         * @since 11
         */
        DELETED_FLAG_FIELD = '#_deleted_flag',
        /**
         * Data status in the cursor-based search result set. The value **0** indicates normal data status; **1** indicates
         * that data is retained after the account is logged out; **2** indicates that data is deleted from the cloud; **3**
         * indicates that data is deleted after the account is logged out.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @crossplatform [since 20]
         * @since 12
         */
        DATA_STATUS_FIELD = '#_data_status',
        /**
         * Party who shares the data. It fills in the result set returned when the owner of the shared data is searched.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @crossplatform [since 20]
         * @since 11
         */
        OWNER_FIELD = '#_cloud_owner',
        /**
         * Operation permission on the shared data. It fills in the result set returned when the permission on the shared
         * data is searched.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @crossplatform [since 20]
         * @since 11
         */
        PRIVILEGE_FIELD = '#_cloud_privilege',
        /**
         * Resource shared. It fills in the result set returned when the shared resource is searched.
         *
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @crossplatform [since 20]
         * @since 11
         */
        SHARING_RESOURCE_FIELD = '#_sharing_resource_field'
    }
    /**
     * Enumerates the RDB store rebuild types. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 12
     */
    enum RebuildType {
        /**
         * The RDB store is not rebuilt.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 12
         */
        NONE = 0,
        /**
         * The RDB store is rebuilt and creates an empty database. You need to create tables and restore data.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 12
         */
        REBUILT = 1,
        /**
         * The database is repaired and the undamaged data is restored. Currently, only the
         * [vector store]{@link @ohos.data.relationalStore:relationalStore.StoreConfig} supports this capability.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 12
         */
        REPAIRED = 2
    }
    /**
     * Enumerates the types of transaction objects that can be created. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 20]
     * @since 14
     */
    enum TransactionType {
        /**
         * Deferred transaction object. When a deferred transaction object is created, automatic commit is disabled and no
         * transaction will start. A read or write transaction starts only when the first read or write operation is
         * performed.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        DEFERRED = 0,
        /**
         * Immediate transaction object. When an immediate transaction object is created, a write transaction starts. If
         * there is any uncommitted write transaction, the transaction object cannot be created and error 14800024 is
         * returned.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        IMMEDIATE = 1,
        /**
         * Exclusive transaction object. In WAL mode, the exclusive transaction object is the same as the immediate
         * transaction object. In other log modes, this type of transaction can prevent the database from being read by
         * other connections during the transaction.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        EXCLUSIVE = 2
    }
    /**
     * Represents the configuration of a transaction object.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 20]
     * @since 14
     */
    interface TransactionOptions {
        /**
         * Transaction object type.
         *
         * Default value: **DEFERRED**.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 14
         */
        transactionType?: TransactionType;
    }
    /**
     * Enumerates the types of the column data. Use the enum name rather than the enum value.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 18
     */
    enum ColumnType {
        /**
         * The value in the column is null.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        NULL = 0,
        /**
         * 64-bit integer.
         *
         * The column can hold 8-bit (including Boolean values), 16-bit, 32-bit, and 64-bit integers. If the 64-bit integer
         * is greater than 2^53 or less than -2^53, use
         * [getString]{@link @ohos.data.relationalStore:relationalStore.ResultSet.getString} to convert the 64-bit integer
         * to a string.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        INTEGER = 1,
        /**
         * The value in the column is a floating point number.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        REAL = 2,
        /**
         * The value in the column is a string.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        TEXT = 3,
        /**
         * The value in the column is a Uint8Array.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        BLOB = 4,
        /**
         * The value in the column is an asset.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        ASSET = 5,
        /**
         * The value in the column is an array of assets.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        ASSETS = 6,
        /**
         * The value in the column is a Float32Array.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        FLOAT_VECTOR = 7,
        /**
         * The value in the column is a bigint.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        UNLIMITED_INT = 8
    }
    /**
     * Specifies the list of field names to return after returning-related APIs are called and the maximum number of
     * records allowed in the result set.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @stagemodelonly
     * @crossplatform
     * @since 23
     */
    interface ReturningConfig {
        /**
         * Fields returned in the result set. One to four fields are supported for input. Note: Field names containing
         * spaces ( ), commas (,), or asterisks (*) are not allowed.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        columns: Array<string>;
        /**
         * Maximum number of rows returned in the result set. The default value is **1024**, and the maximum value is
         * **32766**. Note: If the actual number of modified rows exceeds the value set for **maxReturningCount**, the
         * system will discard the excess data.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        maxReturningCount?: number;
    }
    /**
     * Records the number of affected data rows and the result set.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @stagemodelonly
     * @crossplatform
     * @since 23
     */
    interface Result {
        /**
         * Number of affected rows.
         *
         * @readonly
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        readonly changed: number;
        /**
         * Result set of the affected data. Defaults to 1,024 rows of data, with a maximum supported limit of 32,766 rows
         * supported; excess rows will be discarded.
         *
         * @readonly
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        readonly resultSet: LiteResultSet;
    }
    /**
     * Describes the status of device sync.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    enum SyncResultCode {
        /**
         * Indicates sync success.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        SUCCESS = 0,
        /**
         * Indicates sync fail, for detailed reasons, please refer to the message.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        FAIL = 1,
        /**
         * Indicates that the device is offline.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        OFFLINE = 2,
        /**
         * Indicates parameter is invalid.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        INVALID_ARGS = 3,
        /**
         * Indicates that a distributed table is not set.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        DISTRIBUTED_TABLE_NOT_SET = 4,
        /**
         * Indicates that the synchronization field of the peer device is inconsistent with that of the local device.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        TABLE_FIELD_MISMATCH = 5,
        /**
         * Indicates that the schema field of the peer device is inconsistent with that of the local device.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        DISTRIBUTED_SCHEMA_MISMATCH = 6,
        /**
         * Indicates that the database is busy.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        BUSY = 7,
        /**
         * Indicates that the database is corrupted.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        CORRUPTED = 8,
        /**
         * Indicates synchronization timeout.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        TIMEOUT = 9,
        /**
         * Indicates that the table structure changed during the synchronization process.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        SCHEMA_CHANGED = 10,
        /**
         * Indicates a violation of constraints when synchronizing data.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        CONSTRAINT_VIOLATION = 11
    }
    /**
     * Indicates synchronization result.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface SyncResult {
        /**
         * Indicates the synchronization deviceId.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly device: string;
        /**
         * Indicates the synchronization result code.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly code: SyncResultCode;
        /**
         * Indicates detailed information about the synchronization results.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly message: string;
    }
    /**
     * Defines the predicates for an RDB store. This class determines whether the conditional expression for the RDB store
     * is true or false. Multiple predicates statements can be concatenated by using **and()** by default.
     * **RdbPredicates** cannot be passed across threads using Sendable.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 10]
     * @since 9
     */
    class RdbPredicates {
        /**
         * Defines a constructor used to create an **RdbPredicates** object.
         *
         * @param { string } name - Database table name.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        constructor(name: string);
        /**
              * Creates an **RdbPredicates** object to specify the remote devices to connect on the network during distributed
              * database sync.
              *
              * > **NOTE**
              * >
              * > **devices** can be obtained by using [deviceManager.getAvailableDeviceListSync]
              * > {@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync}.
              * > When calling **sync()**, you need to call **inDevices** to specify the devices. If **inDevices** is not used,
              * > data will be synced to all devices on the network by default.
             *
             * @param { Array<string> } devices - IDs of the remote devices to connect.
             * @returns { RdbPredicates } **RdbPredicates** object created.
             * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
             *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
             * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
             * @since 9
             */
        inDevices(devices: Array<string>): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to specify all remote devices on the network to connect during distributed
         * database sync.
         *
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        inAllDevices(): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are equal to the given
         * value.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        equalTo(field: string, value: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are not equal to the
         * given value.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        notEqualTo(field: string, value: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to add a left parenthesis.
         *
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        beginWrap(): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to add a right parenthesis.
         *
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        endWrap(): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to add the OR condition.
         *
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        or(): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to add the AND condition.
         *
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        and(): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that contain the given
         * value.
         *
         * @param { string } field - Column name in the database table.
         * @param { string } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        contains(field: string, value: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that begin with the given
         * value.
         *
         * @param { string } field - Column name in the database table.
         * @param { string } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        beginsWith(field: string, value: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that end with the given
         * value.
         *
         * @param { string } field - Column name in the database table.
         * @param { string } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        endsWith(field: string, value: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are **null**.
         *
         * @param { string } field - Column name in the database table.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        isNull(field: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are not **null**.
         *
         * @param { string } field - Column name in the database table.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        isNotNull(field: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are similar to the
         * given value.
         *
         * @param { string } field - Column name in the database table.
         * @param { string } value - Condition for fuzzy match. Generally, this parameter is used together with a wildcard.
         *     A percent sign (%) represents any character of any length, and an underscore (_) represents a single
         *     character.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        like(field: string, value: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that match the given
         * string.
         *
         * @param { string } field - Column name in the database table.
         * @param { string } value - Value to match.<br>Wildcards are supported. An asterisk (*) indicates zero, one, or
         *     multiple digits or characters, and a question mark (?) indicates a single digit or character.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        glob(field: string, value: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records that are within the given range (including the min.
         * and max. values) in the specified column.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } low - Minimum value of the range to set.
         * @param { ValueType } high - Maximum value of the range to set.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        between(field: string, low: ValueType, high: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records that are out of the given range (excluding the min.
         * and max. values) in the specified column.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } low - Minimum value of the range to set.
         * @param { ValueType } high - Maximum value of the range to set.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records that are greater than the given value in the
         * specified column.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        greaterThan(field: string, value: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records that are less than the given value in the specified
         * column.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        lessThan(field: string, value: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records that are greater than or equal to the given value
         * in the specified column.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records that are less than or equal to the given value in
         * the specified column.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to sort the records in the specified column in ascending order.
         *
         * @param { string } field - Column name in the database table.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        orderByAsc(field: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to sort the records in the specified column in descending order.
         *
         * @param { string } field - Column name in the database table.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        orderByDesc(field: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to filter out duplicate records.
         *
         * @returns { RdbPredicates } **RdbPredicates** object that can filter out duplicate records.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        distinct(): RdbPredicates;
        /**
         * Creates a **RdbPredicates** object to limit the number of records.
         *
         * @param { number } value - Maximum number of data records. The value should be a positive integer. If a value less
         *     than or equal to **0** is specified, the number of records is not limited.
         * @returns { RdbPredicates } Predicates that specify the maximum number of records.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        limitAs(value: number): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to set the start position of the query result. This API must be used together
         * with **limitAs**. Otherwise, no result will be returned. To query all rows after the specified offset, pass in a
         * parameter less than or equal to **0** in **limitAs**.
         *
         * @param { number } rowOffset - Start position of the query result. By default, the start position is the beginning of
         *     the result set. If **rowOffset** is a negative number, the start position is the beginning of the result set.
         *     If **rowOffset** exceeds the end of the result set, the query result is empty.
         * @returns { RdbPredicates } Predicates that specify the start position of the returned result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        offsetAs(rowOffset: number): RdbPredicates;
        /**
         * Creates a **RdbPredicates** object to group the query results based on the specified columns.
         *
         * @param { Array<string> } fields - Names of columns to group.
         * @returns { RdbPredicates } Predicates that group rows with the same value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        groupBy(fields: Array<string>): RdbPredicates;
        /**
         * Creates a **RdbPredicates** object to specify the index column.
         *
         * @param { string } field - Name of the index column.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        indexedBy(field: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records that are in the given range in the specified
         * column.
         *
         * > **NOTE**
         * >
         * > The **value** array cannot be empty; otherwise, this condition becomes invalid. As a result, the operation (
         * > such as full query, update, or deletion) is performed on all data. Before calling this API, check whether the
         * > **value** array is empty to avoid misoperations.
         *
         * @param { string } field - Column name in the database table.
         * @param { Array<ValueType> } value - Array of **ValueType**s to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        in(field: string, value: Array<ValueType>): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records that are out of the given range in the specified
         * column.
         *
         * @param { string } field - Column name in the database table.
         * @param { Array<ValueType> } value - Array of **ValueType**s to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        notIn(field: string, value: Array<ValueType>): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records that do not contain the given value in the
         * specified column.
         *
         * @param { string } field - Column name in the database table.
         * @param { string } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 12
         */
        notContains(field: string, value: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are not similar to the
         * given value.
         *
         * @param { string } field - Column name in the database table.
         * @param { string } value - Condition for fuzzy match. Generally, this parameter is used together with a wildcard.
         *     A percent sign (%) represents any character of any length, and an underscore (_) represents a single
         *     character.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 12
         */
        notLike(field: string, value: string): RdbPredicates;
        /**
         * Filters for group data that meets the conditions.
         *
         * @param { string } conditions - Condition used to filter the data obtained using
         *     [groupBy]{@link relationalStore.RdbPredicates.groupBy}. This parameter cannot be empty and must be used with
         *     [groupBy]{@link relationalStore.RdbPredicates.groupBy}.
         * @param { Array<ValueType> } args - Parameters used in **conditions**, which replace the placeholder in the
         *     conditional statement. If this parameter is not specified, the default value is an empty array.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range;
         *     <br>2. Missing GROUP BY clause.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 20
         */
        having(conditions: string, args?: Array<ValueType>): RdbPredicates;
    }
    /**
     * Provides APIs to access the result set obtained by querying the RDB store. This result set is the collection of
     * results returned with the **query()** method called.
     *
     * The **ResultSet** instance is not refreshed in real time. After using the result set, if the data in the database
     * is changed (by being added, deleted, or modified), you need to query the result set again to obtain the latest
     * data.
     *
     * For the following APIs, you should use either [query]
     * {@link @ohos.data.relationalStore:relationalStore.RdbStore.query(predicates: RdbPredicates)},
     * [querySql]{@link @ohos.data.relationalStore:relationalStore.RdbStore.querySqlWithoutRowCount},
     * [remoteQuery]
     * {@link @ohos.data.relationalStore:relationalStore.RdbStore.remoteQuery(device: string, table: string)}
     * , or [queryLockedRow]{@link @ohos.data.relationalStore:relationalStore.RdbStore.queryLockedRow} to obtain the
     * **ResultSet** instance first, and then use this instance to call the corresponding method.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 10]
     * @since 9
     */
    interface ResultSet {
        /**
         * Names of all columns in the result set. If the result set contains duplicate column names, the return values are
         * not as expected. You are advised to use the [getColumnNames]{@link relationalStore.ResultSet.getColumnNames} API
         * to obtain the column names.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        columnNames: Array<string>;
        /**
         * Number of columns in the result set.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        columnCount: number;
        /**
         * Number of rows in the result set.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        rowCount: number;
        /**
         * Index of the current row in the result set.
         *
         * Default value: **-1**. The index position starts from **0**.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        rowIndex: number;
        /**
         * Whether the result set pointer is in the first row (the row index is **0**). The value **true** means the result
         * set pointer is in the first row.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        isAtFirstRow: boolean;
        /**
         * Whether the result set pointer is in the last row. The value **true** means the pointer is in the last row.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        isAtLastRow: boolean;
        /**
         * Whether the result set pointer is after the last row. The value **true** means the pointer is after the last row.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        isEnded: boolean;
        /**
         * Whether the result set pointer is moved. The value **true** means the pointer is moved.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        isStarted: boolean;
        /**
         * Whether the result set is closed. The value **true** means the result set is closed.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        isClosed: boolean;
        /**
         * Obtains the names of all columns in the result set.
         *
         * The column names are returned in a string array. The sequence of strings in the array is the same as that of
         * columns in the result set.
         *
         * @returns { Array<string> } Names of all columns in the result set obtained. Duplicate column names can be
         *     obtained.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getColumnNames(): Array<string>;
        /**
         * Obtains the column index based on the column name.
         *
         * @param { string } columnName - Column name.
         * @returns { number } Column index obtained. If the result set contains duplicate column names, the return value is
         *     not as expected.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800019 - The SQL must be a query statement. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        getColumnIndex(columnName: string): number;
        /**
         * Obtains the column name based on the column index.
         *
         * @param { number } columnIndex - Column index.
         * @returns { string } Column name obtained. If the result set contains duplicate column names, the return value is
         *     not as expected.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800019 - The SQL must be a query statement. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        getColumnName(columnIndex: number): string;
        /**
         * Obtains the column type based on the specified column index or column name. This API uses a promise to return the
         * result.
         *
         * @param { number | string } columnIdentifier - Index or name of column in a result set. The index must be a non-
         *     negative integer and cannot exceed the length of **columnNames**. The column name must be a name in
         *     **columnNames**.
         * @returns { Promise<ColumnType> } Promise used to return the column type obtained. If the result set contains
         *     duplicate column names, the return value is not as expected.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        getColumnType(columnIdentifier: number | string): Promise<ColumnType>;
        /**
         * Obtains the column type based on the specified column index or column name. This API returns the result
         * synchronously.
         *
         * @param { number | string } columnIdentifier - Index or name of column in a result set. The index must be a non-
         *     negative integer and cannot exceed the length of **columnNames**. The column name must be a name in
         *     **columnNames**.
         * @returns { ColumnType } Column type obtained. If the result set contains duplicate column names, the return value
         *     is not as expected.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        getColumnTypeSync(columnIdentifier: number | string): ColumnType;
        /**
         * Moves the result set pointer based on the offset specified.
         *
         * @param { number } offset - Offset relative to the position of the current result set pointer. A positive value means
         *     to move the pointer backward, and a negative value means to move the pointer forward.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800019 - The SQL must be a query statement. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        goTo(offset: number): boolean;
        /**
         * Moves to the specified row in the result set.
         *
         * @param { number } position - Destination position to move to.
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800019 - The SQL must be a query statement. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        goToRow(position: number): boolean;
        /**
         * Moves to the first row of the result set.
         *
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800019 - The SQL must be a query statement. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        goToFirstRow(): boolean;
        /**
         * Moves to the last row of the result set.
         *
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800019 - The SQL must be a query statement. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        goToLastRow(): boolean;
        /**
         * Moves to the next row in the result set.
         *
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800019 - The SQL must be a query statement. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        goToNextRow(): boolean;
        /**
         * Moves to the previous row in the result set.
         *
         * @returns { boolean } Returns **true** if the operation is successful; returns **false** otherwise.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800019 - The SQL must be a query statement. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        goToPreviousRow(): boolean;
        /**
         * Obtains the value from the specified column in the current row, and returns it in a byte array.
         *
         * If the type of the value in the specified column is INTEGER, DOUBLE, TEXT, or BLOB, the value will be converted
         * into a byte array and returned. If the column is null/empty, an empty byte array will be returned. If the value
         * is of any other type, 14800000 will be returned.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { Uint8Array } Value obtained.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        getBlob(columnIndex: number): Uint8Array;
        /**
         * Obtains the value from the specified column in the current row, and returns it in the form of a string.
         *
         * If the type of the value in the specified column is INTEGER, DOUBLE, TEXT, or BLOB, a string will be returned. If
         * the value type is INTEGER and the column is null/empty, an empty string **""** will be returned. If the value is
         * of any other type, 14800000 will be returned. If the value in the current column is of the DOUBLE type, the
         * precision may be lost. You are advised to use [getDouble]{@link relationalStore.ResultSet.getDouble} to obtain
         * the value.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { string } Value obtained.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        getString(columnIndex: number): string;
        /**
          * Obtains the value from the specified column in the current row, and returns a value of Long type.
          *
          * If the type of the value in the specified column is INTEGER, DOUBLE, TEXT, or BLOB, a value of Long type will be
          * returned. If the column is null/empty, **0** will be returned. If the value is of any other type, 14800000 will
          * be returned. If the data type in the specified column is INTEGER and the value is greater than
          * **Number.MAX_SAFE_INTEGER** or less than **Number.MIN_SAFE_INTEGER**, you are advised to use the
          * [getString]{@link relationalStore.ResultSet.getString} API to obtain the value without losing precision. If the
          * data type in the specified column is DOUBLE, you are advised to use the
          * [getDouble]{@link relationalStore.ResultSet.getDouble} API to obtain the value without losing precision.
          *
          * @param { number } columnIndex - Index of the target column, starting from 0.
          * @returns { number } Value obtained.
          *     <br>The value range supported by this API is **Number.MIN_SAFE_INTEGER** to **Number.MAX_SAFE_INTEGER**. If
          *     the value is out of this range, use [getDouble]{@link relationalStore.ResultSet.getDouble} for DOUBLE values
          *     and [getString]{@link relationalStore.ResultSet.getString} for INTEGER values.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        getLong(columnIndex: number): number;
        /**
         * Obtains the value from the specified column in the current row, and returns a value of Double type.
         *
         * If the type of the value in the specified column is INTEGER, DOUBLE, TEXT, or BLOB, a value of Double type will
         * be returned. If the column is null/empty, **0.0** will be returned. If the value is of any other type, 14800000
         * will be returned.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { number } Value obtained.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        getDouble(columnIndex: number): number;
        /**
         * Obtains the value from the specified column in the current row, and returns the value in the
         * [Asset]{@link @ohos.data.relationalStore:relationalStore.Asset} format. If the type of the value in the column is
         * **Asset**, the value of the Asset type is returned. If the value in the column is null, **null** is returned. If
         * the value in the column is of other types, 14800000 is returned.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { Asset } Value obtained.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        getAsset(columnIndex: number): Asset;
        /**
         * Obtains the value from the specified column in the current row, and returns the value in the
         * [Assets]{@link @ohos.data.relationalStore:relationalStore.Assets} format. If the type of the value in the column
         * is **Assets**, the value of the Assets type is returned. If the value in the column is null, **null** is
         * returned. If the value in the column is of other types, 14800000 is returned.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { Assets } Value obtained.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        getAssets(columnIndex: number): Assets;
        /**
         * Obtains the value from the specified column in the current row. If the value type is any of **ValueType**, the
         * value of the corresponding type will be returned. Otherwise, 14800000 will be returned. If the value type is
         * INTEGER and the value is greater than **Number.MAX_SAFE_INTEGER** or less than **Number.MIN_SAFE_INTEGER**, you
         * are advised to use the [getString]{@link relationalStore.ResultSet.getString} API to obtain the value without
         * losing precision.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { ValueType } Allowed data field types.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 12
         */
        getValue(columnIndex: number): ValueType;
        /**
         * Obtains this row.
         *
         * @returns { ValuesBucket } Value of the specified row. If the result set contains duplicate column names, the
         *     return value is not as expected. You are advised to use the
         *     [getCurrentRowData]{@link relationalStore.ResultSet.getCurrentRowData} API.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds. [since 12]
         * @throws { BusinessError } 14800013 - Column index is out of bounds. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 11
         */
        getRow(): ValuesBucket;
        /**
         * Obtains a specified amount of data from the result set. This API uses a promise to return the result. Do not call
         * this API concurrently with other APIs of [ResultSet]{@link @ohos.data.relationalStore:relationalStore}. Otherwise
         * , unexpected data may be obtained.
         *
         * @param { number } maxCount - Number of rows to obtain. The value is a positive integer. If the value is not a
         *     positive integer, error 401 will be thrown.
         * @param { number } [position] - Start position for obtaining data from the result set. The value is a non-negative
         *     integer. If this parameter is not specified, data is obtained from the current row of the result set (by
         *     default, it is the first row of the result set when data is obtained for the first time). If the value is not
         *     a non-negative integer, error code 401 will be thrown.
         * @returns { Promise<Array<ValuesBucket>> } Promise used to return **maxCount** rows of data obtained. If the
         *     number of remaining records is less than **maxCount**, the remaining records are returned. Returning an empty
         *     array indicates that the end of the result set is reached. If the result set contains duplicate column names,
         *     the return values are not as expected. You are advised to use the
         *     [getRowsData]{@link relationalStore.ResultSet.getRowsData} API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        getRows(maxCount: number, position?: number): Promise<Array<ValuesBucket>>;
        /**
         * Obtains the sendable data from the current row. The sendable data can be passed across threads.
         *
         * @returns { sendableRelationalStore.ValuesBucket } Sendable data obtained for cross-thread transfer.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 12
         */
        getSendableRow(): sendableRelationalStore.ValuesBucket;
        /**
         * Obtains the values of all columns in this row.
         *
         * @returns { RowData } Values of all columns in this row obtained. The values of columns with the same name can be
         *     obtained.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getCurrentRowData(): RowData;
        /**
         * Obtains data of a specified number of rows from the specified position. This API uses a promise to return the
         * result. Do not call this API concurrently with other APIs of
         * [ResultSet]{@link @ohos.data.relationalStore:relationalStore}. Otherwise, unexpected data may be obtained.
         *
         * @param { number } maxCount - Number of rows to obtain. The value is a positive integer. If the value is not a
         *     positive integer, error 14800001 will be thrown.
         * @param { number } [position] - Start position for obtaining data from the result set. The value is a non-negative
         *     integer. If this parameter is not specified, data is obtained from the current row of the result set (by
         *     default, it is the first row of the result set when data is obtained for the first time). If the value is not
         *     a non-negative integer, error code 14800001 will be thrown.
         * @returns { Promise<RowsData> } Promise used to return **maxCount** rows of data obtained. If the number of
         *     remaining records is less than **maxCount**, the remaining records are returned. Returning an empty array
         *     indicates that the end of the result set is reached. The values of columns with the same name can be
         *     obtained.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getRowsData(maxCount: number, position?: number): Promise<RowsData>;
        /**
         * Checks whether the value in the specified column is null.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { boolean } Returns **true** if the value is null; returns **false** otherwise.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        isColumnNull(columnIndex: number): boolean;
        /**
         * Closes this **resultSet** to release memory. If the **resultSet** is not closed, FD or memory leaks may occur.
         *
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        close(): void;
    }
    /**
     * Defines APIs to access the result set obtained by querying the RDB store. This result set is the collection of
     * results returned with the **query()** method called.
     *
     * The **LiteResultSet** instance is not refreshed in real time. After using the result set, if the data in the
     * database is changed (by being added, deleted, or modified), you need to query the result set again to obtain the
     * latest data.
     *
     * In the following API examples, you need to obtain an **LiteResultSet** instance by using a query method, such as
     * [queryWithoutRowCount]{@link @ohos.data.relationalStore:relationalStore.RdbStore.queryWithoutRowCount} or
     * [querySqlWithoutRowCount]{@link @ohos.data.relationalStore:relationalStore.RdbStore.querySqlWithoutRowCount}, and
     * then call the corresponding method through this instance.
     *
     * > **NOTE**
     * >
     * > - The initial APIs of this class are supported since API version 23.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @stagemodelonly
     * @crossplatform
     * @since 23
     */
    class LiteResultSet {
        /**
         * Obtains the names of all columns in the result set.
         *
         * The column names are returned in a string array. The sequence of strings in the array is the same as that of
         * columns in the result set.
         *
         * @returns { Array<string> } Names of all columns in the result set obtained. Duplicate column names can be
         *     obtained.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getColumnNames(): Array<string>;
        /**
         * Obtains the column index based on the column name.
         *
         * @param { string } columnName - Column name. If the result set contains duplicate column names, the return value
         *     is not as expected.
         * @returns { number } Column index obtained.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getColumnIndex(columnName: string): number;
        /**
         * Obtains the column name based on the column index.
         *
         * @param { number } columnIndex - Index of the column in the result set, starting from 0.
         * @returns { string } Column name obtained. If the result set contains duplicate column names, the return value is
         *     not as expected.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getColumnName(columnIndex: number): string;
        /**
         * Obtains the column type based on the specified column index or column name. This API uses a promise to return the
         * result.
         *
         * @param { number | string } columnIdentifier - Index or name of the column in the result set. The index starts from 0
         *     .
         * @returns { Promise<ColumnType> } Promise used to return the column type obtained. If the result set contains
         *     duplicate column names, the return value is not as expected.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getColumnType(columnIdentifier: number | string): Promise<ColumnType>;
        /**
         * Obtains the column type based on the specified column index or column name.
         *
         * @param { number | string } columnIdentifier - Index or name of the column in the result set. The index starts from 0
         *     .
         * @returns { ColumnType } Column type obtained. If the result set contains duplicate column names, the return value
         *     is not as expected.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getColumnTypeSync(columnIdentifier: number | string): ColumnType;
        /**
         * Moves the result set to the next row.
         *
         * @returns { boolean } Returns **true** if the result set is successfully moved to the next row; returns **false**
         *     otherwise.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        goToNextRow(): boolean;
        /**
         * Obtains the value in the specified column in the current row as a byte array.
         *
         * If the data type of the current column is INTEGER, DOUBLE, TEXT, or BLOB, the data is converted to a byte array
         * and returned. If the content of the column is null/empty, an empty byte array is returned.
         *
         * If the data type of the current column is ASSET, ASSETS, FLOATVECTOR, or BIGINT, 14800041 is returned.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { Uint8Array } Value obtained.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800041 - Type conversion failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getBlob(columnIndex: number): Uint8Array;
        /**
         * Obtains the value in the specified column in the current row as a string.
         *
         * If the data type of the current column is INTEGER, DOUBLE, TEXT, or BLOB type, the value is returned as a string.
         * If the content of the column is null/empty, an empty string **""** is returned.
         *
         * If the data type of the current column is DOUBLE, precision loss may occur. You are advised to use
         * [getDouble]{@link relationalStore.LiteResultSet.getDouble} API to obtain the value.
         *
         * If the data type of the current column is ASSET, ASSETS, FLOATVECTOR, or BIGINT, 14800041 is returned.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { string } Value obtained.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800041 - Type conversion failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getString(columnIndex: number): string;
        /**
              * Obtains the value from the specified column in the current row, and returns a value of Long type.
              *
              * If the data type of the current column is INTEGER, DOUBLE, TEXT, or BLOB, a value of Long type is returned. If
              * the column is null, **0** is returned. If the data type is INTEGER and the value is greater than
              * **Number.MAX_SAFE_INTEGER** or less than **Number.MIN_SAFE_INTEGER**, you are advised to use the
              * [getString]{@link relationalStore.LiteResultSet.getString} API to obtain the value without losing precision. If
              * the data type in the specified column is DOUBLE, you are advised to use the
              * [getDouble]{@link relationalStore.LiteResultSet.getDouble} API to obtain the value without precision loss.
              *
              * If the data type of the current column is ASSET, ASSETS, FLOATVECTOR, or BIGINT, 14800041 is returned.
              *
              * @param { number } columnIndex - Index of the target column, starting from 0.
              * @returns { number } Value obtained.
              *     <br>The value range supported by this API is **Number.MIN_SAFE_INTEGER** to **Number.MAX_SAFE_INTEGER**. If
              *     the value is out of this range, use [getDouble]{@link relationalStore.LiteResultSet.getDouble} for DOUBLE
              *     values and [getString]{@link relationalStore.LiteResultSet.getString} for INTEGER values.
             * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
             * @throws { BusinessError } 14800013 - Column index is out of bounds.
             * @throws { BusinessError } 14800014 - The target instance is already closed.
             * @throws { BusinessError } 14800041 - Type conversion failed.
             * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
             * @stagemodelonly
             * @crossplatform
             * @since 23
             */
        getLong(columnIndex: number): number;
        /**
         * Obtains the value in the specified column in the current row as a Double.
         *
         * If the data type of the current column is INTEGER, DOUBLE, or TEXT, the value is converted to the Double type and
         * returned. Non-numeric TEXT and BLOB types return **0.0**. If the content of the column is null/empty, **0.0** is
         * returned.
         *
         * If the data type of the current column is ASSET, ASSETS, FLOATVECTOR, or BIGINT, 14800041 is returned.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { number } Value obtained.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800041 - Type conversion failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getDouble(columnIndex: number): number;
        /**
         * Obtains the value in the specified column in the current row as an
         * [Asset]{@link @ohos.data.relationalStore:relationalStore.Asset}.
         *
         * If the data type of the current column is Asset, the value is returned as an Asset. If the value in the current
         * column is **null**, **null** is returned. If the data type of the current column is not Asset, 14800041 is
         * returned.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { Asset } Value obtained.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800041 - Type conversion failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getAsset(columnIndex: number): Asset;
        /**
         * Obtains the value in the specified column in the current row as
         * [Assets]{@link @ohos.data.relationalStore:relationalStore.Assets}.
         *
         * If the data type of the current column is Assets, the value is returned as Assets. If the value in the current
         * column is **null**, **null** is returned. If the data type of the current column is not Assets, 14800041 is
         * returned.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { Assets } Value obtained.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800041 - Type conversion failed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getAssets(columnIndex: number): Assets;
        /**
         * Obtains the value of the specified column in the current row.
         *
         * If the value type is INTEGER and the value is greater than **Number.MAX_SAFE_INTEGER** or less than
         * **Number.MIN_SAFE_INTEGER**, you are advised to use the
         * [getString]{@link relationalStore.LiteResultSet.getString} API to obtain the value without precision loss.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { ValueType } Type of the data field returned.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getValue(columnIndex: number): ValueType;
        /**
         * Obtains data for the current row.
         *
         * @returns { ValuesBucket } Value of the specified row. If the result set contains duplicate column names, the
         *     return value is not as expected. You are advised to use the
         *     [getCurrentRowData]{@link relationalStore.LiteResultSet.getCurrentRowData} API.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getRow(): ValuesBucket;
        /**
         * Obtains a specified amount of data from the result set. This API uses a promise to return the result. Do not call
         * this API concurrently with other APIs of [LiteResultSet]{@link @ohos.data.relationalStore:relationalStore}.
         * Otherwise, unexpected data may be obtained.
         *
         * @param { number } maxCount - Number of rows to obtain. The value is a positive integer.
         * @param { number } [position] - Start position for obtaining data from the result set. The value is a non-negative
         *     integer. If this parameter is not specified, data is obtained from the current row of the result set (by
         *     default, it is the first row of the result set when data is obtained for the first time).
         * @returns { Promise<Array<ValuesBucket>> } Promise used to return **maxCount** rows of data obtained. If the
         *     number of remaining records is less than **maxCount**, the remaining records are returned. Returning an empty
         *     array indicates that the end of the result set is reached. If the result set contains duplicate column names,
         *     the return values are not as expected. You are advised to use the
         *     [getRowsData]{@link relationalStore.LiteResultSet.getRowsData} API.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getRows(maxCount: number, position?: number): Promise<Array<ValuesBucket>>;
        /**
         * Obtains the values of all columns in this row.
         *
         * @returns { RowData } Values of all columns in this row obtained. The values of columns with the same name can be
         *     obtained.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getCurrentRowData(): RowData;
        /**
         * Obtains data of a specified number of rows from the specified position. This API uses a promise to return the
         * result. Do not call this API concurrently with other APIs of
         * [ResultSet]{@link @ohos.data.relationalStore:relationalStore}. Otherwise, unexpected data may be obtained.
         *
         * @param { number } maxCount - Number of rows to obtain. The value is a positive integer. If the value is not a
         *     positive integer, error 14800001 will be thrown.
         * @param { number } [position] - Start position for obtaining data from the result set. The value is a non-negative
         *     integer. If this parameter is not specified, data is obtained from the current row of the result set (by
         *     default, it is the first row of the result set when data is obtained for the first time). If the value is not
         *     a non-negative integer, error code 14800001 will be thrown.
         * @returns { Promise<RowsData> } Promise used to return **maxCount** rows of data obtained. If the number of
         *     remaining records is less than **maxCount**, the remaining records are returned. Returning an empty array
         *     indicates that the end of the result set is reached. The values of columns with the same name can be
         *     obtained.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        getRowsData(maxCount: number, position?: number): Promise<RowsData>;
        /**
         * Checks whether the value in the specified column is null.
         *
         * @param { number } columnIndex - Index of the target column, starting from 0.
         * @returns { boolean } Returns **true** if the value is null; returns **false** otherwise.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800012 - ResultSet is empty or pointer index is out of bounds.
         * @throws { BusinessError } 14800013 - Column index is out of bounds.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800019 - The SQL must be a query statement.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        isColumnNull(columnIndex: number): boolean;
        /**
         * Closes this **resultSet** to release memory. If the **resultSet** is not closed, FD or memory leaks may occur.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        close(): void;
    }
    /**
     * Provides APIs for managing data in an RDB store.
     *
     * Before using the following APIs, you should obtain an **RdbStore** instance by calling the
     * [getRdbStore]{@link @ohos.data.relationalStore:relationalStore.getRdbStore(context: Context, config: StoreConfig)}
     * method and then call the corresponding method through the instance.
     *
     * In addition, use
     * [execute]{@link @ohos.data.relationalStore:relationalStore.RdbStore.execute(sql: string, args?: Array<ValueType>)}
     * to initialize the database table structure and related data first, ensuring that the prerequisites for related API
     * calls are met.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 10]
     * @since 9
     */
    interface RdbStore {
        /**
         * Set RdbStore version. The version number must be an integer greater than 0.
         * Obtains the RdbStore version.
         *
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported. [since 12]
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        version: number;
        /**
         * Set whether the database is rebuilt.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 12
         */
        rebuilt: RebuildType;
        /**
         * Inserts a row of data into the target table.
         *
         * @param { string } table - Indicates the target table.
         * @param { ValuesBucket } values - Indicates the row of data {@link ValuesBucket} to be inserted into the table.
         * @param { AsyncCallback<number> } callback - The row ID if the operation is successful. returns -1 otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @since 9
         */
        insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>): void;
        /**
         * Inserts a row of data into the target table.
         *
         * @param { string } table - Indicates the target table.
         * @param { ValuesBucket } values - Indicates the row of data {@link ValuesBucket} to be inserted into the table.
         * @param { ConflictResolution } conflict - Indicates the {@link ConflictResolution} to insert data into the table.
         * @param { AsyncCallback<number> } callback - The row ID if the operation is successful. returns -1 otherwise.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @crossplatform
         * @since 10
         */
        insert(table: string, values: ValuesBucket, conflict: ConflictResolution, callback: AsyncCallback<number>): void;
        /**
         * Inserts a row of data into the target table.
         *
         * @param { string } table - Indicates the target table.
         * @param { ValuesBucket } values - Indicates the row of data {@link ValuesBucket} to be inserted into the table.
         * @returns { Promise<number> } The row ID if the operation is successful. return -1 otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        insert(table: string, values: ValuesBucket): Promise<number>;
        /**
         * Inserts a row of data into the target table.
         *
         * @param { string } table - Indicates the target table.
         * @param { ValuesBucket } values - Indicates the row of data {@link ValuesBucket} to be inserted into the table.
         * @param { ConflictResolution } conflict - Indicates the {@link ConflictResolution} to insert data into the table.
         * @returns { Promise<number> } The row ID if the operation is successful. return -1 otherwise.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        insert(table: string, values: ValuesBucket, conflict: ConflictResolution): Promise<number>;
        /**
         * Inserts a row of data into the target table with sync interface.
         *
         * @param { string } table - Indicates the target table.
         * @param { ValuesBucket } values - Indicates the row of data {@link ValuesBucket} to be inserted into the table.
         * @param { ConflictResolution } conflict - Indicates the {@link ConflictResolution} to insert data into the table.
         * @returns { number } The row ID if the operation is successful. return -1 otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 12
         */
        insertSync(table: string, values: ValuesBucket, conflict?: ConflictResolution): number;
        /**
         * Inserts a row of data into the target table with sync interface.
         *
         * @param { string } table - Indicates the target table.
         * @param { sendableRelationalStore.ValuesBucket } values - Indicates the row of data
         *     {@link sendableRelationalStore.ValuesBucket} to be inserted into the table.
         * @param { ConflictResolution } conflict - Indicates the {@link ConflictResolution} to insert data into the table.
         * @returns { number } The row ID if the operation is successful. return -1 otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 12
         */
        insertSync(table: string, values: sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution): number;
        /**
         * Inserts a batch of data into the target table.
         *
         * The data insertion fails if the API returns an error, or if it returns -1 without throwing an error.
         *
         * Write 32766 parameters per batch using the {@link ConflictResolution.ON_CONFLICT_REPLACE} policy.
         * The product of the number of inserted data records and the size of the union of all fields in the inserted data
         * equals the number of parameters. This API returns immediately upon a failure during the process.
         *
         * @param { string } table - Indicates the target table.
         * @param { Array<ValuesBucket> } values - Indicates the rows of data {@link ValuesBucket}
         *     to be inserted into the table.
         * @param { AsyncCallback<number> } callback -
         *     The number of values that were inserted if the operation is successful. returns -1 otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @since 9
         */
        batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void;
        /**
         * Inserts a batch of data into the target table.
         *
         * The data insertion fails if the API returns an error, or if it returns -1 without throwing an error.
         *
         * Write 32766 parameters per batch using the {@link ConflictResolution.ON_CONFLICT_REPLACE} policy.
         * The product of the number of inserted data records and the size of the union of all fields in the inserted data
         * equals the number of parameters. This API returns immediately upon a failure during the process.
         *
         * @param { string } table - Indicates the target table.
         * @param { Array<ValuesBucket> } values -
         *     Indicates the rows of data {@link ValuesBucket} to be inserted into the table.
         * @returns { Promise<number> } The number of values that were inserted if the operation is successful.
         *     Returns -1 otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>;
        /**
         * Inserts a batch of data into the target table.
         *
         * The data insertion fails if the API returns an error, or if it returns -1 without throwing an error.
         *
         * Write 32766 parameters per batch using the {@link ConflictResolution.ON_CONFLICT_REPLACE} policy.
         * The product of the number of inserted data records and the size of the union of all fields in the inserted data
         * equals the number of parameters. This API returns immediately upon a failure during the process.
         *
         * @param { string } table - Indicates the target table.
         * @param { Array<ValuesBucket> } values -
         *     Indicates the rows of data {@link ValuesBucket} to be inserted into the table.
         * @returns { number } The number of values that were inserted if the operation is successful. returns -1 otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 12
         */
        batchInsertSync(table: string, values: Array<ValuesBucket>): number;
        /**
         * Inserts a batch of data into the target table.
         *
         * A maximum of 32766 parameters can be inserted at a time. If the number of parameters exceeds the upper limit,
         * the error code 14800000 is returned. The product of the number of inserted data records and the size of the union
         * of all fields in the inserted data equals the number of parameters. For example, if the size of the union is 10,
         * a maximum of 3276 data records can be inserted (3276 * 10 = 32760). Ensure that your application complies with
         * this constraint when calling this API to avoid errors caused by excessive parameters.
         *
         * @param { string } table - Indicates the target table.
         * @param { Array<ValuesBucket> } values -
         *     Indicates the rows of data {@link ValuesBucket} to be inserted into the table.
         * @param { ConflictResolution } conflict - Indicates the {@link ConflictResolution} to insert data into the table.
         * @returns { Promise<number> } The number of values that were inserted if the operation is successful.
         *     Returns -1 otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        batchInsertWithConflictResolution(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): Promise<number>;
        /**
         * Inserts a batch of data into the target table.
         *
         * A maximum of 32766 parameters can be inserted at a time. If the number of parameters exceeds the upper limit,
         * the error code 14800000 is returned. The product of the number of inserted data records and the size of the union
         * of all fields in the inserted data equals the number of parameters. For example, if the size of the union is 10,
         * a maximum of 3276 data records can be inserted (3276 * 10 = 32760). Ensure that your application complies with
         * this constraint when calling this API to avoid errors caused by excessive parameters.
         *
         * @param { string } table - Indicates the target table.
         * @param { Array<ValuesBucket> } values -
         *     Indicates the rows of data {@link ValuesBucket} to be inserted into the table.
         * @param { ConflictResolution } conflict - Indicates the {@link ConflictResolution} to insert data into the table.
         * @returns { number } The number of values that were inserted if the operation is successful. returns -1 otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @crossplatform
         * @since 18
         */
        batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): number;
        /**
         * Inserts a batch of data into the target table and return a resultSet of changed fields.
         *
         * A maximum of 32766 parameters can be inserted at a time. If the number of parameters exceeds the upper limit,
         * the error code 14800001 is returned. The product of the number of inserted data records and the size of the union
         * of all fields in the inserted data equals the number of parameters. For example, if the size of the union is 10,
         * a maximum of 3276 data records can be inserted (3276 * 10 = 32760). Ensure that your application complies with
         * this constraint when calling this API to avoid errors caused by excessive parameters.
         *
         * @param { string } table - Indicates the target table.
         * @param { Array<ValuesBucket> } values - Indicates the rows of data {@link ValuesBucket} to be inserted into the
         *     table.
         * @param { ReturningConfig } config - Indicate the information that needs to be returned.
         * @param { ConflictResolution } [conflict] - Indicates the {@link ConflictResolution} to insert data into the
         *     table.
         *     The default conflict resolution policy is {@link ConflictResolution.ON_CONFLICT_NONE}.
         * @returns { Promise<Result> } The {@link Result} result of the inserted field includes the number of modified
         *     rows and the result set of changed data.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>;
        /**
         * Inserts a batch of data into the target table and return a resultSet of changed fields.
         *
         * A maximum of 32766 parameters can be inserted at a time. If the number of parameters exceeds the upper limit,
         * the error code 14800001 is returned. The product of the number of inserted data records and the size of the union
         * of all fields in the inserted data equals the number of parameters. For example, if the size of the union is 10,
         * a maximum of 3276 data records can be inserted (3276 * 10 = 32760). Ensure that your application complies with
         * this constraint when calling this API to avoid errors caused by excessive parameters.
         *
         * @param { string } table - Indicates the target table.
         * @param { Array<ValuesBucket> } values - Indicates the rows of data {@link ValuesBucket} to be inserted into the
         *     table.
         * @param { ReturningConfig } config - Indicate the information that needs to be returned.
         * @param { ConflictResolution } [conflict] - Indicates the {@link ConflictResolution} to insert data into the
         *     table.
         *     The default conflict resolution policy is {@link ConflictResolution.ON_CONFLICT_NONE}.
         * @returns { Result } The {@link Result} result of the inserted field includes the number of modified
         *     rows and the result set of changed data.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Result;
        /**
         * Updates data in the database based on a specified instance object of RdbPredicates.
         *
         * @param { ValuesBucket } values - Indicates the row of data to be updated in the database.
         *     The key-value pairs are associated with column names of the database table.
         * @param { RdbPredicates } predicates -
         *     Indicates the specified update condition by the instance object of  {@link RdbPredicates}.
         * @param { AsyncCallback<number> } callback - The number of affected rows.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @since 9
         */
        update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>): void;
        /**
         * Updates data in the database based on a specified instance object of RdbPredicates.
         *
         * @param { ValuesBucket } values - Indicates the row of data to be updated in the database.
         *     The key-value pairs are associated with column names of the database table.
         * @param { RdbPredicates } predicates -
         *     Indicates the specified update condition by the instance object of  {@link RdbPredicates}.
         * @param { ConflictResolution } conflict - Indicates the {@link ConflictResolution} to insert data into the table.
         * @param { AsyncCallback<number> } callback - The number of affected rows.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @crossplatform
         * @since 10
         */
        update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution, callback: AsyncCallback<number>): void;
        /**
         * Updates data in the database based on a specified instance object of RdbPredicates.
         *
         * @param { ValuesBucket } values - Indicates the row of data to be updated in the database.
         *     The key-value pairs are associated with column names of the database table.
         * @param { RdbPredicates } predicates -
         *     Indicates the specified update condition by the instance object of  {@link RdbPredicates}.
         * @returns { Promise<number> } The number of affected rows.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        update(values: ValuesBucket, predicates: RdbPredicates): Promise<number>;
        /**
         * Updates data in the database based on a specified instance object of RdbPredicates.
         *
         * @param { ValuesBucket } values - Indicates the row of data to be updated in the database.
         *     The key-value pairs are associated with column names of the database table.
         * @param { RdbPredicates } predicates -
         *     Indicates the specified update condition by the instance object of  {@link RdbPredicates}.
         * @param { ConflictResolution } conflict - Indicates the {@link ConflictResolution} to insert data into the table.
         * @returns { Promise<number> } The number of affected rows.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution): Promise<number>;
        /**
         * Updates data in the database based on a specified instance object of RdbPredicates with sync interface.
         *
         * @param { ValuesBucket } values - Indicates the row of data to be updated in the database.
         *     The key-value pairs are associated with column names of the database table.
         * @param { RdbPredicates } predicates -
         *     Indicates the specified update condition by the instance object of  {@link RdbPredicates}.
         * @param { ConflictResolution } conflict - Indicates the {@link ConflictResolution} to insert data into the table.
         * @returns { number } The number of affected rows.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 12
         */
        updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): number;
        /**
         * Updates data in the database based on a specified instance object of RdbPredicates and return a
         * resultSet of changed fields.
         *
         * @param { ValuesBucket } values - Indicates the row of data to be updated in the database.
         *     The key-value pairs are associated with column names of the database table.
         * @param { RdbPredicates } predicates -
         *     Indicates the specified update condition by the instance object of  {@link RdbPredicates}.
         * @param { ReturningConfig } config - Indicate the information that needs to be returned.
         * @param { ConflictResolution } [conflict] -
         *     Indicates the {@link ConflictResolution} to update data into the table.
         * @returns { Promise<Result> } The {@link Result} result of the updated field includes the number of modified
         *     rows and the result set of changed data.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of    valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>;
        /**
         * Updates data in the database based on a specified instance object of RdbPredicates and return a
         * resultSet of changed fields.
         *
         * @param { ValuesBucket } values - Indicates the row of data to be updated in the database.
         *     The key-value pairs are associated with column names of the database table.
         * @param { RdbPredicates } predicates -
         *     Indicates the specified update condition by the instance object of  {@link RdbPredicates}.
         * @param { ReturningConfig } config - Indicate the information that needs to be returned.
         * @param { ConflictResolution } [conflict] -
         *     Indicates the {@link ConflictResolution} to update data into the table.
         * @returns { Result } The {@link Result} result of the updated field includes the number of modified
         *     rows and the result set of changed data.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of    valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Result;
        /**
         * Deletes data from the database based on a specified instance object of RdbPredicates.
         *
         * @param { RdbPredicates } predicates -
         *     The specified delete condition by the instance object of {@link RdbPredicates}.
         * @param { AsyncCallback<number> } callback - The number of affected rows.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @since 9
         */
        delete(predicates: RdbPredicates, callback: AsyncCallback<number>): void;
        /**
         * Deletes data from the database based on a specified instance object of RdbPredicates.
         *
         * @param { RdbPredicates } predicates -
         *     The specified delete condition by the instance object of {@link RdbPredicates}.
         * @returns { Promise<number> } return the number of affected rows.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        delete(predicates: RdbPredicates): Promise<number>;
        /**
         * Deletes data from the database based on a specified instance object of RdbPredicates with sync interface.
         *
         * @param { RdbPredicates } predicates -
         *     The specified delete condition by the instance object of {@link RdbPredicates}.
         * @returns { number } return the number of rows deleted.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 12
         */
        deleteSync(predicates: RdbPredicates): number;
        /**
         * Deletes data from the database based on a specified instance object of RdbPredicates and return a
         * resultSet of changed fields.
         *
         * @param { RdbPredicates } predicates -
         *     The specified delete condition by the instance object of {@link RdbPredicates}.
         * @param { ReturningConfig } config - Indicate the information that needs to be returned.
         * @returns { Promise<Result> } The {@link Result} result of the deleted field includes the number of modified
         *     rows and the result set of changed data.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of    valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>;
        /**
         * Deletes data from the database based on a specified instance object of RdbPredicates and return a
         * resultSet of changed fields.
         *
         * @param { RdbPredicates } predicates -
         *     The specified delete condition by the instance object of {@link RdbPredicates}.
         * @param { ReturningConfig } config - Indicate the information that needs to be returned.
         * @returns { Result } The {@link Result} result of the deleted field includes the number of modified
         *     rows and the result set of changed data.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result;
        /**
         * Queries data in the database based on specified conditions.
         *
         * @param { RdbPredicates } predicates -
         *     The specified query condition by the instance object of {@link RdbPredicates}.
         * @param { AsyncCallback<ResultSet> } callback - The {@link ResultSet} object if the operation is successful.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        query(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>): void;
        /**
         * Queries data in the database based on specified conditions.
         *
         * @param { RdbPredicates } predicates -
         *     The specified query condition by the instance object of {@link RdbPredicates}.
         * @param { Array<string> } columns -
         *     The columns to query. If the value is empty array, the query applies to all columns.
         * @param { AsyncCallback<ResultSet> } callback - The {@link ResultSet} object if the operation is successful.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void;
        /**
         * Queries data in the database based on specified conditions.
         *
         * @param { RdbPredicates } predicates -
         *     The specified query condition by the instance object of {@link RdbPredicates}.
         * @param { Array<string> } columns - The columns to query. If the value is null, the query applies to all columns.
         * @returns { Promise<ResultSet> } The {@link ResultSet} object if the operation is successful.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>;
        /**
         * Queries data in the database based on specified conditions with sync function.
         *
         * @param { RdbPredicates } predicates -
         *     The specified query condition by the instance object of {@link RdbPredicates}.
         * @param { Array<string> } columns -
         *     The columns to query. If the value is empty array, the query applies to all columns.
         * @returns { ResultSet } The {@link ResultSet} object if the operation is successful.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 12
         */
        querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet;
        /**
         * Queries data in the database based on SQL statement.
         *
         * @param { string } sql - Indicates the SQL statement to execute.
         * @param { AsyncCallback<ResultSet> } callback - The {@link ResultSet} object if the operation is successful.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        querySql(sql: string, callback: AsyncCallback<ResultSet>): void;
        /**
         * Queries data in the database based on SQL statement.
         *
         * @param { string } sql - Indicates the SQL statement to execute.
         * @param { Array<ValueType> } bindArgs -
         *     Indicates the {@link ValueType} values of the parameters in the SQL statement. The values are strings.
         * @param { AsyncCallback<ResultSet> } callback - The {@link ResultSet} object if the operation is successful.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>): void;
        /**
         * Queries data in the database based on SQL statement.
         *
         * @param { string } sql - Indicates the SQL statement to execute.
         * @param { Array<ValueType> } bindArgs -
         *     Indicates the {@link ValueType} values of the parameters in the SQL statement. The values are strings.
         * @returns { Promise<ResultSet> } The {@link ResultSet} object if the operation is successful.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        querySql(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>;
        /**
         * Queries data in the database based on SQL statement with sync interface.
         *
         * @param { string } sql - Indicates the SQL statement to execute.
         * @param { Array<ValueType> } bindArgs -
         *     Indicates the {@link ValueType} values of the parameters in the SQL statement. The values are strings.
         * @returns { ResultSet } The {@link ResultSet} object if the operation is successful.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 12
         */
        querySqlSync(sql: string, bindArgs?: Array<ValueType>): ResultSet;
        /**
         * Queries data without rowCount in the database based on specified conditions.
         *
         * @param { RdbPredicates } predicates -
         *     The specified query condition by the instance object of {@link RdbPredicates}.
         * @param { Array<string> } [columns] -
         *     The columns to query. If the value is null, the query applies to all columns.
         * @returns { Promise<LiteResultSet> } The {@link LiteResultSet} object if the operation is successful.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>;
        /**
         * Queries data without rowCount in the database based on specified conditions with sync function.
         *
         * @param { RdbPredicates } predicates -
         *     The specified query condition by the instance object of {@link RdbPredicates}.
         * @param { Array<string> } [columns] -
         *     The columns to query. If the value is null, the query applies to all columns.
         * @returns { LiteResultSet } The {@link LiteResultSet} object if the operation is successful.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet;
        /**
         * Queries data from the RDB store based on specified conditions without calculating the row count. This API uses a
         * promise to return the result and delivers better performance than the
         * [querySql]{@link relationalStore.Transaction.querySql} API. The number of relational operators between
         * expressions and operators in the SQL statement cannot exceed 1,000.
         *
         * @param { string } sql - SQL statement to run.
         * @param { Array<ValueType> } [bindArgs] - Arguments in the SQL statement. The value corresponds to the
         *     placeholders in the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter
         *     blank.
         * @returns { Promise<LiteResultSet> } Promise used to return the result. If the operation is successful, a
         *     **LiteResultSet** object will be returned.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>;
        /**
         * Queries data from the RDB store based on specified SQL statements without calculating the row count. The number
         * of relational operators between expressions and operators in the SQL statement cannot exceed 1,000. If complex
         * logic and a large number of loops are involved in the operations on the **LiteResultSet** obtained by
         * **querySqlWithoutRowCountSync**, the freeze problem may occur. You are advised to perform this operation in the
         * [taskpool]{@link @ohos.taskpool:taskpool} thread.
         *
         * @param { string } sql - SQL statement to run.
         * @param { Array<ValueType> } [bindArgs] - Arguments in the SQL statement. The value corresponds to the
         *     placeholders in the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter
         *     blank. The default value is null.
         * @returns { LiteResultSet } If the operation is successful, a **LiteResultSet** object will be returned.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet;
        /**
         * Query data in the database step‑by‑step based on SQL statements.
         *
         * @param { string } sql - Indicates the SQL statement to execute.
         *     <br>Value range: (0, +∞)
         *     <br>A valid SQL statement must be used. Otherwise, an error code may be thrown when ResultSet is used.
         * @param { Array<ValueType> } [bindArgs] - Indicates the {@link ValueType} values of the parameters in
         *     the SQL statement.
         *     <br>Default value:The default value is an empty array.
         *     <br>The value must be the same as the number of placeholders in the SQL statement.
         * @returns { Promise<ResultSet> } The {@link ResultSet} object if the operation is successful.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 26.0.0
         */
        queryByStep(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>;
        /**
         * Queries data in the database step‑by‑step based on specified conditions.
         *
         * @param { RdbPredicates } predicates - The specified query condition by the instance object
         *     of {@link RdbPredicates}.
         * @param { Array<string> } [columns] - The columns to query.
         *     If the value is null, the query applies to all columns.
         *     <br>Default value: empty array by default.
         *     <br>If an empty array is transferred, all columns are queried.
         * @returns { Promise<ResultSet> } The {@link ResultSet} object if the operation is successful.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 26.0.0
         */
        queryByStep(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>;
        /**
         * Obtains the modify time of rows corresponding to the primary keys.
         *
         * @param { string } table - Indicates the name of the table to check.
         * @param { string } columnName - Indicates the name of the column to check.
         * @param { PRIKeyType[] } primaryKeys - Indicates the primary keys of the rows to check.
         * @returns { Promise<ModifyTime> } -
         *     The promise returned by the function. ModifyTime indicates the modify time of current row.
         *     If this table does not support cloud, the {@link ModifyTime} will be empty.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Need 3 - 4  parameter(s)! 2. The RdbStore must be not nullptr.
         *     3. The tablesNames must be not empty string. 4. The columnName must be not empty string.
         *     5. The PRIKey must be number or string.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType[]): Promise<ModifyTime>;
        /**
         * Obtains the modify time of rows corresponding to the primary keys.
         *
         * @param { string } table - Indicates the name of the table to check.
         * @param { string } columnName - Indicates the name of the column to check.
         * @param { PRIKeyType[] } primaryKeys - Indicates the primary keys of the rows to check.
         * @param { AsyncCallback<ModifyTime> } callback -
         *     The callback of getModifyTime. ModifyTime indicates the modify time of current row.
         *     If this table does not support cloud, the {@link ModifyTime} will be empty.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Need 3 - 4  parameter(s)! 2. The RdbStore must be not nullptr.
         *     3. The tablesNames must be not empty string. 4. The columnName must be not empty string.
         *     5. The PRIKey must be number or string.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType[], callback: AsyncCallback<ModifyTime>): void;
        /**
         * Cleans the dirty data, which is the data deleted in the cloud.
         *
         * Data with a cursor smaller than the specified cursor will be cleaned up.
         *
         * @param { string } table - Indicates the name of the table to check.
         * @param { number } cursor - Indicates the position of the data to be cleaned up.
         * @param { AsyncCallback<void> } callback - Indicates the callback invoked to return the result.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Need 1 - 3  parameter(s)! 2. The RdbStore must be not nullptr.
         *     3. The tablesNames must be not empty string. 4. The cursor must be valid cursor.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @FaAndStageModel
         * @since 11
         */
        cleanDirtyData(table: string, cursor: number, callback: AsyncCallback<void>): void;
        /**
         * Cleans all dirty data deleted in the cloud.
         *
         * @param { string } table - Indicates the name of the table to check.
         * @param { AsyncCallback<void> } callback - The callback of clean.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Need 1 - 3  parameter(s). 2. The RdbStore must be not nullptr.
         *     3. The tablesNames must be not empty string.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 11
         */
        cleanDirtyData(table: string, callback: AsyncCallback<void>): void;
        /**
         * Cleans dirty data deleted in the cloud.
         *
         * If a cursor is specified, data with a cursor smaller than the specified cursor will be cleaned up.
         * otherwise clean all.
         *
         * @param { string } table - Indicates the name of the table to check.
         * @param { number } [cursor] - Indicates the cursor.
         * @returns { Promise<void> } -The promise returned by the function.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Need 1 - 3  parameter(s)! 2. The RdbStore must be not nullptr.
         *     3. The tablesNames must be not empty string. 4. The cursor must be valid cursor.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 11
         */
        cleanDirtyData(table: string, cursor?: number): Promise<void>;
        /**
         * Executes a SQL statement that contains specified parameters but returns no value.
         *
         * @param { string } sql - Indicates the SQL statement to execute.
         * @param { AsyncCallback<void> } callback - The callback of executeSql.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 801 - Capability not supported the sql(attach,begin,commit,rollback etc.). [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 10
         */
        executeSql(sql: string, callback: AsyncCallback<void>): void;
        /**
         * Executes a SQL statement that contains specified parameters but returns no value.
         *
         * @param { string } sql - Indicates the SQL statement to execute.
         * @param { Array<ValueType> } bindArgs -
         *     Indicates the {@link ValueType} values of the parameters in the SQL statement. The values are strings.
         * @param { AsyncCallback<void> } callback - The callback of executeSql.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @throws { BusinessError } 801 - Capability not supported the sql(attach,begin,commit,rollback etc.). [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>): void;
        /**
         * Executes a SQL statement that contains specified parameters but returns no value.
         *
         * @param { string } sql - Indicates the SQL statement to execute.
         * @param { Array<ValueType> } bindArgs -
         *     Indicates the {@link ValueType} values of the parameters in the SQL statement. The values are strings.
         * @returns { Promise<void> } The promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @throws { BusinessError } 801 - Capability not supported the sql(attach,begin,commit,rollback etc.). [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        executeSql(sql: string, bindArgs?: Array<ValueType>): Promise<void>;
        /**
         * Executes a SQL statement that contains specified parameters and returns a value of ValueType.
         *
         * @param { string } sql - Indicates the SQL statement to execute.
         * @param { Array<ValueType> } args - Indicates the {@link ValueType} values of the parameters in the SQL statement.
         *     The values are strings.
         * @returns { Promise<ValueType> } The promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported the sql(attach,begin,commit,rollback etc.).
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 12
         */
        execute(sql: string, args?: Array<ValueType>): Promise<ValueType>;
        /**
         * Executes a SQL statement that contains specified parameters and returns a value of ValueType.
         *
         * @param { string } sql - Indicates the SQL statement to execute.
         * @param { number } txId - Indicates the transaction ID which is obtained by beginTrans or 0.
         * @param { Array<ValueType> } args - Indicates the {@link ValueType} values of the parameters in the SQL statement.
         *     The values are strings.
         * @returns { Promise<ValueType> } The promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported the sql(attach,begin,commit,rollback etc.).
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @since 12
         */
        execute(sql: string, txId: number, args?: Array<ValueType>): Promise<ValueType>;
        /**
         * Executes a SQL statement that contains specified parameters and returns a value of ValueType with sync interface.
         *
         * @param { string } sql - Indicates the SQL statement to execute.
         * @param { Array<ValueType> } args - Indicates the {@link ValueType} values of the parameters in the SQL statement.
         *     The values are strings.
         * @returns { ValueType } The promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 12
         */
        executeSync(sql: string, args?: Array<ValueType>): ValueType;
        /**
         * BeginTransaction before execute your sql.
         *
         * @throws { BusinessError } 401 - Parameter error.  Possible causes: The RdbStore verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit. [since 10]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @since 9
         */
        beginTransaction(): void;
        /**
         * Begins a transaction before executing the SQL statement.
         *
         * @returns { Promise<number> } Returns the transaction ID.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: The RdbStore verification failed.
         * @throws { BusinessError } 801 - Capability not supported the sql(attach,begin,commit,rollback etc.).
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @since 12
         */
        beginTrans(): Promise<number>;
        /**
         * Commit the the sql you have executed.
         *
         * @throws { BusinessError } 401 - Parameter error.  Possible causes: The RdbStore verification failed.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @since 9
         */
        commit(): void;
        /**
         * Commits the SQL statement executed.
         *
         * @param { number } txId - Indicates the transaction ID which is obtained by beginTrans.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @since 12
         */
        commit(txId: number): Promise<void>;
        /**
         * Roll back the sql you have already executed.
         *
         * @throws { BusinessError } 401 - Parameter error.  Possible causes: The RdbStore verification failed.
         * @throws { BusinessError } 14800000 - Inner error. [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @since 9
         */
        rollBack(): void;
        /**
         * Rolls back the SQL statement executed.
         *
         * @param { number } txId - Indicates the transaction ID which is obtained by beginTrans.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @since 12
         */
        rollback(txId: number): Promise<void>;
        /**
         * Backs up a database in a specified name.
         *
         * @param { string } destName - Indicates the name that saves the database backup.
         * @param { AsyncCallback<void> } callback - The callback of backup.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800010 - Failed to open or delete the database by an invalid database path.
         *     [since 12]
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        backup(destName: string, callback: AsyncCallback<void>): void;
        /**
         * Backs up a database in a specified name.
         *
         * @param { string } destName - Indicates the name that saves the database backup.
         * @returns { Promise<void> } The promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        backup(destName: string): Promise<void>;
        /**
         * Restores a database from a specified database file.
         *
         * @param { string } srcName - Indicates the name that saves the database file.
         * @param { AsyncCallback<void> } callback - The callback of restore.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        restore(srcName: string, callback: AsyncCallback<void>): void;
        /**
         * Restores a database from a specified database file.
         *
         * @param { string } srcName - Indicates the name that saves the database file.
         * @returns { Promise<void> } The promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted. [since 12]
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @throws { BusinessError } 14800015 - The database does not respond. [since 12]
         * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked. [since 12]
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked. [since 12]
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory. [since 12]
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
         * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit. [since 12]
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation. [since 12]
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch. [since 12]
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 10]
         * @since 9
         */
        restore(srcName: string): Promise<void>;
        /**
         * Set table to be distributed table.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { Array<string> } tables - Indicates the table names you want to set.
         * @param { AsyncCallback<void> } callback - The callback of setDistributedTables.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void;
        /**
         * Set table to be distributed table.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { Array<string> } tables - Indicates the table names you want to set.
         * @returns { Promise<void> } The promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        setDistributedTables(tables: Array<string>): Promise<void>;
        /**
         * Set table to be distributed table.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { Array<string> } tables - Indicates the table names you want to set.
         * @param { DistributedType } type - Indicates the distributed type {@link DistributedType}.
         *     ohos.permission.DISTRIBUTED_DATASYNC is required only when type is DISTRIBUTED_DEVICE.
         * @param { AsyncCallback<void> } callback - The callback of setDistributedTables.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800051 - The type of the distributed table does not match.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        setDistributedTables(tables: Array<string>, type: DistributedType, callback: AsyncCallback<void>): void;
        /**
         * Set table to be distributed table.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { Array<string> } tables - Indicates the table names you want to set.
         * @param { DistributedType } type - Indicates the distributed type {@link DistributedType}.
         *     ohos.permission.DISTRIBUTED_DATASYNC is required only when type is DISTRIBUTED_DEVICE.
         * @param { DistributedConfig } config -
         *     Indicates the distributed config of the tables. For details, see {@link DistributedConfig}.
         * @param { AsyncCallback<void> } callback - The callback of setDistributedTables.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800051 - The type of the distributed table does not match.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        setDistributedTables(tables: Array<string>, type: DistributedType, config: DistributedConfig, callback: AsyncCallback<void>): void;
        /**
         * Set table to be a distributed table.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { Array<string> } tables - Indicates the table names you want to set.
         * @param { DistributedType } type - Indicates the distributed type {@link DistributedType}.
         *     ohos.permission.DISTRIBUTED_DATASYNC is required only when type is DISTRIBUTED_DEVICE.
         * @param { DistributedConfig } config -
         *     Indicates the distributed config of the tables. For details, see {@link DistributedConfig}.
         * @returns { Promise<void> } The promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800051 - The type of the distributed table does not match.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        setDistributedTables(tables: Array<string>, type?: DistributedType, config?: DistributedConfig): Promise<void>;
        /**
         * Obtain distributed table name of specified remote device according to local table name.
         * When query remote device database, distributed table name is needed.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } device - Indicates the remote device.
         * @param { string } table - {string}: the distributed table name.
         * @param { AsyncCallback<string> } callback
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void;
        /**
         * Obtain distributed table name of specified remote device according to local table name.
         * When query remote device database, distributed table name is needed.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } device - Indicates the remote device.
         * @param { string } table
         * @returns { Promise<string> } {string}: the distributed table name.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        obtainDistributedTableName(device: string, table: string): Promise<string>;
        /**
         * Sync data between devices.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { SyncMode } mode - Indicates the database synchronization mode.
         * @param { RdbPredicates } predicates -
         *     The specified sync condition by the instance object of {@link RdbPredicates}.
         * @param { AsyncCallback<Array<[ string, number ]>> } callback -
         *     {Array<[string, int]>}: devices sync status array,
         *     {string}: device id,
         *     {int}: device sync status.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @since 9
         */
        sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[
            string,
            number
        ]>>): void;
        /**
         * Sync data between devices.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { SyncMode } mode - Indicates the database synchronization mode.
         * @param { RdbPredicates } predicates -
         *     The specified sync condition by the instance object of {@link RdbPredicates}.
         * @returns { Promise<Array<[ string, number ]>> }
         *     {Array<[string, int]>}: devices sync status array, {string}: device id, {int}: device sync status.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[
            string,
            number
        ]>>;
        /**
         * Sync data between devices.
         *
         * 1. The difference between the sync interface and the syncEx interface is that they can return more error codes,
         * but their functionality is similar.
         * 2. Before invoking synchronization, call setdistributedTable to set the distributed table.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { SyncMode } mode - Indicates the database synchronization mode.
         *     <br>Only SYNC_MODE_PUSH and SYNC_MODE_PULL are supported.
         * @param { RdbPredicates } predicates - The specified sync condition by the instance object
         *     of {@link RdbPredicates}.
         * @returns { Promise<Array<SyncResult>> } devices sync result array, see {@link SyncResult} for details.
         * @throws { BusinessError } 201 - the application does not have permission to call this function.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        syncEx(mode: SyncMode, predicates: RdbPredicates): Promise<Array<SyncResult>>;
        /**
         * Sync data to cloud.
         *
         * @param { SyncMode } mode - indicates the database synchronization mode.
         * @param { Callback<ProgressDetails> } progress -
         *     Callback used to return the {@link ProgressDetails} result.
         * @param { AsyncCallback<void> } callback - The callback of cloudSync.
         * @throws { BusinessError } 401 - Parameter error.
         *     Possible causes: 1. Need 2 - 4  parameter(s). 2. The RdbStore must be not nullptr.
         *     3. The mode must be a SyncMode of cloud. 4. The progress must be a callback type.
         *     5. The callback must be a function.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 10
         */
        cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void;
        /**
         * Sync data to cloud.
         *
         * @param { SyncMode } mode - indicates the database synchronization mode.
         * @param { Callback<ProgressDetails> } progress -
         *     Callback used to return the {@link ProgressDetails} result.
         * @returns { Promise<void> } : The promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error.
         *     Possible causes: 1. Need 2 - 4  parameter(s). 2. The RdbStore must be not nullptr.
         *     3. The mode must be a SyncMode of cloud. 4. The progress must be a callback type.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 10
         */
        cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>;
        /**
         * Sync data to cloud.
         *
         * @param { SyncMode } mode - indicates the database synchronization mode.
         * @param { string[] } tables - indicates the database synchronization mode.
         * @param { Callback<ProgressDetails> } progress -
         *     Callback used to return the {@link ProgressDetails} result.
         * @param { AsyncCallback<void> } callback - The callback of cloudSync.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br> 1. Mandatory parameters are left unspecified.
         *     <br> 2. Incorrect parameter types.
         *     <br> 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 10
         */
        cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void;
        /**
         * Sync data to cloud.
         *
         * @param { SyncMode } mode - indicates the database synchronization mode.
         * @param { string[] } tables - indicates the database synchronization mode.
         * @param { Callback<ProgressDetails> } progress -
         *     Callback used to return the {@link ProgressDetails} result.
         * @returns { Promise<void> } : The promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error.
         *     Possible causes: 1. Need 2 - 4  parameter(s). 2. The RdbStore must be not nullptr.
         *     3. The mode must be a SyncMode of cloud. 4. The tablesNames must be not empty.
         *     5. The progress must be a callback type.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @since 10
         */
        cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>;
        /**
         * Synchronizes data to the cloud. This API uses a promise to return the result.
         *
         * @param { CloudSyncConfig } config - indicates the cloud synchronization config.
         * @param { Callback<ProgressDetails> } progress - Callback used to return the sync progress.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @stagemodelonly
         * @since 26.0.0
         */
        cloudSyncEx(config: CloudSyncConfig, progress: Callback<ProgressDetails>): Promise<void>;
        /**
         * Stops synchronizing data with the cloud.
         *
         * @returns { Promise<void> } : The promise returned by the function.
         * @throws { BusinessError } 801 - Capability not supported
         *     because the device does not support the cloud synchronization capability.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.CloudSync.Client
         * @stagemodelonly
         * @since 26.0.0
         */
        stopCloudSync(): Promise<void>;
        /**
         * Queries remote data in the database based on specified conditions before Synchronizing Data.
         *
         * @param { string } device - Indicates specified remote device.
         * @param { string } table - Indicates the target table.
         * @param { RdbPredicates } predicates -
         *     The specified remote remote query condition by the instance object of {@link RdbPredicates}.
         * @param { Array<string> } columns - The columns to remote query.
         *     If the value is empty array, the remote query applies to all columns.
         * @param { AsyncCallback<ResultSet> } callback - The {@link ResultSet} object if the operation is successful.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void;
        /**
         * Queries remote data in the database based on specified conditions before Synchronizing Data.
         *
         * @param { string } device - Indicates specified remote device.
         * @param { string } table - Indicates the target table.
         * @param { RdbPredicates } predicates -
         *     The specified remote remote query condition by the instance object of {@link RdbPredicates}.
         * @param { Array<string> } columns - The columns to remote query.
         *     If the value is empty array, the remote query applies to all columns.
         * @returns { Promise<ResultSet> } The {@link ResultSet} object if the operation is successful.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string>): Promise<ResultSet>;
        /**
         * Subscribes to data changes of this RDB store.
         * The registered callback will be called when data in a distributed RDB store changes.
         * the callback will be invoked.
         *
         * @param { 'dataChange' } event - Indicates the event must be string 'dataChange'.
         * @param { SubscribeType } type - Indicates the subscription type, which is defined in {@link SubscribeType}.
         *     If its value is SUBSCRIBE_TYPE_REMOTE, ohos.permission.DISTRIBUTED_DATASYNC is required.
         * @param { Callback<Array<string>> } observer -
         *     {Array<string>}: the observer of data change events in the distributed database.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void;
        /**
         * Subscribes to data changes of this RDB store.
         * The registered callback will be called when data in a distributed RDB store changes.
         *
         * @param { 'dataChange' } event - Indicates the event must be string 'dataChange'.
         * @param { SubscribeType } type - Indicates the subscription type, which is defined in {@link SubscribeType}.
         *     If its value is SUBSCRIBE_TYPE_REMOTE, ohos.permission.DISTRIBUTED_DATASYNC is required.
         * @param { Callback<Array<string>> | Callback<Array<ChangeInfo>> } observer
         *     {Array<string>}: the observer of data change events in the distributed database.
         *     {Array<ChangeInfo>}: The change info of data change events in the distributed database.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 202 - Permission verification failed,
         *     application which is not a system application uses system API.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>> | Callback<Array<ChangeInfo>>): void;
        /**
         * Registers an observer for the database.
         *
         * @param { string } event - Event type, which must match the event type in {@link emit}.
         * @param { boolean } interProcess -
         *     Indicates whether it is an interprocess subscription or an in-process subscription.
         * @param { Callback<void> } observer - The observer of data change events in the database.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800050 - Failed to obtain the subscription service.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        on(event: string, interProcess: boolean, observer: Callback<void>): void;
        /**
         * Register an automatic synchronization callback to the database.
         *
         * @param { 'autoSyncProgress' } event - Indicates the event must be string 'autoSyncProgress'.
         * @param { Callback<ProgressDetails> } progress -
         *     Callback used to return the {@link ProgressDetails} result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed;
         *     <br>4. The event must be a not empty string; 5. The progress must be function.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 11
         */
        on(event: 'autoSyncProgress', progress: Callback<ProgressDetails>): void;
        /**
         * Subscribes to the SQL statistics.
         *
         * @param { 'statistics' } event - Indicates the event type, which must be 'statistics'.
         * @param { Callback<SqlExecutionInfo> } observer -
         *     Indicates the callback used to return the SQL execution statistics {@link SqlExeInfo} in the database.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 12
         */
        on(event: 'statistics', observer: Callback<SqlExecutionInfo>): void;
        /**
         * Subscribes to the SQL performance statistics.
         *
         * @param { 'perfStat' } event - Event type, which must be 'perfStat'.
         * @param { Callback<SqlExecutionInfo> } observer - Callback used to return the SQL execution statistics
         *     {@link SqlExecutionInfo}.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 20
         */
        on(event: 'perfStat', observer: Callback<SqlExecutionInfo>): void;
        /**
         * Subscribes to the SQL execution error logs.
         *
         * @param { 'sqliteErrorOccurred' } event - Event type, which must be 'sqliteErrorOccurred'.
         * @param { Callback<ExceptionMessage> } observer - Callback used to return the SQL execution errorlog
         *     {@link ExceptionMessage }.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 20
         */
        on(event: 'sqliteErrorOccurred', observer: Callback<ExceptionMessage>): void;
        /**
         * Remove specified observer of specified type from the database.
         *
         * @param { 'dataChange' } event - Indicates the event must be string 'dataChange'.
         * @param { SubscribeType } type - Indicates the subscription type, which is defined in {@link SubscribeType}.
         *     If its value is SUBSCRIBE_TYPE_REMOTE, ohos.permission.DISTRIBUTED_DATASYNC is required.
         * @param { Callback<Array<string>> } observer - {Array<string>}: the data change observer already registered.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 9
         */
        off(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void;
        /**
         * Remove specified observer of specified type from the database.
         *
         * @param { 'dataChange' } event - indicates the event must be string 'dataChange'.
         * @param { SubscribeType } type - indicates the subscription type, which is defined in {@link SubscribeType}.
         *     If its value is SUBSCRIBE_TYPE_REMOTE, ohos.permission.DISTRIBUTED_DATASYNC is required.
         * @param { Callback<Array<string>> | Callback<Array<ChangeInfo>> } observer -
         *     {Array<string>}: the data change observer already registered.
         *     {Array<ChangeInfo>}: the change info already registered.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 202 - Permission verification failed,
         *     application which is not a system application uses system API.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        off(event: 'dataChange', type: SubscribeType, observer?: Callback<Array<string>> | Callback<Array<ChangeInfo>>): void;
        /**
         * Remove specified observer of specified type from the database.
         *
         * @param { string } event - Indicates the subscription event.
         * @param { boolean } interProcess -
         *     Indicates whether it is an interprocess subscription or an in-process subscription.
         * @param { Callback<void> } observer - The data change observer already registered. [since 10 - 11]
         * @param { Callback<void> } [observer] - The data change observer already registered. [since 12]
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800050 - Failed to obtain the subscription service.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        off(event: string, interProcess: boolean, observer?: Callback<void>): void;
        /**
         * Unregister the database auto synchronization callback.
         *
         * @param { 'autoSyncProgress' } event - indicates the event must be string 'autoSyncProgress'.
         * @param { Callback<ProgressDetails> } progress -
         *     Callback used to return the {@link ProgressDetails} result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Need 1 - 3  parameter(s)! 2. The RdbStore must be valid.
         *     3. The event must be a not empty string. 4. The progress must be function.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 11
         */
        off(event: 'autoSyncProgress', progress?: Callback<ProgressDetails>): void;
        /**
         * Unsubscribes from the SQL statistics.
         *
         * @param { 'statistics' } event - Indicates the event type, which must be 'statistics'.
         * @param { Callback<SqlExecutionInfo> } observer - Indicates the callback to unregister.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 12
         */
        off(event: 'statistics', observer?: Callback<SqlExecutionInfo>): void;
        /**
         * Unsubscribes from the SQL performance statistics.
         *
         * @param { 'perfStat' } event - Event type, which must be 'perfStat'.
         * @param { Callback<SqlExecutionInfo> } observer - Callback to unregister.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 20
         */
        off(event: 'perfStat', observer?: Callback<SqlExecutionInfo>): void;
        /**
         * Unsubscribes from the SQL execution error logs.
         *
         * @param { 'sqliteErrorOccurred' } event - Indicates the event type, which must be 'sqliteErrorOccurred'.
         * @param { Callback<ExceptionMessage> } observer - Callback to unregister.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 20
         */
        off(event: 'sqliteErrorOccurred', observer?: Callback<ExceptionMessage>): void;
        /**
         * Notifies the registered observers of a change to the data resource specified by Uri.
         *
         * @param { string } event - Indicates the subscription event.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800050 - Failed to obtain the subscription service.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800014 - The target instance is already closed. [since 12]
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 10
         */
        emit(event: string): void;
        /**
         * Close the RdbStore and all resultSets.
         *
         * @returns { Promise<void> } The promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: The RdbStore verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform [since 20]
         * @since 12
         */
        close(): Promise<void>;
        /**
         * Attaches a database file to the currently linked database.
         *
         * @param { string } fullPath - Indicates the path of the database file to attach.
         * @param { string } attachName - Indicates the alias of the database.
         * @param { number } [waitTime] - Indicates the maximum time allowed for attaching the database file, in seconds.
         * @returns { Promise<number> } Promise used to return the number of attached databases.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800010 - Failed to open or delete the database by an invalid database path.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800016 - The database alias already exists.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @since 12
         */
        attach(fullPath: string, attachName: string, waitTime?: number): Promise<number>;
        /**
         * Attaches a database file to the currently linked database.
         *
         * @param { Context } context - Indicates the context of an application or ability.
         * @param { StoreConfig } config -
         *     Indicates the {@link StoreConfig} configuration of the database related to this RDB store.
         * @param { string } attachName - Indicates the alias of the database.
         * @param { number } [waitTime] - Indicates the maximum time allowed for attaching the database file, in seconds.
         * @returns { Promise<number> } Promise used to return the number of attached databases.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800010 - Failed to open or delete the database by an invalid database path.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800016 - The database alias already exists.
         * @throws { BusinessError } 14801001 - The operation is supported in the stage model only.
         * @throws { BusinessError } 14801002 - Invalid data group ID.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @since 12
         */
        attach(context: Context, config: StoreConfig, attachName: string, waitTime?: number): Promise<number>;
        /**
         * Detaches a database from this database.
         *
         * @param { string } attachName - Indicates the alias of the database.
         * @param { number } [waitTime] - Indicates the maximum time allowed for detaching the database, in seconds.
         * @returns { Promise<number> } Return the current number of attached databases.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @FaAndStageModel
         * @since 12
         */
        detach(attachName: string, waitTime?: number): Promise<number>;
        /**
         * Locks data from the database based on a specified instance object of RdbPredicates.
         *
         * @param { RdbPredicates } predicates -
         *     The specified lock condition by the instance object of {@link RdbPredicates}.
         * @returns { Promise<void> } The promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800018 - No data meets the condition.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 12
         */
        lockRow(predicates: RdbPredicates): Promise<void>;
        /**
         * Unlocks data from the database based on a specified instance object of RdbPredicates.
         *
         * @param { RdbPredicates } predicates -
         *     The specified Unlock condition by the instance object of {@link RdbPredicates}.
         * @returns { Promise<void> } The promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800018 - No data meets the condition.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 12
         */
        unlockRow(predicates: RdbPredicates): Promise<void>;
        /**
         * Queries locked data in the database based on specified conditions.
         *
         * @param { RdbPredicates } predicates -
         *     The specified query condition by the instance object of {@link RdbPredicates}.
         * @param { Array<string> } [columns] - The columns to query. If the value is null, the query applies to all
         *     columns.
         * @returns { Promise<ResultSet> } The {@link ResultSet} object if the operation is successful.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 12
         */
        queryLockedRow(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>;
        /**
         * create a transaction instance and begin.
         *
         * @param { TransactionOptions } options - The option for creating transactions.
         * @returns { Promise<Transaction> } The {@link Transaction} object if the operation is successful.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database is busy.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        createTransaction(options?: TransactionOptions): Promise<Transaction>;
        /**
         * Changes the key used to encrypt the database.
         *
         * @param { CryptoParam } cryptoParam - Specifies the crypto parameters used to rekey.
         *     If valid cryptoParam passed, the cryptoParam is used to rekey.
         *     If cryptoParam is null or not passed, the default cryptoParam is used.
         * @returns { Promise<void> } - Promise that returns no value.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800015 - The database does not respond.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 20
         */
        rekey(cryptoParam?: CryptoParam): Promise<void>;
        /**
         * Support for collations in different languages.
         *
         * @param { string } locale - Language related to the locale.
         *     for example, zh. The value complies with the ISO 639 standard.
         * @returns { Promise<void> } The promise returned by the function.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 20
         */
        setLocale(locale: string): Promise<void>;
        /**
         * Change the encryption parameters of the database.
         *
         * @param { CryptoParam } cryptoParam - Crypto parameters.
         * @returns { Promise<void> } - Promise that returns no value.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 22
         */
        rekeyEx(cryptoParam: CryptoParam): Promise<void>;
    }
    /**
     * Provides APIs for managing databases in transaction mode. A transaction object is created by using
     * [createTransaction]{@link @ohos.data.relationalStore:relationalStore.RdbStore.createTransaction}. Operations on
     * different transaction objects are isolated. For details about the transaction types, see
     * [TransactionType]{@link @ohos.data.relationalStore:relationalStore.TransactionType}.
     *
     * Currently, an RDB store supports only one write transaction at a time. If the current
     * [RdbStore]{@link @ohos.data.relationalStore:relationalStore} has a write transaction that is not released, creating
     * an **IMMEDIATE** or **EXCLUSIVE** transaction object will return error 14800024. If a **DEFERRED** transaction
     * object is created, error 14800024 may be returned when it is used to invoke a write operation for the first time.
     * After a write transaction is created using **IMMEDIATE** or **EXCLUSIVE**, or a **DEFERRED** transaction is
     * upgraded to a write transaction, write operations in the
     * [RdbStore]{@link @ohos.data.relationalStore:relationalStore} will also return error 14800024.
     *
     * When the number of concurrent transactions is large and the write transaction duration is long, the frequency of
     * returning error 14800024 may increase. You can reduce the occurrence of error 14800024 by shortening the
     * transaction duration or by handling the error 14800024 through retries.
     *
     * Before using the following APIs, you should obtain a **Transaction** instance by calling the
     * [createTransaction]{@link @ohos.data.relationalStore:relationalStore.RdbStore.createTransaction} method and then
     * call the corresponding method through the instance.
     *
     * **System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core
     *
     * **Example**:
     *
     * For details about the definition of **this.context** in the sample code, see the application
     * [context]{@link ./application/Context:Context} of the stage model.
     *
     * @interface Transaction
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 14
     */
    interface Transaction {
        /**
         * Commits this executed SQL statement. This API uses a promise to return the result. When using asynchronous APIs
         * to execute SQL statements, ensure that **commit()** is called after the asynchronous API execution is completed.
         * Otherwise, the SQL operations may be lost. After **commit()** is called, the transaction object and the created
         * **ResultSet** object will be closed.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        commit(): Promise<void>;
        /**
         * Rolls back this executed SQL statement. This API uses a promise to return the result. After **rollback()** is
         * called, the transaction object and the created **ResultSet** object will be closed.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        rollback(): Promise<void>;
        /**
         * Inserts a row of data into a table. This API uses a promise to return the result. Due to the limit of the shared
         * memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get**
         * methods such as [getValue]{@link @ohos.data.relationalStore:relationalStore.ResultSet.getValue} and
         * [getString]{@link @ohos.data.relationalStore:relationalStore.ResultSet.getString} after **ResultSet** is obtained
         * through the [query]{@link @ohos.data.relationalStore:relationalStore.RdbStore.query(predicates: RdbPredicates)}
         * or [querySql]{@link @ohos.data.relationalStore:relationalStore.RdbStore.querySqlWithoutRowCount} API of
         * **RdbStore**. As a result, the operation may fail or an exception may be thrown.
         *
         * A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is
         * retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.
         *
         * @param { string } table - Name of the target table.
         * @param { ValuesBucket } values - Row of data to insert.
         * @param { ConflictResolution } conflict - Resolution used to resolve the conflict. <br>Default value:
         *     **relationalStore.ConflictResolution.ON_CONFLICT_NONE**.
         * @returns { Promise<number> } Promise used to return the result. If the operation is successful, the row ID will be
         *     returned. Otherwise, **-1** will be returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        insert(table: string, values: ValuesBucket, conflict?: ConflictResolution): Promise<number>;
        /**
         * Inserts a row of data into a table. This API returns the result synchronously. Due to the limit of the shared
         * memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be obtained using the **get**
         * methods such as [getValue]{@link @ohos.data.relationalStore:relationalStore.ResultSet.getValue} and
         * [getString]{@link @ohos.data.relationalStore:relationalStore.ResultSet.getString} after **ResultSet** is obtained
         * through the [query]{@link @ohos.data.relationalStore:relationalStore.RdbStore.query(predicates: RdbPredicates)}
         * or [querySql]{@link @ohos.data.relationalStore:relationalStore.RdbStore.querySqlWithoutRowCount} API of
         * **RdbStore**. As a result, the operation may fail or an exception may be thrown.
         *
         * A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is
         * retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.
         *
         * @param { string } table - Name of the target table.
         * @param { ValuesBucket | sendableRelationalStore.ValuesBucket } values - Row of data to insert.
         * @param { ConflictResolution } [conflict] - Resolution used to resolve the conflict. <br>Default value:
         *     **relationalStore.ConflictResolution.ON_CONFLICT_NONE**.
         * @returns { number } If the operation is successful, the row ID will be returned. Otherwise, **-1** will be
         *     returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        insertSync(table: string, values: ValuesBucket | sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution): number;
        /**
         * Inserts data into a table in batches. This API uses a promise to return the result.
         *
         * Data is written in batches of up to 32,766 parameters each with the
         * [ConflictResolution.ON_CONFLICT_REPLACE]{@link @ohos.data.relationalStore:relationalStore.ConflictResolution}
         * policy. The total number of parameters is calculated as the number of inserted data records multiplied by the
         * size of the union set of all fields in the inserted data. If the operation fails, an error is returned.
         *
         * A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is
         * retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.
         *
         * @param { string } table - Name of the target table.
         * @param { Array<ValuesBucket> } values - An array of data to insert.
         * @returns { Promise<number> } Promise used to return the result. If the operation is successful, the number of
         *     inserted data records is returned. Otherwise, **-1** is returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>;
        /**
         * Inserts data into a table in batches. This API returns the result synchronously.
         *
         * Data is written in batches of up to 32,766 parameters each with the
         * [ConflictResolution.ON_CONFLICT_REPLACE]{@link @ohos.data.relationalStore:relationalStore.ConflictResolution}
         * policy. The total number of parameters is calculated as the number of inserted data records multiplied by the
         * size of the union set of all fields in the inserted data. If the operation fails, an error is returned.
         *
         * A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is
         * retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.
         *
         * @param { string } table - Name of the target table.
         * @param { Array<ValuesBucket> } values - An array of data to insert.
         * @returns { number } If the operation is successful, the number of inserted data records is returned. Otherwise,
         *     **-1** is returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        batchInsertSync(table: string, values: Array<ValuesBucket>): number;
        /**
         * Inserts data into a table with conflict resolutions in batches. You can use the **conflict** parameter to specify
         * [ConflictResolution]{@link @ohos.data.relationalStore:relationalStore.ConflictResolution}.
         *
         * A maximum of 32,766 parameters can be inserted at a time. If the number of parameters exceeds this limit, the
         * error code 14800000 is returned. The number of inserted data records multiplied by the size of the union across
         * all fields in the inserted data equals the number of parameters.
         *
         * For example, if the size of the union set is 10, a maximum of 3,276 data records can be inserted (3276 × 10 = 327
         * 60).
         *
         * Ensure that your application complies with this constraint when calling this API to avoid errors caused by
         * excessive parameters.
         *
         * A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is
         * retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.
         *
         * @param { string } table - Name of the target table.
         * @param { Array<ValuesBucket> } values - An array of data to insert.
         * @param { ConflictResolution } conflict - Resolution used to resolve the conflict. If **ON_CONFLICT_ROLLBACK** is
         *     used, the transaction will be rolled back when a conflict occurs.
         * @returns { number } If the operation is successful, the number of inserted data records is returned. Otherwise,
         *     **-1** is returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): number;
        /**
         * Inserts data into a table with conflict resolutions in batches. You can use the **conflict** parameter to specify
         * [ConflictResolution]{@link @ohos.data.relationalStore:relationalStore.ConflictResolution}. This API uses a
         * promise to return the result.
         *
         * A maximum of 32,766 parameters can be inserted at a time. If the number of parameters exceeds this limit, the
         * error code 14800000 is returned. The number of inserted data records multiplied by the size of the union across
         * all fields in the inserted data equals the number of parameters.
         *
         * For example, if the size of the union set is 10, a maximum of 3,276 data records can be inserted (3276 × 10 = 327
         * 60).
         *
         * Ensure that your application complies with this constraint when calling this API to avoid errors caused by
         * excessive parameters.
         *
         * @param { string } table - Name of the target table.
         * @param { Array<ValuesBucket> } values - An array of data to insert.
         * @param { ConflictResolution } conflict - Resolution used to resolve the conflict. If **ON_CONFLICT_ROLLBACK** is
         *     used, the transaction will be rolled back when a conflict occurs.
         * @returns { Promise<number> } Promise used to return the result. If the operation is successful, the number of
         *     inserted data records is returned. Otherwise, **-1** is returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800034 - SQLite: Library used incorrectly.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 18
         */
        batchInsertWithConflictResolution(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): Promise<number>;
        /**
         * Inserts data into a table in batches. You can use the **conflict** parameter to specify
         * [ConflictResolution]{@link @ohos.data.relationalStore:relationalStore.ConflictResolution}, and
         * [Result]{@link @ohos.data.relationalStore:relationalStore.Result} is returned. This API uses a promise to return
         * the result.
         *
         * A maximum of 32,766 parameters can be inserted at a time. If the number of parameters exceeds this limit, the
         * error code 14800001 is returned. The number of inserted data records multiplied by the size of the union across
         * all fields in the inserted data equals the number of parameters.
         *
         * For example, if the size of the union set is 10, a maximum of 3,276 data records can be inserted (3276 × 10 = 327
         * 60).
         *
         * Ensure that your application complies with this constraint when calling this API to avoid errors caused by
         * excessive parameters.
         *
         * It is not recommended to use the **ON_CONFLICT_FAIL** policy for the **conflict** parameter, as this may prevent
         * the return of correct results.
         *
         * A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is
         * retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.
         *
         * @param { string } table - Name of the target table for data insertion. Note: A valid table name must not contain
         *     spaces ( ), commas (,), or asterisks (*), and must not start or end with a dot (.). Otherwise, a parameter
         *     error will be thrown.
         * @param { Array<ValuesBucket> } values - An array of data to insert. Note: An empty array or data containing
         *     duplicate asset records will trigger a parameter error.
         * @param { ReturningConfig } config - Configuration information of the return value.
         * @param { ConflictResolution } [conflict] - Resolution used to resolve the conflict. Default value:
         *     **ON_CONFLICT_NONE**.
         * @returns { Promise<Result> } Promise used to return the result. If the operation is successful, the affected
         *     dataset is returned.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>;
        /**
         * Inserts data into a table in batches. You can use the **conflict** parameter to specify
         * [ConflictResolution]{@link @ohos.data.relationalStore:relationalStore.ConflictResolution}, and
         * [Result]{@link @ohos.data.relationalStore:relationalStore.Result} is returned.
         *
         * A maximum of 32,766 parameters can be inserted at a time. If the number of parameters exceeds this limit, the
         * error code 14800001 is returned. The number of inserted data records multiplied by the size of the union across
         * all fields in the inserted data equals the number of parameters.
         *
         * For example, if the size of the union set is 10, a maximum of 3,276 data records can be inserted (3276 × 10 = 327
         * 60).
         *
         * Ensure that your application complies with this constraint when calling this API to avoid errors caused by
         * excessive parameters.
         *
         * It is not recommended to use the **ON_CONFLICT_FAIL** policy for the **conflict** parameter, as this may prevent
         * the return of correct results.
         *
         * A single string field supports a maximum of 8 MB data. If the data exceeds 8 MB, only the first 8 MB data is
         * retained. For data storage requirements exceeding 8 MB, the Blob type is recommended.
         *
         * @param { string } table - Name of the target table for data insertion. Note: A valid table name must not contain
         *     spaces ( ), commas (,), or asterisks (*), and must not start or end with a dot (.). Otherwise, a parameter
         *     error will be thrown.
         * @param { Array<ValuesBucket> } values - An array of data to insert. Note: An empty array or data containing
         *     duplicate asset records will trigger a parameter error.
         * @param { ReturningConfig } config - Configuration information of the return value.
         * @param { ConflictResolution } [conflict] - Resolution used to resolve the conflict. Default value:
         *     **ON_CONFLICT_NONE**.
         * @returns { Result } If the operation is successful, the affected dataset is returned.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Result;
        /**
         * Updates data based on the specified **RdbPredicates** object. This API uses a promise to return the result. Due
         * to the limit of the shared memory, the size of a single data record cannot exceed 2 MB. Otherwise, data cannot be
         * obtained using the **get** methods such as
         * [getValue]{@link @ohos.data.relationalStore:relationalStore.ResultSet.getValue} and
         * [getString]{@link @ohos.data.relationalStore:relationalStore.ResultSet.getString} after **ResultSet** is obtained
         * through the [query]{@link @ohos.data.relationalStore:relationalStore.RdbStore.query(predicates: RdbPredicates)}
         * or [querySql]{@link @ohos.data.relationalStore:relationalStore.RdbStore.querySqlWithoutRowCount} API of
         * **RdbStore**. As a result, the operation may fail or an exception may be thrown.
         *
         * @param { ValuesBucket } values - Rows of data to update in the RDB store. The key-value pair is associated with
         *     the column name in the target table.
         * @param { RdbPredicates } predicates - Update conditions specified by the **RdbPredicates** object.
         * @param { ConflictResolution } conflict - Resolution used to resolve the conflict. <br>Default value:
         *     **relationalStore.ConflictResolution.ON_CONFLICT_NONE**.
         * @returns { Promise<number> } Promise used to return the number of rows updated.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        update(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): Promise<number>;
        /**
         * Updates data in the RDB store based on the specified **RdbPredicates** object. This API returns the result
         * synchronously. Due to the limit of the shared memory, the size of a single data record cannot exceed 2 MB.
         * Otherwise, data cannot be obtained using the **get** methods such as
         * [getValue]{@link @ohos.data.relationalStore:relationalStore.ResultSet.getValue} and
         * [getString]{@link @ohos.data.relationalStore:relationalStore.ResultSet.getString} after **ResultSet** is obtained
         * through the [query]{@link @ohos.data.relationalStore:relationalStore.RdbStore.query(predicates: RdbPredicates)}
         * or [querySql]{@link @ohos.data.relationalStore:relationalStore.RdbStore.querySqlWithoutRowCount} API of
         * **RdbStore**. As a result, the operation may fail or an exception may be thrown.
         *
         * @param { ValuesBucket } values - Rows of data to update in the RDB store. The key-value pair is associated with
         *     the column name in the target table.
         * @param { RdbPredicates } predicates - Update conditions specified by the **RdbPredicates** object.
         * @param { ConflictResolution } conflict - Resolution used to resolve the conflict. <br>Default value:
         *     **relationalStore.ConflictResolution.ON_CONFLICT_NONE**.
         * @returns { number } Number of rows updated.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): number;
        /**
         * Updates data in the RDB store based on the specified **RdbPredicates** instance object. You can use the
         * **conflict** parameter to specify
         * [ConflictResolution]{@link @ohos.data.relationalStore:relationalStore.ConflictResolution}, and
         * [Result]{@link @ohos.data.relationalStore:relationalStore.Result} is returned. This API uses a promise to return
         * the result.
         *
         * It is not recommended to use the **ON_CONFLICT_FAIL** policy for the **conflict** parameter, as this may prevent
         * the return of correct results.
         *
         * @param { ValuesBucket } values - Rows of data to update in the RDB store. The key-value pair is associated with
         *     the column name in the target table.
         * @param { RdbPredicates } predicates - Update conditions specified by the **RdbPredicates** object.
         * @param { ReturningConfig } config - Configuration information of the return value.
         * @param { ConflictResolution } [conflict] - Resolution used to resolve the conflict. Default value:
         *     **ON_CONFLICT_NONE**.
         * @returns { Promise<Result> } Promise used to return the result. If the operation is successful, the affected
         *     dataset is returned.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of    valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>;
        /**
         * Updates data in the RDB store based on the specified **RdbPredicates** instance object. You can use the
         * **conflict** parameter to specify
         * [ConflictResolution]{@link @ohos.data.relationalStore:relationalStore.ConflictResolution}, and
         * [Result]{@link @ohos.data.relationalStore:relationalStore.Result} is returned.
         *
         * It is not recommended to use the **ON_CONFLICT_FAIL** policy for the **conflict** parameter, as this may prevent
         * the return of correct results.
         *
         * @param { ValuesBucket } values - Rows of data to update in the RDB store. The key-value pair is associated with
         *     the column name in the target table.
         * @param { RdbPredicates } predicates - Update conditions specified by the **RdbPredicates** object.
         * @param { ReturningConfig } config - Configuration information of the return value.
         * @param { ConflictResolution } [conflict] - Resolution used to resolve the conflict. Default value:
         *     **ON_CONFLICT_NONE**.
         * @returns { Result } If the operation is successful, the affected dataset is returned.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of    valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Result;
        /**
         * Deletes data from the RDB store based on the specified **RdbPredicates** object. This API uses a promise to
         * return the result.
         *
         * @param { RdbPredicates } predicates - Deletion conditions specified by the **RdbPredicates** object.
         * @returns { Promise<number> } Promise used to return the number of rows deleted.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        delete(predicates: RdbPredicates): Promise<number>;
        /**
         * Deletes data from the RDB store based on the specified **RdbPredicates** object. This API returns the result
         * synchronously.
         *
         * @param { RdbPredicates } predicates - Deletion conditions specified by the **RdbPredicates** object.
         * @returns { number } Number of rows deleted.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        deleteSync(predicates: RdbPredicates): number;
        /**
         * Deletes data from the RDB store based on the specified **RdbPredicates** object and returns
         * [Result]{@link @ohos.data.relationalStore:relationalStore.Result}. This API uses a promise to return the result.
         *
         * @param { RdbPredicates } predicates - Deletion conditions specified by the **RdbPredicates** object.
         * @param { ReturningConfig } config - Configuration information of the return value.
         * @returns { Promise<Result> } Promise used to return the result. If the operation is successful, the affected
         *     dataset is returned.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of    valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>;
        /**
         * Deletes data from the RDB store based on the specified **RdbPredicates** object and returns
         * [Result]{@link @ohos.data.relationalStore:relationalStore.Result}.
         *
         * @param { RdbPredicates } predicates - Deletion conditions specified by the **RdbPredicates** object.
         * @param { ReturningConfig } config - Configuration information of the return value.
         * @returns { Result } If the operation is successful, the affected dataset is returned.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800032 - SQLite: Abort due to constraint violation.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result;
        /**
         * Queries data from the RDB store based on specified conditions. This API uses a promise to return the result.
         *
         * @param { RdbPredicates } predicates - Query conditions specified by the **RdbPredicates** object.
         * @param { Array<string> } columns - Columns to query. If null is passed in, all columns are queried.
         * @returns { Promise<ResultSet> } Promise used to return the result. If the operation is successful, a
         *     **ResultSet** object will be returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>;
        /**
         * Queries data in a database based on specified conditions. This API returns the result synchronously. If complex
         * logic and a large number of loops are involved in the operations on the **resultSet** obtained by **querySync**,
         * the freeze problem may occur. You are advised to perform this operation in the
         * [taskpool]{@link @ohos.taskpool:taskpool} thread.
         *
         * @param { RdbPredicates } predicates - Query conditions specified by the **RdbPredicates** object.
         * @param { Array<string> } columns - Columns to query. If null is passed in, all columns are queried. The default
         *     value is null.
         * @returns { ResultSet } If the operation is successful, a **ResultSet** object will be returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet;
        /**
         * Queries data in the RDB store using the specified SQL statement. The number of relational operators between
         * expressions and operators in the SQL statement cannot exceed 1,000. This API uses a promise to return the result.
         *
         * @param { string } sql - SQL statement to run.
         * @param { Array<ValueType> } args - Arguments in the SQL statement. The value corresponds to the placeholders in
         *     the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter blank.
         * @returns { Promise<ResultSet> } Promise used to return the result. If the operation is successful, a
         *     **ResultSet** object will be returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        querySql(sql: string, args?: Array<ValueType>): Promise<ResultSet>;
        /**
         * Queries data in the RDB store using the specified SQL statement. The number of relational operators between
         * expressions and operators in the SQL statement cannot exceed 1,000. If complex logic and a large number of loops
         * are involved in the operations on the **resultSet** obtained by **querySync**, the freeze problem may occur. You
         * are advised to perform this operation in the [taskpool]{@link @ohos.taskpool:taskpool} thread.
         *
         * @param { string } sql - SQL statement to run.
         * @param { Array<ValueType> } [args] - Arguments in the SQL statement. The value corresponds to the placeholders in
         *     the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter blank. The
         *     default value is null.
         * @returns { ResultSet } If the operation is successful, a **ResultSet** object will be returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        querySqlSync(sql: string, args?: Array<ValueType>): ResultSet;
        /**
         * Queries data from the RDB store based on specified conditions without calculating the row count. This API
         * delivers better performance than the [query]{@link relationalStore.Transaction.query} API. This API uses a
         * promise to return the result.
         *
         * @param { RdbPredicates } predicates - Query conditions specified by the **RdbPredicates** object.
         * @param { Array<string> } [columns] - Columns to query. If null is passed in, all columns are queried. The default
         *     value is null.
         * @returns { Promise<LiteResultSet> } If the operation is successful, a **LiteResultSet** object will be returned.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>;
        /**
         * Queries data from the RDB store based on specified conditions without calculating the row count. If complex logic
         * and a large number of loops are involved in the operations on the **LiteResultSet** obtained by
         * **queryWithoutRowCountSync**, the freeze problem may occur. You are advised to perform this operation in the
         * [taskpool]{@link @ohos.taskpool:taskpool} thread.
         *
         * @param { RdbPredicates } predicates - Query conditions specified by the **RdbPredicates** object.
         * @param { Array<string> } [columns] - Columns to query. If null is passed in, all columns are queried. The default
         *     value is null.
         * @returns { LiteResultSet } If the operation is successful, a **LiteResultSet** object will be returned.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet;
        /**
         * Queries data from the RDB store based on specified conditions without calculating the row count. This API uses a
         * promise to return the result and delivers better performance than the
         * [querySql]{@link relationalStore.Transaction.querySql} API. The number of relational operators between
         * expressions and operators in the SQL statement cannot exceed 1,000.
         *
         * @param { string } sql - SQL statement to run.
         * @param { Array<ValueType> } [bindArgs] - Arguments in the SQL statement. The value corresponds to the
         *     placeholders in the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter
         *     blank.
         * @returns { Promise<LiteResultSet> } Promise used to return the result. If the operation is successful, a
         *     **LiteResultSet** object will be returned.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>;
        /**
         * Queries data from the RDB store based on specified SQL statements without calculating the row count. The number
         * of relational operators between expressions and operators in the SQL statement cannot exceed 1,000. If complex
         * logic and a large number of loops are involved in the operations on the **LiteResultSet** obtained by
         * **querySqlWithoutRowCountSync**, the freeze problem may occur. You are advised to perform this operation in the
         * [taskpool]{@link @ohos.taskpool:taskpool} thread.
         *
         * @param { string } sql - SQL statement to run.
         * @param { Array<ValueType> } [bindArgs] - Arguments in the SQL statement. The value corresponds to the
         *     placeholders in the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter
         *     blank. The default value is null.
         * @returns { LiteResultSet } If the operation is successful, a **LiteResultSet** object will be returned.
         * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>): LiteResultSet;
        /**
             * Executes an SQL statement that contains parameters but does not return data. This API returns the result
             * synchronously. The SQL statement can be used to create, delete, query, and modify a table. The type of the return
             * value varies, depending on the execution result.
             *
             * This API does not support query, database attachment, and transaction operations. You can use
             * [querySql]{@link relationalStore.Transaction.querySql} or [query]{@link relationalStore.Transaction.query} to
             * query data, and use [attach]
             * {@link @ohos.data.relationalStore:relationalStore.RdbStore.attach(fullPath: string, attachName: string)} to
             * attach a database.
             *
             * Statements separated by semicolons (\;) are not supported.
             *
             * Statements starting with comments are not supported.
             *
             * @param { string } sql - SQL statement to run.
             * @param { Array<ValueType> } args - Arguments in the SQL statement. The value corresponds to the placeholders in
             *     the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter
             *     blank. [since 14 - 19]
             * @param { Array<ValueType> } [args] - Arguments in the SQL statement. The value corresponds to the placeholders in
             *     the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter
             *     blank. [since 20]
             * @returns { Promise<ValueType> } Promise used to return the SQL execution result.
             * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
             *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
             * @throws { BusinessError } 801 - Capability not supported the sql(attach,begin,commit,rollback etc.).
             * @throws { BusinessError } 14800000 - Inner error.
             * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
             * @throws { BusinessError } 14800014 - The target instance is already closed.
             * @throws { BusinessError } 14800021 - SQLite: Generic error.
             *     Possible causes: Insert failed or the updated data does not exist.
             * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
             * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
             * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
             * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
             * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
             * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
             * @throws { BusinessError } 14800029 - SQLite: The database is full.
             * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
             * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
             * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
             * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
             * @crossplatform [since 20]
             * @since 14
             */
        execute(sql: string, args?: Array<ValueType>): Promise<ValueType>;
        /**
         * Executes an SQL statement that contains specified arguments. The number of relational operators between
         * expressions and operators in the statement cannot exceed 1,000. This API returns a value of the **ValueType**
         * type.
         *
         * This API can be used to add, delete, and modify data, run SQL statements of the PRAGMA syntax, and create,
         * delete, and modify a table. The type of the return value varies, depending on the execution result.
         *
         * This API does not support query, database attachment, and transaction operations. You can use
         * [querySql]{@link relationalStore.Transaction.querySql} or [query]{@link relationalStore.Transaction.query} to
         * query data, and use [attach]
         * {@link @ohos.data.relationalStore:relationalStore.RdbStore.attach(fullPath: string, attachName: string)} to
         * attach a database.
         *
         * Statements separated by semicolons (\;) are not supported.
         *
         * Statements starting with comments are not supported.
         *
         * @param { string } sql - SQL statement to run.
         * @param { Array<ValueType> } [args] - Arguments in the SQL statement. The value corresponds to the placeholders in
         *     the SQL parameter statement. If this parameter is left blank or set to **null** or **undefined**, the SQL
         *     statement is complete. The default value is null.
         * @returns { ValueType } SQL execution result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported the sql(attach,begin,commit,rollback etc.).
         * @throws { BusinessError } 14800000 - Inner error.
         * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
         * @throws { BusinessError } 14800014 - The target instance is already closed.
         * @throws { BusinessError } 14800021 - SQLite: Generic error.
         *     Possible causes: Insert failed or the updated data does not exist.
         * @throws { BusinessError } 14800023 - SQLite: Access permission denied.
         * @throws { BusinessError } 14800024 - SQLite: The database file is locked.
         * @throws { BusinessError } 14800025 - SQLite: A table in the database is locked.
         * @throws { BusinessError } 14800026 - SQLite: The database is out of memory.
         * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
         * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
         * @throws { BusinessError } 14800029 - SQLite: The database is full.
         * @throws { BusinessError } 14800031 - SQLite: TEXT or BLOB exceeds size limit.
         * @throws { BusinessError } 14800033 - SQLite: Data type mismatch.
         * @throws { BusinessError } 14800047 - The WAL file size exceeds the default limit.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @crossplatform
         * @since 14
         */
        executeSync(sql: string, args?: Array<ValueType>): ValueType;
    }
    /**
     * Obtains an RdbStore instance. You can set the **config** parameter as required and use **RdbStore** APIs to perform
     * data operations. This API uses an asynchronous callback to return the result.
     *
     * If no database file exists in the corresponding sandbox directory, a database file is created. For details, see
     * [StoreConfig]{@link @ohos.data.relationalStore:relationalStore.StoreConfig}. If a database file exists in the
     * corresponding directory, the existing database file is opened.
     *
     * When creating a database, you should consider whether to configure the
     * [encrypt]{@link @ohos.data.relationalStore:relationalStore.StoreConfig} parameter. Once the database is created,
     * you are not allowed to change this parameter.
     *
     * | Encryption Type When the RDB Store Is Opened | Encryption Type When the RDB Store Is Created          | Result|
     * | ------- | -------------------------------- | ---- |
     * | Non-encryption| Encryption                         | The RDB store is opened in encrypted mode.  |
     * | Encryption| Non-encryption                         | The RDB store is opened in non-encrypted mode.  |
     *
     * Currently, **getRdbStore()** does not support multi-thread concurrent operations.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { StoreConfig } config - Configuration of the RDB store.
     * @param { AsyncCallback<RdbStore> } callback - Callback invoked to return the RDB store obtained.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14800000 - Inner error.
     * @throws { BusinessError } 14800010 - Failed to open or delete the database by an invalid database path.
     * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
     * @throws { BusinessError } 14801001 - The operation is supported in the stage model only. [since 10]
     * @throws { BusinessError } 14801002 - Invalid data group ID. [since 10]
     * @throws { BusinessError } 14800017 - StoreConfig is changed. [since 12]
     * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
     * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 12]
     * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 12]
     * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
     * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
     * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
     * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
     * @throws { BusinessError } 14800020 - The secret key is corrupted or lost. [since 14]
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 10]
     * @since 9
     */
    function getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void;
    /**
     * Obtains an RdbStore instance. You can set the **config** parameter as required and use **RdbStore** APIs to perform
     * data operations. This API uses a promise to return the result.
     *
     * If no database file exists in the corresponding sandbox directory, a database file is created. For details, see
     * [StoreConfig]{@link @ohos.data.relationalStore:relationalStore.StoreConfig}. If a database file exists in the
     * corresponding directory, the existing database file is opened.
     *
     * When creating a database, you should consider whether to configure the
     * [encrypt]{@link @ohos.data.relationalStore:relationalStore.StoreConfig} parameter. Once the database is created,
     * you are not allowed to change this parameter.
     *
     * | Encryption Type When the RDB Store Is Opened | Encryption Type When the RDB Store Is Created          | Result|
     * | ------- | -------------------------------- | ---- |
     * | Non-encryption| Encryption                         | The RDB store is opened in encrypted mode.  |
     * | Encryption| Non-encryption                         | The RDB store is opened in non-encrypted mode.  |
     *
     * Currently, **getRdbStore()** does not support multi-thread concurrent operations.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { StoreConfig } config - Configuration of the RDB store.
     * @returns { Promise<RdbStore> } Promise used to return the **RdbStore** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14800000 - Inner error.
     * @throws { BusinessError } 14800010 - Failed to open or delete the database by an invalid database path.
     * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
     * @throws { BusinessError } 14801001 - The operation is supported in the stage model only. [since 10]
     * @throws { BusinessError } 14801002 - Invalid data group ID. [since 10]
     * @throws { BusinessError } 14800017 - StoreConfig is changed. [since 12]
     * @throws { BusinessError } 14800021 - SQLite: Generic error. [since 12]
     * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database. [since 12]
     * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred. [since 12]
     * @throws { BusinessError } 14800029 - SQLite: The database is full. [since 12]
     * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file. [since 12]
     * @throws { BusinessError } 14800020 - The secret key is corrupted or lost. [since 14]
     * @throws { BusinessError } 14800022 - SQLite: Callback routine requested an abort. [since 14]
     * @throws { BusinessError } 14800023 - SQLite: Access permission denied. [since 14]
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 10]
     * @since 9
     */
    function getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>;
    /**
     * Obtains a RDB store.
     * You can set parameters of the RDB store as required. This is a synchronous method
     * that blocks the thread until the RDB store is obtained.
     *
     * @param { Context } context - Indicates the context of an application or ability.
     * @param { StoreConfig } config - Indicates the {@link StoreConfig} configuration of the database related to
     *     this RDB store.
     * @returns { RdbStore } The RDB store {@link RdbStore}.
     * @throws { BusinessError } 14800001 - Invalid args.
     * @throws { BusinessError } 14800010 - Invalid database path.
     * @throws { BusinessError } 14800011 - The current operation failed because the database is corrupted.
     * @throws { BusinessError } 14801001 - The operation is supported in the stage model only.
     * @throws { BusinessError } 14801002 - Invalid data group ID.
     * @throws { BusinessError } 14800017 - Config changed.
     * @throws { BusinessError } 14800020 - The secret key is corrupted or lost.
     * @throws { BusinessError } 14800021 - SQLite: Generic error.
     * @throws { BusinessError } 14800027 - SQLite: Attempt to write a readonly database.
     * @throws { BusinessError } 14800028 - SQLite: Some kind of disk I/O error occurred.
     * @throws { BusinessError } 14800029 - SQLite: The database is full.
     * @throws { BusinessError } 14800030 - SQLite: Unable to open the database file.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @stagemodelonly
     * @crossplatform
     * @since 24
     */
    function getRdbStoreSync(context: Context, config: StoreConfig): RdbStore;
    /**
       * Deletes the RDB store with the specified database file name. This API uses a promise to return the result.
       *
       * If **vector** is set to **true** in [StoreConfig]
       * {@link @ohos.data.relationalStore:relationalStore.StoreConfig} when an RDB store is created, using this API cannot
       * delete the RDB store. Use [deleteRdbStore]
       * {@link relationalStore.deleteRdbStore(context: Context, config: StoreConfig)} instead.
       *
       * Before calling **deleteRdbStore**, ensure that the **RdbStore** and **ResultSet** of the vector store have been
       * closed.
       *
       * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
       *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
       *     [Context]{@link ./application/Context:Context}.
       * @param { string } name - Name of the RDB store to delete.
       * @param { AsyncCallback<void> } callback - Callback invoked to return the result.
       * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
       *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
       * @throws { BusinessError } 14800000 - Inner error.
       * @throws { BusinessError } 14800010 - Failed to open or delete the database by an invalid database path.
       * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
       * @crossplatform [since 10]
       * @since 9
       */
    function deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void;
    /**
     * Deletes an RDB store. This API uses an asynchronous callback to return the result.
     *
     * After the deletion, you are advised to set the database object to null. If the database file is stored in the
     * sandbox directory, use this API to delete the database. If multiple processes operate the same database, other
     * processes should be notified about the database deletion so that they can detect and process the deletion. If a
     * custom path is set in [StoreConfig]{@link @ohos.data.relationalStore:relationalStore.StoreConfig} during RDB store
     * creation, using this API to delete the RDB store.
     *
     * Before calling **deleteRdbStore**, ensure that the **RdbStore** and **ResultSet** of the vector store have been
     * closed.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { StoreConfig } config - Configuration of the RDB store.
     * @param { AsyncCallback<void> } callback - Callback invoked to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14800000 - Inner error.
     * @throws { BusinessError } 14800010 - Failed to open or delete the database by an invalid database path.
     * @throws { BusinessError } 14801001 - The operation is supported in the stage model only.
     * @throws { BusinessError } 14801002 - Invalid data group ID.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 10
     */
    function deleteRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<void>): void;
    /**
     * Deletes an RDB store. This API uses a promise to return the result.
     *
     * After the deletion, you are advised to set the database object to null. If a custom path is set in
     * [StoreConfig]{@link @ohos.data.relationalStore:relationalStore.StoreConfig} when an RDB store is created, using
     * this API cannot delete the RDB store. Use
     * [deleteRdbStore]{@link relationalStore.deleteRdbStore(context: Context, config: StoreConfig)} instead.
     *
     * Before calling **deleteRdbStore**, ensure that the **RdbStore** and **ResultSet** of the vector store have been
     * closed.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { string } name - Name of the RDB store to delete.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14800000 - Inner error.
     * @throws { BusinessError } 14800010 - Failed to open or delete the database by an invalid database path.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform [since 10]
     * @since 9
     */
    function deleteRdbStore(context: Context, name: string): Promise<void>;
    /**
     * Deletes an RDB store. This API uses a promise to return the result.
     *
     * After the deletion, you are advised to set the database object to null. If the database file is stored in the
     * sandbox directory, use this API to delete the database. If multiple processes operate the same database, other
     * processes should be notified about the database deletion so that they can detect and process the deletion. If a
     * custom path is set in [StoreConfig]{@link @ohos.data.relationalStore:relationalStore.StoreConfig} during RDB store
     * creation, using this API to delete the RDB store.
     *
     * Before calling **deleteRdbStore**, ensure that the **RdbStore** and **ResultSet** of the vector store have been
     * closed.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.
     * @param { StoreConfig } config - Configuration of the RDB store.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14800000 - Inner error.
     * @throws { BusinessError } 14800010 - Failed to open or delete the database by an invalid database path.
     * @throws { BusinessError } 14801001 - The operation is supported in the stage model only.
     * @throws { BusinessError } 14801002 - Invalid data group ID.
     * @throws { BusinessError } 801 - Capability not supported. [since 12]
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 10
     */
    function deleteRdbStore(context: Context, config: StoreConfig): Promise<void>;
    /**
     * Checks whether the system supports vector stores.
     *
     * @returns { boolean } Returns **true** if the system supports vector stores; returns **false** otherwise.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 18
     */
    function isVectorSupported(): boolean;
    /**
     * Checks whether the specified tokenizer is supported. This API returns the result synchronously.
     *
     * This API returns **true** if the specified tokenizer is supported; returns **false** otherwise.
     *
     * @param { Tokenizer } tokenizer - Tokenizer to check.
     * @returns { boolean } Returns **true** if the specified tokenizer is supported; returns **false** otherwise.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 18
     */
    function isTokenizerSupported(tokenizer: Tokenizer): boolean;
    /**
     * Obtains the SQL statement used to insert data. This API returns the result synchronously.
     *
     * @param { string } table - Name of the database table to which data is to be written.
     * @param { ValuesBucket } values - Field information and corresponding values of the data to be written to the
     *     database.
     * @param { ConflictResolution } conflict - Resolution used to resolve the conflict. <br>Default value:
     *     **relationalStore.ConflictResolution.ON_CONFLICT_NONE**.
     * @returns { SqlInfo } **SqlInfo** object. **sql** indicates the returned SQL statement, and **args** indicates the
     *     parameters in the executed SQL statement.
     * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 20
     */
    function getInsertSqlInfo(table: string, values: ValuesBucket, conflict?: ConflictResolution): SqlInfo;
    /**
     * Obtains the SQL statement used to update data. This API returns the result synchronously.
     *
     * @param { RdbPredicates } predicates - **RdbPredicates** object that matches the specified field.
     * @param { ValuesBucket } values - Field information and corresponding values of the data to be written to the
     *     database.
     * @param { ConflictResolution } conflict - Resolution used to resolve the conflict. <br>Default value:
     *     **relationalStore.ConflictResolution.ON_CONFLICT_NONE**.
     * @returns { SqlInfo } **SqlInfo** object. **sql** indicates the returned SQL statement, and **args** indicates the
     *     parameters in the executed SQL statement.
     * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 20
     */
    function getUpdateSqlInfo(predicates: RdbPredicates, values: ValuesBucket, conflict?: ConflictResolution): SqlInfo;
    /**
     * Obtains the SQL statement used to delete data. This API returns the result synchronously.
     *
     * @param { RdbPredicates } predicates - **RdbPredicates** object that matches the specified field.
     * @returns { SqlInfo } **SqlInfo** object. **sql** indicates the returned SQL statement, and **args** indicates the
     *     parameters in the executed SQL statement.
     * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 20
     */
    function getDeleteSqlInfo(predicates: RdbPredicates): SqlInfo;
    /**
     * Obtains the SQL statement used to query data. This API returns the result synchronously.
     *
     * @param { RdbPredicates } predicates - **RdbPredicates** object that matches the specified field.
     * @param { Array<string> } columns - Columns to be queried. If this parameter is not specified, all columns are
     *     queried.
     * @returns { SqlInfo } **SqlInfo** object. **sql** indicates the returned SQL statement, and **args** indicates the
     *     parameters in the executed SQL statement.
     * @throws { BusinessError } 14800001 - Invalid arguments. Possible causes: 1. Parameter is out of valid range.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @crossplatform
     * @since 20
     */
    function getQuerySqlInfo(predicates: RdbPredicates, columns?: Array<string>): SqlInfo;
}
export default relationalStore;

```
