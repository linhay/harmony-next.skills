# line

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

绘制线条。

#### 权限列表

无

#### 子组件

支持[animate](animate.md)、[animateMotion](animateMotion.md)、[animateTransform](animateTransform.md)。

#### 属性

支持Svg组件[通用属性](通用属性.md)和以下属性。

名称类型默认值必填描述idstring-否组件的唯一标识。x1<length>|<percentage>-否设置线条起点的x轴坐标。支持属性动画。y1<length>|<percentage>-否设置线条起点的y轴坐标。支持属性动画。x2<length>|<percentage>-否设置线条终点的x轴坐标。支持属性动画。y2<length>|<percentage>-否设置线条终点的y轴坐标。支持属性动画。

#### 示例

```ets
<!-- xxx.hml -->
<div class="container">
    <svg width="400" height="400">
        <line x1="10" x2="300" y1="50" y2="50" stroke-width="4" fill="white" stroke="blue"></line>
        <line x1="10" x2="300" y1="100" y2="100" stroke-width="4" fill="white" stroke="blue"></line>
        <line x1="10" x2="300" y1="150" y2="150" stroke-width="10" stroke="red" stroke-dasharray="5 3"
            stroke-dashoffset="3"></line>
        <!--round：在路径的末端延伸半个圆，直径等于线宽-->
        <line x1="10" x2="300" y1="200" y2="200" stroke-width="10" stroke="black" stroke-linecap="round"></line>
        <!--butt：不在路径两端扩展-->
        <line x1="10" x2="300" y1="220" y2="220" stroke-width="10" stroke="black" stroke-linecap="butt"></line>
        <!-- square：在路径的末端延伸一个矩形，宽度等于线宽的一半，高度等于线宽 -->
        <line x1="10" x2="300" y1="240" y2="240" stroke-width="10" stroke="black" stroke-linecap="square"></line>
    </svg>
</div>
```