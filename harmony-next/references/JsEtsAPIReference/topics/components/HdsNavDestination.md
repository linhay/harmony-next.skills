# HdsNavDestination

作为子页面的根容器，用于显示[HdsNavigation](HdsNavigation.md)的内容区，默认支持标题栏随内容区滚动的动态模糊样式。6.0.0(20)版本以后，推荐使用[bindToScrollable](#ZH-CN_TOPIC_0000002522241308__bindtoscrollable)、[bindToNestedScrollable](#ZH-CN_TOPIC_0000002522241308__bindtonestedscrollable)属性绑定导航组件和可滚动容器组件后，再使用导航组件滚动相关的功能，从而获得更优的体验。如滚动生效动态模糊样式，标题栏随内容区滚动动态显隐功能等。

起始版本： 5.1.0(18)

**导入模块**

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

- HdsNavDestinationAttribute是用于配置HdsNavDestination组件属性的关键接口。6.0.1(21)及之前版本，导入HdsNavDestination组件后需要开发者手动导入HdsNavDestinationAttribute，否则会编译报错。从6.0.2(22)版本开始，编译工具链识别到导入HdsNavDestination组件后，会自动导入HdsNavDestinationAttribute，无需开发者手动导入。

- 如果开发者手动导入HdsNavDestinationAttribute，DevEco Studio会显示置灰，6.0.1(21)及之前版本删除会编译报错，从6.0.2(22)版本开始，删除对功能无影响。

6.0.1(21)及之前版本：

```ets
import { HdsNavDestination, HdsNavDestinationAttribute } from '@kit.UIDesignKit';
```

6.0.2(22)及之后版本：

```ets
import { HdsNavDestination } from '@kit.UIDesignKit';
```

**子组件**

-

子组件类型：系统组件和自定义组件，支持渲染控制类型（[if/else](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse)、[ForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)和[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)）。

-

子组件个数：多个。

**接口**

HdsNavDestination()

创建[HdsNavigation](HdsNavigation.md)子页面的根容器。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

**属性**

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)。

不推荐设置位置、大小等布局相关属性，可能会造成页面显示异常。

**titleBar**

titleBar(options?: HdsNavigationTitleBarOptions)

设置HdsNavDestination组件titleBar区域（包括返回图标区域、标题区域、菜单区域、背景板）样式以及内容。

标题字符串超长时，如果不设置副标题，先缩小再换行（2行）最后以"..."截断。如果设置副标题，先缩小后以"..."截断。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | HdsNavigationTitleBarOptions | 否 | 标题栏配置信息。 |

**hideTitleBar**

hideTitleBar(hide: boolean, animated?: boolean)

设置是否隐藏标题栏，并且可设置在标题栏显示隐藏的状态变化中是否使用动画。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | boolean | 是 | 是否隐藏标题栏。 默认值：false。 true：隐藏标题栏。 false：显示标题栏。 |
| animated | boolean | 否 | 设置是否使用动画显隐标题栏。 默认值：false。 true：使用动画显示隐藏标题栏。 false：不使用动画显示隐藏标题栏。 |

**hideBackButton**

hideBackButton(value: boolean)

设置是否隐藏标题栏中的返回键。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否隐藏标题栏中的返回键。 默认值：false。 true：隐藏返回键。 false：显示返回键。 |

**mode**

mode(value: NavDestinationMode)

设置HdsNavDestination类型，不支持动态修改。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | NavDestinationMode | 是 | HdsNavDestination类型。 默认值：NavDestinationMode.STANDARD。 |

**toolbarConfiguration**

toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)

设置工具栏内容。未调用本接口时不显示工具栏。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| toolbarParam | Array<ToolbarItem> | CustomBuilder | 是 | 工具栏内容。 使用Array<ToolbarItem>写法设置的工具栏有如下特性： - 工具栏所有选项均分底部工具栏，在每个均分内容区布局文本和图标。 - 文本超长时，若工具栏选项个数小于5个，优先拓展选项的宽度，工具栏最大宽度与屏幕等宽，其次逐级缩小，缩小之后换行，最后截断。 - 竖屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标中，点击更多图标，可以展示剩余内容。横屏时，如果为Split模式，仍按照竖屏规则显示，如果为Stack模式，不支持合并工具栏到菜单栏。 使用CustomBuilder写法为用户自定义工具栏选项，仅支持均分底部工具栏。 |
| options | NavigationToolbarOptions | 否 | 工具栏选项。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

