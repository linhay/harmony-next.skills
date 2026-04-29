# grid-row

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

grid-row是栅格布局容器grid-container的子容器组件，使用flex横向布局，排列每个grid-col容器，justify-content与align-items默认为flex-start，支持折行显示。

**权限列表**

无

**子组件**

仅支持<grid-col>。

**属性**

支持[通用属性](通用属性.md)。

**样式**

除支持[通用样式](通用样式.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| flex-wrap | string | nowrap | 否 | flex容器是单行还是多行显示，该值暂不支持动态修改。可选项有： - nowrap：不换行，单行显示。 - wrap：换行，多行显示。 |
| justify-content | string | flex-start | 否 | flex容器当前行的主轴对齐格式。可选项有： - flex-start：项目位于容器的开头。 - flex-end：项目位于容器的结尾。 - center：项目位于容器的中心。 - space-between：项目位于各行之间留有空白的容器内。 - space-around：项目位于各行之前、之间、之后都留有空白的容器内。 |
| align-items | string | flex-start | 否 | flex容器当前行的交叉轴对齐格式，可选值为： - stretch：弹性元素被在交叉轴方向被拉伸到与容器相同的高度或宽度。 - flex-start：元素向交叉轴起点对齐。 - flex-end：元素向交叉轴终点对齐。 - center：元素在交叉轴居中。 |
| align-content | string | flex-start | 否 | 交叉轴中有额外的空间时，多行内容对齐格式，可选值为： - flex-start：所有行从交叉轴起点开始填充。第一行的交叉轴起点边和容器的交叉轴起点边对齐。接下来的每一行紧跟前一行。 - flex-end：所有行从交叉轴末尾开始填充。最后一行的交叉轴终点和容器的交叉轴终点对齐。同时所有后续行与前一个对齐。 - center：所有行朝向容器的中心填充。每行互相紧挨，相对于容器居中对齐。容器的交叉轴起点边和第一行的距离相等于容器的交叉轴终点边和最后一行的距离。 - space-between：所有行在容器中平均分布。相邻两行间距相等。容器的交叉轴起点边和终点边分别与第一行和最后一行的边对齐。 - space-around：所有行在容器中平均分布，相邻两行间距相等。容器的交叉轴起点边和终点边分别与第一行和最后一行的距离是相邻两行间距的一半。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

不支持宽度相关样式。

**事件**

支持[通用事件](通用事件.md)。

**方法**

支持[通用方法](通用方法.md)。

**示例**

详见[grid-col示例](grid-col.md#ZH-CN_TOPIC_0000002553200933__示例)。