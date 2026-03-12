# @ohos.bluetooth.map (蓝牙map模块)

本模块提供基于消息访问协议（Message Access Profile，[MAP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#map)）的蓝牙消息访问能力，支持获取连接状态等方法。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { map } from '@kit.ConnectivityKit';
```

#### BaseProfile

type BaseProfile = baseProfile.BaseProfile

基础Profile接口定义，提供订阅和获取连接状态等公共能力。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

类型说明[baseProfile.BaseProfile](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002497445438__baseprofile)基础Profile接口定义。

#### map.createMapMseProfile

createMapMseProfile(): MapMseProfile

创建蓝牙消息访问协议中的[MSE](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#mse)实例。通过该实例可使用本端作为MSE设备的接口，如：获取和其他设备间的蓝牙消息服务连接状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

类型说明MapMseProfile返回该profile的实例。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let mapMseProfile = map.createMapMseProfile();
    console.info('MapMse success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### MapMseProfile

该实例表示蓝牙消息访问协议中的[MSE](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#mse)角色。

- 该类继承于[BaseProfile](#ZH-CN_TOPIC_0000002529445387__baseprofile)，因此可以使用其父类中的方法。
- 使用该类的接口前，需通过[createMapMseProfile](#ZH-CN_TOPIC_0000002529445387__mapcreatemapmseprofile)接口构造该类的实例。
- 和该实例角色相对应的是[MCE](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#mce)角色。