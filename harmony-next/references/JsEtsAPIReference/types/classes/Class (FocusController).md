# Class (FocusController)

提供控制焦点的能力，如清除、移动和激活焦点等功能。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 12开始支持。

-

以下API需先使用UIContext中的[getFocusController()](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getfocuscontroller12)方法获取FocusController实例，再通过该实例调用对应方法。

#### clearFocus12+

clearFocus(): void

清除焦点，将焦点强制转移到页面根容器节点，焦点链路上其他节点失焦。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

在该示例中，按钮"button2"默认获焦，点击按钮"clearFocus"后，焦点回到该页面的根容器节点"column1"，此时按下键盘TAB键，按钮"button2"重新获焦。可通过点击"button1"使该按钮获焦，点击按钮"clearFocus"后，焦点同样回到该页面的根容器节点"column1"，此时按下键盘TAB键，由按钮"button1"重新获焦。

```ets
@Entry
@Component
struct ClearFocusExample {
  @State inputValue: string = '';
  @State btColor: Color = Color.Blue;

  build() {
    Column({ space: 20 }) {
      Column({ space: 5 }) {
        Button('button1')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .focusOnTouch(true)
          .backgroundColor(Color.Blue)
        Button('button2')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .focusOnTouch(true)
          .backgroundColor(this.btColor)
          .defaultFocus(true)
          .onFocus(() => {
            this.btColor = Color.Red;
          })
          .onBlur(() => {
            this.btColor = Color.Blue;
          })
        Button('clearFocus')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .backgroundColor(Color.Blue)
          .onClick(() => {
            this.getUIContext().getFocusController().clearFocus();
          })
      }
      .id('column2')
    }
    .id('column1')
    .width('100%')
    .height('100%')
  }
```

#### requestFocus12+

requestFocus(key: string): void

通过组件的id将焦点转移到组件树对应的实体节点，当前帧生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 节点对应的[组件标识](../../topics/components/组件标识.md)。 |

**错误码：**

