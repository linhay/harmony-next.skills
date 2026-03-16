# @ohos.net.netFirewall (网络防火墙)

本模块为应用程序提供网络防火墙能力。应用程序可以对机器进行防火墙拦截记录的查询。

本模块首批接口从API version 15开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { netFirewall } from '@kit.NetworkKit';
```

#### netFirewall.getNetFirewallPolicy

getNetFirewallPolicy(userId: number): Promise<NetFirewallPolicy>

查询防火墙状态。使用Promise异步回调。

**需要权限**：ohos.permission.GET_NET_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

参数名类型必填说明userIdnumber是系统中的多用户用户ID，只能是存在的用户ID。

**返回值：**

类型说明Promise<[NetFirewallPolicy](#ZH-CN_TOPIC_0000002529445417__netfirewallpolicy)>以Promise形式返回当前用户防火墙策略。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[网络连接管理错误码](../../errors/网络连接管理错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error.2100001Invalid parameter value.2100002Operation failed. Cannot connect to service.2100003System internal error.29400000The specified user does not exist.

**示例：**

```ets
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

netFirewall.getNetFirewallPolicy(100).then((result: netFirewall.NetFirewallPolicy) => {
  console.info('firewall policy: ', JSON.stringify(result));
}, (reason: BusinessError) => {
  console.error('get firewall policy failed: ', JSON.stringify(reason));
});
```

#### netFirewall.updateNetFirewallRule

updateNetFirewallRule(rule: NetFirewallRule): Promise<void>

更新防火墙规则。使用Promise异步回调。

**需要权限**：ohos.permission.MANAGE_NET_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

参数名类型必填说明rule[NetFirewallRule](#ZH-CN_TOPIC_0000002529445417__netfirewallrule)是防火墙规则。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[网络连接管理错误码](../../errors/网络连接管理错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error.2100001Invalid parameter value.2100002Operation failed. Cannot connect to service.2100003System internal error.29400000The specified user does not exist.29400002The number of IP address rules in the firewall rule exceeds the maximum.29400003The number of port rules in the firewall rule exceeds the maximum.29400004The number of domain rules in the firewall rule exceeds the maximum.29400005The number of domain rules exceeds the maximum.29400006The specified rule does not exist.29400007The dns rule is duplication.

**示例：**

```ets
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ipRuleUpd: netFirewall.NetFirewallRule = {
  id: 1,
  name: "rule1",
  description: "rule1 description update",
  direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
  action:netFirewall.FirewallRuleAction.RULE_DENY,
  type: netFirewall.NetFirewallRuleType.RULE_IP,
  isEnabled: false,
  appUid: 20001,
  localIps: [
    {
      family: 1,
      type: 1,
      address: "10.10.1.1",
      mask: 24
    },{
      family: 1,
      type: 2,
      startIp: "10.20.1.1",
      endIp: "10.20.1.10"
    }],
  userId: 100
};
netFirewall.updateNetFirewallRule(ipRuleUpd).then(() => {
  console.info('update firewall rule success.');
}, (reason: BusinessError) => {
  console.error('update firewall rule failed: ', JSON.stringify(reason));
});
```

#### netFirewall.removeNetFirewallRule

removeNetFirewallRule(userId: number, ruleId: number): Promise<void>

删除防火墙规则。使用Promise异步回调。

**需要权限**：ohos.permission.MANAGE_NET_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

参数名类型必填说明userIdnumber是系统中的多用户用户ID，只能是存在的用户ID。ruleIdnumber是防火墙规则ID。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[网络连接管理错误码](../../errors/网络连接管理错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error.2100001Invalid parameter value.2100002Operation failed. Cannot connect to service.2100003System internal error.29400000The specified user does not exist.29400006The specified rule does not exist.

**示例：**

```ets
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

