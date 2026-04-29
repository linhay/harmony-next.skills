# 共享元素转场 (sharedTransition)

可以通过设置组件的sharedTransition属性将该元素标记为共享元素并设置对应的共享元素转场动效。sharedTransition仅发生在[页面路由（router）](@ohos.router (页面路由)(不推荐).md)跳转时。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**sharedTransition**

sharedTransition(id: string, options?: sharedTransitionOptions): T

设置共享元素转场动效。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 两个页面中id值相同且不为空字符串的组件即为共享元素，在页面转场时可显示共享元素转场动效。 |
| options | sharedTransitionOptions | 否 | 共享元素转场动画参数。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

**sharedTransitionOptions**

共享元素转场动画参数。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

type为SharedTransitionEffectType.Exchange时motionPath才会生效。

type为SharedTransitionEffectType.Exchange时，效果为对匹配的共享元素产生位置、大小的过渡（可通过配置组件的border观察），不支持内容的过渡效果。例如，Text组件在两个页面上使用不同的fontSize属性值，即绘制内容有大小差异，在sharedTransition动画结束后的最后一帧，Text的fontSize效果会突变为跳转目标页fontSize的效果。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 是 | 描述共享元素转场动效播放时长。 默认值：1000  单位：毫秒 取值范围：[0, +∞) |
| curve | Curve | string | ICurve | 否 | 是 | 动画曲线。 推荐以Curve或ICurve形式指定。 当类型为string时，为动画插值曲线，取值参考AnimateParam的curve参数。 默认值：Curve.Linear |
| delay | number | 否 | 是 | 延迟播放时间。 默认值：0  单位：毫秒 |
| motionPath | MotionPathOptions | 否 | 是 | 运动路径信息。 |
| zIndex | number | 否 | 是 | 设置Z轴。 取值范围：(-∞, +∞) 默认值：0 |
| type | SharedTransitionEffectType | 否 | 是 | 动画类型。 默认值：SharedTransitionEffectType.Exchange |

**示例**

 示例代码为点击图片跳转页面时，显示共享元素图片的自定义转场动效。

```ets
// xxx.ets
@Entry
@Component
struct SharedTransitionExample {

  build() {
    Column() {
      // $r('app.media.ic_health_heart')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.ic_health_heart')).width(50).height(50).margin({ left: 20, top: 20 })
        .sharedTransition('sharedImage', { duration: 800, curve: Curve.Linear, delay: 100 })
    }.width('100%').height('100%').alignItems(HorizontalAlign.Start)
    .onClick(() => {
      this.getUIContext().getRouter().pushUrl({ url: 'pages/PageB' })
    })
  }

  pageTransition() {
    PageTransitionEnter({ type: RouteType.None, duration: 0 })
    PageTransitionExit({ type: RouteType.None, duration: 0 })
  }
```

```ets
// PageB.ets
@Entry
@Component
struct PageBExample {
  build() {
    Stack() {
      // $r('app.media.ic_health_heart')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.ic_health_heart')).width(150).height(150)
        .sharedTransition('sharedImage', { duration: 800, curve: Curve.Linear, delay: 100 })
    }.width('100%').height('100%')
  }

  pageTransition() {
    PageTransitionEnter({ type: RouteType.None, duration: 0 })
    PageTransitionExit({ type: RouteType.None, duration: 0 })
  }
```

![image](public_sys-resources/zh-cn_image_0000002553205253.webp)