# @ohos.net.ethernet (以太网连接管理)

本模块提供以太网连接管理能力，包括有线网络能力、获取有线网络的IP地址等信息。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { ethernet } from '@kit.NetworkKit';
```

#### HttpProxy10+

type HttpProxy = connection.HttpProxy

网络代理配置信息。

**系统能力**：SystemCapability.Communication.NetManager.Ethernet

| 类型 | 说明 |
| --- | --- |
| connection.HttpProxy | 网络代理配置信息。 |

#### ethernet.getMacAddress14+

getMacAddress(): Promise<Array<MacAddressInfo>>

获取所有以太网网卡名称及对应网卡的MAC地址信息，使用Promise方式作为异步方法。

**需要权限**：ohos.permission.GET_ETHERNET_LOCAL_MAC

**系统能力**：SystemCapability.Communication.NetManager.Ethernet

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<MacAddressInfo>> | 以Promise形式返回接口信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2200002 | Operation failed. Cannot connect to service. |
| 2201005 | Device information does not exist. |

**示例：**

```ets
import { ethernet } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

ethernet.getMacAddress().then((data: Array<ethernet.MacAddressInfo>) => {
  console.info("getMacAddress promise data = " + JSON.stringify(data));
}).catch((error: BusinessError) => {
  console.error("getMacAddress promise error = " + JSON.stringify(error));
});
```

#### MacAddressInfo14+

以太网网卡名称及MAC地址信息。

**系统能力**：SystemCapability.Communication.NetManager.Ethernet

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iface | string | 否 | 否 | 以太网网卡名称。 |
| macAddress | string | 否 | 否 | 以太网网卡MAC地址信息。 |