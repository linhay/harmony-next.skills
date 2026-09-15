# @ohos.data.distributedDataObject.d.ts

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
import { AsyncCallback } from './@ohos.base';
import type Context from './application/BaseContext';
import commonType from '@ohos.data.commonType';
/**
 * The distributedDataObject module provides basic data object management, including creating, querying, deleting,
 * modifying, and subscribing to data objects, and distributed data object collaboration for the same application among
 * multiple devices. Although this module does not parse user data, you are advised not to transfer sensitive personal
 * data or privacy data due to low-level security of storage path.
 *
 * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
 * @since 8
 */
declare namespace distributedDataObject {
    /**
     * Represents the information about the joint asset in the RDB store to bind. Currently, only the RDB stores are
     * supported.
     *
     * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
     * @since 11
     */
    interface BindInfo {
        /**
         * RDB store to which the target asset (asset to bind) belongs.
         *
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 11
         */
        storeName: string;
        /**
         * Table to which the target asset is located in the RDB store.
         *
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 11
         */
        tableName: string;
        /**
         * Primary key of the target asset in the RDB store.
         *
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 11
         */
        primaryKey: commonType.ValuesBucket;
        /**
         * Column in which the target asset is located in the RDB store.
         *
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 11
         */
        field: string;
        /**
         * Name of the target asset in the RDB store.
         *
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 11
         */
        assetName: string;
    }
    /**
     * Creates a distributed data object.
     *
     * @param { object } source - Properties of the distributed data object.
     * @returns { DistributedObject } Distributed data object created.
     * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
     * @since 8
     * @deprecated since 9
     * @useinstead distributedDataObject.create
     */
    function createDistributedObject(source: object): DistributedObject;
    /**
     * Creates a distributed data object. The object properties support basic types (number, Boolean, and string) and
     * complex types (array and nested basic types).
     *
     * @param { Context } context - Application context. For details about the application context of the FA model,
     *     see Context.For details about the application context of the stage model, see Context.
     * @param { object } source - Properties of the distributed data object.
     * @returns { DataObject } Distributed data object created.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
     * @since 9
     */
    function create(context: Context, source: object): DataObject;
    /**
     * Creates a random session ID.
     *
     * @returns { string } Session ID created.
     * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
     * @since 8
     */
    function genSessionId(): string;
    /**
     * Represents the information returned by the callback of save.
     * .
     *
     * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
     * @since 9
     */
    interface SaveSuccessResponse {
        /**
         * Unique ID for multi-device collaboration.
         *
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        sessionId: string;
        /**
         * Version of the saved object, which is a non-negative integer.
         *
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        version: number;
        /**
         * ID of the device where the distributed data object is stored. The value local indicates a local device.
         *
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        deviceId: string;
    }
    /**
     * Represents the information returned by the callback of revokeSave.
     *
     * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
     * @since 9
     */
    interface RevokeSaveSuccessResponse {
        /**
         * Unique ID for multi-device collaboration.
         *
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        sessionId: string;
    }
    /**
     * Defines an observer for obtaining the data change of a distributed object.
     *
     * @param { string } sessionId - Session ID of the distributed data object, with a maximum length of 128 bytes. The
     *     value can contain only letters, digits, and underscores (_).
     * @param { Array<string> } fields - Changed properties of the distributed data object, with a maximum length of 128
     *     bytes. The value can be customized and must be a non-empty string.
     * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
     * @since 20
     */
    type DataObserver = (sessionId: string, fields: Array<string>) => void;
    /**
     * Defines an observer for obtaining the status change of a distributed object.
     *
     * @param { string } sessionId - Session ID of the distributed data object, with a maximum length of 128 bytes. The
     *     value can contain only letters, digits, and underscores (_).
     * @param { string } networkId - Network ID of the peer device, with a maximum of 255 bytes. The value must be a non-
     *     empty string.
     * @param { string } status - Status of the distributed object. The value can be **online**, **offline**, or
     *     **restore.**
     * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
     * @since 20
     */
    type StatusObserver = (sessionId: string, networkId: string, status: string) => void;
    /**
       * Defines an observer for obtaining the transfer progress.
       *
       * @param { string } sessionId - Session ID of the distributed data object, with a maximum length of 128 bytes. The
       *     value can contain only letters, digits, and underscores (_).
       * @param { number } progress - Asset transfer progress. The value is an integer ranging from -1 to 100. The value
       *     **-1** indicates that the progress fails to be obtained, and the value **100** indicates that the transfer is
       *     complete.
       * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
       * @since 20
       */
    type ProgressObserver = (sessionId: string, progress: number) => void;
    /**
     * Provides APIs for managing a distributed data object. Before using any API of this class, use
     * createDistributedObject() to create a DistributedObject object.
     *
     * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
     * @since 8
     * @deprecated since 9
     * @useinstead null
     */
    interface DistributedObject {
        /**
         * Sets a session ID. For the devices in the collaboration state in a trusted network, data of the distributed
         * objects with the same session ID can be automatically synced across devices.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } sessionId - ID of a distributed data object on a trusted network. To remove a distributed data
         *     object from the network, set this parameter to "" or leave it empty.
         * @returns { boolean } Returns true if the session ID is set successfully; returns false otherwise.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 8
         * @deprecated since 9
         * @useinstead distributedDataObject.DataObject.setSessionId(sessionId: string, callback: AsyncCallback<void>)
         */
        setSessionId(sessionId?: string): boolean;
        /**
         * Subscribes to data changes of this distributed data object.
         *
         * @param { 'change' } type - Event type. The value is 'change', which indicates data changes.
         * @param { Function } callback - Callback used to return the changes of the distributed data object. sessionId
         *     indicates the session ID of the distributed data object. fields indicates the changed properties of the
         *     distributed data object.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 8
         * @deprecated since 9
         * @useinstead distributedDataObject.DataObject.on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void )
         */
        on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void;
        /**
         * Unsubscribes from data changes of this distributed data object.
         *
         * @param { 'change' } type - Event type. The value is 'change', which indicates data changes.
         * @param { Function } callback - Callback to unregister. If this parameter is not specified, this API unsubscribes
         *     from all callbacks for data changes of this distributed object.sessionId indicates the session ID of the
         *     distributed data object. fields indicates the changed properties of the distributed data object.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 8
         * @deprecated since 9
         * @useinstead distributedDataObject.DataObject.off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void )
         */
        off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void;
        /**
         * Subscribes to status changes of this distributed data object.
         *
         * @param { 'status' } type - Event type. The value is 'status', which indicates the status change (online or
         *     offline) of the distributed object.
         * @param { Function } callback - Callback used to return the status change. sessionId indicates the session ID of
         *     the distributed data object. networkId identifies the device. status indicates the object status, which can
         *     be online or offline.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 8
         * @deprecated since 9
         * @useinstead distributedDataObject.DataObject.on( type: 'status', callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void )
         */
        on(type: 'status', callback: (sessionId: string, networkId: string, status: 'online' | 'offline') => void): void;
        /**
         * Unsubscribes from the status change of this distributed data object.
         *
         * @param { 'status' } type - Event type. The value is 'status', which indicates the status change (online or
         *     offline) of the distributed object.
         * @param { Function } callback - Callback to unregister. If this parameter is not specified, this API unsubscribes
         *     from all callbacks for status changes of this distributed object. sessionId indicates the session ID of the
         *     distributed data object. networkId identifies the distributed data object. status indicates the object
         *     status, which can be online or offline.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 8
         * @deprecated since 9
         * @useinstead distributedDataObject.DataObject.off( type: 'status', callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void )
         */
        off(type: 'status', callback?: (sessionId: string, networkId: string, status: 'online' | 'offline') => void): void;
    }
    /**
     * Provides APIs for managing a distributed data object. Before using any API of this class, use create() to create a
     * DataObject object.
     *
     * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
     * @since 9
     */
    interface DataObject {
        /**
         * Sets a session ID. This API uses an asynchronous callback to return the result. For the devices in the
         * collaboration state in a trusted network, data of the distributed objects with the same session ID can be
         * automatically synced across devices.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param {string} sessionId - ID of a distributed data object on a trusted network. The value can contain only
         *     letters, digits, and underscores (_), and cannot exceed 128 characters. If this parameter is set to "" or
         *     null, the distributed data object exits the network.
         * @param {AsyncCallback<void>} callback - Asynchronous callback invoked when the session ID is successfully set.
         * @throws {BusinessError} 201 - Permission verification failed.
         * @throws {BusinessError} 401 - Parameter error. Possible causes: 1. Incorrect parameter types;
         *     2. The sessionId allows only letters, digits, and underscores(_), and cannot exceed 128 in length.
         * @throws {BusinessError} 15400001 - Failed to create the in-memory database.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        setSessionId(sessionId: string, callback: AsyncCallback<void>): void;
        /**
         * Exits all sessions. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC [since 9 - 19]
         * @param {AsyncCallback<void>} callback - Callback invoked when the distributed data object exits all sessions.
         * @throws {BusinessError} 201 - Permission verification failed. [since 9 - 19]
         * @throws {BusinessError} 401 - Parameter error. Incorrect parameter types.
         * @throws {BusinessError} 15400001 - Failed to create the in-memory database.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        setSessionId(callback: AsyncCallback<void>): void;
        /**
         * Sets a session ID or exits the distributed network. This API uses a promise to return the result. If this
         * parameter is set to "" or null, or left empty, the distributed data object exits the network. For the devices in
         * the collaboration state in a trusted network, data of the distributed objects with the same session ID can be
         * automatically synced across devices.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param {string} sessionId - ID of a distributed data object on a trusted network. The value can contain only
         *     letters, digits, and underscores (_), and cannot exceed 128 characters. If this parameter is set to "" or
         *     null, or left empty, the distributed data object exits the network.
         * @returns {Promise<void>} Promise that returns no value.
         * @throws {BusinessError} 201 - Permission verification failed.
         * @throws {BusinessError} 401 - Parameter error. Possible causes: 1. Incorrect parameter types;
         *     2. The sessionId allows only letters, digits, and underscores(_), and cannot exceed 128 in length.
         * @throws {BusinessError} 15400001 - Failed to create the in-memory database.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        setSessionId(sessionId?: string): Promise<void>;
        /**
         * Subscribes to data changes of this distributed data object.
         *
         * @param { 'change' } type - Event type. The value is **'change'**, which indicates data changes. sessionId
         * @param { Function } callback - Callback used to return the changes of the distributed data object.
         *     indicates the session ID of the distributed data object. fields indicates the changed properties of the
         *     distributed data object.
         * @throws {BusinessError} 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void;
        /**
         * Unsubscribes from data changes of this distributed data object.
         *
         * @param { 'change' } type - Event type. The value is 'change', which indicates data changes.
         * @param { Function } callback - Callback to unregister. If this parameter is not specified, this API unsubscribes
         *     from all callbacks for data changes of this distributed object. sessionId indicates the session ID of
         *     the distributed data object. fields indicates the changed properties of the distributed data object.
         * @throws {BusinessError} 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void;
        /**
         * Subscribes to status changes of this distributed data object.
         *
         * @param { 'status' } type - Event type. The value is 'status', which indicates the status change (online or
         *     offline) of the distributed object.
         * @param { Function } callback - Callback used to return the status change. sessionId indicates the session
         *     ID of the distributed data object. networkId identifies the device. status indicates the object status,
         *     which can be online or offline.
         * @throws {BusinessError} 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        on(type: 'status', callback: (sessionId: string, networkId: string, status: 'online' | 'offline') => void): void;
        /**
         * Unsubscribes from the status change of this distributed data object.
         *
         * @param { 'status' } type - Event type. The value is 'status', which indicates the status change (online or
         *     offline) of the distributed object.
         * @param { Function } callback - Callback to unregister. If this parameter is not specified, this API unsubscribes
         *     from all callbacks for status changes of this distributed object. sessionId indicates the session ID
         *     distributed data object. networkId identifies the distributed data object. status indicates the
         *     indicates the object status, which can be online or offline.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        off(type: 'status', callback?: (sessionId: string, networkId: string, status: 'online' | 'offline') => void): void;
        /**
         * Saves a distributed data object. This API uses an asynchronous callback to return the result.
         *
         * @param { string } deviceId - ID of the device where the data is stored. The value local indicates a local
         *     device.
         * @param { AsyncCallback<SaveSuccessResponse> } callback - Callback used to return SaveSuccessResponse, which
         *     contains information such as session ID, version, and device ID.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        save(deviceId: string, callback: AsyncCallback<SaveSuccessResponse>): void;
        /**
         * Saves a distributed data object. This API uses a promise to return the result.
         *
         * @param { string } deviceId - ID of the device where the data is saved. The default value is local, which
         *     indicates a local device.
         * @returns { Promise<SaveSuccessResponse> } Promise used to return SaveSuccessResponse, which contains
         *     information such as session ID, version, and device ID.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        save(deviceId: string): Promise<SaveSuccessResponse>;
        /**
         * Revokes the data of this distributed data object saved. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<RevokeSaveSuccessResponse> } callback - Callback used to return
         *     RevokeSaveSuccessResponse, which contains the session ID.
         * @throws { BusinessError } 401 - Parameter error. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        revokeSave(callback: AsyncCallback<RevokeSaveSuccessResponse>): void;
        /**
         * Revokes the data of this distributed data object saved. This API uses a promise to return the result.
         *
         * @returns { Promise<RevokeSaveSuccessResponse> } Promise used to return RevokeSaveSuccessResponse, which
         *     contains the session ID.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 9
         */
        revokeSave(): Promise<RevokeSaveSuccessResponse>;
        /**
         * Binds joint assets. Currently, only the binding between an asset in a distributed data object and an asset in an
         * RDB store is supported. This API uses an asynchronous callback to return the result.
         *
         * @param { string } assetKey - Key of the joint asset in the distributed data object.
         * @param { BindInfo } bindInfo - Information about the joint asset in the RDB store, including the RDB store name,
         *     table name, primary key, column name, and asset name in the RDB store.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 11
         */
        bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void;
        /**
         * Binds joint assets. Currently, only the binding between an asset in a distributed data object and an asset in an
         * RDB store is supported. This API uses a promise to return the result.
         *
         * @param { string } assetKey - Key of the joint asset in the distributed data object.
         * @param { BindInfo } bindInfo - Information about the joint asset in the RDB store, including the RDB store name,
         *     table name, primary key, column name, and asset name in the RDB store.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 11
         */
        bindAssetStore(assetKey: string, bindInfo: BindInfo): Promise<void>;
        /**
         * Subscribes to data changes of this distributed data object.
         *
         * @param { 'change' } type - Event type. The value is 'change', which indicates data changes.
         * @param { DataObserver } callback - Callback used to listen for data changes of a distributed object.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 20
         */
        on(type: 'change', callback: DataObserver): void;
        /**
         * Unsubscribes from data changes of this distributed object.
         *
         * @param { 'change' } type - Event type. The value is 'change', which indicates data changes.
         * @param { DataObserver } [callback] - Callback to unregister. If this parameter is not specified, this API
         *     unsubscribes from all callbacks for data changes of this distributed object.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 20
         */
        off(type: 'change', callback?: DataObserver): void;
        /**
         * Subscribes to the status changes of this distributed object.
         *
         * @param { 'status' } type - Event type. The value is 'status', which indicates the status changes of a
         *     distributed object.
         * @param { StatusObserver } callback - Callback used to listen for status changes of a distributed object.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 20
         */
        on(type: 'status', callback: StatusObserver): void;
        /**
         * Unsubscribes from status changes of this distributed object.
         *
         * @param { 'status' } type - Event type. The value is 'status', which indicates the status changes of a
         *     distributed object.
         * @param { StatusObserver } [callback] - Callback to unregister. If this parameter is not specified, this API
         *     unsubscribes from all callbacks for status changes of this distributed object.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 20
         */
        off(type: 'status', callback?: StatusObserver): void;
        /**
         * Subscribes to the asset transfer progress changes.
         *
         * @param { 'progressChanged' } type - Event type. The value is 'progressChanged', which indicates the asset
         *     transfer progress changes.
         * @param { ProgressObserver } callback - Callback used to listen for the asset transfer progress changes.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 20
         */
        on(type: 'progressChanged', callback: ProgressObserver): void;
        /**
         * Unsubscribes from asset transfer progress changes.
         *
         * @param { 'progressChanged' } type - Event type. The value is 'progressChanged', which indicates the asset
         *     transfer progress changes.
         * @param { ProgressObserver } [callback] - Callback to unregister. If this parameter is not specified, this API
         *     unsubscribes from all callbacks for progress changes of this distributed object.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 20
         */
        off(type: 'progressChanged', callback?: ProgressObserver): void;
        /**
         * Sets the property information about a single asset in a distributed object. This API must be called before the
         * setSessionId API is called. This API uses a promise to return the result.
         *
         * @param { string } assetKey - Property name of the asset in the distributed object.
         * @param { string } uri - URI of the new asset to be set, indicating the distributed path for storing the asset.
         *     The value must correspond to an existing asset.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 15400002 - Parameter error. Possible causes:
         *     1. The assetKey is invalid, such as "";
         *     2. The uri is invalid, such as "".
         * @throws {BusinessError} 15400003 - The sessionId of the distributed object has been set.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 20
         */
        setAsset(assetKey: string, uri: string): Promise<void>;
        /**
         * Sets the property information about multiple assets in a distributed object. This API must be called before the
         * setSessionId API is called. The number of values contained in the uris array ranges from 1 to 50.
         * This API uses a promise to return the result.
         *
         * @param { string } assetsKey - Property name of the assets in the distributed object.
         * @param { Array<string> } uris - URIs of the new asset array to be set, indicating the distributed paths for
         *     storing each element of the asset. The number of array elements ranges from 1 to 50. The URI of an element
         *     must be the distributed path corresponding to an actual asset.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 15400002 - Parameter error. Possible causes:
         *     1. The assetsKey is invalid, such as "";
         *     2. The uris is invalid, such as the length of uris is more than 50.
         * @throws {BusinessError} 15400003 - The sessionId of the distributed object has been set.
         * @syscap SystemCapability.DistributedDataManager.DataObject.DistributedObject
         * @since 20
         */
        setAssets(assetsKey: string, uris: Array<string>): Promise<void>;
    }
}
export default distributedDataObject;

```
