# textarea

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

多行文本输入的文本框。

**权限列表**

无

**子组件**

不支持。

**属性**

除支持[通用属性](通用属性.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| placeholder | string | - | 否 | 多行文本框的提示文本内容。 |
| maxlength | number | - | 否 | 多行文本框可输入的最多字符数量。 |
| headericon | string | - | 否 | 在文本输入前的图标展示，该图标不支持点击事件，图标格式为jpg，png和svg。 |
| extend | boolean | false | 否 | 文本框是否支持可扩展，true表示文本框支持可扩展，false表示文本框不支持可扩展。设置可扩展属性后文本框高度可以跟随文字自适应。 |
| value5+ | string | - | 否 | 多行文本框的内容。 |
| showcounter5+ | boolean | false | 否 | 文本框是否需要开启计数下标功能，需要配合maxlength一起使用。true表示文本框开启计数下标，false表示文本框不开启计数下标。 |
| menuoptions5+ | Array<MenuOption> | - | 否 | 设置文本选择弹框点击更多按钮之后显示的菜单项。 |
| autofocus6+ | boolean | false | 否 | 是否自动获焦。true表示文本框自动获焦，false表示文本框不自动获焦。 |
| selectedstart6+ | number | -1 | 否 | 开始选择文本时初始选择位置。 |
| selectedend6+ | number | -1 | 否 | 开始选择文本时结尾选择位置。 |
| softkeyboardenabled6+ | boolean | true | 否 | 编辑时是否弹出系统软键盘。true表示编辑时弹出系统软键盘，false表示不弹出。 |

表1 MenuOption5+

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| icon | string | 菜单选项中的图标路径。 |
| content | string | 菜单选项中的文本内容。 |

**样式**

除支持[通用样式](通用样式.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | <color> | #e6000000 | 否 | 多行文本框的文本颜色。 |
| font-size | <length> | 16px | 否 | 多行文本框的文本尺寸。 |
| allow-scale | boolean | true | 否 | 多行文本框的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。 如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| placeholder-color | <color> | #99000000 | 否 | 多行文本框的提示文本颜色，type为text|email|date|time|number|password时生效。 |
| font-weight | number | string | normal | 否 | 多行文本框的字体粗细，见text组件font-weight的样式属性。 |
| font-family | string | sans-serif | 否 | 多行文本框的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过自定义字体指定的字体，会被选中作为文本的字体。 |
| caret-color6+ | <color> | - | 否 | 设置输入光标的颜色。 |

**事件**

除支持[通用事件](通用事件.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { text: newText, lines: textLines, height: textHeight } | 输入内容发生变化时触发该事件，通过参数获取输入内容、行数和行高。 从API version 5开始，改变value属性值不会触发该回调。 |
| translate5+ | { value: selectedText } | 设置此事件后，进行文本选择操作后文本选择弹窗会出现翻译按钮，点击翻译按钮之后，触发该回调，返回选中的文本内容。 |
| share5+ | { value: selectedText } | 设置此事件后，进行文本选择操作后文本选择弹窗会出现分享按钮，点击分享按钮之后，触发该回调，返回选中的文本内容。 |
| search5+ | { value: selectedText } | 设置此事件后，进行文本选择操作后文本选择弹窗会出现搜索按钮，点击搜索按钮之后，触发该回调，返回选中的文本内容。 |
| optionselect5+ | { index:optionIndex, value: selectedText } | 文本选择弹窗中设置menuoptions属性后，用户在文本选择操作后，点击菜单项后触发该回调，返回点击的菜单项序号和选中的文本内容。 |
| selectchange6+ | { start: number，end: number } | 文本选择变化时触发事件。 |

**方法**

支持[通用方法](通用方法.md)。

**示例**

```ets
<!-- xxx.hml -->
<textarea id="textarea" class="textarea" extend="true" maxlength="20"
  headericon="/common/navigation_menu1_icon.svg" placeholder="Please input text"
  onchange="change">
</textarea>
```

```ets
/* xxx.css */
.textarea {
  placeholder-color: gray;
}
```

```ets
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
change(e){
  promptAction.showToast({
    message: 'value: ' + e.text + ', lines: ' + e.lines + ', height: ' + e.height,
    duration: 3000,
  });
}
```

![image](public_sys-resources/zh-cn_image_0000002553205427.webp)