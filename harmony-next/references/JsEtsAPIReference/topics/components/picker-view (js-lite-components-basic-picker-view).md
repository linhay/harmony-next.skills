[]()[]()

# picker-view

嵌入页面的滑动选择器。

该组件从API version 4 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

[]()[]()

#### 子组件

不支持。

[]()[]()

#### 属性

名称类型默认值必填描述typestringtext否

设置滑动选择器的类型，该属性不支持动态修改，可选项有：

- text：文本选择器。

- time：时间选择器。

idstring-否组件的唯一标识。stylestring-否组件的样式声明。classstring-否组件的样式类，用于引用样式表。refstring-否用来指定指向子元素的引用信息，该引用将注册到父组件的$refs 属性对象上。

文本选择器：type=text

名称类型默认值必填描述rangeArray-否

设置文本选择器的取值范围。

使用时需要使用数据绑定的方式，如range = {{data}}，js中声明相应变量：data：["15", "20", "25"]。

selectedstring0否设置文本选择器的默认选择值，该值需要为range的索引。

时间选择器：type=time

名称类型默认值必填描述selectedstring00:00否

设置时间选择器的默认取值，格式为 HH:mm；

[]()[]()

#### 事件

type=text：

名称参数描述change{ newValue: newValue, newSelected: newSelected }文本选择器选定值后触发该事件。

type=time：

名称参数描述change{ hour: hour, minute: minute}

时间选择器选定值后触发该事件。

[]()[]()

#### 样式

名称类型默认值必填描述color<color>

#808080

否候选项字体颜色。font-size<length>

30px

否候选项字体尺寸，类型length，单位px。selected-color<color>

#ffffff

否选中项字体颜色。selected-font-size<length>

38px

否选中项字体尺寸，类型length，单位px。selected-font-familystringHYQiHei-65S否选中项字体类型。font-familystring

HYQiHei-65S

否选项字体类型。width<length> | <percentage>5+-否

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

margin-[left|top|right|bottom]<length> | <percentage>5+0否设置左、上、右、下外边距属性。border-width<length>0否使用简写属性设置元素的所有边框宽度。border-color<color>black否使用简写属性设置元素的所有边框颜色。border-radius<length>-否border-radius属性是设置元素的外边框圆角半径。background-color<color>-否设置背景颜色。displaystringflex否

确定一个元素所产生的框的类型，可选值为：

- flex：弹性布局。

- none：不渲染此元素。

[left|top]<length> | <percentage>6+-否

left|top确定元素的偏移位置。

- left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。

- top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。

[]()[]()

#### 方法

名称参数描述rotation{ focus: boolean }控制picker-view是否请求旋转表冠的焦点。设置focus参数为true，picker-view将获取旋转表冠的焦点，允许用户通过旋转表冠来滚动选择器中的选项；设置为false将释放旋转表冠的焦点。该功能仅在picker-view为单列时生效，对于多列picker-view，需通过用户点击来获取焦点以支持旋转表冠操作。[]()[]()

#### 示例

```ets
<!-- xxx.hml -->
<div class="container" @swipe="handleSwipe">
  <text class="title">
    Selected：{{time}}
  </text>
  <picker-view class="time-picker" type="time" selected="{{defaultTime}}" @change="handleChange"></picker-view>
</div>
```

```ets
/* xxx.css */
.container {
  flex-direction: column;
  justify-content: center;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.title {
  font-size: 30px;
  text-align: center;
}
.time-picker {
  width: 500px;
  height: 400px;
  margin-top: 20px;
}
```

```ets
/* xxx.js */
export default {
  data: {
    defaultTime: "",
    time: "",
  },
  onInit() {
    this.defaultTime = this.now();
  },
  handleChange(data) {
    this.time = this.concat(data.hour, data.minute);
  },
  now() {
    const date = new Date();
    const hours = date.getHours();
    const minutes = date.getMinutes();
    return this.concat(hours, minutes);
  },

  fill(value) {
    return (value > 9 ? "" : "0") + value;
  },

  concat(hours, minutes) {
    return `${this.fill(hours)}:${this.fill(minutes)}`;
  },
}
```