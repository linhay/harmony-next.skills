# @ohos.dlpPermission.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2024 Huawei Device Co., Ltd.
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
 * @file DLP
 * @kit DataProtectionKit
 */
import type { AsyncCallback, Callback } from './@ohos.base';
import type common from './@ohos.app.ability.common';
import type Want from './@ohos.app.ability.Want';
/**
 * Data loss prevention (DLP) is a system solution provided to prevent data disclosure. This module provides APIs for
 * cross-device file access management, encrypted storage, and access authorization. DLP protects sensitive files
 * through encryption and generates encrypted files in .dlp format (DLP files). When opening a DLP file, the system
 * automatically creates an isolated DLP sandbox environment to ensure that the file content is not leaked to
 * unauthorized environments.
 *
 * > **NOTE**
 * >
 * > - The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a
 * > superscript to indicate their earliest API version.
 * >
 * > - The kit to which **@ohos.dlpPermission** belongs has been changed from `DataLossPreventionKit` to `
 * > DataProtectionKit`. You are advised to use the new module name `@
 * > kit.DataProtectionKit` to import the module. If `@
 * > kit.DataLossPreventionKit` is imported, only the APIs before the change can be called and the APIs after the change
 * > cannot be used.
 *
 * @syscap SystemCapability.Security.DataLossPrevention
 * @since 10
 */
