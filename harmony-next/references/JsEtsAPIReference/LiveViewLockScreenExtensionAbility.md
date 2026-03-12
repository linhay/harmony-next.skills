# LiveViewLockScreenExtensionAbility

LiveViewLockScreenExtensionAbility为锁屏沉浸实况窗扩展Ability，继承自[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)。有如下约束：

- LiveViewLockScreenExtensionAbility为独立子进程，不能跨进程拉起其他Ability。
- 不允许调用通知API、窗口API、卡片API、后台任务API、联系人API、分布式数据管理API、相机API、NFC API、上传下载API、蜂窝通信API。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { LiveViewLockScreenExtensionAbility } from '@kit.LiveViewKit';
```

**设备行为差异：**该模块在Phone、Tablet中可正常调用，在其他设备类型中无效果。

#### 属性

**模型约束：**属性仅可在Stage模型下使用。

**系统能力：**SystemCapability.LiveView.LiveViewService

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

context

[LiveViewLockScreenExtensionContext](LiveViewLockScreenExtensionContext.md)

否

否

LiveViewLockScreenExtensionAbility的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。

**示例：**

```ets
import { LiveViewLockScreenExtensionAbility } from '@kit.LiveViewKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class LiveViewLockScreenExtAbility extends LiveViewLockScreenExtensionAbility {
  onCreate(): void {
    hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onCreate begin.');
  }

  onSessionCreate(want: Want, session: UIExtensionContentSession): void {
    hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onSessionCreate begin.');
    let param: Record<string, UIExtensionContentSession> = {
      'session': session
    };
    let storage: LocalStorage = new LocalStorage(param);

    // 解析从liveViewLocalScreenAbilityParameters中传入的参数
    const parameters = want?.parameters;
    let words: string = parameters?.['words'] ? parameters?.['words'] as string : 'Hello World!';
    storage.setOrCreate('words', words);

    // 加载锁屏沉浸实况窗页面
    session.loadContent('pages/LiveViewLockScreenPage', storage);
  }
}

```