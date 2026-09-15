# @ohos.net.vpnExtension.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2023 Huawei Device Co., Ltd.
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
 * @file Enhanced VPN Management
 * @kit NetworkKit
 */
import type connection from './@ohos.net.connection';
import type _VpnExtensionContext from './application/VpnExtensionContext';
import type Want from './@ohos.app.ability.Want';
/**
 * This module implements virtual private network (VPN) management, such as starting and stopping a third-party VPN.
 * Third-party VPNs refer to VPN services provided by third parties. They usually support more security and privacy
 * functions and more comprehensive customization options. Currently, the VPN capabilities provided to third-party
 * applications are primarily used for creating virtual NICs and configuring VPN routing information. The connection
 * tunnel process and internal connection protocols need to be implemented by the applications themselves.
 *
 * > **NOTE**
 * >
 * > The following modules cannot be referenced in the VpnExtensionAbility, as doing so may cause the program to exit
 * > abnormally:
 *
 * > - [@ohos.contact (Contacts)]{@link @ohos.contact:contact}
 *
 * > - [@ohos.geolocation]{@link @ohos.geolocation:geolocation},
 * > [@ohos.geoLocationManager (Geolocation Manager)]{@link @ohos.geoLocationManager:geoLocationManager}
 *
 * > - [@ohos.multimedia.audio (Audio Management)]{@link @ohos.multimedia.audio:audio}
 *
 * > - [@ohos.multimedia.camera (Camera Management)]{@link @ohos.multimedia.camera:camera}
 *
 * > - [@ohos.telephony.call (Call)]{@link @ohos.telephony.call:call}
 *
 * > - [@ohos.telephony.sim (SIM Management)]{@link @ohos.telephony.sim:sim}
 *
 * > - [@ohos.telephony.sms (SMS)]{@link @ohos.telephony.sms:sms}
 *
 * @syscap SystemCapability.Communication.NetManager.Vpn
 * @since 11
 */