declare namespace dlpPermission {
    /**
     * Enumerates the operations that can be performed on a DLP file. For example, the DLP sandbox application can dim
     * its button based on this parameter.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    export enum ActionFlagType {
        /**
         * View the file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        ACTION_VIEW = 0x00000001,
        /**
         * Save the file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        ACTION_SAVE = 0x00000002,
        /**
         * Save the file as another file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        ACTION_SAVE_AS = 0x00000004,
        /**
         * Edit the file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        ACTION_EDIT = 0x00000008,
        /**
         * Capture screenshots of the file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        ACTION_SCREEN_CAPTURE = 0x00000010,
        /**
         * Share the screen of the file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        ACTION_SCREEN_SHARE = 0x00000020,
        /**
         * Record the screen on which the file is open.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        ACTION_SCREEN_RECORD = 0x00000040,
        /**
         * Copy the file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        ACTION_COPY = 0x00000080,
        /**
         * Print the file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        ACTION_PRINT = 0x00000100,
        /**
         * Export the file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        ACTION_EXPORT = 0x00000200,
        /**
         * Modify the permissions on the file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        ACTION_PERMISSION_CHANGE = 0x00000400
    }
    /**
     * Enumerates the permissions on a DLP file.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    export enum DLPFileAccess {
        /**
         * The user has no permission on the file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        NO_PERMISSION = 0,
        /**
         * The user has only the permission to read the file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        READ_ONLY = 1,
        /**
         * Edit the file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        CONTENT_EDIT = 2,
        /**
         * The user has full control on the file.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        FULL_CONTROL = 3
    }
    /**
     * Represents the permission information about a DLP file.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    export interface DLPPermissionInfo {
        /**
         * User permission on the DLP file, for example, read-only.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        dlpFileAccess: DLPFileAccess;
        /**
         * Operations that can be performed on the DLP file. The value is a combination of different
         * [ActionFlagTypes]{@link dlpPermission.ActionFlagType}. If the value is out of range, error code 19100001 is
         * thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        flags: number;
    }
    /**
     * Represents the information about a DLP file opened.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    export interface AccessedDLPFileInfo {
        /**
         * URI of the DLP file. The value contains a maximum of 4095 bytes. If the value is out of range, error code
         * 19100001 is thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        uri: string;
        /**
         * Time when the file was last opened. The value must be greater than or equal to 0. Unit: s.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        lastOpenTime: number;
    }
    /**
     * Represents the sandbox retention information.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    export interface RetentionSandboxInfo {
        /**
         * Index of the DLP sandbox application. The value ranges from 1001 to 1100.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        appIndex: number;
        /**
         * Bundle name of the application. The value contains 7 to 128 bytes. If the value is out of range, error code
         * 19100001 is thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        bundleName: string;
        /**
         * URI list of the DLP files. The length of the array is not limited. Each string contains a maximum of 4095
         * bytes. If the string is out of range, error code 19100001 is thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 10
         */
        docUris: Array<string>;
    }
    /**
     * Checks whether a file is a DLP file based on the FD. This API uses a promise to return the result.
     *
     * During file processing, the system checks whether the file is a DLP file and then determines the subsequent
     * processing policy. For example, whether to open the file in a DLP sandbox.
     *
     * @param { number } fd - FD of the file to be checked. The value range is [0, 2<sup>31</sup>-1]. If the value of
     *     **fd** is less than 0, **false** is returned. If the value of **fd** is greater than 2<sup>31</sup>-1, the
     *     value is truncated.
     * @returns { Promise<boolean> } Returns {@code true} if {@link fd} is a DLP file; returns {@code false} otherwise.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function isDLPFile(fd: number): Promise<boolean>;
    /**
     * Checks whether a file is a DLP file based on the FD. After the API is successfully called, a result is returned.
     * The value **true** means the file is a DLP file; the value **false** means the opposite. This API uses an
     * asynchronous callback to return the result.
     *
     * During file processing, the system checks whether the file is a DLP file and then determines the subsequent
     * processing policy. For example, whether to open the file in a DLP sandbox.
     *
     * @param { number } fd - FD of the file to be checked. The value range is [0, 2<sup>31</sup>-1]. If the value of
     *     **fd** is less than 0, **false** is returned. If the value of **fd** is greater than 2<sup>31</sup>-1, the
     *     value is truncated.
     * @param { AsyncCallback<boolean> } callback - Callback used to receive the query result. The callback parameters
     *     include **err** and **res**. **err** is **undefined** when the query is successful; otherwise, **err** is an
     *     error object. If **true** is returned, **res** is a DLP file; if **false** is returned, **res** is not a DLP
     *     file.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function isDLPFile(fd: number, callback: AsyncCallback<boolean>): void;
    /**
     * Queries the permission information of the current DLP sandbox, including permissions on the file and operations
     * that can be performed (such as viewing, editing, and copying). This API can be called only in DLP sandbox
     * applications. This API uses a promise to return the result.
     *
     * When processing files in the DLP sandbox, the system determines the operations that can be performed for the
     * current user to prevent calling unauthorized capabilities.
     *
     * @returns { Promise<DLPPermissionInfo> } Promise used to return the permission information about the DLP file. The
     *     operation is successful if no error is reported.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100006 - No permission to call this API,
     *     which is available only for DLP sandbox applications.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function getDLPPermissionInfo(): Promise<DLPPermissionInfo>;
    /**
     * Obtains the permission information of this DLP file. The returned permission information includes permissions on
     * the file and operations that can be performed (such as viewing, editing, and copying). This API uses an
     * asynchronous callback to return the result.
     *
     * When processing files in the DLP sandbox, the system determines the operations that can be performed for the
     * current user to prevent calling unauthorized capabilities.
     *
     * @param { AsyncCallback<DLPPermissionInfo> } callback - Callback used to return the result. If the operation is
     *     successful, **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100006 - No permission to call this API,
     *     which is available only for DLP sandbox applications.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function getDLPPermissionInfo(callback: AsyncCallback<DLPPermissionInfo>): void;
    /**
     * Obtains the original name of a DLP file. This API returns the result synchronously.
     *
     * Determine the file type based on the original file name extension and select an application to open the file.
     *
     * @param { string } fileName - Name of the target DLP file. The value contains 1 to 255 bytes. If the value is out
     *     of range, error code 19100001 is thrown.
     * @returns { string } Original name of the DLP file obtained. For example, if the DLP file name is **test.txt.dlp**
     *     , the original file name returned is **test.txt**. The value contains up to 255 bytes.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function getOriginalFileName(fileName: string): string;
    /**
     * Obtains the DLP file name extension. After the API is called successfully, the DLP file name extension (for
     * example, .dlp) is returned. This API returns the result synchronously.
     *
     * This API is used to obtain the standard extension of the DLP file, which can be used to construct the DLP file
     * name or the determination of the file type.
     *
     * @returns { string } DLP file name extension obtained. For example, if the original file name is **test.txt**, the
     *     encrypted DLP file name is **test.txt.dlp**, and the returned extension is **.dlp**.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function getDLPSuffix(): string;
    /**
     * Subscribes to a DLP file open event. After this API is successfully called, a callback notification is sent to
     * the current application when the DLP file is opened. This API can be called only in non-DLP sandbox applications.
     *
     * You can subscribe to this event when your application needs to perform specific operations (such as logging and
     * updating the UI) after a DLP file is opened.
     *
     * @param { 'openDLPFile' } type - Event type. It has a fixed value of **openDLPFile**, which indicates the DLP file
     *     open event.
     * @param { Callback<AccessedDLPFileInfo> } listener - Callback invoked when a DLP file is opened. The application
     *     will be notified when the DLP file is opened.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100007 - No permission to call this API,
     *     which is available only for non-DLP sandbox applications.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function on(type: 'openDLPFile', listener: Callback<AccessedDLPFileInfo>): void;
    /**
     * Unsubscribes from the DLP file open event. This API can be called only in non-DLP sandbox applications. After the
     * API is successfully called, the application will no longer receive notifications for the DLP file open event.
     *
     * This API is usually called to release resources when the page is destroyed or the subscription is no longer
     * needed.
     *
     * @param { 'openDLPFile' } type - Event type. It has a fixed value of **openDLPFile**, which indicates the DLP file
     *     open event.
     * @param { Callback<AccessedDLPFileInfo> } listener - Callback for the DLP file open event. The application will
     *     not be notified when a DLP file is opened. By default, this parameter is left blank, which unregisters all
     *     callbacks for the file open event.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100007 - No permission to call this API,
     *     which is available only for non-DLP sandbox applications.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function off(type: 'openDLPFile', listener?: Callback<AccessedDLPFileInfo>): void;
    /**
     * Checks whether this application is running in a DLP sandbox environment. This API uses a promise to return the
     * result.
     *
     * This API is used to determine whether the current application is running in a DLP sandbox environment. If it is,
     * the system can perform operations or call APIs for sandbox applications.
     *
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** means the application is
     *     running in a sandbox; the value **false** means the opposite.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function isInSandbox(): Promise<boolean>;
    /**
     * Checks whether this application is running in a DLP sandbox environment. This API uses an asynchronous callback
     * to return the result.
     *
     * This API is used to determine whether the current application is running in a DLP sandbox environment. If it is,
     * the system can perform operations or call APIs for sandbox applications.
     *
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**. Otherwise, **err** is an error object. The value **true** means the application is
     *     running in a sandbox; the value **false** means the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function isInSandbox(callback: AsyncCallback<boolean>): void;
    /**
     * Obtains the file name extension types that support DLP. After the API is successfully called, the list of
     * supported file types is returned, indicating the types of files that can be used to generate DLP files. This API
     * uses a promise to return the result.
     *
     * This API is used to obtain the types of files that can be used to generate DLP files. If the current file type is
     * in the list, it can be encrypted.
     *
     * @returns { Promise<Array<string>> } Promise used to return the file name extension types obtained.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function getDLPSupportedFileTypes(): Promise<Array<string>>;
    /**
     * Obtains the file name extension types that support DLP. After the API is successfully called, the list of
     * supported file types is returned, indicating the types of files that can be used to generate DLP files. This API
     * uses an asynchronous callback to return the result.
     *
     * This API is used to obtain the types of files that can be used to generate DLP files. If the current file type is
     * in the list, it can be encrypted.
     *
     * @param { AsyncCallback<Array<string>> } callback - Callback used to return the result. If the operation is
     *     successful, **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function getDLPSupportedFileTypes(callback: AsyncCallback<Array<string>>): void;
    /**
     * Sets the retention state for sandbox applications. By default, when a DLP file is opened, the system
     * automatically creates a sandbox environment. After the file is closed, the sandbox is automatically destroyed.
     * After the retention state is set, the sandbox environment is retained even if the DLP file is closed, allowing
     * the system to quickly reopen the same DLP file. This is applicable to scenarios where the same DLP file needs to
     * be frequently operated, improving the file opening efficiency. This API uses a promise to return the result.
     *
     * @param { Array<string> } docUris - URIs of the files to be set with the retention state. The length of the array
     *     is not limited. Each string contains a maximum of 4095 bytes. If the string is out of range, error code
     *     19100001 is thrown.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100006 - No permission to call this API,
     *     which is available only for DLP sandbox applications.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function setRetentionState(docUris: Array<string>): Promise<void>;
    /**
     * Sets the retention state for sandbox applications. By default, when a DLP file is opened, the system
     * automatically creates a sandbox environment. After the file is closed, the sandbox is automatically destroyed.
     * After the retention state is set, the sandbox environment is retained even if the DLP file is closed, allowing
     * the system to quickly reopen the same DLP file. This is applicable to scenarios where the same DLP file needs to
     * be frequently operated, improving the file opening efficiency.
     *
     * @param { Array<string> } docUris - URIs of the files to be set with the retention state. The length of the array
     *     is not limited. Each string contains a maximum of 4095 bytes. If the string is out of range, error code
     *     19100001 is thrown.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100006 - No permission to call this API,
     *     which is available only for DLP sandbox applications.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function setRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void;
    /**
     * Cancels the sandbox retention state, that is, allows the sandbox application to be automatically uninstalled when
     * the DLP file is closed. This API uses a promise to return the result.
     *
     * This API is used to cancel the retention state for sandbox application and restore the default behavior to
     * release system resources. It is applicable to scenarios where the DLP file is no longer frequently accessed.
     *
     * @param { Array<string> } docUris - URIs of the files to be canceled with the retention state. The length of the
     *     array is not limited. Each string contains a maximum of 4095 bytes. If the string is out of range, error code
     *     19100001 is thrown.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function cancelRetentionState(docUris: Array<string>): Promise<void>;
    /**
     * Cancels the sandbox retention state, that is, allows the sandbox application to be automatically uninstalled when
     * the DLP file is closed. This API uses an asynchronous callback to return the result.
     *
     * This API is used to cancel the retention state for sandbox application and restore the default behavior to
     * release system resources. It is applicable to scenarios where the DLP file is no longer frequently accessed.
     *
     * @param { Array<string> } docUris - URIs of the files to be canceled with the retention state. The length of the
     *     array is not limited. Each string contains a maximum of 4095 bytes. If the string is out of range, error code
     *     19100001 is thrown.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function cancelRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void;
    /**
     * Obtains the sandbox applications in the retention state of an application. This API can be called only in non-DLP
     * sandbox applications. This API uses a promise to return the result.
     *
     * This API is used to query the sandbox retention information of a specified application, so that the sandbox
     * environment in the retention state can be checked or managed.
     *
     * @param { string } [bundleName] - Bundle name of the application, which is used to query the sandbox retention
     *     information of the application. This parameter is required when you need to query the sandbox retention
     *     information of another application. It is optional when you need to query the sandbox retention information
     *     of the current application. The value contains 7 to 128 bytes. If the value is out of range, error code
     *     19100001 is thrown.
     * @returns { Promise<Array<RetentionSandboxInfo>> } Promise used to return the sandbox retention information
     *     obtained.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100007 - No permission to call this API,
     *     which is available only for non-DLP sandbox applications.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function getRetentionSandboxList(bundleName?: string): Promise<Array<RetentionSandboxInfo>>;
    /**
     * Obtains the sandbox applications in the retention state of an application. This API uses an asynchronous callback
     * to return the result.
     *
     * This API is used to query the sandbox retention information of a specified application, so that the sandbox
     * environment in the retention state can be checked or managed.
     *
     * @param { string } bundleName - Bundle name of the application, which is used to query the sandbox retention
     *     information of the application. This parameter is required when you need to query the sandbox retention
     *     information of another application. It is optional when you need to query the sandbox retention information
     *     of the current application. The value contains 7 to 128 bytes. If the value is out of range, error code
     *     19100001 is thrown.
     * @param { AsyncCallback<Array<RetentionSandboxInfo>> } callback - Callback used to return the result. If the
     *     operation is successful, **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100007 - No permission to call this API,
     *     which is available only for non-DLP sandbox applications.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function getRetentionSandboxList(bundleName: string, callback: AsyncCallback<Array<RetentionSandboxInfo>>): void;
    /**
     * Obtains the sandbox applications in the retention state of an application. This API uses an asynchronous callback
     * to return the result.
     *
     * This API is used to query the sandbox retention information of a specified application, so that the sandbox
     * environment in the retention state can be checked or managed.
     *
     * @param { AsyncCallback<Array<RetentionSandboxInfo>> } callback - Callback used to return the result. If the
     *     operation is successful, **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100007 - No permission to call this API,
     *     which is available only for non-DLP sandbox applications.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function getRetentionSandboxList(callback: AsyncCallback<Array<RetentionSandboxInfo>>): void;
    /**
     * Obtains the list of DLP files that are accessed recently. After the API is successfully called, the file access
     * records are returned, which can be used to track and manage the usage of DLP files. This API can be called only
     * in non-DLP sandbox applications. This API uses a promise to return the result.
     *
     * This API is used to obtain the list of DLP files that are accessed recently, which can be used to track and
     * manage file usage.
     *
     * @returns { Promise<Array<AccessedDLPFileInfo>> } Promise used to return the list of recently accessed DLP files
     *     obtained.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100007 - No permission to call this API,
     *     which is available only for non-DLP sandbox applications.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function getDLPFileAccessRecords(): Promise<Array<AccessedDLPFileInfo>>;
    /**
     * Obtains the list of DLP files that are accessed recently. After the API is successfully called, the file access
     * records are returned, which can be used to track and manage the usage of DLP files. This API uses an asynchronous
     * callback to return the result.
     *
     * This API is used to obtain the list of DLP files that are accessed recently, which can be used to track and
     * manage file usage.
     *
     * @param { AsyncCallback<Array<AccessedDLPFileInfo>> } callback - Callback used to return the result. If the
     *     operation is successful, **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100007 - No permission to call this API,
     *     which is available only for non-DLP sandbox applications.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 10
     */
    function getDLPFileAccessRecords(callback: AsyncCallback<Array<AccessedDLPFileInfo>>): void;
    /**
     * Represents information about the trigger of the DLP manager application.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @StageModelOnly
     * @since 11
     */
    export interface DLPManagerResult {
        /**
         * Result code returned after the DLP manager application is started and exits. The value ranges from 0 to 3.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @StageModelOnly
         * @since 11
         */
        resultCode: number;
        /**
         * Data returned after the DLP manager application is started and exits.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @StageModelOnly
         * @since 11
         */
        want: Want;
    }
    /**
     * Starts the DLP manager application on the current
     * [UIAbility]{@link @ohos.app.ability.UIAbility:UIAbility} page in borderless
     * mode. This API uses a promise to return the result.
     *
     * This API starts the DLP manager application to configure file permissions and return the user operation result to
     * the caller.
     *
     * > **NOTE**
     * >
     * > This API can be called only by domain accounts.
     *
     * @param { common.UIAbilityContext } context -
     *     [UIAbility]{@link @ohos.app.ability.UIAbility:UIAbility} context.
     * @param { Want } want - Request object, which must contain the **uri** and **displayName** fields.
     * @returns { Promise<DLPManagerResult> } Promise used to return the **DLPManagerResult** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @throws { BusinessError } 19100016 - The uri field is missing in the want parameter.
     * @throws { BusinessError } 19100017 - The displayName field is missing in the want parameter.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @StageModelOnly
     * @since 11
     */
    function startDLPManagerForResult(context: common.UIAbilityContext, want: Want): Promise<DLPManagerResult>;
    /**
     * Enumerates the types of authorized accounts.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    export enum AccountType {
        /**
         * Cloud account.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        CLOUD_ACCOUNT = 1,
        /**
         * Domain account.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        DOMAIN_ACCOUNT = 2,
        /**
         * Enterprise account.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        ENTERPRISE_ACCOUNT = 4
    }
    /**
     * Represents the user authorization information.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    export interface AuthUser {
        /**
         * Account of the user who can access the DLP file. The value contains a maximum of 255 bytes. If the value is
         * out of range, error code 19100001 is thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        authAccount: string;
        /**
         * Type of the account.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        authAccountType: AccountType;
        /**
         * Permission granted to the user.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        dlpFileAccess: DLPFileAccess;
        /**
         * Time when the authorization expires. The value must be greater than or equal to 0. If the value is out of
         * range, error code 19100001 is thrown. Unit: s.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        permExpiryTime: number;
    }
    /**
     * Represents the authorization information.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    export interface DLPProperty {
        /**
         * Account of the owner who can set the permission. The value contains 1 to 255 bytes. If the value is out of
         * range, error code 19100001 is thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        ownerAccount: string;
        /**
         * Account ID of the owner. The value contains a maximum of 255 bytes. If the value is out of range, error code
         * 19100001 is thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        ownerAccountID: string;
        /**
         * Account type of the owner.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        ownerAccountType: AccountType;
        /**
         * List of users who are authorized to access the DLP file. By default, this parameter is left blank.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        authUserList?: Array<AuthUser>;
        /**
         * Account of the contact. The value contains 1 to 255 bytes. If the value is out of range, error code 19100001
         * is thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        contactAccount: string;
        /**
         * Whether the file can be accessed offline. **true**: yes; **false**: no.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        offlineAccess: boolean;
        /**
         * Permission granted to everyone. This parameter is left blank by default.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        everyoneAccessList?: Array<DLPFileAccess>;
        /**
         * Timestamp when the file permission has expired. This parameter is left blank by default. The value must be
         * greater than or equal to 0. If the value is out of range, an error code is thrown. Unit: s.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        expireTime?: number;
        /**
         * Whether the file can be opened after the permission expires (with the editing permission). This parameter is
         * valid only when **expireTime** is not empty. This parameter is left empty by default.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        actionUponExpiry?: ActionType;
        /**
         * System account ID. This parameter is left empty by default. The value contains a maximum of 255 bytes. If the
         * value is out of range, error code 19100001 is thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        fileId?: string;
        /**
         * Number of allowed opening times. This parameter is left empty by default. The value must be greater than or
         * equal to 0. If the value is out of range, error code 19100001 is thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        allowedOpenCount?: number;
        /**
         * Whether watermarks are required. **true**: yes; **false**: no. This parameter is left empty by default.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 23
         */
        waterMarkConfig?: boolean;
        /**
         * Validity period for file viewing, in seconds. After the validity period expires, the file is automatically
         * closed. This parameter is left empty by default. The value must be greater than or equal to 0. If the value
         * is out of range, error code 19100001 is thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @stagemodelonly
         * @since 23
         */
        countdown?: number;
        /**
         * Extended attribute of a DLP file. This parameter is left empty by default.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @stagemodelonly
         * @since 24
         */
        extensionFields?: Record<string, Object>;
    }
    /**
     * Sets the configuration information of the sandbox application. The configuration information is in JSON string
     * format and can be set by the application. After the API is successfully called, the sandbox application runs
     * based on the configuration information. This API uses a promise to return the result.
     *
     * This API sets the sandbox application configuration so that the application can pass custom parameters as
     * required.
     *
     * @param { string } configInfo - Sandbox application configuration. The value contains a maximum of 4,194,304
     *     bytes. If the value is out of range, error code 19100001 is thrown.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100007 - No permission to call this API,
     *     which is available only for non-DLP sandbox applications.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @throws { BusinessError } 19100018 - The application is not authorized.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 11
     */
    function setSandboxAppConfig(configInfo: string): Promise<void>;
    /**
     * Clears the sandbox application configuration. After the API is successfully called, the sandbox application
     * configuration is cleared and the default state is restored. This API uses a promise to return the result.
     *
     * This API clears the sandbox application configuration and restores the default state to prevent residual
     * configurations from affecting subsequent use.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100007 - No permission to call this API,
     *     which is available only for non-DLP sandbox applications.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @throws { BusinessError } 19100018 - The application is not authorized.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 11
     */
    function cleanSandboxAppConfig(): Promise<void>;
    /**
     * Obtains sandbox application configuration. This API uses a promise to return the result.
     *
     * This API obtains the sandbox application configuration, which can be used to read or verify the current
     * configuration status.
     *
     * @returns { Promise<string> } Promise used to return the result.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @throws { BusinessError } 19100018 - The application is not authorized.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 11
     */
    function getSandboxAppConfig(): Promise<string>;
    /**
     * Checks whether the current system provides the encryption protection feature. This API is available only for
     * enterprise devices and must be enabled by the [MDM](docroot://mdm/mdm-kit-intro.md) kit. After the API is
     * successfully called, the query result is returned, indicating whether the system supports DLP encryption. This
     * API uses a promise to return the result.
     *
     * This API checks whether the current system supports the DLP encryption function, so that compatibility processing
     * or function degradation can be performed on devices that do not support this function.
     *
     * > **NOTE**
     * >
     * > This API is enabled by the [MDM](docroot://mdm/mdm-kit-intro.md) kit and is used for enterprise devices. For
     * > other devices (such as consumer devices), this API is inapplicable. Calling it returns **false**.
     *
     * @returns { Promise<boolean> } Promise used to return the result.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 12
     */
    function isDLPFeatureProvided(): Promise<boolean>;
    /**
     * Enumerates the actions to be performed when the file's permission expiration time is reached. The default value
     * is **NOT_OPEN**.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    export enum ActionType {
        /**
         * Users are not allowed to open the DLP file when the file's permission expiration time is reached.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        NOT_OPEN = 0,
        /**
         * Logged-in accounts can still open and edit the DLP file when the file's permission expiration time is
         * reached.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        OPEN = 1
    }
    /**
     * Represents a custom policy.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    export interface CustomProperty {
        /**
         * JSON string of an enterprise custom policy. The value contains a maximum of 4,194,304 bytes. If the value is
         * out of range, error code 19100001 is thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        enterprise: string;
        /**
         * Query options about an enterprise DLP file. This parameter is left blank by default. **Since**: 26.0.0
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @stagemodelonly
         * @since 26.0.0
         */
        options?: DlpFileQueryOptions;
    }
    /**
     * Encrypts a plaintext file to generate a DLP file for an enterprise account. This API can be called only by
     * enterprise accounts. This API uses a promise to return the result.
     *
     * This API encrypts a plaintext file to generate a DLP file that can be accessed only by enterprise accounts,
     * implementing enterprise-level file permission management.
     *
     * > **NOTE**
     * >
     * > This API can be called only by enterprise accounts. Enterprises need to set up their own enterprise account
     * > servers. This API generates a DLP file, which is an encrypted file that can be accessed only by accounts
     * > authorized by the enterprise server.
     *
     * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE
     * @param { number } plaintextFd - FD of a plaintext file. The value range is [0, 2<sup>31</sup>-1]. If the value of
     *     **fd** is less than 0, error code 19100001 is thrown. If the value of **fd** is greater than 2<sup>31</sup>-1
     *     , the value is truncated.
     * @param { number } dlpFd - FD of an encrypted file. The value range is [0, 2<sup>31</sup>-1]. If the value of
     *     **fd** is less than 0, error code 19100001 is thrown. If the value of **fd** is greater than 2<sup>31</sup>-1
     *     , the value is truncated.
     * @param { DLPProperty } property - General policy of DLP files.
     * @param { CustomProperty } customProperty - Enterprise custom policy.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100002 - Credential service busy due to too many tasks or duplicate tasks.
     * @throws { BusinessError } 19100003 - Credential task time out.
     * @throws { BusinessError } 19100004 - Credential service error.
     * @throws { BusinessError } 19100005 - Credential authentication server error.
     * @throws { BusinessError } 19100009 - Failed to operate the DLP file.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @throws { BusinessError } 19100014 - Account not logged in.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    function generateDlpFileForEnterprise(plaintextFd: number, dlpFd: number, property: DLPProperty, customProperty: CustomProperty): Promise<void>;
    /**
     * Parses the file header in a DLP file to obtain the DLP plaintext policy. The returned JSON string of the DLP
     * policy contains the [DLPProperty]{@link dlpPermission.DLPProperty} and
     * [CustomProperty]{@link dlpPermission.CustomProperty} information. This API uses a promise to return the result.
     *
     * This API obtains the policy information of a DLP file for analysis in scenarios such as viewing the DLP file
     * permission configuration.
     *
     * > **NOTE**
     * >
     * > This API can be called only by enterprise accounts.
     *
     * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE
     * @param { number } dlpFd - FD of the DLP file to be queried. The value range is [0, 2<sup>31</sup>-1]. If the
     *     value of **fd** is less than 0, error code 19100001 is thrown. If the value of **fd** is greater than
     *     2<sup>31</sup>-1, the value is truncated.
     * @returns { Promise<string> } Promise used to return the JSON string of the DLP policy. The length cannot exceed
     *     4,194,304 bytes.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100002 - Credential service busy due to too many tasks or duplicate tasks.
     * @throws { BusinessError } 19100003 - Credential task time out.
     * @throws { BusinessError } 19100004 - Credential service error.
     * @throws { BusinessError } 19100005 - Credential authentication server error.
     * @throws { BusinessError } 19100008 - The file is not a DLP file.
     * @throws { BusinessError } 19100009 - Failed to operate the DLP file.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @throws { BusinessError } 19100013 - The user does not have the permission.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    function queryDlpPolicy(dlpFd: number): Promise<string>;
    /**
     * Decrypts a DLP file to generate a plaintext file. This API can be called only by enterprise accounts. This API
     * uses a promise to return the result.
     *
     * This API decrypts DLP files into plaintext files, which is applicable to exporting or migrating files by users
     * with owner permissions.
     *
     * > **NOTE**
     * >
     * > This API can be called only by enterprise accounts. Enterprises need to set up their own enterprise account
     * > servers. The enterprise server determines whether an account is authorized to decrypt DLP files.
     *
     * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE
     * @param { number } dlpFd - FD of the DLP file to be decrypted. The value range is [0, 2<sup>31</sup>-1]. If the
     *     value of **fd** is less than 0, error code 19100001 is thrown. If the value of **fd** is greater than
     *     2<sup>31</sup>-1, the value is truncated.
     * @param { number } plaintextFd - FD of the decrypted file. The value range is [0, 2<sup>31</sup>-1]. If the value
     *     of **fd** is less than 0, error code 19100001 is thrown. If the value of **fd** is greater than
     *     2<sup>31</sup>, the value is truncated.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100002 - Credential service busy due to too many tasks or duplicate tasks.
     * @throws { BusinessError } 19100003 - Credential task time out.
     * @throws { BusinessError } 19100004 - Credential service error.
     * @throws { BusinessError } 19100005 - Credential authentication server error.
     * @throws { BusinessError } 19100008 - The file is not a DLP file.
     * @throws { BusinessError } 19100009 - Failed to operate the DLP file.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @throws { BusinessError } 19100013 - The user does not have the permission.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    function decryptDlpFile(dlpFd: number, plaintextFd: number): Promise<void>;
    /**
     * Represents an enterprise custom policy.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    export interface EnterprisePolicy {
        /**
         * JSON string of an enterprise custom policy. The value contains a maximum of 4,194,304 bytes. If the value is
         * out of range, error code 19100001 is thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        policyString: string;
    }
    /**
     * Sets the protection policy for enterprise applications. After the API is successfully called, the DLP protection
     * for enterprise applications is implemented based on the configured policy.
     *
     * This API is used by the enterprise administrator to configure DLP security policies for unified management of
     * data security protection rules.
     *
     * > **NOTE**
     * >
     * > This API can be called only by enterprise accounts.
     *
     * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE
     * @param { EnterprisePolicy } policy - Enterprise application protection policy to be set. Access control and
     *     behavior restrictions of enterprise DLP files are implemented based on the policy.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @throws { BusinessError } 19100021 - Failed to set the enterprise policy.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    function setEnterprisePolicy(policy: EnterprisePolicy): void;
    /**
     * Registers the callback capability with the system ability (SA). This API is used in the **registerPlugin** API.
     *
     * > **NOTE**
     * >
     * > [registerPlugin]{@link dlpPermission.DlpConnManager.registerPlugin} requires identical parameters to this API.
     * > [connectServer]{@link dlpPermission.DlpConnPlugin.connectServer} is called by the SA and the parameters are
     * > returned through the callback.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    export interface DlpConnPlugin {
        /**
         * This API is called by the SA. After the request of connecting to the cloud server is processed, the result is
         * returned the SA using a callback.
         *
         * This API can be used in enterprise account authentication and cloud permission verification to enable
         * communication between the SA and the cloud server.
         *
         * > **NOTE**
         * >
         * > **connectServer** indicates a call from the system capability side to the frontend.
         *
         * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE [since 21 - 24]
         * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE [since 26.0.0]
         * @param { string } requestId - ID of the request transferred by the SA. No value range restriction is
         *     specified.
         * @param { string } requestData - Data transferred by the SA. No value range restriction is specified.
         * @param { Callback<string> } callback - API transferred by the SA, which is used for callback. No value range
         *     restriction is specified.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 19100011 - The system ability works abnormally.
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        connectServer(requestId: string, requestData: string, callback: Callback<string>): void;
    }
    /**
     * Calls **registerPlugin** and **unregisterPlugin** to register or unregister callback capabilities in the SA.
     *
     * > **NOTE**
     * >
     * > **registerPlugin** registers callback capabilities in the SA, and **unregisterPlugin** unregisters callback
     * > capabilities from the SA.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @since 21
     */
    export class DlpConnManager {
        /**
         * Represents a constructor for instantiating [DlpConnManager]{@link dlpPermission.DlpConnManager}.
         *
         * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE [since 21 - 24]
         * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE [since 26.0.0]
         * @throws { BusinessError } 201 - Permission denied.
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        constructor();
        /**
         * Registers a callback with the SA.
         *
         * > **NOTE**
         * >
         * > **registerPlugin** registers the callback with the SA.
         *
         * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE [since 21 - 24]
         * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE [since 26.0.0]
         * @param { DlpConnPlugin } plugin - Callback plugin object, which is used to register the callback capability
         *     with the SA. The **DlpConnPlugin** API needs to be inherited and the **connectServer** method needs to be
         *     implemented so that the processing result can be returned using a callback when the API is called on the
         *     SA.
         * @returns { number } Registration result. The unique ID of the callback is returned. The value range is
         *     [0, 2<sup>64</sup>-1].
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 19100001 - Invalid parameter value.
         * @throws { BusinessError } 19100002 - Credential service busy due to too many tasks or duplicate tasks.
         * @throws { BusinessError } 19100003 - Credential task time out.
         * @throws { BusinessError } 19100004 - Credential service error.
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        static registerPlugin(plugin: DlpConnPlugin): number;
        /**
         * Unregisters a callback from the SA.
         *
         * This API unregisters a callback and releases resources when an application exits, ensuring that the callback
         * capability is correctly released.
         *
         * > **NOTE**
         * >
         * > **unregisterPlugin** unregisters a plug-in from the SA.
         *
         * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE [since 21 - 24]
         * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE [since 26.0.0]
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 19100001 - Invalid parameter value.
         * @throws { BusinessError } 19100002 - Credential service busy due to too many tasks or duplicate tasks.
         * @throws { BusinessError } 19100003 - Credential task time out.
         * @throws { BusinessError } 19100004 - Credential service error.
         * @syscap SystemCapability.Security.DataLossPrevention
         * @since 21
         */
        static unregisterPlugin(): void;
    }
    /**
     * Queries the URIs of enterprise DLP files that have been opened and meet the specified options. This API uses a
     * promise to return the result.
     *
     * This API is called when the system needs to manage or track enterprise DLP files that have been opened by the
     * current application. It can be used in scenarios such as file status check and resource management.
     *
     * > **NOTE**
     * >
     * > - This API can only query enterprise DLP files generated by the caller application through
     * > [generateDlpFileForEnterprise]{@link dlpPermission.generateDlpFileForEnterprise}. Enterprise DLP files
     * > generated by other applications cannot be queried.
     * >
     * > - Read-only enterprise DLP files with the same classification label are opened in the same sandbox. If multiple
     * > such files are opened in a sandbox, the URIs of all files that have been opened (including manually closed
     * > files) are returned.
     *
     * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE
     * @param { DlpFileQueryOptions } [options] - Query options about an enterprise DLP file. This parameter is required
     *     when specific enterprise DLP files are queried by classification label. It is optional when all enterprise
     *     DLP files are queried. If this parameter is not passed or an empty string is passed, all enterprise DLP files
     *     are queried.
     * @returns { Promise<Array<string>> } Promise used to return the URI list of the target enterprise DLP files that
     *     have been opened.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @stagemodelonly
     * @since 26.0.0
     */
    function queryOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<Array<string>>;
    /**
     * Closes all opened enterprise DLP files that meet the specified options. This API uses a promise to return the
     * result.
     *
     * This API can be called to close enterprise DLP files in batches, clear file resources, or release file handles
     * before exiting the application.
     *
     * > **NOTE**
     * >
     * > This API can only close enterprise DLP files generated by the caller app through
     * > [generateDlpFileForEnterprise]{@link dlpPermission.generateDlpFileForEnterprise}.
     *
     * @permission ohos.permission.ENTERPRISE_ACCESS_DLP_FILE
     * @param { DlpFileQueryOptions } [options] - Query options about an enterprise DLP file. This parameter is passed
     *     when you need to disable specific enterprise DLP files by category tag. This parameter is not required when
     *     you need to disable all enterprise DLP files. If this parameter is not passed or an empty string is passed,
     *     all enterprise DLP files are closed.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @stagemodelonly
     * @since 26.0.0
     */
    function closeOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<void>;
    /**
     * Represents the query options about an enterprise DLP file.
     *
     * @syscap SystemCapability.Security.DataLossPrevention
     * @stagemodelonly
     * @since 26.0.0
     */
    export interface DlpFileQueryOptions {
        /**
         * User-defined classification label of an enterprise DLP file. The value contains a maximum of 255 bytes. If
         * the value is out of range, error code 19100001 is thrown.
         *
         * @syscap SystemCapability.Security.DataLossPrevention
         * @stagemodelonly
         * @since 26.0.0
         */
        classificationLabel?: string;
    }
    /**
     * Set the list of applications that are subject to enterprise DLP control.
     *
     * @permission ohos.permission.DLP_POLICY_MANAGER
     * @param { Array<string> } appLists - The appIdentifiers of applications to be put under controlled
     *     <br>The maximum length is 100.
     *     <br>The value range of Array is [0, 100], and the value range of String is [0, 4096].
     * @param { number } [userId] - The target userId for which the controlled app list is configured.
     *     If not specified, the current user is used by default
     *     <br>The value range is all integers.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 19100001 - Invalid parameter value.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @throws { BusinessError } 19100023 - The specified userId is inconsistent with the current userId.
     * @throws { BusinessError } 19100024 - The specified userId belongs to a personal space user and
     *     cannot be managed.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @stagemodelonly
     * @since 26.0.0
     */
    function setControlledAppLists(appLists: Array<string>, userId?: number): Promise<void>;
    /**
     * Obtain the list of applications that are subject to enterprise DLP control for the current user.
     *
     * @permission ohos.permission.DLP_POLICY_MANAGER
     * @returns { Promise<Array<string>> } Promise that returns the appIdentifiers of controlled application
     *     for the current user.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 19100011 - The system ability works abnormally.
     * @syscap SystemCapability.Security.DataLossPrevention
     * @stagemodelonly
     * @since 26.0.0
     */
    function getControlledAppLists(): Promise<Array<string>>;
}
export default dlpPermission;

```
