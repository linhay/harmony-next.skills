# arEngine（AR增强现实能力）

本模块提供AR Engine（AR引擎服务）的arEngine（AR增强现实能力）相关接口。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

#### 导入模块

```ets
import { arEngine } from '@kit.AREngine';
```

#### ARAddAugmentedImageMode

枚举，添加图片模式。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

NORMAL

0

正常模式。

当添加的图片数量超过默认的最多图片数量（50）时，AR Engine会报告错误，错误信息见[1009200011](../../errors/AR Engine错误码.md#section4676153191213)。

UPDATE

1

更新模式。

当添加的图片数量超过默认的最多图片数量（50）时，AR Engine会删除原有的最旧数据，以添加新的图片。

#### ARAddAugmentedImageReason

枚举，添加图像失败原因。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

NONE

0

无失败原因，图像成功添加。

SIZE_NOT_MATCH

1

图像尺寸不正确。

 说明：

图像尺寸评价从宽高比、分辨率两个维度进行。建议宽高比、分辨率的评价为Unfit以上。

LIGHT_ANOMALY

2

图像亮度过亮或过暗。

FEATURE_LIMIT

3

图像颜色单一，如纯色图片。

OTHER

4

其他原因，如图片有反光、光斑，重复性内容等。

- 宽高比： 图像宽度与高度之比，如：640*480分辨率的图像，其宽高比为1.33，对应评价Excellent。

图像宽高比

评价

[6, ∞)

Invalid

[4, 6)

Bad

[2.5, 4)

Unfit

[2, 2.5)

Fit

[1.5, 2)

Good

[1, 1.5)

Excellent

- 分辨率：

以640*480为基准，按比例计算。如：选取图像分辨率为320*240，以基准分辨率计算其比值为0.5，对应评价Fit。

图像分辨率比值

评价

[0, 0.2]

Invalid

(0.2, 0.3]

Bad

(0.35, 0.45]

Unfit

(0.45, 0.7]

Fit

(0.7, 0.9]

Good

(0.9, ∞)

Excellent

#### ARDepthMode

枚举，深度模式。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

DISABLED

0

关闭深度模式。

AUTOMATIC

1

开启深度模式。

AR Engine会自动尝试从多种深度源获取深度信息。

 说明：

通常有两种深度源，运动算法和硬件深度传感器 (Time of Flight，简称ToF)。

目前仅支持运动算法。

#### ARFocusMode

枚举，对焦模式。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

FIXED

0

固定焦点模式。

AUTO

1

自动对焦模式。

#### ARImageFormat

枚举，图像数据格式。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

UNKNOWN

0

无效的图像格式。

YUV_420_888

2

YUV_420_888格式，适用于处理高分辨率的图像数据。

Y_8

3

Y_8格式，适用于对图像数据要求较低的精度或存储空间的场景。

Y_16

4

Y_16格式，适用于对图像数据精度要求较高的场景。

#### ARMeshMode

枚举，网格模式。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

DISABLED

0

网格模式关闭。

AR Engine不会处理或显示网格数据。

ENABLE

1

网格模式开启。

AR Engine会尝试处理和显示网格数据。

#### ARPlaneFindingMode

枚举，平面检测模式。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

DISABLED

0

禁用平面检测。

HORIZONTAL

1

只检测水平面，如地板和桌子。

VERTICAL

2

只检测竖直平面，如墙壁。

HORIZONTAL_AND_VERTICAL

3

同时检测水平面和竖直平面。

#### ARPlaneType

枚举，平面类型。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

FACING_HORIZONTAL_UPWARD

0

朝上的水平面，如地面和桌面平台。

FACING_HORIZONTAL_DOWNWARD

1

朝下的水平面，如天花板。

FACING_VERTICAL

2

垂直的水平面，如墙壁。

FACING_INVALID

3

无效或不支持的平面类型。

这可能是由于环境变化、光线条件或其他因素导致。

#### ARPointOrientationMode

枚举，朝向模式。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

INITIALIZED_TO_IDENTITY

0

与世界坐标系的朝向一致，但会稍作调整。

ESTIMATED_SURFACE_NORMAL

1

朝向由估计的平面法向量决定。

点的方向将与平面的方向一致，适用于需要根据平面特征来确定点方向的应用场景。

#### ARPoseMode

枚举，创建世界坐标系的方式。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

GRAVITY

0

由重力确定。

世界坐标系的Y轴与重力方向一致，原点为设备所在的原始位置。参见[AR Engine重力对齐世界坐标系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-coordinate#section51232054151614)。

GRAVITY_AND_HEADING

1

由重力和指南针确定。

世界坐标系的Y轴与重力方向一致，X轴指向指南针北向，原点为设备所在的原始位置。参见[AR Engine重力对齐北向坐标系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-coordinate#section1786771621711)。

 注意：

该选项当前仅支持省电模式，请将[ARPowerMode](#section9223439153519)置为POWER_SAVING以启动该选项。

#### ARPoseType

枚举，位姿类型。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

IDENTITY

0

默认状态，即没有任何旋转或平移。

ROTATE_90

1

顺时针旋转90度。

ROTATE_180

2

顺时针旋转180度。

ROTATE_270

3

顺时针旋转270度。

#### ARPowerMode

枚举，电源功耗模式。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

NORMAL

0

正常模式。

AR Engine在性能和电源消耗之间保持平衡。

POWER_SAVING

1

节能模式。

AR Engine优先减少电源消耗。这可能会降低一些性能，以换取更长的电池寿命。

PERFORMANCE_FIRST

2

性能优先模式。

AR Engine优先考虑性能，提供更高的处理能力和更快的响应时间。这可能会增加电源消耗。

BOOST

3

仅输出设备姿态信息模式。

AR Engine仅输出设备的位姿信息，电源消耗低于正常模式。在此模式下，[ARPlaneFindingMode](#section764515681310)等与平面相关的设置不起作用。

ULTRA_POWER_SAVING

11

超级节能模式。

AR Engine进一步优化电源消耗，提供比节能模式更低的电源消耗，这可能会损失更多的性能。

#### ARSemanticDenseMode

枚举，高精几何重建识别模式。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**6.0.0(20)

**名称**

**值**

**说明**

DISABLED

0

关闭高精几何重建识别模式。

NORMAL

1

正常模式，仅开启稠密点云识别。

CUBE_VOLUME

2

基于高精几何重建的立方体体积测量模式。

CUBE_SPACE

3

基于高精几何重建的立方体空间容积测量模式。

#### ARSemanticMode

枚举，语义模式。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

NONE

0

不使用语义。

PLANE

1

使用平面语义模式。

#### ARSemanticPlaneLabel

枚举，当前平面识别到的语义类型。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

UNKNOWN

0

未知平面类型。

WALL

1

墙面。

FLOOR

2

地面。

SEAT

3

座位，如椅子或凳子。

TABLE

4

桌子。

CEILING

5

天花板。

DOOR

6

门。

WINDOW

7

窗户。

BED

8

床。

PLANE_SPACE

9

平面空间。

**起始版本：**6.0.0(20)

CUBE_VOLUME

10

立方体体积。

**起始版本：**6.0.0(20)

CUBE_SPACE

11

立方体空间容积。

**起始版本：**6.0.0(20)

#### ARTrackingState

枚举，可追踪对象的追踪状态。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

TRACKING

0

正在追踪。

PAUSED

1

暂停追踪。

STOPPED

2

停止追踪。

#### ARTrackingStateReason

枚举，追踪失败的原因。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

NONE

0

未知原因。

这可能是由于系统暂时无法识别可追踪对象，但仍在尝试追踪。

EXCESSIVE_MOTION

1

目标移动过快。

可追踪对象（如平面、点、图像等）移动速度过快，导致AR Engine无法准确识别和跟踪。

INSUFFICIENT_FEATURES

2

视觉特征不足。

可追踪对象的视觉特征不够丰富，如纹理不明显、颜色过于单一等，导致AR Engine无法准确识别和跟踪。

#### ARTrackableType

枚举，可追踪对象类型，如平面、点等。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

BASE

0x41520100

基本的可追踪对象类型，AR Engine默认类型。

PLANE

0x41520101

平面类型的可追踪对象。

POINT

0x41520102

点类型的可追踪对象。

AUGMENTED_IMAGE

0x41520104

增强型图像类型的可追踪对象。

INVALID

0

无效的可追踪对象类型。

#### ARType

枚举，AR能力类型。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**名称**

**值**

**说明**

WORLD

0x01

环境追踪能力。

IMAGE

0x80

图像识别能力。

#### Distortion

type Distortion = [number, number, number, number, number]

类型别名，用于表示一个包含五个数字的数组，为相机的畸变系数。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

类型

说明

number

表示值类型为数字，相机内参，取值范围无限制。

其中Distortion [0]~Distortion [2]表示k1，k2，k3（径向畸变系数），Distortion [3]~Distortion [4]是切向畸变系数。

#### ARAugmentedImageDatabase

增强图像数据库对象。

用于表示增强图像数据库的相关操作，如序列化、反序列化、添加图像、获取图像数量等。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

#### ARAugmentedImageDatabase.deserialize

deserialize(buffer: ArrayBuffer): Promise<void>

将增强图像数据库数据反序列化为一个新的增强图像数据库对象。

使用Promise异步回调。

这个操作是耗时的，建议在后台线程中运行。

**系统能力：**SystemCapability.AREngine.Core

**起始版本****：**5.1.0(18)

**参数：**

参数名

类型

必填

说明

buffer

ArrayBuffer

是

增强图像数据库的ArrayBuffer数据。

**返回值：**

**类型**

**说明**

Promise<void>

无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

401

Invalid parameters, for example, the input parameter is empty or invalid.

1009200001

Failure.

1009200008

Resource exhausted.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function deserialize(): Promise<void> {
  let buffer: ArrayBuffer = new ArrayBuffer(0);
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  await imageDatabase.deserialize(buffer);
}
```

#### ARAugmentedImageDatabase.serialize

serialize(): Promise<ArrayBuffer>

将增强图像数据库数据序列化为一个缓冲区。

使用Promise异步回调返回ArrayBuffer对象。

**系统能力：**SystemCapability.AREngine.Core

**起始版本****：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<ArrayBuffer>

Promise对象，返回ArrayBuffer对象。

ArrayBuffer是一个缓冲区，这个缓冲区包含了增强图像数据库的序列化数据。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function serialize(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  let buffer: ArrayBuffer = await imageDatabase.serialize();
}
```

#### ARAugmentedImageDatabase.addImage

addImage(name: string, pixelMap: image.PixelMap, widthInMeters: number): Promise<ARAddAugmentedImageResult>

将图像添加到图像数据库，并输出对应图像的索引。

使用Promise异步回调返回ARAddAugmentedImageResult对象。

**系统能力：**SystemCapability.AREngine.Core

**起始版本****：**5.1.0(18)

**参数：**

参数名

类型

必填

说明

name

string

是

图像名称。

不允许为空，255个字符以内，超过255个的字符将会被丢弃。

pixelMap

[image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendableimage#pixelmap)

是

图像的信息。

widthInMeters

number

是

图像中对象的实际物理宽度。

无限制，单位为m。默认值是A4纸张的大小。

**返回值：**

**类型**

**说明**

Promise<[ARAddAugmentedImageResult](#section67121231105218)>

Promise对象，返回ARAddAugmentedImageResult对象。

ARAddAugmentedImageResult是一个表示添加增强图像结果的数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

401

Invalid parameters, for example, the input parameter is empty or invalid.

1009200001

Failure.

1009200008

Resource exhausted.

1009200011

The number of images added exceeds the maximum.

1009200012

Attempted to add an image with insufficient quality to the image database.

**示例：**

```ets
import { image } from '@kit.ImageKit';
import { arEngine } from '@kit.AREngine';

async function addImage(): Promise<void> {
  let color: ArrayBuffer = new ArrayBuffer(96); // 96为需要创建的像素buffer大小，取值为：height * width *4
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: image.PixelMapFormat.RGBA_8888,
    size: { height: 4, width: 6 }
  }
  let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  let addImageResult: arEngine.ARAddAugmentedImageResult = await imageDatabase.addImage('xx', pixelMap, 0.3);
}
```

#### ARAugmentedImageDatabase.getImageCount

getImageCount(): number

获取图像数据库中图像的数量。

**系统能力：**SystemCapability.AREngine.Core

**起始版本****：**5.1.0(18)

**返回值：**

**类型**

**说明**

number

返回图像的数量。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function getImageCount(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  let imageCount: number = imageDatabase.getImageCount();
}
```

#### ARAugmentedImageDatabase.getCapacity

getCapacity(): number

获取可添加的最大图像数量。

**系统能力：**SystemCapability.AREngine.Core

**起始版本****：**5.1.0(18)

**返回值：**

**类型**

**说明**

number

返回可添加图像的最大数量。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function getCapacity(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  let imageCapacity: number = imageDatabase.getCapacity();
}
```

#### ARAugmentedImageDatabase.getImageAddMode

getImageAddMode(): ARAddAugmentedImageMode

获取图片添加模式。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARAddAugmentedImageMode](#section913918490464)

返回图片的添加模式。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function getImageAddMode(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  let addImageMode: arEngine.ARAddAugmentedImageMode = imageDatabase.getImageAddMode();
}
```

#### ARAugmentedImageDatabase.setImageAddMode

setImageAddMode(mode: ARAddAugmentedImageMode): void

设置图片添加模式。

**系统能力：**SystemCapability.AREngine.Core

**起始版本****：**5.1.0(18)

**参数：**

参数名

类型

必填

说明

mode

[ARAddAugmentedImageMode](#section913918490464)

是

添加图片模式。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function setImageAddMode(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  imageDatabase.setImageAddMode(arEngine.ARAddAugmentedImageMode.UPDATE);
}
```

#### ARAugmentedImageDatabase.release

release(): Promise<void>

释放增强图像数据库对象[ARAugmentedImageDatabase](#section1410345414514)占用的内存。

使用Promise异步回调。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<void>

无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
  await imageDatabase.release();
}
```

#### ARCameraIntrinsics

相机内参。

包括fx、fy、cx、cy和畸变参数。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

fx

number

是

否

相机在x轴上的焦距。

可取任意值。

fy

number

是

否

相机在y轴上的焦距。

可取任意值。

cx

number

是

否

相机在x轴上的主点。

可取任意值。

cy

number

是

否

相机在y轴上的主点。

可取任意值。

distortion

[Distortion](#section4381141123516)

是

否

相机畸变参数。

#### ARConfig

[ARSession](#section19193165314510)的功能配置参数。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

type

[ARType](#section1712356171319)

否

否

AR能力类型。

planeFindingMode

[ARPlaneFindingMode](#section764515681310)

否

是

平面检测模式。

默认为HORIZONTAL_AND_VERTICAL。

powerMode

[ARPowerMode](#section9223439153519)

否

是

电源功耗模式。

默认为NORMAL。

focusMode

[ARFocusMode](#section6848111619409)

否

是

对焦模式.

默认为FIXED。

semanticMode

[ARSemanticMode](#section19325205718138)

否

是

语义模式.

默认为NONE。

maxMapSize

number

否

是

存储地图数据的最大内存大小，单位为MB。可设定范围100MB~16GB，默认800MB。

建议根据设备的内存容量设置内存大小。超出硬件限制可能会导致意外错误。

poseMode

[ARPoseMode](#section342619402359)

否

是

创建世界坐标系的方式。

默认为GRAVITY。

depthMode

[ARDepthMode](#section947895524619)

否

是

深度模式。

默认为DISABLED。

meshMode

[ARMeshMode](#section111790505464)

否

是

网格模式。

默认为DISABLED。

addAugmentedImageMode

[ARAddAugmentedImageMode](#section913918490464)

否

是

添加图片模式。

默认为NORMAL。

semanticDenseMode

[ARSemanticDenseMode](#section162053411246)

否

是

高精几何重建识别模式。

默认DISABLED。

**起始版本：**6.0.0(20)

#### ARPointCloud

可跟踪的3D点云集合。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

timestamp

number

是

否

当前特征点云检测时的时间戳。

以ns为单位。

points

Array<number>

是

否

表示点云中所有点的坐标以及坐标对应的置信度数组。

#### ARSemanticDenseCubeData

高精几何重建对象的立方体数据。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

id

number

是

否

当前立方体的ID。

vertexSize

number

是

否

当前立方体的顶点数量。

vertexData

Array<number>

是

否

当前立方体的顶点数据。

对应立方体的8个顶点。索引从立方体后表面开始，按逆时针方向排列。

confidence

number

是

否

当前立方体的置信度。取值为0，1，2。

label

[ARSemanticPlaneLabel](#section5137195514137)

是

否

当前立方体的语义标签。

#### ARSemanticDensePointData

高精几何重建对象的稠密点云数据。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

id

ArrayBuffer

是

否

稠密点云数据所有点的id数组。

 说明：

该类型在使用时，如需转换则为int32类型，转换方法参考[数据类型转换说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arraybuffer-info)。

position

ArrayBuffer

是

否

稠密点云数据所有点的坐标，以及它们的置信度数组，格式为[x0, y0, z0, c0, x1, y1, z1, c1, x2, ...]。

 说明：

该类型在使用时，如需转换则为float32类型，转换方法参考[数据类型转换说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arraybuffer-info)。

color

ArrayBuffer

是

否

稠密点云数据所有点的颜色，以 rgba 格式表示，格式为 [r0, g0, b0, a0, r1, g1, b1, a1, r2,...]。

 说明：

该类型在使用时，如需转换则为int32类型，转换方法参考[数据类型转换说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arraybuffer-info)。

#### ARSession

管理AR Engine的系统状态。

**系统能力：**SystemCapability.AREngine.Core

**起始版本****：**5.1.0(18)

#### ARSession.getFrame

getFrame(): ARFrame

获取AR Engine处理后的一帧数据。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARFrame](#section83421523123819)

返回AR Engine处理后的一帧数据。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D';

class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session) {
      // 如果没有创建session则退出，关于如何创建session请参考开发指南
      return;
    }

    let arSession: arEngine.ARSession = ctx.session;
    let frame: arEngine.ARFrame = arSession.getFrame();
    await frame.release();
  }
}
```

#### ARSession.createAnchor

createAnchor(pose: ARPose): ARAnchor

创建一个用于连续跟踪的锚点。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数：**

**参数名**

**类型**

必填

**说明**

pose

[ARPose](#section19274193834913)

是

用于创建锚点的位姿对象。

**返回值：**

**类型**

**说明**

[ARAnchor](#section106411242143016)

返回一个锚点对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

401

Invalid parameters, for example, the input parameter is empty or invalid.

1009200001

Failure.

**示例：**

```ets
import { Quaternion, Vec3 } from '@kit.ArkGraphics3D';
import { arEngine } from '@kit.AREngine';

let r: Quaternion = {
  x: 0,
  y: 0,
  z: 0,
  w: 0
}
let t: Vec3 = { x: 0, y: 0, z: 0 };
let pose: arEngine.ARPose = arEngine.createARPose(r, t);
// arSession创建参考ARSession.getFrame接口示例代码
let anchor: arEngine.ARAnchor= arSession.createAnchor(pose);
```

#### ARSession.detachAnchor

detachAnchor(anchor: ARAnchor): void

停止追踪并解绑锚点。

由于此函数并没有释放锚点[ARAnchor](#section106411242143016)，开发者需要通过调用[ARAnchor.release](#section63641154194411)来释放锚点。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数：**

**参数名**

**类型**

必填

**说明**

anchor

[ARAnchor](#section106411242143016)

是

要解绑的锚点对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

401

Invalid parameters, for example, the input parameter is empty or invalid.

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let pose: arEngine.ARPose = arSession.getFrame().getCamera().getPose();
let anchor: arEngine.ARAnchor = arSession.createAnchor(pose);
arSession.detachAnchor(anchor);
```

#### ARSession.getAllAnchors

getAllAnchors(): Array<ARAnchor>

获取所有状态的锚点。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Array<[ARAnchor](#section106411242143016)>

返回一个锚点对象组成的数组。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

1009200008

Resource exhausted.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let anchors: Array<arEngine.ARAnchor> = arSession.getAllAnchors();
```

#### ARSession.getAllTrackables

getAllTrackables(type: ARTrackableType): Array<ARTrackable>

获取指定类型的所有可追踪对象。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数：**

**参数名**

**类型**

必填

**说明**

type

[ARTrackableType](#section1725585684613)

是

可追踪对象的类型。

**返回值：**

**类型**

**说明**

Array<[ARTrackable](#section1710323720204)>

返回一个可追踪对象组成的数组。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

401

Invalid parameters, for example, the input parameter is empty or invalid.

1009200001

Failure.

1009200008

Resource exhausted.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let allTrackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
```

#### ARSession.openFlash

openFlash(): Promise<boolean>

打开设备的闪光灯。

使用Promise异步回调返回开启结果。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<boolean>

Promise对象，返回true表示设备的闪光灯已开启，返回false表示设备闪光灯未开启。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function openFlash(): Promise<void> {
  // arSession创建参考ARSession.getFrame接口示例代码
  let result: boolean = await arSession.openFlash();
}
```

#### ARSession.closeFlash

closeFlash(): Promise<boolean>

关闭设备的闪光灯。

使用Promise异步回调返回关闭结果。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<boolean>

Promise对象，返回true表示设备的闪光灯已关闭，返回false表示设备闪光灯未关闭。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function closeFlash(): Promise<void> {
  // arSession创建参考ARSession.getFrame接口示例代码
  let result: boolean = await arSession.closeFlash();
}
```

#### ARSession.release

release(): Promise<void>

释放管理AR Engine系统状态对象[ARSession](#section19193165314510)占用的内存。

使用Promise异步回调。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<void>

无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  // arSession创建参考ARSession.getFrame接口示例代码
  await arSession.release();
}
```

#### ImageComponent

图像组件的基本结构参数。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

rowStride

number

是

否

图像中两个连续像素行起始位置之间的字节数。行间距始终大于0。

pixelStride

number

是

否

图像中两个连续像素起始点之间的字节数。像素间距始终大于0。

buffer

ArrayBuffer

是

否

当前帧的平面数据缓冲区对象。

 说明：

该类型在使用时，如需转换则为int32类型，转换方法参考[数据类型转换说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arraybuffer-info)。

#### ARAddAugmentedImageResult

添加增强图像的结果。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

index

number

否

否

图像唯一索引，取值范围0~49。

state

number

否

否

添加增强图像的结果状态。成功为0，否则为对应错误码。

stateReason

[ARAddAugmentedImageReason](#section7453144131020)

否

否

添加图像失败的原因。

#### ARAnchor

锚点对象。

锚点描述与可追踪对象相关联的空间位置。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数：**

名称

类型

只读

可选

说明

id

number

是

否

锚点的索引，取值范围0~49。

trackingState

[ARTrackingState](#section16656547114620)

是

否

可追踪对象的追踪状态。

#### ARAnchor.getPose

getPose(): ARPose

获取锚点在世界坐标系中的位姿信息。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARPose](#section19274193834913)

返回位姿对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let anchors: Array<arEngine.ARAnchor> = arSession.getAllAnchors();
let pose: arEngine.ARPose = anchors[0].getPose();
```

#### ARAnchor.detach

detach(): void

停止追踪并解绑锚点。

这个函数不会释放锚点，开发者需要通过调用[ARAnchor.release](#section63641154194411)方法来释放锚点。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let anchors: Array<arEngine.ARAnchor> = arSession.getAllAnchors();
anchors[0].detach();
```

#### ARAnchor.release

release(): Promise<void>

释放锚点对象[ARAnchor](#section106411242143016)占用的内存。

使用Promise异步回调。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<void>

无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  // arSession创建参考ARSession.getFrame接口示例代码
  let anchors: Array<arEngine.ARAnchor> = arSession.getAllAnchors();
  await anchors[0].release();
}
```

#### ARAugmentedImage

增强图像对象。

这个类继承自[ARTrackable](#section1710323720204)类。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

extendX

number

是

否

表示在X轴上估计的物理图像宽度，单位为m。如果图像的追踪状态为PAUSED或STOPPED，返回的宽度信息是最后一次追踪的宽度。如果图像从未被追踪，返回0。

extendZ

number

是

否

表示在Z轴上估计的物理图像宽度，单位为m。如果图像的追踪状态为PAUSED或STOPPED，返回的宽度信息是最后一次追踪的宽度。如果图像从未被追踪，返回0。

index

number

是

否

表示增强图像在增强图像数据库中的图像索引，数值范围1~50，为图像在数据库中的唯一标识符。

name

string

是

否

表示增强图像的图像名称，最大为255Byte，该值可能不唯一。

#### ARCamera

当前帧的摄像机信息。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数：**

名称

类型

只读

可选

说明

state

[ARTrackingState](#section16656547114620)

是

否

可追踪对象的追踪状态。

stateReason

[ARTrackingStateReason](#section93821938193519)

是

否

追踪失败的原因。

viewMatrix

[Matrix4](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#matrix4)

是

否

摄像机在最新帧中的视图矩阵。

#### ARCamera.getPose

getPose(): ARPose

获取摄像机在世界空间中的位姿。

位姿信息可参考[坐标系说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-coordinate)。

位姿信息仅在状态返回TRACKING时才可使用。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARPose](#section19274193834913)

返回一个位姿对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let camera: arEngine.ARCamera = frame.getCamera();
let cameraPose: arEngine.ARPose = camera.getPose();
```

#### ARCamera.getDisplayOrientedPose

getDisplayOrientedPose(): ARPose

获取面向显示屏的虚拟摄像机在世界空间中的位姿。

位姿信息可参考[坐标系说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-coordinate)。

位姿信息仅在状态返回TRACKING时才可使用。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARPose](arEngine（AR增强现实能力）.md#section19274193834913)

返回一个位姿对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let camera: arEngine.ARCamera = frame.getCamera();
let displayOrientedPose: arEngine.ARPose = camera.getDisplayOrientedPose();
```

#### ARCamera.getProjectionMatrix

getProjectionMatrix(near: number, far: number): Matrix4

获取用于在相机图像上渲染虚拟内容的投影矩阵。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数：**

**参数名**

**类型**

必填

**说明**

near

number

是

相机坐标系统中的近裁剪平面的距离，单位为m，值必须大于0。

far

number

是

相机坐标系统中的远裁剪平面的距离，单位为m，值必须大于0且大于near。

**返回值：**

**类型**

**说明**

[Matrix4](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#matrix4)

返回一个Matrix4对象。

Matrix4是一个包含16个浮点数的数组，表示OpenGL中的列主旋转变换矩阵。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

401

Invalid parameters, for example, the input parameter is empty or invalid.

1009200001

Failure.

**示例：**

```ets
import { Matrix4 } from '@kit.ArkUI';
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let camera: arEngine.ARCamera = frame.getCamera();
let matrix: Matrix4 = camera.getProjectionMatrix(0, 1);
```

#### ARCamera.getImageIntrinsics

getImageIntrinsics(): ARCameraIntrinsics

获取离线相机的内参对象。

该对象可用于获取相机的焦距、图像尺寸、主点和畸变参数。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARCameraIntrinsics](#section1472734105519)

返回一个相机内参对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let camera: arEngine.ARCamera = frame.getCamera();
let imageIntrinsics: arEngine.ARCameraIntrinsics = camera.getImageIntrinsics();
```

#### ARFrame

AR Engine处理的一帧数据。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

timestamp

number

是

否

表示当前帧的时间戳。

以ns为单位。

pointCloud

[ARPointCloud](#section1941316821)

是

否

表示当前帧中可追踪的3D点云集合。

#### ARFrame.getCamera

getCamera(): ARCamera

获取当前帧的相机对象。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARCamera](#section176984261612)

返回当前帧的相机对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let camera: arEngine.ARCamera = frame.getCamera();

```

#### ARFrame.getUpdatedTrackables

getUpdatedTrackables(type: ARTrackableType): Array<ARTrackable>

获取更新后的指定类型的可追踪对象。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数：**

**参数名**

**类型**

必填

**说明**

type

[ARTrackableType](#section1725585684613)

是

可追踪对象类型。

**返回值：**

**类型**

**说明**

Array<[ARTrackable](#section1710323720204)>

返回一个可追踪对象组成的数组。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

401

Invalid parameters, for example, the input parameter is empty or invalid.

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let trackables: arEngine.ARTrackable[] = frame.getUpdatedTrackables(arEngine.ARTrackableType.BASE);
```

#### ARFrame.hitTest

hitTest(x: number, y: number): Array<ARHitResult>

根据相机投射光线，获取预览区域中的像素坐标（pixelX和pixelY）来确定射线方向，然后检测这个射线在平面、Mesh或点云中是否有交点。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数：**

**参数名**

**类型**

必填

**说明**

x

number

是

表示预览区域中的像素的X坐标。

该值由设备显示分辨率大小确定。

y

number

是

表示预览区域中的像素的Y坐标。

该值由设备显示分辨率大小确定。

**返回值：**

**类型**

**说明**

Array<[ARHitResult](#section14725141314593)>

返回一个命中检测结果对象组成的数组。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

401

Invalid parameters, for example, the input parameter is empty or invalid.

1009200001

Failure.

1009200008

Resource exhausted.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let hitResult: arEngine.ARHitResult[] = frame.hitTest(0, 0);
```

#### ARFrame.acquireSceneMesh

acquireSceneMesh(): ARSceneMesh

获取当前帧的场景网格数据。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARSceneMesh](#section81184417712)

返回环境网格数据的集合。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

1009200008

Resource exhausted.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();
```

#### ARFrame.acquireDepthImage16Bits

acquireDepthImage16Bits(): ARImage

获取当前帧对应的深度图像对象。

深度图像是索引0处的单个16位平面。每个像素包含到相机平面的距离，以mm为单位，可表示的深度范围在0mm~65535mm之间，即约65m。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARImage](#section3211104815419)

返回相机视频流帧对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let arImage: arEngine.ARImage = frame.acquireDepthImage16Bits();
```

#### ARFrame.acquireDepthConfidenceImage

acquireDepthConfidenceImage(): ARImage

获取当前帧的深度置信度图像。

置信度值为0、1和2，0表示估计深度值的置信度最低，1表示估计深度值置信度中等，2表示估计深度值置信度最高，深度置信度图像的宽高与深度图像一致。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARImage](#section3211104815419)

返回相机视频流帧对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let depthConfidenceImage: arEngine.ARImage = frame.acquireDepthConfidenceImage();
```

#### ARFrame.acquireSemanticDense

acquireSemanticDense(): ARSemanticDenseData

获取高精几何重建对象数据。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**6.0.0(20)

**返回值：**

**类型**

**说明**

[ARSemanticDenseData](#section137161158185414)

返回当前帧的高精几何重建对象数据。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let semanticData: arEngine.ARSemanticDenseData = frame.acquireSemanticDense();
```

#### ARFrame.release

release(): Promise<void>

释放帧数据对象[ARFrame](#section83421523123819)占用的内存。

使用Promise异步回调。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<void>

无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  // arSession创建参考ARSession.getFrame接口示例代码
  let frame: arEngine.ARFrame = arSession.getFrame();
  await frame.release();
}
```

#### ARHitResult

命中检测结果对象，描述单个可跟踪对象的命中检测结果。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数：**

名称

类型

只读

可选

说明

distance

number

是

否

从相机到命中位置的距离，单位为m，其值范围0~65535。

#### ARHitResult.getHitPose

getHitPose(): ARPose

获取交点位姿。

位姿信息可参考[坐标系说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-coordinate)。

如果[ARPointOrientationMode](#section188141239153515)是ESTIMATED_SURFACE_NORMAL，则 X+ 是射线的垂直向量，也就是平面的平行向量，Y+ 是平面的法向量，Z+ 是平面的平行向量，大致指向相机。

如果[ARPointOrientationMode](#section188141239153515)是INITIALIZED_TO_IDENTITY，则坐标的旋转不会随着平面的角度变化而变化。X+ 是射线的垂直向量，指向右侧（从设备的视角），Y+ 指向上方，Z+ 大致指向相机。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARPose](#section19274193834913)

返回一个位姿对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let hitResult: Array<arEngine.ARHitResult> = frame.hitTest(0, 0);
let hitPose: arEngine.ARPose = hitResult[0].getHitPose();
```

#### ARHitResult.getTrackable

getTrackable(): ARTrackable

获取被命中的可追踪对象。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARTrackable](#section1710323720204)

返回可被追踪的对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let hitResult: Array<arEngine.ARHitResult> = frame.hitTest(0, 0);
let trackable: arEngine.ARTrackable = hitResult[0].getTrackable();
```

#### ARHitResult.createAnchor

createAnchor(): ARAnchor

在交点（intersection）处创建一个锚点。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARAnchor](#section106411242143016)

返回一个锚点对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let hitResult: Array<arEngine.ARHitResult> = frame.hitTest(0, 0);
let anchor: arEngine.ARAnchor = hitResult[0].createAnchor();
```

#### ARHitResult.release

release(): Promise<void>

释放命中检测结果对象[ARHitResult](#section14725141314593)占用的内存。

使用Promise异步回调。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<void>

无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let hitResult: Array<arEngine.ARHitResult> = frame.hitTest(0, 0);
hitResult[0].release();
```

#### ARImage

相机视频流帧对象。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

format

[ARImageFormat](#section183476224713)

是

否

图像数据格式。

width

number

是

否

当前帧的图像宽度，以像素为单位。其数值范围与设备相机像素有关。

height

number

是

否

当前帧的图像高度，以像素为单位。其数值范围与设备相机像素有关。

imageTimestamp

number

是

否

图像的时间戳，以ns为单位。

planes

Array<[ImageComponent](#section175993235012)>

是

否

图像组件的基本结构参数列表。

#### ARImage.release

release(): Promise<void>

释放相机视频流帧对象[ARImage](#section3211104815419)占用的内存。

使用Promise异步回调。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<void>

无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  // arSession创建参考ARSession.getFrame接口示例代码
  let frame: arEngine.ARFrame = arSession.getFrame();
  let image: arEngine.ARImage = frame.acquireDepthImage16Bits();
  await image.release();
}
```

#### ARPlane

平面对象，描述被检测到的可跟踪平面信息。

这个类继承自[ARTrackable](#section1710323720204)类。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

planeType

[ARPlaneType](#section766818120479)

否

否

平面类型。

extendX

number

否

否

平面边界矩形沿平面局部坐标系X轴的长度，以m为单位，数值范围无限制。

extendZ

number

否

否

平面边界矩形沿平面局部坐标系Z轴的长度，以m为单位，数值范围无限制。

label

[ARSemanticPlaneLabel](#section5137195514137)

否

否

当前平面识别到的语义类型。

#### ARPlane.getPolygonXZ

getPolygonXZ(): ArrayBuffer

获取检测到的平面2D顶点数组。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

ArrayBuffer

返回一个ArrayBuffer缓冲区对象，这个对象包含顶点坐标的数组。表示平面局部坐标系X-Z平面的坐标。

 说明：

该类型在使用时，如需转换则为float32类型，转换方法参考[数据类型转换说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arraybuffer-info)。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
let plane = trackables[0] as arEngine.ARPlane;
let buffer: ArrayBuffer = plane.getPolygonXZ();
```

#### ARPlane.getSubsumedBy

getSubsumedBy(): ARPlane

获取平面的父平面（当平面与另一个平面合并时会生成父平面）。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARPlane](#section3392194311417)

返回一个平面对象，表示父平面。如果没有父平面，将返回undefined。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
let plane = trackables[0] as arEngine.ARPlane;
let subsumedPlane: arEngine.ARPlane = plane.getSubsumedBy();
```

#### ARPlane.isPoseInExtents

isPoseInExtents(pose: ARPose): boolean

检查给定位姿是否在平面的边界矩形内。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数**：

**参数名**

**类型**

必填

**说明**

pose

[ARPose](#section19274193834913)

是

位姿对象。

**返回值：**

**类型**

**说明**

boolean

返回true表示位姿在平面的边界矩形内，false表示位姿不在平面的边界矩形内。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

401

Invalid parameters, for example, the input parameter is empty or invalid.

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
let pose: arEngine.ARPose = trackables[0].getPose();
let plane = trackables[0] as arEngine.ARPlane;
let result: boolean = plane.isPoseInExtents(pose);
```

#### ARPlane.isPoseInPolygon

isPoseInPolygon(pose: ARPose): boolean

检查给定位姿是否在平面的边界多边形内。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数**：

**参数名**

**类型**

必填

**说明**

pose

[ARPose](#section19274193834913)

是

位姿对象。

**返回值：**

**类型**

**说明**

boolean

返回true表示位姿在平面的边界多边形内，false表示位姿不在平面的边界多边形内。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

401

Invalid parameters, for example, the input parameter is empty or invalid.

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
let pose: arEngine.ARPose = trackables[0].getPose();
let plane = trackables[0] as arEngine.ARPlane;
let result: boolean = plane.isPoseInPolygon(pose);
```

#### ARPlaneAnchor

一个平面类型的锚点对象。

这个类继承自[ARAnchor](#section106411242143016)类。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

#### ARPlaneAnchor.getPlane

getPlane(): ARPlane

获取平面。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARPlane](#section3392194311417)

返回平面对象，描述被检测到的可跟踪平面信息。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node } from '@kit.ArkGraphics3D';
// 该方法在ARViewCallback中使用
onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  let planeAnchor: arEngine.ARPlaneAnchor = anchor as arEngine.ARPlaneAnchor;
  let plane: arEngine.ARPlane = planeAnchor.getPlane();
  plane.release();
}
```

#### ARPoint

可被追踪的3D点云对象。

这个类继承自[ARTrackable](#section1710323720204)类。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

orientationMode

[ARPointOrientationMode](#section188141239153515)

是

否

朝向模式。

#### ARPose

位姿对象。

代表从一个坐标系到另一个坐标系的不可改变刚性变换，如平移或旋转。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

rotation

[Quaternion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-types#quaternion)

是

否

来自位姿对象的姿势数据，包括旋转分量。

translation

[Vec3](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-types#vec3)

是

否

来自位姿对象的姿势数据，包括平移组件。

#### ARPose.getMatrix

getMatrix(): Matrix4

将位姿数据转换为一个4x4的矩阵。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[Matrix4](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#matrix4)

返回一个包含16个浮点数的数组，按照列主序（column-major order）存储。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { Matrix4 } from '@kit.ArkUI';
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let camera: arEngine.ARCamera = frame.getCamera();
let pose: arEngine.ARPose = camera.getPose();
let matrix: Matrix4 = pose.getMatrix();
```

#### ARPose.release

release(): Promise<void>

释放位姿对象[ARPose](#section19274193834913)占用的内存。

使用Promise异步回调。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<void>

无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  // arSession创建参考ARSession.getFrame接口示例代码
  let frame: arEngine.ARFrame = arSession.getFrame();
  let camera: arEngine.ARCamera = frame.getCamera();
  let pose: arEngine.ARPose = camera.getPose();
  await pose.release();
}
```

#### ARSceneMesh

环境网格数据集合。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

verticesSize

number

是

否

场景网格中的顶点数量。

最小为0，无上限。

triangleIndicesSize

number

是

否

场景网格中的三角形索引数量。最小为0，无上限。

#### ARSceneMesh.getVertices

getVertices(): ArrayBuffer

获取场景网格中的顶点坐标数据。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

ArrayBuffer

返回一个ArrayBuffer缓冲区对象。这个缓冲区包含了顶点在平面局部坐标系X-Z平面的坐标。

 说明：

该类型在使用时，如需转换则为float32类型，转换方法参考[数据类型转换说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arraybuffer-info)。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();
let buffer: ArrayBuffer = sceneMesh.getVertices();
```

#### ARSceneMesh.getVertexNormals

getVertexNormals(): ArrayBuffer

获取场景网格中的顶点法线坐标数据。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

ArrayBuffer

返回一个ArrayBuffer缓冲区对象。这个缓冲区包含了顶点在平面局部坐标系X-Z平面的坐标。

 说明：

该类型在使用时，如需转换则为float32类型，转换方法参考[数据类型转换说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arraybuffer-info)。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();
let buffer: ArrayBuffer = sceneMesh.getVertexNormals();
```

#### ARSceneMesh.getTriangleIndices

getTriangleIndices(): ArrayBuffer

获取场景网格中的三角形索引数据。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

ArrayBuffer

返回一个ArrayBuffer缓冲区对象。这个缓冲区包含了顶点在平面局部坐标系X-Z平面的坐标。

 说明：

该类型在使用时，如需转换则为int32类型，转换方法参考[数据类型转换说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arraybuffer-info)。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();
let buffer: ArrayBuffer = sceneMesh.getTriangleIndices();
```

#### ARSceneMesh.release

release(): Promise<void>

释放环境网格数据对象[ARSceneMesh](#section81184417712)占用的内存。

使用Promise异步回调。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<void>

无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function release(): Promise<void> {
  // arSession创建参考ARSession.getFrame接口示例代码
  let frame: arEngine.ARFrame = arSession.getFrame();
  let sceneMesh: arEngine.ARSceneMesh = frame.acquireSceneMesh();
  await sceneMesh.release();
}
```

#### ARSemanticDenseData

表示高精几何重建对象数据的集合。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**6.0.0(20)

名称

类型

只读

可选

说明

timestamp

number

是

否

高精几何重建对象数据的时间戳。以ns为单位。

pointDataSize

number

是

否

高精几何重建对象数据中稠密点云数量的大小。最小为0，最大为10000。

cubeDataSize

number

是

否

高精几何重建对象数据中立方体数量的大小。最小为0，最大为1。

#### ARSemanticDenseData.acquirePointData

acquirePointData(): ARSemanticDensePointData

高精几何重建对象数据中稠密点云数据信息。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**6.0.0(20)

**返回值：**

**类型**

**说明**

[ARSemanticDensePointData](#section1031071863714)

返回所有高精几何重建对象数据中稠密点云数据信息。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let semanticData: arEngine.ARSemanticDenseData = frame.acquireSemanticDense();
let semanticPointData: arEngine.ARSemanticDensePointData = semanticData.acquirePointData();
```

#### ARSemanticDenseData.acquireCubeData

acquireCubeData(): Array<ARSemanticDenseCubeData>

高精几何重建对象数据中立方体数据信息。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**6.0.0(20)

**返回值：**

**类型**

**说明**

Array<[ARSemanticDenseCubeData](#section1516742919422)>

返回一个高精几何重建对象数据的立方体数据信息的列表。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let semanticData: arEngine.ARSemanticDenseData = frame.acquireSemanticDense();
let semanticCubeData: arEngine.ARSemanticDenseCubeData = semanticData.acquireCubeData()[0];
```

#### ARSemanticDenseData.release

release(): Promise<void>

释放高精几何重建对象数据[ARSemanticDenseData](#section137161158185414)占用的内存。

使用Promise异步回调。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**6.0.0(20)

**返回值：**

**类型**

**说明**

Promise<void>

无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let frame: arEngine.ARFrame = arSession.getFrame();
let semanticData: arEngine.ARSemanticDenseData = frame.acquireSemanticDense();
semanticData.release();
```

#### ARTrackable

可追踪的对象。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

type

[ARTrackableType](#section1725585684613)

是

否

可追踪对象类型。

state

[ARTrackingState](#section16656547114620)

是

否

可追踪对象的追踪状态。

#### ARTrackable.getPose

getPose(): ARPose

获取追踪对象的位姿信息。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

[ARPose](#section19274193834913)

返回可追踪对象的位姿信息。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
let trackablePose: arEngine.ARPose = trackables[0].getPose();
```

#### ARTrackable.getAnchors

getAnchors(): Array<ARAnchor>

获取可跟踪对象的锚点信息。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Array<[ARAnchor](#section106411242143016)>

返回一个锚点对象组成的数组。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
let anchors: Array<arEngine.ARAnchor> = trackables[0].getAnchors();
```

#### ARTrackable.createAnchor

createAnchor(pose: ARPose): ARAnchor

使用可追踪对象的位姿信息创建一个锚点对象。这个锚点将与当前可追踪对象绑定。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**参数**：

**参数名**

**类型**

必填

**说明**

pose

[ARPose](#section19274193834913)

是

位姿对象。

**返回值：**

**类型**

**说明**

[ARAnchor](#section106411242143016)

返回一个锚点对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

401

Invalid parameters, for example, the input parameter is empty or invalid.

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
let pose: arEngine.ARPose = trackables[0].getPose();
let anchor: arEngine.ARAnchor = trackables[0].createAnchor(pose);
```

#### ARTrackable.release

release(): Promise<void>

释放被追踪对象[ARTrackable](#section1710323720204)占用的内存。

使用Promise异步回调。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<void>

无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

// arSession创建参考ARSession.getFrame接口示例代码
let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.BASE);
trackables[0].release();
```

#### arEngine.createARAugmentedImageDatabase

createARAugmentedImageDatabase(): Promise<ARAugmentedImageDatabase>

创建一个增强型图像数据库。

使用Promise异步回调返回一个[ARAugmentedImageDatabase](#section1410345414514)对象。

**系统能力：**SystemCapability.AREngine.Core

**起始版本：**5.1.0(18)

**返回值：**

**类型**

**说明**

Promise<[ARAugmentedImageDatabase](#section1410345414514)>

Promise对象，返回ARAugmentedImageDatabase对象。

**错误码：**

以下错误码的详细介绍请参见[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

1009200001

Failure.

**示例：**

```ets
import { arEngine } from '@kit.AREngine';

async function createARAugmentedImageDatabase(): Promise<void> {
  let imageDatabase: arEngine.ARAugmentedImageDatabase = await arEngine.createARAugmentedImageDatabase();
}
```

#### arEngine.createARPose

createARPose(rotation: Quaternion, translation: Vec3): ARPose

在AR Engine中创建和初始化一个新的[ARPose](#section19274193834913)对象并返回。

**系统能力：**SystemCapability.AREngine.Core

**起始版本****：**5.1.0(18)

**参数：**

参数名

类型

必填

说明

rotation

[Quaternion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-types#quaternion)

是

表示旋转组件的数据。这个参数是Quaternion类型，通常是一个包含四个元素的数组，为四元数，用于表示和操作3D旋转。

translation

[Vec3](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-types#vec3)

是

表示平移组件的数据。这个参数是Vec3类型，通常是一个包含三个元素的数组，表示3D向量的x、y和z分量，用于表示物体的平移位置。

**返回值：**

**类型**

**说明**

[ARPose](#section19274193834913)

返回创建的位姿对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[AR Engine错误码](../../errors/AR Engine错误码.md)。

错误码ID

错误信息

401

Invalid parameters, for example, the input parameter is empty or invalid.

1009200001

Failure.

**示例：**

```ets
import { Quaternion, Vec3 } from '@kit.ArkGraphics3D';
import { arEngine } from '@kit.AREngine';

let r: Quaternion = {
  x: 0,
  y: 0,
  z: 0,
  w: 0
};
let t: Vec3 = { x: 0, y: 0, z: 0 };
let pose: arEngine.ARPose = arEngine.createARPose(r, t);
```
