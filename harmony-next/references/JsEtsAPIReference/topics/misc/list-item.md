# list-item

<[list](list.md)>的子组件，用来展示列表具体item。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

由于父元素list组件的align-items默认样式为stretch，该组件宽度默认充满list组件。设置父元素list组件的align-items样式为非stretch来生效自定义宽度。

-

list-item组件开发避免长按和拖动操作。

**子组件**

支持。

**属性**

除支持[通用属性](通用属性.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | string | default | 否 | list-item类型，默认值为default，同一list中可以包含多种type的list-item，相同type的list-item需要确保渲染后的视图布局也相同，如果type固定，则使用show属性代替if属性，确保视图布局不变。 |
| section | string | - | 否 | 当前item的匹配字符串，如不设置则为空。不支持动态修改。group内只有主item设置有效。 |
| sticky | string | none | 否 | 设置当前item是否为吸顶item以及其吸顶消失的效果，当前仅支持纵向list，group内部的item不可吸顶，设置该属性无效。 - none：当前item不吸顶。 - normal：当前item吸顶，消失效果滑动消失。 - opacity：当前item吸顶，消失效果渐隐消失，仅在智能穿戴上支持。 |
| clickeffect | boolean | true | 否 | 设置当前item是否有点击动效。 - false：item点击时无点击动效。 - true：item点击时有点击动效。 |

**样式**

除支持[通用样式](通用样式.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| column-span | <number> | 1 | 否 | 当前的list-item需要在list中占据的列的数量，默认占一列，仅在list为多列时生效。 |
| click-color | <color> | - | 否 | 设置列表项按压点击时的背板颜色。 |

**事件**

支持[通用事件](通用事件.md)。

**示例**

详见[list示例](list.md#ZH-CN_TOPIC_0000002553200975__示例)。