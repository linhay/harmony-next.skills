# Class (UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12))

UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)实例对象。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

-

以下API需要通过对应的UIContext实例调用。获取UIContext分为三种方式，第一种是使用ohos.window中的[getUIContext()](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__getuicontext10)方法获取UIContext实例，第二种是通过自定义组件内置方法[getUIContext()](自定义组件内置方法.md#ZH-CN_TOPIC_0000002522240898__getuicontext)获取UIContext实例，第三种是通过UIContext类的静态方法如[getCallingScopeUIContext](#ZH-CN_TOPIC_0000002522240732__getcallingscopeuicontext22)获取UIContext实例。本文中UIContext对象以uiContext表示。

**示例：**

以下示例展示了三种获取UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)实例的方法。

```ets
// 三种方法获取到的UIContext没有差异
//index.ets
import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button("Button")
          .onClick(()=>{
            //通过自定义组件内置方法获取
            this.getUIContext()
            // 通过UIContext类的静态方法获取
            let uiContext = UIContext.getCallingScopeUIContext();
            //其他运行逻辑
          })
}

//EntryAbility.ets
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    //通过ohos.window获取
    windowStage.getMainWindowSync().getUIContext()
    //其他运行逻辑
  }
```

**constructor22+**

constructor()

构造UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)对象。


通过构造函数创建的UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)对象指向不明确的UI上下文，即不指向任何UI实例。该UIContext对应实例的唯一标识ID为-1。

元服务API： 从API version 22开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

示例：

```ets
import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

function GetUIContextByAtomicInterface(): UIContext {
  let callingScopeUIContext = UIContext.getCallingScopeUIContext();
  if (callingScopeUIContext) {
    hilog.info(0x00, 'testTag', `Get UIContext of calling scope.`)
    return callingScopeUIContext;
  }
  let allContexts = UIContext.getAllUIContexts();
  let length = allContexts.length;
  if (length === 1) {
    hilog.info(0x00, 'testTag', `Get UIContext of unique UI instance.`)
    return allContexts[0];
  }
  let lastFocusedUIContext = UIContext.getLastFocusedUIContext();
  if (lastFocusedUIContext) {
    hilog.info(0x00, 'testTag', `Get UIContext of last focused instance.`)
    return lastFocusedUIContext;
  }
  let lastForegroundUIContext = UIContext.getLastForegroundUIContext();
  if (lastForegroundUIContext) {
    hilog.info(0x00, 'testTag', `Get UIContext of last foregrounded instance.`)
    return lastForegroundUIContext;
  }
  if (length !== 0) {
    hilog.info(0x00, 'testTag', `Get UIContext with maximum instanceId.`)
    return allContexts[length - 1];
  }
  hilog.info(0x00, 'testTag', `Get UIContext of undefined calling scope.`)
  return new UIContext();
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  aboutToAppear() {
    let uiContext = this.getUIContext();
    hilog.info(0x00, 'testTag', `aboutToAppear UIContext: ${uiContext.getId()}`)
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let resolvedUIContext = UIContext.resolveUIContext();
          let contextByAtomicInterface = GetUIContextByAtomicInterface();
          hilog.info(0x00, 'testTag',
            `UIContext id: ${resolvedUIContext.getId()}, strategy: ${resolvedUIContext.strategy}}, contextByAtomicInterface: ${contextByAtomicInterface.getId()}`);
          this.message = 'Welcome';
        })
    }
    .height('100%')
    .width('100%')
  }
```

**getCallingScopeUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)22+**

static getCallingScopeUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)(): UIContext | undefined

获取当前[调用作用域](Class (UIContext).md)的UIContext，调用作用域不明确时返回undefined。


返回的UIContext对象可能指向一个已销毁的UI实例，通常在由已销毁的实例抛出异步任务时出现。建议通过[isAvailable](#ZH-CN_TOPIC_0000002522240732__isavailable20)接口判断其有效性。

元服务API： 从API version 22开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12) | undefined | 当前调用作用域的UIContext，调用作用域不明确时返回undefined。 |

示例：

```ets
import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
          let uiContext = UIContext.getCallingScopeUIContext();
          hilog.info(0x00, 'testTag', 'Current calling UIContext is : ' + uiContext?.isAvailable());
        })
    }
    .height('100%')
    .width('100%')
  }
```

**getLastFocusedUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)22+**

static getLastFocusedUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)(): UIContext | undefined

获取最近一次切换到获焦状态的UI实例的UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)。

元服务API： 从API version 22开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12) | undefined | 返回最近一次切换到获焦状态的UI实例的UIContext。如果最近一次切换到获焦状态的实例已被销毁或无实例曾经处于获焦状态，返回undefined。 |

示例：

```ets
import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
          let uiContext = UIContext.getLastFocusedUIContext();
          hilog.info(0x00, 'testTag', 'Current calling UIContext is : ' + uiContext?.isAvailable());
        })
    }
    .height('100%')
    .width('100%')
  }
```

**getLastForegroundUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)22+**

static getLastForegroundUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)(): UIContext | undefined

获取最近一次切换到前台状态的UI实例的UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)。

元服务API： 从API version 22开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12) | undefined | 返回最近一次切换到前台状态的UI实例的UIContext。如果最近一次切换到前台状态的UI实例已被销毁或无UI实例曾经处于前台状态，则返回undefined。 |

示例：

```ets
import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
          let uiContext = UIContext.getLastForegroundUIContext();
          hilog.info(0x00, 'testTag', 'Current calling UIContext is : ' + uiContext?.isAvailable());
        })
    }
    .height('100%')
    .width('100%')
  }
```

**getAllUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)s22+**

static getAllUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)s(): UIContext[]

获取所有当前有效的UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)实例。

元服务API： 从API version 22开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)[] | 返回所有当前有效UIContext实例的数组。如果没有有效的UIContext实例，则返回空数组。 |

示例：

```ets
import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
          let uiContexts = UIContext.getAllUIContexts();
          hilog.info(0x00, 'testTag', `There are ${uiContexts.length} UIContext(s)`);
        })
    }
    .height('100%')
    .width('100%')
  }
```

**resolveUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)22+**

static resolveUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)(): ResolvedUIContext

使用优先级策略获取带有解析策略的UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)实例对象。


按照预定义的优先级顺序解析并返回UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)实例和UIContext的解析策略。

解析规则按顺序如下：

1. 当前调用作用域中的UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)。

1. 如果只存在一个UI实例，则返回其UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)。

1. 如果存在UI实例切换到获焦状态，且最近一次切换到获焦状态的UI实例未销毁，则返回最近一次获焦UI实例的UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)。

1. 如果存在UI实例切换到前台状态，且最近一次切换到前台状态的UI实例未销毁，则返回最近一次切换到前台状态的UI实例的UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)。

1. 如果存在多个UI实例，则返回实例唯一标识的ID最大的UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)。

1. 如果以上条件均不满足，则返回一个无效的UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)实例。

元服务API： 从API version 22开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| ResolvedUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12) | 返回带有解析策略的UIContext实例对象。 |

示例：

```ets
import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('click').onClick(() => {
        let resolvedUIContext = UIContext.resolveUIContext();
        hilog.info(0x00, 'testTag', `UIContext id: ${resolvedUIContext.getId()}, strategy: ${resolvedUIContext.strategy}}`);
      })
    }
    .width(UIContext.resolveUIContext().px2vp(100))
    .height('100%')
}
```

#### isAvailable20+

isAvailable(): boolean

判断UIContext对象对应的UI实例是否有效。使用[getUIContext](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__getuicontext10)方法获取UIContext对象。后端UI实例存在时，该UI实例有效。通过new UIContext()创建的UIContext对象无对应的UI实例；多次[loadContent](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__loadcontent9)后，旧的UI实例会失效。多窗口应用场景，当窗口关闭后，该窗口的UI实例失效。总而言之，当UIContext对象没有对应的后端UI实例时，该对象是无效的。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)对象对应的UI实例是否有效。true表示有效，false表示无效。 |

**示例：**

```ets
import { UIContext } from '@kit.ArkUI'

@Entry
@Component
struct UIContextCompare {
  @State result1: string = ""
  @State result2: string = ""

  build() {
    Column() {
      Text("getUIContext() 结果: " + this.result1)
        .fontSize(20)
        .margin(10)

      Text("new UIContext() 结果: " + this.result2)
        .fontSize(20)
        .margin(10)

      Divider().margin(20)

      Button("getUIContext()")
        .width("70%")
        .height(50)
        .margin(10)
        .onClick(() => {
          try {
            const ctx: UIContext = this.getUIContext();
            const available: boolean = ctx.isAvailable();
            this.result1 = `可用状态: ${available} UI实例有效 `;
            console.info("getUIContext测试:", available);
          } catch (e) {
            this.result1 = "错误: " + (e instanceof Error ? e.message : String(e));
          }
        })

      Button("new UIContext()")
        .width("70%")
        .height(50)
        .margin(10)
        .onClick(() => {
          try {
            const ctx: UIContext = new UIContext();
            const available: boolean = ctx.isAvailable();
            this.result2 = `可用状态: ${available} UI实例无效`;
            console.info("new UIContext测试:", available);
          } catch (e) {
            this.result2 = "错误: " + (e instanceof Error ? e.message : String(e));
          }
        })
    }
    .width("100%")
    .height("100%")
    .padding(20)
  }
```

#### getFont

getFont(): Font

获取Font对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Font | 返回Font实例对象。 |

**示例：**

完整示例请参考[Font](Class (Font).md)中的示例。

#### getComponentUtils

getComponentUtils(): ComponentUtils

获取ComponentUtils对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ComponentUtils | 返回ComponentUtils实例对象。 |

**示例：**

