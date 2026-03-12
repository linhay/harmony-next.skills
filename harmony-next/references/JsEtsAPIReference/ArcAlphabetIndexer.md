# ArcAlphabetIndexer

弧形索引条是一种弧形的、可按字母顺序排序进行快速定位的组件，可以与容器组件联动，按逻辑结构快速定位至容器显示区域。

该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 导入模块

-

ArcAlphabetIndexerAttribute是用于配置ArcAlphabetIndexer组件属性的关键接口。API version 21及之前版本，导入ArcAlphabetIndexer组件后需要开发者手动导入ArcAlphabetIndexerAttribute，否则会编译报错。从API version 22开始，编译工具链识别到导入ArcAlphabetIndexer组件后，会自动导入ArcAlphabetIndexerAttribute，无需开发者手动导入ArcAlphabetIndexerAttribute。

-

如果开发者手动导入ArcAlphabetIndexerAttribute，DevEco Studio会显示置灰，API version 21及之前版本删除会编译报错，API version 22开始，删除对功能无影响。

API version 21及之前版本：

```ets
import { ArcAlphabetIndexer, ArcAlphabetIndexerAttribute } from '@kit.ArkUI';
```

API version 22及之后版本：

```ets
import { ArcAlphabetIndexer } from '@kit.ArkUI';
```

#### 子组件

无

#### 接口

ArcAlphabetIndexer(info: ArcAlphabetIndexerInitInfo)

创建弧形索引条实例，传入弧形索引条配置项参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：** 参数内容为设置弧形索引条索引项字符串数组、初始选中项索引位置。

