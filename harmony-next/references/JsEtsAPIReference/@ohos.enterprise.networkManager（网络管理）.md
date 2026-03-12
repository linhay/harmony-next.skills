# @ohos.enterprise.networkManager（网络管理）

本模块提供设备网络管理能力，包括查询设备IP地址、MAC地址信息等。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-guide)。

#### 导入模块

```ets
import { networkManager } from '@kit.MDMKit';
```

#### networkManager.getAllNetworkInterfacesSync

getAllNetworkInterfacesSync(admin: Want): Array<string>

获取所有激活的有线网络接口。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明Array<string>返回所有激活的有线网络接口名称数组。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<string> = networkManager.getAllNetworkInterfacesSync(wantTemp);
  console.info(`Succeeded in getting all network interfaces, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get all network interfaces. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.getIpAddressSync

getIpAddressSync(admin: Want, networkInterface: string): string

根据网络接口获取设备IP地址。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。networkInterfacestring是指定网络接口。

**返回值：**

类型说明string返回设备指定网络接口的IP地址。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: string = networkManager.getIpAddressSync(wantTemp, 'eth0');
  console.info(`Succeeded in getting ip address, result : ${result}`);
} catch (err) {
  console.error(`Failed to get ip address. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.getMacSync

getMacSync(admin: Want, networkInterface: string): string

根据网络接口获取设备MAC地址。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。networkInterfacestring是指定网络接口。

**返回值：**

类型说明string返回设备指定网络接口的MAC地址。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: string = networkManager.getMacSync(wantTemp, 'eth0');
  console.info(`Succeeded in getting mac, result : ${result}`);
} catch (err) {
  console.error(`Failed to get mac. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.isNetworkInterfaceDisabledSync

isNetworkInterfaceDisabledSync(admin: Want, networkInterface: string): boolean

查询指定网络接口是否被禁用。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。networkInterfacestring是指定网络接口。

**返回值：**

类型说明boolean返回指定网络接口是否被禁用，true表示该网络接口被禁用，false表示该网络接口未被禁用。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: boolean = networkManager.isNetworkInterfaceDisabledSync(wantTemp, 'eth0');
  console.info(`Succeeded in querying network interface is disabled or not, result : ${result}`);
} catch (err) {
  console.error(`Failed to query network interface is disabled or not. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.setNetworkInterfaceDisabledSync

setNetworkInterfaceDisabledSync(admin: Want, networkInterface: string, isDisabled: boolean): void

禁止设备使用指定网络接口。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。networkInterfacestring是指定网络接口。isDisabledboolean是true表示禁用该网络接口，false表示开启该网络接口。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  networkManager.setNetworkInterfaceDisabledSync(wantTemp, 'eth0', true);
  console.info(`Succeeded in setting network interface disabled`);
} catch (err) {
  console.error(`Failed to set network interface disabled. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.setGlobalProxySync

setGlobalProxySync(admin: Want, httpProxy: connection.HttpProxy): void

设置网络全局代理。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。httpProxy[connection.HttpProxy](@ohos.net.connection (网络连接管理).md#ZH-CN_TOPIC_0000002497605446__httpproxy10)是网络全局Http代理配置信息。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { connection } from '@kit.NetworkKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 需根据实际情况进行替换
let exclusionStr: string = "192.168,baidu.com";
let exclusionArray: Array<string> = exclusionStr.split(',');
let httpProxy: connection.HttpProxy = {
  host: "192.168.xx.xxx",
  port: 8080,
  exclusionList: exclusionArray
};

try {
  networkManager.setGlobalProxySync(wantTemp, httpProxy);
  console.info(`Succeeded in setting network global proxy.`);
} catch (err) {
  console.error(`Failed to set network global proxy. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.setGlobalProxyForAccount15+

setGlobalProxyForAccount(admin: Want, httpProxy: connection.HttpProxy, accountId: number): void

设置指定用户下的网络代理。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。httpProxy[connection.HttpProxy](@ohos.net.connection (网络连接管理).md#ZH-CN_TOPIC_0000002497605446__httpproxy10)是网络代理配置信息。accountIdnumber是

用户ID，取值范围：大于等于0。

accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](@ohos.account.osAccount (系统账号管理).md#ZH-CN_TOPIC_0000002529285493__getosaccountlocalid9-1)等接口来获取。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.801Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { connection } from '@kit.NetworkKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let httpProxy: connection.HttpProxy = {
  // 需根据实际情况进行替换
  host: '192.168.xx.xxx',
  port: 8080,
  exclusionList: ['192.168', 'baidu.com']
};

try {
  // 参数需根据实际情况进行替换
  networkManager.setGlobalProxyForAccount(wantTemp, httpProxy, 100);
  console.info(`Succeeded in setting network global proxy.`);
} catch (err) {
  console.error(`Failed to set network global proxy. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.getGlobalProxySync

getGlobalProxySync(admin: Want): connection.HttpProxy

获取网络全局代理。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明[connection.HttpProxy](@ohos.net.connection (网络连接管理).md#ZH-CN_TOPIC_0000002497605446__httpproxy10)返回网络全局Http代理配置信息。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { connection } from '@kit.NetworkKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: connection.HttpProxy = networkManager.getGlobalProxySync(wantTemp);
  console.info(`Succeeded in getting network global proxy, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get network global proxy. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.getGlobalProxyForAccount15+

getGlobalProxyForAccount(admin: Want | null, accountId: number): connection.HttpProxy

获取指定用户下的网络代理。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md) | null是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。accountIdnumber是

用户ID，取值范围：大于等于0。

accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](@ohos.account.osAccount (系统账号管理).md#ZH-CN_TOPIC_0000002529285493__getosaccountlocalid9-1)等接口来获取。

**返回值：**

类型说明[connection.HttpProxy](@ohos.net.connection (网络连接管理).md#ZH-CN_TOPIC_0000002497605446__httpproxy10)网络代理配置信息。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.801Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { connection } from '@kit.NetworkKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: connection.HttpProxy = networkManager.getGlobalProxyForAccount(wantTemp, 100);
  console.info(`Succeeded in getting network global proxy, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get network global proxy. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.addFirewallRule

addFirewallRule(admin: Want, firewallRule: FirewallRule): void

为设备添加防火墙过滤规则，从API version 22开始，支持IPv4和IPv6。API version 21及之前版本，仅支持IPv4。

添加了[Action](#ZH-CN_TOPIC_0000002497445612__action)为ALLOW规则后，将会默认添加DENY规则，不在ALLOW规则之内的网络数据包将会被丢弃或拦截。

设备重启，将会清空防火墙过滤规则。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。firewallRule[FirewallRule](#ZH-CN_TOPIC_0000002497445612__firewallrule)是添加防火墙过滤规则。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let firewallRule: networkManager.FirewallRule = {
  // 需根据实际情况进行替换
  "srcAddr": "192.168.1.1-192.168.22.66",
  "destAddr": "10.1.1.1",
  "srcPort": "8080",
  "destPort": "8080",
  "appUid": "9696",
  "direction": networkManager.Direction.OUTPUT,
  "action": networkManager.Action.DENY,
  "protocol": networkManager.Protocol.UDP,
  "family": 1
};

try {
  networkManager.addFirewallRule(wantTemp, firewallRule);
  console.info('Succeeded in adding firewall rule.');
} catch (err) {
  console.error(`Failed to add firewall rule. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.removeFirewallRule

removeFirewallRule(admin: Want, firewallRule?: FirewallRule): void

移除设备防火墙过滤规则，从API version 22开始，支持IPv4和IPv6。API version 21及之前版本，仅支持IPv4。

移除规则后如果不存在[Action](#ZH-CN_TOPIC_0000002497445612__action)为ALLOW规则后，会将[addFirewallRule](#ZH-CN_TOPIC_0000002497445612__networkmanageraddfirewallrule)添加的默认DENY规则清空。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。firewallRule[FirewallRule](#ZH-CN_TOPIC_0000002497445612__firewallrule)否移除防火墙过滤规则。值为空时，清空所有的防火墙规则。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let firewallRule: networkManager.FirewallRule = {
  // 需根据实际情况进行替换
  "srcAddr": "192.168.1.1-192.168.22.66",
  "destAddr": "10.1.1.1",
  "srcPort": "8080",
  "destPort": "8080",
  "appUid": "9696",
  "direction": networkManager.Direction.OUTPUT,
  "action": networkManager.Action.DENY,
  "protocol": networkManager.Protocol.UDP,
  "family": 1
};

// 移除指定的规则
try {
  networkManager.removeFirewallRule(wantTemp, firewallRule);
  console.info('Succeeded in removing firewall rule.');
} catch (err) {
  console.error(`Failed to remove firewall rule. Code: ${err.code}, message: ${err.message}`);
}

// 清空所有规则
try {
  networkManager.removeFirewallRule(wantTemp);
  console.info('Succeeded in removing all firewall rule.');
} catch (err) {
  console.error(`Failed to remove all firewall rule. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.getFirewallRules

getFirewallRules(admin: Want): Array<FirewallRule>

查询设备防火墙过滤规则，从API version 22开始，支持IPv4和IPv6。API version 21及之前版本，仅支持IPv4。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明Array<[FirewallRule](#ZH-CN_TOPIC_0000002497445612__firewallrule)>返回当前设备配置的防火墙过滤规则列表，当方法调用错误时会抛出异常。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let firewallRule: Array<networkManager.FirewallRule>;
try {
  firewallRule = networkManager.getFirewallRules(wantTemp);
  console.info('Succeeded in getting firewall rules');
} catch (err) {
  console.error(`Failed to get firewall rules. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.addDomainFilterRule

addDomainFilterRule(admin: Want, domainFilterRule: DomainFilterRule): void

为设备添加域名过滤规则，从API version 22开始，支持IPv4和IPv6。API version 21及之前版本，仅支持IPv4。

添加了[Action](#ZH-CN_TOPIC_0000002497445612__action)为ALLOW规则后，将会默认添加DENY规则，不在ALLOW规则之内的域名解析数据包将会被丢弃或拦截。

设备重启，将会清空域名过滤规则。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。domainFilterRule[DomainFilterRule](#ZH-CN_TOPIC_0000002497445612__domainfilterrule)是添加域名过滤规则。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let domainFilterRule: networkManager.DomainFilterRule = {
  // 需根据实际情况进行替换
  "domainName": "www.example.com",
  "appUid": "9696",
  "action": networkManager.Action.DENY,
  "family": 1
};

try {
  networkManager.addDomainFilterRule(wantTemp, domainFilterRule);
  console.info('Succeeded in adding domain filter rules');
} catch (err) {
  console.error(`Failed to add domain filter rules. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.removeDomainFilterRule

removeDomainFilterRule(admin: Want, domainFilterRule?: DomainFilterRule): void

移除设备域名过滤规则，从API version 22开始，支持IPv4和IPv6。API version 21及之前版本，仅支持IPv4。

移除规则后如果不存在[Action](#ZH-CN_TOPIC_0000002497445612__action)为ALLOW规则后，会将[addDomainFilterRule](#ZH-CN_TOPIC_0000002497445612__networkmanageradddomainfilterrule)添加的默认DENY规则清空。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。domainFilterRule[DomainFilterRule](#ZH-CN_TOPIC_0000002497445612__domainfilterrule)否移除域名过滤规则。值为空时，清空所有的域名规则。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let domainFilterRule: networkManager.DomainFilterRule = {
  // 需根据实际情况进行替换
  "domainName": "www.example.com",
  "appUid": "9696",
  "action": networkManager.Action.DENY,
  "family": 1
};

// 移除指定的规则
try {
  networkManager.removeDomainFilterRule(wantTemp, domainFilterRule);
  console.info('Succeeded in removing domain filter rules');
} catch (err) {
  console.error(`Failed to remove domain filter rules. Code: ${err.code}, message: ${err.message}`);
}

// 清空所有规则
try {
  networkManager.removeDomainFilterRule(wantTemp);
  console.info('Succeeded in removing all domain filter rules');
} catch (err) {
  console.error(`Failed to remove all domain filter rules. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.getDomainFilterRules

getDomainFilterRules(admin: Want): Array<DomainFilterRule>

查询设备域名过滤规则，从API version 22开始，支持IPv4和IPv6。API version 21及之前版本，仅支持IPv4。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明Array<[DomainFilterRule](#ZH-CN_TOPIC_0000002497445612__domainfilterrule)>返回当前设备配置的域名过滤规则列表，当方法调用错误时会抛出异常。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let domainFilterRule: Array<networkManager.DomainFilterRule>;
try {
  domainFilterRule = networkManager.getDomainFilterRules(wantTemp);
  console.info('Succeeded in getting  domain filter rules');
} catch (err) {
  console.error(`Failed to get domain filter rules. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.turnOnMobileData20+

turnOnMobileData(admin: Want, isForce: boolean): void

开启移动数据网络。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。isForceboolean是是否强制打开移动数据网络。true表示强制开启，强制开启后不支持用户在设备上手动关闭，必须采用[turnOffMobileData](#ZH-CN_TOPIC_0000002497445612__networkmanagerturnoffmobiledata20)接口关闭。false表示非强制开启，此时用户可以在设备上手动操作关闭移动数据网络。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  networkManager.turnOnMobileData(wantTemp, true);
  console.info(`Turn on mobile data succeeded`);
} catch (err) {
  console.error(`Failed to turn on mobile data. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.turnOffMobileData20+

turnOffMobileData(admin: Want): void

关闭移动数据网络。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  networkManager.turnOffMobileData(wantTemp);
  console.info(`Turn off mobile data succeeded`);
} catch (err) {
  console.error(`Failed to turn off mobile data. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.addApn20+

addApn(admin: Want, apnInfo: Record<string, string>): void

添加APN（Access Point Name，接入点名称）。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。apnInfoRecord<string, string>是

需要添加的APN参数信息。

- apnName：APN配置的名称标识符，必选。

- mcc：3位数字的移动国家代码，必选。

- mnc：2-3位数字的移动网络代码，必选。

- apn：接入点名称，必选。

- type：APN的服务类型，可选。

- user：APN身份验证的用户名，可选。

- password：APN身份验证的密码，可选。

- proxy：普通数据连接的代理服务器地址，可选。

- mmsproxy：彩信服务的专用代理地址，可选。

- authType：APN的认证协议类型，可选。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnInfo: Record<string, string> = {
  //需根据实际情况进行替换
  "apnName": "CTNET",
  "apn": "CTNET",
  "mnc": "11",
  "mcc": "460",
};
try {
  networkManager.addApn(wantTemp, apnInfo);
  console.info(`Succeeded in adding apn.`);
} catch (err) {
  console.error(`Failed to add apn. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.deleteApn20+

deleteApn(admin: Want, apnId: string): void

删除APN。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。apnIdstring是需要删除的APN ID。可以通过[networkManager.queryApn](#ZH-CN_TOPIC_0000002497445612__networkmanagerqueryapn20)获取设备信息。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnId: string = "1"; //需根据实际情况进行替换
try {
  networkManager.deleteApn(wantTemp, apnId);
  console.info(`Succeeded in deleting apn.`);
} catch (err) {
  console.error(`Failed to delete apn. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.updateApn20+

updateApn(admin: Want, apnInfo: Record<string, string>, apnId: string): void

更新APN。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。apnInfoRecord<string, string>是

需要更新的APN参数信息。

- apnName：APN配置的名称标识符，可选。

- mcc：3位数字的移动国家代码，可选。

- mnc：2-3位数字的移动网络代码，可选。

- APN：接入点名称，可选。

- type：APN的服务类型，可选。

- user：APN身份验证的用户名，可选。

- password：APN身份验证的密码，可选。

- proxy：普通数据连接的代理服务器地址，可选。

- mmsproxy：彩信服务的专用代理地址，可选。

- authType：APN的认证协议类型，可选。

apnIdstring是需要更新的APN ID。可以通过[networkManager.queryApn](#ZH-CN_TOPIC_0000002497445612__networkmanagerqueryapn20)获取设备信息。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnInfo: Record<string, string> = {
  //需根据实际情况进行替换
  "apnName": "CTNET",
  "apn": "CTNET",
  "mnc": "11",
  "mcc": "460",
};
let apnId: string = "1"; //需根据实际情况进行替换
try {
  networkManager.updateApn(wantTemp, apnInfo, apnId);
  console.info(`Succeeded in updating apn.`);
} catch (err) {
  console.error(`Failed to update apn. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.setPreferredApn20+

setPreferredApn(admin: Want, apnId: string): void

设置优选APN。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。apnIdstring是需要设置成优选的APN ID。可以通过[networkManager.queryApn](#ZH-CN_TOPIC_0000002497445612__networkmanagerqueryapn20)获取设备信息。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnId: string = "1"; //需根据实际情况进行替换
try {
  networkManager.setPreferredApn(wantTemp, apnId);
  console.info(`Succeeded in setting preferred apn.`);
} catch (err) {
  console.error(`Failed to set preferred apn. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.queryApn20+

queryApn(admin: Want, apnInfo: Record<string, string>): Array<string>

查询符合特定APN信息的APN ID。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。apnInfoRecord<string, string>是

APN的查询条件。

- apnName：APN配置的名称标识符，可选。

- mcc：3位数字的移动国家代码，可选。

- mnc：2-3位数字的移动网络代码，可选。

- apn：接入点名称，可选。

- type：APN的服务类型，可选。

- user：APN身份验证的用户名，可选。

- proxy：普通数据连接的代理服务器地址，可选。

- mmsproxy：彩信服务的专用代理地址，可选。

- authType：APN的认证协议类型，可选。

**返回值：**

类型说明Array<string>满足要求的APN ID。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnInfo: Record<string, string> = {
  //需根据实际情况进行替换
  "apnName": "CTNET",
  "apn": "CTNET",
  "mnc": "11",
  "mcc": "460",
};
try {
  let queryResult: Array<string> = networkManager.queryApn(wantTemp, apnInfo);
  console.info(`Succeeded in querying apn, result : ${JSON.stringify(queryResult)}`);
} catch (err) {
  console.error(`Failed to query apn. Code: ${err.code}, message: ${err.message}`);
}
```

#### networkManager.queryApn20+

queryApn(admin: Want, apnId: string): Record<string, string>

查询特定APN的APN参数信息。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。apnIdstring是指定的APN ID。可以通过[networkManager.queryApn](#ZH-CN_TOPIC_0000002497445612__networkmanagerqueryapn20)获取设备信息。

**返回值：**

类型说明Record<string, string>

指定APN ID的APN参数信息。

- apnName：APN配置的名称标识符。

- mcc：3位数字的移动国家代码。

- mnc：2-3位数字的移动网络代码。

- apn：接入点名称。

- type：APN的服务类型。

- user：APN身份验证的用户名。

- proxy：普通数据连接的代理服务器地址。

- mmsproxy：彩信服务的专用代理地址。

- authType：APN的认证协议类型。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnId: string = "1"; //需根据实际情况进行替换
try {
  let queryResult: Record<string, string> = networkManager.queryApn(wantTemp, apnId);
  console.info(`Succeeded in querying apn, result : ${JSON.stringify(queryResult)}`);
} catch (err) {
  console.error(`Failed to query apn. Code: ${err.code}, message: ${err.message}`);
}
```

#### FirewallRule

防火墙过滤规则。从API version 22开始，支持IPv4和IPv6。API version 21及之前版本，仅支持IPv4。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明srcAddrstring否是ip源地址。支持IP段，例如：192.168.0.0/22或者192.168.1.100-192.168.1.200destAddrstring否是ip目标地址。支持IP段，例如：192.168.0.0/22或者192.168.1.100-192.168.1.200srcPortstring否是源端口。destPortstring否是目标端口。appUidstring否是应用uid。direction[Direction](#ZH-CN_TOPIC_0000002497445612__direction)否是

规则链。

添加防火墙过滤规则时必填；

移除防火墙时非必填，当值为空时，表示清空所有的[Direction](#ZH-CN_TOPIC_0000002497445612__direction)链，且srcAddr，destAddr，srcPort，destPort，appUid也必须传入空值。

action[Action](#ZH-CN_TOPIC_0000002497445612__action)否是

接收或者丢弃数据包。

添加防火墙过滤规则时必填；

移除防火墙时非必填，当值为空时，表示清空所有的匹配[Action](#ZH-CN_TOPIC_0000002497445612__action)规则的链，且srcAddr，destAddr，srcPort，destPort，appUid也必须传入空值。

protocol[Protocol](#ZH-CN_TOPIC_0000002497445612__protocol)否是网络协议。当值为ALL或者ICMP时，设置srcPort与destPort无效。family22+number否是IP协议版本。支持取值为1或2，取值为1表示IPv4，取值为2表示IPv6。

#### DomainFilterRule

域名过滤规则。从API version 22开始，支持IPv4和IPv6。API version 21及之前版本，仅支持IPv4。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明domainNamestring否是域名。添加域名过滤规则时必填。支持域名分段匹配，例如，domainName传入"example.com"，那么"example.com"、"[www.example.com"、"www.test.example.com"会被匹配，"linkexample.com"不会被匹配。](http://www.example.com)appUidstring否是应用uid。action[Action](#ZH-CN_TOPIC_0000002497445612__action)否是

接收或者丢弃数据包。

添加域名过滤规则时必填；

移除域名过滤规则时非必填，当值为空时，表示清空所有的匹配[Action](#ZH-CN_TOPIC_0000002497445612__action)规则的链，且domainName，appUid也必须传入空值。

direction15+[Direction](#ZH-CN_TOPIC_0000002497445612__direction)否是

规则链。

添加域名过滤规则时非必填；当值设为输出链或输入链时，实际效果为输出链。设为转发链时，appUid需设置为空，否则会报401错误码。

移除域名过滤规则时非必填，当值为空时，表示清空所有的[Direction](#ZH-CN_TOPIC_0000002497445612__direction)链，且domainName，appUid也必须传入空值。

family22+number否是IP协议版本。支持取值为1或2，取值为1表示IPv4，取值为2表示IPv6。

#### Direction

规则链。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称值说明INPUT0输入链。OUTPUT1输出链。FORWARD15+2转发链。

#### Action

数据包的行为。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称值说明ALLOW0接收数据包。DENY1丢弃数据包。REJECT15+2拒绝数据包。

#### Protocol

网络协议。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称值说明ALL0全部网络协议。TCP1网络协议TCP。UDP2网络协议UDP。ICMP3网络协议ICMP。