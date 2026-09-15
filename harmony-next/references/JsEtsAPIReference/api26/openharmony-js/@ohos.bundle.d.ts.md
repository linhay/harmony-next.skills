# @ohos.bundle.d.ts

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
 * @kit AbilityKit
 */
import { AsyncCallback } from './@ohos.base';
import { ApplicationInfo } from './bundle/applicationInfo';
import { AbilityInfo } from './bundle/abilityInfo';
import Want from './@ohos.app.ability.Want';
import image from './@ohos.multimedia.image';
import { BundleInfo } from './bundle/bundleInfo';
/**
 * The module provides APIs for obtaining information about an application, including
 * [bundle information]{@link ./bundle/bundleInfo},
 * [application information]{@link ./bundle/applicationInfo:ApplicationInfo}, and
 * [ability information]{@link ./bundle/abilityInfo:AbilityInfo}. It also provides APIs to obtain and set the
 * application disabling state.
 *
 * > **NOTE**
 * >
 * > The APIs of this module have been deprecated since API version 9. You are advised to use
 * > [@ohos.bundle.bundleManager]{@link @ohos.bundle.bundleManager:bundleManager} instead.
 *
 * @syscap SystemCapability.BundleManager.BundleFramework
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.bundle.bundleManager:bundleManager
 */
