# Navigator

路由容器组件，提供路由跳转能力。

从API version 13开始，该组件不再维护，推荐使用组件[Navigation](Navigation.md)进行页面路由。

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

可以包含子组件。

#### 接口

#### Navigator

Navigator(value?: {target: string, type?: NavigationType})

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明targetstring是指定跳转目标页面的路径。type[NavigationType](#ZH-CN_TOPIC_0000002497604978__navigationtype枚举说明)否

指定路由方式。

默认值：NavigationType.Push

#### Navigator

Navigator()

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### NavigationType枚举说明

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明Push1跳转到应用内的指定页面。Replace2用应用内的某个页面替换当前页面，并销毁被替换的页面。Back3返回到指定的页面。指定的页面不存在栈中时不响应。未传入指定的页面时返回上一页。

#### 属性

#### active

active(value: boolean)

设置当前路由组件是否处于激活状态，处于激活状态时，会生效相应的路由操作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是路由组件是否处于激活状态。设置为true时，组件处于激活态。设置为false时，组件不处于激活态。

#### params

params(value: object)

设置跳转时传递到目标页面的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueobject是跳转时要同时传递到目标页面的数据，可在目标页面使用[router.getParams()](@ohos.router (页面路由)(不推荐).md#ZH-CN_TOPIC_0000002529444757__routergetparamsdeprecated)获得。

#### target

target(value: string)

设置跳转目标页面的路径。目标页面需加入main_pages.json文件中。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuestring是跳转目标页面的路径。

#### type

type(value: NavigationType)

设置路由跳转方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[NavigationType](#ZH-CN_TOPIC_0000002497604978__navigationtype枚举说明)是

路由跳转方式。

默认值：NavigationType.Push

#### 示例

```ets
// Navigator.ets
@Entry
@Component
struct NavigatorExample {
  @State active: boolean = false
  @State name: NameObject = { name: 'news' }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
      Navigator({ target: 'pages/container/navigator/Detail', type: NavigationType.Push }) {
        Text('Go to ' + this.name.name + ' page')
          .width('100%').textAlign(TextAlign.Center)
      }.params(new TextObject(this.name)) // 传参数到Detail页面

      Navigator() {
        Text('Back to previous page').width('100%').textAlign(TextAlign.Center)
      }.active(this.active)
      .onClick(() => {
        this.active = true
      })
    }.height(150).width(350).padding(35)
  }
}

interface NameObject {
  name: string;
}

class TextObject {
  text: NameObject;

  constructor(text: NameObject) {
    this.text = text;
  }
}
```

```ets
// Detail.ets
@Entry
@Component
struct DetailExample {
  // 接收Navigator.ets的传参
  params: Record<string, NameObject> = this.getUIContext().getRouter().getParams() as Record<string, NameObject>
  @State name: NameObject = this.params.text

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
      Navigator({ target: 'pages/container/navigator/Back', type: NavigationType.Push }) {
        Text('Go to back page').width('100%').height(20)
      }

      Text('This is ' + this.name.name + ' page')
        .width('100%').textAlign(TextAlign.Center)
    }
    .width('100%').height(200).padding({ left: 35, right: 35, top: 35 })
  }
}

interface NameObject {
  name: string;
}
```

```ets
// Back.ets
@Entry
@Component
struct BackExample {
  build() {
    Column() {
      Navigator({ target: 'pages/container/navigator/Navigator', type: NavigationType.Back }) {
        Text('Return to Navigator Page').width('100%').textAlign(TextAlign.Center)
      }
    }.width('100%').height(200).padding({ left: 35, right: 35, top: 35 })
  }
}
```