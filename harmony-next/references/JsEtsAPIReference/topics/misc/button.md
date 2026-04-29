# button

按钮组件，包括胶囊按钮、圆形按钮和文本按钮。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**子组件**

不支持。

**属性**

除支持[通用属性](通用属性.md)外，还支持如下属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | string | capsule | 否 | 不支持动态修改。如果该属性缺省，展示为胶囊型按钮，不同于胶囊类型，四边圆角可以通过border-radius分别指定，如果需要设置该属性，可选值如下： - "capsule"：胶囊型按钮，带圆角按钮，有背景色和文本。 - "circle"：圆形按钮，支持放置图标。 - "text"：文本按钮，仅包含文本显示。 |
| value | string | - | 否 | button的文本值，circle类型不生效。 |
| icon | string | - | 否 | button的图标路径，图标格式为jpg，png和svg。 |
| placement | string | end | 否 | 仅在type属性为缺省时生效，设置图标位于文本的位置，可选值为： - "start"：图标位于文本起始处。 - "end"：图标位于文本结束处。 - "top"：图标位于文本上方。 - "bottom"：图标位于文本下方。 |
| waiting | boolean | false | 否 | 是否处于waiting状态，值为true时展现等待中转圈效果，位于文本左侧。值为false时，不展示等待中效果。类型为download时不生效。 |

**事件**

支持[通用事件](通用事件.md)。

**样式**

除支持[通用样式](通用样式.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| text-color | <color> | - | 否 | 按钮的文本颜色。 |
| font-size | <length> | - | 否 | 按钮的文本尺寸。 |
| font-style | string | normal | 否 | 按钮的字体样式。 |
| font-weight | number | string | normal | 否 | 按钮的字体粗细，见text组件font-weight的样式属性。 |
| font-family | <string> | sans-serif | 否 | 按钮的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过自定义字体指定的字体，会被选中作为文本的字体。 |
| icon-width | <length> | - | 否 | 设置圆形按钮内部图标的宽，默认填满整个圆形按钮。 icon使用svg图源时必须设置该样式。 |
| icon-height | <length> | - | 否 | 设置圆形按钮内部图标的高，默认填满整个圆形按钮。 icon使用svg图源时必须设置该样式。 |
| radius | <length> | - | 否 | 圆形按钮半径或者胶囊按钮圆角半径。在圆形按钮类型下该样式优先于通用样式的width和height样式。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

-

胶囊按钮（type=capsule）时，不支持border相关样式。

-

圆形按钮（type=circle）时，不支持文本相关样式。

-

文本按钮（type=text）时，自适应文本大小，不支持尺寸设置（radius，width，height），背景透明不支持background-color样式。

**示例**

```ets
<!-- xxx.hml -->
<div class="div-button">
  <button class="button" type="capsule" value="Capsule button"></button>
  <button class="button circle" type="circle" icon="common/ic_add_default.png"></button>
  <button class="button text" type="text">Text button</button>
</div>
```

```ets
/* xxx.css */
.div-button {
  flex-direction: column;
  align-items: center;
}
.button {
  margin-top: 15px;
}
.circle {
  background-color: #007dff;
  radius: 72px;
  icon-width: 72px;
  icon-height: 72px;
}
.text {
  text-color: red;
  font-size: 40px;
  font-weight: 900;
  font-family: sans-serif;
  font-style: normal;
}
```

4*4卡片

![image](public_sys-resources/zh-cn_image_0000002553365613.webp)