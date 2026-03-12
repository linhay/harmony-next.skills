# polygon

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

绘制多边形。

#### 权限列表

无

#### 子组件

支持[animate](animate.md)、[animateMotion](animateMotion.md)、[animateTransform](animateTransform.md)。

#### 属性

支持Svg组件[通用属性](通用属性.md)和以下属性。

名称类型默认值必填描述idstring-否组件的唯一标识。pointsstring-否

设置多边形的多个坐标点。

格式为[x1,y1 x2,y2 x3,y3]。

支持属性动画，如果属性动画里设置的动效变化值的坐标个数与原始points的格式不一样，则无效。

#### 示例

```ets
<!-- xxx.hml -->
<div class="container">
  <svg fill="white" stroke="blue" width="400" height="400">
    <polygon points="10,110 60,35 60,85 110,10" fill="red"></polygon>
    <polygon points="10,200 60,125 60,175 110,100" stroke-dasharray="10 5" stroke-dashoffset="3"></polygon>
  </svg>
</div>
```