完整示例请参考[示例1（获取ComponentUtils对象）](@ohos.arkui.componentUtils (componentUtils).md#ZH-CN_TOPIC_0000002553360643__示例1获取componentutils对象)。

#### getUIInspector

getUIInspector(): UIInspector

获取UIInspector对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| UIInspector | 返回UIInspector实例对象。 |

**示例：**

完整示例请参考[UIInspector](Class (UIInspector).md)中的示例。

#### getUIObserver11+

getUIObserver(): UIObserver

获取UIObserver对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| UIObserver | 返回UIObserver实例对象。 |

**示例：**

```ets
@Component
struct PageOne {
  build() {
    NavDestination() {
      Text("pageOne")
    }.title("pageOne")
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  @Builder
  PageBuilder(name: string) {
    PageOne()
  }

  aboutToAppear() {
    this.getUIContext().getUIObserver().on('navDestinationUpdate', (info) => {
      console.info('NavDestination state update', JSON.stringify(info));
    });
  }

  aboutToDisappear() {
    this.getUIContext().getUIObserver().off('navDestinationUpdate');
  }

  build() {
    Column() {
      Navigation(this.stack) {
        Button("push").onClick(() => {
          this.stack.pushPath({ name: "pageOne" });
        })
      }
      .title("Navigation")
      .navDestination(this.PageBuilder)
    }
    .width('100%')
    .height('100%')
  }
```

#### getId22+

getId(): number

获取UI实例对象唯一标识，多实例场景下，开发者可使用此唯一标识区分多个UI实例对象，便于管理。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回后端实例唯一标识的ID，取值范围：[-1, +∞) |

**示例：**

```ets
@Entry
@Component
struct Index{
  build(){
    Column()
      .width("100%")
      .height("100%")
      .onClick(()=>{
      console.info(`id:${this.getUIContext()?.getId()}`);
    })
}
```

#### getMediaQuery

getMediaQuery(): MediaQuery

获取MediaQuery对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| MediaQuery | 返回MediaQuery实例对象。 |

**示例：**

完整示例请参考[mediaquery示例](@ohos.mediaquery (媒体查询).md#ZH-CN_TOPIC_0000002522080740__示例)。

#### getRouter

getRouter(): Router

获取Router对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Router | 返回Router实例对象。 |

**示例：**

完整示例请参考[pushUrl](Class (Router).md#ZH-CN_TOPIC_0000002553200695__pushurl)。

#### getPromptAction

getPromptAction(): PromptAction

获取PromptAction对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PromptAction | 返回PromptAction实例对象。 |

**示例：**

完整示例请参考[PromptAction](Class (PromptAction).md)中的示例。

#### getOverlayManager12+

getOverlayManager(): OverlayManager

获取OverlayManager对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：**: SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| OverlayManager | 返回OverlayManager实例对象。 |

**示例：**

完整示例请参考[OverlayManager](Class (OverlayManager).md)中的示例。

#### setOverlayManagerOptions15+

setOverlayManagerOptions(options: OverlayManagerOptions): boolean

设置[OverlayManager](Class (OverlayManager).md)参数。用于在使用OverlayManager能力之前先初始化overlayManager的参数，包括是否需要渲染overlay根节点等属性。该方法需要在执行getOverlayManager方法之前执行生效，且该方法只生效一次。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：**: SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | OverlayManagerOptions | 是 | OverlayManager参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否设置成功。 返回true表示设置成功。返回false表示设置失败。 |

**示例：**

完整示例请参考[OverlayManager](Class (OverlayManager).md)中的示例。

#### getOverlayManagerOptions15+

getOverlayManagerOptions(): OverlayManagerOptions

用于获取当前[OverlayManagerOptions](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200699__overlaymanageroptions15)参数。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：**: SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| OverlayManagerOptions | 返回当前OverlayManagerOptions。 |

**示例：**

完整示例请参考[OverlayManager](Class (OverlayManager).md)中的示例。

**animateToImmediately23+**

animateToImmediately(param: AnimateParam, processor: Callback<void>): void

通过UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)对象指定明确的动画主实例上下文，并触发显式动画立即下发。避免由于找不到实例或实例不对，导致的动画不执行或动画结束回调不执行问题。使用callback异步回调。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | AnimateParam | 是 | 设置动画效果相关参数。 |
| processor | Callback<void> | 是 | 回调函数。指定显示动效的闭包函数，在闭包函数中导致的状态变化系统会自动插入过渡动画。 |

示例：

该示例通过UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)对象获取显式立即动画，并调用animateToImmediately接口实现参数定义的动画效果。

```ets
// xxx.ets
@Entry
@Component
struct AnimateToImmediatelyExample {
  @State widthSize: number = 250
  @State heightSize: number = 100
  @State opacitySize: number = 0
  private flag: boolean = true
  uiContext: UIContext | null | undefined = this.getUIContext();

  build() {
    Column() {
      Column()
        .width(this.widthSize)
        .height(this.heightSize)
        .backgroundColor(Color.Green)
        .opacity(this.opacitySize)
      Button('change size')
        .margin(30)
        .onClick(() => {
          if (this.flag) {
            this.uiContext?.animateToImmediately({
              delay: 0,
              duration: 1000
            }, () => {
              this.opacitySize = 1
            })
            this.uiContext?.animateTo({
              delay: 1000,
              duration: 1000
            }, () => {
              this.widthSize = 150
              this.heightSize = 60
            })
          } else {
            this.uiContext?.animateToImmediately({
              delay: 0,
              duration: 1000
            }, () => {
              this.widthSize = 250
              this.heightSize = 100
            })
            this.uiContext?.animateTo({
              delay: 1000,
              duration: 1000
            }, () => {
              this.opacitySize = 0
            })
          }
          this.flag = !this.flag
        })
    }.width('100%').margin({ top: 5 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553364603.webp)

#### animateTo

animateTo(value: AnimateParam, event: () => void): void

提供animateTo接口来指定由于闭包代码导致的状态变化插入过渡动效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full


- 不推荐在[aboutToAppear](../../topics/components/自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__abouttoappear)、[aboutToDisappear](../../topics/components/自定义组件的生命周期.md#ZH-CN_TOPIC_0000002529444913__abouttodisappear)中调用动画。

- 如果在[aboutToAppear](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002553200861__abouttoappear)中调用动画，自定义组件内的build还未执行，内部组件还未创建，动画时机过早，动画属性没有初值无法对组件产生动画。

- 执行[aboutToDisappear](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002553200861__abouttodisappear)时，组件即将销毁，不能在aboutToDisappear里面做动画。

- 在组件出现和消失时，可以通过[组件内转场](组件内转场 (transition).md)添加动画效果。

- 组件内转场不支持的属性，可以参考[显式动画](显式动画 (animateTo).md)中的[示例2](显式动画 (animateTo).md#ZH-CN_TOPIC_0000002553360803__示例2动画执行结束后组件消失)，使用animateTo实现动画执行结束后组件消失的效果。

- 某些场景下，在[状态管理V2](../../guides/状态管理概述.md#状态管理v2)中使用animateTo动画，会产生异常效果，具体可参考：[在状态管理V2中使用animateTo动画效果异常](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-local#在状态管理v2中使用animateto动画效果异常)。

- UIAbility从前台切换至后台时会立即结束仍在步进中的有限循环动画，从而触发[onFinish动画播放完成回调](显式动画 (animateTo).md#ZH-CN_TOPIC_0000002553360803__animateparam对象说明)。

- 在设置的开发者选项中关闭过渡动画，动画会当帧结束，onFinish动画播放完成回调会立即执行，请避免在回调中加入时序相关的功能逻辑。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | AnimateParam | 是 | 设置动画效果相关参数。 |
| event | () => void | 是 | 指定显示动效的闭包函数，在闭包函数中导致的状态变化系统会自动插入过渡动画。 |

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct AnimateToExample {
  @State widthSize: number = 250;
  @State heightSize: number = 100;
  @State rotateAngle: number = 0;
  private flag: boolean = true;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
    if (!this.uiContext) {
      console.warn("no uiContext");
      return;
  }

  build() {
    Column() {
      Button('change size')
        .width(this.widthSize)
        .height(this.heightSize)
        .margin(30)
        .onClick(() => {
          if (this.flag) {
            this.uiContext?.animateTo({
              duration: 2000,
              curve: Curve.EaseOut,
              iterations: 3,
              playMode: PlayMode.Normal,
              onFinish: () => {
                console.info('play end');
              }
            }, () => {
              this.widthSize = 150;
              this.heightSize = 60;
            });
          } else {
            this.uiContext?.animateTo({}, () => {
              this.widthSize = 250;
              this.heightSize = 100;
            });
          }
          this.flag = !this.flag;
        })
      Button('stop rotating')
        .margin(50)
        .rotate({ x: 0, y: 0, z: 1, angle: this.rotateAngle })
        .onAppear(() => {
          // 组件出现时开始做动画
          this.uiContext?.animateTo({
            duration: 1200,
            curve: Curve.Friction,
            delay: 500,
            iterations: -1, // 设置-1表示动画无限循环
            playMode: PlayMode.Alternate,
            expectedFrameRateRange: {
              min: 10,
              max: 120,
              expected: 60,
            }
          }, () => {
            this.rotateAngle = 90
          });
        })
        .onClick(() => {
          this.uiContext?.animateTo({ duration: 0 }, () => {
            // this.rotateAngle之前为90，在duration为0的动画中修改属性，可以停止该属性之前的动画，按新设置的属性显示
            this.rotateAngle = 0;
          });
        })
    }.width('100%').margin({ top: 5 })
  }
```

#### getShared[LocalStorage](../../topics/components/应用级变量的状态管理.md#ZH-CN_TOPIC_0000002529284961__localstorage9)12+

getShared[LocalStorage](../../topics/components/应用级变量的状态管理.md#ZH-CN_TOPIC_0000002529284961__localstorage9)(): LocalStorage | undefined

获取当前stage共享的[LocalStorage](../../topics/components/应用级变量的状态管理.md#ZH-CN_TOPIC_0000002529284961__localstorage9)实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LocalStorage](../../topics/components/应用级变量的状态管理.md#ZH-CN_TOPIC_0000002529284961__localstorage9) | undefined | 返回LocalStorage实例。共享的LocalStorage实例不存在时返回undefined。 |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  storage: LocalStorage = new LocalStorage();

  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', this.storage);
}
```

```ets
// Index.ets

@Entry
@Component
struct SharedLocalStorage {
  localStorage = this.getUIContext().getSharedLocalStorage();

  build() {
    Row() {
      Column() {
        Button("Change Local Storage to 47")
          .onClick(() => {
            this.localStorage?.setOrCreate("propA", 47);
          })
        Button("Get Local Storage")
          .onClick(() => {
            console.info(`localStorage: ${this.localStorage?.get("propA")}`);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### getHost[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)12+

getHost[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)(): Context | undefined

获得当前元能力的[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12) | undefined | 返回当前组件所在Ability的Context，Context的具体类型为当前Ability关联的Context对象。例如：在UIAbility窗口中的页面调用该接口，返回类型为[UIAbilityContext](../../topics/misc/[UIAbilityContext](../../topics/misc/UIAbilityContext.md).md#ZH-CN_TOPIC_0000002497604628__uiabilitycontext-1)。在ExtensionAbility窗口中的页面调用该接口，返回类型为[ExtensionContext](../../topics/misc/ExtensionContext.md)。ability上下文不存在时返回undefined。 |

**示例：**

```ets
@Entry
@Component
struct Index {
  uiContext = this.getUIContext();

  build() {
    Row() {
      Column() {
        Text("cacheDir='"+this.uiContext?.getHostContext()?.cacheDir+"'")
          .fontSize(25)
          .border({ color:Color.Red, width:2 })
          .padding(50)
        Text("bundleCodeDir='"+this.uiContext?.getHostContext()?.bundleCodeDir+"'")
          .fontSize(25)
          .border({ color:Color.Red, width:2 })
          .padding(50)
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### get[FrameNode](../../topics/misc/FrameNode.md)ById12+

get[FrameNode](../../topics/misc/FrameNode.md)ById(id: string): FrameNode | null

通过组件的id获取组件树的实体节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 节点对应的[组件标识](../../topics/components/组件标识.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](../../topics/misc/FrameNode.md) | null | 返回的组件树的实体节点或者空节点。 |


getFrameNodeById通过遍历查询对应id的节点，性能较差。推荐使用[getAttachedFrameNodeById](#ZH-CN_TOPIC_0000002522240732__getattachedframenodebyid12)。

**示例：**

完整示例请参考[获取根节点示例](FrameNode.md#ZH-CN_TOPIC_0000002522240744__[获取根节点示例](../../topics/misc/FrameNode.md#ZH-CN_TOPIC_0000002529284787__获取根节点示例))。

#### getAttached[FrameNode](../../topics/misc/FrameNode.md)ById12+

getAttached[FrameNode](../../topics/misc/FrameNode.md)ById(id: string): FrameNode | null

通过组件的id获取当前窗口上的实体节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 节点对应的[组件标识](../../topics/components/组件标识.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](../../topics/misc/FrameNode.md) | null | 返回的组件树的实体节点或者空节点。 |


getAttached[FrameNode](../../topics/misc/FrameNode.md)ById仅能查询上屏节点。

**示例：**

```ets
@Entry
@Component
struct MyComponent {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let node = this.getUIContext().getAttachedFrameNodeById("HelloWorld");
          console.info(`Find HelloWorld Tag:${node!.getNodeType()} id:${node!.getUniqueId()}`);
        })
    }
    .height('100%')
    .width('100%')
  }
```

#### get[FrameNode](../../topics/misc/FrameNode.md)ByUniqueId12+

get[FrameNode](../../topics/misc/FrameNode.md)ByUniqueId(id: number): FrameNode | null

提供get[FrameNode](../../topics/misc/FrameNode.md)ByUniqueId接口通过组件的uniqueId获取组件树的实体节点。

1. 当uniqueId对应的是系统组件时，返回组件所对应的[FrameNode](../../topics/misc/FrameNode.md)；
1. 当uniqueId对应的是自定义组件时，若其有渲染内容，则返回该自定义组件的根节点，类型为__Common__；若其无渲染内容，则返回其第一个子组件的[FrameNode](../../topics/misc/FrameNode.md)。
1. 当uniqueId无对应的组件时，返回null。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 节点对应的UniqueId |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](../../topics/misc/FrameNode.md) | null | 返回的组件树的实体节点或者空节点。 |

**示例：**

```ets
import { UIContext, FrameNode } from '@kit.ArkUI';

@Entry
@Component
struct MyComponent {
  aboutToAppear() {
    let uniqueId: number = this.getUniqueId();
    let uiContext: UIContext = this.getUIContext();
    if (uiContext) {
      let node: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
    }

  build() {
    // ...
}
```

#### getPageInfoByUniqueId12+

getPageInfoByUniqueId(id: number): PageInfo

提供getPageInfoByUniqueId接口通过组件的uniqueId获取该节点对应的Router和NavDestination页面信息。

1. 当uniqueId对应的节点在Page节点中，routerPageInfo属性为其对应的Router信息；
1. 当uniqueId对应的节点在NavDestination节点中，navDestinationInfo属性为其对应的NavDestination信息；
1. 当uniqueId对应的节点无对应的Router或NavDestination信息时，对应的属性为undefined；

1. 模态弹窗并不在任何Page节点中。当uniqueId对应的节点在模态弹窗中，例如[CustomDialog](自定义弹窗 (CustomDialog).md)、[bindSheet](半模态转场.md#ZH-CN_TOPIC_0000002522080800__bindsheet)和[bindContentCover](全屏模态转场.md#ZH-CN_TOPIC_0000002553200763__bindcontentcover)构建的模态页面中，routerPageInfo属性为undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 节点对应的UniqueId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PageInfo | 返回节点对应的Router和NavDestination信息。 |

**示例：**

```ets
import { UIContext, PageInfo } from '@kit.ArkUI';

@Entry
@Component
struct PageInfoExample {
  @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();

  build() {
    Column() {
      Navigation(this.pageInfos) {
        NavDestination() {
          MyComponent()
        }
      }.id('navigation')
}

@Component
struct MyComponent {
  @State content: string = '';

  build() {
    Column() {
      Text('PageInfoExample')
      Button('click').onClick(() => {
        const uiContext: UIContext = this.getUIContext();
        const uniqueId: number = this.getUniqueId();
        const pageInfo: PageInfo = uiContext.getPageInfoByUniqueId(uniqueId);
        console.info('pageInfo: ' + JSON.stringify(pageInfo));
        console.info('navigationInfo: ' + JSON.stringify(uiContext.getNavigationInfoByUniqueId(uniqueId)));
      })
      TextArea({
        text: this.content
      })
      .width('100%')
      .height(100)
    }
    .width('100%')
    .alignItems(HorizontalAlign.Center)
  }
```

#### getNavigationInfoByUniqueId12+

getNavigationInfoByUniqueId(id: number): observer.NavigationInfo | undefined

提供getNavigationInfoByUniqueId接口通过组件的uniqueId获取该节点对应的Navigation页面信息。

1. 当uniqueId对应的节点在Navigation节点中，返回其对应的Navigation信息；
1. 当uniqueId对应的节点无对应的Navigation信息时，返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 节点对应的UniqueId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| observer.NavigationInfo | undefined | 返回节点对应的Navigation信息。 |

**示例：**

请参考[getPageInfoByUniqueId](#ZH-CN_TOPIC_0000002522240732__getpageinfobyuniqueid12)的示例。

#### showAlertDialog

showAlertDialog(options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void

显示警告弹窗组件，可设置文本内容与响应回调。


不支持在输入法类型窗口中使用子窗（[showInSubWindow](警告弹窗 (AlertDialog).md#ZH-CN_TOPIC_0000002553200847__alertdialogparam对象说明) 为true）的showAlertDialog，详情见输入法框架的约束与限制说明[createPanel](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__createpanel10-1)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions | 是 | 定义并显示AlertDialog组件。 |

**示例：**

```ets
@Entry
@Component
struct Index {
  uiContext: UIContext = this.getUIContext()

  build() {
    Column() {
      Button('showAlertDialog')
        .onClick(() => {
          this.uiContext.showAlertDialog(
            {
              title: 'title',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              offset: { dx: 0, dy: -20 },
              gridCount: 3,
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              }
          );
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
}
```

#### showActionSheet

showActionSheet(value: Action[SheetOptions](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__sheetoptions)): void

定义列表弹窗并弹出。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Action[SheetOptions](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__sheetoptions) | 是 | 配置列表弹窗的参数。 |

**示例：**

```ets
@Entry
@Component
struct Index {
  uiContext: UIContext = this.getUIContext()

  build() {
    Column() {
      Button('showActionSheet')
        .onClick(() => {
          this.uiContext.showActionSheet({
            title: 'ActionSheet title',
            message: 'message',
            autoCancel: true,
            confirm: {
              value: 'Confirm button',
              action: () => {
                console.info('Get ActionSheet handled');
              }
            },
            cancel: () => {
              console.info('ActionSheet canceled');
            },
            alignment: DialogAlignment.Bottom,
            offset: { dx: 0, dy: -10 },
            sheets: [
              {
                title: 'apples',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('pears');
                }
            ]
          });
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
```

#### showDatePickerDialog

showDatePickerDialog(options: DatePickerDialogOptions): void

定义日期滑动选择器弹窗并弹出。


不支持在输入法类型窗口中使用子窗（showInSubwindow为true）的showDatePickerDialog，详情见输入法框架的约束与限制说明[createPanel](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__createpanel10-1)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | DatePickerDialogOptions | 是 | 配置日期滑动选择器弹窗的参数。 |

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date("2010-1-1");

  build() {
    Row(){
      Column() {
        Button("DatePickerDialog")
          .margin(20)
          .onClick(() => {
            this.getUIContext().showDatePickerDialog({
              start: new Date("2000-1-1"),
              end: new Date("2100-12-31"),
              selected: this.selectedDate,
              showTime: true,
              useMilitaryTime: false,
              dateTimeOptions: { hour: "numeric", minute: "2-digit" },
              onDateAccept: (value: Date) => {
                // 通过Date的setFullYear方法设置按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
                this.selectedDate = value;
                console.info("DatePickerDialog:onDateAccept()" + value.toString());
              },
              onCancel: () => {
                console.info("DatePickerDialog:onCancel()");
              },
              onDateChange: (value: Date) => {
                console.info("DatePickerDialog:onDateChange()" + value.toString());
              },
              onDidAppear: () => {
                console.info("DatePickerDialog:onDidAppear()");
              },
              onDidDisappear: () => {
                console.info("DatePickerDialog:onDidDisappear()");
              },
              onWillAppear: () => {
                console.info("DatePickerDialog:onWillAppear()");
              },
              onWillDisappear: () => {
                console.info("DatePickerDialog:onWillDisappear()");
              }
            })
      }.width('100%')
    }.height('100%')
}
```

#### showTimePickerDialog

showTimePickerDialog(options: TimePickerDialogOptions): void

定义时间滑动选择器弹窗并弹出。


不支持在输入法类型窗口中使用子窗（showInSubwindow为true）的showTimePickerDialog，详情见输入法框架的约束与限制说明[createPanel](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__createpanel10-1)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | TimePickerDialogOptions | 是 | 配置时间滑动选择器弹窗的参数。 |

**示例：**

```ets
// xxx.ets

class SelectTime{
  selectTime: Date = new Date('2020-12-25T08:30:00');
  hours(h:number,m:number){
    this.selectTime.setHours(h, m);
}

@Entry
@Component
struct TimePickerDialogExample {
  @State selectTime: Date = new Date('2023-12-25T08:30:00');

  build() {
    Column() {
      Button('showTimePickerDialog')
        .margin(30)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            selected: this.selectTime,
            onAccept: (value: TimePickerResult) => {
              // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
              let time = new SelectTime();
              if(value.hour && value.minute){
                time.hours(value.hour, value.minute);
              }
              console.info("TimePickerDialog:onAccept()" + JSON.stringify(value));
            },
            onCancel: () => {
              console.info("TimePickerDialog:onCancel()");
            },
            onChange: (value: TimePickerResult) => {
              console.info("TimePickerDialog:onChange()" + JSON.stringify(value));
            }
          });
        })
    }.width('100%').margin({ top: 5 })
  }
```

#### showTextPickerDialog

showTextPickerDialog(options: TextPickerDialogOptions): void

定义文本滑动选择器弹窗并弹出。


不支持在输入法类型窗口中使用子窗（showInSubwindow为true）的showTextPickerDialog，详情见输入法框架的约束与限制说明[createPanel](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__createpanel10-1)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | TextPickerDialogOptions | 是 | 配置文本滑动选择器弹窗的参数。 |

**示例：**

```ets
// xxx.ets

class SelectedValue{
  select: number = 2;
  set(val: number){
    this.select = val;
  }
class SelectedArray{
  select: number[] = [];
  set(val: number[]){
    this.select = val;
}
@Entry
@Component
struct TextPickerDialogExample {
  @State selectTime: Date = new Date('2023-12-25T08:30:00');
  private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4', 'banana5'];
  private select: number  = 0;
  build() {
    Row(){
      Column() {
        Button('showTextPickerDialog')
          .margin(30)
          .onClick(() => {
            this.getUIContext().showTextPickerDialog({
              range: this.fruits,
              selected: this.select,
              onAccept: (value: TextPickerResult) => {
                // 设置select为按下确定按钮时候的选中项index，这样当弹窗再次弹出时显示选中的是上一次确定的选项
                let selectedVal = new SelectedValue();
                let selectedArr = new SelectedArray();
                if (value.index){
                  value.index instanceof Array?selectedArr.set(value.index) : selectedVal.set(value.index);
                }
                console.info("TextPickerDialog:onAccept()" + JSON.stringify(value));
              },
              onCancel: () => {
                console.info("TextPickerDialog:onCancel()");
              },
              onChange: (value: TextPickerResult) => {
                console.info("TextPickerDialog:onChange()" + JSON.stringify(value));
              }
            });
          })
      }.width('100%').margin({ top: 5 })
    }.height('100%')
  }
```

#### showTextPickerDialog20+

showTextPickerDialog(style: TextPickerDialogOptions|TextPickerDialogOptionsExt): void

定义文本滑动选择器弹窗并弹出，相比API version 11，新增了TextPickerDialogOptionsExt参数支持。


不支持在输入法类型窗口中使用子窗（showInSubwindow为true）的showTextPickerDialog，详情见输入法框架的约束与限制说明[createPanel](@ohos.inputMethodEngine (输入法服务).md#ZH-CN_TOPIC_0000002553201227__createpanel10-1)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | TextPickerDialogOptions| TextPickerDialogOptionsExt | 是 | 配置文本滑动选择器弹窗的参数。 |

#### createAnimator

createAnimator(options: AnimatorOptions): AnimatorResult

定义Animator类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | AnimatorOptions | 是 | 定义动画选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AnimatorResult | Animator结果接口。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { AnimatorOptions, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // 创建主窗口，设置此功能的主页
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', err.message);
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
      let uiContext = windowStage.getMainWindowSync().getUIContext();
      let options:AnimatorOptions = {
        duration: 1500,
        easing: "friction",
        delay: 0,
        fill: "forwards",
        direction: "normal",
        iterations: 3,
        begin: 200.0,
        end: 400.0
      };
      uiContext.createAnimator(options);
    });
  }
```

#### createAnimator18+

createAnimator(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult

创建animator动画结果对象（AnimatorResult）。与[createAnimator](#ZH-CN_TOPIC_0000002522240732__createanimator)相比，新增对[SimpleAnimatorOptions](@ohos.animator (动画).md#ZH-CN_TOPIC_0000002553200681__simpleanimatoroptions18)类型入参的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | AnimatorOptions | SimpleAnimatorOptions | 是 | 定义动画选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AnimatorResult | Animator结果接口。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { SimpleAnimatorOptions, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // 创建主窗口，设置此功能的主页
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', err.message);
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
      let uiContext = windowStage.getMainWindowSync().getUIContext();
      let options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).duration(2000);
      uiContext.createAnimator(options);
    });
  }
```

#### runScopedTask

runScopedTask(callback: () => void): void

在当前UI上下文执行传入的回调函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 回调函数 |

**示例：**

```ets
@Entry
@Component
struct Index {
  uiContext = this.getUIContext();

  build() {
    Row() {
      Column() {
        Button("run task").onClick(()=>{
          this.uiContext.runScopedTask(()=>{
            // do something
          })
      }
      .width('100%')
    }
    .height('100%')
}
```

#### set[KeyboardAvoidMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604786__keyboardavoidmode11)11+

set[KeyboardAvoidMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604786__keyboardavoidmode11)(value: KeyboardAvoidMode): void

配置虚拟键盘弹出时，页面的避让模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [KeyboardAvoidMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604786__keyboardavoidmode11) | 是 | 键盘弹出时的页面避让模式。 默认值：KeyboardAvoidMode.OFFSET |


[KeyboardAvoidMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604786__keyboardavoidmode11).RESIZE模式会压缩页面大小，页面中设置百分比宽高的组件会跟随页面压缩，而直接设置宽高的组件会按设置的固定大小布局。设置KeyboardAvoidMode的RESIZE模式时，expandSafeArea([SafeAreaType.KEYBOARD],[SafeAreaEdge.BOTTOM])不生效。

[KeyboardAvoidMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604786__keyboardavoidmode11).NONE模式配置页面不避让键盘，页面会被抬起的键盘遮盖。

setKeyboardAvoidMode针对页面生效，对于弹窗类组件不生效，比如Dialog、Popup、Menu、BindSheet、BindContentCover、Toast、OverlayManager。弹窗类组件的避让模式可以参考[CustomDialogControllerOptions对象说明](自定义弹窗 (CustomDialog).md#ZH-CN_TOPIC_0000002553360809__customdialogcontrolleroptions对象说明)。

**示例：**

完整示例请参考[示例4（设置键盘避让模式为压缩）](安全区域.md#ZH-CN_TOPIC_0000002553360705__示例4设置键盘避让模式为压缩)、[示例5（设置键盘避让模式为上抬）](安全区域.md#ZH-CN_TOPIC_0000002553360705__示例5设置键盘避让模式为上抬)以及[示例6（切换避让模式）](安全区域.md#ZH-CN_TOPIC_0000002553360705__示例6切换避让模式)。

```ets
// EntryAbility.ets
import { KeyboardAvoidMode, UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility{
  onWindowStageCreate(windowStage: window.WindowStage) {

      windowStage.loadContent('pages/Index', (err, data) => {
        let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
        uiContext.setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
      });
    }
```

#### get[KeyboardAvoidMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604786__keyboardavoidmode11)11+

get[KeyboardAvoidMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604786__keyboardavoidmode11)(): KeyboardAvoidMode

获取虚拟键盘弹出时，页面的避让模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [KeyboardAvoidMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604786__keyboardavoidmode11) | 返回当前的页面避让模式。 |

**示例：**

完整示例请参考[示例4（设置键盘避让模式为压缩）](安全区域.md#ZH-CN_TOPIC_0000002553360705__示例4设置键盘避让模式为压缩)、[示例5（设置键盘避让模式为上抬）](安全区域.md#ZH-CN_TOPIC_0000002553360705__示例5设置键盘避让模式为上抬)以及[示例6（切换避让模式）](安全区域.md#ZH-CN_TOPIC_0000002553360705__示例6切换避让模式)。

```ets
// EntryAbility.ets
import { KeyboardAvoidMode, UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility{
  onWindowStageCreate(windowStage: window.WindowStage) {

      windowStage.loadContent('pages/Index', (err, data) => {
        let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
        let KeyboardAvoidMode = uiContext.getKeyboardAvoidMode();
        console.info("KeyboardAvoidMode:", JSON.stringify(KeyboardAvoidMode));
      });
    }
```

#### getAtomicServiceBar11+

getAtomicServiceBar(): Nullable<AtomicServiceBar>

获取AtomicServiceBar对象，通过该对象设置元服务menuBar的属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Nullable<AtomicServiceBar> | 如果是元服务则返回AtomicServerBar类型，否则返回undefined。 |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Main window is created, set main page for this ability
    console.info('Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      let atomicServiceBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
      if (atomicServiceBar != undefined) {
        console.info('Get AtomServiceBar Successfully.');
      } else {
        console.error('Get AtomicServiceBar failed.');
      }
    });
  }
```

#### getDragController11+

getDragController(): DragController

获取DragController对象，可通过该对象创建并发起拖拽。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DragController | 获取DragController对象。 |

**示例：**

完整示例请参考[DragController](Class (DragController).md)中的示例。

#### keyframeAnimateTo11+

keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void

产生关键帧动画。该接口的使用说明请参考[keyframeAnimateTo](关键帧动画 (keyframeAnimateTo).md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | KeyframeAnimateParam | 是 | 关键帧动画的整体动画参数。 |
| keyframes | Array<KeyframeState> | 是 | 所有的关键帧状态的列表。 |

**示例：**

```ets
// xxx.ets
import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct KeyframeDemo {
  @State myScale: number = 1.0;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
  }

  build() {
    Column() {
      Circle()
        .width(100)
        .height(100)
        .fill("#46B1E3")
        .margin(100)
        .scale({ x: this.myScale, y: this.myScale })
        .onClick(() => {
          if (!this.uiContext) {
            console.error("no uiContext, keyframe failed");
            return;
          }
          this.myScale = 1;
          // 设置关键帧动画整体播放3次
          this.uiContext.keyframeAnimateTo({
              iterations: 3,
              expectedFrameRateRange: {
                min: 10,
                max: 120,
                expected: 60,
              }
            }, [
            {
              // 第一段关键帧动画时长为800ms，scale属性做从1到1.5的动画
              duration: 800,
              event: () => {
                this.myScale = 1.5;
              }
            },
            {
              // 第二段关键帧动画时长为500ms，scale属性做从1.5到1的动画
              duration: 500,
              event: () => {
                this.myScale = 1;
              }
          ]);
        })
    }.width('100%').margin({ top: 5 })
}
```

#### getFocusController12+

getFocusController(): FocusController

获取[FocusController](Class (FocusController).md)对象，可通过该对象控制焦点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FocusController | 获取FocusController对象。 |

**示例：**

完整示例请参考[FocusController](Class (FocusController).md)中的示例。

#### getFilteredInspectorTree12+

getFilteredInspectorTree(filters?: Array<string>): string

获取组件树及组件属性。此接口耗时较长，仅适用于测试场景。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filters | Array<string> | 否 | 需要获取的组件属性的过滤列表。目前仅支持过滤字段： "id"：组件唯一标识。 "src"：资源来源。 "content"：元素、组件或对象所包含的信息或数据。 "editable"：是否可编辑。 "scrollable"：是否可滚动。 "selectable"：是否可选择。 "focusable"：是否可聚焦。 "focused"：是否已聚焦。 如果在filters参数中包含以上一个或者多个字段，则未包含的字段会在组件属性查询结果中被过滤掉。如果用户未传入filters参数或者filters参数为空数组，则以上字段全部不会在组件属性查询结果中被过滤掉。 从API version 20开始，支持该过滤字段： "isLayoutInspector"：返回组件树是否包含自定义组件。如果用户未传入filters参数或者filters数组不包含isLayoutInspector，返回的组件树将缺少自定义组件的信息。 其余字段仅供测试场景使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 获取组件树及组件属性的JSON字符串。组件中每个字段的含义请参考[getInspectorInfo](../../topics/misc/FrameNode.md#ZH-CN_TOPIC_0000002529284787__getinspectorinfo12)的返回值说明。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |

**示例：**

```ets
uiContext.getFilteredInspectorTree(['id', 'src', 'content']);
```

```ets
// xxx.ets
import { UIContext } from '@kit.ArkUI';
@Entry
@Component
struct ComponentPage {
  loopConsole(inspectorStr: string, i: string) {
    console.info(`InsTree ${i}| type: ${JSON.parse(inspectorStr).$type}, ID: ${JSON.parse(inspectorStr).$ID}`);
    if (JSON.parse(inspectorStr).$children) {
      i += '-';
      for (let index = 0; index < JSON.parse(inspectorStr).$children.length; index++) {
        this.loopConsole(JSON.stringify(JSON.parse(inspectorStr).$children[index]), i);
  }

  build() {
    Column() {
      Button('content').onClick(() => {
        const uiContext: UIContext = this.getUIContext();
        let inspectorStr = uiContext.getFilteredInspectorTree(['content']);
        console.info(`InsTree : ${inspectorStr}`);
        inspectorStr = JSON.stringify(JSON.parse(inspectorStr));
        this.loopConsole(inspectorStr, '-');
      })
      Button('isLayoutInspector').onClick(() => {
        const uiContext: UIContext = this.getUIContext();
        let inspectorStr = uiContext.getFilteredInspectorTree(['isLayoutInspector']);
        console.info(`InsTree : ${inspectorStr}`);
        inspectorStr = JSON.stringify(JSON.parse(inspectorStr).content);
        this.loopConsole(inspectorStr, '-');
      })
    }
    .width('100%')
    .height('100%')
}
```

当传入"content"过滤字段时，返回的JSON字符串结构如下：

```ets
InsTree : {"$type":"root","width":"720.000000","height":"1280.000000","$resolution":"1.500000","$children":[{"$type":"Column","$ID":15,"type":"build-in","$rect":"[0.00, 72.00],[720.00,1208.00]","$debugLine":"","$attrs":{},"$children":[{"$type":"Button","$ID":16,"type":"build-in","$rect":"[293.00, 72.00],[427.00,132.00]","$debugLine":"","$attrs":{}},{"$type":"Button","$ID":18,"type":"build-in","$rect":"[237.00, 132.00],[484.00,192.00]","$debugLine":"","$attrs":{}}]}]}\
InsTree -| type: root, ID: undefined
InsTree --| type: Column, ID: 15
InsTree ---| type: Button, ID: 16
InsTree ---| type: Button, ID: 18
```

从API version 20开始，当传入"isLayoutInspector"过滤字段时，返回的JSON字符串结构新增外层结构"type"与"content"，其中"content"包含未增加该字段时的原有JSON字符串结构；同时，返回值结构中增添自定义组件。返回的JSON字符串结构如下：

```ets
InsTree : {"type":"root","content":{"$type":"root","width":"720.000000","height":"1280.000000","$resolution":"1.500000","$children":[{"$type":"JsView","$ID":13,"type":"custom","state":{"observedPropertiesInfo":[],"viewInfo":{"componentName":"ComponentPage","id":14,"isV2":false,"isViewActive_":true}},"$rect":"[0.00, 72.00],[720.00,1208.00]","$debugLine":"{\"$line\":\"(0:0)\"}","viewTag":"ComponentPage","$attrs":{"viewKey":"13"},"$children":[{"$type":"Column","$ID":15, "type":"build-in","$rect":"[0.00, 72.00],[720.00,1208.00]","$debugLine":"","$attrs":{ ...
InsTree -| type: root, ID: undefined
InsTree --| type: JsView, ID: 13
InsTree ---| type: Column, ID: 15
InsTree ----| type: Button, ID: 16
InsTree ----| type: Button, ID: 18
```

#### getFilteredInspectorTreeById12+

getFilteredInspectorTreeById(id: string, depth: number, filters?: Array<string>): string

获取指定的组件及其子组件的属性。此接口耗时较长，仅适用于测试场景。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 指定的[组件标识](../../topics/components/组件标识.md)id。 |
| depth | number | 是 | 获取子组件的层数。当取值0时，获取指定的组件及其所有的子孙组件的属性。当取值1时，仅获取指定的组件的属性。当取值2时，指定的组件及其1层子组件的属性。以此类推。 |
| filters | Array<string> | 否 | 需要获取的组件属性的过滤列表。目前仅支持过滤字段： "id"：组件唯一标识。 "src"：资源来源。 "content"：元素、组件或对象所包含的信息或数据。 "editable"：是否可编辑。 "scrollable"：是否可滚动。 "selectable"：是否可选择。 "focusable"：是否可聚焦。 "focused"：是否已聚焦。 如果在filters参数中包含以上一个或者多个字段，则未包含的字段会在组件属性查询结果中被过滤掉。如果用户未传入filters参数或者filters参数为空数组，则以上字段全部不会在组件属性查询结果中被过滤掉。 其余字段仅供测试场景使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 获取指定的组件及其子组件的属性的JSON字符串。组件中每个字段的含义请参考[getInspectorInfo](../../topics/misc/FrameNode.md#ZH-CN_TOPIC_0000002529284787__getinspectorinfo12)的返回值说明。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |

**示例：**

```ets
uiContext.getFilteredInspectorTreeById('testId', 0, ['id', 'src', 'content']);
```

```ets
import { UIContext } from '@kit.ArkUI';
@Entry
@Component
struct ComponentPage {
  build() {
    Column() {
      Text("Hello World")
        .fontSize(20)
        .id("TEXT")
      Button('getFilteredInspectorTreeById').onClick(() => {
        const uiContext: UIContext = this.getUIContext();
        try {
          let inspectorStr = uiContext.getFilteredInspectorTreeById('TEXT', 1, ["id", "src"]);
          console.info(`result1: ${inspectorStr}`);
          inspectorStr = JSON.stringify(JSON.parse(inspectorStr)['$children'][0]);
          console.info(`result2: ${inspectorStr}`);
          inspectorStr = uiContext.getFilteredInspectorTreeById('TEXT', 1, ["src"]);
          inspectorStr = JSON.stringify(JSON.parse(inspectorStr)['$children'][0]);
          console.info(`result3: ${inspectorStr}`);
        } catch(e) {
          console.error(`getFilteredInspectorTreeById error: ${e}`);
        }
      })
    }
    .width('100%')
    .height('100%')
  }
```

返回的JSON字符串结构如下：

```ets
result1: {"$type":"root","width":"1260.000000","height":"2720.000000","$resolution":"3.250000","$children":[{"$type":"Text","$ID":6,"type":"build-in","$rect":"[457.00, 123.00],[804.00,199.00]","$debugLine":"","$attrs":{"id":"TEXT","isLayoutDirtyMarked":false,"isRenderDirtyMarked":false,"isMeasureBoundary":false,"hasPendingRequest":false,"isFirstBuilding":false}}]}
result2: {"$type":"Text","$ID":6,"type":"build-in","$rect":"[457.00, 123.00],[804.00,199.00]","$debugLine":"","$attrs":{"id":"TEXT","isLayoutDirtyMarked":false,"isRenderDirtyMarked":false,"isMeasureBoundary":false,"hasPendingRequest":false,"isFirstBuilding":false}}
result3: {"$type":"Text","$ID":6,"type":"build-in","$rect":"[457.00, 123.00],[804.00,199.00]","$debugLine":"","$attrs":{"isLayoutDirtyMarked":false,"isRenderDirtyMarked":false,"isMeasureBoundary":false,"hasPendingRequest":false,"isFirstBuilding":false}}
```

若需获取getFilteredInspectorTreeById方法中首个参数id指定的组件，须参照示例代码将getFilteredInspectorTreeById方法结果先转换为json对象，随后提取$children数组的首项。通过result2和result3的结果对比可知，如果filters参数由["id", "src"]改为["src"]，获取到的$attrs属性将缺少"id"这一key。

#### getCursorController12+

getCursorController(): CursorController

获取[CursorController](Class (CursorController).md)对象，可通过该对象控制光标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CursorController | 获取CursorController对象。 |

**示例：**

完整示例请参考[CursorController](Class (CursorController).md)中的示例。

#### get[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)MenuController12+

get[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)MenuController(): ContextMenuController

获取[ContextMenuController](Class (ContextMenuController).md)对象，可通过该对象控制菜单。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)MenuController | 获取ContextMenuController对象。 |

#### getMeasureUtils12+

getMeasureUtils(): MeasureUtils

允许用户通过UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)对象，获取MeasureUtils对象进行文本计算。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| MeasureUtils | 提供文本宽度、高度等相关计算。 |

**示例：**

完整示例请参考[MeasureUtils](Class (MeasureUtils).md)中的示例。

#### getComponentSnapshot12+

getComponentSnapshot(): ComponentSnapshot

获取ComponentSnapshot对象，可通过该对象获取组件截图的能力。

典型使用场景（如长截图）及最佳实践请参考[使用组件截图](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-component-snapshot)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ComponentSnapshot | 获取ComponentSnapshot对象。 |

**示例：**

完整示例请参考[ComponentSnapshot](Class (ComponentSnapshot).md)中的示例。

#### vp2px12+

vp2px(value : number) : number

将vp单位的数值转换为以px为单位的数值。

转换公式为：px值 = vp值 × 像素密度

像素密度：当前窗口生效的像素密度值，即屏幕物理像素密度[VirtualScreenConfig](@ohos.display (屏幕属性).md#ZH-CN_TOPIC_0000002522240754__virtualscreenconfig16).density。


1.

getUIContext需在windowStage.[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)之后调用，确保UIContext初始化完成后调用此接口，否则无法返回准确结果。

1.

UI实例未创建时，[像素单位]([像素单位](../../topics/components/像素单位.md).md)中的vp2px接口使用默认屏幕的虚拟像素比进行转换。在该场景下，开发者使用UIContext接口替换时，可参考[像素单位转换接口替换为UIContext接口](Class (UIContext).md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将vp单位的数值转换为以px为单位的数值。 取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。 取值范围：(-∞, +∞) |

**示例：**

```ets
@Entry
@Component
struct MatrixExample {
  build() {
    Column({ space: 100 }) {
      Text('Hello1')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .rotate({
          z: 1,
          angle: 90,
          centerX: this.getUIContext().vp2px(50),
          centerY: this.getUIContext().vp2px(30)
        })
    }.width('100%')
    .height('100%')
  }
```

#### px2vp12+

px2vp(value : number) : number

将px单位的数值转换为以vp为单位的数值。

转换公式为：vp值 = px值 ÷ 像素密度

像素密度：当前窗口生效的像素密度值，即屏幕物理像素密度[VirtualScreenConfig](@ohos.display (屏幕属性).md#ZH-CN_TOPIC_0000002522240754__virtualscreenconfig16).density。


1.

getUIContext需在windowStage.[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)之后调用，确保UIContext初始化完成后调用此接口，否则无法返回准确结果。

1.

UI实例未创建时，[像素单位](像素单位.md)中的px2vp接口使用默认屏幕的虚拟像素比进行转换。在该场景下，开发者使用UIContext接口替换时，可参考[像素单位转换接口替换为UIContext接口](Class (UIContext).md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将px单位的数值转换为以vp为单位的数值。 取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。 取值范围：(-∞, +∞) |

**示例：**

```ets
@Entry
@Component
struct MatrixExample {
  build() {
    Column({ space: 100 }) {
      Text('Hello1')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .rotate({
          z: 1,
          angle: 90,
          centerX: this.getUIContext().px2vp(50),
          centerY: this.getUIContext().px2vp(30)
        })
    }.width('100%')
    .height('100%')
  }
```

#### fp2px12+

fp2px(value : number) : number

将fp单位的数值转换为以px为单位的数值。

转换公式为：px值 = fp值 × 像素密度 × 字体缩放比例

像素密度：当前窗口生效的像素密度值，即屏幕物理像素密度[VirtualScreenConfig](@ohos.display (屏幕属性).md#ZH-CN_TOPIC_0000002522240754__virtualscreenconfig16).density。

字体缩放比例：系统设置的字体缩放系数，对应 [Configuration.fontScale](基础类型定义.md#ZH-CN_TOPIC_0000002553360849__configuration)。


getUIContext需在windowStage.[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)之后调用，确保UIContext初始化完成后调用此接口，否则无法返回准确结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将fp单位的数值转换为以px为单位的数值。 取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。 取值范围：(-∞, +∞) |

**示例：**

```ets
@Entry
@Component
struct MatrixExample {
  build() {
    Column({ space: 100 }) {
      Text('Hello1')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .rotate({
          z: 1,
          angle: 90,
          centerX: this.getUIContext().fp2px(50),
          centerY: this.getUIContext().fp2px(30)
        })
    }.width('100%')
    .height('100%')
  }
```

#### px2fp12+

px2fp(value : number) : number

将px单位的数值转换为以fp为单位的数值。

转换公式为：fp值 = px值 ÷ 像素密度 ÷ 字体缩放比例

像素密度：当前窗口生效的像素密度值，通常就是屏幕物理像素密度[VirtualScreenConfig](@ohos.display (屏幕属性).md#ZH-CN_TOPIC_0000002522240754__virtualscreenconfig16).density。

字体缩放比例：系统设置的字体缩放系数，对应 [Configuration.fontScale](基础类型定义.md#ZH-CN_TOPIC_0000002553360849__configuration)。


getUIContext需在windowStage.[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)之后调用，确保UIContext初始化完成后调用此接口，否则无法返回准确结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将px单位的数值转换为以fp为单位的数值。 取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。 取值范围：(-∞, +∞) |

**示例：**

```ets
@Entry
@Component
struct MatrixExample {
  build() {
    Column({ space: 100 }) {
      Text('Hello1')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .rotate({
          z: 1,
          angle: 90,
          centerX: this.getUIContext().px2fp(50),
          centerY: this.getUIContext().px2fp(30)
        })
    }.width('100%')
    .height('100%')
  }
```

#### lpx2px12+

lpx2px(value : number) : number

将lpx单位的数值转换为以px为单位的数值。

转换公式为：px值 = lpx值 × 实际屏幕宽度与逻辑宽度（通过[designWidth](../../guides/module.json5配置文件.md#pages标签)配置）的比值。


getUIContext需在windowStage.[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)之后调用，确保UIContext初始化完成后调用此接口，否则无法返回准确结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将lpx单位的数值转换为以px为单位的数值。 取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。 取值范围：(-∞, +∞) |

**示例：**

```ets
@Entry
@Component
struct MatrixExample {
  build() {
    Column({ space: 100 }) {
      Text('Hello1')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .rotate({
          z: 1,
          angle: 90,
          centerX: this.getUIContext().lpx2px(50),
          centerY: this.getUIContext().lpx2px(30)
        })
    }.width('100%')
    .height('100%')
  }
```

#### px2lpx12+

px2lpx(value : number) : number

将px单位的数值转换为以lpx为单位的数值。

转换公式为：lpx值 = px值 ÷ 实际屏幕宽度与逻辑宽度（通过[designWidth](../../guides/module.json5配置文件.md#pages标签)配置）的比值。


getUIContext需在windowStage.[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)之后调用，确保UIContext初始化完成后调用此接口，否则无法返回准确结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将px单位的数值转换为以lpx为单位的数值。 取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。 取值范围：(-∞, +∞) |

**示例：**

```ets
@Entry
@Component
struct MatrixExample {
  build() {
    Column({ space: 100 }) {
      Text('Hello1')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .rotate({
          z: 1,
          angle: 90,
          centerX: this.getUIContext().px2lpx(50),
          centerY: this.getUIContext().px2lpx(30)
        })
    }.width('100%')
    .height('100%')
  }
```

#### getWindowName12+

getWindowName(): string | undefined

获取当前实例所在窗口的名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | undefined | 当前实例所在窗口的名称。若窗口不存在，则返回undefined。 |

**示例：**

```ets
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  aboutToAppear() {
    const windowName = this.getUIContext().getWindowName();
    console.info('WindowName ' + windowName);
    const currWindow = window.findWindow(windowName);
    const windowProperties = currWindow.getWindowProperties();
    console.info(`Window width ${windowProperties.windowRect.width}, height ${windowProperties.windowRect.height}`);
  }

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
```

**getWindowId23+**

getWindowId(): number | undefined

获取当前应用实例所属的窗口ID。


若UIContext位于主应用程序进程中的[UIExtensionAbility](@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)内，则返回主应用程序的顶层窗口ID。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

返回值：

| 类型 | 说明 |
| --- | --- |
| number | undefined | 当前应用实例所属的窗口ID。若窗口不存在，则返回undefined。 |

示例：

```ets
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  aboutToAppear() {
    const windowId = this.getUIContext().getWindowId();
    hilog.info(0x0000, 'testTag', 'current window id: %{public}d', windowId);
  }

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
}
```

#### getWindow[WidthBreakpoint](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__widthbreakpoint13)13+

getWindow[WidthBreakpoint](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__widthbreakpoint13)(): WidthBreakpoint

获取当前实例所在窗口的宽度断点枚举值。具体枚举值根据窗口宽度vp值确定，详见 [WidthBreakpoint](枚举说明.md#ZH-CN_TOPIC_0000002553200889__widthbreakpoint13)。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WidthBreakpoint](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__widthbreakpoint13) | 当前实例所在窗口的宽度断点枚举值。若窗口宽度为 0vp，则返回WIDTH_XS。 |

**示例：**

```ets
import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
        Button() {
          Text('test')
            .fontSize(30)
        }
        .onClick(() => {
          let uiContext: UIContext = this.getUIContext();
          let widthBp: WidthBreakpoint = uiContext.getWindowWidthBreakpoint();
          console.info(`Window widthBp: ${widthBp}`);
        })
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### getWindow[HeightBreakpoint](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__heightbreakpoint13)13+

getWindow[HeightBreakpoint](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__heightbreakpoint13)(): HeightBreakpoint

获取当前实例所在窗口的高度断点。具体枚举值根据窗口高宽比确定，详见 [HeightBreakpoint](枚举说明.md#ZH-CN_TOPIC_0000002553200889__heightbreakpoint13)。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HeightBreakpoint](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__heightbreakpoint13) | 当前实例所在窗口的宽高比对应的高度断点枚举值。若窗口高宽比为0，则返回HEIGHT_SM。 |

**示例：**

```ets
import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
        Button() {
          Text('test')
            .fontSize(30)
        }
        .onClick(() => {
          let uiContext: UIContext = this.getUIContext();
          let heightBp: HeightBreakpoint = uiContext.getWindowHeightBreakpoint();
          let widthBp: WidthBreakpoint = uiContext.getWindowWidthBreakpoint();
          console.info(`Window heightBP: ${heightBp}, widthBp: ${widthBp}`);
        })
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### postFrameCallback12+

postFrameCallback(frameCallback: FrameCallback): void

注册一个回调，仅在下一帧渲染时调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| frameCallback | FrameCallback | 是 | 下一帧需要执行的回调。 |

**示例：**

```ets
import {FrameCallback } from '@kit.ArkUI';

class MyFrameCallback extends FrameCallback {
  private tag: string;

  constructor(tag: string) {
    super();
    this.tag = tag;
  }

  onFrame(frameTimeNanos: number) {
    console.info('MyFrameCallback ' + this.tag + ' ' + frameTimeNanos.toString());
  }

@Entry
@Component
struct Index {
  build() {
    Row() {
      Button('点击触发postFrameCallback')
        .onClick(() => {
          this.getUIContext().postFrameCallback(new MyFrameCallback("normTask"));
        })
    }
```

#### postDelayedFrameCallback12+

postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: number): void

注册一个回调，在延迟一段时间后的下一帧进行渲染时执行。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| frameCallback | FrameCallback | 是 | 下一帧需要执行的回调。 |
| delayTime | number | 是 | 延迟的时间，以毫秒为单位。传入null、undefined或小于0的值，会按0处理。 |

**示例：**

```ets
import {FrameCallback } from '@kit.ArkUI';

class MyFrameCallback extends FrameCallback {
  private tag: string;

  constructor(tag: string) {
    super();
    this.tag = tag;
  }

  onFrame(frameTimeNanos: number) {
    console.info('MyFrameCallback ' + this.tag + ' ' + frameTimeNanos.toString());
  }

@Entry
@Component
struct Index {
  build() {
    Row() {
      Button('点击触发postDelayedFrameCallback')
        .onClick(() => {
          this.getUIContext().postDelayedFrameCallback(new MyFrameCallback("delayTask"), 5);
        })
    }
```

#### requireDynamicSyncScene12+

requireDynamicSyncScene(id: string): Array<DynamicSyncScene>

请求组件的动态帧率场景，用于自定义场景相关帧率配置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 节点对应的[组件标识](../../topics/components/组件标识.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<DynamicSyncScene> | 获取DynamicSyncScene对象数组。 |

**示例：**

```ets
import { SwiperDynamicSyncSceneType, SwiperDynamicSyncScene } from '@kit.ArkUI';

@Entry
@Component
struct Frame {
  @State ANIMATION: ExpectedFrameRateRange = { min: 0, max: 120, expected: 90 };
  @State GESTURE: ExpectedFrameRateRange = { min: 0, max: 120, expected: 30};
  private scenes: SwiperDynamicSyncScene[] = [];

  build() {
    Column() {
      Text("动画"+ JSON.stringify(this.ANIMATION))
      Text("跟手"+ JSON.stringify(this.GESTURE))
      Row(){
        Swiper() {
          Text("one")
          Text("two")
          Text("three")
        }
        .width('100%')
        .height('300vp')
        .id("dynamicSwiper")
        .backgroundColor(Color.Blue)
        .autoPlay(true)
        .onAppear(()=>{
          this.scenes = this.getUIContext().requireDynamicSyncScene("dynamicSwiper") as SwiperDynamicSyncScene[];
        })
      }

      Button("set frame")
        .onClick(() => {
          this.scenes.forEach((scenes: SwiperDynamicSyncScene) => {

            if (scenes.type == SwiperDynamicSyncSceneType.ANIMATION) {
              scenes.setFrameRateRange(this.ANIMATION);
            }

            if (scenes.type == SwiperDynamicSyncSceneType.GESTURE) {
              scenes.setFrameRateRange(this.GESTURE);
            }
          });
        })
    }
```

#### openBindSheet12+

openBindSheet<T extends Object>([bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content: [ComponentContent<T>](../../topics/misc/ComponentContent.md), sheetOptions?: SheetOptions, targetId?: number): Promise<void>

创建并弹出以[bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content作为内容的半模态页面，使用Promise异步回调。通过该接口弹出的半模态页面样式完全按照bindSheetContent中设置的样式显示。

1.

使用该接口时，若未传入有效的targetId，则不支持设置[SheetOptions](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__sheetoptions).preferType为POPUP模式、不支持设置SheetOptions.mode为EMBEDDED模式。

1.

由于[updateBindSheet](#ZH-CN_TOPIC_0000002522240732__updatebindsheet12)和[closeBindSheet](#ZH-CN_TOPIC_0000002522240732__closebindsheet12)依赖bindSheetContent去更新或者关闭指定的半模态页面，开发者需自行维护传入的bindSheetContent。

1.

不支持设置SheetOptions.UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content | ComponentContent<T> | 是 | 半模态页面中显示的组件内容。 |
| sheetOptions | SheetOptions | 否 | 半模态页面样式。 说明： 1. 不支持设置SheetOptions.ui[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)，该属性的值固定为当前实例的UIContext。 2. 若不传递targetId，则不支持设置SheetOptions.preferType为POPUP样式，若设置了POPUP样式则使用CENTER样式替代。 3. 若不传递targetId，则不支持设置SheetOptions.mode为EMBEDDED模式，默认为OVERLAY模式。 4. 其余属性的默认值参考SheetOptions文档。 |
targetIdnumber否需要绑定组件的ID，若不指定则不绑定任何组件。id不存在时返回错误码120004。在传入undefined时返回错误码401。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[半模态错误码]([半模态错误码](../../errors/半模态错误码.md).md)错误码。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 120001 | The [bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content is incorrect. |
| 120002 | The [bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content already exists. |
| 120004 | The targetId does not exist. |
| 120005 | The node of targetId is not in the component tree. |
| 120006 | The node of targetId is not a child of the page node or NavDestination node. |

**示例：**

```ets
import { FrameNode, ComponentContent } from "@kit.ArkUI";
import { BusinessError } from '@kit.BasicServicesKit';

class Params {
  text: string = "";

  constructor(text: string) {
    this.text = text;
}

let contentNode: ComponentContent<Params>;
let gUIContext: UIContext;

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
    Button('Update BindSheet')
      .fontSize(20)
      .onClick(() => {
        gUIContext.updateBindSheet(contentNode, {
          backgroundColor: Color.Pink,
        }, true)
          .then(() => {
            console.info('updateBindSheet success');
          })
          .catch((err: BusinessError) => {
            console.error('updateBindSheet error: ' + err.code + ' ' + err.message);
          })

    Button('Close BindSheet')
      .fontSize(20)
      .onClick(() => {
        gUIContext.closeBindSheet(contentNode)
          .then(() => {
            console.info('closeBindSheet success');
          })
          .catch((err: BusinessError) => {
            console.error('closeBindSheet error: ' + err.code + ' ' + err.message);
          })
}

@Entry
@Component
struct UIContextBindSheet {
  @State message: string = 'BindSheet';

  aboutToAppear() {
    gUIContext = this.getUIContext();
    contentNode = new ComponentContent(this.getUIContext(), wrapBuilder(buildText), new Params(this.message));
  }

  build() {
    RelativeContainer() {
      Column() {
        Button('Open BindSheet')
          .fontSize(20)
          .onClick(() => {
            let uiContext = this.getUIContext();
            let uniqueId = this.getUniqueId();
            let frameNode: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
            let targetId = frameNode?.getFirstChild()?.getUniqueId();
            uiContext.openBindSheet(contentNode, {
              height: SheetSize.MEDIUM,
              backgroundColor: Color.Green,
              title: { title: "Title", subtitle: "subtitle" }
            }, targetId)
              .then(() => {
                console.info('openBindSheet success');
              })
              .catch((err: BusinessError) => {
                console.error('openBindSheet error: ' + err.code + ' ' + err.message);
              })
    }
    .height('100%')
    .width('100%')
}
```

#### updateBindSheet12+

updateBindSheet<T extends Object>([bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content: ComponentContent<T>, sheetOptions: SheetOptions, partialUpdate?: boolean ): Promise<void>

更新[bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content对应的半模态页面的样式，使用Promise异步回调。

不支持更新SheetOptions.UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)、SheetOptions.mode、回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content | ComponentContent<T> | 是 | 半模态页面中显示的组件内容。 |
| sheetOptions | SheetOptions | 是 | 半模态页面样式。 说明： 不支持更新SheetOptions.ui[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)、SheetOptions.mode、回调函数。 |
| partialUpdate | boolean | 否 | 半模态页面更新方式, 默认值为false。 说明： 1. true为增量更新，保留当前值，更新[SheetOptions](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__sheetoptions)中的指定属性。 2. false为全量更新，除SheetOptions中的指定属性，其他属性恢复默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[半模态错误码](半模态错误码.md)错误码。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 120001 | The [bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content is incorrect. |
| 120003 | The [bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content cannot be found. |

**示例：**

```ets
import { FrameNode, ComponentContent } from "@kit.ArkUI";
import { BusinessError } from '@kit.BasicServicesKit';

class Params {
  text: string = "";

  constructor(text: string) {
    this.text = text;
}

let contentNode: ComponentContent<Params>;
let gUIContext: UIContext;

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
    Button('Update BindSheet')
      .fontSize(20)
      .onClick(() => {
        gUIContext.updateBindSheet(contentNode, {
          backgroundColor: Color.Pink,
        }, true)
          .then(() => {
            console.info('updateBindSheet success');
          })
          .catch((err: BusinessError) => {
            console.error('updateBindSheet error: ' + err.code + ' ' + err.message);
          })

    Button('Close BindSheet')
      .fontSize(20)
      .onClick(() => {
        gUIContext.closeBindSheet(contentNode)
          .then(() => {
            console.info('closeBindSheet success');
          })
          .catch((err: BusinessError) => {
            console.error('closeBindSheet error: ' + err.code + ' ' + err.message);
          })
}

@Entry
@Component
struct UIContextBindSheet {
  @State message: string = 'BindSheet';

  aboutToAppear() {
    gUIContext = this.getUIContext();
    contentNode = new ComponentContent(this.getUIContext(), wrapBuilder(buildText), new Params(this.message));
  }

  build() {
    RelativeContainer() {
      Column() {
        Button('Open BindSheet')
          .fontSize(20)
          .onClick(() => {
            let uiContext = this.getUIContext();
            let uniqueId = this.getUniqueId();
            let frameNode: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
            let targetId = frameNode?.getFirstChild()?.getUniqueId();
            uiContext.openBindSheet(contentNode, {
              height: SheetSize.MEDIUM,
              backgroundColor: Color.Green,
              title: { title: "Title", subtitle: "subtitle" }
            }, targetId)
              .then(() => {
                console.info('openBindSheet success');
              })
              .catch((err: BusinessError) => {
                console.error('openBindSheet error: ' + err.code + ' ' + err.message);
              })
    }
    .height('100%')
    .width('100%')
}
```

#### closeBindSheet12+

closeBindSheet<T extends Object>([bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content: ComponentContent<T>): Promise<void>

关闭[bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content对应的半模态页面，使用Promise异步回调。

使用此接口关闭半模态页面时，不会触发shouldDismiss回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content | ComponentContent<T> | 是 | 半模态页面中显示的组件内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[半模态错误码](半模态错误码.md)错误码。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 120001 | The [bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content is incorrect. |
| 120003 | The [bindSheet](../../topics/components/半模态转场.md#ZH-CN_TOPIC_0000002497604850__bindsheet)Content cannot be found. |

**示例：**

```ets
import { FrameNode, ComponentContent } from "@kit.ArkUI";
import { BusinessError } from '@kit.BasicServicesKit';

class Params {
  text: string = "";

  constructor(text: string) {
    this.text = text;
}

let contentNode: ComponentContent<Params>;
let gUIContext: UIContext;

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
    Button('Update BindSheet')
      .fontSize(20)
      .onClick(() => {
        gUIContext.updateBindSheet(contentNode, {
          backgroundColor: Color.Pink,
        }, true)
          .then(() => {
            console.info('updateBindSheet success');
          })
          .catch((err: BusinessError) => {
            console.error('updateBindSheet error: ' + err.code + ' ' + err.message);
          })

    Button('Close BindSheet')
      .fontSize(20)
      .onClick(() => {
        gUIContext.closeBindSheet(contentNode)
          .then(() => {
            console.info('closeBindSheet success');
          })
          .catch((err: BusinessError) => {
            console.error('closeBindSheet error: ' + err.code + ' ' + err.message);
          })
}

@Entry
@Component
struct UIContextBindSheet {
  @State message: string = 'BindSheet';

  aboutToAppear() {
    gUIContext = this.getUIContext();
    contentNode = new ComponentContent(this.getUIContext(), wrapBuilder(buildText), new Params(this.message));
  }

  build() {
    RelativeContainer() {
      Column() {
        Button('Open BindSheet')
          .fontSize(20)
          .onClick(() => {
            let uiContext = this.getUIContext();
            let uniqueId = this.getUniqueId();
            let frameNode: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
            let targetId = frameNode?.getFirstChild()?.getUniqueId();
            uiContext.openBindSheet(contentNode, {
              height: SheetSize.MEDIUM,
              backgroundColor: Color.Green,
              title: { title: "Title", subtitle: "subtitle" }
            }, targetId)
              .then(() => {
                console.info('openBindSheet success');
              })
              .catch((err: BusinessError) => {
                console.error('openBindSheet error: ' + err.code + ' ' + err.message);
              })
    }
    .height('100%')
    .width('100%')
}
```

#### isFollowingSystemFontScale13+

isFollowingSystemFontScale(): boolean

获取当前UI上下文是否跟随系统字体倍率。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前UI上下文是否跟随系统字体倍率。 true表示UI上下文跟随系统倍率，false表示UI上下文不跟随系统倍率。 |

**示例：**

参考[configuration标签](../../guides/app.json5配置文件.md#configuration标签)，配置fontSizeScale的值为“followSystem”。

```ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('isFollowingSystemFontScale').onClick(() => {
        console.info('isFollowingSystemFontScale', this.getUIContext().isFollowingSystemFontScale());
      });
    }
```

#### getMaxFontScale13+

getMaxFontScale(): number

获取当前UI上下文最大字体倍率。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前UI上下文最大字体倍率。 |

**示例：**

参考[configuration标签](../../guides/app.json5配置文件.md#configuration标签)，配置fontSizeMaxScale的值为“1.75”。

```ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('getMaxFontScale').onClick(() => {
        console.info('getMaxFontScale', this.getUIContext().getMaxFontScale().toFixed(2));
      });
    }
```

#### bindTabsTo[Scroll](../../topics/components/Scroll.md)able13+

bindTabsTo[Scroll](../../topics/components/Scroll.md)able(tabsController: TabsController, scroller: [Scroller](../../topics/components/Scroll.md#ZH-CN_TOPIC_0000002497444896__scroller)): void

绑定Tabs组件和可滚动容器组件（支持[List]([List](../../topics/components/list.md).md)、[Scroll](Scroll.md)、[Grid]([Grid](../../topics/components/Grid.md).md)、[WaterFlow]([WaterFlow](../../topics/components/WaterFlow.md).md)），当滑动可滚动容器组件时，会触发所有与其绑定的Tabs组件的TabBar的显示和隐藏动效，上滑隐藏，下滑显示。一个TabsController可与多个Scroller绑定，一个Scroller也可与多个TabsController绑定。


当多个可滚动容器组件绑定了同一个Tabs组件时，只要滑动任意一个可滚动容器组件，就会触发TabBar的显示或隐藏。且当任意一个可滚动容器组件滑动到底部时，会立即触发TabBar的显示动效。因此不建议同时触发多个可滚动容器组件的滑动。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tabsController | [TabsController](../../topics/components/tabs.md#ZH-CN_TOPIC_0000002497604882__tabscontroller) | 是 | Tabs组件的控制器。 |
| scroller | [Scroll](../../topics/components/Scroll.md)er | 是 | 可滚动容器组件的控制器。 |

**示例：**

```ets
@Entry
@Component
struct TabsExample {
  private arr: string[] = [];
  private parentTabsController: TabsController = new TabsController();
  private childTabsController: TabsController = new TabsController();
  private listScroller: Scroller = new Scroller();
  private parentScroller: Scroller = new Scroller();
  private childScroller: Scroller = new Scroller();

  aboutToAppear(): void {
    for (let i = 0; i < 20; i++) {
      this.arr.push(i.toString());
    }
    let context = this.getUIContext();
    context.bindTabsToScrollable(this.parentTabsController, this.listScroller);
    context.bindTabsToScrollable(this.childTabsController, this.listScroller);
    context.bindTabsToNestedScrollable(this.parentTabsController, this.parentScroller, this.childScroller);
  }

  aboutToDisappear(): void {
    let context = this.getUIContext();
    context.unbindTabsFromScrollable(this.parentTabsController, this.listScroller);
    context.unbindTabsFromScrollable(this.childTabsController, this.listScroller);
    context.unbindTabsFromNestedScrollable(this.parentTabsController, this.parentScroller, this.childScroller);
  }

  build() {
    Tabs({ barPosition: BarPosition.End, controller: this.parentTabsController }) {
      TabContent() {
        Tabs({ controller: this.childTabsController }) {
          TabContent() {
            List({ space: 20, initialIndex: 0, scroller: this.listScroller }) {
              ForEach(this.arr, (item: string) => {
                ListItem() {
                  Text(item)
                    .width('100%')
                    .height(100)
                    .fontSize(16)
                    .textAlign(TextAlign.Center)
                    .borderRadius(10)
                    .backgroundColor(Color.Gray)
                }
              }, (item: string) => item)
            }
            .scrollBar(BarState.Off)
            .width('90%')
            .height('100%')
            .contentStartOffset(56)
            .contentEndOffset(52)
          }.tabBar(SubTabBarStyle.of('顶部页签'))
        }
        .width('100%')
        .height('100%')
        .barOverlap(true) // 使TabBar叠加在TabContent上，当TabBar向上或向下隐藏后，原位置处不为空白
        .clip(true) // 对超出Tabs组件范围的子组件进行裁剪，防止TabBar向上或向下隐藏后误触TabBar
      }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), 'scroller联动多个TabsController'))

      TabContent() {
        Scroll(this.parentScroller) {
            List({ space: 20, initialIndex: 0, scroller: this.childScroller }) {
              ForEach(this.arr, (item: string) => {
                ListItem() {
                  Text(item)
                    .width('100%')
                    .height(100)
                    .fontSize(16)
                    .textAlign(TextAlign.Center)
                    .borderRadius(10)
                    .backgroundColor(Color.Gray)
                }
              }, (item: string) => item)
            }
            .scrollBar(BarState.Off)
            .width('90%')
            .height('100%')
            .contentEndOffset(52)
            .nestedScroll({ scrollForward: NestedScrollMode.SELF_FIRST, scrollBackward: NestedScrollMode.SELF_FIRST })
        }
        .width('100%')
        .height('100%')
        .scrollBar(BarState.Off)
        .scrollable(ScrollDirection.Vertical)
        .edgeEffect(EdgeEffect.Spring)
      }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), '嵌套的scroller联动TabsController'))
    }
    .width('100%')
    .height('100%')
    .barOverlap(true) // 使TabBar叠加在TabContent上，当TabBar向上或向下隐藏后，原位置处不为空白
    .clip(true) // 对超出Tabs组件范围的子组件进行裁剪，防止TabBar向上或向下隐藏后误触TabBar
  }
```

#### unbindTabsFrom[Scroll](../../topics/components/Scroll.md)able13+

unbindTabsFrom[Scroll](../../topics/components/Scroll.md)able(tabsController: TabsController, scroller: Scroller): void

解除Tabs组件和可滚动容器组件的绑定。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tabsController | [TabsController](../../topics/components/tabs.md#ZH-CN_TOPIC_0000002497604882__tabscontroller) | 是 | Tabs组件的控制器。 |
| scroller | [Scroll](../../topics/components/Scroll.md)er | 是 | 可滚动容器组件的控制器。 |

**示例：**

参考[bindTabsToScrollable](#ZH-CN_TOPIC_0000002522240732__bindtabstoscrollable13)接口示例。

#### bindTabsToNested[Scroll](../../topics/components/Scroll.md)able13+

bindTabsToNested[Scroll](../../topics/components/Scroll.md)able(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void

绑定Tabs组件和嵌套的可滚动容器组件（支持[List](List.md)、[Scroll](Scroll.md)、[Grid](Grid.md)、[WaterFlow](WaterFlow.md)），当滑动父组件或子组件时，会触发所有与其绑定的Tabs组件的TabBar的显示和隐藏动效，上滑隐藏，下滑显示。一个TabsController可与多个嵌套的Scroller绑定，嵌套的Scroller也可与多个TabsController绑定。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tabsController | [TabsController](../../topics/components/tabs.md#ZH-CN_TOPIC_0000002497604882__tabscontroller) | 是 | Tabs组件的控制器。 |
| parent[Scroll](../../topics/components/Scroll.md)er | Scroller | 是 | 可滚动容器组件的控制器。 |
| child[Scroll](../../topics/components/Scroll.md)er | Scroller | 是 | 可滚动容器组件的控制器。其对应组件为parentScroller对应组件的子组件，且组件间存在嵌套滚动关系。 |

**示例：**

参考[bindTabsToScrollable](#ZH-CN_TOPIC_0000002522240732__bindtabstoscrollable13)接口示例。

#### unbindTabsFromNested[Scroll](../../topics/components/Scroll.md)able13+

unbindTabsFromNested[Scroll](../../topics/components/Scroll.md)able(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void

解除Tabs组件和嵌套的可滚动容器组件的绑定。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tabsController | [TabsController](../../topics/components/tabs.md#ZH-CN_TOPIC_0000002497604882__tabscontroller) | 是 | Tabs组件的控制器。 |
| parent[Scroll](../../topics/components/Scroll.md)er | Scroller | 是 | 可滚动容器组件的控制器。 |
| child[Scroll](../../topics/components/Scroll.md)er | Scroller | 是 | 可滚动容器组件的控制器。其对应组件为parentScroller对应组件的子组件，且组件间存在嵌套滚动关系。 |

**示例：**

参考[bindTabsToScrollable](#ZH-CN_TOPIC_0000002522240732__bindtabstoscrollable13)接口示例。

#### enableSwipeBack18+

enableSwipeBack(enabled: Optional<boolean>): void

设置是否支持应用内横向滑动返回上一级。

元服务API： 从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | Optional<boolean> | 是 | 是否支持应用内横向滑动返回，默认值为true。 当值为true时，支持应用内横向滑动返回。 当值为false时，不支持应用内横向滑动返回。 |

**示例：**

```ets
@Entry
@Component
struct Index {
  @State isEnable: boolean = true;

  build() {
    RelativeContainer() {
      Button(`enable swipe back: ${this.isEnable}`).onClick(() => {
        this.isEnable = !this.isEnable;
        this.getUIContext().enableSwipeBack(this.isEnable);
      })
    }
    .height('100%')
    .width('100%')
  }
```

#### getTextMenuController16+

getTextMenuController(): TextMenuController

获取[TextMenuController](Class (TextMenuController).md)对象，可通过该对象控制文本选择菜单。

元服务API： 从API version 16 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| TextMenuController | 获取TextMenuController对象。 |

**示例：**

参考[TextMenuController](Class (TextMenuController).md)接口示例。

#### createUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)WithoutWindow17+

static createUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)WithoutWindow(context: common.UIAbilityContext | common.ExtensionContext) : UIContext | undefined

创建一个不依赖窗口的UI实例，并返回其UI上下文。该接口所创建的UI实例是单例。

返回的UI上下文只可用于创建[自定义节点](../../guides/自定义节点概述.md)，不能执行其他UI操作。

元服务API： 从API version 17 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.UIAbility[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12) | common.ExtensionContext | 是 | UIAbility或ExtensionAbility所对应的上下文环境。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| UI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12) | undefined | 创建的UI实例的上下文，创建失败时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[接口调用异常错误码]([接口调用异常错误码](../../errors/接口调用异常错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. The number of parameters is incorrect. 2. Invalid parameter type of context. |
100001Internal error.

**示例：**

```ets
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    let uiContext : UIContext | undefined = UIContext.createUIContextWithoutWindow(this.context);
  }

  // ......
}
```

#### destroyUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)WithoutWindow17+

static destroyUI[Context](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444808__context12)WithoutWindow(): void

销毁[createUIContextWithoutWindow](#ZH-CN_TOPIC_0000002522240732__createuicontextwithoutwindow17)创建的UI实例。

元服务API： 从API version 17 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ets
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    let uiContext : UIContext | undefined = UIContext.createUIContextWithoutWindow(this.context);
    UIContext.destroyUIContextWithoutWindow();
  }

  // ......
}
```

#### dispatch[KeyEvent](../../topics/components/按键事件.md#ZH-CN_TOPIC_0000002529284805__keyevent对象说明)15+

dispatch[KeyEvent](../../topics/components/按键事件.md#ZH-CN_TOPIC_0000002529284805__keyevent对象说明)(node: number | string, event: KeyEvent): boolean

按键事件应分发给指定的组件。为了确保行为的可预测性，目标组件必须位于分发组件的子树中。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | number | string | 是 | 组件的id或者节点UniqueID。 |
| event | [KeyEvent](../../topics/components/按键事件.md#ZH-CN_TOPIC_0000002529284805__keyevent对象说明) | 是 | KeyEvent对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 按键事件是否成功分发给指定的组件。 true表示分发成功，false表示分发失败。 |

**示例：**

```ets
@Entry
@Component
struct Index {
  build() {
      Row() {
        Button('Button1').id('Button1').onKeyEvent((event) => {
          console.info("Button1");
          return true;
        })
        Button('Button2').id('Button2').onKeyEvent((event) => {
          console.info("Button2");
          return true;
        })
      }
      .width('100%')
      .height('100%')
      .id('Row1')
      .onKeyEventDispatch((event) => {
        let context = this.getUIContext();
        context.getFocusController().requestFocus('Button1');
        return context.dispatchKeyEvent('Button1', event);
      })

    }
    .height('100%')
    .width('100%')
    .onKeyEventDispatch((event) => {
      if (event.type == KeyType.Down) {
        let context = this.getUIContext();
        context.getFocusController().requestFocus('Row1');
        return context.dispatchKeyEvent('Row1', event);
      }
      return true;
    })
  }
```

#### set[PixelRoundMode](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__pixelroundmode18)18+

set[PixelRoundMode](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__pixelroundmode18)(mode: PixelRoundMode): void

配置当前页面的像素取整模式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [PixelRoundMode](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__pixelroundmode18) | 是 | 像素取整模式。 默认值：PixelRoundMode.PIXEL_ROUND_ON_LAYOUT_FINISH |

**示例：**

```ets
// EntryAbility.ets
import { UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility{
  onWindowStageCreate(windowStage: window.WindowStage) {

      windowStage.loadContent('pages/Index', (err, data) => {
        let uiContext :UIContext = windowStage.getMainWindowSync().getUIContext();
        uiContext.setPixelRoundMode(PixelRoundMode.PIXEL_ROUND_ON_LAYOUT_FINISH);
      });
    }
```

#### get[PixelRoundMode](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__pixelroundmode18)18+

get[PixelRoundMode](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__pixelroundmode18)(): PixelRoundMode

获取当前页面的像素取整模式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelRoundMode](../../topics/components/枚举说明.md#ZH-CN_TOPIC_0000002529284967__pixelroundmode18) | 当前页面的像素取整模式。 |

**示例：**

```ets
// EntryAbility.ets
import { UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility{
  onWindowStageCreate(windowStage: window.WindowStage) {

      windowStage.loadContent('pages/Index', (err, data) => {
        let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
        console.info("pixelRoundMode : " + uiContext.getPixelRoundMode().valueOf());
      });
    }
```

#### setResourceManagerCacheMaxCountForHSP21+

static setResourceManagerCacheMaxCountForHSP(count: number): void

设置HSP资源管理对象缓存个数上限。

如果缓存上限设置的太大，有内存开销过大的风险，建议合理配置。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 设置的资源缓存数量，取值范围为非负整数。 |

**错误码：**

以下错误码的详细介绍请参见[UI上下文错误码]([UI上下文错误码](../../errors/UI上下文错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100101 | The parameter is less than 0. |
| 100102 | The parameter value cannot be a floating point number. |
| 100103 | The function cannot be called from a non main thread. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIContext, window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', err.message);
        return;
      }
      UIContext.setResourceManagerCacheMaxCountForHSP(5);
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
```

**setImageCacheCount23+**

setImageCacheCount(value: number): void

设置内存中缓存解码后图片的数量上限，以加快同源图片的再次加载速度。默认值为0，表示不缓存。缓存使用LRU策略，新图片加载超过上限时，会移除最久未使用的缓存。建议根据应用内存需求，合理设置缓存数量，避免内存使用过高。

setImageCacheCount方法需要在@Entry标记的页面，[onPageShow](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002553200861__onpageshow)或[aboutToAppear](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002553200861__abouttoappear)里面设置才生效。

setImageCacheCount、setImageRawDataCacheSize和setImageFileCacheSize并不灵活，后续不继续演进。对于复杂情况，更推荐使用[ImageKnife](https://gitcode.com/openharmony-tpc/ImageKnife)。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内存中解码后图片的缓存数量。 取值范围：[0, +∞) |

示例：

```ets
// xxx.ets
@Entry
@Component
struct Index {
  onPageShow() {
    // 设置解码后图片内存缓存上限为100张
    this.getUIContext().setImageCacheCount(100);
    console.info('Application onPageShow');
  }
  onDestroy() {
    console.info('Application onDestroy');
  }

  build() {
    Row(){
      Image('https://www.example.com/xxx.png') // 请填写一个具体的网络图片地址
        .width(200)
        .height(50)
    }.width('100%')
  }
```

**setImageRawDataCacheSize23+**

setImageRawDataCacheSize(value: number): void

设置内存中缓存解码前图片数据的大小上限，单位为字节，以加快再次加载同源图片的速度。默认值为0，表示不缓存。缓存使用LRU策略，新图片加载后，若解码前数据超过上限，会删除最久未使用的图片数据缓存。建议根据应用内存需求，设置合理的缓存上限，避免内存使用过高。

setImageRawDataCacheSize方法需要在@Entry标记的页面，[onPageShow](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002553200861__onpageshow)或[aboutToAppear](自定义组件的生命周期.md#ZH-CN_TOPIC_0000002553200861__abouttoappear)里面设置才生效。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内存中解码前图片数据的缓存大小，单位为字节。 取值范围：[0, +∞) |

示例：

```ets
// xxx.ets
@Entry
@Component
struct Index {
  onPageShow() {
    // 设置解码前图片数据内存缓存上限为100MB (100MB=100*1024*1024B=104857600B)
    this.getUIContext().setImageRawDataCacheSize(104857600);
    console.info('Application onPageShow');
  }
  onDestroy() {
    console.info('Application onDestroy');
  }

  build() {
    Row(){
      Image('https://www.example.com/xxx.png') // 请填写一个具体的网络图片地址
        .width(200)
        .height(50)
    }.width('100%')
}
```

#### getMagnifier22+

getMagnifier(): Magnifier

获取[Magnifier](Class (Magnifier).md)对象，可控制放大镜显示和隐藏。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Magnifier | Magnifier对象，可用于控制放大镜的显示和隐藏。 |

**示例：**

参考[Magnifier](Class (Magnifier).md)的[bind](Class (Magnifier).md#ZH-CN_TOPIC_0000002553360653__bind)接口示例。

**setCustomKeyboardContinueFeature23+**

setCustomKeyboardContinueFeature(feature: CustomKeyboardContinueFeature): void

设置自定义键盘之间切换时，是否接续。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

模型约束：此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| feature | CustomKeyboardContinueFeature | 是 | 自定义键盘之间切换时是否接续。 默认值：CustomKeyboardContinueFeature.DISABLED，即不接续。 |

示例：

```ets
// xxx.ets
import { CustomKeyboardContinueFeature } from '@ohos.arkui.UIContext';

@Entry
@Component
struct Index {
  controller: TextInputController = new TextInputController();
  controller2: TextInputController = new TextInputController();
  @State inputValue: string = '';
  @State inputValue2: string = '';
  @State supportAvoidance: boolean = true;
  @State isValue: CustomKeyboardContinueFeature = CustomKeyboardContinueFeature.DISABLED;
  @State str: string = '否';

  // 自定义键盘组件
  @Builder
  CustomKeyboardBuilder() {
    Column() {
      Row() {
        Button('x').onClick(() => {
          // 关闭自定义键盘
          this.controller.stopEditing();
        }).margin(10)
        Button('delete').onClick(() => {
          this.inputValue = this.inputValue.slice(0, -1);
        }).margin(10)
      }

      Grid() {
        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
          GridItem() {
            Button(item + '')
              .width(110).onClick(() => {
              this.inputValue += item;
            })
          }
        })
      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
    }.backgroundColor('rgb(213, 213, 213)').height(300)
  }

  // 自定义键盘组件
  @Builder
  CustomKeyboardBuilder2() {
    Column() {
      Row() {
        Button('x').onClick(() => {
          // 关闭自定义键盘
          this.controller2.stopEditing();
        }).margin(10)
        Button('delete').onClick(() => {
          this.inputValue2 = this.inputValue2.slice(0, -1);
        }).margin(10)
      }

      Grid() {
        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
          GridItem() {
            Button(item + '')
              .width(110).onClick(() => {
              this.inputValue2 += item;
            })
          }
        })
      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
    }.backgroundColor('rgb(227, 248, 249)').height(150)
  }

  build() {
    Scroll() {
      Column() {
        Button('是否接续：' + this.str).onClick(() => {
          if (this.isValue == CustomKeyboardContinueFeature.ENABLED) {
            this.isValue = CustomKeyboardContinueFeature.DISABLED
            this.str = '否'
          } else {
            this.isValue = CustomKeyboardContinueFeature.ENABLED
            this.str = '是'
          }
          this.getUIContext().setCustomKeyboardContinueFeature(this.isValue);
        }).fontSize(20).width('80%').key('button')

        TextInput({
          placeholder: 'TextInput1 bind CustomKeyboardBuilder',
          controller: this.controller,
          text: this.inputValue
        })// 绑定自定义键盘
          .customKeyboard(this.CustomKeyboardBuilder(), { supportAvoidance: this.supportAvoidance })
          .margin(10)
          .border({ width: 1 })
        TextInput({
          placeholder: 'TextInput2 bind CustomKeyboardBuilder2',
          controller: this.controller2,
          text: this.inputValue2
        })// 绑定自定义键盘
          .customKeyboard(this.CustomKeyboardBuilder2(), { supportAvoidance: this.supportAvoidance })
          .margin(10)
          .border({ width: 1 })
      }
```

![image](public_sys-resources/zh-cn_image_0000002553204647.webp)