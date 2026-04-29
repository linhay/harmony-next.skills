# menu

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

提供菜单组件，作为临时性弹出窗口，用于展示用户可执行的操作。

**权限列表**

无

**子组件**

<[option](option.md)>子组件。

**属性**

除支持[通用属性](通用属性.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| target | string | - | 否 | 目标元素选择器。当使用目标元素选择器后，点击目标元素会自动弹出menu菜单。弹出菜单位置优先为目标元素右下角，当右边可视空间不足时会适当左移，当下方空间不足时会适当上移。 |
| type | string | click | 否 | 目标元素触发弹窗的方式，可选值有： - click：点击弹窗。 - longpress：长按弹窗。 |
| title | string | - | 否 | 菜单标题内容。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

 不支持focusable、disabled属性。

**样式**

仅支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| text-color | <color> | - | 否 | 设置菜单的文本颜色。 |
| font-size | <length> | 30px | 否 | 设置菜单的文本尺寸。 |
| allow-scale | boolean | true | 否 | 设置菜单的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。 如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| letter-spacing | <length> | 0 | 否 | 设置菜单的字符间距。 |
| font-style | string | normal | 否 | 设置菜单的字体样式。见text组件font-style的样式属性。 |
| font-weight | number | string | normal | 否 | 设置菜单的字体粗细。见text组件font-weight的样式属性。 |
| font-family | string | sans-serif | 否 | 设置菜单的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过自定义字体指定的字体，会被选中作为文本的字体。 |

**事件**

仅支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| selected | { value:value } | 菜单中某个值被点击选中时触发，返回的value值为option组件的value属性。 |
| cancel | - | 用户取消。 |

**方法**

仅支持如下方法。

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| show | { x:x, y:y } | 显示menu菜单。(x, y)指定菜单弹窗位置。其中x表示距离可见区域左边沿的 X 轴坐标，不包含任何滚动偏移，y表示距离可见区域上边沿的 Y 轴坐标，不包含任何滚动偏移以及状态栏。菜单优先显示在弹窗位置右下角，当右边可视空间不足时会适当左移，当下方空间不足时会适当上移。 |

**示例**

```ets
<!-- xxx.hml -->
<div class="container">
  <text onclick="onTextClick" class="title-text">Show popup menu.</text>
  <menu id="apiMenu">
    <option value="Item 1">Item 1</option>
    <option value="Item 2">Item 2</option>
    <option value="Item 3">Item 3</option>
  </menu>
</div>
```

```ets
/* xxx.css */
.container {
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
}
.title-text {
  margin: 20px;
}
```

```ets
// xxx.js
export default {
    onTextClick() {
        this.$element("apiMenu").show({ x: 175, y: 50 });
    }
```

![image](public_sys-resources/zh-cn_image_0000002522245456.webp)