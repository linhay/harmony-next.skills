# TileOverlay

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### TileOverlay

瓦片图层，继承[BaseOverlay](BaseOverlay.md)。

建议最多添加10个TileOverlay，且提供的图层瓦片分辨率是256*256。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.3(15)

**示例：**

```ets
let params: mapCommon.TileOverlayParams = {
  // 设置地图瓦片图层的地址,必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
  tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
  transparency: 0,
  fadeIn: false
};
let tileOverlay: map.TileOverlay = this.mapController?.addTileOverlay(params);
```

#### clearTileCache

clearTileCache(): void

清除瓦片图层的缓存。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.3(15)

**示例：**

```ets
tileOverlay.clearTileCache();
```

#### setFadeIn

setFadeIn(fadeIn: boolean): void

是否开启瓦片图层淡入。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.3(15)

**参数：**

**参数名**

**类型**

必填

**说明**

fadeIn

boolean

是

是否开启瓦片图层淡入。

- true：开启瓦片图层淡入。
- false：不开启瓦片图层淡入。

**示例：**

```ets
tileOverlay.setFadeIn(false);
```

#### setTransparency

setTransparency(transparency: number): void

设置瓦片图层的透明度。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.3(15)

**参数：**

**参数名**

**类型**

必填

**说明**

transparency

number

是

瓦片图层的透明度。取值范围：[0, 1]。0表示不透明，1表示全透明。

**示例：**

```ets
tileOverlay.setTransparency(0.5);
```

#### getFadeIn

getFadeIn(): boolean

返回是否开启瓦片图层淡入。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.3(15)

**返回值：**

类型

说明

boolean

返回是否开启瓦片图层淡入。

- true：已开启瓦片图层淡入。
- false：未开启瓦片图层淡入。

**示例：**

```ets
let isFadeIn: boolean = tileOverlay.getFadeIn();
```

#### getTransparency

getTransparency(): number

返回瓦片图层的透明度。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.3(15)

**返回值：**

类型

说明

number

返回瓦片图层的透明度。

**示例：**

```ets
let transparency: number = tileOverlay.getTransparency();
```

#### clearDiskCache

clearDiskCache(): Promise<void>

清除磁盘缓存，内存缓存也会被清除。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**6.0.0(20)

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**示例：**

```ets
tileOverlay.clearDiskCache();
```