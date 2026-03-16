# @ohos.wifiManager (WLAN)

该模块主要提供WLAN基础功能（无线接入、无线加密、无线漫游等）、P2P（peer-to-peer）服务的基础功能和WLAN消息通知的相应服务，让应用可以通过WLAN和其他设备互联互通。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { wifiManager } from '@kit.ConnectivityKit';
```

#### wifiManager.isWifiActive

isWifiActive(): boolean

查询WLAN开关是否已使能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明booleantrue:已使能， false:未使能。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let isWifiActive = wifiManager.isWifiActive();
    console.info("isWifiActive:" + isWifiActive);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.enableWifi15+

enableWifi(): void

启动WLAN。

**需要权限：** ohos.permission.SET_WIFI_INFO 和 (ohos.permission.MANAGE_WIFI_CONNECTION 仅系统应用可用 或 ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION 仅企业应用可用)

**系统能力：** SystemCapability.Communication.WiFi.STA

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.2501003Operation failed because the service is being closed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.enableWifi();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.disableWifi20+

disableWifi(): void

关闭WLAN。

**需要权限：** ohos.permission.SET_WIFI_INFO 和 (ohos.permission.MANAGE_WIFI_CONNECTION 仅系统应用可用 或 ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION 仅企业应用可用)

**系统能力：** SystemCapability.Communication.WiFi.STA

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.2501004Operation failed because the service is being opened.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.disableWifi();
  }catch(error){
    console.error(`disableWifi failed. ${error.message}`);
  }
```

#### wifiManager.scan(deprecated)

scan(): void

启动WLAN扫描，使用前先使能WLAN。

