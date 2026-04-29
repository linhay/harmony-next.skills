# @ohos.net.connection (网络连接管理)

网络连接管理提供管理网络一些基础能力，包括获取默认激活的网络、获取所有激活网络列表、获取网络能力信息等功能。


本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

无特殊说明，接口默认不支持并发。

#### 导入模块

```ets
import { connection } from '@kit.NetworkKit';
```

#### connection.createNetConnection

createNetConnection(netSpecifier?: NetSpecifier, timeout?: number): NetConnection

创建一个NetConnection对象，可用于监听网络状态。[netSpecifier](#ZH-CN_TOPIC_0000002553201441__netspecifier)表示需要监听网络的网络特征；timeout是超时时间（单位：毫秒)；netSpecifier是timeout的必要条件，两者都没有则表示关注默认网络。


若需要监听网络状态，创建一个NetConnection对象后，还需调用[register](#ZH-CN_TOPIC_0000002553201441__register)注册指定网络状态变化的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netSpecifier | NetSpecifier | 否 | 需要监听网络的网络特征，缺省则表示监听默认网络。 |
| timeout | number | 否 | 获取netSpecifier指定网络时的超时时间，传入值需为uint32_t范围内的整数，仅netSpecifier存在时生效，默认值为0。 说明：当监听网络不存在时，会尝试激活此网络。若超过设置的超时时间，且注册了网络状态监听，则会触发netUnavailable事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| NetConnection | 需要监听的网络连接对象的类型。 |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

// 示例1：仅关注默认网络, 无需指定netSpecifier参数，timeout参数未传入说明未使用超时时间，此时timeout为0。
let netConnection = connection.createNetConnection();

// 示例2：仅关注蜂窝网络，需要指定网络类型为蜂窝网络。
let timeout = 1000;
let netConnectionCellular = connection.createNetConnection({
  netCapabilities: {
    bearerTypes: [connection.NetBearType.BEARER_CELLULAR]
  }
}, timeout);

// 示例3：关注蜂窝或Wi-Fi网络，需要指定网络类型为蜂窝网络和Wi-Fi网络。
let netConnectionCellularAndWifi = connection.createNetConnection({
  netCapabilities: {
    bearerTypes: [connection.NetBearType.BEARER_CELLULAR,
      connection.NetBearType.BEARER_WIFI]
  }
});
```

#### connection.getDefaultNet

getDefaultNet(callback: AsyncCallback<NetHandle>): void

获取系统默认使用的网络句柄，包含网络ID。使用callback异步回调。


-

系统默认使用的网络，该网络的capabilities必须具备[NET_CAPABILITY_INTERNET](#ZH-CN_TOPIC_0000002553201441__netcap)且不是VPN类型的网络。

-

该接口的返回由系统决定，与应用是否指定网络无关。

-

一般情况下优先级为：以太网（PC）|蓝牙（手表）> WIFI > 蜂窝，特殊情况以实际返回结果为准。

-

[NetHandle](#ZH-CN_TOPIC_0000002553201441__nethandle)为网络唯一标识，当无网络可用时，返回0。其可用于[getNetCapabilities](#ZH-CN_TOPIC_0000002553201441__connectiongetnetcapabilities)继续查询更多网络信息。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<NetHandle> | 是 | 回调函数。当成功获取默认激活网络的网络句柄时，error为undefined，data为默认网络的网络句柄；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码]([网络连接管理错误码](../../errors/网络连接管理错误码.md).md)和[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet((error: BusinessError, data: connection.NetHandle) => {
  if (error) {
    console.error(`Failed to get default net. Code:${error.code}, message:${error.message}`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
});
```

#### connection.getDefaultNet

getDefaultNet(): Promise<NetHandle>

获取系统默认使用的网络句柄，包含网络ID。使用Promise异步回调。


-

系统默认使用的网络，该网络的capabilities必须具备[NET_CAPABILITY_INTERNET](#ZH-CN_TOPIC_0000002553201441__netcap)且不是VPN类型的网络。

-

该接口的返回由系统决定，与应用是否指定网络无关。

-

一般情况下，优先级：以太网（PC）|蓝牙（手表）> WIFI > 蜂窝，特殊情况以实际返回结果为准。

-

[NetHandle](#ZH-CN_TOPIC_0000002553201441__nethandle)为网络唯一标识，当无网络可用时，返回0。其可用于[getNetCapabilities](#ZH-CN_TOPIC_0000002553201441__connectiongetnetcapabilities)继续查询更多网络信息。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<NetHandle> | 以Promise形式返回默认网络的网络句柄。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((data: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});
```

#### connection.getDefaultNetSync9+

getDefaultNetSync(): NetHandle

获取系统默认使用的网络句柄，包含网络ID。使用同步方式返回。


-

系统默认使用的网络，该网络的capabilities必须具备[NET_CAPABILITY_INTERNET](#ZH-CN_TOPIC_0000002553201441__netcap)且不是VPN类型的网络。

-

该接口的返回由系统决定，与应用是否指定网络无关。

-

一般情况下，优先级：以太网（PC）|蓝牙（手表）> WIFI > 蜂窝，特殊情况以实际返回结果为准。

-

[NetHandle](#ZH-CN_TOPIC_0000002553201441__nethandle)为网络唯一标识，当无网络可用时，返回0。其可用于[getNetCapabilities](#ZH-CN_TOPIC_0000002553201441__connectiongetnetcapabilities)继续查询更多网络信息。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| NetHandle | 以同步方式返回默认网络的网络句柄。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

let netHandle = connection.getDefaultNetSync();
```

#### connection.setAppHttpProxy11+

setAppHttpProxy(httpProxy: HttpProxy): void

设置应用级Http代理配置信息。


若需使用本接口所配置的代理信息，则需在[HttpRequestOptions](@ohos.net.http (数据请求).md#ZH-CN_TOPIC_0000002553361401__httprequestoptions)字段中将usingProxy设置为true以启用代理转发。本接口仅负责配置代理规则，不校验代理服务的有效性。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| httpProxy | HttpProxy | 是 | 网络应用级Http代理配置信息。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid http proxy. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { http } from '@kit.NetworkKit';

let exclusionStr = "192.168,baidu.com";
let exclusionArray = exclusionStr.split(',');
connection.setAppHttpProxy({
  host: "192.168.xx.xxx",
  port: 8080,
  exclusionList: exclusionArray
} as connection.HttpProxy);
let httpRequest = http.createHttp();
let options: http.HttpRequestOptions = {
  usingProxy: true, // 选择使用网络代理，从API 10开始支持该属性。
};
// 发起一个HTTP请求。
httpRequest.request("EXAMPLE_URL", options, (err: Error, data: http.HttpResponse) => {
  if (!err) {
   console.info(`Result: ${data.result}`);
   console.info(`code: ${data.responseCode}`);
   console.info(`type: ${JSON.stringify(data.resultType)}`);
   console.info(`header: ${JSON.stringify(data.header)}`);
   console.info(`cookies: ${data.cookies}`); // 从API version 8开始支持cookie。
  } else {
   console.error(`error: ${JSON.stringify(err)}`);
  }
});
```

#### connection.getDefaultHttpProxy10+

getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void

获取网络的默认代理配置信息。使用callback异步回调。


- 如果设置了全局代理，则返回全局代理配置信息。

- 如果进程使用[setAppNet](#ZH-CN_TOPIC_0000002553201441__connectionsetappnet9)绑定到指定[NetHandle](#ZH-CN_TOPIC_0000002553201441__nethandle)对应的网络，则返回[NetHandle](#ZH-CN_TOPIC_0000002553201441__nethandle)对应网络的代理配置信息。在其它情况下，将返回默认网络的代理配置信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<HttpProxy> | 是 | 回调函数。当成功获取网络的默认代理配置信息时，error为undefined，data为网络的默认代理配置信息；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultHttpProxy((error: BusinessError, data: connection.HttpProxy) => {
  if (error) {
    console.error(`Failed to get default http proxy. Code:${error.code}, message:${error.message}`);
    return;
  }
  console.info("Succeeded to get data" + JSON.stringify(data));
});
```

#### connection.getDefaultHttpProxy10+

getDefaultHttpProxy(): Promise<HttpProxy>

获取网络默认的代理配置信息。使用Promise异步回调。


- 如果设置了全局代理，则返回全局代理配置信息。

- 如果进程使用[setAppNet](#ZH-CN_TOPIC_0000002553201441__connectionsetappnet9)绑定到指定[NetHandle](#ZH-CN_TOPIC_0000002553201441__nethandle)对应的网络，则返回[NetHandle](#ZH-CN_TOPIC_0000002553201441__nethandle)对应网络的代理配置信息。在其它情况下，将返回默认网络的代理配置信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<HttpProxy> | 以Promise形式返回网络默认的代理配置信息。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultHttpProxy().then((data: connection.HttpProxy) => {
  console.info(JSON.stringify(data));
}).catch((error: BusinessError) => {
  console.info(JSON.stringify(error));
});
```

#### connection.getAppNet9+

getAppNet(callback: AsyncCallback<NetHandle>): void

获取App绑定的网络句柄。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<NetHandle> | 是 | 回调函数。当成功获取App绑定的网络信息时，error为undefined，data为获取到App绑定的网络信息；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getAppNet((error: BusinessError, data: connection.NetHandle) => {
  if (error) {
    console.error(`Failed to get App net. Code:${error.code}, message:${error.message}`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
})
```

#### connection.getAppNet9+

getAppNet(): Promise<NetHandle>

获取App绑定的网络信息。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<NetHandle> | 以Promise形式返回App绑定的网络信息。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getAppNet().then((data: connection.NetHandle) => {
  console.info(JSON.stringify(data));
}).catch((error: BusinessError) => {
  console.info(JSON.stringify(error));
});
```

#### connection.getAppNetSync10+

getAppNetSync(): NetHandle

获取App绑定的网络信息。使用同步方式返回。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| NetHandle | 返回App绑定的数据网络。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

let netHandle = connection.getAppNetSync();
```

#### connection.setAppNet9+

setAppNet(netHandle: NetHandle, callback: AsyncCallback<void>): void

将App绑定到特定的网络，绑定后App只能通过netHandle对应的网络访问网络。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功绑定App到指定网络时，error为undefined，否则为错误对象。 |


如需解除App和指定网络的绑定关系，可以调用[setAppNet](#ZH-CN_TOPIC_0000002553201441__connectionsetappnet9)，并传入一个netId = 0的NetHandle对象，参考以下示例。

```ets
connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  netHandle.netId = 0;
  connection.setAppNet(netHandle, (error: BusinessError, data: void) => {
    if (error) {
      console.error(`Failed to get default net. Code:${error.code}, message:${error.message}`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
```

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet((error: BusinessError, netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  // 表示APP使用当前默认网络访问网络
  connection.setAppNet(netHandle, (error: BusinessError, data: void) => {
    if (error) {
      console.error(`Failed to get default net. Code:${error.code}, message:${error.message}`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
```

#### connection.setAppNet9+

setAppNet(netHandle: NetHandle): Promise<void>

将App异步绑定到特定的网络，绑定后App只能通过netHandle对应的网络访问网络。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄。 |


如需解除App和指定网络的绑定关系，可以调用[setAppNet](#ZH-CN_TOPIC_0000002553201441__connectionsetappnet9)，并传入一个netId = 0的NetHandle对象，参考以下示例。

```ets
connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  netHandle.netId = 0;
  connection.setAppNet(netHandle, (error: BusinessError, data: void) => {
    if (error) {
      console.error(`Failed to get default net. Code:${error.code}, message:${error.message}`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
```

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }

  connection.setAppNet(netHandle).then(() => {
    console.info("success");
  }).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  })
});
```

#### connection.getAllNets

getAllNets(callback: AsyncCallback<Array<NetHandle>>): void

获取所有处于连接状态的网络列表，使用callback异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<NetHandle>> | 是 | 回调函数。当成功获取所有处于连接状态的网络列表时，error为undefined，data为处于激活状态的网络列表；否则为错误对象。  说明： 在Wi-Fi和蜂窝数据开关均开启的情况下，若无应用指定使用蜂窝网络，则仅激活Wi-Fi网络，因此仅返回Wi-Fi的NetHandle。除非有特定应用启动蜂窝网络，才能同时获取Wi-Fi和蜂窝数据的NetHandle。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getAllNets((error: BusinessError, data: connection.NetHandle[]) => {
  if (error) {
    console.error(`Failed to get all nets. Code:${error.code}, message:${error.message}`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
});
```

#### connection.getAllNets

getAllNets(): Promise<Array<NetHandle>>

获取所有处于连接状态的网络列表。使用Promise异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<NetHandle>> | Promise对象，返回处于激活状态的网络列表。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

connection.getAllNets().then((data: connection.NetHandle[]) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});
```

#### connection.getAllNetsSync10+

getAllNetsSync(): Array<NetHandle>

获取所有处于连接状态的网络列表。使用同步方式返回。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<NetHandle> | 返回所有处于连接状态的网络列表。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

let netHandle = connection.getAllNetsSync();
```

#### connection.getConnectionProperties

getConnectionProperties(netHandle: NetHandle, callback: AsyncCallback<ConnectionProperties>): void

获取netHandle对应的网络的连接信息，包含网卡名称、域名、链路信息、路由信息、网络地址及最大传输单元。使用callback异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄。 |
| callback | AsyncCallback<ConnectionProperties> | 是 | 回调函数。当成功获取netHandle对应的网络的连接信息时，error为undefined，data为获取的网络连接信息；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 示例： 获取当前默认网络的连接信息。
connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  connection.getConnectionProperties(netHandle, (error: BusinessError, data: connection.ConnectionProperties) => {
    if (error) {
      console.error(`Failed to get connection properties. Code:${error.code}, message:${error.message}`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  })
});
```

#### connection.getConnectionProperties

getConnectionProperties(netHandle: NetHandle): Promise<ConnectionProperties>

获取netHandle对应的网络的连接信息，包含网卡名称、域名、链路信息、路由信息、网络地址及最大传输单元。使用Promise异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 数据网络的句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ConnectionProperties> | Promise对象，返回网络的连接信息。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }

  connection.getConnectionProperties(netHandle).then((data: connection.ConnectionProperties) => {
    console.info("Succeeded to get data: " + JSON.stringify(data));
  })
});
```

#### connection.getConnectionPropertiesSync10+

getConnectionPropertiesSync(netHandle: NetHandle): ConnectionProperties

获取netHandle对应的网络的连接信息，包含网卡名称、域名、链路信息、路由信息、网络地址及最大传输单元。使用同步方式返回。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ConnectionProperties | 返回网络的连接信息。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netHandle: connection.NetHandle;
let connectionproperties: connection.ConnectionProperties;

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  netHandle = connection.getDefaultNetSync();
  connectionproperties = connection.getConnectionPropertiesSync(netHandle);
  console.info("Succeeded to get connectionproperties: " + JSON.stringify(connectionproperties));
});
```

#### connection.getNetCapabilities

getNetCapabilities(netHandle: NetHandle, callback: AsyncCallback<NetCapabilities>): void

获取netHandle对应网络的能力集，包含上/下行带宽、网络具体能力、网络类型。使用callback异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络的句柄。 |
| callback | AsyncCallback<NetCapabilities> | 是 | 回调函数。当成功获取netHandle对应网络的能力集时，error为undefined，data为获取到的网络能力集；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
    if (error) {
      console.error(`Failed to get net capabilities. Code:${error.code}, message:${error.message}`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  })
}).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
});
```

#### connection.getNetCapabilities

getNetCapabilities(netHandle: NetHandle): Promise<NetCapabilities>

获取netHandle对应网络的能力集，包含上/下行带宽、网络具体能力、网络类型。使用Promise异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<NetCapabilities> | Promise对象，返回网络的能力集。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  connection.getNetCapabilities(netHandle).then((data: connection.NetCapabilities) => {
      console.info("Succeeded to get data: " + JSON.stringify(data));
  })
}).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
});
```

#### connection.getNetCapabilitiesSync10+

getNetCapabilitiesSync(netHandle: NetHandle): NetCapabilities

获取netHandle对应网络的能力信息，包含上/下行带宽、网络具体能力、网络类型。使用同步方式返回。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| NetCapabilities | 返回网络的能力集。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netHandle: connection.NetHandle;
let getNetCapabilitiesSync: connection.NetCapabilities;

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }

  getNetCapabilitiesSync = connection.getNetCapabilitiesSync(netHandle);
  console.info("Succeeded to get net capabilities sync: " + JSON.stringify(getNetCapabilitiesSync));
});
```

#### connection.isDefaultNetMetered9+

isDefaultNetMetered(callback: AsyncCallback<boolean>): void

检查当前默认网络上的数据流量使用是否被计费（例如：WiFi网络不会被计费，蜂窝网络会被计费）。使用callback异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回当前网络上的数据流量是否被计费。true表示会被计费，false表示不会被计费。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.isDefaultNetMetered((error: BusinessError, data: boolean) => {
  console.error(JSON.stringify(error));
  console.info('data: ' + data);
});
```

#### connection.isDefaultNetMetered9+

isDefaultNetMetered(): Promise<boolean>

检查当前默认网络上的数据流量使用是否被计费（例如：WiFi网络不会被计费，蜂窝网络会被计费）。使用Promise异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回当前网络上的数据流量是否被计费。true表示会被计费，false表示不会被计费。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

connection.isDefaultNetMetered().then((data: boolean) => {
  console.info('data: ' + data);
});
```

#### connection.isDefaultNetMeteredSync10+

isDefaultNetMeteredSync(): boolean

检查当前网络上的数据流量使用是否被计费（例如：WiFi网络不会被计费，蜂窝网络会被计费）。使用同步方式返回。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示当前网络上的数据流量是否被计费。true表示会被计费，false表示不会被计费。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

let isMetered = connection.isDefaultNetMeteredSync();
```

#### connection.hasDefaultNet

hasDefaultNet(callback: AsyncCallback<boolean>): void

获取当前是否有可用网络，使用callback异步回调。如果有可用网络，可以使用[getDefaultNet](#ZH-CN_TOPIC_0000002553201441__connectiongetdefaultnet)获取默认网络句柄。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回当前是否有可用网络。true表示当前有可用网络，false表示当前没有可用网络。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.hasDefaultNet((error: BusinessError, data: boolean) => {
  console.error(JSON.stringify(error));
  console.info('data: ' + data);
});
```

#### connection.hasDefaultNet

hasDefaultNet(): Promise<boolean>

获取当前是否有可用网络。使用Promise异步回调。如果有可用网络，可以使用[getDefaultNet](#ZH-CN_TOPIC_0000002553201441__connectiongetdefaultnet)获取默认网络句柄。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回当前是否有可用网络。true表示当前有可用网络，false表示当前没有可用网络。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

connection.hasDefaultNet().then((data: boolean) => {
  console.info('data: ' + data);
});
```

#### connection.hasDefaultNetSync10+

hasDefaultNetSync(): boolean

获取当前是否有可用网络。使用同步方式返回。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回当前是否有可用网络。true表示当前有可用网络，false表示当前没有可用网络。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

let hasDefaultNet = connection.hasDefaultNetSync();
```

#### connection.reportNetConnected

reportNetConnected(netHandle: NetHandle, callback: AsyncCallback<void>): void

向网络管理上报网络处于可用状态。使用callback方式异步回调。


该接口用于浏览器连接portal网络，网络认证成功后，向网络管理上报网络连接成功，网络管理会触发网络探测，更新网络状态。

**需要权限**：ohos.permission.GET_NETWORK_INFO 和 ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄，参考NetHandle。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当向网络管理报告网络处于可用状态成功，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  connection.reportNetConnected(netHandle, (error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
```

#### connection.reportNetConnected

reportNetConnected(netHandle: NetHandle): Promise<void>

向网络管理报告网络处于可用状态。使用Promise异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO 和 ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄，参考NetHandle。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  connection.reportNetConnected(netHandle).then(() => {
    console.info(`report success`);
  });
```

#### connection.reportNetDisconnected

reportNetDisconnected(netHandle: NetHandle, callback: AsyncCallback<void>): void

向网络管理上报网络处于不可用状态。使用callback异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO 和 ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄，参考NetHandle。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当向网络管理报告网络处于不可用状态成功时，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet((error: BusinessError, netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  connection.reportNetDisconnected(netHandle, (error: BusinessError, data: void) => {
    if (error) {
      console.error(`Failed to get default net. Code:${error.code}, message:${error.message}`);
      return;
    }
    console.info("report success");
  });
```

#### connection.reportNetDisconnected

reportNetDisconnected(netHandle: NetHandle): Promise<void>

向网络管理上报网络处于不可用状态。使用Promise异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO 和 ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回值的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  connection.reportNetDisconnected(netHandle).then( () => {
    console.info(`report success`);
  });
```

#### connection.getAddressesByName

getAddressesByName(host: string, callback: AsyncCallback<Array<NetAddress>>): void

使用当前默认网络解析主机名以获取所有IP地址。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。 |
| callback | AsyncCallback<Array<NetAddress>> | 是 | 回调函数。当使用默认网络解析主机名成功获取所有IP地址，error为undefined，data为获取到的所有IP地址；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getAddressesByName("xxxx", (error: BusinessError, data: connection.NetAddress[]) => {
  if (error) {
    console.error(`Failed to get addresses. Code:${error.code}, message:${error.message}`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
});
```

#### connection.getAddressesByName

getAddressesByName(host: string): Promise<Array<NetAddress>>

使用当前默认网络解析主机名以获取所有IP地址。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<NetAddress>> | Promise对象。返回所有IP地址。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

connection.getAddressesByName("xxxx").then((data: connection.NetAddress[]) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});
```

**connection.getAddressesByNameWithOptions23+**

getAddressesByNameWithOptions(host: string, option?: QueryOptions): Promise<Array<NetAddress>>

使用当前默认网络基于指定IP类型进行DNS解析。使用Promise异步回调。

需要权限：ohos.permission.INTERNET

模型约束：此接口仅可在Stage模型下使用。

系统能力：SystemCapability.Communication.NetManager.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。例如："www.example.com"。 |
| option | QueryOptions | 否 | 需要查询的IP类型，默认值为FAMILY_TYPE_ALL。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<NetAddress>> | Promise对象，返回查询到的IP地址。返回值中的port字段固定为0，无需关注。 |

错误码：

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

示例：

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
let option: connection.QueryOptions = {
  family: connection.FamilyType.FAMILY_TYPE_IPV4
};
connection.getAddressesByNameWithOptions("www.example.com", option).then((data: connection.NetAddress[]) => {
  console.info(`Succeeded to get data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`get ERROR msg: ${JSON.stringify(err)}`)
});
```

**QueryOptions23+**

需要查询的IP类型。

系统能力：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| family | FamilyType | 否 | 是 | 需要查询的具体IP地址类型，默认值为FAMILY_TYPE_ALL。 |

**FamilyType23+**

需要查询的具体IP地址类型。

系统能力：SystemCapability.Communication.NetManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FAMILY_TYPE_ALL | 0 | 查询所有IPv4和IPv6地址。 |
| FAMILY_TYPE_IPV4 | 1 | 仅查询IPv4地址。 |
| FAMILY_TYPE_IPV6 | 2 | 仅查询IPv6地址。 |

#### connection.addCustomDnsRule11+

addCustomDnsRule(host: string, ip: Array<string>, callback: AsyncCallback<void>): void

为当前应用程序添加自定义host和对应的IP地址的映射。使用callback异步回调。


不需要时可调用[removeCustomDnsRule](#ZH-CN_TOPIC_0000002553201441__connectionremovecustomdnsrule11)删除某一条自定义规则或调用[clearCustomDnsRules](#ZH-CN_TOPIC_0000002553201441__connectionclearcustomdnsrules11)删除当前应用程序的所有的自定义DNS规则 。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要自定义解析的主机名。 |
| ip | Array<string> | 是 | 主机名所映射的IP地址列表。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当为当前应用程序添加自定义host和对应的ip地址的映射成功，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.addCustomDnsRule("xxxx", ["xx.xx.xx.xx","xx.xx.xx.xx"], (error: BusinessError, data: void) => {
  if (error) {
    console.error(`Failed to get add custom dns rule. Code:${error.code}, message:${error.message}`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
})
```

#### connection.addCustomDnsRule11+

addCustomDnsRule(host: string, ip: Array<string>): Promise<void>

为当前应用程序添加自定义host和对应的IP地址的映射。使用Promise异步回调。


不需要时可调用[removeCustomDnsRule](#ZH-CN_TOPIC_0000002553201441__connectionremovecustomdnsrule11)删除某一条自定义规则或调用[clearCustomDnsRules](#ZH-CN_TOPIC_0000002553201441__connectionclearcustomdnsrules11)删除当前应用程序的所有的自定义DNS规则 。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要自定义解析的主机名。 |
| ip | Array<string> | 是 | 主机名所映射的IP地址列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.addCustomDnsRule("xxxx", ["xx.xx.xx.xx","xx.xx.xx.xx"]).then(() => {
    console.info("success");
}).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
})
```

#### connection.removeCustomDnsRule11+

removeCustomDnsRule(host: string, callback: AsyncCallback<void>): void

删除当前应用程序中对应host的自定义DNS规则。使用callback异步回调。


可调用[addCustomDnsRule](#ZH-CN_TOPIC_0000002553201441__connectionaddcustomdnsrule11)添加自定义规则。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要删除自定义DNS规则的主机名。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除当前应用程序中对应host的自定义DNS规则成功，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.removeCustomDnsRule("xxxx", (error: BusinessError, data: void) => {
  if (error) {
    console.error(`Failed to remove custom dns rule. Code:${error.code}, message:${error.message}`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
})
```

#### connection.removeCustomDnsRule11+

removeCustomDnsRule(host: string): Promise<void>

删除当前应用程序中对应host的自定义DNS规则。使用Promise异步回调。


可调用[addCustomDnsRule](#ZH-CN_TOPIC_0000002553201441__connectionaddcustomdnsrule11)添加自定义规则。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要删除自定义DNS规则的主机名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.removeCustomDnsRule("xxxx").then(() => {
    console.info("success");
}).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
})
```

#### connection.clearCustomDnsRules11+

clearCustomDnsRules(callback: AsyncCallback<void>): void

删除当前应用程序的所有的自定义DNS规则。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除当前应用程序的所有的自定义DNS规则成功，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.clearCustomDnsRules((error: BusinessError, data: void) => {
  if (error) {
    console.error(`Failed to clear custom dns rules. Code:${error.code}, message:${error.message}`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
})
```

