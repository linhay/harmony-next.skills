[]()[]()

# marquee

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 从API version 6开始，仅当文本内容宽度超过跑马灯组件宽度时滚动。

跑马灯组件，用于展示一段单行滚动的文字。

[]()[]()

#### 权限列表

无

[]()[]()

#### 子组件

不支持。

[]()[]()

#### 属性

除支持[通用属性](通用属性 (js-components-common-attributes).md)外，还支持如下属性：

名称类型默认值必填描述scrollamountnumber6否跑马灯每次滚动时移动的最大长度。loopnumber-1否跑马灯滚动的次数。如果未指定，则默认值为-1，当该值小于等于零时表示marquee将连续滚动。directionstringleft否设置跑马灯的文字滚动方向，可选值为left和right。[]()[]()

#### 样式

除支持[通用样式](通用样式 (js-components-common-styles).md)外，还支持如下样式：

名称类型默认值必填描述color<color>#e5000000否设置跑马灯中文字的文本颜色。font-size<length>37.5否设置跑马灯中文字的文本尺寸。allow-scalebooleantrue否

设置跑马灯中文字的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。

如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。

font-weightnumber | stringnormal否设置跑马灯中文字的字体的粗细，见[text组件font-weight的样式属性](text (js-components-basic-text).md#ZH-CN_TOPIC_0000002529444973__样式)。font-familystringsans-serif否设置跑马灯中文字的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](自定义字体样式 (js-components-common-customizing-font).md)指定的字体，会被选中作为文本的字体。[]()[]()

#### 事件

除支持[通用事件](通用事件 (js-components-common-events).md)外，还支持如下事件：

名称参数描述bounce-当文本滚动到末尾时触发该事件。finish-当完成滚动次数时触发该事件。需要在 loop 属性值大于 0 时触发。start-当文本滚动开始时触发该事件。[]()[]()

#### 方法

除支持[通用方法](../misc/通用方法.md)外，还支持如下方法：

名称参数描述start-开始滚动。stop-停止滚动。[]()[]()

#### 示例

```ets
<!-- xxx.hml -->
<div class="tutorial-page">
  <div class="mymarquee">
    <marquee  style="color: {{color1}}" loop="{{loopval}}" scrollamount="{{scroll}}" direction="{{isleft}}" class="marqueetext"
    id="testmarquee" onfinish="setfinish">
      Life is a journey, not the destination.
    </marquee>
  </div>
  <div style="width: 600px;height: 150px;flex-direction: row;justify-content: space-around;">
    <button onclick="makestart"  value="start"></button>
    <button onclick="makestop" value="stop"></button>
  </div>
</div>
```

```ets
/* xxx.css */
.tutorial-page {
  width: 750px;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.marqueetext {
  font-size: 37px;
}
.mymarquee {
  margin-top: 20px;
  width:100%;
  height: 100px;
  margin-left: 50px;
  margin-right: 50px;
  border: 1px solid #dc0f27;
  border-radius: 15px;
  align-items: center;
}
button{
  width: 200px;
  height: 80px;
  margin-top: 100px;
}
```

```ets
// xxx.js
export default {
  private: {
    loopval: 1,
    scroll: 8,
    color1: 'red'
  },
  onInit(){
  },
  setfinish(e) {
    this.loopval=  this.loopval + 1,
    this.r = Math.floor(Math.random()*255),
    this.g = Math.floor(Math.random()*255),
    this.b = Math.floor(Math.random()*255),
    this.color1 = 'rgba('+ this.r +','+ this.g +','+ this.b +',0.8)',
    this.$element('testmarquee').start(),
    this.loopval=  this.loopval - 1
  },
  makestart(e) {
    this.$element('testmarquee').start()
  },
  makestop(e) {
    this.$element('testmarquee').stop()
  }
}
```