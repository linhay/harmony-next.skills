# MultiNavigation

MultiNavigation用于在大尺寸设备上分栏显示、进行路由跳转。

该组件从API version 14开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

由于MultiNavigation存在多重栈嵌套，调用本文档明确说明的不支持接口或不在本文档支持接口列表中的接口(例如getParent、setInterception、pushDestination等)，可能会发生无法预期的问题。

MultiNavigation在深层嵌套场景下，可能存在路由动效异常的问题。

#### 导入模块

```ets
import { MultiNavigation, MultiNavPathStack, SplitPolicy } from '@kit.ArkUI';
```

#### 子组件

不可以包含子组件。

#### MultiNavigation

MultiNavigation({navDestination: NavDestinationBuildFunction, multiStack: MultiNavPathStack, onNavigationModeChange?: OnNavigationModeChangeCallback, onHomeShowOnTop?: OnHomeShowOnTopCallback})

创建并初始化MultiNavigation组件。

MultiNavigation组件遵循默认的左起右清栈规则，这意味着从左侧主页点击时，会触发详情页的加载并同时清除右侧所有其他详情页，确保右侧仅展示最新加载的详情页。然而，若在右侧的详情页上再次执行详情页加载操作，系统将不会执行清栈动作。效果可参见[主页跳转详情页效果演示](#ZH-CN_TOPIC_0000002529444847__示例)。

**装饰器类型：**@Component

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型必填装饰器类型说明multiStack[MultiNavPathStack](#ZH-CN_TOPIC_0000002529444847__multinavpathstack)是@State设置路由栈。navDestination[NavDestinationBuildFunction](#ZH-CN_TOPIC_0000002529444847__navdestinationbuildfunction)是@BuilderParam设置加载目标页面的路由规则。onNavigationModeChange[OnNavigationModeChangeCallback](#ZH-CN_TOPIC_0000002529444847__onnavigationmodechangecallback)否-设置MultiNavigation模式变更时的回调。onHomeShowOnTop[OnHomeShowOnTopCallback](#ZH-CN_TOPIC_0000002529444847__onhomeshowontopcallback)否-设置主页处于栈顶时的回调。

#### MultiNavPathStack

当前，MultiNavigation的路由栈仅支持由使用方自行创建，不支持通过回调方式获取。请勿使用NavDestination的onReady等类似事件或接口来获取NavPathStack并进行栈操作，因为这可能会导致不可预知的问题。

#### constructor

constructor()

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### pushPath

pushPath(info: NavPathInfo, animated?: boolean, policy?: SplitPolicy): void

将指定的NavDestination页面信息入栈。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明info[NavPathInfo](Navigation.md#ZH-CN_TOPIC_0000002497444902__navpathinfo10)是NavDestination页面的信息。animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

policy[SplitPolicy](#ZH-CN_TOPIC_0000002529444847__splitpolicy枚举说明)否当前入栈页面的策略。默认值：DETAIL_PAGE

#### pushPath

pushPath(info: NavPathInfo, options?: NavigationOptions, policy?: SplitPolicy): void

将指定的NavDestination页面信息入栈，通过NavigationOptions设置页面栈操作选项。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明info[NavPathInfo](Navigation.md#ZH-CN_TOPIC_0000002497444902__navpathinfo10)是NavDestination页面的信息。options[NavigationOptions](Navigation.md#ZH-CN_TOPIC_0000002497444902__navigationoptions12)否页面栈操作选项。仅支持其中的animated字段。policy[SplitPolicy](#ZH-CN_TOPIC_0000002529444847__splitpolicy枚举说明)否当前入栈页面的策略。默认值：DETAIL_PAGE

#### pushPathByName

pushPathByName(name: string, param: Object, animated?: boolean, policy?: SplitPolicy): void

将name指定的NavDestination页面信息入栈，传递的数据为param。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。paramObject是NavDestination页面详细参数。animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

policy[SplitPolicy](#ZH-CN_TOPIC_0000002529444847__splitpolicy枚举说明)否当前入栈页面的策略。默认值：DETAIL_PAGE

#### pushPathByName

pushPathByName(name: string, param: Object, onPop?: base.Callback<PopInfo>, animated?: boolean, policy?: SplitPolicy): void

将name指定的NavDestination页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。paramObject是NavDestination页面详细参数。onPopbase.[Callback](@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__callback)<[PopInfo](Navigation.md#ZH-CN_TOPIC_0000002497444902__popinfo11)>否Callback回调，用于页面出栈时触发该回调处理返回结果。animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

policy[SplitPolicy](#ZH-CN_TOPIC_0000002529444847__splitpolicy枚举说明)否当前入栈页面的策略。默认值：DETAIL_PAGE

#### replacePath

replacePath(info: NavPathInfo, animated?: boolean): void

将当前页面栈栈顶退出，将指定的NavDestination页面信息入栈，新页面的分栏策略继承原栈顶页面的策略。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明info[NavPathInfo](Navigation.md#ZH-CN_TOPIC_0000002497444902__navpathinfo10)是NavDestination页面的信息。animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

#### replacePath

replacePath(info: NavPathInfo, options?: NavigationOptions): void

将当前页面栈栈顶退出，将指定的NavDestination页面信息入栈，新页面的分栏策略继承原栈顶页面的策略，通过NavigationOptions设置页面栈操作选项。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明info[NavPathInfo](Navigation.md#ZH-CN_TOPIC_0000002497444902__navpathinfo10)是NavDestination页面的信息。options[NavigationOptions](Navigation.md#ZH-CN_TOPIC_0000002497444902__navigationoptions12)否页面栈操作选项。仅支持其中的animated字段。

#### replacePathByName

replacePathByName(name: string, param: Object, animated?: boolean): void

将当前页面栈栈顶退出，将name指定的页面入栈，新页面的分栏策略继承原栈顶页面的策略。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。paramObject是NavDestination页面详细参数。animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

#### removeByIndexes

removeByIndexes(indexes: Array<number>): number

将页面栈内索引值在indexes中的NavDestination页面删除。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexesArray<number>是

待删除NavDestination页面的索引值数组。

number类型的取值范围：[0, +∞)

**返回值：**

类型说明number返回删除的NavDestination页面数量。

#### removeByName

removeByName(name: string): number

将页面栈内指定name的NavDestination页面删除。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是待删除NavDestination页面的名字。

**返回值：**

类型说明number返回删除的NavDestination页面数量。

#### pop

pop(animated?: boolean): NavPathInfo | undefined

弹出路由栈栈顶元素。

当调用[keepBottomPage](#ZH-CN_TOPIC_0000002529444847__keepbottompage)接口并设置为true时，会保留栈底页面。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

**返回值：**

类型说明[NavPathInfo](Navigation.md#ZH-CN_TOPIC_0000002497444902__navpathinfo10) | undefined返回栈顶NavDestination页面的信息。

#### pop

pop(result?: Object, animated?: boolean): NavPathInfo | undefined

弹出路由栈栈顶元素，并触发onPop回调传入页面处理结果。

当调用[keepBottomPage](#ZH-CN_TOPIC_0000002529444847__keepbottompage)接口并设置为true时，会保留栈底页面。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明resultObject否页面自定义处理结果。animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

**返回值：**

类型说明[NavPathInfo](Navigation.md#ZH-CN_TOPIC_0000002497444902__navpathinfo10) | undefined返回栈顶NavDestination页面的信息。

#### popToName

popToName(name: string, animated?: boolean): number

回退路由栈到由栈底开始第一个名为name的NavDestination页面。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

**返回值：**

类型说明number

如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。

取值范围：[-1, +∞)

#### popToName

popToName(name: string, result: Object, animated?: boolean): number

回退路由栈到由栈底开始第一个名为name的NavDestination页面，并触发onPop回调传入页面处理结果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。resultObject是页面自定义处理结果。animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

**返回值：**

类型说明number

如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。

取值范围：[-1, +∞)

#### popToIndex

popToIndex(index: number, animated?: boolean): void

回退路由栈到index指定的NavDestination页面。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是

NavDestination页面的位置索引。

取值范围：[0, +∞)

animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

#### popToIndex

popToIndex(index: number, result: Object, animated?: boolean): void

回退路由栈到index指定的NavDestination页面，并触发onPop回调传入页面处理结果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是

NavDestination页面的位置索引。

取值范围：[0, +∞)

resultObject是页面自定义处理结果。animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

#### moveToTop

moveToTop(name: string, animated?: boolean): number

将由栈底开始第一个名为name的NavDestination页面移到栈顶。

根据找到的第一个名为name的页面的不同，MultiNavigation会进行不同的处理：

1)当找到的是最上层主页或者全屏页，此时不做任何处理；

2)当找到的是最上层主页对应的详情页，则会将对应的详情页移到栈顶；

3)当找到的是非最上层的主页，则会将主页和对应所有详情页移到栈顶，详情页相对栈关系不变；

4)当找到的是非最上层的详情页，则会将主页和对应所有详情页移到栈顶，且将目标详情页移动到对应所有详情页的栈顶；

5)当找到的是非最上层的全屏页，则会将全屏页移动到栈顶。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

**返回值：**

类型说明number如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。

#### moveIndexToTop

moveIndexToTop(index: number, animated?: boolean): void

将指定index的NavDestination页面移到栈顶。

根据找到的第一个名为name的页面的不同，MultiNavigation会进行不同的处理：

1)当找到的是最上层主页或者全屏页，此时不做任何处理；

2)当找到的是最上层主页对应的详情页，则会将对应的详情页移到栈顶；

3)当找到的是非最上层的主页，则会将主页和对应所有详情页移到栈顶，详情页相对栈关系不变；

4)当找到的是非最上层的详情页，则会将主页和对应所有详情页移到栈顶，且将目标详情页移动到对应所有详情页的栈顶；

5)当找到的是非最上层的全屏页，则会将全屏页移动到栈顶。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是

NavDestination页面的位置索引。

取值范围：[0, +∞)

animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

#### clear

clear(animated?: boolean): void

清除栈中所有页面。

当调用[keepBottomPage](#ZH-CN_TOPIC_0000002529444847__keepbottompage)接口并设置为true时，会保留栈底页面。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明animatedboolean否

是否支持转场动画。

默认值：true

true：支持转场动画。

false：不支持转场动画。

#### getAllPathName

getAllPathName(): Array<string>

获取栈中所有NavDestination页面的名称。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明Array<string>返回栈中所有NavDestination页面的名称。

#### getParamByIndex

getParamByIndex(index: number): Object | undefined

获取index指定的NavDestination页面的参数信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明indexnumber是

NavDestination页面的位置索引。

取值范围：[0, +∞)

**返回值：**

类型说明Object | undefined

Object：返回对应NavDestination页面的参数信息。

undefined: 传入index无效时返回undefined。

#### getParamByName

getParamByName(name: string): Array<Object>

获取全部名为name的NavDestination页面的参数信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。

**返回值：**

类型说明Array<Object>返回全部名为name的NavDestination页面的参数信息。

#### getIndexByName

getIndexByName(name: string): Array<number>

获取全部名为name的NavDestination页面的位置索引。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是NavDestination页面名称。

**返回值：**

类型说明Array<number>

返回全部名为name的NavDestination页面的位置索引。

number类型的取值范围：[0, +∞)

#### size

size(): number

获取栈大小。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

类型说明number

返回栈大小。

取值范围：[0, +∞)

#### disableAnimation

disableAnimation(disable: boolean): void

关闭（true）或打开（false）当前MultiNavigation中所有转场动画。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明disableboolean是

是否关闭转场动画。

默认值：false

true：关闭转场动画。

false：不关闭转场动画。

#### switchFullScreenState

switchFullScreenState(isFullScreen?: boolean): boolean

切换当前顶栈详情页面的显示模式。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明isFullScreenboolean否是否切换为全屏。默认值为false。true表示全屏模式，false表示分栏模式。

**返回值：**

类型说明boolean

切换成功或失败。

true：切换成功。

false：切换失败。

#### setHomeWidthRange

setHomeWidthRange(minPercent: number, maxPercent: number): void

设置主页宽度可拖动范围。应用不设置的情况下宽度为50%，且不可拖动。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明minPercentnumber是

最小主页宽度百分比。

取值范围：[0, 100]

maxPercentnumber是

最大主页宽度百分比。

取值范围：[0, 100]

#### keepBottomPage

keepBottomPage(keepBottom: boolean): void

设置在调用pop和clear接口时是否保留栈底页面。

MultiNavigation将主页也当作了NavDestination页面入栈，所以调用pop或clear接口时会将栈底页面也出栈。

应用调用此接口并设置为TRUE时，MultiNavigation会在调用pop和clear接口时保留栈底页面。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明keepBottomboolean是

是否保留栈底页面。

默认值：false

true：保留栈底页面。

false：不保留栈底页面。

#### setPlaceholderPage

setPlaceholderPage(info: NavPathInfo): void

设置占位页面。

占位页面为特殊页面类型，当应用设置后，在一些大屏设备上会和主页默认形成左右分栏的效果，即左边主页，右边占位页。

当应用可绘制区域小于600VP、折叠屏由展开态切换为折叠态及平板横屏转竖屏等场景时，会自动将占位页出栈，只显示主页；

而当应用可绘制区域大于等于600VP、折叠屏由折叠态切换为展开态及平板竖屏转横屏等场景时，会自动补充占位页，形成分栏。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明info[NavPathInfo](Navigation.md#ZH-CN_TOPIC_0000002497444902__navpathinfo10)是占位页页面信息。

#### SplitPolicy枚举说明

表示MultiNavigation中页面的类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明HOME_PAGE0主页页面类型。全屏模式显示。DETAIL_PAGE1详情页页面类型。分栏模式显示。FULL_PAGE2全屏页页面类型。全屏模式显示。

#### NavDestinationBuildFunction

type NavDestinationBuildFunction = (name: string, param?: object) => void

MultiNavigation用以加载NavDestination的方法。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是路由页面的标识符。paramobject否路由跳转创建页面时传递的参数。

#### OnNavigationModeChangeCallback

type OnNavigationModeChangeCallback = (mode: NavigationMode) => void

当MultiNavigation的mode变化时触发的回调函数。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明mode[NavigationMode](Navigation.md#ZH-CN_TOPIC_0000002497444902__navigationmode9枚举说明)是当回调触发时的NavigationMode。

#### OnHomeShowOnTopCallback

type OnHomeShowOnTopCallback = (name: string) => void

当主页在栈顶显示时触发的回调函数。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是显示在栈顶的页面的标识符。

#### 属性

不支持[通用属性](通用属性.md)。

#### 事件

不支持[通用事件](通用事件.md)。

#### 示例

本示例演示MultiNavigation的基本功能。

```ets
// pages/Index.ets
import { MultiNavigation, MultiNavPathStack, SplitPolicy } from '@kit.ArkUI';
import { PageDetail1 } from './PageDetail1';
import { PageDetail2 } from './PageDetail2';
import { PageFull1 } from './PageFull1';
import { PageHome1 } from './PageHome1';
import { PagePlaceholder } from './PagePlaceholder';

@Entry
@Component
struct Index {
  @Provide('pageStack') pageStack: MultiNavPathStack = new MultiNavPathStack();

  @Builder
  PageMap(name: string, param?: object) {
    if (name === 'PageHome1') {
      PageHome1({ param: param });
    } else if (name === 'PageDetail1') {
      PageDetail1({ param: param });
    } else if (name === 'PageDetail2') {
      PageDetail2({ param: param });
    } else if (name === 'PageFull1') {
      PageFull1();
    } else if (name === 'PagePlaceholder') {
      PagePlaceholder();
    }
  }

  aboutToAppear(): void {
    this.pageStack.pushPathByName('PageHome1', 'paramTest', false, SplitPolicy.HOME_PAGE);
  }

  build() {
    Column() {
      Row() {
        MultiNavigation({ navDestination: this.PageMap, multiStack: this.pageStack })
      }
      .width('100%')
    }
  }
}
```

```ets
// pages/PageHome1.ets, 对应首页
import { MultiNavPathStack, SplitPolicy } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Component
export struct PageHome1 {
  @State message: string = 'PageHome1';
  @Consume('pageStack') pageStack: MultiNavPathStack;
  controller: TextInputController = new TextInputController();
  text: string = '';
  param: Object = new Object();
  lastBackTime: number = 0;

  build() {
    if (this.log()) {
      NavDestination() {
        Column() {
          Column() {
            Text(this.message)
              .fontSize(40)
              .fontWeight(FontWeight.Bold)
          }
          .width('100%')
          .height('8%')
          Scroll(){
            Column() {
              Button('OpenHome', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 跳转至PageHome1页面
                    this.pageStack.pushPathByName('PageHome1', 'testParam', true, SplitPolicy.HOME_PAGE);
                  }
                })
              Button('OpenDetail', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 跳转至PageDetail1页面
                    this.pageStack.pushPathByName('PageDetail1', 'testParam');
                  }
                })
              Button('OpenFull', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 跳转至PageFull1页面
                    this.pageStack.pushPathByName('PageFull1', 'testParam', true, SplitPolicy.FULL_PAGE);
                  }
                })
              TextInput({placeholder: 'input your popToIndex ...', controller: this.controller })
                .placeholderColor(Color.Grey)
                .placeholderFont({ size: 14, weight: 400 })
                .caretColor(Color.Blue)
                .width('50%')
                .height(40)
                .margin(20)
                .type(InputType.Number)
                .fontSize(14)
                .fontColor(Color.Black)
                .onChange((value: string) => {
                  this.text = value;
                })
              Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 返回至指定index页面，删除大于该index的所有页面
                    this.pageStack.popToIndex(Number(this.text));
                    this.controller.caretPosition(1);
                  }
                })
              Button('OpenDetailWithName', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 跳转至PageDetail1页面
                    this.pageStack.pushPathByName('PageDetail1', 'testParam', undefined, true);
                  }
                })
              Button('pop', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    this.pageStack.pop();
                  }
                })
              Button('moveToTopByName: PageDetail1', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(10)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 将PageDetail1页面移动至栈顶
                    let indexFound = this.pageStack.moveToTop('PageDetail1');
                    hilog.info(0x0000, 'demoTest', 'moveToTopByName,indexFound:' + indexFound);
                  }
                })
              Button('removeByName HOME', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 删除名称为PageHome1的页面
                    this.pageStack.removeByName('PageHome1');
                  }
                })
              Button('removeByIndexes 0135', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 删除栈中index为0，1，3，5的页面
                    this.pageStack.removeByIndexes([0,1,3,5]);
                  }
                })
              Button('getAllPathName', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    let result = this.pageStack.getAllPathName();
                    hilog.info(0x0000, 'demoTest', 'getAllPathName: ' + result.toString());
                  }
                })
              Button('getParamByIndex0', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 获取index为0的页面的参数
                    let result = this.pageStack.getParamByIndex(0);
                    hilog.info(0x0000, 'demoTest', 'getParamByIndex: ' + result);
                  }
                })
              Button('getParamByNameHomePage', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 获取名称为PageHome1的页面的参数
                    let result = this.pageStack.getParamByName('PageHome1');
                    hilog.info(0x0000, 'demoTest', 'getParamByName: ' + result.toString());
                  }
                })
              Button('getIndexByNameHomePage', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 获取名称为PageHome1的页面的Index
                    let result = this.pageStack.getIndexByName('PageHome1');
                    hilog.info(0x0000, 'demoTest', 'getIndexByName: ' + result);
                  }
                })
              Button('keepBottomPage True', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(10)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 设置栈底页面无法被移除
                    this.pageStack.keepBottomPage(true);
                  }
                })
              Button('keepBottomPage False', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(10)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 设置栈底页面可以被移除
                    this.pageStack.keepBottomPage(false);
                  }
                })
              Button('setPlaceholderPage', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(10)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    this.pageStack.setPlaceholderPage({ name: 'PagePlaceholder' });
                  }
                })
            }.backgroundColor(0xFFFFFF).width('100%').padding(10).borderRadius(15)
            }
            .width('100%')
          }
          .width('100%')
          .height('92%')
        }.hideTitleBar(true)
      }
    }

  log(): boolean {
    hilog.info(0x0000, 'demoTest', 'PageHome1 build called');
    return true;
  }
}
```

```ets
// pages/PageDetail1.ets：详情页
import { MultiNavPathStack, SplitPolicy } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Component
export struct PageDetail1 {
  @State message: string = 'PageDetail1';
  @Consume('pageStack') pageStack: MultiNavPathStack;
  controller: TextInputController = new TextInputController();
  text: string = '';
  param: Object = new Object();

  build() {
    if (this.log()) {
      NavDestination() {
        Column() {
          Column() {
            Text(this.message)
              .fontSize(40)
              .fontWeight(FontWeight.Bold)
          }
          .height('8%')
          .width('100%')
          Scroll(){
            Column(){
              Button('OpenHome', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 跳转至PageHome1页面
                    this.pageStack.pushPathByName('PageHome1', 'testParam', true, SplitPolicy.HOME_PAGE);
                  }
                })
              Button('OpenDetail', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 跳转至PageDetail1页面
                    this.pageStack.pushPathByName('PageDetail1', 'testParam');
                  }
                })
              Button('OpenFull', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 跳转至PageFull1页面
                    this.pageStack.pushPathByName('PageFull1', 'testParam', true, SplitPolicy.FULL_PAGE);
                  }
                })
              Button('ReplaceDetail', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 使用PageDetail2替换当前页面
                    this.pageStack.replacePathByName('PageDetail2', 'testParam');
                  }
                })
              Button('removeByName PageDetail1', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 删除栈中name为PageDetail1的页面
                    this.pageStack.removeByName('PageDetail1');
                  }
                })
              Button('removeByIndexes 0135', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 删除栈中index为0，1，3，5的页面
                    this.pageStack.removeByIndexes([0,1,3,5]);
                  }
                })
              Button('switchFullScreenState true', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 将页面设置为全屏
                    this.pageStack.switchFullScreenState(true);
                  }
                })
              Button('switchFullScreenState false', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 将页面设置为非全屏
                    this.pageStack.switchFullScreenState(false);
                  }
                })
              Button('pop', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    this.pageStack.pop('123');
                  }
                })
              Button('popToHome1', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 返回至指定name的页面，删除大于该页面index的所有其他页面
                    this.pageStack.popToName('PageHome1');
                  }
                })
              TextInput({placeholder: 'input your popToIndex ...', controller: this.controller })
                .placeholderColor(Color.Grey)
                .placeholderFont({ size: 14, weight: 400 })
                .caretColor(Color.Blue)
                .type(InputType.Number)
                .width('50%')
                .height(40)
                .margin(20)
                .fontSize(14)
                .fontColor(Color.Black)
                .onChange((value: string) => {
                  this.text = value;
                })
              Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 返回至指定index页面，删除大于该index的所有页面
                    this.pageStack.popToIndex(Number(this.text));
                    this.controller.caretPosition(1);
                  }
                })
              Button('moveIndexToTop', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 将指定Index页面移动至栈顶
                    this.pageStack.moveIndexToTop(Number(this.text));
                    this.controller.caretPosition(1);
                  }
                })
              Button('clear', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 清空当前路由栈
                    this.pageStack.clear();
                  }
                })
              Button('disableAnimation', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 关闭当前栈对应栈操作的动画
                    this.pageStack.disableAnimation(true);
                  }
                })
              Button('enableAnimation', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 开启当前栈对应栈操作的动画
                    this.pageStack.disableAnimation(false);
                  }
                })
              Button('setHomeWidthRange(20, 80)', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    this.pageStack.setHomeWidthRange(20, 80);
                  }
                })
              Button('setHomeWidthRange(-1, 20)', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    this.pageStack.setHomeWidthRange(-1, 20);
                  }
                })
              Button('setHomeWidthRange(20, 120)', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    this.pageStack.setHomeWidthRange(20, 120);
                  }
                })
            }
            .width('100%')
          }
          .width('100%')
          .height('92%')
        }
      }.hideTitleBar(true)
    }
  }

  log(): boolean {
    hilog.info(0x0000, 'demoTest', 'PageDetail1 build called');
    return true;
  }
}
```

```ets
// pages/PageDetail2.ets: 详情页
import { MultiNavPathStack, SplitPolicy } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Component
export struct PageDetail2 {
  @State message: string = 'PageDetail2';
  @Consume('pageStack') pageStack: MultiNavPathStack;
  controller: TextInputController = new TextInputController();
  text: string = '';
  param: Object = new Object();

  build() {
    if (this.log()) {
      NavDestination() {
        Column() {
          Column() {
            Text(this.message)
              .fontSize(40)
              .fontWeight(FontWeight.Bold)
          }
          .width('100%')
          .height('8%')
          Scroll(){
            Column() {
              Button('OpenHome', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 跳转至PageHome1页面
                    this.pageStack.pushPathByName('PageHome1', 'testParam', true, SplitPolicy.HOME_PAGE);
                  }
                })
              Button('OpenDetail', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 跳转至PageDetail1页面
                    this.pageStack.pushPathByName('PageDetail1', 'testParam');
                  }
                })
              Button('OpenFull', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 跳转至PageFull1页面
                    this.pageStack.pushPathByName('PageFull1', 'testParam', true, SplitPolicy.FULL_PAGE);
                  }
                })
              Button('ReplaceDetail', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 使用PageDetail2替换当前页面
                    this.pageStack.replacePathByName('PageDetail2', 'testParam');
                  }
                })
              TextInput({placeholder: 'input your popToIndex ...', controller: this.controller })
                .placeholderColor(Color.Grey)
                .placeholderFont({ size: 14, weight: 400 })
                .caretColor(Color.Blue)
                .type(InputType.Number)
                .width('50%')
                .height(40)
                .margin(20)
                .fontSize(14)
                .fontColor(Color.Black)
                .onChange((value: string) => {
                  this.text = value;
                })
              Button('moveIndexToTop', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 将指定index的页面移动至栈顶
                    this.pageStack.moveIndexToTop(Number(this.text));
                    this.controller.caretPosition(1);
                  }
                })
              Button('pop', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    this.pageStack.pop();
                  }
                })
              TextInput({placeholder: 'input your popToIndex ...', controller: this.controller })
                .placeholderColor(Color.Grey)
                .placeholderFont({ size: 14, weight: 400 })
                .caretColor(Color.Blue)
                .type(InputType.Number)
                .width('50%')
                .height(40)
                .margin(20)
                .fontSize(14)
                .fontColor(Color.Black)
                .onChange((value: string) => {
                  this.text = value;
                })
              Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 返回至指定index页面，删除大于该index的所有页面
                    this.pageStack.popToIndex(Number(this.text));
                    this.controller.caretPosition(1);
                  }
                })
              Button('clear', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 清空当前路由栈
                    this.pageStack.clear();
                  }
                })
              Button('disableAnimation', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 关闭当前栈对应栈操作的动画
                    this.pageStack.disableAnimation(true);
                  }
                })
              Button('enableAnimation', { stateEffect: true, type: ButtonType.Capsule})
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 开启当前栈对应栈操作的动画
                    this.pageStack.disableAnimation(false);
                  }
                })
            }
            .width('100%')
          }
          .width('100%')
          .height('92%')
        }
      }
      .hideTitleBar(true)
    }
  }

  log(): boolean {
    hilog.info(0x0000, 'demoTest', 'PageDetail2 build called');
    return true;
  }
}
```

```ets
// pages/PageFull1.ets: 不参与分栏的页面，默认全屏展示
import { MultiNavPathStack, SplitPolicy } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Component
export struct PageFull1 {
  @State message: string = 'PageFull1';
  @Consume('pageStack') pageStack: MultiNavPathStack;
  controller: TextInputController = new TextInputController();
  text: string = '';

  build() {
    if (this.log()) {
      NavDestination() {
        Column() {
          Column() {
            Text(this.message)
              .fontSize(40)
              .fontWeight(FontWeight.Bold)
          }
          .width('100%')
          .height('8%')

          Scroll() {
            Column() {
              Button('OpenHome', { stateEffect: true, type: ButtonType.Capsule })
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 跳转至PageHome1页面
                    this.pageStack.pushPathByName('PageHome1', 'testParam', true, SplitPolicy.HOME_PAGE);
                  }
                })
              Button('OpenDetail', { stateEffect: true, type: ButtonType.Capsule })
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 跳转至PageDetail1页面
                    this.pageStack.pushPathByName('PageDetail1', 'testParam');
                  }
                })
              Button('OpenFull', { stateEffect: true, type: ButtonType.Capsule })
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 跳转至PageFull1页面
                    this.pageStack.pushPathByName('PageFull1', 'testParam', true, SplitPolicy.FULL_PAGE);
                  }
                })
              Button('ReplaceFULL', { stateEffect: true, type: ButtonType.Capsule })
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 使用PageFull1页面替换当前页面
                    this.pageStack.replacePathByName('PageFull1', 'testParam', true);
                  }
                })
              Button('removeByName PageFull1', { stateEffect: true, type: ButtonType.Capsule })
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 删除栈中name为PageFull1的页面
                    this.pageStack.removeByName('PageFull1');
                  }
                })
              Button('removeByIndexes 0135', { stateEffect: true, type: ButtonType.Capsule })
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    // 删除栈中index为0，1，3，5的页面
                    this.pageStack.removeByIndexes([0, 1, 3, 5]);
                  }
                })
              Button('pop', { stateEffect: true, type: ButtonType.Capsule })
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    this.pageStack.pop();
                  }
                })
              TextInput({ placeholder: 'input your popToIndex ...', controller: this.controller })
                .placeholderColor(Color.Grey)
                .placeholderFont({ size: 14, weight: 400 })
                .caretColor(Color.Blue)
                .width('50%')
                .height(40)
                .margin(20)
                .type(InputType.Number)
                .fontSize(14)
                .fontColor(Color.Black)
                .onChange((value: string) => {
                  this.text = value;
                })
              Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule })
                .width('50%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  if (this.pageStack !== undefined && this.pageStack !== null) {
                    this.pageStack.popToIndex(Number(this.text));
                    this.controller.caretPosition(1);
                  }
                })
            }
            .width('100%')
          }
          .width('100%')
          .height('92%')
        }
      }
      .hideTitleBar(true)
      .onBackPressed(() => {
        hilog.info(0x0000, 'demoTest', 'PageFull1 onBackPressed: ');
        return false;
      })
    }
  }

  log(): boolean {
    hilog.info(0x0000, 'demoTest', 'PageFull1 build called');
    return true;
  }
}
```

```ets
// pages/PagePlaceholder.ets: 占位页
import { MultiNavPathStack } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Component
export struct PagePlaceholder {
  @State message: string = 'PagePlaceholder';
  @Consume('pageStack') pageStack: MultiNavPathStack;
  controller: TextInputController = new TextInputController();
  text: string = '';
  lastBackTime: number = 0;

  build() {
    if (this.log()) {
      NavDestination() {
        Column() {
          Column() {
            Text(this.message)
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
          }
          .width('100%')
          .height('8%')

          Stack({alignContent: Alignment.Center}) {
            Text('Placeholder示例页面')
              .fontSize(80)
              .fontWeight(FontWeight.Bold)
              .fontColor(Color.Red)
          }
          .width('100%')
          .height('92%')
        }
      }.hideTitleBar(true)
    }
  }

  log(): boolean {
    hilog.info(0x0000, 'demoTest', 'PagePlaceholder build called');
    return true;
  }
}
```

分栏效果演示：

主页跳转详情页效果演示：

全屏类型页面效果演示：