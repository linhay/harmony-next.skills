# @ohos.sendableResourceManager (资源管理)

资源管理导入sendableResourceManager模块，通过调用[resourceToSendableResource](#ZH-CN_TOPIC_0000002529285309__sendableresourcemanagerresourcetosendableresource)和[sendableResourceToResource](#ZH-CN_TOPIC_0000002529285309__sendableresourcemanagersendableresourcetoresource)方法可以将[Resource](#ZH-CN_TOPIC_0000002529285309__resource)对象和[SendableResource](#ZH-CN_TOPIC_0000002529285309__sendableresource)对象进行互转。

Resource对象通过转换为SendableResource对象后，可以被[Sendable类](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable)持有。Sendable类在跨线程传输后，取出持有的SendableResource对象转为Resource对象，作为参数获取资源。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { sendableResourceManager } from '@kit.LocalizationKit';
```

#### sendableResourceManager.resourceToSendableResource

resourceToSendableResource(resource: Resource): SendableResource

将Resource对象转换为SendableResource对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.ResourceManager

**参数：**

参数名类型必填说明resource[Resource](#ZH-CN_TOPIC_0000002529285309__resource)是Resource对象。

**返回值：**

类型说明[SendableResource](#ZH-CN_TOPIC_0000002529285309__sendableresource)转换后的SendableResource对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed.

**示例：**

```ets
// 资源文件路径: src/main/resources/base/element/string.json
{
  "string": [
    {
      "name": "test",
      "value": "I'm a test string resource."
    }
  ]
}
```

```ets
import { sendableResourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let sendableResource: sendableResourceManager.SendableResource = sendableResourceManager.resourceToSendableResource($r('app.string.test'));
} catch (error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    console.error(`resourceToSendableResource failed, error code: ${code}, message: ${message}.`);
}
```

#### sendableResourceManager.sendableResourceToResource

sendableResourceToResource(resource: SendableResource): Resource

将SendableResource对象转换为Resource对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Global.ResourceManager

**参数：**

参数名类型必填说明resource[SendableResource](#ZH-CN_TOPIC_0000002529285309__sendableresource)是SendableResource对象。

**返回值：**

类型说明[Resource](#ZH-CN_TOPIC_0000002529285309__resource)转换后的Resource对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed.

**示例：**

```ets
// 资源文件路径: src/main/resources/base/element/string.json
{
  "string": [
    {
      "name": "test",
      "value": "I'm a test string resource."
    }
  ]
}
```

```ets
import { sendableResourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let resource: sendableResourceManager.Resource = sendableResourceManager.sendableResourceToResource(sendableResourceManager.resourceToSendableResource($r('app.string.test')));
} catch (error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    console.error(`sendableResourceToResource failed, error code: ${code}, message: ${message}.`);
}
```

#### Resource

type Resource = _Resource

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

类型说明[_Resource](../../topics/system-services/Resource.md#ZH-CN_TOPIC_0000002497445340__resource-1)表示Resource资源信息。

#### SendableResource

type SendableResource = _SendableResource

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

类型说明[_SendableResource](../../topics/system-services/SendableResource.md#ZH-CN_TOPIC_0000002529285311__sendableresource-1)表示SendableResource资源信息。