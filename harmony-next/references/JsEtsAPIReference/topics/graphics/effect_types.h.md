# effect_types.h

**概述**

声明滤镜效果的数据类型。

引用文件： <native_effect/effect_types.h>

库： libnative_effect.so

系统能力： SystemCapability.Multimedia.Image.Core

起始版本： 12

相关模块： [effectKit](effectKit.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Filter_ColorMatrix | - | 定义一个用来创建滤镜效果的矩阵。 |
| OH_Filter | OH_Filter | 滤镜结构体，用来生成滤镜位图。 |
| OH_PixelmapNative | OH_PixelmapNative | 定义一个位图。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| EffectErrorCode | EffectErrorCode | 定义滤镜效果的状态码。 |
| EffectTileMode | EffectTileMode | 定义着色器效果平铺模式的枚举。 |

**枚举类型说明**

**EffectErrorCode**

```ets
enum EffectErrorCode
```

描述

定义滤镜效果的状态码。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| EFFECT_SUCCESS = 0 | 成功。 |
| EFFECT_BAD_PARAMETER = 401 | 无效的参数。 |
| EFFECT_UNSUPPORTED_OPERATION = 7600201 | 不支持的操作。 |
| EFFECT_UNKNOWN_ERROR = 7600901 | 未知错误。 |

**EffectTileMode**

```ets
enum EffectTileMode
```

描述

定义着色器效果平铺模式的枚举。

起始版本： 14

| 枚举项 | 描述 |
| --- | --- |
| CLAMP = 0 | 如果着色器效果超出其原始边界，剩余区域使用着色器的边缘颜色填充。 |
| REPEAT | 在水平和垂直方向上重复着色器效果。 |
| MIRROR | 在水平和垂直方向上重复着色器效果，交替镜像图像，以便相邻图像始终接合。 |
| DECAL | 仅在其原始边界内渲染着色器效果。 |