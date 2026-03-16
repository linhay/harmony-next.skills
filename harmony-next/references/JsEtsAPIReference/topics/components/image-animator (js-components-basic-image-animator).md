[]()[]()

# image-animator

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

图片帧动画播放器。

[]()[]()

#### 子组件

不支持。

[]()[]()

#### 属性

除支持[通用属性](通用属性 (js-components-common-attributes).md)外，还支持如下属性：

名称类型默认值必填描述imagesArray<ImageFrame>-是

设置图片帧信息集合。每一帧的帧信息包含图片路径、图片大小和图片位置信息。目前支持以下图片格式：png、jpg。ImageFrame的详细说明请见表 ImageFrame说明。

使用时需要使用数据绑定的方式：

- hml文件中引用图片资源：images = {{images}}，

- js文件中声明相应变量：

images: [{src: "/common/heart-rate01.png",duration:"100"}]。从API version 6开始，支持配置每一帧图片的时长，单位毫秒。

predecode6+number0否是否启用预解码，默认值为0，即不启用预解码，如该值设为2，则播放当前页时会提前加载后面两张图片至缓存以提升性能。iterationnumber | stringinfinite否设置帧动画播放次数。number表示固定次数，infinite枚举表示无限次数播放。reversebooleanfalse否设置播放顺序。false表示从第1张图片播放到最后1张图片； true表示从最后1张图片播放到第1张图片。fixedsizebooleantrue否设置图片大小是否固定为组件大小。 true表示图片大小与组件大小一致，此时设置图片的width 、height 、top 和left属性是无效的。false表示每一张图片的 width 、height 、top和left属性都要单独设置。durationstring-是设置单次播放时长。单位支持[s(秒)|ms(毫秒)]，默认单位为ms。 duration为0时，不播放图片。 值改变只会在下一次循环开始时生效，当images中设置了单独的duration后，该属性设置无效。fillmode5+stringforwards否

指定帧动画执行结束后的状态。可选项有：

- none：恢复初始状态。

- forwards：保持帧动画结束时的状态（在最后一个关键帧中定义）。

**表1** ImageFrame说明

名称类型默认值必填描述src<uri>-是图片路径，图片格式支持svg、png、jpg和heif。width<length>0否图片宽度。height<length>0否图片高度。top<length>0否图片相对于组件左上角的纵向坐标。left<length>0否图片相对于组件左上角的横向坐标。duration6+number-否每一帧图片的播放时长，单位毫秒。[]()[]()

#### 样式

支持[通用样式](通用样式 (js-components-common-styles).md)。

[]()[]()

#### 事件

除支持[通用事件](通用事件 (js-components-common-events).md)外，还支持如下事件：

名称参数描述start-帧动画启动时触发。pause-帧动画暂停时触发。stop-帧动画结束时触发。resume-帧动画恢复时触发。[]()[]()

#### 方法

支持[通用方法](../misc/通用方法.md)外，还支持如下方法：

名称参数描述start-开始播放图片帧动画。再次调用，重新从第1帧开始播放。pause-暂停播放图片帧动画。stop-停止播放图片帧动画。resume-继续播放图片帧。getState-

获取播放状态。

- playing：播放中。

- paused：已暂停。

- stopped：已停止。

[]()[]()

#### 示例

```ets
<!-- xxx.hml -->
<div class="container">
  <image-animator class="animator" ref="animator" images="{{frames}}" duration="1s" />
  <div class="btn-box">
    <input class="btn" type="button" value="start" @click="handleStart" />
    <input class="btn" type="button" value="stop" @click="handleStop" />
    <input class="btn" type="button" value="pause" @click="handlePause" />
    <input class="btn" type="button" value="resume" @click="handleResume" />
  </div>
</div>
```

```ets
/* xxx.css */
.container {
  flex-direction: column;
  justify-content: center;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.animator {
  width: 70px;
  height: 70px;
}
.btn-box {
  width: 264px;
  height: 120px;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
}
.btn {
  border-radius: 8px;
  width: 120px;
  margin-top: 8px;
}
```

```ets
//xxx.js
export default {
  data: {
    frames: [
      {
        src: "/common/assets/heart78.png",
      },
      {
        src: "/common/assets/heart79.png",
      },
      {
        src: "/common/assets/heart80.png",
      },
      {
        src: "/common/assets/heart81.png",
      },
      {
        src: "/common/assets/heart82.png",
      },
      {
        src: "/common/assets/heart83.png",
      },
      {
        src: "/common/assets/heart84.png",
      },
      {
        src: "/common/assets/heart85.png",
      },
      {
        src: "/common/assets/heart86.png",
      },
      {
        src: "/common/assets/heart87.png",
      },
      {
        src: "/common/assets/heart88.png",
      },
      {
        src: "/common/assets/heart89.png",
      },
      {
        src: "/common/assets/heart90.png",
      },
      {
        src: "/common/assets/heart91.png",
      },
      {
        src: "/common/assets/heart92.png",
      },
      {
        src: "/common/assets/heart93.png",
      },
      {
        src: "/common/assets/heart94.png",
      },
      {
        src: "/common/assets/heart95.png",
      },
      {
        src: "/common/assets/heart96.png",
      },
    ],
  },
  handleStart() {
    this.$refs.animator.start();
  },
  handlePause() {
    this.$refs.animator.pause();
  },
  handleResume() {
    this.$refs.animator.resume();
  },
  handleStop() {
    this.$refs.animator.stop();
  },
};
```