不支持通过SymbolGlyphModifier对象的fontSize属性修改图标大小、effectStrategy属性修改动效、symbolEffect属性修改动效类型。

**hideToolBar**

hideToolBar(hide: boolean, animated?: boolean)

设置是否隐藏工具栏，并且可设置在工具栏显示隐藏的状态变化中是否使用动画。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hide | boolean | 是 | 是否隐藏工具栏。 默认值：false。 true：隐藏工具栏。 false：显示工具栏。 |
| animated | boolean | 否 | 设置是否使用动画显隐工具栏。 默认值：false。 true：使用动画显示隐藏工具栏。 false：不使用动画显示隐藏工具栏。 |

**ignoreLayoutSafeArea**

ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>)

控制组件的布局，使其扩展到非安全区域。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | Array <LayoutSafeAreaType> | 否 | 配置扩展安全区域的类型。 默认值：[LayoutSafeAreaType.SYSTEM]。 |
| edges | Array <LayoutSafeAreaEdge> | 否 | 配置扩展安全区域的方向。 默认值：[LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM]。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

组件设置LayoutSafeArea之后生效的条件为：

设置LayoutSafeAreaType.SYSTEM时，组件的边界与非安全区域重合时组件能够延伸到非安全区域下。

例如：设备顶部状态栏高度100，组件在屏幕中纵向方位的绝对偏移需要在0到100之间。

若组件延伸到非安全区域内，此时在非安全区域里触发的事件（例如：点击事件）等可能会被系统拦截，优先响应状态栏等系统组件。

**systemBarStyle**

systemBarStyle(originalStyle: Optional<SystemBarStyle>, scrollEffectStyle: Optional<SystemBarStyle>)

当HdsNavigation中显示当前HdsNavDestination时，设置对应系统状态栏的样式。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| originalStyle | Optional<SystemBarStyle> | 是 | 系统状态栏初始样式。未设置systemBarStyle属性时，颜色默认值同主标题栏字体颜色。 |
| scrollEffectStyle | Optional<SystemBarStyle> | 是 | HdsNavDestination动态样式生效后，系统状态栏对应的最终动态样式。未设置systemBarStyle属性时，颜色默认值同主标题栏字体颜色。 |

说明：

1.

必须配合HdsNavigation使用，作为其HdsNavigation目的页面的根节点时才能生效。

1.

