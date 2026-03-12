# SceneType

本模块提供3D图形中常用的数据类型。

- 本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标标记接口的起始版本。

#### 导入模块

```ets
import { Vec2, Vec3, Vec4, Quaternion, Aabb, Color, Rect, GeometryType, PrimitiveTopology, CustomGeometry, CubeGeometry, PlaneGeometry, SphereGeometry, Position3, Rotation3, Scale3 } from '@kit.ArkGraphics3D';
```

#### Vec2

二维向量，通常用于表示2D空间中的点或方向，由x和y两个分量组成。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明xnumber否否x轴分量，取值范围是实数。ynumber否否y轴分量，取值范围是实数。

#### Vec3

三维向量，通常用于表示3D空间中的点、方向或向量变换，由x、y和z三个分量组成。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明xnumber否否x轴分量，取值范围是实数。ynumber否否y轴分量，取值范围是实数。znumber否否z轴分量，取值范围是实数。

#### Vec4

四维向量，通常用于表示4D空间中的点、方向或向量变换，由x、y、z和w四个分量组成，增加第四个分量为各种计算和变换增加了规整性和便捷性。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明xnumber否否x轴分量，取值范围是实数。ynumber否否y轴分量，取值范围是实数。znumber否否z轴分量，取值范围是实数。wnumber否否w轴分量，取值范围是实数。

#### Quaternion

用于表示3D空间中旋转的数学结构。与传统的欧拉角相比，四元数在数值稳定性和避免万向节锁方面具有优势。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明xnumber否否x轴分量，取值范围是实数。ynumber否否y轴分量，取值范围是实数。znumber否否z轴分量，取值范围是实数。wnumber否否w轴分量，取值范围是实数。

#### Aabb

轴对齐边界盒，主要用于判断空间中的物体是否重叠。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明aabbMin[Vec3](#ZH-CN_TOPIC_0000002497446096__vec3)否否轴对齐边界盒的小值点。aabbMax[Vec3](#ZH-CN_TOPIC_0000002497446096__vec3)否否轴对齐边界盒的大值点。

#### Color

用于表示RGBA格式的颜色，包含四个分量，依次为红色、绿色、蓝色和透明度。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明rnumber否否红色分量，取值范围是[0, 1]。gnumber否否绿色分量，取值范围是[0, 1]。bnumber否否蓝色分量，取值范围是[0, 1]。anumber否否透明度分量，取值范围是[0, 1]。

#### Rect

用于表示平面中的矩形。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明xnumber否否矩形左下角x轴分量，单位为所属坐标系的单位长度，取值为任意实数，具体范围依赖场景坐标系设置。ynumber否否矩形左下角y轴分量，单位为所属坐标系的单位长度，取值为任意实数，具体范围依赖场景坐标系设置。widthnumber否否矩形宽度，单位为所属坐标系的单位长度，有效取值范围大于0。heightnumber否否矩形高度，单位为所属坐标系的单位长度，有效取值范围大于0。

#### RenderingPipelineType21+

渲染管线类型枚举。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称值说明FORWARD_LIGHTWEIGHT0轻量级前向渲染管线，直接渲染到后缓冲区。该管线只能在着色器中实现逐像素效果（例如色调映射），不支持复杂效果（例如光晕）。FORWARD1高质量前向渲染管线，用于复杂的视觉效果（例如光晕）。

#### GeometryType18+

几何类型枚举，用于指定不同的几何类型。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称值说明CUSTOM0自定义几何体类型。CUBE1立方体类型。PLANE2平面类型。SPHERE3球体类型。

#### GeometryDefinition18+

几何类型定义抽象类，用于解释特定几何类型的属性。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明geometryType[GeometryType](#ZH-CN_TOPIC_0000002497446096__geometrytype18)是否定义不同的几何类型。

#### PrimitiveTopology18+

 图元拓扑枚举，在顶点处理过程中，指定顶点的不同处理方式。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称值说明TRIANGLE_LIST0由不相交的顶点集合构成不同的三角形。TRIANGLE_STRIP1每个顶点和前一个三角形的一条边构成新的三角形。

#### CustomGeometry18+

自定义几何类型，继承自[GeometryDefinition](#ZH-CN_TOPIC_0000002497446096__geometrydefinition18)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明topology[PrimitiveTopology](#ZH-CN_TOPIC_0000002497446096__primitivetopology18)否是三角形图元的解析方式，默认值为TRIANGLE_LIST。vertices[Vec3](#ZH-CN_TOPIC_0000002497446096__vec3)[]否否模型的顶点数组。indicesnumber[]否是顶点索引数组，数组中元素的取值范围大于等于0，默认值为undefined。normals[Vec3](#ZH-CN_TOPIC_0000002497446096__vec3)[]否是顶点数组对应的法向量数组，默认值为undefined。uvs[Vec2](#ZH-CN_TOPIC_0000002497446096__vec2)[]否是顶点数组对应的UV坐标数组，默认值为undefined。colors[Color](#ZH-CN_TOPIC_0000002497446096__color)[]否是顶点数组对应的颜色数组，默认值为undefined。

#### CubeGeometry18+

立方体几何类型，继承自[GeometryDefinition](#ZH-CN_TOPIC_0000002497446096__geometrydefinition18)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明size[Vec3](#ZH-CN_TOPIC_0000002497446096__vec3)否否立方体的宽、高和深度，表示立方体的大小。

#### PlaneGeometry18+

平面几何类型，继承自[GeometryDefinition](#ZH-CN_TOPIC_0000002497446096__geometrydefinition18)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明size[Vec2](#ZH-CN_TOPIC_0000002497446096__vec2)否否平面的宽、高，表示平面的大小。

#### SphereGeometry18+

球体几何类型，继承自[GeometryDefinition](#ZH-CN_TOPIC_0000002497446096__geometrydefinition18)。

**系统能力：** SystemCapability.ArkUi.Graphics3D

名称类型只读可选说明radiusnumber否否球体半径，单位为世界坐标系下的场景单位（比如cm、m、km等），取值范围大于0。segmentCountnumber否否在球体上以经纬度分割的段数，取值范围大于0。

#### Position3

type Position3 = Vec3

用于表示3维空间中物体的位置，是[Vec3](#ZH-CN_TOPIC_0000002497446096__vec3)类型。

**系统能力：** SystemCapability.ArkUi.Graphics3D

类型说明[Vec3](#ZH-CN_TOPIC_0000002497446096__vec3)类型为三维向量，可取任意值。

#### Rotation3

type Rotation3 = Vec3

用于表示3维空间中物体的旋转，是[Vec3](#ZH-CN_TOPIC_0000002497446096__vec3)类型。

**系统能力：** SystemCapability.ArkUi.Graphics3D

类型说明[Vec3](#ZH-CN_TOPIC_0000002497446096__vec3)类型为三维向量，可取任意值。

#### Scale3

type Scale3 = Vec3

用于表示3维空间中物体的缩放，是[Vec3](#ZH-CN_TOPIC_0000002497446096__vec3)类型。

**系统能力：** SystemCapability.ArkUi.Graphics3D

类型说明[Vec3](#ZH-CN_TOPIC_0000002497446096__vec3)类型为三维向量，可取任意值。