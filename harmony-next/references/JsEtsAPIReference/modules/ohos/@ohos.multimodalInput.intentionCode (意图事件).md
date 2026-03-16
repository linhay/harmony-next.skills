# @ohos.multimodalInput.intentionCode (意图事件)

将键盘输入设备的原始事件映射为归一化交互的意图事件，如键盘上空格键映射后的事件为INTENTION_SELECT，意图为选中。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { IntentionCode } from '@kit.InputKit';
```

#### IntentionCode

意图事件枚举值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

名称值说明INTENTION_UNKNOWN-1未知意图INTENTION_UP1上INTENTION_DOWN2下INTENTION_LEFT3左INTENTION_RIGHT4右INTENTION_SELECT5选中INTENTION_ESCAPE6逃逸INTENTION_BACK7返回INTENTION_FORWARD8前进INTENTION_MENU9菜单INTENTION_PAGE_UP11上一页INTENTION_PAGE_DOWN12下一页INTENTION_ZOOM_OUT13缩小键INTENTION_ZOOM_IN14放大键