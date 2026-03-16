# skeletonDetection（骨骼点检测）

骨骼点检测可以从图像中检测出人体的关键骨骼点，如头部、肩部、手肘、手腕、髋部、膝盖、脚踝等，并给出它们的位置坐标和置信度。同时，骨骼点检测是一项底层的AI能力，还可以与Core Vision Kit中其他AI能力如人脸识别、文字识别等组合使用，开发出更加智能化的应用。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { visionBase, skeletonDetection } from '@kit.CoreVisionKit';
```

#### SkeletonPointType

骨骼点类型的枚举类。

**系统能力：**SystemCapability.AI.Vision.SkeletonDetection

**起始版本：**5.0.0(12)

名称

值

说明

NOSE

0

鼻子。

LEFT_EYE

1

左眼。

RIGHT_EYE

2

右眼。

LEFT_EAR

3

左耳。

RIGHT_EAR

4

右耳。

LEFT_SHOULDER

5

左肩。

RIGHT_SHOULDER

6

右肩。

LEFT_ELBOW

7

左肘。

RIGHT_ELBOW

8

右肘。

LEFT_WRIST

9

左腕。

RIGHT_WRIST

10

右腕。

LEFT_HIP

11

左髋。

RIGHT_HIP

12

右髋。

LEFT_KNEE

13

左膝。

RIGHT_KNEE

14

右膝。

LEFT_ANKLE

15

左脚踝。

RIGHT_ANKLE

16

右脚踝。

#### SkeletonPoint

详细的骨骼点信息。

**系统能力：**SystemCapability.AI.Vision.SkeletonDetection

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

point

visionBase.[Point](VisionBase（Core Vision Kit基类）.md#section1465431712919)

否

否

骨骼点的图像坐标，即它在图像中的x和y位置。

score

number

否

否

骨骼点的置信度。取值范围是(0,1)。0表示置信度最低，1表示置信度最高，置信度越高，说明这个点的位置越可靠。

type

[SkeletonPointType](#section4298938144913)

否

否

骨骼点的类型，即它在人体骨骼模型中的位置。

#### Skeleton

用于描述一个完整的人体骨骼检测结果。包括总体置信度和人体在图像中的大致位置，还详细列出了各个关键点的位置和类型。

**系统能力：**SystemCapability.AI.Vision.SkeletonDetection

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

boundingBox

visionBase.[BoundingBox](VisionBase（Core Vision Kit基类）.md#section789716171126)

否

否

骨骼的边界框，也就是所有骨骼点加一起的矩形框。

score

number

否

否

表示骨骼点的总体置信度,取值范围是(0,1)，0表示置信度最低，1表示置信度最高。反映了这个骨骼整体的可信程度。

points

Array<[SkeletonPoint](#section674171818172)>

否

否

返回包含骨骼点详情的对象数组。

#### SkeletonDetectionResponse

用于表示一次骨骼点检测的完整结果。作为骨骼点检测的顶层输出，封装了一次检测的全部结果。继承自visionBase的[Response](VisionBase（Core Vision Kit基类）.md#section13793135121418)。

**系统能力：**SystemCapability.AI.Vision.SkeletonDetection

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

skeletons

Array<[Skeleton](#section49341529125412)>

否

否

包含图片内所有人的人体骨骼点结果集合。

#### SkeletonDetector

定义骨骼点检测的接口和基本结构。继承自[visionBase.Analyzer](VisionBase（Core Vision Kit基类）.md#section6867321337)类。它有以下功能函数：

- private constructor()：这是一个私有构造函数，意味着不能直接通过 new 关键字实例化SkeletonDetector。必须通过 create() 静态方法来创建实例。
- static create(): Promise<SkeletonDetector>：这是一个静态方法，用于创建SkeletonDetector的实例。使用Promise异步回调。它返回一个 Promise，解析为创建的SkeletonDetector实例。
- process(request: visionBase.Request): Promise<SkeletonDetectionResponse>：这是一个实例方法，用于处理骨骼点检测请求。使用Promise异步回调。
- destroy(): Promise<void>：这是一个实例方法，用于销毁骨骼点检测的进程，使用Promise异步回调。

**系统能力：**SystemCapability.AI.Vision.SkeletonDetection

**起始版本：**5.0.0(12)

名称

说明

constructor

强制开发者必须使用static create()方法来创建SkeletonDetector的实例。

create

初始化骨骼点检测接口。

process

骨骼点检测的实际执行接口。

destroy

骨骼点检测的销毁接口。

#### create

static create(): Promise<SkeletonDetector>

骨骼点检测的初始化接口。使用Promise异步回调。

**系统能力：**SystemCapability.AI.Vision.SkeletonDetection

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

Promise<[SkeletonDetector](#section1372216360530)>

Promise对象，返回[SkeletonDetector](#section1372216360530)实例。

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1011000001

Failed to run, please try again.

1011000002

The service is abnormal.

**示例：**

```ets
import { skeletonDetection } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function createAndDestroyDetector() {
  const detector = await skeletonDetection.SkeletonDetector.create();
  if (detector) {
    hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector created successfully');
  } else {
    hilog.error(0x0000,'skeletonDetectionSample','Failed to create Skeleton detector');
    return;
  }
  // 使用 detector 进行一些操作
  // ...

  // 完成后销毁 detector
  if (detector) {
    await detector.destroy();
    hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector destroyed successfully');
  } else {
    hilog.error(0x0000,'skeletonDetectionSample','Failed to destroy Skeleton detector');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('createAndDestroyDetector').onClick(() => {
        createAndDestroyDetector()
      })
    }
  }
}
```

#### destroy

destroy(): Promise<void>

销毁骨骼点检测能力。使用Promise异步回调。

**系统能力：**SystemCapability.AI.Vision.SkeletonDetection

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

Promise<void>

无返回结果的Promise对象。

**示例：**

```ets
import { skeletonDetection } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function createAndDestroyDetector() {
  const detector = await skeletonDetection.SkeletonDetector.create();
  if (detector) {
    hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector created successfully');
  } else {
    hilog.error(0x0000,'skeletonDetectionSample','Failed to create Skeleton detector');
    return;
  }
  // 使用 detector 进行一些操作
  // ...

  // 完成后销毁 detector
  if (detector) {
    await detector.destroy();
    hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector destroyed successfully');
  } else {
    hilog.error(0x0000,'skeletonDetectionSample','Failed to destroy Skeleton detector');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('createAndDestroyDetector').onClick(() => {
        createAndDestroyDetector()
      })
    }
  }
}
```

#### process

process(request: visionBase.Request): Promise<SkeletonDetectionResponse>

创建骨骼点检测实例并执行骨骼点检测。使用Promise异步回调。

**系统能力：**SystemCapability.AI.Vision.SkeletonDetection

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

request

visionBase.[Request](VisionBase（Core Vision Kit基类）.md#section6430105121211)

是

图片实例。骨骼点检测接口仅支持传入一张图片，不支持传入多张图片。

具体规格请参考[约束与限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-introduction#section625292610522)。

**返回值：**

类型

说明

Promise<[SkeletonDetectionResponse](#section1565918285820)>

返回骨骼点识别的结果。

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

The parameter check failed.

1011000001

Failed to run, please try again.

1011000003

Failed to run the model, please try again.

1011000004

**Running the model timed out. Try again later.

**示例：**

```ets
import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

