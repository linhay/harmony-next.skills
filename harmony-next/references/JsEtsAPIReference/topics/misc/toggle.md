# [toggle](toggle.md)


 从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

状态按钮用于从一组选项中进行选择，并可能在界面上实时显示选择后的结果。通常这一组选项都是由状态按钮构成。

**权限列表**

无

#### 子组件

不支持。

**属性**

除支持[通用属性](通用属性.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| value | [string](../components/组件标识.md) | - | 是 | 状态按钮的文本值。 |
| checked | boolean | false | 否 | 状态按钮是否被选中。true表示选中，false表示未选中。 |

**样式**

除支持[通用样式](通用样式.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| [text](../components/Text.md)-color | <color> | #E5000000 | 否 | 状态按钮的文本颜色。 |
| font-[size](../components/尺寸设置.md#ZH-CN_TOPIC_0000002497444850__size) | <length> | 16px | 否 | 状态按钮的文本尺寸。 |
| allow-[scale](../components/图形变换.md#ZH-CN_TOPIC_0000002497604834__scale) | boolean | true | 否 | 状态按钮的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。 如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| font-style | [string](../components/组件标识.md) | normal | 否 | 状态按钮的字体样式。 |
| font-weight | number | string | normal | 否 | 状态按钮的字体粗细。见[text](../components/Text.md)组件font-weight的样式属性。 |
| font-family | <[string](../components/组件标识.md)> | sans-serif | 否 | 状态按钮的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过自定义字体指定的字体，会被选中作为文本的字体。 |

**事件**

除支持[通用事件](通用事件.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { checked：isChecked } | 组件选中状态发生变化时触发。 |

**方法**

支持[通用方法](通用方法.md)。

**示例**

```ets
<!-- xxx.hml -->
<div style="flex-direction: column;">
  <text class="margin">1. Multiple choice example</text>
  <div style="flex-wrap: wrap">
    <toggle class="margin" for="{{toggles}}">{{$item}}</toggle>
  </div>
  <text class="margin">2. Single choice example</text>
  <div style="flex-wrap: wrap">
    <toggle class="margin" for="{{toggle_list}}" id="{{$item.id}}" checked="{{$item.checked}}"
      value="{{$item.name}}" @change="allchange" @click="allclick({{$item.id}})"></toggle>
  </div>
```

```ets
/* xxx.css */
.margin {
  margin: 7px;
}
```

```ets
// xxx.js
export default {
    data: {
        toggle_list: [
{
                "id": "1001", "name": "Living room", "checked": true
            },
{
                "id": "1002", "name": "Bedroom", "checked": false
            },
            {
                "id": "1003", "name": "Second bedroom", "checked": false
            },
            {
                "id": "1004", "name": "Kitchen", "checked": false
            },
            {
                "id": "1005", "name": "Study", "checked": false
            },
            {
                "id": "1006", "name": "Garden", "checked": false
            },
            {
                "id": "1007", "name": "Bathroom", "checked": false
            },
            {
                "id": "1008", "name": "Balcony", "checked": false
            },
        ],
        toggles: ["Living room", "Bedroom", "Kitchen", "Study"],
        idx: ""
    },
    allclick(arg) {
        this.idx = arg;
    },
    allchange(e) {
        if (e.checked != true) {
            return;
      }
        for (var i = 0; i < this.toggle_list.length; i++) {
            if (this.toggle_list[i].id === this.idx) {
                this.toggle_list[i].checked = true;
            } else {
                this.toggle_list[i].checked = false;
      }
```

![image](public_sys-resources/zh-cn_image_0000002553365389.webp)