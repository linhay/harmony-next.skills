# @ohos.arkui.componentSnapshot (组件截图)

本模块提供获取组件截图的能力，包括已加载的组件的截图和没有加载的组件的截图。组件截图只能够截取组件大小的区域，如果组件的绘制超出了它的区域，或子组件的绘制超出了父组件的区域，这些在组件区域外绘制的内容不会在截图中呈现。兄弟节点堆叠在组件区域内，截图不会显示兄弟组件。

缩放、平移、旋转等图形变换属性只对被截图组件的子组件生效；对目标组件本身应用图形变换属性不生效，显示的仍然是图形变换前的效果。

组件截图典型使用场景（如长截图）及最佳实践请参考[使用组件截图](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-component-snapshot)。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

对于使用[XComponent]([XComponent](../../topics/components/XComponent.md).md)的场景，例如：Video或者相机流媒体展示类组件，不建议使用组件截图相关接口，建议使用[createPixelMapFromSurface](Functions.md#ZH-CN_TOPIC_0000002522241966__imagecreatepixelmapfrom[surface](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445805__imagecreatepixelmapfromsurface11)11)直接获取图片。

-

如果组件自身内容不能填满组件大小区域，那么剩余位置截图返回的内容为透明像素。如果组件使用了[图像效果]([图像效果](../../topics/components/图像效果.md).md)类属性或其他的效果类属性，则可能产生非用户预期的截图结果。请排查是否需要填充组件透明内容区域，或使用[窗口截图](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__snapshot9)替代。

-

示例效果请以真机运行为准，当前 DevEco Studio预览器不支持。

#### 导入模块

```ets
import { componentSnapshot } from '@kit.ArkUI';
```

#### componentSnapshot.get(deprecated)

get(id: string, callback: AsyncCallback<image.PixelMap>, options?: SnapshotOptions): void

获取已加载的组件的截图，传入组件的[组件标识](组件标识.md)，找到对应组件进行截图。通过回调返回结果。


-

从API version 10开始支持，从API version 18开始废弃，建议使用[get](Class (ComponentSnapshot).md#ZH-CN_TOPIC_0000002522080724__get12)替代。get需先通过[UIContext](Class (UIContext).md)中的[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)方法获取[ComponentSnapshot](Class (ComponentSnapshot).md)对象，然后通过该对象进行调用。

-

从API version 12开始，可以通过使用[UIContext](Class (UIContext).md)中的[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)方法获取当前UI上下文关联的[ComponentSnapshot](Class (ComponentSnapshot).md)对象。

-

截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 目标组件的[组件标识](../../topics/components/组件标识.md)。 |
| callback | AsyncCallback<image.PixelMap> | 是 | 截图返回结果的回调。 |
| options12+ | SnapshotOptions | 否 | 截图相关的自定义参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[接口调用异常错误码](接口调用异常错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Invalid ID. |


直接使用componentSnapshot可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](Class (UIContext).md)实例，并使用[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)获取绑定实例的componentSnapshot。

**示例：**

```ets
import { componentSnapshot } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct SnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  build() {
    Column() {
      Row() {
        Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
        // $r('app.media.img')需要替换为开发者所需的图像资源文件
        Image($r('app.media.img'))
          .autoResize(true)
          .width(200)
          .height(200)
          .margin(5)
          .id("root")
      }

      Button("click to generate UI snapshot")
        .onClick(() => {
          // 建议使用this.getUIContext().getComponentSnapshot().get()
          componentSnapshot.get("root", (error: Error, pixmap: image.PixelMap) => {
            if (error) {
              console.error(`error:${JSON.stringify(error)}`)
              return;
            }
            this.pixmap = pixmap
          }, { scale: 2, waitUntilRenderFinished: true })
        }).margin(10)
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
  }
```

#### componentSnapshot.get(deprecated)

get(id: string, options?: SnapshotOptions): Promise<image.PixelMap>

获取已加载的组件的截图，传入组件的[组件标识](组件标识.md)，找到对应组件进行截图。通过Promise返回结果。


-

从API version 10开始支持，从API version 18开始废弃，建议使用[get](Class (ComponentSnapshot).md#ZH-CN_TOPIC_0000002522080724__get12-1)替代。get需先通过[UIContext](Class (UIContext).md)中的[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)方法获取[ComponentSnapshot](Class (ComponentSnapshot).md)对象，然后通过该对象进行调用。

-

从API version 12开始，可以通过使用[UIContext](Class (UIContext).md)中的[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)方法获取当前UI上下文关联的[ComponentSnapshot](Class (ComponentSnapshot).md)对象。

-

截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 目标组件的[组件标识](../../topics/components/组件标识.md)。 |
| options12+ | SnapshotOptions | 否 | 截图相关的自定义参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<image.PixelMap> | 截图返回的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Invalid ID. |


直接使用componentSnapshot可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](Class (UIContext).md)实例，并使用[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)获取绑定实例的componentSnapshot。

**示例：**

```ets
import { componentSnapshot } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct SnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  build() {
    Column() {
      Row() {
        Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
        // $r('app.media.img')需要替换为开发者所需的图像资源文件
        Image($r('app.media.img'))
          .autoResize(true)
          .width(200)
          .height(200)
          .margin(5)
          .id("root")
      }

      Button("click to generate UI snapshot")
        .onClick(() => {
          // 建议使用this.getUIContext().getComponentSnapshot().get()
          componentSnapshot.get("root", { scale: 2, waitUntilRenderFinished: true })
            .then((pixmap: image.PixelMap) => {
              this.pixmap = pixmap
            }).catch((err: Error) => {
            console.error(`error:${err}`)
          })
        }).margin(10)
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
  }
```

#### componentSnapshot.createFromBuilder(deprecated)

createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>, delay?: number, check[Image](../../types/interfaces/Image.md)Status?: boolean, options?: SnapshotOptions): void

在应用后台渲染[CustomBuilder](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)自定义组件，并输出其截图。通过回调返回结果并支持在回调中获取离屏组件绘制区域坐标和大小。


-

从API version 10开始支持，从API version 18开始废弃，建议使用[createFromBuilder](Class (ComponentSnapshot).md#ZH-CN_TOPIC_0000002522080724__createfrombuilder12)替代。createFromBuilder需先通过[UIContext](Class (UIContext).md)中的[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)方法获取[ComponentSnapshot](Class (ComponentSnapshot).md)对象，然后通过该对象进行调用。

-

从API version 12开始，可以通过使用[UIContext](Class (UIContext).md)中的[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)方法获取当前UI上下文关联的[ComponentSnapshot](Class (ComponentSnapshot).md)对象。

-

由于需要等待组件构建、渲染成功，离屏截图的回调有500ms以内的延迟。

-

builder中的组件不支持设置动画相关的属性，如[transition](组件内转场 (transition).md)。

-

部分执行耗时任务的组件可能无法及时在截图前加载完成，因此会截取不到加载成功后的图像。例如：加载网络图片的[Image](Image.md)组件、[Web](组件描述.md)组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | 是 | 自定义组件构建函数。 说明： 不支持全局builder。 builder的根组件宽高为0时，截图操作会失败并抛出100001错误码。 |
| callback | AsyncCallback<image.PixelMap> | 是 | 截图返回结果的回调。支持在回调中获取离屏组件绘制区域坐标和大小。 |
| delay12+ | number | 否 | 指定触发截图指令的延迟时间。当布局中使用了图片组件时，需要指定延迟时间，以便系统解码图片资源。资源越大，解码需要的时间越长，建议尽量使用不需要解码的PixelMap资源。 当使用PixelMap资源或对[Image](../../types/interfaces/Image.md)组件设置syncLoad为true时，可以配置delay为0，强制不等待触发截图。该延迟时间并非指接口从调用到返回的时间，由于系统需要对传入的builder进行临时离屏构建，因此返回的时间通常要比该延迟时间长。 说明： 截图接口传入的builder中，不应使用状态变量控制子组件的构建，如果必须要使用，在调用截图接口时，也不应再有变化，以避免出现截图不符合预期的情况。 默认值：300 单位：毫秒 取值范围：[0, +∞)，小于0时按默认值处理。 |
| check[Image](../../types/interfaces/Image.md)Status12+ | boolean | 否 | 指定是否允许在截图之前，校验图片解码状态。如果为true，则会在截图之前检查所有Image组件是否已经解码完成。为false，则不会校验图片解码状态。如果没有完成检查，则会放弃截图并返回异常。 默认值：false |
| options12+ | SnapshotOptions | 否 | 截图相关的自定义参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[截图错误码](截图错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The builder is not a valid build function. |
| 160001 | An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the check[Image](../../types/interfaces/Image.md)Status option is enabled. |


直接使用componentSnapshot可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](Class (UIContext).md)实例，并使用[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)获取绑定实例的componentSnapshot。

**示例：**

```ets
import { componentSnapshot } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct OffscreenSnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  @Builder
  RandomBuilder() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text('Test menu item 1')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
      Divider().height(10)
      Text('Test menu item 2')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
    }
    .width(100)
    .id("builder")
  }

  build() {
    Column() {
      Button("click to generate offscreen UI snapshot")
        .onClick(() => {
          // 建议使用this.getUIContext().getComponentSnapshot().createFromBuilder()
          componentSnapshot.createFromBuilder(() => {
            this.RandomBuilder()
          },
            (error: Error, pixmap: image.PixelMap) => {
              if (error) {
                console.error(`error:${JSON.stringify(error)}`)
                return;
              }
              this.pixmap = pixmap
              // 保存pixmap到文件中
              // ....
              // 获取组件大小和位置
              let info = this.getUIContext().getComponentUtils().getRectangleById("builder")
              console.info(info.size.width + ' ' + info.size.height + ' ' + info.localOffset.x + ' ' +
              info.localOffset.y + ' ' + info.windowOffset.x + ' ' + info.windowOffset.y)
            }, 320, true, { scale: 2, waitUntilRenderFinished: true })
        })
      Image(this.pixmap)
        .margin(10)
        .height(200)
        .width(200)
        .border({ color: Color.Black, width: 2 })
    }.width('100%').margin({ left: 10, top: 5, bottom: 5 }).height(300)
  }
```

#### componentSnapshot.createFromBuilder(deprecated)

createFromBuilder(builder: CustomBuilder, delay?: number, check[Image](../../types/interfaces/Image.md)Status?: boolean, options?: SnapshotOptions): Promise<image.PixelMap>

在应用后台渲染[CustomBuilder](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8)自定义组件，并输出其截图。通过Promise返回结果，支持获取离屏组件绘制区域的坐标和大小。


-

从API version 10开始支持，从API version 18开始废弃，建议使用[createFromBuilder](Class (ComponentSnapshot).md#ZH-CN_TOPIC_0000002522080724__createfrombuilder12-1)替代。createFromBuilder需先通过[UIContext](Class (UIContext).md)中的[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)方法获取[ComponentSnapshot](Class (ComponentSnapshot).md)对象，然后通过该对象进行调用。

-

从API version 12开始，可以通过使用[UIContext](Class (UIContext).md)中的[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)方法获取当前UI上下文关联的[ComponentSnapshot](Class (ComponentSnapshot).md)对象。

-

由于需要等待组件构建、渲染成功，离屏截图的回调有500ms以内的延迟。

-

builder中的组件不支持设置动画相关的属性，如[transition](组件内转场 (transition).md)。

-

部分执行耗时任务的组件可能无法及时在截图前加载完成，因此会截取不到加载成功后的图像。例如：加载网络图片的[Image](Image.md)组件、[Web](组件描述.md)组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | 是 | 自定义组件构建函数。 说明： 不支持全局builder。 builder的根组件宽高为0时，截图操作会失败并抛出100001错误码。 |
| delay12+ | number | 否 | 指定触发截图指令的延迟时间。当布局中使用了图片组件时，需要指定延迟时间，以便系统解码图片资源。资源越大，解码需要的时间越长，建议尽量使用不需要解码的PixelMap资源。 当使用PixelMap资源或对[Image](../../types/interfaces/Image.md)组件设置syncLoad为true时，可以配置delay为0，强制不等待触发截图。该延迟时间并非指接口从调用到返回的时间，由于系统需要对传入的builder进行临时离屏构建，因此返回的时间通常要比该延迟时间长。 说明： 截图接口传入的builder中，不应使用状态变量控制子组件的构建，如果必须要使用，在调用截图接口时，也不应再有变化，以避免出现截图不符合预期的情况。 默认值：300 单位：毫秒 |
| check[Image](../../types/interfaces/Image.md)Status12+ | boolean | 否 | 指定是否允许在截图之前，校验图片解码状态。如果为true，则会在截图之前检查所有Image组件是否已经解码完成。为false，则不会校验图片解码状态。如果没有完成检查，则会放弃截图并返回异常。 默认值：false |
| options12+ | SnapshotOptions | 否 | 截图相关的自定义参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<image.PixelMap> | 截图返回的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[截图错误码](截图错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The builder is not a valid build function. |
| 160001 | An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the check[Image](../../types/interfaces/Image.md)Status option is enabled. |


直接使用componentSnapshot可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](Class (UIContext).md)实例，并使用[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)获取绑定实例的componentSnapshot。

**示例：**

```ets
import { componentSnapshot } from '@kit.ArkUI'
import { image } from '@kit.ImageKit'

@Entry
@Component
struct OffscreenSnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  @Builder
  RandomBuilder() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text('Test menu item 1')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
      Divider().height(10)
      Text('Test menu item 2')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
    }
    .width(100)
    .id("builder")
  }

  build() {
    Column() {
      Button("click to generate offscreen UI snapshot")
        .onClick(() => {
          // 建议使用this.getUIContext().getComponentSnapshot().createFromBuilder()
          componentSnapshot.createFromBuilder(() => {
            this.RandomBuilder()
          }, 320, true, { scale: 2, waitUntilRenderFinished: true })
            .then((pixmap: image.PixelMap) => {
              this.pixmap = pixmap
              // 保存pixmap到文件中
              // ....
              // 获取组件大小和位置
              let info = this.getUIContext().getComponentUtils().getRectangleById("builder")
              console.info(`${info.size.width} ${info.size.height} ${info.localOffset.x} ${
              info.localOffset.y} ${info.windowOffset.x} ${info.windowOffset.y}`)
            }).catch((err: Error) => {
            console.error(`error:${err}`)
        })
      Image(this.pixmap)
        .margin(10)
        .height(200)
        .width(200)
        .border({ color: Color.Black, width: 2 })
    }.width('100%').margin({ left: 10, top: 5, bottom: 5 }).height(300)
  }
```

#### componentSnapshot.getSync12+

getSync(id: string, options?: SnapshotOptions): image.PixelMap

获取已加载的组件的截图，传入组件的[组件标识](组件标识.md)，找到对应组件进行截图。同步等待截图完成返回[PixelMap](Interface (PixelMap).md)。


截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 目标组件的[组件标识](../../topics/components/组件标识.md)。 |
| options | SnapshotOptions | 否 | 截图相关的自定义参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| image.PixelMap | 截图返回的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)、[截图错误码](截图错误码.md)和[接口调用异常错误码](接口调用异常错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Invalid ID. |
| 160002 | Timeout. |
| 160003 | Unsupported color space or dynamic range mode in snapshot options. |


直接使用componentSnapshot可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题。建议使用getUIContext()获取[UIContext](Class (UIContext).md)实例，并使用[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)获取绑定实例的componentSnapshot。

**示例：**

```ets
import { componentSnapshot } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct SnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  build() {
    Column() {
      Row() {
        Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
        // $r('app.media.img')需要替换为开发者所需的图像资源文件
        Image($r('app.media.img'))
          .autoResize(true)
          .width(200)
          .height(200)
          .margin(5)
          .id("root")
      }

      Button("click to generate UI snapshot")
        .onClick(() => {
          try {
            // 建议使用this.getUIContext().getComponentSnapshot().getSync()
            let pixelmap = componentSnapshot.getSync("root", { scale: 2, waitUntilRenderFinished: true })
            this.pixmap = pixelmap
          } catch (error) {
            console.error(`getSync errorCode:${error.code} message:${error.message}`)
          }
        }).margin(10)
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
  }
```

![image](public_sys-resources/zh-cn_image_0000002522244670.webp)

#### SnapshotOptions12+

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scale | number | 否 | 是 | 指定截图时图形侧绘制pixelmap的缩放比例，比例过大时截图时间会变长，或者截图可能会失败。 取值范围：[0, +∞)，当小于等于0时按默认情况处理。 默认值：1 说明： 请不要截取过大尺寸的图片，截图不建议超过屏幕尺寸的大小。当要截取的图片目标长宽超过底层限制时，截图会返回失败，不同设备的底层限制不同。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| waitUntilRenderFinished | boolean | 否 | 是 | 设置是否强制系统在截图前等待所有绘制指令执行完毕。true表示强制系统在截图前等待所有绘制指令执行完毕，false表示不强制系统在截图前等待所有绘制指令执行完毕。该选项可尽可能确保截图内容是最新的状态，应尽量开启。需要注意的是，开启后接口可能需要更长的时间返回，具体的时间依赖页面当时时刻需要重绘区域的大小。 默认值：false 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| region15+ | SnapshotRegionType | 否 | 是 | 指定截图的矩形区域范围，默认为整个组件。 元服务API： 从API version 15开始，该接口支持在元服务中使用。 |
| colorMode23+ | ColorModeOptions | 否 | 是 | 指定截图使用的色彩空间。 默认值：{colorSpace: SRGB, isAuto: false} 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |
| dynamicRangeMode23+ | DynamicRangeModeOptions | 否 | 是 | 指定截图使用的动态范围模式。 默认值：{dynamicRangeMode: STANDARD, isAuto: false} 元服务API： 从API version 23开始，该接口支持在元服务中使用。 |

**ColorModeOptions23+**

定义截图时所使用的色彩空间。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colorSpace | colorSpaceManager.ColorSpace | 否 | 是 | 指定截图使用的色彩空间。 如果知道被截图组件使用的色彩空间，可以通过colorSpace字段指定，并将isAuto设置为false，以达到预期的截图效果。 取值范围：colorSpaceManager.ColorSpace中DISPLAY_P3、SRGB、DISPLAY_BT2020_SRGB。 默认值：SRGB 如果值为undefined、null或未设置，则使用默认值截图；其他异常值会导致截图失败，返回错误码160003。 |
| isAuto | boolean | 否 | 是 | 是否由系统自动决定所使用的色彩空间。 支持取值为：true表示系统自动决定所使用的色彩空间；false表示使用通过colorSpace字段设置的色彩空间类型进行截图。取非法值时，按默认值false处理。 默认值：false 离屏截图仅支持设置为false，否则会返回错误码160004。 当isAuto设置为true时，建议将SnapshotOptions中的waitUntilRenderFinished字段也设置为true，以便确保系统可以正常检测到所用的模式。 在不确定组件使用的色彩空间时，建议将isAuto设置为true，让系统根据实际情况自动决定使用的色彩空间。 当isAuto为true时，colorSpace字段设置的值会被忽略。此时，如果被截图组件同时包含不同色彩空间的子组件时，截图的色彩空间为优先级最高的色彩空间类型，优先级排序为DISPLAY_BT2020_SRGB > DISPLAY_P3 > SRGB。 |

示例：

```ets
import { image } from '@kit.ImageKit';
import { colorSpaceManager } from '@kit.ArkGraphics2D';

@Entry
@Component
struct SnapshotColorModeExample {
  @State pixmap: image.PixelMap | undefined = undefined;

  build() {
    Column() {
      Row() {
        Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
        // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
        Image($r('app.media.startIcon'))
          .autoResize(true)
          .width(200)
          .height(200)
          .margin(5)
          .id("root")
      }

      Button("click to generate UI snapshot")
        .onClick(() => {
          this.getUIContext().getComponentSnapshot().get("root", (error: Error, pixmap: image.PixelMap) => {
            if (error) {
              console.error(`error:${JSON.stringify(error)}`)
              return;
            }
            this.pixmap = pixmap
          }, {
            scale: 2,
            waitUntilRenderFinished: true,
            // 设置色彩空间为：DISPLAY_P3
            colorMode: { colorSpace: colorSpaceManager.ColorSpace.DISPLAY_P3, isAuto: false }
          })
        }).margin(10)
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
  }
```

**DynamicRangeModeOptions23+**

定义截图所使用的动态范围模式。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dynamicRangeMode | DynamicRangeMode | 否 | 是 | 指定截图使用的动态范围模式。 默认情况下，系统以STANDARD模式进行截图。如果知道被截图组件使用的动态范围模式，可通过dynamicRangeMode字段指定具体的动态范围模式，并将isAuto设置为false，以达到预期的截图效果。 虽然动态范围模式有三种，但是HIGH和CONSTRAINT的表现均为HDR（高动态范围）。STANDARD模式对应表现为SDR（标准动态范围）。 在指定了合法的动态范围模式之后，截图实际采用的动态范围会受到被截图组件和设置值的双重影响，具体如下： 1. 当被截图组件的动态范围为SDR时，即使指定动态范围模式为HIGH，截图实际采用的动态范围为SDR。 2. 当被截图组件的动态范围为HDR时，截图实际采用的动态范围为指定的动态范围模式。 3. 当配置色彩空间为SRGB或DISPLAY_P3时，截图实际采用的动态范围为SDR。 4. 如果被截图组件同时包含SDR和HDR两种动态范围的子组件时，则当作HDR处理。 5. 如果3和4的条件同时被满足，则截图实际采用的动态范围为SDR。 取值范围：DynamicRangeMode 枚举值。 默认值：STANDARD 如果值为undefined、null或未设置，则使用默认值截图；其他异常值会导致截图失败，返回错误码160003。 |
| isAuto | boolean | 否 | 是 | 是否由系统自动决定所使用的动态范围模式。 支持取值为：true表示系统自动决定所使用的动态范围模式；false表示使用通过dynamicRangeMode字段设置的动态范围类型进行截图。取非法值时，按默认值false处理。 默认值：false 离屏截图仅支持设置为false，否则会返回错误码160004。 当isAuto设置为true时，建议将SnapshotOptions中的waitUntilRenderFinished字段也设置为true，以便确保系统可以正常检测到所用的模式。 在不确定组件使用的动态范围模式时，建议将isAuto设置为true，让系统根据实际情况自动决定使用的动态范围模式。 当isAuto为true时，dynamicRangeMode字段设置的值会被忽略。 |

示例：

```ets
import { image } from '@kit.ImageKit';

@Entry
@Component
struct SnapshotDynamicRangeExample {
  @State pixmap: image.PixelMap | undefined = undefined;

  build() {
    Column() {
      Row() {
        Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
        // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
        Image($r('app.media.startIcon'))
          .autoResize(true)
          .width(200)
          .height(200)
          .margin(5)
          .id("root")
      }

      Button("click to generate UI snapshot")
        .onClick(() => {
          this.getUIContext().getComponentSnapshot().get("root", (error: Error, pixmap: image.PixelMap) => {
            if (error) {
              console.error(`error:${JSON.stringify(error)}`)
              return;
            }
            this.pixmap = pixmap
          }, {
            scale: 2,
            waitUntilRenderFinished: true,
            // 设置动态范围为自动模式
            dynamicRangeMode: { dynamicRangeMode: DynamicRangeMode.STANDARD, isAuto: true }
          })
        }).margin(10)
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
  }
```

#### SnapshotRegionType15+

type SnapshotRegionType = SnapshotRegion | LocalizedSnapshotRegion

表示组件截图区域，取值类型为下表中的任一类型。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| SnapshotRegion | 表示组件截图的矩形区域。 |
| LocalizedSnapshotRegion | 表示组件截图的矩形区域，根据布局方向确定是否对矩形区域水平翻转，若布局方向为RTL，则把指定的截图区域做左右翻转处理以适应RTL布局方向。 |

#### SnapshotRegion15+

定义组件截图的矩形区域。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 截图区域矩形左上角的x轴坐标。 单位：px 取值范围：[0, 组件宽度] |
| top | number | 否 | 否 | 截图区域矩形左上角的y轴坐标。 单位：px 取值范围：[0, 组件高度] |
| right | number | 否 | 否 | 截图区域矩形右下角的x轴坐标。 单位：px 取值范围：[0, 组件宽度] |
| bottom | number | 否 | 否 | 截图区域矩形右下角的y轴坐标。 单位：px 取值范围：[0, 组件高度] |

#### LocalizedSnapshotRegion15+

定义组件截图的矩形区域，start和end的值在布局方向为LTR时指定为left和right，在布局方向为RTL时指定为right和left。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 否 | 布局方向为LTR时表示截图区域矩形左上角的x轴坐标，布局方向为RTL时表示截图区域矩形右上角的x轴坐标。 单位：px 取值范围：[0, 组件宽度] |
| top | number | 否 | 否 | 布局方向为LTR时表示截图区域矩形左上角的y轴坐标，布局方向为RTL时表示截图区域矩形右上角的y轴坐标。 单位：px 取值范围：[0, 组件高度] |
| end | number | 否 | 否 | 布局方向为LTR时表示截图区域矩形右下角的x轴坐标，布局方向为RTL时表示截图区域矩形左下角的x轴坐标。 单位：px 取值范围：[0, 组件宽度] |
| bottom | number | 否 | 否 | 布局方向为LTR时表示截图区域矩形右下角的y轴坐标，布局方向为RTL时表示截图区域矩形左下角的y轴坐标。 单位：px 取值范围：[0, 组件高度] |


直接使用componentSnapshot可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](Class (UIContext).md)实例，并使用[getComponentSnapshot](Class (UIContext).md#ZH-CN_TOPIC_0000002522240732__getcomponentsnapshot12)获取绑定实例的componentSnapshot。

**示例：**

```ets
import { image } from '@kit.ImageKit';

@Entry
@Component
struct SnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  build() {
    Column() {
      Row() {
        Column() {
          TextClock()
          Button("Button ABCDE").type(ButtonType.Normal)
          Row() {
            Checkbox()
            Text("√")
            Text(" | ")
            Checkbox()
            Text("×")
          }.align(Alignment.Start)

          TextInput()
        }
        .align(Alignment.Start)
        .id("component1")
        .width("600px")
        .height("600px")
        .borderRadius(6)
        .borderWidth(2)
        .borderColor(Color.Green)

      }

      Button("get capture")
        .onClick(() => {
          try {
            let pixelmap = this.getUIContext().getComponentSnapshot().getSync("component1",
              {
                scale: 2,
                waitUntilRenderFinished: true,
                region: {
                  start: 20,
                  top: 20,
                  end: 200,
                  bottom: 240
                }
              })
            this.pixmap = pixelmap
          } catch (error) {
            console.error(`getSync errorCode:${error.code} message:${error.message}`)
          }
        }).margin(10)
      Image(this.pixmap).border({ color: Color.Black, width: 2 }).width("600px")
    }.width("100%").align(Alignment.Center)
  }
```