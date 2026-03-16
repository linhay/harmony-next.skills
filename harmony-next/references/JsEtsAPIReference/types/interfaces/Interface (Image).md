# Interface (Image)

Image类，用于获取图像内容。

调用[readNextImage](Interface (ImageReceiver).md#ZH-CN_TOPIC_0000002497605844__readnextimage9)和[readLatestImage](Interface (ImageReceiver).md#ZH-CN_TOPIC_0000002497605844__readlatestimage9)接口时会返回Image实例。

Image的属性仅支持在创建时初始化，后续无法再修改，且它的属性不对图像内容产生实际影响，请以图片生产者写入的属性为准，即以向[ImageReceiver](Interface (ImageReceiver).md)发送图片数据的发送方实际写入的内容为准。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用[release](#ZH-CN_TOPIC_0000002497445862__release9)方法及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

- 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 9开始支持。

#### 导入模块

```ets
import { image } from '@kit.ImageKit';
```

#### 属性

**系统能力：** SystemCapability.Multimedia.Image.Core

名称类型只读可选说明clipRect9+[Region](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__region8)否否要裁剪的图像区域。size9+[Size](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__size)是否

图像大小。

如果Image对象所存储的是相机预览流数据（YUV图像数据），那么获取到的size中的宽和高分别对应YUV图像的宽和高。

如果Image对象所存储的是相机拍照流数据（JPEG图像数据），由于已是编码后的文件，size中的宽等于JPEG文件大小，高等于1。

Image对象所存储的数据是预览流还是拍照流，取决于应用将receiver中的surfaceId传给相机的是previewOutput还是captureOutput。

相机预览与拍照最佳实践请参考[双路预览(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-dual-channel-preview)与[拍照实践(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-shooting-case)。

format9+number是否图像格式，参考[OH_NativeBuffer_Format](../../capi/headers/buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_format)。timestamp12+number是否图像时间戳。时间戳以纳秒为单位，通常是单调递增的。时间戳的具体含义和基准取决于图像的生产者，在相机预览/拍照场景，生产者就是相机。来自不同生产者的图像的时间戳可能有不同的含义和基准，因此可能无法进行比较。如果要获取某张照片的生成时间，可以通过[getImageProperty](Interface (ImageSource).md#ZH-CN_TOPIC_0000002497445864__getimageproperty11)接口读取相关的EXIF信息。

#### getComponent9+

getComponent(componentType: ComponentType, callback: AsyncCallback<Component>): void

根据图像的组件类型从图像中获取组件缓存。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明componentType[ComponentType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285837__componenttype9)是图像的组件类型。（目前仅支持 ComponentType:JPEG，实际返回格式由生产者决定，如相机）callbackAsyncCallback<[Component](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__component9)>是回调函数，当返回组件缓冲区成功，err为undefined，data为获取到的组件缓冲区；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetComponent(img : image.Image) {
  img.getComponent(image.ComponentType.JPEG, (err: BusinessError, component: image.Component) => {
    if (err) {
      console.error(`Failed to get the component.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in getting component.');
    }
  })
}
```

#### getComponent9+

getComponent(componentType: ComponentType): Promise<Component>

根据图像的组件类型从图像中获取组件缓存。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明componentType[ComponentType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285837__componenttype9)是图像的组件类型。（目前仅支持 ComponentType:JPEG，实际返回格式由生产者决定，如相机）。

**返回值：**

类型说明Promise<[Component](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445866__component9)>Promise对象，返回组件缓冲区。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function GetComponent(img : image.Image) {
  img.getComponent(image.ComponentType.JPEG).then((component: image.Component) => {
    console.info('Succeeded in getting component.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to get the component.code ${error.code},message is ${error.message}`);
  })
}
```

#### release9+

release(callback: AsyncCallback<void>): void

释放当前图像。使用callback异步回调。

在接收另一个图像前必须先释放对应资源。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数，当图像释放成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the image instance.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the image instance.');
    }
  })
}
```

#### release9+

release(): Promise<void>

释放当前图像。使用Promise异步回调。

在接收另一个图像前必须先释放对应资源。

由于图片占用内存较大，所以当Image实例使用完成后，应主动调用该方法，及时释放内存。

释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release().then(() => {
    console.info('Succeeded in releasing the image instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image instance.code ${error.code},message is ${error.message}`);
  })
}
```