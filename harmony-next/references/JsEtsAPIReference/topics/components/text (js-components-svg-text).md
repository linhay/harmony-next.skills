[]()[]()

# text

文本，用于呈现一段信息。

-

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

-

文本的展示内容需要写在元素标签内，可嵌套tspan子元素标签分段，可嵌套textPath子元素标签按指定路径绘制。

-

只支持被父元素标签svg嵌套。

-

只支持默认字体sans-serif。

[]()[]()

#### 权限列表

无

[]()[]()

#### 子组件

支持[tspan](tspan.md)、[textpath](../graphics/textPath.md)、[animate](../misc/animate.md)、[animateTransform](../misc/animateTransform.md)。

[]()[]()

#### 属性

支持以下表格中的属性。

名称类型默认值必填描述idstring-否组件的唯一标识。x<length>|<percentage>0否设置组件左上角x轴坐标。y<length>|<percentage>0否设置组件左上角y轴坐标。dx<length>|<percentage>0否设置文本x轴偏移。dy<length>|<percentage>0否设置文本y轴偏移。rotatenumber0否字体以左下角为圆心旋转角度，正数顺时针，负数逆时针。font-size<length>30px否设置文本的尺寸。fill<color>black否字体填充颜色。fill-opacitynumber1.0否字体填充透明度。opacitynumber1否元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。支持属性动画。stroke<color>black否绘制字体边框并指定颜色。stroke-widthnumber1否

字体边框宽度。

默认单位：px

stroke-opacitynumber1.0否字体边框透明度。[]()[]()

#### 示例

```ets
/* xxx.css */
.container {
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    height: 1000px;
    width: 1080px;
}
```

```ets
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text x="20px" y="0px" font-size="30" fill="blue">test x|y</text>
    <text x="150" y="15" font-size="30" fill="blue">test x|y</text>
    <text x="300" y="30" font-size="30" fill="blue" opacity="0.1">test opacity</text>
    <text dx="20" y="30" dy="50" fill="blue" font-size="30">test dx|dy|fill|font-size</text>
    <text x="20" y="150" fill="blue" font-size="30" fill-opacity="0.2">test fill-opacity</text>
    <text x="20" y="200" fill="red" font-size="40">test 0123456789</text>
    <text x="20" y="250" fill="red" font-size="40" fill-opacity="0.2">test 中文</text>
    <text x="20" y="300" rotate="30" fill="red" font-size="40">test rotate</text>
    <text x="20" y="350" fill="blue" font-size="40" stroke="red" stroke-width="2">test stroke</text>
    <text x="20" y="400" fill="white" font-size="40" stroke="red" stroke-width="2" stroke-opacity="0.5">test stroke-opacity</text>
  </svg>
</div>
```

属性动画示例

```ets
/* xxx.css  */
.container {
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    height: 3000px;
    width: 1080px;
}
```

```ets
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text y="50" font-size="30" fill="blue">
        text attribute x|opacity|rotate
      <animate attributeName="x" from="100" by="400" dur="3s" repeatCount="indefinite"></animate>
      <animate attributeName="opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
      <animate attributeName="rotate" from="0" to="360" dur="3s" repeatCount="indefinite"></animate>
    </text>
  </svg>
</div>
```

```ets
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text x="20" y="200" fill="blue">
      text attribute font-size
      <animate attributeName="font-size" from="10" to="50" dur="3s" repeatCount="indefinite">
      </animate>
    </text>
  </svg>
</div>
```

```ets
<!-- xxx.hml -->
<div class="container">
  <svg>
    <text x="20" y="250" font-size="25" fill="blue" stroke="red">
      text attribute stroke
      <animate attributeName="stroke" from="red" to="#00FF00" dur="3s" repeatCount="indefinite"></animate>
    </text>
    <text x="300" y="250" font-size="25" fill="white" stroke="red">
      text attribute stroke-width-opacity
      <animate attributeName="stroke-width" from="1" to="5" dur="3s" repeatCount="indefinite"></animate>
      <animate attributeName="stroke-opacity" from="0.01" to="0.99" dur="3s" repeatCount="indefinite"></animate>
    </text>
  </svg>
</div>
```