[]()[]()

# Marquee

跑马灯组件，用于滚动展示一段单行文本。仅当文本内容宽度大于等于跑马灯组件宽度时滚动，当文本内容宽度小于跑马灯组件宽度时不滚动。

 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

 为了不影响滚动帧率，建议在滚动类组件中Marquee的个数不超过4个，或者使用[Text](../graphics/Text.md)组件的[TextOverflow.MARQUEE](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__textoverflow)替代。

对于Marquee组件动态帧率的场景，可以使用[MarqueeDynamicSyncScene](../../types/classes/Class (MarqueeDynamicSyncScene).md)接口实现。

在文本宽度小于跑马灯组件宽度时，使用[属性动画](../misc/属性动画 (animation).md)实现滚动。

[]()[]()

#### 子组件

无

[]()[]()

#### 接口

Marquee(options: MarqueeOptions)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[MarqueeOptions](#ZH-CN_TOPIC_0000002529444873__marqueeoptions18对象说明)18+是配置跑马灯组件的参数。[]()[]()

#### MarqueeOptions18+对象说明

Marquee初始化参数。

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

名称类型只读可选说明start8+boolean否否

控制跑马灯是否进入播放状态。

true表示播放，false表示不播放。

**说明：**

有限的滚动次数播放完毕后，不可以通过改变start重置滚动次数重新开始播放。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

step8+number否是

滚动动画文本滚动步长。当step大于Marquee的文本宽度时，取默认值。

默认值：6

单位：[vp](../misc/像素单位.md)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

loop8+number否是

设置重复滚动的次数，小于等于零时无限循环。

默认值：-1

**说明：**

ArkTS卡片上该参数设置任意值都仅在可见时滚动一次。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

fromStart8+boolean否是

设置文本从头开始滚动或反向滚动。

true表示从头开始滚动，false表示反向滚动。

默认值：true

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

src8+string否否

需要滚动的文本。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

[]()[]()

#### 属性

除支持[通用属性](../components/通用属性 (ts-component-general-attributes).md)外，还支持以下属性：

[]()[]()

#### fontColor

fontColor(value: ResourceColor)

设置字体颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)是字体颜色。[]()[]()

#### fontSize

fontSize(value: Length)

设置字体大小。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)是字体大小。fontSize为number类型时，使用fp单位。字体默认大小16fp。不支持设置百分比字符串。[]()[]()

#### fontWeight

fontWeight(value: number | FontWeight | string)

设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuenumber | [FontWeight](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__fontweight) | string是

文本的字体粗细，number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。

默认值：FontWeight.Normal

[]()[]()

#### fontFamily

fontFamily(value: string | Resource)

设置字体列表。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valuestring | [Resource](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource)是

字体列表。默认字体'HarmonyOS Sans'。

应用当前支持'HarmonyOS Sans'字体和注册自定义字体[loadFontSync](../../modules/ohos/@ohos.graphics.text (文本模块).md#ZH-CN_TOPIC_0000002497605988__loadfontsync)。

卡片当前仅支持'HarmonyOS Sans'字体。

[]()[]()

#### allowScale

allowScale(value: boolean)

设置是否允许文本缩放。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明valueboolean是

是否允许文本缩放。

true表示允许文本缩放，false表示不允许文本缩放。

默认值：false

**说明：**

仅当fontSize为fp单位时生效。

[]()[]()

#### marqueeUpdateStrategy12+

marqueeUpdateStrategy(value: MarqueeUpdateStrategy)

跑马灯组件属性更新后，跑马灯的滚动策略。(当跑马灯为播放状态，且文本内容宽度超过跑马灯组件宽度时，该属性生效。)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明value[MarqueeUpdateStrategy](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__marqueeupdatestrategy12)是

跑马灯组件属性更新后，跑马灯的滚动策略。

默认值: MarqueeUpdateStrategy.DEFAULT

[]()[]()

#### 事件

[]()[]()

#### onStart

onStart(event: () => void)

当滚动的文本内容变化或者开始滚动时触发回调。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event () => void是当滚动的文本内容变化或者开始滚动时的回调。[]()[]()

#### onBounce

onBounce(event: () => void)

完成一次滚动时触发，若循环次数不为1，则该事件会多次触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event () => void是完成一次滚动时触发的回调。[]()[]()

#### onFinish

onFinish(event: () => void)

滚动全部循环次数完成时触发回调。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明event () => void是滚动全部循环次数完成时的回调。[]()[]()

#### 示例

该示例通过设置start、step、loop、fromStart、src、[marqueeUpdateStrategy](#ZH-CN_TOPIC_0000002529444873__marqueeupdatestrategy12)（从API version 12开始）展示了跑马灯内容动态更新时运行的效果。

```ets
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
        src: this.marqueeText + this.src
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
}
```