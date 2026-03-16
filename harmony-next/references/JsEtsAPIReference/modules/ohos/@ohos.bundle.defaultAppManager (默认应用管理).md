# @ohos.bundle.defaultAppManager (默认应用管理)

本模块提供查询默认应用的能力，支持查询当前应用是否是默认应用。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { defaultAppManager } from '@kit.AbilityKit';
```

#### ApplicationType

默认应用的应用类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

名称值说明BROWSERWeb Browser默认浏览器。IMAGEImage Gallery默认图片查看器。AUDIOAudio Player默认音频播放器。VIDEOVideo Player默认视频播放器。PDFPDF Viewer默认PDF文档查看器。WORDWord Viewer默认WORD文档查看器。EXCELExcel Viewer默认EXCEL文档查看器。PPTPPT Viewer默认PPT文档查看器。EMAIL12+Email默认邮件。

#### defaultAppManager.isDefaultApplication

isDefaultApplication(type: string): Promise<boolean>

根据系统已定义的应用类型或者[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md)类型判断当前应用是否是该类型的默认应用。使用Promise异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**参数：**

参数名类型必填说明typestring是要查询的应用类型，取[ApplicationType](#ZH-CN_TOPIC_0000002529284605__applicationtype)或者[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md)类型中的值。

**返回值：**

类型说明Promise<boolean>Promise对象，返回当前应用是否是默认应用，true表示是默认应用，false表示不是默认应用。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.801Capability not supported.

**示例：**

```ets
import { defaultAppManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

defaultAppManager.isDefaultApplication(defaultAppManager.ApplicationType.BROWSER)
  .then((data) => {
    console.info('Operation successful. IsDefaultApplication ? ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
});
```

#### defaultAppManager.isDefaultApplication

isDefaultApplication(type: string, callback: AsyncCallback<boolean>): void

根据系统已定义的应用类型或者[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md)类型判断当前应用是否是该类型的默认应用。使用callback异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**参数：**

参数名类型必填说明typestring是要查询的应用类型，取[ApplicationType](#ZH-CN_TOPIC_0000002529284605__applicationtype)或者[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md)类型中的值。callbackAsyncCallback<boolean>是[回调函数](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__asynccallback)，当获取成功时，err为null，data为bool值，true表示是默认应用，false表示不是默认应用；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.801Capability not supported.

**示例：**

```ets
import { defaultAppManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

defaultAppManager.isDefaultApplication(defaultAppManager.ApplicationType.BROWSER, (err: BusinessError, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. IsDefaultApplication ? ' + JSON.stringify(data));
});
```

#### defaultAppManager.isDefaultApplicationSync10+

isDefaultApplicationSync(type: string): boolean

以同步方法根据系统已定义的应用类型或者[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md)类型判断当前应用是否是该类型的默认应用，使用boolean形式返回结果。

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**参数：**

参数名类型必填说明typestring是要查询的应用类型，取[ApplicationType](#ZH-CN_TOPIC_0000002529284605__applicationtype)或者[UniformDataType](@ohos.data.uniformTypeDescriptor (标准化数据定义与描述).md)类型中的值。

**返回值：**

类型说明boolean返回当前应用是否是默认应用，true表示是默认应用，false表示不是默认应用。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.801Capability not supported.

**示例：**

```ets
import { defaultAppManager } from '@kit.AbilityKit';

try {
  let data = defaultAppManager.isDefaultApplicationSync(defaultAppManager.ApplicationType.BROWSER)
  console.info('Operation successful. IsDefaultApplicationSync ? ' + JSON.stringify(data));
} catch (error) {
  console.error('Operation failed. Cause: ' + JSON.stringify(error));
}
```