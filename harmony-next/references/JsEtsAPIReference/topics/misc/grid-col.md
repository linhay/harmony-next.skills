# grid-col

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

 从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

grid-col是栅格布局容器grid-row的子容器组件。

**权限列表**

无

**子组件**

支持。

**属性**

除支持[通用属性](通用属性.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| xs | number | object | - | 否 | 在分辨率为xs模式下，设置该项占用列数与偏移列数，当值为number类型时，仅设置列数，也可通过object同时设置占用列数与偏移列数。如 {"span": 1, "offset": 0} |
| sm | number | object | - | 否 | 在分辨率为sm模式下，该项占用列数与偏移列数，当值为number类型时，仅设置列数，也可通过object同时设置占用列数与偏移列数。如 {"span": 1, "offset": 0} |
| md | number | object | - | 否 | 在分辨率为md模式下，该项占用列数与偏移列数，当值为number类型时，仅设置列数，也可通过object同时设置占用列数与偏移列数。如 {"span": 1, "offset": 0} |
| lg | number | object | - | 否 | 在分辨率为lg模式下，该项占用列数与偏移列数，当值为number类型时，仅设置列数，也可通过object同时设置占用列数与偏移列数。如 {"span": 1, "offset": 0} |
| span | number | 1 | 否 | 在未设置明确断点时，默认占用列数。 |
| offset | number | 0 | 否 | 未设置具体分辨率模式下偏移时，当前元素沿容器布局方向，默认偏移的列数。 |

**样式**

除支持[通用样式](通用样式.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| flex-direction | string | row | 否 | flex容器主轴方向。可选项有： - column：垂直方向从上到下 - row：水平方向从左到右 |
| flex-wrap | string | nowrap | 否 | flex容器是单行还是多行显示，该值暂不支持动态修改。可选项有： - nowrap：不换行，单行显示。 - wrap：换行，多行显示。 |
| justify-content | string | flex-start | 否 | flex容器当前行的主轴对齐格式。可选项有： - flex-start：项目位于容器的开头。 - flex-end：项目位于容器的结尾。 - center：项目位于容器的中心。 - space-between：项目位于各行之间留有空白的容器内。 - space-around：项目位于各行之前、之间、之后都留有空白的容器内。 |
| align-items | string | stretch | 否 | flex容器当前行的交叉轴对齐格式，可选值为： - stretch：弹性元素被在交叉轴方向被拉伸到与容器相同的高度或宽度。 - flex-start：元素向交叉轴起点对齐。 - flex-end：元素向交叉轴终点对齐。 - center：元素在交叉轴居中。 |
| align-content | string | flex-start | 否 | 交叉轴中有额外的空间时，多行内容对齐格式，可选值为： - flex-start：所有行从交叉轴起点开始填充。第一行的交叉轴起点边和容器的交叉轴起点边对齐。接下来的每一行紧跟前一行。 - flex-end：所有行从交叉轴末尾开始填充。最后一行的交叉轴终点和容器的交叉轴终点对齐。同时所有后续行与前一个对齐。 - center：所有行朝向容器的中心填充。每行互相紧挨，相对于容器居中对齐。容器的交叉轴起点边和第一行的距离相等于容器的交叉轴终点边和最后一行的距离。 - space-between：所有行在容器中平均分布。相邻两行间距相等。容器的交叉轴起点边和终点边分别与第一行和最后一行的边对齐。 - space-around：所有行在容器中平均分布，相邻两行间距相等。容器的交叉轴起点边和终点边分别与第一行和最后一行的距离是相邻两行间距的一半。 |
| display | string | flex | 否 | 确定该元素视图框的类型，该值暂不支持动态修改。可选值为： - flex：弹性布局 - grid：网格布局 - none：不渲染此元素 |
| grid-template-[columns|rows] | string | 1行1列 | 否 | 用于设置当前网格布局行和列的数量，不设置时默认1行1列，仅当display为grid时生效。 示例：如设置grid-template-columns为： - 50px 100px 60px：分三列，第一列50px，第二列100px，第三列60px； - 1fr 1fr 2fr：分三列，将父组件允许的宽分为4等份，第一列占1份，第二列占一份，第三列占2份； - 30% 20% 50%：分三列，将父组件允许的宽为基准，第一列占30%，第二列占20%，第三列占50%； - repeat(2,100px)：分两列，第一列100px，第二列100px； - auto 1fr 1fr：分三列，第一列自适应内部子组件所需宽度，剩余空间分为两等份，第二列占一份，第三列占一份。 |
| grid-[columns|rows]-gap | <length> | 0 | 否 | 用于设置行与行的间距或者列与列的间距，也可以支持通过grid-gap设置相同的行列间距，仅当display为grid时生效。 |
| grid-row-[start|end] | number | - | 否 | 用于设置当前元素在网格布局中的起止行号，仅当父组件display样式为grid时生效（仅div支持display样式设置为grid）。 |
| grid-column-[start|end] | number | - | 否 | 用于设置当前元素在网格布局中的起止列号，仅当父组件display样式为grid时生效（仅div支持display样式设置为grid）。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

 不支持宽度相关样式。

**事件**

支持[通用事件](通用事件.md)。

**方法**

支持[通用方法](通用方法.md)。

**示例**

```ets
<!-- index.hml -->
<div class="container">
  <grid-container id="mygrid" columns="5" gutter="20px" style="background-color: pink;">
    <grid-row style="height:400px;justify-content:space-around;">
      <grid-col span="2">
        <div style="align-items: center;justify-content: center;height: 100%;width: 100%;">
          <text style="color: dodgerblue;" onclick="getCol">Element text</text>
        </div>
      </grid-col>
      <grid-col span="3" style="background-color:orange;">
        <div style="width: 100%;height: 100%;padding: 20px;align-items: center;">
          <text onclick="getColWidth">Element text</text>
        </div>
      </grid-col>
    </grid-row>
  </grid-container>
</div>
```

```ets
/* index.css */
.container {
  flex-direction: column;
  padding-top: 80px;
}
```

```ets
// index.js
import promptAction from '@ohos.promptAction';
export default {
  getCol(e) {
    this.$element('mygrid').getColumns(function (result) {
      promptAction.showToast({
        message: e.target.id + ' result = ' + result,
        duration: 3000,
      });
    })
  },
  getColWidth(e) {
    this.$element('mygrid').getColumnWidth(function (result) {
      promptAction.showToast({
        message: e.target.id + ' result = ' + result,
        duration: 3000,
      });
    })
  }
```

![image](public_sys-resources/zh-cn_image_0000002522245502.webp)