# ProcessInformation

运行进程信息，可以通过appManager的[getRunningProcessInformation](@ohos.app.ability.appManager (应用管理).md#ZH-CN_TOPIC_0000002522080556__appmanagergetrunningprocessinformation)来获取运行进程信息。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**导入模块**

```ets
import { appManager } from '@kit.AbilityKit';
```

**属性**

系统能力：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 否 | 进程ID。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| uid | number | 否 | 否 | 应用程序的UID。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| processName | string | 否 | 否 | 进程名称。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| bundleNames | Array<string> | 否 | 否 | 进程中所有运行的Bundle名称。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| state10+ | appManager.ProcessState | 否 | 否 | 当前进程运行状态。 元服务API：从API version 11开始，该接口支持在元服务中使用。 |
| bundleType12+ | bundleManager.BundleType | 否 | 否 | 当前进程运行的包类型。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| appCloneIndex12+ | number | 否 | 是 | 分身应用索引。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |

示例：

```ets
import { appManager } from '@kit.AbilityKit';

appManager.getRunningProcessInformation((error, data) => {
  if (error) {
    console.error(`getRunningProcessInformation fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`getRunningProcessInformation success, data: ${JSON.stringify(data)}`);
  }
});
```