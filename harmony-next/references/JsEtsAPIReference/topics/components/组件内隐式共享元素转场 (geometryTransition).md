# 组件内隐式共享元素转场 (geometryTransition)

在视图切换过程中提供丝滑的上下文传承过渡。通用transition机制提供了opacity、scale等转场效果，geometryTransition通过安排绑定的in/out组件（in指新视图、out指旧视图）的frame、position使得原本独立的transition动画在空间位置上发生联系，将视觉焦点由旧视图位置引导到新视图位置。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 7开始支持，从API version 10开始生效。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

[geometryTransition](组件内隐式共享元素转场 (geometryTransition).md)必须配合[animateTo](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__animateto)使用才有动画效果，动效时长、曲线跟随[animateTo](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__animateto)中的配置，不支持[animation](属性动画 (animation).md)动画。

**geometryTransition**

geometryTransition(id: string): T

组件内隐式共享元素转场。

系统能力： SystemCapability.ArkUI.ArkUI.Full

元服务API： 从API version 11开始，该接口支持在元服务中使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 用于设置绑定关系，id置空字符串清除绑定关系避免参与共享行为，id可更换重新建立绑定关系。同一个id只能有两个组件绑定且是in/out不同类型角色，不能多个组件绑定同一个id。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

**geometryTransition11+**

geometryTransition(id: string, options?: GeometryTransitionOptions): T

组件内隐式共享元素转场。

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 用于设置绑定关系，id置空字符串清除绑定关系避免参与共享行为，id可更换重新建立绑定关系。同一个id只能有两个组件绑定且是in/out不同类型角色，不能多个组件绑定同一个id。 |
| options | GeometryTransitionOptions | 否 | 组件内共享元素转场动画参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

**GeometryTransitionOptions11+**

系统能力： SystemCapability.ArkUI.ArkUI.Full

元服务API： 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| follow | boolean | 否 | 是 | 仅用于if范式下标记始终在组件树上的组件是否跟随做共享动画。true代表跟随做共享动画，false代表不跟随做共享动画。 默认值：false |

**示例**

```ets
// xxx.ets
@Entry
@Component
struct Index {
  @State isShow: boolean = false;

  build() {
    Stack({ alignContent: Alignment.Center }) {
      if (this.isShow) {
        // 图片使用Resource资源，需用户自定义
        Image($r('app.media.pic'))
          .autoResize(false)
          .clip(true)
          .width(300)
          .height(400)
          .offset({ y: 100 })
          .geometryTransition("picture", { follow: false })
          .transition(TransitionEffect.OPACITY)
      } else {
        // geometryTransition此处绑定的是容器，那么容器内的子组件需设为相对布局跟随父容器变化，
        // 套多层容器为了说明相对布局约束传递
        Column() {
            // 图片使用Resource资源，需用户自定义
            Image($r('app.media.icon'))
              .width('100%').height('100%')
          }.width('100%').height('100%')
        }
        .width(80)
        .height(80)
        // geometryTransition会同步圆角，但仅限于geometryTransition绑定处，此处绑定的是容器
        // 则对容器本身有圆角同步而不会操作容器内部子组件的borderRadius
        .borderRadius(20)
        .clip(true)
        .geometryTransition("picture")
        // transition保证组件离场不被立即析构，可设置其他转场效果
        .transition(TransitionEffect.OPACITY)
      }
    .onClick(() => {
      this.getUIContext().animateTo({ duration: 1000 }, () => {
        this.isShow = !this.isShow;
      });
    })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522085298.webp)