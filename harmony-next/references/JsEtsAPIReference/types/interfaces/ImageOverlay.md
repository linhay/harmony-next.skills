# ImageOverlay

**导入模块**

```ets
import { map, mapCommon } from '@kit.MapKit';
```

**ImageOverlay**

图片覆盖物。继承[BaseOverlay](BaseOverlay.md)。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

示例：

```ets
let imageOverlayParams: mapCommon.ImageOverlayParams = {
  bounds: {
    southwest: { latitude: 32, longitude: 118 },
    northeast: { latitude: 32.4, longitude: 118.4 }
  },
  // 图标需存放在resources/rawfile目录下
  image: 'icon.png',
  transparency: 0.3,
  zIndex: 101,
  anchorU: 0.5,
  anchorV: 0.5,
  clickable: true,
  visible: true,
  bearing: 0
};
let imageOverlay = await this.mapController?.addImageOverlay(imageOverlayParams);
imageOverlay.setBearing(180);
let bearing: number = imageOverlay.getBearing();
```

**getBearing**

getBearing(): number

获取覆盖物的旋转角度。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 返回覆盖物的旋转角度。 |

示例：

```ets
let bearing: number = imageOverlay.getBearing();
```

**getBounds**

getBounds(): mapCommon.LatLngBounds

获取覆盖物的矩形区域。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| mapCommon.LatLngBounds | 获取覆盖物的矩形区域。 |

示例：

```ets
let bounds: mapCommon.LatLngBounds = imageOverlay.getBounds();
```

**getHeight**

getHeight(): number

获取覆盖物的高度。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的高度，单位：米。 |

示例：

```ets
let height: number = imageOverlay.getHeight();
```

**getWidth**

getWidth(): number

获取覆盖物的宽度。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的宽度，单位：米。 |

示例：

```ets
let width: number = imageOverlay.getWidth();
```

**getPosition**

getPosition(): mapCommon.LatLng

获取覆盖物的位置。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| mapCommon.LatLng | 覆盖物的位置。 |

示例：

```ets
let position: mapCommon.LatLng = imageOverlay.getPosition();
```

**getTransparency**

getTransparency(): number

获取覆盖物的透明度。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的透明度。取值范围：[0, 1]。0表示不透明，1表示全透明。 |

示例：

```ets
let transparency: number = imageOverlay.getTransparency();
```

**isClickable**

isClickable(): boolean

获取是否可点击。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 是否可点击。 - true：可点击 - false：不可点击 |

示例：

```ets
let click: boolean = imageOverlay.isClickable();
```

**setBearing**

setBearing(bearing: number): void

设置覆盖物的旋转角度。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bearing | number | 是 | 覆盖物的旋转角度。 以正北方向为0度、顺时针方向为正的角度，默认值为0，取值范围：[0, 360)。超出取值范围的值会换算成取值范围内的值，比如361会被换算成1，-1换算为359。 |

示例：

```ets
imageOverlay.setBearing(180);
```

**setClickable**

setClickable(clickable: boolean): void

设置是否开启可点击开关。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clickable | boolean | 是 | 是否开启可点击开关。 - true：开启 - false：不开启 |

示例：

```ets
imageOverlay.setClickable(false);
```

**setDimensions**

setDimensions(width: number, height?: number): void

设置覆盖物的宽度和高度。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 宽度。width为正整数，单位：米。 |
| height | number | 否 | 高度。height为正整数，单位：米。若不设置高度，则以覆盖物图片默认宽高比例显示高度。 |

示例：

```ets
imageOverlay.setDimensions(100000, 100000);
```

**setImage**

setImage(image: ResourceStr | image.PixelMap): Promise<void>

设置覆盖物的图像。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | ResourceStr | image.PixelMap | 是 | 覆盖物的图像。 图片格式支持jpg、jpeg、png、gif、webp、svg。 说明： ResourceStr为Resource和string两种格式，其中string类型入参支持两种格式： - 资源相对路径格式：图标存放在resources/rawfile，image参数传入rawfile文件夹下的相对路径。 - toDataURL格式（如data:image/png;base64,<图片的Base64字节编码值>）。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

示例：

```ets
// 图标需存放在resources/rawfile目录下
await imageOverlay.setImage("icon.png");
```

**setBounds**

setBounds(bounds: mapCommon.LatLngBounds): void

设置覆盖物的矩形区域。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bounds | mapCommon.LatLngBounds | 是 | 覆盖物的矩形区域。 |

示例：

```ets
let bounds: mapCommon.LatLngBounds = {
  southwest: { longitude: 118, latitude: 31 },
  northeast: { longitude: 119, latitude: 32 }
};
imageOverlay.setBounds(bounds);
```

**setPosition**

setPosition(position: mapCommon.LatLng): void

设置覆盖物的位置。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | mapCommon.LatLng | 是 | 覆盖物的位置。 |

示例：

```ets
let position: mapCommon.LatLng = { longitude: 118, latitude: 31 };
imageOverlay.setPosition(position);
```

**setTransparency**

setTransparency(transparency: number): void

设置覆盖物的透明度。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transparency | number | 是 | 覆盖物的透明度。取值范围：[0, 1]。0表示不透明，1表示全透明。异常值不生效。 |

示例：

```ets
imageOverlay.setTransparency(0.1);
```