# Marquee

跑马灯组件，用于滚动展示一段单行文本。仅当文本内容宽度大于等于跑马灯组件宽度时滚动，当文本内容宽度小于跑马灯组件宽度时不滚动。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 为了不影响滚动帧率，建议在滚动类组件中Marquee的个数不超过4个，或者使用[Text](Text.md)组件的[TextOverflow.MARQUEE](枚举说明.md#ZH-CN_TOPIC_0000002553200889__textoverflow)替代。

对于Marquee组件动态帧率的场景，可以使用[MarqueeDynamicSyncScene](Class (MarqueeDynamicSyncScene).md)接口实现。

在文本宽度小于跑马灯组件宽度时，使用[属性动画](属性动画 (animation).md)实现滚动。

**子组件**

无

**接口**

Marquee(options: MarqueeOptions)

创建跑马灯组件。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | MarqueeOptions18+ | 是 | 配置跑马灯组件的参数。 |

**MarqueeOptions18+对象说明**

Marquee初始化参数。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start8+ | boolean | 否 | 否 | 控制跑马灯是否进入播放状态。 true：播放；false：不播放。 说明： 有限的滚动次数播放完毕后，不可以通过改变start重置滚动次数重新开始播放。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| step8+ | number | 否 | 是 | 滚动动画文本滚动步长。当step大于Marquee的文本宽度时，取默认值。 默认值：6  单位：vp  卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| loop8+ | number | 否 | 是 | 设置重复滚动的次数，小于等于零时无限循环。 默认值：-1 说明： ArkTS卡片上该参数设置任意值都仅在可见时滚动一次。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。  元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| fromStart8+ | boolean | 否 | 是 | 设置文本从头开始滚动或反向滚动。 true：表示从头开始滚动 false：表示反向滚动。 默认值：true 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| src8+ | string | 否 | 否 | 需要滚动的文本。 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| spacing23+ | LengthMetrics | 否 | 是 | 两轮跑马灯之间的间距。如果LengthMetrics的unit值是PERCENT，当前设置不生效，按默认值处理。  默认值：跑马灯组件宽度。  卡片能力： 从API version 23开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 模型约束： 此接口仅可在Stage模型下使用。 |
| delay23+ | number | 否 | 是 | 设置每次滚动的时间间隔。 默认值：0  取值范围：[0, +∞)，设置的值小于0时等价于设置0。 单位：毫秒 卡片能力： 从API version 23开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 23开始，该接口支持在元服务中使用。 模型约束： 此接口仅可在Stage模型下使用。 |

**属性**

除支持[通用属性](通用属性.md)外，还支持以下属性：

**fontColor**

fontColor(value: ResourceColor)

设置字体颜色。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 字体颜色。 Wearable设备上默认值为：'#c5ffffff'，显示为淡蓝色，其他设备默认值为：'e6182431'，显示为黑色。 |

**fontSize**

fontSize(value: Length)

设置字体大小。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 字体大小。fontSize为number类型时，使用fp单位。字体默认大小16fp。不支持设置百分比字符串。 |

**fontWeight**

fontWeight(value: number | FontWeight | string)

设置文本的字体粗细，设置过大可能会在不同字体下有截断。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | FontWeight | string | 是 | 文本的字体粗细，number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。 默认值：FontWeight.Normal |

**fontFamily**

fontFamily(value: string | Resource)

设置字体列表。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | Resource | 是 | 字体列表。默认字体'HarmonyOS Sans'。 应用当前支持'HarmonyOS Sans'字体和注册自定义字体loadFontSync。 卡片当前仅支持'HarmonyOS Sans'字体。 |

**allowScale**

allowScale(value: boolean)

设置是否允许文本缩放。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否允许文本缩放。 true：允许文本缩放；false：不允许文本缩放。 默认值：false 说明： 仅当fontSize为fp单位时生效。 |

**marqueeUpdateStrategy12+**

marqueeUpdateStrategy(value: MarqueeUpdateStrategy)

跑马灯组件属性更新后，跑马灯的滚动策略。(当跑马灯为播放状态，且文本内容宽度超过跑马灯组件宽度时，该属性生效。)

元服务API： 从API version 12开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | MarqueeUpdateStrategy | 是 | 跑马灯组件属性更新后，跑马灯的滚动策略。 默认值: MarqueeUpdateStrategy.DEFAULT |

**事件**

**onStart**

onStart(event: () => void)

当滚动的文本内容变化或者开始滚动时触发回调。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 当滚动的文本内容变化或者开始滚动时的回调。 |

**onBounce**

onBounce(event: () => void)

完成一次滚动时触发，若循环次数不为1，则该事件会多次触发。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 完成一次滚动时触发的回调。 |

**onFinish**

onFinish(event: () => void)

滚动全部循环次数完成时触发回调。

卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。

元服务API： 从API version 11开始，该接口支持在元服务中使用。

系统能力： SystemCapability.ArkUI.ArkUI.Full

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 滚动全部循环次数完成时的回调。 |

**示例**

该示例通过设置[MarqueeOptions](#ZH-CN_TOPIC_0000002553200821__marqueeoptions18对象说明)的start、step、loop、fromStart、src、spacing、delay属性和[marqueeUpdateStrategy](#ZH-CN_TOPIC_0000002553200821__marqueeupdatestrategy12)展示了跑马灯内容动态更新时运行的效果。

从API version 23开始，[MarqueeOptions](#ZH-CN_TOPIC_0000002553200821__marqueeoptions18对象说明)新增spacing、delay属性。

```ets
import { LengthMetrics } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct MarqueeExample {
  @State start: boolean = false;
  @State src: string = '';
  @State marqueeText: string = 'Running Marquee';
  private fromStart: boolean = true;
  private step: number = 10;
  private loop: number = Number.POSITIVE_INFINITY;
  controller: TextClockController = new TextClockController();

  convert2time(value: number): string {
    let date = new Date(Number(value + '000'));
    let hours = date.getHours().toString().padStart(2, '0');
    let minutes = date.getMinutes().toString().padStart(2, '0');
    let seconds = date.getSeconds().toString().padStart(2, '0');
    return hours + ":" + minutes + ":" + seconds;
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Marquee({
        start: this.start,
        step: this.step,
        loop: this.loop,
        fromStart: this.fromStart,
        src: this.marqueeText + this.src,
        spacing: LengthMetrics.vp(300), // 从API version 23开始，新增spacing属性
        delay: 0, // 从API version 23开始，新增delay属性
      })
        .marqueeUpdateStrategy(MarqueeUpdateStrategy.PRESERVE_POSITION)
        .width('300vp')
        .height('80vp')
        .fontColor('#FFFFFF')
        .fontSize('48fp')
        .allowScale(true) // 当fontSize为‘fp’单位且想要Marquee组件文本跟随系统字体大小缩放，可以设置该属性为true
        .fontWeight(700)
        .fontFamily('HarmonyOS Sans') // 不想跟随主题字体可设置该属性为默认字体'HarmonyOS Sans'
        .backgroundColor('#182431')
        .margin({ bottom: '40vp' })
        .onStart(() => {
          console.info('Succeeded in completing the onStart callback of marquee animation');
        })
        .onBounce(() => {
          console.info('Succeeded in completing the onBounce callback of marquee animation');
        })
        .onFinish(() => {
          console.info('Succeeded in completing the onFinish callback of marquee animation');
        })
      Button('Start')
        .onClick(() => {
          this.start = true
          // 启动文本时钟
          this.controller.start();
        })
        .width('120vp')
        .height('40vp')
        .fontSize('16fp')
        .fontWeight(500)
        .backgroundColor('#007DFF')
      TextClock({ timeZoneOffset: -8, controller: this.controller })
        .format('hms')
        .onDateChange((value: number) => {
          this.src = this.convert2time(value);
        })
        .margin('20vp')
        .fontSize('30fp')
    }
    .width('100%')
    .height('100%')
  }
```

![image](public_sys-resources/zh-cn_image_0000002553365097.webp)