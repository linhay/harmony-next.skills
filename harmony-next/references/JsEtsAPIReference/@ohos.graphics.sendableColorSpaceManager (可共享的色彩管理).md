# @ohos.graphics.sendableColorSpaceManager (可共享的色彩管理)

本模块提供管理抽象化色域对象的一些基础能力，包括可共享的色彩管理的创建与可共享的色域基础属性的获取等。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { sendableColorSpaceManager } from '@kit.ArkGraphics2D';
```

#### ISendable

type ISendable = lang.ISendable

ISendable是所有Sendable类型（除null和undefined）的父类型。自身没有任何必须的方法和属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

类型说明[lang.ISendable](@arkts.lang (ArkTS语言基础能力).md#ZH-CN_TOPIC_0000002497444768__langisendable)所有Sendable类型的父类型。

#### sendableColorSpaceManager.create

create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager

创建标准可共享的色彩管理。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

参数名类型必填说明colorSpaceName[colorSpaceManager.ColorSpace](@ohos.graphics.colorSpaceManager (色彩管理).md#ZH-CN_TOPIC_0000002497445992__colorspace)是

标准色域类型枚举值。

UNKNOWN与CUSTOM不可用于直接创建色域对象。

**返回值：**

类型说明[ColorSpaceManager](#ZH-CN_TOPIC_0000002529285963__colorspacemanager)

返回当前创建的可共享的色彩管理实例。

该实例继承ISendable，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[色彩管理错误码](色彩管理错误码.md)。

错误码ID错误信息401Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed.18600001The parameter value is abnormal.

**示例：**

```ets
import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
colorSpace = sendableColorSpaceManager.create(colorSpaceManager.ColorSpace.SRGB);
```

#### sendableColorSpaceManager.create

create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager

创建用户自定义可共享的色彩管理实例。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

参数名类型必填说明primaries[colorSpaceManager.ColorSpacePrimaries](@ohos.graphics.colorSpaceManager (色彩管理).md#ZH-CN_TOPIC_0000002497445992__colorspaceprimaries)是色域标准三原色。gammanumber是色域gamma值，取值为大于0的浮点数。

**返回值：**

类型说明[ColorSpaceManager](#ZH-CN_TOPIC_0000002529285963__colorspacemanager)

返回当前创建的可共享的色彩管理实例。

色域类型定义为[colorSpaceManager.ColorSpace](@ohos.graphics.colorSpaceManager (色彩管理).md#ZH-CN_TOPIC_0000002497445992__colorspace)枚举值CUSTOM。

该实例继承ISendable，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[色彩管理错误码](色彩管理错误码.md)。

错误码ID错误信息401Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed.18600001The parameter value is abnormal.

**示例：**

```ets
import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
let primaries: colorSpaceManager.ColorSpacePrimaries = {
  redX: 0.1,
  redY: 0.1,
  greenX: 0.2,
  greenY: 0.2,
  blueX: 0.3,
  blueY: 0.3,
  whitePointX: 0.4,
  whitePointY: 0.4
};
let gamma: number = 2.2;
colorSpace = sendableColorSpaceManager.create(primaries, gamma);
```

#### ColorSpaceManager

当前可共享的色彩管理实例。

下列API示例中都需先使用[create()](#ZH-CN_TOPIC_0000002529285963__sendablecolorspacemanagercreate)获取到ColorSpaceManager实例，再通过此实例调用对应方法。

#### getColorSpaceName

getColorSpaceName(): colorSpaceManager.ColorSpace

获取色域类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

类型说明[colorSpaceManager.ColorSpace](@ohos.graphics.colorSpaceManager (色彩管理).md#ZH-CN_TOPIC_0000002497445992__colorspace)返回色域类型枚举值。

**错误码：**

以下错误码的详细介绍请参见[色彩管理错误码](色彩管理错误码.md)。

错误码ID错误信息18600001The parameter value is abnormal.

**示例：**

```ets
let spaceName: colorSpaceManager.ColorSpace = colorSpace.getColorSpaceName();
```

#### getWhitePoint

getWhitePoint(): collections.Array<number>

获取色域白点值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

类型说明[collections.Array<number>](Class (Array).md)返回色域白点值[x, y]。

**错误码：**

以下错误码的详细介绍请参见[色彩管理错误码](色彩管理错误码.md)。

错误码ID错误信息18600001The parameter value is abnormal.

**示例：**

```ets
import { collections } from '@kit.ArkTS';
let point: collections.Array<number> = colorSpace.getWhitePoint();
```

#### getGamma

getGamma(): number

获取色域gamma值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

类型说明number返回色域gamma值。

**错误码：**

以下错误码的详细介绍请参见[色彩管理错误码](色彩管理错误码.md)。

错误码ID错误信息18600001The parameter value is abnormal.

**示例：**

```ets
let gamma: number = colorSpace.getGamma();
```