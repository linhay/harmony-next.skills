[]()[]()

# input

交互式组件，提供单选框功能。

从API Version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

[]()[]()

#### 属性

除支持[通用属性](通用属性 (js-service-widget-common-attributes).md)外，还支持如下属性：

名称类型默认值必填描述typestringradio是

input组件类型，当前仅支持radio类型：

- "radio"：定义单选按钮，允许在多个拥有相同name值的选项中选中其中一个。

checkedbooleanfalse否当前组件是否选中，true表示选中，false表示未选中。namestring-否input组件的名称。valuestring-否input组件的value值，类型为radio时必填且相同name值的选项该值唯一。[]()[]()

#### 样式

支持[通用样式](通用样式 (js-service-widget-common-styles).md)。

[]()[]()

#### 事件

名称参数描述change$event.checkedItemradio单选框的checked状态发生变化时触发该事件，返回选中的组件value值。click-点击动作触发该事件。[]()[]()

#### 示例

```ets
<!-- xxx.hml -->
<div class="content">
  <input type="radio" checked='true' name="radioSample" value="radio1" onchange="onRadioChange"></input>
  <input type="radio" checked='false' name="radioSample" value="radio2" onchange="onRadioChange"></input>
  <input type="radio" checked='false' name="radioSample" value="radio3" onchange="onRadioChange"></input>
</div>
```

```ets
/* xxx.css */
.content{
  width: 100%;
  height: 200px;
  justify-content: center;
  align-items: center;
}
```

```ets
{
  "actions": {
    "onRadioChange":{
      "action": "message",
      "params": {
        "checkedRadio": "$event.checkedItem"
      }
    }
  }
}
```

**4*4卡片**