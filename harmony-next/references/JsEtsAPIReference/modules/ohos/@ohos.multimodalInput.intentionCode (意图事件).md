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

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTENTION_UNKNOWN | -1 | 未知意图 |
| INTENTION_UP | 1 | 上 |
| INTENTION_DOWN | 2 | 下 |
| INTENTION_LEFT | 3 | 左 |
| INTENTION_RIGHT | 4 | 右 |
| INTENTION_SELECT | 5 | 选中 |
| INTENTION_ESCAPE | 6 | 逃逸 |
| INTENTION_BACK | 7 | 返回 |
| INTENTION_FORWARD | 8 | 前进 |
| INTENTION_MENU | 9 | 菜单 |
| INTENTION_PAGE_UP | 11 | 上一页 |
| INTENTION_PAGE_DOWN | 12 | 下一页 |
| INTENTION_ZOOM_OUT | 13 | 缩小键 |
| INTENTION_ZOOM_IN | 14 | 放大键 |