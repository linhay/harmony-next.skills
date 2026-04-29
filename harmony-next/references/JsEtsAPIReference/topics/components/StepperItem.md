# [Stepper](../misc/Stepper.md)Item

用作[Stepper]([Stepper](../misc/Stepper.md).md)组件的页面子组件。


-

从API version 8开始支持，从API version 22开始废弃，建议使用[Swiper]([Swiper](../misc/swiper.md).md)替代。

-

 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

支持单个子组件。

#### 接口

[Stepper](../misc/Stepper.md)Item()

创建[Stepper]([Stepper](../misc/Stepper.md).md)组件的页面子组件。


从API version 8开始支持，从API version 22开始废弃，建议使用[Swiper](Swiper.md#ZH-CN_TOPIC_0000002522240824__属性)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### 属性

**prevLabel(deprecated)**

prevLabel(value: string)

设置左侧文本按钮内容，第一页没有左侧文本按钮，当步骤导航器大于一页时，除第一页外默认值都为“返回”。


从API version 8开始支持，从API version 22开始废弃，建议使用[showPrevious](Swiper.md#ZH-CN_TOPIC_0000002522240824__showprevious)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 左侧文本按钮内容。字符串超长时，先缩小再换行（2行）最后截断。 |

**nextLabel(deprecated)**

nextLabel(value: string)

设置右侧文本按钮内容，最后一页默认值为“开始”，其余页默认值为“下一步”。


从API version 8开始支持，从API version 22开始废弃，建议使用[showNext](Swiper.md#ZH-CN_TOPIC_0000002522240824__shownext)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 右侧文本按钮内容。字符串超长时，先缩小再换行（2行）最后截断。 |

**status(deprecated)**

status(value?: ItemState)

设置步骤导航器nextLabel的显示状态。


从API version 8开始支持，从API version 22开始废弃，建议使用[indicatorInteractive](Swiper.md#ZH-CN_TOPIC_0000002522240824__indicatorinteractive12)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ItemState | 否 | 步骤导航器nextLabel的显示状态。 默认值：ItemState.Normal |


- [Stepper](../misc/Stepper.md)Item组件不支持设置通用宽度属性，其宽度默认撑满Stepper父组件。

- [Stepper](../misc/Stepper.md)Item组件不支持设置通用高度属性，其高度由Stepper父组件高度减去label按钮组件高度。

- StepperItem组件不支持设置[aspectRatio](布局约束.md#ZH-CN_TOPIC_0000002553200743__aspectratio)/[constraintSize](尺寸设置.md#ZH-CN_TOPIC_0000002553360703__constraintsize)影响长宽的属性。

#### ItemState枚举说明

步骤导航器nextLabel的显示状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Normal | 0 | 正常状态，右侧文本按钮正常显示，可点击进入下一个[Stepper](../misc/Stepper.md)Item。 说明： 从API version 8开始支持，从API version 22开始废弃，建议使用index替代。 |
| Disabled | 1 | 不可用状态，右侧文本按钮灰度显示，不可点击进入下一个[Stepper](../misc/Stepper.md)Item。 说明： 从API version 8开始支持，从API version 22开始废弃，建议使用indicatorInteractive替代。 |
| Waiting | 2 | 等待状态，右侧文本按钮不显示，显示等待进度条，不可点击进入下一个[Stepper](../misc/Stepper.md)Item。 说明： 从API version 8开始支持，从API version 22开始废弃，建议使用Swiper替代。 |
| Skip | 3 | 跳过状态，右侧文本按钮默认显示“跳过”，此时可在[Stepper](../misc/Stepper.md)的onSkip回调中自定义相关逻辑。 说明： 从API version 8开始支持，从API version 22开始废弃，建议使用index替代。 |

#### 示例

见[Stepper]([Stepper](../misc/Stepper.md).md)。
