# svg

基础容器，主要作为svg的根节点使用，也可以在svg中嵌套使用。

-

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

svg父组件或者svg组件需要定义宽高值，否则不进行绘制。

#### 权限列表

无

#### 子组件

支持[svg](svg.md)、[rect](Rect.md)、[circle](circle.md)、[ellipse](Ellipse.md)、[path](../graphics/path.md)、[line](../graphics/Line.md)、[polygon](Polygon.md)、[polyline](../graphics/Polyline.md)、[text](../graphics/Text.md)、[animate](animate.md)、[animateTransform](animateTransform.md)。

#### 属性

支持svg组件[通用属性](通用属性.md)和以下属性，设置的通用属性会传递给子组件。

名称类型默认值必填描述idstring-否组件的唯一标识。width<length>|<percentage>-否设置组件的宽度。height<length>|<percentage>-否设置组件的高度。x<length>|<percentage>-否设置当前svg的x轴坐标，根svg节点无效。y<length>|<percentage>-否设置当前svg的y轴坐标，根svg节点无效。viewBoxstring-否设置当前svg的视口。支持的格式为<number number number number>，4个参数分别表示min-x, min-y, width and height，viewBox的宽高和svg的宽高不一致，会以中心对齐进行缩放。

#### 示例

```ets
<!-- xxx.hml -->
<div class="container">
  <svg width="400" height="400">
    <svg width="200" height="200" viewBox="0 0 100 100">
      <rect x="10" y="10" width="80" height="80" fill="#00FF00"></rect>
    </svg>
    <rect x="10" y="10" width="80" height="80" fill="red" ></rect>
    <svg x="0" y="0" width="200" height="200" viewBox="0 0 200 200">
      <rect x="10" y="10" width="80" height="80" fill="red"></rect>
    </svg>
    <svg x="0" y="0" width="200" height="200" viewBox="0 0 400 400">
      <rect x="10" y="10" width="80" height="80" fill="blue"></rect>
    </svg>
  </svg>
</div>
```