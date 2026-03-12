# FolderStack

FolderStack继承于[Stack](Stack.md)(层叠布局)控件，新增了[折叠屏悬停](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-folded-hover)能力，通过在FolderStack的配置项[FolderStackOptions](#ZH-CN_TOPIC_0000002497604958__folderstackoptions18对象说明)的upperItems数组上设置子组件id，使相应子组件自动避让折叠屏折痕区后移到上半屏。

该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件的悬停态能力针对[双折叠](https://developer.huawei.com/consumer/cn/doc/design-guides/foldable-0000002352875141)设计，只在双折叠设备生效。

当该组件的父组件为[if/else条件渲染节点](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse)时，折叠屏悬停能力将会失效。

#### 子组件

可以包含多个子组件。

#### 接口

FolderStack(options?: FolderStackOptions)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明options[FolderStackOptions](#ZH-CN_TOPIC_0000002497604958__folderstackoptions18对象说明)否FolderStack的配置项。

#### FolderStackOptions18+对象说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明upperItems11+Array<string>否是

定义悬停态会被移到上半屏的子组件的id数组。

当悬停触发时，upperItems数组中的子组件自动避让折叠屏折痕区后移到上半屏，其它组件堆叠在下半屏区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### 属性

设置offset和margin属性，可能会导致上下半屏遮挡折痕区，不建议开发者使用。

除支持[通用属性](通用属性.md)外，还支持以下属性：

#### alignContent

alignContent(value: Alignment)

设置子组件在容器内的对齐方式。该属性与[align](位置设置.md#ZH-CN_TOPIC_0000002529284821__align)同时设置时，后设置的属性生效。

从API version 12开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明value[Alignment](枚举说明.md#ZH-CN_TOPIC_0000002529284967__alignment)是

子组件在容器内的对齐方式。

默认值：Alignment.Center

非法值：按默认值处理。

#### enableAnimation

enableAnimation(value: boolean)

设置是否使用默认动效。

从API version 12开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明valueboolean是

是否使用默认动效。

默认值：true，设置true表示使用默认动效，设置false表示不使用默认动效。

非法值：按默认值处理。

#### autoHalfFold

autoHalfFold(value: boolean)

设置是否开启自动旋转，仅在系统自动旋转关闭时该属性生效。

从API version 12开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明valueboolean是

是否开启自动旋转。

默认值：true，设置true表示FolderStack在[半折叠状态](枚举说明.md#ZH-CN_TOPIC_0000002529284967__foldstatus11)进行布局时开启自动旋转，设置false表示关闭自动旋转。该属性不区分设备类型。

非法值：按默认值处理。

#### 事件

除支持[通用事件](通用事件.md)外，还支持以下事件：

#### onFolderStateChange

onFolderStateChange(callback: OnFoldStatusChangeCallback)

当前设备的折叠状态改变时触发回调，仅在横屏状态下生效。

从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明callback[OnFoldStatusChangeCallback](#ZH-CN_TOPIC_0000002497604958__onfoldstatuschangecallback18)是当前设备的折叠状态改变时触发的回调。

#### onHoverStatusChange12+

onHoverStatusChange(handler: OnHoverStatusChangeCallback)

当前设备的悬停状态改变时触发回调。

从API version 20开始，该接口支持在[attributeModifier](动态属性设置.md#ZH-CN_TOPIC_0000002529284843__attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明handler[OnHoverStatusChangeCallback](#ZH-CN_TOPIC_0000002497604958__onhoverstatuschangecallback18)是当前设备的悬停状态改变时触发的回调。

#### OnHoverStatusChangeCallback18+

type OnHoverStatusChangeCallback = (param: HoverEventParam) => void

当前设备的悬停状态改变时触发的回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明param[HoverEventParam](#ZH-CN_TOPIC_0000002497604958__hovereventparam12对象说明)是当前设备与悬停状态相关的参数，包括设备的折叠状态、悬停状态、应用方向以及窗口模式枚举。

#### OnFoldStatusChangeCallback18+

type OnFoldStatusChangeCallback = (event: OnFoldStatusChangeInfo) => void

当前设备的折叠状态。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

参数名类型必填说明event[OnFoldStatusChangeInfo](#ZH-CN_TOPIC_0000002497604958__onfoldstatuschangeinfo18)是当前设备的折叠状态。

#### OnFoldStatusChangeInfo18+

当折叠状态改变的时候回调，仅在横屏状态下生效。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明foldStatus11+[FoldStatus](枚举说明.md#ZH-CN_TOPIC_0000002529284967__foldstatus11)否否

当前设备的折叠状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### HoverEventParam12+对象说明

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

名称类型只读可选说明foldStatus[FoldStatus](枚举说明.md#ZH-CN_TOPIC_0000002529284967__foldstatus11)否否当前设备的折叠状态。isHoverModeboolean否否当前是否为悬停态。设置为true时表示当前为悬停态，设置为false时表示当前为非悬停态。appRotation[AppRotation](枚举说明.md#ZH-CN_TOPIC_0000002529284967__approtation12)否否当前应用方向。windowStatusType[WindowStatusType](#ZH-CN_TOPIC_0000002497604958__windowstatustype12)否否窗口模式枚举。

#### WindowStatusType12+

type WindowStatusType = WindowStatusType

窗口模式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

类型说明[WindowStatusType](Enums.md#ZH-CN_TOPIC_0000002529444769__windowstatustype11)窗口模式枚举。

#### 示例

#### 示例1（FolderStack折叠屏悬停能力）

该示例实现了折叠屏悬停能力。

```ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      // upperItems将所需要的悬停到上半屏的id放入upperItems传入，其余组件会堆叠在下半屏区域
      FolderStack({ upperItems: ["upperitemsId"] }) {
        // 此Column会自动上移到上半屏
        Column() {
          Text("video zone").height("100%").width("100%").textAlign(TextAlign.Center).fontSize(25)
        }.backgroundColor('rgb(0, 74, 175)').width("100%").height("100%").id("upperitemsId")

        // 下列两个Column堆叠在下半屏区域
        Column() {
          Text("video title")
            .width("100%")
            .height(50)
            .textAlign(TextAlign.Center)
            .backgroundColor('rgb(213, 213, 213)')
            .fontSize(25)
        }.width("100%").height("100%").justifyContent(FlexAlign.Start)

        Column() {
          Text("video bar ")
            .width("100%")
            .height(50)
            .textAlign(TextAlign.Center)
            .backgroundColor('rgb(213, 213, 213)')
            .fontSize(25)
        }.width("100%").height("100%").justifyContent(FlexAlign.End)
      }
      .backgroundColor('rgb(39, 135, 217)')
      // 是否启动动效
      .enableAnimation(true)
      // 是否自动旋转
      .autoHalfFold(true)
      // folderStack回调 当折叠状态改变时回调
      .onFolderStateChange((msg) => {
        if (msg.foldStatus === FoldStatus.FOLD_STATUS_EXPANDED) {
          console.info("The device is currently in the expanded state")
        } else if (msg.foldStatus === FoldStatus.FOLD_STATUS_HALF_FOLDED) {
          console.info("The device is currently in the half folded state")
        } else {
          // .............
        }
      })
      // hoverStatusChange回调 当悬停状态改变时回调
      .onHoverStatusChange((msg) => {
        console.info('this foldStatus:' + msg.foldStatus);
        console.info('this isHoverMode:' + msg.isHoverMode);
        console.info('this appRotation:' + msg.appRotation);
        console.info('this windowStatusType:' + msg.windowStatusType);
      })
      // folderStack如果不撑满页面全屏，作为普通Stack使用
      .alignContent(Alignment.Bottom)
      .height("100%")
      .width("100%")
      .backgroundColor('rgb(39, 135, 217)')

    }
    .height("100%")
    .width("100%")
    .borderWidth(1)
    .borderColor('rgb(213, 213, 213)')
    .backgroundColor('rgb(0, 74, 175)')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
  }
}
```

**图1** 横屏展开

**图2** 横屏半折叠

#### 示例2（使用attributeModifier动态设置FolderStack组件的属性及方法）

该示例展示了如何使用attributeModifier动态设置FolderStack组件的onFolderStateChange和onHoverStatusChange方法。

```ets
// xxx.ets
class MyFolderStackModifier implements AttributeModifier<FolderStackAttribute> {
  applyNormalAttribute(instance: FolderStackAttribute): void {
    // folderStack回调 当折叠状态改变时回调
    instance.onFolderStateChange((msg) => {
      if (msg.foldStatus === FoldStatus.FOLD_STATUS_EXPANDED) {
        console.info("The device is currently in the expanded state")
      } else if (msg.foldStatus === FoldStatus.FOLD_STATUS_HALF_FOLDED) {
        console.info("The device is currently in the half folded state")
      } else if (msg.foldStatus === FoldStatus.FOLD_STATUS_FOLDED) {
        console.info("The device is currently in the folded state")
      } else {
        // .............
      }
    })
    // hoverStatusChange回调 当悬停状态改变时回调
    instance.onHoverStatusChange((msg) => {
      console.info('this foldStatus:' + msg.foldStatus);
      console.info('this isHoverMode:' + msg.isHoverMode);
      console.info('this appRotation:' + msg.appRotation);
      console.info('this windowStatusType:' + msg.windowStatusType);
    })
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyFolderStackModifier = new MyFolderStackModifier()

  build() {
    Column() {
      // upperItems将所需要的悬停到上半屏的id放入upperItems传入，其余组件会堆叠在下半屏区域
      FolderStack({ upperItems: ["upperitemsId"] }) {
        // 此Column会自动上移到上半屏
        Column() {
          Text("video zone").height("100%").width("100%").textAlign(TextAlign.Center).fontSize(25)
        }.backgroundColor('rgb(0, 74, 175)').width("100%").height("100%").id("upperitemsId")

        // 下列两个Column堆叠在下半屏区域
        Column() {
          Text("video title")
            .width("100%")
            .height(50)
            .textAlign(TextAlign.Center)
            .backgroundColor('rgb(213, 213, 213)')
            .fontSize(25)
        }.width("100%").height("100%").justifyContent(FlexAlign.Start)

        Column() {
          Text("video bar ")
            .width("100%")
            .height(50)
            .textAlign(TextAlign.Center)
            .backgroundColor('rgb(213, 213, 213)')
            .fontSize(25)
        }.width("100%").height("100%").justifyContent(FlexAlign.End)
      }
      .backgroundColor('rgb(39, 135, 217)')
      // 是否启动动效
      .enableAnimation(true)
      // 是否自动旋转
      .autoHalfFold(true)
      .attributeModifier(this.modifier)
      // folderStack如果不撑满页面全屏，作为普通Stack使用
      .alignContent(Alignment.Bottom)
      .height("100%")
      .width("100%")
      .backgroundColor('rgb(39, 135, 217)')
    }
    .height("100%")
    .width("100%")
    .borderWidth(1)
    .borderColor('rgb(213, 213, 213)')
    .backgroundColor('rgb(0, 74, 175)')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
  }
}
```

**图1** 横屏展开

预期日志：

The device is currently in the expanded state

this foldStatus:1

this isHoverMode:0

this appRotation:3

this windowStatusType:1

**图2** 横屏半折叠

预期日志：

The device is currently in the half folded state

this foldStatus:3

this isHoverMode:1

this appRotation:3

this windowStatusType:1