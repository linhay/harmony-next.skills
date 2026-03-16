# staticMap（静态图）

本模块提供获取静态图功能。

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { staticMap } from '@kit.MapKit';
```

#### getMapImage

getMapImage(options: StaticMapOptions): Promise<image.PixelMap>

根据提供的参数创建静态图。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

options

[StaticMapOptions](#section1555293218278)

是

静态图参数。

**返回值：**

类型

说明

Promise<[image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)>

Promise对象，返回[image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

1002600001

System internal error.

1002600002

Failed to connect to the Map Kit server.

1002600003

App authentication failed.

1002600004

The Map permission is not enabled.

1002600005

The network is unavailable.

1002600006

The API call times exceed the quota.

1002600007

The API QPS exceeds the quota.

1002600008

The API is in arrears.

1002600009

The API has not subscribed to any pay-as-you-go package.

1002600010

The server is busy. Please wait and try again.

**示例：**

```ets
let staticMapOptions: staticMap.StaticMapOptions = {
  location: {
    latitude: 39.9,
    longitude: 116.4
  },
  zoom: 3,
  imageWidth: 10,
  imageHeight: 10
};
await staticMap.getMapImage(staticMapOptions);
```

#### getMapImage

getMapImage(context: common.Context, options: StaticMapOptions): Promise<image.PixelMap>

根据提供的参数创建静态图，支持传入Context上下文。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

Context上下文。

options

[StaticMapOptions](#section1555293218278)

是

静态图参数。

**返回值：**

类型

说明

Promise<[image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)>

Promise对象，返回[image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

1002600001

System internal error.

1002600002

Failed to connect to the Map Kit server.

1002600003

App authentication failed.

1002600004

The Map permission is not enabled.

1002600005

The network is unavailable.

1002600006

The API call times exceed the quota.

1002600007

The API QPS exceeds the quota.

1002600008

The API is in arrears.

1002600009

The API has not subscribed to any pay-as-you-go package.

1002600010

The server is busy. Please wait and try again.

**示例：**

```ets
let staticMapOptions: staticMap.StaticMapOptions = {
  location: {
    latitude: 39.9,
    longitude: 116.4
  },
  zoom: 3,
  imageWidth: 10,
  imageHeight: 10
};
await staticMap.getMapImage(this.getUIContext().getHostContext(), staticMapOptions);
```

#### StaticMapOptions

StaticMapOptions定义了静态图的参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**名称**

**类型**

只读

可选

**说明**

location

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

否

否

地图的中心点坐标。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

zoom

number

否

否

地图的缩放级别，取值范围[2, 17]，仅支持整数，小数会被向下取整处理。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

imageWidth

number

否

否

图片的宽度。

如果scale为1，则取值范围为(0, 1024]；如果scale为2，则取值范围为(0, 512]。单位：px。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

imageHeight

number

否

否

图片的高度。

如果scale为1，则取值范围为(0, 1024]；如果scale为2，则取值范围为(0, 512]。单位：px。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

scale

number

否

是

比例，取值为1或2，默认值为1。

可使用scale参数返回高分辨率地图图像。scale*imageWidth*imageHeight可确定图像的实际输出大小，单位：px。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

logoAlignment

[mapCommon.LogoAlignment](mapCommon（地图属性模型）.md#section892653673414)

否

是

地图logo的对齐模式，默认为BOTTOM_START，表示左下角。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

markers

Array<[StaticMapMarker](#section2425142418218)>

否

是

在地图图像上添加标记。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

 说明：

网络图标资源的载入会影响网络性能，建议不超过3个。

path

[StaticMapPath](#section5891333163917)

否

是

添加在地图图像上的路径信息。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

dayNightMode

[mapCommon.DayNightMode](mapCommon（地图属性模型）.md#section634916281725)

否

是

昼夜模式，默认值为[mapCommon.DayNightMode](mapCommon（地图属性模型）.md#section634916281725).DAY。

**起始版本：**5.0.0(12)

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**示例：**

```ets
let staticMapOptions: staticMap.StaticMapOptions = {
  location: {
    latitude: 39.9,
    longitude: 116.4
  },
  zoom: 3,
  imageWidth: 10,
  imageHeight: 10
};
```

#### StaticMapMarker

StaticMapMarker定义了标记点位置。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**名称**

**类型**

只读

可选

**说明**

location

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

否

否

标记点坐标。

icon

string

否

是

标记点自定义图标，该图标必须以http://或https://开头。如果未设置或者图标不符合要求，系统将使用默认图标。

 说明：

图标格式为png，大小不能大于16KB，像素不超过128*128。

defaultIconSize

[IconSize](#section18522846142615)

否

是

如果使用默认图标，请选择使用默认图标的大小。默认值为[IconSize](#section18522846142615).NORMAL，表示中等大小。

font

string

否

是

标记点的名称，超长名称超出部分用省略号“...”表示。

fontColor

number

否

是

标记点文字的颜色，ARGB格式，默认值为0xff000000（黑色）。

rotation

number

否

是

标记点图标的旋转角度（仅支持自定义图标）。

以正北方向为0度、顺时针方向为正的角度，默认值为0，取值范围：[0, 360)。超出取值范围的值会换算成取值范围内的值，比如361会被换算成1，-1换算为359。

**示例：**

```ets
let staticMapMarker: staticMap.StaticMapMarker = {
  location: {
    latitude: 50,
    longitude: 126
  },
  icon: 'https://icons.iconarchive.com/icons/papirus-team/papirus-apps/48/pingus-icon-icon.png',
  font: 'statics',
  fontColor: 0xff000000,
  rotation: 180,
  defaultIconSize: staticMap.IconSize.TINY
};
```

#### StaticMapPath

StaticMapPath定义了添加到地图图像上的路径信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**名称**

**类型**

只读

可选

**说明**

locations

Array<[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)>

否

否

路径的坐标。

color

number

否

是

指示路径的颜色，ARGB格式，默认值为0xff000000（黑色）。

fillColor

number

否

是

指示路径的填充颜色，ARGB格式。如果设置fillColor，则路径指示一个多边形。默认值为0x00000000（透明）。

width

number

否

是

路径的宽度，取值范围：(0, 1024]，单位：px，默认值为5px，异常值不处理。

**示例：**

```ets
let staticMapPath: staticMap.StaticMapPath = {
  locations: [
    { latitude: 50, longitude: 126 },
    { latitude: 50.3, longitude: 126 },
    { latitude: 50.3, longitude: 126.3 },
    { latitude: 49.7, longitude: 126 },
    { latitude: 50, longitude: 126 }
  ],
  color: 0xff00ff00,
  fillColor: 0xff0000ff,
  width: 15
};
```

#### IconSize

IconSize定义了静态地图标记的默认图标大小。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

名称

值

说明

TINY

0

最小的图标。

SMALL

1

小图标。

NORMAL

2

中等大小图标。

**示例：**

```ets
let iconSize = staticMap.IconSize.TINY;
```