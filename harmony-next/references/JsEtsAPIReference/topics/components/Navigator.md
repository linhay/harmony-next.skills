# Navigator

路由容器组件，提供路由跳转能力。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 13开始，该组件不再维护，建议使用[Navigation](Navigation.md)组件进行页面路由。

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**子组件**

可以包含子组件。

**接口**

**Navigator(deprecated)**

Navigator(value?: {target: string, type?: NavigationType})

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 7开始支持，从API version 13开始废弃，建议使用[NavPathInfo](Navigation.md#ZH-CN_TOPIC_0000002553360755__navpathinfo10)替代。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 指定跳转目标页面的路径。 |
| type | NavigationType | 否 | 指定路由方式。 默认值：NavigationType.Push |

**Navigator(deprecated)**

Navigator()

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 7开始支持，从API version 13开始废弃，建议使用[NavigationAttribute](Navigation.md#ZH-CN_TOPIC_0000002553360755__属性)替代。NavigationAttribute为Navigation组件的属性。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

**NavigationType(deprecated)枚举说明**

路由的跳转方式。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Push | 1 | 跳转到应用内的指定页面。 说明： 从API version 7开始支持，从API version 13开始废弃，建议使用pushPath替代。 |
| Replace | 2 | 用应用内的某个页面替换当前页面，并销毁被替换的页面。 说明： 从API version 7开始支持，从API version 13开始废弃，建议使用replacePath替代。 |
| Back | 3 | 返回到指定的页面。指定的页面不存在栈中时不响应。未传入指定的页面时返回上一页。 说明： 从API version 7开始支持，从API version 13开始废弃，建议使用pop替代。 |

**属性**

**active(deprecated)**

active(value: boolean)

设置当前路由组件是否处于激活状态，处于激活状态时，会生效相应的路由操作。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 7开始支持，从API version 13开始废弃，建议使用[Navigation](Navigation.md)替代。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 路由组件是否处于激活状态。设置为true时，组件处于激活态。设置为false时，组件不处于激活态。 |

**params(deprecated)**

params(value: object)

设置跳转时传递到目标页面的数据。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 7开始支持，从API version 13开始废弃，建议使用[param](Navigation.md#ZH-CN_TOPIC_0000002553360755__属性-1)替代。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | object | 是 | 跳转时要同时传递到目标页面的数据，可在目标页面使用router.getParams()获得。 |

**target(deprecated)**

target(value: string)

设置跳转目标页面的路径。目标页面需加入main_pages.json文件中。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 7开始支持，从API version 13开始废弃，建议使用[Navigation](Navigation.md)替代。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 跳转目标页面的路径。 |

**type(deprecated)**

type(value: NavigationType)

设置路由跳转方式。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 7开始支持，从API version 13开始废弃，建议使用[Navigation](Navigation.md)替代。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | NavigationType | 是 | 路由跳转方式。 默认值：NavigationType.Push |

**示例**

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

interface NameObject {
  name: string;
}

class TextObject {
  text: NameObject;

  constructor(text: NameObject) {
    this.text = text;
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
```

![image](public_sys-resources/zh-cn_image_0000002522245428.webp)