#### connection.clearCustomDnsRules11+

clearCustomDnsRules(): Promise<void>

删除当前应用程序的所有的自定义DNS规则。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.clearCustomDnsRules().then(() => {
    console.info("success");
}).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
})
```

#### connection.setPacFileUrl20+

setPacFileUrl(pacFileUrl: string): void

设置PAC脚本（Proxy Auto-Configuration Script，代理自动配置脚本）的URL地址，并启动PAC代理能力，比如：[http://127.0.0.1:21998/PacProxyScript.pac](http://127.0.0.1:21998/PacProxyScript.pac) 。可通过调用[findProxyForUrl](#ZH-CN_TOPIC_0000002553201441__connectionfindproxyforurl20)解析URL地址来获取代理信息。


1、本接口当前只在PC设备上支持解析脚本并启用PAC代理能力，其他设备类型上只保存脚本地址，不会启用PAC代理能力。

2、该接口不会校验URL真实性，PC设备上在设置完成之后，会启动PAC代理，若URL有误，则启动代理失败，返回2100002错误码。

**需要权限**：ohos.permission.SET_PAC_URL

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pacFileUrl | string | 是 | 当前PAC脚本的URL地址。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

let pacFileUrl = "http://example.com/proxy.pac";
connection.setPacFileUrl(pacFileUrl);
```

