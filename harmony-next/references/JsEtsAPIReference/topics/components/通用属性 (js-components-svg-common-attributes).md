[]()[]()

# 通用属性

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

名称类型默认值必填描述fill<color>black否使用简写属性设置元素的填充色。支持属性动画。fill-opacitynumber1否填充色的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。支持属性动画。fill-rulenonzero | evenoddnonzero否nonzero：非零规则； evenodd：奇偶规则。opacitynumber1否元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。支持属性动画。stroke<color>-否设置形状轮廓的颜色。支持属性动画。stroke-dasharray<string>-否指定短划线和缺口的长度。格式为[length length length length]，短划线和缺口的长度中间空格隔开成对出现。stroke-dashoffset<length>0否设置关联虚线数组渲染时的偏移量。支持属性动画。stroke-linejoin[bevel | miter | round]miter否

进行描边时在路径的拐角处使用的形状。

bevel：使用斜角连接路径段；

miter：使用尖角连接路径段；

round：使用圆角连接路径段。

stroke-linecap[butt | round | square]butt否

路径描边时在它们的结尾处使用的形状。

butt：不在路径两端扩展；

round：在路径的末端延伸半个圆，直径等于线宽；

square：在路径的末端延伸一个矩形，宽度等于线宽的一半，高度等于线宽。

stroke-miterlimitnumber4否设置将锐角绘制成斜角的极限值。支持属性动画。stroke-opacitynumber1否轮廓线条的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。支持属性动画。stroke-width<length>1px否设置轮廓线条的宽度。支持属性动画。transform<string>-否

设置组件以及子组件的坐标变换参数。

支持以下格式：

translate(<x> [<y>]) ：沿x[y]轴方向平移。

scale(<x> [<y>]) ：沿x[y]轴缩放。

rotate(<a> [<x> <y>]) ：以(x,y)点进行旋转a度角。

skewX(<a>) ：沿x轴倾斜a度角的变换。

skewY(<a>) ：沿y轴倾斜a度角的变换。