# @ohos.wifi (WLAN)

该模块主要提供WLAN基础功能、P2P（peer-to-peer）功能和WLAN消息通知的相应服务，让应用可以通过WLAN和其他设备互联互通。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 9 开始，该接口不再维护，推荐使用[@ohos.wifiManager (WLAN)](@ohos.wifiManager (WLAN).md)等相关接口。

#### 导入模块

```ets
import wifi from '@ohos.wifi';
```

#### wifi.isWifiActive

isWifiActive(): boolean

查询WLAN是否已使能。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明booleantrue:已使能， false:未使能。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    let isWifiActive = wifi.isWifiActive();
    console.info("isWifiActive:" + isWifiActive);
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.scan

scan(): boolean

启动WLAN扫描。

**需要权限：** ohos.permission.SET_WIFI_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明booleantrue:扫描操作执行成功， false:扫描操作执行失败。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    wifi.scan();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.getScanInfos

getScanInfos(): Promise<Array<WifiScanInfo>>

获取扫描结果，使用Promise异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 (ohos.permission.GET_WIFI_PEERS_MAC 或 ohos.permission.LOCATION)

ohos.permission.GET_WIFI_PEERS_MAC权限仅系统应用可申请。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明Promise< Array<[WifiScanInfo](#ZH-CN_TOPIC_0000002497445456__wifiscaninfo)> >Promise对象。返回扫描到的热点列表。

#### wifi.getScanInfos

getScanInfos(callback: AsyncCallback<Array<WifiScanInfo>>): void

获取扫描结果，使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 (ohos.permission.GET_WIFI_PEERS_MAC 或 ohos.permission.LOCATION)

ohos.permission.GET_WIFI_PEERS_MAC权限仅系统应用可申请。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明callbackAsyncCallback< Array<[WifiScanInfo](#ZH-CN_TOPIC_0000002497445456__wifiscaninfo)>>是回调函数。当成功时，err为0，data为扫描到的热点；否则err为非0值，data为空。

**示例：**

```ets
import wifi from '@ohos.wifi';

wifi.getScanInfos().then(result => {
    let len = result.length;
    console.log("wifi received scan info: " + len);
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
```

#### WifiScanInfo

WLAN热点信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称类型只读可选说明ssidstring否否热点的SSID，最大长度为32字节，编码格式为UTF-8。bssidstring否否热点的BSSID，例如：00:11:22:33:44:55。capabilitiesstring否否热点能力。securityType[WifiSecurityType](#ZH-CN_TOPIC_0000002497445456__wifisecuritytype)否否WLAN加密类型。rssinumber否否热点的信号强度(dBm)。bandnumber否否WLAN接入点的频段。1表示2.4GHZ；2表示5GHZ。frequencynumber否否WLAN接入点的频率。channelWidthnumber否否WLAN接入点的带宽。timestampnumber否否时间戳。

#### WifiSecurityType

表示加密类型的枚举。

**系统能力：** SystemCapability.Communication.WiFi.Core

名称值说明WIFI_SEC_TYPE_INVALID0无效加密类型。WIFI_SEC_TYPE_OPEN1开放加密类型。WIFI_SEC_TYPE_WEP2Wired Equivalent Privacy (WEP)加密类型。WIFI_SEC_TYPE_PSK3Pre-shared key (PSK)加密类型。WIFI_SEC_TYPE_SAE4Simultaneous Authentication of Equals (SAE)加密类型。

#### WifiDeviceConfig

WLAN配置信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称类型只读可选说明ssidstring否否热点的SSID，最大长度为32字节，编码格式为UTF-8。bssidstring否否热点的BSSID，例如：00:11:22:33:44:55。preSharedKeystring否否热点的密钥，最大长度为64字节。isHiddenSsidboolean否否是否是隐藏网络。true:是隐藏网络，false:不是隐藏网络。securityType[WifiSecurityType](#ZH-CN_TOPIC_0000002497445456__wifisecuritytype)否否加密类型。

#### wifi.addUntrustedConfig7+

addUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>

添加不可信网络配置，使用Promise异步回调。

**需要权限：** ohos.permission.SET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明config[WifiDeviceConfig](#ZH-CN_TOPIC_0000002497445456__wifideviceconfig)是WLAN配置信息。

**返回值：**

类型说明Promise<boolean>Promise对象。表示操作结果，true: 成功， false: 失败。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "****",
        bssid:  "****",
        preSharedKey: "****",
        isHiddenSsid: false,
        securityType: 0,
        creatorUid: 0,
        disableReason: 0,
        netId: 0,
        randomMacType: 0,
        randomMacAddr:  "****",
        ipType: 0,
        staticIp: {
            ipAddress: 0,
            gateway: 0,
            dnsServers: [],
            domains: []
        }
    }
    wifi.addUntrustedConfig(config).then(result => {
        console.info("result:" + JSON.stringify(result));
    });
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.addUntrustedConfig7+

addUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void

添加不可信网络配置，使用callback异步回调。

**需要权限：** ohos.permission.SET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明config[WifiDeviceConfig](#ZH-CN_TOPIC_0000002497445456__wifideviceconfig)是WLAN配置信息。callbackAsyncCallback<boolean>是回调函数。当操作成功时，err为0，data表示操作结果，true: 成功， false: 失败。如果error为非0，表示处理出现错误。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "****",
        bssid:  "****",
        preSharedKey: "****",
        isHiddenSsid: false,
        securityType: 0,
        creatorUid: 0,
        disableReason: 0,
        netId: 0,
        randomMacType: 0,
        randomMacAddr:  "****",
        ipType: 0,
        staticIp: {
            ipAddress: 0,
            gateway: 0,
            dnsServers: [],
            domains: []
        }
    }
    wifi.addUntrustedConfig(config,(error,result) => {
        console.info("result:" + JSON.stringify(result));
    });
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.removeUntrustedConfig7+

removeUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>

移除不可信网络配置，使用Promise异步回调。

**需要权限：** ohos.permission.SET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明config[WifiDeviceConfig](#ZH-CN_TOPIC_0000002497445456__wifideviceconfig)是WLAN配置信息。

**返回值：**

类型说明Promise<boolean>Promise对象。表示操作结果，true: 成功， false: 失败。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "****",
        bssid:  "****",
        preSharedKey: "****",
        isHiddenSsid: false,
        securityType: 0,
        creatorUid: 0,
        disableReason: 0,
        netId: 0,
        randomMacType: 0,
        randomMacAddr:  "****",
        ipType: 0,
        staticIp: {
            ipAddress: 0,
            gateway: 0,
            dnsServers: [],
            domains: []
        }
    }
    wifi.removeUntrustedConfig(config).then(result => {
        console.info("result:" + JSON.stringify(result));
    });
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.removeUntrustedConfig7+

removeUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void

移除不可信网络配置，使用callback异步回调。

**需要权限：** ohos.permission.SET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明config[WifiDeviceConfig](#ZH-CN_TOPIC_0000002497445456__wifideviceconfig)是WLAN配置信息。callbackAsyncCallback<boolean>是回调函数。当操作成功时，err为0，data表示操作结果，true: 成功， false: 失败。如果error为非0，表示处理出现错误。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "****",
        bssid:  "****",
        preSharedKey: "****",
        isHiddenSsid: false,
        securityType: 0,
        creatorUid: 0,
        disableReason: 0,
        netId: 0,
        randomMacType: 0,
        randomMacAddr:  "****",
        ipType: 0,
        staticIp: {
            ipAddress: 0,
            gateway: 0,
            dnsServers: [],
            domains: []
        }
    }
    wifi.removeUntrustedConfig(config,(error,result) => {
    console.info("result:" + JSON.stringify(result));
    });
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.getSignalLevel

getSignalLevel(rssi: number, band: number): number

查询WLAN信号强度。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明rssinumber是热点的信号强度(dBm)。bandnumber是WLAN接入点的频段。

**返回值：**

类型说明number信号强度，取值范围为[0, 4]。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    let rssi = 0;
    let band = 0;
    let level = wifi.getSignalLevel(rssi,band);
    console.info("level:" + JSON.stringify(level));
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.getLinkedInfo

getLinkedInfo(): Promise<WifiLinkedInfo>

获取WLAN连接信息。使用Promise异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明Promise<[WifiLinkedInfo](#ZH-CN_TOPIC_0000002497445456__wifilinkedinfo)>Promise对象。表示WLAN连接信息。

#### wifi.getLinkedInfo

getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void

获取WLAN连接信息。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明callbackAsyncCallback<[WifiLinkedInfo](#ZH-CN_TOPIC_0000002497445456__wifilinkedinfo)>是回调函数。当获取成功时，err为0，data表示WLAN连接信息。如果error为非0，表示处理出现错误。

**示例：**

```ets
import wifi from '@ohos.wifi';

wifi.getLinkedInfo((err, data:wifi.WifiLinkedInfo) => {
    if (err) {
        console.error("get linked info error");
        return;
    }
    console.info("get wifi linked info: " + JSON.stringify(data));
});

wifi.getLinkedInfo().then(data => {
    console.info("get wifi linked info: " + JSON.stringify(data));
}).catch((error:number) => {
    console.info("get linked info error");
});
```

#### WifiLinkedInfo

提供WLAN连接的相关信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称类型只读可选说明ssidstring否否热点的SSID，最大长度为32字节，编码格式为UTF-8。bssidstring否否热点的BSSID，例如：00:11:22:33:44:55。rssinumber否否热点的信号强度(dBm)。bandnumber否否WLAN接入点的频段。1表示2.4GHZ；2表示5GHZ。linkSpeednumber否否WLAN接入点的速度，单位Mbps。frequencynumber否否WLAN接入点的频率。isHiddenboolean否否WLAN接入点是否是隐藏网络。true:是隐藏网络，false:不是隐藏网络。isRestrictedboolean否否WLAN接入点是否限制数据量。true: 限制，false:不限制。macAddressstring否否设备的MAC地址。ipAddressnumber否否WLAN连接的IP地址。connState[ConnState](#ZH-CN_TOPIC_0000002497445456__connstate)否否WLAN连接状态。

#### ConnState

表示WLAN连接状态的枚举。

**系统能力：** SystemCapability.Communication.WiFi.STA

名称值说明SCANNING0设备正在搜索可用的AP。CONNECTING1正在建立WLAN连接。AUTHENTICATING2WLAN连接正在认证中。OBTAINING_IPADDR3正在获取WLAN连接的IP地址。CONNECTED4WLAN连接已建立。DISCONNECTING5WLAN连接正在断开。DISCONNECTED6WLAN连接已断开。UNKNOWN7WLAN连接建立失败。

#### wifi.isConnected7+

isConnected(): boolean

查询WLAN是否已连接。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明booleantrue:已连接， false:未连接。

#### wifi.isFeatureSupported7+

isFeatureSupported(featureId: number): boolean

判断设备是否支持相关WLAN特性。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.Core

**参数：**

参数名类型必填说明featureIdnumber是特性ID值。

**返回值：**

类型说明booleantrue:支持， false:不支持。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    let featureId = 0;
    let ret = wifi.isFeatureSupported(featureId);
    console.info("isFeatureSupported:" + ret);
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.getIpInfo7+

getIpInfo(): IpInfo

获取IP信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

类型说明[IpInfo](#ZH-CN_TOPIC_0000002497445456__ipinfo7)IP信息。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    let info = wifi.getIpInfo();
    console.info("info:" + JSON.stringify(info));
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### IpInfo7+

IP信息。

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

名称类型只读可选说明ipAddressnumber否否IP地址。gatewaynumber否否网关。netmasknumber否否掩码。primaryDnsnumber否否主DNS服务器IP地址。secondDnsnumber否否备DNS服务器IP地址。serverIpnumber否否DHCP服务端IP地址。leaseDurationnumber否否IP地址租用时长。

#### wifi.getCountryCode7+

getCountryCode(): string

获取国家码信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.Core

**返回值：**

类型说明string国家码。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    let code = wifi.getCountryCode();
    console.info("code:" + code);
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.getP2pLinkedInfo8+

getP2pLinkedInfo(): Promise<WifiP2pLinkedInfo>

获取P2P连接信息。使用Promise异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

类型说明Promise<[WifiP2pLinkedInfo](#ZH-CN_TOPIC_0000002497445456__wifip2plinkedinfo8)>Promise对象。表示P2P连接信息。

#### WifiP2pLinkedInfo8+

提供WLAN连接的相关信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称类型只读可选说明connectState[P2pConnectState](#ZH-CN_TOPIC_0000002497445456__p2pconnectstate8)否否P2P连接状态。isGroupOwnerboolean否否是否是群主。true:是群主，false:不是群主。groupOwnerAddrstring否否群组MAC地址。

#### P2pConnectState8+

表示P2P连接状态的枚举。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称值说明DISCONNECTED0断开状态。CONNECTED1连接状态。

#### wifi.getP2pLinkedInfo8+

getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void

获取P2P连接信息。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明callbackAsyncCallback<[WifiP2pLinkedInfo](#ZH-CN_TOPIC_0000002497445456__wifip2plinkedinfo8)>是回调函数。当操作成功时，err为0，data表示P2P连接信息。如果error为非0，表示处理出现错误。

**示例：**

```ets
import wifi from '@ohos.wifi';

wifi.getP2pLinkedInfo((err, data:wifi.WifiP2pLinkedInfo) => {
   if (err) {
       console.error("get p2p linked info error");
       return;
   }
    console.info("get wifi p2p linked info: " + JSON.stringify(data));
});

wifi.getP2pLinkedInfo().then(data => {
    console.info("get wifi p2p linked info: " + JSON.stringify(data));
});
```

#### wifi.getCurrentGroup8+

getCurrentGroup(): Promise<WifiP2pGroupInfo>

获取P2P当前组信息。使用Promise异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

类型说明Promise<[WifiP2pGroupInfo](#ZH-CN_TOPIC_0000002497445456__wifip2pgroupinfo8)>Promise对象。表示当前组信息。

#### wifi.getCurrentGroup8+

getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void

获取P2P当前组信息。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明callbackAsyncCallback<[WifiP2pGroupInfo](#ZH-CN_TOPIC_0000002497445456__wifip2pgroupinfo8)>是回调函数。当操作成功时，err为0，data表示当前组信息。如果error为非0，表示处理出现错误。

**示例：**

```ets
import wifi from '@ohos.wifi';

wifi.getCurrentGroup((err, data:wifi.WifiP2pGroupInfo) => {
   if (err) {
       console.error("get current P2P group error");
       return;
   }
    console.info("get current P2P group: " + JSON.stringify(data));
});

wifi.getCurrentGroup().then(data => {
    console.info("get current P2P group: " + JSON.stringify(data));
});
```

#### wifi.getP2pPeerDevices8+

getP2pPeerDevices(): Promise<WifiP2pDevice[]>

获取P2P对端设备列表信息。使用Promise异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

类型说明Promise<[WifiP2pDevice[]](#ZH-CN_TOPIC_0000002497445456__wifip2pdevice8)>Promise对象。表示对端设备列表信息。

#### wifi.getP2pPeerDevices8+

getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void

获取P2P对端设备列表信息。使用callback异步回调。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明callbackAsyncCallback<[WifiP2pDevice[]](#ZH-CN_TOPIC_0000002497445456__wifip2pdevice8)>是回调函数。当操作成功时，err为0，data表示对端设备列表信息。如果error为非0，表示处理出现错误。

**示例：**

```ets
import wifi from '@ohos.wifi';

wifi.getP2pPeerDevices((err, data:wifi.WifiP2pDevice) => {
   if (err) {
       console.error("get P2P peer devices error");
       return;
   }
    console.info("get P2P peer devices: " + JSON.stringify(data));
});

wifi.getP2pPeerDevices().then(data => {
    console.info("get P2P peer devices: " + JSON.stringify(data));
});
```

#### WifiP2pDevice8+

表示P2P设备信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称类型只读可选说明deviceNamestring否否设备名称。deviceAddressstring否否设备MAC地址。primaryDeviceTypestring否否主设备类型。deviceStatus[P2pDeviceStatus](#ZH-CN_TOPIC_0000002497445456__p2pdevicestatus8)否否设备状态。groupCapabilitysnumber否否群组能力。

#### P2pDeviceStatus8+

表示设备状态的枚举。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称值说明CONNECTED0连接状态。INVITED1邀请状态。FAILED2失败状态。AVAILABLE3可用状态。UNAVAILABLE4不可用状态。

#### wifi.createGroup8+

createGroup(config: WifiP2PConfig): boolean

创建群组。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明config[WifiP2PConfig](#ZH-CN_TOPIC_0000002497445456__wifip2pconfig8)是群组配置信息。

**返回值：**

类型说明booleantrue:创建群组操作执行成功， false:创建群组操作执行失败。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiP2PConfig = {
        deviceAddress: "****",
        netId: 0,
        passphrase: "*****",
        groupName: "****",
        goBand: 0
    }
    wifi.createGroup(config);

}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### WifiP2PConfig8+

表示P2P配置信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称类型只读可选说明deviceAddressstring否否设备地址。netIdnumber否否网络ID。创建群组时-1表示创建临时组，-2表示创建永久组。passphrasestring否否群组密钥。groupNamestring否否群组名称。goBand[GroupOwnerBand](#ZH-CN_TOPIC_0000002497445456__groupownerband8)否否群组带宽。

#### GroupOwnerBand8+

表示群组带宽的枚举。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称值说明GO_BAND_AUTO0自动模式。GO_BAND_2GHZ12GHZ。GO_BAND_5GHZ25GHZ。

#### wifi.removeGroup8+

removeGroup(): boolean

移除群组。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

类型说明booleantrue:操作执行成功， false:操作执行失败。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    wifi.removeGroup();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.p2pConnect8+

p2pConnect(config: WifiP2PConfig): boolean

执行P2P连接。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明config[WifiP2PConfig](#ZH-CN_TOPIC_0000002497445456__wifip2pconfig8)是连接配置信息。

**返回值：**

类型说明booleantrue:操作执行成功， false:操作执行失败。

**示例：**

```ets
import wifi from '@ohos.wifi';

let recvP2pConnectionChangeFunc = (result:wifi.WifiP2pLinkedInfo) => {
    console.info("p2p connection change receive event: " + JSON.stringify(result));
    wifi.getP2pLinkedInfo((err, data:wifi.WifiP2pLinkedInfo) => {
        if (err) {
            console.error('failed to get getP2pLinkedInfo: ' + JSON.stringify(err));
            return;
        }
        console.info("get getP2pLinkedInfo: " + JSON.stringify(data));
    });
}
wifi.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

let recvP2pDeviceChangeFunc = (result:wifi.WifiP2pDevice) => {
    console.info("p2p device change receive event: " + JSON.stringify(result));
}
wifi.on("p2pDeviceChange", recvP2pDeviceChangeFunc);

let recvP2pPeerDeviceChangeFunc = (result:wifi.WifiP2pDevice[]) => {
    console.info("p2p peer device change receive event: " + JSON.stringify(result));
    wifi.getP2pPeerDevices((err, data:wifi.WifiP2pDevice[]) => {
        if (err) {
            console.error('failed to get peer devices: ' + JSON.stringify(err));
            return;
        }
        console.info("get peer devices: " + JSON.stringify(data));
        let len = data.length;
        for (let i = 0; i < len; ++i) {
            if (data[i].deviceName === "my_test_device") {
                console.info("p2p connect to test device: " + data[i].deviceAddress);
                let config:wifi.WifiP2PConfig = {
                    deviceAddress:data[i].deviceAddress,
                    netId:-2,
                    passphrase:"",
                    groupName:"",
                    goBand:0,
                }
                wifi.p2pConnect(config);
            }
        }
    });
}
wifi.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

let recvP2pPersistentGroupChangeFunc = () => {
    console.info("p2p persistent group change receive event");

    wifi.getCurrentGroup((err, data:wifi.WifiP2pGroupInfo) => {
        if (err) {
            console.error('failed to get current group: ' + JSON.stringify(err));
            return;
        }
        console.info("get current group: " + JSON.stringify(data));
    });
}
wifi.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

setTimeout(() => {wifi.off("p2pConnectionChange", recvP2pConnectionChangeFunc);}, 125 * 1000);
setTimeout(() => {wifi.off("p2pDeviceChange", recvP2pDeviceChangeFunc);}, 125 * 1000);
setTimeout(() => {wifi.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);}, 125 * 1000);
setTimeout(() => {wifi.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);}, 125 * 1000);
console.info("start discover devices -> " + wifi.startDiscoverDevices());
```

#### wifi.p2pCancelConnect8+

p2pCancelConnect(): boolean

取消P2P连接。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

类型说明booleantrue:操作执行成功， false:操作执行失败。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    wifi.p2pCancelConnect();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.startDiscoverDevices8+

startDiscoverDevices(): boolean

开始发现设备。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

类型说明booleantrue:操作执行成功， false:操作执行失败。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    wifi.startDiscoverDevices();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.stopDiscoverDevices8+

stopDiscoverDevices(): boolean

停止发现设备。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

类型说明booleantrue:操作执行成功 false:操作执行失败。

**示例：**

```ets
import wifi from '@ohos.wifi';

try {
    wifi.stopDiscoverDevices();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### WifiP2pGroupInfo8+

表示P2P群组相关信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

名称类型只读可选说明isP2pGoboolean否否是否是群主。true:是群主，false:不是群主。ownerInfo[WifiP2pDevice](#ZH-CN_TOPIC_0000002497445456__wifip2pdevice8)否否群组的设备信息。passphrasestring否否群组密钥。interfacestring否否接口名称。groupNamestring否否群组名称。networkIdnumber否否网络ID。frequencynumber否否群组的频率。clientDevices[WifiP2pDevice[]](#ZH-CN_TOPIC_0000002497445456__wifip2pdevice8)否否接入的设备列表信息。goIpAddressstring否否群组IP地址。

#### wifi.on('wifiStateChange')7+

on(type: 'wifiStateChange', callback: Callback<number>): void

注册WLAN状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiStateChange"字符串。callbackCallback<number>是状态改变回调函数。

**状态改变事件的枚举：**

枚举值说明0未激活。1已激活。2激活中。3去激活中。

#### wifi.off('wifiStateChange')7+

off(type: 'wifiStateChange', callback?: Callback<number>): void

取消注册WLAN状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiStateChange"字符串。callbackCallback<number>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**示例：**

```ets
import wifi from '@ohos.wifi';

let recvPowerNotifyFunc = (result:number) => {
    console.info("Receive power state change event: " + result);
}

// Register event
wifi.on("wifiStateChange", recvPowerNotifyFunc);

// Unregister event
wifi.off("wifiStateChange", recvPowerNotifyFunc);
```

#### wifi.on('wifiConnectionChange')7+

on(type: 'wifiConnectionChange', callback: Callback<number>): void

注册WLAN连接状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiConnectionChange"字符串。callbackCallback<number>是状态改变回调函数。

**连接状态改变事件的枚举：**

枚举值说明0已断开。1已连接。

#### wifi.off('wifiConnectionChange')7+

off(type: 'wifiConnectionChange', callback?: Callback<number>): void

取消注册WLAN连接状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiConnectionChange"字符串。callbackCallback<number>否连接状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**示例：**

```ets
import wifi from '@ohos.wifi';

let recvWifiConnectionChangeFunc = (result:number) => {
    console.info("Receive wifi connection change event: " + result);
}

// Register event
wifi.on("wifiConnectionChange", recvWifiConnectionChangeFunc);

// Unregister event
wifi.off("wifiConnectionChange", recvWifiConnectionChangeFunc);
```

#### wifi.on('wifiScanStateChange')7+

on(type: 'wifiScanStateChange', callback: Callback<number>): void

注册扫描状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiScanStateChange"字符串。callbackCallback<number>是状态改变回调函数。

**扫描状态改变事件的枚举：**

枚举值说明0扫描失败。1扫描成功。

#### wifi.off('wifiScanStateChange')7+

off(type: 'wifiScanStateChange', callback?: Callback<number>): void

取消注册扫描状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiScanStateChange"字符串。callbackCallback<number>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**示例：**

```ets
import wifi from '@ohos.wifi';

let recvWifiScanStateChangeFunc = (result:number) => {
    console.info("Receive Wifi scan state change event: " + result);
}

// Register event
wifi.on("wifiScanStateChange", recvWifiScanStateChangeFunc);

// Unregister event
wifi.off("wifiScanStateChange", recvWifiScanStateChangeFunc);
```

#### wifi.on('wifiRssiChange')7+

on(type: 'wifiRssiChange', callback: Callback<number>): void

注册RSSI状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiRssiChange"字符串。callbackCallback<number>是状态改变回调函数，返回以dBm为单位的RSSI值。

#### wifi.off('wifiRssiChange')7+

off(type: 'wifiRssiChange', callback?: Callback<number>): void

取消注册RSSI状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

参数名类型必填说明typestring是固定填"wifiRssiChange"字符串。callbackCallback<number>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**示例：**

```ets
import wifi from '@ohos.wifi';

let recvWifiRssiChangeFunc = (result:number) => {
    console.info("Receive wifi rssi change event: " + result);
}

// Register event
wifi.on("wifiRssiChange", recvWifiRssiChangeFunc);

// Unregister event
wifi.off("wifiRssiChange", recvWifiRssiChangeFunc);
```

#### wifi.on('hotspotStateChange')7+

on(type: 'hotspotStateChange', callback: Callback<number>): void

注册热点状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**参数：**

参数名类型必填说明typestring是固定填"hotspotStateChange"字符串。callbackCallback<number>是状态改变回调函数。

**热点状态改变事件的枚举：**

枚举值说明0未激活。1已激活。2激活中。3去激活中。

**示例：**

```ets
import wifi from '@ohos.wifi';

let recvHotspotStateChangeFunc = (result:number) => {
    console.info("Receive hotspot state change event: " + result);
}

// Register event
wifi.on("hotspotStateChange", recvHotspotStateChangeFunc);

// Unregister event
wifi.off("hotspotStateChange", recvHotspotStateChangeFunc);
```

#### wifi.off('hotspotStateChange')7+

off(type: 'hotspotStateChange', callback?: Callback<number>): void

取消注册热点状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**参数：**

参数名类型必填说明typestring是固定填"hotspotStateChange"字符串。callbackCallback<number>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

#### wifi.on('p2pStateChange')8+

on(type: 'p2pStateChange', callback: Callback<number>): void

注册P2P开关状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pStateChange"字符串。callbackCallback<number>是状态改变回调函数。

**P2P状态改变事件的枚举：**

枚举值说明1空闲。2打开中。3已打开。4关闭中。5已关闭。

#### wifi.off('p2pStateChange')8+

off(type: 'p2pStateChange', callback?: Callback<number>): void

取消注册P2P开关状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pStateChange"字符串。callbackCallback<number>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**示例：**

```ets
import wifi from '@ohos.wifi';

let recvP2pStateChangeFunc = (result:number) => {
    console.info("Receive p2p state change event: " + result);
}

// Register event
wifi.on("p2pStateChange", recvP2pStateChangeFunc);

// Unregister event
wifi.off("p2pStateChange", recvP2pStateChangeFunc);
```

#### wifi.on('p2pConnectionChange')8+

on(type: 'p2pConnectionChange', callback: Callback<WifiP2pLinkedInfo>): void

注册P2P连接状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pConnectionChange"字符串。callbackCallback<[WifiP2pLinkedInfo](#ZH-CN_TOPIC_0000002497445456__wifip2plinkedinfo8)>是状态改变回调函数。

#### wifi.off('p2pConnectionChange')8+

off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>): void

取消注册P2P连接状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pConnectionChange"字符串。callbackCallback<[WifiP2pLinkedInfo](#ZH-CN_TOPIC_0000002497445456__wifip2plinkedinfo8)>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**示例：**

```ets
import wifi from '@ohos.wifi';

let recvP2pConnectionChangeFunc = (result:wifi.WifiP2pLinkedInfo) => {
    console.info("Receive p2p connection change event: " + result);
}

// Register event
wifi.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

// Unregister event
wifi.off("p2pConnectionChange", recvP2pConnectionChangeFunc);
```

#### wifi.on('p2pDeviceChange')8+

on(type: 'p2pDeviceChange', callback: Callback<WifiP2pDevice>): void

注册P2P设备状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pDeviceChange"字符串。callbackCallback<[WifiP2pDevice](#ZH-CN_TOPIC_0000002497445456__wifip2pdevice8)>是状态改变回调函数。

#### wifi.off('p2pDeviceChange')8+

off(type: 'p2pDeviceChange', callback?: Callback<WifiP2pDevice>): void

取消注册P2P设备状态改变事件。

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pDeviceChange"字符串。callbackCallback<[WifiP2pDevice](#ZH-CN_TOPIC_0000002497445456__wifip2pdevice8)>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**示例：**

```ets
import wifi from '@ohos.wifi';

let recvP2pDeviceChangeFunc = (result:wifi.WifiP2pDevice) => {
    console.info("Receive p2p device change event: " + result);
}

// Register event
wifi.on("p2pDeviceChange", recvP2pDeviceChangeFunc);

// Unregister event
wifi.off("p2pDeviceChange", recvP2pDeviceChangeFunc);
```

#### wifi.on('p2pPeerDeviceChange')8+

on(type: 'p2pPeerDeviceChange', callback: Callback<WifiP2pDevice[]>): void

注册P2P对端设备状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pPeerDeviceChange"字符串。callbackCallback<[WifiP2pDevice[]](#ZH-CN_TOPIC_0000002497445456__wifip2pdevice8)>是状态改变回调函数。

#### wifi.off('p2pPeerDeviceChange')8+

off(type: 'p2pPeerDeviceChange', callback?: Callback<WifiP2pDevice[]>): void

取消注册P2P对端设备状态改变事件。

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pPeerDeviceChange"字符串。callbackCallback<[WifiP2pDevice[]](#ZH-CN_TOPIC_0000002497445456__wifip2pdevice8)>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**示例：**

```ets
import wifi from '@ohos.wifi';

let recvP2pPeerDeviceChangeFunc = (result:wifi.WifiP2pDevice[]) => {
    console.info("Receive p2p peer device change event: " + result);
}

// Register event
wifi.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

// Unregister event
wifi.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);
```

#### wifi.on('p2pPersistentGroupChange')8+

on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void

注册P2P永久组状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pPersistentGroupChange"字符串。callbackCallback<void>是状态改变回调函数。

#### wifi.off('p2pPersistentGroupChange')8+

off(type: 'p2pPersistentGroupChange', callback?: Callback<void>): void

取消注册P2P永久组状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pPersistentGroupChange"字符串。callbackCallback<void>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**示例：**

```ets
import wifi from '@ohos.wifi';

let recvP2pPersistentGroupChangeFunc = (result:void) => {
    console.info("Receive p2p persistent group change event: " + result);
}

// Register event
wifi.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

// Unregister event
wifi.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);
```

#### wifi.on('p2pDiscoveryChange')8+

on(type: 'p2pDiscoveryChange', callback: Callback<number>): void

注册发现设备状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pDiscoveryChange"字符串。callbackCallback<number>是状态改变回调函数。

**发现设备状态改变事件的枚举：**

枚举值说明0初始状态。1发现成功。

#### wifi.off('p2pDiscoveryChange')8+

off(type: 'p2pDiscoveryChange', callback?: Callback<number>): void

取消注册发现设备状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

参数名类型必填说明typestring是固定填"p2pDiscoveryChange"字符串。callbackCallback<number>否状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。

**示例：**

```ets
import wifi from '@ohos.wifi';

let recvP2pDiscoveryChangeFunc = (result:number) => {
    console.info("Receive p2p discovery change event: " + result);
}

// Register event
wifi.on("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);

// Unregister event
wifi.off("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);
```