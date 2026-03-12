# AAID（应用匿名标识符）

本模块提供了开发者获取和删除应用匿名标识符（AAID，Anonymous Application Identifier）的能力。AAID用于标识应用身份。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Push.PushService

**起始版本：**4.0.0(10)

#### 导入模块

```ets
import { AAID } from '@kit.PushKit';
```

#### AAID.getAAID

getAAID(callback: AsyncCallback<string>): void

获取AAID，使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：**4.0.0(10)

**参数：**

参数名

类型

必填

说明

callback

AsyncCallback<string>

是

回调函数。当获取AAID成功，err为undefined，data为获取到的AAID，字符长度为36；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-error-code)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

1000900001

System internal error.

1000900006

Failed to connect to the AAID service.

1000900007

Internal error of the AAID service.

**示例：**

```ets
import { AAID } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  AAID.getAAID((err: BusinessError, data: string) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'Failed to get AAID: %{public}d %{public}s', err.code, err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'Succeeded in getting AAID');
    }
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to get AAID: %{public}d %{public}s', e.code, e.message);
}
```

#### AAID.getAAID

getAAID(): Promise<string>

获取AAID，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：**4.0.0(10)

**返回值：**

类型

说明

Promise<string>

Promise对象，返回AAID，字符长度为36。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

1000900001

System internal error.

1000900006

Failed to connect to the AAID service.

1000900007

Internal error of the AAID service.

**示例：**

```ets
import { AAID } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  AAID.getAAID().then((data: string) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in getting AAID');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to get AAID: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to get AAID: %{public}d %{public}s', e.code, e.message);
}
```

#### AAID.deleteAAID

deleteAAID(callback: AsyncCallback<void>): void

删除AAID，使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：**4.0.0(10)

**参数：**

参数名

类型

必填

说明

callback

AsyncCallback<void>

是

回调函数。当删除AAID成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

1000900001

System internal error.

1000900006

Failed to connect to the AAID service.

1000900007

Internal error of the AAID service.

**示例：**

```ets
import { AAID } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  AAID.deleteAAID((err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'Failed to delete AAID: %{public}d %{public}s', err.code, err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'Succeeded in deleting AAID.');
    }
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to delete AAID: %{public}d %{public}s', e.code, e.message);
}
```

#### AAID.deleteAAID

deleteAAID(): Promise<void>

删除AAID，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：**4.0.0(10)

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

1000900001

System internal error.

1000900006

Failed to connect to the AAID service.

1000900007

Internal error of the AAID service.

**示例：**

```ets
import { AAID } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  AAID.deleteAAID().then(() => {
    hilog.info(0x0000, 'testTag', 'Succeeded in deleting AAID');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to delete AAID: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to delete AAID: %{public}d %{public}s', e.code, e.message);
}
```