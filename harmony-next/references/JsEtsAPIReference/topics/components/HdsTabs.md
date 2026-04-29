# HdsTabs

本模块提供Tabs容器组件的分割线样式，模糊样式和页签侧边栏半屏居中对齐样式的效果。

HdsTabs组件是根视图容器，一般作为Page页面的根容器使用。HdsTabs组件包含了内容区和页签栏，其中内容区默认显示第一个页签内容，开发者可以通过翻页滑动或者点击页签切换内容区。

**起始版本：**6.0.0(20)

#### 导入模块


- HdsTabsAttribute是用于配置HdsTabs组件属性的关键接口。6.0.1(21)及之前版本，导入HdsTabs组件后需要开发者手动导入HdsTabsAttribute，否则会编译报错。从6.0.2(22)版本开始，编译工具链识别到导入HdsTabs组件后，会自动导入HdsTabsAttribute，无需开发者手动导入。

- 如果开发者手动导入HdsTabsAttribute，DevEco Studio会显示置灰，6.0.1(21)及之前版本删除会编译报错，从6.0.2(22)版本开始，删除对功能无影响。

6.0.1(21)及之前版本：

```ets
import { HdsTabs, HdsTabsAttribute, HdsTabsController } from '@kit.UIDesignKit';
```

6.0.2(22)及之后版本：

```ets
import { HdsTabs, HdsTabsController } from '@kit.UIDesignKit';
```

#### 子组件

子组件为[TabContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent)。

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

#### 接口

HdsTabs(options?: HdsTabsOptions)

创建HdsTabs容器。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | HdsTabsOptions | 否 | HdsTabs组件参数。 |

#### HdsTabsOptions

