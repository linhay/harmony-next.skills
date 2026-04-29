# @ohos.net.eap (扩展认证)

该模块提供了第三方客户端接入802.1X认证（一种基于端口的网络接入控制协议）流程的机制，支撑客户端的定制认证等功能。

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import {eap} from '@kit.NetworkKit';
```

#### eap.regCustomEapHandler

regCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback<EapData>): void

用于指定需要定制化处理的EAP报文类型和对应的处理callback。使用callback异步回调。

系统会将符合条件的EAP报文送入callback函数中供企业应用获取。

**需要权限**：ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

**系统能力**：SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netType | number | 是 | 网络类型，取值为1或2。 netType=1表示WLAN，netType=2表示以太网。 |
| eapCode | number | 是 | 需要进行定制的EAP code，取值为1、2、3、4 。 code=1 Request、 code=2 Response、 code=3 Success、 code=4 Failure。 |
| eapType | number | 是 | 需要进行定制处理的EAP method类型，取值范围[0, 255]。 常用取值包括：eapType=1 Identity，eapType=2 Notification，eapType=3 NAK，eapType=4 MD5-Challenge，eapType=5 OTP（One-Time Password），eapType=6 GTC（Generic Token Card），eapType=13 EAP-TLS，eapType=21 EAP-TTLS，eapType=25 EAP-PEAP，eapType=254 Expanded Types，eapType=255 Experimental use。 |
| callback | Callback<EapData> | 是 | 回调函数，返回指定的eapCode+eapType的报文。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[扩展认证错误码]([扩展认证错误码](../../errors/扩展认证错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 33200006 | Invalid net type. |
| 33200007 | Invalid eap code. |
| 33200008 | Invalid eap type. |
| 33200009 | netmanager stop. |
| 33200099 | internal error. |

**示例：**

```ets
import {eap} from '@kit.NetworkKit';
let netType = 1;
let eapCode = 1;
let eapType = 25;
let  eapData = (eapData:eap.EapData):void => {
  console.info("rsp result",JSON.stringify(eapData))
}

