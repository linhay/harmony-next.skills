# @ohos.net.netFirewall.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2024 Huawei Device Co., Ltd.
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
 * @file Network Firewall
 * @kit NetworkKit
 */
/**
 * The **netFirewall** module implements the network firewall functionality for applications. It allows applications to
 * query the firewall interception records of the device.
 *
 * @syscap SystemCapability.Communication.NetManager.NetFirewall
 * @since 14
 */
declare namespace netFirewall {
    /**
     * Sets the firewall policy for a system user ID, including the firewall switch status and default inbound or outbound
     * behavior (allow or deny). Different firewall policies can be configured for different system user IDs. This API
     * uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > If this API is called by multiple applications under the same system user, the latest delivered policy prevails.
     * > **Required permission**: ohos.permission.MANAGE_NET_FIREWALL
     *
     * @permission ohos.permission.MANAGE_NET_FIREWALL
     * @param { number } userId - System user ID, which must exist.
     * @param { NetFirewallPolicy } policy - Firewall policy.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100001 - Invalid parameter value.
     * @throws { BusinessError } 2100002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 29400000 - The specified user does not exist.
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    function setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>;
    /**
     * Queries the firewall policy for a system user ID, including the firewall switch status and default inbound or
     * outbound behavior (allow or deny). This API uses a promise to return the result.
     *
     * **Required permission**: ohos.permission.GET_NET_FIREWALL
     *
     * @permission ohos.permission.GET_NET_FIREWALL
     * @param { number } userId - System user ID, which must exist.
     * @returns { Promise<NetFirewallPolicy> } Promise used to return the result, which is a firewall policy.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100001 - Invalid parameter value.
     * @throws { BusinessError } 2100002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 29400000 - The specified user does not exist.
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    function getNetFirewallPolicy(userId: number): Promise<NetFirewallPolicy>;
    /**
     * Adds a firewall rule for the system user ID. The supported rule types are IP, Domain, and DNS. This API uses a
     * promise to return the result.
     *
     * > **Description**
     * >
     * > 1. The priority of firewall rules is described as follows (there is no requirement on the call sequence of
     * > [setNetFirePolicy]{@link netFirewall.setNetFirewallPolicy} and
     * > [addNetFirewallRule]{@link netFirewall.addNetFirewallRule}):
     * >
     * > - Call [setNetFirePolicy]{@link netFirewall.setNetFirewallPolicy} to set the default policy to **DENY** and call
     * > [addNetFirewallRule]{@link netFirewall.addNetFirewallRule} to add an explicit rule. The priorities of the rules
     * > are as follows:
     * >
     * > - Explicit denying rule
     * >
     * > - Explicit allowing rule
     * >
     * > - Default denying policy
     * >
     * > - Call [setNetFirePolicy]{@link netFirewall.setNetFirewallPolicy} to set the default policy to **ALLOW** and call
     * > [addNetFirewallRule]{@link netFirewall.addNetFirewallRule} to add an explicit rule. The priorities of the rules
     * > are as follows:
     * >
     * > - Explicit allowing rule
     * >
     * > - Explicit denying rule
     * >
     * > - Default allowing policy
     * >
     * > - When the IP address rule and domain name rule of the firewall conflict (the IP of the domain name resolution is
     * > the same as that in the IP address rule, and the rule behavior conflicts):
     * >
     * > - If the access is performed using a domain name, the domain name rule has a higher priority than the IP address
     * > rule and is not affected by the rule of the IP parsed from the domain name.
     * >
     * > - If the access is performed using an IP address, the following rules are followed:
     * >
     * > - If the domain name rule allows the access and the domain name resolution has been performed, the IP address
     * > denying rule or the default denying policy will not take effect, and the access using the IP address will be
     * > allowed.
     * >
     * > - If the domain name rule allows the access and the domain name resolution has not been performed, the IP address
     * > denying rule or the default denying policy will take effect, and the access using the IP address will be denied.
     * >
     * > - If the domain name rule denies the access, the IP address allowing rule or the default policy will take effect,
     * > and the access using the IP address will be allowed.
     * >
     * > 2. Supplementary description of rule types:
     * >
     * > - When the input parameter **rule.type** of **addNetFirewallRule** is set to **RULE_IP**:
     * >
     * > - If **rule.action** is set to **RULE_ALLOW** and **rule.localIps** and **rule.remoteIps** are not configured,
     * > the rule takes effect as full IP range access is allowed.
     * >
     * > - If **rule.action** is set to **RULE_DENY** and **rule.localIps** and **rule.remoteIps** are not configured, the
     * > rule takes effect as full IP range access is denied.
     * >
     * > - If **rule.type** of **addNetFirewallRule** is set to **RULE_DOMAIN** and **rule.domains** is not configured,
     * > the rule does not take effect.
     * >
     * > 3. Description of the upper limit for adding firewall rules:
     * >
     * > - A maximum of 1000 firewall rules can be added for a single system user ID. If this limit is exceeded, error
     * > code **29400001** is reported.
     * >
     * > - A maximum of 2000 firewall rules can be added for all system user IDs. If this limit is exceeded, error code
     * > **29400001** is reported.
     * >
     * > - A maximum of 100 fuzzy domain name rules can be added for all system user IDs. If this limit is exceeded, error
     * > code **29400005** is reported.
     * > **Required permission**: ohos.permission.MANAGE_NET_FIREWALL
     *
     * @permission ohos.permission.MANAGE_NET_FIREWALL
     * @param { NetFirewallRule } rule - Firewall rule.
     * @returns { Promise<number> } Promise used to return the result, which is the firewall rule ID automatically generated
     *     by the system.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100001 - Invalid parameter value.
     * @throws { BusinessError } 2100002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 29400000 - The specified user does not exist.
     * @throws { BusinessError } 29400001 - The number of firewall rules exceeds the maximum.
     * @throws { BusinessError } 29400002 - The number of IP address rules in the firewall rule exceeds the maximum.
     * @throws { BusinessError } 29400003 - The number of port rules in the firewall rule exceeds the maximum.
     * @throws { BusinessError } 29400004 - The number of domain rules in the firewall rule exceeds the maximum.
     * @throws { BusinessError } 29400005 - The number of domain rules exceeds the maximum.
     * @throws { BusinessError } 29400007 - The dns rule is duplication.
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    function addNetFirewallRule(rule: NetFirewallRule): Promise<number>;
    /**
     * Updates a firewall rule. This API uses a promise to return the result.
     *
     * **Required permission**: ohos.permission.MANAGE_NET_FIREWALL
     *
     * @permission ohos.permission.MANAGE_NET_FIREWALL
     * @param { NetFirewallRule } rule - Firewall rule.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100001 - Invalid parameter value.
     * @throws { BusinessError } 2100002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 29400000 - The specified user does not exist.
     * @throws { BusinessError } 29400002 - The number of IP address rules in the firewall rule exceeds the maximum.
     * @throws { BusinessError } 29400003 - The number of port rules in the firewall rule exceeds the maximum.
     * @throws { BusinessError } 29400004 - The number of domain rules in the firewall rule exceeds the maximum.
     * @throws { BusinessError } 29400005 - The number of domain rules exceeds the maximum.
     * @throws { BusinessError } 29400006 - The specified rule does not exist.
     * @throws { BusinessError } 29400007 - The dns rule is duplication.
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    function updateNetFirewallRule(rule: NetFirewallRule): Promise<void>;
    /**
     * Deletes a specified firewall rule of a system user ID. This API uses a promise to return the result.
     *
     * **Required permission**: ohos.permission.MANAGE_NET_FIREWALL
     *
     * @permission ohos.permission.MANAGE_NET_FIREWALL
     * @param { number } userId - System user ID, which must exist.
     * @param { number } ruleId - ID of the firewall rule.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100001 - Invalid parameter value.
     * @throws { BusinessError } 2100002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 29400000 - The specified user does not exist.
     * @throws { BusinessError } 29400006 - The specified rule does not exist.
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    function removeNetFirewallRule(userId: number, ruleId: number): Promise<void>;
    /**
     * Obtains firewall rules by user ID. You need to specify the pagination query parameter when calling this API.
     * Currently, firewall rules can be sorted by name. This API uses a promise to return the result.
     *
     * **Required permission**: ohos.permission.GET_NET_FIREWALL
     *
     * @permission ohos.permission.GET_NET_FIREWALL
     * @param { number } userId - System user ID, which must exist.
     * @param { RequestParam } requestParam - Pagination query parameter. The **orderField** field can be sorted only by
     *     firewall rule name.
     * @returns { Promise<FirewallRulePage> } Promise used to return the result, which is list of firewall rules.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100001 - Invalid parameter value.
     * @throws { BusinessError } 2100002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 29400000 - The specified user does not exist.
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    function getNetFirewallRules(userId: number, requestParam: RequestParam): Promise<FirewallRulePage>;
    /**
     * Obtains a firewall rule based on the specified user ID and rule ID. This API uses a promise to return the result.
     *
     * **Required permission**: ohos.permission.GET_NET_FIREWALL
     *
     * @permission ohos.permission.GET_NET_FIREWALL
     * @param { number } userId - System user ID, which must exist.
     * @param { number } ruleId - ID of the firewall rule.
     * @returns { Promise<NetFirewallRule> } Promise used to return the result, which is a firewall rule.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2100001 - Invalid parameter value.
     * @throws { BusinessError } 2100002 - Operation failed. Cannot connect to service.
     * @throws { BusinessError } 2100003 - System internal error.
     * @throws { BusinessError } 29400000 - The specified user does not exist.
     * @throws { BusinessError } 29400006 - The specified rule does not exist.
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    function getNetFirewallRule(userId: number, ruleId: number): Promise<NetFirewallRule>;
    /**
     * Enumerates the firewall rule directions, including inbound and outbound.
     *
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    enum NetFirewallRuleDirection {
        /**
         * Inbound direction.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        RULE_IN = 1,
        /**
         * Outbound direction.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        RULE_OUT = 2
    }
    /**
     * Enumerates the firewall rule actions, including allowing or denying network connections.
     *
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    enum FirewallRuleAction {
        /**
         * Allowing network connection.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        RULE_ALLOW = 0,
        /**
         * Denying network connection.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        RULE_DENY = 1
    }
    /**
     * Enumerates the firewall rule types, including IP, Domain, and DNS.
     *
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    enum NetFirewallRuleType {
        /**
         * IP address-based firewall rule.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        RULE_IP = 1,
        /**
         * Domain name-based rule.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        RULE_DOMAIN = 2,
        /**
         * DNS-based firewall rule.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        RULE_DNS = 3
    }
    /**
     * Enumerates the sorting methods of firewall rules.
     *
     * > **Description**
     * >
     * > [getNetFirewallRules]{@link netFirewall.getNetFirewallRules} supports only the **ORDER_BY_RULE_NAME** field.
     *
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    enum NetFirewallOrderField {
        /**
         * Sorting of firewall rules by name.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        ORDER_BY_RULE_NAME = 1,
        /**
         * Sorting of firewall rules by time.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        ORDER_BY_RECORD_TIME = 100
    }
    /**
     * Enumerates the sorting order of firewall rules, which can be ascending or descending.
     *
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    enum NetFirewallOrderType {
        /**
         * Sorting in ascending order.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        ORDER_ASC = 1,
        /**
         * Sorting in descending order.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        ORDER_DESC = 100
    }
    /**
     * Defines the firewall policy, including the firewall switch status and default inbound or outbound action (allow or
     * deny).
     *
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    interface NetFirewallPolicy {
        /**
         * Whether to enable the firewall. The value **true** means to enable the firewall, and the value **false** means
         * the opposite.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        isOpen: boolean;
        /**
         * Inbound action.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        inAction: FirewallRuleAction;
        /**
         * Outbound action.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        outAction: FirewallRuleAction;
    }
    /**
     * Defines the IP parameters of the firewall rule. The IP address type can be IPv4 or IPv6. A single IP address or IP
     * address segment is supported.
     *
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    interface NetFirewallIpParams {
        /**
         * **1**: IP address or subnet. In this case, the **address** and **mask** fields must be specified. When a single
         * IP address is used, the **mask** field must be set to **32**.
         *
         * **2**: IP address segment. In this case, the **startIp** and **endIp** fields must be specified.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        type: number;
        /**
         * **1**: IPv4.
         *
         * **2**: IPv6.
         *
         * The default value is **IPv4**. Other values are not supported currently.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        family?: number;
        /**
         * IP address. This parameter is mandatory and valid only when type is set to **1**.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        address?: string;
        /**
         * IPv4: subnet mask.
         *
         * IPv6: address prefix.
         *
         * This parameter is mandatory and valid only when type is set to **1**.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        mask?: number;
        /**
         * Start IP address. This parameter is mandatory and valid only when type is set to **2**. The value ranges from 0.0
         * .0.1 to 255.255.255.254. Otherwise, this parameter will be ignored.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        startIp?: string;
        /**
         * End IP address. This parameter is mandatory and valid only when type is set to **2**. The value ranges from 0.0.0
         * .1 to 255.255.255.254. Otherwise, this parameter will be ignored.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        endIp?: string;
    }
    /**
     * Defines the port parameters of a firewall rule.
     *
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    interface NetFirewallPortParams {
        /**
         * Start port number.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        startPort: number;
        /**
         * End port number.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        endPort: number;
    }
    /**
     * Defines domain name parameters of a firewall rule. Currently, Chinese domain names are not supported.
     *
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    interface NetFirewallDomainParams {
        /**
         * Whether to contain wildcards. The value **true** means to contain wildcards; and the value **false** means the
         * opposite.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        isWildcard: boolean;
        /**
         * If **isWildcard** is set to **false**, the complete domain name, for example, "www.example.cn", needs to be
         * specified.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        domain: string;
    }
    /**
     * Defines the DNS information of a firewall rule.
     *
     * > **Description**
     * >
     * > This parameter cannot be empty when **rule.type** of [addNetFirewallRule]{@link netFirewall.addNetFirewallRule}
     * > is set to RULE_DNS.
     *
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    interface NetFirewallDnsParams {
        /**
         * Active DNS server.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        primaryDns: string;
        /**
         * Standby DNS server.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        standbyDns?: string;
    }
    /**
     * Defines a firewall rule.
     *
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    interface NetFirewallRule {
        /**
         * System user ID, which must exist.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        userId: number;
        /**
         * Rule name. This parameter is mandatory and can contain a maximum of 128 characters.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        name: string;
        /**
         * Rule direction, which can be inbound or outbound.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        direction: NetFirewallRuleDirection;
        /**
         * Action, which can be allowing or denying.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        action: FirewallRuleAction;
        /**
         * Rule type, which can be IP, Domain, or DNS.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        type: NetFirewallRuleType;
        /**
         * Whether to enable the rule. The value **true** means to enable the rule, and the value **false** means the
         * opposite.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        isEnabled: boolean;
        /**
         * ID of the firewall rule.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        id?: number;
        /**
         * Firewall rule description. This parameter is optional and can contain a maximum of 256 characters.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        description?: string;
        /**
         * Application or service UID.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        appUid?: number;
        /**
         * Local IP addresses. This parameter is valid only when **type** is set to **RULE_IP**. Otherwise, it will be
         * ignored. A maximum of 10 IP addresses can be specified.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        localIps?: Array<NetFirewallIpParams>;
        /**
         * Remote IP addresses. This parameter is valid only when **type** is set to **RULE_IP**. Otherwise, it will be
         * ignored. A maximum of 10 IP addresses can be specified.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        remoteIps?: Array<NetFirewallIpParams>;
        /**
         * Protocol, which can be TCP (value **6**) or UDP (value **17**). This parameter is valid only when **type** is set
         * to **RULE_IP**.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        protocol?: number;
        /**
         * Local ports. This parameter is valid only when **type** is set to **RULE_IP**. Otherwise, it will be ignored. A
         * maximum of 10 IP addresses can be specified.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        localPorts?: Array<NetFirewallPortParams>;
        /**
         * Remote ports. This parameter is valid only when **type** is set to **RULE_IP**. Otherwise, it will be ignored. A
         * maximum of 10 ports can be specified.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        remotePorts?: Array<NetFirewallPortParams>;
        /**
         * List of domain names. This parameter is valid only when **type** is set to **RULE_DOMAIN**. Currently, domain
         * names cannot contain Chinese characters.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        domains?: Array<NetFirewallDomainParams>;
        /**
         * List of DNS server names. This parameter is valid only when **type** is set to **RULE_DNS**. This parameter
         * cannot be empty when **type** is set to **RULE_DNS**.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        dns?: NetFirewallDnsParams;
        /**
         * Interface name: valid when type = RULE_IP, otherwise it will be ignored.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @stagemodelonly
         * @since 26.0.0
         */
        interface?: string;
    }
    /**
     * Defines query parameters.
     *
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    interface RequestParam {
        /**
         * Page number. The value range is [1,1000].
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        page: number;
        /**
         * Page size. The value range is [1,50].
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        pageSize: number;
        /**
         * Sorting method. This parameter can be used to sort firewall rules only by name.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        orderField: NetFirewallOrderField;
        /**
         * Sorting order type.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        orderType: NetFirewallOrderType;
    }
    /**
     * Defines the pagination structure for firewall rules.
     *
     * @syscap SystemCapability.Communication.NetManager.NetFirewall
     * @since 15
     */
    interface FirewallRulePage {
        /**
         * Current page number. The value range is [1,1000].
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        page: number;
        /**
         * Page size. The value range is [1,50].
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        pageSize: number;
        /**
         * Total number of pages. The value range is [1,1000].
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        totalPage: number;
        /**
         * Page data.
         *
         * @syscap SystemCapability.Communication.NetManager.NetFirewall
         * @since 15
         */
        data: Array<NetFirewallRule>;
    }
}
export default netFirewall;

```
