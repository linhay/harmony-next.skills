# input

交互式组件，包括单选框，多选框，按钮。

该组件从API version 4 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

不支持。

#### 属性

名称类型默认值必填描述typestring

button

否

input组件类型，可选值为button，checkbox，radio。

button，checkbox，radio不支持动态修改。可选值定义如下：

- button：定义可点击的按钮。

- checkbox：定义多选框。

- radio：定义单选按钮，允许在多个拥有相同name值的选项中选中其中一个。

checkedbooleanfalse否当前组件是否选中，true表示选中，false表示未选中。仅type为checkbox和radio生效。namestring-否input组件的名称。valuestring-否input组件的value值，当类型为radio时必填且相同name值的选项该值唯一。idstring-否组件的唯一标识。stylestring-否组件的样式声明。classstring-否组件的样式类，用于引用样式表。refstring-否用来指定指向子元素的引用信息，该引用将注册到父组件的$refs 属性对象上。

#### 事件

-

当input类型为checkbox、radio时，支持如下事件：

名称参数描述change{ checked:true | false }checkbox多选框或radio单选框的checked状态发生变化时触发该事件。click-点击动作触发该事件。longpress-长按动作触发该事件。swipe5+[SwipeEvent](通用事件.md)组件上快速滑动后触发。
-

当input类型为button时，支持如下事件：

名称参数描述click-点击动作触发该事件。longpress-长按动作触发该事件。swipe5+[SwipeEvent](通用事件.md)组件上快速滑动后触发。

#### 样式

名称类型默认值必填描述color<color>#ffffff否按钮的文本颜色。font-size<length>30px否按钮的文本尺寸。width<length>-否type为button时，默认值为100px。height<length>-否type为button时，默认值为50px。font-familystringSourceHanSansSC-Regular否字体。目前仅支持SourceHanSansSC-Regular 字体。padding<length>0否

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

#### 示例

1.

type为button

```ets
<!-- xxx.hml -->
<div class="div-button">
  <input class="button" type="button" value="Input-Button"></input>
</div>
```

```ets
/* xxx.css */
.div-button {
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}
.button {
  margin-top: 30px;
  width: 280px;
}
```

1.

type为checkbox

```ets
<!-- xxx.hml -->
<div class="content">
  <input onchange="checkboxOnChange" checked="true" type="checkbox"></input>
  <text class="text">{{text}}</text>
</div>
```

```ets
/* xxx.css */
.content{
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.text{
  font-size: 30px;
  text-align: center;
  width: 200px;
  margin-top: 20px;
  height: 100px;
}
```

```ets
// xxx.js
export default {
  data: {
    text: "text"
  },
  checkboxOnChange(e) {
    this.text = e.checked;
  }
}
```

1.

type为radio

```ets
<!-- xxx.hml -->
<div class="container">
  <div class="item">
    <input type="radio" checked="true" name="radioSample" value="radio1" onchange="onRadioChange"></input>
    <text class="text">radio1</text>
  </div>
  <div class="item">
    <input type="radio" checked="false" name="radioSample" value="radio2" onchange="onRadioChange"></input>
    <text class="text">radio2</text>
  </div>
  <div class="item">
    <input type="radio" checked="false" name="radioSample" value="radio3" onchange="onRadioChange"></input>
    <text class="text">radio3</text>
  </div>
</div>
```

```ets
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.item {
  width: 50%;
  height: 30%;
  justify-content: center;
}
.text {
  margin-top: 25%;
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}
```