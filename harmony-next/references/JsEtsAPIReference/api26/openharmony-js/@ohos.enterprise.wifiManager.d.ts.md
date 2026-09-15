# @ohos.enterprise.wifiManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2025 Huawei Device Co., Ltd.
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
 * @file Wi-Fi Management
 * @kit MDMKit
 */
import type Want from './@ohos.app.ability.Want';
/**
 * This module provides Wi-Fi management capabilities for enterprise devices, including querying the Wi-Fi enabling
 * status, configuring Wi-Fi connections, and managing the Wi-Fi list.
 *
 * **Use cases:**
 *
 * - Configuring Wi-Fi connections for enterprise devices in batches, simplifying the device initialization process
 * - Controlling the Wi-Fi networks that devices can connect to, implementing network access compliance management
 * - Managing the Wi-Fi switch of enterprise devices and unifying network policies
 *
 * **Benefits:**
 *
 * - Improve enterprise network management efficiency and reduces IT O&M costs.
 * - Ensure that devices connect only to secure Wi-Fi networks, reducing security risks.
 * - Implement unified management and control of network policies to meet enterprise compliance requirements.
 *
 * > **NOTE**
 * >
 * > The APIs of this module can be called only by a device administrator application that is enabled. For details, see
 * > [MDM Kit Development](docroot://mdm/mdm-kit-guide.md).
 * >
 * > The global restriction policies are provided by **restrictions**. To disable Wi-Fi globally, see
 * > [@ohos.enterprise.restrictions]{@link @ohos.enterprise.restrictions:restrictions}.
 *
 * @syscap SystemCapability.Customization.EnterpriseDeviceManager
 * @stagemodelonly
 * @since 12
 */
