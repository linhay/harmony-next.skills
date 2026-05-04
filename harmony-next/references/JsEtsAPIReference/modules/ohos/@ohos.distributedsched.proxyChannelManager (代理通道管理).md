# @ohos.distributedsched.proxyChannelManager (代理通道管理)

软总线具备常驻运行能力，可为跨设备通信提供稳定可靠的底层通道。本模块基于软总线进程开发，支持手机与穿戴设备间高效的数据互通，可为用户提供无缝的设备互联体验。使用场景：手机侧APP与手表侧APP协同时，当手机APP不在前台被使用，手机应用的下行消息经由通知服务器，通过代理模块发送给手表侧。模块核心功能包括：代理通道管理、数据路由管理、 应用状态感知和唤醒、链路状态监听。

-

代理通道管理：通过蓝牙 BR 协议建立手机与穿戴设备的双向数据通道，支持的数据通道 ID 范围是[1,2147483647] 。

-

数据路由管理：基于 UUID 服务识别机制，精准转发穿戴设备数据。

-

应用状态感知和唤醒：代理通道使能后，收到穿戴设备发送的数据后，动态分析和唤醒手机端对应应用进程。

-

全链路状态监控：通过回调实时感知通道连接状态。

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

模型约束：此接口仅可在Stage模型下使用

#### 导入模块

```ets
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

#### 使用说明

调用模块接口前，需要完成如下配置。

1.

需要申请ohos.permission.ACCESS_BLUETOOTH权限。如何配置和申请权限，具体操作请参考[声明权限](../../guides/声明权限.md)和[向用户申请授权](../../guides/向用户申请授权.md)。

1.

对于需要代理拉起的应用进程，需要在module.json5文件中配置action字段: "action.ohos.pull.listener"。

#### proxyChannelManager.openProxyChannel

openProxyChannel(channelInfo: ChannelInfo): Promise<number>

打开代理通道，使用Promise异步回调返回结果。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| channelInfo | ChannelInfo | 是 | 对端设备及服务的MAC和UUID信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回代理通道的channelId，取值范围为1~2147483647。channelId的生命周期和代理通道生命周期相同，不关闭代理时，传入相同入参将返回相同channelId。 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码]([代理通道管理错误码](../../errors/代理通道管理错误码.md).md)和[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390001 | BR is disabled. |
| 32390002 | Device not paired. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |
| 32390102 | Operation failed or Connection timed out. |

**示例：**

```ets
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button("测试")
        .onClick(() => {
          let channelInfo: proxyChannelManager.ChannelInfo = {
            linkType: proxyChannelManager.LinkType.LINK_BR,
            peerDevAddr: "xx:xx:xx:xx:xx:xx", //穿戴设备蓝牙mac
            peerUuid: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", //穿戴侧监听的uuid
          };
          // 以下为使用 try/catch 判断
          try {
            proxyChannelManager.openProxyChannel(channelInfo)
              .then((channelId: number) => {
                // 获得通道id
              })
              .catch((error: BusinessError) => {
                console.error(`getErr: ${error.code} ${error.message}`);
              });
          } catch (err) {
            let error = err as BusinessError;
            console.error(`getErr: ${error.code} ${error.message}`);
            // 如果 code:undefined message:"Cannot read property openProxyChannel of undefined"， 则这个 API 在当前镜像不支持
          }
        })
    }
    .height('100%')
    .width('100%')
  }
```

#### proxyChannelManager.closeProxyChannel

closeProxyChannel(channelId: number): void

关闭已打开的代理通道。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| channelId | number | 是 | 打开代理通道时获取的channelId。 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码](代理通道管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

**示例：**

```ets
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button("测试")
        .onClick(() => {
          // 以下为使用 try/catch 判断
          try {
            proxyChannelManager.closeProxyChannel(1); // 假设通道id为1
          } catch (err) {
            let error = err as BusinessError;
            console.error(`getErr: ${error.code} ${error.message}`);
            // 如果 code:undefined message:"Cannot read property closeProxyChannel of undefined"， 则这个 API 在当前镜像不支持
          }
        })
    }
    .height('100%')
    .width('100%')
  }