#### connection.getPacFileUrl20+

getPacFileUrl(): string

获取当前PAC脚本的URL地址。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前PAC脚本的URL地址，如果没有PAC脚本则返回空字符串。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

let pacFileUrl = connection.getPacFileUrl();
console.info(pacFileUrl);
```

#### connection.findProxyForUrl20+

findProxyForUrl(url: string): string

通过设置的PAC脚本，解析指定的URL代理地址，返回对应的PAC代理信息。


1、可通过 [setPacFileUrl](#ZH-CN_TOPIC_0000002553201441__connectionsetpacfileurl20) 或 [setPacUrl](#ZH-CN_TOPIC_0000002553201441__connectionsetpacurl15) 设置PAC脚本。

2、如果调用本接口前未设置PAC脚本，则返回空字符串。

3、由于[setPacFileUrl](#ZH-CN_TOPIC_0000002553201441__connectionsetpacfileurl20)接口当前仅支持PC设备解析脚本并启用PAC代理能力，因此本接口当前也仅支持PC设备获取PAC代理信息。 其他设备调用本接口功能不生效，返回空字串。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要查找代理信息的URL。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回代理信息。 |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

let proxyInfo = connection.findProxyForUrl("http://example.com");
console.info(proxyInfo);
```

#### connection.setPacUrl15+