declare namespace vpnExtension {
    /**
     * Defines the network link address information.
     *
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 11
     */
    export type LinkAddress = connection.LinkAddress;
    /**
     * Defines the network route information.
     *
     * @syscap SystemCapability.Communication.NetManager.Core
     * @since 11
     */
    export type RouteInfo = connection.RouteInfo;
    /**
     * Defines the VPN extension context. It allows access to serviceExtension-specific resources.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 11
     */
    export type VpnExtensionContext = _VpnExtensionContext;
    /**
     * Enables the VPN extension ability. This API uses a promise to return the result.
     *
     * @param { Want } want - Want information.
     *     <br> Note: From API version 22, the **parameters** field in **want** can be passed when the VPN is started for
     *     the first time.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @throws { BusinessError } 16000001 - The specified ability does not exist.
     * @throws { BusinessError } 16000002 - Incorrect ability type.
     * @throws { BusinessError } 16000006 - Cross-user operations are not allowed.
     * @throws { BusinessError } 16000008 - The crowdtesting application expires.
     * @throws { BusinessError } 16000011 - The context does not exist.
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 16200001 - The caller has been released.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    function startVpnExtensionAbility(want: Want): Promise<void>;
    /**
     * Stops the VPN extension ability. This API uses a promise to return the result.
     *
     * @param { Want } want - Want information.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @throws { BusinessError } 16000001 - The specified ability does not exist.
     * @throws { BusinessError } 16000002 - Incorrect ability type.
     * @throws { BusinessError } 16000006 - Cross-user operations are not allowed.
     * @throws { BusinessError } 16000011 - The context does not exist.
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 16200001 - The caller has been released.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    function stopVpnExtensionAbility(want: Want): Promise<void>;
    /**
     * Creates a **VpnConnection** object.
     *
     * > **NOTE**
     * >
     * > Before calling **createVpnConnection**, call **startVpnExtensionAbility** to enable the VPN function.
     *
     * @param { VpnExtensionContext } context - Specified context.
     * @returns { VpnConnection } VPN connection object.
     * @throws { BusinessError } 401 - Parameter error.
     * @syscap SystemCapability.Communication.NetManager.Vpn
     * @stagemodelonly
     * @since 11
     */
    function createVpnConnection(context: VpnExtensionContext): VpnConnection;
    /**
     * Creates a VPN observer object. It is used to listen for VPN-related events.
     *
     * @returns { VpnObserver } VPN observer object.
     * @syscap SystemCapability.Communication.NetManager.Vpn
     * @stagemodelonly
     * @since 26.0.0
     */
    function createVpnObserver(): VpnObserver;
    /**
     * Defines a VPN observer object. It is used to listen for VPN-related events. Before calling **VpnObserver** APIs,
     * you need to create a VPN connection object by calling
     * [vpnExtension.createVpnObserver]{@link vpnExtension.createVpnObserver}.
     *
     * @syscap SystemCapability.Communication.NetManager.Vpn
     * @stagemodelonly
     * @since 26.0.0
     */
    export interface VpnObserver {
        /**
         * Registers a listener for the user authorization result. The authorization result is displayed in a dialog box
         * after [startVpnExtensionAbility]{@link vpnExtension.startVpnExtensionAbility} is called. The notification is sent
         * only when the user taps the dialog box, and only the result of the current VPN is received. If you do not need to
         * listen for the authorization result, call [offAuthorizationResult]{@link vpnExtension.VpnObserver.off} to cancel
         * the registration.
         *
         * > **NOTE**
         * >
         * > If this API is called multiple times, only the last callback takes effect.
         *
         * @param { Callback<boolean> } callback - Callback used to return the user authorization result. The value **true**
         *     indicates that the user agrees to the authorization, and the value **false** indicates the opposite.
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @stagemodelonly
         * @since 26.0.0
         */
        onAuthorizationResult(callback: Callback<boolean>): void;
        /**
         * Unregisters a listener for the user authorization result.
         *
         * > **NOTE**
         * >
         * > If you have called [onAuthorizationResult]{@link vpnExtension.VpnObserver.on} multiple times to register
         * > listeners and want to unregister the listener, you need to pass the callback passed in the last call or pass no
         * > parameter.
         *
         * @param { Callback<boolean> } [callback] - Listener callback used to return the user authorization result.
         *     <br>If this parameter is passed, the specified listener is unregistered. If no parameter is passed, all
         *     registered listeners are unregistered.
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @stagemodelonly
         * @since 26.0.0
         */
        offAuthorizationResult(callback?: Callback<boolean>): void;
    }
    /**
     * Defines a VPN connection object. Before calling **VpnConnection** APIs, you need to create a VPN connection object
     * by calling **vpnExt.createVpnConnection**.
     *
     * @syscap SystemCapability.Communication.NetManager.Vpn
     * @since 11
     */
    export interface VpnConnection {
        /**
         * Creates a VPN based on the specified configuration. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > You are advised to call [destroy()]{@link vpnExtension.VpnConnection.destroy()} or
         * > [destroy(vpnId: string)]{@link vpnExtension.VpnConnection.destroy(vpnId: string)} to destroy the VPN and clear
         * > resources when the VPN is not needed.
         *
         * @param { VpnConfig } config - VPN configuration.
         * @returns { Promise<number> } Promise used to return the result, which is the file descriptor of the virtual network
         *     interface card (vNIC).
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2200001 - Invalid parameter value.
         * @throws { BusinessError } 2200002 - Operation failed. Cannot connect to service.
         * @throws { BusinessError } 2200003 - System internal error.
         * @throws { BusinessError } 2203001 - VPN creation denied, please check the user type.
         * @throws { BusinessError } 2203002 - VPN exist already, please execute destroy first.
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        create(config: VpnConfig): Promise<number>;
        /**
         * Generates a unique VPN ID. This API uses a promise to return the result.
         *
         * To use the multi-VPN capability of the system, you need to call this API to generate a VPN ID and configure it in
         * **VpnConfig**.
         *
         * > **NOTE**
         * >
         * > Currently, the multi-VPN capability of the system supports only IPv4.
         *
         * @returns { Promise<string> } Promise used to return the result.
         * @throws { BusinessError } 19900001 - Invalid parameter value.
         * @throws { BusinessError } 19900002 - System internal error.
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 20
         */
        generateVpnId(): Promise<string>;
        /**
         * Protects sockets against a VPN connection. The data sent through sockets is directly transmitted over the
         * physical network and therefore the traffic does not traverse through the VPN. This API uses a promise to return
         * the result.
         *
         * @param { number } socketFd - Socket file descriptor. It can be obtained through
         *     [getSocketFd]{@link @ohos.net.socket:socket.TCPSocket.getSocketFd()}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2200001 - Invalid parameter value.
         * @throws { BusinessError } 2200002 - Operation failed. Cannot connect to service.
         * @throws { BusinessError } 2200003 - System internal error.
         * @throws { BusinessError } 2203004 - Invalid socket file descriptor.
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        protect(socketFd: number): Promise<void>;
        /**
         * Destroys a VPN. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 2200002 - Operation failed. Cannot connect to service.
         * @throws { BusinessError } 2200003 - System internal error.
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        destroy(): Promise<void>;
        /**
         * Destroys a VPN based on the specified VPN ID. This API uses a promise to return the result.
         *
         * @param { string } vpnId - Unique VPN ID.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 19900001 - Invalid parameter value.
         * @throws { BusinessError } 19900002 - System internal error.
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 20
         */
        destroy(vpnId: string): Promise<void>;
        /**
         * Protects application processes against a VPN connection. The data sent through the protected processes is
         * transmitted over the physical network without traversing the VPN. This API uses a promise to return the result.
         *
         * @returns { Promise<void>} Promise that returns no value.
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 22
         */
        protectProcessNet(): Promise<void>;
    }
    /**
     * Defines the VPN configuration.
     *
     * @syscap SystemCapability.Communication.NetManager.Vpn
     * @since 11
     */
    export interface VpnConfig {
        /**
         * Unique VPN ID.
         *
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 20
         */
        vpnId?: string;
        /**
         * IP addresses of vNICs. Before API version 23, a maximum of 64 IP addresses are supported. Starting from API
         * version 23, a maximum of 2000 IP addresses are supported.
         *
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        addresses: Array<LinkAddress>;
        /**
         * Route information of the vNIC. Before API version 23, a maximum of 1024 routes can be configured. Starting from
         * API version 23, a maximum of 10,000 routes can be configured.
         *
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        routes?: Array<RouteInfo>;
        /**
         * IP address of the DNS server. After the IP address is configured, when the VPN is active and proxy-enabled
         * applications access the Internet, the configured DNS server will be used for DNS queries.
         *
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        dnsAddresses?: Array<string>;
        /**
         * List of DNS search domains.
         *
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        searchDomains?: Array<string>;
        /**
         * Maximum transmission unit (MTU), in bytes. The value range is [576,1500].
         *
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        mtu?: number;
        /**
         * Whether IPv4 is supported. The value **true** indicates that the IPv4 is supported, and the value **false**
         * indicates the opposite. The default value is **true**.
         *
         * Note: If the IPv4 is supported, you need to configure IPv4 addresses in **addresses**.
         *
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        isIPv4Accepted?: boolean;
        /**
         * Whether IPv6 is supported. The value **true** indicates that the IPV6 is supported, and the value **false**
         * indicates the opposite. The default value is **false**.
         *
         * Note: If the IPv6 is supported, you need to configure IPv6 addresses in **addresses**.
         *
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        isIPv6Accepted?: boolean;
        /**
         * Whether the built-in VPN is supported. The value **true** indicates that the built-in VPN is supported, and the
         * value **false** indicates the opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        isInternal?: boolean;
        /**
         * Whether the blocking mode is used. The value **true** indicates that the blocking mode is used, and the value
         * **false** indicates the opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        isBlocking?: boolean;
        /**
         * List of trusted applications, which are represented by bundle names of the string type. After such a list is
         * configured, only the applications in the list can be proxied by the VPN according to the specified **routes**.
         * Before API version 23, a maximum of 64 trusted application bundle names can be configured. Since API version 23,
         * a maximum of 256 trusted application bundle names can be configured.
         *
         * **Note**: Configure either **trustedApplications** or **blockedApplications** as they are mutually exclusive.
         *
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        trustedApplications?: Array<string>;
        /**
         * List of blocked applications, which are represented by bundle names of the string type. After such a list is
         * configured, only applications that are not in the list can be proxied by the VPN according to the specified
         * **routes**. Before API version 23, a maximum of 64 blocked application bundle names can be configured. Since API
         * version 23, a maximum of 256 blocked application bundle names can be configured.
         *
         * **Note**: Configure either **trustedApplications** or **blockedApplications** as they are mutually exclusive.
         *
         * @syscap SystemCapability.Communication.NetManager.Vpn
         * @since 11
         */
        blockedApplications?: Array<string>;
    }
}
export default vpnExtension;

```
