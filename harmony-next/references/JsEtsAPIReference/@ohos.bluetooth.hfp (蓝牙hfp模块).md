# @ohos.bluetooth.hfp (蓝牙hfp模块)

本模块提供基于免提协议（Hands-Free Profile， [HFP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#hfp)）的蓝牙通话音频能力，支持获取连接状态等方法。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { hfp } from '@kit.ConnectivityKit';
```

#### BaseProfile

type BaseProfile = baseProfile.BaseProfile

基础Profile接口定义，提供订阅和获取连接状态等公共能力。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

类型说明[baseProfile.BaseProfile](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002497445438__baseprofile)基础Profile接口定义。

#### hfp.createHfpAgProfile

createHfpAgProfile(): HandsFreeAudioGatewayProfile

创建蓝牙通话音频中的[HFP AG](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#hfp-ag)实例。通过该实例可使用本端作为HFP AG设备的接口，如：获取和其他设备间的蓝牙通话音频连接状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

类型说明[HandsFreeAudioGatewayProfile](#ZH-CN_TOPIC_0000002529285411__handsfreeaudiogatewayprofile)返回HFP AG实例。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let hfpAgProfile = hfp.createHfpAgProfile();
    console.info('hfpAg success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### HandsFreeAudioGatewayProfile

该实例表示蓝牙通话音频中的[HFP AG](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#hfp-ag)角色‌。

- 该类继承于[BaseProfile](#ZH-CN_TOPIC_0000002529285411__baseprofile)，因此可以使用其父类中的方法。
- 使用该类的接口前，需通过[createHfpAgProfile](#ZH-CN_TOPIC_0000002529285411__hfpcreatehfpagprofile)接口构造该类的实例。
- 和该实例角色相对应的是[HF](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#hf)角色。