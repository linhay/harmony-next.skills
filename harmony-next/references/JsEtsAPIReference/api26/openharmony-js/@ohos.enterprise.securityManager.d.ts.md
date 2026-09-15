# @ohos.enterprise.securityManager.d.ts

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
 * @file Security Management
 * @kit MDMKit
 */
/**
 * This module provides enterprise device security management capabilities, including certificate management, device
 * security policy management, password policy management, clipboard policy management, watermark policy management, and
 * permission management. Enterprises can use this module to monitor the device security status in real time, manage the
 * lifecycle of enterprise certificates, configure device password policies in a unified manner, control the use of the
 * app clipboard, set screen and app watermarks to prevent information leakage, and implement refined management of app
 * permissions. This helps enterprises enhance device security protection capabilities and reduce data leakage risks.
 *
 * > **NOTE**
 * >
 * > The APIs of this module can be called only by a device administrator application that is enabled. For details, see
 * > [MDM Kit Development](docroot://mdm/mdm-kit-guide.md).
 *
 * @syscap SystemCapability.Customization.EnterpriseDeviceManager
 * @stagemodelonly
 * @since 12
 */
declare namespace securityManager {
    /**
     * Represents the certificate information.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    export interface CertBlob {
        /**
         * Binary content of the certificate.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        inData: Uint8Array;
        /**
         * Certificate alias. The value length must be less than 40 characters.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        alias: string;
    }
    /**
     * Defines watermark properties.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    export interface WatermarkProperties {
        /**
         * Number of rows for displaying the watermark.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        intervalsRow: number;
        /**
         * Number of columns for displaying the watermark.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        intervalsCol: number;
    }
    /**
     * Represents the management status of application permissions.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    export enum PermissionManagedState {
        /**
         * This permission is denied silently.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 20
         */
        DENIED = -1,
        /**
         * This permission is granted silently.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 20
         */
        GRANTED = 0,
        /**
         * The permission is granted by the user by default.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 20
         */
        DEFAULT = 1
    }
    /**
     * Application instance
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    export interface ApplicationInstance {
        /**
         * The [unique identifier]{@link ./bundleManager/BundleInfo:SignatureInfo} of an application. If an application does
         * not have **appIdentifier**, **appId** can be used instead. Both **bundleInfo.signatureInfo.appIdentifier** and
         * **bundleInfo.signatureInfo.appId** can be obtained via the
         * [bundleManager.getBundleInfo]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfo} API.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 20
         */
        appIdentifier: string;
        /**
         * User ID, which must be greater than or equal to 0. You can call
         * [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
         * **@ohos.account.osAccount** to obtain the user ID.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 20
         */
        accountId: number;
        /**
         * Index of the application clone. The default value is **0**.
         *
         * If **appIndex** is set to **0**, the main application is used. If **appIndex** is set to a value greater than 0,
         * the application clone with the specified index is used.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 20
         */
        appIndex: number;
    }
    /**
     * Enumerates the encryption algorithms used to process password data.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    export enum PasswordAlgs {
        /**
         * SCRYPT-HKDF-AES combined encryption algorithm.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        SCRYPT_HKDF_AES = 0,
        /**
         * SCRYPT-HKDF-SM4 combined encryption algorithm.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        SCRYPT_HKDF_SM4 = 1
    }
    /**
     * Obtains the security status of the current device. This API is applicable to scenarios such as device compliance
     * check, security status audit, and policy execution effect verification, helping enterprise administrators determine
     * whether devices meet security requirements. Enterprises can use this API to monitor the security patch status and
     * file encryption status of devices in real time, enabling timely detection of device security risks and prompt
     * action to protect enterprise devices and data.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } item - Type of the security status to obtain.
     *     <br>- **patch**: device security patch.
     *     <br>- **encryption**: device file system encryption.
     * @returns { string } Security status obtained.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function getSecurityStatus(admin: Want, item: string): string;
    /**
     * Installs a user certificate. This API uses a promise to return the result. Enterprises can use this API to install
     * certificates on devices in scenarios such as enterprise VPN connection, security authentication, and digital
     * signatures, implementing enterprise-level secure communication and data protection.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_CERTIFICATE
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { CertBlob } certificate - Certificate information. The certificate file must be stored in the path that the
     *     app has the permission to access, such as the app sandbox path. For details about the mapping between the app
     *     sandbox path and the actual physical path, see
     *     [Mappings Between App Sandbox Paths and Physical Paths](docroot://file-management/app-sandbox-directory.md#mappings-between-application-sandbox-paths-and-physical-paths).
     * @returns { Promise<string> } Promise used to return the URI of the installed certificate. This URI can be used to
     *     uninstall the certificate.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9201001 - Failed to manage the certificate.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function installUserCertificate(admin: Want, certificate: CertBlob): Promise<string>;
    /**
     * Installs a user certificate based on the system account. Enterprises can install independent certificates for
     * different user accounts, enabling security isolation and personalized certificate management in multi-user
     * environments, thus meeting the security control requirements of multi-user devices.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_CERTIFICATE
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { CertBlob } certificate - Certificate information. The certificate file must be stored in the path that the
     *     app has the permission to access, such as the app sandbox path. For details about the mapping between the app
     *     sandbox path and the actual physical path, see
     *     [Mappings Between App Sandbox Paths and Physical Paths](docroot://file-management/app-sandbox-directory.md#mappings-between-application-sandbox-paths-and-physical-paths).
     * @param { number } accountId - User ID, which must be greater than or equal to 0. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @returns { string } URI of the installed certificate, which is used to uninstall the certificate.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9201001 - Failed to manage the certificate.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 18
     */
    function installUserCertificate(admin: Want, certificate: CertBlob, accountId: number): string;
    /**
     * Uninstalls a user certificate. This API uses a promise to return the result. This API is applicable to enterprise
     * certificate management scenarios, such as replacing an expired certificate and revoking an employee's access to
     * enterprise resources. Enterprises can call this API to uninstall a certificate when the certificate expires, is
     * replaced, or is no longer needed, ensuring the flexibility and security of device certificate management.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_CERTIFICATE
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } certUri - Certificate URI, which is set and returned by the
     *     [installUserCertificate]{@link securityManager.installUserCertificate} API for installing a user certificate.
     * @returns { Promise<void> } Promise that returns no value. An error object is thrown when a user certificate fails
     *     to be uninstalled.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9201001 - Failed to manage the certificate.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function uninstallUserCertificate(admin: Want, certUri: string): Promise<void>;
    /**
     * Obtains the user certificate of a specified system account. Enterprises can use this API to query the list of user
     * certificates installed on a device for scenarios such as certificate audit and certificate validity period
     * management, ensuring traceability of certificate management.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_CERTIFICATE
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } accountId - User ID, which must be greater than or equal to 0. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @returns { Array<string> } All user certificates installed under the specified user ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 18
     */
    function getUserCertificates(admin: Want, accountId: number): Array<string>;
    /**
     * Sets the device screen lock password policy. After the policy is set, when a user sets a lock screen password, if
     * the password does not meet the requirements, a security prompt will be displayed asking the user to reset the
     * password. This policy is applicable to enterprise security compliance scenarios, such as requiring employees to use
     * strong passwords and change passwords periodically, to reduce the risk of enterprise data leakage.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { PasswordPolicy } policy - Device screen lock password policy.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200007 - The system ability works abnormally.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function setPasswordPolicy(admin: Want, policy: PasswordPolicy): void;
    /**
     * Obtains the device screen lock password policy.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { PasswordPolicy } Device screen lock password policy.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function getPasswordPolicy(admin: Want): PasswordPolicy;
    /**
     * Obtains the device screen lock password policy. Enterprises can use this API to query the current password policy
     * for policy audit and compliance check, ensuring that the device password policy complies with enterprise security
     * specifications.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { PasswordPolicy } Device screen lock password policy.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getPasswordPolicy(admin: Want | null): PasswordPolicy;
    /**
     * Sets the device clipboard policy. After the policy is set, applications will be restricted in their clipboard usage
     * according to the configured policy. This API is applicable to enterprise data leakage prevention scenarios, such as
     * restricting clipboard usage for sensitive applications (such as enterprise email and financial systems) to prevent
     * sensitive data from being copied to unauthorized applications, thereby reducing the risk of data leakage.
     * Enterprises can use this API to control application clipboard usage permissions, preventing sensitive data from
     * being leaked to unauthorized applications via the clipboard, and enhancing enterprise data security protection
     * capabilities.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } tokenId - Application token ID, which can be obtained using
     *     [bundleManager.getApplicationInfo]{@link ./bundleManager/ApplicationInfo}.
     * @param { ClipboardPolicy } policy - Clipboard policy to set.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function setAppClipboardPolicy(admin: Want, tokenId: number, policy: ClipboardPolicy): void;
    /**
     * Obtains the device clipboard policy.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } [tokenId] - Application token ID, which can be obtained using
     *     [bundleManager.getApplicationInfo]{@link ./bundleManager/ApplicationInfo}.
     * @returns { string } Device clipboard policy in JSON format.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function getAppClipboardPolicy(admin: Want, tokenId?: number): string;
    /**
     * Obtains the device clipboard policy. Enterprises can use this API to query the current clipboard policy for policy
     * audit and compliance check, ensuring that the clipboard policy complies with enterprise security requirements.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { number } [tokenId] - Application token ID, which can be obtained using
     *     [bundleManager.getApplicationInfo]{@link ./bundleManager/ApplicationInfo}.
     * @returns { string } Device clipboard policy in JSON format.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getAppClipboardPolicy(admin: Want | null, tokenId?: number): string;
    /**
     * Sets the device clipboard policy of a specified application for a specified user. After the policy is set, the
     * clipboard of the specified application will be restricted in its usage scope according to the configured policy.
     * Enterprises can configure differentiated clipboard usage permissions for different applications across different
     * users, enabling fine-grained data access control and meeting the security management requirements in multi-user,
     * multi-application scenarios.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Bundle name of the application for which the device clipboard policy is set.
     * @param { number } accountId - User ID, which must be greater than or equal to 0. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @param { ClipboardPolicy } policy - Clipboard policy to set.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 18
     */
    function setAppClipboardPolicy(admin: Want, bundleName: string, accountId: number, policy: ClipboardPolicy): void;
    /**
     * Obtains the device clipboard policy of a specified application for a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Bundle name of the application for which the device clipboard policy is set.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the account ID.
     * @returns { string } Device clipboard policy in JSON format.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 18
     */
    function getAppClipboardPolicy(admin: Want, bundleName: string, accountId: number): string;
    /**
     * Obtains the device clipboard policy of a specified application for a specified user. Enterprises can use this API
     * to query the clipboard usage permission configuration of a specific application for policy audit and compliance
     * check.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { string } bundleName - Bundle name of the application for which the device clipboard policy is set.
     * @param { number } accountId - User ID, which must be greater than or equal to 0. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @returns { string } Device clipboard policy in JSON format.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getAppClipboardPolicy(admin: Want | null, bundleName: string, accountId: number): string;
    /**
     * Sets a watermark policy for a specified application of a specified user. Currently, a maximum of 100 policies can
     * be saved.
     *
     * > **NOTE**
     * >
     * > 1. This API is intended for setting watermarks on third-party applications in enterprise scenarios to reduce the
     * > risk of information leakage. You are not advised to set watermarks for system applications (such as the home
     * > screen application), as unknown exceptions may occur.
     * >
     * > 2. The watermark image will be tiled repeatedly to cover the entire application interface.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Bundle name of the application for which the watermark is set.
     * @param { string | image.PixelMap } source - **string** indicates the image path, which is the path that the app has
     *     the permission to access, such as the app sandbox path. For details about the mapping between the app sandbox
     *     path and the actual physical path, see
     *     [Mappings Between App Sandbox Paths and Physical Paths](docroot://file-management/app-sandbox-directory.md#mappings-between-application-sandbox-paths-and-physical-paths).
     *     <br>**image.PixelMap** indicates the image object.
     *     <br>The size of the image pixel data cannot exceed 500 KB.
     *     <br>The size of the image pixel data is calculated as follows: Image width (pixels) × Image height (pixels) ×
     *     Number of bytes per pixel (typically 4). For example, the size of a 100 × 100 image is 100 × 100 × 4 = 40,000
     *     bytes.
     * @param { number } accountId - User ID. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     */
    function setWatermarkImage(admin: Want, bundleName: string, source: string | image.PixelMap, accountId: number): void;
    /**
     * Cancels the watermark policy for a specified user. When an application no longer requires watermark protection or
     * needs to be updated, enterprises can call this API to cancel the watermark policy.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Bundle name of the application for which the watermark is removed.
     * @param { number } accountId - User ID. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     */
    function cancelWatermarkImage(admin: Want, bundleName: string, accountId: number): void;
    /**
     * Represents a device screen lock password policy.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    export interface PasswordPolicy {
        /**
         * Regular expression for password complexity.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        complexityRegex?: string;
        /**
         * Password validity period, in ms.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        validityPeriod?: number;
        /**
         * Password complexity description, for example, "The password must contain 8 to 30 characters consisting of
         * letters, digits, and special characters".
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        additionalDescription?: string;
        /**
         * Encryption algorithm used to process password data. After the setting, the encryption algorithm specified by this
         * parameter is used to process the original password into a password credential on a PC/2-in-1 device. This
         * parameter has no effect on other device types.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        passwordAlgs?: PasswordAlgs;
    }
    /**
     * Represents a device clipboard policy.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    export enum ClipboardPolicy {
        /**
         * Default policy, which indicates no policy.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        DEFAULT = 0,
        /**
         * Allow the clipboard to be used in the same application.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        IN_APP = 1,
        /**
         * Allow the clipboard to be used on the same device.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        LOCAL_DEVICE = 2,
        /**
         * Allow the clipboard to be used across devices.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        CROSS_DEVICE = 3
    }
    /**
     * Sets a watermark policy for a specified application of a specified user. Currently, a maximum of 100 policies can
     * be saved.
     *
     * > **NOTE**
     * >
     * > This API is intended for setting watermarks on third-party applications in enterprise scenarios to reduce the
     * > risk of information leakage. You are not advised to set watermarks for system applications (such as the home
     * > screen application), as unknown exceptions may occur.
     * >
     * > The row and column parameters in the watermark [properties]{@link securityManager.WatermarkProperties} must be
     * > integers in the range [1, 255]. If a value less than 1 or greater than 255 is passed, the API returns error code
     * > 9200012.
     * >
     * > When both the row count and column count are set to **1**, a single watermark image is displayed at the center of
     * > the screen. When the row count is set to **m** and the column count to **n**, m × n watermark images are
     * > displayed in an m-by-n grid layout. If the specified row and column counts are too large for the grid layout to
     * > fit within the window, the watermark will be repeatedly tiled across the entire application window, starting from
     * > the top-left corner. Any part of the watermark image that exceeds the right or bottom edges of the window will be
     * > clipped. (For example, for a screen size of 1260 × 2720 pixels and a watermark image of 100 × 100 pixels, if the
     * > row count exceeds 27 or the column count exceeds 12, the watermark will be repeatedly tiled to cover the entire
     * > application window.)
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Bundle name of the application for which the watermark is set.
     * @param { string | image.PixelMap } source - **string** indicates the image path, which is the path that the app has
     *     the permission to access, such as the app sandbox path. For details about the mapping between the app sandbox
     *     path and the actual physical path, see
     *     [Mappings Between App Sandbox Paths and Physical Paths](docroot://file-management/app-sandbox-directory.md#mappings-between-application-sandbox-paths-and-physical-paths).
     *     <br>**image.PixelMap** indicates the image object.
     *     <br>The size of the image pixel data cannot exceed 500 KB.
     *     <br>The size of the image pixel data is calculated as follows: Image width (pixels) × Image height (pixels) ×
     *     Number of bytes per pixel (typically 4). For example, the size of a 100 × 100 image is 100 × 100 × 4 = 40,000
     *     bytes.
     * @param { number } accountId - User ID, which must be greater than or equal to 0. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @param { WatermarkProperties } properties - Number of rows and columns for the watermark.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function setWatermarkImage(admin: Want, bundleName: string, source: string | image.PixelMap, accountId: number, properties: WatermarkProperties): void;
    /**
     * Obtains the list of application bundle names for which watermarks have been set for a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } accountId - User ID, which must be greater than or equal to 0. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @returns { Array<string> } List of application bundle names for which watermarks have been set.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getWatermarkImageApps(admin: Want, accountId: number): Array<string>;
    /**
     * Sets the management policy for the [user_grant permission]{@link permissions:Permissions} of a specified
     * application. This is applicable to enterprise application batch deployment scenarios, such as granting permissions
     * silently to reduce permission prompt interruptions, and unifying permission management policies for enterprise
     * applications, thereby improving employee user experience and management efficiency.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USER_GRANT_PERMISSION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { ApplicationInstance } applicationInstance - Application instance.
     * @param { Array<string> } permissions - List of permissions to be managed. Only
     *     [user_grant permission]{@link permissions:Permissions} is supported. The list is grouped by
     *     [application permission groups](docroot://security/AccessToken/app-permission-group-list.md) and must include
     *     all permissions in the same permission group declared by the application in
     *     [module.json5](docroot://quick-start/module-configuration-file.md). For example, if an application declares
     *     ohos.permission.READ_CALENDAR and ohos.permission.WRITE_CALENDAR in **module.json5**, the input permission list
     *     must contain both ohos.permission.READ_CALENDAR and ohos.permission.WRITE_CALENDAR.
     * @param { PermissionManagedState } managedState - Management policy for application permissions.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function setPermissionManagedState(admin: Want, applicationInstance: ApplicationInstance, permissions: Array<string>, managedState: PermissionManagedState): void;
    /**
     * Obtains the management policy for the [user_grant permission]{@link permissions:Permissions} of a specified
     * application.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USER_GRANT_PERMISSION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { ApplicationInstance } applicationInstance - Application instance.
     * @param { string } permission - Name of the permission required for obtaining the management policy. Only the
     *     **user_grant** permission is supported.
     * @returns { PermissionManagedState } Management policy for application permissions.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function getPermissionManagedState(admin: Want, applicationInstance: ApplicationInstance, permission: string): PermissionManagedState;
    /**
     * Sets the management policy for extensions from external sources. After the policy is set, the system controls the
     * running behavior of extensions from external sources based on the configured policy. This API is applicable to
     * enterprise security management scenarios, such as preventing employees from installing unauthorized browser
     * extensions or forcibly enabling enterprise-approved extension functions to ensure enterprise device security.
     *
     * - DEFAULT:
     *
     *  Default policy with no restrictions applied. Users can enable or disable **Run extensions from external sources**
     * in **Settings** > **Privacy & security** > **Advanced option**.
     * - DISALLOW:
     *
     *  Policy that disallows extensions from external sources to run. With this policy, currently running extensions can
     * continue, but cannot be started after being closed. Users cannot enable **Run extensions from external sources**.
     * - FORCE_OPEN:
     *
     *  Policy that forcibly enables extensions from external sources to run. Users cannot disable
     * **Run extensions from external sources**.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { common.ManagedPolicy } policy - Management policy.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 22
     */
    function setExternalSourceExtensionsPolicy(admin: Want, policy: common.ManagedPolicy): void;
    /**
     * Obtains the management policy for extensions from external sources.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { common.ManagedPolicy } Management policy obtained.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 22
     */
    function getExternalSourceExtensionsPolicy(admin: Want): common.ManagedPolicy;
    /**
     * Obtains the management policy for extensions from external sources.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { common.ManagedPolicy } Management policy obtained.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getExternalSourceExtensionsPolicy(admin: Want | null): common.ManagedPolicy;
    /**
     * Installs the enterprise application re-signing certificate. After the installation is successful, the enterprise
     * can use the certificate to re-sign applications.
     *
     * A maximum of 10 distinct certificates can be deployed per user. The certificate alias serves as a unique identifier
     * for each certificate and cannot be duplicated during deployment. To update a certificate with an existing alias,
     * you must first uninstall the old certificate by calling
     * [uninstallEnterpriseReSignatureCertificate]{@link securityManager.uninstallEnterpriseReSignatureCertificate}.
     *
     * The installed certificates are retained on the device and will not be removed when the MDM app is uninstalled or
     * the admin privilege is deactivated.
     *
     * In the enterprise app distribution scenario, you can use the re-signing certificate to re-
     * sign enterprise apps. After re-signing, the app package is provided to enterprise administrators, who can then
     * install the re-signed app on enterprise devices where the corresponding re-signing certificate has been deployed.
     *
     * Process of using the enterprise application re-signing certificate:
     *
     * 1. Install the enterprise application re-signing certificate through the MDM application.
     * 2. Re-sign the original HAP package using a signing tool (**ohos-signer** or the DevEco Studio signing plugin).
     * 3. Install the re-signed app (through the enterprise private app store).
     * 4. Launch and run the app.
     *
     * Specifications:
     *
     * 1. Apps signed with the old certificate will continue to run normally after a new re-signing certificate is
     * installed.
     * 2. After a new enterprise signing certificate is installed for an installed enterprise app, if the installed app
     * needs to be updated, you can directly overwrite the original app without uninstalling it.
     * 3. In enterprise scenarios (especially those involving information security), enterprises need to ensure that only
     * designated internal software and tools are installed and run on employees' mobile devices. The enterprise
     * application re-signing certificate, in conjunction with the system's application management and permission control
     * mechanisms (via a unified application ID), supports silent installation of enterprise applications, controlled
     * invocation of system capabilities, and restriction of application running scopes. This enables admission control
     * and security governance for enterprise software on managed devices.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } certificateAlias - Certificate alias, which must end with **.cer**.
     * @param { number } fd - Descriptor of an existing re-signing certificate file. The certificate file must be stored in
     *     the [app sandbox directory](docroot://file-management/app-sandbox-directory.md).
     * @param { number } accountId - User ID, which must be greater than or equal to 0. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 9201006 - The number of certificates has reached the limit.
     * @throws { BusinessError } 9201007 - The certificate is invalid.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 24
     */
    function installEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, fd: number, accountId: number): void;
    /**
     * Uninstalls the enterprise application re-signing certificate. After the enterprise re-signing certificate is
     * uninstalled, the applications signed using this certificate can run properly before the device is restarted, but
     * cannot run after the device is restarted.
     *
     * Usage scenarios:
     *
     * 1. Installing a new certificate: After a new certificate is installed via the
     * [installEnterpriseReSignatureCertificate]{@link securityManager.installEnterpriseReSignatureCertificate} API,
     * applications re-signed using the new certificate can run properly. If the application corresponding to the old
     * signing certificate is a super device administrator application, the application must be deactivated before the
     * certificate can be uninstalled. Otherwise, after the certificate is uninstalled, the application cannot be
     * uninstalled or run.
     * 2. Restoring a mistakenly deleted certificate: After a mistakenly deleted certificate is re-installed via the
     * [installEnterpriseReSignatureCertificate]{@link securityManager.installEnterpriseReSignatureCertificate} API,
     * re-signed applications can run normally without being affected.
     *
     * > **NOTE**
     * >
     * > Certificate deletion is typically performed in scenarios such as certificate expiration or certificate leakage.
     * > You are advised to implement this feature with a strong prompt to administrators, advising them to delete
     * > certificates with caution. Before deleting a certificate, ensure that a new re-signing certificate has been
     * > loaded and that all applications have been updated and switched to the new re-signing certificate. Otherwise,
     * > historically installed applications will fail to run after a device restart.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } certificateAlias - Certificate alias, which must end with **.cer**.
     * @param { number } accountId - User ID, which must be greater than or equal to 0. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 9201008 - The certificate does not exist.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 24
     */
    function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: number): void;
    /**
     * Sets a screen watermark policy, which takes effect for all users.
     *
     * > **NOTE**
     * >
     * > 1. The screen watermark policy tiles the configured image across the entire screen. It is advised to use an image
     * > with transparency to ensure that the device screen content remains visible.
     * >
     * > 2. If the watermark image size is smaller than the screen, the image will be stretched. If the watermark image
     * > size is larger than the screen, the image will be compressed. This implementation differs from the repeated
     * > tiling approach used for application-level watermarks.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { image.PixelMap } pixelMap - Image object. The image width must not exceed twice the screen width, and the
     *     image height must not exceed twice the screen height. The size of the image pixel data cannot exceed 128 MB.
     *     The size of the image pixel data is calculated as follows: Image width (pixels) × Image height (pixels) ×
     *     Number of bytes per pixel (typically 4). For example, the size of a 100 × 100 image is 100 × 100 × 4 = 40,000
     *     bytes. For a 1920 × 1080 screen, using an image of the same resolution results in a pixel data size of 1920 × 1
     *     080 × 4 = 8,294,400 bytes (approximately 7.9 MB).
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function setScreenWatermarkImage(admin: Want, pixelMap: image.PixelMap): void;
    /**
     * Cancels a screen watermark policy, which takes effect for all users. After the cancellation is successful, the
     * watermark on the device screen disappears. When a device no longer requires screen watermark protection,
     * enterprises can call this API to cancel the watermark policy. Only the user who sets the screen watermark can
     * cancel it. For example, user 101 cannot cancel the screen mark set by user 100
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function cancelScreenWatermarkImage(admin: Want): void;
    /**
     * Disables the specified permission of the specified user. After the permission is disabled, all applications under
     * the specified user will be denied by default when applying for or using the specified permission. This API is
     * applicable to enterprise security compliance scenarios, such as disabling high-risk permissions like camera and
     * microphone to prevent privacy leaks, or disabling specific features (such as Bluetooth sharing) to prevent
     * enterprise data from being transferred out.
     *
     * > **NOTE**
     * >
     * > 1. Only permissions with an
     * > [APL level](docroot://security/AccessToken/app-permission-mgmt-overview.md#basic-concepts-in-the-permission-mechanism)
     * > of normal or system_basic can be disabled. Otherwise, error code 9201045 is returned.
     * >
     * > 2. A maximum of 200 permissions can be disabled per user.
     * >
     * > 3. After a permission is disabled, only applications (system and common applications) are affected. System SAs
     * > can still use the permission.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } permission - Name of the permission.
     * @param { boolean } disallow - Whether to disable the permission. The value **true** indicates yes, and the value
     *     **false** indicates no.
     * @param { number } accountId - User ID, which must be greater than or equal to 0. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 9201045 - This permission cannot be disallowed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function setDisallowedPermission(admin: Want, permission: string, disallow: boolean, accountId: number): void;
    /**
     * Obtains the list of disabled permissions of a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application. If the **admin** is **null**, the list
     *     of disabled permissions delivered by all enterprise device administrator applications is obtained, and the
     *     merged result is returned.
     * @param { number } accountId - User ID, which must be greater than or equal to 0. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @returns { Array<string> } List of disabled permissions.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getDisallowedPermissions(admin: Want | null, accountId: number): Array<string>;
    /**
     * Adds an application to the permission usage exception list. Applications in the list are not subject to the
     * permission restriction policy set via [setDisallowedPermission]{@link securityManager.setDisallowedPermission}.
     * This API is applicable to enterprise scenarios. For example, when the camera permission is disabled, attendance
     * applications and collaborative office applications can still use the camera, ensuring that critical enterprise
     * business operates normally.
     *
     * > **NOTE**
     * >
     * > 1. The permission must first be disabled via the
     * > [setDisallowedPermission]{@link securityManager.setDisallowedPermission} API before an application can be added
     * > to the permission usage exception list. Otherwise, error code 9201044 is returned.
     * >
     * > 2. An application cannot be added to the permission usage exception list if it has not actually requested the
     * > specified permission. For example, if the camera permission is disabled and application A has not requested the
     * > camera permission, it cannot be added to the exception list for the camera permission, and error code 9200012 is
     * > returned. You can use the [bm dump](docroot://tools/bm-tool.md#dump) command to check whether an application has
     * > requested a specific permission.
     * >
     * > 3. When a specified permission is enabled via the
     * > [setDisallowedPermission]{@link securityManager.setDisallowedPermission} API, the corresponding permission usage
     * > exception list is cleared synchronously.
     * >
     * > 4. For any given permission, a maximum of 1024 applications can be added to the exception list across all users.
     * >
     * > 5. Both system applications and third-party applications can be added.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } permission - Name of the permission.
     * @param { common.ApplicationInstance } applicationInstance - Information about the application instance to be added
     *     to the permission exception list.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 9201015 - The application is not installed.
     * @throws { BusinessError } 9201044 - This permission is not disallowed.
     *     Applications cannot be added to or removed from the trustlist.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function addAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void;
    /**
     * Removes an application from the permission usage exception list. After the application is removed, it cannot use
     * the corresponding permission any more.
     *
     * > **NOTE**
     * >
     * > The permission must first be disabled via the
     * > [setDisallowedPermission]{@link securityManager.setDisallowedPermission} API before an application can be removed
     * > from the permission usage exception list. Otherwise, error code 9201044 is returned.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } permission - Name of the permission.
     * @param { common.ApplicationInstance } applicationInstance - Information about the application instance to be
     *     removed from the permission exception list.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 9201044 - This permission is not disallowed.
     *     Applications cannot be added to or removed from the trustlist.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function removeAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void;
    /**
     * Obtains the list of applications in the permission exception list.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { string } permission - Name of the permission.
     * @param { number } accountId - User ID, which must be greater than or equal to 0. You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @returns { Array<common.ApplicationInstance> } List of applications in the permission exception list.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getAllowedPermissionBundles(admin: Want | null, permission: string, accountId: number): Array<common.ApplicationInstance>;
    /**
     * Disables or enables swipe-to-unlock for the current user. When enabled, the user must swipe on the screen after the
     * screen is turned on to access the home screen. When disabled, the screen goes directly to the home screen after
     * being turned on. This API is suitable for enterprise device management scenarios, such as disabling swipe-to-unlock
     * in specific security environments to simplify operations, or enabling it in general scenarios as a basic security
     * measure.
     *
     * > **NOTE**
     * >
     * > 1. This API takes effect only when no lock screen password is set on the device.
     * >
     * > 2. By default, swipe-to-unlock is enabled on the device.
     * >
     * > 3. If a lock screen password exists on the device, attempting to disable swipe-to-unlock will fail and return
     * > error code 9201021.
     * >
     * > 4. After a policy to disable swipe-to-unlock is applied, if the user subsequently sets a device password, the
     * > password will take effect and the device will require password verification before entering the home screen. In
     * > this case, the previously applied policy will no longer take effect.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { boolean } disable - Whether to disable swipe-to-unlock for the current user. The value **true** indicates
     *     yes, and the value **false** indicates no.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9201021 - A lock screen password has been set for the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function setScreenLockDisabledForAccount(admin: Want, disable: boolean): void;
    /**
     * Checks whether swipe-to-unlock is disabled for the current user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_SECURITY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { boolean } The value **true** indicates that swipe-to-unlock is disabled for the current user, and
     *     **false** indicates that it is enabled.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function isScreenLockDisabledForAccount(admin: Want): boolean;
}
import type Want from './@ohos.app.ability.Want';
import type common from './@ohos.enterprise.common';
import type image from './@ohos.multimedia.image';
export default securityManager;

```
