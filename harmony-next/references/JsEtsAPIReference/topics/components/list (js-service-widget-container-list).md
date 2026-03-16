[]()[]()

# list

列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。

从API Version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

针对卡片场景，建议开发者控制list中的子节点list-item的数量（建议30条以内）以便获取更好的卡片交互体验。

[]()[]()

#### 子组件

仅支持<[list-item](list-item (js-service-widget-container-list-item).md)>子组件。

[]()[]()

#### 属性

除支持[通用属性](../system-services/通用属性 (js-service-widget-common-attributes).md)外，还支持如下属性：

名称类型默认值必填描述cachedcountnumber0否长列表延迟加载时list-item最少缓存数量。scrollbarstringoff否

侧边滑动栏的显示模式（当前只支持纵向）：

- off：不显示。

- auto：按需显示(触摸时显示，2s后消失)。

- on：常驻显示。

scrolleffectstringspring否

滑动效果，目前支持如下滑动效果：

- spring：弹性物理动效，滑动到边缘后可以根据初始速度或通过触摸事件继续滑动一段距离，松开后回弹。

- fade：渐隐物理动效，滑动到边缘后展示一个波浪形的渐隐，根据速度和滑动距离的变化渐隐也会发生一定的变化。

- no：滑动到边缘后无效果。

dividerbooleanfalse否

item是否自带分隔线。

其样式参考[样式列表](#ZH-CN_TOPIC_0000002529285053__样式)的divider-color、divider-height、divider-length、divider-origin。

- false：item不自带分隔线。

- true：item自带分隔线。

shapemodestringdefault否

侧边滑动栏的形状类型。

- default：不指定，跟随主题。

- rect：矩形。

- round：圆形。

updateeffectbooleanfalse否

用于设置当list内部的item发生删除或新增时是否支持动效。

- false：新增删除item时无过渡动效。

- true：新增删除item时播放过程动效。

initialindexnumber0否用于设置当前List初次加载时视口起始位置显示的item，默认为0，即显示第一个item，如设置的序号超过了最后一个item的序号，则设置不生效，当同时设置了initialoffset属性时，当前属性不生效。initialoffset<length>0否用于设置当前List初次加载时视口的起始偏移量，偏移量无法超过当前List可滑动的范围，如果超过会被截断为可滑动范围的极限值。selectedstring-否指定当前列表中被选中激活的项，可选值为list-item的section属性值。[]()[]()

#### 样式

除支持[通用样式](../system-services/通用样式 (js-service-widget-common-styles).md)外，还支持如下样式：

名称类型默认值必填描述divider-color<color>transparent否item分隔线颜色，仅当list的divider属性为true时生效。divider-height<length>1否item分隔线高度，仅当list的divider属性为true时生效。divider-length<length>主轴宽度否item分隔线长度，不设置时最大长度为主轴宽度，具体长度取决于divider-origin，仅当list的divider属性为true时生效。divider-origin<length>0否item分隔线相对于item主轴起点位置的偏移量，仅当list的divider属性为true时生效。flex-directionstringcolumn否

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

item-extent<length> | <percentage>-否设置内部item为固定大小，设置为百分比格式时，指相对于list的视口主轴方向长度的百分比。fade-color<color>grey否设置渐隐物理动效的颜色。当滑动效果设置为渐隐物理动效时生效。scrollbar-color<color>-否设置滚动条的颜色。scrollbar-width<length>-否设置滚动条的宽度。scrollbar-offset<length>0否设置滚动条距离List默认位置的偏移量，只支持正数，默认位置在List右边缘，可以通过这个偏移量调整滚动条的水平位置，如果滚动条绘制在list外部，而list父组件有裁剪，会导致滚动条被裁剪。[]()[]()

#### 事件

支持[通用事件](../system-services/通用事件 (js-service-widget-common-events).md)。

[]()[]()

#### 示例

```ets
<!-- index.hml -->
<div class="container">
  <list class="todo-wrapper">
    <list-item for="{{todolist}}" class="todo-item">
      <text class="todo-title">{{$item.title}}</text>
      <text class="todo-title">{{$item.date}}</text>
    </list-item>
  </list>
</div>
```

```ets
{
  "data": {
    "todolist": [{
      "title": "work",
      "date": "2021-12-31 10:00:00"
    }, {
      "title": "watch movie",
      "date": "2021-12-31 20:00:00"
    }]
  }
}
```

```ets
/* index.css */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.todo-wrapper {
  width: 454px;
  height: 300px;
}
.todo-item {
  width: 454px;
  height: 80px;
  flex-direction: column;
}
.todo-title {
  width: 454px;
  height: 40px;
  text-align: center;
}
```

**4*4卡片**