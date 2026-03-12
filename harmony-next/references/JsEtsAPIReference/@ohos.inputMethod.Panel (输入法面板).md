# @ohos.inputMethod.Panel (输入法面板)

本模块提供对输入法面板的属性管理。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
```

#### PanelInfo

输入法面板属性信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

名称类型只读可选说明type[PanelType](#ZH-CN_TOPIC_0000002497605288__paneltype)否否输入法面板类型。flag[PanelFlag](#ZH-CN_TOPIC_0000002497605288__panelflag)否是

输入法面板状态类型。

- 默认值为固定态。

- 当前仅用于描述软键盘类型的面板的状态。

#### PanelType

输入法面板类型枚举。

**系统能力**：SystemCapability.MiscServices.InputMethodFramework

名称值说明SOFT_KEYBOARD0软键盘类型。STATUS_BAR1状态栏类型。

#### PanelFlag

输入法面板状态类型枚举。

**系统能力**：SystemCapability.MiscServices.InputMethodFramework

名称值说明FLAG_FIXED0固定态面板类型。FLAG_FLOATING1悬浮态面板类型。FLAG_CANDIDATE2

候选词态面板类型。

- 当输入面板为候选词态时，面板为显示用户输入候选词的窗口。

- 输入法服务不会主动控制候选词态面板的显示和隐藏，需要开发者根据情况自行控制。