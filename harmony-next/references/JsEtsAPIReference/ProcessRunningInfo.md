# ProcessRunningInfo

运行进程信息，可以通过appManager中[getProcessRunningInfos](@ohos.application.appManager (appManager).md#ZH-CN_TOPIC_0000002497604642__appmanagergetprocessrunninginfosdeprecated)方法来获取运行进程信息。

- 本模块接口从API version 9 开始废弃，建议使用[ProcessInformation9+](ProcessInformation.md)替代。
- 本模块首批接口从API version 8 开始支持。

#### 导入模块

```ets
import appManager from '@ohos.application.appManager';
```

#### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.Mission

名称类型只读可选说明pidnumber否否进程ID。uidnumber否否应用程序的UID。processNamestring否否进程名称。bundleNamesArray<string>否否进程中所有运行的Bundle名称。

**示例：**

```ets
import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

appManager.getProcessRunningInfos().then((data) => {
    console.info(`success: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
    console.error(`failed: ${JSON.stringify(error)}`);
});
```