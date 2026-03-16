[]()[]()

# 动画样式

组件支持通过style或css设置动态的旋转、平移及缩放效果。

名称类型默认值描述transformstring-详见表1。animation-namestring-指定@keyframes，详见表2。animation-delay<time>0定义动画播放的延迟时间。支持的单位为[s(秒)|ms(毫秒) ]，默认单位为ms，格式为：1000ms或1s。animation-duration<time>0

定义一个动画周期。支持的单位为[s(秒)|ms(毫秒) ]，默认单位为ms，格式为：1000ms或1s。

**说明：**

animation-duration 样式必须设置，否则时长为 0，则不会播放动画。

animation-iteration-countnumber | infinite1定义动画播放的次数，默认播放一次，可通过设置为infinite无限次播放。animation-timing-functionstring

linear

描述动画执行的速度曲线，用于使动画更为平滑。

可选项有：

- linear：表示动画从头到尾的速度都是相同的。

- ease-in：表示动画以低速开始，cubic-bezier(0.42, 0.0, 1.0, 1.0)。

- ease-out：表示动画以低速结束，cubic-bezier(0.0, 0.0, 0.58, 1.0)。

- ease-in-out：表示动画以低速开始和结束，cubic-bezier(0.42, 0.0, 0.58, 1.0)。

animation-fill-modestringnone

指定动画开始和结束的状态：

- none：在动画执行之前和之后都不会应用任何样式到目标上。

- forwards：在动画结束后，目标将保留动画结束时的状态（在最后一个关键帧中定义）。

**表1** transform操作说明

名称类型描述translateX<length>X轴方向平移动画属性translateY<length>Y轴方向平移动画属性rotate<deg> | <rad>旋转动画属性

 轻量级智能穿戴仅支持原始大小的图片进行旋转。

**表2** @keyframes属性说明

名称类型默认值描述background-color<color>-动画执行后应用到组件上的背景颜色。width<length>-动画执行后应用到组件上的宽度值。height<length>-动画执行后应用到组件上的高度值。transformstring-定义应用在组件上的变换类型，见表1。

对于不支持起始值或终止值缺省的情况，可以通过from和to显示指定起始和结束。示例：

```ets
@keyframes Go
{
   from {
     background-color: #f76160;
   }
   to {
     background-color: #09ba07;
   }
}
```

 @keyframes的from/to不支持动态绑定。