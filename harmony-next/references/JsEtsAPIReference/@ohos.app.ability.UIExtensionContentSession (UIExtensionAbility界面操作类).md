# @ohos.app.ability.UIExtensionContentSession (UIExtensionAbility界面操作类)

UIExtensionContentSession是[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)组件的界面操作类，提供页面加载、设置宿主应用（UIExtensionAbility组件的拉起方）窗口隐私模式等功能。当宿主应用拉起指定的UIExtensionAbility组件时，系统创建UIExtensionContentSession对象，并通过[onSessionCreate](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md#ZH-CN_TOPIC_0000002497604594__onsessioncreate)回调传递给开发者。一个UIExtensionAbility组件对应一个UIExtensionContentSession对象，每个UIExtensionAbility组件的UIExtensionContentSession对象之间互不影响。

本模块首批接口从API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { UIExtensionContentSession } from '@kit.AbilityKit';
```

#### UIExtensionContentSession

UIExtensionAbility组件的界面操作类，提供页面加载、设置宿主应用窗口隐私模式等功能。

#### loadContent

loadContent(path: string, storage?: LocalStorage): void

为[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)组件加载页面，支持通过[LocalStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localstorage)传递状态属性给被加载的页面。该接口用于开发者在UIExtensionAbility组件的[onSessionCreate](zh-cn_topic_0000002497604594.md#ZH-CN_TOPIC_0000002497604594__onsessioncreate)生命周期中加载页面。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明pathstring是要加载的页面所在的路径，该路径通过[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中的[pages标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#pages标签)配置。storage[LocalStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localstorage)否页面级UI状态存储单元，开发者可通过该参数为加载的页面传递状态属性。

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.16000050Internal error.

**示例：**

```ets
// UIExtensionAbility组件不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { UIExtensionContentSession, ShareExtensionAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  // ...

  onSessionCreate(want: Want, session: UIExtensionContentSession): void {
    try {
      let storage: LocalStorage = new LocalStorage();
      storage.setOrCreate('session', session);
      session.loadContent('pages/Extension', storage);
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(`Failed to load content, code: ${code}, msg: ${message}`);
    }
  }

  // ...
}
```

#### loadContentByName18+

loadContentByName(name: string, storage?: LocalStorage): void

为[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)组件加载[命名路由](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-routing#命名路由)页面，支持通过[LocalStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localstorage)传递状态属性给被加载的页面。该接口用于开发者在UIExtensionAbility组件的[onSessionCreate](zh-cn_topic_0000002497604594.html#ZH-CN_TOPIC_0000002497604594__onsessioncreate)生命周期中加载命名路由页面。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明namestring是命名路由页面的名称。storage[LocalStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localstorage)否页面级UI状态存储单元，开发者可通过该参数为加载的页面传递状态属性。

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

错误码ID错误信息16000050Internal error.

**示例：**

UIExtensionAbility组件的实现：

```ets
// UIExtensionAbility组件不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { UIExtensionContentSession, ShareExtensionAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import './pages/UIExtensionPage'; // 导入命名路由页面，示例代码以“./pages/UIExtensionPage.ets”文件为例，在实际代码开发过程中修改为真实路径和文件名称。

export default class ShareExtAbility extends ShareExtensionAbility {
  // 其他生命周期和实现

  onSessionCreate(want: Want, session: UIExtensionContentSession): void {
    let storage: LocalStorage = new LocalStorage();
    storage.setOrCreate('session', session);

    let name: string = 'UIExtPage'; // 命名路由页面的名字。
    try {
      session.loadContentByName(name, storage);
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(`Failed to load content by name ${name}, code: ${code}, msg: ${message}`);
    }
  }

  // 其他生命周期和实现
}
```

UIExtensionAbility组件加载的命名路由页面的实现：

```ets
// “./pages/UIExtensionPage.ets”文件的实现。
import { UIExtensionContentSession } from '@kit.AbilityKit';

@Entry({ routeName: 'UIExtPage' }) // 通过“routeName”定义命名路由页面的名字。
@Component
struct UIExtensionPage {
  @State message: string = 'Hello world';
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  private session: UIExtensionContentSession | undefined = this.storage?.get<UIExtensionContentSession>('session');

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

#### terminateSelf

terminateSelf(callback: AsyncCallback<void>): void

销毁UIExtensionAbility组件自身，同时关闭对应的宿主应用窗口界面。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当接口调用成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { UIExtensionContentSession } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry()
@Component
struct Index {
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  private session: UIExtensionContentSession | undefined =
    this.storage?.get<UIExtensionContentSession>('session');