HdsTabs组件参数，继承自[TabsOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#tabsoptions15)。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| controller | HdsTabsController | 否 | 是 | HdsTabs控制器。 默认值：undefined。 |

#### HdsTabsController

HdsTabs组件的控制器，用于控制HdsTabs组件进行页签切换。不支持一个HdsTabsController控制多个HdsTabs组件，继承自[TabsController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#tabscontroller)。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

#### bindScroller

bindScroller(value: number, scroller: Scroller, parentScroller?: Scroller): void

HdsTabs的控制器绑定内容区的滚动组件。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 页签的索引，索引从0开始计算。 |
| scroller | Scroller | 是 | 滚动组件的控制器。 |
| parentScroller | Scroller | 否 | 滚动组件的父控制器。 |

#### unbindScroller

unbindScroller(scroller: Scroller): void

HdsTabs的控制器解除绑定内容区的滚动组件。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scroller | Scroller | 是 | 滚动组件的控制器。 |

**applyMiniBarStyle**

applyMiniBarStyle(style: HdsBarStyle): void

HdsTabs的控制器更新[迷你栏](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating#迷你栏)样式并伴随动效。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | HdsBarStyle | 是 | 迷你栏样式 |

**applyHideAnimation**

applyHideAnimation(mode: HdsAnimationMode): void

HdsTabs的控制器调用页签栏和[迷你栏](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating#迷你栏)的隐藏动效。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | HdsAnimationMode | 是 | 动效模式 |

**applyShowAnimation**

applyShowAnimation(mode: HdsAnimationMode): void

HdsTabs的控制器调用页签栏和[迷你栏](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating#迷你栏)的显示动效。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | HdsAnimationMode | 是 | 动效模式 |

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

#### vertical

vertical(value: boolean)

设置是否为纵向Tab。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否为纵向Tab。 true：纵向Tabs。 false：横向Tabs。 默认值：false。 当横向Tabs设置height为auto时，HdsTabs组件高度自适应子组件高度，即为tabBar高度+divider线宽+TabContent高度+上下padding值+上下border宽度。 当纵向Tabs设置width为auto时，HdsTabs组件宽度自适应子组件宽度，即为tabBar宽度+divider线宽+TabContent宽度+左右padding值+左右border宽度。 尽量保持每一个页面中的子组件尺寸大小一致，避免滑动页面时出现页面切换动画跳动现象。 |

#### barPosition

barPosition(value: BarPosition)

设置Tabs的页签位置。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | BarPosition | 是 | 设置Tabs的页签位置。 默认值：BarPosition.Start。 |

#### scrollable

scrollable(value: boolean)

设置是否可以通过滑动页面进行页面切换。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否可以通过滑动页面进行页面切换。 true：可以通过滑动页面来切换页面。 false：不可通过滑动页面来切换页面。 默认值：true。 |

#### barWidth

barWidth(value: Length)

设置TabBar的宽度值。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | TabBar的宽度值，单位：vp。若设置值小于0或大于Tabs宽度值时，按默认值显示。 默认值： - 未设置SubTabBarStyle和BottomTabBarStyle的TabBar且vertical属性为false时，默认值为Tabs的宽度。 - 未设置SubTabBarStyle和BottomTabBarStyle的TabBar且vertical属性为true时，默认值为56vp。 - 设置SubTabBarStyle样式且vertical属性为false时，默认值为Tabs的宽度。 - 设置SubTabBarStyle样式且vertical属性为true时，默认值为56vp。 - 设置BottomTabBarStyle样式且vertical属性为true时，默认值为96vp。 - 设置BottomTabBarStyle样式且vertical属性为false时，默认值为Tabs的宽度。 |

#### barHeight

barHeight(value: Length)

设置TabBar的高度值。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | TabBar的高度值。单位：vp。设置为'auto'时，TabBar自适应子组件高度，仅在横向Tabs下有效。设置为小于0或大于Tabs高度值时，按默认值显示。 默认值： - 未设置带样式的TabBar且vertical属性为false时，默认值为48vp。 - 未设置带样式的TabBar且vertical属性为true时，默认值为Tabs的高度。 - 设置SubTabBarStyle样式且vertical属性为false时，默认值为48vp。设置SubTabBarStyle样式且vertical属性为true时，默认值为Tabs的高度。 - 设置BottomTabBarStyle样式且vertical属性为true时，默认值为Tabs的高度。 - 设置BottomTabBarStyle样式且vertical属性为false时，默认值为48vp。 |

#### animationDuration

animationDuration(value: number)

设置点击TabBar页签或调用HdsTabsController的changeIndex接口时切换TabContent的动画时长。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 点击TabBar页签或调用TabsController的changeIndex接口切换TabContent的动画时长。 默认值： - 不设置该属性或设置为异常值情况下，若存在BottomTabBarStyle样式的TabBar时，默认值为0。 - 设置所有TabBar为非BottomTabBarStyle样式时，默认值为300。 单位：ms。 取值范围：[0, +∞)。 |

#### barOverlap

barOverlap(value: boolean)

设置TabBar是否背后变模糊并叠加在TabContent之上。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | TabBar是否背后变模糊并叠加在TabContent之上。 true：TabBar背后变模糊并叠加在TabContent之上，并且barBackgroundBlurStyle属性默认模糊材质的BlurStyle值修改为'BlurStyle.COMPONENT_THICK'。 false：无模糊和叠加效果。 默认值：false。 |

#### barBackgroundColor

barBackgroundColor(value: ResourceColor)

设置TabBar的背景颜色。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | TabBar的背景颜色。 默认值：Color.Transparent。 |

#### barBackgroundBlurStyle

barBackgroundBlurStyle(style: BlurStyle, options?: BackgroundBlurStyleOptions)

为TabBar提供一种在背景和内容之间的模糊能力，通过枚举值的方式封装了不同的模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | BlurStyle | 是 | 背景模糊样式。 |
| options | BackgroundBlurStyleOptions | 否 | 背景模糊选项。 |

#### barBackgroundEffect

barBackgroundEffect(options: BackgroundEffectOptions)

设置TabBar背景属性，包含背景模糊半径，亮度，饱和度，颜色等参数。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | BackgroundEffectOptions | 是 | 设置TabBar背景属性包括：模糊半径、亮度、饱和度、颜色等。 |

#### barMode

barMode(value: HdsBarMode, options?: ScrollableBarModeOptions)

设置TabBar的布局模式。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | HdsBarMode | 是 | 所有TabBar都使用实际布局宽度，当设置为BarMode.Scrollable时，若实际布局宽度超过总宽度（横向Tabs的barWidth，纵向Tabs的barHeight），则具有滑动效果；当设置为HALF_SCREEN_FIXED时，所有页签总高度之和为HdsTabs组件高度的四分之一，且处在二分之一屏的居中位置。 说明：当设置为HALF_SCREEN_FIXED样式时： 1. 依赖页签位于侧边栏，vertical设置为true。 2. 依赖页签使用BottomTabBarStyle样式。 |
| options | ScrollableBarModeOptions | 否 | Scrollable模式下的TabBar的布局样式。 说明：仅横向tabs（vertical为false）下有效。 |

#### divider

divider(value: Optional<HdsDividerStyle>)

设置区分TabBar和TabContent的分割线样式。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Optional<HdsDividerStyle> | 是 | 分割线样式，默认跟手渐变。 mode：分割线模式，可以设置为常隐，常显和跟手渐变显隐（当内容区超过页签栏）。 style：分割线的样式。 |


1.依赖页签栏位于容器底部，barPosition设置为BarPosition.End，vertical设置为false。

2.跟手滑动效果仅限支持滚动的通用接口的组件，其他类型组件由开发者自己实现。

3.跟手滑动效果依赖HdsTabs控制器绑定需要设置的list滑动控制器。

#### barBackgroundStyle

barBackgroundStyle(backgroundStyle: Optional<HdsTabsBackgroundStyle>)

设置模糊样式为渐变模糊。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| backgroundStyle | Optional<HdsTabsBackgroundStyle> | 是 | 设置模糊的颜色和高度，默认模糊效果失效。 |


1.依赖页签栏位于容器底部，barPosition设置为BarPosition.End，vertical设置为false。

2.TabBar叠加在TabContent之上，barOverlap设置为true。

3.去掉TabBar节点默认设置的模糊值barBackgroundBlurStyle的值为BlurStyle.NONE。

#### blurStrategy

blurStrategy(value: [BlurStrategy](HdsNavigation.md#section1086755971212))

设置页签栏的模糊生效策略。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BlurStrategy](HdsNavigation.md#section1086755971212) | 是 | 设置页签栏的模糊生效策略。 默认值：BlurStrategy.ADAPTIVE。 |

**cachedMaxCount**

cachedMaxCount(count: number, mode: TabsCacheMode)

设置子组件的最大缓存个数及缓存模式。未设置该属性时默认缓存所有子组件且缓存后不会释放。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 子组件的最大缓存个数。超出范围时自动释放不再需要的子组件。 取值范围：大于等于0。 |
| mode | TabsCacheMode | 是 | 子组件的缓存模式。 默认值：TabsCacheMode.CACHE_BOTH_SIDE |

**barFloatingStyle**

barFloatingStyle(barFloatingStyle?: Optional<HdsTabsFloatingStyle>)

设置页签栏为悬浮样式。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| barFloatingStyle | Optional<HdsTabsFloatingStyle> | 否 | 设置页签为悬浮样式。 |

**HdsTabsFloatingStyle**

设置页签栏的悬浮样式属性。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| barWidth | HdsBarWidthRangeOptions | 否 | 是 | 页签栏分档宽度。 默认值：页签个数小于等于3时，且HdsTabs宽度小于600vp，单个页签宽度76vp，当HdsTabs宽度大于等于600vp时，单个页签宽度80vp。页签个数大于等于4时，页签栏最大宽度不超过328vp。 |
| barSideMargin | Length | 否 | 是 | 页签栏与HdsTabs左右边距。 默认值：HdsTabs宽度小于600vp时，默认边距16vp；HdsTabs宽度在600vp-840vp之间，默认边距24vp，HdsTabs宽度大于840vp，默认边距32vp。 |
| barBottomMargin | Length | 否 | 是 | 页签栏与HdsTabs底部距离。 默认值：页签栏距离底部0vp。 |
| gradientMask | HdsTabsBackgroundStyle | 否 | 是 | 背板蒙层的样式设置，可用来设置背板蒙层的高度和颜色。 默认值：蒙层颜色浅色模式是#66F1F3F5，深色模式是#33000000。蒙层高度等于页签栏默认高度加16vp。 |
| miniBar | HdsTabsMiniBar | 否 | 是 | 迷你栏的属性配置。 默认值：undefined，表示没有迷你栏。 |
| adaptToHandedness | boolean | 否 | 是 | 左右跟手开关。 true：跟手。 false：不跟手。 默认值：false。 |
| lightColor | ResourceColor | 否 | 是 | 页签栏光效颜色。 默认值：深色模式#33E5E5E5，浅色模式#33fffffff。 |
| barOpacity | number | 否 | 是 | 页签栏透明度，1表示不透明，0表示完全透明。 默认值：1。 |
| thermoCtrl | boolean | 否 | 是 | 温控开关。 true：开启温控。 false：不开启温控。 默认值：false。 |
| systemMaterialEffect | SystemMaterialParams | 否 | 是 | 材质参数。 默认值：undefined，没有新材质。 |

**HdsBarWidthRangeOptions**

设置页签栏或[迷你栏](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating#迷你栏)的分档宽度。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| smallWidth | Length | 否 | 是 | 当HdsTabs宽度小于440vp时，页签栏或迷你栏的宽度。 默认值：页签个数小于等于3，且HdsTabs宽度小于600vp时，单个页签宽度76vp。页签个数大于等于4时，页签栏最大宽度不超过328vp。迷你栏最大宽度不超过328vp。 |
| mediumWidth | Length | 否 | 是 | 当HdsTabs宽度在440vp-600vp之间，或宽度在600-840vp之间且高宽比小于0.8时，页签栏或迷你栏的宽度。 默认值：页签个数小于等于3，且HdsTabs宽度小于600vp时，单个页签宽度76vp，HdsTabs宽度大于600vp时，单个页签宽度80vp。页签个数大于等于4时，页签栏最大宽度不超过328vp。迷你栏最大宽度不超过328vp。 |
| largeWidth | Length | 否 | 是 | 当HdsTabs宽度大于840vp，或宽度在600vp-840vp之间且高宽比大于0.8时，页签栏或迷你栏的宽度。 默认值：页签个数小于等于3，单个页签宽度80vp。页签个数大于等于4时，页签栏最大宽度不超过328vp。迷你栏最大宽度不超过328vp。 |

**HdsTabsMiniBar**

设置迷你栏的属性。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| miniBarBuilder | CustomBuilder|ComponentContent | 否 | 否 | 迷你栏自定义内容区。 |
| miniBarWidth | HdsBarWidthRangeOptions | 否 | 是 | 迷你栏展开时，分档宽度。最大宽度不超过328vp。 |
| miniBarStyle | HdsBarStyle | 否 | 是 | 迷你栏的样式，仅HdsTabs宽度小于600vp生效设置。 首次创建迷你栏时，默认是折叠样式，如果HdsTabs宽度大于600vp则为展开样式。 |
| onBarStyleChange | BarStyleChangeCallback | 否 | 是 | 页签栏或迷你栏样式更新回调。 |
| onMiniBarAnimationStart | MiniBarAnimationStartCallback | 否 | 是 | 迷你栏折叠展开动效开始回调。 |
| onMiniBarAnimationEnd | MiniBarAnimationEndCallback | 否 | 是 | 迷你栏折叠展开动效结束回调。 |
| onTabBarAnimationStart | TabBarAnimationStartCallback | 否 | 是 | 页签栏折叠展开动效开始回调。 |
| enableMiniBarBackground | boolean | 否 | 是 | 迷你栏背景。 true：迷你栏跟随页签栏背景。 false：迷你栏背景无色透明。 默认值：true。 |
| enableMiniBarClip | boolean | 否 | 是 | 迷你栏是否裁剪miniBarBuilder内容。 true：裁剪miniBarBuilder内容。 false：不裁剪miniBarBuilder内容。 默认值：true。 |

**SystemMaterialParams**

材质效果参数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| materialType | hdsMaterial.MaterialType | 否 | 是 | 设置材质类型。 默认值：hdsMaterial.MaterialType.NONE。 |
| materialLevel | hdsMaterial.MaterialLevel | 否 | 是 | 设置材质等级。 默认值：hdsMaterial.MaterialLevel.ADAPTIVE。 |

**HdsAnimationMode**

显示隐藏动效模式。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCROLL_ANIMATION | 0 | 滚动动效。 |
| CLICK_ANIMATION | 1 | 点击动效。 |

**HdsBarStyle**

页签栏和[迷你栏](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating#迷你栏)样式类型枚举。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLLAPSE | 0 | 折叠样式。 |
| EXPAND | 1 | 展开样式。 |

**HdsTabsBarChangeMode**

页签栏和[迷你栏](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating#迷你栏)更新模式。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 普通模式。屏幕尺寸更新触发迷你栏和页签栏样式和宽度更新。 |
| USER_CLICK | 1 | 用户点击模式。用户通过点击折叠的迷你栏或页签栏触发样式和宽度更新。 |
| APP_TRIGGER | 2 | 应用触发模式。应用通过控制器触发样式更新。 |

**BarStyleChangeCallback**

BarStyleChangeCallback = (miniBarStyle: HdsBarStyle, tabBarStyle: HdsBarStyle, miniBarWidth: number, tabBarWidth: number, mode: HdsTabsBarChangeMode) => void

[迷你栏](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating#迷你栏)或者页签栏样式更新时触发回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| miniBarStyle | HdsBarStyle | 是 | 迷你栏样式。 |
| tabBarStyle | HdsBarStyle | 是 | 页签栏样式。 |
| miniBarWidth | number | 是 | 迷你栏宽度，单位vp。 |
| tabBarWidth | number | 是 | 页签栏宽度，单位vp。 |
| mode | HdsTabsBarChangeMode | 是 | 样式更新类型。 |

**MiniBarAnimationStartCallback**

MiniBarAnimationStartCallback = (style: HdsBarStyle, width: number) => void

[迷你栏](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating#迷你栏)折叠展开动效开始时回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | HdsBarStyle | 是 | 动效开始时迷你栏的状态。 |
| width | number | 是 | 动效结束时迷你栏的宽度，单位vp。 |

**MiniBarAnimationEndCallback**

MiniBarAnimationEndCallback = (style: HdsBarStyle) => void

[迷你栏](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating#迷你栏)折叠展开动效结束时回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | HdsBarStyle | 是 | 动效结束时迷你栏的状态。 |

**TabBarAnimationStartCallback**

TabBarAnimationStartCallback = (style: HdsBarStyle, width: number) => void

底部页签折叠展开动效开始时回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | HdsBarStyle | 是 | 动效开始时页签栏的状态。 |
| width | number | 是 | 动效结束时页签栏的宽度，单位vp。 |

#### HdsDividerStyle

页签栏分割线配置。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mode | DividerMode | 否 | 否 | 页签栏分割线显示类型。 默认值：DividerMode.FOLLOW_SCROLL。 |
| style | DividerStyle | 否 | 是 | 页签栏分割线样式。 默认值： {strokeWidth: '1px'，color: '#33000000'}。 |

#### HdsTabsBackgroundStyle

渐变模糊样式。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maskColor | ResourceColor | 否 | 是 | 渐变模糊的颜色设置。 默认值：#CCFFFFFF。 |
| maskHeight | number | 否 | 是 | 渐变模糊的高度设置。 默认值：组件高度（包含底部TabBar高度）+32vp。 |

#### 事件

#### onChange

onChange(event: Callback<number>)

底部页签切换时触发该事件。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<number> | 是 | 底部页签切换时触发该事件，获取切换后的页签下标。 |

#### onAnimationStart

onAnimationStart(handler: OnTabsAnimationStartCallback)

切换动画开始时触发该回调。当[animationDuration](#ZH-CN_TOPIC_0000002553201279__animationduration)为0时动画关闭，不触发该回调。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | OnTabsAnimationStartCallback | 是 | 切换的动画开始时触发该事件。 |

#### onContentWillChange

onContentWillChange(handler: OnTabsContentWillChangeCallback)

自定义Tabs页面切换拦截事件能力，新页面即将显示时触发该回调。

满足以下任一条件，即可触发该事件：

1、滑动TabContent切换新页面时触发。

2、通过TabsController.changeIndex接口切换新页面时触发。

3、通过动态修改index属性值切换新页面时触发。

4、通过点击TabBar页签切换新页面时触发。

5、TabBar页签获焦后，通过键盘左右方向键等切换新页面时触发。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | OnTabsContentWillChangeCallback | 是 | 自定义Tabs页面切换拦截事件能力。 |

#### onTabBarClick

onTabBarClick(event: Callback<number>)

Tab页签点击后触发的事件。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<number> | 是 | 被点击的index索引，索引从0开始计算。 |

**onSelected**

onSelected(event: Callback<number>)

底部页签切换时触发该事件。

满足以下任一条件，即可触发该事件：

1. 滑动离手时满足翻页阈值，开始切换动画时触发。

1. 通过[TabsController控制器](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#tabscontroller)调用[changeIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#changeindex)接口，开始切换动画时触发。

1. 动态修改[状态变量](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)构造的index属性值后触发。

1. 通过页签处点击触发。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<number> | 是 | 当前选中元素的索引。 |

**onUnselected**

onUnselected(event: Callback<number>)

当选中元素改变时触发该回调，返回值为将要隐藏的元素的索引值。

满足以下任一条件，即可触发该事件：

1. 滑动离手时满足翻页阈值，开始切换动画时触发。

1. 通过[TabsController控制器](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#tabscontroller)调用[changeIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#changeindex)接口，开始切换动画时触发。

1. 动态修改[状态变量](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)构造的index属性值后触发。

1. 通过页签处点击触发。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<number> | 是 | 将要隐藏元素的索引。 |

#### ExtendBarMode

页签栏布局模式枚举。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HALF_SCREEN_FIXED | 100 | 页签栏布局模式：半屏居中布局。 |

#### DividerMode

页签栏分割线显示类型枚举。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VISIBLE | 0 | 页签栏分割线显示类型：常显。 |
| NONE | 1 | 页签栏分割线显示类型：常隐。 |
| FOLLOW_SCROLL | 2 | 页签栏分割线显示类型：跟手渐变。 |

#### HdsBarMode

type HdsBarMode= ExtendBarMode | BarMode

HdsBarMode页签栏的布局模式和扩展模式设置。

模型约束： 此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSComponent.Core

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

| 类型 | 说明 |
| --- | --- |
| ExtendBarMode | TabBar扩展的布局模式。 |
| BarMode | TabBar布局模式。 |

#### bleedIconStyle

bleedIconStyle(builder: CustomTabBuilder): void

在TabsContent组件上设置自定义的出血图标。

**装饰器类型：**@Builder

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | CustomTabBuilder | 是 | 设置自定义组件出血效果。 |

#### CustomTabBuilder

type CustomTabBuilder= () => void

自定义组件。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.UIDesign.HDSPattern.Standard

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

**起始版本：**6.0.0(20)

**HdsTabsModifier**

动态设置HdsTabs组件的属性和样式，继承自[HdsTabsAttribute](#ZH-CN_TOPIC_0000002553201279__属性)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

**applyNormalAttribute**

applyNormalAttribute?(instance: HdsTabsAttribute): void

组件普通状态时的样式。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.UIDesign.HDSComponent.Core

设备行为差异： 该接口在TV无效果，在其他设备类型中可正常调用。

起始版本： 6.1.0(23)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | HdsTabsAttribute | 是 | 动态设置HdsTabs组件的属性。 |

#### 示例

#### 支持分割线出现和消失

通过设置分割线属性中的类型 ，控制分割线的常显、常隐、跟手效果。

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

```ets
// 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
import {
  HdsTabs,
  HdsTabsAttribute,
  HdsTabsController,
  DividerMode } from '@kit.UIDesignKit';

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
```

**表1 **效果

   ![image](public_sys-resources/zh-cn_image_0000002553205745.webp)![image](public_sys-resources/zh-cn_image_0000002522085792.webp)![image](public_sys-resources/zh-cn_image_0000002553365705.webp)
| 常显 | 常隐 | 跟手 |
| --- | --- | --- |

#### 支持渐变模糊

通过设置HdsTabs组件的barBackgroundStyle样式，可以自定义模糊的颜色和高度，实现渐变模糊。

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

```ets
// 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
import { HdsTabs, HdsTabsAttribute, HdsTabsController } from '@kit.UIDesignKit';

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
```

效果：

#### 支持出血效果

通过设置HdsTabs组件TabContent的tabBar样式，可以实现出血效果。

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

```ets
// 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
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
  @Builder
  tabBuilder() {
    Column() {
      Image($r('app.media.startIcon'))
        .width(48)
        .height(48)
        .borderRadius(24)
    }
```

效果：

#### 页签半屏居中对齐布局

通过设置HdsTabs组件的barMode样式为ExtendBarMode.HALF_SCREEN_FIXED，页签高度是Tabs高度的四分之一均分，并且半屏居中对齐。

**设备行为差异：**该接口在TV无效果，在其他设备类型中可正常调用。

```ets
// 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
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
```

效果：