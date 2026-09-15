# @ohos.security.huksExternalCrypto.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
 * @file External Key Management
 * @kit UniversalKeystoreKit
 */
/**
 * Provides the functionalities such as registration and deregistration of external key management extension, PIN
 * authentication, and acquisition of authentication state.
 *
 * @syscap SystemCapability.Security.Huks.CryptoExtension
 * @since 22
 */
declare namespace huksExternalCrypto {
    /**
     * Enumerates the external encrypted data types.
     *
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @since 22
     */
    export enum HuksExternalCryptoTagType {
        /**
         * The tag value is an integer.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @since 22
         */
        HUKS_EXT_CRYPTO_TAG_TYPE_INT = 1 << 28,
        /**
         * The tag value is a byte array.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @since 22
         */
        HUKS_EXT_CRYPTO_TAG_TYPE_BYTES = 5 << 28
    }
    /**
     * Enumerates the tags used to invoke parameters.
     *
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @since 22
     */
    export enum HuksExternalCryptoTag {
        /**
         * Tag of the PIN.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @since 22
         */
        HUKS_EXT_CRYPTO_TAG_UKEY_PIN = HuksExternalCryptoTagType.HUKS_EXT_CRYPTO_TAG_TYPE_BYTES | 200001,
        /**
         * Name of [CryptoExtensionAbility]{@link @ohos.security.CryptoExtensionAbility}.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @since 22
         */
        HUKS_EXT_CRYPTO_TAG_ABILITY_NAME = HuksExternalCryptoTagType.HUKS_EXT_CRYPTO_TAG_TYPE_BYTES | 200002,
        /**
         * External data, which indicates the return data in the common query scenario.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @since 22
         */
        HUKS_EXT_CRYPTO_TAG_EXTRA_DATA = HuksExternalCryptoTagType.HUKS_EXT_CRYPTO_TAG_TYPE_BYTES | 200003,
        /**
         * UID of the caller.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @since 22
         */
        HUKS_EXT_CRYPTO_TAG_UID = HuksExternalCryptoTagType.HUKS_EXT_CRYPTO_TAG_TYPE_INT | 200004,
        /**
         * Usage type of the key corresponding to the certificate chain. For details, see
         * [CertificatePurpose]{@link @ohos.security.certManager:certificateManager.CertificatePurpose}.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @since 22
         */
        HUKS_EXT_CRYPTO_TAG_PURPOSE = HuksExternalCryptoTagType.HUKS_EXT_CRYPTO_TAG_TYPE_INT | 200005,
        /**
         * Specify the information required to obtain the resource ID. The format and content are defined by the provider.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @stagemodelonly
         * @since 26.0.0
         */
        HUKS_EXT_CRYPTO_TAG_RESOURCE_INFO = HuksExternalCryptoTagType.HUKS_EXT_CRYPTO_TAG_TYPE_BYTES | 200007,
        /**
         * Specifies the ability configuration for the custom PIN dialog.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @stagemodelonly
         * @since 26.0.0
         */
        HUKS_EXT_CRYPTO_TAG_ABILITY_INFO = HuksExternalCryptoTagType.HUKS_EXT_CRYPTO_TAG_TYPE_BYTES | 200008,
        /**
         * Specifies the hap bundle name of the crypto extension ability.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @stagemodelonly
         * @since 26.0.0
         */
        HUKS_EXT_CRYPTO_TAG_BUNDLE_NAME = HuksExternalCryptoTagType.HUKS_EXT_CRYPTO_TAG_TYPE_BYTES | 200009
    }
    /**
     * Enumerates the Ukey PIN authentication states.
     *
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @since 22
     */
    export enum HuksExternalPinAuthState {
        /**
         * The Ukey PIN is not authenticated.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @since 22
         */
        HUKS_EXT_CRYPTO_PIN_NO_AUTH = 0,
        /**
         * The Ukey PIN is authenticated successfully.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @since 22
         */
        HUKS_EXT_CRYPTO_PIN_AUTH_SUCCEEDED = 1,
        /**
         * The Ukey PIN is locked.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @since 22
         */
        HUKS_EXT_CRYPTO_PIN_LOCKED = 2
    }
    /**
     * Defines the type of the param array used for calling the API.
     *
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @since 22
     */
    export interface HuksExternalCryptoParam {
        /**
         * Parameter tag, which is used to distinguish parameters.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @since 22
         */
        tag: HuksExternalCryptoTag;
        /**
         * Value of the tag.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @since 22
         */
        value: boolean | number | bigint | Uint8Array;
    }
    /**
     * Defines detailed error information.
     *
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @stagemodelonly
     * @since 26.0.0
     */
    export interface HuksExternalErrorInfo {
        /**
         * The detailed error code.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @stagemodelonly
         * @since 26.0.0
         */
        errno: number;
        /**
         * The detailed error description.
         *
         * @syscap SystemCapability.Security.Huks.CryptoExtension
         * @stagemodelonly
         * @since 26.0.0
         */
        errorDesc: string;
    }
    /**
     * Registers a specified external Provider. This API uses a promise to return the result.
     *
     * @permission ohos.permission.CRYPTO_EXTENSION_REGISTER
     * @param { string } providerName - Provider name, which contains a maximum of 128 characters. It is recommended that
     *     the value contain the vendor information, be globally unique, and not contain sensitive data such as personal
     *     contact information.<br>A maximum of 10 providers can be registered.
     * @param { Array<HuksExternalCryptoParam> } params - Parameters to be passed during the operation. The mandatory tag
     *     is [HUKS_EXT_CRYPTO_TAG_ABILITY_NAME]{@link huksExternalCrypto.HuksExternalCryptoTagType}, indicating the
     *     ability name. Set this parameter based on the actual service requirements.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - check permission failed.
     * @throws { BusinessError } 801 - api is not supported.
     * @throws { BusinessError } 12000002 - the ability name param is missing.
     * @throws { BusinessError } 12000005 - IPC communication failed.
     * @throws { BusinessError } 12000014 - memory is insufficient.
     * @throws { BusinessError } 12000018 - the input parameter is invalid.
     * @throws { BusinessError } 12000019 - the provider is already registered.
     * @throws { BusinessError } 12000020 - an error occurred in the dependent module.
     * @throws { BusinessError } 12000025 - the number of providers exceeds the limit.
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @since 22
     */
    function registerProvider(providerName: string, params: Array<HuksExternalCryptoParam>): Promise<void>;
    /**
     * Unregisters a specified external Provider. This API uses a promise to return the result.
     *
     * @permission  ohos.permission.CRYPTO_EXTENSION_REGISTER
     * @param { string } providerName - Provider name, which contains a maximum of 128 characters. It is recommended that
     *     the value contain the vendor information, be globally unique, and not contain sensitive data such as personal
     *     contact information. If a provider has registered multiple extension capabilities, all the extension
     *     capabilities of the provider will be unregistered.
     * @param { Array<HuksExternalCryptoParam> } [params] - Parameters to be passed during the operation.<br>You can
     *     specify [HUKS_EXT_CRYPTO_TAG_ABILITY_NAME]{@link huksExternalCrypto.HuksExternalCryptoTagType} in the
     *     **params** parameter to unregister the corresponding **cryptoExtensionAbility** based on the bundle name,
     *     **providerName**, and **abilityName**.<br>If
     *     [HUKS_EXT_CRYPTO_TAG_ABILITY_NAME]{@link huksExternalCrypto.HuksExternalCryptoTagType} is not specified in the
     *     **params** parameter or the **params** parameter is not passed, all providers under the corresponding
     *     **providerName** are unregistered.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - check permission failed.
     * @throws { BusinessError } 801 - api is not supported.
     * @throws { BusinessError } 12000005 - IPC communication failed.
     * @throws { BusinessError } 12000011 - the provider is not found.
     * @throws { BusinessError } 12000012 - Device environment or input parameter is abnormal.
     *     This may happen for several reasons, such as the model already being unloaded.
     * @throws { BusinessError } 12000014 - memory is insufficient.
     * @throws { BusinessError } 12000018 - the input parameter is invalid.
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @since 22
     */
    function unregisterProvider(providerName: string, params?: Array<HuksExternalCryptoParam>): Promise<void>;
    /**
     * Obtains the PIN authentication state. This API uses a promise to return the result.
     *
     * @param { string } resourceId - Resource ID, which can be obtained using
     *     [certificateManagerDialog.openAuthorizeDialog22+]{@link @ohos.security.certManagerDialog:certificateManagerDialog.openAuthorizeDialog(context: common.Context, authorizeRequest: AuthorizeRequest)}
     *     . The result contains **resourceId**.
     * @param { Array<HuksExternalCryptoParam> } [params] - Operation parameters. If a non-system application passes
     *     [HUKS_EXT_CRYPTO_TAG_UID]{@link huksExternalCrypto.HuksExternalCryptoTagType}, the parameter is invalid.
     * @returns { Promise<HuksExternalPinAuthState> } Promise used to return the authentication result.
     *     <br>**HUKS_EXT_CRYPTO_PIN_NO_AUTH**: The PIN authentication fails. **HUKS_EXT_CRYPTO_PIN_AUTH_SUCCEEDED**: The PIN
     *     authentication is successful. **HUKS_EXT_CRYPTO_PIN_LOCKED**: The PIN is locked.
     * @throws { BusinessError } 801 - api is not supported.
     * @throws { BusinessError } 12000005 - IPC communication failed.
     * @throws { BusinessError } 12000006 - the UKey driver operation failed.
     * @throws { BusinessError } 12000011 - queried entity does not exist. This may happen
     *     because the resource ID has not been opened.
     * @throws { BusinessError } 12000012 - Device environment or input parameter is abnormal.
     *     This error may occur if the process function is not found, or due to other issues.
     * @throws { BusinessError } 12000014 - memory is insufficient.
     * @throws { BusinessError } 12000018 - the input parameter is invalid.
     * @throws { BusinessError } 12000020 - the provider operation failed.
     * @throws { BusinessError } 12000024 - the provider or UKey is busy.
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @since 22
     */
    function getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>;
    /**
     * Clear the PIN auth state of the specified resource ID.
     *
     * @param { string } resourceId - Indicates the resource ID of the provider.
     * @returns { Promise<void> } The promise returned by the function.
     * @throws { BusinessError } 801 - API is not supported.
     * @throws { BusinessError } 12000005 - IPC communication failed.
     * @throws { BusinessError } 12000006 - Failed to call the UKey driver interface.
     *     Please check the UKey connection and driver status.
     * @throws { BusinessError } 12000011 - The cached resource ID not found.
     * @throws { BusinessError } 12000012 - Device environment or input parameters are abnormal.
     *     This may occur if the process function is null, or due to other issues.
     * @throws { BusinessError } 12000014 - The memory is insufficient.
     * @throws { BusinessError } 12000018 - The input parameters are invalid. Possible causes:
     *     1. The resourceId length is invalid.
     * @throws { BusinessError } 12000020 - The provider operation failed.
     *     This means an error occurred in the crypto extension before calling the UKey driver interface.
     * @throws { BusinessError } 12000024 - The provider or UKey is busy.
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @stagemodelonly
     * @since 26.0.0
     */
    function clearUkeyPinAuthState(resourceId: string): Promise<void>;
    /**
     * Obtains a property value. This API uses a promise to return the result.
     *
     * The **propertyId** indicates the ID of the property to be queried. Currently, only the SKF API names defined in GMT
     * 0016-2023 can be used as property IDs. The supported IDs are as follows:
     *
     * - SKF_EnumDev
     * - SKF_GetDevInfo
     * - SKF_EnumApplication
     * - SKF_EnumContainer
     *
     * @param { string } resourceId - Resource ID, which can be obtained using
     *     [certificateManagerDialog.openAuthorizeDialog22+]{@link @ohos.security.certManagerDialog:certificateManagerDialog.openAuthorizeDialog(context: common.Context, authorizeRequest: AuthorizeRequest)}
     *     . The result contains **resourceId**.
     * @param { string } propertyId - Property name for the search operation, which is the SKF API name defined in GMT 001
     *     6-2023. You need to make adaptation based on the API name.
     * @param { Array<HuksExternalCryptoParam> } [params] - Parameters to be passed to
     *     [Extension Ability]{@link @ohos.security.CryptoExtensionAbility}. If a non-system application passes
     *     [HUKS_EXT_CRYPTO_TAG_UID]{@link huksExternalCrypto.HuksExternalCryptoTagType}, the parameter is invalid.
     * @returns { Promise<Array<HuksExternalCryptoParam>> } Promise that returns the operation result. If the call is
     *     successful, an array of the **HuksExternalCryptoParam** type is returned, containing the properties to be
     *     queried.
     * @throws { BusinessError } 801 - API is not supported.
     * @throws { BusinessError } 12000005 - IPC communication failed.
     * @throws { BusinessError } 12000006 - If the UKey driver operation failed. Possible causes:
     *     1. Error reported when the provider accesses the SKF interface of UKey.
     * @throws { BusinessError } 12000011 - If the cached resource ID is not found.
     * @throws { BusinessError } 12000012 - Device environment or input parameter is abnormal.
     *     This error may occur if the process function is not found, or due to other issues.
     * @throws { BusinessError } 12000014 - If the memory is insufficient.
     * @throws { BusinessError } 12000018 - Input parameter is invalid. Possible causes:
     *     1. The resourceId or propertyId length is invalid.
     *     2. The params contains invalid tags or invalid value types.
     * @throws { BusinessError } 12000020 - If the provider operation failed. Possible causes:
     *     1. The provider experienced an internal processing error.
     * @throws { BusinessError } 12000021 - The UKey PIN is locked.
     * @throws { BusinessError } 12000023 - The UKey PIN is not authenticated.
     * @throws { BusinessError } 12000024 - If the provider or UKey is busy.
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @stagemodelonly
     * @since 22
     */
    function getProperty(resourceId: string, propertyId: string, params?: Array<HuksExternalCryptoParam>): Promise<Array<HuksExternalCryptoParam>>;
    /**
     * The set-type operations of the external crypto extension support calling custom interfaces.
     *     However, the custom interface must be registered with the provider.
     *
     * @param { string } resourceId - Indicates the resource ID of the provider.
     * @param { string } propertyId - Indicates the ID of the property needed to set.
     *     Currently supports part of the method names defined in GMT 0016-2023 and self-defined methods registered.
     * @param { HuksExternalCryptoParam[] } [params] - Indicates the operation parameters.
     *     This parameter is optional and contains parameters related to the property ID needed to set.
     * @returns { Promise<void> } The promise returned by the function.
     * @throws { BusinessError } 801 - API is not supported.
     * @throws { BusinessError } 12000005 - IPC communication failed.
     * @throws { BusinessError } 12000006 - Failed to call the UKey driver interface.
     *     Please check the UKey connection and driver status.
     * @throws { BusinessError } 12000011 - The cached resource ID not found.
     * @throws { BusinessError } 12000012 - Device environment or input parameters are abnormal.
     *     This may occur if the process function is null, or due to other issues.
     * @throws { BusinessError } 12000014 - The memory is insufficient.
     * @throws { BusinessError } 12000018 - The input parameters are invalid. Possible causes:
     *     1. The resourceId or propertyId length is invalid.
     *     2. The parameters contain invalid tags or invalid value types.
     * @throws { BusinessError } 12000020 - The provider operation failed.
     *     This means an error occurred in the crypto extension before calling the UKey driver interface.
     * @throws { BusinessError } 12000021 - The UKey PIN is locked.
     * @throws { BusinessError } 12000023 - The UKey PIN is not authenticated.
     * @throws { BusinessError } 12000024 - The provider or UKey is busy.
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @stagemodelonly
     * @since 26.0.0
     */
    function setProperty(resourceId: string, propertyId: string, params?: HuksExternalCryptoParam[]): Promise<void>;
    /**
     * Obtain the resource ID of the provider.
     *
     * @param { string } providerName - Indicates the name of the external crypto provider
     *     and must be globally unique. One effective way is to include manufacturer information.
     * @param { HuksExternalCryptoParam[] } params - Indicates the input operation parameters,
     *     including the bundle name, ability name, and the related information to get the resource ID.
     * @returns { Promise<string> } The promise returned by the function.
     * @throws { BusinessError } 801 - API is not supported.
     * @throws { BusinessError } 12000002 - The ability name, bundle name parameter or resource information is missing.
     * @throws { BusinessError } 12000005 - IPC communication failed.
     * @throws { BusinessError } 12000011 - The provider is not found.
     * @throws { BusinessError } 12000012 - Device environment or input parameters are abnormal.
     *     This error may occur if the process function is not found, or due to other issues.
     * @throws { BusinessError } 12000014 - The memory is insufficient.
     * @throws { BusinessError } 12000018 - Input parameters are invalid. Possible causes:
     *     1. The providerName length is invalid.
     *     2. The parameters contain invalid tags or invalid value types.
     * @throws { BusinessError } 12000020 - The provider operation failed.
     *     This means an error occurred in the crypto extension before calling the UKey driver interface.
     * @throws { BusinessError } 12000024 - The provider or UKey is busy.
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @stagemodelonly
     * @since 26.0.0
     */
    function getResourceId(providerName: string, params: HuksExternalCryptoParam[]): Promise<string>;
    /**
     * Open resource by specific resource ID.
     * NOTE: The opened resource must be closed using closeResource.
     *
     * @param { string } resourceId - Indicates the resource ID of the provider.
     * @param { HuksExternalCryptoParam[] } [params] - Indicates the input operation parameters.
     * @returns { Promise<void> } Return value of the Promise type
     * @throws { BusinessError } 801 - API is not supported.
     * @throws { BusinessError } 12000005 - IPC communication failed.
     * @throws { BusinessError } 12000006 - Failed to call the UKey driver interface.
     *     Please check the UKey connection and driver status.
     * @throws { BusinessError } 12000011 - The cached resource ID is not found.
     *     This may happen because the resource ID has not been opened.
     * @throws { BusinessError } 12000012 - Device environment or input parameters are abnormal.
     *     This error may occur if the process function is not found, or due to other issues.
     * @throws { BusinessError } 12000014 - The memory is insufficient.
     * @throws { BusinessError } 12000017 - The resource with the resource ID is already open.
     * @throws { BusinessError } 12000018 - Input parameters are invalid. Possible causes:
     *     1. The resourceId length is invalid.
     *     2. The parameters contain invalid tags or invalid value types.
     * @throws { BusinessError } 12000020 - The provider operation failed.
     *     This means an error occurred in the crypto extension before calling the UKey driver interface.
     * @throws { BusinessError } 12000024 - The provider or UKey is busy.
     * @throws { BusinessError } 12000025 - The opened resources exceed the limit.
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @stagemodelonly
     * @since 26.0.0
     */
    function openResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>;
    /**
     * Close the resource with a specific resource ID.
     *
     * @param { string } resourceId - Indicates the resource ID of the provider.
     * @param { HuksExternalCryptoParam[] } [params] - Indicates the input operation parameters.
     * @returns { Promise<void> } The promise returned by the function.
     * @throws { BusinessError } 801 - API is not supported.
     * @throws { BusinessError } 12000005 - IPC communication failed.
     * @throws { BusinessError } 12000006 - Failed to call the UKey driver interface.
     *     Please check the UKey connection and driver status.
     * @throws { BusinessError } 12000012 - Device environment or input parameters are abnormal.
     *     This error may occur if the process function is not found, or due to other issues.
     * @throws { BusinessError } 12000014 - The memory is insufficient.
     * @throws { BusinessError } 12000018 - Input parameters are invalid. Possible causes:
     *     1. The resourceId length is invalid.
     *     2. The parameters contain invalid tags or invalid value types.
     * @throws { BusinessError } 12000020 - The provider operation failed.
     *     This means an error occurred in the crypto extension before calling the UKey driver interface.
     * @throws { BusinessError } 12000024 - The provider or UKey is busy.
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @stagemodelonly
     * @since 26.0.0
     */
    function closeResource(resourceId: string, params?: HuksExternalCryptoParam[]): Promise<void>;
    /**
     * Get the detailed error information.
     *
     * @returns { HuksExternalErrorInfo } The returned error information.
     * @syscap SystemCapability.Security.Huks.CryptoExtension
     * @stagemodelonly
     * @since 26.0.0
     */
    function getErrorInfo(): HuksExternalErrorInfo;
}
export default huksExternalCrypto;

```