```

#### proxyChannelManager.sendData

sendData(channelId:number, data:ArrayBuffer):Promise<void>

向对端发送数据，使用Promise异步回调。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| channelId | number | 是 | 打开代理通道时获取的channelId。 |
| data | ArrayBuffer | 是 | 向对端发送的字节消息，长度最大为4096个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回值的Promise的对象。 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码](代理通道管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |
| 32390103 | Data too long. |
| 32390104 | Send failed. |

**示例：**

```ets
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button("测试")
        .onClick(() => {
          const data = new ArrayBuffer(10); // 创建一个长度为 10 的 ArrayBuffer
          try {
            proxyChannelManager.sendData(1, data)// 假设通道id为1
              .then(() => {
              })
              .catch((error: BusinessError) => {
                console.error(`getErr: ${error.code} ${error.message}`);
              });
          } catch (err) {
            let error = err as BusinessError;
            console.error(`getErr: ${error.code} ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
```

#### proxyChannelManager.on('receiveData')

on(type: 'receiveData', channelId: number, callback: Callback<DataInfo>): void

订阅数据接收事件，使用异步回调。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置订阅类型，固定取值为'receiveData'。 |
| channelId | number | 是 | 打开代理通道时获取的channelId。 |
| callback | Callback<DataInfo> | 是 | 回调函数，返回接收到的数据。多次注册回调函数，最后一次注册的回调函数生效。 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码](代理通道管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

**示例：**

```ets
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button("测试")
        .onClick(() => {
          const receiveDataCallback = (dataInfo: proxyChannelManager.DataInfo) => {
          };
          try {
            proxyChannelManager.on('receiveData', 1, receiveDataCallback); // 假设通道id为1
          } catch (err) {
            let error = err as BusinessError;
            console.error(`register receiveData error: ${error.code} ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
```

#### proxyChannelManager.off('receiveData')

off(type: 'receiveData', channelId: number, callback?: Callback<DataInfo>): void

取消订阅数据接收事件，停止接收数据。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置订阅类型，固定取值为'receiveData'。 |
| channelId | number | 是 | 打开代理通道时获取的channelId。 |
| callback | Callback<DataInfo> | 否 | 注册的回调函数。如果为空、undefined、null，则取消订阅所有的数据接收事件。如果不为空，传入最后一次注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码](代理通道管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

**示例：**

```ets
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button("测试")
        .onClick(() => {
          try {
            proxyChannelManager.off('receiveData', 1); // 假设通道id为1
          } catch (err) {
            let error = err as BusinessError;
            console.error(`getErr: ${error.code} ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
```

#### proxyChannelManager.on('channelStateChange')

on(type: 'channelStateChange', channelId: number, callback: Callback<ChannelStateInfo>): void

订阅通道状态事件，使用callback进行异步回调。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置订阅类型，固定取值为'channelStateChange'。 |
| channelId | number | 是 | 打开代理通道时获取的channelId。 |
| callback | Callback<ChannelStateInfo> | 是 | 回调函数，返回接收到的通道状态。多次注册callback，最后一次注册的callback生效 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码](代理通道管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

**示例：**

```ets
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button("测试")
        .onClick(() => {
          const receiveStatusCallback = (channelStateInfo: proxyChannelManager.ChannelStateInfo) => {
          };
          try {
            proxyChannelManager.on('channelStateChange', 1, receiveStatusCallback); // 假设打开的通道id为1
          } catch (err) {
            let error = err as BusinessError;
            console.error(`getErr: ${error.code} ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
```

#### proxyChannelManager.off('channelStateChange')

off(type: 'channelStateChange', channelId: number, callback?: Callback<ChannelStateInfo>): void

取消订阅通道状态事件。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

模型约束：此接口仅可在Stage模型下使用

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置订阅类型为'channelStateChange'。 |
| channelId | number | 是 | 打开代理通道时获取的channelId。 |
| callback | Callback<ChannelStateInfo> | 否 | 注册的回调函数。如果为空、undefined、null，则取消订阅所有的数据接收事件。如果不为空，传入最后一次注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码](代理通道管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

**示例：**

```ets
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button("测试")
        .onClick(() => {
          try {
            proxyChannelManager.off('channelStateChange', 1); // 假设打开的通道id为1
          } catch (err) {
            let error = err as BusinessError;
            console.error(`getErr: ${error.code} ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
```

#### DataInfo

存放接收的数据信息，包括通道Id和数据。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| channelId | number | 否 | 否 | 代理通道的channelId。 |
| data | ArrayBuffer | 否 | 否 | 接收到的字节数据。 |

#### ChannelInfo

打开代理通道函数的入参，包括对端设备的MAC地址和监听服务的UUID。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| linkType | LinkType | 否 | 否 | 代理通道的链路类型。 |
| peerDevAddr | string | 否 | 否 | 对端设备的MAC地址。 |
| peerUuid | string | 否 | 否 | 对端监听的服务的UUID。 |

#### ChannelStateInfo

当代理通道状态变化时，用于表示代理通道的连接状态。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| channelId | number | 否 | 否 | 代理通道的channelId。 |
| state | ChannelState | 否 | 否 | 通道的连接状态。 |

#### ChannelState

通道状态发生变化时，代理通道上报的通道连接状态。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CHANNEL_WAIT_RESUME | 0 | 连接已断开，通道不可用。 |
| CHANNEL_RESUME | 1 | 连接已恢复，通道可用。 |
| CHANNEL_EXCEPTION_SOFTWARE_FAILED | 2 | 其他软件错误导致通道不可用。 |
| CHANNEL_BR_NO_PAIRED | 3 | 蓝牙配对关系被删除，通道不可用。 |

#### LinkType

链路类型。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LINK_BR | 0 | 蓝牙。 |