declare namespace bundle {
    /**
     * > **NOTE**
     * >
     * > This API has been supported since API version 7 and deprecated since API version 9. You are advised to use
     * > [bundleManager.BundleFlag]{@link @ohos.bundle.bundleManager:bundleManager.BundleFlag} instead.
     *
     * Enumerates the bundle flags, which indicate the type of bundle information to obtain.
     *
     * If an API does not match the flag, the flag is ignored. For example, using **GET_ABILITY_INFO_WITH_PERMISSION** to
     * obtain the application information does not affect the result.
     *
     * Flags can be used together. For example, you can use the combination of **GET_APPLICATION_INFO_WITH_PERMISSION**
     * and **GET_APPLICATION_INFO_WITH_DISABLE** to obtain the result that contains both application permission
     * information and disabled application information.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.bundle.bundleManager:bundleManager.BundleFlag
     */
    enum BundleFlag {
        /**
         * Obtains the default application information.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.BundleFlag#GET_BUNDLE_INFO_DEFAULT
         */
        GET_BUNDLE_DEFAULT = 0x00000000,
        /**
         * Obtains the bundle information with the ability information.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.BundleFlag#GET_BUNDLE_INFO_WITH_ABILITY
         */
        GET_BUNDLE_WITH_ABILITIES = 0x00000001,
        /**
         * Obtains the ability information with the permission information.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.AbilityFlag#GET_ABILITY_INFO_WITH_PERMISSION
         */
        GET_ABILITY_INFO_WITH_PERMISSION = 0x00000002,
        /**
         * Obtains the ability information with the application information.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.AbilityFlag#GET_ABILITY_INFO_WITH_APPLICATION
         */
        GET_ABILITY_INFO_WITH_APPLICATION = 0x00000004,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        GET_APPLICATION_INFO_WITH_PERMISSION = 0x00000008,
        /**
         * Obtains the bundle information with the information about the required permissions.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.BundleFlag#GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION
         */
        GET_BUNDLE_WITH_REQUESTED_PERMISSION = 0x00000010,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        GET_ALL_APPLICATION_INFO = 0xFFFF0000,
        /**
         * Obtains the ability metadata information.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.AbilityFlag#GET_ABILITY_INFO_WITH_METADATA
         */
        GET_ABILITY_INFO_WITH_METADATA = 0x00000020,
        /**
         * No uninstallation permission.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 8
         * @deprecated since 9
         */
        GET_APPLICATION_INFO_WITH_METADATA = 0x00000040,
        /**
         * Obtains the ability information of system applications.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.AbilityFlag#GET_ABILITY_INFO_ONLY_SYSTEM_APP
         */
        GET_ABILITY_INFO_SYSTEMAPP_ONLY = 0x00000080,
        /**
         * Obtains information about disabled abilities.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.AbilityFlag#GET_ABILITY_INFO_WITH_DISABLE
         */
        GET_ABILITY_INFO_WITH_DISABLE = 0x00000100,
        /**
         * No uninstallation permission.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 8
         * @deprecated since 9
         */
        GET_APPLICATION_INFO_WITH_DISABLE = 0x00000200
    }
    /**
     * > **NOTE**
     * >
     * > This API has been supported since API version 7 and deprecated since API version 9. No substitute is provided.
     *
     * Enumerates the color modes of applications and widgets.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     * @useinstead null
     */
    export enum ColorMode {
        /**
         * Auto mode.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.app.ability.ConfigurationConstant/ConfigurationConstant.ColorMode#COLOR_MODE_NOT_SET
         */
        AUTO_MODE = -1,
        /**
         * Dark mode.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.app.ability.ConfigurationConstant/ConfigurationConstant.ColorMode#COLOR_MODE_DARK
         */
        DARK_MODE = 0,
        /**
         * Light mode.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.app.ability.ConfigurationConstant/ConfigurationConstant.ColorMode#COLOR_MODE_LIGHT
         */
        LIGHT_MODE = 1
    }
    /**
     * > **NOTE**
     * >
     * > This API has been supported since API version 7 and deprecated since API version 9. You are advised to use
     * > [bundleManager.PermissionGrantState]{@link @ohos.bundle.bundleManager:bundleManager.PermissionGrantState}
     * > instead.
     *
     * Enumerates the permission grant states.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.bundle.bundleManager:bundleManager.PermissionGrantState
     */
    export enum GrantStatus {
        /**
         * Permission denied.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.PermissionGrantState#PERMISSION_DENIED
         */
        PERMISSION_DENIED = -1,
        /**
         * Permission granted.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.PermissionGrantState#PERMISSION_GRANTED
         */
        PERMISSION_GRANTED = 0
    }
    /**
     * > **NOTE**
     * >
     * > This API has been supported since API version 7 and deprecated since API version 9. You are advised to use
     * > [bundleManager.AbilityType]{@link @ohos.bundle.bundleManager:bundleManager.AbilityType} instead.
     *
     * Enumerates the ability types.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.bundle.bundleManager:bundleManager.AbilityType
     */
    export enum AbilityType {
        /**
         * Unknown ability type.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        UNKNOWN = 0,
        /**
         * FA developed using the Page template to provide the capability of interacting with users.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.AbilityType#PAGE
         */
        PAGE = 1,
        /**
         * PA developed using the Service template to provide the capability of running tasks in the background.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.AbilityType#SERVICE
         */
        SERVICE = 2,
        /**
         * PA developed using the Data template to provide unified data access for external systems.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.AbilityType#DATA
         */
        DATA = 3
    }
    /**
     * > **NOTE**
     * >
     * > This API has been supported since API version 7 and deprecated since API version 9. No substitute is provided.
     *
     * Enumerates the ability subtypes.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    export enum AbilitySubType {
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        UNSPECIFIED = 0,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        CA = 1
    }
    /**
     * > **NOTE**
     * >
     * > This API has been supported since API version 7 and deprecated since API version 9. You are advised to use
     * > [bundleManager.DisplayOrientation]{@link @ohos.bundle.bundleManager:bundleManager.DisplayOrientation} instead.
     *
     * Enumerates display orientations.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.bundle.bundleManager:bundleManager.DisplayOrientation
     */
    export enum DisplayOrientation {
        /**
         * Unspecified display orientation.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.DisplayOrientation#UNSPECIFIED
         */
        UNSPECIFIED = 0,
        /**
         * Landscape orientation.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.DisplayOrientation#LANDSCAPE
         */
        LANDSCAPE = 1,
        /**
         * Portrait orientation.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.DisplayOrientation#PORTRAIT
         */
        PORTRAIT = 2,
        /**
         * Orientation same as that of the nearest ability in the stack.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.DisplayOrientation#FOLLOW_RECENT
         */
        FOLLOW_RECENT = 3
    }
    /**
     * > **NOTE**
     * >
     * > This API has been supported since API version 7 and deprecated since API version 9. You are advised to use
     * > [bundleManager.LaunchType]{@link @ohos.bundle.bundleManager:bundleManager.LaunchType} instead.
     *
     * Enumerates the ability launch modes.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.bundle.bundleManager:bundleManager.LaunchType
     */
    export enum LaunchMode {
        /**
         * The ability has only one instance.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.LaunchType#SINGLETON
         */
        SINGLETON = 0,
        /**
         * The ability can have multiple instances.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.bundle.bundleManager/bundleManager.LaunchType#MULTITON
         */
        STANDARD = 1
    }
    /**
     * > **NOTE**
     * >
     * > This API has been supported since API version 7 and deprecated since API version 9. No substitute is provided.
     *
     * Options that contain the user ID.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    export interface BundleOptions {
        /**
         * User ID. The default value is the user ID of the caller. The value must be greater than or equal to 0.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        userId?: number;
    }
    /**
     * > **NOTE**
     * >
     * > This API has been supported since API version 7 and deprecated since API version 9. You are advised to use
     * > [errorcode-bundle](docroot://reference/apis-ability-kit/errorcode-bundle.md) instead.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    export enum InstallErrorCode {
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        SUCCESS = 0,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_INSTALL_FAILURE = 1,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_INSTALL_FAILURE_ABORTED = 2,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_INSTALL_FAILURE_INVALID = 3,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_INSTALL_FAILURE_CONFLICT = 4,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_INSTALL_FAILURE_STORAGE = 5,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_INSTALL_FAILURE_INCOMPATIBLE = 6,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_UNINSTALL_FAILURE = 7,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_UNINSTALL_FAILURE_BLOCKED = 8,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_UNINSTALL_FAILURE_ABORTED = 9,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_UNINSTALL_FAILURE_CONFLICT = 10,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_INSTALL_FAILURE_DOWNLOAD_TIMEOUT = 0x0B,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_INSTALL_FAILURE_DOWNLOAD_FAILED = 0x0C,
        /**
         * No uninstallation permission.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 8
         * @deprecated since 9
         */
        STATUS_RECOVER_FAILURE_INVALID = 0x0D,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_ABILITY_NOT_FOUND = 0x40,
        /**
         * Installation conflict. (The basic information of the application to update is inconsistent with that of the
         * existing application.)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 7
         * @deprecated since 9
         */
        STATUS_BMS_SERVICE_ERROR = 0x41,
        /**
         * No uninstallation permission.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 8
         * @deprecated since 9
         */
        STATUS_FAILED_NO_SPACE_LEFT = 0x42,
        /**
         * No uninstallation permission.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 8
         * @deprecated since 9
         */
        STATUS_GRANT_REQUEST_PERMISSIONS_FAILED = 0x43,
        /**
         * No uninstallation permission.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 8
         * @deprecated since 9
         */
        STATUS_INSTALL_PERMISSION_DENIED = 0x44,
        /**
         * No uninstallation permission.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework
         * @since 8
         * @deprecated since 9
         */
        STATUS_UNINSTALL_PERMISSION_DENIED = 0x45
    }
    /**
     * Obtains the bundle information based on a given bundle name and bundle options. This API uses an asynchronous
     * callback to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { number } bundleFlags - Type of information that will be returned. For details about the available
     *     enumerated values, see the bundle information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { BundleOptions } options - Includes **userId**.
     * @param { AsyncCallback<BundleInfo> } callback - Callback used to return the bundle information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     * @useinstead null
     */
    function getBundleInfo(bundleName: string, bundleFlags: number, options: BundleOptions, callback: AsyncCallback<BundleInfo>): void;
    /**
     * Obtains the bundle information based on a given bundle name. This API uses an asynchronous callback to return the
     * result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { number } bundleFlags - Type of information that will be returned. For details about the available
     *     enumerated values, see the bundle information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { AsyncCallback<BundleInfo> } callback - Callback used to return the bundle information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     * @useinstead null
     */
    function getBundleInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void;
    /**
     * Obtains the bundle information based on a given bundle name. This API uses a promise to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { number } bundleFlags - Type of information that will be returned. For details about the available
     *     enumerated values, see the bundle information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { BundleOptions } options - Options that contain the user ID.
     * @returns { Promise<BundleInfo> } Promise used to return the bundle information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     * @useinstead null
     */
    function getBundleInfo(bundleName: string, bundleFlags: number, options?: BundleOptions): Promise<BundleInfo>;
    /**
     * Obtains the ability information based on a given bundle name and ability name. This API uses an asynchronous
     * callback to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { string } abilityName - Ability name.
     * @param { AsyncCallback<AbilityInfo> } callback - Callback used to return the ability information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getAbilityInfo(bundleName: string, abilityName: string, callback: AsyncCallback<AbilityInfo>): void;
    /**
     * Obtains the ability information based on a given bundle name and ability name. This API uses a promise to return
     * the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { string } abilityName - Ability name.
     * @returns { Promise<AbilityInfo> } Promise used to return the ability information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getAbilityInfo(bundleName: string, abilityName: string): Promise<AbilityInfo>;
    /**
     * Obtains the application information of the specified user based on a given bundle name. This API uses an
     * asynchronous callback to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { number } bundleFlags - Type of information that will be returned. For details about the available
     *     enumerated values, see the application information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { number } userId - User ID. The value must be greater than or equal to 0.
     * @param { AsyncCallback<ApplicationInfo> } callback - Callback used to return the application information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getApplicationInfo(bundleName: string, bundleFlags: number, userId: number, callback: AsyncCallback<ApplicationInfo>): void;
    /**
     * Obtains the application information based on a given bundle name. This API uses an asynchronous callback to return
     * the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { number } bundleFlags - Type of information that will be returned. For details about the available
     *     enumerated values, see the application information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { AsyncCallback<ApplicationInfo> } callback - Callback used to return the application information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getApplicationInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<ApplicationInfo>): void;
    /**
     * Obtains the application information based on a given bundle name. This API uses a promise to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { number } bundleFlags - Type of information that will be returned. For details about the available
     *     enumerated values, see the application information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { number } userId - User ID. The default value is the user ID of the caller. The value must be greater than
     *     or equal to 0.
     * @returns { Promise<ApplicationInfo> } Promise used to return the application information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getApplicationInfo(bundleName: string, bundleFlags: number, userId?: number): Promise<ApplicationInfo>;
    /**
     * Obtains the ability information of the specified user based on given Want. This API uses an asynchronous callback
     * to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { Want } want - Want containing the bundle name.
     * @param { number } bundleFlags - Ability information to be returned. For details about the available enumerated
     *     values, see the ability information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { number } userId - User ID. The value must be greater than or equal to 0.
     * @param { AsyncCallback<Array<AbilityInfo>> } callback - Callback used to return the ability information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function queryAbilityByWant(want: Want, bundleFlags: number, userId: number, callback: AsyncCallback<Array<AbilityInfo>>): void;
    /**
     * Obtains the ability information based on given Want. This API uses an asynchronous callback to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { Want } want - Want containing the bundle name.
     * @param { number } bundleFlags - Ability information to be returned. For details about the available enumerated
     *     values, see the ability information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { AsyncCallback<Array<AbilityInfo>> } callback - Callback used to return the ability information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function queryAbilityByWant(want: Want, bundleFlags: number, callback: AsyncCallback<Array<AbilityInfo>>): void;
    /**
     * Obtains the ability information based on given Want. This API uses a promise to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { Want } want - Want containing the bundle name.
     * @param { number } bundleFlags - Ability information to be returned. For details about the available enumerated
     *     values, see the ability information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { number } userId - User ID. The default value is the user ID of the caller. The value must be greater than
     *     or equal to 0.
     * @returns { Promise<Array<AbilityInfo>> } Promise used to return the ability information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function queryAbilityByWant(want: Want, bundleFlags: number, userId?: number): Promise<Array<AbilityInfo>>;
    /**
     * Obtains the information of all bundles of the specified user. This API uses an asynchronous callback to return the
     * result
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED
     * @param { BundleFlag } bundleFlag - Type of information that will be returned. For details about the available
     *     enumerated values, see the bundle information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { number } userId - User ID. The default value is the user ID of the caller. The value must be greater than
     *     or equal to 0.
     * @param { AsyncCallback<Array<BundleInfo>> } callback - Callback used to return the information of all bundles.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getAllBundleInfo(bundleFlag: BundleFlag, userId: number, callback: AsyncCallback<Array<BundleInfo>>): void;
    /**
     * Obtains the information of all bundles of the current user. This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED
     * @param { BundleFlag } bundleFlag - Type of information that will be returned. For details about the available
     *     enumerated values, see the bundle information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { AsyncCallback<Array<BundleInfo>> } callback - Callback used to return the information of all bundles.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getAllBundleInfo(bundleFlag: BundleFlag, callback: AsyncCallback<Array<BundleInfo>>): void;
    /**
     * Obtains the information of all bundles of the specified user. This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED
     * @param { BundleFlag } bundleFlag - Type of information that will be returned. For details about the available
     *     enumerated values, see the bundle information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { number } userId - User ID. The default value is the user ID of the caller. The value must be greater than
     *     or equal to 0.
     * @returns { Promise<Array<BundleInfo>> } Promise used to return the information of all bundles.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getAllBundleInfo(bundleFlag: BundleFlag, userId?: number): Promise<Array<BundleInfo>>;
    /**
     * Obtains the information about all applications. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED
     * @param { number } bundleFlags - Type of information that will be returned. For details about the available
     *     enumerated values, see the application information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { number } userId - User ID. The default value is the user ID of the caller. The value must be greater than
     *     or equal to 0.
     * @param { AsyncCallback<Array<ApplicationInfo>> } callback - Callback used to return the application information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getAllApplicationInfo(bundleFlags: number, userId: number, callback: AsyncCallback<Array<ApplicationInfo>>): void;
    /**
     * Obtains the information about all applications of the current user. This API uses an asynchronous callback to
     * return the result.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED
     * @param { number } bundleFlags - Type of information that will be returned. For details about the available
     *     enumerated values, see the application information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { AsyncCallback<Array<ApplicationInfo>> } callback - Callback used to return the application information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getAllApplicationInfo(bundleFlags: number, callback: AsyncCallback<Array<ApplicationInfo>>): void;
    /**
     * Obtains the information about all applications of the specified user. This API uses a promise to return the result.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED
     * @param { number } bundleFlags - Type of information that will be returned. For details about the available
     *     enumerated values, see the application information flags in [BundleFlag]{@link bundle.BundleFlag}.
     * @param { number } userId - User ID. The default value is the user ID of the caller. The value must be greater than
     *     or equal to 0.
     * @returns { Promise<Array<ApplicationInfo>> } Promise used to return the application information.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getAllApplicationInfo(bundleFlags: number, userId?: number): Promise<Array<ApplicationInfo>>;
    /**
     * Obtains bundle name by the given uid.
     *
     * @param { number } uid - Indicates the UID of an application.
     * @param { AsyncCallback<string> } callback
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.bundle.bundleManager/bundleManager#getBundleNameByUid
     */
    function getNameForUid(uid: number, callback: AsyncCallback<string>): void;
    /**
     * Obtains the bundle name based on a UID. This API uses a promise to return the result.
     *
     * @param { number } uid - UID based on which the bundle name is to obtain.
     * @returns { Promise<string> } Returns the bundle name.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 8
     * @deprecated since 9
     * @useinstead null
     */
    function getNameForUid(uid: number): Promise<string>;
    /**
     * Obtains information about the bundles contained in a HAP file. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { string } hapFilePath - Path where the HAP file is stored. The absolute path of the application and the
     *     data directory sandbox path are supported.
     * @param { number } bundleFlags - Flags used to specify information contained in the BundleInfo object that will be
     *     returned. For details about the available enumerated values, see the bundle information flags in
     *     [BundleFlag]{@link bundle.BundleFlag}.
     * @param { AsyncCallback<BundleInfo> } callback - Callback used to return the information about the bundles.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getBundleArchiveInfo(hapFilePath: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void;
    /**
     * Obtains information about the bundles contained in a HAP file. This API uses a promise to return the result.
     *
     * @param { string } hapFilePath - Path where the HAP file is stored. The absolute path of the application and the
     *     data directory sandbox path are supported.
     * @param { number } bundleFlags - Flags used to specify information contained in the BundleInfo object that will be
     *     returned. For details about the available enumerated values, see the bundle information flags in
     *     [BundleFlag]{@link bundle.BundleFlag}.
     * @returns { Promise<BundleInfo> } - Returns the BundleInfo object.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getBundleArchiveInfo(hapFilePath: string, bundleFlags: number): Promise<BundleInfo>;
    /**
     * Obtains the Want object that launches the specified application. This API uses an asynchronous callback to return
     * the result.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED
     * @param { string } bundleName - Bundle name.
     * @param { AsyncCallback<Want> } callback - Callback used to return the Want object.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getLaunchWantForBundle(bundleName: string, callback: AsyncCallback<Want>): void;
    /**
     * Obtains the Want object that launches the specified application. This API uses a promise to return the result.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED
     * @param { string } bundleName - Bundle name.
     * @returns { Promise<Want> } Returns the Want for starting the application's main ability if any.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 7
     * @deprecated since 9
     */
    function getLaunchWantForBundle(bundleName: string): Promise<Want>;
    /**
     * Obtains the application name based on a given bundle name and ability name. This API uses an asynchronous callback
     * to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { string } abilityName - Ability name.
     * @param { AsyncCallback<string> } callback - Callback used to return the application name.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 8
     * @deprecated since 9
     */
    function getAbilityLabel(bundleName: string, abilityName: string, callback: AsyncCallback<string>): void;
    /**
     * Obtains the application name based on a given bundle name and ability name. This API uses a promise to return the
     * result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { string } abilityName - Ability name.
     * @returns { Promise<string> } Promise used to return the application name.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 8
     * @deprecated since 9
     */
    function getAbilityLabel(bundleName: string, abilityName: string): Promise<string>;
    /**
     * Obtains the [PixelMap]{@link @ohos.multimedia.image:image} of the icon corresponding to a given bundle name and
     * ability name. This API uses an asynchronous callback to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { string } abilityName - Ability name.
     * @param { AsyncCallback<image.PixelMap> } callback - Callback used to return the
     *     [PixelMap]{@link @ohos.multimedia.image:image}.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 8
     * @deprecated since 9
     * @useinstead null
     */
    function getAbilityIcon(bundleName: string, abilityName: string, callback: AsyncCallback<image.PixelMap>): void;
    /**
     * Obtains the [PixelMap]{@link @ohos.multimedia.image:image} of the icon corresponding to a given bundle name and
     * ability name. This API uses a promise to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { string } abilityName - Ability name.
     * @returns { Promise<image.PixelMap> } Returns the PixelMap object representing the icon of the specified ability.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 8
     * @deprecated since 9
     * @useinstead null
     */
    function getAbilityIcon(bundleName: string, abilityName: string): Promise<image.PixelMap>;
    /**
     * Checks whether the ability that matches a given AbilityInfo object is enabled. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { AbilityInfo } info - Ability information.
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. **true** if enabled, **false**
     *     otherwise.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 8
     * @deprecated since 9
     */
    function isAbilityEnabled(info: AbilityInfo, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether the ability that matches a given AbilityInfo object is enabled. This API uses a promise to return
     * the result.
     *
     * @param { AbilityInfo } info - Ability information.
     * @returns { Promise<boolean> } Promise used to return the result. **true** if enabled, **false** otherwise.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 8
     * @deprecated since 9
     */
    function isAbilityEnabled(info: AbilityInfo): Promise<boolean>;
    /**
     * Checks whether an application is enabled based on a given bundle name. This API uses an asynchronous callback to
     * return the result.
     *
     * @param { string } bundleName - Bundle name.
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. **true** if enabled, **false**
     *     otherwise.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 8
     * @deprecated since 9
     */
    function isApplicationEnabled(bundleName: string, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether an application is enabled based on a given bundle name. This API uses a promise to return the
     * result.
     *
     * @param { string } bundleName - Bundle name.
     * @returns { Promise<boolean> } Promise used to return the result. **true** if enabled, **false** otherwise.
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 8
     * @deprecated since 9
     */
    function isApplicationEnabled(bundleName: string): Promise<boolean>;
}
export default bundle;

```
