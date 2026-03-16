# @ohos.net.statistics (流量管理)

流量管理模块提供获取指定网卡实时上行、下行流量等能力。

本模块首批接口从 API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { statistics } from '@kit.NetworkKit';
```

#### statistics.getIfaceRxBytes10+

getIfaceRxBytes(nic: string, callback: AsyncCallback<number>): void

获取指定网卡实时下行流量，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明nicstring是指定查询的网卡名。callbackAsyncCallback<number>是回调函数。当成功获取网卡实时下行流量时，error 为 undefined，stats 为获取到的网卡实时下行流量(单位:字节)；否则为错误对象。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.2103012Failed to obtain the NIC name.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getIfaceRxBytes("wlan0", (error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```

#### statistics.getIfaceRxBytes10+

getIfaceRxBytes(nic: string): Promise<number>

获取指定网卡实时下行流量，使用 Promise 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明nicstring是指定查询的网卡名。

**返回值：**

类型说明Promise<number>以 Promise 形式返回获取结果。返回网卡实时下行流量(单位:字节)。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.2103012Failed to obtain the NIC name.

**示例：**

```ets
import { statistics } from '@kit.NetworkKit';

statistics.getIfaceRxBytes("wlan0").then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```

#### statistics.getIfaceTxBytes10+

getIfaceTxBytes(nic: string, callback: AsyncCallback<number>): void

获取指定网卡实时上行流量，使用 callback 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明nicstring是指定查询的网卡名。callbackAsyncCallback<number>是回调函数。当成功获取网卡实时上行流量时，error 为 undefined，stats 为获取到的网卡实时上行流量(单位:字节)；否则为错误对象。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.2103012Failed to obtain the NIC name.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getIfaceTxBytes("wlan0", (error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```

#### statistics.getIfaceTxBytes10+

getIfaceTxBytes(nic: string): Promise<number>

获取指定网卡实时上行流量，使用 Promise 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明nicstring是指定查询的网卡名。

**返回值：**

类型说明Promise<number>以 Promise 形式返回获取结果。返回网卡实时上行流量(单位:字节)。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.2103012Failed to obtain the NIC name.

**示例：**

```ets
import { statistics } from '@kit.NetworkKit';

statistics.getIfaceTxBytes("wlan0").then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```

#### statistics.getCellularRxBytes10+

getCellularRxBytes(callback: AsyncCallback<number>): void

获取蜂窝实时下行流量，使用 callback 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。当成功获取蜂窝实时下行流量时，error 为 undefined，stats 为获取到的蜂窝实时下行流量(单位:字节)；否则为错误对象。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)。

错误码ID错误信息2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.2103012Failed to obtain the NIC name.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getCellularRxBytes((error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```

#### statistics.getCellularRxBytes10+

getCellularRxBytes(): Promise<number>

获取蜂窝实时下行流量，使用 Promise 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

类型说明Promise<number>以 Promise 形式返回获取结果。返回蜂窝实时下行流量(单位:字节)。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)。

错误码ID错误信息2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.2103012Failed to obtain the NIC name.

**示例：**

```ets
import { statistics } from '@kit.NetworkKit';

statistics.getCellularRxBytes().then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```

#### statistics.getCellularTxBytes10+

getCellularTxBytes(callback: AsyncCallback<number>): void

获取蜂窝实时上行流量，使用 callback 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。当成功获取蜂窝实时上行流量时，error 为 undefined，stats 为获取到的蜂窝实时上行流量(单位:字节)；否则为错误对象。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)。

