# @ohos.distributedsched.linkEnhance (增强连接)

linkEnhance模块提供高效的蓝牙连接和数据传输功能，增强设备间连接的稳定性。使用多通道合并算法，增加设备间连接数，提升跨设备数据传输能力，改善用户使用体验。

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用

#### 导入模块

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
```

#### linkEnhance.createServer

createServer(name: string): Server

在服务端设备上，应用创建服务。通过start()开启后，该设备可作为服务端被其他设备连接。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 自定义的非空字符串，标识应用的服务名，最大长度255字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Server | 创建成功的服务对象。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390203 | Duplicate server name. |
| 32390206 | Invalid parameter. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start sever name = ' + name);
  // 使用服务名构造Server
  let server: linkEnhance.Server = linkEnhance.createServer(name);
} catch (err) {
  hilog.info(0x0000, TAG, 'start sever errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### linkEnhance.createConnection

createConnection(deviceId: string, name: string): Connection

作为客户端的设备创建连接对象，以便后续向服务端设备发起连接。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 连接的目标设备的deviceId，即对端设备的BLE MAC地址。BLE MAC的获取方法，请参考查找设备。 |
| name | string | 是 | 连接的目标设备的服务名，非空字符串，最大长度255字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Connection | 创建成功的连接对象。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

在客户端设备上，应用需要主动调用createConnection()接口创建连接对象。

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection sever deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
} catch (err) {
  hilog.info(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### Server

服务对象，提供启动服务、停止服务、关闭服务、注册/取消注册服务端回调等方法。

以下方法，在服务端设备上执行。

#### start()

start(): void

创建服务成功后，需要调用start()开启该服务，方可被客户端连接，最大服务个数为10。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390202 | The number of servers exceeds the limit. |
| 32390300 | Internal error. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start sever name = ' + name);
  let server: linkEnhance.Server = linkEnhance.createServer(name);
  server.start();
} catch (err) {
  hilog.error(0x0000, TAG, 'start sever errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### stop()

stop(): void

使用完服务时，调用stop停止服务，停止后可以调用start重新开启服务。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start sever name = ' + name);
  let server: linkEnhance.Server = linkEnhance.createServer(name);
  server.start();
  server.stop();
} catch (err) {
  hilog.error(0x0000, TAG, 'start sever errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### close()

close(): void

当业务执行完毕，服务端清理资源时，调用close()方法，销毁Server对象，释放相关资源。之后如果再次与对端设备交互，需要重新创建Server对象。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start sever name = ' + name);
  let server: linkEnhance.Server = linkEnhance.createServer(name);
  server.start();
  server.close();
} catch (err) {
  hilog.error(0x0000, TAG, 'start sever errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### on('connectionAccepted')

on(type: 'connectionAccepted', callback: Callback<Connection>): void

创建服务成功后，注册connectionAccepted事件的回调监听，等待对端连接。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionAccepted'，收到对端连接，触发该事件。 |
| callback | Callback<Connection> | 是 | 注册的回调函数。Connection返回的连接对象。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Parameter invalid. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start sever name = ' + name);
  // 使用服务名构造Server
  let server: linkEnhance.Server = linkEnhance.createServer(name);

  // 订阅服务接收事件
  server.on('connectionAccepted', (connection: linkEnhance.Connection): void => {
    hilog.info(0x0000, TAG, 'serverOnCallback = ' + JSON.stringify(connection));
  });
  // 启动服务
  server.start();
} catch (err) {
  hilog.info(0x0000, TAG, 'start sever errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### off('connectionAccepted')

off(type: 'connectionAccepted', callback?: Callback<Connection>): void

取消注册connectionAccepted事件的回调监听。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionAccepted'，收到对端连接，触发该事件。 |
| callback | Callback<Connection> | 否 | 注册的回调函数。Connection返回的连接对象。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Parameter invalid. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start sever name = ' + name);
  // 使用服务名构造Server
  let server: linkEnhance.Server = linkEnhance.createServer(name);
  server.on('connectionAccepted', (connection: linkEnhance.Connection): void => {
    hilog.info(0x0000, TAG, 'accept new connection');
  });
  // 取消订阅服务接收
  server.off('connectionAccepted', (connection: linkEnhance.Connection): void => {
    hilog.info(0x0000, TAG, 'accept new connection');
  });
} catch (err) {
  hilog.error(0x0000, TAG, 'start sever errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### on('serverStopped')

on(type: 'serverStopped', callback: Callback<number>): void

在创建服务成功后，注册serverStopped回调，监听服务异常停止。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'serverStopped'，底层服务异常时，触发该事件。 |
| callback | Callback<number> | 是 | 注册的回调函数，number为返回的错误码。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Parameter invalid. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start sever name = ' + name);
  // 使用服务名构造Server
  let server: linkEnhance.Server = linkEnhance.createServer(name);

  // 订阅服务停止
  server.on('serverStopped', (reason: number): void => {
    hilog.info(0x0000, TAG, 'serverStopped， reason= ' + reason);
  });
  // 启动服务
  server.start();
} catch (err) {
  hilog.error(0x0000, TAG, 'start sever errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### off('serverStopped')

off(type: 'serverStopped', callback?: Callback<number>): void

取消注册serverStopped事件的回调监听。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'serverStopped'，底层服务异常时触发。 |
| callback | Callback<number> | 否 | 注册的回调函数，number为返回的错误码。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Parameter invalid. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let name: string = "demo";
  hilog.info(0x0000, TAG, 'start sever name = ' + name);
  // 使用服务名构造Server
  let server: linkEnhance.Server = linkEnhance.createServer(name);
  server.on('serverStopped', (reason: number): void => {
    hilog.info(0x0000, TAG, 'serverStopped， reason= ' + reason);
  });
  // 取消订阅服务停止
  server.off('serverStopped', (reason: number): void => {
    hilog.info(0x0000, TAG, 'serverStopped， reason= ' + reason);
  });
} catch (err) {
  hilog.info(0x0000, TAG, 'start sever errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### ConnectResult

客户端调用connect()后，返回的连接结果。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 对端设备ID，成功返回对端设备的deviceId，失败返回空字符串。 |
| success | boolean | 否 | 否 | 连接结果，true表示连接成功，false表示连接失败。 |
| reason | number | 否 | 否 | 连接成功返回0，连接失败返回错误码： - 32390200：表示客户端连接超时。 - 32390201：表示服务端服务未启动。 - 32390300：表示内部错误。 更多关于错误码的详细介绍请参考[增强连接错误码](../../errors/增强连接错误码.md)。 |

#### Connection

连接对象，提供连接、断连、获取对端设备ID、发送数据、注册/取消注册回调等方法。

#### connect()

connect(): void

在客户端执行，向服务端设备发起连接，最大连接个数限制为10。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390204 | The number of connection exceeds the limit. |
| 32390300 | Internal error. |

**示例：**

客户端设备上的应用在创建Connection对象成功后，调用connect()方法连接目标设备（即服务端）。

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection sever deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  // 订阅连接结果
  connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
  });
  // 发起连接
  connection.connect();
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### disconnect()

disconnect(): void

业务执行完毕后，双端任意设备可调用该接口断开连接。创建的connection对象仍有效，需要时可调用connect()重新连接。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection sever deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
    if (result.success) {
      connection.disconnect();
    }
  });
  connection.connect();
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### close()

close(): void

业务执行完毕后，任意设备可调用该接口销毁connection对象，释放资源。若需再次与对端设备交互，必须重新创建connection对象并调用connect()发起连接。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection sever deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
    if (result.success) {
      connection.close();
    }
  });
  connection.connect();
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### getPeerDeviceId()

getPeerDeviceId(): string

获取对端设备的deviceId，作为对端设备的标识符，连接成功后或者被连接成功后调用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 对端设备的deviceId，即对端设备的BLE MAC地址。如果获取失败返回空字符串。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection sever deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.getPeerDeviceId();
  hilog.info(0x0000, TAG, "peerDeviceId=%{public}s" + connection.getPeerDeviceId());
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### sendData()

sendData(data: ArrayBuffer): void

客户端连接成功后，可以向服务端发送数据。服务端接收到连接回调时，也可以向客户端发送数据。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | ArrayBuffer | 是 | 需要发送的数据，最大发送长度为1024字节。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390205 | Connection is not ready. |
| 32390206 | Invalid parameter. |
| 32390300 | Internal error. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection sever deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
    if (result.success) {
      let len = 1;
      let arraybuffer = new ArrayBuffer(len); // 创建需要发送的数据
      connection.sendData(arraybuffer);
      hilog.info(0x0000, TAG, "sendData data connection peerDeviceId=%{public}s" + connection.getPeerDeviceId());
      connection.disconnect();
    }
  });
  connection.connect();
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### on('connectResult')

on(type: 'connectResult', callback: Callback<ConnectResult>): void

注册connect事件的回调监听，通过回调函数获取连接结果。使用callback进行异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectResult'，完成connect()调用，触发该事件。 |
| callback | Callback<ConnectResult> | 是 | 注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection sever deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  // 订阅连接结果
  connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
  });

  // 发起连接
  connection.connect();
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### off('connectResult')

off(type: 'connectResult', callback?: Callback<ConnectResult>): void

取消connect事件的回调监听，使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectResult'，完成connect()调用，触发该事件。 |
| callback | Callback<ConnectResult> | 否 | 注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection sever deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.on('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
  });
  // 取消订阅连接结果
  connection.off('connectResult', (result: linkEnhance.ConnectResult): void => {
    hilog.info(0x0000, TAG, 'clientConnectResultCallback result = ' + result.success);
  });
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### on('disconnected')

on(type: 'disconnected', callback: Callback<number>): void

注册disconnected事件的回调监听，连接被动断开或者底层异常断开时触发该事件。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'disconnected'，连接被动断开或底层异常断开时，触发该事件。 |
| callback | Callback<number> | 是 | 注册的回调函数，number为返回的错误码。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection sever deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  // 订阅断连通知
  connection.on('disconnected', (number: number) => {
    hilog.info(0x0000, TAG, 'connection disconnected reason = ' + number);
  });
} catch (err) {
  hilog.info(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### off('disconnected')

off(type: 'disconnected', callback?: Callback<number>): void

取消注册disconnected事件的回调监听。连接被动断开或底层异常断开时触发该事件，使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'disconnected'，连接被动断开或底层异常断开时，触发该事件。 |
| callback | Callback<number> | 否 | 注册的回调函数。number为返回的错误码。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection sever deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.on('disconnected', (number: number) => {
    hilog.info(0x0000, TAG, 'connection disconnected reason = ' + number);
  });
  // 取消订阅断连通知
  connection.off('disconnected', (number: number) => {
    hilog.info(0x0000, TAG, 'connection disconnected reason = ' + number);
  });
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### on('dataReceived')

on(type: 'dataReceived', callback: Callback<ArrayBuffer>): void

注册dataReceived事件的回调监听。使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'dataReceived'，收到数据时，触发该事件。 |
| callback | Callback<ArrayBuffer> | 是 | 注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection sever deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.connect();
  connection.on('dataReceived', (data: ArrayBuffer) => {
    hilog.info(0x0000, TAG, 'recv dataLen = ' + data.byteLength);
  });
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```

#### off('dataReceived')

off(type: 'dataReceived', callback?: Callback<ArrayBuffer>): void

取消dataReceived事件的回调监听，使用callback异步回调。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'dataReceived'，收到数据时，触发该事件。 |
| callback | Callback<ArrayBuffer> | 否 | 注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参考[增强连接错误码](增强连接错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390206 | Invalid parameter. |

**示例：**

```ets
import { linkEnhance } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "testDemo";

try {
  let peerDeviceId: string = "00:11:22:33:44:55";
  hilog.info(0x0000, TAG, 'connection sever deviceId = ' + peerDeviceId);
  let connection: linkEnhance.Connection = linkEnhance.createConnection(peerDeviceId, "demo");
  connection.on('dataReceived', (data: ArrayBuffer) => {
    hilog.info(0x0000, TAG, 'recv dataLen = ' + data.byteLength);
  });
  connection.off('dataReceived', (data: ArrayBuffer) => {
    hilog.info(0x0000, TAG, 'recv dataLen = ' + data.byteLength);
  });
} catch (err) {
  hilog.error(0x0000, TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' +
  (err as BusinessError).message);
}
```