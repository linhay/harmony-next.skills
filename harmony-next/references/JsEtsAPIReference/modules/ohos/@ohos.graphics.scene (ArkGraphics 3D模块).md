# @ohos.graphics.scene (ArkGraphics 3D模块)

@ohos.graphics.scene将3D开发相关模块的API组织在一起，方便开发者进行导出使用。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### Scene

[Scene](../../topics/media/Scene.md)：ArkGraphics 3D基础模块，提供SceneResourceParameters、SceneNodeParameters等通用数据类型。同时提供glTF模型加载，场景元素、资源创建等基础方法。

**系统能力：** SystemCapability.ArkUi.Graphics3D

#### SceneNode

[SceneNode](../../topics/components/SceneNode.md)：3D场景是以树状结构进行组织的，通过操作结点属性以及结点树结构可以改变3D场景。本模块提供3D图形中场景资源结点的类型及操作方法。

**系统能力：** SystemCapability.ArkUi.Graphics3D

#### SceneType

[SceneType](../../topics/networking/SceneType.md)：本模块覆盖3D图形中的数据类型，包括向量、四元数等。

**系统能力：** SystemCapability.ArkUi.Graphics3D

#### SceneResources

[SceneResources](../../topics/system-services/SceneResource.md)：本模块提供3D图形中常用的基本资源类型，包括材质、图片、着色器等。

**系统能力：** SystemCapability.ArkUi.Graphics3D

#### ScenePostProcessSettings

[ScenePostProcessSettings](../../topics/system-services/ScenePostProcessSettings.md)：本模块提供3D图形中的色调映射等图像后处理方法。

**系统能力：** SystemCapability.ArkUi.Graphics3D