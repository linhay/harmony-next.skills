# EmbeddedComponent

EmbeddedComponent用于支持在当前页面嵌入本应用内其他[EmbeddedUIExtensionAbility](@ohos.app.ability.EmbeddedUIExtensionAbility (支持跨进程界面嵌入的ExtensionAbility组件).md)提供的UI。EmbeddedUIExtensionAbility在独立进程中运行，完成页面布局和渲染。

通常用于有进程隔离诉求的模块化开发场景。

该组件从API Version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 使用约束

EmbeddedComponent仅支持在拥有多进程权限的设备上使用。

EmbeddedComponent只能在UIAbility中使用，且被拉起的EmbeddedUIExtensionAbility需与UIAbility属于同一应用。

#### 子组件

无

#### 接口

EmbeddedComponent(loader: Want, type: EmbeddedType)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明loader[Want](@ohos.app.ability.Want (Want).md)是要加载的EmbeddedUIExtensionAbility。type[EmbeddedType](枚举说明.md#ZH-CN_TOPIC_0000002529284967__embeddedtype12)是提供方的类型。

#### 属性

支持[通用属性](通用属性.md)。

EmbeddedComponent组件宽高默认值和最小值均为10vp, 不支持如下与宽高相关的属性："constraintSize"、"aspectRatio"、"layoutWeight"、"flexBasis"、"flexGrow"和"flexShrink"。

#### 事件

与屏幕坐标相关的事件信息会基于EmbeddedComponent的位置宽高进行坐标转换后传递给被拉起的EmbeddedUIExtensionAbility处理。

不支持[点击](点击事件.md)等通用事件。仅支持以下事件：

#### onTerminated

onTerminated(callback: Callback<TerminationInfo>)

被拉起的EmbeddedUIExtensionAbility通过调用terminateSelfWithResult或者terminateSelf正常退出时，触发本回调函数。

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback[Callback](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__callback)<[TerminationInfo](#ZH-CN_TOPIC_0000002497444946__terminationinfo)>是回调函数，入参用于接收EmbeddedUIExtensionAbility的返回结果，类型为[TerminationInfo](#ZH-CN_TOPIC_0000002497444946__terminationinfo)。

- 若EmbeddedUIExtensionAbility通过调用terminateSelfWithResult退出，其携带的信息会传给回调函数的入参；
- 若EmbeddedUIExtensionAbility通过调用terminateSelf退出，上述回调函数的入参中，"code"取默认值"0"，"want"为"undefined"。

#### onError

onError(callback: ErrorCallback)

被拉起的EmbeddedUIExtensionAbility在运行过程中发生异常时触发本回调。可通过回调参数中的code、name和message获取错误信息并做处理，业务错误码详细介绍请参见[UIExtension错误码](UIExtension错误码.md)。

该接口不支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明callback[ErrorCallback](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)是回调函数，入参用于接收异常信息，类型为[BusinessError](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__businesserror)，可通过参数中的code、name和message获取错误信息并做处理。

如下情形会触发本回调：

- 通知提供方拉起EmbeddedUIExtensionAbility失败。
- 通知提供方EmbeddedUIExtensionAbility切后台失败。
- 通知提供方销毁EmbeddedUIExtensionAbility失败。
- 提供方EmbeddedUIExtensionAbility异常退出。
- 在EmbeddedUIExtensionAbility中嵌套使用EmbeddedComponent。

#### TerminationInfo

用于表示被拉起的EmbeddedUIExtensionAbility的返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明codenumber否否被拉起EmbeddedUIExtensionAbility退出时返回的结果码，返回的结果码由terminateSelfWithResult或者terminateSelf被调用时传入的数据决定。want[Want](@ohos.app.ability.Want (Want).md)否是被拉起EmbeddedUIExtensionAbility退出时返回的数据。

#### 示例（加载EmbeddedComponent）

本示例展示EmbeddedComponent组件和EmbeddedUIExtensionAbility的基础使用方式，示例应用的bundleName为"com.example.embeddeddemo", 同应用下被拉起的EmbeddedUIExtensionAbility为"ExampleEmbeddedAbility"。本示例仅支持在拥有多进程权限的设备上运行，如2in1。

-

示例应用中的EntryAbility(UIAbility)加载首页文件ets/pages/Index.ets，其中内容如下：

```ets
import { Want } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'Message: ';
  private want: Want = {
    bundleName: "com.example.embeddedComponent",
    abilityName: "ExampleEmbeddedAbility",
  };

  build() {
    Row() {
      Column() {
        Text(this.message).fontSize(30)
        EmbeddedComponent(this.want, EmbeddedType.EMBEDDED_UI_EXTENSION)
          .width('100%')
          .height('90%')
          .onTerminated((info) => {
            // 点击extension页面内的terminateSelfWithResult按钮后触发onTerminated回调，文本框显示如下信息
            this.message = 'Termination: code = ' + info.code + ', want = ' + JSON.stringify(info.want);
          })
          .onError((error) => {
            // 失败或异常触发onError回调，文本框显示如下报错内容
            this.message = 'Error: code = ' + error.code;
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

-

EmbeddedComponent拉起的ExampleEmbeddedAbility(EmbeddedUIExtensionAbility)在ets/extensionAbility/ExampleEmbeddedAbility.ets文件中实现，内容如下：

```ets
import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';

const TAG: string = '[ExampleEmbeddedAbility]';

export default class ExampleEmbeddedAbility extends EmbeddedUIExtensionAbility {
  onCreate() {
    console.info(TAG, `onCreate`);
  }

  onForeground() {
    console.info(TAG, `onForeground`);
  }

  onBackground() {
    console.info(TAG, `onBackground`);
  }

  onDestroy() {
    console.info(TAG, `onDestroy`);
  }

  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
    let param: Record<string, UIExtensionContentSession> = {
      'session': session
    };
    let storage: LocalStorage = new LocalStorage(param);
    // 加载pages/extension.ets页面内容
    session.loadContent('pages/extension', storage);
  }

  onSessionDestroy(session: UIExtensionContentSession) {
    console.info(TAG, `onSessionDestroy`);
  }
}
```

-

ExampleEmbeddedAbility(EmbeddedUIExtensionAbility)的入口页面文件ets/pages/extension.ets内容如下，同时需要在resources/base/profile/main_pages.json文件中配置该页面路径：

```ets
import { UIExtensionContentSession } from '@kit.AbilityKit';

@Entry
@Component
struct Extension {
  @State message: string = 'EmbeddedUIExtensionAbility Index';
  private storage: LocalStorage | undefined = this.getUIContext()?.getSharedLocalStorage();
  private session: UIExtensionContentSession | undefined = this.storage?.get<UIExtensionContentSession>('session');

  build() {
    Column() {
      Text(this.message)
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
      Button("terminateSelfWithResult").fontSize(20).onClick(() => {
        // 点击按钮后调用terminateSelfWithResult退出
        this.session?.terminateSelfWithResult({
          resultCode: 1,
          want: {
            bundleName: "com.example.embeddedComponent",
            abilityName: "ExampleEmbeddedAbility",
          }
        });
      })
    }.width('100%').height('100%')
  }
}
```

-

在module.json5配置文件的"extensionAbilities"标签下增加ExampleEmbeddedAbility配置，其type类型为embeddedUI，具体内容如下：

```ets
{
  "name": "ExampleEmbeddedAbility",
  "srcEntry": "./ets/extensionAbility/ExampleEmbeddedAbility.ets",
  "type": "embeddedUI"
}
```

-

文件目录结构如下：

```ets
.
└── main
    ├── ets
    │   ├── extensionAbility
    │   │   └── ExampleEmbeddedAbility.ets
    │   └── pages
    |       ├── extension.ets
    │       └── Index.ets
    ├── resources
    |   └── base
    |       └── profile
    |           └── main_pages.json
    └── module.json5
```

-

示例图如下：