其他使用限制请参考HdsNavigation对应的[systemBarStyle](HdsNavigation.md#ZH-CN_TOPIC_0000002553361235__systembarstyle)属性说明。

**recoverable**

recoverable(recoverable: Optional<boolean>)

配置HdsNavDestination是否可恢复。如配置为可恢复，当应用进程异常退出并重新冷启动时，可自动创建该HdsNavDestination。该功能需HdsNavDestination对应的HdsNavigation也配置了可恢复属性使用。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| recoverable | Optional<boolean> | 是 | HdsNavDestination是否可恢复，默认为不可恢复。 默认值：false。 true：页面栈可恢复。 false：页面栈不可恢复。 |

**dynamicHideTitleBar**

dynamicHideTitleBar(value: DynamicHideParams)

设置标题栏跟随内容区动态显隐配置，推荐搭配[bindToScrollable](HdsNavigation.md#ZH-CN_TOPIC_0000002553361235__bindtoscrollable)/[bindToNestedScrollable](HdsNavigation.md#ZH-CN_TOPIC_0000002553361235__bindtonestedscrollable)体验更佳的滑动效果。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | DynamicHideParams | 是 | 标题栏跟随内容区滚动动态显隐配置。 当配置了标题栏动态显隐时，不支持配置标题栏模式动态切换。 当标题栏模式为HdsNavDestinationTitleMode.MODAL时该接口设置无效。 不支持在显隐过程中动态切换属性。 |

**bindToScrollable**

bindToScrollable(scrollers: Array<Scroller>)

绑定导航组件和可滚动容器组件，动态显隐标题区域，状态栏及底部自定义区域，使能动态显隐更优体验。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollers | Array<Scroller> | 是 | 可滚动容器组件的控制器。 |

**bindToNestedScrollable**

bindToNestedScrollable(scrollers: Array<NestedScrollInfo>)

绑定导航组件和嵌套的可滚动容器组件，动态显隐标题区域，状态栏及底部自定义区域，使能动态显隐更优体验。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollers | Array<NestedScrollInfo> | 是 | 嵌套的可滚动容器组件的控制器。 |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

当多个可滚动容器组件绑定了同一个导航组件时，滚动任何一个容器都会触发标题栏显示或隐藏效果。且当任何一个可滚动容器组件滑动到底部或顶部位置时，会立即触发标题栏显示动效。

因此，为了获得最佳用户体验，不建议同时触发多个可滚动容器组件的滚动事件。

**systemTransition**

systemTransition(type: NavigationSystemTransitionType)

设置HdsNavDestination系统转场动画，支持分别设置系统标题栏动画和内容动画。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | NavigationSystemTransitionType | 是 | 系统转场动画类型。 默认值：NavigationSystemTransitionType.DEFAULT。 |

**customTransition**

customTransition(delegate: NavDestinationTransitionDelegate)

设置HdsNavDestination自定义转场动画。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate | NavDestinationTransitionDelegate | 是 | HdsNavDestination自定义动画的代理函数。 |

**titleMode**

titleMode(value: HdsNavDestinationTitleMode)

设置页面标题栏显示模式。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | HdsNavDestinationTitleMode | 是 | 页面标题栏显示模式。默认值：HdsNavDestinationTitleMode.MINI。 |

**withTheme**

设置HdsNavDestination的[WithTheme](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-theme)能力。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.1.0(23)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | WithThemeOptions | 是 | WithTheme能力配置信息。 |

**事件**

**onShown**

onShown(callback: Callback<void>)

当显示HdsNavDestination页面时，触发onShown回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 当该HdsNavDestination页面显示时触发的回调。 |

**onShown**

onShown(callback: Callback<VisibilityChangeReason>)

当显示HdsNavDestination页面时，触发onShown回调。通过[VisibilityChangeReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#visibilitychangereason21)说明触发的原因。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.1.0(23)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<VisibilityChangeReason> | 是 | 当该HdsNavDestination页面显示时触发的回调。回调会提供入参VisibilityChangeReason以说明onShown触发的原因。 |

**onHidden**

onHidden(callback: Callback<void>)

当隐藏HdsNavDestination页面时，触发onHidden回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 当该HdsNavDestination页面隐藏时触发的回调。 |

**onHidden**

onHidden(callback: Callback<VisibilityChangeReason>)

当隐藏HdsNavDestination页面时, 触发onHidden回调。通过[VisibilityChangeReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#visibilitychangereason21)说明触发的原因。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.1.0(23)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<VisibilityChangeReason> | 是 | 当该HdsNavDestination页面隐藏时触发的回调。回调会提供入参VisibilityChangeReason以说明onHidden触发的原因。 |

**onReady**

onReady(callback: Callback<NavDestinationContext>)

当HdsNavDestination即将构建子组件之前会触发此回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<NavDestinationContext> | 是 | 当该HdsNavDestination即将构建子组件之前会触发的回调。 |

**onWillAppear**

onWillAppear(callback: Callback<void>)

当该HdsNavDestination挂载之前触发此回调。在该回调中允许修改页面栈，当前帧生效。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 当该HdsNavDestination挂载之前触发的回调。 |

**onWillDisappear**

onWillDisappear(callback: Callback<void>)

当该HdsNavDestination卸载之前触发的生命周期（有转场动画时，在转场动画开始之前触发）。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 当该HdsNavDestination卸载之前触发的生命周期（有转场动画时，在转场动画开始之前触发）。 |

**onWillShow**

onWillShow(callback: Callback<void>)

当该HdsNavDestination显示之前触发此回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 当该HdsNavDestination显示之前触发的回调。 |

**onWillHide**

onWillHide(callback: Callback<void>)

当该HdsNavDestination隐藏之前触发此回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 5.1.0(18)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 当该HdsNavDestination隐藏之前触发的回调。 |

**onBackPressed**

onBackPressed(callback: Callback<void, boolean>)

当与HdsNavigation绑定的页面栈中存在内容时，此回调生效。当点击返回键时，触发该回调。

返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。不推荐同时设置返回键自定义事件与onBackPressed回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.0.0(20)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void, boolean> | 是 | 当与HdsNavigation绑定的页面栈中存在内容时，并且点击返回键时，触发的回调。 |

**onActive**

onActive(callback: Optional<Callback<NavDestinationActiveReason>>)

HdsNavDestination处于激活态（处于栈顶可操作，且上层无特殊组件遮挡）时，触发该回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.0.1(21)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Optional<Callback<NavDestinationActiveReason>> | 是 | HdsNavDestination由非激活态变为激活态的原因。 |

**onInactive**

onInactive(callback: Optional<Callback<NavDestinationActiveReason>>)

HdsNavDestination处于非激活态（处于非栈顶不可操作，或处于栈顶时上层有特殊组件遮挡）时，触发该回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.0.1(21)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Optional<Callback<NavDestinationActiveReason>> | 是 | HdsNavDestination由激活态变为非激活态的原因。 |

**HdsNavDestinationTitleMode**

标题栏显示模式枚举。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

起始版本： 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MINI | 100 | 固定为小标题模式。标题栏高度为56vp。 |
| MODAL | 101 | 固定为半模态模式。背板高度64vp，标题栏高度为56vp，上padding为8vp。 |

**示例**

通过titleBar属性，自定义设置标题栏随内容区滚动的动态模糊样式。

```ets
// 从6.0.2(22)版本开始，无需手动导入HdsNavDestinationAttribute。具体请参考HdsNavDestination的导入模块说明。
import { HdsNavDestination, HdsNavDestinationAttribute, ScrollEffectType } from '@kit.UIDesignKit';
import { LengthMetrics } from '@kit.ArkUI';

const  TITLE_BAR_HEIGHT_MINI: number = 56;

@Entry
@Component
struct PageOne {
  scroller: Scroller = new Scroller()

  build() {
    HdsNavDestination() {
      Scroll(this.scroller) {
        Column() {
          Blank().height(TITLE_BAR_HEIGHT_MINI)
          Image($r('app.media.scenery')).width('100%') // scenery为自定义资源，开发者需替换本地资源
        }
      }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
    }
    .titleBar({
      padding: {
        start: LengthMetrics.vp(2),
        end: LengthMetrics.vp(2)
      },
      style: {
        scrollEffectOpts: {
          enableScrollEffect: true,
          scrollEffectType: ScrollEffectType.COMMON_BLUR,
          blurEffectiveStartOffset: LengthMetrics.vp(0),
          blurEffectiveEndOffset: LengthMetrics.vp(20)
        },
        originalStyle: {
          backgroundStyle: {
            backgroundColor: $r('sys.color.ohos_id_color_background'),
          },
          contentStyle: {
            titleStyle: { mainTitleColor: $r('sys.color.font_primary'), subTitleColor: $r('sys.color.font_secondary') },
            menuStyle: { backgroundColor: $r('sys.color.comp_background_tertiary'), iconColor: $r('sys.color.icon_primary') },
            backIconStyle: { backgroundColor: $r('sys.color.comp_background_tertiary'), iconColor: $r('sys.color.icon_primary') }
          }
        },
        scrollEffectStyle: {
          backgroundStyle: {
            backgroundColor: $r('sys.color.ohos_id_color_background_transparent'),
          },
          contentStyle: {
            titleStyle: { mainTitleColor: $r('sys.color.font_primary'), subTitleColor: $r('sys.color.font_secondary') },
            menuStyle: { backgroundColor: $r('sys.color.comp_background_tertiary'), iconColor: $r('sys.color.icon_primary') },
            backIconStyle: { backgroundColor: $r('sys.color.comp_background_tertiary'), iconColor: $r('sys.color.icon_primary') }
          }
      },
      content: {
        title: {
          mainTitle: "PageOne",
        },
        menu: {
          value: [{
            content: {
              label: 'menu1',
              icon: 'resources/base/media/startIcon.png',
              isEnabled: true,
              action: () => {
                console.info("HdsNavDestination menu1");
              }
          }, {
            content: {
              label: 'menu2',
              icon: 'resources/base/media/startIcon.png',
              isEnabled: true,
              action: () => {
                console.info("HdsNavDestination menu2");
              }
          }]
        },
      }
    })
    .systemBarStyle({ statusBarContentColor: '#0A59F7' }, { statusBarContentColor: '#C7C7CD' })
    .hideBackButton(false)
  }
```

![image](public_sys-resources/zh-cn_image_0000002522245778.webp)

HdsNavDestination更多示例可以参考HdsNavigation[示例代码](HdsNavigation.md#ZH-CN_TOPIC_0000002553361235__示例)。