# @ohos.bluetooth.pan (蓝牙pan模块)

本模块提供基于蓝牙个人局域网协议（Personal Area Networking，[PAN](../../guides/Connectivity Kit术语.md#pan)）的蓝牙共享网络能力，支持获取连接状态等方法。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { pan } from '@kit.ConnectivityKit';
```

#### BaseProfile

type BaseProfile = baseProfile.BaseProfile

基础Profile接口定义，提供订阅和获取连接状态等公共能力。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| baseProfile.BaseProfile | 基础Profile接口定义。 |

#### pan.createPanProfile

createPanProfile(): PanProfile

创建蓝牙[NAP](../../guides/Connectivity Kit术语.md#nap)实例。通过该实例可使用本端作为NAP设备的接口，如：获取和其他设备间的蓝牙个人局域网服务连接状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PanProfile | 返回NAP实例。 - 该类继承于BaseProfile，因此可以使用其父类中的方法。 - 和该实例角色相对应的是PANU角色。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码]([蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let panProfile : pan.PanProfile= pan.createPanProfile();
    console.info('pan success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```