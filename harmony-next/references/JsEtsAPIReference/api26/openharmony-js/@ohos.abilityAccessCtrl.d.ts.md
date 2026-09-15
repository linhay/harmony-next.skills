# @ohos.abilityAccessCtrl.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2024 Huawei Device Co., Ltd.
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
 * Program access control provides permission verification and management capabilities for apps, supporting permission
 * status checks before accessing protected resources, runtime authorization requests, settings page authorization
 * guidance, and permission status change monitoring. Permissions are divided into three categories: system_grant
 * (automatically granted by the system), user_grant (requires manual user authorization), and
 * manual_settings (manual setting authorization). Apps must declare the required permissions in the configuration file.
 * For details about the permission management mechanism, see
 * [Application Permission Management Overview](docroot://security/AccessToken/app-permission-mgmt-overview.md).
 *
 * This module is mainly used in the following scenarios:
 *
 * - Before executing a service, verify whether the current app has the permissions required to access protected
 * resources.
 * - When a permission is not granted, bring up the runtime permission dialog box or the permission settings page to
 * request user authorization.
 * - Subscribe to permission status change events of the current app, and adjust the service process in a timely manner
 * after the permission status changes.
 *
 * ###### Core Enum Types
 *
 * - **[GrantStatus]{@link abilityAccessCtrl.GrantStatus}:** Enum for permission authorization status, used to indicate
 * the authorization status of the current permission.
 * - **[SwitchType]{@link abilityAccessCtrl.SwitchType}:** Enum for global switch types, used to indicate the type of
 * system global switch to request.
 * - **[PermissionStateChangeType]{@link abilityAccessCtrl.PermissionStateChangeType}:** Enum for permission state
 * change types, used to indicate changes such as authorization and deauthorization.
 * - **[PermissionStatus]{@link abilityAccessCtrl.PermissionStatus}:** Enum for permission status, used to indicate the
 * current permission status.
 * - **[SelectedResult]{@link abilityAccessCtrl.SelectedResult}:** Enum for the selection result on the settings page
 * authorization, used to indicate the user's selection result in the permission settings dialog box.
 *
 * ###### Core Interface Types
 *
 * - **[PermissionStateChangeInfo]{@link abilityAccessCtrl.PermissionStateChangeInfo}:** Permission state change event
 * object, used to return the change type, app identity, and permission name.
 * - **[PermissionRequestResult]{@link PermissionRequestResult}:** Permission request result object, used to return the
 * list of requested permission names, authorization results, and dialog box display results.
 * - **[Context]{@link Context}:** Context object, used to initiate a permission request or open the permission
 * settings dialog box.
 *
 * ###### Core Class
 *
 * - **[AtManager]{@link abilityAccessCtrl.AtManager}:** Program access control management class, providing
 * capabilities such as permission verification, permission dialog box request, settings page authorization guidance,
 * and permission status monitoring.
 *
 * ![image_abilityAccessCtrl](docroot://reference/apis-ability-kit/figures/accessAccessCtrl.png)
 *
 * @file Application Access Control
 * @kit AbilityKit
 */
import { AsyncCallback, Callback } from './@ohos.base';
import { Permissions } from './permissions';
import type _Context from './application/Context';
import type _PermissionRequestResult from './security/PermissionRequestResult';
/**
 *
 * @syscap SystemCapability.Security.AccessToken
 * @FaAndStageModel
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 8
 */
declare namespace abilityAccessCtrl {
    /**
     * Creates a program access control management instance for scenarios such as permission verification, runtime
     * permission request, settings page authorization guidance, and permission status change monitoring. After the call
     * is successful, an AtManager instance is returned, which can be used for subsequent permission management
     * operations.
     *
     * @returns { AtManager } **AtManager** instance obtained.
     * @syscap SystemCapability.Security.AccessToken
     * @FaAndStageModel
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     */
    function createAtManager(): AtManager;
    /**
     * Program access control management class, providing capabilities such as permission verification, runtime
     * permission dialog box request, settings page authorization guidance, global switch request, and permission
     * status monitoring. Obtain an instance through [createAtManager]{@link abilityAccessCtrl.createAtManager}.
     *
     * @syscap SystemCapability.Security.AccessToken
     * @FaAndStageModel
     * @atomicservice [since 11]
     * @since 8
     */
    interface AtManager {
        /**
         * Verifies whether an app has been granted the specified permission. After the call is successful, the
         * authorization status of the current permission is returned. The developer can decide accordingly whether to
         * directly execute subsequent services, continue to initiate a permission request, or guide the user to go to
         * system settings to modify the authorization status. This API uses a promise to return the result.
         *
         * Applicable to scenarios where a pre-permission check is performed before an app accesses protected resources.
         *
         * > **NOTE**
         * > You are advised to use [checkAccessToken]{@link abilityAccessCtrl.AtManager.checkAccessToken}.
         *
         * @param { number } tokenID - Identity identifier of the target app to be verified. It can be obtained through the
         *     [accessTokenId]{@link ./bundleManager/ApplicationInfo:ApplicationInfo.accessTokenId} field in ApplicationInfo
         *     of BundleInfo. Passing an invalid value returns error code 12100001.
         *     <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0.
         *     <br>
         *     For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoSync}.
         *     <br>If verifying the current app, it can also be obtained through
         *     [bundleManager.getBundleInfoForSelfSync]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoForSelfSync}.
         * @param { Permissions } permissionName - Name of the permission to be verified. Passing an invalid value returns
         *     error code 12100001.
         *     <br>Value constraint: The permission name length cannot exceed 256 characters.
         * @returns { Promise<GrantStatus> } Promise used to return the authorization status result.
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @since 9
         */
        verifyAccessToken(tokenID: number, permissionName: Permissions): Promise<GrantStatus>;
        /**
         * Verifies whether an app has been granted the specified permission. After the call is successful, the
         * authorization status of the current permission is returned, and the developer can decide on subsequent
         * operations accordingly. This API uses a promise to return the result.
         *
         * > **NOTE**
         * > This API is supported since API version 8 and deprecated since API version 9. It is recommended to use
         * > [checkAccessToken]{@link abilityAccessCtrl.AtManager.checkAccessToken} instead.
         *
         * @param { number } tokenID - Identity identifier of the target app to be verified. It can be obtained through the
         *     [accessTokenId]{@link ./bundleManager/ApplicationInfo:ApplicationInfo.accessTokenId} field in ApplicationInfo
         *     of BundleInfo. Passing an invalid value returns error code 12100001.
         *     <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0.
         *     <br>
         *     For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoSync}.
         *     <br>If verifying the current app, it can also be obtained through
         *     [bundleManager.getBundleInfoForSelfSync]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoForSelfSync}.
         * @param { string } permissionName - Name of the permission to be verified. Passing an invalid value returns error
         *     code 12100001.
         *     <br>Value constraint: The permission name length cannot exceed 256 characters.
         * @returns { Promise<GrantStatus> } Promise used to return the authorization status result.
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.abilityAccessCtrl.AtManager#checkAccessToken
         */
        verifyAccessToken(tokenID: number, permissionName: string): Promise<GrantStatus>;
        /**
         * Verifies whether an app has been granted the specified permission, and synchronously returns the authorization
         * status of the permission. The developer can decide accordingly whether to directly execute subsequent service
         * processes, continue to initiate a permission request, or guide the user to go to system settings to modify the
         * authorization status.
         *
         * Applicable to scenarios where a pre-permission check is performed before an app accesses protected resources
         * such as the camera, microphone, or location.
         *
         * It is recommended to use [checkAccessTokenSync]{@link abilityAccessCtrl.AtManager.checkAccessTokenSync} instead.
         *
         * @param { number } tokenID - Identity identifier of the target app to be verified. It can be obtained through the
         *     [accessTokenId]{@link ./bundleManager/ApplicationInfo:ApplicationInfo.accessTokenId} field in ApplicationInfo
         *     of BundleInfo. Passing an invalid value returns error code 12100001.
         *     <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0.
         *     <br>
         *     For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoSync}.
         *     <br>If verifying the current app, it can also be obtained through
         *     [bundleManager.getBundleInfoForSelfSync]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoForSelfSync}.
         * @param { Permissions } permissionName - Name of the permission to be verified. Passing an invalid value returns
         *     error code 12100001.
         *     <br>Value constraint: The permission name length cannot exceed 256 characters.
         * @returns { GrantStatus } Permission grant state.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 12100001 - Invalid parameter. The tokenID is 0, or the permissionName exceeds 256
         *     characters.
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @since 9
         */
        verifyAccessTokenSync(tokenID: number, permissionName: Permissions): GrantStatus;
        /**
         * Verifies whether an app has been granted the specified permission. After the call is successful, the
         * authorization status of the current permission is returned. The developer can decide accordingly whether to
         * directly execute subsequent services, continue to initiate a permission request, or guide the user to go to
         * system settings to modify the authorization status. This API uses a promise to return the result.
         *
         * Applicable to scenarios where a pre-permission check is performed before an app accesses protected resources
         * such as the camera, microphone, or location.
         *
         * @param { number } tokenID - Identity identifier of the target app to be verified. It can be obtained through the
         *     [accessTokenId]{@link ./bundleManager/ApplicationInfo:ApplicationInfo.accessTokenId} field in ApplicationInfo
         *     of BundleInfo. Passing an invalid value returns error code 12100001.
         *     <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0.
         *     <br>
         *     For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoSync}.
         *     <br>If verifying the current app, it can also be obtained through
         *     [bundleManager.getBundleInfoForSelfSync]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoForSelfSync}.
         * @param { Permissions } permissionName - Name of the permission to be verified. Passing an invalid value returns
         *     error code 12100001.
         *     <br>Value constraint: The permission name length cannot exceed 256 characters.
         * @returns { Promise<GrantStatus> } Promise used to return the authorization status result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 12100001 - Invalid parameter. The tokenID is 0, or the permissionName exceeds 256
         *     characters.
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        checkAccessToken(tokenID: number, permissionName: Permissions): Promise<GrantStatus>;
        /**
         * Verifies whether an app has been granted the specified permission, and synchronously returns the authorization
         * status of the permission. The developer can decide accordingly whether to directly execute subsequent service
         * processes, continue to initiate a permission request, or guide the user to go to the settings page to modify the
         * authorization status.
         *
         * Compared with [checkAccessToken]{@link abilityAccessCtrl.AtManager.checkAccessToken}, this API returns the
         * authorization status synchronously, making it suitable for permission verification scenarios that do not require
         * asynchronous processing.
         *
         * Applicable to scenarios where a pre-permission check is performed before an app accesses protected resources
         * such as the camera, microphone, or location.
         *
         * @param { number } tokenID - Identity identifier of the target app to be verified. It can be obtained through the
         *     [accessTokenId]{@link ./bundleManager/ApplicationInfo:ApplicationInfo.accessTokenId} field in ApplicationInfo
         *     of BundleInfo. Passing an invalid value returns error code 12100001.
         *     <br>The value should be an integer. Value constraint: This parameter must be an integer greater than 0.
         *     <br>
         *     For BundleInfo acquisition, please refer to: [bundleManager.getBundleInfoSync]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoSync}.
         *     <br>If verifying the current app, it can also be obtained through
         *     [bundleManager.getBundleInfoForSelfSync]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoForSelfSync}.
         * @param { Permissions } permissionName - Name of the permission to be verified. Passing an invalid value returns
         *     error code 12100001.
         *     <br>Value constraint: The permission name length cannot exceed 256 characters.
         * @returns { GrantStatus } Permission grant state.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 12100001 - Invalid parameter. The tokenID is 0, or the permissionName exceeds 256
         *     characters.
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        checkAccessTokenSync(tokenID: number, permissionName: Permissions): GrantStatus;
        /**
         * Used by <!--RP1-->[UIAbility]{@link @ohos.app.ability.UIAbility:UIAbility}<!--RP1End--> to bring up a dialog box
         * to request [user authorization](docroot://security/AccessToken/request-user-authorization.md), and returns the
         * authorization result of the permissions requested this time. This API uses an asynchronous callback to return
         * the result.
         *
         * Applicable to scenarios where an app proactively applies for
         * [user_grant](docroot://security/AccessToken/app-permission-mgmt-overview.md#user_grant-user-authorization)
         * permissions from the user before accessing protected resources for the first time.
         *
         * If the user denies authorization, the authorization dialog box cannot be brought up again through this API.
         * The developer can guide the user to go to the system settings interface for manual authorization, or call
         * [requestPermissionOnSetting]{@link abilityAccessCtrl.AtManager.requestPermissionOnSetting} to bring up the
         * permission settings dialog box to guide the user to complete authorization.
         *
         * <!--RP3-->
         *
         * ![requestPermissionsFromUser](docroot://reference/apis-ability-kit/figures/requestPermissionsFromUser.png)
         *
         * <!--RP3End-->
         *
         * @param { Context } context - Context of the <!--RP1-->UIAbility<!--RP1End--> requesting the permission.
         *     <br>If the context of another app, an invalid page, or a non-stage model is passed in, the API may report an
         *     error or fail to display the dialog box.
         * @param { Array<Permissions> } permissionList - List of permission names. It is recommended to pass in only the
         *     sensitive permissions necessary for the current business scenario, avoiding requesting too many permissions at
         *     once.
         *     <br>The minimum length is 1. Value constraint: The permission name can contain a maximum of 256 characters.
         * @param { AsyncCallback<PermissionRequestResult> } requestCallback - Callback function. After the call is
         *     complete, error information is returned through **err**, and the permission request result object is
         *     returned through **data**. The developer can determine whether the user has authorized, whether a dialog box
         *     has been displayed, and the reason for failure based on the permission request result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left
         *     unspecified; 2. Incorrect parameter types.
         * @throws { BusinessError } 12100001 - (Deprecated in 12) Invalid parameter. The context is invalid when it
         *     does not belong to the application itself.
         * @throws { BusinessError } 12100009 - Common inner error. An error occurs when creating the pop-up window
         *     or obtaining user operation results.
         * @syscap SystemCapability.Security.AccessToken
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>, requestCallback: AsyncCallback<PermissionRequestResult>): void;
        /**
         * Used by <!--RP1-->[UIAbility]{@link @ohos.app.ability.UIAbility:UIAbility}<!--RP1End--> to bring up a dialog box
         * to request [user authorization](docroot://security/AccessToken/request-user-authorization.md), and returns the
         * authorization result of the permissions requested this time. This API uses a promise to return the result.
         *
         * Applicable to scenarios where an app proactively applies for user_grant permissions from the user before
         * accessing protected resources for the first time.
         *
         * If the user denies authorization, the authorization dialog box cannot be brought up again through this API.
         * The developer can guide the user to go to the system settings interface for manual authorization, or call
         * [requestPermissionOnSetting]{@link abilityAccessCtrl.AtManager.requestPermissionOnSetting} to bring up the
         * permission settings dialog box to guide the user to complete authorization.
         *
         * @param { Context } context - Context of the <!--RP1-->UIAbility<!--RP1End--> requesting the permission. If the
         *     context of another app, an invalid page, or a non-stage model is passed in, the API may report an error or fail
         *     to display the dialog box.
         * @param { Array<Permissions> } permissionList - List of permission names. This array cannot be empty. It is
         *     recommended to pass in only the sensitive permissions necessary for the current business scenario and avoid
         *     requesting too many permissions at once.
         *     <br>The minimum length is 1. Value constraint: The length of a permission name cannot exceed 256 characters.
         * @returns { Promise<PermissionRequestResult> } Promise used to return the permission request result object, which
         *     contains information such as the permission array, the authorization result of each permission, whether to
         *     show a dialog box, and the failure reason.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left
         *     unspecified; 2. Incorrect parameter types.
         * @throws { BusinessError } 12100001 - (Deprecated in 12) Invalid parameter. The context is invalid when it
         *     does not belong to the application itself.
         * @throws { BusinessError } 12100009 - Common inner error. An error occurs when creating the pop-up window or
         *     obtaining the user operation result. [since 11]
         * @syscap SystemCapability.Security.AccessToken
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>): Promise<PermissionRequestResult>;
        /**
         * Subscribes to permission authorization status change events for a specified permission list of this app,
         * using an asynchronous callback. It can be used in scenarios such as updating the UI or service logic
         * in real time based on permission status, and monitoring user authorization behavior.
         * When monitoring is no longer needed, call [off]{@link abilityAccessCtrl.AtManager.off} to unsubscribe.
         *
         * - When this subscription API is called for multiple times, if the subscribed permission lists are the same but
         * the callbacks are different, the subscription is successful.
         * - When this subscription API is called for multiple times, if the subscribed permission lists contain the same
         * subset and the callbacks are the same, the subscription fails.
         *
         * There are two possible scenarios when the permission status changes from "authorized" to "unauthorized":
         *
         * - User actively revokes: The system will terminate the corresponding app process.
         * - System actively reclaims: The app process will not be terminated. A typical scenario is the one-time
         * authorization of a security component, which is automatically reclaimed by the system after the authorization
         * period ends.
         *
         * This API is usually used in conjunction with [off]{@link abilityAccessCtrl.AtManager.off}.
         * When monitoring is no longer needed, call off to unsubscribe.
         *
         * @param { 'selfPermissionStateChange' } type - Event type. The value is **'selfPermissionStateChange'**, which
         *     indicates the changes in the permission states specific to this application alone.
         * @param { Array<Permissions> } permissionList - List of permission names to subscribe to. Passing an invalid value
         *     returns error code 12100001.
         *     <br>The maximum length is 1024. Value constraint: Each permission name in the list must be a valid permission
         *     name, and its length cannot exceed 256 characters.
         * @param { Callback<PermissionStateChangeInfo> } callback - Callback used to return the result. Callback for
         *     subscribing to status change events of the specified permission name.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left
         *     unspecified; 2. Incorrect parameter types.
         * @throws { BusinessError } 12100001 - Invalid parameter. Possible causes: 1. The permissionList exceeds
         *     the size limit; 2. The permissionNames in the list are all invalid.
         * @throws { BusinessError } 12100004 - The API is used repeatedly with the same input.
         * @throws { BusinessError } 12100005 - The registration time has exceeded the limit.
         * @throws { BusinessError } 12100007 - Service exception.
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @atomicservice
         * @since 18
         */
        on(type: 'selfPermissionStateChange', permissionList: Array<Permissions>, callback: Callback<PermissionStateChangeInfo>): void;
        /**
         * Unsubscribes from permission status change events for the specified permission list of itself. After the
         * unsubscription is successful, status change notifications for the specified permission list will no longer be
         * received.
         *
         * This API can be called to unsubscribe in scenarios such as when there is no need to continue monitoring
         * permission changes, when the app exits, or when switching pages.
         *
         * When the callback parameter is not passed in, all callback functions associated with the permissionList will be
         * deleted in batch.
         *
         * This API is usually used in conjunction with [on]{@link abilityAccessCtrl.AtManager.on}
         * to cancel the monitoring relationship created through on.
         *
         * @param { 'selfPermissionStateChange' } type - Type of the unsubscription event, which is fixed as
         *     'selfPermissionStateChange', indicating a permission status change event.
         * @param { Array<Permissions> } permissionList - List of permission names to unsubscribe from. If empty, it
         *     indicates unsubscribing from all permission status changes, and must match the permission list used during
         *     [on]{@link abilityAccessCtrl.AtManager.on} subscription (order insensitive).
         *     <br>The maximum length is 1024. Value constraint: Each permission name in the list must be a valid permission
         *     name, and its length cannot exceed 256 characters.
         * @param { Callback<PermissionStateChangeInfo> } [callback] - Callback function. Callback for unsubscribing from
         *     the status change event of the specified permission names. If this parameter is not passed, all callback
         *     functions associated with permissionList will be deleted in batch.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left
         *     unspecified; 2. Incorrect parameter types.
         * @throws { BusinessError } 12100004 - The API is not used in pair with 'on'.
         * @throws { BusinessError } 12100007 - Service exception.
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @atomicservice
         * @since 18
         */
        off(type: 'selfPermissionStateChange', permissionList: Array<Permissions>, callback?: Callback<PermissionStateChangeInfo>): void;
        /**
         * Used by [UIAbility]{@link @ohos.app.ability.UIAbility:UIAbility}/
         * [UIExtensionAbility]{@link @ohos.app.ability.UIExtensionAbility:UIExtensionAbility} to bring up the permission
         * settings dialog box for a second time, and returns an array of authorization statuses.
         * This API uses a promise to return the result.
         *
         * Applicable to scenarios where the user has already denied the permission grant in the first dialog box and needs
         * to continue applying for the permission through the settings page.
         *
         * Before calling this API, the app needs to call
         * [requestPermissionsFromUser]{@link abilityAccessCtrl.AtManager.requestPermissionsFromUser} first.
         * If the user has already authorized in the first dialog box, calling this API will not bring up the
         * authorization dialog box.
         *
         * <!--RP4-->
         *
         * ![requestPermissionOnSetting](docroot://reference/apis-ability-kit/figures/requestPermissionOnSetting.png)
         *
         * <!--RP4End-->
         *
         * @param { Context } context - Context of the UIAbility or UIExtensionAbility requesting the permission. If the
         *     context of another app, an invalid page, or a non-stage model is passed in, the API may report an error or
         *     fail to display the pop-up window.
         * @param { Array<Permissions> } permissionList - List of permission names. This array cannot be empty. Only
         *     user_grant permissions that have been declared and for which the user has revoked authorization can be
         *     passed in, and the permissions passed in must belong to the same
         *     [permission group](docroot://security/AccessToken/app-permission-group-list.md).
         *     <br>Value constraint: The permission name length cannot exceed 256 characters.
         * @returns { Promise<Array<GrantStatus>> } Promise used to return an array of authorization statuses. Each element
         *     in the array corresponds to the authorization result of the respective permission in permissionList.
         * @throws { BusinessError } 12100001 - Invalid parameter. Possible causes: 1. The context is invalid
         *     because it does not belong to the application itself; 2. The permission list contains the permission
         *     that is not declared in the module.json file; 3. The permission list is invalid because the permissions in it
         *     do not belong to the same permission group; 4. The permission list contains one or more system_grant
         *     permissions.
         * @throws { BusinessError } 12100009 - Common inner error. An error occurs when creating the pop-up window or
         *     obtaining the user operation result.
         * @throws { BusinessError } 12100010 - The request already exists. [since 12 - 20]
         * @throws { BusinessError } 12100011 - All permissions in the permission list have been granted.
         * @throws { BusinessError } 12100012 - The permission list contains the permission that has not been
         *     revoked by the user.
         * @throws { BusinessError } 12100014 - Unexpected permission. You cannot request this type of permission
         *     from users via a pop-up window. [since 21]
         * @syscap SystemCapability.Security.AccessToken
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>;
        /**
         * Used by [UIAbility]{@link @ohos.app.ability.UIAbility:UIAbility}/
         * [UIExtensionAbility]{@link @ohos.app.ability.UIExtensionAbility:UIExtensionAbility} to bring up the permission
         * settings page. After the call is successful, the permission settings page will be opened. After the user operates
         * on the page, the user's selection result on the settings page will be returned. This API uses a promise to return
         * the result.
         *
         * Applicable to scenarios where
         * [manual_settings](docroot://security/AccessToken/app-permission-mgmt-overview.md#manual_settings-manual-authorization)
         * type permissions cannot be applied for through the normal authorization dialog box and the user must be
         * guided to enter system settings to complete authorization. manual_settings type permissions are permissions that
         * can only be manually enabled by the user in system settings and cannot be directly applied for through the normal
         * authorization dialog box.
         *
         * @param { Context } context - Context of the UIAbility or UIExtensionAbility requesting the permission. If the
         *     context of another app, an invalid page, or a non-stage model is passed in, the API may report an error or
         *     fail to open the settings page.
         * @param { Permissions } permission - Name of the permission for which the settings page needs to be opened. If an
         *     invalid permission or a permission not declared in module.json is passed in, error code 12100001 is returned.
         *     Only permissions of the
         *     [manual_settings](docroot://security/AccessToken/app-permission-mgmt-overview.md#manual_settings-manual-authorization)
         *     type are supported. If a permission of another type is passed in, error code 12100014 is returned.
         *     <br>Value constraint: The permission name cannot exceed 256 characters.
         * @returns { Promise<SelectedResult> } Promise used to return the user's selection result on the settings page.
         * @throws { BusinessError } 12100001 - Invalid parameter. Possible causes: 1. The context is invalid
         *     because it does not belong to the application itself; 2. The permission is invalid or not
         *     declared in the module.json file.
         * @throws { BusinessError } 12100009 - Common inner error. An error occurs when creating the pop-up window or
         *     obtaining the user operation result.
         * @throws { BusinessError } 12100014 - Unexpected permission. The permission is not a manual_settings
         *     permission.
         * @syscap SystemCapability.Security.AccessToken
         * @stagemodelonly
         * @since 22
         */
        openPermissionOnSetting(context: Context, permission: Permissions): Promise<SelectedResult>;
        /**
         * Used by UIAbility/UIExtensionAbility to bring up the global switch settings dialog box. After the call is
         * successful, if the global switch is off, the global switch settings interface will pop up for the user to
         * operate. If the global switch is already on, the dialog box will not be brought up and **true** will be returned.
         * This API uses a promise to return the result.
         *
         * Applicable to scenarios that depend on system-level global switches (such as camera, microphone, and location)
         * being turned on.
         *
         * When an app needs to use functions such as the camera, microphone, or location that require global switch
         * control, if the corresponding global switch is turned off, the app can bring up this dialog box to request the
         * user to turn on the corresponding function. If the current global switch status is on, the dialog box will not
         * be brought up.
         *
         * <!--RP5-->
         *
         * ![requestGlobalSwitch](docroot://reference/apis-ability-kit/figures/requestGlobalSwitch.png)
         *
         * <!--RP5End-->
         *
         * @param { Context } context - Context of the UIAbility or UIExtensionAbility that requests the global switch. If
         *     the context of another app, an invalid page, or a non-stage model is passed in, the API may report an error
         *     or fail to display the dialog box.
         * @param { SwitchType } type - Specifies the type of global switch to request to enable.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates the current global
         *     switch is enabled, and **false** indicates the current global switch is still disabled.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types.
         * @throws { BusinessError } 12100001 - Invalid parameter. Possible causes: 1. The context is invalid because
         *     it does not belong to the application itself; 2. The type of global switch is not supported.
         * @throws { BusinessError } 12100009 - Common inner error. An error occurs when creating the pop-up window
         *     or obtaining user operation result.
         * @throws { BusinessError } 12100013 - The specific global switch is already open.
         * @syscap SystemCapability.Security.AccessToken
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        requestGlobalSwitch(context: Context, type: SwitchType): Promise<boolean>;
        /**
         * Queries the permission status of the current app and returns the result synchronously. After the call is
         * successful, the status of the current permission is returned. Unlike
         * [checkAccessToken]{@link abilityAccessCtrl.AtManager.checkAccessToken}, this API does not require passing in the
         * app identity and is only used to query the permission status of the current app itself.
         *
         * Applicable to scenarios such as before determining whether to request a permission, confirming the authorization
         * result after a permission request, or re-querying after monitoring a permission status change.
         *
         * @param { Permissions } permissionName - Name of the permission whose status is to be queried. Passing an invalid
         *     value returns error code 12100001.
         *     <br>Value constraint: The permission name length cannot exceed 256 characters.
         * @returns { PermissionStatus } Permission status.
         * @throws { BusinessError } 12100001 - Invalid parameter. The permissionName is empty or exceeds 256 characters.
         * @throws { BusinessError } 12100007 - Service exception.
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @atomicservice
         * @since 20
         */
        getSelfPermissionStatus(permissionName: Permissions): PermissionStatus;
    }
    /**
     * Enumerates the permission grant states.
     *
     * @syscap SystemCapability.Security.AccessToken
     * @FaAndStageModel
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     */
    export enum GrantStatus {
        /**
         * The permission is not granted.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        PERMISSION_DENIED = -1,
        /**
         * The permission is granted.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        PERMISSION_GRANTED = 0
    }
    /**
     * Enumerates the results of the dialog box for redirection to the settings page.
     *
     * @syscap SystemCapability.Security.AccessToken
     * @stagemodelonly
     * @since 22
     */
    export enum SelectedResult {
        /**
         * The user chooses not to go to the settings.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @stagemodelonly
         * @since 22
         */
        REJECTED = -1,
        /**
         * The user chooses to go to the settings.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @stagemodelonly
         * @since 22
         */
        OPENED = 0,
        /**
         * The permission has been granted and no dialog box is displayed.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @stagemodelonly
         * @since 22
         */
        GRANTED = 1
    }
    /**
     * Enumerates the operations that trigger permission state changes.
     *
     * @syscap SystemCapability.Security.AccessToken
     * @FaAndStageModel
     * @atomicservice
     * @since 18
     */
    export enum PermissionStateChangeType {
        /**
         * Operation to revoke a permission.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @atomicservice
         * @since 18
         */
        PERMISSION_REVOKED_OPER = 0,
        /**
         * Operation to grant a permission.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @atomicservice
         * @since 18
         */
        PERMISSION_GRANTED_OPER = 1
    }
    /**
     * Represents the permission state change details.
     *
     * @syscap SystemCapability.Security.AccessToken
     * @FaAndStageModel
     * @atomicservice
     * @since 18
     * @name PermissionStateChangeInfo
     */
    interface PermissionStateChangeInfo {
        /**
         * Operation that triggers the permission state change.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @atomicservice
         * @since 18
         */
        change: PermissionStateChangeType;
        /**
         * ID of the subscribed application, which can be obtained through the
         * [accessTokenId]{@link ./bundleManager/ApplicationInfo:ApplicationInfo.accessTokenId} field in ApplicationInfo of
         * BundleInfo. <br>For BundleInfo acquisition, please refer to:
         * [bundleManager.getBundleInfoSync]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoSync}.
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @atomicservice
         * @since 18
         */
        tokenID: number;
        /**
         * Permissions whose authorization state changes. For details about the permissions, see
         * [Application Permissions](docroot://security/AccessToken/app-permissions.md).
         *
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @atomicservice
         * @since 18
         */
        permissionName: Permissions;
    }
    /**
     * Enumerates the permission states.
     *
     * @syscap SystemCapability.Security.AccessToken
     * @FaAndStageModel
     * @atomicservice
     * @since 20
     */
    export enum PermissionStatus {
        /**
         * The permission is not granted.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @atomicservice
         * @since 20
         */
        DENIED = -1,
        /**
         * The permission is granted.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @atomicservice
         * @since 20
         */
        GRANTED = 0,
        /**
         * Indicates not operated. The app declares a [user authorization permission]{@link permissions:Permissions} but has
         * not yet called the [requestPermissionsFromUser]{@link abilityAccessCtrl.AtManager.requestPermissionsFromUser}
         * API to request authorization, or the user has changed the permission status to asking eve
         * this value is returned when querying the permission status.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @atomicservice
         * @since 20
         */
        NOT_DETERMINED = 1,
        /**
         * The permission is invalid. The application does not
         * [declare permissions](docroot://security/AccessToken/declare-permissions.md) or cannot process the request. For
         * example, if the status of the approximate location permission is **NOT_DETERMINED**, this value will be returned
         * when the status of the precise location permission is queried.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @atomicservice
         * @since 20
         */
        INVALID = 2,
        /**
         * Indicates restricted. <!--RP2-->The app is prohibited from requesting user authorization through the
         * [requestPermissionsFromUser]{@link abilityAccessCtrl.AtManager.requestPermissionsFromUser} API. <!--RP2End-->
         *
         * @syscap SystemCapability.Security.AccessToken
         * @FaAndStageModel
         * @atomicservice
         * @since 20
         */
        RESTRICTED = 3
    }
    /**
     * Enumerates the global switch types.
     *
     * @syscap SystemCapability.Security.AccessToken
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    export enum SwitchType {
        /**
         * Global switch of the camera.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        CAMERA = 0,
        /**
         * Global switch of the microphone.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        MICROPHONE = 1,
        /**
         * Global switch of the location service.
         *
         * @syscap SystemCapability.Security.AccessToken
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        LOCATION = 2
    }
}
export { Permissions };
/**
 * Permission request result object, containing information such as the list of requested permission names, the
 * authorization result of each permission, the dialog box display result, and the failure reason.
 *
 * @syscap SystemCapability.Security.AccessToken
 * @stagemodelonly
 * @crossplatform
 * @atomicservice [since 11]
 * @since 10
 */
export type PermissionRequestResult = _PermissionRequestResult;
/**
 * Provides the context for the ability or application, which can be used to access application resources.
 *
 * @syscap SystemCapability.Security.AccessToken
 * @stagemodelonly
 * @crossplatform
 * @atomicservice [since 11]
 * @since 10
 */
export type Context = _Context;
export default abilityAccessCtrl;

```
