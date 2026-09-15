# @ohos.data.commonType.d.ts

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
/**
 * The commonType module defines common data types in data management.
 *
 * @syscap SystemCapability.DistributedDataManager.CommonType
 * @crossplatform
 * @since 11
 */
declare namespace commonType {
    /**
     * Enumerates the asset statuses.
     *
     * @syscap SystemCapability.DistributedDataManager.CommonType
     * @crossplatform
     * @since 11
     */
    enum AssetStatus {
        /**
         * The asset is in normal status.
         *
         * @syscap SystemCapability.DistributedDataManager.CommonType
         * @crossplatform
         * @since 11
         */
        ASSET_NORMAL,
        /**
         * The asset is to be inserted to the cloud.
         *
         * @syscap SystemCapability.DistributedDataManager.CommonType
         * @crossplatform
         * @since 11
         */
        ASSET_INSERT,
        /**
         * The asset is to be updated to the cloud.
         *
         * @syscap SystemCapability.DistributedDataManager.CommonType
         * @crossplatform
         * @since 11
         */
        ASSET_UPDATE,
        /**
         * The asset is to be deleted from the cloud.
         *
         * @syscap SystemCapability.DistributedDataManager.CommonType
         * @crossplatform
         * @since 11
         */
        ASSET_DELETE,
        /**
         * The asset is in abnormal status.
         *
         * @syscap SystemCapability.DistributedDataManager.CommonType
         * @crossplatform
         * @since 11
         */
        ASSET_ABNORMAL,
        /**
         * The asset is being downloaded to a local device.
         *
         * @syscap SystemCapability.DistributedDataManager.CommonType
         * @crossplatform
         * @since 11
         */
        ASSET_DOWNLOADING
    }
    /**
     * Represents asset (such as a file, image, or video) information.
     *
     * @syscap SystemCapability.DistributedDataManager.CommonType
     * @crossplatform
     * @since 11
     */
    interface Asset {
        /**
         * Asset name.
         *
         * @syscap SystemCapability.DistributedDataManager.CommonType
         * @crossplatform
         * @since 11
         */
        name: string;
        /**
         * Asset URI, which is an absolute path in the system.
         *
         * @syscap SystemCapability.DistributedDataManager.CommonType
         * @crossplatform
         * @since 11
         */
        uri: string;
        /**
         * Application sandbox path of the asset.
         *
         * @syscap SystemCapability.DistributedDataManager.CommonType
         * @crossplatform
         * @since 11
         */
        path: string;
        /**
         * Time when the asset was created.
         *
         * @syscap SystemCapability.DistributedDataManager.CommonType
         * @crossplatform
         * @since 11
         */
        createTime: string;
        /**
         * Time when the asset was last modified.
         *
         * @syscap SystemCapability.DistributedDataManager.CommonType
         * @crossplatform
         * @since 11
         */
        modifyTime: string;
        /**
         * Size of the asset. If this field changes, the asset is considered to have changed.
         *
         * @syscap SystemCapability.DistributedDataManager.CommonType
         * @crossplatform
         * @since 11
         */
        size: string;
        /**
         * Asset status. The default value is ASSET_NORMAL.
         *
         * @syscap SystemCapability.DistributedDataManager.CommonType
         * @crossplatform
         * @since 11
         */
        status?: AssetStatus;
    }
    /**
     * Represents an array of Assets.
     *
     * @syscap SystemCapability.DistributedDataManager.CommonType
     * @crossplatform
     * @since 11
     */
    type Assets = Array<Asset>;
    /**
     * Enumerates the value types, which vary with the parameter function.
     *
     * @unionmember { null } The value is null.
     * @unionmember { long } The value is a 64-bit integer (int64_t).
     * @unionmember { double } The value is a floating-point number (float).
     * @unionmember { string } The value is a string.
     * @unionmember { boolean } The value is true or false.
     * @unionmember { Uint8Array } The value is an array of 8-bit unsigned integers.
     * @unionmember { Asset } The value is an instance of the Asset type.
     * @unionmember { Assets } The value is an instance of the Assets type.
     * @syscap SystemCapability.DistributedDataManager.CommonType
     * @crossplatform
     * @since 11
     */
    type ValueType = null | number | string | boolean | Uint8Array | Asset | Assets;
    /**
     * Defines the types of the key and value in a KV pair.
     *
     * @syscap SystemCapability.DistributedDataManager.CommonType
     * @crossplatform
     * @since 11
     */
    type ValuesBucket = Record<string, ValueType>;
}
export default commonType;

```