try {
  eap.regCustomEapHandler(netType, eapCode, eapType, eapData);
  console.info('regCustomEapHandler success');
} catch (err) {
  console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

#### eap.unregCustomEapHandler

unregCustomEapHandler(netType:number, eapCode: number, eapType: number, callback: Callback<EapData>): void

用于指定需要取消定制化处理的EAP报文类型和对应的处理callback。使用callback异步回调。

**需要权限**：ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

**系统能力**：SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netType | number | 是 | 网络类型，取值为1或2。 netType=1表示WLAN，netType=2表示以太网。 |
| eapCode | number | 是 | 需要进行定制的EAP code，取值为1、2、3、4 。 code=1 Request、 code=2 Response、 code=3 Success、 code=4 Failure。 |
| eapType | number | 是 | 需要进行定制处理的EAP method类型，取值范围[0, 255]。 常用取值包括：eapType=1 Identity，eapType=2 Notification，eapType=3 NAK，eapType=4 MD5-Challenge，eapType=5 OTP（One-Time Password），eapType=6 GTC（Generic Token Card），eapType=13 EAP-TLS，eapType=21 EAP-TTLS，eapType=25 EAP-PEAP，eapType=254 Expanded Types，eapType=255 Experimental use。 |
| callback | Callback<EapData> | 是 | 回调函数，返回指定的eapCode+eapType的报文。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[扩展认证错误码](扩展认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 33200006 | Invalid net type. |
| 33200007 | Invalid eap code. |
| 33200008 | Invalid eap type. |
| 33200009 | netmanager stop. |
| 33200099 | internal error. |

**示例：**

```ets
import {eap} from '@kit.NetworkKit';
let netType = 1;
let eapCode = 1;
let eapType = 25;
let  eapData = (eapData:eap.EapData):void => {
  console.info("rsp result",JSON.stringify(eapData))
}

try {
  eap.unregCustomEapHandler(netType, eapCode, eapType, eapData);
  console.info('unregCustomEapHandler success');
} catch (err) {
  console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

#### eap.replyCustomEapData

replyCustomEapData(result: CustomResult, data: EapData): void

该接口用于通知系统已完成该步定制化处理。

- 若用于处理收EAP数据包(rx)时的callback，传给系统的EAP数据需要剥离服务器添加的定制部分。
- 若用于处理发EAP数据包(tx)时的callback，传给系统的EAP数据为经过添加定制部分后的EAP数据。

**需要权限**：ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

**系统能力**：SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | CustomResult | 是 | 定制化判定结果。 |
| data | EapData | 是 | 经过定制化的EAP数据。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[扩展认证错误码](扩展认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 33200004 | Invalid result. |
| 33200005 | Invalid size of eap data. |
| 33200009 | netmanager stop. |
| 33200099 | internal error. |

```ets
import {eap} from '@kit.NetworkKit';
let eapData:eap.EapData= {
  msgId: 1,
  eapBuffer: new Uint8Array([1, 2, 3, 4, 5]),
  bufferLen: 5,
};
let result = 1;

try {
  eap.replyCustomEapData(result, eapData);
  console.info('replyCustomEapData success');
} catch (err) {
  console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

#### eap.startEthEap

startEthEap(netId: number, profile: EthEapProfile): void

该接口用于指定一个以太网卡发起EAP认证。

**需要权限**：ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

**系统能力**：SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netId | number | 是 | 以太网卡Id。（传入默认参数-1，系统将自动匹配以太网卡发起EAP认证） |
| profile | EthEapProfile | 是 | EAP配置信息。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[扩展认证错误码](扩展认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 33200001 | Invalid netId. |
| 33200003 | Invalid profile. |
| 33200009 | netmanager stop. |
| 33200010 | invalid eth state. |
| 33200099 | internal error. |

**示例：**

```ets
import {eap} from '@kit.NetworkKit';
let netId = 100;
let profile: eap.EthEapProfile = {
  eapMethod: eap.EapMethod.EAP_TTLS,
  phase2Method: eap.Phase2Method.PHASE2_AKA_PRIME,
  identity: "identity",
  anonymousIdentity: "anonymousIdentity",
  password: "password",
  caCertAliases: "caCertAliases",
  caPath: "caPath",
  clientCertAliases: "clientCertAliases",
  certEntry: new Uint8Array([5,6,7,8,9,10]),
  certPassword: "certPassword",
  altSubjectMatch: "altSubjectMatch",
  domainSuffixMatch: "domainSuffixMatch",
  realm: "realm",
  plmn: "plmn",
  eapSubId: 1
};

try {
  eap.startEthEap(netId, profile);
  console.info('startEthEap success');
} catch (err) {
  console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

#### eap.logOffEthEap

logOffEthEap(netId: number): void

该接口用于指定一个以太网卡从EAP已认证状态退出。

**需要权限**：ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

**系统能力**：SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netId | number | 是 | 以太网卡Id。（传入默认参数-1，系统将自动匹配以太网卡发起EAP认证） |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[扩展认证错误码](扩展认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 33200001 | Invalid netId. |
| 33200002 | Log off fail. |
| 33200009 | netmanager stop. |
| 33200010 | invalid eth state. |
| 33200099 | internal error. |

**示例：**

```ets
import {eap} from '@kit.NetworkKit';
let netId = 100;
try{
  eap.logOffEthEap(netId);
  console.info("logOffEthEap success");
} catch (err) {
  console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

#### EapData

EAP信息。

​**系统能力**​：SystemCapability.Communication.NetManager.Eap

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| msgId | number | 否 | 否 | 伪随机数，用于关联处理前后的EAP数据。 |
| eapBuffer | Uint8Array | 否 | 否 | 从EAP header开始的EAP原始数据，未加密。 |
| bufferLen | number | 否 | 否 | 数据长度。 |

#### CustomResult

表示EAP认证处理结果的枚举。

​**系统能力**​：SystemCapability.Communication.NetManager.Eap

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RESULT_FAIL | 0 | 认证流程结束，结果失败。 |
| RESULT_NEXT | 1 | 认证当前流程成功，跳转到下一步。 |
| RESULT_FINISH | 2 | 认证流程结束，结果成功。 |

#### EapMethod

表示EAP认证方式的枚举。

**系统能力：** SystemCapability.Communication.NetManager.Eap

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EAP_NONE | 0 | 不指定。 |
| EAP_PEAP | 1 | PEAP类型。 |
| EAP_TLS | 2 | TLS类型。 |
| EAP_TTLS | 3 | TTLS类型。 |
| EAP_PWD | 4 | PWD类型。 |
| EAP_SIM | 5 | SIM类型。 |
| EAP_AKA | 6 | AKA类型。 |
| EAP_AKA_PRIME | 7 | AKA Prime类型。 |
| EAP_UNAUTH_TLS | 8 | UNAUTH TLS类型。 |

#### Phase2Method

表示第二阶段认证方式的枚举。

**系统能力：** SystemCapability.Communication.NetManager.Eap

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

#### EthEapProfile

可扩展身份验证协议配置信息。

**系统能力：** SystemCapability.Communication.NetManager.Eap

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eapMethod | EapMethod | 否 | 否 | AP认证方式。 |
| phase2Method | Phase2Method | 否 | 否 | 第二阶段认证方式。 |
| identity | string | 否 | 否 | 身份信息。 |
| anonymousIdentity | string | 否 | 否 | 匿名身份。 |
| password | string | 否 | 否 | 密码。 |
| caCertAliases | string | 否 | 否 | CA证书别名。 |
| caPath | string | 否 | 否 | CA证书路径。 |
| clientCertAliases | string | 否 | 否 | 客户端证书别名。 |
| certEntry | Uint8Array | 否 | 否 | CA证书内容。 |
| certPassword | string | 否 | 否 | CA证书密码。 |
| altSubjectMatch | string | 否 | 否 | 替代主题匹配。 |
| domainSuffixMatch | string | 否 | 否 | 域后缀匹配。 |
| realm | string | 否 | 否 | 通行证凭证的领域。 |
| plmn | string | 否 | 否 | 公共陆地移动网的直通凭证提供商。 |
| eapSubId | number | 否 | 否 | SIM卡的子ID。 |