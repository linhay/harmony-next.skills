# MapPolyline

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### MapPolyline

折线，继承[BaseOverlay](../misc/BaseOverlay.md)。在调用map.[MapComponentController](../components/MapComponentController.md)类的[addPolyline](../components/MapComponentController.md#section6818109112812)方法时会返回该类型的实例。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**示例：**

```ets
// 数组存放图片内容
let customTextures: Array<ResourceStr | image.PixelMap> = new Array();
// 图标存放在resources/rawfile目录下
customTextures.push('icon/img.png');
customTextures.push('icon/img_1.png');
let cusIndexNumber: Array<number> = new Array();
// cusIndexNumber数组长度与折线点数量必须相同，数组元素内容与customTextures下标相对应，图片从数组第二个元素开始选择
cusIndexNumber.push(0, 0, 1);
let polylineOption: mapCommon.MapPolylineOptions = {
  points: [
    { latitude: 31.68, longitude: 118.166 },
    { latitude: 31.48, longitude: 118.366 },
    { latitude: 31.28, longitude: 118.766 }
  ],
  customTextures: customTextures,
  customTextureIndexes: cusIndexNumber
};
let mapPolyline = await this.mapController.addPolyline(polylineOption);
```

#### getColor

getColor(): number

获取折线的颜色值。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

number

ARGB格式颜色值。

**示例：**

```ets
let color: number = mapPolyline.getColor();
```

#### getColors

getColors(): Array<number>

获取折线的分段颜色值数组。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

Array<number>

折线的分段颜色值数组。

**示例：**

```ets
let colors: Array<number> = mapPolyline.getColors();
```

#### getEndCap

getEndCap(): mapCommon.CapStyle

获取折线的末尾端点样式。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

[mapCommon.CapStyle](../misc/mapCommon（地图属性模型）.md#section173028494409)

折线的末尾端点样式。

**示例：**

```ets
let endCap: mapCommon.CapStyle = mapPolyline.getEndCap();
```

#### getJointType

getJointType(): mapCommon.JointType

获取折线除起始和结束顶点之外的所有顶点的节点类型属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

[mapCommon.JointType](../misc/mapCommon（地图属性模型）.md#section73559613164)

折线除起始和结束顶点之外的所有顶点的节点类型属性。

**示例：**

```ets
let jointType: mapCommon.JointType = mapPolyline.getJointType();
```

#### getPatterns

getPatterns(): Array<mapCommon.PatternItem>

获取折线的样式属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

Array<[mapCommon.PatternItem](../misc/mapCommon（地图属性模型）.md#section917314511192)>

折线的样式属性。

**示例：**

```ets
let patterns: Array<mapCommon.PatternItem> = mapPolyline.getPatterns();
```

#### getPoints

getPoints(): Array<mapCommon.LatLng>

获取折线的顶点坐标属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

Array<[mapCommon.LatLng](../misc/mapCommon（地图属性模型）.md#section20691173773810)>

折线的顶点坐标属性。

**示例：**

```ets
let points: Array<mapCommon.LatLng> = mapPolyline.getPoints();
```

#### getStartCap

getStartCap(): mapCommon.CapStyle

获取折线的起始端点样式。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

[mapCommon.CapStyle](../misc/mapCommon（地图属性模型）.md#section173028494409)

折线的起始端点样式。

**示例：**

```ets
let startCap: mapCommon.CapStyle = mapPolyline.getStartCap();
```

#### getWidth

getWidth(): number

获取折线的宽度属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

number

折线的宽度属性，单位：px。

**示例：**

```ets
let width: number = mapPolyline.getWidth();
```

#### isClickable

isClickable(): boolean

获取折线的可点击属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

boolean

折线的可点击性。

- true：可点击
- false：不可点击

**示例：**

```ets
let isClickable: boolean = mapPolyline.isClickable();
```

#### isGeodesic

isGeodesic(): boolean

获取折线的大地线属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

boolean

折线的大地线属性。

- true：大地线
- false：非大地线

**示例：**

```ets
let isGeodesic: boolean = mapPolyline.isGeodesic();
```

#### isGradient

isGradient(): boolean

获取折线的渐变属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

boolean

折线的渐变属性。

- true：渐变
- false：不渐变

**示例：**

```ets
let isGradient: boolean = mapPolyline.isGradient();
```

#### setClickable

setClickable(clickable: boolean): void

设置折线是否可以点击。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

clickable

boolean

是

设置折线是否可以点击，默认值为false。

- true：可以
- false：不可以

**示例：**

```ets
mapPolyline.setClickable(true);
```

#### setColor

setColor(color: number): void

设置折线的颜色值。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

color

number

是

ARGB格式颜色值，默认值为黑色（0xff000000）。

**示例：**

```ets
mapPolyline.setColor(0xff000000);
```

#### setColors

setColors(colors: Array<number>): void

设置折线的多段颜色值数组。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

colors

Array<number>

是

多段颜色，ARGB格式颜色值数组。

**示例：**

```ets
mapPolyline.setColors([0xffffff00, 0xff000000]);
```

#### setEndCap

setEndCap(endCap: mapCommon.CapStyle): void

设置折线的末尾端点样式。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

endCap

[mapCommon.CapStyle](../misc/mapCommon（地图属性模型）.md#section173028494409)

是

折线的末尾端点样式。

**示例：**

```ets
mapPolyline.setEndCap(mapCommon.CapStyle.BUTT);
```

#### setGeodesic

setGeodesic(geodesic: boolean): void

设置是否将折线的每个线段绘制为大地线。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

geodesic

boolean

是

将折线的每个线段绘制为大地线，默认值为false。

- true：每段绘制为大地线
- false：不是大地线

**示例：**

```ets
mapPolyline.setGeodesic(true);
```

#### setGradient

setGradient(gradient: boolean): void

设置折线的渐变属性是否启用。需设置折线颜色方可生效。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

gradient

boolean

是

设置渐变属性是否启用，默认值为false。

- true：渐变
- false：不渐变

**示例：**

```ets
mapPolyline.setGradient(true);
```

#### setJointType

setJointType(jointType: mapCommon.JointType): void

设置折线除起始和结束顶点之外的所有顶点的节点类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

jointType

[mapCommon.JointType](../misc/mapCommon（地图属性模型）.md#section73559613164)

是

节点类型。

**示例：**

```ets
mapPolyline.setJointType(mapCommon.JointType.DEFAULT);
```

#### setPatterns

setPatterns(patterns: Array<mapCommon.PatternItem>): void

设置折线的样式。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

patterns

Array<[mapCommon.PatternItem](../misc/mapCommon（地图属性模型）.md#section917314511192)>

是

[PatternItem](../misc/mapCommon（地图属性模型）.md#section917314511192)对象的集合。

**示例：**

```ets
let linePattern: Array<mapCommon.PatternItem> = [
  { type: mapCommon.PatternItemType.DASH, length: 100 },
  { type: mapCommon.PatternItemType.DOT, length: 100 },
  { type: mapCommon.PatternItemType.GAP, length: 100 }
];
mapPolyline.setPatterns(linePattern);
```

#### setPoints

setPoints(points: Array<mapCommon.LatLng>): void

设置折线的顶点坐标。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

points

Array<[mapCommon.LatLng](../misc/mapCommon（地图属性模型）.md#section20691173773810)>

是

折线顶点的集合。默认情况下，折线不闭合；要形成闭合的折线，起点和终点必须相同。

**示例：**

```ets
let points: Array<mapCommon.LatLng> = [
  { latitude: 31.18, longitude: 118.766 },
  { latitude: 31.38, longitude: 118.366 },
  { latitude: 31.68, longitude: 118.566 },
  { latitude: 31.98, longitude: 118.266 },
  { latitude: 31.88, longitude: 118.866 }
];
mapPolyline.setPoints(points);
```

#### setStartCap

setStartCap(startCap: mapCommon.CapStyle): void

设置折线的起始端点样式。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

startCap

[mapCommon.CapStyle](../misc/mapCommon（地图属性模型）.md#section173028494409)

是

折线的起始端点样式。

**示例：**

```ets
mapPolyline.setStartCap(mapCommon.CapStyle.BUTT);
```

#### setWidth

setWidth(width: number): void

设置折线的宽度。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

width

number

是

折线的宽度，单位：px，取值范围：大于等于0。

默认值：10，异常值按默认值处理。

**示例：**

```ets
mapPolyline.setWidth(20);
```

#### setCustomTexture

setCustomTexture(customTexture: ResourceStr | image.PixelMap): Promise<void>

设置折线纹理。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

参数名

**类型**

必填

**说明**

customTexture

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | [image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

是

折线纹理。建议纹理使用没有背景色（透明色）的图片。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**示例：**

```ets
// 图标存放在resources/rawfile目录下
await mapPolyline.setCustomTexture("icon/naviline_arrow.png");
```

#### setCustomTexture

setCustomTexture(customTexture: ResourceStr | image.PixelMap, isTextureMappingUsed: boolean): Promise<void>

设置折线纹理。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.3(15)

**参数：**

参数名

**类型**

必填

**说明**

customTexture

[ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | [image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

是

折线纹理。建议纹理使用没有背景色（透明色）的图片。

isTextureMappingUsed

boolean

是

是否使用贴图模式进行纹理绘制，默认为false。如果设置为false，建议纹理没有背景色（使用透明色）。

- true：使用贴图模式
- false：不使用贴图模式

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**示例：**

```ets
// 图标需存放在resources/rawfile目录下
await mapPolyline.setCustomTexture("icon/naviline_arrow.png", true);
```

#### setCustomTextureIndexes

setCustomTextureIndexes(customTextureIndexes: number[]): Promise<void>

动态设置自定义纹理索引。折线设置纹理后，该接口可以将已有的纹理资源动态应用在各个折线段上。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.3(15)

**参数：**

参数名

**类型**

必填

**说明**

customTextureIndexes

number[]

是

每个坐标对应的纹理索引。数组长度需要和points的数量保持一致。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

**示例：**

```ets
await mapPolyline.setCustomTextureIndexes([0,1,0]);
```