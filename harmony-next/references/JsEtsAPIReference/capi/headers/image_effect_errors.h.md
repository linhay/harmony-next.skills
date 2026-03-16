# image_effect_errors.h

#### 概述

声明图片效果器错误码。

**库：** libimage_effect.so

**引用文件：** <multimedia/image_effect/image_effect_errors.h>

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**相关模块：**[ImageEffect](../../topics/graphics/ImageEffect.md)

#### 汇总

#### 枚举

名称typedef关键字描述[ImageEffect_ErrorCode](#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)ImageEffect_ErrorCode效果器错误码。

#### 枚举类型说明

#### ImageEffect_ErrorCode

```ets
enum ImageEffect_ErrorCode
```

**描述**

效果器错误码。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

枚举项描述EFFECT_SUCCESS = 0操作成功。EFFECT_ERROR_PERMISSION_DENIED = 201权限校验失败。EFFECT_ERROR_PARAM_INVALID = 401参数检查失败。EFFECT_BUFFER_SIZE_NOT_MATCH = 29000001输出buffer尺寸不匹配。EFFECT_COLOR_SPACE_NOT_MATCH = 29000002输入输出色彩空间不匹配。EFFECT_INPUT_OUTPUT_NOT_MATCH = 29000101输入输出配置不一致。比如：输入Surface，输出Pixelmap。EFFECT_EFFECT_NUMBER_LIMITED = 29000102超出管线最大规格。EFFECT_INPUT_OUTPUT_NOT_SUPPORTED = 29000103输入、输出配置不支持。EFFECT_ALLOCATE_MEMORY_FAILED = 29000104申请内存失败。EFFECT_PARAM_ERROR = 29000121参数值错误。 例如：滤镜无效的参数值。EFFECT_KEY_ERROR = 29000122参数错误。例如：滤镜无效的参数。EFFECT_UNKNOWN = 29000199未定义错误。