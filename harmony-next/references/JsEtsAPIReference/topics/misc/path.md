# path

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

绘制路径。

**权限列表**

无

**子组件**

支持[animate](animate.md)、[animateMotion](animateMotion.md)、[animateTransform](animateTransform.md)。

**属性**

支持Svg组件[通用属性](通用属性.md)和以下属性，设置的通用属性会传递给子组件。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| d | string | - | 否 | 设置路径的形状。包含一组字符指令，大写字母为绝对路径，小写字符为相对路径。 字母指令表示的意义如下： - M/m = moveto - L/l = lineto - H/h = horizontal lineto - V/v = vertical lineto - C/c = curveto - S/s = smooth curveto - Q/q = quadratic Bezier curve - T/t = smooth quadratic Bezier curveto - A/a = elliptical Arc - Z/z = closepath |

**示例**

```ets
<!-- xxx.hml -->
<div class="container">
    <svg width="400" height="400">
        <path d="M 10,30 A 20,20 0,0,1 50,30 A 20,20 0,0,1 90,30 Q 90,60 50,90 Q 10,60 10,30 z"
          stroke="blue" stroke-width="3" fill="red">
        </path>
    </svg>
</div>
```

![image](public_sys-resources/zh-cn_image_0000002553205467.webp)