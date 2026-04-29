# native_color_space_manager.h

**概述**

定义创建和使用色彩空间的相关函数。

引用文件： <native_color_space_manager/native_color_space_manager.h>

库： libnative_color_space_manager.so

系统能力： SystemCapability.Graphic.Graphic2D.ColorManager.Core

起始版本： 13

相关模块： [NativeColorSpaceManager](NativeColorSpaceManager.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ColorSpacePrimaries | ColorSpacePrimaries | 提供色彩原色结构体声明。 |
| WhitePointArray | - | 提供白点数组结构体，白点是指在当前色域中表示白色的坐标。 |
| OH_NativeColorSpaceManager | OH_NativeColorSpaceManager | 提供OH_NativeColorSpaceManager结构体声明。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ColorSpaceName | ColorSpaceName | 色彩空间枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_NativeColorSpaceManager* OH_NativeColorSpaceManager_CreateFromName(ColorSpaceName colorSpaceName) | 通过colorSpaceName创建OH_NativeColorSpaceManager实例。 每次调用此函数时，都会创建一个新的OH_NativeColorSpaceManager实例。 |
| OH_NativeColorSpaceManager* OH_NativeColorSpaceManager_CreateFromPrimariesAndGamma(ColorSpacePrimaries primaries, float gamma) | 通过原色和伽马值创建OH_NativeColorSpaceManager实例。 每次调用此函数时，都会创建一个新的OH_NativeColorSpaceManager实例。 |
| void OH_NativeColorSpaceManager_Destroy(OH_NativeColorSpaceManager* nativeColorSpaceManager) | 销毁OH_NativeColorSpaceManager实例。 |
| int OH_NativeColorSpaceManager_GetColorSpaceName(OH_NativeColorSpaceManager* nativeColorSpaceManager) | 获取色彩空间名称。 |
| WhitePointArray OH_NativeColorSpaceManager_GetWhitePoint(OH_NativeColorSpaceManager* nativeColorSpaceManager) | 获取白点。 |
| float OH_NativeColorSpaceManager_GetGamma(OH_NativeColorSpaceManager* nativeColorSpaceManager) | 获取伽马值。 |

**枚举类型说明**

**ColorSpaceName**

```ets
enum ColorSpaceName
```

描述

色彩空间枚举。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| NONE = 0 | 表示未知的色彩空间。 |
| ADOBE_RGB = 1 | 表示基于Adobe RGB的色彩空间。 |
| DCI_P3 = 2 | 表示基于SMPTE RP 431-2-2007和IEC 61966-2.1：1999的色彩空间。 |
| DISPLAY_P3 = 3 | 表示基于SMPTE RP 431-2-2007和IEC 61966-2.1：1999的色彩空间。 |
| SRGB = 4 | 表示基于IEC 61966-2.1：1999的标准红绿蓝（SRGB）色彩空间。 |
| BT709 = 6 | 表示基于ITU-R BT.709的色彩空间。 |
| BT601_EBU = 7 | 表示基于ITU-R BT.601的色彩空间。 |
| BT601_SMPTE_C = 8 | 表示基于ITU-R BT.601的色彩空间。 |
| BT2020_HLG = 9 | 表示基于ITU-R BT.2020的色彩空间。 |
| BT2020_PQ = 10 | 表示基于ITU-R BT.2020的色彩空间。 |
| P3_HLG = 11 | 表示色彩原色为P3_D65，传输特性为HLG，色彩范围为Full的色彩空间。 |
| P3_PQ = 12 | 表示色彩原色为P3_D65，传输特性为PQ，色彩范围为Full的色彩空间。 |
| ADOBE_RGB_LIMIT = 13 | 表示色彩原色为ADOBE_RGB，传输特性为ADOBE_RGB，色彩范围为LIMIT的色彩空间。 |
| DISPLAY_P3_LIMIT = 14 | 表示色彩原色为P3_D65，传输特性为SRGB，色彩范围为LIMIT的色彩空间。 |
| SRGB_LIMIT = 15 | 表示色彩原色为SRGB，传输特性为SRGB，色彩范围为LIMIT的色彩空间。 |
| BT709_LIMIT = 16 | 表示色彩原色为BT709，传输特性为BT709，色彩范围为LIMIT的色彩空间。 |
| BT601_EBU_LIMIT = 17 | 表示色彩原色为BT601_P，传输特性为BT709，色彩范围为LIMIT的色彩空间。 |
| BT601_SMPTE_C_LIMIT = 18 | 表示色彩原色为BT601_N，传输特性为BT709，色彩范围为LIMIT的色彩空间。 |
| BT2020_HLG_LIMIT = 19 | 表示色彩原色为BT2020，传输特性为HLG，色彩范围为LIMIT的色彩空间。 |
| BT2020_PQ_LIMIT = 20 | 表示色彩原色为BT2020，传输特性为PQ，色彩范围为LIMIT的色彩空间。 |
| P3_HLG_LIMIT = 21 | 表示色彩原色为P3_D65，传输特性为HLG，色彩范围为LIMIT的色彩空间。 |
| P3_PQ_LIMIT = 22 | 表示色彩原色为P3_D65，传输特性为PQ，色彩范围为LIMIT的色彩空间。 |
| LINEAR_P3 = 23 | 表示色彩原色为P3_D65，传输特性为LINEAR的色彩空间。 |
| LINEAR_SRGB = 24 | 表示色彩原色为SRGB，传输特性为LINEAR的色彩空间。 |
| LINEAR_BT709 = LINEAR_SRGB | 表示色彩原色为BT709，传输特性为LINEAR的色彩空间。 |
| LINEAR_BT2020 = 25 | 表示色彩原色为BT2020，传输特性为LINEAR的色彩空间。 |
| DISPLAY_SRGB = SRGB | 表示色彩原色为SRGB，传输特性为SRGB，色彩范围为Full的色彩空间。 |
| DISPLAY_P3_SRGB = DISPLAY_P3 | 表示色彩原色为P3_D65，传输特性为SRGB，色彩范围为Full的色彩空间。 |
| DISPLAY_P3_HLG = P3_HLG | 表示色彩原色为P3_D65，传输特性为HLG，色彩范围为Full的色彩空间。 |
| DISPLAY_P3_PQ = P3_PQ | 表示色彩原色为P3_D65，传输特性为PQ，色彩范围为Full的色彩空间。 |
| CUSTOM = 5 | 表示自定义色彩空间。 |

**函数说明**

**OH_NativeColorSpaceManager_CreateFromName()**

```ets
OH_NativeColorSpaceManager* OH_NativeColorSpaceManager_CreateFromName(ColorSpaceName colorSpaceName)
```

描述

通过colorSpaceName创建OH_NativeColorSpaceManager实例。

每次调用此函数时，都会创建一个新的OH_NativeColorSpaceManager实例。

系统能力： SystemCapability.Graphic.Graphic2D.ColorManager.Core

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ColorSpaceName colorSpaceName | 表示创建OH_NativeColorSpaceManager的色彩空间名称。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_NativeColorSpaceManager* | 返回一个指向OH_NativeColorSpaceManager实例的指针。内存不足时，会导致创建OH_NativeColorSpaceManager实例失败。 |

**OH_NativeColorSpaceManager_CreateFromPrimariesAndGamma()**

```ets
OH_NativeColorSpaceManager* OH_NativeColorSpaceManager_CreateFromPrimariesAndGamma(ColorSpacePrimaries primaries, float gamma)
```

描述

通过原色和伽马值创建OH_NativeColorSpaceManager实例。

每次调用此函数时，都会创建一个新的OH_NativeColorSpaceManager实例。

系统能力： SystemCapability.Graphic.Graphic2D.ColorManager.Core

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ColorSpacePrimaries primaries | 表示创建OH_NativeColorSpaceManager的色彩原色。 |
| float gamma | 表示创建OH_NativeColorSpaceManager的伽马值，伽马值为一个浮点数，用于校正亮度范围。 伽马值通常为正值，负值会使弱光区域更亮，强光区域变暗，伽马值为0表示线性色彩空间。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_NativeColorSpaceManager* | 返回一个指向OH_NativeColorSpaceManager实例的指针。  内存不足时，会导致创建OH_NativeColorSpaceManager实例失败。 |

**OH_NativeColorSpaceManager_Destroy()**

```ets
void OH_NativeColorSpaceManager_Destroy(OH_NativeColorSpaceManager* nativeColorSpaceManager)
```

描述

销毁OH_NativeColorSpaceManager实例。

系统能力： SystemCapability.Graphic.Graphic2D.ColorManager.Core

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeColorSpaceManager* nativeColorSpaceManager | 表示指向OH_NativeColorSpaceManager实例的指针。 |

**OH_NativeColorSpaceManager_GetColorSpaceName()**

```ets
int OH_NativeColorSpaceManager_GetColorSpaceName(OH_NativeColorSpaceManager* nativeColorSpaceManager)
```

描述

获取色彩空间名称。

系统能力： SystemCapability.Graphic.Graphic2D.ColorManager.Core

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeColorSpaceManager* nativeColorSpaceManager | 表示指向OH_NativeColorSpaceManager实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回色彩空间枚举ColorSpaceName对应的值。其中，当返回值为0时，表示接口操作失败。 |

**OH_NativeColorSpaceManager_GetWhitePoint()**

```ets
WhitePointArray OH_NativeColorSpaceManager_GetWhitePoint(OH_NativeColorSpaceManager* nativeColorSpaceManager)
```

描述

获取白点。

系统能力： SystemCapability.Graphic.Graphic2D.ColorManager.Core

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeColorSpaceManager* nativeColorSpaceManager | 表示指向OH_NativeColorSpaceManager实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| WhitePointArray | 返回值为float数组，返回值为<0.0, 0.0>表示接口操作失败，其余返回值表示操作成功。 |

**OH_NativeColorSpaceManager_GetGamma()**

```ets
float OH_NativeColorSpaceManager_GetGamma(OH_NativeColorSpaceManager* nativeColorSpaceManager)
```

描述

获取伽马值。

系统能力： SystemCapability.Graphic.Graphic2D.ColorManager.Core

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeColorSpaceManager* nativeColorSpaceManager | 表示指向OH_NativeColorSpaceManager实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 返回值为float类型，返回值为0.0表示接口操作失败，其余返回值表示操作成功。 |