let imageSource: image.ImageSource | undefined = undefined;
let chooseImage: image.PixelMap | undefined = undefined;

// 创建骨骼检测器
let detector: skeletonDetection.SkeletonDetector | undefined = undefined;

async function createDetector() {
  detector = await skeletonDetection.SkeletonDetector.create();
  hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector created successfully');
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Button').onClick(() => {
        // 将图片转换为PixelMap，可以通过图库获取
        let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
        photoPicker.select({
          MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
          maxSelectNumber: 1
        }).then((res: photoAccessHelper.PhotoSelectResult) => {
          let uri = res.photoUris[0];
          if (uri === undefined) {
            hilog.info(0x0000, 'skeletonDetectionSample', 'uri is undefined');
            return
          }
          setTimeout(async () => {
            let file = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
            imageSource = image.createImageSource(file.fd);
            chooseImage = await imageSource.createPixelMap();
            hilog.info(0x0000, 'skeletonDetectionSample', 'chooseImage:', chooseImage);
            if (!chooseImage) {
              return
            }

            // 创建检测器
            await createDetector();

            if (!detector) {
              hilog.error(0x0000, 'skeletonDetectionSample', 'Detector is not initialized');
              return;
            }

            // 调用骨骼检测接口
            let request: visionBase.Request = {
              inputData: { pixelMap: chooseImage },
              scene: visionBase.SceneMode.FOREGROUND
            };

            let response: skeletonDetection.SkeletonDetectionResponse = await detector.process(request);

            if (response.skeletons.length === 0) {
              hilog.info(0x0000, 'skeletonDetectionSample', 'No skeletons detected in the image.');
            } else {
              hilog.info(0x0000, 'skeletonDetectionSample', `Detected ${response.skeletons.length} skeletons.`);
              response.skeletons.forEach((skeleton, index) => {
                hilog.info(0x0000, 'skeletonDetectionSample', `  Score: ${skeleton.score}`);
                hilog.info(0x0000, 'skeletonDetectionSample', `  Number of points: ${skeleton.points.length}`);
                skeleton.points.forEach(point => {
                  hilog.info(0x0000, 'skeletonDetectionSample', `    ${skeletonDetection.SkeletonPointType[point.type]}: (${point.point.x}, ${point.point.y}), Score: ${point.score}`);
                });
              });
            }

            // 清理资源
            if (chooseImage && imageSource) {
              chooseImage.release();
              imageSource.release();
            }
            if (file) {
              try {
                await fileIo.close(file);
              } catch (err) {
                hilog.error(0x0000, 'skeletonDetectionSample', `Failed to close fileSource. Code: ${err.code}，message: ${err.message}`);
              }
            }
            if (detector) {
              await detector.destroy();
              hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector destroyed successfully');
            }
          }, 100);
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, 'skeletonDetectionSample', `Failed to get photo image uri. code: ${err.code}，message: ${err.message}`);
        });
      })
    }
  }
}
```