# cloudFunction (云函数模块)

本模块提供调用云函数的能力。

起始版本： 5.0.0(12)

**导入模块**

```ets
import { cloudFunction } from '@kit.CloudFoundationKit';
```

**call**

call(parameters: FunctionParams, callback: AsyncCallback<FunctionResult>): void

调用云函数时使用，使用云函数实现的功能。使用callback异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

需要权限： ohos.permission.INTERNET

系统能力： SystemCapability.DeviceCloudGateway.CloudFoundation

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameters | FunctionParams | 是 | 云函数调用必备参数。 |
| callback | AsyncCallback<FunctionResult> | 是 | 回调函数。当调用云函数成功，err为undefined，data为获取到的FunctionResult；否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS错误码](ArkTS错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1008210001 | Network connection error. |
| 1008210009 | Client internal error. |
| 1008211001 | Server error. |

示例：

```ets
import { cloudFunction } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

cloudFunction.call({
  name: 'my-handler-xxxx',
  version: '$latest',
  timeout: 10 * 1000,
  data: {
    param1: 'val1',
    param2: 'val2'
  }
}, (err: BusinessError, value: cloudFunction.FunctionResult) => {
  if (err) {
    hilog.error(0x0000, 'testTag', `Failed to call the function, code: ${err.code}, message: ${err.message}`);
    return;
  }
  hilog.info(0x0000, 'testTag', `Succeeded in calling the function, result: ${JSON.stringify(value.result)}`);
})
```

**call**

call(parameters: FunctionParams): Promise<FunctionResult>

调用云函数时使用，使用云函数实现的功能。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

需要权限： ohos.permission.INTERNET

系统能力： SystemCapability.DeviceCloudGateway.CloudFoundation

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameters | FunctionParams | 是 | 云函数调用必备参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<FunctionResult> | Promise对象，返回函数调用结果。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS错误码](ArkTS错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1008210001 | Network connection error. |
| 1008210009 | Client internal error. |
| 1008211001 | Server error. |

示例：

```ets
import { cloudFunction } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

cloudFunction.call({
  name: 'my-handler-xxxx',
  version: '$latest',
  timeout: 10 * 1000,
  data: {
    param1: 'val1',
    param2: 'val2'
  }
}).then((value: cloudFunction.FunctionResult) => {
  hilog.info(0x0000, 'testTag', `Succeeded in calling the function, result: ${JSON.stringify(value.result)}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `Failed to call the function, code: ${err.code}, message: ${err.message}`);
})
```

**FunctionParams**

云函数调用参数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudFoundation

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 云函数名称。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| data | string | Object | 否 | 是 | 函数请求体。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| version | string | 否 | 是 | 云函数版本，默认是‘$latest’，表示最新版本。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| timeout | number | 否 | 是 | 函数请求超时时间，单位毫秒，默认为70*1000毫秒。 取值范围无限制，会转成unsigned long类型。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| loadMode | LoadMode | 否 | 是 | 函数请求加载模式，默认为NORMAL。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| localUrl | string | 否 | 是 | 本地启动的云函数地址，格式为http://域名:端口，例如http://localhost:18090。 该参数仅在调试本地云函数阶段需要使用，调试完成将云函数部署至云侧后不能再使用。 起始版本： 6.0.1(21) 元服务API： 从版本6.0.1(21)开始，该接口支持在元服务中使用。 |

**LoadMode**

枚举， 函数请求加载模式。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudFoundation

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 普通模式，每次调用call方法均需请求服务器拉取数据。 |
| PRELOAD | 1 | 预加载模式，仅在安装应用时返回一次结果数据，后续调用将返回错误。 设备行为差异： 该参数在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中传此参数时，返回1008211001错误码。 说明： HarmonyOS 5.0.3版本增强了预加载功能，将多种预加载能力（如安装预加载、周期性预加载）整合进了一套全新的API中，使体验更加友好，具体请参见cloudResPrefetch（预加载模块）。 |

**FunctionResult**

云函数返回的结果。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudFoundation

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | string | Object | 否 | 否 | 云函数返回的结果。 |