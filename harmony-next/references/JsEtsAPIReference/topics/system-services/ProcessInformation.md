# ProcessInformation

运行进程信息，可以通过appManager的[getRunningProcessInformation](../../modules/ohos/@ohos.app.ability.appManager (应用管理).md#ZH-CN_TOPIC_0000002497444628__appmanagergetrunningprocessinformation)来获取运行进程信息。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { appManager } from '@kit.AbilityKit';
```

#### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明pidnumber否否

进程ID。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

uidnumber否否

应用程序的UID。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

processNamestring否否

进程名称。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

bundleNamesArray<string>否否

进程中所有运行的Bundle名称。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

state10+[appManager.ProcessState](../../modules/ohos/@ohos.app.ability.appManager (应用管理).md#ZH-CN_TOPIC_0000002497444628__processstate10)否否

当前进程运行状态。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

bundleType12+[bundleManager.BundleType](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundletype)否否

当前进程运行的包类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

appCloneIndex12+number否是

分身应用索引。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**示例：**

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