setPacUrl(pacUrl: string): void

设置系统级代理自动配置（Proxy Auto Config，PAC）脚本地址。


只支持设置脚本地址，不支持解析和启用代理功能，如需设置脚本并启用代理，则可调用[setPacFileUrl](#ZH-CN_TOPIC_0000002553201441__connectionsetpacfileurl20)接口。

**需要权限**：ohos.permission.SET_PAC_URL

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pacUrl | string | 是 | 需要设置的PAC脚本的地址，该接口不会对脚本地址进行校验。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

let pacUrl = "xxx";
connection.setPacUrl(pacUrl);
```

#### connection.getPacUrl15+

getPacUrl(): string

获取系统级代理自动配置（PAC）脚本地址。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回PAC脚本地址。PAC脚本不存在时，抛出2100003错误码。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

let pacUrl = connection.getPacUrl();
```

#### connection.setNetExtAttribute20+

setNetExtAttribute(netHandle: NetHandle, netExtAttribute: string): Promise<void>

为netHandle对应的网络设置扩展属性，标识网络的安全级别。使用Promise异步回调。

该接口所需的权限目前仅支持PC设备。

**需要权限**：ohos.permission.SET_NET_EXT_ATTRIBUTE

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄。 |
| netExtAttribute | string | 是 | 需要设置的网络扩展属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  let netExtAttribute: string = "xxx";
  connection.setNetExtAttribute(netHandle, netExtAttribute).then(() => {
    console.info("setNetExtAttribute success");
  }).catch((error: BusinessError) => {
    console.error("setNetExtAttribute failed, err: " + error.code);
  })
});
```

#### connection.setNetExtAttributeSync20+

setNetExtAttributeSync(netHandle: NetHandle, netExtAttribute: string): void

为netHandle对应的网络设置扩展属性，标识网络的安全级别。使用同步方式返回。


该接口所需的权限目前仅支持PC设备。

**需要权限**：ohos.permission.SET_NET_EXT_ATTRIBUTE

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄。 |
| netExtAttribute | string | 是 | 需要设置的网络扩展属性。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netExtAttribute: string = "xxx";
let netHandle = connection.getDefaultNetSync();
if (netHandle.netId != 0) {
  connection.setNetExtAttributeSync(netHandle, netExtAttribute);
}
```

#### connection.getNetExtAttribute20+

