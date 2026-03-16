[]()[]()

# Types

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### CustomBuilderWithId18+

type CustomBuilderWithId = (id: number) => void

组件属性、方法参数可使用CustomBuilderWithId类型来自定义UI描述，并且可以指定组件ID生成用户自定义组件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明idnumber是组件ID。[]()[]()

#### ClickEventListenerCallback12+

type ClickEventListenerCallback = (event: ClickEvent, node?: FrameNode) => void

定义了用于在UIObserver中监听点击事件的回调类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event[ClickEvent](../misc/点击事件.md#ZH-CN_TOPIC_0000002529284807__clickevent)是触发事件监听的点击事件的相关信息。node[FrameNode](../components/FrameNode.md)否触发事件监听的点击事件所绑定的组件。[]()[]()

#### PanListenerCallback19+

type PanListenerCallback = (event: GestureEvent, current: GestureRecognizer, node?: FrameNode) => void

Pan手势事件监听函数类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event[GestureEvent](../misc/手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)是触发事件监听的手势事件的相关信息。current[GestureRecognizer](../misc/手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gesturerecognizer12)是触发事件监听的手势识别器的相关信息。node[FrameNode](../components/FrameNode.md)否触发事件监听的手势事件所绑定的组件。[]()[]()

#### GestureEventListenerCallback12+

type GestureEventListenerCallback = (event: GestureEvent, node?: FrameNode) => void

定义了用于在UIObserver中监听手势的回调类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event[GestureEvent](../misc/手势公共接口.md#ZH-CN_TOPIC_0000002497604864__gestureevent对象说明)是触发事件监听的手势事件的相关信息。node[FrameNode](../components/FrameNode.md)否触发事件监听的手势事件所绑定的组件。[]()[]()

#### NodeIdentity20+

type NodeIdentity = string | number

组件标识。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

类型说明string指定组件id，该id通过通用属性[id](../misc/组件标识.md#ZH-CN_TOPIC_0000002497604824__id)设置。number系统分配的唯一标识的节点UniqueID，可通过[getUniqueId](../components/FrameNode.md#ZH-CN_TOPIC_0000002529284787__getuniqueid12)获取。[]()[]()

#### NodeRenderStateChangeCallback20+

type NodeRenderStateChangeCallback = (state: NodeRenderState, node?: FrameNode) => void

定义了用于在UIObserver中监控某个特定节点渲染状态的回调类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明state[NodeRenderState](Enums (arkts-apis-uicontext-e).md#ZH-CN_TOPIC_0000002497604786__noderenderstate20)是触发事件监听的手势事件的相关信息。node[FrameNode](../components/FrameNode.md)否触发事件监听的手势事件所绑定的组件，如果组件被释放将返回null。[]()[]()

#### GestureListenerCallback20+

type GestureListenerCallback = (info: GestureTriggerInfo) => void

定义了用于在UIObserver中监控特定手势触发信息的回调类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明info[GestureTriggerInfo](../../types/interfaces/Interfaces (其他) (arkts-apis-uicontext-i).md#ZH-CN_TOPIC_0000002529444751__gesturetriggerinfo20)是交互触发的手势详情。[]()[]()

#### PointerStyle12+

type PointerStyle = pointer.PointerStyle

光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

类型说明[pointer.PointerStyle](../../modules/ohos/@ohos.multimodalInput.pointer (鼠标光标).md#ZH-CN_TOPIC_0000002529285561__pointerstyle)光标样式。[]()[]()

#### Context12+

type Context = common.Context

当前组件所在Ability的上下文。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**模型约束：** 此接口仅可在Stage模型下使用。

类型说明[common.Context](../../modules/ohos/@ohos.app.ability.common (Ability公共模块).md#ZH-CN_TOPIC_0000002497444606__context)Context的具体类型为当前Ability关联的Context对象。