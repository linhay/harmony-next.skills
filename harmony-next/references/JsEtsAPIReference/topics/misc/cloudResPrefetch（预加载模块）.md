# cloudResPrefetch（预加载模块）

本模块提供调用预加载的能力。

起始版本：5.0.3(15)

**导入模块**

```ets
import { cloudResPrefetch } from '@kit.CloudFoundationKit';
```

**registerPrefetchTask**

registerPrefetchTask(options: PrefetchOptions): void

注册周期性预加载任务。周期性预加载适用，安装预加载不涉及。在应用启动后，需显式调用本接口，调用成功后才可触发周期性预加载任务。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudResPrefetch

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | PrefetchOptions | 是 | 周期性预加载任务的初始化配置参数。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS错误码](ArkTS错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1008240009 | Client internal error. |

示例：

```ets
import { cloudResPrefetch } from '@kit.CloudFoundationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  cloudResPrefetch.registerPrefetchTask({
    token: "testToken",
    params: "testParams"
  });
  hilog.info(0x0000, 'testTag', `Succeeded in registering prefetch task`);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to register prefetch task`);
}
```

**PrefetchOptions**

周期性预加载任务初始化配置参数。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudResPrefetch

起始版本： 5.0.3(15)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| token | string | 否 | 是 | 自定义用户级别的访问令牌。会携带透传至开发者自己的函数中，由开发者自行完成认证。 |
| params | string | Object | 否 | 是 | 自定义参数。会携带透传至开发者自己的函数中，由开发者自行定义并解析。 |

**getPrefetchResult**

getPrefetchResult(mode: PrefetchMode, callback: AsyncCallback<PrefetchResult>, params?: PrefetchParams): void

获取预加载数据。安装预加载和周期性预加载均适用。使用callback异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudResPrefetch

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | PrefetchMode | 是 | 预加载类型。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| callback | AsyncCallback<PrefetchResult> | 是 | 回调函数。当获取预加载数据成功，err为undefined，data为获取到的PrefetchResult；否则为错误对象。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| params | PrefetchParams | 否 | 预加载参数。 起始版本： 6.1.0(23) 说明： 元服务不支持该字段。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS错误码](ArkTS错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1008240009 | Client internal error. |

示例：

```ets
import { cloudResPrefetch } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 获取安装预加载数据
cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.INSTALL_PREFETCH,
  (err: BusinessError, data: cloudResPrefetch.PrefetchResult) => {
    if (err) {
      hilog.error(0x0000, 'testTag', `Failed to get install prefetch data, code: ${err.code}, message: ${err.message}`);
    } else {
      hilog.info(0x0000, 'testTag',
        `Succeeded in getting install prefetch data, result: ${JSON.stringify(data.result)}`);
    }
  });

// 获取周期性预加载数据
cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH,
  (err: BusinessError, data: cloudResPrefetch.PrefetchResult) => {
    if (err) {
      hilog.error(0x0000, 'testTag',
        `Failed to get periodic prefetch data, code: ${err.code}, message: ${err.message}`);
    } else {
      hilog.info(0x0000, 'testTag',
        `Succeeded in getting periodic prefetch data, result: ${JSON.stringify(data.result)}`);
    }
  });

// 获取跳链安装预加载数据
let params: cloudResPrefetch.PrefetchParams = {
  link: 'link' // 需要替换为延迟链接
}
cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.LINK_PREFETCH,
  (err: BusinessError, data: cloudResPrefetch.PrefetchResult) => {
    if (err) {
      hilog.error(0x0000, 'testTag',
        `Failed to get link prefetch data, code: ${err.code}, message: ${err.message}`);
    } else {
      hilog.info(0x0000, 'testTag',
        `Succeeded in getting link prefetch data, result: ${JSON.stringify(data.result)}`);
    }
  }, params);
```

**getPrefetchResult**

getPrefetchResult(mode: PrefetchMode, params?: PrefetchParams): Promise<PrefetchResult>

获取预加载数据。安装预加载和周期性预加载均适用。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudResPrefetch

起始版本： 5.0.3(15)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | PrefetchMode | 是 | 预加载类型。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| params | PrefetchParams | 否 | 预加载参数。 起始版本： 6.1.0(23) 说明： 元服务不支持该字段。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<PrefetchResult> | Promise对象，返回获取的预加载数据。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS错误码](ArkTS错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1008240009 | Client internal error. |

示例：

```ets
import { cloudResPrefetch } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 获取安装预加载数据
cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.INSTALL_PREFETCH)
  .then((data: cloudResPrefetch.PrefetchResult) => {
    hilog.info(0x0000, 'testTag', `Succeeded in getting install prefetch data, result: ${JSON.stringify(data.result)}`);
  })
  .catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', `Failed to get install prefetch data, code: ${err.code}, message: ${err.message}`);
  });

// 获取周期性预加载数据
cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH)
  .then((data: cloudResPrefetch.PrefetchResult) => {
    hilog.info(0x0000, 'testTag',
      `Succeeded in getting periodic prefetch data, result: ${JSON.stringify(data.result)}`);
  })
  .catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', `Failed to get periodic prefetch data, code: ${err.code}, message: ${err.message}`);
  });

// 获取跳链安装预加载数据
let params: cloudResPrefetch.PrefetchParams = {
  link: 'link' // 需要替换为延迟链接
}
cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.LINK_PREFETCH, params)
  .then((data: cloudResPrefetch.PrefetchResult) => {
    hilog.info(0x0000, 'testTag',
      `Succeeded in getting link prefetch data, result: ${JSON.stringify(data.result)}`);
  })
  .catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', `Failed to get link prefetch data, code: ${err.code}, message: ${err.message}`);
  });
```

**PrefetchMode**

枚举， 预加载类型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudResPrefetch

起始版本： 5.0.3(15)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INSTALL_PREFETCH | 1 | 安装预加载。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| PERIODIC_PREFETCH | 2 | 周期性预加载。 元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| LINK_PREFETCH | 3 | 跳链安装预加载。 起始版本： 6.1.0(23) 说明： 元服务不支持该字段。 |

**PrefetchParams**

预加载参数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudResPrefetch

起始版本： 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| link | string | 否 | 是 | 跳链安装预加载延迟链接。 说明： 元服务不支持该字段。 |

**PrefetchResult**

获取预加载数据返回的结果。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.3(15)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.DeviceCloudGateway.CloudResPrefetch

起始版本： 5.0.3(15)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | string | Object | 否 | 否 | 返回的预加载数据，字符串或JSON字符串转换的Object对象。 |
| timestamp | Date | 否 | 否 | 返回的预加载数据时间戳，UTC时间格式。 |
| token | string | 否 | 否 | 返回注册周期性预加载任务时所用的Token。 |