netFirewall.removeNetFirewallRule(100, 1).then(() => {
  console.info("delete firewall rule success.");
}).catch((error : BusinessError) => {
  console.error("delete firewall rule failed: " + JSON.stringify(error));
});
```

#### netFirewall.getNetFirewallRules

getNetFirewallRules(userId: number, requestParam: RequestParam): Promise<FirewallRulePage>

按userId获取防火墙规则，需要指定分页查询参数。使用Promise异步回调。

**需要权限**：ohos.permission.GET_NET_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

参数名类型必填说明userIdnumber是系统中的多用户用户ID，只能是存在的用户ID。requestParam[RequestParam](#ZH-CN_TOPIC_0000002529445417__requestparam)是分页查询参数，其中orderField字段仅支持根据防火墙规则名排序。

**返回值：**

类型说明Promise<[FirewallRulePage](#ZH-CN_TOPIC_0000002529445417__firewallrulepage)>以Promise形式返回防火墙分页规则列表。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[网络连接管理错误码](../../errors/网络连接管理错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error.2100001Invalid parameter value.2100002Operation failed. Cannot connect to service.2100003System internal error.29400000The specified user does not exist.

**示例：**

```ets
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ruleParam: netFirewall.RequestParam = {
  page: 1,
  pageSize: 10,
  orderField: netFirewall.NetFirewallOrderField.ORDER_BY_RULE_NAME,
  orderType: netFirewall.NetFirewallOrderType.ORDER_ASC
};
netFirewall.getNetFirewallRules(100, ruleParam).then((result: netFirewall.FirewallRulePage) => {
  console.info("result:", JSON.stringify(result));
}, (error: BusinessError) => {
  console.error("get firewall rules failed: " + JSON.stringify(error));
});
```

#### netFirewall.getNetFirewallRule

getNetFirewallRule(userId: number, ruleId: number): Promise<NetFirewallRule>

通过userId和ruleId获取指定的防火墙规则。使用Promise异步回调。

**需要权限**：ohos.permission.GET_NET_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

参数名类型必填说明userIdnumber是系统中的多用户用户ID，只能是存在的用户ID。ruleIdnumber是防火墙规则ID。

**返回值：**

类型说明Promise<[NetFirewallRule](#ZH-CN_TOPIC_0000002529445417__netfirewallrule)>以Promise形式返回防火墙规则。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[网络连接管理错误码](../../errors/网络连接管理错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error.2100001Invalid parameter value.2100002Operation failed. Cannot connect to service.2100003System internal error.29400000The specified user does not exist.29400006The specified rule does not exist.

**示例：**

```ets
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

