# PlayImageAnimation

#### 导入模块

```ets
import { map } from '@kit.MapKit';
```

#### PlayImageAnimation

控制多张图片的帧动画，继承[Animation](../misc/Animation.md)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**示例：**

```ets
import { image } from '@kit.ImageKit';

let images: Array<ResourceStr | image.PixelMap> = [
   'test1.png',
   'test2.png',
   'test3.png',
   'test4.png'
];
let playImageAnimation: map.PlayImageAnimation = new map.PlayImageAnimation();
await playImageAnimation.addImages(images);
```

#### addImages

addImages(images: Array<ResourceStr | image.PixelMap>): Promise<void>

添加动画的图片资源。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

images

Array<[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | [image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)>

是

动画的图片资源。

 说明：

- 建议图片大小相同。
- 图片数量不超过200张。
- 持续时间需要大于33毫秒。如果不是，它将被更改为33。
- string类型入参，图片存放在resources/rawfile。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

**示例：**

```ets
import { image } from '@kit.ImageKit';

let images: Array<ResourceStr | image.PixelMap> = [
   'test1.png',
   'test2.png',
   'test3.png',
   'test4.png'
];
await playImageAnimation.addImages(images);
```