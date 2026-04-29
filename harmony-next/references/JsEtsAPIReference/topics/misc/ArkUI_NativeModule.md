# ArkUI_NativeModule

**概述**

提供ArkUI在Native侧的通用拖拽及主动发起拖拽能力。更多详细介绍请参考[拖拽事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-drag-event)。

提供ArkUI在Native侧的通用按键事件能力。

提供ArkUI在Native侧的注册手势回调的能力。更多详细介绍请参考[绑定手势事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-bind-gesture-events)。

提供ArkUI在Native侧使用动画回调的能力。更多详细介绍请参考[使用动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-use-animation)。

提供ArkUI在Native侧的UI能力，如UI组件创建销毁、树节点操作、属性设置、事件监听等。更多详细介绍请参考[接入ArkTS页面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-access-the-arkts-page)。

起始版本： 12

**文件汇总**

| 名称 | 描述 |
| --- | --- |
| drag_and_drop.h | 提供NativeDrag相关接口定义。 |
| drawable_descriptor.h | 提供NativeDrawableDescriptor接口的类型定义。 |
| native_animate.h | 提供ArkUI在Native侧的动画接口定义集合。 |
| native_dialog.h | 提供ArkUI在Native侧的自定义弹窗接口定义集合。 |
| native_gesture.h | 提供NativeGesture接口的类型定义。 |
| native_interface.h | 提供NativeModule接口的统一入口函数。 |
| native_interface_focus.h | 定义焦点管理的相关接口，主要用于主动转移焦点或管理控制焦点转移默认行为，控制焦点激活态。 |
| native_key_event.h | 提供NativeKeyEvent相关接口定义。 |
| native_node.h | 提供NativeNode接口的类型定义。 |
| native_node_napi.h | 提供ArkTS侧的FrameNode转换NodeHandle的方式。 |
| native_type.h | 提供NativeModule公共的类型定义。 |
| styled_string.h | 提供ArkUI在Native侧的属性字符串能力。 |