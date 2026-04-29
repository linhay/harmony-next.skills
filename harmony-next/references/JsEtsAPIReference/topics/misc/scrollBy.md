# scrollBy

**导入模块**

```ets
import { map } from '@kit.MapKit';
```

**scrollBy**

scrollBy(x: number, y: number): CameraUpdate

按像素移动地图中心点。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本4.1.0(11)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Map.Core

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 水平移动的像素数。正值代表可视区域向右移动，负值代表可视区域向左移动。单位：px。 |
| y | number | 是 | 竖直移动的像素数。正值代表可视区域向下移动，负值代表可视区域向上移动。单位：px。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| CameraUpdate | 描述地图状态将要发生的变化。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |

示例：

```ets
let cameraUpdate: map.CameraUpdate = map.scrollBy(100, 200);
```