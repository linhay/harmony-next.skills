# canvas组件

提供画布组件。用于自定义绘制图形。

该组件从API version 5 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

不支持。

#### 属性

名称类型默认值必填描述idstring-否组件的唯一标识。stylestring-否组件的样式声明。classstring-否组件的样式类，用于引用样式表。refstring-否用来指定指向子元素的引用信息，该引用将注册到父组件的$refs 属性对象上。

#### 事件

名称参数描述click-点击动作触发该事件。longpress-长按动作触发该事件。swipe5+[SwipeEvent](通用事件.md)组件上快速滑动后触发。

#### 样式

名称类型默认值必填描述width<length> | <percentage>5+-否

设置组件自身的宽度。

未设置时组件宽度默认为0。

height<length> | <percentage>5+-否

设置组件自身的高度。

未设置时组件高度默认为0。

padding<length>0否

使用简写属性设置所有的内边距属性。

 该属性可以有1到4个值：

- 指定一个值时，该值指定四个边的内边距。

- 指定两个值时，第一个值指定上下两边的内边距，第二个指定左右两边的内边距。

- 指定三个值时，第一个指定上边的内边距，第二个指定左右两边的内边距，第三个指定下边的内边距。

- 指定四个值时分别为上、右、下、左边的内边距（顺时针顺序）。

margin<length> | <percentage>5+0否

使用简写属性设置所有的外边距属性，该属性可以有1到4个值。

- 只有一个值时，这个值会被指定给全部的四个边。

- 两个值时，第一个值被匹配给上和下，第二个值被匹配给左和右。

- 三个值时，第一个值被匹配给上, 第二个值被匹配给左和右，第三个值被匹配给下。

- 四个值时，会依次按上、右、下、左的顺序匹配 (即顺时针顺序)。

margin-[left|top|right|bottom]<length> | <percentage>5+0否设置左、上、右、下外边距属性。border-width<length>0否使用简写属性设置元素的所有边框宽度。border-color<color>black否使用简写属性设置元素的所有边框颜色。border-radius<length>-否border-radius属性是设置元素的外边框圆角半径。background-color<color>-否设置背景颜色。displaystringflex否

确定一个元素所产生的框的类型，可选值为：

- flex：弹性布局。

- none：不渲染此元素。

[left|top]<length> | <percentage>6+-否

left|top确定元素的偏移位置。

- left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。

- top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。

#### 方法

名称参数描述getContextstring 获取canvas绘图上下文，参数仅支持“2d”，返回值为2D绘制对象，该对象提供具体的2D绘制操作。详见[CanvasRenderingContext2D对象](CanvasRenderingContext2D对象.md)章节。