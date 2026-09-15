# @ohos.data.rdb.d.ts

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
import { ResultSet as _ResultSet } from './data/rdb/resultSet';
import Context from './application/BaseContext';
/**
 * The relational database (RDB) manages data based on relational models. With the underlying SQLite database, the RDB
 * provides a complete mechanism for managing local databases. To satisfy different needs in complicated scenarios, the
 * RDB offers a series of methods for performing operations such as adding, deleting, modifying, and querying data, and
 * supports direct execution of SQL statements. The worker threads are not supported.
 *
 * This module provides the following RDB-related functions:
 *
 * - [RdbPredicates]{@link rdb.RdbPredicates}: provides APIs for creating predicates. The predicates represent the
 * properties, characteristics, or relationships between data entities in an RDB store and are used to define data
 * operation conditions.
 * - [RdbStore]{@link rdb.RdbStore}: provides APIs for managing data in an RDB store.
 *
 * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.data.relationalStore:relationalStore
 */
declare namespace rdb {
    /**
     * Obtains an RDB store. This API uses an asynchronous callback to return the result. You can set parameters for the
     * RDB store based on service requirements and call APIs to perform data operations.
     *
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see [Context]{@link ./app/context}.
     *     <br>For details about the application context of the stage model, see [Context]{@link ./app/context}.
     * @param { StoreConfig } config - Configuration of the RDB store.
     * @param { number } version - RDB store version.<br>Currently, automatic RDB upgrades and downgrades performed based
     *     on **version** is not supported.
     * @param { AsyncCallback<RdbStore> } callback - Callback used to return the RDB store obtained.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.data.relationalStore:relationalStore.getRdbStore
     */
    function getRdbStore(context: Context, config: StoreConfig, version: number, callback: AsyncCallback<RdbStore>): void;
    /**
     * Obtains an RDB store. This API uses a promise to return the result. You can set parameters for the RDB store based
     * on service requirements and call APIs to perform data operations.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.
     *     <br>For details about the application context of the stage model, see [Context]{@link ./app/context}.
     * @param { StoreConfig } config - Configuration of the RDB store.
     * @param { number } version - RDB store version.<br>Currently, automatic RDB upgrades and downgrades performed based
     *     on **version** is not supported.
     * @returns { Promise<RdbStore> } Promise used to return the **RdbStore** object.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 7
     * @deprecated since 9
     */
    function getRdbStore(context: Context, config: StoreConfig, version: number): Promise<RdbStore>;
    /**
     * Deletes an RDB store. This API uses an asynchronous callback to return the result.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.
     *     <br>For details about the application context of the stage model, see [Context]{@link ./app/context}.
     * @param { string } name - Name of the RDB store to delete.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.data.relationalStore:relationalStore.deleteRdbStore
     */
    function deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void;
    /**
     * Deletes an RDB store. This API uses a promise to return the result.
     *
     * @param { Context } context - Application context.<br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.
     *     <br>For details about the application context of the stage model, see [Context]{@link ./app/context}.
     * @param { string } name - Name of the RDB store to delete.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.data.relationalStore:relationalStore.deleteRdbStore
     */
    function deleteRdbStore(context: Context, name: string): Promise<void>;
    /**
     * Defines the database sync mode.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.data.relationalStore:relationalStore.SyncMode
     */
    enum SyncMode {
        /**
         * Data is pushed from a local device to a remote device.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.SyncMode.SYNC_MODE_PUSH
         */
        SYNC_MODE_PUSH = 0,
        /**
         * Data is pulled from a remote device to a local device.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.SyncMode.SYNC_MODE_PULL
         */
        SYNC_MODE_PULL = 1
    }
    /**
     * Defines the subscription type.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.data.relationalStore:relationalStore.SubscribeType
     */
    enum SubscribeType {
        /**
         * Subscribe to remote data changes.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE
         */
        SUBSCRIBE_TYPE_REMOTE = 0
    }
    /**
     * Provides APIs for managing data in an RDB store.
     *
     * Before using the APIs of this class, use
     * [executeSql]{@link rdb.RdbStore.executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>)}
     * to initialize the database table structure and related data.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore
     */
    interface RdbStore {
        /**
         * Inserts a row of data into a table. This API uses an asynchronous callback to return the result.
         *
         * @param { string } table - Name of the target table.
         * @param { ValuesBucket } values - Row of data to insert.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     the row ID will be returned. Otherwise, **-1** will be returned.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.insert
         */
        insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>): void;
        /**
         * Inserts a row of data into a table. This API uses a promise to return the result.
         *
         * @param { string } table - Name of the target table.
         * @param { ValuesBucket } values - Row of data to insert.
         * @returns { Promise<number> } Promise used to return the result. If the operation is successful, the row ID will
         *     be returned. Otherwise, **-1** will be returned.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.insert
         */
        insert(table: string, values: ValuesBucket): Promise<number>;
        /**
         * Inserts a batch of data into a table. This API uses an asynchronous callback to return the result.
         *
         * @param { string } table - Name of the target table.
         * @param { Array<ValuesBucket> } values - An array of data to insert.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     the number of inserted data records is returned. Otherwise, **-1** is returned.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.batchInsert
         */
        batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void;
        /**
         * Inserts a batch of data into a table. This API uses a promise to return the result.
         *
         * @param { string } table - Name of the target table.
         * @param { Array<ValuesBucket> } values - An array of data to insert.
         * @returns { Promise<number> } Promise used to return the result. If the operation is successful, the number of
         *     inserted data records is returned. Otherwise, **-1** is returned.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.batchInsert
         */
        batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>;
        /**
         * Updates data in the RDB store based on the specified **RdbPredicates** object. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { ValuesBucket } values - Rows of data to update in the RDB store. The key-value pair is associated with
         *     the column name in the target table.
         * @param { RdbPredicates } predicates - Update conditions specified by the **RdbPredicates** object.
         * @param { AsyncCallback<number> } callback - Callback invoked to return the number of rows updated.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.update
         */
        update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>): void;
        /**
         * Updates data based on the specified **RdbPredicates** object. This API uses a promise to return the result.
         *
         * @param { ValuesBucket } values - Rows of data to update in the RDB store. The key-value pair is associated with
         *     the column name in the target table.
         * @param { RdbPredicates } predicates - Update conditions specified by the **RdbPredicates** object.
         * @returns { Promise<number> } Promise used to return the number of rows updated.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.update
         */
        update(values: ValuesBucket, predicates: RdbPredicates): Promise<number>;
        /**
         * Deletes data from the RDB store based on the specified **RdbPredicates** object. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { RdbPredicates } predicates - Deletion conditions specified by the **RdbPredicates** object.
         * @param { AsyncCallback<number> } callback - Callback used to return the number of rows deleted.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.delete
         */
        delete(predicates: RdbPredicates, callback: AsyncCallback<number>): void;
        /**
         * Deletes data from the RDB store based on the specified **RdbPredicates** object. This API uses a promise to
         * return the result.
         *
         * @param { RdbPredicates } predicates - Deletion conditions specified by the **RdbPredicates** object.
         * @returns { Promise<number> } Promise used to return the number of rows deleted.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.delete
         */
        delete(predicates: RdbPredicates): Promise<number>;
        /**
         * Queries data from the RDB store based on specified conditions. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { RdbPredicates } predicates - Query conditions specified by the **RdbPredicates** object.
         * @param { Array<string> } columns - Columns to query. If this parameter is not specified, the query applies to all
         *     columns.
         * @param { AsyncCallback<ResultSet> } callback - Callback used to return the result. If the operation is successful
         *     , a **ResultSet** object will be returned.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.query
         */
        query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>): void;
        /**
         * Queries data from the RDB store based on specified conditions. This API uses a promise to return the result.
         *
         * @param { RdbPredicates } predicates - Query conditions specified by the **RdbPredicates** object.
         * @param { Array<string> } columns - Columns to query. If this parameter is not specified, the query applies to all
         *     columns.
         * @returns { Promise<ResultSet> } Promise used to return the result. If the operation is successful, a
         *     **ResultSet** object will be returned.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.query
         */
        query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>;
        /**
         * Queries data using the specified SQL statement. This API uses an asynchronous callback to return the result.
         *
         * @param { string } sql - SQL statement to run.
         * @param { Array<ValueType> } bindArgs - Arguments in the SQL statement. The value corresponds to the placeholders
         *     in the SQL parameter statement. If the SQL parameter statement is complete, the value of this parameter must
         *     be an empty array.
         * @param { AsyncCallback<ResultSet> } callback - Callback used to return the result. If the operation is successful
         *     , a **ResultSet** object will be returned.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.querySql
         */
        querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>): void;
        /**
         * Queries data using the specified SQL statement. This API uses a promise to return the result.
         *
         * @param { string } sql - SQL statement to run.
         * @param { Array<ValueType> } bindArgs - Arguments in the SQL statement. The value corresponds to the placeholders
         *     in the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter blank.
         * @returns { Promise<ResultSet> } Promise used to return the result. If the operation is successful, a
         *     **ResultSet** object will be returned.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.querySql
         */
        querySql(sql: string, bindArgs?: Array<ValueType>): Promise<ResultSet>;
        /**
         * Executes an SQL statement that contains specified arguments but returns no value. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { string } sql - SQL statement to run.
         * @param { Array<ValueType> } bindArgs - Arguments in the SQL statement. The value corresponds to the placeholders
         *     in the SQL parameter statement. If the SQL parameter statement is complete, the value of this parameter must
         *     be an empty array.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.executeSql
         */
        executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>): void;
        /**
         * Executes an SQL statement that contains specified arguments but returns no value. This API uses a promise to
         * return the result.
         *
         * @param { string } sql - SQL statement to run.
         * @param { Array<ValueType> } bindArgs - Arguments in the SQL statement. The value corresponds to the placeholders
         *     in the SQL parameter statement. If the SQL parameter statement is complete, leave this parameter blank.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.executeSql
         */
        executeSql(sql: string, bindArgs?: Array<ValueType>): Promise<void>;
        /**
         * Starts the transaction before executing an SQL statement.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.beginTransaction
         */
        beginTransaction(): void;
        /**
         * Commits the executed SQL statements.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.commit
         */
        commit(): void;
        /**
         * Rolls back the SQL statements that have been executed.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.rollBack
         */
        rollBack(): void;
        /**
         * Sets distributed tables. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { Array<string> } tables - Names of the distributed tables to set.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.setDistributedTables
         */
        setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void;
        /**
         * Sets distributed tables. This API uses a promise to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { Array<string> } tables - Names of the distributed tables to set.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.setDistributedTables
         */
        setDistributedTables(tables: Array<string>): Promise<void>;
        /**
         * Obtains the distributed table name of a remote device based on the local table name of the device. The
         * distributed table name is required when the RDB store of a remote device is queried. This API uses an
         * asynchronous callback to return the result.
         *
         * > **NOTE**
         *
         * > The value of **device** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}
         * > . <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } device - ID of the remote device.
         * @param { string } table - Local table name of the remote device.
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation succeeds, the
         *     distributed table name of the remote device is returned.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.obtainDistributedTableName
         */
        obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void;
        /**
         * Obtains the distributed table name of a remote device based on the local table name of the device. The
         * distributed table name is required when the RDB store of a remote device is queried. This API uses a promise to
         * return the result.
         *
         * > **NOTE**
         *
         * > The value of **device** can be obtained by <!--RP1-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}
         * > . <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } device - ID of the remote device.
         * @param { string } table - Local table name of the remote device.
         * @returns { Promise<string> } Promise used to return the result. If the operation succeeds, the distributed table
         *     name of the remote device is returned.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.obtainDistributedTableName
         */
        obtainDistributedTableName(device: string, table: string): Promise<string>;
        /**
         * Synchronizes data across devices. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { SyncMode } mode - Data sync mode. The value can be **push** or **pull**.
         * @param { RdbPredicates } predicates - **RdbPredicates** object that specifies the data and devices to
         *     synchronize.
         * @param { AsyncCallback<Array<[ string, number ]>> } callback - Callback invoked to send the sync result to the
         *     caller. <br>**string** indicates the device ID. <br>**number** indicates the sync status of that device. The
         *     value **0** indicates a successful sync. Other values indicate a sync failure.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.sync
         */
        sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[
            string,
            number
        ]>>): void;
        /**
         * Synchronizes data across devices. This API uses a promise to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { SyncMode } mode - Data sync mode. The value can be **push** or **pull**.
         * @param { RdbPredicates } predicates - **RdbPredicates** object that specifies the data and devices to
         *     synchronize.
         * @returns { Promise<Array<[ string, number ]>> } Promise used to send the sync result.
         *     <br>**string** indicates the device ID.
         *     <br>**number** indicates the sync status of that device. The value **0** indicates a successful sync. Other values
         *     indicate a sync failure.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.sync
         */
        sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[
            string,
            number
        ]>>;
        /**
         * Registers an observer for this RDB store. When the data in the RDB store changes, a callback is invoked to return
         * the data changes.
         *
         * @param { 'dataChange' } event - Event to observe. The value is **dataChange**, which indicates a data change
         *     event.
         * @param { SubscribeType } type - Subscription type to register.
         * @param { Callback<Array<string>> } observer - Observer that listens for the data changes in the RDB store.
         *     **Array<string>** indicates the ID of the peer device whose data in the database is changed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.on
         */
        on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void;
        /**
         * Unregisters the observer of the specified type from the RDB store. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'dataChange' } event - Event to observe. The value is **dataChange**, which indicates a data change
         *     event.
         * @param { SubscribeType } type - Subscription type to register.
         * @param { Callback<Array<string>> } observer - Data change observer registered. **Array<string>** indicates the ID
         *     of the peer device whose data in the database is changed.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbStore.off
         */
        off(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void;
    }
    /**
     * Defines the data types allowed.
     *
     * @unionmember { number } Number.
     * @unionmember { string } String.
     * @unionmember { boolean } Boolean.
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.data.relationalStore:relationalStore.ValueType
     */
    type ValueType = number | string | boolean;
    /**
     * Defines the types of the key and value in a KV pair.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.data.relationalStore:relationalStore.ValuesBucket
     */
    type ValuesBucket = {
        [key: string]: ValueType | Uint8Array | null;
    };
    /**
     * Defines the RDB store configuration.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.data.relationalStore:relationalStore.StoreConfig
     */
    interface StoreConfig {
        /**
         * Database file name.
         *
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.StoreConfig.name
         */
        name: string;
    }
    /**
     * Defines predicates for an RDB store. This class determines whether the conditional expression for the RDB store is
     * true or false.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates
     */
    class RdbPredicates {
        /**
         * A constructor used to create an **RdbPredicates** object.
         *
         * @param { string } name - Database table name.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates
         */
        constructor(name: string);
        /**
         * Creates an **RdbPredicates** object to specify the remote devices to connect on the network during distributed
         * database sync.
         *
         * > **NOTE**
         *
         * > The value of **devices** can be obtained by using <!--RP2-->
         * > [deviceManager.getTrustedDeviceListSync]{@link @ohos.distributedHardware.deviceManager:deviceManager.DeviceManager.getTrustedDeviceListSync()}
         * > . <!--RP2End-->The APIs of the **deviceManager** module are system interfaces and available only to system
         * > applications.
         *
         * @param { Array<string> } devices - IDs of the remote devices in the same network.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.inDevices
         */
        inDevices(devices: Array<string>): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to specify all remote devices on the network to connect during distributed
         * database sync.
         *
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.inAllDevices
         */
        inAllDevices(): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are equal to the given
         * value.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.equalTo
         */
        equalTo(field: string, value: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are not equal to the
         * given value.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.notEqualTo
         */
        notEqualTo(field: string, value: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to add a left parenthesis.
         *
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.beginWrap
         */
        beginWrap(): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to add a right parenthesis.
         *
         * @returns { RdbPredicates } **RdbPredicates** created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.endWrap
         */
        endWrap(): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to add the OR condition.
         *
         * @returns { RdbPredicates } **RdbPredicates** created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.or
         */
        or(): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to add the AND condition.
         *
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.and
         */
        and(): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that contain the given
         * value.
         *
         * @param { string } field - Column name in the database table.
         * @param { string } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.contains
         */
        contains(field: string, value: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that start with the given
         * value.
         *
         * @param { string } field - Column name in the database table.
         * @param { string } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.beginsWith
         */
        beginsWith(field: string, value: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that end with the given
         * value.
         *
         * @param { string } field - Column name in the database table.
         * @param { string } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.endsWith
         */
        endsWith(field: string, value: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are **null**.
         *
         * @param { string } field - Column name in the database table.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.isNull
         */
        isNull(field: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are not **null**.
         *
         * @param { string } field - Column name in the database table.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2
         *     . Incorrect parameter types.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.isNotNull
         */
        isNotNull(field: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are similar to the
         * given value.
         *
         * @param { string } field - Column name in the database table.
         * @param { string } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.like
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
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.glob
         */
        glob(field: string, value: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are within the
         * specified range.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } low - Minimum value of the range to set.
         * @param { ValueType } high - Maximum value of the range to set.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.between
         */
        between(field: string, low: ValueType, high: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are out of the
         * specified range.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } low - Minimum value of the range to set.
         * @param { ValueType } high - Maximum value of the range to set.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.notBetween
         */
        notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are greater than the
         * given value.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.greaterThan
         */
        greaterThan(field: string, value: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are less than the
         * given value.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.lessThan
         */
        lessThan(field: string, value: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are greater than or
         * equal to the given value.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.greaterThanOrEqualTo
         */
        greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are less than or equal
         * to the given value.
         *
         * @param { string } field - Column name in the database table.
         * @param { ValueType } value - Value to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.lessThanOrEqualTo
         */
        lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to sort the records in the specified column in ascending order.
         *
         * @param { string } field - Column name in the database table.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.orderByAsc
         */
        orderByAsc(field: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to sort the records in the specified column in descending order.
         *
         * @param { string } field - Column name in the database table.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.orderByDesc
         */
        orderByDesc(field: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to filter out duplicate records.
         *
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.distinct
         */
        distinct(): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to limit the number of records.
         *
         * @param { number } value - Maximum number of records.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.limitAs
         */
        limitAs(value: number): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to specify the start position of the returned result. This API must be used
         * together with **limitAs**. Otherwise, no result will be returned. To query all rows after the specified offset,
         * pass in **-1** in **limitAs**.
         *
         * @param { number } rowOffset - Start position, which is a positive integer.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.offsetAs
         */
        offsetAs(rowOffset: number): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to group the query results based on the specified columns.
         *
         * @param { Array<string> } fields - Names of columns to group.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.groupBy
         */
        groupBy(fields: Array<string>): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to specify the index column.
         *
         * @param { string } field - Name of the index column.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.indexedBy
         */
        indexedBy(field: string): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are within the
         * specified range.
         *
         * @param { string } field - Column name in the database table.
         * @param { Array<ValueType> } value - Array of **ValueType**s to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.in
         */
        in(field: string, value: Array<ValueType>): RdbPredicates;
        /**
         * Creates an **RdbPredicates** object to search for the records in the specified column that are out of the
         * specified range.
         *
         * @param { string } field - Column name in the database table.
         * @param { Array<ValueType> } value - Array of **ValueType**s to match.
         * @returns { RdbPredicates } **RdbPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.data.relationalStore:relationalStore.RdbPredicates.notIn
         */
        notIn(field: string, value: Array<ValueType>): RdbPredicates;
    }
    /**
     * Configure RdbPredicates to match the specified field whose data type is ValueType array and values
     * are out of a given range.
     *
     * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
     * @since 7
     * @deprecated since 9
     */
    export type ResultSet = _ResultSet;
}
/**
 * Provides methods for rdbStore create and delete.
 * @syscap SystemCapability.DistributedDataManager.RelationalStore.Core
 * @since 7
 * @deprecated since 9
 */
export default rdb;

```
