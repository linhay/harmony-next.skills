# @ohos.data.dataAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
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
import rdb from './@ohos.data.rdb';
/**
 * The **DataAbility** module provides APIs to create predicates for querying data from relational database (RDB)
 * stores.
 *
 * @syscap SystemCapability.DistributedDataManager.DataShare.Core
 * @since 7
 */
declare namespace dataAbility {
    /**
     * Creates an **RdbPredicates** object with a table name and **DataAbilityPredicates** object.
     *
     * @param { string } name - Name of a database table.
     * @param { DataAbilityPredicates } dataAbilityPredicates - **DataAbilityPredicates** object.
     * @returns { rdb.RdbPredicates } **RdbPredicates** object created.
     * @syscap SystemCapability.DistributedDataManager.DataShare.Core
     * @since 7
     */
    function createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates;
    /**
     * Provides APIs for creating diverse query conditions.
     *
     * @syscap SystemCapability.DistributedDataManager.DataShare.Core
     * @since 7
     */
    class DataAbilityPredicates {
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that are equal to
         * the given value.
         *
         * This API is similar to the SQL equal to (=) operator.
         *
         * @param { string } field - Column name in the table.
         * @param { ValueType } value - Value to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        equalTo(field: string, value: ValueType): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that are not equal
         * to the given value.
         *
         * This API is similar to the SQL not equal (!=) operator.
         *
         * @param { string } field - Column name in the table.
         * @param { ValueType } value - Value to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        notEqualTo(field: string, value: ValueType): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to add a left parenthesis. This API is similar to "(" in an SQL
         * statement and must be used with **endWrap**.
         *
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object with a left parenthesis.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        beginWrap(): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to add a right parenthesis. This API is similar to ")" in an SQL
         * statement and must be used with **beginWrap**.
         *
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object with a right parenthesis.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        endWrap(): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to add the OR condition.
         *
         * This API is similar to the SQL **or** operator.
         *
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object with the OR condition.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        or(): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to add the AND condition.
         *
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object with the AND condition.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        and(): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that contain the
         * given value.
         *
         * @param { string } field - Column name in the table.
         * @param { string } value - Value to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        contains(field: string, value: string): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that begin with the
         * given value.
         *
         * This API is similar to the percent sign (%) in SQL statements.
         *
         * @param { string } field - Column name in the table.
         * @param { string } value - Value to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        beginsWith(field: string, value: string): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that end with the
         * given value.
         *
         * This API is similar to the percent sign (%) in SQL statements.
         *
         * @param { string } field - Column name in the table.
         * @param { string } value - Value to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        endsWith(field: string, value: string): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that are **null**.
         *
         * @param { string } field - Column name in the table.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        isNull(field: string): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that are not
         * **null**.
         *
         * @param { string } field - Column name in the table.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        isNotNull(field: string): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that are similar to
         * the given value.
         *
         * This API is similar to the SQL **like** statement.
         *
         * @param { string } field - Column name in the table.
         * @param { string } value - Value to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        like(field: string, value: string): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that match the given
         * string. Different from **like**, the input parameters of this API are case-sensitive.
         *
         * @param { string } field - Column name in the table.
         * @param { string } value - Value to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        glob(field: string, value: string): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that are within the
         * given range.
         *
         * @param { string } field - Column name in the table.
         * @param { ValueType } low - Minimum value to match.
         * @param { ValueType } high - Maximum value to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        between(field: string, low: ValueType, high: ValueType): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that are out of the
         * given range.
         *
         * @param { string } field - Column name in the table.
         * @param { ValueType } low - Minimum value to match.
         * @param { ValueType } high - Maximum value to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        notBetween(field: string, low: ValueType, high: ValueType): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that are greater
         * than the given value.
         *
         * @param { string } field - Column name in the table.
         * @param { ValueType } value - Value to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        greaterThan(field: string, value: ValueType): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that are less than
         * the given value.
         *
         * @param { string } field - Column name in the table.
         * @param { ValueType } value - Value to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        lessThan(field: string, value: ValueType): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that are greater
         * than or equal to the given value.
         *
         * @param { string } field - Column name in the table.
         * @param { ValueType } value - Value to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        greaterThanOrEqualTo(field: string, value: ValueType): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that are less than
         * or equal to the given value.
         *
         * @param { string } field - Column name in the table.
         * @param { ValueType } value - Value to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        lessThanOrEqualTo(field: string, value: ValueType): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to sort the records in the specified column in ascending order. When
         * there are multiple **orderByAsc**s, the first **orderByAsc** used has the highest priority.
         *
         * @param { string } field - Column name in the table.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        orderByAsc(field: string): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to sort the records in the specified column in descending order. When
         * there are multiple **orderByDesc**s, the first **orderByDesc** used has the highest priority.
         *
         * @param { string } field - Column name in the table.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        orderByDesc(field: string): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to filter out duplicate records.
         *
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        distinct(): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to limit the number of records.
         *
         * @param { number } value - Maximum number of records. The value should be a positive integer. If a value less than
         *     or equal to **0** is specified, the number of records is not limited.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        limitAs(value: number): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to set the start position of the query result. This API must be used
         * together with **limitAs**. Otherwise, no result will be returned. To query all rows after the specified offset,
         * pass in **-1** in **limitAs**.
         *
         * @param { number } rowOffset - Start position. The value should be a positive integer. If a value less than or
         *     equal to **0** is specified, the query result is returned from the first element.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        offsetAs(rowOffset: number): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to group the query results based on the specified columns.
         *
         * @param { Array<string> } fields - Names of columns to group.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        groupBy(fields: Array<string>): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to specify the index column. Before calling this API, you need to
         * create an index column.
         *
         * @param { string } field - Name of the index.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        indexedBy(field: string): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that are in the
         * given range.
         *
         * @param { string } field - Column name in the table.
         * @param { Array<ValueType> } value - Array of **ValueType**s to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        in(field: string, value: Array<ValueType>): DataAbilityPredicates;
        /**
         * Creates a **DataAbilityPredicates** object to search for the records in the specified column that are out of the
         * given range.
         *
         * @param { string } field - Column name in the table.
         * @param { Array<ValueType> } value - Array of **ValueType**s to match.
         * @returns { DataAbilityPredicates } **DataAbilityPredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @since 7
         */
        notIn(field: string, value: Array<ValueType>): DataAbilityPredicates;
    }
    /**
     * Defines the value types.
     *
     * @unionmember { number } The value is a number.
     * @unionmember { string } The value is a string.
     * @unionmember { boolean } The value is of Boolean type.
     * @syscap SystemCapability.DistributedDataManager.DataShare.Core
     * @since 7
     */
    type ValueType = number | string | boolean;
}
export default dataAbility;

```
