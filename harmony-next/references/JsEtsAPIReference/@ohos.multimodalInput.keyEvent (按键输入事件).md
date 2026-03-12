# @ohos.multimodalInput.keyEvent (按键输入事件)

设备上报的按键事件，继承自[InputEvent](@ohos.multimodalInput.inputEvent (输入事件).md)。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { Action, Key, KeyEvent } from '@kit.InputKit';
```

#### Action

按键事件类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

名称值说明CANCEL0按键取消。DOWN1按键按下。UP2按键抬起。

#### Key

按键。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

名称类型只读可选说明code[KeyCode](@ohos.multimodalInput.keyCode (键值).md#ZH-CN_TOPIC_0000002529285559__keycode)否否键值。pressedTimenumber否否按键按下时间，单位：μs。deviceIdnumber否否输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。

#### KeyEvent

按键事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

名称类型只读可选说明action[Action](#ZH-CN_TOPIC_0000002529445533__action)否否按键事件类型。key[Key](#ZH-CN_TOPIC_0000002529445533__key)否否按键。unicodeCharnumber否否按键对应的unicode字符。keys[Key](#ZH-CN_TOPIC_0000002529445533__key) []否否当前处于按下状态的按键列表。ctrlKeyboolean否否

当前ctrlKey是否处于按下状态。

true表示处于按下状态，false表示处于抬起状态。

altKeyboolean否否

当前altKey是否处于按下状态。

true表示处于按下状态，false表示处于抬起状态。

shiftKeyboolean否否

当前shiftKey是否处于按下状态。

true表示处于按下状态，false表示处于抬起状态。

logoKeyboolean否否

当前logoKey是否处于按下状态。

true表示处于按下状态，false表示处于抬起状态。

fnKeyboolean否否

当前fnKey是否处于按下状态。

true表示处于按下状态，false表示处于抬起状态。

capsLockboolean否否

当前capsLock是否处于使能状态。

true表示处于使能状态，false表示处于未使能状态。

numLockboolean否否

当前numLock是否处于使能状态。

true表示处于使能状态，false表示处于未使能状态。

scrollLockboolean否否

当前scrollLock是否处于使能状态。

true表示处于使能状态，false表示处于未使能状态。