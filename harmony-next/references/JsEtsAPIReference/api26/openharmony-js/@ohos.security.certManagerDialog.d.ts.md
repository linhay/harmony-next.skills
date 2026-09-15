# @ohos.security.certManagerDialog.d.ts

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
 * @kit DeviceCertificateKit
 */
import type common from '@ohos.app.ability.common';
import type certificateManager from '@ohos.security.certManager';
/**
 * The **certificateManagerDialog** module provides APIs for opening the certificate management pages, on which you can
 * view and manage certificates (install, uninstall, and authorize certificates).
 *
 * @syscap SystemCapability.Security.CertificateManagerDialog
 * @stagemodelonly
 * @since 13
 */
declare namespace certificateManagerDialog {
    /**
     * Enumerates the error codes reported when the certificate management dialog box APIs are called.
     *
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 13
     */
    export enum CertificateDialogErrorCode {
        /**
         * Internal error.
         * For example, IPC communication failure, memory operation failure, and file operation failure.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 13
         */
        ERROR_GENERIC = 29700001,
        /**
         * The user canceled the operation in the certificate management dialog box.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 14
         */
        ERROR_OPERATION_CANCELED = 29700002,
        /**
         * The operation fails in the certificate management dialog box.
         * For example, the certificate fails to be installed.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 14
         */
        ERROR_OPERATION_FAILED = 29700003,
        /**
         * The device does not support the API called.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 14
         */
        ERROR_DEVICE_NOT_SUPPORTED = 29700004,
        /**
         * The device security policy is not met when the API is called.
         * For example, the device does not allow users to manage the CA certificate of GLOBAL_USER.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 18
         */
        ERROR_NOT_COMPLY_SECURITY_POLICY = 29700005,
        /**
         * The input parameter verification fails.
         *
         * For example, the parameter format is incorrect or the parameter range is invalid.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 22
         */
        ERROR_PARAMETER_VALIDATION_FAILED = 29700006,
        /**
         * No certificate is available.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 22
         */
        ERROR_NO_AVAILABLE_CERTIFICATE = 29700007
    }
    /**
     * Enumerates the page types of the certificate management dialog box.
     *
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 13
     */
    export enum CertificateDialogPageType {
        /**
         * Main page of the Certificate Manager application.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 13
         */
        PAGE_MAIN = 1,
        /**
         * CA certificate list page.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 13
         */
        PAGE_CA_CERTIFICATE = 2,
        /**
         * Credential list page.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 13
         */
        PAGE_CREDENTIAL = 3,
        /**
         * Certificate installation page.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 13
         */
        PAGE_INSTALL_CERTIFICATE = 4
    }
    /**
     * Opens the certificate management dialog box and displays the page of the specified type. After the interface is
     * invoked successfully, you can view, install, and uninstall the certificate in the dialog box that is displayed.
     * This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { common.Context } context - Context of the application.
     * @param { CertificateDialogPageType } pageType - Type of the page to display.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 29700001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 13
     */
    function openCertificateManagerDialog(context: common.Context, pageType: CertificateDialogPageType): Promise<void>;
    /**
     * Enumerates the types of the certificate to be installed.
     *
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 14
     */
    export enum CertificateType {
        /**
         * CA certificate.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 14
         */
        CA_CERT = 1,
        /**
         * User public credential.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 22
         */
        CREDENTIAL_USER = 2,
        /**
         * Private credential of an application.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 22
         */
        CREDENTIAL_APP = 3,
        /**
         * USB Key credential.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 22
         */
        CREDENTIAL_UKEY = 4,
        /**
         * System credential.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 23
         */
        CREDENTIAL_SYSTEM = 5
    }
    /**
     * Defines the usage scope of the certificate to be installed.
     *
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 14
     */
    export enum CertificateScope {
        /**
         * No user is specified.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 18
         */
        NOT_SPECIFIED = 0,
        /**
         * The installed certificate is accessible only to the current user.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 14
         */
        CURRENT_USER = 1,
        /**
         * The installed certificate is accessible to all users of the device.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 18
         */
        GLOBAL_USER = 2
    }
    /**
     * Opens the Certificate Management Install Certificate dialog box. After the certificate is successfully installed,
     * the unique identifier of the certificate is returned. Applications can use the identifier to use the certificate.
     * Use Promise asynchronous callback.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { common.Context } context - Context of the application.
     * @param { CertificateType } certType - Type of the certificate to install. **CA_CERT**, **CREDENTIAL_USER**, and
     *     **CREDENTIAL_SYSTEM** are currently supported.
     * @param { CertificateScope } certScope - Usage scope of the certificate to install. **CURRENT_USER** and
     *     **NOT_SPECIFIED** are currently supported.
     * @param { Uint8Array } cert - The certificate data. The size cannot exceed 8 KB. <br>When certType is set to
     *     CA_CERT, the certificate data must be in PEM or DER format. <br>When certType is set to CREDENTIAL_USER or
     *     CREDENTIAL_SYSTEM, the value must be in the P12 encoding format.
     * @returns { Promise<string> } Promise used to return the certificate URI. The value contains up to 256 bytes.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - The certificate management application Hap is not preinstalled in the system,
     *     and the capability is not supported. [since 26.0.0]
     * @throws { BusinessError } 29700001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 29700002 - The user cancels the installation operation.
     * @throws { BusinessError } 29700003 - The user install certificate failed in the certificate manager dialog, such as
     *     the certificate is in an invalid format.
     * @throws { BusinessError } 29700004 - For security purposes, the current device does not support this API.
     *     You can use the [supportsCACertDialog]{@link certificateManagerDialog.supportsCACertDialog} to determine
     *     whether the device supports opening the dialog box for installing a CA certificate with certType set to CA.
     * @throws { BusinessError } 29700005 - The operation does not comply with the device security policy, such as the
     *     device does not allow users to manage the CA certificate of the global user. [since 18]
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 14
     */
    function openInstallCertificateDialog(context: common.Context, certType: CertificateType, certScope: CertificateScope, cert: Uint8Array): Promise<string>;
    /**
     * Opens the authorization page of the certificate management dialog box to grant a credential to the application.
     * After the API is successfully called, the app can use the URI of the authorization certificate returned by the API
     * to sign, verify the signature, and query details.
     * This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { common.Context } context - Context of the application.
     * @returns { Promise<string> } Promise used to return the URI of the certificate authorized. The value contains up to
     *     256 bytes.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
     *     permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. A mandatory parameter is left
     *     unspecified.
     *     2. Incorrect parameter type. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - The certificate management application Hap is not preinstalled in the system,
     *     and the capability is not supported. [since 26.0.0]
     * @throws { BusinessError } 29700001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 29700002 - The user cancels the authorization.
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 20
     */
    function openAuthorizeDialog(context: common.Context): Promise<string>;
    /**
     * Opens the Certificate Management dialog box to display the certificate details. After the interface is invoked
     * successfully, detailed information about the certificate, such as the basic information, validity period, issuer,
     * and user, is displayed. Use Promise asynchronous callback.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { common.Context } context - Context of the application.
     * @param { Uint8Array } cert - The certificate Data.
     * @param { CertificateDialogProperty } property - Property of the certificate management dialog box.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 29700001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 29700003 - Show the certificate detail dialog failed, such as the certificate is in an
     *     invalid format.
     * @throws { BusinessError } 29700004 - The API is not supported on this device.
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 18
     */
    function openCertificateDetailDialog(context: common.Context, cert: Uint8Array, property: CertificateDialogProperty): Promise<void>;
    /**
     * Open the Certificate Management Uninstall Certificate dialog. The corresponding page is displayed. Use Promise
     * asynchronous callbacks.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { common.Context } context - Context of the application.
     * @param { CertificateType } certType - The type of the certificate to uninstall, only CA_CERT is supported.
     *     <br>Currently, only the CA_CERT type is supported.
     * @param { string } certUri - Unique identifier of the certificate to uninstall. You can obtain the certUri by using
     *     the API for installing a CA certificate or querying the CA certificate list.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 29700001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 29700002 - The user cancels the uninstallation operation.
     * @throws { BusinessError } 29700003 - The user uninstall certificate failed in the certificate manager dialog, such
     *     as the certificate uri is not exist.
     * @throws { BusinessError } 29700004 - For security purposes, the current device does not support this API.
     *     You can use the [supportsCACertDialog]{@link certificateManagerDialog.supportsCACertDialog} to determine
     *     whether the device can open the dialog box for deleting a CA certificate with certType set to CA.
     * @throws { BusinessError } 29700005 - The operation does not comply with the device security policy, such as the
     *     device does not allow users to manage the CA certificate of the global user.
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 18
     */
    function openUninstallCertificateDialog(context: common.Context, certType: CertificateType, certUri: string): Promise<void>;
    /**
     * Defines the property of the certificate management dialog box.
     *
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 18
     */
    export interface CertificateDialogProperty {
        /**
         * Whether to display the button for installing the certificate. The value **true** means to display the button; the
         * value **false** means the opposite.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 18
         */
        showInstallButton: boolean;
    }
    /**
     * Opens the Certificate Credential Authorization page of the Certificate Management dialog box. On the page that is
     * displayed, you can authorize the application to use certificate credentials. After the API is called successfully,
     * the app can use the URI of the authorization certificate returned by the API to sign, verify the signature, and
     * query details. The types of certificates that can be authorized include application certificate credentials, user
     * certificate credentials, and USB Key certificate credentials. Using Promise Asynchronous Callbacks.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { common.Context } context - Context of the application.
     * @param { AuthorizeRequest } authorizeRequest - Authorization request information.
     * @returns { Promise<CertReference> } Promise used to return the result of the authorization certificate reference.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
     *     permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 29700001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error; 4. Call other service failed. Please try again.
     * @throws { BusinessError } 29700002 - The user cancels the authorization.
     * @throws { BusinessError } 29700006 - Indicates that the input parameters validation failed.
     *     for example, the parameter format is incorrect or the value range is invalid.
     * @throws { BusinessError } 29700007 - No available certificate for authorization. Possible causes:
     *     1. No certificate matches the filter criteria;
     *     2. All certificates have been deleted.
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 22
     */
    function openAuthorizeDialog(context: common.Context, authorizeRequest: AuthorizeRequest): Promise<CertReference>;
    /**
     * Represents the authorization request information of the credentials.
     *
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 22
     */
    export interface AuthorizeRequest {
        /**
         * List of certificate types.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 22
         */
        certTypes: Array<CertificateType>;
        /**
         * Certificate usage.
         * If the **certTypes** parameter contains the **CertificateType.CREDENTIAL_UKEY** type, the **certPurpose**
         * parameter takes effect , indicating that the certificate credentials of the USB key are filtered based on the
         * specified certificate usage.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 22
         */
        certPurpose?: certificateManager.CertificatePurpose;
        /**
         * Indicates the algorithm type of the public key of the certificate. It is used to filter the list of
         * certificates that can be selected in the authorization dialog box. Only the certificates that match
         * the public key algorithm are displayed.
         * The value can only be RSA, EC, or ECDSA (case sensitive). If this parameter is not specified, certificates are
         * not filtered by algorithm type.
         * If the keyAlgIDs array contains an unsupported algorithm type,
         * the keyAlgIDs filter does not take effect.
         * The maximum length is 20.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 26.0.0
         */
        keyAlgIDs?: Array<string>;
        /**
         * Indicates the certificate issuer, which is encoded in DER format. This parameter is used to filter the list
         * of certificates that can be selected by users in the Authorization dialog box. Only the certificates that
         * match the certificate issuer are displayed.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 26.0.0
         */
        issuers?: Array<Uint8Array>;
        /**
         * This URI is displayed in the authorization dialog box and is used to provide the user with more context about
         * requesting authorization to use certificate credentials.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 26.0.0
         */
        uri?: string;
    }
    /**
     * Represents the reference information of the credential.
     *
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 22
     */
    export interface CertReference {
        /**
         * Certificate type.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 22
         */
        certType: CertificateType;
        /**
         * Unique identifier of the credential. The value contains up to 256 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 22
         */
        keyUri: string;
    }
    /**
     * Opens the PIN authentication dialog box of the USB Key credential. On the displayed page, the user can enter the
     * PIN to
     * authorize the USB credential. After the call is successful, the USB key credential will be unlocked. The app can
     * use the credential to perform operations such as signing and encryption. This API uses a promise to return the
     * result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { common.Context } context - Context of the application.
     * @param { UkeyAuthRequest } ukeyAuthRequest - Authentication request information of the USB Key credential
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
     *     permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 29700006 - Indicates that the input parameters validation failed.
     *     For example, the parameter format is incorrect or the value range is invalid.
     * @throws { BusinessError } 29700001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 29700002 - The user cancels the authentication operation.
     * @throws { BusinessError } 29700003 - The authentication operation failed, such as the USB key certificate
     *     does not exist, the USB key status is abnormal.
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 22
     */
    function openUkeyAuthDialog(context: common.Context, ukeyAuthRequest: UkeyAuthRequest): Promise<void>;
    /**
     * USB key PIN authentication request.
     *
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 22
     */
    export interface UkeyAuthRequest {
        /**
         * Unique identifier of the USB Key credential. The value contains up to 256 bytes.
         * The value of this parameter can be obtained from the CertReference returned by invoking the
         * [openAuthorizeDialog]{@link certificateManagerDialog.openAuthorizeDialog} interface.
         *
         * @syscap SystemCapability.Security.CertificateManagerDialog
         * @stagemodelonly
         * @since 22
         */
        keyUri: string;
    }
    /**
     * Check whether the device supports the [openCertificateDetailDialog]{@link
     * certificateManagerDialog.openCertificateDetailDialog}, [openInstallCertificateDialog]{@link
     * certificateManagerDialog.openInstallCertificateDialog}, and [openUninstallCertificateDialog]{@link
     * certificateManagerDialog.openUninstallCertificateDialog} interfaces to open the dialog box for managing CA
     * certificates.
     *
     * @returns { boolean } Whether the CA certificate management dialog box can be opened. **true**: supported; **false**
     *     : not supported
     * @throws { BusinessError } 29700001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @syscap SystemCapability.Security.CertificateManagerDialog
     * @stagemodelonly
     * @since 26.0.0
     */
    function supportsCACertDialog(): boolean;
}
export default certificateManagerDialog;

```
