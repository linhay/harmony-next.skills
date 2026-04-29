# @ohos.graphics.colorSpaceManager (色彩管理)

本模块提供管理抽象化色域对象的一些基础能力，包括色域对象的创建与色域基础属性的获取等。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { colorSpaceManager } from '@kit.ArkGraphics2D';
```

#### ColorSpace

色域类型枚举。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 未知的色域类型。 |
| ADOBE_RGB_1998 | 1 | RGB色域为Adobe RGB(1998)类型。 转换函数为Adobe RGB(1998)类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| DCI_P3 | 2 | RGB色域为DCI-P3类型。 转换函数为Gamma 2.6类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| DISPLAY_P3 | 3 | RGB色域为Display P3类型。 转换函数为SRGB类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| SRGB | 4 | RGB色域为SRGB类型。 转换函数为SRGB类型。 编码范围为Full类型。 系统默认色域类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| CUSTOM | 5 | 用户自定义色域类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| BT70911+ | 6 | RGB色域为BT709类型。 转换函数为BT709类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| BT601_EBU11+ | 7 | RGB色域为BT601_P类型。 转换函数为BT709类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| BT601_SMPTE_C11+ | 8 | RGB色域为BT601_N类型。 转换函数为BT709类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| BT2020_HLG11+ | 9 | RGB色域为BT2020类型。 转换函数为HLG类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| BT2020_PQ11+ | 10 | RGB色域为BT2020类型。 转换函数为PQ类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| P3_HLG11+ | 11 | RGB色域为Display P3类型。 转换函数为HLG类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| P3_PQ11+ | 12 | RGB色域为Display P3类型。 转换函数为PQ类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ADOBE_RGB_1998_LIMIT11+ | 13 | RGB色域为Adobe RGB(1998)类型。 转换函数为Adobe RGB(1998)类型。 编码范围为Limit类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| DISPLAY_P3_LIMIT11+ | 14 | RGB色域为Display P3类型。 转换函数为SRGB类型。 编码范围为Limit类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| SRGB_LIMIT11+ | 15 | RGB色域为SRGB类型。 转换函数为SRGB类型。 编码范围为Limit类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| BT709_LIMIT11+ | 16 | RGB色域为BT709类型。 转换函数为BT709类型。 编码范围为Limit类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| BT601_EBU_LIMIT11+ | 17 | RGB色域为BT601_P类型。 转换函数为BT709类型。 编码范围为Limit类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| BT601_SMPTE_C_LIMIT11+ | 18 | RGB色域为BT601_N类型。 转换函数为BT709类型。 编码范围为Limit类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| BT2020_HLG_LIMIT11+ | 19 | RGB色域为BT2020类型。 转换函数为HLG类型。 编码范围为Limit类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| BT2020_PQ_LIMIT11+ | 20 | RGB色域为BT2020类型。 转换函数为PQ类型。 编码范围为Limit类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| P3_HLG_LIMIT11+ | 21 | RGB色域为Display P3类型。 转换函数为HLG类型。 编码范围为Limit类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| P3_PQ_LIMIT11+ | 22 | RGB色域为Display P3类型。 转换函数为PQ类型。 编码范围为Limit类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| LINEAR_P311+ | 23 | RGB色域为Display P3类型。 转换函数为Linear类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| LINEAR_SRGB11+ | 24 | RGB色域为SRGB类型。 转换函数为Linear类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| LINEAR_BT70911+ | 24 | 与LINEAR_SRGB相同。 RGB色域为BT709类型。 转换函数为Linear类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| LINEAR_BT202011+ | 25 | RGB色域为BT2020类型。 转换函数为Linear类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| H_LOG18+ | 26 | RGB色域为BT2020类型。 转换函数为LOG类型。 |
| DISPLAY_BT2020_SRGB20+ | 27 | RGB色域为DISPLAY BT2020类型。 转换函数为SRGB类型。 编码范围为Full类型。 |
| DISPLAY_SRGB11+ | 4 | 与SRGB相同。 RGB色域为SRGB类型。 转换函数为SRGB类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| DISPLAY_P3_SRGB11+ | 3 | 与DISPLAY_P3相同。 RGB色域为Display P3类型。 转换函数为SRGB类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| DISPLAY_P3_HLG11+ | 11 | 与P3_HLG相同。 RGB色域为Display P3类型。 转换函数为HLG类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| DISPLAY_P3_PQ11+ | 12 | 与P3_PQ相同。 RGB色域为Display P3类型。 转换函数为PQ类型。 编码范围为Full类型。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

#### ColorSpacePrimaries

色域标准三原色（红、绿、蓝）和白色，使用(x, y)表示其在色彩空间中的位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| redX | number | 否 | 否 | 标准红色在色彩空间的x坐标值。 |
| redY | number | 否 | 否 | 标准红色在色彩空间的y坐标值。 |
| greenX | number | 否 | 否 | 标准绿色在色彩空间的x坐标值。 |
| greenY | number | 否 | 否 | 标准绿色在色彩空间的y坐标值。 |
| blueX | number | 否 | 否 | 标准蓝色在色彩空间的x坐标值。 |
| blueY | number | 否 | 否 | 标准蓝色在色彩空间的y坐标值。 |
| whitePointX | number | 否 | 否 | 标准白色在色彩空间的x坐标值。 |
| whitePointY | number | 否 | 否 | 标准白色在色彩空间的y坐标值。 |

#### colorSpaceManager.create

create(colorSpaceName: ColorSpace): ColorSpaceManager

创建标准色域对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpaceName | ColorSpace | 是 | 标准色域类型枚举值。 UNKNOWN与CUSTOM不可用于直接创建色域对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ColorSpaceManager | 返回当前创建的色域对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[色彩管理错误码]([色彩管理错误码](../../errors/色彩管理错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | The parameter value is abnormal. |

**示例：**

```ets
let colorSpace: colorSpaceManager.ColorSpaceManager;
try {
    colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.SRGB);
} catch (err) {
    console.error(`Failed to create SRGB colorSpace. Cause: ` + JSON.stringify(err));
}
```

#### colorSpaceManager.create

create(primaries: ColorSpacePrimaries, gamma: number): ColorSpaceManager

创建用户自定义色域对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| primaries | ColorSpacePrimaries | 是 | 色域标准三原色。 |
| gamma | number | 是 | 色域gamma值，取值为大于0的浮点数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ColorSpaceManager | 返回当前创建的色域对象实例。 色域类型定义为ColorSpace枚举值CUSTOM。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[色彩管理错误码](色彩管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | Invalid parameter value. Possible cause: Used UNKNOWN or CUSTOM color space type enum values to directly create a colorSpaceManager object. |

**示例：**

```ets
let colorSpace: colorSpaceManager.ColorSpaceManager;
try {
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
    let gamma = 2.2;
    colorSpace = colorSpaceManager.create(primaries, gamma);
} catch (err) {
    console.error(`Failed to create colorSpace with customized primaries and gamma. Cause: ` + JSON.stringify(err));
}
```

#### ColorSpaceManager

当前色域对象实例。

下列API示例中都需先使用[create()](#ZH-CN_TOPIC_0000002522242120__colorspacemanagercreate)获取到ColorSpaceManager实例，再通过此实例调用对应方法。

#### getColorSpaceName

getColorSpaceName(): ColorSpace

获取色域类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ColorSpace | 返回色域类型枚举值。 |

**示例：**

```ets
try {
    let spaceName = colorSpace.getColorSpaceName();
} catch (err) {
    console.error(`Fail to get colorSpace's name. Cause: ` + JSON.stringify(err));
}
```

#### getWhitePoint

getWhitePoint(): Array<number>

获取色域白点值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 返回色域白点值[x, y]。 |

**示例：**

```ets
try {
    let point = colorSpace.getWhitePoint();
} catch (err) {
    console.error(`Failed to get white point. Cause: ` + JSON.stringify(err));
}
```

#### getGamma

getGamma(): number

获取色域gamma值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回色域gamma值。 |

**示例：**

```ets
try {
    let gamma = colorSpace.getGamma();
} catch (err) {
    console.error(`Failed to get gamma. Cause: ` + JSON.stringify(err));
}
```