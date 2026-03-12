# BaseOverlay

#### 导入模块

```ets
import { map, mapCommon } from '@kit.MapKit';
```

#### BaseOverlay

覆盖物基础类。[Marker](Marker.md)、[MapPolyline](MapPolyline.md)、[MapPolygon](MapPolygon.md)、[MapCircle](MapCircle.md)、[MapArc](MapArc.md)、[ImageOverlay](ImageOverlay.md)、[BasePriorityOverlay](BasePriorityOverlay.md)等覆盖物继承该基础类。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

返回类型

方法

string

[getId](#section7073612370)()

获取覆盖物的ID属性。

number

[getZIndex](#section15225105915396)()

获取覆盖物的z指数。

Object

[getTag](#section19301111714013)()

覆盖物的tag属性。

boolean

[isVisible](#section186444914423)()

覆盖物的可见性。

void

[remove](#section39155506439)()

从地图移除覆盖物。

void

[setZIndex](#section394129124411)(zIndex: number)

设置覆盖物的z指数。

void

[setTag](#section15199510114518)(tag: Object)

设置覆盖物的tag属性。

void

[setVisible](#section132033103450)(visible: boolean)

设置覆盖物的可见性。

#### getId

getId(): string

获取覆盖物的ID。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

string

覆盖物的ID。

**示例：**

```ets
// 以marker为例
let markerOptions: mapCommon.MarkerOptions = {
  position: {
    latitude: 39.9,
    longitude: 116.4
  }
};
let marker: map.Marker = await this.mapController.addMarker(markerOptions);
let id: string = marker.getId();
```

#### getZIndex

getZIndex(): number

获取覆盖物的z指数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

number

覆盖物的z指数。z指数指覆盖物的叠加顺序，具有较大z指数的覆盖物会绘制在具有较小z指数的覆盖物上，具有相同z指数的叠加顺序为元素添加的先后顺序。覆盖物初始化时如果未设置zIndex参数，默认值为0。异常值按默认值处理。

**示例：**

```ets
// 以marker为例
let zIndex: number = marker.getZIndex();
```

#### getTag

getTag(): Object

获取覆盖物的tag属性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

Object

覆盖物的tag属性。

**示例：**

```ets
// 以marker为例
let tag: Object = marker.getTag();
```

#### isVisible

isVisible(): boolean

获取覆盖物的可见性。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**返回值：**

类型

说明

boolean

覆盖物的可见性。

- true：可见
- false：不可见

**示例：**

```ets
// 以marker为例
let isVisible: boolean = marker.isVisible();
```

#### remove

remove(): void

从地图移除覆盖物。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**示例：**

```ets
// 以marker为例
marker.remove();
```

#### setZIndex

setZIndex(zIndex: number): void

设置覆盖物的z指数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

参数名

**类型**

必填

**说明**

zIndex

number

是

覆盖物的z指数。z指数指覆盖物的叠加顺序，具有较大z指数的覆盖物会绘制在具有较小z指数的覆盖物上，具有相同z指数的叠加顺序为元素添加的先后顺序。覆盖物初始化时如果未设置zIndex参数，默认值为0。异常值按默认值处理。

**示例：**

```ets
// 以marker为例
marker.setZIndex(3);
```

#### setTag

setTag(tag: Object): void

设置覆盖物的tag属性。tag属性可以是任意对象，如果设置为空，则清除tag。当您不再需要使用tag时，您可以调用setTag(null)或setTag(undefined)清除tag，以防止应用程序发生内存泄漏。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

tag

Object

是

覆盖物的tag属性。

**示例：**

```ets
// 以marker为例
let tag = "tag-1";
marker.setTag(tag);
```

#### setVisible

setVisible(visible: boolean): void

设置覆盖物的可见性，默认可见。

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

覆盖物的可见性。

- true：可见
- false：不可见

默认值为true。

**示例：**

```ets
// 以marker为例
marker.setVisible(true);
```