declare namespace wifiManager {
    /**
     * Enumerates the Wi-Fi security types.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    enum WifiSecurityType {
        /**
         * Invalid security type. For example, airport public Wi-Fi.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        WIFI_SEC_TYPE_INVALID = 0,
        /**
         * Open security type.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        WIFI_SEC_TYPE_OPEN = 1,
        /**
         * Wired Equivalent Privacy (WEP).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        WIFI_SEC_TYPE_WEP = 2,
        /**
         * PSK. For example, home and small office Wi-Fi.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        WIFI_SEC_TYPE_PSK = 3,
        /**
         * Simultaneous Authentication of Equals (SAE). For example, smart home and small- and medium-sized enterprise
         * networks.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        WIFI_SEC_TYPE_SAE = 4,
        /**
         * EAP. For example, large enterprise authentication and university campus networks.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        WIFI_SEC_TYPE_EAP = 5,
        /**
         * Suite B 192-bit encryption. After the setting, Wi-Fi will use Suite-B 192-bit high-strength encryption, providing
         * a high level of security authentication. It is suitable for government and high-security institutions.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        WIFI_SEC_TYPE_EAP_SUITE_B = 6,
        /**
         * Opportunistic Wireless Encryption (OWE). For example, public Wi-Fi in a coffee shop, which does not require a
         * password to provide encryption for connections.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        WIFI_SEC_TYPE_OWE = 7,
        /**
         * WLAN Authentication and Privacy Infrastructure (WAPI) in certificate-based mode (WAPI-CERT). It is China's own
         * wireless security standard.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        WIFI_SEC_TYPE_WAPI_CERT = 8,
        /**
         * WAPI-PSK.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        WIFI_SEC_TYPE_WAPI_PSK = 9
    }
    /**
     * Enumerates the IP address types.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    enum IpType {
        /**
         * Static IP address, which is used in scenarios where a fixed IP address is required, for example, a fixed IP
         * address of an office printer.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        STATIC = 0,
        /**
         * Dynamic Host Configuration Protocol (DHCP), which is a service that automatically allocates IP addresses and
         * other network configuration information to devices on a network.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        DHCP = 1,
        /**
         * Not specified.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        UNKNOWN = 2
    }
    /**
     * Represents IP configuration information.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    interface IpProfile {
        /**
         * IP address, represented in decimal format. For example, the standard dotted decimal notation **192.168.1.1**
         * corresponds to the decimal value **3232235777**. The address ranges from 0.0.0.0 to 255.255.255.255.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        ipAddress: number;
        /**
         * Default gateway, represented in decimal format, usually the IP address of the router. The address ranges from 0.0
         * .0.0 to 255.255.255.255.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        gateway: number;
        /**
         * Subnet mask. The address ranges from 0.0.0.0 to 255.255.255.255.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        prefixLength: number;
        /**
         * DNS server. The array can contain a maximum of two addresses: the primary DNS server and the secondary DNS
         * server. The address ranges from 0.0.0.0 to 255.255.255.255.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        dnsServers: number[];
        /**
         * Domain information.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        domains: Array<string>;
    }
    /**
     * Enumerates the EAP authentication methods.
     *
     * > **NOTE**
     * >
     * > Currently, only the EAP_PEAP and EAP_TLS authentication methods are supported.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    enum EapMethod {
        /**
         * Not specified.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        EAP_NONE = 0,
        /**
         * Protected Extensible Authentication Protocol (PEAP). It first establishes a secure TLS tunnel, followed by
         * performing simple authentication within the tunnel.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        EAP_PEAP = 1,
        /**
         * Transport Layer Security (TLS). It implements mutual certificate authentication.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        EAP_TLS = 2,
        /**
         * Tunnel Transport Layer Security (TTLS). It is similar to PEAP, but supports a more diverse set of authentication
         * methods inside the tunnel.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        EAP_TTLS = 3,
        /**
         * Password Authentication (PWD). It enables password-based authentication and does not require a server
         * certificate.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        EAP_PWD = 4,
        /**
         * Subscriber Identity Module (SIM). It performs authentication using the keys and algorithms stored in the SIM card
         * of a smartphone.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        EAP_SIM = 5,
        /**
         * Authentication and Key Agreement (AKA). It performs authentication using enhanced keys and algorithms stored in a
         * USIM card (applicable to 3G/4G/5G SIM cards).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        EAP_AKA = 6,
        /**
         * AKA Prime. It is an enhanced version of EAP-AKA and binds the network name during key derivation.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        EAP_AKA_PRIME = 7,
        /**
         * Unauthenticated TLS (UNAUTH TLS). It implements one-way authentication (client authentication only) while
         * establishing an encrypted communication channel.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        EAP_UNAUTH_TLS = 8
    }
    /**
     * Enumerates the Phase 2 authentication methods.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    enum Phase2Method {
        /**
         * Not specified.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        PHASE2_NONE = 0,
        /**
         * PAP.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        PHASE2_PAP = 1,
        /**
         * MS-CHAP.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        PHASE2_MSCHAP = 2,
        /**
         * MS-CHAPv2.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        PHASE2_MSCHAPV2 = 3,
        /**
         * GTC.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        PHASE2_GTC = 4,
        /**
         * SIM.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        PHASE2_SIM = 5,
        /**
         * AKA.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        PHASE2_AKA = 6,
        /**
         * AKA Prime.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        PHASE2_AKA_PRIME = 7
    }
    /**
     * Represents EAP profile (configuration) information.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    interface WifiEapProfile {
        /**
         * EAP authentication method.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        eapMethod: EapMethod;
        /**
         * Phase 2 authentication method. This parameter is mandatory only when **eapMethod** is **EAP_PEAP** or
         * **EAP_TTLS**.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        phase2Method: Phase2Method;
        /**
         * Identity Information. This parameter cannot be empty when **eapMethod** is **TLS**.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        identity: string;
        /**
         * Anonymous identity.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        anonymousIdentity: string;
        /**
         * Password Authentication (PWD). It enables password-based authentication and does not require a server
         * certificate.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        password: string;
        /**
         * CA certificate alias.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        caCertAliases: string;
        /**
         * CA certificate path.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        caPath: string;
        /**
         * Client certificate alias. When the client certificate content is empty, the client certificate must be installed
         * first via the certificate management API before passing in the alias.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        clientCertAliases: string;
        /**
         * Client certificate content. When **eapMethod** is set to **EAP_TLS**, if this field is empty, the client
         * certificate alias cannot be empty.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        certEntry: Uint8Array;
        /**
         * CA certificate password.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        certPassword: string;
        /**
         * A string to match the alternate subject. In addition to checking the primary domain name of the certificate, the
         * system checks whether the alternate subject name of the certificate matches the certificate.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        altSubjectMatch: string;
        /**
         * A string to match the domain suffix.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        domainSuffixMatch: string;
        /**
         * Realm for the passpoint credential.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        realm: string;
        /**
         * Credential provider.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        plmn: string;
        /**
         * Sub-ID of the SIM card.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        eapSubId: number;
    }
    /**
     * Represents the Wi-Fi configuration information.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    interface WifiProfile {
        /**
         * Wi-Fi hotspot name. The maximum length is 32 bytes, and the encoding format is UTF-8.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        ssid: string;
        /**
         * MAC address of the Wi-Fi hotspot, with a length of 6 bytes. For example, **00:11:22:33:44:55**. To obtain the MAC
         * address, enable **Enable Wi-Fi verbose logging** under **Settings** > **System & updates** >
         * **Developer options** first, and then go to the WLAN list to check the MAC address. If a Wi-Fi network has
         * multiple MAC addresses, all of them must be added here.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        bssid?: string;
        /**
         * Key of the hotspot, which is used for Wi-Fi connection authentication. The maximum length is 64 bytes.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        preSharedKey: string;
        /**
         * Whether the network is hidden. The value **true** indicates yes, and the value **false** indicates no. The
         * default value is **false**.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        isHiddenSsid?: boolean;
        /**
         * Security type.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        securityType: WifiSecurityType;
        /**
         * ID of the user who creates the network. The default value is **-1**.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        creatorUid?: number;
        /**
         * Disabling reason. The default value is **0**.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        disableReason?: number;
        /**
         * Allocated network ID. The default value is **-1**.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        netId?: number;
        /**
         * Random MAC. The value **0** indicates random MAC address, and the value **1** indicates device MAC address. The
         * default value is **0**.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        randomMacType?: number;
        /**
         * MAC address. This field is mandatory when **randomMacType** is set to device MAC address.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        randomMacAddr?: string;
        /**
         * IP address type. The default value is **DHCP**.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        ipType?: IpType;
        /**
         * Static IP address information. This field is mandatory when **ipType** is set to **STATIC**.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        staticIp?: IpProfile;
        /**
         * Extensible Authentication Protocol (EAP) configuration. This field is mandatory only when **securityType** is set
         * to **WIFI_SEC_TYPE_EAP**.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        eapProfile?: WifiEapProfile;
    }
    /**
     * Represents Wi-Fi access information containing Service Set Identifier (SSID) and Basic Service Set Identifier (
     * BSSID).
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 19
     */
    interface WifiAccessInfo {
        /**
         * Name of the Wi-Fi hotspot. The encoding format is UTF-8 and the maximum length is 32 bytes (three bytes for each
         * Chinese character and one byte for each English character).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 19
         */
        ssid: string;
        /**
         * MAC address of the Wi-Fi hotspot, for example, **00:11:22:33:44:55**. To obtain the MAC address, enable
         * **Enable Wi-Fi verbose logging** under **Settings** > **System & updates** > **Developer options** first, and
         * then go to the WLAN list to check the MAC address. If a Wi-Fi network has multiple MAC addresses, all of them
         * must be added here.
         *
         * This property is optional when the [addDisallowedWifiList]{@link wifiManager.addDisallowedWifiList} and
         * [removeDisallowedWifiList]{@link wifiManager.removeDisallowedWifiList} APIs are called. The default value is an
         * empty string.
         *
         * This property is optional (available since API version 21) when the
         * [addAllowedWifiList]{@link wifiManager.addAllowedWifiList} and
         * [removeAllowedWifiList]{@link wifiManager.removeAllowedWifiList} APIs are called. The default value is an empty
         * string. However, this property is mandatory in API version 20 and earlier versions.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 19
         */
        bssid?: string;
    }
    /**
     * Queries the Wi-Fi status of the current device.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_WIFI
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { boolean } Returns the Wi-Fi status. The value **true** means Wi-Fi is enabled, and the value **false**
     *     means the opposite.
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
    function isWifiActiveSync(admin: Want): boolean;
    /**
     * Configures Wi-Fi for the current device to connect to a specified network.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_WIFI
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { WifiProfile } profile - Wi-Fi configuration information, which is used to specify the configuration
     *     parameters of the Wi-Fi network to be connected, including the SSID, BSSID, key, and security type.
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
    function setWifiProfileSync(admin: Want, profile: WifiProfile): void;
    /**
     * Adds disallowed Wi-Fi networks. The current device cannot connect to the disallowed Wi-Fi networks. This API is
     * applicable to enterprise security control and management scenarios, such as preventing devices from connecting to
     * insecure public Wi-Fi networks (for example, those in cafes or airports), and preventing employees from connecting
     * to competitor or malicious networks, thereby safeguarding enterprise data security.
     *
     * A policy conflict is reported when this API is called in the following scenarios:
     *
     * 1. The device Wi-Fi capability has been disabled via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}.
     * You can resolve the conflict by enabling Wi-Fi via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}.
     * 2. Allowed Wi-Fi networks have been added by calling [addAllowedWifiList]{@link wifiManager.addAllowedWifiList}.
     * You can resolve the conflict by removing the allowed Wi-Fi networks through [removeAllowedWifiList]{@link wifiManager.removeAllowedWifiList}.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_WIFI
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<WifiAccessInfo> } list - Array of disallowed Wi-Fi networks. The maximum length of the array is 200.
     *     For example, if there are already 100 Wi-Fi networks, a maximum of 100 more can be added.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 19
     */
    function addDisallowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void;
    /**
     * Removes disallowed Wi-Fi networks. If some Wi-Fi networks are removed from the disallowed list, the current device
     * cannot connect to the remaining ones; if all Wi-Fi networks are removed from the disallowed list, the current
     * device can connect to any Wi-Fi network. This API is applicable to enterprise Wi-Fi policy adjustment scenarios,
     * such as lifting restrictions on a specific Wi-Fi network, allowing employees to connect to newly approved office
     * networks, or completely removing the disabling policy.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_WIFI
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<WifiAccessInfo> } list - Array of Wi-Fi networks to be removed. The maximum length of the array is 2
     *     00.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 19
     */
    function removeDisallowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void;
    /**
     * Obtains disallowed Wi-Fi networks.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_WIFI
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Array<WifiAccessInfo> } Array of disallowed Wi-Fi networks.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 19
     */
    function getDisallowedWifiList(admin: Want): Array<WifiAccessInfo>;
    /**
     * Obtains disallowed Wi-Fi networks.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_WIFI
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { Array<WifiAccessInfo> } Array of disallowed Wi-Fi networks.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getDisallowedWifiList(admin: Want | null): Array<WifiAccessInfo>;
    /**
     * Adds allowed Wi-Fi networks. The current device can only connect to the allowed Wi-Fi networks. This API is
     * applicable to enterprise security management scenarios, for example, restricting employees' devices to connect only
     * to Wi-Fi networks authorized by the enterprise, preventing connection to insecure external Wi-Fi networks and
     * ensuring enterprise network and data security.
     *
     * A policy conflict is reported when this API is called in the following scenarios:
     *
     * 1. The device Wi-Fi capability has been disabled via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}.
     * You can resolve the conflict by enabling Wi-Fi via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}.
     * 2. Disallowed Wi-Fi networks have been added by calling [addDisallowedWifiList]{@link wifiManager.addDisallowedWifiList}.
     * You can resolve the conflict by removing the disallowed Wi-Fi networks through [removeDisallowedWifiList]{@link wifiManager.removeDisallowedWifiList}.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_WIFI
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<WifiAccessInfo> } list - Array of allowed Wi-Fi networks. The maximum length of the array is 200.
     *     For example, if there are already 100 Wi-Fi networks, a maximum of 100 more can be added.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 19
     */
    function addAllowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void;
    /**
     * Removes Wi-Fi networks from the allowed list. If some Wi-Fi networks are removed from the allowed list, the current
     * device can only connect to the remaining ones; if all Wi-Fi networks are removed from the allowed list, the current
     * device can connect to any Wi-Fi network. This API is applicable to enterprise Wi-Fi policy adjustment scenarios,
     * such as removing restrictions on old Wi-Fi networks when the company switches to a new Wi-Fi network, or lifting
     * some Wi-Fi restrictions to allow employees to connect to new office networks.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_WIFI
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<WifiAccessInfo> } list - Array of Wi-Fi networks to be removed from the allowed list. The maximum
     *     length of the array is 200.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 19
     */
    function removeAllowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void;
    /**
     * Obtains Wi-Fi networks from the allowed list.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_WIFI
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Array<WifiAccessInfo> } Array of allowed Wi-Fi networks.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 19
     */
    function getAllowedWifiList(admin: Want): Array<WifiAccessInfo>;
    /**
     * Obtains Wi-Fi networks from the allowed list.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_WIFI
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { Array<WifiAccessInfo> } Array of allowed Wi-Fi networks.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getAllowedWifiList(admin: Want | null): Array<WifiAccessInfo>;
    /**
     * Enables Wi-Fi. This API is applicable to enterprise device remote management scenarios, such as administrators
     * remotely enabling Wi-Fi on employee devices, or ensuring that Wi-Fi is turned on when specific policies are
     * enforced.
     *
     * In the following scenario, attempting to enable Wi-Fi using this API will fail, and a message indicating that the
     * system function is disabled will be returned:
     *
     * ​Wi-Fi has been disabled via
     * [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}. In this case, you must
     * call [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy} to enable Wi-Fi.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_WIFI
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { boolean } isForce - Whether to forcibly enable Wi-Fi.
     *     <br>The value **true** means to forcibly enable Wi-Fi. Once enabled, it cannot be disabled manually. You must
     *     call [turnOffWifi]{@link wifiManager.turnOffWifi} instead. The value **false** means the opposite and the Wi-Fi
     *     can be disabled manually.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 203 - This function is prohibited by enterprise management policies.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function turnOnWifi(admin: Want, isForce: boolean): void;
    /**
     * Disables Wi-Fi.
     *
     * In the following scenario, attempting to disable Wi-Fi using this API will fail, and a message indicating that the
     * system function is disabled will be returned:
     *
     * ​Wi-Fi has been disabled via
     * [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}. In this case, you must
     * call [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy} to enable Wi-Fi.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_WIFI
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 203 - This function is prohibited by enterprise management policies.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function turnOffWifi(admin: Want): void;
}
export default wifiManager;

```
