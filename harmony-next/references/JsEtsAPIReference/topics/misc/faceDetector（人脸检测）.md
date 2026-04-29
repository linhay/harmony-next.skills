# faceDetector（人脸检测）

人脸检测支持2D人脸检测框的检测能力。检测给定图片中的人脸数量、人脸位置、特征点（左右眼中心、鼻子、左右嘴角）和姿态（pitch、roll、yaw）信息。人脸检测框按照大小排序。

与Vision Kit的活体检测的区别是：活体检测用于视频，人脸检测用于图片。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { faceDetector } from '@kit.CoreVisionKit';
```

#### VisionInfo

待识别的视觉信息，目前仅支持颜色数据格式为RGBA_8888的PixelMap类型的视觉信息。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AI.Face.Detector

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | image.PixelMap | 是 | 否 | 待识别的图片。 具体规格请参考约束与限制。 |

#### FaceRecognitionConfiguration

人脸遮挡检测的配置项。

**系统能力：**SystemCapability.AI.Face.Detector

**起始版本：**5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| faceBlock | boolean | 是 | 否 | 是否开启人脸遮挡检测。 true：开启人脸遮挡检测；false：不开启人脸遮挡检测。默认为false。 |

#### FaceBlock

人脸遮挡检测结果的枚举类。

**系统能力：**SystemCapability.AI.Face.Detector

**起始版本：**5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNINITIALIZED | -1 | 人脸遮挡检测未开启。 |
| UNBLOCKED | 0 | 人脸无遮挡。 |
| BLOCKED | 1 | 人脸有遮挡。 |

#### FacePoint

指示像素点的位置。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AI.Face.Detector

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 是 | 否 | 像素点横向x坐标。 |
| y | number | 是 | 否 | 像素点纵向y坐标。 |

#### FacePose

描述人脸在三维空间中的方向。坐标系可参考[世界坐标系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-face-detector#世界坐标系)。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AI.Face.Detector

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| yaw | number | 是 | 否 | 头型航向，将物体绕Y轴旋转（localRotationY）。取值范围[-180,180]。 |
| pitch | number | 是 | 否 | 头型俯仰，将物体绕X轴旋转（localRotationX）。取值范围[-180,180]。 |
| roll | number | 是 | 否 | 头型横滚，将物体绕Z轴旋转（localRotationZ）。取值范围[-180,180]。 |

#### FaceRectangle

表示人脸的矩形框。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AI.Face.Detector

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 是 | 否 | 人脸矩形框左上角x坐标。 |
| top | number | 是 | 否 | 人脸矩形框左上角y坐标。 |
| width | number | 是 | 否 | 人脸框宽，单位：pixel。 |
| height | number | 是 | 否 | 人脸框高，单位：pixel。 |

#### Face

表示人脸的信息列表。

**系统能力：**SystemCapability.AI.Face.Detector

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| probability | number | 是 | 否 | 表示人脸检测结果的置信度，取值范围为(0,1)的浮点数，数值越大代表置信度越高。 元服务API：从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| block | FaceBlock | 是 | 是 | 人脸遮挡结果。 起始版本：5.0.2(14)。 |
| pose | FacePose | 是 | 否 | 人脸头型航向。 元服务API：从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| rect | FaceRectangle | 是 | 否 | 人脸框列表。 元服务API：从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| points | Array<FacePoint> | 是 | 否 | 人脸五官位置数组，包括：左右眼中心、鼻子、左右嘴角。参数顺序为：左眼中心，右眼中心，鼻子，左嘴角，右嘴角。 元服务API：从版本5.0.2(14)开始，该接口支持在元服务中使用。 |

#### faceDetector.init

init(): Promise<boolean>

初始化人脸检测分析器服务。使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AI.Face.Detector

**起始版本：**5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回初始化是否成功。 true：初始化成功；false：初始化失败。 |

**示例：**

```ets
import { faceDetector } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseFaceDetector() {
  // 初始化人脸检测服务
  const initResult = await faceDetector.init();
  hilog.info(0x0000, 'faceDetectorSample', `Face detector initialization result:${initResult}`);

  if (initResult) {
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector initialized successfully');

    // 这里可以添加使用人脸检测服务的代码

    // 使用完毕后，释放人脸检测服务
    await faceDetector.release();
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
  } else {
    hilog.error(0x0000, 'faceDetectorSample', 'Failed to initialize face detector');
  }

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseFaceDetector').onClick(() => {
        // 调用函数
        void initAndReleaseFaceDetector();
      })
}
```

#### faceDetector.init

init(faceRecognitionConfiguration: FaceRecognitionConfiguration): Promise<boolean>

初始化人脸遮挡检测分析器服务。同一个进程内只要有人脸检测服务开启了遮挡检测，在该人脸检测服务未release这段时间内，这个进程内的其他所有人脸检测服务都等同于开启了遮挡检测。使用Promise异步回调。

**系统能力：**SystemCapability.AI.Face.Detector

**起始版本：**5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| faceRecognitionConfiguration | FaceRecognitionConfiguration | 是 | 人脸遮挡检测配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回初始化是否成功。 true：初始化成功；false：初始化失败。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```ets
import { faceDetector } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseFaceDetector() {
  let config: faceDetector.FaceRecognitionConfiguration = {
    faceBlock: true
  }
  // 初始化人脸遮挡检测服务
  const initResult = await faceDetector.init(config);
  hilog.info(0x0000, 'faceDetectorSample', `Face detector initialization result:${initResult}`);

  if (initResult) {
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector initialized successfully');

    // 这里可以添加使用人脸检测服务的代码

    // 使用完毕后，释放人脸检测服务
    await faceDetector.release();
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
  } else {
    hilog.error(0x0000, 'faceDetectorSample', 'Failed to initialize face detector');
  }

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseFaceDetector').onClick(() => {
        // 调用函数
        void initAndReleaseFaceDetector();
      })
}
```

#### faceDetector.release

release(): Promise<void>

释放人脸检测分析器服务。使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AI.Face.Detector

**起始版本：**5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，释放接口无返回值。 |

**示例：**

```ets
import { faceDetector } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseFaceDetector() {
  // 初始化人脸检测服务
  const initResult = await faceDetector.init();
  hilog.info(0x0000, 'faceDetectorSample', `Face detector initialization result:${initResult}`);

  if (initResult) {
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector initialized successfully');

    // 这里可以添加使用人脸检测服务的代码

    // 使用完毕后，释放人脸检测服务
    await faceDetector.release();
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
  } else {
    hilog.error(0x0000, 'faceDetectorSample', 'Failed to initialize face detector');
  }

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseFaceDetector').onClick(() => {
        // 调用函数
        void initAndReleaseFaceDetector();
      })
}
```

#### faceDetector.detect

detect(visionInfo: VisionInfo): Promise<Array<Face>>

检测一张图片中的人脸信息，使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AI.Face.Detector

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visionInfo | VisionInfo | 是 | 图片实例（包含人脸）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<Face>> | Promise对象，返回人脸检测的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1008800001 | Failed to run, please try again. |
| 1008800002 | The service is abnormal. |

**示例：**

```ets
import { faceDetector } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

