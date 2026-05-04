# @ohos.bundle.overlay (overlay模块)

本模块提供overlay特征应用的[OverlayModuleInfo](OverlayModuleInfo.md)信息查询以及禁用使能的能力。

overlay特征应用指应用中包含有overlay资源包，overlay资源包详见[overlay机制](../../guides/资源分类与访问.md#overlay机制)。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅适用于stage模型，且仅适用于[静态overlay](../../guides/资源分类与访问.md#静态overlay配置方式)。

#### 导入模块

```ets
import { overlay } from '@kit.AbilityKit';
```

#### overlay.setOverlayEnabled

setOverlayEnabled(moduleName:string, isEnabled: boolean): Promise<void>

设置当前应用中overlay特征module的禁用使能状态。使用Promise异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | overlay特征module的名称。 |
| isEnabled | boolean | 是 | 值为true表示使能，值为false表示禁用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[ohos.bundle错误码](包管理子系统通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700033 | The specified module is not an overlay module. |

**示例：**

```ets
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let moduleName = "feature";
let isEnabled = false;

try {
  overlay.setOverlayEnabled(moduleName, isEnabled)
    .then(() => {
      console.info('setOverlayEnabled success');
    }).catch((err: BusinessError) => {
    console.error('setOverlayEnabled failed due to err code: ' + err.code + ' ' + 'message:' + err.message);
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('setOverlayEnabled failed due to err code: ' + code + ' ' + 'message:' + message);
}
```

#### overlay.setOverlayEnabled

setOverlayEnabled(moduleName: string, isEnabled: boolean, callback: AsyncCallback<void>): void

设置当前应用中overlay module的禁用使能状态。使用callback异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | overlay特征module的名称。 |
| isEnabled | boolean | 是 | 值为true表示使能，值为false表示禁用。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当设置指定module的overlay禁用使能状态成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.bundle错误码](包管理子系统通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700033 | The specified module is not an overlay module. |

**示例：**

```ets
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let moduleName = "feature";
let isEnabled = false;

try {
  overlay.setOverlayEnabled(moduleName, isEnabled, (err, data) => {
    if (err) {
      console.error('setOverlayEnabled failed due to err code: ' + err.code + ' ' + 'message:' + err.message);
      return;
    }
    console.info('setOverlayEnabled success');
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('setOverlayEnabled failed due to err code: ' + code + ' ' + 'message:' + message);
}
```

#### overlay.get[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)

get[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)(moduleName: string): Promise<OverlayModuleInfo>

获取当前应用中overlay特征module的[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)信息。使用Promise异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 指定当前应用中的overlay module的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)> | Promise对象，返回OverlayModuleInfo。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.bundle错误码](包管理子系统通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700032 | The specified bundle does not contain any overlay module. |
| 17700033 | The specified module is not an overlay module. |

**示例：**

```ets
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let moduleName = "feature";

(async () => {
  try {
    let overlayModuleInfo = await overlay.getOverlayModuleInfo(moduleName);
    console.info('overlayModuleInfo is ' + JSON.stringify(overlayModuleInfo));
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error('getOverlayModuleInfo failed due to err code : ' + code + ' ' + 'message :' + message);
  }
})();
```

#### overlay.get[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)

get[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)(moduleName: string, callback: AsyncCallback<OverlayModuleInfo>): void

获取当前应用中overlay特征module的[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)信息。使用callback异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 指定当前应用中的overlay特征module的名称。 |
| callback | AsyncCallback<[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)> | 是 | 回调函数，当获取当前应用中指定的module的OverlayModuleInfo信息成功时，err返回null。否则回调函数返回具体错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.bundle错误码](包管理子系统通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700032 | The specified bundle does not contain any overlay module. |
| 17700033 | The specified module is not an overlay module. |

**示例：**

```ets
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let moduleName = "feature";

try {
  overlay.getOverlayModuleInfo(moduleName, (err, data) => {
    if (err) {
      console.error('getOverlayModuleInfo failed due to err code : ' + err.code + ' ' + 'message :' + err.message);
      return;
    }
    console.info('overlayModuleInfo is ' + JSON.stringify(data));
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('getOverlayModuleInfo failed due to err code : ' + code + ' ' + 'message :' + message);
}
```

#### overlay.getTarget[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)s

getTarget[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)s(targetModuleName: string): Promise<Array<OverlayModuleInfo>>

获取指定的目标module所关联的[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)。overlay特征的module一般是为设备上存在的非overlay特征的module提供覆盖的资源文件，其中非overlay特征的module被称作目标module。使用Promise异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetModuleName | string | 是 | 指定当前应用中的目标module的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)>> | Promise对象，返回<Array<OverlayModuleInfo>>。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.bundle错误码](包管理子系统通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700034 | The specified module is an overlay module. |

**示例：**

```ets
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let targetModuleName = "feature";

(async () => {
  try {
    let overlayModuleInfos = await overlay.getTargetOverlayModuleInfos(targetModuleName);
    console.info('overlayModuleInfos are ' + JSON.stringify(overlayModuleInfos));
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error('getTargetOverlayModuleInfos failed due to err code : ' + code + ' ' + 'message :' + message);
  }
})();
```

#### overlay.getTarget[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)s

getTarget[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)s(targetModuleName: string, callback: AsyncCallback<Array<OverlayModuleInfo>>): void

获取指定的目标module所关联的[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)。overlay特征的module一般是为设备上存在的非overlay特征的module提供覆盖的资源文件，其中非overlay特征的module被称作目标module。使用callback异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetModuleName | string | 是 | 指定当前应用中的目标module的名称。 |
| callback | AsyncCallback<Array<[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)>> | 是 | 回调函数，当获取指定的目标module的OverlayModuleInfo成功时，err返回null。否则回调函数返回具体错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[ohos.bundle错误码](包管理子系统通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700034 | The specified module is an overlay module. |

**示例：**

```ets
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let targetModuleName = "feature";

try {
  overlay.getTargetOverlayModuleInfos(targetModuleName, (err, data) => {
    if (err) {
      console.error('getTargetOverlayModuleInfos failed due to err code : ' + err.code + ' ' + 'message :' +
      err.message);
      return;
    }
    console.info('overlayModuleInfo is ' + JSON.stringify(data));
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('getTargetOverlayModuleInfos failed due to err code : ' + code + ' ' + 'message :' + message);
}
```

#### [OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)

type [OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md) = [_OverlayModuleInfo.OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md#ZH-CN_TOPIC_0000002497604636__overlaymoduleinfo-1)

[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md)信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

| 类型 | 说明 |
| --- | --- |
| _[OverlayModuleInfo](../../topics/misc/OverlayModuleInfo.md).OverlayModuleInfo | OverlayModuleInfo信息。 |