错误码ID错误信息2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.2103012Failed to obtain the NIC name.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getCellularTxBytes((error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```

#### statistics.getCellularTxBytes10+

getCellularTxBytes(): Promise<number>

获取蜂窝实时上行流量，使用 Promise 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

类型说明Promise<number>以 Promise 形式返回获取结果。返回蜂窝实时上行流量(单位:字节)。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)。

错误码ID错误信息2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.2103012Failed to obtain the NIC name.

**示例：**

```ets
import { statistics } from '@kit.NetworkKit';

statistics.getCellularTxBytes().then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```

#### statistics.getAllRxBytes10+

getAllRxBytes(callback: AsyncCallback<number>): void

获取所有网卡实时下行流量，使用 callback 方式作为异步方法。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。当成功获取所有网卡实时下行流量，error 为 undefined，stats 为获取到的所有网卡实时下行流量(单位:字节)；否则为错误对象。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)。

错误码ID错误信息2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.

**示例：**

```ets
import { statistics } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

statistics.getAllRxBytes((error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```

#### statistics.getAllRxBytes10+

getAllRxBytes(): Promise<number>

获取所有网卡实时下行流量，使用 Promise 方式作为异步方法。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

类型说明Promise<number>以 Promise 形式返回获取结果。返回所有网卡实时下行流量(单位:字节)。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)。

错误码ID错误信息2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.

**示例：**

```ets
import { statistics } from '@kit.NetworkKit';

statistics.getAllRxBytes().then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```

#### statistics.getAllTxBytes10+

getAllTxBytes(callback: AsyncCallback<number>): void

获取所有网卡实时上行流量，使用 callback 方式作为异步方法。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。当成功获取所有网卡实时上行流量，error 为 undefined，stats 为获取到的所有网卡实时上行流量(单位:字节)；否则为错误对象。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)。

错误码ID错误信息2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getAllTxBytes((error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```

#### statistics.getAllTxBytes10+

getAllTxBytes(): Promise<number>

获取所有网卡实时上行流量，使用 Promise 方式作为异步方法。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

**返回值：**

类型说明Promise<number>以 Promise 形式返回获取结果。返回所有网卡实时上行流量(单位:字节)。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)。

错误码ID错误信息2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.

**示例：**

```ets
import { statistics } from '@kit.NetworkKit';

statistics.getAllTxBytes().then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```

#### statistics.getUidRxBytes10+

getUidRxBytes(uid: number, callback: AsyncCallback<number>): void

获取指定应用实时下行流量，使用 callback 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明uidnumber是指定查询的应用 uid。callbackAsyncCallback<number>是回调函数。当成功获取应用实时下行流量时，error 为 undefined，stats 为获取到的应用实时下行流量(单位:字节)；否则为错误对象。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getUidRxBytes(20010038, (error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```

#### statistics.getUidRxBytes10+

getUidRxBytes(uid: number): Promise<number>

获取指定应用实时下行流量，使用 Promise 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明uidnumber是指定查询的应用 uid。

**返回值：**

类型说明Promise<number>以 Promise 形式返回获取结果。返回指定应用实时下行流量(单位:字节)。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.

**示例：**

```ets
import { statistics } from '@kit.NetworkKit';

statistics.getUidRxBytes(20010038).then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```

#### statistics.getUidTxBytes10+

getUidTxBytes(uid: number, callback: AsyncCallback<number>): void

获取指定应用实时上行流量，使用 callback 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明uidnumber是指定查询的应用 uid。callbackAsyncCallback<number>是回调函数。当成功获取应用实时上行流量时，error 为 undefined，stats 为获取到的应用实时上行流量(单位:字节)；否则为错误对象。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getUidTxBytes(20010038, (error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```

#### statistics.getUidTxBytes10+

getUidTxBytes(uid: number): Promise<number>

获取指定应用实时上行流量，使用 Promise 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明uidnumber是指定查询的应用 uid。

**返回值：**

类型说明Promise<number>以 Promise 形式返回获取结果。返回指定应用实时上行流量(单位:字节)。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2103005Failed to read the system map.2103011Failed to create a system map.

**示例：**

```ets
import { statistics } from '@kit.NetworkKit';

statistics.getUidTxBytes(20010038).then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```

#### statistics.getSockfdRxBytes11+

getSockfdRxBytes(sockfd: number, callback: AsyncCallback<number>): void

获取指定socket的下行流量信息，使用 callback 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明sockfdnumber是指定查询的socket的fd(file description)。callbackAsyncCallback<number>是回调函数。当成功获取socket的下行流量时，error 为 undefined，stats 为获取到的该socket的实时下行流量(单位:字节)；否则为错误对象。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.2100001Invalid parameter value.2100002Failed to connect to the service.2100003System internal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

let sockfd = 50; // 实际开发中需要先根据自己创建的socket获取到。
statistics.getSockfdRxBytes(sockfd, (error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```

#### statistics.getSockfdRxBytes11+

getSockfdRxBytes(sockfd: number): Promise<number>

获取指定socket的下行流量信息，使用 Promise 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明sockfdnumber是指定查询的socket的fd(file description)。

**返回值：**

类型说明Promise<number>以 Promise 形式返回获取结果，返回该socket的实时下行流量(单位:字节)。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.2100001Invalid parameter value.2100002Failed to connect to the service.2100003System internal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

let sockfd = 50; // 实际开发中需要先根据自己创建的socket获取到。
statistics.getSockfdRxBytes(sockfd).then((stats: number) => {
  console.info(JSON.stringify(stats));
}).catch((err: BusinessError) => {
  console.error(JSON.stringify(err));
});
```

#### statistics.getSockfdTxBytes11+

getSockfdTxBytes(sockfd: number, callback: AsyncCallback<number>): void

获取指定socket的上行流量信息，使用 callback 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明sockfdnumber是指定查询的socket的fd(file description)。callbackAsyncCallback<number>是回调函数。当成功获取socket的上行流量时，error 为 undefined，stats 为获取到的该socket的实时上行流量(单位:字节)；否则为错误对象。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.2100001Invalid parameter value.2100002Failed to connect to the service.2100003System internal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

let sockfd = 50; // 实际开发中需要先根据自己创建的socket获取到。
statistics.getSockfdTxBytes(sockfd, (error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```

#### statistics.getSockfdTxBytes11+

getSockfdTxBytes(sockfd: number): Promise<number>

获取指定socket的上行流量信息，使用 Promise 方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明sockfdnumber是指定查询的socket的fd(file description)。

**返回值：**

类型说明Promise<number>以 Promise 形式返回获取结果，返回该socket的实时上行流量(单位:字节)。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error.2100001Invalid parameter value.2100002Failed to connect to the service.2100003System internal error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

let sockfd = 50; // 实际开发中需要先根据自己创建的socket获取到。
statistics.getSockfdTxBytes(sockfd).then((stats: number) => {
  console.info(JSON.stringify(stats));
}).catch((err: BusinessError) => {
  console.error(JSON.stringify(err));
});
```

#### statistics.getSelfTrafficStats22+

getSelfTrafficStats(networkInfo: NetworkInfo): Promise<NetStatsInfo>

获取指定时间段内，本应用在指定网络中的流量使用情况。使用Promise方式作为异步方法。

-

当前只支持获取蜂窝和Wi-Fi流量使用情况。

- 当前只支持获取31天之内的流量使用情况，如果参数中传入的时间戳早于当前系统时间31天，会返回错误码2103019。

**系统能力**：SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明networkInfo[NetworkInfo](#ZH-CN_TOPIC_0000002529285441__networkinfo22)是指定查询的网络信息。

**返回值：**

类型说明Promise<[NetStatsInfo](#ZH-CN_TOPIC_0000002529285441__netstatsinfo22)>Promise对象，返回应用历史流量统计信息。

**错误码：**

以下错误码的详细介绍参见[流量管理错误码](../../errors/流量管理错误码.md)。

错误码ID错误信息2100001Invalid parameter value.2100002Failed to connect to the service.2100003System internal error.2103017Failed to read the database.2103019The timestamp in param is invalid.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { connection, statistics } from '@kit.NetworkKit';

let networkInfo: statistics.NetworkInfo = {
    type: connection.NetBearType.BEARER_CELLULAR,
    startTime: Math.floor(Date.now() / 1000) - 86400 * 31,
    endTime: Math.floor(Date.now() / 1000),
    simId: 1,
}

statistics.getSelfTrafficStats(networkInfo).then((stats: statistics.NetStatsInfo) => {
    console.info('getSelfTrafficStats success : ' + JSON.stringify(stats));
}).catch((err: BusinessError) => {
    console.error('getSelfTrafficStats error. code: ' + `${err.code}` + ', message: ' + `${err.message}`);
});
```

#### NetBearType12+

type NetBearType = connection.NetBearType

网络类型。

**系统能力**：SystemCapability.Communication.NetManager.Core

类型说明[connection.NetBearType](@ohos.net.connection (网络连接管理).md#ZH-CN_TOPIC_0000002497605446__netbeartype)枚举网络类型。

#### NetworkInfo22+

网络信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

名称类型只读可选说明type[NetBearType](#ZH-CN_TOPIC_0000002529285441__netbeartype12)否否

网络类型。

**注意：** 当type为蜂窝网络时，需指定simId字段。

startTimenumber否否开始时间戳(单位：秒)。endTimenumber否否结束时间戳(单位：秒)。simIdnumber否是

SIM卡ID。默认值为uint32_t类型最大值。

**注意：** 当type为蜂窝网络时，需指定本字段。

#### NetStatsInfo22+

获取的历史流量信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

名称类型只读可选说明rxBytesnumber否否流量下行数据(单位：字节)。txBytesnumber否否流量上行数据(单位：字节)。rxPacketsnumber否否流量下行包个数。txPacketsnumber否否流量上行包个数。