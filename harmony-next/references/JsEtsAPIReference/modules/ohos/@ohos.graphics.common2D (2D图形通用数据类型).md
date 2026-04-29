# @ohos.graphics.common2D (2D图形通用数据类型)

本模块定义了一些2D图形领域的通用数据类型。

-

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块使用屏幕物理像素单位px。

#### 导入模块

```ets
import { common2D } from '@kit.ArkGraphics2D';
```

#### Color

ARGB格式的颜色描述。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| alpha | number | 否 | 否 | 颜色的A分量（透明度），值是0~255的整数。 |
| red | number | 否 | 否 | 颜色的R分量（红色），值是0~255的整数。 |
| green | number | 否 | 否 | 颜色的G分量（绿色），值是0~255的整数。 |
| blue | number | 否 | 否 | 颜色的B分量（蓝色），值是0~255的整数。 |

#### Rect

矩形区域，通过2个坐标点可以描述出一个矩形区域，这2个点分别认为是矩形区域的左上角点与右下角点。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 矩形区域的左上角横坐标，浮点数。 |
| top | number | 否 | 否 | 矩形区域的左上角纵坐标，浮点数。 |
| right | number | 否 | 否 | 矩形区域的右下角横坐标，浮点数。 |
| bottom | number | 否 | 否 | 矩形区域的右下角纵坐标，浮点数。 |

#### Point12+

坐标点。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 横坐标，浮点数。 |
| y | number | 否 | 否 | 纵坐标，浮点数。 |

#### Color4f20+

ARGB格式的颜色描述。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| alpha | number | 否 | 否 | 颜色的A分量（透明度），值是0.0~1.0的浮点数。 |
| red | number | 否 | 否 | 颜色的R分量（红色），值是0.0~1.0的浮点数。 |
| green | number | 否 | 否 | 颜色的G分量（绿色），值是0.0~1.0的浮点数。 |
| blue | number | 否 | 否 | 颜色的B分量（蓝色），值是0.0~1.0的浮点数。 |

#### Point3d12+

三维的坐标点。继承自[Point](#ZH-CN_TOPIC_0000002522082126__point12)。

**系统能力：** SystemCapability.Graphics.Drawing

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| z | number | 否 | 否 | z轴坐标，浮点数。 |