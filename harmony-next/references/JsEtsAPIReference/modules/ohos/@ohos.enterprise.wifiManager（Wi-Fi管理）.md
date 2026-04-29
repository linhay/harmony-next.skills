# @ohos.enterprise.wifiManager（Wi-Fi管理）

本模块提供企业设备Wi-Fi管理能力，包括查询Wi-Fi开启状态等。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-guide)。

全局通用限制类策略由restrictions统一提供，若要全局禁用Wi-Fi，请参考[@ohos.enterprise.restrictions（限制类策略）](@ohos.enterprise.restrictions （限制类策略）.md)。

#### 导入模块

```ets
import { wifiManager } from '@kit.MDMKit';
```

#### wifiManager.isWifiActiveSync

isWifiActiveSync(admin: Want): boolean

查询当前设备Wi-Fi开启状态。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回Wi-Fi开启状态，true表示Wi-Fi开启，false表示Wi-Fi关闭。 |

**错误码**：

以下的错误码的详细介绍请参见[企业设备管理错误码]([企业设备管理错误码](../../errors/企业设备管理错误码.md).md)和[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

try {
  let result: boolean = wifiManager.isWifiActiveSync(wantTemp);
  console.info(`Succeeded in querying whether the Wi-Fi is active or not, result : ${result}`);
} catch (err) {
  console.error(`Failed to query whether the Wi-Fi is active or not. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.setWifiProfileSync

setWifiProfileSync(admin: Want, profile: WifiProfile): void

为当前设备配置Wi-Fi，连接到指定网络。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| profile | WifiProfile | 是 | Wi-Fi配置信息。 |

**错误码**：

以下的错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

适用于公共开发Wi-Fi

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let profile: wifiManager.WifiProfile = {
  //需根据实际情况进行替换
  'ssid': 'guest-Wi-Fi',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI_SEC_TYPE_OPEN
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(`Succeeded in setting Wi-Fi profile.`);
} catch (err) {
  console.error(`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}`);
}
```

适用于多个同名Wi-Fi但不同bssid的场景

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

let profile: wifiManager.WifiProfile = {
  // 需根据实际情况进行替换
  'ssid': 'guest-Wi-Fi',
  'bssid': 'AA:BB:CC:DD:EE:FF',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI_SEC_TYPE_OPEN
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(`Succeeded in setting Wi-Fi profile.`);
} catch (err) {
  console.error(`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}`);
}
```

适用于老旧的工业设备等场景、安全性低

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

let profile: wifiManager.WifiProfile = {
  // 需根据实际情况进行替换
  'ssid': 'Legacy-Office-Wi-Fi',
  'bssid': 'AA:BB:CC:DD:EE:FF',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI_SEC_TYPE_WEP
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(`Succeeded in setting Wi-Fi profile.`);
} catch (err) {
  console.error(`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}`);
}
```

适用于家庭网络、小型办公室、消费级路由器等场景

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

let profile: wifiManager.WifiProfile = {
  // 需根据实际情况进行替换
  'ssid': 'home_Wi-Fi',
  'preSharedKey': 'passwd',
  'securityType': wifiManager.WifiSecurityType.WIFI_SEC_TYPE_PSK
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(`Succeeded in setting Wi-Fi profile.`);
} catch (err) {
  console.error(`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}`);
}
```

适用于现代化IoT设备网络

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

let profile: wifiManager.WifiProfile = {
  // 需根据实际情况进行替换
  'ssid': 'iot_Wi-Fi',
  'preSharedKey': 'passwd',
  'securityType': wifiManager.WifiSecurityType.WIFI_SEC_TYPE_SAE
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(`Succeeded in setting Wi-Fi profile.`);
} catch (err) {
  console.error(`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}`);
}
```

适用于公司网络和大学校园网络

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