从 API version 9开始支持，从API version 10开始废弃。建议使用[wifiManager.startScan](#ZH-CN_TOPIC_0000002497445446__wifimanagerstartscan21)代替。

**需要权限：** ohos.permission.SET_WIFI_INFO、ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Communication.WiFi.STA

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.scan();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.startScan21+

startScan(): void

启动WLAN扫描。

- 应用程序在前台运行时，两分钟内最多可扫描四次。
- 在后台运行时，三十分钟内最多可扫描一次。
- 通过[on('wifiScanStateChange')](#ZH-CN_TOPIC_0000002497445446__wifimanageronwifiscanstatechange)订阅扫描状态变更事件，监听扫描完成通知。

**需要权限：** ohos.permission.SET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.startScan();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.getScanResults(deprecated)

getScanResults(): Promise<Array<WifiScanInfo>>

获取扫描结果，使用Promise异步回调。

- 返回一个Promise对象，解析后得到一个包含多个WifiScanInfo对象的数组，每个对象表示一个WLAN网络的扫描信息。

从 API version 9开始支持，从API version 10开始废弃。建议使用[wifiManager.getScanInfoList](#ZH-CN_TOPIC_0000002497445446__wifimanagergetscaninfolist10)代替。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 (ohos.permission.GET_WIFI_PEERS_MAC 或(ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION))

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明Promise< Array<[WifiScanInfo](#ZH-CN_TOPIC_0000002497445446__wifiscaninfo)> >Promise对象。返回扫描到的热点列表。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.

#### wifiManager.getScanResults(deprecated)

getScanResults(callback: AsyncCallback<Array<WifiScanInfo>>): void

获取扫描结果，使用callback异步回调。

- 通过回调函数返回一个包含多个WifiScanInfo对象的数组，每个对象表示一个WLAN网络的扫描信息。

从 API version 9开始支持，从API version 10开始废弃。建议使用[wifiManager.getScanInfoList](#ZH-CN_TOPIC_0000002497445446__wifimanagergetscaninfolist10)代替。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 (ohos.permission.GET_WIFI_PEERS_MAC 或 (ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION))

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明callbackAsyncCallback< Array<[WifiScanInfo](#ZH-CN_TOPIC_0000002497445446__wifiscaninfo)>>是回调函数。当成功时，err为0，data为扫描到的热点；否则err为非0值，data为空。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  wifiManager.getScanResults((err, result) => {
      if (err) {
          console.error("get scan info error");
          return;
      }

      let len = result.length;
      console.info("wifi received scan info: " + len);
      for (let i = 0; i < len; ++i) {
          console.info("ssid: " + result[i].ssid);
          console.info("bssid: " + result[i].bssid);
          console.info("capabilities: " + result[i].capabilities);
          console.info("securityType: " + result[i].securityType);
          console.info("rssi: " + result[i].rssi);
          console.info("band: " + result[i].band);
          console.info("frequency: " + result[i].frequency);
          console.info("channelWidth: " + result[i].channelWidth);
          console.info("timestamp: " + result[i].timestamp);
      }
  });

  wifiManager.getScanResults().then(result => {
      let len = result.length;
      console.info("wifi received scan info: " + len);
      for (let i = 0; i < len; ++i) {
          console.info("ssid: " + result[i].ssid);
          console.info("bssid: " + result[i].bssid);
          console.info("capabilities: " + result[i].capabilities);
          console.info("securityType: " + result[i].securityType);
          console.info("rssi: " + result[i].rssi);
          console.info("band: " + result[i].band);
          console.info("frequency: " + result[i].frequency);
          console.info("channelWidth: " + result[i].channelWidth);
          console.info("timestamp: " + result[i].timestamp);
      }
  }).catch((err:number) => {
      console.error("failed:" + JSON.stringify(err));
  });
```

#### wifiManager.getScanResultsSync(deprecated)

getScanResultsSync(): Array<[WifiScanInfo](#ZH-CN_TOPIC_0000002497445446__wifiscaninfo)>

获取扫描结果，使用同步方式返回一个包含多个WifiScanInfo对象的数组，每个对象表示一个WLAN网络的扫描信息。

从 API version 9开始支持，从API version 10开始废弃。建议使用[wifiManager.getScanInfoList](#ZH-CN_TOPIC_0000002497445446__wifimanagergetscaninfolist10)代替。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 (ohos.permission.GET_WIFI_PEERS_MAC 或 (ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY_LOCATION))

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明 Array<[WifiScanInfo](#ZH-CN_TOPIC_0000002497445446__wifiscaninfo)>扫描结果数组。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let scanInfoList = wifiManager.getScanResultsSync();
    console.info("scanInfoList:" + JSON.stringify(scanInfoList));
    let len = scanInfoList.length;
        console.info("wifi received scan info: " + len);
    if(len > 0){
      for (let i = 0; i < len; ++i) {
        console.info("ssid: " + scanInfoList[i].ssid);
        console.info("bssid: " + scanInfoList[i].bssid);
        console.info("capabilities: " + scanInfoList[i].capabilities);
        console.info("securityType: " + scanInfoList[i].securityType);
        console.info("rssi: " + scanInfoList[i].rssi);
        console.info("band: " + scanInfoList[i].band);
        console.info("frequency: " + scanInfoList[i].frequency);
        console.info("channelWidth: " + scanInfoList[i].channelWidth);
        console.info("timestamp: " + scanInfoList[i].timestamp);
      }
    }
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

```

#### wifiManager.getScanInfoList10+

getScanInfoList(): Array<WifiScanInfo>

获取包含当前时间点前30s内的缓存扫描结果。

**需要权限：** ohos.permission.GET_WIFI_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明Array<[WifiScanInfo](#ZH-CN_TOPIC_0000002497445446__wifiscaninfo)>返回扫描到的热点列表。如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限，则返回结果中的bssid为真实设备地址，否则为随机设备地址。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let scanInfoList = wifiManager.getScanInfoList();
    console.info("scanInfoList:" + JSON.stringify(scanInfoList));
    let len = scanInfoList.length;
        console.info("wifi received scan info: " + len);
    if(len > 0){
      for (let i = 0; i < len; ++i) {
        console.info("ssid: " + scanInfoList[i].ssid);
        console.info("bssid: " + scanInfoList[i].bssid);
        console.info("capabilities: " + scanInfoList[i].capabilities);
        console.info("securityType: " + scanInfoList[i].securityType);
        console.info("rssi: " + scanInfoList[i].rssi);
        console.info("band: " + scanInfoList[i].band);
        console.info("frequency: " + scanInfoList[i].frequency);
        console.info("channelWidth: " + scanInfoList[i].channelWidth);
        console.info("timestamp: " + scanInfoList[i].timestamp);
        console.info("supportedWifiCategory: " + scanInfoList[i].supportedWifiCategory);
        console.info("isHiLinkNetwork: " + scanInfoList[i].isHiLinkNetwork);
      }
    }
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

```

#### WifiScanInfo

WLAN热点信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称类型只读可选说明ssidstring否否

热点的SSID，最大长度为32字节，编码格式为UTF-8。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

bssidstring否否

热点的BSSID，例如：00:11:22:33:44:55。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

bssidType10+[DeviceAddressType](#ZH-CN_TOPIC_0000002497445446__deviceaddresstype10)否否

热点的BSSID类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

capabilitiesstring否否热点能力。securityType[WifiSecurityType](#ZH-CN_TOPIC_0000002497445446__wifisecuritytype)否否

WLAN加密类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

rssinumber否否

热点的信号强度(dBm)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

bandnumber否否WLAN接入点的频段，1表示2.4GHZ；2表示5GHZ。frequencynumber否否

WLAN接入点的频率。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

channelWidthnumber否否WLAN接入点的带宽，具体定义参见[WifiChannelWidth](#ZH-CN_TOPIC_0000002497445446__wifichannelwidth)。centerFrequency0number否否热点的中心频率。centerFrequency1number否否热点的中心频率。如果热点使用两个不重叠的WLAN信道，则返回两个中心频率，分别用centerFrequency0和centerFrequency1表示。infoElemsArray<[WifiInfoElem](#ZH-CN_TOPIC_0000002497445446__wifiinfoelem)>否否信息元素。timestampnumber否否时间戳。supportedWifiCategory12+[WifiCategory](#ZH-CN_TOPIC_0000002497445446__wificategory12)否否热点支持的最高Wi-Fi级别。isHiLinkNetwork20+boolean否否热点是否支持hiLink，true表示支持， false表示不支持。

#### DeviceAddressType10+

WLAN设备地址（MAC/BSSID）类型。是标识WLAN设备或接入点的唯一地址。

在WLAN相关操作中，如连接指定的WLAN网络、获取设备信息等，需要使用DeviceAddressType类型的参数。

**系统能力：** SystemCapability.Communication.WiFi.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

名称值说明RANDOM_DEVICE_ADDRESS0随机设备地址。REAL_DEVICE_ADDRESS1真实设备地址。

#### WifiSecurityType

表示加密类型的枚举。

**系统能力：** SystemCapability.Communication.WiFi.Core

名称值说明WIFI_SEC_TYPE_INVALID0无效加密类型。WIFI_SEC_TYPE_OPEN1

开放加密类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

WIFI_SEC_TYPE_WEP2Wired Equivalent Privacy (WEP)加密类型。候选网络(添加网络配置信息)配置不支持该加密类型。WIFI_SEC_TYPE_PSK3Pre-shared key (PSK)加密类型。WIFI_SEC_TYPE_SAE4Simultaneous Authentication of Equals (SAE)加密类型。WIFI_SEC_TYPE_EAP5EAP authentication (EAP)加密类型。WIFI_SEC_TYPE_EAP_SUITE_B6Suite-B 192位加密类型。WIFI_SEC_TYPE_OWE7Opportunistic Wireless Encryption (OWE)机会性无线加密类型。WIFI_SEC_TYPE_WAPI_CERT8WAPI-Cert加密类型。WIFI_SEC_TYPE_WAPI_PSK9WAPI-PSK加密类型。

#### WifiBandType10+

表示WIFI频段类型的枚举。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称值说明WIFI_BAND_NONE0无效频段类型。WIFI_BAND_2G12.4G频段类型。WIFI_BAND_5G25G频段类型。WIFI_BAND_6G36G频段类型。WIFI_BAND_60G460G频段类型。

#### WifiStandard10+

表示WIFI标准的枚举。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称值说明WIFI_STANDARD_UNDEFINED0无效WIFI标准类型。WIFI_STANDARD_11A1802.11a WiFi标准类型。WIFI_STANDARD_11B2802.11b WiFi标准类型。WIFI_STANDARD_11G3802.11g WiFi标准类型。WIFI_STANDARD_11N4802.11n WiFi标准类型。WIFI_STANDARD_11AC5802.11ac WiFi标准类型。WIFI_STANDARD_11AX6802.11ax WiFi标准类型。WIFI_STANDARD_11AD7802.11ad WiFi标准类型。

#### WifiInfoElem

WLAN热点信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称类型只读可选说明eidnumber否否元素ID。contentUint8Array否否元素内容。

#### WifiChannelWidth

表示带宽类型的枚举。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称值说明WIDTH_20MHZ020MHZ。WIDTH_40MHZ140MHZ。WIDTH_80MHZ280MHZ。WIDTH_160MHZ3160MHZ。WIDTH_80MHZ_PLUS480MHZ+。WIDTH_INVALID5无效值

#### WifiDeviceConfig

WLAN配置信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称类型只读可选说明ssidstring否否

热点的SSID，最大长度为32字节，编码格式为UTF-8。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

bssidstring否是

热点的BSSID，例如：00:11:22:33:44:55。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

bssidType10+[DeviceAddressType](#ZH-CN_TOPIC_0000002497445446__deviceaddresstype10)否是

热点的BSSID类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

preSharedKeystring否否

热点的密钥，最大长度为64字节。

当securityType为WIFI_SEC_TYPE_OPEN时该字段需为空串，其他加密类型不能为空串。

当securityType为WIFI_SEC_TYPE_WEP时，该字段长度只允许为5、10、13、26、16和32字节其中之一，并且当字段长度为偶数时，该字段必须为纯十六进制数字构成。

当securityType为WIFI_SEC_TYPE_SAE时，该字段最小长度为1字节。

当securityType为WIFI_SEC_TYPE_PSK时，该字段最小长度为8字节。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

isHiddenSsidboolean否是是否是隐藏网络。true表示是隐藏网络，false表示不是隐藏网络。netId22+number否是分配的网络ID。securityType[WifiSecurityType](#ZH-CN_TOPIC_0000002497445446__wifisecuritytype)否否

加密类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

eapConfig10+[WifiEapConfig](#ZH-CN_TOPIC_0000002497445446__wifieapconfig10)否是可扩展身份验证协议配置。只有securityType为WIFI_SEC_TYPE_EAP时需要填写。wapiConfig12+[WifiWapiConfig](#ZH-CN_TOPIC_0000002497445446__wifiwapiconfig12)否是WAPI身份验证协议配置。只有securityType为WIFI_SEC_TYPE_WAPI_CERT或WIFI_SEC_TYPE_WAPI_PSK时需要填写。

#### WifiEapConfig10+

可扩展身份验证协议配置信息。

- WifiEapConfig是一个用于配置WLAN网络EAP认证的类型。
- 包含EAP认证方式、第二阶段认证方式、身份信息、密码、证书等配置项。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称类型只读可选说明eapMethod[EapMethod](#ZH-CN_TOPIC_0000002497445446__eapmethod10)否否EAP认证方式。phase2Method[Phase2Method](#ZH-CN_TOPIC_0000002497445446__phase2method10)否否第二阶段认证方式。只有eapMethod为EAP_PEAP或EAP_TTLS时需要填写。identitystring否否身份信息。当eapMethod为EAP_PEAP、EAP_TLS或EAP_PWD时，该字段不能为空串。anonymousIdentitystring否否匿名身份。暂未使用。passwordstring否否密码。当eapMethod为EAP_PEAP或EAP_PWD时，该字段不能为空串，最大长度为128字节。caCertAliasstring否否CA证书别名。caPathstring否否CA证书路径。clientCertAliasstring否否客户端证书别名。certEntryUint8Array否否CA证书内容。当eapMethod为EAP_TLS时，如果该字段为空，则clientCertAlias不能为空。certPasswordstring否否CA证书密码，最大长度为128字节。altSubjectMatchstring否否替代主题匹配。domainSuffixMatchstring否否域后缀匹配。realmstring否否通行证凭证的领域。plmnstring否否公共陆地移动网的直通凭证提供商。eapSubIdnumber否否SIM卡的子ID。

#### WifiWapiConfig12+

WAPI身份验证协议配置。

WAPI(Wireless LAN Authentication and Privacy Infrastructure) 身份验证协议配置。

当用户通过WAPI身份验证协议连接无线网时，可通过以下方式配置参数或者证书进行连接。

- 方式一:通过配置证书进行连接。WifiDeviceConfig中关键字段的配置如下:

  - preSharedKey无需传参;
  - securityType设置为WIFI_SEC_TYPE_WAPI_CERT;
  - 在wapiConfig中：

    - wapiAsCert传递AS证书的文本内容。
    - wapiUserCert传递用户证书的文本内容。

- 方式二:通过配置preSharedKey进行链接。WifiDeviceConfig中关键字段的配置如下:

  - preSharedKey传参为路由器上设置的密码;
  - securityType设置为WIFI_SEC_TYPE_WAPI_PSK。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称类型只读可选说明wapiPskType[WapiPskType](#ZH-CN_TOPIC_0000002497445446__wapipsktype12)否否加密类型。wapiAsCertstring否否AS证书(Authentication Server Certificate，认证服务器证书)。wapiUserCertstring否否用户证书。

#### WapiPskType12+

WAPI认证方式的枚举。

**系统能力：** SystemCapability.Communication.WiFi.Core

名称值说明WAPI_PSK_ASCII0ASCII类型。WAPI_PSK_HEX1HEX类型。

#### EapMethod10+

表示EAP认证方式的枚举。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称值说明EAP_NONE0不指定。EAP_PEAP1PEAP类型。EAP_TLS2TLS类型。EAP_TTLS3TTLS类型。EAP_PWD4PWD类型。EAP_SIM5SIM类型。EAP_AKA6AKA类型。EAP_AKA_PRIME7AKA Prime类型。EAP_UNAUTH_TLS8UNAUTH TLS类型。

#### Phase2Method10+

表示第二阶段认证方式的枚举。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称值说明PHASE2_NONE0不指定。PHASE2_PAP1PAP类型。PHASE2_MSCHAP2MSCHAP类型。PHASE2_MSCHAPV23MSCHAPV2类型。PHASE2_GTC4GTC类型。PHASE2_SIM5SIM类型。PHASE2_AKA6AKA类型。PHASE2_AKA_PRIME7AKA Prime类型。

#### WifiCategory12+

表示热点支持的最高WLAN类别。可以用于识别和区分不同WLAN技术标准的热点。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称值说明DEFAULT1Default。Wifi6以下的wifi类别。WIFI62Wifi6。WIFI6_PLUS3Wifi6+。WIFI715+4Wifi7。WIFI7_PLUS15+5Wifi7+。

#### wifiManager.addCandidateConfig

addCandidateConfig(config: WifiDeviceConfig): Promise<number>

添加候选网络配置，使用Promise异步回调，使用前先使能WLAN。

- 通过传入[WifiDeviceConfig](#ZH-CN_TOPIC_0000002497445446__wifideviceconfig)对象，配置WLAN网络的详细信息，如SSID、密码、安全类型等。
- 返回一个Promise对象，解析后得到一个数字，表示配置的ID(用于区分、管理不同WLAN配置，其他相关API操作，错误处理调试等)。

**需要权限：** ohos.permission.SET_WIFI_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明config[WifiDeviceConfig](#ZH-CN_TOPIC_0000002497445446__wifideviceconfig)是WLAN配置信息。如果bssidType未指定值，则bssidType默认为随机设备地址类型。

**返回值：**

类型说明Promise<number>Promise对象。表示网络配置ID。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401

Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2. Incorrect parameter types. 3. Parameter verification failed.

801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let config:wifiManager.WifiDeviceConfig = {
      ssid : "****",
      preSharedKey : "****",
      securityType : 0
    }
    wifiManager.addCandidateConfig(config).then(result => {
      console.info("result:" + JSON.stringify(result));
    }).catch((err:number) => {
      console.error("failed:" + JSON.stringify(err));
    });
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.addCandidateConfig

addCandidateConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void

添加候选网络配置，使用callback异步回调。

- 将指定的WLAN设备配置添加为候选网络，添加后的网络在没有连接记录的情况下无法触发自动回连，可以通过 connectToCandidateConfig或connectToCandidateConfigWithUserAction 方法实现候选网络连接，页面确认连接成功后，可实现自动回连。
- 候选网络属于应用维度添加的网络配置，和系统网络配置是相互隔离的，在系统WLAN页面不可见。

**需要权限：** ohos.permission.SET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明config[WifiDeviceConfig](#ZH-CN_TOPIC_0000002497445446__wifideviceconfig)是WLAN配置信息。如果bssidType未指定值，则bssidType默认为随机设备地址类型。callbackAsyncCallback<number>是

回调函数。err为0时：操作成功，data为添加的网络配置ID，如果data值为-1，表示添加失败。

 err为非0值时：操作出现错误。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401

Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2. Incorrect parameter types. 3. Parameter verification failed.

801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let config:wifiManager.WifiDeviceConfig = {
      ssid : "****",
      preSharedKey : "****",
      securityType : 0
    }
    wifiManager.addCandidateConfig(config,(error,result) => {
      console.info("result:" + JSON.stringify(result));
    });
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.removeCandidateConfig

removeCandidateConfig(networkId: number): Promise<void>

移除候选网络配置，使用Promise异步回调。

- 从系统中删除指定网络ID的WLAN候选配置，清理不再需要的WLAN候选配置，释放系统资源。
- 只能移除通过[addCandidateConfig](#ZH-CN_TOPIC_0000002497445446__wifimanageraddcandidateconfig)添加的候选配置，移除后该候选网络将不再被系统自动连接。

**需要权限：** ohos.permission.SET_WIFI_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明networkIdnumber是网络配置ID。

**返回值：**

类型说明Promise<void>Promise对象。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401

Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2. Incorrect parameter types. 3. Parameter verification failed.

801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let networkId = 0;
    wifiManager.removeCandidateConfig(networkId).then(result => {
      console.info("result:" + JSON.stringify(result));
    }).catch((err:number) => {
      console.error("failed:" + JSON.stringify(err));
    });
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.removeCandidateConfig

removeCandidateConfig(networkId: number, callback: AsyncCallback<void>): void

移除指定的候选网络配置，使用callback异步回调。

- 从系统中删除指定网络ID的WLAN候选配置，清理不再需要的WLAN候选配置，释放系统资源。
- 只能移除通过[addCandidateConfig](#ZH-CN_TOPIC_0000002497445446__wifimanageraddcandidateconfig)添加的候选配置，移除后该候选网络将不再被系统自动连接。

**需要权限：** ohos.permission.SET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

参数名类型必填说明networkIdnumber是网络配置ID。callbackAsyncCallback<void>是回调函数。当操作成功时，err为0。如果error为非0，表示处理出现错误。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401

Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2. Incorrect parameter types. 3. Parameter verification failed.

801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let networkId = 0;
    wifiManager.removeCandidateConfig(networkId,(error,result) => {
    console.info("result:" + JSON.stringify(result));
    });
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.removeDevice15+

removeDevice(id: number): void

移除网络配置。

- 通过网络配置ID删除已保存的WLAN网络配置信息。
- 移除后对应的网络配置将不再可用，设备也不会再自动连接该网络。

**需要权限：** ohos.permission.SET_WIFI_INFO 和 (ohos.permission.MANAGE_WIFI_CONNECTION 仅系统应用可用 或 ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION 仅企业应用可用)

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明idnumber是网络配置ID。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401

Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2. Incorrect parameter types. 3. Parameter verification failed.

801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

    try {
      let id = 0;
      wifiManager.removeDevice(id);
    }catch(error){
      console.error("failed:" + JSON.stringify(error));
    }
```

#### wifiManager.getCandidateConfigs

getCandidateConfigs(): Array<WifiDeviceConfig>

获取候选网络配置。

- 候选网络是指曾经连接过或者手动添加的网络配置。
- 该接口返回系统中所有已保存但当前未连接的WLAN网络配置。
- 用于展示可连接的网络列表或进行网络管理操作。

**需要权限：**

API 10起：ohos.permission.GET_WIFI_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明 Array<[WifiDeviceConfig](#ZH-CN_TOPIC_0000002497445446__wifideviceconfig)>候选网络配置数组。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let configs = wifiManager.getCandidateConfigs();
    console.info("configs:" + JSON.stringify(configs));
    let len = configs.length;
        console.info("result len: " + len);
    if(len > 0){
      for (let i = 0; i < len; ++i) {
        console.info("ssid: " + configs[i].ssid);
        console.info("bssid: " + configs[i].bssid);
      }
    }
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

```

#### wifiManager.connectToCandidateConfig

connectToCandidateConfig(networkId: number): void

应用使用该接口连接到自己添加的候选网络。

**需要权限：** ohos.permission.SET_WIFI_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明networkIdnumber是候选网络配置的ID。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401

Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2. Incorrect parameter types. 3. Parameter verification failed.

801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let networkId = 0; // 候选网络ID，在添加候选网络时生成
    wifiManager.connectToCandidateConfig(networkId);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }

```

#### wifiManager.connectToCandidateConfigWithUserAction20+

connectToCandidateConfigWithUserAction(networkId: number): Promise<void>

该接口用于应用连接到用户添加的候选网络，并在连接时提示用户进行信任确认。使用Promise异步回调用户响应结果。

- 调用此接口时，系统将提示用户确认是否信任并连接到指定的候选网络，通过Promise异步返回用户响应结果。
- 用户确认是连接过程中的必要步骤，未获得用户信任确认前，连接操作不会执行。
- 建议在发起连接前先通过startScan接口触发一次WLAN扫描，通过[wifiManager.on('wifiScanStateChange')](#ZH-CN_TOPIC_0000002497445446__wifimanageronwifiscanstatechange)方法监听到扫描结果刷新后再连接，以提高连接成功率。

调用[wifiManager.connectToCandidateConfig](#ZH-CN_TOPIC_0000002497445446__wifimanagerconnecttocandidateconfig)连接候选网络时，不会返回用户响应结果。

**需要权限：** ohos.permission.SET_WIFI_INFO

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明networkIdnumber是候选网络配置的ID，ID不能小于0。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.2501005The user does not respond.2501006The user refused the action.2501007Parameter validation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let networkId = 0; // 候选网络ID，在添加候选网络时生成
    wifiManager.connectToCandidateConfigWithUserAction(networkId).then(result => {
      console.info("result:" + JSON.stringify(result));
    }).catch((err:number) => {
      console.error("failed:" + JSON.stringify(err));
    });
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.addDeviceConfig15+

addDeviceConfig(config: WifiDeviceConfig): Promise<number>

添加网络配置。使用Promise异步回调。

**需要权限：** ohos.permission.SET_WIFI_INFO 和 ohos.permission.SET_WIFI_CONFIG

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明config[WifiDeviceConfig](#ZH-CN_TOPIC_0000002497445446__wifideviceconfig)是WLAN配置信息。如果bssidType无指定值，则bssidType默认为随机设备地址类型。

**返回值：**

类型说明Promise<number>Promise对象。表示网络配置ID。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401

Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2. Incorrect parameter types. 3. Parameter verification failed.

801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let config:wifiManager.WifiDeviceConfig = {
      ssid : "****",
      preSharedKey : "****",
      securityType : 0
    }
    wifiManager.addDeviceConfig(config).then(result => {
      console.info("result:" + JSON.stringify(result));
    }).catch((err:number) => {
      console.error("failed:" + JSON.stringify(err));
    });
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.addDeviceConfig15+

addDeviceConfig(config: WifiDeviceConfig, callback: AsyncCallback<number>): void

添加网络配置。使用callback异步回调。

**需要权限：** ohos.permission.SET_WIFI_INFO 和 ohos.permission.SET_WIFI_CONFIG

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明config[WifiDeviceConfig](#ZH-CN_TOPIC_0000002497445446__wifideviceconfig)是WLAN配置信息。如果bssidType无指定值，则bssidType默认为随机设备地址类型。callbackAsyncCallback<number>是回调函数。当操作成功时，err为0，data为添加的网络配置ID，如果data值为-1，表示添加失败。当操作错误，err为非0值。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401

Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2. Incorrect parameter types. 3. Parameter verification failed.

801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

    try {
      let config:wifiManager.WifiDeviceConfig = {
        ssid : "****",
        preSharedKey : "****",
        securityType : 0
      }
      wifiManager.addDeviceConfig(config,(error,result) => {
        console.info("result:" + JSON.stringify(result));
      });
    }catch(error){
      console.error("failed:" + JSON.stringify(error));
    }
```

#### wifiManager.getDeviceConfigs15+

getDeviceConfigs(): Array<WifiDeviceConfig>

获取网络配置。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 ohos.permission.GET_WIFI_CONFIG

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明 Array<[WifiDeviceConfig](#ZH-CN_TOPIC_0000002497445446__wifideviceconfig)>网络配置数组。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

    try {
      let configs = wifiManager.getDeviceConfigs();
      console.info("configs:" + JSON.stringify(configs));
    }catch(error){
      console.error("failed:", error.code, error.message);
    }

```

#### wifiManager.connectToNetwork15+

connectToNetwork(networkId: number): void

应用使用该接口连接到热点。

**需要权限：** ohos.permission.MANAGE_WIFI_CONNECTION 仅系统应用可用 或 ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION 仅企业应用可用

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明networkIdnumber是候选网络配置的ID。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401

Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2. Incorrect parameter types. 3. Parameter verification failed.

801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

    try {
      let networkId = 0;
      wifiManager.connectToNetwork(networkId);
    }catch(error){
      console.error("failed:" + JSON.stringify(error));
    }

```

#### wifiManager.getSignalLevel

getSignalLevel(rssi: number, band: number): number

查询WLAN信号强度。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明rssinumber是热点的信号强度(dBm)。bandnumber是WLAN接入点的频段，1表示2.4GHZ；2表示5GHZ。

**返回值：**

类型说明number信号强度，取值范围为[0, 4]。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let rssi = 0;
    let band = 0;
    let level = wifiManager.getSignalLevel(rssi,band);
    console.info("level:" + JSON.stringify(level));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.getLinkedInfo

getLinkedInfo(): Promise<WifiLinkedInfo>

获取WLAN连接信息。使用Promise异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO 。

当macType是1 - 设备MAC地址时，获取 macAddress 还需申请ohos.permission.GET_WIFI_LOCAL_MAC权限（该权限仅系统应用可申请），无该权限时，macAddress 返回随机MAC地址。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明Promise<[WifiLinkedInfo](#ZH-CN_TOPIC_0000002497445446__wifilinkedinfo)>Promise对象。表示WLAN连接信息。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

#### wifiManager.getLinkedInfo

getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void

获取WLAN连接信息。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO 。

- 当macType是1（设备MAC地址），获取macAddress还需申请ohos.permission.GET_WIFI_LOCAL_MAC权限（该权限仅系统应用可申请），无该权限时，macAddress返回为空。
- 如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限，则返回结果中的bssid为真实BSSID地址，否则为随机设备地址。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明callbackAsyncCallback<[WifiLinkedInfo](#ZH-CN_TOPIC_0000002497445446__wifilinkedinfo)>是回调函数。当获取成功时，err为0，data表示WLAN连接信息。如果err为非0，表示处理出现错误。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

**示例：**

```ets
import { wifiManager } from '@kit.ConnectivityKit';

wifiManager.getLinkedInfo().then((data: wifiManager.WifiLinkedInfo) => {
    console.info("get wifi linked info: " + JSON.stringify(data));
}).catch((error: Error) => {
    console.error("get linked info error: ", error);
});
```

#### wifiManager.getLinkedInfoSync18+

getLinkedInfoSync(): WifiLinkedInfo;

获取WLAN连接信息，使用同步方式返回结果。

**需要权限：** ohos.permission.GET_WIFI_INFO 。

- 当macType是1（设备MAC地址），获取macAddress还需申请ohos.permission.GET_WIFI_LOCAL_MAC权限（该权限仅系统应用可申请），无该权限时，macAddress返回为空。
- 如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限，则返回结果中的bssid为真实BSSID地址，否则为随机设备地址。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明[WifiLinkedInfo](#ZH-CN_TOPIC_0000002497445446__wifilinkedinfo)表示WLAN连接信息。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';
  try {
    let linkInfo = wifiManager.getLinkedInfoSync();
    console.info("get linked info:" + JSON.stringify(linkInfo));
  } catch(error) {
    console.error("get linked info failed:" + JSON.stringify(error));
  }
```

#### WifiLinkedInfo

提供WLAN连接的相关信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称类型只读可选说明ssidstring否否

热点的SSID，编码格式为UTF-8。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

bssidstring否否

热点的BSSID。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

rssinumber否否

热点的信号强度(dBm)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

bandnumber否否WLAN接入点的频段，1表示2.4GHZ；2表示5GHZ。linkSpeednumber否否WLAN接入点的上行速度，单位Mbps。rxLinkSpeed10+number否否WLAN接入点的下行速度，单位Mbps。maxSupportedTxLinkSpeed10+number否否当前支持的最大上行速率，单位Mbps。maxSupportedRxLinkSpeed10+number否否当前支持的最大下行速率，单位Mbps。frequencynumber否否

WLAN接入点的频率。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

isHiddenboolean否否WLAN接入点是否是隐藏网络，true表示是隐藏网络，false表示不是隐藏网络。isRestrictedboolean否否WLAN接入点是否限制数据量，true表示限制，false表示不限制。macTypenumber否否MAC地址类型。0 - 随机MAC地址，1 - 设备MAC地址。macAddressstring否否设备的MAC地址。ipAddressnumber否否

WLAN连接的IP地址。

1. IP地址在WiFi连接信息和"设置 > 关于本机 > 状态信息"中可以查看。

2. ipAddress值为number类型，需要转换为IP常用格式，具体请参考[IP格式转换](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-4)。

connState[ConnState](#ZH-CN_TOPIC_0000002497445446__connstate)否否WLAN连接状态。channelWidth10+[WifiChannelWidth](#ZH-CN_TOPIC_0000002497445446__wifichannelwidth)否否当前连接热点的信道带宽。wifiStandard10+[WifiStandard](#ZH-CN_TOPIC_0000002497445446__wifistandard10)否否当前连接热点的Wi-Fi标准。supportedWifiCategory12+[WifiCategory](#ZH-CN_TOPIC_0000002497445446__wificategory12)否否热点支持的最高Wi-Fi级别。isHiLinkNetwork12+boolean否否热点是否支持hilink，true表示支持， false表示不支持。wifiLinkType18+[WifiLinkType](#ZH-CN_TOPIC_0000002497445446__wifilinktype18)否是Wi-Fi7连接类型。

#### WifiLinkType18+

枚举，Wi-Fi7连接类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称值说明DEFAULT_LINK0默认连接类型。WIFI7_SINGLE_LINK1Wi-Fi7单链连接。WIFI7_MLSR2Wi-Fi7 MLSR（multi-link single-radio，多链路多天线）连接。WIFI7_EMLSR3Wi-Fi7 EMLSR（enhanced multi-link single-radio，增强型多链路单天线）连接。WIFI7_STR4Wi-Fi7 STR（Simultaneous Tx and Rx，同时发送和接收）连接。

#### ConnState

表示WLAN连接状态的枚举。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称值说明SCANNING0设备正在搜索可用的AP。CONNECTING1正在建立WLAN连接。AUTHENTICATING2WLAN连接正在认证中。OBTAINING_IPADDR3正在获取WLAN连接的IP地址。CONNECTED4WLAN连接已建立。DISCONNECTING5WLAN连接正在断开。DISCONNECTED6WLAN连接已断开。UNKNOWN7WLAN连接建立失败。

#### wifiManager.isConnected

isConnected(): boolean

查询WLAN是否已连接。

**需要权限：** ohos.permission.GET_WIFI_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明booleantrue:已连接， false:未连接。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let ret = wifiManager.isConnected();
    console.info("isConnected:" + ret);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.disconnect15+

disconnect(): void

断开WLAN连接。

**需要权限：** ohos.permission.SET_WIFI_INFO 和 (ohos.permission.MANAGE_WIFI_CONNECTION 仅系统应用可用 或

 ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION 仅企业应用可用)

**系统能力：** SystemCapability.Communication.WiFi.STA

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.disconnect();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.isFeatureSupported

isFeatureSupported(featureId: number): boolean

判断设备是否支持相关WLAN特性。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.Core

**参数：**

参数名类型必填说明featureIdnumber是特性ID值。

**特性ID值枚举：**

枚举值说明0x0001基础结构模式特性。0x00025 GHz带宽特性。0x0004GAS/ANQP特性。0x0008Wifi-Direct特性。0x0010Soft AP特性。0x0040Wi-Fi AWare组网特性。0x8000AP STA共存特性。0x8000000WPA3-Personal SAE特性。0x10000000WPA3-Enterprise Suite-B。0x20000000增强开放特性。

**返回值：**

类型说明booleantrue:支持， false:不支持。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401

Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

801Capability not supported.2401000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let featureId = 0;
    let ret = wifiManager.isFeatureSupported(featureId);
    console.info("isFeatureSupported:" + ret);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.getDeviceMacAddress15+

getDeviceMacAddress(): string[]

获取设备的MAC地址。

**需要权限：** ohos.permission.GET_WIFI_LOCAL_MAC 和 ohos.permission.GET_WIFI_INFO

API8-15 ohos.permission.GET_WIFI_LOCAL_MAC权限仅向系统应用开放，从API16开始，在PC/2in1设备上面向普通应用开放，在其余设备上仍仅面向系统应用开放。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明string[]MAC地址。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let ret = wifiManager.getDeviceMacAddress();
    console.info("deviceMacAddress:" + JSON.stringify(ret));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.getIpInfo

getIpInfo(): IpInfo

获取IPV4信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明[IpInfo](#ZH-CN_TOPIC_0000002497445446__ipinfo)IP信息。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let info = wifiManager.getIpInfo();
    console.info("info:" + JSON.stringify(info));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### IpInfo

IPV4信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称类型只读可选说明ipAddressnumber否否IP地址。（ipAddress值为number类型，需要转换为IP常用格式，具体请参考[IP格式转换](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-4)）。gatewaynumber否否网关。netmasknumber否否掩码。primaryDnsnumber否否主DNS服务器IP地址。secondDnsnumber否否备DNS服务器IP地址。serverIpnumber否否DHCP服务端IP地址。leaseDurationnumber否否IP地址租用时长，单位：秒。

#### wifiManager.getIpv6Info10+

getIpv6Info(): Ipv6Info

获取IPV6信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明[Ipv6Info](#ZH-CN_TOPIC_0000002497445446__ipv6info10)Ipv6信息。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let info = wifiManager.getIpv6Info();
    console.info("info:" + JSON.stringify(info));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### Ipv6Info10+

Ipv6信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称类型只读可选说明linkIpv6Addressstring否否链路Ipv6地址。globalIpv6Addressstring否否全局Ipv6地址。randomGlobalIpv6Addressstring否否随机全局Ipv6地址。 预留字段，暂不支持。uniqueIpv6Address12+string否是唯一本地Ipv6地址。randomUniqueIpv6Address12+string否是随机唯一本地Ipv6地址。gatewaystring否否网关。netmaskstring否否网络掩码。primaryDNSstring否否主DNS服务器Ipv6地址。secondDNSstring否否备DNS服务器Ipv6地址。

#### wifiManager.getCountryCode

getCountryCode(): string

获取国家码信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.Core

**返回值：**

类型说明string国家码。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2401000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let code = wifiManager.getCountryCode();
    console.info("code:" + code);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.isBandTypeSupported10+

isBandTypeSupported(bandType: WifiBandType): boolean

判断当前频段是否支持。

**需要权限：** ohos.permission.GET_WIFI_INFO。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明bandType[WifiBandType](#ZH-CN_TOPIC_0000002497445446__wifibandtype10)是Wifi 频段类型。

**返回值：**

类型说明booleantrue:支持， false:不支持。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let type = 0;
    let isBandTypeSupported = wifiManager.isBandTypeSupported(type);
    console.info("isBandTypeSupported:" + isBandTypeSupported);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.isMeteredHotspot11+

isMeteredHotspot(): boolean

查询设备当前连接的wifi是否是手机热点。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明booleantrue:是手机热点， false:不是手机热点。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let isMeteredHotspot = wifiManager.isMeteredHotspot();
    console.info("isMeteredHotspot:" + isMeteredHotspot);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.isHotspotActive15+

isHotspotActive(): boolean

热点是否已使能。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**返回值：**

类型说明booleantrue:已使能， false:未使能。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2601000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let ret = wifiManager.isHotspotActive();
    console.info("result:" + ret);
  } catch(error) {
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.getP2pLinkedInfo

getP2pLinkedInfo(): Promise<WifiP2pLinkedInfo>

获取P2P连接信息。使用Promise异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

获取 groupOwnerAddr 还需申请ohos.permission.GET_WIFI_LOCAL_MAC权限（该权限仅系统应用可申请），无该权限时，groupOwnerAddr 返回全零地址。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

类型说明Promise<[WifiP2pLinkedInfo](#ZH-CN_TOPIC_0000002497445446__wifip2plinkedinfo)>Promise对象。表示P2P连接信息。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2801000Operation failed.

#### wifiManager.getP2pLinkedInfo

getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void

获取P2P连接信息。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

获取 groupOwnerAddr 还需申请ohos.permission.GET_WIFI_LOCAL_MAC权限（该权限仅系统应用可申请），无该权限时，groupOwnerAddr 返回全零地址。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明callbackAsyncCallback<[WifiP2pLinkedInfo](#ZH-CN_TOPIC_0000002497445446__wifip2plinkedinfo)>是回调函数。当操作成功时，err为0，data表示P2P连接信息。如果err为非0，表示处理出现错误。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2801000Operation failed.2801001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  wifiManager.getP2pLinkedInfo((err, data:wifiManager.WifiP2pLinkedInfo) => {
    if (err) {
        console.error("get p2p linked info error");
        return;
    }
    console.info("get wifi p2p linked info: " + JSON.stringify(data));
  });

  wifiManager.getP2pLinkedInfo().then(data => {
    console.info("get wifi p2p linked info: " + JSON.stringify(data));
  });
```

#### WifiP2pLinkedInfo

提供WLAN连接的相关信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称类型只读可选说明connectState[P2pConnectState](#ZH-CN_TOPIC_0000002497445446__p2pconnectstate)否否P2P连接状态。isGroupOwnerboolean否否true表示是群主，false表示不是群主。groupOwnerAddrstring否否群组IP地址。

#### P2pConnectState

表示P2P连接状态的枚举。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称值说明DISCONNECTED0断开状态。CONNECTED1连接状态。

#### wifiManager.getCurrentGroup

getCurrentGroup(): Promise<WifiP2pGroupInfo>

获取P2P当前组信息。使用Promise异步回调。

**需要权限：**

API 10起：ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

类型说明Promise<[WifiP2pGroupInfo](#ZH-CN_TOPIC_0000002497445446__wifip2pgroupinfo)>Promise对象。表示当前组信息。如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限，则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2801000Operation failed.

#### wifiManager.getCurrentGroup

getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void

获取P2P当前组信息。使用callback异步回调。

**需要权限：**

API 10起：ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明callbackAsyncCallback<[WifiP2pGroupInfo](#ZH-CN_TOPIC_0000002497445446__wifip2pgroupinfo)>是回调函数。当操作成功时，err为0，data表示当前组信息。如果error为非0，表示处理出现错误。如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限，则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2801000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';
  // p2p已经建组或者连接成功，才能正常获取到当前组信息
  wifiManager.getCurrentGroup((err, data:wifiManager.WifiP2pGroupInfo) => {
    if (err) {
        console.error("get current P2P group error");
        return;
    }
    console.info("get current P2P group: " + JSON.stringify(data));
  });

  wifiManager.getCurrentGroup().then(data => {
    console.info("get current P2P group: " + JSON.stringify(data));
  });
```

#### wifiManager.getP2pPeerDevices

getP2pPeerDevices(): Promise<WifiP2pDevice[]>

获取P2P对端设备列表信息。使用Promise异步回调。

**需要权限：**

API 10起：ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

类型说明Promise<[WifiP2pDevice[]](#ZH-CN_TOPIC_0000002497445446__wifip2pdevice)>Promise对象。表示对端设备列表信息。如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限，则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2801000Operation failed.

#### wifiManager.getP2pPeerDevices

getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void

获取P2P对端设备列表信息。使用callback异步回调。

**需要权限：**

API 10起：ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明callbackAsyncCallback<[WifiP2pDevice[]](#ZH-CN_TOPIC_0000002497445446__wifip2pdevice)>是回调函数。当操作成功时，err为0，data表示对端设备列表信息。如果err为非0，表示处理出现错误。如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限，则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2801000Operation failed.2801001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';
  // p2p发现阶段完成，才能正常获取到对端设备列表信息
  wifiManager.getP2pPeerDevices((err, data:wifiManager.WifiP2pDevice[]) => {
    if (err) {
        console.error("get P2P peer devices error");
        return;
    }
    console.info("get P2P peer devices: " + JSON.stringify(data));
  });

  wifiManager.getP2pPeerDevices().then(data => {
    console.info("get P2P peer devices: " + JSON.stringify(data));
  });
```

#### WifiP2pDevice

表示P2P设备信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称类型只读可选说明deviceNamestring否否设备名称。deviceAddressstring否否设备MAC地址。deviceAddressType10+[DeviceAddressType](#ZH-CN_TOPIC_0000002497445446__deviceaddresstype10)否是设备MAC地址类型。primaryDeviceTypestring否否主设备类型。deviceStatus[P2pDeviceStatus](#ZH-CN_TOPIC_0000002497445446__p2pdevicestatus)否否设备状态。groupCapabilitiesnumber否否群组能力。

#### P2pDeviceStatus

表示设备状态的枚举。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称值说明CONNECTED0连接状态。INVITED1邀请状态。FAILED2失败状态。AVAILABLE3可用状态。UNAVAILABLE4不可用状态。

#### wifiManager.getP2pLocalDevice

getP2pLocalDevice(): Promise<WifiP2pDevice>

获取P2P本端设备信息，使用Promise异步回调。

**需要权限：**

API 11起：ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

类型说明Promise<[WifiP2pDevice](#ZH-CN_TOPIC_0000002497445446__wifip2pdevice)>Promise对象。表示本端设备信息。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2801000Operation failed.

#### wifiManager.getP2pLocalDevice

getP2pLocalDevice(callback: AsyncCallback<WifiP2pDevice>): void

获取P2P本端设备信息，使用callback异步回调。

**需要权限：**

API 11起：ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明callbackAsyncCallback<[WifiP2pDevice](#ZH-CN_TOPIC_0000002497445446__wifip2pdevice)>是回调函数。当操作成功时，err为0，data表示本端设备信息。如果error为非0，表示处理出现错误。

**错误码：**

错误码ID错误信息201Permission denied.801Capability not supported.2801000Operation failed.2801001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';
  // p2p已经建组或者连接成功，才能正常获取到本端设备信息
  wifiManager.getP2pLocalDevice((err, data:wifiManager.WifiP2pDevice) => {
    if (err) {
        console.error("get P2P local device error");
        return;
    }
    console.info("get P2P local device: " + JSON.stringify(data));
  });

  wifiManager.getP2pLocalDevice().then(data => {
    console.info("get P2P local device: " + JSON.stringify(data));
  });
```

#### wifiManager.createGroup

createGroup(config: WifiP2PConfig): void

创建群组。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明config[WifiP2PConfig](#ZH-CN_TOPIC_0000002497445446__wifip2pconfig)是群组配置信息。如果DeviceAddressType未指定值，则DeviceAddressType默认为随机设备地址类型。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401

Invalid parameters. Possible causes: 1. Incorrect parameter types.

2. Parameter verification failed.

801Capability not supported.2801000Operation failed.2801001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let config:wifiManager.WifiP2PConfig = {
      deviceAddress: "****",
      netId: 0,
      passphrase: "*****",
      groupName: "****",
      goBand: 0
    }
    wifiManager.createGroup(config);

  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### WifiP2PConfig

表示P2P配置信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称类型只读可选说明deviceAddressstring否否设备地址。deviceAddressType10+[DeviceAddressType](#ZH-CN_TOPIC_0000002497445446__deviceaddresstype10)否是设备地址类型。netIdnumber否否网络ID。创建群组时-1表示创建临时组，-2表示创建永久组。passphrasestring否否群组密钥。groupNamestring否否群组名称。goBand[GroupOwnerBand](#ZH-CN_TOPIC_0000002497445446__groupownerband)否否群组带宽。

#### GroupOwnerBand

表示群组带宽的枚举。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称值说明GO_BAND_AUTO0自动模式。GO_BAND_2GHZ12.4GHZ。GO_BAND_5GHZ25GHZ。

#### wifiManager.removeGroup

removeGroup(): void

移除群组。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2801000Operation failed.2801001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.removeGroup();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.p2pConnect

p2pConnect(config: WifiP2PConfig): void

执行P2P连接。

**需要权限：**

API 10起：ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明config[WifiP2PConfig](#ZH-CN_TOPIC_0000002497445446__wifip2pconfig)是连接配置信息。如果DeviceAddressType未指定值，则DeviceAddressType默认为随机设备地址类型。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401

Invalid parameters. Possible causes: 1. Incorrect parameter types.

2. Parameter verification failed.

801Capability not supported.2801000Operation failed.2801001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  let recvP2pConnectionChangeFunc = (result:wifiManager.WifiP2pLinkedInfo) => {
      console.info("p2p connection change receive event: " + JSON.stringify(result));
      wifiManager.getP2pLinkedInfo((err, data:wifiManager.WifiP2pLinkedInfo) => {
          if (err) {
              console.error('failed to get getP2pLinkedInfo: ' + JSON.stringify(err));
              return;
          }
          console.info("get getP2pLinkedInfo: " + JSON.stringify(data));
      });
  }
  wifiManager.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

  let recvP2pDeviceChangeFunc = (result:wifiManager.WifiP2pDevice) => {
      console.info("p2p device change receive event: " + JSON.stringify(result));
  }
  wifiManager.on("p2pDeviceChange", recvP2pDeviceChangeFunc);

  let recvP2pPeerDeviceChangeFunc = (result:wifiManager.WifiP2pDevice[]) => {
      console.info("p2p peer device change receive event: " + JSON.stringify(result));
      wifiManager.getP2pPeerDevices((err, data:wifiManager.WifiP2pDevice[]) => {
          if (err) {
              console.error('failed to get peer devices: ' + JSON.stringify(err));
              return;
          }
          console.info("get peer devices: " + JSON.stringify(data));
          let len = data.length;
          for (let i = 0; i < len; ++i) {
              if (data[i].deviceName === "my_test_device") {
                  console.info("p2p connect to test device: " + data[i].deviceAddress);
                  let config:wifiManager.WifiP2PConfig = {
                      deviceAddress:data[i].deviceAddress,
                      netId:-2,
                      passphrase:"",
                      groupName:"",
                      goBand:0,
                  }
                  wifiManager.p2pConnect(config);
              }
          }
      });
  }
  wifiManager.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

  let recvP2pPersistentGroupChangeFunc = () => {
      console.info("p2p persistent group change receive event");

      wifiManager.getCurrentGroup((err, data:wifiManager.WifiP2pGroupInfo) => {
          if (err) {
              console.error('failed to get current group: ' + JSON.stringify(err));
              return;
          }
          console.info("get current group: " + JSON.stringify(data));
      });
  }
  wifiManager.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

  setTimeout(() => {wifiManager.off("p2pConnectionChange", recvP2pConnectionChangeFunc);}, 125 * 1000);
  setTimeout(() =>  {wifiManager.off("p2pDeviceChange", recvP2pDeviceChangeFunc);}, 125 * 1000);
  setTimeout(() =>  {wifiManager.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);}, 125 * 1000);
  setTimeout(() =>  {wifiManager.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);}, 125 * 1000);
  console.info("start discover devices -> " + wifiManager.startDiscoverDevices());
```

#### wifiManager.p2pCancelConnect

p2pCancelConnect(): void

在P2P连接过程中，取消P2P连接。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2801000Operation failed.2801001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.p2pCancelConnect();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.startDiscoverDevices

startDiscoverDevices(): void

开始发现设备。

**需要权限：**

API 10起：ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2801000Operation failed.2801001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.startDiscoverDevices();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.stopDiscoverDevices

stopDiscoverDevices(): void

停止发现设备。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2801000Operation failed.2801001Wi-Fi STA disabled.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  try {
    wifiManager.stopDiscoverDevices();
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### wifiManager.getMultiLinkedInfo18+

getMultiLinkedInfo(): Array<WifiLinkedInfo>

获取MLO(Multi-Link Operation，多链路操作)WLAN连接信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

- 当macType是1（设备MAC地址），获取macAddress还需申请ohos.permission.GET_WIFI_LOCAL_MAC权限（该权限仅系统应用可申请），无该权限时，macAddress返回为空。
- 如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限，则返回结果中的bssid为真实BSSID地址，否则为随机设备地址。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明 Array<[WifiLinkedInfo](#ZH-CN_TOPIC_0000002497445446__wifilinkedinfo)>Wi-Fi连接信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2501000Operation failed.2501001Wi-Fi STA disabled.

**示例：**

```ets
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let linkedInfo = wifiManager.getMultiLinkedInfo();
    console.info("linkedInfo:" + JSON.stringify(linkedInfo));
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

#### WifiP2pGroupInfo

表示P2P群组相关信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称类型只读可选说明isP2pGoboolean否否是否是群主。true表示是群主，false表示不是群主。ownerInfo[WifiP2pDevice](#ZH-CN_TOPIC_0000002497445446__wifip2pdevice)否否群组的设备信息。passphrasestring否否群组密钥。interfacestring否否接口名称。groupNamestring否否群组名称。networkIdnumber否否网络ID。frequencynumber否否群组的频率。clientDevices[WifiP2pDevice[]](#ZH-CN_TOPIC_0000002497445446__wifip2pdevice)否否接入的设备列表信息。goIpAddressstring否否群组IP地址。

#### wifiManager.on('wifiStateChange')

on(type: 'wifiStateChange', callback: Callback<number>): void

注册WLAN状态改变事件，在业务退出时，要调用off(type: 'wifiStateChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiStateChange"字符串。callbackCallback<number>是状态改变回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2501000Operation failed.

**状态改变事件的枚举：**

枚举值说明0未激活。1已激活。2激活中。3去激活中。

#### wifiManager.off('wifiStateChange')

off(type: 'wifiStateChange', callback?: Callback<number>): void

取消注册WLAN状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiStateChange"字符串。callbackCallback<number>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  let recvPowerNotifyFunc = (result:number) => {
      console.info("Receive power state change event: " + result);
  }

  // Register event
  wifiManager.on("wifiStateChange", recvPowerNotifyFunc);

  // Unregister event
  wifiManager.off("wifiStateChange", recvPowerNotifyFunc);
```

#### wifiManager.on('wifiConnectionChange')

on(type: 'wifiConnectionChange', callback: Callback<number>): void

注册WLAN连接状态改变事件，在业务退出时，要调用off(type: 'wifiConnectionChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiConnectionChange"字符串。callbackCallback<number>是状态改变回调函数。

**连接状态改变事件的枚举：**

枚举值说明0已断开。1已连接。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2501000Operation failed.

#### wifiManager.off('wifiConnectionChange')

off(type: 'wifiConnectionChange', callback?: Callback<number>): void

取消注册WLAN连接状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiConnectionChange"字符串。callbackCallback<number>否连接状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  let recvWifiConnectionChangeFunc = (result:number) => {
      console.info("Receive wifi connection change event: " + result);
  }

  // Register event
  wifiManager.on("wifiConnectionChange", recvWifiConnectionChangeFunc);

  // Unregister event
  wifiManager.off("wifiConnectionChange", recvWifiConnectionChangeFunc);
```

#### wifiManager.on('wifiScanStateChange')

on(type: 'wifiScanStateChange', callback: Callback<number>): void

注册扫描状态改变事件，在业务退出时，要调用off(type: 'wifiScanStateChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiScanStateChange"字符串。callbackCallback<number>是状态改变回调函数。

**扫描状态改变事件的枚举：**

枚举值说明0扫描失败。1扫描成功。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2501000Operation failed.

#### wifiManager.off('wifiScanStateChange')

off(type: 'wifiScanStateChange', callback?: Callback<number>): void

取消注册扫描状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiScanStateChange"字符串。callbackCallback<number>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  let recvWifiScanStateChangeFunc = (result:number) => {
      console.info("Receive Wifi scan state change event: " + result);
  }

  // Register event
  wifiManager.on("wifiScanStateChange", recvWifiScanStateChangeFunc);

  // Unregister event
  wifiManager.off("wifiScanStateChange", recvWifiScanStateChangeFunc);
```

#### wifiManager.on('wifiRssiChange')

on(type: 'wifiRssiChange', callback: Callback<number>): void

注册WLAN接收信号强度(RSSI)变化事件，在业务退出时，要调用off(type: 'wifiRssiChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiRssiChange"字符串。callbackCallback<number>是状态改变回调函数，返回以dBm为单位的RSSI值。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2501000Operation failed.

#### wifiManager.off('wifiRssiChange')

off(type: 'wifiRssiChange', callback?: Callback<number>): void

取消注册WLAN接收信号强度(RSSI)变化事件。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiRssiChange"字符串。callbackCallback<number>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2501000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  let recvWifiRssiChangeFunc = (result:number) => {
      console.info("Receive wifi rssi change event: " + result);
  }

  // Register event
  wifiManager.on("wifiRssiChange", recvWifiRssiChangeFunc);

  // Unregister event
  wifiManager.off("wifiRssiChange", recvWifiRssiChangeFunc);
```

#### wifiManager.on('hotspotStateChange')

on(type: 'hotspotStateChange', callback: Callback<number>): void

注册热点状态改变事件，在业务退出时，要调用off(type: 'hotspotStateChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**参数：**

参数名类型必填说明typestring是固定填"hotspotStateChange"字符串。callbackCallback<number>是状态改变回调函数。

**热点状态改变事件的枚举：**

枚举值说明0未激活。1已激活。2激活中。3去激活中。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2601000Operation failed.

#### wifiManager.off('hotspotStateChange')

off(type: 'hotspotStateChange', callback?: Callback<number>): void

取消注册热点状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**参数：**

参数名类型必填说明typestring是固定填"hotspotStateChange"字符串。callbackCallback<number>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2601000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  let recvHotspotStateChangeFunc = (result:number) => {
      console.info("Receive hotspot state change event: " + result);
  }

  // Register event
  wifiManager.on("hotspotStateChange", recvHotspotStateChangeFunc);

  // Unregister event
  wifiManager.off("hotspotStateChange", recvHotspotStateChangeFunc);
```

#### wifiManager.on('p2pStateChange')

on(type: 'p2pStateChange', callback: Callback<number>): void

注册P2P开关状态改变事件，在业务退出时，要调用off(type: 'p2pStateChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pStateChange"字符串。callbackCallback<number>是状态改变回调函数。

**P2P状态改变事件的枚举：**

枚举值说明1空闲。2打开中。3已打开。4关闭中。5已关闭。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2801000Operation failed.

#### wifiManager.off('p2pStateChange')

off(type: 'p2pStateChange', callback?: Callback<number>): void

取消注册P2P开关状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pStateChange"字符串。callbackCallback<number>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2801000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  let recvP2pStateChangeFunc = (result:number) => {
      console.info("Receive p2p state change event: " + result);
  }

  // Register event
  wifiManager.on("p2pStateChange", recvP2pStateChangeFunc);

  // Unregister event
  wifiManager.off("p2pStateChange", recvP2pStateChangeFunc);
```

#### wifiManager.on('p2pConnectionChange')

on(type: 'p2pConnectionChange', callback: Callback<WifiP2pLinkedInfo>): void

注册P2P连接状态改变事件，在业务退出时，要调用off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pConnectionChange"字符串。callbackCallback<[WifiP2pLinkedInfo](#ZH-CN_TOPIC_0000002497445446__wifip2plinkedinfo)>是状态改变回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2801000Operation failed.

#### wifiManager.off('p2pConnectionChange')

off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>): void

取消注册P2P连接状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pConnectionChange"字符串。callbackCallback<[WifiP2pLinkedInfo](#ZH-CN_TOPIC_0000002497445446__wifip2plinkedinfo)>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2801000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  let recvP2pConnectionChangeFunc = (result:wifiManager.WifiP2pLinkedInfo) => {
      console.info("Receive p2p connection change event: " + result);
  }

  // Register event
  wifiManager.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

  // Unregister event
  wifiManager.off("p2pConnectionChange", recvP2pConnectionChangeFunc);
```

#### wifiManager.on('p2pDeviceChange')

on(type: 'p2pDeviceChange', callback: Callback<WifiP2pDevice>): void

注册P2P设备状态改变事件，在业务退出时，要调用off(type: 'p2pDeviceChange', callback?: Callback<WifiP2pDevice>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：**

API 10起：ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pDeviceChange"字符串。callbackCallback<[WifiP2pDevice](#ZH-CN_TOPIC_0000002497445446__wifip2pdevice)>是状态改变回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2801000Operation failed.

#### wifiManager.off('p2pDeviceChange')

off(type: 'p2pDeviceChange', callback?: Callback<WifiP2pDevice>): void

取消注册P2P设备状态改变事件。使用callback异步回调。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pDeviceChange"字符串。callbackCallback<[WifiP2pDevice](#ZH-CN_TOPIC_0000002497445446__wifip2pdevice)>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2801000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  let recvP2pDeviceChangeFunc = (result:wifiManager.WifiP2pDevice) => {
      console.info("Receive p2p device change event: " + result);
  }

  // Register event
  wifiManager.on("p2pDeviceChange", recvP2pDeviceChangeFunc);

  // Unregister event
  wifiManager.off("p2pDeviceChange", recvP2pDeviceChangeFunc);
```

#### wifiManager.on('p2pPeerDeviceChange')

on(type: 'p2pPeerDeviceChange', callback: Callback<WifiP2pDevice[]>): void

注册P2P对端设备状态改变事件，在业务退出时，要调用off(type: 'p2pPeerDeviceChange', callback?: Callback<WifiP2pDevice[]>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：**

API 10起：ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pPeerDeviceChange"字符串。callbackCallback<[WifiP2pDevice[]](#ZH-CN_TOPIC_0000002497445446__wifip2pdevice)>是状态改变回调函数。如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限，则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2801000Operation failed.

#### wifiManager.off('p2pPeerDeviceChange')

off(type: 'p2pPeerDeviceChange', callback?: Callback<WifiP2pDevice[]>): void

取消注册P2P对端设备状态改变事件。使用callback异步回调。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pPeerDeviceChange"字符串。callbackCallback<[WifiP2pDevice[]](#ZH-CN_TOPIC_0000002497445446__wifip2pdevice)>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限，则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息20110+Permission denied.401Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2801000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  let recvP2pPeerDeviceChangeFunc = (result:wifiManager.WifiP2pDevice[]) => {
      console.info("Receive p2p peer device change event: " + result);
  }

  // Register event
  wifiManager.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

  // Unregister event
  wifiManager.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);
```

#### wifiManager.on('p2pPersistentGroupChange')

on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void

注册P2P永久组状态改变事件，在业务退出时，要调用off(type: 'p2pPersistentGroupChange', callback?: Callback<void>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pPersistentGroupChange"字符串。callbackCallback<void>是状态改变回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2801000Operation failed.

#### wifiManager.off('p2pPersistentGroupChange')

off(type: 'p2pPersistentGroupChange', callback?: Callback<void>): void

取消注册P2P永久组状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pPersistentGroupChange"字符串。callbackCallback<void>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2801000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  let recvP2pPersistentGroupChangeFunc = (result:void) => {
      console.info("Receive p2p persistent group change event: " + result);
  }

  // Register event
  wifiManager.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

  // Unregister event
  wifiManager.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);
```

#### wifiManager.on('p2pDiscoveryChange')

on(type: 'p2pDiscoveryChange', callback: Callback<number>): void

注册发现设备状态改变事件，在业务退出时，要调用off(type: 'p2pDiscoveryChange', callback?: Callback<number>)接口去掉之前的注册回调。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pDiscoveryChange"字符串。callbackCallback<number>是状态改变回调函数。

**发现设备状态改变事件的枚举：**

枚举值说明0初始状态。1发现成功。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2801000Operation failed.

#### wifiManager.off('p2pDiscoveryChange')

off(type: 'p2pDiscoveryChange', callback?: Callback<number>): void

取消注册发现设备状态改变事件。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pDiscoveryChange"字符串。callbackCallback<number>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](../../errors/WIFI错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.2801000Operation failed.

**示例：**

```ets
  import { wifiManager } from '@kit.ConnectivityKit';

  let recvP2pDiscoveryChangeFunc = (result:number) => {
      console.info("Receive p2p discovery change event: " + result);
  }

  // Register event
  wifiManager.on("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);

  // Unregister event
  wifiManager.off("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);
```