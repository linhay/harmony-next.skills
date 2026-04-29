# marquee

跑马灯组件，用于展示一段单行滚动的文字。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

该组件从API version 4 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**子组件**

不支持。

**属性**

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| scrollamount | number | 6 | 否 | 跑马灯每次滚动时移动的最大长度。 |
| id | string | - | 否 | 组件的唯一标识。 |
| style | string | - | 否 | 组件的样式声明。 |
| class | string | - | 否 | 组件的样式类，用于引用样式表。 |
| ref | string | - | 否 | 用来指定指向子元素的引用信息，该引用将注册到父组件的$refs 属性对象上。 |

**事件**

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| click | - | 点击动作触发该事件。 |
| longpress | - | 长按动作触发该事件。 |
| swipe5+ | SwipeEvent | 组件上快速滑动后触发。 |

**样式**

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | <color> | #ffffff | 否 | 设置跑马灯中文字的文本颜色。 |
| font-size | <length> | 30 | 否 | 设置跑马灯中文字的文本尺寸。 |
| font-family | string | SourceHanSansSC-Regular | 否 | 字体。目前仅支持SourceHanSansSC-Regular 字体。 |
| width | <length> | <percentage>5+ | - | 否 | 设置组件自身的宽度。 未设置时组件宽度默认为0。 |
| height | <length> | <percentage>5+ | - | 否 | 设置组件自身的高度。 未设置时组件高度默认为0。 |
| padding | <length> | 0 | 否 | 使用简写属性设置所有的内边距属性。  该属性可以有1到4个值： - 指定一个值时，该值指定四个边的内边距。 - 指定两个值时，第一个值指定上下两边的内边距，第二个指定左右两边的内边距。 - 指定三个值时，第一个指定上边的内边距，第二个指定左右两边的内边距，第三个指定下边的内边距。 - 指定四个值时分别为上、右、下、左边的内边距（顺时针顺序）。 |
| padding-[left|top|right|bottom] | <length> | 0 | 否 | 设置左、上、右、下内边距属性。 |
| margin | <length> | <percentage>5+ | 0 | 否 | 使用简写属性设置所有的外边距属性，该属性可以有1到4个值。 - 只有一个值时，这个值会被指定给全部的四个边。 - 两个值时，第一个值被匹配给上和下，第二个值被匹配给左和右。 - 三个值时，第一个值被匹配给上； 第二个值被匹配给左和右；第三个值被匹配给下。 - 四个值时，会依次按上、右、下、左的顺序匹配 (即顺时针顺序)。 |
| margin-[left|top|right|bottom] | <length> | <percentage>5+ | 0 | 否 | 设置左、上、右、下外边距属性。 |
| border-width | <length> | 0 | 否 | 使用简写属性设置元素的所有边框宽度。 |
| border-color | <color> | black | 否 | 使用简写属性设置元素的所有边框颜色。 |
| border-radius | <length> | - | 否 | border-radius属性是设置元素的外边框圆角半径。 |
| background-color | <color> | - | 否 | 设置背景颜色。 |
| opacity5+ | number | 1 | 否 | 元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。 |
| display | string | flex | 否 | 确定一个元素所产生的框的类型，可选值为： - flex：弹性布局。 - none：不渲染此元素。 |
| [left|top] | <length> | <percentage>6+ | - | 否 | left|top确定元素的偏移位置。 - left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。 - top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。 |

**示例**

```ets
<!-- xxx.hml -->
<div class="container">
  <marquee class="customMarquee" scrollamount="{{scrollAmount}}">{{marqueeCustomData}}</marquee>
  <text class="text" onclick="addSpeed">speed+</text>
  <text class="text" onclick="downSpeed">speed-</text>
  <text class="text" onclick="changeData">changeData</text>
</div>
```

```ets
/* xxx.css */
.container {
  flex-direction: column;
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
}
.customMarquee {
  width: 50%;
  height: 80px;
  padding: 10px;
  margin: 20px;
  border-width: 4px;
  border-color: #ffffff;
  border-radius: 20px;
  font-size: 38px;
}
.text {
  font-size: 30px;
  text-align: center;
  width: 30%;
  height: 10%;
  margin-top: 5%;
  background-color: #f2f2f2;
  border-radius: 40px;
  color: #0d81f2;
}
```

```ets
// xxx.js
export default {
  data: {
    scrollAmount: 30,
    marqueeCustomData: 'Custom marquee Custom marquee Custom marquee'
  },
  addSpeed() {
    this.scrollAmount++;
  },
  downSpeed() {
    this.scrollAmount--;
  },
  changeData() {
    this.marqueeCustomData = 'Change Data Change Data Change Data';
  }
```

![image](public_sys-resources/zh-cn_image_0000002522085682.webp)