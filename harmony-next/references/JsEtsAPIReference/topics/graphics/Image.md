# image

图片组件，用来渲染展示图片。

该组件从API version 4 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

不支持。

#### 属性

名称类型必填描述srcstring否

图片的路径，支持的图片格式包括png、jpg。

说明：部分轻量级设备不支持原图片格式的解析。所以，在应用编译阶段，图片会被直接编译为可解析的位图（总字节数约：图片长x宽x4），并打包在应用安装包里，这会增加安装包的大小。因此，在使用图片资源时，应尽量控制图片的分辨率，尺寸越大的图片对于空间的占用越明显。

idstring否组件的唯一标识。stylestring否组件的样式声明。classstring否组件的样式类，用于引用样式表。refstring否用来指定指向子元素的引用信息，该引用将注册到父组件的$refs 属性对象上。

#### 事件

名称参数描述click-点击动作触发该事件。longpress-长按动作触发该事件。swipe5+[SwipeEvent](../misc/通用事件.md)组件上快速滑动后触发。

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

padding-[left|top|right|bottom]<length>0否设置左、上、右、下内边距属性。margin<length> | <percentage>5+0否

使用简写属性设置所有的外边距属性，该属性可以有1到4个值。

- 只有一个值时，这个值会被指定给全部的四个边。

- 两个值时，第一个值被匹配给上和下，第二个值被匹配给左和右。

- 三个值时，第一个值被匹配给上, 第二个值被匹配给左和右，第三个值被匹配给下。

- 四个值时，会依次按上、右、下、左的顺序匹配 (即顺时针顺序)。

margin-[left|top|right|bottom]<length> | <percentage>5+0否设置左、上、右、下外边距属性。border-width<length>0否使用简写属性设置元素的所有边框宽度。border-color<color>black否使用简写属性设置元素的所有边框颜色。border-radius<length>-否border-radius属性是设置元素的外边框圆角半径。background-color<color>-否设置背景颜色。opacitynumber1否元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。displaystringflex否

确定一个元素所产生的框的类型，可选值为：

- flex：弹性布局。

- none：不渲染此元素。

[left|top]<length> | <percentage>6+-否

left|top确定元素的偏移位置。

- left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。

- top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。

#### 示例

```ets
<!-- xxx.hml -->
<div class="container">
  <image src="common/images/hw_right.png" style="width: 300px; height: 300px; border-color: red; border-width: 2px;">
  </image>
</div>
```

```ets
/* xxx.css */
.container {
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
```