netFirewall.getNetFirewallRule(100, 1).then((rule: netFirewall.NetFirewallRule) => {
  console.info("result:", JSON.stringify(rule));
}).catch((error : BusinessError) => {
  console.error(" get firewall rules failed: " + JSON.stringify(error));
});
```

#### netFirewall.setNetFirewallPolicy

setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>

设置防火墙状态。使用Promise异步回调。

**需要权限**：ohos.permission.MANAGE_NET_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

参数名类型必填说明userIdnumber是系统中的多用户用户ID，只能是存在的用户ID。policy[NetFirewallPolicy](#ZH-CN_TOPIC_0000002529445417__netfirewallpolicy)是设置的防火墙策略。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[网络连接管理错误码](../../errors/网络连接管理错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error.2100001Invalid parameter value.2100002Operation failed. Cannot connect to service.2100003System internal error.29400000The specified user does not exist.

**示例：**

```ets
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let policy: netFirewall.NetFirewallPolicy = {
  isOpen: true,
  inAction: netFirewall.FirewallRuleAction.RULE_DENY,
  outAction: netFirewall.FirewallRuleAction.RULE_ALLOW
};
netFirewall.setNetFirewallPolicy(100, policy).then(() => {
  console.info("set firewall policy success.");
}).catch((error : BusinessError) => {
  console.error("set firewall policy failed: " + JSON.stringify(error));
});
```

#### netFirewall.addNetFirewallRule

addNetFirewallRule(rule: NetFirewallRule): Promise<number>

添加防火墙规则。使用Promise异步回调。

1.

防火墙规则优先级说明（[setNetFirePolicy](#ZH-CN_TOPIC_0000002529445417__netfirewallsetnetfirewallpolicy)和[addNetFirewallRule](#ZH-CN_TOPIC_0000002529445417__netfirewalladdnetfirewallrule)无调用顺序要求）：

（1）调用[setNetFirePolicy](#ZH-CN_TOPIC_0000002529445417__netfirewallsetnetfirewallpolicy)设置默认策略为阻止，调用[addNetFirewallRule](#ZH-CN_TOPIC_0000002529445417__netfirewalladdnetfirewallrule)新增显式规则，规则优先级由高到低为：

 ◦ 显式阻止规则

 ◦ 显式允许规则

 ◦ 默认阻止策略

（2）调用[setNetFirePolicy](#ZH-CN_TOPIC_0000002529445417__netfirewallsetnetfirewallpolicy)设置默认策略为允许，调用[addNetFirewallRule](#ZH-CN_TOPIC_0000002529445417__netfirewalladdnetfirewallrule)新增显式规则，规则优先级由高到低为：

 ◦ 显式允许规则

 ◦ 显式阻止规则

 ◦ 默认允许策略

1.

规则类型补充说明：

（1）当addNetFirewallRule的入参rule.type配置为RULE_IP时：

 ◦ 若rule.action为RULE_ALLOW，且rule.localIps、rule.remoteIps均不配置，规则生效为全IP段允许通行；

 ◦ 若rule.action 为RULE_DENY，且rule.localIps、rule.remoteIps均不配置，规则生效为全IP段拦截。

（2）当adNetFirewallRule的入参rule.type配置为RULE_DOMAIN时，若rule.domains未配置， 该规则不生效。

**需要权限**：ohos.permission.MANAGE_NET_FIREWALL

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

**参数：**

参数名类型必填说明rule[NetFirewallRule](#ZH-CN_TOPIC_0000002529445417__netfirewallrule)是防火墙规则。

**返回值：**

类型说明Promise<number>以Promise形式返回防火墙规则ID，防火墙规则ID由系统自动生成。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[网络连接管理错误码](../../errors/网络连接管理错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error.2100001Invalid parameter value.2100002Operation failed. Cannot connect to service.2100003System internal error.29400000The specified user does not exist.29400001The number of firewall rules exceeds the maximum.29400002The number of IP address rules in the firewall rule exceeds the maximum.29400003The number of port rules in the firewall rule exceeds the maximum.29400004The number of domain rules in the firewall rule exceeds the maximum.29400005The number of domain rules exceeds the maximum.29400007The dns rule is duplication.

**示例：**

```ets
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ipRule: netFirewall.NetFirewallRule = {
  name: "rule1",
  description: "rule1 description",
  direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
  action:netFirewall.FirewallRuleAction.RULE_DENY,
  type: netFirewall.NetFirewallRuleType.RULE_IP,
  isEnabled: true,
  appUid: 20001,
  localIps: [
    {
      family: 1,
      type: 1,
      address: "10.10.1.1",
      mask: 24
    },{
      family: 1,
      type: 2,
      startIp: "10.20.1.1",
      endIp: "10.20.1.10"
    }],
  remoteIps:[
    {
      family: 1,
      type: 1,
      address: "20.10.1.1",
      mask: 24
    },{
      family: 1,
      type: 2,
      startIp: "20.20.1.1",
      endIp: "20.20.1.10"
    }],
  protocol: 6,
  localPorts: [
    {
      startPort: 1000,
      endPort: 1000
    },{
      startPort: 2000,
      endPort: 2001
    }],
  remotePorts: [
    {
      startPort: 443,
      endPort: 443
    }],
  userId: 100
};
netFirewall.addNetFirewallRule(ipRule).then((result: number) => {
  console.info('rule Id: ', result);
}, (reason: BusinessError) => {
  console.error('add firewall rule failed: ', JSON.stringify(reason));
});

