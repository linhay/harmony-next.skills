[]()[]()

# list

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。

[]()[]()

#### 权限列表

无

[]()[]()

#### 子组件

仅支持<[list-item-group](list-item-group.md)>和<[list-item](list-item (js-components-container-list-item).md)>。

[]()[]()

#### 属性

除支持[通用属性](通用属性 (js-components-common-attributes).md)外，还支持如下属性：

名称类型默认值必填描述scrollpagebooleanfalse否设置为true时，将 list 顶部页面中非 list 部分随 list 一起滑出可视区域，当list方向为row时，不支持此属性。cachedcountnumber0否

长列表延迟加载时list-item最少缓存数量。

可视区域外缓存的list-item数量少于该值时，会触发requestitem事件。

scrollbarstringoff否

侧边滑动栏的显示模式（当前只支持纵向）：

- off：不显示。

- auto：按需显示(触摸时显示，2s后消失)。

- on：常驻显示。

scrolleffectstringspring否

滑动效果，目前支持如下滑动效果：

- spring：弹性物理动效，滑动到边缘后可以根据初始速度或通过触摸事件继续滑动一段距离，松手后回弹。

- fade：渐隐物理动效，滑动到边缘后展示一个波浪形的渐隐，根据速度和滑动距离的变化渐隐也会发生一定的变化。

- no：滑动到边缘后无效果。

indexerboolean | Array<string>false否

是否展示侧边栏快速字母索引栏。设置为true或者自定义索引时，索引栏会显示在列表右边界处。示例：

"indexer" : "true"表示使用默认字母索引表。

"indexer" : "false"表示无索引。

"indexer" : ['#','1','2','3','4','5','6','7','8']表示自定义索引表。自定义时"#"必须要存在。

indexer属性生效需要flex-direction属性配合设置为column，且columns属性设置为1。

