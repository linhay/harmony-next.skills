# @system.network (网络状态)

-

本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

从API Version 8 开始，该接口不再维护，推荐使用新接口['@ohos.net.connection'](@ohos.net.connection (网络连接管理).md)。

#### 导入模块

```ets
import network from '@system.network';
```

#### 权限列表

ohos.permission.GET_WIFI_INFO

ohos.permission.GET_NETWORK_INFO

#### network.getType3+

getType(options?: {

 success?: (data: NetworkResponse) => void;

 fail?: (data: any, code: number) => void;

 complete?: () => void;

}): void

获取当前设备的网络类型。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明successFunction否接口调用成功的回调函数，返回值为[NetworkResponse](#ZH-CN_TOPIC_0000002497445500__networkresponse3)。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

fail返回值：

错误码说明602当前权限未声明。

**示例：**

```ets
export default class Network {
  getType() {
    network.getType({
      success: (data) => {
        console.info('success get network type:' + data.type);
      }
    });
  }
}
```

#### network.subscribe3+

subscribe(options?:{

 success?: (data: NetworkResponse) => void;

 fail?: (data: any, code: number) => void;

 }): void

订阅当前设备的网络连接状态。如果多次调用，会覆盖前一次调用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

参数名类型必填说明successFunction否网络发生变化的回调函数。返回值为[NetworkResponse](#ZH-CN_TOPIC_0000002497445500__networkresponse3)。failFunction否接口调用失败的回调函数。

fail返回值：

错误码说明602当前权限未声明。200订阅失败。

**示例：**

```ets
export default class Network {
  subscribe() {
    network.subscribe({
      success: (data) => {
        console.info('success get network type:' + data.type);
      }
    });
  }
}
```

#### network.unsubscribe3+

unsubscribe(): void

取消订阅设备的网络连接状态。

**系统能力：** SystemCapability.Communication.NetManager.Core

**示例：**

```ets
import network from '@system.network';

network.unsubscribe();
```

#### NetworkResponse3+

**系统能力：** SystemCapability.Communication.NetManager.Core

名称类型只读可选说明meteredboolean否是是否按照流量计费。true：按照流量计费；false：不按照流量计费。typestring否否网络类型，可能的值有2g，3g，4g，5g，wifi，none等。