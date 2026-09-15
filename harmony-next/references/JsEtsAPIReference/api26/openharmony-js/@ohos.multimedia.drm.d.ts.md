# @ohos.multimedia.drm.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
* Copyright (C) 2023 Huawei Device Co., Ltd.
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
 * @file Defines the DRM capability.
 * @kit DrmKit
 */
/**
 * The Digital Rights Management (DRM) framework enables you to develop digital rights management features for audio and
 * video services. By calling the DRM plugins provided by the system, you can achieve the following:
 *
 * - DRM certificate management: Generate certificate requests and handle certificate responses to facilitate
 * certificate provisioning (downloading).
 * - DRM media key management: Generate media key requests, manage media key responses, and handle offline media keys.
 * - DRM content authorization: Allow DRM plugins to authorize content based on media key permissions.
 * - DRM content decryption: Decrypt DRM content to support media playback functionality.
 *
 * @syscap SystemCapability.Multimedia.Drm.Core
 * @atomicservice [since 12]
 * @since 11
 */
declare namespace drm {
    /**
     * Enumerates the DRM error codes.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 11
     */
    enum DrmErrorCode {
        /**
         * Unknown error.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        ERROR_UNKNOWN = 24700101,
        /**
         * Maximum number of MediaKeySystem instances (64) reached.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        MAX_SYSTEM_NUM_REACHED = 24700103,
        /**
         * Maximum number of MediaKeySession instances (64) reached.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        MAX_SESSION_NUM_REACHED = 24700104,
        /**
         * DRM service fatal error.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        SERVICE_FATAL_ERROR = 24700201
    }
    /**
     * Enumerates the predefined configuration properties.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 11
     */
    enum PreDefinedConfigName {
        /**
         * Plugin vendor name, which corresponds to the value of **vendor** in the return value of
         * [getConfigurationString]{@link @ohos.multimedia.drm:drm.MediaKeySystem.getConfigurationString}.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        CONFIG_DEVICE_VENDOR = 'vendor',
        /**
         * Plugin version number, which corresponds to the value of **version** in the return value of
         * [getConfigurationString]{@link @ohos.multimedia.drm:drm.MediaKeySystem.getConfigurationString}.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        CONFIG_DEVICE_VERSION = 'version',
        /**
         * Device description, which corresponds to the value of **description** in the return value of
         * [getConfigurationString]{@link @ohos.multimedia.drm:drm.MediaKeySystem.getConfigurationString}.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        CONFIG_DEVICE_DESCRIPTION = 'description',
        /**
         * Supported algorithms, which correspond to the value of **algorithms** in the return value of
         * [getConfigurationString]{@link @ohos.multimedia.drm:drm.MediaKeySystem.getConfigurationString}.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        CONFIG_DEVICE_ALGORITHMS = 'algorithms',
        /**
         * Unique device ID, which corresponds to the value of **deviceUniqueId** in the return value of
         * [getConfigurationByteArray]{@link @ohos.multimedia.drm:drm.MediaKeySystem.getConfigurationByteArray}.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        CONFIG_DEVICE_UNIQUE_ID = 'deviceUniqueId',
        /**
         * Maximum number of supported sessions, which corresponds to the value of **maxSessionNum** in the return value of
         * [getConfigurationString]{@link @ohos.multimedia.drm:drm.MediaKeySystem.getConfigurationString}.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        CONFIG_SESSION_MAX = 'maxSessionNum',
        /**
         * Number of active sessions, which corresponds to the value of **currentSessionNum** in the return value of
         * [getConfigurationString]{@link @ohos.multimedia.drm:drm.MediaKeySystem.getConfigurationString}.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        CONFIG_SESSION_CURRENT = 'currentSessionNum'
    }
    /**
     * Enumerates the types of media keys.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 11
     */
    enum MediaKeyType {
        /**
         * Offline media key.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        MEDIA_KEY_TYPE_OFFLINE = 0,
        /**
         * Online media key.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        MEDIA_KEY_TYPE_ONLINE = 1
    }
    /**
     * Enumerates the statuses of offline media keys.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 11
     */
    enum OfflineMediaKeyStatus {
        /**
         * Unknown status.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        OFFLINE_MEDIA_KEY_STATUS_UNKNOWN = 0,
        /**
         * The media key is available.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        OFFLINE_MEDIA_KEY_STATUS_USABLE = 1,
        /**
         * The media key is inactive.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        OFFLINE_MEDIA_KEY_STATUS_INACTIVE = 2
    }
    /**
     * Enumerates the statuses of device certificates.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 11
     */
    enum CertificateStatus {
        /**
         * A device certificate is provisioned.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        CERT_STATUS_PROVISIONED = 0,
        /**
         * A device certificate is not provisioned.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        CERT_STATUS_NOT_PROVISIONED = 1,
        /**
         * The device certificate has expired.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        CERT_STATUS_EXPIRED = 2,
        /**
         * The device certificate is invalid.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        CERT_STATUS_INVALID = 3,
        /**
         * The device certificate is unavailable.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        CERT_STATUS_UNAVAILABLE = 4
    }
    /**
     * Enumerates the types of media key requests.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 12]
     * @since 11
     */
    enum MediaKeyRequestType {
        /**
         * Unknown type.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        MEDIA_KEY_REQUEST_TYPE_UNKNOWN = 0,
        /**
         * Initial request.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        MEDIA_KEY_REQUEST_TYPE_INITIAL = 1,
        /**
         * Renewal request.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        MEDIA_KEY_REQUEST_TYPE_RENEWAL = 2,
        /**
         * Release request.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        MEDIA_KEY_REQUEST_TYPE_RELEASE = 3,
        /**
         * No request.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        MEDIA_KEY_REQUEST_TYPE_NONE = 4,
        /**
         * Update request.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        MEDIA_KEY_REQUEST_TYPE_UPDATE = 5
    }
    /**
     * Enumerates the content protection levels.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 12]
     * @since 11
     */
    enum ContentProtectionLevel {
        /**
         * Unknown content protection level.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        CONTENT_PROTECTION_LEVEL_UNKNOWN = 0,
        /**
         * Software-based content protection.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        CONTENT_PROTECTION_LEVEL_SW_CRYPTO = 1,
        /**
         * Hardware-based content protection.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        CONTENT_PROTECTION_LEVEL_HW_CRYPTO = 2,
        /**
         * Enhanced hardware-based content protection.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        CONTENT_PROTECTION_LEVEL_ENHANCED_HW = 3,
        /**
         * Maximum content protection level.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        CONTENT_PROTECTION_LEVEL_MAX = 4
    }
    /**
     * Defines a device certificate provisioning request.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 11
     */
    interface ProvisionRequest {
        /**
         * Binary data of the provisioning request.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        data: Uint8Array;
        /**
         * URL of the device certificate provisioning server.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        defaultURL: string;
    }
    /**
     * Defines optional parameters for a device certificate request.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 12]
     * @since 11
     */
    interface OptionsData {
        /**
         * Name of the optional parameter.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        name: string;
        /**
         * Value of the optional parameter.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        value: string;
    }
    /**
     * Defines a media key request.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 12]
     * @since 11
     */
    interface MediaKeyRequest {
        /**
         * Type of the media key request.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        mediaKeyRequestType: MediaKeyRequestType;
        /**
         * Binary data of the media key request.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        data: Uint8Array;
        /**
         * URL of the license server.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        defaultURL: string;
    }
    /**
     * Defines the DRM event information.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 12]
     * @since 11
     */
    interface EventInfo {
        /**
         * Event payload data.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        info: Uint8Array;
        /**
         * Additional event context.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        extraInfo: string;
    }
    /**
     * Defines a key-value pair for DRM metrics.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 11
     */
    interface StatisticKeyValue {
        /**
         * Name of the metric.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        name: string;
        /**
         * Value of the metric.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        value: string;
    }
    /**
     * Defines a status attribute for a media key.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 12]
     * @since 11
     */
    interface MediaKeyStatus {
        /**
         * Name of the media key status attribute, for example, expiration time or content protection level.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        name: string;
        /**
         * Value of the media key status attribute.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        value: string;
    }
    /**
     * Defines the status information of a media key.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 12]
     * @since 11
     */
    interface KeysInfo {
        /**
         * Media key ID.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        keyId: Uint8Array;
        /**
         * Media key status.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        value: string;
    }
    /**
     * Defines the DRM information for encrypted content.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 12]
     * @since 11
     */
    interface MediaKeySystemInfo {
        /**
         * Drm system ID.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        uuid: string;
        /**
         * PSSH(protection scheme specific header) contain drm info.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        pssh: Uint8Array;
    }
    /**
     * Defines the DRM plugin information.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 12
     */
    interface MediaKeySystemDescription {
        /**
         * Name of DRM plugin.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 12
         */
        name: string;
        /**
         * UUID supported by DRM plugin.
         *
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 12
         */
        uuid: string;
    }
    /**
     * Obtains the UUID of the DRM content protection system supported by the specified DRM solution.
     *
     * @param { string } name - DRM solution name. You can check whether the solution name is supported by calling
     *     [isMediaKeySystemSupported]{@link @ohos.multimedia.drm:drm.isMediaKeySystemSupported(name: string)}.
     * @returns { string } UUID of the DRM content protection system.
     * @throws { BusinessError } 401 - The parameter check failed.Possibly because:
     *     <br>1.Mandatory parameters are left unspecified. 2.Parameter verification failed.
     * @throws { BusinessError } 24700101 - All unknown errors.
     * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 12
     */
    function getMediaKeySystemUuid(name: string): string;
    /**
     * Obtains the list of plugins supported by the device.
     *
     * @returns { MediaKeySystemDescription[] } Array of supported plugins.
     * @throws { BusinessError } 24700101 - All unknown errors.
     * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 12
     */
    function getMediaKeySystems(): MediaKeySystemDescription[];
    /**
     * Creates a MediaKeySystem instance.
     *
     * @param { string } name - DRM solution name, for example, **"com.clearplay.drm"**.
     * @returns { MediaKeySystem } MediaKeySystem instance.
     * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
     *     1.Mandatory parameters are left unspecified. 2.Parameter verification failed.
     * @throws { BusinessError } 24700101 - All unknown errors.
     * @throws { BusinessError } 24700103 - Meet max MediaKeySystem num limit.
     * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 11
     */
    function createMediaKeySystem(name: string): MediaKeySystem;
    /**
     * Checks whether the device supports the combination of the DRM solution, MIME type, and content protection level.
     *
     * @param { string } name - DRM solution name. Before calling this API, ensure that the DRM solution name is supported
     *     by calling [isMediaKeySystemSupported]{@link @ohos.multimedia.drm:drm.isMediaKeySystemSupported(name: string)}.
     * @param { string } mimeType - MIME type. The supported MIME types depend on the DRM solution. Before calling this
     *     API, ensure that the MIME type is supported by calling
     *     [isMediaKeySystemSupported]{@link @ohos.multimedia.drm:drm.isMediaKeySystemSupported(name: string, mimeType: string)}
     *     .
     * @param { ContentProtectionLevel } level - Content protection level.
     * @returns { boolean } Check result for the support of the combination. **true** if supported, **false** otherwise.
     * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
     *     1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.
     *     3.Parameter verification failed.
     * @throws { BusinessError } 24700101 - All unknown errors.
     * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 11
     */
    function isMediaKeySystemSupported(name: string, mimeType: string, level: ContentProtectionLevel): boolean;
    /**
     * Checks whether the device supports the combination of the DRM solution and MIME type.
     *
     * @param { string } name - DRM solution name. Before calling this API, ensure that the DRM solution name is supported
     *     by calling [isMediaKeySystemSupported]{@link @ohos.multimedia.drm:drm.isMediaKeySystemSupported(name: string)}.
     * @param { string } mimeType - MIME type. The supported MIME types depend on the DRM solution. For example, video/avc
     *     and video/hevc.
     * @returns { boolean } Check result for the support of the combination. **true** if supported, **false** otherwise.
     * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
     *     1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.
     *     3.Parameter verification failed.
     * @throws { BusinessError } 24700101 - All unknown errors.
     * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 11
     */
    function isMediaKeySystemSupported(name: string, mimeType: string): boolean;
    /**
     * Checks whether the device supports the specified DRM solution.
     *
     * @param { string } name - DRM solution name, for example, **"com.clearplay.drm"**.
     * @returns { boolean } Check result for the support of the DRM solution. **true** if supported, **false** otherwise.
     * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
     *     1.Mandatory parameters are left unspecified. 2.Parameter verification failed,
     *     the param name's length is zero or too big(exceeds 4096 Bytes).
     * @throws { BusinessError } 24700101 - All unknown errors.
     * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 11
     */
    function isMediaKeySystemSupported(name: string): boolean;
    /**
     * MediaKeySystem manages MediaKeySystem instances, handles device certificate (DRM certificate) requests and
     * processing, creates sessions, manages offline media keys, obtains DRM metrics, and obtain device configurations.
     * Before calling any API in MediaKeySystem, you must use
     * [createMediaKeySystem]{@link @ohos.multimedia.drm:drm.createMediaKeySystem(name: string)} to create a
     * MediaKeySystem instance.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 14]
     * @since 11
     */
    interface MediaKeySystem {
        /**
         * Obtains the value of a configuration item in the form of a string.
         *
         * @param { string } configName - Name of the configuration item, which is determined by the DRM solution on the
         *     device and cannot be empty. For details about available options, see
         *     [PreDefinedConfigName]{@link @ohos.multimedia.drm:drm.PreDefinedConfigName}.
         * @returns { string } Value of the configuration item in the form of a string.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified. 2.Parameter verification failed,
         *     the param's length is zero or too big(exceeds 4096 Bytes).
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        getConfigurationString(configName: string): string;
        /**
         * Sets a configuration item in the form of a string.
         *
         * @param { string } configName - Name of the configuration item, which is determined by the DRM solution on the
         *     device and cannot be empty. For details about available options, see
         *     [PreDefinedConfigName]{@link @ohos.multimedia.drm:drm.PreDefinedConfigName}.
         * @param { string } value - Value of the configuration item.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        setConfigurationString(configName: string, value: string): void;
        /**
         * Obtains the value of a configuration item in the form of a byte array.
         *
         * @param { string } configName - Name of the configuration item, which is determined by the DRM solution on the
         *     device and cannot be empty. For details about available options, see
         *     [PreDefinedConfigName]{@link @ohos.multimedia.drm:drm.PreDefinedConfigName}.
         * @returns { Uint8Array } Value of the configuration item in the form of an array.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified. 2.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        getConfigurationByteArray(configName: string): Uint8Array;
        /**
         * Sets a configuration item in the form of a byte array.
         *
         * @param { string } configName - Name of the configuration item, which is determined by the DRM solution on the
         *     device and cannot be empty. For details about available options, see
         *     [PreDefinedConfigName]{@link @ohos.multimedia.drm:drm.PreDefinedConfigName}.
         * @param { Uint8Array } value - Value of the configuration item in the form of an array. The specific value is
         *     determined by the DRM solution on the device.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        setConfigurationByteArray(configName: string, value: Uint8Array): void;
        /**
         * Obtains the DRM metrics, including the number of active sessions, plugin version details, the maximum decryption
         * time for each session (over three attempts), the total count of decryption operations, and the number of
         * decryption failures.
         *
         * @returns { StatisticKeyValue[] } Metrics.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        getStatistics(): StatisticKeyValue[];
        /**
         * Obtains the maximum content protection level supported by the current DRM solution.
         *
         * @returns { ContentProtectionLevel } Maximum content protection level.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        getMaxContentProtectionLevel(): ContentProtectionLevel;
        /**
         * Generates a request to obtain a device certificate for the MediaKeySystem. This API uses a promise to return the
         * result.
         *
         * @returns { Promise<ProvisionRequest> } Promise used to return the request for a device certificate. If a device
         *     certificate already exists on the device, this operation fails.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        generateKeySystemRequest(): Promise<ProvisionRequest>;
        /**
         * Processes the response to a previously generated device certificate request. This API uses a promise to return
         * the result.
         *
         * @param { Uint8Array } response - Response to a previously generated device certificate request.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        processKeySystemResponse(response: Uint8Array): Promise<void>;
        /**
         * Obtains the status of the device certificate.
         *
         * @returns { CertificateStatus } Certificate status.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        getCertificateStatus(): CertificateStatus;
        /**
         * Subscribes to events indicating that the application requests a device certificate. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'keySystemRequired' } type - Event type. This event is available for listening after a MediaKeySystem
         *     instance is created by calling
         *     [createMediaKeySystem]{@link @ohos.multimedia.drm:drm.createMediaKeySystem(name: string)}. It is triggered
         *     when a device certificate is required.
         * @param { function } callback - Callback used to return the event information. The occurrence of this event
         *     signals the need to request a device certificate.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void;
        /**
         * Unsubscribes from events indicating that the application requests a device certificate. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { 'keySystemRequired' } type - Event type. This event is available for listening after a MediaKeySystem
         *     instance is created by calling
         *     [createMediaKeySystem]{@link @ohos.multimedia.drm:drm.createMediaKeySystem(name: string)}.
         * @param { function } callback - Callback used to return the event information.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void;
        /**
         * Creates a MediaKeySession instance with the specified content protection level.
         *
         * @param { ContentProtectionLevel } level - Content protection level.
         * @returns { MediaKeySession } MediaKeySession instance.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified. 2.The param level exceeds reasonable range,
         *     please use value in ContentProtectionLevel.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700104 - Meet max MediaKeySession num limit.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        createMediaKeySession(level: ContentProtectionLevel): MediaKeySession;
        /**
         * Creates a MediaKeySession instance with the default content protection level.
         *
         * @returns { MediaKeySession } MediaKeySession instance.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700104 - Meet max MediaKeySession num limit.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        createMediaKeySession(): MediaKeySession;
        /**
         * Obtains the IDs of offline media keys.
         *
         * @returns { Uint8Array[] } Array of offline media key IDs.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        getOfflineMediaKeyIds(): Uint8Array[];
        /**
         * Obtains the status of offline media keys with the specified IDs.
         *
         * @param { Uint8Array } mediaKeyId - Array of offline media key IDs.
         * @returns { OfflineMediaKeyStatus } Status of the offline media keys.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus;
        /**
         * Clears offline media keys with the specified IDs.
         *
         * @param { Uint8Array } mediaKeyId - Array of offline media key IDs.
         * @throws { BusinessError } 401 - The parameter check failed.Possibly because:
         *     1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        clearOfflineMediaKeys(mediaKeyId: Uint8Array): void;
        /**
         * Destroys this MediaKeySystem instance.
         *
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 14]
         * @since 11
         */
        destroy(): void;
    }
    /**
     * MediaKeySession implements media key management. Before calling any API in MediaKeySession, you must use
     * [createMediaKeySession]{@link @ohos.multimedia.drm:drm.MediaKeySystem.createMediaKeySession(level: ContentProtectionLevel)}
     * to create a MediaKeySession instance.
     *
     * @syscap SystemCapability.Multimedia.Drm.Core
     * @atomicservice [since 12]
     * @since 11
     */
    interface MediaKeySession {
        /**
         * Generates a media key request. This API uses a promise to return the result.
         *
         * @param { string } mimeType - MIME type. The supported DRM solution names can be obtained by calling
         *     [isMediaKeySystemSupported]{@link @ohos.multimedia.drm:drm.isMediaKeySystemSupported(name: string, mimeType: string)}
         *     .
         * @param { Uint8Array } initData - Initial data.
         * @param { number } mediaKeyType - Type of the media key. The value **0** means an online media key, and **1** means
         *     an offline media key.
         * @param { OptionsData[] } options - Optional data.
         * @returns { Promise<MediaKeyRequest> } Promise used to return the media key request generated.
         * @throws { BusinessError } 401 -The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        generateMediaKeyRequest(mimeType: string, initData: Uint8Array, mediaKeyType: number, options?: OptionsData[]): Promise<MediaKeyRequest>;
        /**
         * Processes a media key response. This API uses a promise to return the result.
         *
         * @param { Uint8Array } response - Media key response.
         * @returns { Promise<Uint8Array> } Promise used to return an array of media key IDs.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        processMediaKeyResponse(response: Uint8Array): Promise<Uint8Array>;
        /**
         * Checks the status of the media keys in use.
         *
         * @returns { MediaKeyStatus[] } Media key status.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        checkMediaKeyStatus(): MediaKeyStatus[];
        /**
         * Clears the media keys in use.
         *
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        clearMediaKeys(): void;
        /**
         * Generates a request to release offline media keys. This API uses a promise to return the result.
         *
         * @param { Uint8Array } mediaKeyId - Array of offline media key IDs.
         * @returns { Promise<Uint8Array> } Promise used to return the request generated if the DRM solution on the device
         *     supports the release of offline media keys.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        generateOfflineReleaseRequest(mediaKeyId: Uint8Array): Promise<Uint8Array>;
        /**
         * Processes a response to a request for releasing offline media keys. This API uses a promise to return the result.
         *
         * @param { Uint8Array } mediaKeyId - Array of offline media key IDs.
         * @param { Uint8Array } response - Response to the request for releasing offline media keys.
         * @returns { Promise<void> } Promise used to return the result if the DRM solution on the device supports the
         *     release of offline media keys.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        processOfflineReleaseResponse(mediaKeyId: Uint8Array, response: Uint8Array): Promise<void>;
        /**
         * Restores offline media keys. This API uses a promise to return the result.
         *
         * @param { Uint8Array } mediaKeyId - Array of offline media key IDs.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        restoreOfflineMediaKeys(mediaKeyId: Uint8Array): Promise<void>;
        /**
         * Obtains the content protection level of this media key session.
         *
         * @returns { ContentProtectionLevel } Content protection level.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        getContentProtectionLevel(): ContentProtectionLevel;
        /**
         * Checks whether secure decoding is required.
         *
         * @param { string } mimeType - MIME type. The supported MIME types depend on the DRM solution and can be obtained
         *     by calling
         *     [isMediaKeySystemSupported]{@link @ohos.multimedia.drm:drm.isMediaKeySystemSupported(name: string, mimeType: string)}
         *     .
         * @returns { boolean } Check result for whether secure decoding is required. **true** if required, **false**
         *     otherwise.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        requireSecureDecoderModule(mimeType: string): boolean;
        /**
         * Subscribes to events indicating that the application requests a media key. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { 'keyRequired' } type - Event type. The value is fixed at **'keyRequired'**, which is triggered when the
         *     application requires a media key.
         * @param { function } callback - Callback used to return the event information.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'keyRequired', callback: (eventInfo: EventInfo) => void): void;
        /**
         * Unsubscribes from events indicating that the application requests a media key. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'keyRequired' } type - Event type. The value is fixed at **'keyRequired'**.
         * @param { function } callback - Callback used to return the event information.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'keyRequired', callback?: (eventInfo: EventInfo) => void): void;
        /**
         * Subscribes to events indicating that a media key expires. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'keyExpired' } type - Event type. The value is fixed at **'keyExpired'**, which is triggered when a
         *     media key expires.
         * @param { function } callback - Callback used to return the event information.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'keyExpired', callback: (eventInfo: EventInfo) => void): void;
        /**
         * Unsubscribes from events indicating that a media key expires. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'keyExpired' } type - Event type. The value is fixed at **'keyExpired'**.
         * @param { function } callback - Callback used to return the event information.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'keyExpired', callback?: (eventInfo: EventInfo) => void): void;
        /**
         * Subscribes to vendor-defined events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'vendorDefined' } type - Event type. The value is fixed at **'vendorDefined'**, which is triggered when
         *     a vendor-defined event occurs.
         * @param { function } callback - Callback used to return the event information.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'vendorDefined', callback: (eventInfo: EventInfo) => void): void;
        /**
         * Unsubscribes from vendor-defined events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'vendorDefined' } type - Event type. The value is fixed at **'vendorDefined'**.
         * @param { function } callback - Callback used to return the event information.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'vendorDefined', callback?: (eventInfo: EventInfo) => void): void;
        /**
         * Subscribes to events indicating that a media key is updated upon expiry. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { 'expirationUpdate' } type - Event type. The value is fixed at **'expirationUpdate'**, which is triggered
         *     when a media key is updated upon expiry.
         * @param { function } callback - Callback used to return the event information.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'expirationUpdate', callback: (eventInfo: EventInfo) => void): void;
        /**
         * Unsubscribes from events indicating that a media key is updated upon expiry. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'expirationUpdate' } type - Event type. The value is fixed at **'expirationUpdate'**.
         * @param { function } callback - Callback used to return the event information.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'expirationUpdate', callback?: (eventInfo: EventInfo) => void): void;
        /**
         * Subscribes to events indicating that a media key changes. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'keysChange' } type - Event type. The value is fixed at **'keysChange'**, which is triggered when a
         *     media key changes.
         * @param { function } callback - Callback used to return the event information, including a list of key IDs,
         *     descriptions of their statuses, and whether each key is available.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'keysChange', callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void;
        /**
         * Unsubscribes from events indicating that a media key changes. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'keysChange' } type - Event type. The value is fixed at **'keysChange'**.
         * @param { function } callback - Callback used to return the event information, including a list of key IDs,
         *     descriptions of their statuses, and whether each key is available.
         * @throws { BusinessError } 401 - The parameter check failed. Possibly because:
         *     1.Mandatory parameters are left unspecified or too many parameters. 2.Incorrect parameter types.
         *     3.Parameter verification failed.
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'keysChange', callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void;
        /**
         * Destroys this MediaKeySession instance.
         *
         * @throws { BusinessError } 24700101 - All unknown errors.
         * @throws { BusinessError } 24700201 - Fatal service error, for example, service died.
         * @syscap SystemCapability.Multimedia.Drm.Core
         * @atomicservice [since 12]
         * @since 11
         */
        destroy(): void;
    }
}
export default drm;

```