let imageSource: image.ImageSource | undefined = undefined;
let chooseImage: PixelMap | undefined = undefined;

// 将图片转换为PixelMap，可以通过图库获取
let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select({
  MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
  maxSelectNumber: 1
}).then((res: photoAccessHelper.PhotoSelectResult) => {
  let uri = res.photoUris[0];
  if (uri === undefined) {
    hilog.info(0x0000, 'faceDetectorSample', 'uri is undefined');
    return
  }
  setTimeout(async () => {
    let file = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
    imageSource = image.createImageSource(file.fd);
    chooseImage = await imageSource.createPixelMap();
    hilog.info(0x0000, 'faceDetectorSample', 'chooseImage:', chooseImage);
    if (!chooseImage) {
      return
    }
    // 调用人脸检测接口
    let visionInfo: faceDetector.VisionInfo = {
      pixelMap: chooseImage
    };
    let data: faceDetector.Face[] = await faceDetector.detect(visionInfo);
    if (data.length === 0) {
      hilog.info(0x0000, 'faceDetectorSample', 'No face is detected in the image.');
    } else {
      let faceString = JSON.stringify(data);
      hilog.info(0x0000, 'faceDetectorSample', 'faceString data is ' + faceString);
    }

    if (chooseImage && imageSource) {
      void chooseImage.release();
      void imageSource.release();
    }
    if (file) {
      try {
        await fileIo.close(file);
      } catch (err) {
        hilog.error(0x0000, 'faceDetectorSample', `Failed to close fileSource. Code: ${err.code}, message: ${err.message}`);
    }
  }, 100);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'faceDetectorSample', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
});

@Entry
@Component
struct Page {

  build() {
    Column(){
    }
```