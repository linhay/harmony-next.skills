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

名称类型只读可选说明type[ActionType](#ZH-CN_TOPIC_0000002497445590__actiontype)否否手势事件类型。如：手势开始、手势更新、手势结束等。scalenumber否否捏合度，取值范围大于等于0。

#### Rotate11+

旋转手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

名称类型只读可选说明type[ActionType](#ZH-CN_TOPIC_0000002497445590__actiontype)否否手势事件类型。如：手势开始、手势更新、手势结束等。anglenumber否否旋转角度。

#### ThreeFingersSwipe

三指滑动手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

名称类型只读可选说明type[ActionType](#ZH-CN_TOPIC_0000002497445590__actiontype)否否手势事件类型。如：手势开始、手势更新、手势结束等。xnumber否否坐标x。ynumber否否坐标y。

#### FourFingersSwipe

四指滑动手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

名称类型只读可选说明type[ActionType](#ZH-CN_TOPIC_0000002497445590__actiontype)否否手势事件类型。如：手势开始、手势更新、手势结束等。xnumber否否坐标x。ynumber否否坐标y。

#### ThreeFingersTap11+

三指轻点手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

名称类型只读可选说明type[ActionType](#ZH-CN_TOPIC_0000002497445590__actiontype)否否手势事件类型。如：手势开始、手势更新、手势结束等。

#### ActionType

手势事件类型。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

名称值说明CANCEL0取消。BEGIN1手势开始。UPDATE2手势更新。END3手势结束。