以下错误码的详细介绍请参见[焦点错误码]([焦点错误码](../../errors/焦点错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 150001 | the component cannot be focused. |
| 150002 | This component has an unfocusable ancestor. |
| 150003 | the component is not on tree or does not exist. |

**示例：**

```ets
@Entry
@Component
struct RequestExample {
  @State btColor: Color = Color.Blue;

  build() {
    Column({ space: 20 }) {
      Column({ space: 5 }) {
        Button('Button')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .focusOnTouch(true)
          .backgroundColor(this.btColor)
          .onFocus(() => {
            this.btColor = Color.Red;
          })
          .onBlur(() => {
            this.btColor = Color.Blue;
          })
          .id("testButton")

        Divider()
          .vertical(false)
          .width("80%")
          .backgroundColor(Color.Black)
          .height(10)

        Button('requestFocus')
          .width(200)
          .height(70)
          .onClick(() => {
            this.getUIContext().getFocusController().requestFocus("testButton");
          })

        Button('requestFocus fail')
          .width(200)
          .height(70)
          .onClick(() => {
            try {
              this.getUIContext().getFocusController().requestFocus("eee");
            } catch (error) {
              console.error(`requestFocus failed code is ${error.code} message is ${error.message}`);
            }
          })
      }
    .width('100%')
    .height('100%')
}
```

#### activate14+

activate(isActive: boolean, autoInactive?: boolean): void

设置当前界面的[焦点激活态](../../topics/components/焦点事件.md)。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isActive | boolean | 是 | 设置是否进入/退出焦点激活态。 true表示设置进入焦点激活态，false表示设置退出焦点激活态。 |
| autoInactive | boolean | 否 | 设置焦点激活态退出逻辑。 为true时，会自动在触摸事件、鼠标事件触发时退出，为false时，仅受开发者API控制。 默认值：true |

**示例：**

```ets
// 该示例表示在页面加载完成时进入焦点激活态，可按方向键在button间走焦
@Entry
@Component
struct ActivateExample {
  aboutToAppear() {
    this.getUIContext().getFocusController().activate(true, false);
  }

  aboutToDisappear() {
    this.getUIContext().getFocusController().activate(false);
  }

  build() {
    Row() {
      Button('Button1')
        .width(200)
        .height(70)
        .defaultFocus(true)

      Button('Button2')
        .width(200)
        .height(70)

      Button('Button3')
        .width(200)
        .height(70)
    }
    .padding(10)
    .justifyContent(FlexAlign.SpaceBetween)
    .width(800)
  }
```

#### isActive20+

isActive(): boolean

返回UI实例的焦点激活态。

焦点激活态可参考[基础概念：焦点激活态](../../topics/components/焦点事件.md)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回UI实例的焦点激活态。true表示当前进入焦点激活态，false表示当前已退出焦点激活态。 |

**示例：**

验证isActive返回UI实例的焦点激活态。

```ets
@Entry
@Component
struct ClearFocusExample {
  @State inputValue: string = '';
  @State btColor: Color = Color.Blue;

  build() {
    Column({ space: 20 }) {
      Column({ space: 5 }) {
        Button('button1')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .focusOnTouch(true)
          .backgroundColor(Color.Blue)
          .onClick(()=> {
            console.info("button1 onClick");
            this.getUIContext().getFocusController().activate(true);
            console.info(`focus status ${this.getUIContext().getFocusController().isActive()}`);
          })
        Button('button2')
          .width(200)
          .height(70)
          .fontColor(Color.White)
          .focusOnTouch(true)
          .backgroundColor(this.btColor)
          .defaultFocus(true)
          .onClick(()=> {
            console.info("button2 onClick");
            this.getUIContext().getFocusController().activate(false);
            console.info(`focus status ${this.getUIContext().getFocusController().isActive()}`);
          })
          .onFocus(() => {
            this.btColor = Color.Red;
          })
          .onBlur(() => {
            this.btColor = Color.Blue;
          })
      }
    .width('100%')
    .height('100%')
}
```

#### setAutoFocusTransfer14+

setAutoFocusTransfer(isAutoFocusTransfer: boolean): void

设置页面切换时，新的页面是否需要主动获取焦点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isAutoFocusTransfer | boolean | 是 | 设置页面切换时，新的页面是否需要主动获取焦点，例如Router、[Navigation](../../topics/components/Navigation.md)、[Menu](../../topics/components/menu.md)、Dialog、[Popup](../../topics/misc/popup.md)等。true表示需要主动获取焦点，false表示不需要主动获取焦点。默认值为true。 |

**示例：**

```ets
@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;
  build() {
    Column() {
      Text('这是自定义弹窗')
        .fontSize(30)
        .height(100)
      Text('弹窗不能主动获取焦点')
        .fontSize(20)
        .height(100)
      Button('点我关闭弹窗')
        .onClick(() => {
          if (this.controller != undefined) {
            this.getUIContext().getFocusController().setAutoFocusTransfer(true);
            this.controller.close();
          }
        })
        .margin(20)
    }

@Entry
@Component
struct CustomDialogUser {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({}),
  });
  aboutToDisappear() {
    this.dialogController = null;
  }

  build() {
    Column() {
      Button('click me')
        .onClick(() => {
          if (this.dialogController != null) {
            this.getUIContext().getFocusController().setAutoFocusTransfer(false);
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
```

#### set[KeyProcessingMode](../../topics/components/焦点控制.md#ZH-CN_TOPIC_0000002529444807__keyprocessingmode15)15+

set[KeyProcessingMode](../../topics/components/焦点控制.md#ZH-CN_TOPIC_0000002529444807__keyprocessingmode15)(mode: KeyProcessingMode): void

设置按键事件处理的优先级。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [KeyProcessingMode](../../topics/components/焦点控制.md#ZH-CN_TOPIC_0000002529444807__keyprocessingmode15) | 是 | 按键处理模式。 |

**示例：**

```ets
// 该示例演示了在页面加载完成后设置走焦类型的实现方式。
@Entry
@Component
struct Index {
  aboutToAppear() {
    this.getUIContext().getFocusController().setKeyProcessingMode(KeyProcessingMode.ANCESTOR_EVENT);
  }

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