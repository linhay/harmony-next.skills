[]()[]()

# slider

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

滑动条组件，用来快速调节设置值，如音量、亮度等。

[]()[]()

#### 子组件

不支持。

[]()[]()

#### 属性

除支持[通用属性](通用属性 (js-components-common-attributes).md)外，还支持以下属性：

名称类型默认值必填描述minnumber0否滑动选择器的最小值。maxnumber100否滑动选择器的最大值。stepnumber1否每次滑动的步长。valuenumber0否滑动选择器的初始值。mode5+stringoutset否

滑动条样式：

- outset：滑块在滑杆上；

- inset：滑块在滑杆内。

showsteps5+booleanfalse否是否显示步长标识。true表示显示步长标识，false表示不显示步长标识。showtips5+booleanfalse否滑动时是否有气泡提示百分比。true表示有气泡提示百分比，false表示没有气泡提示百分比。[]()[]()

#### 样式

除支持[通用样式](通用样式 (js-components-common-styles).md)外，还支持如下样式：

名称类型默认值必填描述color<color>#19000000否滑动条的背景颜色。selected-color<color>#ff007dff否滑动条的已选择颜色。block-color<color>#ffffff否滑动条的滑块颜色。[]()[]()

#### 事件

除支持[通用事件](通用事件 (js-components-common-events).md)外，还支持如下事件：

名称参数描述changeChangeEvent选择值发生变化时触发该事件。

**表1** ChangeEvent

属性类型说明value5+number当前slider的进度值。mode5+string

当前change事件的类型，可选值为：

- start：slider的值开始改变。

- move：slider的值跟随手指拖动中。

- end：slider的值结束改变。

- click：slider的值在点击进度条后改变。

[]()[]()

#### 示例

```ets
<!-- xxx.hml -->
<div class="container">
    <slider min="0" max="100" value="{{ value }}" mode="outset" showtips="true"></slider>
    <slider class="slider" min="0" max="100" value="{{ value }}" step="20" mode="inset"  showtips="true"></slider>
    <slider class="slider" min="0" max="100" value="{{ value }}" showsteps="true" step="20" mode="inset"  showtips="false"></slider>
</div>
```

```ets
/* xxx.css */
.container {
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.slider{
    margin-top: 100px;
}
```