let domainRule: netFirewall.NetFirewallRule = {
  name: "rule2",
  description: "rule2 description",
  direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
  action:netFirewall.FirewallRuleAction.RULE_DENY,
  type: netFirewall.NetFirewallRuleType.RULE_DOMAIN,
  isEnabled: true,
  appUid: 20002,
  domains: [
    {
      isWildcard: false,
      domain: "www.example.cn"
    },{
      isWildcard: true,
      domain: "*.example.cn"
    }],
  userId: 100
};
netFirewall.addNetFirewallRule(domainRule).then((result: number) => {
  console.info('rule Id: ', result);
}, (reason: BusinessError) => {
  console.error('add firewall rule failed: ', JSON.stringify(reason));
});

let dnsRule: netFirewall.NetFirewallRule = {
  name: "rule3",
  description: "rule3 description",
  direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
  action:netFirewall.FirewallRuleAction.RULE_DENY,
  type: netFirewall.NetFirewallRuleType.RULE_DNS,
  isEnabled: true,
  appUid: 20003,
  dns:{
   primaryDns: "4.4.4.4",
   standbyDns: "8.8.8.8",
  },
  userId: 100
};
netFirewall.addNetFirewallRule(dnsRule).then((result: number) => {
  console.info('rule Id: ', result);
}, (reason: BusinessError) => {
  console.error('add firewall rule failed: ', JSON.stringify(reason));
});
```

#### NetFirewallRule

防火墙规则信息结构。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

名称类型只读可选说明userIdnumber否否系统中的多用户用户ID，只能是存在的用户ID。namestring否否规则名称，必填，最多128个字符。direction[NetFirewallRuleDirection](#ZH-CN_TOPIC_0000002529445417__netfirewallruledirection)否否规则方向，入站或出站。action[FirewallRuleAction](#ZH-CN_TOPIC_0000002529445417__firewallruleaction)否否行为。type[NetFirewallRuleType](#ZH-CN_TOPIC_0000002529445417__netfirewallruletype)否否规则类型。isEnabledboolean否否是否启用规则。true表示启用，false表示不启用。idnumber否是规则ID。descriptionstring否是规则描述，可选，最多256个字符。appUidnumber否是应用程序或服务UID。localIpsArray<[NetFirewallIpParams](#ZH-CN_TOPIC_0000002529445417__netfirewallipparams)>否是本地IP地址：ruleType=RULE_IP有效，否则忽略，最多10个。remoteIpsArray<[NetFirewallIpParams](#ZH-CN_TOPIC_0000002529445417__netfirewallipparams)>否是远端IP地址：当ruleType=RULE_IP时有效，否则将被忽略，最多10个。protocolnumber否是协议，TCP：6，UDP：17，当ruleType=RULE_IP时有效，否则将被忽略。localPortsArray<[NetFirewallPortParams](#ZH-CN_TOPIC_0000002529445417__netfirewallportparams)>否是本地端口：当ruleType=RULE_IP时有效，否则将被忽略，最多10个。remotePortsArray<[NetFirewallPortParams](#ZH-CN_TOPIC_0000002529445417__netfirewallportparams)>否是远端端口：当ruleType=RULE_IP时有效，否则将被忽略，最多10个。domainsArray<[NetFirewallDomainParams](#ZH-CN_TOPIC_0000002529445417__netfirewalldomainparams)>否是域名列表：当ruleType=RULE_DOMAIN时有效，否则将被忽略。dns[NetFirewallDnsParams](#ZH-CN_TOPIC_0000002529445417__netfirewalldnsparams)否是DNS：当ruleType=RULE_DNS时有效，否则将被忽略。

#### RequestParam

查询输入信息结构。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

名称类型只读可选说明pagenumber否否页码，值范围：[1, 1000]。pageSizenumber否否页面大小，值范围：[1, 50]。orderField[NetFirewallOrderField](#ZH-CN_TOPIC_0000002529445417__netfirewallorderfield)否否排序字段。orderType[NetFirewallOrderType](#ZH-CN_TOPIC_0000002529445417__netfirewallordertype)否否排序顺序。

#### FirewallRulePage

防火墙规则页信息结构。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

名称类型只读可选说明pagenumber否否当前页码，值范围：[1,1000]。pageSizenumber否否页大小，值范围：[1,50]。totalPagenumber否否总页数，值范围：[1,1000]。dataArray<[NetFirewallRule](#ZH-CN_TOPIC_0000002529445417__netfirewallrule)>否否页面数据。

#### NetFirewallPolicy

防火墙状态。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

名称类型只读可选说明isOpenboolean否否是否开启防火墙。true表示开启防火墙，false表示关闭防火墙。inAction[FirewallRuleAction](#ZH-CN_TOPIC_0000002529445417__firewallruleaction)否否入站行动。outAction[FirewallRuleAction](#ZH-CN_TOPIC_0000002529445417__firewallruleaction)否否出站行动。

#### NetFirewallRuleDirection

枚举，防火墙规则的拦截方向。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

名称值说明RULE_IN1入站。RULE_OUT2出站。

#### FirewallRuleAction

枚举，防火墙规则行为，允许网络连接或阻断连接。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

名称值说明RULE_ALLOW0允许。RULE_DENY1阻断。

#### NetFirewallRuleType

枚举，防火墙规则类型。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

名称值说明RULE_IP1IP类规则。RULE_DOMAIN2域名类规则。RULE_DNS3DNS规则。

#### NetFirewallOrderField

枚举，防火墙规则排序类型。

[getNetFirewallRules](#ZH-CN_TOPIC_0000002529445417__netfirewallgetnetfirewallrules)接口，仅支持ORDER_BY_RULE_NAME字段。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

名称值说明ORDER_BY_RULE_NAME1根据防火墙规则名排序。ORDER_BY_RECORD_TIME100根据记录时间排序。

#### NetFirewallOrderType

枚举，防火墙规则排序类型，按名称或时间顺序排序。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

名称值说明ORDER_ASC1按防火墙规则排序类型升序排序。ORDER_DESC100按防火墙规则排序类型降序排序。

#### NetFirewallIpParams

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

名称类型只读可选说明typenumber否否

1：IP地址或子网，当使用单个IP时，掩码为32。

2：IP段。

familynumber否是

1：表示family设置为IPv4。

2：表示family设置为IPv6。

默认IPv4，其他当前不支持。

addressstring否是IP地址。当type等于1时需要设置，并且仅在type等于1时有效，否则将被忽略。masknumber否是

IPv4：子网掩码。

IPv6：前缀。

当type等于1时需要设置，并且仅在type等于1时有效，否则将被忽略。

startIpstring否是起始IP。当type等于2时需要设置，并且仅在type等于2时有效，范围从0.0.0.1到255.255.255.254，否则将被忽略。endIpstring否是结束IP。当type等于2时需要设置，并且仅在type等于2时有效，范围从0.0.0.1到255.255.255.254，否则将被忽略。

#### NetFirewallPortParams

防火墙规则端口参数。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

名称类型只读可选说明startPortnumber否否开始端口。endPortnumber否否结束端口。

#### NetFirewallDomainParams

防火墙规则域信息。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

名称类型只读可选说明isWildcardboolean否否是否包含通配符。true表示包含，false表示不包含。domainstring否否当isWildcard为false时，需要确定的完整域。

#### NetFirewallDnsParams

防火墙规则DNS信息。

**系统能力**：SystemCapability.Communication.NetManager.NetFirewall

名称类型只读可选说明primaryDnsstring否否主域名服务器。standbyDnsstring否是备份DNS。