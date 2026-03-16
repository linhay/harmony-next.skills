# CollaborationService (跨设备互通组件)

该模块提供了组件[createCollaborationServiceMenuItems](#section1633482912443)和[CollaborationServiceFilter](#section12639651397)，两者需要配合使用，完成分布式跨端能力，如在2in1端跨端调用手机端拍照。

通过[createCollaborationServiceMenuItems](#section1633482912443)组件，可以获取组网内具有对应能力的设备列表。用户选择对应的设备后，拉起应用。调用[CollaborationServiceStateDialog](#section158671330145417)，应用将弹出提示框，提示对端应用状态。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { CollaborationServiceStateDialog, createCollaborationServiceMenuItems, CollaborationServiceFilter} from '@kit.ServiceCollaborationKit';
```

#### createCollaborationServiceMenuItems

createCollaborationServiceMenuItems(businessFilter?: Array<CollaborationServiceFilter>): void

设备列表选择器，需要在[Menu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menu)组件内调用。用于显示组网内具有对应能力的设备列表。

该方法为自定义构建函数，开发者在使用前需要先了解[@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)。

**装饰器类型：**@Builder

**系统能力：**SystemCapability.Collaboration.Service

**设备行为差异：**该接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

businessFilter

Array<[CollaborationServiceFilter](#section12639651397)>

否

传入能力类型。默认值为ALL，匹配跨端拍照、文档扫描和图库选择器。

对于API 6.0.0(20)及之后版本，支持匹配跨端拍照、文档扫描、图库选择器、视频选择器、图片和视频选择器；对于API 6.0.0(20)之前版本，仅支持匹配跨端拍照、文档扫描、图库选择器。

**示例****：**

```ets
@Builder
MyTestMenu() {
  Menu() {
    createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL])
  }
}
```

#### createCollaborationServiceMenuItems

createCollaborationServiceMenuItems(businessFilter: Array<CollaborationServiceFilter>, canReceiveNumber: number): void

设备列表选择器，需要在[Menu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menu)组件内调用。用于显示组网内具有对应能力的设备列表，此接口支持自定义对端图库能力图片选择的数量。

该方法为自定义构建函数，开发者在使用前需要先了解[@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)。

**装饰器类型：**@Builder

**系统能力：**SystemCapability.Collaboration.Service

**设备行为差异：**该接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

businessFilter

Array<[CollaborationServiceFilter](#section12639651397)>

是

传入能力类型。默认值为ALL，匹配跨端拍照、文档扫描和图库选择器。

对于API 6.0.0(20)及之后版本，支持匹配跨端拍照、文档扫描、图库选择器、视频选择器、图片和视频选择器；对于API 6.0.0(20)之前版本，仅支持匹配跨端拍照、文档扫描、图库选择器。

canReceiveNumber

number

是

传入照片最大张数，数量1到50，小于等于0时不会拉起被调用设备的能力，大于50默认为50。

**示例****：**

```ets
@Builder
MyTestMenu() {
  Menu() {
    createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 30)
  }
}
```

#### CollaborationServiceFilter

能力类型枚举值。

**系统能力：**SystemCapability.Collaboration.Service

**设备行为差异：**该接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：**5.0.0(12)

名称

值

说明

ALL

0

匹配跨端拍照、文档扫描和图库选择器。

TAKE_PHOTO

1

匹配跨端拍照。

SCAN_DOCUMENT

2

匹配文档扫描。

IMAGE_PICKER

3

匹配图库选择器。

VIDEO_PICKER

5

匹配视频选择器。

**起始版本：**6.0.0(20)

IMAGE_VIDEO_PICKER

6

匹配图片和视频选择器。

**起始版本：**6.0.0(20)

**示例****：**

```ets
@Builder
MyTestMenu() {
  Menu() {
    createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 30)
  }
}
```

#### CollaborationServiceStateDialog

弹窗组件，用于提示对端应用状态。

您需要实现[onState](#section33027582114)方法，并且在页面中定义这个组件，在业务开始后，此方法将被协同框架调用。

该组件为自定义组件，开发者在使用前需要先了解[@Component](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#component)。

**装饰器类型：**@Component

**系统能力：**SystemCapability.Collaboration.Service

**设备行为差异：**该接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：**5.0.0(12)

#### onState

onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer) => void

接收数据的回调函数，其中传入的stateCode是完成状态，bufferType是回传的数据类型，buffer是回传的数据内容，开发者可通过状态和数据结合自身的业务逻辑实现onState方法。

**系统能力：**SystemCapability.Collaboration.Service

**设备行为差异：**该接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

stateCode

number

是

标识业务完成状态，含义详见下面状态码。

bufferType

string

是

标识回传数据类型。

"general.image"：图片类型。

"general.fileName"：文件名称。

"general.video"：视频。

buffer

ArrayBuffer

是

成功则返回对应数据，失败则返回空。

**状态码：**

以下部分错误状态的详细介绍请参见[ArkTS 错误码](../../errors/ArkTS 错误码.md)。

状态码ID

错误信息

0

成功。

1001202001

对端取消。

1001202002

协同框架内部出现错误。

1001202003

本端取消。

1001202004

跨设备互通能力开始。

1001202005

图片全部回传结束。

1001202006

回传文件名称。

1001202007

当[createCollaborationServiceMenuItems](#section149271552154711)传入自定义图片张数canReceiveNumber小于等于0时，不会拉起被调用设备的能力。

#### build

build(): void

struct的默认构造函数，开发者无法直接调用此方法。

**系统能力：**SystemCapability.Collaboration.Service

**设备行为差异：**该接口在PC/2in1、Tablet可被组件正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：**5.0.0(12)

**示例**

参考以下示例，可以完成一次调用对端应用的操作。

跨设备互通详细介绍可参考[跨设备互通特性简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/servicecollaboration-service-overview)。

```ets
import {
  createCollaborationServiceMenuItems,
  CollaborationServiceStateDialog,
  CollaborationServiceFilter
} from '@kit.ServiceCollaborationKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State picture: PixelMap | undefined = undefined;

  @Builder
  MyTestMenu() {
    Menu() {
      createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 30)
    }
  }

  build() {
    Column({ space: 20 }) {
      CollaborationServiceStateDialog({
        onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer): void => this.doInsertPicture(stateCode, bufferType, buffer)
      })
      Button('使用远端设备进行拍照')
        .type(ButtonType.Normal)
        .borderRadius(10)
        .bindMenu(this.MyTestMenu)

      if (this.picture) {
        Image(this.picture)
          .borderStyle(BorderStyle.Dotted)
          .borderWidth(1)
          .objectFit(ImageFit.Contain)
          .height('80%')
          .onComplete((event) => {
            if (event != undefined) {
              hilog.info(0, "MEMOMOCK", "onComplete " + event.loadingStatus)
            }
          })
      }
    }
    .padding(20)
    .width('100%')
    .alignItems(HorizontalAlign.Center)
  }

  doInsertPicture(stateCode: number, bufferType: string, buffer: ArrayBuffer): void {
    if (stateCode != 0) {
      return
    }
    if (bufferType == "general.image") {
      let imageSource = image.createImageSource(buffer)
      imageSource.createPixelMap().then((pixelMap) => {
        this.picture = pixelMap;
      })
    }
  }
}
```