  build() {
    RelativeContainer() {
      Button('TerminateSelf')
        .onClick(() => {
          this.session?.terminateSelf((err: BusinessError) => {
            if (err) {
              console.error(`Failed to terminate self, code: ${err.code}, msg: ${err.message}`);
              return;
            }
            console.info(`Succeeded in terminating self.`);
          });

          this.storage?.clear();
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

#### terminateSelf

terminateSelf(): Promise<void>

销毁UIExtensionAbility组件自身，同时关闭对应的宿主应用窗口界面。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**示例：**

```ets
import { UIExtensionContentSession } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry()
@Component
struct Index {
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  private session: UIExtensionContentSession | undefined =
    this.storage?.get<UIExtensionContentSession>('session');

  build() {
    RelativeContainer() {
      Button('TerminateSelf')
        .onClick(() => {
          this.session?.terminateSelf()
            .then(() => {
              console.info(`Succeeded in terminating self.`);
            })
            .catch((err: BusinessError) => {
              console.error(`Failed to terminate self, code: ${err.code}, msg: ${err.message}`);
            });

          this.storage?.clear();
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

#### terminateSelfWithResult

terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void

销毁UIExtensionAbility组件自身，关闭对应的宿主应用窗口界面，并将结果返回给宿主应用。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明parameter[AbilityResult](AbilityResult.md)是返回给宿主应用的信息。callbackAsyncCallback<void>是回调函数。当接口调用成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { UIExtensionContentSession, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry()
@Component
struct Index {
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  private session: UIExtensionContentSession | undefined =
    this.storage?.get<UIExtensionContentSession>('session');

  build() {
    RelativeContainer() {
      Button('TerminateSelfWithResult')
        .onClick(() => {
          let abilityResult: common.AbilityResult = {
            resultCode: 0,
            want: {
              bundleName: 'com.ohos.uiextensioncontentsession',
              parameters: {
                'result': 123456
              }
            }
          };

          this.session?.terminateSelfWithResult(abilityResult, (err: BusinessError) => {
            if (err) {
              console.error(`Failed to terminate self with result, code: ${err.code}, msg: ${err.message}`);
              return;
            }
            console.info(`Succeeded in terminating self with result.`);
          });

          this.storage?.clear();
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

#### terminateSelfWithResult

terminateSelfWithResult(parameter: AbilityResult): Promise<void>

销毁UIExtensionAbility组件自身，关闭对应的宿主应用窗口界面，并将结果返回给宿主应用。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明parameter[AbilityResult](AbilityResult.md)是返回给宿主应用的信息。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { UIExtensionContentSession, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry()
@Component
struct Index {
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  private session: UIExtensionContentSession | undefined =
    this.storage?.get<UIExtensionContentSession>('session');

  build() {
    RelativeContainer() {
      Button('TerminateSelfWithResult')
        .onClick(() => {
          let abilityResult: common.AbilityResult = {
            resultCode: 0,
            want: {
              bundleName: 'com.ohos.uiextensioncontentsession',
              parameters: {
                'result': 123456
              }
            }
          };

          this.session?.terminateSelfWithResult(abilityResult)
            .then(() => {
              console.info(`Succeeded in terminating self with result.`);
            })
            .catch((err: BusinessError) => {
              console.error(`Failed to terminate self with result, code: ${err.code}, msg: ${err.message}`);
            });

          this.storage?.clear();
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

#### setWindowPrivacyMode

setWindowPrivacyMode(isPrivacyMode: boolean): Promise<void>

设置宿主应用窗口的隐私模式开启或关闭。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**需要权限**：ohos.permission.PRIVACY_WINDOW

**参数：**

参数名类型必填说明isPrivacyModeboolean是表示是否开启隐私模式。true表示开启；false表示关闭。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

错误码ID错误信息201The application does not have permission to call the interface.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
// UIExtensionAbility组件不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { UIExtensionContentSession, ShareExtensionAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  // ...

  onSessionCreate(want: Want, session: UIExtensionContentSession): void {
    let isPrivacyMode: boolean = true;
    try {
      session.setWindowPrivacyMode(isPrivacyMode)
        .then(() => {
          console.info(`Succeeded in setting window to privacy mode.`);
        })
        .catch((err: BusinessError) => {
          console.error(`Failed to set window to privacy mode, code: ${err.code}, msg: ${err.message}`);
        });
    } catch (e) {
      let code = (e as BusinessError).code;
      let msg = (e as BusinessError).message;
      console.error(`Failed to set window to privacy mode, code: ${code}, msg: ${msg}`);
    }
  }

  // ...
}
```

#### setWindowPrivacyMode

setWindowPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void

设置宿主应用窗口的隐私模式开启或关闭。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**需要权限**：ohos.permission.PRIVACY_WINDOW

**参数：**

参数名类型必填说明isPrivacyModeboolean是表示是否开启隐私模式。true表示开启；false表示关闭。callbackAsyncCallback<void>是回调函数。当设置成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

错误码ID错误信息201The application does not have permission to call the interface.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
// UIExtensionAbility组件不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { UIExtensionContentSession, ShareExtensionAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  // ...

  onSessionCreate(want: Want, session: UIExtensionContentSession): void {
    let isPrivacyMode: boolean = true;
    try {
      session.setWindowPrivacyMode(isPrivacyMode, (err: BusinessError) => {
        if (err) {
          console.error(`Failed to set window to privacy mode, code: ${err.code}, msg: ${err.message}`);
          return;
        }
        console.info(`Succeeded in setting window to privacy mode.`);
      });
    } catch (e) {
      let code = (e as BusinessError).code;
      let msg = (e as BusinessError).message;
      console.error(`Failed to set window to privacy mode, code: ${code}, msg: ${msg}`);
    }
  }

  // ...
}
```

#### startAbilityByType11+

startAbilityByType(type: string, wantParam: Record<string, Object>,

abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>): void

通过type隐式启动UIExtensionAbility。使用callback异步回调。仅支持处于前台的应用调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明typestring是UIExtensionAbility组件类型，取值详见[通过startAbilityByType接口拉起垂类面板](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-intent-panel#匹配规则)。wantParamRecord<string, Object>是表示启动UIExtensionAbility组件时传递的参数。abilityStartCallback[AbilityStartCallback](zh-cn_topic_0000002497604620.html)是表示启动UIExtensionAbility组件的执行结果。callbackAsyncCallback<void>是回调函数。当接口调用成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.16000050Internal error.

**示例：**

```ets
// UIExtensionAbility组件不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { UIExtensionContentSession, ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  // ...

  onSessionCreate(want: Want, session: UIExtensionContentSession): void {
    let wantParams: Record<string, Object> = {
      'sceneType': 1
    };
    let abilityStartCallback: common.AbilityStartCallback = {
      onError: (code: number, name: string, message: string) => {
        console.error(`onError, code: ${code}, name: ${name}, msg: ${message}`);
      },
      onResult: (result: common.AbilityResult) => {
        console.info(`onResult, result: ${JSON.stringify(result)}`);
      }
    };

    session.startAbilityByType('navigation', wantParams, abilityStartCallback, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to startAbilityByType, code: ${err.code}, msg: ${err.message}`);
        return;
      }
      console.info(`Succeeded in startAbilityByType`);
    });
  }

  // ...
}
```

#### startAbilityByType11+

startAbilityByType(type: string, wantParam: Record<string, Object>,

abilityStartCallback: AbilityStartCallback): Promise<void>

通过type隐式启动UIExtensionAbility组件。使用Promise异步回调。仅支持处于前台的应用调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明typestring是UIExtensionAbility组件类型，取值详见[通过startAbilityByType接口拉起垂类面板](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-intent-panel#匹配规则)。wantParamRecord<string, Object>是表示启动UIExtensionAbility组件时传递的参数。abilityStartCallback[AbilityStartCallback](zh-cn_topic_0000002497604620.html)是表示启动UIExtensionAbility组件的执行结果。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.16000050Internal error.

**示例：**

```ets
// UIExtensionAbility组件不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
import { UIExtensionContentSession, ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  // ...

  onSessionCreate(want: Want, session: UIExtensionContentSession): void {
    let wantParams: Record<string, Object> = {
      'sceneType': 1
    };
    let abilityStartCallback: common.AbilityStartCallback = {
      onError: (code: number, name: string, message: string) => {
        console.error(`onError, code: ${code}, name: ${name}, msg: ${message}`);
      },
      onResult: (result: common.AbilityResult) => {
        console.info(`onResult, result: ${JSON.stringify(result)}`);
      }
    };

    session.startAbilityByType('test', wantParams, abilityStartCallback)
      .then(() => {
        console.info(`Succeeded in startAbilityByType`);
      })
      .catch((err: BusinessError) => {
        console.error(`Failed to startAbilityByType, code: ${err.code}, msg: ${err.message}`);
      });
  }

  // ...
}
```

#### getUIExtensionWindowProxy12+

getUIExtensionWindowProxy(): uiExtension.WindowProxy

获取UIExtension窗口代理。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

类型说明[uiExtension.WindowProxy](@ohos.arkui.uiExtension (uiExtension).md#ZH-CN_TOPIC_0000002529284779__windowproxy)UIExtensionAbility组件的宿主应用窗口代理。

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](元能力子系统错误码.md)。

错误码ID错误信息16000050Internal error.

**示例：**

```ets
// Index.ets
import { UIExtensionContentSession } from '@kit.AbilityKit';
import { uiExtension } from '@kit.ArkUI';

@Entry()
@Component
struct Extension {
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  @State message: string = 'EmbeddedUIExtensionAbility Index';
  private session: UIExtensionContentSession | undefined = this.storage?.get<UIExtensionContentSession>('session');
  private extensionWindow: uiExtension.WindowProxy | undefined = this.session?.getUIExtensionWindowProxy();

  aboutToAppear(): void {
    this.extensionWindow?.on('windowSizeChange', (size) => {
      console.info(`size = ${JSON.stringify(size)}`);
    });
    this.extensionWindow?.on('avoidAreaChange', (info) => {
      console.info(`type = ${JSON.stringify(info.type)}, area = ${JSON.stringify(info.area)}`);
    });
  }

  aboutToDisappear(): void {
    this.extensionWindow?.off('windowSizeChange');
    this.extensionWindow?.off('avoidAreaChange');
  }

  build() {
    Column() {
      Text(this.message)
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
  }
}
```