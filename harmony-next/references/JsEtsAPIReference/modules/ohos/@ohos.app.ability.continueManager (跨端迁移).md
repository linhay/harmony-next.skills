# @ohos.app.ability.continueManager (跨端迁移)

continueManager提供了应用跨端迁移的管理能力，如获取应用跨端迁移过程中快速拉起目标应用的结果。

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { continueManager } from '@kit.AbilityKit';
```

#### continueManager.on

on(type: 'prepareContinue', context: Context, callback: AsyncCallback<ContinueResultInfo>): void

在应用快速拉起时，注册回调函数以获取快速拉起结果。使用callback异步回调。

快速拉起功能支持在用户触发迁移、等待迁移数据返回的过程中，并行拉起应用，减小用户等待时间。在源端应用[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)的continueType标签的取值中添加“_ContinueQuickStart”后缀，可以开启快速拉起功能。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Mission

**参数**：

参数名类型必填说明typestring是固定值：prepareContinue。context[Context](../../topics/graphics/BaseContext.md)是Ability的Context。callbackAsyncCallback<[ContinueResultInfo](@ohos.app.ability.continueManager (跨端迁移).md#ZH-CN_TOPIC_0000002497444630__continueresultinfo)>是回调函数。当快速拉起结果获取成功，err为undefined，ContinueResultInfo为获取到的快速启动结果。否则为错误对象。

**错误码：**

以下错误码详细介绍请参考[DistributedSchedule错误码](../../errors/DistributedSchedule错误码.md)。

错误码ID错误信息16300501the system ability work abnormally.

**示例**：

```ets
import { AbilityConstant, UIAbility, Want, continueManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[MigrationAbility]';
const DOMAIN_NUMBER: number = 0xFF00;

export default class MigrationAbility extends UIAbility {
    storage : LocalStorage = new LocalStorage();

    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onCreate');

        // 1.已配置快速拉起功能，应用立即启动时触发应用生命周期回调
        if (launchParam.launchReason === AbilityConstant.LaunchReason.PREPARE_CONTINUATION) {
            // 注册快速拉起结果通知的回调函数
            try {
              continueManager.on("prepareContinue", this.context, (err, continueResultInfo) => {
                if (err.code != 0) {
                  console.error('register failed, cause: ' + JSON.stringify(err));
                  return;
                }
                console.info('register finished, ' + JSON.stringify(continueResultInfo));
              });
            } catch (e) {
              console.error('register failed, cause: ' + JSON.stringify(e));
            }
            //若应用迁移数据较大，可在此处添加加载页面(页面中显示loading等)
            //可处理应用自定义跳转、时序等问题
            // ...
        }
    }
}
```

#### continueManager.off

off(type: 'prepareContinue', context: Context, callback?: AsyncCallback<ContinueResultInfo>): void

在应用快速拉起时，注销回调函数，不再获取快速拉起结果。使用callback异步回调。

快速拉起功能支持在用户触发迁移、等待迁移数据返回的过程中，并行拉起应用，减小用户等待时间。在源端应用[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)的continueType标签的取值中添加“_ContinueQuickStart”后缀，可以开启快速拉起功能。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Mission

**参数**：

参数名类型必填说明typestring是固定值：prepareContinue。context[Context](../../topics/graphics/BaseContext.md)是Ability的Context。callbackAsyncCallback<[ContinueResultInfo](@ohos.app.ability.continueManager (跨端迁移).md#ZH-CN_TOPIC_0000002497444630__continueresultinfo)>否回调函数。当回调函数注销成功，err为undefined，ContinueResultInfo为获回调函数注销结果。否则为错误对象。

**错误码：**

以下错误码详细介绍请参考[DistributedSchedule错误码](../../errors/DistributedSchedule错误码.md)。

错误码ID错误信息16300501the system ability work abnormally.

**示例**：

```ets
import { AbilityConstant, UIAbility, Want, continueManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[MigrationAbility]';
const DOMAIN_NUMBER: number = 0xFF00;

export default class MigrationAbility extends UIAbility {
    storage : LocalStorage = new LocalStorage();

    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onCreate');

        // 1.已配置快速拉起功能，应用立即启动时触发应用生命周期回调
        if (launchParam.launchReason === AbilityConstant.LaunchReason.PREPARE_CONTINUATION) {
            // 注销快速拉起结果通知的回调函数
            try {
              continueManager.off("prepareContinue", this.context, (err, continueResultInfo) => {
                if (err.code != 0) {
                  console.error('unregister failed, cause: ' + JSON.stringify(err));
                  return;
                }
                console.info('unregister finished, ' + JSON.stringify(continueResultInfo));
              });
            } catch (e) {
              console.error('unregister failed, cause: ' + JSON.stringify(e));
            }
            //若应用迁移数据较大，可在此处添加加载页面(页面中显示loading等)
            //可处理应用自定义跳转、时序等问题
            // ...
        }
    }
}
```

#### ContinueResultInfo

注册或注销回调函数返回的快速拉起的结果。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Mission

名称类型只读可选说明resultState[ContinueStateCode](@ohos.app.ability.continueManager (跨端迁移).md#ZH-CN_TOPIC_0000002497444630__continuestatecode)否否操作结果状态码。resultInfostring否是操作结果的说明。

#### ContinueStateCode

快速拉起的结果状态码的枚举值。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Mission

名称值说明SUCCESS0操作成功。SYSTEM_ERROR其它操作失败。