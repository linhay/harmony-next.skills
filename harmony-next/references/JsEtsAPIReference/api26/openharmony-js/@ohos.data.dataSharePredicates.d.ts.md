# @ohos.data.dataSharePredicates.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
import { ValueType } from './@ohos.data.ValuesBucket';
/**
 * **DataSharePredicates** provides a filter object to query data in a database by using **DataShare** APIs. It is often
 * used to update, delete, and query data.
 *
 * The APIs provided by **DataSharePredicates** correspond to the filter criteria of the database. Before using the APIs
 * , you need to have basic database knowledge.
 *
 * **DataSharePredicates** applies to the following scenario:
 *
 * - It is used as a search criterion in the media file management service. For details, see
 * [FetchOptions]{@link @ohos.file.photoAccessHelper:photoAccessHelper.FetchOptions} in the fetch options of the album
 * management. In this scenario, you do not need to pay attention to the database type.
 *
 * <!--Del-->
 *
 * - It is used as a search criterion when APIs of the
 * [RDB store](docroot://apis-arkdata/js-apis-data-relationalStore-sys.md) and
 * [KV store](docroot://apis-arkdata/js-apis-distributedKVStore-sys.md) are called. In this scenario, use the
 * corresponding predicate based on the database type.
 *
 * <!--DelEnd-->
 *
 * @syscap SystemCapability.DistributedDataManager.DataShare.Core
 * @StageModelOnly
 * @crossplatform [since 12]
 * @atomicservice [since 20]
 * @since 10
 */
