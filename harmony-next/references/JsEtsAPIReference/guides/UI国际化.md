# UI国际化

本文根据华为开发者官网 `arkts-internationalization` 页面整理为离线版入口。
来源：<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-internationalization>
更新时间：2026-04-30 02:41:24

## 利用资源限定词配置国际化资源
在开发阶段，通过DevEco Studio，可以为应用在对应语言和地区的资源限定词目录下配置不同的资源，来实现UI国际化。详细介绍请参考资源分类与访问。

## 使用镜像能力
不同国家对文本对齐方式和读取顺序有所不同，例如英语采用从左到右的顺序，阿拉伯语和希腊语则采用从右到左（RTL）的顺序。为满足不同用户的阅读习惯，ArkUI提供了镜像能力。在特定情况下将显示内容在X轴上进行镜像反转，由从左到右显示变成从右到左显示。
镜像前
镜像后
当组件满足以下任意条件时，镜像能力生效：
组件的direction属性设置为Direction.Rtl。
组件的direction属性设置为Direction.Auto，且当前的系统语言（如维吾尔语）的阅读习惯是从右向左。

## 基本概念
LTR：顺序为从左到右。
RTL：顺序为从右到左。

## 使用约束
ArkUI 如下能力已默认适配镜像：
类别
名称
基础组件
Swiper、Tabs、TabContent、List、Progress、CalendarPicker、CalendarPickerDialog、TextPicker、TextPickerDialog、DatePicker、DatePickerDialog、Grid、WaterFlow、Scroll、ScrollBar、AlphabetIndexer、Stepper、SideBarContainer、Navigation、NavDestination、Rating、Slider、Toggle、Badge、Counter、Chip、SegmentButton、bindMenu、bindContextMenu、TextInput、TextArea、Search、Stack、GridRow、Text、Select、Marquee、Row、Column、Flex、RelativeContainer、ListItemGroup
高级组件
SelectionMenu 、TreeView 、Filter、SplitLayout、ToolBar、ComposeListItem、EditableTitleBar、ProgressButton、SubHeader 、Popup、Dialog、SwipeRefresher
通用属性
position、markAnchor、offset、alignRules、borderWidth、borderColor、borderRadius、padding、margin
接口
AlertDialog、ActionSheet、promptAction.showDialog、promptAction.showToast
但如下三种场景还需要进行适配：

## 界面布局和边框设置
目前，以下三类通用属性需要使用新入参类型适配：
位置设置：position、markAnchor、offset、alignRules
边框设置：borderWidth、borderColor、borderRadius
尺寸设置：padding、margin
以position为例，需要把绝对方向x、y描述改为新入参类型start、end的描述，其他属性类似。
import { LengthMetrics } from '@kit.ArkUI'; @Entry @Component struct InterfaceLayoutBorderSettings { build() { Stack({ alignContent: Alignment.TopStart }) { Stack({ alignContent: Alignment.TopStart }) { Column() .width(100) .height(100) .backgroundColor(Color.Red) .position({ start: LengthMetrics.px(200), top: LengthMetrics.px(200) }) // 需要同时支持LTR和RTL时使用API12新增的LocalizedEdges入参类型, // 仅支持LTR时等同于.position({ x: '200px', y: '200px' }) }.backgroundColor(Color.Blue) }.width('100%').height('100%').border({ color: '#880606' }) } }

## 自定义绘制Canvas组件
Canvas组件的绘制内容和坐标均不支持镜像能力。已绘制到Canvas组件上的内容并不会跟随系统语言的切换自动做镜像效果。
CanvasRenderingContext2D的文本绘制支持镜像能力，在使用时需要与Canvas组件的通用属性direction（组件显示方向）和CanvasRenderingContext2D的属性direction（文本绘制方向）协同使用。具体规格如下：
优先级：CanvasRenderingContext2D的direction属性 > Canvas组件通用属性direction > 系统语言决定的水平显示方向。
Canvas组件本身不会自动跟随系统语言切换镜像效果，需要应用监听到系统语言切换后自行重新绘制。
CanvasRenderingContext2D绘制文本时，只有符号等文本会对绘制方向生效，英文字母和数字不响应绘制方向的变化。
import { BusinessError, commonEventManager } from '@kit.BasicServicesKit'; @Entry @Component struct CustomizeCanvasComponentDrawing { @State message: string = 'Hello world'; private settings: RenderingContextSettings = new RenderingContextSettings(true) private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings) aboutToAppear(): void { // 监听系统语言切换 let subscriber: commonEventManager.CommonEventSubscriber | null = null; let subscribeInfo2: commonEventManager.CommonEventSubscribeInfo = { events: ['usual.event.LOCALE_CHANGED'], } commonEventManager.createSubscriber(subscribeInfo2, (err: BusinessError, data: commonEventManager.CommonEventSubscriber) => { if (err) { console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`); return; } subscriber = data; if (subscriber !== null) { commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => { if (err) { return; } // 监听到语言切换后，需要重新绘制Canvas内容 this.drawText(); }) } else { console.error(`MayTest Need create subscriber`); } }) } drawText(): void { console.error('MayTest drawText') this.context.reset() this.context.direction = 'inherit' this.context.font = '30px sans-serif' this.context.fillText('ab%123&*@', 50, 50) } build() { Row() { Canvas(this.context) .direction(Direction.Auto) .width('100%') .height('100%') .onReady(() =>{ this.drawText() }) } .height('100%') } }
镜像前
镜像后

## 镜像状态字符对齐
Direction是指文字的方向，即文本在屏幕上呈现时字符的顺序。在从左到右（LTR）文本中，显示顺序是从左向右；在从右到左（RTL）文本中，显示顺序是从右到左。
TextAlign是将文本作为一个整体，在布局上的影响，具体位置会受Direction影响，以TextAlign为start为例，当Direction为LTR时，布局位置靠左；当Direction为RTL时，布局位置靠右。
在LTR与RTL文本混排时，如一个英文句子中包含阿拉伯语的单词或短语，显示顺序将变得复杂。下图为数字和维吾尔语混合时对应的字符逻辑顺序。
此时，文本渲染引擎会采用名为“双向算法”或“Unicode双向算法”（Unicode Bidirectional Algorithm）的方法来确定字符的显示顺序。下图展示了LTR与RTL文本混合时对应的字符显示顺序，确定字符方向的基本原则如下：
强字符的方向性：强字符具有明确的方向性，例如，中文为LTR，阿拉伯语为RTL，这类字符的方向性会影响其周围的中性字符。
弱字符的方向性：弱字符不具备明确的方向性，这些字符不会影响其周围中性字符的方向。
中性字符的方向性：中性字符无固定方向性，它们会继承其最近的强字符的方向；若附近无强字符，则采用全局方向。