getNetExtAttribute(netHandle: NetHandle): Promise<string>

获取netHandle对应网络的扩展属性，以确定网络的安全级别。使用Promise异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回的网络扩展属性。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  connection.getNetExtAttribute(netHandle).then((netExtAttribute: string) => {
    console.info("getNetExtAttribute: " + netExtAttribute);
  }).catch((error: BusinessError) => {
    console.error("getNetExtAttribute failed, err: " + error.code);
  })
});
```

#### connection.getNetExtAttributeSync20+

getNetExtAttributeSync(netHandle: NetHandle): string

获取netHandle对应网络的扩展属性，以确定网络的安全级别。使用同步方式返回。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | NetHandle | 是 | 网络句柄。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 以同步方式返回的网络扩展属性。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netHandle = connection.getDefaultNetSync();
if (netHandle.netId != 0) {
  let netExtAttribute: string = connection.getNetExtAttributeSync(netHandle);
  console.info("getNetExtAttribute: " + netExtAttribute);
}
```

#### connection.getIpNeighTable22+

getIpNeighTable(): Promise<Array<NetIpMacInfo>>

获取本地设备IP邻居表条目信息，包括IPv4和IPv6，每个条目信息包括IP地址、MAC地址、网卡名。使用Promise异步回调。

该接口获取IP邻居表的缓存的数据，并非局域网内所有连接的数据。

开发者可使用此接口排查网络异常、解析IP地址与MAC地址映射。

**需要权限**：ohos.permission.GET_NETWORK_INFO 和 ohos.permission.GET_IP_MAC_INFO

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<NetIpMacInfo>> | Promise对象，返回ip邻居表条目信息。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getIpNeighTable().then((data: connection.NetIpMacInfo[]) => {
  if (data.length !== 0) {
    console.info(`ipAddress:${data[0].ipAddress}`);
    console.info(`ifaceName:${data[0].iface}`);
    console.info(`macAddress:${data[0].macAddress}`);
  }
}).catch((error: BusinessError) => {
  console.error(`error fetching ip neigh table. Code:${error.code}, message:${error.message}`);
});
```

**connection.getConnectOwnerUid23+**

getConnectOwnerUid(protocol: ProtocolType, local: NetAddress, remote: NetAddress): Promise<number>

用于查询发起指定网络连接的应用UID。使用Promise异步回调。


- 该接口仅限在VPN应用中调用。

- 调用接口时请设置local和remote参数的端口号。若未设置端口号或将端口号设置为0，接口会基于其他参数筛选出符合条件的UID的集合，并从中返回一个匹配的UID。

- protocol参数为PROTO_TYPE_UDP时，若通过local，remote参数未筛选出符合条件的UID，则仅基于local参数筛选并返回匹配的UID。

需要权限：ohos.permission.GET_NETWORK_INFO

系统能力：SystemCapability.Communication.NetManager.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| protocol | ProtocolType | 是 | 网络协议的类型。 |
| local | NetAddress | 是 | 源网络地址。 |
| remote | NetAddress | 是 | 目标网络地址。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回应用程序的UID。如果不存在匹配的UID则返回-1。 |

错误码：

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100301 | Incorrect usage in non-VPN application. |
| 2100003 | System internal error. |

示例：

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let protocol = connection.ProtocolType.PROTO_TYPE_TCP;
let local: connection.NetAddress = { address: '192.168.1.100', family: 1, port: 6666 };
let remote: connection.NetAddress = { address: '192.168.1.200', family: 1, port: 8888 };
connection.getConnectOwnerUid(protocol, local, remote).then((uid) => {
  console.info(`uid: ${uid}`);
}).catch((error: BusinessError) => {
  console.error(`getConnectOwnerUid failed. errorCode: ${error.code} message:${error.message}`);
});
```

**connection.getConnectOwnerUidSync23+**

getConnectOwnerUidSync(protocol: ProtocolType, local: NetAddress, remote: NetAddress): number

用于查询发起指定网络连接的应用UID。使用同步方式返回。


- 该接口仅限在VPN应用中调用。

- 调用接口时请设置local和remote参数的端口号。若未设置端口号或将端口号设置为0，接口会基于其他参数筛选出符合条件的UID的集合，并从中返回一个匹配的UID。

- protocol参数为PROTO_TYPE_UDP时，若通过local，remote参数未筛选出符合条件的UID，则仅基于local参数筛选并返回匹配的UID。

需要权限：ohos.permission.GET_NETWORK_INFO

系统能力：SystemCapability.Communication.NetManager.Core

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| protocol | ProtocolType | 是 | 网络协议的类型。 |
| local | NetAddress | 是 | 源网络地址。 |
| remote | NetAddress | 是 | 目标网络地址。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 返回应用程序的UID。如果不存在匹配的UID则返回-1。 |

错误码：

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100301 | Incorrect usage in non-VPN application. |
| 2100003 | System internal error. |

示例：

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let protocol = connection.ProtocolType.PROTO_TYPE_TCP;
let local: connection.NetAddress = { address: '192.168.1.100', family: 1, port: 6666 };
let remote: connection.NetAddress = { address: '192.168.1.200', family: 1, port: 8888 };
try {
  let uid = connection.getConnectOwnerUidSync(protocol, local, remote);
  console.info(`uid: ${uid}`);
} catch (e) {
  let err = e as BusinessError;
  console.error(`getConnectOwnerUid failed. errorCode: ${err.code} message:${err.message}`);
}
```

**connection.getDnsAscii23+**

getDnsAscii(host: string, flag?: ConversionProcess): string

将Unicode编码形式的主机名转换为ASCII编码形式，并可通过可选的转换流程参数（conversionProcess）控制转换行为。


conversionProcess设置为NO_CONFIGURATION时，只能转换已正式分配含义的Unicode字符所对应的域名。

conversionProcess设置为ALLOW_UNASSIGNED时，可以转换包含尚未分配含义的Unicode字符的域名。

conversionProcess设置为USE_STD3_ASCII_RULES时，会在转换过程中强制按照STD-3 ASCII规则（即RFC 1123标准）对生成的ASCII域名进行检查。

传入参数中的数字和英文不做转码。

系统能力：SystemCapability.Communication.NetManager.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 要转换的主机名（host）。每个标签（点分隔的部分）长度不超过63字节。 |
| flag | ConversionProcess | 否 | 转换流程参数，默认值为NO_CONFIGURATION。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| string | 返回转换结果。 |

错误码：

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

示例：

```ets
import { connection } from '@kit.NetworkKit';

let result = connection.getDnsAscii("www.示例.com", connection.ConversionProcess.NO_CONFIGURATION);
console.info(result);  // 预期结果：www.xn--fsq092h.com
let result = connection.getDnsAscii("www.example.com", connection.ConversionProcess.NO_CONFIGURATION);
console.info(result);  // 预期结果：www.example.com
```

**connection.getDnsUnicode23+**

getDnsUnicode(host: string, flag?: ConversionProcess): string

使用Punycode编码方式，将ASCII编码形式的主机名转换为Unicode编码形式，并通过可选的conversionProcess参数控制转换行为。

系统能力：SystemCapability.Communication.NetManager.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 要转换的主机名（host）。 |
| flag | ConversionProcess | 否 | 转换流程参数，默认值为NO_CONFIGURATION。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| string | 返回转换结果。 |

错误码：

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

示例：

```ets
import { connection } from '@kit.NetworkKit';

