# @ohos.multimedia.avCastPickerParam (投播组件参数)

avCastPickerParam提供了[@ohos.multimedia.avCastPicker](@ohos.multimedia.avCastPicker (投播组件).md)组件状态枚举值。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### AVCastPickerState

投播组件设备列表状态参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE_APPEARING | 0 | 组件显示。 |
| STATE_DISAPPEARING | 1 | 组件消失。 |

#### AVCastPickerStyle12+

投播组件样式参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STYLE_PANEL | 0 | 面板样式。 |
| STYLE_MENU | 1 | 菜单样式。 |

#### AVCastPickerColorMode12+

投播组件显示模式参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 跟随系统模式。 |
| DARK | 1 | 深色模式。 |
| LIGHT | 2 | 浅色模式。 |