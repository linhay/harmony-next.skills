# MassPointOverlayCallback

#### MassPointOverlayCallback

type MassPointOverlayCallback = (massPointOverlay: MassPointOverlay, massPointItem: mapCommon.MassPointItem) => void

无返回结果的回调函数，监听海量点图层点击事件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**6.0.0(20)

**参数**：

**名称**

**类型**

必填

**说明**

massPointOverlay

[MassPointOverlay](MassPointOverlay.md)

是

海量点管理对象。

massPointItem

[mapCommon.MassPointItem](mapCommon（地图属性模型）.md#section17837254174411)

是

海量点列表。