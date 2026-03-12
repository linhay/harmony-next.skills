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

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明boolean返回Wi-Fi开启状态，true表示Wi-Fi开启，false表示Wi-Fi关闭。

**错误码**：

以下的错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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
  console.info(`Succeeded in querying whether the wifi is active or not, result : ${result}`);
} catch (err) {
  console.error(`Failed to query whether the wifi is active or not. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.setWifiProfileSync

setWifiProfileSync(admin: Want, profile: WifiProfile): void

为当前设备配置Wi-Fi，使连接到指定网络。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。profile[WifiProfile](#ZH-CN_TOPIC_0000002529285585__wifiprofile)是Wi-Fi配置信息。

**错误码**：

以下的错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

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
  'ssid': 'name',
  'preSharedKey': 'passwd',
  'securityType': wifiManager.WifiSecurityType.WIFI_SEC_TYPE_PSK
};

try {
  wifiManager.setWifiProfileSync(wantTemp, profile);
  console.info('Succeeded in setting wifi profile.');
} catch (err) {
  console.error(`Failed to set wifi profile. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.addAllowedWifiList19+

addAllowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void

添加Wi-Fi允许名单。添加允许名单后当前设备仅允许连接该名单下的Wi-Fi。

以下情况下，调用本接口会报策略冲突：

1. 已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了设备Wi-Fi能力。通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)解除Wi-Fi禁用后，可解除冲突。
1. 已经通过[addDisallowedWifiList](#ZH-CN_TOPIC_0000002529285585__wifimanageradddisallowedwifilist19)接口添加了Wi-Fi禁用名单。通过[removeDisallowedWifiList](#ZH-CN_TOPIC_0000002529285585__wifimanagerremovedisallowedwifilist19)移除Wi-Fi禁用名单后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。listArray<[WifiAccessInfo](#ZH-CN_TOPIC_0000002529285585__wifiaccessinfo19)>是Wi-Fi允许名单数组。数组总长度不能超过200。例如，若当前允许名单数组中已有100个Wi-Fi，则最多支持通过该接口再添加100个。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.9200010A conflict policy has been configured.201Permission verification failed. The application does not have the permission required to call the API.

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
  console.info(`Succeeded in adding allowed wifi list.`);
} catch (err) {
  console.error(`Failed to add allowed wifi list. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.removeAllowedWifiList19+

removeAllowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void

移除Wi-Fi允许名单。若移除允许名单中的部分Wi-Fi，则当前设备仅允许连接剩下未移除的Wi-Fi。若移除允许名单中的所有Wi-Fi，则当前设备可以连接任意Wi-Fi。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。listArray<[WifiAccessInfo](#ZH-CN_TOPIC_0000002529285585__wifiaccessinfo19)>是待移除的Wi-Fi允许名单数组。数组总长度不能超过200。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

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
  console.info(`Succeeded in removing allowed wifi list.`);
} catch (err) {
  console.error(`Failed to remove allowed wifi list. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.getAllowedWifiList19+

getAllowedWifiList(admin: Want): Array<WifiAccessInfo>

获取Wi-Fi允许名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明Array<[WifiAccessInfo](#ZH-CN_TOPIC_0000002529285585__wifiaccessinfo19)>Wi-Fi允许名单数组。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

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
  console.info(`Succeeded in getting allowed wifi list. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get allowed wifi list. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.addDisallowedWifiList19+

addDisallowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void

添加Wi-Fi禁用名单。添加禁用名单后当前设备不允许连接该名单下的Wi-Fi。

以下情况下，调用本接口会报策略冲突：

1. 已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了设备Wi-Fi能力。通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)解除Wi-Fi禁用后，可解除冲突。
1. 已经通过[addAllowedWifiList](#ZH-CN_TOPIC_0000002529285585__wifimanageraddallowedwifilist19)接口添加了Wi-Fi允许名单。通过[removeAllowedWifiList](#ZH-CN_TOPIC_0000002529285585__wifimanagerremoveallowedwifilist19)移除Wi-Fi允许名单后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。listArray<[WifiAccessInfo](#ZH-CN_TOPIC_0000002529285585__wifiaccessinfo19)>是Wi-Fi禁用名单数组。数组总长度不能超过200。例如，若当前禁用名单数组中已有100个Wi-Fi，则最多支持通过该接口再添加100个。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.9200010A conflict policy has been configured.201Permission verification failed. The application does not have the permission required to call the API.

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
  console.info(`Succeeded in adding disallowed wifi list.`);
} catch (err) {
  console.error(`Failed to add disallowed wifi list. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.removeDisallowedWifiList19+

removeDisallowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void

移除Wi-Fi禁用名单。若移除禁用名单中的部分Wi-Fi，则当前设备不允许连接禁用名单内剩余的Wi-Fi。若移除禁用名单中的所有Wi-Fi，则当前设备可以连接任意的Wi-Fi。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。listArray<[WifiAccessInfo](#ZH-CN_TOPIC_0000002529285585__wifiaccessinfo19)>是待移除的Wi-Fi禁用名单数组。数组总长度不能超过200。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

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
  console.info(`Succeeded in removing disallowed wifi list.`);
} catch (err) {
  console.error(`Failed to remove disallowed wifi list. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.getDisallowedWifiList19+

getDisallowedWifiList(admin: Want): Array<WifiAccessInfo>

获取Wi-Fi禁用名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明Array<[WifiAccessInfo](#ZH-CN_TOPIC_0000002529285585__wifiaccessinfo19)>Wi-Fi禁用名单数组。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

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
  console.info(`Succeeded in getting disallowed wifi list. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed wifi list. Code: ${err.code}, message: ${err.message}`);
}
```

#### WifiAccessInfo19+

Wi-Fi的SSID和BSSID信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明ssidstring否否Wi-Fi热点名称，编码格式为UTF-8，最大长度为32字节（中文字符占3位，英文字符占1位）。bssidstring否是

Wi-Fi热点的mac地址，例如：00:11:22:33:44:55。

作为[addDisallowedWifiList](#ZH-CN_TOPIC_0000002529285585__wifimanageradddisallowedwifilist19)和[removeDisallowedWifiList](#ZH-CN_TOPIC_0000002529285585__wifimanagerremovedisallowedwifilist19)接口的入参时，该属性可选，默认值为空字符串。

作为[addAllowedWifiList](#ZH-CN_TOPIC_0000002529285585__wifimanageraddallowedwifilist19)和[removeAllowedWifiList](#ZH-CN_TOPIC_0000002529285585__wifimanagerremoveallowedwifilist19)接口入参时，从API version 21开始，该属性可选，默认值为空字符串。API version 20及之前的版本，该属性必填。

#### WifiProfile

Wi-Fi配置信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明ssidstring否否热点的SSID，编码格式为UTF-8。bssidstring否是热点的BSSID。preSharedKeystring否否热点的密钥。isHiddenSsidboolean否是是否是隐藏网络。true表示是隐藏网络，false表示不是隐藏网络。securityType[WifiSecurityType](#ZH-CN_TOPIC_0000002529285585__wifisecuritytype)否否加密类型。creatorUidnumber否是创建用户的ID。disableReasonnumber否是禁用原因。netIdnumber否是分配的网络ID。randomMacTypenumber否是随机MAC类型。randomMacAddrstring否是随机MAC地址。ipType[IpType](#ZH-CN_TOPIC_0000002529285585__iptype)否是IP地址类型。staticIp[IpProfile](#ZH-CN_TOPIC_0000002529285585__ipprofile)否是静态IP配置信息。eapProfile[WifiEapProfile](#ZH-CN_TOPIC_0000002529285585__wifieapprofile)否是可扩展身份验证协议配置。

#### WifiSecurityType

表示加密类型的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称值说明WIFI_SEC_TYPE_INVALID0无效加密类型。WIFI_SEC_TYPE_OPEN1开放加密类型。WIFI_SEC_TYPE_WEP2Wired Equivalent Privacy (WEP)加密类型。WIFI_SEC_TYPE_PSK3Pre-shared key (PSK)加密类型。WIFI_SEC_TYPE_SAE4Simultaneous Authentication of Equals (SAE)加密类型。WIFI_SEC_TYPE_EAP5EAP加密类型。WIFI_SEC_TYPE_EAP_SUITE_B6Suite-B 192位加密类型。WIFI_SEC_TYPE_OWE7机会性无线加密类型。WIFI_SEC_TYPE_WAPI_CERT8WAPI-Cert加密类型。WIFI_SEC_TYPE_WAPI_PSK9WAPI-PSK加密类型。

#### IpType

表示IP类型的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称值说明STATIC0静态IP。DHCP1通过DHCP获取。UNKNOWN2未指定。

#### IpProfile

IP配置信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明ipAddressnumber否否IP地址。gatewaynumber否否网关。prefixLengthnumber否否掩码。dnsServersnumber[]否否DNS服务器。domainsArray<string>否否域信息。

#### WifiEapProfile

可扩展身份验证协议配置信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明eapMethod[EapMethod](#ZH-CN_TOPIC_0000002529285585__eapmethod)否否AP认证方式。phase2Method[Phase2Method](#ZH-CN_TOPIC_0000002529285585__phase2method)否否第二阶段认证方式。identitystring否否身份信息。anonymousIdentitystring否否匿名身份。passwordstring否否密码。caCertAliasesstring否否CA 证书别名。caPathstring否否CA 证书路径。clientCertAliasesstring否否客户端证书别名。certEntryUint8Array否否CA 证书内容。certPasswordstring否否CA证书密码。altSubjectMatchstring否否替代主题匹配。domainSuffixMatchstring否否域后缀匹配。realmstring否否通行证凭证的领域。plmnstring否否公共陆地移动网的直通凭证提供商。eapSubIdnumber否否SIM卡的子ID。

#### EapMethod

表示EAP认证方式的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称值说明EAP_NONE0不指定。EAP_PEAP1PEAP类型。EAP_TLS2TLS类型。EAP_TTLS3TTLS类型。EAP_PWD4PWD类型。EAP_SIM5SIM类型。EAP_AKA6AKA类型。EAP_AKA_PRIME7AKA Prime类型。EAP_UNAUTH_TLS8UNAUTH TLS类型。

#### Phase2Method

表示第二阶段认证方式的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称值说明PHASE2_NONE0不指定。PHASE2_PAP1PAP类型。PHASE2_MSCHAP2MSCHAP类型。PHASE2_MSCHAPV23MSCHAPV2类型。PHASE2_GTC4GTC类型。PHASE2_SIM5SIM类型。PHASE2_AKA6AKA类型。PHASE2_AKA_PRIME7AKA Prime类型。

#### wifiManager.turnOnWifi20+

turnOnWifi(admin: Want, isForce: boolean): void

打开Wi-Fi开关。

以下情况下，通过本接口打开Wi-Fi开关，会打开失败并提示"系统功能被禁用"：

​已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了Wi-Fi。需通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口启用Wi-Fi，解决"系统功能被禁用"报错。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。isForceboolean是

是否强制打开Wi-Fi功能。

true表示强制开启Wi-Fi，强制开启后不支持用户在设备上手动关闭Wi-Fi开关，必须采用[turnOffWifi](#ZH-CN_TOPIC_0000002529285585__wifimanagerturnoffwifi20)接口关闭。false表示非强制开启Wi-Fi，此时用户可以在设备上手动操作关闭Wi-Fi开关。

**错误码**：

以下的错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.203This function is prohibited by enterprise management policies.

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
  console.info(`Succeeded in turning on wifi.`);
} catch (err) {
  console.error(`Failed to turn on wifi. Code: ${err.code}, message: ${err.message}`);
}
```

#### wifiManager.turnOffWifi20+

turnOffWifi(admin: Want): void

关闭Wi-Fi开关。

以下情况下，通过本接口关闭Wi-Fi开关，会提示"系统功能被禁用"：

​已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了Wi-Fi。需通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口启用Wi-Fi，解决"系统功能被禁用"报错。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**错误码**：

以下的错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.203This function is prohibited by enterprise management policies.

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
  console.info(`Succeeded in turning off wifi.`);
} catch (err) {
  console.error(`Failed to turn off wifi. Code: ${err.code}, message: ${err.message}`);
}
```