点击索引条进行列表项索引需要list-item子组件配合设置相应的[section属性](list-item (js-components-container-list-item).md#ZH-CN_TOPIC_0000002497604990__属性)。

indexercircle5+boolean-否

是否为环形索引。

穿戴设备默认为true，其他为false。indexer为false时不生效。

indexermulti5+booleanfalse否

是否开启索引条多语言功能。

indexer为false时不生效。

- false：不开启索引条多语言功能。

- true：开启索引条多语言功能。

indexerbubble5+booleantrue否

是否开启索引切换的气泡提示。

indexer为false时不生效。

- false：不开启索引切换的气泡提示。

- true：开启索引切换的气泡提示。

divider5+booleanfalse否

item是否自带分隔线。

其样式参考样式列表的divider-color、divider-height、divider-length、divider-origin。

- false：item不自带分隔线。

- true：item自带分隔线。

shapemodestringdefault否

侧边滑动栏的形状类型。

- default：不指定，跟随主题；

- rect：矩形；

- round：圆形。

updateeffectbooleanfalse否

用于设置当list内部的item发生删除或新增时是否支持动效。

- false：新增删除item时无过渡动效。

- true：新增删除item时播放过程动效。

chainanimation5+booleanfalse否

用于设置当前list是否启用链式联动动效，开启后列表滑动以及顶部和底部拖拽时会有链式联动的效果。链式联动效果：list内的list-item间隔一定距离，在基本的滑动交互行为下，主动对象驱动从动对象进行联动，驱动效果遵循弹簧物理动效。

- false：不启用链式联动。

- true：启用链式联动。

不支持动态修改。

同时配置了indexer，链式动效不生效。

如配置了链式动效，list-item的sticky不生效。

initialindexnumber0否用于设置当前List初次加载时视口起始位置显示的item，默认为0，即显示第一个item，如设置的序号超过了最后一个item的序号，则设置不生效，当同时设置了initialoffset属性时，当前属性不生效。当indexer为true或者scrollpage为true时，不生效。initialoffset<length>0否用于设置当前List初次加载时视口的起始偏移量，偏移量无法超过当前List可滑动的范围，如果超过会被截断为可滑动范围的极限值。当indexer为true或者scrollpage为true时，不生效。selected5+string-否指定当前列表中被选中激活的项，可选值为list-item的section属性值。[]()[]()

#### 样式

除支持[通用样式](通用样式 (js-components-common-styles).md)外，还支持如下样式：

名称类型默认值必填描述divider-color5+<color>transparent否item分隔线颜色，仅当list的divider属性为true时生效。divider-height5+<length>1否item分隔线高度，仅当list的divider属性为true时生效。divider-length5+<length>主轴宽度否item分隔线长度，不设置时最大长度为主轴宽度，具体长度取决于divider-origin，仅当list的divider属性为true时生效。divider-origin5+<length>0否item分隔线相对于item主轴起点位置的偏移量，仅当list的divider属性为true时生效。flex-directionstringcolumn否

设置flex容器主轴的方向，指定flex项如何放置在flex容器中，可选值为：

- column：主轴为纵向。

- row：主轴为横向。

其他组件默认值为row，在list组件中默认值为column。

columnsnumber1否

list交叉轴方向的显示列数，默认为1列。

设置多列时，在list交叉轴上进行均分，每一列大小相同。

align-itemsstringstretch否

list每一列交叉轴上的对齐格式，可选值为：

- stretch：弹性元素被在交叉轴方向被拉伸到与容器相同的高度或宽度。

- flex-start：元素向交叉轴起点对齐。

- flex-end：元素向交叉轴终点对齐。

- center：元素在交叉轴居中。

align-items样式作用在每一列的子元素上，列与列之间采用均分方式布局。

item-extent<length> | <percentage>-否设置内部item为固定大小，设置为百分比格式时，指相对于list的视口主轴方向长度的百分比。fade-color<color>grey否设置渐隐物理动效的颜色。当滑动效果设置为渐隐物理动效时生效。scrollbar-color6+<color>-否设置滚动条的颜色。scrollbar-width6+<length>-否设置滚动条的宽度。scrollbar-offset6+<length>0否设置滚动条距离List默认位置的偏移量，只支持正数，默认位置在List右边缘，可以通过这个偏移量调整滚动条的水平位置，如果滚动条绘制在list外部，而list父组件有裁剪，会导致滚动条被裁剪。[]()[]()

#### 事件

除支持[通用事件](通用事件 (js-components-common-events).md)外，还支持如下事件：

名称参数描述indexerchange5+{ local: booleanValue }

多语言索引条切换事件，仅当indexer属性为true，indexermulti为true时生效。booleanValue取值为true或false：

- true: 当前展示本地索引。

- false: 当前展示字母索引。

scroll{ scrollX: scrollXValue, scrollY: scrollYValue, scrollState: stateValue }

列表滑动的偏移量和状态回调。

stateValue为0时表示列表滑动已停止。

stateValue为1时表示列表在用户触摸状态下处于滑动中。

stateValue为2时表示列表在用户松手状态下处于滑动中。

scrollbottom-当前列表已滑动到底部位置。scrolltop-当前列表已滑动到顶部位置。scrollend-列表滑动已经结束。scrolltouchup-手指已经抬起且列表仍在惯性滑动。requestitem-

请求创建新的list-item。

长列表延迟加载时，可视区域外缓存的list-item数量少于cachedcount时，会触发该事件。

rotation7+{ rotateValue: number }返回表冠旋转角度增量值，仅智能穿戴支持。[]()[]()

#### 方法

支持[通用方法](../misc/通用方法.md)外，还支持如下方法：

名称参数描述scrollTo{ index: number(指定位置) }list滑动到指定index的item位置。scrollTop{ smooth: boolean }

smooth缺省为false，表示直接滚动到顶部。

smooth为true，表示平滑滚动到顶部。

scrollBottom{ smooth: boolean }

smooth缺省为false，表示直接滚动到底部。

smooth为true，表示平滑滚动到底部。

scrollPage{ reverse: boolean, smooth: boolean }

reverse缺省值为false，表示下一页，无完整页则滚动到底部。

reverse为true，表示上一页，无完整页则滚动到顶部。

smooth缺省值为false，表示直接滚动一页。

smooth为true，表示平滑滚动一页。

scrollArrow{ reverse: boolean, smooth: boolean }

reverse缺省值为false，表示向底部方向滑动一段距离，无足够距离则滚动到底部。

reverse为true，表示向顶部方向滑动一段距离，无足够距离则滚动到顶部。

smooth缺省值为false，表示直接滚动。

smooth为true，表示平滑滚动。

collapseGroup{ groupid: string }

收起指定的group。

groupid：需要收拢的group的id。

当未指定groupid时收起所有group。

expandGroup{ groupid: string }

展开指定的group。

groupid：需要展开的group的id。

当groupid未指定时展开所有的group。

currentOffset-返回当前滑动的偏移量。返回值类型是Object，返回值说明请参见表1 currentOffset返回对象属性说明。

**表1** currentOffset返回对象属性说明

名称类型备注xnumber当前x轴滑动偏移量，单位为px。ynumber当前y轴滑动偏移量，单位为px。[]()[]()

#### 示例

```ets
<!-- index.hml -->
<div class="container">
  <list class="todo-wrapper">
    <list-item for="{{todolist}}" class="todo-item">
      <div style="flex-direction: column;align-items: center;justify-content: center;">
        <text class="todo-title">{{$item.title}}</text>
        <text class="todo-title">{{$item.date}}</text>
      </div>
    </list-item>
  </list>
</div>
```

```ets
/* index.css */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}
.todo-wrapper {
  width: 100%;
  height: 300px;
}
.todo-item {
  width: 100%;
  height: 120px;
  justify-content:center;
}
.todo-title {
  width: 100%;
  height: 80px;
  text-align: center;
}
```

```ets
// index.js
export default {
  data: {
    todolist: [{
      title: '刷题',
      date: '2021-12-31 10:00:00'
    }, {
      title: '看电影',
      date: '2021-12-31 20:00:00'
    }],
  },
}
```