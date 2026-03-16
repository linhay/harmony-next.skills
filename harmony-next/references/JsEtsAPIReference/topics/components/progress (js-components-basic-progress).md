[]()[]()

# progress

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

进度条，用于显示内容加载或操作处理进度。

[]()[]()

#### 权限列表

无

[]()[]()

#### 子组件

不支持。

[]()[]()

#### 属性

除支持[通用属性](通用属性 (js-components-common-attributes).md)外，还支持如下属性：

名称类型默认值必填描述typestringhorizontal否

设置进度条的类型，该属性不支持动态修改，可选值为：

- horizontal：线性进度条。

- circular：loading型进度条。

- ring：圆环形进度条。

- scale-ring：带刻度圆环形进度条。

- arc：弧形进度条。

- eclipse5+：圆形进度条，展现类似月圆月缺的进度展示效果。

不同类型的进度条还支持不同的属性：

-

类型为horizontal、ring、scale-ring时，支持如下属性：

名称类型默认值必填描述percentnumber0否当前进度。取值范围为0-100。secondarypercentnumber0否次级进度。取值范围为0-100。
-

类型为ring、scale-ring时，支持如下属性：

名称类型默认值必填描述clockwisebooleantrue否

圆环形进度条是否采用顺时针。

默认值：true，表示圆环形进度条采用顺时针。

-

类型为arc、eclipse5+时，支持如下属性：

名称类型默认值必填描述percentnumber0否当前进度。取值范围为0-100。

[]()[]()

#### 样式

除支持[通用样式](通用样式 (js-components-common-styles).md)外，还支持如下样式：

type=horizontal

名称类型默认值必填描述color<color>#ff007dff否设置进度条的颜色。stroke-width<length>4px否设置进度条的宽度。background-color<color>-否设置进度条的背景色。secondary-color<color>-否设置次级进度条的颜色。

type=circular

名称类型默认值必填描述color<color>-否loading型进度条上的圆点颜色。

type=ring, scale-ring

名称类型默认值必填描述color<color> | <linear-gradient>-否

环形进度条的颜色，ring类型支持线性渐变色设置。

线性渐变色仅支持两个颜色参数设置格式，如color = linear-gradient(#ff0000, #00ff00)。

background-color<color>-否环形进度条的背景色。secondary-color<color>-否环形次级进度条的颜色。stroke-width<length>10px否环形进度条的宽度。scale-width<length>-否带刻度的环形进度条的刻度粗细，类型为scale-ring生效。scale-numbernumber120否带刻度的环形进度条的刻度数量，类型为scale-ring生效。

type=arc

名称类型默认值必填描述color<color>-否弧形进度条的颜色。background-color<color>-否弧形进度条的背景色。stroke-width<length>4px否

弧形进度条的宽度，始终在半径区域内。

进度条宽度越大，进度条越靠近圆心。

start-angle<deg>240否弧形进度条起始角度，以时钟0点为基线，取值范围为0到360（顺时针）。total-angle<deg>240否弧形进度条总长度，范围为-360到360，负数标识起点到终点为逆时针。center-x<length>弧形进度条宽度的一半否弧形进度条中心位置，坐标原点为组件左上角顶点。该属性需要和center-y和radius一起使用。center-y<length>弧形进度条高度的一半否弧形进度条中心位置，坐标原点为组件左上角顶点。该属性需要和center-x和radius一起使用。radius<length>弧形进度条宽高最小值的一半否弧形进度条半径，该属性需要和center-x和center-y一起使用。

type=eclipse5+

名称类型默认值必填描述color<color>-否圆形进度条的颜色。background-color<color>-否弧形进度条的背景色。[]()[]()

#### 事件

支持[通用事件](通用事件 (js-components-common-events).md)。

[]()[]()

#### 方法

支持[通用方法](../misc/通用方法.md)。

[]()[]()

#### 示例

```ets
<!--xxx.hml -->
<div class="container">
  <progress class="min-progress" type="scale-ring"  percent= "10" secondarypercent="50"></progress>
  <progress class="min-progress" type="horizontal" percent= "10" secondarypercent="50"></progress>
  <progress class="min-progress" type="arc" percent= "10"></progress>
  <progress class="min-progress" type="ring" percent= "10" secondarypercent="50"></progress>
</div>
```

```ets
/* xxx.css */
.container {
  flex-direction: column;
  height: 100%;
  width: 100%;
  align-items: center;
}
.min-progress {
  width: 300px;
  height: 300px;
}
```