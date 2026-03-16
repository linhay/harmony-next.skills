[]()[]()

# swiper

滑动容器，提供切换子组件显示的能力。

该组件从API version 4 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

[]()[]()

#### 子组件

支持除<list>之外的子组件。

[]()[]()

#### 属性

名称类型默认值必填描述indexnumber0否当前在容器中显示的子组件的索引值。loopbooleantrue否是否开启循环轮播。true为开启循环，false为不开启循环。durationnumber-否子组件切换的动画时长。verticalbooleanfalse否

是否为纵向滑动，纵向滑动时采用纵向的指示器。true为纵向滑动，false为水平滑动。

不支持动态修改。

idstring-否组件的唯一标识。stylestring-否组件的样式声明。classstring-否组件的样式类，用于引用样式表。refstring-否用来指定指向子元素的引用信息，该引用将注册到父组件的$refs 属性对象上。[]()[]()

#### 事件

名称参数描述change{ index: currentIndex }当前显示的组件索引变化时触发该事件。click-点击动作触发该事件。longpress-长按动作触发该事件。swipe5+[SwipeEvent](../misc/通用事件 (js-lite-common-events).md)组件上快速滑动后触发。[]()[]()

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

margin-[left|top|right|bottom]<length> | <percentage>5+0否设置左、上、右、下外边距属性。border-width<length>0否使用简写属性设置元素的所有边框宽度。border-color<color>black否使用简写属性设置元素的所有边框颜色。border-radius<length>-否border-radius属性是设置元素的外边框圆角半径。background-color<color>-否设置背景颜色。opacity5+number1否元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。displaystringflex否

确定一个元素所产生的框的类型，可选值为：

- flex：弹性布局。

- none：不渲染此元素。

[left|top]<length> | <percentage>6+-否

left|top确定元素的偏移位置。

- left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。

- top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。

[]()[]()

#### 方法

名称参数描述rotation{ focus: boolean }控制swiper是否请求旋转表冠的焦点。设置focus参数为true，swiper将获取旋转表冠的焦点，允许用户通过旋转表冠来滚动选择器中的选项；设置为false将释放旋转表冠的焦点。[]()[]()

#### 示例

```ets
<!-- xxx.hml -->
<swiper class="container" index="{{index}}" ref="swiperObj">
    <div class="swiper-item primary-item">
        <text>1</text>
    </div>
    <div class="swiper-item warning-item">
        <text>2</text>
    </div>
    <div class="swiper-item success-item">
        <text>3</text>
    </div>
</swiper>
```

```ets
/* xxx.css */
.container {
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.swiper-item {
  width: 454px;
  height: 454px;
  justify-content: center;
  align-items: center;
}
.primary-item {
  background-color: #007dff;
}
.warning-item {
  background-color: #ff7500;
}
.success-item {
  background-color: #41ba41;
}
```

```ets
/* xxx.js */
export default {
    data: {
        index: 1
    },
    onShow() {
        this.$refs.swiperObj.rotation({focus: true});
    }
}
```