# HandwriteController (手写套件功能)

手写套件的主要功能入口类，包含手写能力的主要方法。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Stylus.Handwrite

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { HandwriteController } from '@kit.Penkit';
```

本模块提供以下方法，完成手写内容的加载和保存等功能。

方法名称

说明

[load](#section81796536265)

从指定路径加载笔记文件。

[save](#section1858041418291)

保存手写内容。

[onLoad](#section759192934316)

加载完成时的回调接口。

[getContentRange](#section2152194517128)

获取笔迹范围。

[getThumbnail](#section1464912012163)

获取缩略图数据。

#### load

load(path: string): void

从指定路径加载笔记文件，调用时机：手写套件初始化之后。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Stylus.Handwrite

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

path

string

是

加载文件的路径。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API 错误码](../../errors/ArkTS API 错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

1010400001

load filed.

**示例**：

具体代码示例见[示例](#section67991620439)。

#### save

save(path: string): Promise<void>

保存笔记到指定路径，使用Promise异步回调。调用时机：手写套件加载完之后。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Stylus.Handwrite

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

path

string

是

保存文件的路径。

**返回值**:

类型

说明

Promise<void>

无返回结果的Promise对象。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API 错误码](../../errors/ArkTS API 错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

1010400002

save filed.

**示例**：

具体代码示例见[示例](#section67991620439)。

#### onLoad

onLoad(callback: AsyncCallback<string>): void

注册回调，加载完成后将会触发此回调，使用callback异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Stylus.Handwrite

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

callback

AsyncCallback<string>

是

回调函数。当加载成功时，err的message为load success；加载失败时，err的message为load failed；string为加载的路径。

**错误码**：

 以下错误码的详细介绍请参见 [ArkTS API 错误码](../../errors/ArkTS API 错误码.md)。

错误码ID

错误信息（此处仅提供错误抛出的关键信息）

1010400001

load filed.

#### getContentRange

getContentRange(): Rect

获取笔迹范围。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Stylus.Handwrite

**起始版本：**6.0.0(20)

**返回值**:

类型

说明

[Rect](#section10728472378)

Rect信息参数，表示内容涵盖的矩形区域。

#### getThumbnail

getThumbnail(rect: Rect): Promise<PixelMap>

获取缩略图数据。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Stylus.Handwrite

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

rect

[Rect](#section10728472378)

是

Rect信息参数，表示缩略图包含的矩形区域。

**返回值：**

类型

说明

Promise<[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)>

缩略图的数据。

#### Rect

Rect信息参数，表示矩形区域。

**系统能力：**SystemCapability.Stylus.Handwrite

**起始版本：**6.0.0(20)

名称

类型

说明

left

number

矩形左侧的位置。单位：手写套件组件[HandwriteComponent](../components/HandwriteComponent（手写套件组件）.md)宽度的1/1000。

top

number

矩形顶部的位置。单位：手写套件组件[HandwriteComponent](../components/HandwriteComponent（手写套件组件）.md)宽度的1/1000。

right

number

矩形右侧的位置。单位：手写套件组件[HandwriteComponent](../components/HandwriteComponent（手写套件组件）.md)宽度的1/1000。

bottom

number

矩形底部的位置。单位：手写套件组件[HandwriteComponent](../components/HandwriteComponent（手写套件组件）.md)宽度的1/1000。

#### **示例**

```ets
import { HandwriteController, HandwriteComponent, PenType, PenHspInfo } from '@kit.Penkit';

@Entry
@Component
struct HandWriteDemoComp {
  controller: HandwriteController = new HandwriteController();
  // 根据应用存储规则，获取到手写文件保存的路径，此处仅为实例参考
  initPath: string = this.getUIContext().getHostContext()?.filesDir + '/aa';
  penWidth: number = 5;
  ballpointPenWidth: number = 6;

  aboutToAppear() {
    // 加载时设置保存动作完成后的回调。
    this.controller.onLoad(this.callback);
  }

  // 手写文件内容加载完毕渲染上屏后的回调,通知接入用户,可在此处进行自定义行为
  callback = () => {
    // 自定义行为,例如文件加载完毕后展示用户操作指导
  }

  build() {
    Row() {
      Stack({ alignContent: Alignment.TopStart }) {
        HandwriteComponent({
          handwriteController: this.controller,
          defaultPenType: PenType.PEN, // 可选属性，默认笔刷
          defaultPenInfo: [{ penType: PenType.PEN, penWidth: this.penWidth },
            { penType: PenType.BALLPOINT_PEN, penWidth: this.ballpointPenWidth }] as PenHspInfo[], //可选属性，各笔刷的默认宽度
          widthRatio: 1,  //可选属性，自定义画布大小，宽度占比（0-1）。
          heightRatio: 1,  //可选属性，自定义画布大小，高度占比（0-1）。
          onInit: () => {
            // 画布初始化完成时的回调。此时可以调用接口加载和显示笔记内容
            this.controller?.load(this.initPath);
          },
          onScale: (scale: number) => {
            // 画布缩放时的回调方法，将返回当前手写控件的缩放比例，可在此处进行自定义行为。
          }
        })
        Button("save")
          .onClick(async () => {
            // 需根据应用存储规则，获取到手写文件保存的路径，此处仅为实例参考。
            const path = this.getUIContext().getHostContext()?.filesDir + '/aa';
            await this.controller?.save(path).then().catch((error: Error) => {
              console.info("err：" + error);
            })
            this.controller.getThumbnail(this.controller?.getContentRange())?.then((pixelMap: PixelMap) => {
              if (pixelMap) {
                pixelMap.release()
                console.info('getThumbnail success')
              }
            })
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

HandwriteController中的方法需要放在上述示例的画布控件初始化的回调中运行或自定义的方法中运行。

使用前需要先[设置context信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-suite#section151484318552)。

完整示例代码可参考[手写笔服务（ArkTS）](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_PenKit-Next-Easy)。