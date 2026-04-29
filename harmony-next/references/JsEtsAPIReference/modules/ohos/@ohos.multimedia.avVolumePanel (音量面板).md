# @ohos.multimedia.avVolumePanel (音量面板)

本模块提供创建音量面板AVVolumePanel的功能，提供展示和调节系统音量的统一面板。

应用无法直接调节系统音量，可以通过系统音量面板，让用户通过界面操作来调节音量。当用户通过应用内音量面板调节音量时，系统会展示音量提示界面，显性地提示用户系统音量发生改变。

- 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 示例效果请以真机为准，当前DevEco Studio预览器无真实音量展示和调节功能。
- **设备限制：**

  - 在穿戴设备上，可用于调节系统音量，但不显示UX界面，需开发者自行设计界面。
  - 本模块接口暂不支持TV设备使用。

#### 导入模块

```ets
import { AVVolumePanel } from '@kit.AudioKit';
```

#### 属性

支持[通用属性]([通用属性](../../topics/misc/通用属性.md).md)。

#### AVVolumePanel

AVVolumePanel({volumeLevel?: number, volumeParameter?: AVVolumePanelParameter})

音量面板，可用于在当前应用内展示音量调节面板。

装饰器类型： [@Component](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#component)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| volumeLevel | number | 否 | @Prop | 通过音量面板设置的音量值。 该值应介于当前设备音量的最小值和最大值之间。 如果该值大于当前设备音量的最大值，则视为设置最大音量值。 如果该值小于当前设备音量的最小值，则视为设置最小音量值。 获取设备的最大值、最小值和当前值，可参考AudioVolumeGroupManager。 |
| volumeParameter | AVVolumePanelParameter | 否 | @Prop | 设置音量面板的自定义参数。 如果不设置该参数，则为系统音量条。 |

#### AVVolumePanelParameter

音量面板参数设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| position | [Position](../../topics/components/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__position) | 否 | 是 | 设置音量面板的位置。 如果不设置该参数，则为系统音量条位置。 如果设置该参数且参数对应屏幕内位置，则显示开发者设置的位置。 如果设置该参数且参数对应屏幕外位置，例如（-1, -1），不显示系统音量条，建议开发者显示自定义音量条。 |

#### 事件

支持[通用事件]([通用事件](../../topics/misc/通用事件.md).md)。

#### 使用建议

1. 应用在实现自定义音量条的过程中，建议使用音频框架的音量变化监听接口，通过接口回调的音量类型volumeEvent.volumeType，音量等级volumeEvent.volume以及是否显示音量条volumeEvent.updateUi等信息，应用可以判断是否需要处理当前数据和显示自定义的音量条，具体可参考[on('streamVolumeChange')](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002522081822__onstreamvolumechange20)介绍。

1. 为确保用户能感知音量变化，不允许应用后台调节音量，系统会做出对应的控制措施。

#### 示例

音量面板功能的示例说明参考如下。需要实际修改volume值或者按压音量按键体验调节音量效果。

```ets
import { AVVolumePanel } from '@kit.AudioKit';

@Entry
@Component
struct Index {

  @State volume: number = 0;

  build() {
    Row() {
      Column() {
        AVVolumePanel({
          volumeLevel: this.volume,
          volumeParameter: {
            position: {
              x: 100,
              y: 200
            }
        })
      }
    }.width('50%').height('50%')
  }
```