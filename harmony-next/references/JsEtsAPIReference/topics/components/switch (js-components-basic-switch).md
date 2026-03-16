[]()[]()

# switch

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

开关选择器，通过开关，开启或关闭某个功能。

[]()[]()

#### 权限列表

无

[]()[]()

#### 子组件

不支持。

[]()[]()

#### 属性

除支持[通用属性](通用属性 (js-components-common-attributes).md)外，还支持如下属性：

名称类型默认值必填描述checkedbooleanfalse否是否选中。 true表示选中，false表示未选中。showtextbooleanfalse否是否显示文本。true表示显示文本，false表示不显示文本。textonstring"On"否选中时显示的文本。textoffstring"Off"否未选中时显示的文本。[]()[]()

#### 样式

除支持[通用样式](通用样式 (js-components-common-styles).md)外，还支持如下样式：

名称类型默认值必填描述texton-color<color>#000000否选中时显示的文本颜色，仅设置texton和textoff生效。textoff-color<color>#000000否未选中时显示的文本颜色，仅设置texton和textoff生效。text-paddingnumber0px否texton/textoff中最长文本两侧距离滑块边界的距离。font-size<length>-否文本尺寸，仅设置texton和textoff生效。allow-scalebooleantrue否

文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。

如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。

font-stylestringnormal否字体样式，仅设置texton和textoff生效。见text组件[font-style的样式属性](text (js-components-basic-text).md#ZH-CN_TOPIC_0000002529444973__样式)。font-weightnumber | stringnormal否字体粗细，仅设置texton和textoff生效。见text组件的[font-weight的样式属性](text (js-components-basic-text).md#ZH-CN_TOPIC_0000002529444973__样式)。font-familystringsans-serif否字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](自定义字体样式 (js-components-common-customizing-font).md)指定的字体，会被选中作为文本的字体。仅设置texton和textoff生效。[]()[]()

#### 事件

除支持[通用事件](通用事件 (js-components-common-events).md)外，还支持如下事件：

名称参数描述change{ checked: checkedValue }选中状态改变时触发该事件。[]()[]()

#### 方法

支持[通用方法](../misc/通用方法.md)。

[]()[]()

#### 示例

```ets
<!-- xxx.hml -->
<div class="container">
    <switch @change="normalSwitchChange">
    </switch>
    <switch class="switch" showtext="true" texton="开启" textoff="关闭" @change="switchChange">
    </switch>
    <switch class="switch text" showtext="true" texton="开启" textoff="关闭" checked="true" @change="switchChange">
    </switch>
</div>
```

```ets
/* xxx.css */
.container {
    display: flex;
    justify-content: center;
    align-items: center;
}
.switch {
    texton-color: red;
    textoff-color: forestgreen;
}
.text {
    text-padding: 20px;
    font-size: 30px;
    font-weight: 700;
}
```

```ets
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
    data: {
        title: 'World'
    },
    switchChange(e) {
        if (e.checked) {
            promptAction.showToast({
                message: "打开开关"
            });
        } else {
            promptAction.showToast({
                message: "关闭开关"
            });
        }
    },
    normalSwitchChange(e) {
        if (e.checked) {
            promptAction.showToast({
                message: "switch on"
            });
        } else {
            promptAction.showToast({
                message: "switch off"
            });
        }
    }
}
```