# Class (UIInspector)

提供注册组件布局和组件绘制送显完成回调通知的能力。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 10开始支持。

-

以下API需先使用UIContext中的[getUIInspector()](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__getuiinspector)方法获取到UIInspector对象，再通过该对象调用对应方法。

#### createComponentObserver

createComponentObserver(id: string): inspector.ComponentObserver

注册组件布局和组件绘制送显完成回调通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明idstring是指定组件id，该id通过通用属性[id](../../topics/misc/组件标识.md#ZH-CN_TOPIC_0000002497604824__id)或者[key](../../topics/misc/组件标识.md#ZH-CN_TOPIC_0000002497604824__key12)设置。

**返回值：**

类型说明[inspector.ComponentObserver](../../modules/ohos/@ohos.arkui.inspector (布局回调).md#ZH-CN_TOPIC_0000002497444792__componentobserver)组件回调事件监听句柄，用于注册和取消注册监听回调。

**示例：**

```ets
import { inspector, UIInspector } from '@kit.ArkUI'

@Entry
@Component
struct UIInspectorExample {
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row({ space: 5 }) {
          Text("UIInspector")
            .width(110)
            .height(110)
            .border({ width: 1 })
            .id('TEXT_ID')
        }.width(80).width(80)
      }.width(80).width(80)
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }

  uiInspector: UIInspector = this.getUIContext().getUIInspector();
  listener:inspector.ComponentObserver = this.uiInspector.createComponentObserver("TEXT_ID")

  aboutToAppear() {
    let onLayoutComplete:()=>void=():void=>{
      console.info("TEXT_ID layout complete")
    }
    let onDrawComplete:()=>void=():void=>{
      console.info("TEXT_ID draw complete")
    }

    this.listener.on('layout', onLayoutComplete)
    this.listener.on('draw', onDrawComplete)

    // 通过句柄向对应的查询条件取消注册回调，由开发者自行决定在何时调用。
    // this.listener.off('layout', onLayoutComplete)
    // this.listener.off('draw', onDrawComplete)
  }
}
```