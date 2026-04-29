# @ohos.data.cloudData (端云服务)

端云服务提供端云协同、端云共享和端云策略。

端云协同提供结构化数据（RDB Store）端云同步的能力。即：云作为数据的中心节点，通过与云的数据同步，实现数据云备份、同账号设备间的数据一致性。

端云配置提供端云同步策略配置的能力。

- 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { cloudData } from '@kit.ArkData';
```

#### StrategyType

云同步策略类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NETWORK | 0 | 通过网络同步策略。 |

#### NetWorkStrategy

网络策略参数枚举。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WIFI | 1 | WIFI网络策略。 |
| CELLULAR | 2 | 蜂窝网络策略。 |

#### cloudData.setCloudStrategy

setCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>

设置应用自身的云同步策略，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | StrategyType | 是 | 配置的策略类型。 |
| param | Array<commonType.ValueType> | 否 | 策略参数。当前仅支持设置网络策略，默认支持WIFI和蜂窝网络策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |

**样例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 仅WIFI同步
cloudData.setCloudStrategy(cloudData.StrategyType.NETWORK, [cloudData.NetWorkStrategy.WIFI]).then(() => {
    console.info('Succeeded in setting the cloud strategy');
}).catch((err: BusinessError) => {
    console.error(`Failed to set cloud strategy. Code: ${err.code}, message: ${err.message}`);
});
```