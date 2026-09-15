# @ohos.security.asset.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
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
 * @kit AssetStoreKit
 */
/**
 * This module provides the capabilities for life cycle management of sensitive user data (Asset) such as passwords
 * and tokens, including adding, removing, updating, and querying.
 *
 * @syscap SystemCapability.Security.Asset
 * @atomicservice [since 14]
 * @since 11
 */
declare namespace asset {
    /**
     * Adds an asset. This API uses a promise to return the result.
     *
     * To set {@link Tag.IS_PERSISTENT}, the application must have the ohos.permission.STORE_PERSISTENT_DATA permission.
     *
     * @param { AssetMap } attributes - Attributes of the asset to add, including the asset plaintext,
     *     access control attributes, and custom data.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - The caller doesn't have the permission.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     *     3. Parameter verification failed.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000003 - The asset already exists.
     * @throws { BusinessError } 24000005 - The screen lock status does not match.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000007 - The asset is corrupted.
     * @throws { BusinessError } 24000008 - The database operation failed.
     * @throws { BusinessError } 24000009 - The cryptography operation failed.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000014 - The file operation failed.
     * @throws { BusinessError } 24000015 - Getting the system time failed.
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    function add(attributes: AssetMap): Promise<void>;
    /**
     * Adds assets in batches based on an attributes array.
     * To set {@link Tag.IS_PERSISTENT}, the application must have the ohos.permission.STORE_PERSISTENT_DATA permission.
     *
     * Only assets with the same {@link Tag.GROUP_ID} and {@link Tag.REQUIRE_ATTR_ENCRYPTED} can be added in batches.
     *
     * @param { Array<AssetMap> } attributesArray - an array of assets to be added.
     * @returns { Promise<BatchResult> } The result of the batch operation, including error information for adding
     *     failed assets, if there are any failures.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000005 - The screen lock status does not match.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000007 - The asset is corrupted.
     * @throws { BusinessError } 24000008 - The database operation failed.
     * @throws { BusinessError } 24000009 - The cryptography operation failed.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000014 - The file operation failed.
     * @throws { BusinessError } 24000015 - Getting the system time failed.
     * @throws { BusinessError } 24000019 - Each value of {@link Tag.GROUP_ID} and {@link Tag.REQUIRE_ATTR_ENCRYPTED}
     *     in the array is not consistent.
     * @syscap SystemCapability.Security.Asset
     * @FaAndStageModel
     * @since 26.0.0
     */
    function batchAdd(attributesArray: Array<AssetMap>): Promise<BatchResult>;
    /**
     * Adds an asset. This API returns the result synchronously.
     *
     * To set {@link Tag.IS_PERSISTENT}, the application must have the ohos.permission.STORE_PERSISTENT_DATA permission.
     *
     * @param { AssetMap } attributes - Attributes of the asset to add, including the asset plaintext,
     *     access control attributes, and custom data.
     * @throws { BusinessError } 201 - The caller doesn't have the permission.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     *     3. Parameter verification failed.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000003 - The asset already exists.
     * @throws { BusinessError } 24000005 - The screen lock status does not match.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000007 - The asset is corrupted.
     * @throws { BusinessError } 24000008 - The database operation failed.
     * @throws { BusinessError } 24000009 - The cryptography operation failed.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000014 - The file operation failed.
     * @throws { BusinessError } 24000015 - Getting the system time failed.
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 12
     */
    function addSync(attributes: AssetMap): void;
    /**
     * Removes one or more assets. This API uses a promise to return the result.
     *
     * @param { AssetMap } query - Attributes of the asset to remove, such as the asset alias, access control attributes,
     *     and custom data.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Incorrect parameter types.
     *     2. Parameter verification failed.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000002 - The asset is not found.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000007 - The asset is corrupted.
     * @throws { BusinessError } 24000008 - The database operation failed.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000015 - Getting the system time failed.
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    function remove(query: AssetMap): Promise<void>;
    /**
     * Removes assets in batches based on an alias list.
     *
     * Only assets with the same {@link Tag.GROUP_ID} and {@link Tag.REQUIRE_ATTR_ENCRYPTED} can be removed in batches.
     *
     * @param { Array<AssetMap> } assetsToBeRemoved - an array of attributes of the asset to remove,
     *     such as the asset alias, access control attributes, and custom data.
     *     <br>The {@link Tag.GROUP_ID} and {@link Tag.REQUIRE_ATTR_ENCRYPTED} attributes of all data must be the same.
     * @returns { Promise<void> } the promise object returned by the function.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000007 - The asset is corrupted.
     * @throws { BusinessError } 24000008 - The database operation failed.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000015 - Getting the system time failed.
     * @throws { BusinessError } 24000019 - Each value of {@link Tag.GROUP_ID} and {@link Tag.REQUIRE_ATTR_ENCRYPTED}
     *     in the array is not consistent.
     * @syscap SystemCapability.Security.Asset
     * @FaAndStageModel
     * @since 26.0.0
     */
    function batchRemove(assetsToBeRemoved: Array<AssetMap>): Promise<void>;
    /**
     * Removes one or more assets. This API returns the result synchronously.
     *
     * @param { AssetMap } query - Attributes of the asset to remove, such as the asset alias, access control attributes,
     *     and custom data.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Incorrect parameter types.
     *     2. Parameter verification failed.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000002 - The asset is not found.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000007 - The asset is corrupted.
     * @throws { BusinessError } 24000008 - The database operation failed.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000015 - Getting the system time failed.
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 12
     */
    function removeSync(query: AssetMap): void;
    /**
     * Updates an asset. This API uses a promise to return the result.
     *
     * @param { AssetMap } query - Attributes of the asset to update, such as the asset alias, access control attributes,
     *     and custom data.
     * @param { AssetMap } attributesToUpdate - New attributes of the asset, such as the asset plaintext and custom data.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     *     3. Parameter verification failed.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000002 - The asset is not found.
     * @throws { BusinessError } 24000005 - The screen lock status does not match.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000007 - The asset is corrupted.
     * @throws { BusinessError } 24000008 - The database operation failed.
     * @throws { BusinessError } 24000009 - The cryptography operation failed.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000015 - Getting the system time failed.
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    function update(query: AssetMap, attributesToUpdate: AssetMap): Promise<void>;
    /**
     * Updates assets in batches based on an attributes array.
     *
     * Only assets with the same {@link Tag.GROUP_ID} and {@link Tag.REQUIRE_ATTR_ENCRYPTED} can be updated in batches.
     *
     * @param { Array<AssetMap> } sourceAttributes - an array of map objects containing asset attributes to query.
     *     <br>The {@link Tag.GROUP_ID} and {@link Tag.REQUIRE_ATTR_ENCRYPTED} attributes of all assets must be the same.
     * @param { Array<AssetMap> } destAttributes - an array of map objects containing asset attributes to be updated.
     *     <br>The {@link Tag.GROUP_ID} and {@link Tag.REQUIRE_ATTR_ENCRYPTED} attributes of all assets must be the same.
     * @returns { Promise<BatchResult> } the promise object returned by the function.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000007 - The asset is corrupted.
     * @throws { BusinessError } 24000008 - The database operation failed.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000015 - Getting the system time failed.
     * @throws { BusinessError } 24000019 - Each value of {@link Tag.GROUP_ID} and {@link Tag.REQUIRE_ATTR_ENCRYPTED}
     *     in the array is not consistent.
     * @syscap SystemCapability.Security.Asset
     * @FaAndStageModel
     * @since 26.0.0
     */
    function batchUpdate(sourceAttributes: Array<AssetMap>, destAttributes: Array<AssetMap>): Promise<BatchResult>;
    /**
     * Updates an asset. This API returns the result synchronously.
     *
     * @param { AssetMap } query - Attributes of the asset to update, such as the asset alias, access control attributes,
     *     and custom data.
     * @param { AssetMap } attributesToUpdate - New attributes of the asset, such as the asset plaintext and custom data.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     *     3. Parameter verification failed.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000002 - The asset is not found.
     * @throws { BusinessError } 24000005 - The screen lock status does not match.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000007 - The asset is corrupted.
     * @throws { BusinessError } 24000008 - The database operation failed.
     * @throws { BusinessError } 24000009 - The cryptography operation failed.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000015 - Getting the system time failed.
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 12
     */
    function updateSync(query: AssetMap, attributesToUpdate: AssetMap): void;
    /**
     * Performs preprocessing for the asset query. This API is used when user authentication is required for the access to
     * the asset. After the user authentication is successful, call [asset.query]{@link asset.query} and
     * [asset.postQuery]{@link asset.postQuery}. This API uses a promise to return the result.
     *
     * @param { AssetMap } query - Attributes of the asset to query, such as the asset alias, access control attributes,
     *     and custom data.
     * @returns { Promise<Uint8Array> } Promise used to return a challenge value.
     *     <br>**Note**: The challenge value is used for subsequent user authentication.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Incorrect parameter types.
     *     2. Parameter verification failed.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000002 - The asset is not found.
     * @throws { BusinessError } 24000005 - The screen lock status does not match.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000007 - The asset is corrupted.
     * @throws { BusinessError } 24000008 - The database operation failed.
     * @throws { BusinessError } 24000009 - The cryptography operation failed.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000016 - The cache exceeds the limit.
     * @throws { BusinessError } 24000017 - The capability is not supported.
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    function preQuery(query: AssetMap): Promise<Uint8Array>;
    /**
     * Performs preprocessing for the asset query. This API is used when user authentication is required for the access to
     * the asset. After the user authentication is successful, call [asset.querySync]{@link asset.querySync} and
     * [asset.postQuerySync]{@link asset.postQuerySync}. This API returns the result synchronously.
     *
     * @param { AssetMap } query - Attributes of the asset to query, such as the asset alias, access control attributes,
     *     and custom data.
     * @returns { Uint8Array } Challenge value.
     *     <br>**Note**: The challenge value is used for subsequent user authentication.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Incorrect parameter types.
     *     2. Parameter verification failed.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000002 - The asset is not found.
     * @throws { BusinessError } 24000005 - The screen lock status does not match.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000007 - The asset is corrupted.
     * @throws { BusinessError } 24000008 - The database operation failed.
     * @throws { BusinessError } 24000009 - The cryptography operation failed.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000016 - The cache exceeds the limit.
     * @throws { BusinessError } 24000017 - The capability is not supported.
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 12
     */
    function preQuerySync(query: AssetMap): Uint8Array;
    /**
     * Queries one or more assets. If user authentication is required for the access to the asset,
     * call [asset.preQuery]{@link asset.preQuery} before this API and call [asset.postQuery]{@link asset.postQuery}
     * after this API. For details about the development procedure, see
     * [Development Guidance](docroot://security/AssetStoreKit/asset-js-query-auth.md).
     * This API uses a promise to return the result.
     *
     * If no asset is found, an exception indicating that no asset is found is thrown instead of returning
     * an empty query result list.
     *
     * @param { AssetMap } query - Attributes of the asset to query, such as the asset alias, access control attributes,
     *     and custom data.
     * @returns { Promise<Array<AssetMap>> } Promise used to return the result obtained.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Incorrect parameter types.
     *     2. Parameter verification failed.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000002 - The asset is not found.
     * @throws { BusinessError } 24000004 - Access denied.
     * @throws { BusinessError } 24000005 - The screen lock status does not match.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000007 - The asset is corrupted.
     * @throws { BusinessError } 24000008 - The database operation failed.
     * @throws { BusinessError } 24000009 - The cryptography operation failed.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000017 - The capability is not supported.
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    function query(query: AssetMap): Promise<Array<AssetMap>>;
    /**
     * Queries one or more assets. If user authentication is required for the access to the asset, call
     * [asset.preQuerySync]{@link asset.preQuerySync} before this API and call
     * [asset.postQuerySync]{@link asset.postQuerySync} after this API. For details about the development procedure, see
     * [Development Guidance](docroot://security/AssetStoreKit/asset-js-query-auth.md).
     * This API returns the result synchronously.
     *
     * If no asset is found, an exception indicating that no asset is found is thrown instead of returning
     * an empty query result list.
     *
     * @param { AssetMap } query - Attributes of the asset to query, such as the asset alias, access control attributes,
     *     and custom data.
     * @returns { Array<AssetMap> } Array of query results.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Incorrect parameter types.
     *     2. Parameter verification failed.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000002 - The asset is not found.
     * @throws { BusinessError } 24000004 - Access denied.
     * @throws { BusinessError } 24000005 - The screen lock status does not match.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000007 - The asset is corrupted.
     * @throws { BusinessError } 24000008 - The database operation failed.
     * @throws { BusinessError } 24000009 - The cryptography operation failed.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000017 - The capability is not supported.
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 12
     */
    function querySync(query: AssetMap): Array<AssetMap>;
    /**
     * Performs postprocessing for the asset query. This API is used when user authentication is required for the access
     * to an asset. This API must be used with [asset.preQuery]{@link asset.preQuery} together.
     * This API uses a promise to return the result.
     *
     * @param { AssetMap } handle - Handle of the query operation, including the challenge value returned by
     *     [asset.preQuery]{@link asset.preQuery}.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     *     3. Parameter verification failed.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    function postQuery(handle: AssetMap): Promise<void>;
    /**
     * Performs postprocessing for the asset query. This API is used when user authentication is required for the access
     * to the asset. This API must be used with [asset.preQuerySync]{@link asset.preQuerySync} together.
     * This API returns the result synchronously.
     *
     * @param { AssetMap } handle - Handle of the query operation, including the challenge value returned by
     *     [asset.preQuerySync]{@link asset.preQuerySync}.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     *     3. Parameter verification failed.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 12
     */
    function postQuerySync(handle: AssetMap): void;
    /**
     * Queries the result of the sync operation. This API uses a promise to return the result.
     *
     * @param { AssetMap } query - Attributes of the sync result to query, such as the group to which the asset belongs
     *     and whether the custom attribute information is encrypted.
     * @returns { Promise<SyncResult> } Promise used to return the result obtained.
     * @throws { BusinessError } 24000001 - The ASSET service is unavailable.
     * @throws { BusinessError } 24000006 - Insufficient memory.
     * @throws { BusinessError } 24000010 - IPC failed.
     * @throws { BusinessError } 24000011 - Calling the Bundle Manager service failed.
     * @throws { BusinessError } 24000012 - Calling the OS Account service failed.
     * @throws { BusinessError } 24000013 - Calling the Access Token service failed.
     * @throws { BusinessError } 24000014 - The file operation failed.
     * @throws { BusinessError } 24000018 - Parameter verification failed.
     * @syscap SystemCapability.Security.Asset
     * @since 20
     */
    function querySyncResult(query: AssetMap): Promise<SyncResult>;
    /**
     * Represents a set of asset attributes in the form of KV pairs.
     *
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    type AssetMap = Map<Tag, Value>;
    /**
     * Represents the value of each attribute in [AssetMap]{@link asset.AssetMap}.
     *
     * @unionmember { boolean } The value is a boolean value, with a range of true or false.
     * @unionmember { number } The value is a number, and the value range is the enumerated value or number
     *     corresponding to the tag.
     * @unionmember { Uint8Array } The value is a byte array, and the content is defined by the service.
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    declare type Value = boolean | number | Uint8Array;
    /**
     * Enumerates the types of access control based on the lock screen status.
     *
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    enum Accessibility {
        /**
         * The asset can be accessed after the device is powered on.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DEVICE_POWERED_ON = 0,
        /**
         * The asset can be accessed only after the device is unlocked for the first time.
         *
         * **Note**: If no lock screen password is set, this option is equivalent to **DEVICE_POWERED_ON**.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DEVICE_FIRST_UNLOCKED = 1,
        /**
         * The asset can be accessed only when the device is unlocked.
         *
         * **Note**: If no lock screen password is set, this option is equivalent to **DEVICE_POWERED_ON**.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DEVICE_UNLOCKED = 2
    }
    /**
     * Enumerates the types of user authentication supported by an asset.
     *
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    enum AuthType {
        /**
         * No user authentication is required before the asset is accessed.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        NONE = 0x00,
        /**
         * The asset can be accessed if any user authentication (such as PIN, facial, or fingerprint authentication) is
         * successful.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        ANY = 0xFF
    }
    /**
     * Enumerates the sync types supported by an asset.
     *
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    enum SyncType {
        /**
         * Asset sync is not allowed.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        NEVER = 0,
        /**
         * Asset sync is allowed only on the local device, for example, in data restore on the local device.
         *
         * **Note**: This field is reserved for future use and is not supported currently.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        THIS_DEVICE = 1 << 0,
        /**
         * Asset sync is allowed only between trusted devices, for example, in the case of cloning.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        TRUSTED_DEVICE = 1 << 1,
        /**
         * Asset sync is allowed only between the devices that are logged in with trusted accounts, for example,
         * in cloud sync scenarios.
         *
         * **Note**: This field is reserved for future use and is not supported currently.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 12
         */
        TRUSTED_ACCOUNT = 1 << 2
    }
    /**
     * Enumerates the encrypted import/export types supported by the asset.
     *
     * @syscap SystemCapability.Security.Asset
     * @since 18
     */
    enum WrapType {
        /**
         * Encrypted import/export is not allowed for the asset.
         *
         * @syscap SystemCapability.Security.Asset
         * @since 18
         */
        NEVER = 0,
        /**
         * Encrypted import/export is allowed for the asset only on devices where a trusted account is logged in.
         *
         * @syscap SystemCapability.Security.Asset
         * @since 18
         */
        TRUSTED_ACCOUNT = 1
    }
    /**
     * Enumerates the policies for resolving conflicts (for example, a duplicate alias) when an asset is added.
     *
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    enum ConflictResolution {
        /**
         * Overwrites the original asset.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        OVERWRITE = 0,
        /**
         * Throws an exception for the service to perform subsequent processing.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        THROW_ERROR = 1
    }
    /**
     * Enumerates the type of information returned by an asset query operation.
     *
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    enum ReturnType {
        /**
         * The query result contains the asset in plaintext and its attributes.
         *
         * **Note**: Use this option when you need to query the plaintext of a single asset.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        ALL = 0,
        /**
         * The query result contains only the asset attributes.
         *
         * **Note**: Use this option when you need to query attributes of multiple assets.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        ATTRIBUTES = 1
    }
    /**
     * Enumerates the types of additional operation to perform.
     *
     * @syscap SystemCapability.Security.Asset
     * @since 12
     */
    enum OperationType {
        /**
         * Sync.
         *
         * @syscap SystemCapability.Security.Asset
         * @since 12
         */
        NEED_SYNC = 0,
        /**
         * Logout.
         *
         * @syscap SystemCapability.Security.Asset
         * @since 12
         */
        NEED_LOGOUT = 1
    }
    /**
     * Result object containing error information with a specific index, error code, and message for a single asset.
     *
     * @syscap SystemCapability.Security.Asset
     * @FaAndStageModel
     * @since 26.0.0
     */
    interface BatchErrInfo {
        /**
         * The index in the source assets array.
         *
         * @syscap SystemCapability.Security.Asset
         * @FaAndStageModel
         * @since 26.0.0
         */
        index: number;
        /**
         * The error code of the batch operation.
         *
         * @syscap SystemCapability.Security.Asset
         * @FaAndStageModel
         * @since 26.0.0
         */
        errCode: number;
        /**
         * The error message of the batch operation.
         *
         * @syscap SystemCapability.Security.Asset
         * @FaAndStageModel
         * @since 26.0.0
         */
        message: string;
    }
    /**
     * Result object containing batch operation,including {@link batchAdd},{@link batchUpdate},{@link batchRemove}.
     *
     * @syscap SystemCapability.Security.Asset
     * @FaAndStageModel
     * @since 26.0.0
     */
    interface BatchResult {
        /**
         * Failed count of the batch operation, 0 means all success.
         *
         * @syscap SystemCapability.Security.Asset
         * @FaAndStageModel
         * @since 26.0.0
         */
        failedCount: number;
        /**
         * An array of error details for assets that failed in the batch operation,
         * including {@link BatchResult#failedCount} items, which is an empty array if all succeed.
         *
         * @syscap SystemCapability.Security.Asset
         * @FaAndStageModel
         * @since 26.0.0
         */
        failedErrorInfos: Array<BatchErrInfo>;
    }
    /**
     * Represents the sync result of an asset.
     *
     * @syscap SystemCapability.Security.Asset
     * @since 20
     */
    interface SyncResult {
        /**
         * Sync result code of an asset. If the sync is successful, the result code is **0**. If the sync fails, see
         * [ErrorCode]{@link asset.ErrorCode} for the result code.
         *
         * @syscap SystemCapability.Security.Asset
         * @since 20
         */
        readonly resultCode: number;
        /**
         * Total number of assets to be synced.
         *
         * @syscap SystemCapability.Security.Asset
         * @since 20
         */
        readonly totalCount?: number;
        /**
         * Number of assets that fail to be synced.
         *
         * @syscap SystemCapability.Security.Asset
         * @since 20
         */
        readonly failedCount?: number;
    }
    /**
     * Enumerates the asset attribute types.
     *
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    enum TagType {
        /**
         * Boolean.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        BOOL = 0x01 << 28,
        /**
         * Number.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        NUMBER = 0x02 << 28,
        /**
         * Byte array.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        BYTES = 0x03 << 28
    }
    /**
     * Enumerate the keys of asset attributes ([AssetMap]{@link asset.AssetMap}), which are in key-value (KV) pairs.
     *
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    enum Tag {
        /**
         * Asset plaintext.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        SECRET = TagType.BYTES | 0x01,
        /**
         * Asset alias, which uniquely identifies an asset.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        ALIAS = TagType.BYTES | 0x02,
        /**
         * Access control based on the lock screen status.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        ACCESSIBILITY = TagType.NUMBER | 0x03,
        /**
         * Whether the asset is accessible only when a lock screen password is set.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        REQUIRE_PASSWORD_SET = TagType.BOOL | 0x04,
        /**
         * Type of user authentication required for accessing the asset.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        AUTH_TYPE = TagType.NUMBER | 0x05,
        /**
         * Validity period of the user authentication.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        AUTH_VALIDITY_PERIOD = TagType.NUMBER | 0x06,
        /**
         * Challenge for the user authentication.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        AUTH_CHALLENGE = TagType.BYTES | 0x07,
        /**
         * Authorization token obtained after the user authentication is successful.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        AUTH_TOKEN = TagType.BYTES | 0x08,
        /**
         * Asset sync type.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        SYNC_TYPE = TagType.NUMBER | 0x10,
        /**
         * Whether to retain the asset when the application is uninstalled.
         *
         * @syscap SystemCapability.Security.Asset
         * @since 11
         */
        IS_PERSISTENT = TagType.BOOL | 0x11,
        /**
         * Additional asset data customized by the service with integrity protection.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DATA_LABEL_CRITICAL_1 = TagType.BYTES | 0x20,
        /**
         * Additional asset data customized by the service with integrity protection.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DATA_LABEL_CRITICAL_2 = TagType.BYTES | 0x21,
        /**
         * Additional asset data customized by the service with integrity protection.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DATA_LABEL_CRITICAL_3 = TagType.BYTES | 0x22,
        /**
         * Additional asset data customized by the service with integrity protection.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DATA_LABEL_CRITICAL_4 = TagType.BYTES | 0x23,
        /**
         * Additional asset data customized by the service without integrity protection.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DATA_LABEL_NORMAL_1 = TagType.BYTES | 0x30,
        /**
         * Additional asset data customized by the service without integrity protection.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DATA_LABEL_NORMAL_2 = TagType.BYTES | 0x31,
        /**
         * Additional asset data customized by the service without integrity protection.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DATA_LABEL_NORMAL_3 = TagType.BYTES | 0x32,
        /**
         * Additional asset data customized by the service without integrity protection.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DATA_LABEL_NORMAL_4 = TagType.BYTES | 0x33,
        /**
         * Local information about the asset. The value is assigned by the service without integrity protection and
         * will not be synced.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 12
         */
        DATA_LABEL_NORMAL_LOCAL_1 = TagType.BYTES | 0x34,
        /**
         * Local information about the asset. The value is assigned by the service without integrity protection and
         * will not be synced.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 12
         */
        DATA_LABEL_NORMAL_LOCAL_2 = TagType.BYTES | 0x35,
        /**
         * Local information about the asset. The value is assigned by the service without integrity protection and
         * will not be synced.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 12
         */
        DATA_LABEL_NORMAL_LOCAL_3 = TagType.BYTES | 0x36,
        /**
         * Local information about the asset. The value is assigned by the service without integrity protection and
         * will not be synced.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 12
         */
        DATA_LABEL_NORMAL_LOCAL_4 = TagType.BYTES | 0x37,
        /**
         * Type of the asset query result to return.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        RETURN_TYPE = TagType.NUMBER | 0x40,
        /**
         * Maximum number of asset records to return.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        RETURN_LIMIT = TagType.NUMBER | 0x41,
        /**
         * Offset of the asset query result.
         *
         * **Note**: This parameter specifies the starting asset record to return in batch asset query.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        RETURN_OFFSET = TagType.NUMBER | 0x42,
        /**
         * Sorting order of the query results. Currently, the results can be sorted only by **ASSET_TAG_DATA_LABEL**.
         *
         * **Note**: By default, assets are returned in the order in which they are added.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        RETURN_ORDERED_BY = TagType.NUMBER | 0x43,
        /**
         * Policy for resolving the conflict (for example, a duplicate alias).
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        CONFLICT_RESOLUTION = TagType.NUMBER | 0x44,
        /**
         * Data update time, in timestamp.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 12
         */
        UPDATE_TIME = TagType.BYTES | 0x45,
        /**
         * Additional operation type.
         *
         * @syscap SystemCapability.Security.Asset
         * @since 12
         */
        OPERATION_TYPE = TagType.NUMBER | 0x46,
        /**
         * Whether to encrypt the additional asset information customized by the service.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice
         * @since 14
         */
        REQUIRE_ATTR_ENCRYPTED = TagType.BOOL | 0x47,
        /**
         * Group to which the asset belongs.
         *
         * @syscap SystemCapability.Security.Asset
         * @since 18
         */
        GROUP_ID = TagType.BYTES | 0x48,
        /**
         * Encrypted import/export type supported by the asset.
         *
         * @syscap SystemCapability.Security.Asset
         * @since 18
         */
        WRAP_TYPE = TagType.NUMBER | 0x49
    }
    /**
     * Enumerates the error codes.
     *
     * @syscap SystemCapability.Security.Asset
     * @atomicservice [since 14]
     * @since 11
     */
    enum ErrorCode {
        /**
         * The caller does not have the permission.
         *
         * @syscap SystemCapability.Security.Asset
         * @since 11
         */
        PERMISSION_DENIED = 201,
        /**
         * The caller is not a system application.
         *
         * @syscap SystemCapability.Security.Asset
         * @since 12
         */
        NOT_SYSTEM_APPLICATION = 202,
        /**
         * The argument is invalid.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        INVALID_ARGUMENT = 401,
        /**
         * The ASSET service is unavailable.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        SERVICE_UNAVAILABLE = 24000001,
        /**
         * Failed to find the asset.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        NOT_FOUND = 24000002,
        /**
         * The specified asset already exists.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DUPLICATED = 24000003,
        /**
         * The access to the asset is denied.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        ACCESS_DENIED = 24000004,
        /**
         * The screen lock status does not match.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        STATUS_MISMATCH = 24000005,
        /**
         * The system memory is insufficient.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        OUT_OF_MEMORY = 24000006,
        /**
         * The asset is corrupted.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DATA_CORRUPTED = 24000007,
        /**
         * The database operation failed.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        DATABASE_ERROR = 24000008,
        /**
         * The crypto operation failed.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        CRYPTO_ERROR = 24000009,
        /**
         * IPC failed.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        IPC_ERROR = 24000010,
        /**
         * The Bundle Manager service is abnormal.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        BMS_ERROR = 24000011,
        /**
         * The account service is abnormal.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        ACCOUNT_ERROR = 24000012,
        /**
         * The Access Token service is abnormal.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        ACCESS_TOKEN_ERROR = 24000013,
        /**
         * The file operation failed.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        FILE_OPERATION_ERROR = 24000014,
        /**
         * Failed to obtain the system time.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        GET_SYSTEM_TIME_ERROR = 24000015,
        /**
         * The number of cached records exceeds the upper limit.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        LIMIT_EXCEEDED = 24000016,
        /**
         * The feature is not supported.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice [since 14]
         * @since 11
         */
        UNSUPPORTED = 24000017,
        /**
         * Parameter verification failed.
         *
         * @syscap SystemCapability.Security.Asset
         * @atomicservice
         * @since 20
         */
        PARAM_VERIFICATION_FAILED = 24000018,
        /**
         * The error code indicates that the attributes required to be consistent are inconsistent.
         *
         * @syscap SystemCapability.Security.Asset
         * @FaAndStageModel
         * @atomicservice
         * @since 26.0.0
         */
        INCONSISTENT_ATTRIBUTE = 24000019
    }
}
export default asset;

```