let result = connection.getDnsUnicode("www.xn--fsq092h.com", connection.ConversionProcess.NO_CONFIGURATION);
console.info(result);  // 预期结果：www.示例.com
let result = connection.getDnsUnicode("www.example.com", connection.ConversionProcess.NO_CONFIGURATION);
console.info(result);  // 预期结果：www.example.com
```

#### NetConnection

网络连接对象类型。


（1）设备从无网络状态转变为有网络状态时，将触发netAvailable事件、netCapabilitiesChange事件和netConnectionPropertiesChange事件；

（2）接收到netAvailable事件后，若设备从有网络状态转变为无网络状态，将触发netLost事件；

（3）若未接收到netAvailable事件，则将直接接收到netUnavailable事件；

（4）设备从WiFi网络切换至蜂窝网络时，将先触发netLost事件（WiFi丢失），随后触发netAvailable事件（蜂窝可用）。

#### register

register(callback: AsyncCallback<void>): void

订阅指定网络状态变化的通知。如需监听特定事件，确保调用on监听事件后再调用register进行注册。

使用完register接口后需要及时调用unregister取消注册。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当订阅指定网络状态变化的通知成功，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2101008 | The callback already exists. |
| 2101022 | The number of requests exceeded the maximum allowed. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netCon: connection.NetConnection = connection.createNetConnection();
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

#### unregister

unregister(callback: AsyncCallback<void>): void

取消订阅默认网络状态变化的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当取消订阅指定网络状态变化的通知成功，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2101007 | The callback does not exist. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netCon: connection.NetConnection = connection.createNetConnection();
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

#### on('netAvailable')

on(type: 'netAvailable', callback: Callback<NetHandle>): void

订阅网络可用事件。此接口需在调用register接口之前调用。若无需接收网络状态变化的回调通知，应使用unregister取消订阅默认的网络状态变化通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'netAvailable'。 netAvailable：数据网络可用事件。 |
| callback | Callback<NetHandle> | 是 | 回调函数，返回数据网络句柄。 |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建NetConnection对象。
let netCon: connection.NetConnection = connection.createNetConnection();

// 先使用on接口订阅网络可用事件。
netCon.on('netAvailable', (data: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// 注册网络状态变化事件。此接口要在调用on后调用。
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// 使用unregister接口取消订阅网络可用事件。
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

#### on('netBlockStatusChange')

on(type: 'netBlockStatusChange', callback: Callback<NetBlockStatusInfo>): void

订阅网络阻塞状态事件。此接口需要在调用register接口之前调用。若无需接收网络状态变化的回调通知，应使用unregister取消订阅默认的网络状态变化通知。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'netBlockStatusChange'。 netBlockStatusChange：网络阻塞状态事件。 |
| callback | Callback<NetBlockStatusInfo> | 是 | 回调函数，获取网络阻塞状态信息。 |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建NetConnection对象。
let netCon: connection.NetConnection = connection.createNetConnection();

// 先使用on接口订阅网络阻塞状态事件。
netCon.on('netBlockStatusChange', (data: connection.NetBlockStatusInfo) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// 注册网络状态变化事件。此接口要在调用on后调用。
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// 使用unregister接口取消订阅网络阻塞状态事件。
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

#### on('netCapabilitiesChange')

on(type: 'netCapabilitiesChange', callback: Callback<NetCapabilityInfo>): void

订阅网络能力变化事件。此接口要在register接口调用前调用，不需要网络状态变化回调通知时，使用unregister取消订阅默认网络状态变化的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'netCapabilitiesChange'。 netCapabilitiesChange：网络能力变化事件。 |
| callback | Callback<NetCapabilityInfo> | 是 | 回调函数，返回数据网络句柄(netHandle)和网络的能力信息(netCap)。 |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建NetConnection对象。
let netCon: connection.NetConnection = connection.createNetConnection();

// 先使用on接口订阅网络能力变化事件。
netCon.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

//  注册网络状态变化事件。此接口要在调用on后调用。
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// 使用unregister接口取消订阅网络能力变化事件。
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

#### on('netConnectionPropertiesChange')

on(type: 'netConnectionPropertiesChange', callback: Callback<NetConnectionPropertyInfo>): void

订阅网络连接信息变化事件。此接口要在register接口调用前调用，不需要网络状态变化回调通知时，使用unregister取消订阅默认网络状态变化的通知。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'netConnectionPropertiesChange'。 netConnectionPropertiesChange：网络连接信息变化事件。 |
| callback | Callback<NetConnectionPropertyInfo> | 是 | 回调函数，获取网络连接属性信息。 |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建NetConnection对象。
let netCon: connection.NetConnection = connection.createNetConnection();

// 先使用on接口订阅网络连接信息变化事件。
netCon.on('netConnectionPropertiesChange', (data: connection.NetConnectionPropertyInfo) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// 注册网络状态变化事件。此接口要在调用on后调用。
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// 使用unregister接口取消订阅网络连接信息变化事件。
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

#### on('netLost')

on(type: 'netLost', callback: Callback<NetHandle>): void

订阅网络丢失事件。此接口要在register接口调用前调用，不需要网络状态变化回调通知时，使用unregister取消订阅默认网络状态变化的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'netLost'。 netLost：网络严重中断或正常断开事件。 |
| callback | Callback<NetHandle> | 是 | 回调函数，数据网络句柄(netHandle)。 |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建NetConnection对象。
let netCon: connection.NetConnection = connection.createNetConnection();

// 先使用on接口订阅网络丢失事件。
netCon.on('netLost', (data: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// 注册网络状态变化事件。此接口要在调用on后调用。
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// 使用unregister接口取消订阅网络丢失事件。
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

#### on('netUnavailable')

on(type: 'netUnavailable', callback: Callback<void>): void

订阅网络不可用事件。此接口要在register接口调用前调用，不需要网络状态变化回调通知时，使用unregister取消订阅默认网络状态变化的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'netUnavailable'。 netUnavailable：网络不可用事件。 |
callbackCallback<void>是回调函数，无返回结果。

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建NetConnection对象。
let netCon: connection.NetConnection = connection.createNetConnection();

// 先使用on接口订阅网络不可用事件。
netCon.on('netUnavailable', () => {
  console.info("Succeeded to get unavailable net event");
});

// 注册网络状态变化事件。此接口要在调用on后调用。
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// 使用unregister接口取消订阅网络不可用事件。
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

#### NetHandle

网络句柄。

在调用NetHandle的方法之前，需要先获取NetHandle对象。例如可通过[getDefaultNet](#ZH-CN_TOPIC_0000002553201441__connectiongetdefaultnet)获取系统当前默认网络的网络句柄。

**系统能力**：SystemCapability.Communication.NetManager.Core

#### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| netId | number | 否 | 否 | 网络ID，取值为0代表没有默认网络，其余有效取值必须大于等于100。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

#### bindSocket9+

bindSocket(socketParam: TCPSocket | UDPSocket, callback: AsyncCallback<void>): void

将TCPSocket或UDPSocket绑定到当前NetHandle对应的网络。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socketParam | TCPSocket | UDPSocket | 是 | 待绑定的TCPSocket或UDPSocket对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当TCPSocket或UDPSocket成功绑定到当前网络，error为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection, socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface Data {
  message: ArrayBuffer,
  remoteInfo: socket.SocketRemoteInfo
}

  connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
  }
  let tcp : socket.TCPSocket = socket.constructTCPSocketInstance();
  let udp : socket.UDPSocket = socket.constructUDPSocketInstance();
  let socketType = "TCPSocket";
  if (socketType == "TCPSocket") {
    tcp.bind({address:"192.168.xxx.xxx",
              port:8080,
              family:1} as socket.NetAddress, (error: Error) => {
      if (error) {
        console.error('bind fail');
        return;
      }
      netHandle.bindSocket(tcp, (error: BusinessError, data: void) => {
        if (error) {
          console.error(`Failed to bind socket. Code:${error.code}, message:${error.message}`);
          return;
        } else {
          console.info(JSON.stringify(data));
        }
      });
  } else {
    let callback: (value: Data) => void = (value: Data) => {
      console.info("on message, message:" + value.message + ", remoteInfo:" + value.remoteInfo);
    };
    udp.bind({address:"192.168.xxx.xxx",
              port:8080,
              family:1} as socket.NetAddress, (error: BusinessError) => {
      if (error) {
        console.error(`Failed to bind. Code:${error.code}, message:${error.message}`);
        return;
      }
      udp.on('message', (data: Data) => {
        console.info("Succeeded to get data: " + JSON.stringify(data));
      });
      netHandle.bindSocket(udp, (error: BusinessError, data: void) => {
        if (error) {
          console.error(`Failed to bind socket. Code:${error.code}, message:${error.message}`);
          return;
        } else {
          console.info(JSON.stringify(data));
        }
      });
  }
})
```

