# MvtOverlay

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### MvtOverlay

矢量图层的管理对象。在调用map.[MapComponentController](MapComponentController.md)类的[addMvtOverlay](MapComponentController.md#section10177450104116)方法时会返回该类型的实例，继承[BaseOverlay](BaseOverlay.md)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core.EnhancedOverlay

**起始版本：**6.0.0(20)

**示例：**

```ets
let params: mapCommon.MvtOverlayParams = {
  source: {
    // 设置矢量图层的地址,必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
    tileUrl: 'http://xxx/tiles/{z}/{x}/{y}.pbf',
    minZoom: 2,
    maxZoom: 15
  },
  layers: [{
    id: 'layer-map',
    type: mapCommon.MvtLayerType.FILL,
    // 对应矢量图层数据中图层的name字段
    sourceLayer: 'XX',
    paint: {
      fillColor: {
        operator: mapCommon.Operator.GET,
        args: 'fill'
      },
      fillOpacity: {
        operator: mapCommon.Operator.GET,
        args: 'fill-opacity'
      }
    }
  }]
};
let mvtOverlay = this.mapController?.addMvtOverlay(params);
```

#### addLayers

addLayers(layers: mapCommon.MvtLayer[]): void

添加新矢量图层。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core.EnhancedOverlay

**起始版本：**6.0.0(20)

**参数：**

**参数名**

**类型**

必填

**说明**

layers

[mapCommon.MvtLayer](mapCommon（地图属性模型）.md#section14599124818)[]

是

矢量图层。

**示例：**

```ets
let renderLayers: Array<mapCommon.MvtLayer> = []
let staticLayerIds = [-12, -8, -4, 0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44];
for (let index = 0; index < staticLayerIds.length; index++) {
  let layer: mapCommon.MvtLayer = {
    id: index.toString(),
    type: mapCommon.MvtLayerType.FILL,
    sourceLayer: staticLayerIds[index].toString(),
    paint: {
      fillColor: {
        operator: mapCommon.Operator.GET,
        args: 'fill'
      },
      fillOpacity: {
        operator: mapCommon.Operator.GET,
        args: 'fill-opacity'
      }
    }
  }
  renderLayers.push(layer)
};

mvtOverlay.addLayers(renderLayers);
```

#### removeLayers

removeLayers(layerIds: string[]): void

移除指定的图层。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core.EnhancedOverlay

**起始版本：**6.0.0(20)

**参数：**

**参数名**

**类型**

必填

**说明**

layerIds

string[]

是

需要删除的图层ID。

**示例：**

```ets
let layerIds = ['111'];
mvtOverlay.removeLayers(layerIds);
```

#### changeLayers

changeLayers(addedLayers: mapCommon.MvtLayer[], removedLayerIds: string[]): void

新增矢量图层，根据图层ID删除图层。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core.EnhancedOverlay

**起始版本：**6.0.0(20)

**参数：**

**参数名**

**类型**

必填

**说明**

addedLayers

[mapCommon.MvtLayer](mapCommon（地图属性模型）.md#section14599124818)[]

是

矢量图层。

removedLayerIds

string[]

是

需要删除的图层ID。

**示例：**

```ets
let renderLayers: Array<mapCommon.MvtLayer> = [];
let staticLayerIds = [-12, -8, -4, 0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44];
for (let index = 0; index < staticLayerIds.length; index++) {
  let layer: mapCommon.MvtLayer = {
    id: index.toString(),
    type: mapCommon.MvtLayerType.FILL,
    sourceLayer: staticLayerIds[index].toString(),
    paint: {
      fillColor: {
        operator: mapCommon.Operator.GET,
        args: 'fill'
      },
      fillOpacity: {
        operator: mapCommon.Operator.GET,
        args: 'fill-opacity'
      }
    }
  }
  renderLayers.push(layer)
}
let layerIds = ['111'];

mvtOverlay.changeLayers(renderLayers, layerIds);
```

#### setBlur

setBlur(blurIntensity: number | Record<number, number>): void

更新矢量图层的模糊强度。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core.EnhancedOverlay

**起始版本：**6.0.2(22)

**参数：**

**参数名**

**类型**

必填

**说明**

blurIntensity

number | Record<number, number>

是

矢量图层的模糊强度。

模糊度范围：[0, 20]，小数向下取整，默认值为0，异常值按默认值处理。

若传数字，表示所有缩放层级按同一模糊度处理。

若传键值对，key为缩放层级，value为模糊度，有效层级范围：[2，20]，层级异常值大于20取20，小于2取2。例如：{ 5: 5, 10: 8, 18: 15 }，2到4层级为0，默认不模糊，5到9层级模糊度为5，10到17层级模糊度为8，18到20层级模糊度为15。

**示例：**

```ets
mvtOverlay.setBlur(8);
```

#### getBlur

getBlur(): number | Record<number, number>

获取矢量图层的模糊强度。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core.EnhancedOverlay

**起始版本：**6.0.2(22)

**返回值：**

类型

说明

number | Record<number, number>

矢量图层的模糊强度。

**示例：**

```ets
let blur: number | Record<number, number> = mvtOverlay.getBlur()
```