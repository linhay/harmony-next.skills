# @ohos.data.dataShare.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022 Huawei Device Co., Ltd.
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
import type { AsyncCallback } from './@ohos.base';
import { ValueType } from './@ohos.data.ValuesBucket';
/**
 * The **DataShare** module allows an application to manage its own data and share data with other applications on the
 * same device.
 *
 * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
 * @stagemodelonly
 * @since 20
 */
declare namespace dataShare {
    /**
     * Enumerates the data change types.
     *
     * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
     * @stagemodelonly
     * @since 20
     */
    enum ChangeType {
        /**
         * Data is inserted.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        INSERT = 0,
        /**
         * Data is deleted.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        DELETE = 1,
        /**
         * Data is updated.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        UPDATE = 2
    }
    /**
     * Creates a **DataProxyHandle** instance. This API uses a promise to return the result.
     *
     * @returns { Promise<DataProxyHandle> } Promise used to return the result.
     * @throws { BusinessError } 15700000 - Inner error. Possible causes: The service is not ready or is being
     *     restarted abnormally.
     * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
     * @stagemodelonly
     * @since 20
     */
    function createDataProxyHandle(): Promise<DataProxyHandle>;
    /**
     * Defines a struct for shared configurations.
     *
     * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
     * @stagemodelonly
     * @since 20
     */
    interface ProxyData {
        /**
         * Unique ID of a shared configuration, fixed at the format of **"datashareproxy://{*bundleName*}/{*path*}"**, in
         * which **bundleName** indicates the bundle name of the publisher application, and **path** can be set to any value
         * but must be unique in the same application. The value is a string with a maximum of 256 bytes.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        uri: string;
        /**
         * Value of a shared configuration. If not specified, the value is an empty string. The value is a string with a
         * maximum of 4,096 bytes. If this parameter is not set when the shared configuration is published for the first
         * time, the value will be an empty string by default. If this parameter is not set when a shared configuration is
         * updated, the value of the shared configuration will not be updated.
         * In versions earlier than API version 26.0.0, the maximum length of a string is 4096 bytes. In API version 26.0.0
         * and later versions, the maximum length of a string is 4096 bytes by default, and can be extended to 102,400
         * bytes by setting the maxValueLength parameter in [DataProxyConfig]{@link dataShare.DataProxyConfig}.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        value?: ValueType;
        /**
         * List of applications that can subscribe to and read shared configurations. If this parameter is left empty, the
         * value is an empty string array. The array can contain a maximum of 256 elements. Excess elements are invalid.
         * Each element in the array is the
         * [appIdentifier](docroot://quick-start/common-problem-of-application.md#what-is-appidentifier) of an application.
         * The maximum length of an **appIdentifier** is 128 bytes. If the length exceeds 128 bytes, the **appIdentifier**
         * does not take effect. If this parameter is not set when the shared configuration is published for the first time,
         * the allowlist is empty by default. If this parameter is not set when the shared configuration is updated, the
         * allowlist will not be updated. An empty allowlist indicates that only the publisher can access the shared
         * configuration.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        allowList?: string[];
        /**
         * Indicates whether the shared configuration is multi-value type. The default value is false, indicating that the
         * shared configuration is not multi-value type. If the value is true, it indicates that the data being published is
         * multi-value type, and the [value]{@link ProxyData#value} parameter will be ignored.
         * Default value: false.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 26.0.0
         */
        isMultiValues?: boolean;
        /**
         * Values of the multi-value type. The first parameter in the **Record** is the key specified by the user, which
         * must be unique. The second parameter is the value corresponding to the key. A maximum of 10 values can be added
         * to a single URI for an application. Each value can contain a maximum of 4096 bytes. At the same time, the total
         * length of all values is limited by the [maxValueLength]{@link DataProxyConfig#maxValueLength} parameter value.
         * This parameter is valid only when [isMultiValues]{@link ProxyData#isMultiValues} is set to true.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 26.0.0
         */
        values?: Record<number, ValueType>;
        /**
         * List of applications that can add values to the shared configuration of multi-value type. The array can contain a
         * maximum of 256 elements. Excess elements are invalid.
         * Each element in the array is the
         * [appIdentifier](docroot://quick-start/common-problem-of-application.md#what-is-appidentifier) of an application.
         * The maximum length of an **appIdentifier** is 128 bytes. If the length exceeds 128 bytes, the **appIdentifier**
         * does not take effect. If this parameter is not set when the shared configuration is published for the first time,
         * the list is empty by default. If this parameter is not set when the shared configuration is updated, the
         * list will not be updated. An empty list indicates that only the publisher can add values to the shared
         * configuration.
         * The array supports the special string "all" (case-sensitive), which indicates that all applications are allowed
         * to add values to the shared configuration.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 26.0.0
         */
        trustProviders?: string[];
    }
    /**
     * Defines a struct for notifying subscribers of the shared configuration changes, including data change type, URI,
     * and content.
     *
     * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
     * @stagemodelonly
     * @since 20
     */
    interface DataProxyChangeInfo {
        /**
         * Data change type.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        type: ChangeType;
        /**
         * URI to change.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        uri: string;
        /**
         * Changed data.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        value: ValueType;
        /**
         * Changed data of the multi-value type. If the changed data is not multi-value type, the **values** is undefined.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 26.0.0
         */
        values?: ValueType[];
    }
    /**
     * Enumerates the status code returned by the batch operations of shared configuration.
     *
     * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
     * @stagemodelonly
     * @since 20
     */
    enum DataProxyErrorCode {
        /**
         * The operation is successful.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        SUCCESS = 0,
        /**
         * The URI does not exist or the URI is not subscribed to.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        URI_NOT_EXIST = 1,
        /**
         * No permission to perform this operation on the URI.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        NO_PERMISSION = 2,
        /**
         * The number of configurations published by the current application exceeds the upper limit of 32.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        OVER_LIMIT = 3
    }
    /**
     * Defines a struct for the batch operation result of shared configuration.
     *
     * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
     * @stagemodelonly
     * @since 20
     */
    interface DataProxyResult {
        /**
         * URI to be operated, with a maximum of 256 bytes. The value is fixed at the format of
         * **"datashareproxy://{*bundleName*}/{*path*}"**, in which **bundleName** indicates the bundle name of the
         * publisher application, and **path** can be set to any value but must be unique in the same application.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        uri: string;
        /**
         * Operation result code.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        result: DataProxyErrorCode;
    }
    /**
     * Defines a struct for obtaining the batch operation result of shared configuration.
     *
     * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
     * @stagemodelonly
     * @since 20
     */
    interface DataProxyGetResult {
        /**
         * URI to be operated, with a maximum of 256 bytes. The value is fixed at the format of
         * **"datashareproxy://{*bundleName*}/{*path*}"**, in which **bundleName** indicates the bundle name of the
         * publisher application, and **path** can be set to any value but must be unique in the same application.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        uri: string;
        /**
         * Operation result code.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        result: DataProxyErrorCode;
        /**
         * If the operation is successful, the value is the one set in shared configuration; otherwise, the value is
         * undefined.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        value: ValueType | undefined;
        /**
         * If the operation is successful, the allowlist is the one set in shared configuration; otherwise, the allowlist is
         * undefined. Only the publisher can obtain the allowlist. Other applications can obtain only the value.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        allowList: string[] | undefined;
    }
    /**
     * Enumerates the data proxy types.
     *
     * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
     * @stagemodelonly
     * @since 20
     */
    enum DataProxyType {
        /**
         * Inter-application shared configuration.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        SHARED_CONFIG = 0
    }
    /**
     * The maximum length of {@link ProxyData#value}, {@link DataProxyChangeInfo#value}, {@link DataProxyGetResult#value}.
     *
     * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
     * @stagemodelonly
     * @since 26.0.0
     */
    enum DataProxyMaxValueLength {
        /**
         * The maximum length of value is 4096 bytes.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 26.0.0
         */
        MAX_LENGTH_4K = 4096,
        /**
         * The maximum length of value is 102400 bytes.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 26.0.0
         */
        MAX_LENGTH_100K = 102400
    }
    /**
     * Defines a struct for the data proxy configuration.
     *
     * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
     * @stagemodelonly
     * @since 20
     */
    interface DataProxyConfig {
        /**
         * Type of the data proxy.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        type: DataProxyType;
        /**
         * Sets the maximum length of the data proxy value. The default value is MAX_LENGTH_4K, indicating that the maximum
         * value length is 4096 bytes.
         * If the length of the value that is actually transferred or obtained exceeds the maximum value length specified by
         * this parameter, the publish or get operation will fail.
         * Default value: MAX_LENGTH_4K.
         *
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 26.0.0
         */
        maxValueLength?: DataProxyMaxValueLength;
    }
    /**
     * Defines the data proxy handle, which can be used to access or manage shared configuration information. Before
     * calling an API provided by **DataProxyHandle**, you must create a **DataProxyHandle** instance using
     * [createDataProxyHandle]{@link dataShare.createDataProxyHandle}.
     *
     * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
     * @stagemodelonly
     * @since 20
     */
    interface DataProxyHandle {
        /**
         * Subscribes to the change event of the shared configuration corresponding to a specified URI. If the change event
         * is subscribed, the subscriber will receive a callback notification that carries the data change type, changed URI
         * , and changed content when the publisher modifies the configuration. This API uses an asynchronous callback to
         * return the result. This function does not support cross-user notification subscription or subscription to
         * unpublished configurations. If the permission is revoked after the subscription is successful, the subscriber
         * will not be notified consequently.
         *
         * When the publisher calls the [publish]{@link dataShare.DataProxyHandle.publish} or
         * [delete]{@link dataShare.DataProxyHandle.delete(uris: string[], config: DataProxyConfig)} API to publish or
         * delete a configuration, a notification is automatically triggered.
         *
         * @param { 'dataChange' } event - Event or callback type. The value is **dataChange**, which indicates the data
         *     change. This event is triggered when the publisher modifies the configuration.
         * @param { string[] } uris - Array of URIs to be subscribed, with a maximum of 32 URIs. The URI value is fixed at
         *     the format of **"datashareproxy://{*bundleName*}/{*path*}"**, in which **bundleName** indicates the bundle
         *     name of the publisher application, and **path** can be set to any value but must be unique in the same
         *     application. The value contains a maximum of 256 bytes.
         * @param { DataProxyConfig } config - Data proxy configuration.
         * @param { AsyncCallback<DataProxyChangeInfo[]> } callback - Callback triggered when the publisher modifies the
         *     configuration.
         * @returns { DataProxyResult[] } Batch operation result array.
         * @throws { BusinessError } 15700000 - Inner error. Possible causes: The service is not ready or is being
         *     restarted abnormally.
         * @throws { BusinessError } 15700014 - The parameter format is incorrect or the value range is invalid.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        on(event: 'dataChange', uris: string[], config: DataProxyConfig, callback: AsyncCallback<DataProxyChangeInfo[]>): DataProxyResult[];
        /**
         * Unsubscribes from the change event of the proxy data corresponding to a specified URI.
         *
         * @param { 'dataChange' } event - Event or callback type. The value is **dataChange**, which indicates the data
         *     change.
         * @param { string[] } uris - Array of URIs to be unsubscribed, with a maximum of 32 URIs. The URI value is fixed at
         *     the format of **"datashareproxy://{*bundleName*}/{*path*}"**, in which **bundleName** indicates the bundle
         *     name of the publisher application, and **path** can be set to any value but must be unique in the same
         *     application. The value contains a maximum of 256 bytes.
         * @param { DataProxyConfig } config - Data proxy configuration.
         * @param { AsyncCallback<DataProxyChangeInfo[]> } [callback] - Callback function. If the value is empty, undefined,
         *     or null, all notifications of the URIs are unsubscribed.
         * @returns { DataProxyResult[] } Batch operation result array.
         * @throws { BusinessError } 15700000 - Inner error. Possible causes: The service is not ready or is being
         *     restarted abnormally.
         * @throws { BusinessError } 15700014 - The parameter format is incorrect or the value range is invalid.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        off(event: 'dataChange', uris: string[], config: DataProxyConfig, callback?: AsyncCallback<DataProxyChangeInfo[]>): DataProxyResult[];
        /**
         * Publishes shared configuration items. This API uses a promise to return the result. After shared configuration
         * items are published, the publisher and the applications in the allowlist can access these items. If the URI to be
         * published already exists, the corresponding shared configuration item is updated. If any URI in the configuration
         * item to be published exceeds the maximum length or fails the format verification, the current publish operation
         * fails. Only the publisher can update shared configuration items. Each application supports a maximum of 32 shared
         * configurations.
         *
         * @param { ProxyData[] } data - Array of shared configuration items to be created or updated, with a maximum of 32
         *     items.
         * @param { DataProxyConfig } config - Data proxy configuration.
         * @returns { Promise<DataProxyResult[]> } Promise used to return the result array of the batch operations.
         * @throws { BusinessError } 15700000 - Inner error. Possible causes: The service is not ready or is being
         *     restarted abnormally.
         * @throws { BusinessError } 15700014 - The parameter format is incorrect or the value range is invalid.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        publish(data: ProxyData[], config: DataProxyConfig): Promise<DataProxyResult[]>;
        /**
         * Deletes the specified shared configuration items based on URIs. This API uses a promise to return the result.
         * Only the publisher is allowed to delete shared configuration items.
         *
         * @param { string[] } uris - URI array of the shared configuration items to be deleted, with a maximum of 32 URIs.
         *     The URI value is fixed at the format of **"datashareproxy://{*bundleName*}/{*path*}"**, in which
         *     **bundleName** indicates the bundle name of the publisher application, and **path** can be set to any value
         *     but must be unique in the same application. The value contains a maximum of 256 bytes.
         * @param { DataProxyConfig } config - Data proxy configuration.
         * @returns { Promise<DataProxyResult[]> } Promise used to return the result array of the batch operations.
         * @throws { BusinessError } 15700000 - Inner error. Possible causes: The service is not ready or is being
         *     restarted abnormally.
         * @throws { BusinessError } 15700014 - The parameter format is incorrect or the value range is invalid.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        delete(uris: string[], config: DataProxyConfig): Promise<DataProxyResult[]>;
        /**
         * Deletes all the data published by the publisher.
         * Only the data publisher can delete the data.
         *
         * @param { DataProxyConfig } config - Configuration of the data proxy operation.
         * @returns { Promise<DataProxyResult[]> } Promise used to return the operation result.
         * @throws { BusinessError } 15700000 - Inner error. Possible causes: The service is not ready or is
         *     being restarted abnormally.
         * @throws { BusinessError } 15700014 - The parameter format is incorrect or the value range is invalid.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 26.0.0
         */
        deleteMyPublishedData(config: DataProxyConfig): Promise<DataProxyResult[]>;
        /**
         * Obtains a specified shared configuration item based on the URI. This API uses a promise to return the result.
         * Only the publisher and applications in the allowed list can access the shared configuration item.
         *
         * @param { string[] } uris - URI array of the shared configuration items to be obtained, with a maximum of 32 URIs.
         *     The URI value is fixed at the format of **"datashareproxy://{*bundleName*}/{*path*}"**, in which
         *     **bundleName** indicates the bundle name of the publisher application, and **path** can be set to any value
         *     but must be unique in the same application. The value contains a maximum of 256 bytes.
         * @param { DataProxyConfig } config - Data proxy configuration.
         * @returns { Promise<DataProxyGetResult[]> } Promise used to return the result array of the batch operations.
         * @throws { BusinessError } 15700000 - Inner error. Possible causes: The service is not ready or is being
         *     restarted abnormally.
         * @throws { BusinessError } 15700014 - The parameter format is incorrect or the value range is invalid.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 20
         */
        get(uris: string[], config: DataProxyConfig): Promise<DataProxyGetResult[]>;
        /**
         * Puts a value into the published data. This operation can be performed only on multi-value type data. If the
         * input **key** does not exist, a new value is added. If the input **key** already exists, the value corresponding
         * to the key is updated. By default, a maximum of 10 values can be added to a single data record (that is, a URI)
         * for a single application, and the maximum length of each value is 4096 bytes. In addition, the total length of
         * all values in a single data record is limited by the value of the **maxValueLength** parameter that is specified
         * during data publishing. Note that the **maxValueLength** parameter does not take effect in this API. This API
         * uses a promise to return the result.
         *
         * @param { string } uri - Indicates the URI of the data to operate.
         * @param { number } key - The key corresponding to the added value. It is unique for the same application.
         *     <br>The value range is all integers.
         * @param { ValueType } value - The value to be put.
         * @param { DataProxyConfig } config - Configuration of the data proxy operation.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 15700000 - Inner error. Possible causes: The service is not ready or is
         *     being restarted abnormally.
         * @throws { BusinessError } 15700011 - The URI does not exist.
         * @throws { BusinessError } 15700014 - The parameter format is incorrect or the value range is invalid.
         * @throws { BusinessError } 15700015 - No permission to access the data specified by the URI.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 26.0.0
         */
        putValue(uri: string, key: number, value: ValueType, config: DataProxyConfig): Promise<void>;
        /**
         * Removes the value corresponding to the key. This operation can be performed only on multi-value type data. Only
         * values added by this application can be removed. This API uses a promise to return the result.
         *
         * @param { string } uri - Indicates the URI of the data to operate.
         * @param { number } key - The key corresponding to the added value.
         *     <br>The value range is all integers.
         * @param { DataProxyConfig } config - Configuration of the data proxy operation.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 15700000 - Inner error. Possible causes: The service is not ready or is
         *     being restarted abnormally.
         * @throws { BusinessError } 15700011 - The URI does not exist.
         * @throws { BusinessError } 15700014 - The parameter format is incorrect or the value range is invalid.
         * @throws { BusinessError } 15700015 - No permission to access the data specified by the URI.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 26.0.0
         */
        removeValue(uri: string, key: number, config: DataProxyConfig): Promise<void>;
        /**
         * Obtains all multi-value data under a specified URI. Only the publisher and the applications in the
         * [allowList]{@link dataShare.ProxyData#allowList} can obtain the data. This API uses a promise to return the
         * result.
         *
         * @param { string } uri - Indicates the URI of the data to operate.
         * @param { DataProxyConfig } config - Configuration of the data proxy operation.
         * @returns { Promise<ValueType[]> } Promise used to return an array of all values under the URI.
         * @throws { BusinessError } 15700000 - Inner error. Possible causes: The service is not ready or is
         *     being restarted abnormally.
         * @throws { BusinessError } 15700011 - The URI does not exist.
         * @throws { BusinessError } 15700014 - The parameter format is incorrect or the value range is invalid.
         * @throws { BusinessError } 15700015 - No permission to access the data specified by the URI.
         * @syscap SystemCapability.DistributedDataManager.DataShare.Consumer
         * @stagemodelonly
         * @since 26.0.0
         */
        getValues(uri: string, config: DataProxyConfig): Promise<ValueType[]>;
    }
}
export default dataShare;

```
