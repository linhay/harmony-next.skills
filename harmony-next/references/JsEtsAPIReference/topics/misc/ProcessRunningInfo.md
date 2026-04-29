# ProcessRunningInfo

运行进程信息，可以通过appManager中[getProcessRunningInfos](@ohos.application.appManager (appManager).md#ZH-CN_TOPIC_0000002553200555__appmanagergetprocessrunninginfosdeprecated)方法来获取运行进程信息。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

- 本模块接口从API version 9 开始废弃，建议使用[ProcessInformation9+](ProcessInformation.md)替代。

- 本模块首批接口从API version 8 开始支持。

**导入模块**

```ets
import appManager from '@ohos.application.appManager';
```

**属性**

系统能力：SystemCapability.Ability.AbilityRuntime.Mission

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 否 | 进程ID。 |
| uid | number | 否 | 否 | 应用程序的UID。 |
| processName | string | 否 | 否 | 进程名称。 |
| bundleNames | Array<string> | 否 | 否 | 进程中所有运行的Bundle名称。 |

示例：

```ets
import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

appManager.getProcessRunningInfos().then((data) => {
    console.info(`success: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
    console.error(`failed: ${JSON.stringify(error)}`);
});
```