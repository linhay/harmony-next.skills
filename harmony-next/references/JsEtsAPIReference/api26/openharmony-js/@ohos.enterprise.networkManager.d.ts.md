# @ohos.enterprise.networkManager.d.ts

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
 * @file Network Management
 * @kit MDMKit
 */
import type Want from './@ohos.app.ability.Want';
import type connection from './@ohos.net.connection';
/**
 * This module provides device network management capabilities, including querying IP addresses and MAC addresses,
 * managing network interface states, configuring global network proxies, managing firewall rules and domain name
 * filtering rules, controlling mobile data networks, managing APN configurations, and configuring Ethernet networks. It
 * is suitable for enterprise IT administrators to centrally manage and secure device networks, helping enterprises
 * achieve unified network access policy management, prevent network attacks and data leaks, and reduce network
 * management costs.
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
declare namespace networkManager {
    /**
     * Enumerates the direction chains to which the rule applies.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    enum Direction {
        /**
         * Input chain.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        INPUT = 0,
        /**
         * Output chain.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        OUTPUT = 1,
        /**
         * Forward chain.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 15
         */
        FORWARD = 2
    }
    /**
     * Enumerates the actions that can be taken for data packets.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    enum Action {
        /**
         * Receive data packets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        ALLOW = 0,
        /**
         * Discard data packets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        DENY = 1,
        /**
         * Reject data packets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 15
         */
        REJECT = 2
    }
    /**
     * Enumerates network protocols.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    enum Protocol {
        /**
         * All network protocols.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        ALL = 0,
        /**
         * TCP.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        TCP = 1,
        /**
         * UDP.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        UDP = 2,
        /**
         * ICMP.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        ICMP = 3
    }
    /**
     * Enumerates the log types.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    enum LogType {
        /**
         * Data packet logging function in the kernel Netfilter framework.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 23
         */
        NFLOG = 0
    }
    /**
     * Represents a firewall rule.
     *
     * In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22.
     *
     * [LogType]{@link networkManager.LogType} is supported since API version 23.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    interface FirewallRule {
        /**
         * Source IP address. An IP address segment, for example, **192.168.0.0/22** or **192.168.1.100-192.168.1.200** is
         * supported.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        srcAddr?: string;
        /**
         * Destination IP address. An IP address segment, for example, **192.168.0.0/22** or **192.168.1.100-192.168.1.200**
         * is supported.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        destAddr?: string;
        /**
         * Source port.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        srcPort?: string;
        /**
         * Destination port.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        destPort?: string;
        /**
         * UID of the application.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        appUid?: string;
        /**
         * Direction chains to which the rule applies.
         *
         * This parameter is mandatory when a firewall filtering rule is added.
         *
         * This parameter is optional when a firewall is removed. If this parameter is left empty, all
         * [Direction]{@link networkManager.Direction} chains are cleared, and **srcAddr**, **destAddr**, **srcPort**,
         * **destPort**, and **appUid** must be also left empty.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        direction?: Direction;
        /**
         * Action to take, that is, receive or discard the data packets.
         *
         * This parameter is mandatory when a firewall filtering rule is added.
         *
         * This parameter is optional when a firewall is removed. If this parameter is left empty, all
         * [Action]{@link networkManager.Action} chains are cleared, and **srcAddr**, **destAddr**, **srcPort**,
         * **destPort**, and **appUid** must be also left empty.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        action?: Action;
        /**
         * Network protocol. If the value is **ALL** or **ICMP**, the settings of **srcPort** and **destPort** are invalid.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        protocol?: Protocol;
        /**
         * IP protocol version. The value can be **1** (IPv4) or **2** (IPv6).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 22
         */
        family?: number;
        /**
         * Log type. Currently, only **NFLOG** is supported. This parameter applies only to PCs/2-in-1 devices.
         *
         * When adding a firewall filter rule, this parameter is optional. If configured, it only takes effect when data
         * packets are dropped or rejected.
         *
         * When removing firewall filter rules, this parameter is optional if a chain is cleared. The clearing of the entire
         * chain is not affected. When removing a single rule, the value of this parameter must be the same as that of the
         * rule. Otherwise, the filter rule may have been removed, but logs are still recorded. When removing the same
         * filter rule, you must remove the rule in the sequence in which the rule is added.
         *
         * When obtaining firewall filter rules, the **logType** field can be obtained only when logs take effect.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 23
         */
        logType?: LogType;
    }
    /**
     * Represents a domain name filtering rule.
     *
     * In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22.
     *
     * [LogType]{@link networkManager.LogType} is supported since API version 23.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    interface DomainFilterRule {
        /**
         * Domain name. This parameter is mandatory when a domain name filtering rule is added. Segment domain name matching
         * is supported. For example, if `domainName` is set to `example.com`, then `example.com`, `www.example.com`, and
         * `www.test.example.com` will be matched, while `linkexample.com` will not.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        domainName?: string;
        /**
         * UID of the application.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        appUid?: string;
        /**
         * Action to take, that is, receive or discard the data packets.
         *
         * This parameter is mandatory when a domain name filtering rule is added.
         *
         * This parameter is optional when a domain name filtering rule is removed. If this parameter is left empty, all
         * [Action]{@link networkManager.Action} chains are cleared, and **domainName** and **appUid** must be also left
         * empty.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        action?: Action;
        /**
         * Direction chains to which the rule applies.
         *
         * This parameter is optional when a domain name filtering rule is added. If this parameter is null or set to output
         * chain or input chain, the output chain takes effect. If this parameter is set to a forward chain, **appUid** must
         * be empty. Otherwise, error code 401 will be returned.
         *
         * This parameter is optional when a domain name filtering rule is removed. If the value is empty, all
         * [Direction]{@link networkManager.Direction} chains are cleared, and **domainName** and **appUid** must be empty.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 15
         */
        direction?: Direction;
        /**
         * IP protocol version. The value can be **1** (IPv4) or **2** (IPv6).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 22
         */
        family?: number;
        /**
         * Log type. Currently, only **NFLOG** is supported. This parameter applies only to PCs/2-in-1 devices.
         *
         * This parameter is optional when you add a domain name filtering rule. If configured, it only takes effect when
         * data packets are dropped or rejected.
         *
         * When removing domain name filter rules, this parameter is optional if a chain is cleared. The clearing of the
         * entire chain is not affected. When removing a single rule, the value of this parameter must be the same as that
         * of the rule. Otherwise, the filter rule may have been removed, but logs are still recorded. When removing the
         * same filter rule, you must remove the rule in the sequence in which the rule is added.
         *
         * When obtaining domain name filter rules, the **logType** field can be obtained only when logs take effect.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 23
         */
        logType?: LogType;
    }
    /**
     * Enumerates Ethernet connection configuration modes.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    enum IpSetMode {
        /**
         * Static configuration of network information for Ethernet connection. When this mode is set, the IP address,
         * subnet mask, default gateway, and DNS server need to be configured synchronously.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 23
         */
        STATIC = 0,
        /**
         * Dynamic configuration of network information for Ethernet connection. When this mode is set, the DHCP server in
         * the network automatically assigns the IP address and other related information.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 23
         */
        DHCP = 1
    }
    /**
     * Enumerates Ethernet network interface configurations. Only IPv4 is supported.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    interface InterfaceConfig {
        /**
         * Ethernet connection configuration mode.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 23
         */
        ipSetMode: IpSetMode;
        /**
         * Static IP address. The value ranges from **0.0.0.0** to **255.255.255.255**. (This parameter is not required in
         * DHCP mode.)
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 23
         */
        ipAddress?: string;
        /**
         * Gateway. The value ranges from **0.0.0.0** to **255.255.255.255**. (This parameter is not required in DHCP mode.)
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 23
         */
        gateway?: string;
        /**
         * Subnet mask. The value ranges from **0.0.0.0** to **255.255.255.255**. (This parameter is not required in DHCP
         * mode.)
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 23
         */
        netMask?: string;
        /**
         * DNS service address. The value ranges from **0.0.0.0** to **255.255.255.255**. (This parameter is not required in
         * DHCP mode.) Multiple addresses are separated by commas (,).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 23
         */
        dnsServers?: string;
    }
    /**
     * Obtains all activated wired network interfaces. This API is suitable for enterprise network management scenarios,
     * such as viewing available network connections on the current device, auditing network interface status, and
     * preparing for subsequent network configuration operations. It helps enterprises understand device network
     * connection status, facilitating centralized management of network resources and troubleshooting of network issues.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Array<string> } Names of all activated wired network interfaces.
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
    function getAllNetworkInterfacesSync(admin: Want): Array<string>;
    /**
     * Obtains the device IP address based on the network interface. This API is suitable for enterprise network
     * management scenarios, such as network audit, device positioning, network connection troubleshooting, and IP address
     * allocation management. It helps enterprise IT administrators understand device network configurations, facilitating
     * network management and fault diagnosis.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } networkInterface - Network port.
     * @returns { string } IP address of the network interface specified by the device.
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
    function getIpAddressSync(admin: Want, networkInterface: string): string;
    /**
     * Obtains the MAC address of a device based on the network interface. This API is suitable for enterprise network
     * management scenarios, such as device identification, network access control, MAC address audit, and device asset
     * management. It helps enterprises identify and track devices, implementing refined network access control.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } networkInterface - Network port.
     * @returns { string } MAC address of the network interface specified by the device.
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
    function getMacSync(admin: Want, networkInterface: string): string;
    /**
     * Queries whether a specified network interface is disabled.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } networkInterface - Network port.
     * @returns { boolean } Returns **true** if the network port is disabled; returns **false** otherwise.
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
    function isNetworkInterfaceDisabledSync(admin: Want, networkInterface: string): boolean;
    /**
     * Queries whether a specified network interface is disabled. This API is suitable for enterprise network management
     * scenarios, such as checking network interface status, auditing network interface usage, and verifying the execution
     * effect of network policies. It helps enterprises determine whether their network interface management policies have
     * taken effect, facilitating policy adjustment and troubleshooting.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { string } networkInterface - Network port.
     * @returns { boolean } Returns **true** if the network port is disabled; returns **false** otherwise.
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
    function isNetworkInterfaceDisabledSync(admin: Want | null, networkInterface: string): boolean;
    /**
     * Disables the device from using the specified network interface. This API is suitable for enterprise network
     * security management and control scenarios. It can be used to disable high-risk network interfaces, restrict devices
     * from using specific network connections, and prevent data leaks through network interfaces. This helps enterprises
     * reduce network security risks and prevent attacks or data leaks through specific network interfaces.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } networkInterface - Network port.
     * @param { boolean } isDisabled - Network port status to set. The value **true** means to disable the network port,
     *     and **false** means to enable the network port.
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
    function setNetworkInterfaceDisabledSync(admin: Want, networkInterface: string, isDisabled: boolean): void;
    /**
     * Sets the global network proxy. This API is suitable for enterprise network management scenarios, such as setting a
     * unified network proxy for an enterprise, implementing network access audit, controlling network access paths, and
     * optimizing network performance. It helps enterprises centrally manage network access, making network access
     * auditable and controllable.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { connection.HttpProxy } httpProxy - Global HTTP proxy to set.
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
    function setGlobalProxySync(admin: Want, httpProxy: connection.HttpProxy): void;
    /**
     * Sets the network proxy for a specified user. This API is suitable for network management scenarios in enterprise
     * environments with multiple users. For example, you can set different network proxy policies for different users,
     * implement user-level network access control, and meet the network access requirements of different users, helping
     * enterprises implement refined user-level network management.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { connection.HttpProxy } httpProxy - HTTP proxy configuration of the network.
     * @param { number } accountId - User ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 15
     */
    function setGlobalProxyForAccount(admin: Want, httpProxy: connection.HttpProxy, accountId: number): void;
    /**
     * Obtains the global network proxy. This API is suitable for enterprise network management scenarios, such as
     * auditing the current network proxy configuration, verifying whether the proxy policy takes effect, and
     * troubleshooting network access issues. It helps enterprises check the network proxy settings and ensure that the
     * network access policy is correctly executed.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { connection.HttpProxy } Global HTTP proxy configuration information.
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
    function getGlobalProxySync(admin: Want): connection.HttpProxy;
    /**
     * Obtains the network proxy for a specified user. This API is suitable for network management scenarios in enterprise
     * environments with multiple users, such as auditing user-level network proxy configurations, verifying user network
     * access policies, and troubleshooting user network access issues. It helps enterprises check and verify user-level
     * network management policies.
     *
     * > **NOTE**
     * >
     * > This API is used to obtain the proxy configuration of a specified user set by the **setGlobalProxyForAccount**
     * > API. To obtain the global proxy configuration that applies to all users, you are advised to use the
     * > [getGlobalProxySync]{@link networkManager.getGlobalProxySync} API.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application. [since 15 - 19]
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application. [since 20]
     * @param { number } accountId - User ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of
     *     **@ohos.account.osAccount** to obtain the user ID.
     * @returns { connection.HttpProxy } HTTP proxy configuration of the network.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities. [since 20]
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 15
     */
    function getGlobalProxyForAccount(admin: Want | null, accountId: number): connection.HttpProxy;
    /**
     * Adds firewall rules for the device. This API is suitable for enterprise network security
     * management and control scenarios. For example, it can be used to restrict network access from specific IP
     * addresses, prevent malicious network attacks, control network communication of applications, and manage the
     * trustlist or blocklist for network access. This helps enterprises implement refined control over network access and
     * prevent network attacks and data leaks.
     *
     * In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22.
     *
     * [LogType]{@link networkManager.LogType} is supported since API version 23.
     *
     * > **NOTE**
     * >
     * > - After a rule with [Action]{@link networkManager.Action} set to **ALLOW** is added, a rule with **Action** set
     * > to **DENY** is added by default to discard or intercept all network data packets that do not meet the **ALLOW**
     * > rule.
     * >
     * > - After the device is restarted, the firewall rules are cleared.
     * >
     * > - Rule matching order: Domain name filtering rules (added via
     * > [addDomainFilterRule]{@link networkManager.addDomainFilterRule}) are matched first, followed by IP firewall rules
     * > added by this API. Within both domain name rules and IP rules, matching is performed in the order of ALLOW, DENY,
     * > and REJECT [actions]{@link networkManager.Action}.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { FirewallRule } firewallRule - Firewall rule to add.
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
    function addFirewallRule(admin: Want, firewallRule: FirewallRule): void;
    /**
     * Removes a firewall rule. This API is suitable for enterprise network security policy adjustment scenarios, such as
     * canceling certain network access restrictions, adjusting firewall policies, and clearing outdated or invalid rules.
     * It helps enterprises flexibly adjust network security policies and ensure that network access control policies meet
     * actual requirements.
     *
     * In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22.
     *
     * [LogType]{@link networkManager.LogType} is supported since API version 23.
     *
     * If there is no rule with [Action]{@link networkManager.Action} being **ALLOW** after the rule is removed, the
     * **DENY** rules that are added by default with [addFirewallRule]{@link networkManager.addFirewallRule} will be
     * removed.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { FirewallRule } firewallRule - Firewall rule to remove. If the value is empty, all firewall rules will be
     *     removed.
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
    function removeFirewallRule(admin: Want, firewallRule?: FirewallRule): void;
    /**
     * Queries firewall rules of a device. This API is suitable for enterprise network security audit scenarios, such as
     * checking the current firewall policy configuration, auditing network access control rules, verifying whether
     * firewall rules are correctly executed, and troubleshooting network access issues. It helps enterprises audit and
     * verify network security policies and ensure that network access control meets security requirements.
     *
     * In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22.
     *
     * [LogType]{@link networkManager.LogType} is supported since API version 23.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Array<FirewallRule> } A list of firewall rules configured for the device is returned. If the operation
     *     fails, an exception will be thrown.
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
    function getFirewallRules(admin: Want): Array<FirewallRule>;
    /**
     * Adds domain name filtering rules for the device.<!--RP3--><!--RP3End-->
     *
     * In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22.
     *
     * [LogType]{@link networkManager.LogType} is supported since API version 23.
     *
     * > **NOTE**
     * >
     * > - After a rule with [Action]{@link networkManager.Action} set to **ALLOW** is added, a default **DENY** rule is
     * > added automatically to discard or intercept domain name resolution packets that are not covered by the **ALLOW**
     * > rule.
     * >
     * > - The added rules will be cleared after the device restarts.
     * >
     * > - To prevent interception rules from becoming ineffective due to DNS caching, it is recommended that you
     * > configure domain name filtering rules immediately after the system starts up. If interception fails because of
     * > DNS caching, restart the system to clear the cache and restore the interception function.
     * >
     * > - Rule matching order: Domain name filtering rules added by this API are matched first, followed by IP firewall
     * > rules (added via [addFirewallRule]{@link networkManager.addFirewallRule}). Within both domain name rules and IP
     * > rules, matching is performed in the order of ALLOW, DENY, and REJECT [actions]{@link networkManager.Action}.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { DomainFilterRule } domainFilterRule - Domain name filtering rule object, including the domain name,
     *     application UID, and IP protocol version.
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
    function addDomainFilterRule(admin: Want, domainFilterRule: DomainFilterRule): void;
    /**
     * Removes the domain name filtering rules. This API is suitable for enterprise network security policy adjustment
     * scenarios, such as canceling access restrictions on certain domain names, adjusting domain name filtering policies,
     * removing outdated or invalid rules, and resolving false positive blocking issues. It helps enterprises flexibly
     * adjust domain name access policies to ensure that network access control policies meet actual business
     * requirements.
     *
     * In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22.
     *
     * [LogType]{@link networkManager.LogType} is supported since API version 23.
     *
     * If there is no rule with [Action]{@link networkManager.Action} being **ALLOW** after the rule is removed, the
     * **DENY** rules that are added by default with [addDomainFilterRule]{@link networkManager.addDomainFilterRule} will
     * be removed.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { DomainFilterRule } domainFilterRule - Domain name filtering rule to remove. If the value is empty, all
     *     domain name filtering rules will be removed.
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
    function removeDomainFilterRule(admin: Want, domainFilterRule?: DomainFilterRule): void;
    /**
     * Obtains domain name filtering rules. This API is suitable for enterprise network security audit scenarios, such as
     * checking current domain name filtering policy configurations, auditing domain name access control rules, verifying
     * whether domain name filtering rules are correctly executed, and troubleshooting domain name access issues. It helps
     * enterprises review and validate domain name access control policies to ensure network access control complies with
     * security requirements.
     *
     * In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22.
     *
     * [LogType]{@link networkManager.LogType} is supported since API version 23.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Array<DomainFilterRule> } A list of domain name filtering rules configured for the device is returned.
     *     If the operation fails, an exception will be thrown.
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
    function getDomainFilterRules(admin: Want): Array<DomainFilterRule>;
    /**
     * Adds an access point name (APN).
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APN
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Record<string, string> } apnInfo - APN information to be added. After the setting, the system uses these
     *     parameters to configure the mobile data network access point, affecting the network connection method and data
     *     transmission path.
     *     <br>- **apnName**: APN identifier, which is mandatory.
     *     <br>- **mcc**: 3-digit mobile country code (MCC), which is mandatory.
     *     <br>- **mnc**: 2-digit or 3-digit mobile network code (MNC), which is mandatory.
     *     <br>- **apn**: access point name, which is mandatory.
     *     <br>- **type**: APN service type, which is optional.
     *     <br>- **user**: user name for APN authentication, which is optional.
     *     <br>- **password**: password for APN authentication, which is optional.
     *     <br>- **proxy**: address of the proxy server for a common data connection, which is optional.
     *     <br>- **mmsproxy**: dedicated proxy address of the MMS service, which is optional.
     *     <br>- **authType**: authentication protocol type of the APN, which is optional.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function addApn(admin: Want, apnInfo: Record<string, string>): void;
    /**
     * Deletes the APN. This API is suitable for enterprise mobile network configuration management scenarios, such as
     * removing invalid APN configurations, adjusting mobile network access point settings, and preventing the use of
     * incorrect APN configurations. It helps enterprises maintain correct mobile network configurations and ensure that
     * devices connect to mobile networks through the appropriate access points.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APN
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } apnId - APN ID to be deleted. After the setting, the system will remove the APN configuration,
     *     and the corresponding access point will no longer be available. You can obatin the device APN information via
     *     [networkManager.queryApn]{@link networkManager.queryApn}.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function deleteApn(admin: Want, apnId: string): void;
    /**
     * Updates the APN. This API is suitable for enterprise mobile network configuration management scenarios, such as
     * modifying APN configuration parameters, adjusting carrier settings, and optimizing mobile network connection
     * performance. It helps enterprises flexibly adjust mobile network configurations and ensure that the mobile network
     * connection parameters of devices meet actual requirements.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APN
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Record<string, string> } apnInfo - APN information to be updated. After the setting, the system uses the
     *     updated parameters to modify the corresponding APN configuration, affecting the network connection mode and
     *     data transmission path.
     *     <br>- **apnName**: APN identifier, which is optional.
     *     <br>- **mcc**: 3-digit mobile country code (MCC), which is optional.
     *     <br>- **mnc**: 2-digit or 3-digit mobile network code (MNC), which is optional.
     *     <br>- **APN**: access point name, which is optional.
     *     <br>- **type**: APN service type, which is optional.
     *     <br>- **user**: user name for APN authentication, which is optional.
     *     <br>- **password**: password for APN authentication, which is optional.
     *     <br>- **proxy**: address of the proxy server for a common data connection, which is optional.
     *     <br>- **mmsproxy**: dedicated proxy address of the MMS service, which is optional.
     *     <br>- **authType**: authentication protocol type of the APN, which is optional.
     * @param { string } apnId - APN ID to be updated. You can obatin the device APN information via
     *     [networkManager.queryApn]{@link networkManager.queryApn}.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function updateApn(admin: Want, apnInfo: Record<string, string>, apnId: string): void;
    /**
     * Sets the preferred APN.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APN
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } apnId - Preferred APN ID to be set. You can obatin the device APN information via
     *     [networkManager.queryApn]{@link networkManager.queryApn}.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function setPreferredApn(admin: Want, apnId: string): void;
    /**
     * Queries the APN ID. This API is suitable for enterprise mobile network configuration audit scenarios, such as
     * finding APNs with specific configurations, verifying whether an APN configuration exists, and providing APN ID
     * parameters for APN management operations. It helps enterprises locate and manage APN configurations, and supplies
     * the necessary parameter information for updating and deleting APNs.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APN
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Record<string, string> } apnInfo - APN information. After the setting, the system filters the APN
     *     configurations based on the specified conditions and returns the list of APN IDs that meet the conditions.
     *     <br>- **apnName**: APN identifier, which is optional.
     *     <br>- **mcc**: 3-digit mobile country code (MCC), which is optional.
     *     <br>- **mnc**: 2-digit or 3-digit mobile network code (MNC), which is optional.
     *     <br>- **apn**: access point name, which is optional.
     *     <br>- **type**: APN service type, which is optional.
     *     <br>- **user**: user name for APN authentication, which is optional.
     *     <br>- **proxy**: address of the proxy server for a common data connection, which is optional.
     *     <br>- **mmsproxy**: dedicated proxy address of the MMS service, which is optional.
     *     <br>- **authType**: authentication protocol type of the APN, which is optional.
     * @returns { Array<string> } APN ID obtained.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function queryApn(admin: Want, apnInfo: Record<string, string>): Array<string>;
    /**
     * Queries the APN parameter information. This API is suitable for enterprise mobile network configuration audit
     * scenarios, such as checking the configuration parameters of a specific APN, verifying whether the APN configuration
     * is correct, and auditing mobile network access point settings. It helps enterprises review and validate APN
     * configurations to ensure that mobile network settings meet requirements.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APN
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } apnId - Specified APN ID. After the setting, the system queries the detailed parameter settings
     *     corresponding to the APN ID. You can obtain device information using
     *     [networkManager.queryApn]{@link networkManager.queryApn}.
     * @returns { Record<string, string> } APN parameter information of the specified APN ID.
     *     <br>- **apnName**: APN identifier.
     *     <br>- **mcc**: 3-digit mobile country code (MCC).
     *     <br>- **mnc**: 2-digit or 3-digit mobile network code (MNC).
     *     <br>- **apn**: access point name.
     *     <br>- **type**: APN service type.
     *     <br>- **user**: user name for APN authentication.
     *     <br>- **proxy**: address of the proxy server for a common data connection.
     *     <br>- **mmsproxy**: dedicated proxy address of the MMS service.
     *     <br>- **authType**: authentication protocol type of the APN.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function queryApn(admin: Want, apnId: string): Record<string, string>;
    /**
     * Turns on mobile data.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { boolean } isForce - Whether to forcibly enable mobile data.
     *     <br>The value **true** means to forcibly enable mobile data. Once enabled, it cannot be turned off manually; it
     *     can only be disabled via the [turnOffMobileData]{@link networkManager.turnOffMobileData} API. The value
     *     **false** means not to forcibly enable mobile data. It can be turned off manually. This API is suitable for
     *     enterprise network security management and control scenarios, such as preventing data leaks via mobile data
     *     networks, controlling network connection methods, reducing communication costs, and ensuring that devices use
     *     only enterprise networks. It helps enterprises control how devices access networks, mitigating security risks
     *     and preventing data exfiltration through mobile data networks.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function turnOnMobileData(admin: Want, isForce: boolean): void;
    /**
     * Turns off mobile data.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function turnOffMobileData(admin: Want): void;
    /**
     * Sets the IP address of a specific Ethernet interface. This API is suitable for enterprise network management
     * scenarios, such as configuring static IP addresses for devices, centrally managing IP address allocation for
     * enterprise network devices, and setting network parameters. It helps enterprises centrally manage network
     * configurations and ensures that device network parameters comply with enterprise network management policies.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_NETWORK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } networkInterface - Network interface name to set.
     * @param { InterfaceConfig } config - Network interface configuration to set.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 9201010 - Ethernet configuration failed. Ethernet device not connected.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    function setEthernetConfig(admin: Want, networkInterface: string, config: InterfaceConfig): void;
}
export default networkManager;

```