参数名类型必填说明info[ArcAlphabetIndexerInitInfo](#ZH-CN_TOPIC_0000002497444926__arcalphabetindexerinitinfo对象说明)是定义弧形字母索引条的初始化参数。

#### 属性

除支持[通用属性](通用属性.md)外，还支持以下属性：

#### color

color(color: Optional<ColorMetrics>)

设置普通状态下索引项文字颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明color[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[ColorMetrics](Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)>是

文字颜色。

默认值：0xFFFFFF，显示为白色。

#### selectedColor

selectedColor(color: Optional<ColorMetrics>)

设置选中项文字颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明color[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[ColorMetrics](Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)>是

选中项文字颜色。

默认值：0xFFFFFF，显示为白色。

#### popupColor

popupColor(color: Optional<ColorMetrics>)

设置提示弹窗文字颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明color[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[ColorMetrics](Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)>是

提示弹窗文字颜色。

默认值：0xFFFFFF，显示为白色。

#### selectedBackgroundColor

selectedBackgroundColor(color: Optional<ColorMetrics>)

设置选中项背景颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明color[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[ColorMetrics](Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)>是

选中项背景颜色。

默认值：0x1F71FF，显示为深蓝色。

#### popupBackground

popupBackground(color: Optional<ColorMetrics>)

设置提示弹窗背景色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明color[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[ColorMetrics](Graphics.md#ZH-CN_TOPIC_0000002529444761__colormetrics12)>是

提示弹窗背景色。

默认值：0xD8404040，显示为微透明的深灰色。

当通过popupBackground设置弹窗气泡的背景颜色后，不建议再通过[popupBackgroundBlurStyle](#ZH-CN_TOPIC_0000002497444926__popupbackgroundblurstyle)设置背景模糊效果。

#### usePopup

usePopup(enabled: Optional<boolean>)

设置是否使用提示弹窗。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明enabled[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<boolean>是

是否使用提示弹窗。

true表示使用提示弹窗；false表示不使用提示弹窗。

默认值：false

#### selectedFont

selectedFont(font: Optional<Font>)

设置选中项文字尺寸、粗细、字体族、倾斜等样式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明font[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[Font](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__font)>是

选中项文字样式。

默认值：{

size:'13.0fp',

style:FontStyle.Normal,

weight:500,

family:'HarmonyOS Sans'

}

#### popupFont

popupFont(font: Optional<Font>)

设置提示弹窗字体样式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明font[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[Font](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__font)>是

提示弹窗字体样式。

默认值：

{

size:'19.0fp',

style:FontStyle.Normal,

weight:500,

family:'HarmonyOS Sans'

}

#### font

font(font: Optional<Font>)

设置字母索引条默认字体样式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明font[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[Font](基础类型定义.md#ZH-CN_TOPIC_0000002497604974__font)>是

字母索引条默认字体样式。

默认值：

{

size:'13.0fp',

style:FontStyle.Normal,

weight:500,

family:'HarmonyOS Sans'

}

#### itemSize

itemSize(size: Optional<LengthMetrics>)

设置字母索引条字母区域大小。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明size[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[LengthMetrics](Graphics.md#ZH-CN_TOPIC_0000002529444761__lengthmetrics12)>是

字母索引条字母区域大小，字母区域为圆形，即圆形直径。不支持设置为百分比。

默认值：24.0

单位：vp

#### selected

selected(index: Optional<number>)

设置选中项索引值。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明indexOptional<number>是

选中项索引值。

默认值：0

该参数支持[!!](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding)双向绑定变量。

#### autoCollapse

autoCollapse(enable: Optional<boolean>)

设置是否使用自适应折叠模式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明enable[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<boolean>是

是否使用自适应折叠模式。

默认值：true

true：使用自适应折叠模式。

false：不使用自适应折叠模式。

#### popupBackgroundBlurStyle

popupBackgroundBlurStyle(style: Optional<BlurStyle>)

设置提示弹窗的背景模糊材质。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明style[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[BlurStyle](背景设置.md#ZH-CN_TOPIC_0000002529444791__blurstyle9)>是

设置提示弹窗的背景模糊材质。

默认值：NONE

当通过popupBackgroundBlurStyle设置弹窗气泡的背景模糊材质时，不建议再通过[popupBackground](#ZH-CN_TOPIC_0000002497444926__popupbackground)设置背景色。

#### 事件

除支持[通用事件](通用事件.md)外，还支持以下事件：

#### onSelect

onSelect(handler: Optional<OnSelectCallback>)

索引条选中回调，返回值为当前选中索引。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明handler[Optional](自定义属性设置.md#ZH-CN_TOPIC_0000002529284845__optionalt12)<[OnSelectCallback](#ZH-CN_TOPIC_0000002497444926__onselectcallback)>是回调函数类型。

#### ArcAlphabetIndexerInitInfo对象说明

定义弧形字母索引条的初始化参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

名称类型只读可选说明arrayValuestring[]否否字母索引字符串数组，不可设置为空。selectednumber否否

初始选中项索引值，若超出索引值范围，则取默认值0。

该参数支持[!!](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding)双向绑定变量。

#### OnSelectCallback

type OnSelectCallback = (index: number) => void

定义[onSelect](#ZH-CN_TOPIC_0000002497444926__onselect)中使用的回调类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

参数名类型必填说明indexnumber是选中项序号。

#### 示例

该示例实现了弧形索引条和弧形列表联动控制和定位。

```ets
// xxx.ets
import {
  LengthMetrics,
  ColorMetrics,
  ArcList,
  ArcListItem,
  ArcListAttribute,
  ArcListItemAttribute,
  ArcAlphabetIndexer,
  ArcAlphabetIndexerAttribute
} from '@kit.ArkUI';
// 从API Version 22开始，无需手动导入ArcListAttribute、ArcListItemAttribute、ArcAlphabetIndexerAttribute。具体请参考ArcList、ArcListItem、ArcAlphabetIndexer的导入模块说明。

@Entry
@Component
struct ArcListAndIndexer {
  private fullValue: string[] = [
    '#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
  ];
  private arrName : string[] = [
    '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20',
    '21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38',
    '39','40', '41','42',
  ];

  private scrollerForList: Scroller = new Scroller();
  @State indexerIndex: number = 0;

  private watchSize: string = '466px'; // 手表默认宽高：233*233
  private itemSize: number = 24;  // 索引项默认大小：24

  build() {
    Column() {
      Row() {
        Stack() {
          ArcList({ scroller : this.scrollerForList, initialIndex: 0 }) {
            ForEach(this.arrName, (itemName: string, index: number) => {
              ArcListItem() {
                Text(itemName)
                  .width('90%')
                  .height('92px')
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .backgroundColor(index % 2 == 0 ? 0xAFEEEE : 0x00FFFF)
                  .borderRadius(23)
              }
            })
          }
          .scrollBar(BarState.Off)
          .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {
            this.indexerIndex = centerIndex;
          })
          .borderWidth(1)
          .width(this.watchSize)
          .height(this.watchSize)
          .borderRadius(this.watchSize)
          .space(LengthMetrics.px(4))

          ArcAlphabetIndexer({ arrayValue: this.fullValue, selected: 0 })
            .autoCollapse(true)
            .width(this.watchSize)
            .height(this.watchSize)
            .usePopup(false)
            .selected(this.indexerIndex)
            .onSelect((index: number) => {
              this.indexerIndex = index;
              this.scrollerForList.scrollToIndex(this.indexerIndex);
            })
            .borderWidth(1)
            .hitTestBehavior(HitTestMode.Transparent)
            .selectedColor(ColorMetrics.resourceColor(0xFFFFFF))
            .selectedBackgroundColor(ColorMetrics.resourceColor(0x1F71FF))
            .color(ColorMetrics.resourceColor(0xFFFFFF))
            .popupColor(ColorMetrics.resourceColor(0xFFFFFF))
            .popupBackground(ColorMetrics.resourceColor(0xD8404040))
            .itemSize(LengthMetrics.px(this.itemSize))
            .selectedFont({
              size:'11.0fp',
              style:FontStyle.Normal,
              weight:500,
              family:'HarmonyOS Sans'
            })
            .font({
              size:'11.0fp',
              style:FontStyle.Normal,
              weight:500,
              family:'HarmonyOS Sans'
            })

        }.width('100%').height('100%')
      }.width('100%').height('100%')
    }
  }
}
```