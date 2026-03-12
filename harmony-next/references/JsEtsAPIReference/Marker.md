# Marker

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### Marker

标记，继承[BaseOverlay](BaseOverlay.md)。在调用map.[MapComponentController](MapComponentController.md)类的[addMarker](MapComponentController.md#section0810361284)方法时会返回该类型的实例。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**示例：**

```ets
let markerOptions: mapCommon.MarkerOptions = {
  position: {
    latitude: 39.9,
    longitude: 116.4
  }
};
let marker: map.Marker = await this.mapController.addMarker(markerOptions);
```

#### getTitle

getTitle(): string

返回信息窗的标题。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

string

信息窗的标题。

**示例：**

```ets
let title: string = marker.getTitle();
```

#### getSnippet

getSnippet(): string

返回信息窗的子标题。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

string

信息窗的子标题。

**示例：**

```ets
let snippet: string = marker.getSnippet();
```

#### getAlpha

getAlpha(): number

获取标记的透明度。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

number

标记的透明度，取值范围：[0, 1]。

**示例：**

```ets
let alpha: number = marker.getAlpha();
```

#### getPosition

getPosition(): mapCommon.LatLng

获取标记的位置。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

标记的位置。

**示例：**

```ets
let position: mapCommon.LatLng = marker.getPosition();
```

#### getRotation

getRotation(): number

获取标记的旋转角度。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

number

标记的旋转角度。

**示例：**

```ets
let rotation: number = marker.getRotation();
```

#### isClickable

isClickable(): boolean

获取标记是否可以点击。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

boolean

标记是否可以点击。

- true：可以
- false：不可以

**示例：**

```ets
let isClickable: boolean = marker.isClickable();
```

#### isDraggable

isDraggable(): boolean

获取标记是否可以通过长按来拖拽。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

boolean

标记是否可以通过长按来拖拽。

- true：可以
- false：不可以

**示例：**

```ets
let isDraggable: boolean = marker.isDraggable();
```

#### isFlat

isFlat(): boolean

获取标记是否平贴地图。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

boolean

标记是否平贴地图。

- true：平贴地图
- false：面对相机

**示例：**

```ets
let isFlat: boolean = marker.isFlat();
```

#### setAlpha

setAlpha(alpha: number): void

设置标记的透明度属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

alpha

number

是

标记的透明度，取值范围：[0, 1]，默认值为1，异常值不处理。

- 0：完全透明
- 1：完全不透明

**示例：**

```ets
marker.setAlpha(0.5);
```

#### setClickable

setClickable(clickable: boolean): void

设置标记是否可以点击。

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

设置标记是否可以点击，默认值为false。

- true：可以
- false：不可以

**示例：**

```ets
marker.setClickable(true);
```

#### setDraggable

setDraggable(draggable: boolean): void

设置标记是否可以长按拖拽。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

draggable

boolean

是

是否可以长按拖拽，默认值为false。

- true：可以
- false：不可以

**示例：**

```ets
marker.setDraggable(true);
```

#### setFlat

setFlat(flat: boolean): void

设置标记是否平贴地图。如果标记平贴地图，则在相机旋转和倾斜时，标记仍将停留在地图上，它将保持与照相机缩放时相同的大小。 如果标记面对相机，它将始终面向相机绘制，并随相机旋转和倾斜。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

flat

boolean

是

是否平贴地图，默认值为false。

- true：平贴地图
- false：面对相机

**示例：**

```ets
marker.setFlat(true);
```

#### setIcon

setIcon(icon: string | image.PixelMap | Resource): Promise<void>

设置标记的图标。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

icon

string | [image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource)

是

标记的图标。

- 图片格式支持jpg、jpeg、png、gif、webp、svg。
- string类型入参支持两种格式：

  - 资源相对路径格式：图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径。
  - toDataURL格式（如data:image/png;base64,<图片的Base64字节编码值>）

 说明：

从5.0.0(12)版本开始，icon属性支持[Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource)和[image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)类型。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**示例：**

```ets
// 图标需存放在resources/rawfile目录下
await marker.setIcon('icon/test.png');
```

#### setMarkerAnchor

setMarkerAnchor(anchorU: number, anchorV: number): void

设置标记的锚点位置。锚点是标记图标接触地图平面的点，图标的左顶点为（0, 0）点，右顶点为（1, 0）点，左底点为（0, 1）点，右底点为（1, 1）点。例如，在标记X（0.5, 0.3）处的锚点坐标如下：

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

anchorU

number

是

锚点的水平坐标，以图像宽度的比例，取值范围：[0, 1]，异常值不处理。

anchorV

number

是

锚点的垂直坐标，以图像高度的比例，取值范围：[0, 1]，异常值不处理。

**示例：**

```ets
marker.setMarkerAnchor(1.0, 1.0);
```

#### setPosition

setPosition(latLng: mapCommon.LatLng): void

设置标记的位置坐标。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

latLng

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

是

标记的位置坐标。

**示例：**

```ets
let position: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
marker.setPosition(position);
```

#### setRotation

setRotation(rotation: number): void

设置标记的旋转角度，即标记围绕标记锚点顺时针旋转的角度，旋转轴垂直于标记。默认旋转角度为0，默认位置为北对齐。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

rotation

number

是

标记的旋转角度。

以正北方向为0度、顺时针方向为正的角度，默认值为0，取值范围：[0, 360)。超出取值范围的值会换算成取值范围内的值，比如361会被换算成1，-1换算为359。

**示例：**

```ets
marker.setRotation(30);
```

#### setTitle

setTitle(title: string): void

设置信息窗的标题。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

title

string

是

信息窗口的标题，超长字串超出部分用省略号“…”表示。

**示例：**

```ets
marker.setTitle("title");
```

#### setSnippet

setSnippet(snippet: string): void

设置信息窗口的子标题。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

snippet

string

是

信息窗口的子标题，超长字串超出部分用省略号“…”表示。

**示例：**

```ets
marker.setSnippet("su");
```

#### setInfoWindowAnchor

setInfoWindowAnchor(anchorU: number, anchorV: number): void

设置信息窗的锚点位置。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

anchorU

number

是

锚点在水平方向上的位置，取值范围：[0, 1]，异常值不处理。

anchorV

number

是

锚点在垂直方向上的位置，取值范围：[0, 1]，异常值不处理。

**示例：**

```ets
marker.setInfoWindowAnchor(0.5, 0.5);
```

#### setInfoWindowVisible

setInfoWindowVisible(visible: boolean): void

设置信息窗是否可见。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

visible

boolean

是

设置信息窗是否可见。

- true：可见
- false：不可见

**示例：**

```ets
marker.setInfoWindowVisible(true);
```

#### isInfoWindowVisible

isInfoWindowVisible(): boolean

返回信息窗是否可见。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

**类型**

**说明**

boolean

信息窗口是否可见。

- true：可见
- false：不可见

**示例：**

```ets
let visible: boolean = marker.isInfoWindowVisible();
```

#### setAnimation

setAnimation(animation: Animation): void

设置标记的动画，不支持[FontSizeAnimation](FontSizeAnimation.md)。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

animation

[Animation](Animation.md)

是

动画。

**示例：**

```ets
let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
animation.setDuration(3000);
let callbackStart = () => {
  console.info("animationStart", `callback`);
};
let callbackEnd = () => {
  console.info("animationEnd", `callback`);
};
animation.on("animationStart", callbackStart);
animation.on("animationEnd", callbackEnd);
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
animation.setRepeatCount(100);

marker.setAnimation(animation);
```

#### startAnimation

startAnimation(): void

启动标记的动画。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**示例：**

```ets
let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
animation.setDuration(3000);
let callbackStart = () => {
  console.info("animationStart", `callback`);
};
let callbackEnd = () => {
  console.info("animationEnd", `callback`);
};
animation.on("animationStart", callbackStart);
animation.on("animationEnd", callbackEnd);
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
animation.setRepeatCount(100);

marker.setAnimation(animation);
marker.startAnimation();
```

#### clearAnimation

clearAnimation(): void

清除标记的动画。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**示例：**

```ets
marker.clearAnimation();
```

#### getAltitude

getAltitude(): number

获取海拔高度。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

number

海拔高度，单位：米。

**示例：**

```ets
let altitude: number = marker.getAltitude();
```

#### setAltitude

setAltitude(altitude: number): void

设置海拔高度。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

参数名

**类型**

必填

**说明**

altitude

number

是

海拔高度，单位：米。

**示例：**

```ets
marker.setAltitude(500);
```

#### setAnnotationVisible

setAnnotationVisible(visible: boolean): void

设置标记是否显示文本。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

**参数：**

参数名

**类型**

必填

**说明**

visible

boolean

是

标记是否显示文本。

- true：显示
- false：不显示

**示例：**

```ets
marker.setAnnotationVisible(true);
```

#### isAnnotationVisible

isAnnotationVisible(): boolean

返回标记文本是否可见。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.1.1(19)

**返回值：**

类型

说明

boolean

标记文本是否可见。

- true：可见
- false：不可见

**示例：**

```ets
let isVisible = marker.isAnnotationVisible();
```

#### setIconBuilder

setIconBuilder(iconBuilder: CustomBuilder): Promise<void>

设置生成标记图标的自定义组件。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**6.0.0(20)

**参数：**

参数名

**类型**

必填

**说明**

iconBuilder

[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)

是

自定义组件。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

1002601005

Failed to generate the icon of the custom component.

**示例：**

```ets
@Builder
renderBuilder() {
  Stack({ alignContent: Alignment.Center }) {
    Text('Test Icon Builder')
  }
  .height(50)
  .width(200)
}
// 设置自定义组件
try {
  await this.marker?.setIconBuilder(() => {
    this.renderBuilder();
  })
} catch (error) {
  let err = error as BusinessError;
  console.error('Marker icon builder test error code' + err.code + 'message:' + err.message);
}
```

#### setOffset

setOffset(x: number, y: number): void

设置标记图标的偏移量。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**6.0.2(22)

**参数：**

参数名

**类型**

必填

**说明**

x

number

是

X轴方向的偏移量，单位：px，原点是图标的中心点，异常值不处理。

y

number

是

Y轴方向的偏移量，单位：px，原点是图标的中心点，异常值不处理。

**示例：**

```ets
marker.setOffset(20,20);
```

#### getOffsetX

getOffsetX(): number

获取标记图标在X轴方向的偏移量。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**6.0.2(22)

**返回值：**

类型

说明

number

获取标记图标在X轴方向的偏移量，单位：px，原点是图标的中心点。

**示例：**

```ets
let X: number = marker.getOffsetX();
```

#### getOffsetY

getOffsetY(): number

获取标记图标在Y轴方向的偏移量。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**6.0.2(22)

**返回值：**

类型

说明

number

获取标记图标在Y轴方向的偏移量，单位：px，原点是图标的中心点。

**示例：**

```ets
let Y: number = marker.getOffsetY();
```