# faceComparator（人脸比对）

识别人脸，对人像进行高精度比对，给出置信度分数，判断对象是否为同一个人。人脸比对技术可应用于实现对图库照片的智能分类管理等场景中。基于领先的端侧智能图像识别算法，对人脸识别准确度高，让应用体验更好。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { faceComparator } from '@kit.CoreVisionKit';
```

#### VisionInfo

待识别的视觉信息，目前仅支持颜色数据格式为RGBA_8888的PixelMap类型的视觉信息。

**系统能力：**SystemCapability.AI.Face.Comparator

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

pixelMap

[image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

是

否

待识别的图片。

具体规格请参考[约束与限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-introduction#section625292610522)。

#### FaceCompareResult

人脸比对的结果。

**系统能力：**SystemCapability.AI.Face.Comparator

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

isSamePerson

boolean

是

否

是否是同一个人，true代表为同一个人，false不是同一个人。

similarity

number

是

否

相似度，取值范围是(0,1)的浮点数。值越大说明相似程度越高。

#### faceComparator.init

init(): Promise<boolean>

初始化人脸比对分析器服务。使用Promise异步回调。

**系统能力：**SystemCapability.AI.Face.Comparator

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

Promise<boolean>

Promise对象，返回初始化是否成功。

true：初始化成功；false：初始化失败。

**示例：**

```ets
import { faceComparator } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseFaceComparator() {
  // 初始化人脸比较服务
  const initResult = await faceComparator.init();
  hilog.info(0x0000, 'faceComparatorSample', `Face comparator initialization result:${initResult}`);

  if (initResult) {
    hilog.info(0x0000, 'faceComparatorSample', 'Face comparator initialized successfully');

    // 这里可以添加使用人脸比较服务的代码

    // 使用完毕后，释放人脸比较服务
    await faceComparator.release();
    hilog.info(0x0000, 'faceComparatorSample', 'Face comparator released successfully');
  } else {
    hilog.error(0x0000, 'faceComparatorSample', 'Failed to initialize face comparator');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseFaceComparator').onClick(() => {
        // 调用函数
        initAndReleaseFaceComparator();
      })
    }
  }
}
```

#### faceComparator.release

release(): Promise<void>

释放人脸比对分析器服务。使用Promise异步回调。

**系统能力：**SystemCapability.AI.Face.Comparator

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

Promise<void>

Promise对象，释放接口无返回值。

**示例：**

```ets
import { faceComparator } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseFaceComparator() {
  // 初始化人脸比较服务
  const initResult = await faceComparator.init();
  hilog.info(0x0000, 'faceComparatorSample', `Face comparator initialization result:${initResult}`);

  if (initResult) {
    hilog.info(0x0000, 'faceComparatorSample', 'Face comparator initialized successfully');

    // 这里可以添加使用人脸比较服务的代码

    // 使用完毕后，释放人脸比较服务
    await faceComparator.release();
    hilog.info(0x0000, 'faceComparatorSample', 'Face comparator released successfully');
  } else {
    hilog.error(0x0000, 'faceComparatorSample', 'Failed to initialize face comparator');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseFaceComparator').onClick(() => {
        // 调用函数
        initAndReleaseFaceComparator();
      })
    }
  }
}
```

#### faceComparator.compareFaces

compareFaces(visionInfo1: VisionInfo, visionInfo2: VisionInfo): Promise<FaceCompareResult>

创建人脸比对实例，使用Promise异步回调。

**系统能力：**SystemCapability.AI.Face.Comparator

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

visionInfo1

[VisionInfo](#section674171818172)

是

第一张包含人脸的图片。

visionInfo2

[VisionInfo](#section674171818172)

是

第二张包含人脸的图片。

**返回值：**

类型

说明

Promise<[FaceCompareResult](#section1518613358392)>

Promise对象，返回人脸比对的结果。

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

200

Run timed out, please try again later.

401

The parameter check failed.

1008400001

Failed to run, please try again.

1008400002

The service is abnormal.

**示例：**

```ets
import { faceComparator } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function faceCompareTest() {
  let chooseImage: PixelMap | undefined = undefined;
  let chooseImage1: PixelMap | undefined = undefined;

  // 从图库中选择两张图片
  let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
  PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
  PhotoSelectOptions.maxSelectNumber = 2;
  let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
  let PhotoSelectResult = await photoPicker.select(PhotoSelectOptions);
  let uris = PhotoSelectResult.photoUris;

  if (uris.length !== 2) {
    hilog.info(0x0000, 'testTag', 'selected uris length is not 2');
    return;
  }

  // 将选择的图片转换为PixelMap
  let fileSource = await fileIo.open(uris[0], fileIo.OpenMode.READ_ONLY);
  let imageSource = image.createImageSource(fileSource.fd);
  chooseImage = await imageSource.createPixelMap();

  fileSource = await fileIo.open(uris[1], fileIo.OpenMode.READ_ONLY);
  imageSource = image.createImageSource(fileSource.fd);
  chooseImage1 = await imageSource.createPixelMap();

  if (!chooseImage || !chooseImage1) {
    hilog.info(0x0000, 'testTag', 'chooseImage or chooseImage1 is undefined');
    return;
  }

  // 调用人脸比对接口
  let visionInfo: faceComparator.VisionInfo = {
    pixelMap: chooseImage
  };
  let visionInfo1: faceComparator.VisionInfo = {
    pixelMap: chooseImage1
  };

  let data: faceComparator.FaceCompareResult = await faceComparator.compareFaces(visionInfo, visionInfo1);
  let similarity = (data.similarity * 100).toFixed(2);
  let isSamePerson = data.isSamePerson ? 'is' : 'is not';
  let faceString = `Similarity: ${similarity}%. ${isSamePerson} the same person`;
  hilog.info(0x0000, 'testTag', 'faceString data is ' + faceString);

  // 释放资源
  if (chooseImage && chooseImage1) {
    chooseImage.release();
    chooseImage1.release();
  }
  if (fileSource) {
    try {
      await fileIo.close(fileSource);
    } catch (err) {
      hilog.error(0x0000, 'testTag', `Failed to close fileSource. Code: ${err.code}，message: ${err.message}`);
    }
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('faceCompareTest').onClick(() => {
        faceCompareTest().catch((err: BusinessError) => {
          hilog.error(0x0000, 'faceCompareSample', `Failed to compare faces. code: ${err.code}，message: ${err.message}`);
        });
      })
    }
  }
}
```