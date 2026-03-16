[]()[]()

# divider

分隔器组件，分隔不同内容块/内容元素。可用于列表或界面布局。

从API Version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

[]()[]()

#### 属性

除支持[通用属性](通用属性 (js-service-widget-common-attributes).md)外，还支持如下属性：

名称类型默认值必填描述verticalbooleanfalse否使用水平分割线还是垂直分割线，默认水平分割线。[]()[]()

#### 样式

仅支持如下样式：

名称类型默认值必填描述margin<length>0否使用简写属性设置所有的外边距属性，该属性可以有1到4个值。margin-[left|top|right|bottom]<length>0否使用简写属性设置左、上、右、下外边距属性，类型length，单位px，默认值0。color<color>-否设置分割线颜色。stroke-width<length>1否设置分割线宽度。displaystringflex否确定分割线所产生的框的类型。值flex/none，默认值flex。visibilitystringvisible否是否显示分割线，不可见的框会占用布局。visible代表显示元素，hidden代表不显示元素。line-capstringbutt否

设置分割线条的端点样式，默认为butt，可选值为：

- "butt"：分割线两端为平行线。

- "round"：分割线两端额外添加半圆。

- "square"：分割线两端额外添加半方形。

"round"和"square"会额外增加一个线宽的分割线长度。

flexnumber-否

规定了分割线如何适应父组件中的可用空间。作为一个简写属性，用来设置组件的flex-grow。

仅父容器为<div>、<list-item>、<tabs>时生效。

flex-grownumber0否

设置分割线的伸展因子，指定父组件容器主轴方向上剩余空间（容器本身大小减去所有flex项加起来的大小）的分配系数。0为不伸展。

仅父容器为<div>、<list-item>、<tabs>时生效。

flex-shrinknumber1否

设置分割线的收缩因子，flex元素仅在默认宽度之和大于容器的时候才会发生收缩，0为不收缩。

仅父容器为<div>、<list-item>、<tabs>时生效。

flex-basis<length>-否

设置分割线在主轴方向上的初始大小。

仅父容器为<div>、<list-item>、<tabs>时生效。

[]()[]()

#### 事件

不支持。

[]()[]()

#### 示例

```ets
<!-- xxx.hml -->
<div class="container">
  <div class="content">
    <divider class="divider" vertical="false"></divider>
  </div>
</div>
```

```ets
/* xxx.css */
.container {
  margin: 20px;
  flex-direction:column;
  width:100%;
  height:100%;
  align-items:center;
}
.content{
  width:80%;
  height:40%;
  margin-top:100px;
  border:1px solid #000000;
  align-items: center;
  justify-content: center;
  flex-direction:column;
}
.divider {
  margin: 10px;
  color: #ff0000ff;
  stroke-width: 3px;
  line-cap: round;
}
```

**4*4卡片**