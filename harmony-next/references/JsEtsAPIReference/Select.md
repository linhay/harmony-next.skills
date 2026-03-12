# select

下拉选择按钮，可使用下拉菜单展示并选择内容。

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

支持<[option](option.md)>。

#### 属性

支持[通用属性](通用属性.md)。

#### 样式

除支持[通用样式](通用样式.md)外，还支持如下样式：

名称类型必填描述font-familystring否

字体样式列表，用逗号分隔。列表中第一个系统中存在的字体样式或者通过[自定义字体](自定义字体样式.md)指定的字体样式，会被选中作为当前文本的字体样式。

默认值：sans-serif

#### 事件

除支持[通用事件](通用事件.md)外，还支持如下事件：

名称参数描述change{newValue: newValue}选择下拉选项后触发该事件，返回值为一个对象，其中newValue为选中项option的value值。

 select组件不支持click事件。

#### 方法

支持[通用方法](通用方法.md)。

#### 示例

```ets
<!-- xxx.hml -->
<div class="container">
    <select>
        <option for="{{ array }}" value="{{ $item.value }}">
            {{ $item.name }}
        </option>
    </select>
</div>
```

```ets
/* xxx.css */
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}
```

```ets
// xxx.js
export default {
    data: {
        array: [
            {
                "value": "下拉选项0", "name": "选项0"
            },
            {
                "value": "下拉选项1", "name": "选项1"
            },
            {
                "value": "下拉选项2", "name": "选项2"
            },
            {
                "value": "下拉选项3", "name": "选项3"
            },
        ]
    }
}
```