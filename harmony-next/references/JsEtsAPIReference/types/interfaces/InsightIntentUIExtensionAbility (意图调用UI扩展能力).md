# InsightIntentUIExtensionAbility (意图调用UI扩展能力)

InsightIntentUIExtensionAbility用于小艺对话过程中的意图调用时的信息展示，为意图调用UI扩展能力，应用可以声明一个或多个InsightIntentUI来展示其意图的窗口化界面，继承自[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)。

起始版本： 5.0.0(12)

**导入模块**

```ets
import { InsightIntentUIExtensionAbility } from '@kit.IntentsKit';
```

**InsightIntentUIExtensionAbility**

模型约束： 该类仅可在Stage模型下使用。

系统能力： SystemCapability.AI.InsightIntent

起始版本： 5.0.0(12)

**示例**

```ets
import { InsightIntentUIExtensionAbility } from '@kit.IntentsKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';

// 此处以TestUiExtAbility继承InsightIntentUIExtensionAbility为例
export default class TestUiExtAbility extends InsightIntentUIExtensionAbility {
    onCreate() {
    }

    onForeground() {
    }

    onBackground() {
    }

    onDestroy() {
    }

    onSessionCreate(want: Want, session: UIExtensionContentSession) {
    }

    onSessionDestroy(session: UIExtensionContentSession) {
    }
```