#### bindSocket9+

bindSocket(socketParam: TCPSocket | UDPSocket): Promise<void>

将TCPSocket或UDPSocket绑定到当前NetHandle对应的网络。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socketParam | TCPSocket | UDPSocket | 是 | 待绑定的TCPSocket或UDPSocket对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection, socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface Data {
  message: ArrayBuffer,
  remoteInfo: socket.SocketRemoteInfo
}

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandle的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  let tcp : socket.TCPSocket = socket.constructTCPSocketInstance();
  let udp : socket.UDPSocket = socket.constructUDPSocketInstance();
  let socketType = "TCPSocket";
  if (socketType == "TCPSocket") {
    tcp.bind({address:"192.168.xxx.xxx",
              port:8080,
              family:1} as socket.NetAddress, (error: Error) => {
      if (error) {
        console.error('bind fail');
        return;
      }
      netHandle.bindSocket(tcp).then(() => {
        console.info("bind socket success");
      }).catch((error: BusinessError) => {
        console.error(`Failed to bind socket. Code:${error.code}, message:${error.message}`);
      });
  } else {
    let callback: (value: Data) => void = (value: Data) => {
      console.info("on message, message:" + value.message + ", remoteInfo:" + value.remoteInfo);
    }
    udp.bind({address:"192.168.xxx.xxx",
              port:8080,
              family:1} as socket.NetAddress, (error: BusinessError) => {
      if (error) {
        console.error(`Failed to bind. Code:${error.code}, message:${error.message}`);
        return;
      }
      udp.on('message', (data: Data) => {
        console.info("Succeeded to get data: " + JSON.stringify(data));
      });
      netHandle.bindSocket(udp).then(() => {
        console.info("bind socket success");
      }).catch((error: BusinessError) => {
        console.error(`Failed to bind socket. Code:${error.code}, message:${error.message}`);
      });
  }
});
```

#### getAddressesByName

getAddressesByName(host: string, callback: AsyncCallback<Array<NetAddress>>): void

使用当前NetHandle对应的网络解析主机名获取到的所有IP地址。使用callback异步回调。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。例如："www.example.com"。 |
| callback | AsyncCallback<Array<NetAddress>> | 是 | 回调函数。当使用对应网络解析主机名成功获取所有IP地址，error为undefined，data为获取到的所有IP地址；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandler的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  let host = "www.example.com";
  netHandle.getAddressesByName(host, (error: BusinessError, data: connection.NetAddress[]) => {
    if (error) {
      console.error(`Failed to get addresses. Code:${error.code}, message:${error.message}`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
```

#### getAddressesByName

getAddressesByName(host: string): Promise<Array<NetAddress>>

使用当前NetHandle对应的网络解析主机名获取到的所有IP地址。使用Promise异步回调。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。例如："www.example.com"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<NetAddress>> | Promise对象，返回所有IP地址。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandler的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  let host = "www.example.com";
  netHandle.getAddressesByName(host).then((data: connection.NetAddress[]) => {
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
```

**getAddressesByNameWithOptions23+**

getAddressesByNameWithOptions(host: string, option?: QueryOptions): Promise<Array<NetAddress>>

使用当前NetHandle对应的网络基于指定IP类型进行DNS解析。使用Promise异步回调。

需要权限：ohos.permission.INTERNET

模型约束：此接口仅可在Stage模型下使用。

系统能力：SystemCapability.Communication.NetManager.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。例如："www.example.com"。 |
| option | QueryOptions | 否 | 需要查询的IP类型。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<NetAddress>> | Promise对象，返回查询到的IP地址。返回值中的port字段固定为0，无需关注。 |

错误码：

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

示例：

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandler的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  let host = "www.example.com";
  let option: connection.QueryOptions = {
      family: connection.FamilyType.FAMILY_TYPE_IPV4
    };
  netHandle.getAddressesByNameWithOptions(host, option).then((data: connection.NetAddress[]) => {
    console.info(`Succeeded to get data: ${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`get ERROR msg: ${JSON.stringify(err)}`)
});
```

#### getAddressByName

getAddressByName(host: string, callback: AsyncCallback<NetAddress>): void

使用当前NetHandle对应的网络解析主机名获取到的第一个IP地址。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。例如："www.example.com"。 |
| callback | AsyncCallback<NetAddress> | 是 | 回调函数。当使用对应网络解析主机名获取第一个IP地址成功，error为undefined，data为获取的第一个IP地址；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandler的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  let host = "www.example.com";
  netHandle.getAddressByName(host, (error: BusinessError, data: connection.NetAddress) => {
    if (error) {
      console.error(`Failed to get address. Code:${error.code}, message:${error.message}`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
```

#### getAddressByName

getAddressByName(host: string): Promise<NetAddress>

使用当前NetHandle对应的网络解析主机名获取到的第一个IP地址。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | 需要解析的主机名。例如："www.example.com"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<NetAddress> | Promise对象，返回获取到的第一个IP地址。 |

**错误码：**

以下错误码的详细介绍请参见[网络连接管理错误码](网络连接管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // 当前没有已连接的网络时，netHandler的netId为0，属于异常场景。可根据实际情况添加处理机制。
    return;
  }
  let host = "www.example.com";
  netHandle.getAddressByName(host).then((data: connection.NetAddress) => {
    console.info("Succeeded to get data: " + JSON.stringify(data));
  });
```

#### NetCap

网络具体能力。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NET_CAPABILITY_MMS | 0 | 表示网络可以访问运营商的MMSC（Multimedia Message Service，多媒体短信服务）发送和接收彩信。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| NET_CAPABILITY_NOT_METERED | 11 | 表示网络流量未被计费。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| NET_CAPABILITY_INTERNET | 12 | 表示该网络应具有访问Internet的能力，此能力由网络提供者设置，但该网络访问Internet的连通性并未被网络管理成功验证。网络连通性可以通过NET_CAPABILITY_VALIDATED和NET_CAPABILITY_CHECKING_CONNECTIVITY判断。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| NET_CAPABILITY_NOT_VPN | 15 | 表示网络不使用VPN（Virtual Private Network，虚拟专用网络）。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| NET_CAPABILITY_VALIDATED | 16 | 表示网络管理通过该网络与华为云地址成功建立连接，此能力由网络管理模块设置。 注意： 网络管理可能会与华为云地址建立连接失败，导致网络能力不具备此标记位，但不完全代表该网络无法访问互联网。另外，对于新完成连接的网络，由于网络正在进行连通性验证，此值可能无法反映真实的验证结果。对此，应用可以通过NET_CAPABILITY_CHECKING_CONNECTIVITY12+检查网络是否正在检测连通性。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| NET_CAPABILITY_PORTAL12+ | 17 | 表示系统发现该网络存在强制网络门户，需要用户登陆认证，该能力由网络管理模块设置。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| NET_CAPABILITY_CHECKING_CONNECTIVITY12+ | 31 | 表示网络管理正在检验当前网络的连通性，此值会在网络连接时设置。当此值存在时，NET_CAPABILITY_VALIDATED的值不准确，连通性检测结束后不再设置，此时可以通过判断NetCap是否包含NET_CAPABILITY_VALIDATED判断连通性。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

#### NetBearType

网络类型。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BEARER_CELLULAR | 0 | 蜂窝网络。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| BEARER_WIFI | 1 | Wi-Fi网络。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| BEARER_BLUETOOTH12+ | 2 | 蓝牙网络。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| BEARER_ETHERNET | 3 | 以太网网络。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
BEARER_VPN12+4VPN网络。

**ConversionProcess23+**

ASCII/Unicode转码转换流程参数的枚举。

系统能力：SystemCapability.Communication.NetManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO_CONFIGURATION | 0 | 仅允许转换已分配的Unicode代码点的域名（Unicode为每个字符分配一个唯一的数字，这个数字就叫做代码点）。 |
| ALLOW_UNASSIGNED | 1 | 允许转换包含未分配Unicode代码点的域名(在Unicode字符集中，并非所有代码点都已分配字符，即未分配Unicode代码点)。 |
| USE_STD3_ASCII_RULES | 2 | 在转换过程中，强制使用STD-3 ASCII规则（即RFC 1123标准）检查生成的ASCII域名。 |

#### HttpProxy10+

网络代理配置信息

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| host | string | 否 | 否 | 代理服务器主机名。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| port | number | 否 | 否 | 主机端口。取值范围[0,65535]。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| exclusionList | Array<string> | 否 | 否 | 不使用代理的主机名列表，主机名支持域名、IP地址以及通配符形式，详细匹配规则如下： 1、域名匹配规则： （1）完全匹配：代理服务器主机名只要与列表中的任意一个主机名完全相同，就可以匹配。 （2）包含匹配：代理服务器主机名只要包含列表中的任意一个主机名，就可以匹配。 例如，如果在主机名列表中设置了 “ample.com”，则 “ample.com”、“www.ample.com”、“ample.com:80”都会被匹配，而 “www.example.com”、“ample.com.org”则不会被匹配。 2、IP地址匹配规则：代理服务器主机名只要与列表中的任意一个IP地址完全相同，就可以匹配。 3、域名跟IP地址可以同时添加到列表中进行匹配。 4、单个“*”是唯一有效的通配符，当列表中只有通配符时，将与所有代理服务器主机名匹配，表示禁用代理。通配符只能单独添加，不可以与其他域名、IP地址一起添加到列表中，否则通配符将不生效。 5、匹配规则不区分主机名大小写。 6、匹配主机名时，不考虑http和https等协议前缀。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| username12+ | string | 否 | 是 | 使用代理的用户名。 说明: 需同时设置password参数才会生效。 |
| password12+ | string | 否 | 是 | 使用代理的用户密码。 说明: 需同时设置username参数才会生效。 |

#### NetSpecifier

提供承载数据网络能力的实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| netCapabilities | NetCapabilities | 否 | 否 | 存储数据网络的传输能力和承载类型。 |
| bearerPrivateIdentifier | string | 否 | 是 | 网络标识符，蜂窝网络的标识符是"slot0"（对应SIM卡1）、"slot1"（对应SIM卡2）。从API12开始可以通过传递注册的WLAN热点信息表示应用希望激活的指定的WLAN网络。 |

**示例：**

```ets
import { connection } from '@kit.NetworkKit';
import { wifiManager } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let config: wifiManager.WifiDeviceConfig = {
  ssid: "TEST",
  preSharedKey: "**********",
  securityType: wifiManager.WifiSecurityType.WIFI_SEC_TYPE_PSK
};
// 通过wifiManager.addCandidateConfig获取注册WLAN的networkId。
wifiManager.addCandidateConfig(config,(error,networkId) => {
 let netConnectionWlan = connection.createNetConnection({
   netCapabilities: {
     bearerTypes: [connection.NetBearType.BEARER_WIFI]
   },
   bearerPrivateIdentifier: `${networkId}`
 });
 netConnectionWlan.register((error: BusinessError) => {
   console.error(JSON.stringify(error));
 });
```

#### NetCapabilityInfo10+

提供承载数据网络能力的实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| netHandle | NetHandle | 否 | 否 | 网络句柄。 |
| netCap | NetCapabilities | 否 | 否 | 存储数据网络的传输能力和承载类型。 |

#### NetCapabilities

网络的能力集。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| linkUpBandwidthKbps | number | 否 | 是 | 上行（设备到网络）带宽，单位(kb/s)。0表示无法评估当前网络带宽。 |
| linkDownBandwidthKbps | number | 否 | 是 | 下行（网络到设备）带宽，单位(kb/s)。0表示无法评估当前网络带宽。 |
| networkCap | Array<NetCap> | 否 | 是 | 网络具体能力。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| bearerTypes | Array<NetBearType> | 否 | 否 | 网络类型。数组里面只包含了一种网络类型。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

#### NetConnectionPropertyInfo11+

网络连接信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

#### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| netHandle | NetHandle | 否 | 否 | 网络句柄。 |
| connectionProperties | ConnectionProperties | 否 | 否 | 网络连接信息。 |

#### NetBlockStatusInfo11+

获取网络状态信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

#### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| netHandle | NetHandle | 否 | 否 | 网络句柄。 |
| blocked | boolean | 否 | 否 | 标识当前网络是否是堵塞状态。true：标识当前网络是堵塞状态；false：标识当前网络不是堵塞状态。 |

#### ConnectionProperties

网络连接信息。


linkAddresses、routes和dnses可能为空，需要做好空值保护，建议使用前先判断对象是否存在。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interfaceName | string | 否 | 否 | 网卡名称。 |
| domains | string | 否 | 否 | 域名。 |
| linkAddresses | Array<LinkAddress> | 否 | 否 | 链路信息。 |
| routes | Array<RouteInfo> | 否 | 否 | 路由信息。 |
| dnses | Array<NetAddress> | 否 | 否 | 网络地址，参考NetAddress。 |
| mtu | number | 否 | 否 | 最大传输单元。 |

#### RouteInfo

网络路由信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interface | string | 否 | 否 | 网卡名称。 |
| destination | LinkAddress | 否 | 否 | 目的地址。 |
| gateway | NetAddress | 否 | 否 | 网关地址。 |
| hasGateway | boolean | 否 | 否 | 是否有网关。true：有网关；false：无网关。 |
| isDefaultRoute | boolean | 否 | 否 | 是否为默认路由。true：默认路由；false：非默认路由。  说明： IPv4默认路由是指目的地址为0.0.0.0/0的路由；IPv6默认路由是指目的地址为::/0的路由。 |
| isExcludedRoute20+ | boolean | 否 | 是 | 是否为排除路由。true表示排除路由，false表示非排除路由，默认值为false。 |

#### LinkAddress

网络链路信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | NetAddress | 否 | 否 | 链路地址。 |
| prefixLength | number | 否 | 否 | 链路地址前缀的长度。 |

#### NetAddress

网络地址。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 地址。 |
| family | number | 否 | 是 | IPv4 = 1，IPv6 = 2，默认IPv4。 |
| port | number | 否 | 是 | 端口，取值范围[0, 65535]，默认值为0。 |

#### HttpRequest

type HttpRequest = http.HttpRequest

定义一个HTTP请求，可以通过[http.createHttp](@ohos.net.http (数据请求).md#ZH-CN_TOPIC_0000002553361401__httpcreatehttp)创建。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| http.HttpRequest | 定义HTTP请求任务。在调用HttpRequest提供的API之前。 |

#### TCPSocket

type TCPSocket = socket.TCPSocket

定义一个TCPSocket对象，可以通过[socket.constructTCPSocketInstance](@ohos.net.socket (Socket连接).md#ZH-CN_TOPIC_0000002522081482__socketconstructtcpsocketinstance)创建。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| socket.TCPSocket | 定义一个TCPSocket连接。 |

#### UDPSocket

type UDPSocket = socket.UDPSocket

定义一个UDPSocket对象，可以通过[socket.constructUDPSocketInstance](@ohos.net.socket (Socket连接).md#ZH-CN_TOPIC_0000002522081482__socketconstructudpsocketinstance)创建。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| socket.UDPSocket | 定义UDPSocket连接。 |

#### NetIpMacInfo22+

IP邻居表条目信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ipAddress | NetAddress | 否 | 否 | IP地址相关信息。 |
| iface | string | 否 | 否 | 网卡名。 |
| macAddress | string | 否 | 否 | MAC地址。 |

**ProtocolType23+**

网络协议类型的枚举。

系统能力：SystemCapability.Communication.NetManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PROTO_TYPE_TCP | 6 | TCP网络协议。 |
| PROTO_TYPE_UDP | 17 | UDP网络协议。 |