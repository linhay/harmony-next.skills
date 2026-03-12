# @ohos.multimedia.videoProcessingEngine (视频处理引擎)

本模块提供图片内容的清晰度增强及缩放能力。

本模块包含一个基础类：[ImageProcessor](#ZH-CN_TOPIC_0000002497445868__imageprocessor)类。

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { videoProcessingEngine } from '@kit.ImageKit';
```

#### videoProcessingEngine.initializeEnvironment

initializeEnvironment(): Promise<void>

初始化环境。使用Promise异步回调。

**卡片能力**：从API version 18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[视频处理引擎错误码](视频处理引擎错误码.md)

错误码ID错误信息801Capability not supported. Function initializeEnvironment can not work correctly due to limited device capabilities.29200002The global environment initialization for image processing failed, such as failure to initialize the GPU environment.29200006The operation is not permitted. This may be caused by incorrect status.29200007Out of memory.

**示例：**

```ets
import { videoProcessingEngine } from '@kit.ImageKit';

async function initializeEnvironment() {
  videoProcessingEngine.initializeEnvironment();
}
```

#### videoProcessingEngine.deinitializeEnvironment

deinitializeEnvironment(): Promise<void>

释放处理资源。使用Promise异步回调。

**卡片能力**：从API version 18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[视频处理引擎错误码](视频处理引擎错误码.md)

错误码ID错误信息29200006The operation is not permitted. This may be caused by incorrect status.

**示例：**

```ets
import { videoProcessingEngine } from '@kit.ImageKit';

async function deinitializeEnvironment() {
  videoProcessingEngine.initializeEnvironment();
  videoProcessingEngine.deinitializeEnvironment();
}
```

#### videoProcessingEngine.create

create(): ImageProcessor

如果操作成功，创建图片处理模块实例，否则返回null。

**卡片能力**：从API version 18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**返回值：**

类型说明[ImageProcessor](#ZH-CN_TOPIC_0000002497445868__imageprocessor)图片处理模块实例。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[视频处理引擎错误码](视频处理引擎错误码.md)

错误码ID错误信息801Capability not supported. Function create can not work correctly due to limited device capabilities.29200003Failed to create image processing instance. For example, the number of instances exceeds the upper limit.29200007Out of memory.

**示例：**

```ets
import { videoProcessingEngine } from '@kit.ImageKit';

async function create() {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
}
```

#### ImageProcessor

图像处理类，提供图片内容的清晰度增强及缩放能力。根据源图像的宽度和高度进行必要的缩放操作，生成目标图像。提供不同级别的缩放方法以平衡性能和图像质量。

规格约束如下：

- 当前仅支持处理SDR（Standard dynamic range）图片。
- 当前支持处理RGBA、BGRA、NV12、NV21像素格式的图片，输出格式与输入格式一致。

#### enhanceDetail

enhanceDetail(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): Promise<image.PixelMap>

细节增强处理异步方法。使用Promise异步回调。

**卡片能力**：从API version 18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

参数名类型必填说明sourceImage[image.PixelMap](Interface (PixelMap).md)是输入图像，内存类型需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。widthnumber是

目标宽度，单位为像素（px）。

当level为high时，支持范围[512, 2000]；当level为其他时，支持范围[32, 3000]。

heightnumber是

目标高度，单位为像素（px）。

当level为high时，支持范围[512, 2000]；当level为其他时，支持范围[32, 3000]。

level[QualityLevel](#ZH-CN_TOPIC_0000002497445868__qualitylevel)否算法档位（HIGH、MEDIUM、LOW、NONE），默认为NONE。

**返回值：**

类型说明Promise<[image.PixelMap](Interface (PixelMap).md)>异步方法返回PixelMap的Promise实例。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[视频处理引擎错误码](视频处理引擎错误码.md)

错误码ID错误信息801Capability not supported. Function enhanceDetail can not work correctly due to limited device capabilities.29200007Out of memory.29200009

Input value is invalid. This error is returned for all of the following error conditions:

1 - Invalid input or output image buffer - The image buffer width(height) is too large or colorspace is incorrect.

2 - Invalid parameter - The parameter does not contain valid information, such as detail enhancer level is incorrect.

**示例：**

```ets
import { image, videoProcessingEngine } from '@kit.ImageKit';

async function enhanceDetail(sourceImage: image.PixelMap, width: number, height: number) {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
  // 示例：width可配置为1024，height可配置为1280。
  let enhancedPixelmap: Promise<image.PixelMap> =
    imageProcessor.enhanceDetail(sourceImage, width, height, videoProcessingEngine.QualityLevel.HIGH);
}
```

#### enhanceDetail

enhanceDetail(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): Promise<image.PixelMap>

细节增强处理异步方法。使用Promise异步回调。

**卡片能力**：从API version 18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

参数名类型必填说明sourceImage[image.PixelMap](Interface (PixelMap).md)是输入图像，内存类型需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。scalenumber是目标缩放比例。取值范围(0.0, 32.0]（在满足[上述分辨率范围](#ZH-CN_TOPIC_0000002497445868__enhancedetail)的前提下，最高支持32倍放大）。level[QualityLevel](#ZH-CN_TOPIC_0000002497445868__qualitylevel)否算法档位（HIGH、MEDIUM、LOW、NONE），默认为NONE。

**返回值：**

类型说明Promise<[image.PixelMap](Interface (PixelMap).md)>异步方法返回PixelMap的Promise实例。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[视频处理引擎错误码](视频处理引擎错误码.md)

错误码ID错误信息801Capability not supported. Function enhanceDetail can not work correctly due to limited device capabilities.29200007Out of memory.29200009

Input value is invalid. This error is returned for all of the following error conditions:

1 - Invalid input or output image buffer - The image buffer width(height) is too large or colorspace is incorrect.

2 - Invalid parameter - The parameter does not contain valid information, such as detail enhancer level is incorrect.

**示例：**

```ets
import { image, videoProcessingEngine } from '@kit.ImageKit';

async function enhanceDetail(sourceImage: image.PixelMap, scale: number) {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
  // 示例：scale可配置为2.0。
  let enhancedPixelmap: Promise<image.PixelMap> =
    imageProcessor.enhanceDetail(sourceImage, scale, videoProcessingEngine.QualityLevel.HIGH);
}
```

#### enhanceDetailSync

enhanceDetailSync(sourceImage: image.PixelMap, width: number, height: number, level?: QualityLevel): image.PixelMap

细节增强处理同步方法。

**卡片能力**：从API version 18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

参数名类型必填说明sourceImage[image.PixelMap](Interface (PixelMap).md)是输入图像，内存类型需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。widthnumber是

目标宽度，单位为像素（px）。

当level为high时，支持范围[512, 2000]；当level为其他时，支持范围[32, 3000]。

heightnumber是

目标高度，单位为像素（px）。

当level为high时，支持范围[512, 2000]；当level为其他时，支持范围[32, 3000]。

level[QualityLevel](#ZH-CN_TOPIC_0000002497445868__qualitylevel)否算法档位（HIGH、MEDIUM、LOW、NONE），默认为NONE。

**返回值：**

类型说明[image.PixelMap](Interface (PixelMap).md)成功同步返回PixelMap对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[视频处理引擎错误码](视频处理引擎错误码.md)

错误码ID错误信息801Capability not supported. Function enhanceDetailSync can not work correctly due to limited device capabilities.29200004Failed to process image buffer. For example, the processing times out.29200007Out of memory.29200009

Input value is invalid. This error is returned for all of the following error conditions:

1 - Invalid input or output image buffer - The image buffer width(height) is too large or colorspace is incorrect.

2 - Invalid parameter - The parameter does not contain valid information, such as detail enhancer level is incorrect.

**示例：**

```ets
import { image, videoProcessingEngine } from '@kit.ImageKit';

async function enhanceDetailSync(sourceImage: image.PixelMap, width: number, height: number) {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
  // 示例：width可配置为1024，height可配置为1280。
  let enhancedPixelmap: image.PixelMap = imageProcessor.enhanceDetailSync(
    sourceImage, width, height, videoProcessingEngine.QualityLevel.HIGH);
}
```

#### enhanceDetailSync

enhanceDetailSync(sourceImage: image.PixelMap, scale: number, level?: QualityLevel): image.PixelMap

细节增强处理同步方法。

**卡片能力**：从API version 18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**参数：**

参数名类型必填说明sourceImage[image.PixelMap](Interface (PixelMap).md)是输入图像，内存类型需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。scalenumber是目标缩放比例。取值范围(0.0, 32.0]（在满足[上述分辨率范围](#ZH-CN_TOPIC_0000002497445868__enhancedetail)的前提下，最高支持32倍放大）。level[QualityLevel](#ZH-CN_TOPIC_0000002497445868__qualitylevel)否算法档位（HIGH、MEDIUM、LOW、NONE），默认为NONE。

**返回值：**

类型说明[image.PixelMap](Interface (PixelMap).md)成功同步返回PixelMap对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[视频处理引擎错误码](视频处理引擎错误码.md)

错误码ID错误信息801Capability not supported. Function enhanceDetailSync can not work correctly due to limited device capabilities.29200004Failed to process image buffer. For example, the processing times out.29200007Out of memory.29200009

Input value is invalid. This error is returned for all of the following error conditions:

1 - Invalid input or output image buffer - The image buffer width(height) is too large or colorspace is incorrect.

2 - Invalid parameter - The parameter does not contain valid information, such as detail enhancer level is incorrect.

**示例：**

```ets
import { image, videoProcessingEngine } from '@kit.ImageKit';

async function enhanceDetailSync(sourceImage: image.PixelMap, scale: number) {
  videoProcessingEngine.initializeEnvironment();
  let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
  // 示例：scale可配置为2.0。
  let enhancedPixelmap: image.PixelMap = imageProcessor.enhanceDetailSync(
    sourceImage, scale, videoProcessingEngine.QualityLevel.HIGH);
}
```

#### QualityLevel

枚举，算法档位。

**卡片能力**：从API version 18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

名称值说明NONE0

仅适用于缩放场景，支持改变宽高比例。

- 输入分辨率要求（单位为像素，px）：宽：[32，3000]，高：[32，3000]。

- 输出分辨率要求（单位为像素，px）：宽：[32，3000]，高：[32，3000]。

LOW1

仅适用于缩放场景，支持改变宽高比例。

- 输入分辨率要求（单位为像素，px）：宽：[32，3000]，高：[32，3000]。

- 输出分辨率要求（单位为像素，px）：宽：[32，3000]，高：[32，3000]。

MEDIUM2

仅适用于缩放场景，支持改变宽高比例。

- 输入分辨率要求（单位为像素，px）：宽：[32，3000]，高：[32，3000]。

- 输出分辨率要求（单位为像素，px）：宽：[32，3000]，高：[32，3000]。

HIGH3

1. 缩放场景，不支持改变宽高比例。

- 输入分辨率要求（单位为像素，px）：宽：(32，512) (2000，8192]，高：(32，512) (2000，8192]。

- 输出分辨率要求（单位为像素，px）：宽：(32，512) (2000，8192]，高：(32，512) (2000，8192]。

2. 清晰度增强、缩放场景，支持改变宽高比例。

- 输入分辨率要求（单位为像素，px）：宽：[512，2000]，高：[512，2000]。

- 输出分辨率要求（单位为像素，px）：宽：[512，2000]，高：[512，2000]。