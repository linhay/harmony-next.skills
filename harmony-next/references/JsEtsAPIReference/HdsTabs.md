# HdsTabs

该组件暂不支持TV设备。

本模块提供Tabs容器组件的分割线样式，模糊样式和页签侧边栏半屏居中对齐样式的效果。

HdsTabs组件是根视图容器，一般作为Page页面的根容器使用。HdsTabs组件包含了内容区和页签栏，其中内容区默认显示第一个页签内容，开发者可以通过翻页滑动或者点击页签切换内容区。

**起始版本：**6.0.0(20)

#### 导入模块

```ets
import { HdsTabs, HdsTabsAttribute, HdsTabsController } from '@kit.UIDesignKit';
```

#### 子组件

子组件为[TabContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent)。

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

#### 接口

HdsTabs(options?: HdsTabsOptions)

创建HdsTabs容器。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[HdsTabsOptions](#section194091491257)

否

HdsTabs组件参数。

#### HdsTabsOptions

HdsTabs组件参数，继承自[TabsOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#tabsoptions15)。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

名称

类型

只读

可选

说明

controller

[HdsTabsController](#section13103111423616)

否

是

HdsTabs控制器。

默认值：undefined。

#### HdsTabsController

HdsTabs组件的控制器，用于控制HdsTabs组件进行页签切换。不支持一个HdsTabsController控制多个HdsTabs组件，继承自[TabsController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#tabscontroller)。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

#### bindScroller

bindScroller(value: number, scroller: Scroller, parentScroller?: Scroller): void

HdsTabs的控制器绑定内容区的滚动组件。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

value

number

是

页签的索引，索引从0开始计算。

scroller

[Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scroller)

是

滚动组件的控制器。

parentScroller

[Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scroller)

否

滚动组件的父控制器。

#### unbindScroller

unbindScroller(scroller: Scroller): void

HdsTabs的控制器解除绑定内容区的滚动组件。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

scroller

[Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scroller)

是

滚动组件的控制器。

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：

#### vertical

vertical(value: boolean)

设置是否为纵向Tab。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

value

boolean

是

是否为纵向Tab。

true：纵向Tabs；false：横向Tabs。

默认值：false。

当横向Tabs设置height为auto时，HdsTabs组件高度自适应子组件高度，即为tabBar高度+divider线宽+TabContent高度+上下padding值+上下border宽度。

当纵向Tabs设置width为auto时，HdsTabs组件宽度自适应子组件宽度，即为tabBar宽度+divider线宽+TabContent宽度+左右padding值+左右border宽度。

尽量保持每一个页面中的子组件尺寸大小一致，避免滑动页面时出现页面切换动画跳动现象。

#### barPosition

barPosition(value: BarPosition)

设置Tabs的页签位置。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

value

[BarPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#barposition枚举说明)

是

设置Tabs的页签位置。

默认值：BarPosition.Start。

#### scrollable

scrollable(value: boolean)

设置是否可以通过滑动页面进行页面切换。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

value

boolean

是

是否可以通过滑动页面进行页面切换。

true：可以通过滑动页面来切换页面；false：不可通过滑动页面来切换页面。

默认值：true。

#### barWidth

barWidth(value: Length)

设置TabBar的宽度值。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

value

[Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length)

是

TabBar的宽度值，单位：vp。若设置值小于0或大于Tabs宽度值时，按默认值显示。

默认值：

- 未设置[SubTabBarStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent#subtabbarstyle9)和[BottomTabBarStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent#bottomtabbarstyle9)的TabBar且vertical属性为false时，默认值为Tabs的宽度。
- 未设置SubTabBarStyle和BottomTabBarStyle的TabBar且vertical属性为true时，默认值为56vp。
- 设置SubTabBarStyle样式且vertical属性为false时，默认值为Tabs的宽度。
- 设置SubTabBarStyle样式且vertical属性为true时，默认值为56vp。
- 设置BottomTabBarStyle样式且vertical属性为true时，默认值为96vp。
- 设置BottomTabBarStyle样式且vertical属性为false时，默认值为Tabs的宽度。

#### barHeight

barHeight(value: Length)

设置TabBar的高度值。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

value

[Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length)

是

TabBar的高度值。单位：vp。设置为'auto'时，TabBar自适应子组件高度，仅在横向Tabs下有效。设置为小于0或大于Tabs高度值时，按默认值显示。

默认值：

- 未设置带样式的TabBar且vertical属性为false时，默认值为48vp。
- 未设置带样式的TabBar且vertical属性为true时，默认值为Tabs的高度。
- 设置[SubTabBarStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent#subtabbarstyle9)样式且vertical属性为false时，默认值为48vp。设置SubTabBarStyle样式且vertical属性为true时，默认值为Tabs的高度。
- 设置[BottomTabBarStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent#bottomtabbarstyle9)样式且vertical属性为true时，默认值为Tabs的高度。
- 设置BottomTabBarStyle样式且vertical属性为false时，默认值为48vp。

#### animationDuration

animationDuration(value: number)

设置点击TabBar页签或调用HdsTabsController的changeIndex接口时切换TabContent的动画时长。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

value

number

是

点击TabBar页签或调用TabsController的changeIndex接口切换TabContent的动画时长。

默认值：

- 不设置该属性或设置为异常值情况下，若存在BottomTabBarStyle样式的TabBar时，默认值为0。
- 设置所有TabBar为非BottomTabBarStyle样式时，默认值为300。

单位：ms。

取值范围：[0, +∞)。

#### barOverlap

barOverlap(value: boolean)

设置TabBar是否背后变模糊并叠加在TabContent之上。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

value

boolean

是

TabBar是否背后变模糊并叠加在TabContent之上。

true：TabBar背后变模糊并叠加在TabContent之上，并且barBackgroundBlurStyle属性默认模糊材质的BlurStyle值修改为'BlurStyle.COMPONENT_THICK'。

false：无模糊和叠加效果。

默认值：false。

#### barBackgroundColor

barBackgroundColor(value: ResourceColor)

设置TabBar的背景颜色。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

value

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

是

TabBar的背景颜色。

默认值：Color.Transparent。

#### barBackgroundBlurStyle

barBackgroundBlurStyle(style: BlurStyle, options?: BackgroundBlurStyleOptions)

为TabBar提供一种在背景和内容之间的模糊能力，通过枚举值的方式封装了不同的模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

style

[BlurStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#blurstyle9)

是

背景模糊样式。

options

[BackgroundBlurStyleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundblurstyleoptions10对象说明)

否

背景模糊选项。

#### barBackgroundEffect

barBackgroundEffect(options: BackgroundEffectOptions)

设置TabBar背景属性，包含背景模糊半径，亮度，饱和度，颜色等参数。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

options

[BackgroundEffectOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundeffectoptions11)

是

设置TabBar背景属性包括：模糊半径、亮度、饱和度、颜色等。

#### barMode

barMode(value: HdsBarMode, options?: ScrollableBarModeOptions)

设置TabBar的布局模式。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

value

[HdsBarMode](#section880135003119)

是

所有TabBar都使用实际布局宽度，当设置为BarMode.Scrollable时，若实际布局宽度超过总宽度（横向Tabs的barWidth，纵向Tabs的barHeight），则具有滑动效果；当设置为HALF_SCREEN_FIXED时，所有页签总高度之和为HdsTabs组件高度的四分之一，且处在二分之一屏的居中位置。

 说明：

当设置为HALF_SCREEN_FIXED样式时：

1. 依赖页签位于侧边栏，vertical设置为true。
1. 依赖页签使用BottomTabBarStyle样式。

options

[ScrollableBarModeOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#scrollablebarmodeoptions10对象说明)

否

Scrollable模式下的TabBar的布局样式。

 说明：

仅横向tabs（vertical为false）下有效。

#### divider

divider(value: Optional<HdsDividerStyle>)

设置区分TabBar和TabContent的分割线样式。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

value

[Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt12)<[HdsDividerStyle](#section9535642152319)>

是

分割线样式，默认跟手渐变。

mode：分割线模式，可以设置为常隐，常显和跟手渐变显隐（当内容区超过页签栏）。

style：分割线的样式。

1.依赖页签栏位于容器底部，barPosition设置为BarPosition.End，vertical设置为false。

2.跟手滑动效果仅限支持滚动的通用接口的组件，其他类型组件由开发者自己实现。

3.跟手滑动效果依赖HdsTabs控制器绑定需要设置的list滑动控制器。

#### barBackgroundStyle

barBackgroundStyle(backgroundStyle: Optional<HdsTabsBackgroundStyle>)

设置模糊样式为渐变模糊。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

backgroundStyle

[Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt12)<[HdsTabsBackgroundStyle](#section86661977269)>

是

设置模糊的颜色和高度，默认模糊效果失效。

1.依赖页签栏位于容器底部，barPosition设置为BarPosition.End，vertical设置为false。

2.TabBar叠加在TabContent之上，barOverlap设置为true。

3.去掉TabBar节点默认设置的模糊值barBackgroundBlurStyle的值为BlurStyle.NONE。

#### blurStrategy

blurStrategy(value: BlurStrategy)

设置页签栏的模糊生效策略。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

value

[BlurStrategy](HdsNavigation.md#section1086755971212)

是

设置页签栏的模糊生效策略。

默认值：BlurStrategy.ADAPTIVE。

#### HdsDividerStyle

页签栏分割线配置。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

名称

类型

只读

可选

说明

mode

[DividerMode](#section186781730153111)

否

否

页签栏分割线显示类型。

默认值：DividerMode.FOLLOW_SCROLL。

style

[DividerStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#dividerstyle10对象说明)

否

是

页签栏分割线样式。

默认值：

{strokeWidth: '1px'，color: '#33000000'}。

#### HdsTabsBackgroundStyle

渐变模糊样式。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

名称

类型

只读

可选

说明

maskColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

是

渐变模糊的颜色设置。

默认值：#CCFFFFFF。

maskHeight

number

否

是

渐变模糊的高度设置。

默认值：组件高度（包含底部TabBar高度）+32vp。

#### 事件

#### onChange

onChange(event: Callback<number>)

底部页签切换时触发该事件。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

event

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)<number>

是

底部页签切换时触发该事件，获取切换后的页签下标。

#### onAnimationStart

onAnimationStart(handler: OnTabsAnimationStartCallback)

切换动画开始时触发该回调。当[animationDuration](#section13511122142)为0时动画关闭，不触发该回调。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

handler

[OnTabsAnimationStartCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#ontabsanimationstartcallback18)

是

切换的动画开始时触发该事件。

#### onContentWillChange

onContentWillChange(handler: OnTabsContentWillChangeCallback)

自定义Tabs页面切换拦截事件能力，新页面即将显示时触发该回调。

满足以下任一条件，即可触发该事件：

1、滑动TabContent切换新页面时触发。

2、通过TabsController.changeIndex接口切换新页面时触发。

3、通过动态修改index属性值切换新页面时触发。

4、通过点击TabBar页签切换新页面时触发。

5、TabBar页签获焦后，通过键盘左右方向键等切换新页面时触发。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

handler

[OnTabsContentWillChangeCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#ontabscontentwillchangecallback18)

是

自定义Tabs页面切换拦截事件能力。

#### onTabBarClick

onTabBarClick(event: Callback<number>)

Tab页签点击后触发的事件。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

参数：

参数名

类型

必填

说明

event

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)<number>

是

被点击的index索引，索引从0开始计算。

#### ExtendBarMode

页签栏布局模式枚举。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

名称

值

说明

HALF_SCREEN_FIXED

100

页签栏布局模式：半屏居中布局。

#### DividerMode

页签栏分割线显示类型枚举。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

名称

值

说明

VISIBLE

0

页签栏分割线显示类型：常显。

NONE

1

页签栏分割线显示类型：常隐。

FOLLOW_SCROLL

2

页签栏分割线显示类型：跟手渐变。

#### HdsBarMode

type HdsBarMode= ExtendBarMode | BarMode

HdsBarMode页签栏的布局模式和扩展模式设置。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

类型

说明

[ExtendBarMode](#section15758214103115)

TabBar扩展的布局模式。

[BarMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#barmode枚举说明)

TabBar布局模式。

#### bleedIconStyle

bleedIconStyle(builder: CustomTabBuilder): void

在TabsContent组件上设置自定义的出血图标。

**装饰器类型：**@Builder

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

builder

[CustomTabBuilder](#section1434192490)

是

设置自定义组件出血效果。

#### CustomTabBuilder

type CustomTabBuilder= () => void

自定义组件。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

#### 示例

#### 支持分割线出现和消失

通过设置分割线属性中的类型 ，控制分割线的常显、常隐、跟手效果。

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

```ets
import { HdsTabs, HdsTabsController, DividerMode, HdsTabsAttribute } from '@kit.UIDesignKit';

@Entry
@Component
struct Index {
  private controller: HdsTabsController = new HdsTabsController();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8];
  @State mode: DividerMode = DividerMode.FOLLOW_SCROLL;
  listScroller0: ListScroller = new ListScroller();
  listScroller1: ListScroller = new ListScroller();

  aboutToAppear(): void {
    this.controller.bindScroller(0, this.listScroller0);
    this.controller.bindScroller(1, this.listScroller1);
  }

  aboutToDisappear(): void {
    this.controller.unbindScroller(this.listScroller0);
    this.controller.unbindScroller(this.listScroller1);
  }

  build() {
    Column() {
      Column() {
        Row() {
          Text('分割线展示:')
            .width('25%')
          Button('Visible')
            .onClick(() => {
              this.mode = DividerMode.VISIBLE; // 将分割线显示类型设置为常显
            })
          Button('None')
            .onClick(() => {
              this.mode = DividerMode.NONE; // 将分割线显示类型设置为常隐
            })
          Button('Follow Scroll')
            .onClick(() => {
              this.mode = DividerMode.FOLLOW_SCROLL;  // 将分割线显示类型设置为跟手
            })
        }
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('10%')

      HdsTabs({ controller: this.controller }) {
        TabContent() {
          this.ContentBuilder(this.listScroller0)
        }
        .tabBar({ icon: $r('app.media.startIcon'), text: '页签1' })

        TabContent() {
          this.ContentBuilder(this.listScroller1)
        }
        .tabBar({ icon: $r('app.media.startIcon'), text: '页签2' })
      }
      .barOverlap(true)
      .barPosition(BarPosition.End)
      .vertical(false)
      .divider({
        mode: this.mode,
        style: {
          color: Color.Black,
          strokeWidth: 1,
          startMargin: 0,
          endMargin: 0
        }
      })
      .width('100%')
      .height('90%')
    }
  }

  @Builder
  ContentBuilder(listScroller: Scroller) {
    List({ scroller: listScroller }) {
      ForEach(this.arr, (item: number) => {
        ListItem() {
          Text("item" + item)
            .height(96)
            .width('100%')
            .backgroundColor(item % 2 === 0 ? Color.Pink : Color.Yellow)
            .textAlign(TextAlign.Center)
        }
      }, (item: string) => item)
    }
    .width('100%')
    .height('100%')
  }
}
```

**表1 **效果

常显

常隐

跟手

#### 支持渐变模糊

通过设置HdsTabs组件的barBackgroundStyle样式，可以自定义模糊的颜色和高度，实现渐变模糊。

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

```ets
import { HdsTabs, HdsTabsController, HdsTabsAttribute } from '@kit.UIDesignKit';

@Entry
@Component
struct Index {
  private controller: HdsTabsController = new HdsTabsController();

  build() {
    Column() {
      HdsTabs({ controller: this.controller }) {
        TabContent() {
          Column().width('100%').height('100%').backgroundColor(Color.White)
        }
        .tabBar({ icon: $r('app.media.startIcon'), text: '页签1' })

        TabContent() {
          Column().width('100%').height('100%').backgroundColor(Color.White)
        }
        .tabBar({ icon: $r('app.media.startIcon'), text: '页签2' })
      }
      .barOverlap(true)
      .barPosition(BarPosition.End)
      .vertical(false)
      .barBackgroundStyle({
        maskColor: Color.Orange,
        maskHeight: 80
      })
    }
  }
}
```

效果：

#### 支持出血效果

通过设置HdsTabs组件TabContent的tabBar样式，可以实现出血效果。

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

```ets
import { HdsTabs, HdsTabsAttribute, bleedIconStyle } from '@kit.UIDesignKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      HdsTabs() {
        TabContent() {
          Column().width('100%').height('100%').backgroundColor(Color.Yellow)
        }
        .tabBar(bleedIconStyle(() => {
          this.tabBuilder()
        }))
        TabContent() {
          Column().width('100%').height('100%').backgroundColor(Color.Blue)
        }
        .tabBar(this.tabBuilder())
      }
      .vertical(false)
      .barPosition(BarPosition.End)
    }
  }
  @Builder
  tabBuilder() {
    Column() {
      Image($r('app.media.startIcon'))
        .width(48)
        .height(48)
        .borderRadius(24)
    }
  }
}
```

效果：

#### 页签半屏居中对齐布局

通过设置HdsTabs组件的barMode样式为ExtendBarMode.HALF_SCREEN_FIXED，页签高度是Tabs高度的四分之一均分，并且半屏居中对齐。

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

```ets
import { HdsTabs, HdsTabsAttribute, ExtendBarMode } from '@kit.UIDesignKit';

@Entry
@Component
struct Index {
  @State isVertical: boolean = true;

  build() {
    Column(){
      HdsTabs({ barPosition: BarPosition.End }) {
        TabContent() {
          Column().width('100%').height('100%').backgroundColor(Color.Yellow)
        }
        .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Yellow'))
        TabContent() {
          Column().width('100%').height('100%').backgroundColor(Color.Blue)
        }
        .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Blue'))
        TabContent() {
          Column().width('100%').height('100%').backgroundColor(Color.Pink)
        }
        .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Pink'))
      }
      .vertical(this.isVertical)
      .barMode(ExtendBarMode.HALF_SCREEN_FIXED)
      .width('100%')
      .height('100%')
    }
  }
}
```

效果：