// EAP-PEAP 配置示例
let profile: wifiManager.WifiProfile = {
  // 需根据实际情况进行替换
  'ssid': 'company_Wi-Fi',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI_SEC_TYPE_EAP,
  'eapProfile': {
    eapMethod: wifiManager.EapMethod.EAP_PEAP,
    phase2Method: wifiManager.Phase2Method.PHASE2_MSCHAPV2,
    identity: 'zhangsan@company.com',
    password: 'passwd',
    anonymousIdentity: '',
    caPath: '/system/etc/security/caCerts/company-ca.pem',
    caCertAliases:  '',
    clientCertAliases: '',
    certEntry: new Uint8Array(),
    certPassword: '',
    altSubjectMatch: 'CN=radius.company.com,OU=IT Department,O=Company Inc.,C=US',
    domainSuffixMatch: 'company.com',
    realm: '',
    eapSubId: 0,
    plmn: ''
  }
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(`Succeeded in setting Wi-Fi profile.`);
} catch (err) {
  console.error(`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}`);
}
```

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

// EAP-TLS 配置示例
let profile: wifiManager.WifiProfile = {
  // 需根据实际情况进行替换
  'ssid': 'tls_Wi-Fi',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI_SEC_TYPE_EAP,
  'eapProfile': {
    eapMethod: wifiManager.EapMethod.EAP_TLS,
    phase2Method: wifiManager.Phase2Method.PHASE2_NONE,
    identity: 'zhangsan@company.com',
    password: '',
    anonymousIdentity: '',
    caPath: '/system/etc/security/caCerts/company-ca.pem',
    caCertAliases: '',
    clientCertAliases: 'zhangsan-auth-cert',
    certEntry: new Uint8Array(),
    certPassword: '',
    altSubjectMatch: 'CN=radius.company.com,OU=IT Department,O=Company Inc.,C=US',
    domainSuffixMatch: 'company.com',
    realm: '',
    eapSubId: 0,
    plmn: ''
  }
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(`Succeeded in setting Wi-Fi profile.`);
} catch (err) {
  console.error(`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}`);
}
```

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

// EAP-TTLS 配置示例
let profile: wifiManager.WifiProfile = {
  // 需根据实际情况进行替换
  'ssid': 'ttls_Wi-Fi',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI_SEC_TYPE_EAP,
  'eapProfile': {
    eapMethod: wifiManager.EapMethod.EAP_TTLS,
    phase2Method: wifiManager.Phase2Method.PHASE2_GTC,
    identity: 'zhangsan@company.com',
    password: '123456', // 根据令牌生成的动态密码
    anonymousIdentity: '',
    caPath: '',
    caCertAliases: 'company-ca',
    clientCertAliases: '',
    certEntry: new Uint8Array(),
    certPassword: '',
    altSubjectMatch: 'CN=radius.company.com,OU=IT Department,O=Company Inc.,C=US',
    domainSuffixMatch: 'company.com',
    realm: 'company.com',
    plmn: '',
    eapSubId: 0,
  }
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(`Succeeded in setting Wi-Fi profile.`);
} catch (err) {
  console.error(`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}`);
}
```

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

// EAP-SIM 配置示例
let profile: wifiManager.WifiProfile = {
  // 需根据实际情况进行替换
  'ssid': 'eap_sim_Wi-Fi',
  'preSharedKey': '',
  'securityType': wifiManager.WifiSecurityType.WIFI_SEC_TYPE_EAP,
  'eapProfile': {
    eapMethod: wifiManager.EapMethod.EAP_SIM,
    phase2Method: wifiManager.Phase2Method.PHASE2_NONE,
    identity: '',
    password:'',
    anonymousIdentity: '',
    caPath: '',
    caCertAliases:  'carrier-root-ca',
    clientCertAliases: '',
    certEntry: new Uint8Array(),
    certPassword: '',
    altSubjectMatch: 'CN=radius.company.com,OU=IT Department,O=Company Inc.,C=US',
    domainSuffixMatch: 'company.com',
    realm: 'waln.mnc000.mcc460.3gppnetwork.org',
    eapSubId: 0,
    plmn: '46000'
  }
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(`Succeeded in setting Wi-Fi profile.`);
} catch (err) {
  console.error(`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}`);
}
```

适用于需要固定IP地址供客户端访问等场景

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};

