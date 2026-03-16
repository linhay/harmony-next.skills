# StatusBarViewExtensionAbility（状态栏扩展Ability）

StatusBarViewExtensionAbility为状态栏扩展Ability，继承自[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability#uiextensionability)，用于给应用提供接入状态栏图标左键业务弹窗的能力。

- 本模块接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { StatusBarViewExtensionAbility } from '@kit.DeskTopExtensionKit';
```

**示例：**

```ets
import { StatusBarViewExtensionAbility } from '@kit.DeskTopExtensionKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';

let TAG = "MyStatusBarViewAbility";

export default class MyStatusBarViewAbility extends StatusBarViewExtensionAbility {
  onCreate() {
    console.info(TAG, `onCreate`);
  }

  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    console.info(TAG, `onSessionCreate, want: ${want.abilityName}`);
    session.loadContent('pages/Index');
  }

  onForeground() {
    console.info(TAG, `onForeground`);
  }

  onBackground() {
    console.info(TAG, `onBackground`);
  }

  onSessionDestroy(session: UIExtensionContentSession) {
    console.info(TAG, `onSessionDestroy`);
  }

  onDestroy() {
    console.info(TAG, `onDestroy`);
  }
}
```