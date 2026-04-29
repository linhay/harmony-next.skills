# @ohos.application.Configuration (Configuration)

定义环境变化信息。Configuration是接口定义，仅做字段声明。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块从API version 9废弃，替换模块为[@ohos.app.ability.Configuration (Configuration)](@ohos.app.ability.Configuration (环境变量).md)。

#### 导入模块

```ets
import Configuration from '@ohos.application.Configuration';
```

#### Configuration

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| language8+ | string | 否 | 是 | 表示应用程序的当前语言。例如：zh。 |
| colorMode8+ | ConfigurationConstant.ColorMode | 否 | 是 | 表示深浅色模式，取值范围：浅色模式（COLOR_MODE_LIGHT），深色模式（COLOR_MODE_DARK）。默认为浅色。 |

具体字段描述参考ohos.application.Configuration.d.ts文件

**示例：**

```ets
import UIAbility from '@ohos.app.ability.UIAbility';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import EnvironmentCallback from '@ohos.app.ability.EnvironmentCallback';
import Want from '@ohos.app.ability.Want';
import Window from '@ohos.window';
import { BusinessError } from '@ohos.base';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
  }

  onDestroy() {
  }

  onWindowStageCreate(windowStage: Window.WindowStage) {
    let envCallback: EnvironmentCallback = {
      onConfigurationUpdated(config) {
        console.info(`envCallback onConfigurationUpdated success: ${JSON.stringify(config)}`);
        let language = config.language;
        let colorMode = config.colorMode;
      },
      onMemoryLevel(level) {
        console.info(`onMemoryLevel level: ${JSON.stringify(level)}`);
      }
    };

    let applicationContext = this.context.getApplicationContext();
    try {
      applicationContext.on('environment', envCallback);
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }

    windowStage.loadContent('pages/index', (err, data) => {
      if (err.code) {
        console.error(`failed to load the content, error: ${JSON.stringify(err)}`);
        return;
      }
      console.info(`Succeeded in loading the content, data: ${JSON.stringify(data)}`);
    });
  }
```