declare namespace dataSharePredicates {
    /**
     * Provides APIs for setting different **DataSharePredicates** objects. This type is not multi-thread safe. If a
     * **DataSharePredicates** instance is operated by multiple threads at the same time in an application, use a lock for
     * it.
     *
     * @syscap SystemCapability.DistributedDataManager.DataShare.Core
     * @StageModelOnly
     * @crossplatform [since 12]
     * @atomicservice [since 20]
     * @since 10
     */
    class DataSharePredicates {
        /**
         * Creates a **DataSharePredicates** object to search for the records in the specified column that are equal to the
         * given value.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @param { string } field - Column name in the database table.If this parameter is set to **undefined** or
         *     **null**, the predicate used is invalid.
         * @param { ValueType } value - Value to match.If this parameter is set to **undefined** or **null**, the
         *     predicate used is invalid.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        equalTo(field: string, value: ValueType): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object to match the data that is not equal to the specified value.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @param { string } field - Column name in the database table.If this parameter is set to **undefined** or
         *     **null**, the predicate used is invalid.If this parameter is set to **'null'** or **'undefined'** in
         *     string, the matching result may not be as expected or an exception may be thrown when the predicate is used
         *     by the KV store and RDB store APIs.
         * @param { ValueType } value - Value to match.If this parameter is set to **undefined** or **null**, the
         *     predicate used is invalid.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @since 23
         */
        notEqualTo(field: string, value: ValueType): DataSharePredicates;
        /**
         * Adds a left parenthesis to this **DataSharePredicates**. This API is similar to "(" in an SQL statement and must
         * be used with the right parenthesis.
         *
         * Currently, only RDB store supports this predicate.
         *
         * @returns { DataSharePredicates } **DataSharePredicates** object with a left parenthesis.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @since 23
         */
        beginWrap(): DataSharePredicates;
        /**
         * Adds a right parenthesis to this **DataSharePredicates**. This API is similar to ")" in an SQL statement and must
         * be used with the left parenthesis.
         *
         * Currently, only RDB store supports this predicate.
         *
         * @returns { DataSharePredicates } **DataSharePredicates** object with a right parenthesis.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @since 23
         */
        endWrap(): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object to add the OR condition.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @returns { DataSharePredicates } **DataSharePredicates** object with the OR operator.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @since 23
         */
        or(): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object to add the AND condition.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @returns { DataSharePredicates } **DataSharePredicates** object with the AND operator.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        and(): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object to match the data that matches the specified wildcard expression.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @param { string } field - Column name in the database table.If this parameter is set to **undefined** or
         *     **null**, the predicate used is invalid.If this parameter is set to **'null'** or **'undefined'** in
         *     string, the matching result may not be as expected or an exception may be thrown when the predicate is used
         *     by the KV store and RDB store APIs.
         * @param { string } value - Wildcard expression to match.In the expression, '%' represents zero, one, or more
         *     digits or characters, and '_' represents a single digit or character. It is case insensitive.If this
         *     parameter is set to **undefined** or **null**, the predicate used is invalid.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @since 23
         */
        like(field: string, value: string): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object to match the data that is within the specified range, including the
         * start and end values.
         *
         * Currently, only RDB store supports this predicate.
         *
         * @param { string } field - Column name in the database table.If this parameter is set to **undefined** or
         *     **null**, the predicate used is invalid.If this parameter is set to **'null'** or **'undefined'** in
         *     string, the matching result may not be as expected or an exception may be thrown when the predicate is used
         *     by the KV store and RDB store APIs.
         * @param { ValueType } low - Minimum value of the range to set.If **low** is set to a number, the matching
         *     range is specified based on the numeric order.If **low** is set to a string, the matching range is
         *     specified based on the lexicographical order.If **low** is set to boolean, the matching range is
         *     specified based on the numeric order.
         * @param { ValueType } high - Maximum value to match the **DataAbilityPredicates**.If **high** is set to a
         *     number, the matching range is specified based on the numeric order.If **high** is set to a string, the
         *     matching range is specified based on the lexicographical order.If **high** is set to boolean, the
         *     matching range is specified based on the numeric order.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @since 23
         */
        between(field: string, low: ValueType, high: ValueType): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object to match the data that is out of the specified range, excluding the
         * start and end values.
         *
         * Currently, only RDB store supports this predicate.
         *
         * @param { string } field - Column name in the database table.If this parameter is set to **undefined** or
         *     **null**, the predicate used is invalid.If this parameter is set to **'null'** or **'undefined'** in
         *     string, the matching result may not be as expected or an exception may be thrown when the predicate is used
         *     by the KV store and RDB store APIs.
         * @param { ValueType } low - Minimum value of the range to set.If **low** is set to a number, the matching
         *     range is specified based on the numeric order.If **low** is set to a string, the matching range is
         *     specified based on the lexicographical order.If **low** is set to boolean, the matching range is
         *     specified based on the numeric order.
         * @param { ValueType } high - Maximum value to match the **DataAbilityPredicates**.If **high** is set to a
         *     number, the matching range is specified based on the numeric order.If **high** is set to a string, the
         *     matching range is specified based on the lexicographical order.If **high** is set to boolean, the
         *     matching range is specified based on the numeric order.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @since 23
         */
        notBetween(field: string, low: ValueType, high: ValueType): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object to match the data that is greater than the specified value.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @param { string } field - Column name in the database table.If this parameter is set to **undefined** or
         *     **null**, the predicate used is invalid.If this parameter is set to **'null'** or **'undefined'** in
         *     string, the matching result may not be as expected or an exception may be thrown when the predicate is used
         *     by the KV store and RDB store APIs.
         * @param { ValueType } value - Value to match.If this parameter is set to **undefined** or **null**, the
         *     predicate used is invalid.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @since 23
         */
        greaterThan(field: string, value: ValueType): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object to match the data that is less than the specified value.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @param { string } field - Column name in the database table.If field is null or undefined, the predicate
         *     configured by calling this API is invalid.If this parameter is set to **'null'** or **'undefined'** in
         *     string, the matching result may not be as expected or an exception may be thrown when the predicate is used
         *     by the KV store and RDB store APIs.
         * @param { ValueType } value - Value to match.If this parameter is set to **undefined** or **null**, the
         *     predicate used is invalid.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @since 23
         */
        lessThan(field: string, value: ValueType): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object to match the data that is greater than or equal to the specified value.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @param { string } field - Column name in the database table.If this parameter is set to **undefined** or
         *     **null**, the predicate used is invalid.If this parameter is set to **'null'** or **'undefined'** in
         *     string, the matching result may not be as expected or an exception may be thrown.
         * @param { ValueType } value - Value to match.If this parameter is set to **undefined** or **null**, the
         *     predicate used is invalid.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @since 23
         */
        greaterThanOrEqualTo(field: string, value: ValueType): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object to match the data that is less than or equal to the specified value.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @param { string } field - Column name in the database table.If this parameter is set to **undefined** or
         *     **null**, the predicate used is invalid.If this parameter is set to **'null'** or **'undefined'** in
         *     string, the matching result may not be as expected or an exception may be thrown when the predicate is used
         *     by the KV store and RDB store APIs.
         * @param { ValueType } value - Value to match.If this parameter is set to **undefined** or **null**, the
         *     predicate used is invalid.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @since 23
         */
        lessThanOrEqualTo(field: string, value: ValueType): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object that sorts records in ascending order.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @param { string } field - Column name in the database table.If this parameter is set to **undefined** or
         *     **null**, the predicate used is invalid.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        orderByAsc(field: string): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object that sorts data in descending order.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @param { string } field - Column name in the database table.If this parameter is set to **undefined** or
         *     **null**, the predicate used is invalid.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        orderByDesc(field: string): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object to specify the number of records in the result and the start position.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @param { number } total - Maximum number of records.If the KV store is used and **total** is **undefined** or
         *     **null**, the maximum number of records is 0. For details about the value range, see the description of this
         *     parameter in [limit]{@link @ohos.data.distributedKVStore:distributedKVStore.Query.limit}.If the RDB store
         *     is used and **total** is **undefined** or **null**, the maximum number of records is not limited. For details
         *     about the value range, see the description of this parameter in
         *     [limitAs]{@link @ohos.data.distributedKVStore:distributedKVStore.Query.limit}.
         * @param { number } offset - Start position of the query result.If this parameter is set to **undefined** or
         *     **null**, the start position is the beginning of the result set.For details about the value range in a KV
         *     store, see the description of this parameter in
         *     [limit]{@link @ohos.data.distributedKVStore:distributedKVStore.Query.limit}.For details about the value
         *     range in an RDB store, see the description of the **rowOffset** parameter in
         *     [offsetAs]{@link @ohos.data.relationalStore:relationalStore.RdbPredicates.offsetAs}.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        limit(total: number, offset: number): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object to match the data that is within the specified range.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @param { string } field - Column name in the database table.If this parameter is set to **undefined** or
         *     **null**, the predicate used is invalid.
         * @param { Array<ValueType> } value - Array of the values to match.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        in(field: string, value: Array<ValueType>): DataSharePredicates;
        /**
         * Creates a **DataSharePredicates** object to match the data that is not in the specified value.
         *
         * Currently, both the RDB store and KV store support this predicate.
         *
         * @param { string } field - Column name in the database table.If this parameter is set to **undefined** or
         *     **null**, the predicate used is invalid.If this parameter is set to **'null'** or **'undefined'** in
         *     string, the matching result may not be as expected or an exception may be thrown when the predicate is used
         *     by the KV store and RDB store APIs.
         * @param { Array<ValueType> } value - Array of the values to match.If this parameter is set to **undefined** or
         *     **null**, the predicate used is invalid.
         * @returns { DataSharePredicates } **DataSharePredicates** object created.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Core
         * @StageModelOnly
         * @since 23
         */
        notIn(field: string, value: Array<ValueType>): DataSharePredicates;
    }
}
export default dataSharePredicates;

```