let profile: wifiManager.WifiProfile = {
  // 需根据实际情况进行替换
  'ssid': 'static_ip_Wi-Fi',
  'preSharedKey': 'passwd',
  'securityType': wifiManager.WifiSecurityType.WIFI_SEC_TYPE_PSK,
  'ipType': wifiManager.IpType.STATIC,
  'staticIp': {
    ipAddress: 3232235778, // 192.168.1.2
    gateway: 3232235777, // 192.168.1.1
    prefixLength: 24,
    dnsServers: [3232235777, 3232235777],
    domains: []
  }
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info(`Succeeded in setting Wi-Fi profile.`);
} catch (err) {
  console.error(`Failed to set Wi-Fi profile. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.addAllowedWifiList19+

addAllowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void

添加Wi-Fi允许名单。添加允许名单后当前设备仅允许连接该名单下的Wi-Fi。

以下情况下，调用本接口会报策略冲突：

1. 已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002522241688__restrictionssetdisallowedpolicy)接口禁用了设备Wi-Fi能力。通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002522241688__restrictionssetdisallowedpolicy)解除Wi-Fi禁用后，可解除冲突。

1. 已经通过[addDisallowedWifiList](#ZH-CN_TOPIC_0000002522241690__wifimanageradddisallowedwifilist19)接口添加了Wi-Fi禁用名单。通过[removeDisallowedWifiList](#ZH-CN_TOPIC_0000002522241690__wifimanagerremovedisallowedwifilist19)移除Wi-Fi禁用名单后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| list | Array<WifiAccessInfo> | 是 | Wi-Fi允许名单数组。数组总长度不能超过200。例如，若当前允许名单数组中已有100个Wi-Fi，则最多支持通过该接口再添加100个。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.edmtest',
  abilityName: 'com.example.edmtest.EnterpriseAdminAbility'
};
try {
  let wifiIds: Array<wifiManager.WifiAccessInfo> = [{
    //需根据实际情况进行替换
    ssid: "wifi_name",
    bssid: "68:77:24:77:A6:D8"
  }];
  wifiManager.addAllowedWifiList(wantTemp, wifiIds);
  console.info(`Succeeded in adding allowed Wi-Fi list.`);
} catch (err) {
  console.error(`Failed to add allowed Wi-Fi list. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.removeAllowedWifiList19+

removeAllowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void

移除Wi-Fi允许名单。若移除允许名单中的部分Wi-Fi，则当前设备仅允许连接剩下未移除的Wi-Fi。若移除允许名单中的所有Wi-Fi，则当前设备可以连接任意Wi-Fi。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| list | Array<WifiAccessInfo> | 是 | 待移除的Wi-Fi允许名单数组。数组总长度不能超过200。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let wifiIds: Array<wifiManager.WifiAccessInfo> = [{
    //需根据实际情况进行替换
    ssid: "wifi_name",
    bssid: "68:77:24:77:A6:D8"
  }];
  wifiManager.removeAllowedWifiList(wantTemp, wifiIds);
  console.info(`Succeeded in removing allowed Wi-Fi list.`);
} catch (err) {
  console.error(`Failed to remove allowed Wi-Fi list. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.getAllowedWifiList19+

getAllowedWifiList(admin: Want): Array<WifiAccessInfo>

获取Wi-Fi允许名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<WifiAccessInfo> | Wi-Fi允许名单数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: Array<wifiManager.WifiAccessInfo> = wifiManager.getAllowedWifiList(wantTemp);
  console.info(`Succeeded in getting allowed Wi-Fi list. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get allowed Wi-Fi list. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.addDisallowedWifiList19+

addDisallowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void

添加Wi-Fi禁用名单。添加禁用名单后当前设备不允许连接该名单下的Wi-Fi。

以下情况下，调用本接口会报策略冲突：

1. 已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002522241688__restrictionssetdisallowedpolicy)接口禁用了设备Wi-Fi能力。通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002522241688__restrictionssetdisallowedpolicy)解除Wi-Fi禁用后，可解除冲突。

1. 已经通过[addAllowedWifiList](#ZH-CN_TOPIC_0000002522241690__wifimanageraddallowedwifilist19)接口添加了Wi-Fi允许名单。通过[removeAllowedWifiList](#ZH-CN_TOPIC_0000002522241690__wifimanagerremoveallowedwifilist19)移除Wi-Fi允许名单后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| list | Array<WifiAccessInfo> | 是 | Wi-Fi禁用名单数组。数组总长度不能超过200。例如，若当前禁用名单数组中已有100个Wi-Fi，则最多支持通过该接口再添加100个。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let wifiIds: Array<wifiManager.WifiAccessInfo> = [{
    //需根据实际情况进行替换
    ssid: "wifi_name",
    bssid: "68:77:24:77:A6:D8"
  }];
  wifiManager.addDisallowedWifiList(wantTemp, wifiIds);
  console.info(`Succeeded in adding disallowed Wi-Fi list.`);
} catch (err) {
  console.error(`Failed to add disallowed Wi-Fi list. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.removeDisallowedWifiList19+

removeDisallowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void

移除Wi-Fi禁用名单。若移除禁用名单中的部分Wi-Fi，则当前设备不允许连接禁用名单内剩余的Wi-Fi。若移除禁用名单中的所有Wi-Fi，则当前设备可以连接任意的Wi-Fi。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| list | Array<WifiAccessInfo> | 是 | 待移除的Wi-Fi禁用名单数组。数组总长度不能超过200。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let wifiIds: Array<wifiManager.WifiAccessInfo> = [{
    //需根据实际情况进行替换
    ssid: "wifi_name",
    bssid: "68:77:24:77:A6:D8"
  }];
  wifiManager.removeDisallowedWifiList(wantTemp, wifiIds);
  console.info(`Succeeded in removing disallowed Wi-Fi list.`);
} catch (err) {
  console.error(`Failed to remove disallowed Wi-Fi list. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.getDisallowedWifiList19+

getDisallowedWifiList(admin: Want): Array<WifiAccessInfo>

获取Wi-Fi禁用名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<WifiAccessInfo> | Wi-Fi禁用名单数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: Array<wifiManager.WifiAccessInfo> = wifiManager.getDisallowedWifiList(wantTemp);
  console.info(`Succeeded in getting disallowed Wi-Fi list. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed Wi-Fi list. Code: ${err.code}, message: ${err.message}`);
}
```

#### WifiAccessInfo19+

Wi-Fi的SSID和BSSID信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ssid | string | 否 | 否 | Wi-Fi热点名称，编码格式为UTF-8，最大长度为32字节（中文字符占3位，英文字符占1位）。 |
| bssid | string | 否 | 是 | Wi-Fi热点的mac地址，例如：00:11:22:33:44:55。 作为addDisallowedWifiList和removeDisallowedWifiList接口的入参时，该属性可选，默认值为空字符串。 作为addAllowedWifiList和removeAllowedWifiList接口入参时，从API version 21开始，该属性可选，默认值为空字符串。API version 20及之前的版本，该属性必填。 |

#### WifiProfile

Wi-Fi配置信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ssid | string | 否 | 否 | Wi-Fi热点名称，编码格式为UTF-8。 |
| bssid | string | 否 | 是 | Wi-Fi热点的MAC地址。 |
| preSharedKey | string | 否 | 否 | 预共享密钥。 |
| isHiddenSsid | boolean | 否 | 是 | 是否是隐藏网络。true表示是隐藏网络，false表示不是隐藏网络。 |
| securityType | WifiSecurityType | 否 | 否 | 安全类型。 |
| creatorUid | number | 否 | 是 | 创建用户的ID。 |
| disableReason | number | 否 | 是 | 禁用原因。 |
| netId | number | 否 | 是 | 分配的网络ID。 |
| randomMacType | number | 否 | 是 | 随机MAC类型。0-随机MAC地址， 1-设备MAC地址。 |
| randomMacAddr | string | 否 | 是 | MAC地址。randomMacType为设备mac类型时，该字段必填。 |
| ipType | IpType | 否 | 是 | IP地址类型。 |
| staticIp | IpProfile | 否 | 是 | 静态IP配置信息。ipType为STATIC时，该字段必填。 |
| eapProfile | WifiEapProfile | 否 | 是 | 可扩展身份验证协议配置。只有securityType为WIFI_SEC_TYPE_EAP时必填。 |

#### WifiSecurityType

表示加密类型的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WIFI_SEC_TYPE_INVALID | 0 | 无效加密类型。例如机场公共Wi-Fi。 |
| WIFI_SEC_TYPE_OPEN | 1 | 开放加密类型。 |
| WIFI_SEC_TYPE_WEP | 2 | Wired Equivalent Privacy (WEP)加密类型。 |
| WIFI_SEC_TYPE_PSK | 3 | Pre-shared key (PSK)加密类型。 例如家庭、小型办公室Wi-Fi。 |
| WIFI_SEC_TYPE_SAE | 4 | Simultaneous Authentication of Equals (SAE)加密类型。例如智能家居、中小型企业网络。 |
| WIFI_SEC_TYPE_EAP | 5 | EAP加密类型。例如大型企业认证、大学校园网络等。 |
| WIFI_SEC_TYPE_EAP_SUITE_B | 6 | Suite-B 192位加密类型。例如政府和高安全机构。 |
| WIFI_SEC_TYPE_OWE | 7 | 机会性无线加密类型。例如咖啡馆的公共Wi-Fi，无需密码为连接提供加密。 |
| WIFI_SEC_TYPE_WAPI_CERT | 8 | WAPI-Cert加密类型。中国自主的无线安全标准。 |
| WIFI_SEC_TYPE_WAPI_PSK | 9 | WAPI-PSK加密类型。 |

#### IpType

表示IP类型的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATIC | 0 | 静态IP，一般用于需要固定IP的场景、例如办公室打印机，固定打印机IP地址，便于大家稳定地添加和使用。 |
| DHCP | 1 | 动态主机配置协议，一种能自动为网络中的设备分配IP地址和其他网络配置信息的服务。 |
| UNKNOWN | 2 | 未指定。 |

#### IpProfile

IP配置信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ipAddress | number | 否 | 否 | IP地址，十进制表示，正常点分十进制写法为192.168.1.1，对应的十进制为3232235777。 |
| gateway | number | 否 | 否 | 默认网关，十进制表示，通常是路由器的IP地址。 |
| prefixLength | number | 否 | 否 | 子网掩码。 |
| dnsServers | number[] | 否 | 否 | DNS服务器，数组内最多包含首选DNS服务器和备用DNS服务器两个地址。 |
| domains | Array<string> | 否 | 否 | 域信息。 |

#### WifiEapProfile

可扩展身份验证协议配置信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eapMethod | EapMethod | 否 | 否 | AP认证方式。 |
| phase2Method | Phase2Method | 否 | 否 | 第二阶段认证方式。只有eapMethod为EAP_PEAP或EAP_TTLS时需要填写。 |
| identity | string | 否 | 否 | 身份信息。当eapMethod为TLS时，该字段不能为空。 |
| anonymousIdentity | string | 否 | 否 | 匿名身份。 |
| password | string | 否 | 否 | 密码。当eapMethod为EAP_PEAP或EAP_PWD时，该字段不能为空串，最大长度为128字节。 |
| caCertAliases | string | 否 | 否 | CA 证书别名。 |
| caPath | string | 否 | 否 | CA 证书路径。 |
| clientCertAliases | string | 否 | 否 | 客户端证书别名。当客户端证书内容为空时，客户端证书需先调用证书管理接口安装后传入别名。 |
| certEntry | Uint8Array | 否 | 否 | 客户端证书内容。当eapMethod为EAP_TLS时，如果该字段为空，则客户端证书别名不能为空。 |
| certPassword | string | 否 | 否 | CA证书密码。 |
| altSubjectMatch | string | 否 | 否 | 替代主题匹配。证书验证中，除了检查证书主域名，还检查证书的主题备用名称是否匹配。 |
| domainSuffixMatch | string | 否 | 否 | 域后缀匹配。 |
| realm | string | 否 | 否 | 通行证凭证的领域。 |
| plmn | string | 否 | 否 | 凭证提供商。 |
| eapSubId | number | 否 | 否 | SIM卡的子ID。 |

#### EapMethod

表示EAP认证方式的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EAP_NONE | 0 | 不指定。 |
| EAP_PEAP | 1 | PEAP类型，受保护的可扩展认证协议。先建立安全的TLS隧道、然后进行简单认证。 |
| EAP_TLS | 2 | TLS类型，传输层安全协议。双向证书认证。 |
| EAP_TTLS | 3 | TTLS类型，隧道传输层安全协议。与PEAP类似，但后续隧道内部认证方法更加丰富。 |
| EAP_PWD | 4 | PWD类型，密码认证。无需服务器证书。 |
| EAP_SIM | 5 | SIM类型，使用手机SIM卡中的密钥和算法进行认证。 |
| EAP_AKA | 6 | AKA类型，使用USIM卡（3G/4G/5G SIM卡）中的增强密钥和算法进行认证。 |
| EAP_AKA_PRIME | 7 | AKA Prime类型，EAP-AKA增强版，在密钥派生中绑定网络名称。 |
| EAP_UNAUTH_TLS | 8 | UNAUTH TLS类型，单向认证（仅认证客户端）和加密通道。 |

#### Phase2Method

表示第二阶段认证方式的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PHASE2_NONE | 0 | 不指定。 |
| PHASE2_PAP | 1 | PAP类型。 |
| PHASE2_MSCHAP | 2 | MSCHAP类型。 |
| PHASE2_MSCHAPV2 | 3 | MSCHAPV2类型。 |
| PHASE2_GTC | 4 | GTC类型。 |
| PHASE2_SIM | 5 | SIM类型。 |
| PHASE2_AKA | 6 | AKA类型。 |
| PHASE2_AKA_PRIME | 7 | AKA Prime类型。 |

#### wifiManager.turnOnWifi20+

turnOnWifi(admin: Want, isForce: boolean): void

打开Wi-Fi开关。

以下情况下，通过本接口打开Wi-Fi开关，会打开失败并提示"系统功能被禁用"：

​已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002522241688__restrictionssetdisallowedpolicy)接口禁用了Wi-Fi。需通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002522241688__restrictionssetdisallowedpolicy)接口启用Wi-Fi，解决"系统功能被禁用"报错。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

冲突规则： 任意MDM应用​通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002522241688__restrictionssetdisallowedpolicy)接口禁用了Wi-Fi，则无法通过本接口直接打开Wi-Fi开关。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| isForce | boolean | 是 | 是否强制打开Wi-Fi功能。 true表示强制开启Wi-Fi，强制开启后不支持用户在设备上手动关闭Wi-Fi开关，必须采用turnOffWifi接口关闭。false表示非强制开启Wi-Fi，此时用户可以在设备上手动操作关闭Wi-Fi开关。 |

**错误码**：

以下的错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 203 | This function is prohibited by enterprise management policies. |

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { wifiManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  wifiManager.turnOnWifi(wantTemp, true);
  console.info(`Succeeded in turning on Wi-Fi.`);
} catch (err) {
  console.error(`Failed to turn on Wi-Fi. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.turnOffWifi20+

turnOffWifi(admin: Want): void

关闭Wi-Fi开关。

以下情况下，通过本接口关闭Wi-Fi开关，会提示"系统功能被禁用"：

​已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002522241688__restrictionssetdisallowedpolicy)接口禁用了Wi-Fi。需通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002522241688__restrictionssetdisallowedpolicy)接口启用Wi-Fi，解决"系统功能被禁用"报错。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

冲突规则： 任意MDM应用通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002522241688__restrictionssetdisallowedpolicy)接口禁用了Wi-Fi，则无法通过本接口直接关闭Wi-Fi开关。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**错误码**：

以下的错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 203 | This function is prohibited by enterprise management policies. |

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { wifiManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  wifiManager.turnOffWifi(wantTemp);
  console.info(`Succeeded in turning off Wi-Fi.`);
} catch (err) {
  console.error(`Failed to turn off Wi-Fi. Code: ${err.code}, message: ${err.message}`);
}
```