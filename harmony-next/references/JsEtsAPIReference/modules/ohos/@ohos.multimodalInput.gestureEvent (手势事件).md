# @ohos.multimodalInput.gestureEvent (手势事件)

设备上报的手势事件。


本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { Rotate, Pinch, ThreeFingersSwipe, FourFingersSwipe, ActionType } from '@kit.InputKit';
```

#### Pinch

捏合手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | ActionType | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| scale | number | 否 | 否 | 捏合度，取值范围大于等于0。 |

#### Rotate11+

旋转手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | ActionType | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| angle | number | 否 | 否 | 旋转角度。 |

#### ThreeFingersSwipe

三指滑动手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | ActionType | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| x | number | 否 | 否 | 坐标x。 |
| y | number | 否 | 否 | 坐标y。 |

#### FourFingersSwipe

四指滑动手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | ActionType | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| x | number | 否 | 否 | 坐标x。 |
| y | number | 否 | 否 | 坐标y。 |

#### ThreeFingersTap11+

三指轻点手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | ActionType | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |

#### ActionType

手势事件类型。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CANCEL | 0 | 取消。 |
| BEGIN | 1 | 手势开始。 |
| UPDATE | 2 | 手势更新。 |
| END | 3 | 手势结束。 |