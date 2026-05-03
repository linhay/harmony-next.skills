# @ohos.multimedia.avCastPicker (投播组件)

本模块提供创建投播组件AVCastPicker的功能，提供设备发现连接的统一入口。

- 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

- 示例效果请以真机为准，当前DevEco Studio预览器无实际投播功能。

#### 导入模块

```ets
import { AVCastPicker } from '@kit.AVSessionKit';
```

#### 属性

支持[通用属性]([通用属性](../../topics/misc/通用属性.md).md)。

#### AVCastPicker

```ets
AVCastPicker({
  normalColor?: Color | number | string;
  activeColor?: Color | number | string;
  pickerStyle?: AVCastPickerStyle;
  colorMode?: AVCastPickerColorMode;
  sessionType?: string;
  customPicker?: CustomBuilder;
  onStateChange?: (state: AVCastPickerState) => void;
})
```

投播组件，可用于将音视频资源投放到其它设备播放。

该组件为自定义组件，开发者在使用前需要先了解[@Component](../../topics/components/自定义组件.md)。

**装饰器类型：**[@Component](../../topics/components/自定义组件.md)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| normalColor11+ | Color | number | string | 否 | @Prop | 指正常状态下投播组件的颜色。 未设置将采用colorMode下的颜色设置。 |
| activeColor11+ | Color | number | string | 否 | @Prop | 指设备切换成功状态下投播组件的颜色。未设置系统将优先根据normalColor的颜色匹配；如果normalColor也未设置，将采用colorMode下的颜色设置。 |
| pickerStyle12+ | AVCastPickerStyle | 否 | @Prop | 投播样式。 - 当sessionType是audio或者video时，默认值为STYLE_PANEL。 - 当sessionType是voice_call或者video_call时，默认值为STYLE_MENU，且不可修改为STYLE_PANEL。 |
| colorMode12+ | AVCastPickerColorMode | 否 | @Prop | 显示模式。默认值为AUTO。 - 当colorMode设置为AUTO时，跟随系统的深浅色模式的默认色值。 - 当colorMode设置为DARK、LIGHT时，使用对应模式的系统预设色值。 |
| sessionType12+ | string | 否 | @Prop | 会话类型，可参考[AVSessionType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__avsessiontype10)。默认值为当前应用创建的AVSessionType。 |
| customPicker12+ | [CustomBuilder](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | 否 | @Prop | 自定义样式。建议应用自定义组件样式，可有效提升组件显示速度。 |
| onStateChange11+ | (state: AVCastPickerState) => void | 否 | - | 投播状态更改回调。 |

#### 事件

支持[通用事件]([通用事件](../../topics/misc/通用事件.md).md)。

#### 示例

投播功能的示例说明参考如下。

体验完整功能请具体参考[播放类开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/distributed-playback-guide)和[通话类开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-switch-call-devices)。

```ets
import { AVCastPickerState, AVCastPicker } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {

  @State pickerImage: ResourceStr = $r('app.media.castPicker'); // 自定义资源。

  private onStateChange(state: AVCastPickerState) {
    if (state == AVCastPickerState.STATE_APPEARING) {
      console.info('The picker starts showing.');
    } else if (state == AVCastPickerState.STATE_DISAPPEARING) {
      console.info('The picker finishes presenting.');
  }

  @Builder
  customPickerBuilder() {
    Image(this.pickerImage)
      .width('100%')
      .height('100%')
      .fillColor(Color.Black)
  }

  build() {
    Row() {
      Column() {
        AVCastPicker({
          normalColor: Color.Red,
          customPicker: () => this.customPickerBuilder(),
          onStateChange: this.onStateChange
        })
          .width('40vp')
          .height('40vp')
          .border({ width: 1, color: Color.Red })
      }.height('50%')
    }.width('50%')
  }
```