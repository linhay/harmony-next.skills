# AtomicServiceNavigation

作为Page页面的根容器使用，其内部默认包含了标题栏、内容区，其中内容区默认首页显示导航内容或非首页显示（[NavDestination](../misc/NavDestination.md)的子组件），首页和非首页通过路由进行切换。

该组件从API Version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 导入模块

```ets
import { AtomicServiceNavigation } from '@kit.ArkUI';
```

#### 子组件

可以包含子组件。

从API Version 10开始，推荐使用[NavPathStack](../misc/Navigation.md#ZH-CN_TOPIC_0000002497444902__navpathstack10)进行页面路由。

#### AtomicServiceNavigation

```ets
AtomicServiceNavigation({
    navPathStack?: NavPathStack,
    navigationContent: Callback<void>,
    title?: ResourceStr,
    titleOptions?: TitleOptions,
    gradientBackground?: GradientBackground,
    hideTitleBar?: boolean,
    navBarWidth?: Length,
    mode?: NavigationMode,
    navDestinationBuilder?: NavDestinationBuilder,
    navBarWidthRange?: [Dimension, Dimension],
    minContentWidth?: Dimension,
    sideBarOptions?: sideBarOptions,
    sideBarContent?: Callback<void>,
    menus?:	CustomBuilder | Array<NavigationMenuItem>,
    stateChangeCallback?: Callback<boolean>,
    modeChangeCallback?: Callback<NavigationMode>
})
```

**装饰器类型：** @Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**：

名称类型必填装饰器类型说明navPathStack[NavPathStack](../misc/Navigation.md#ZH-CN_TOPIC_0000002497444902__navpathstack10)否@State

路由栈信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

navigationContentCallback<void>否@BuilderParam

Navigation容器内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

title[ResourceStr](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否@Prop

设置页面标题。默认值为空字符串。当titleOptions的titleBarType字段设置为[TitleBarType](#ZH-CN_TOPIC_0000002497604942__titlebartype18).ROUND_ICON或者[TitleBarType](#ZH-CN_TOPIC_0000002497604942__titlebartype18).SQUARED_ICON，且设置了titleIcon时，title标题内容将不会显示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

titleOptions[TitleOptions](#ZH-CN_TOPIC_0000002497604942__titleoptions)否@Prop

标题栏选项。当titleBarType字段设置为[TitleBarType](#ZH-CN_TOPIC_0000002497604942__titlebartype18).ROUND_ICON或者[TitleBarType](#ZH-CN_TOPIC_0000002497604942__titlebartype18).SQUARED_ICON，且设置了titleIcon时，title标题内容将不会显示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

gradientBackground18+[GradientBackground](#ZH-CN_TOPIC_0000002497604942__gradientbackground18)否@Prop

背景色选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

hideTitleBarboolean否@Prop

设置是否隐藏标题栏。默认为false。

false表示显示标题栏，true表示隐藏标题栏。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

navBarWidth[Length](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__length)否@Prop

设置导航栏宽度。默认值为240vp。

仅在Navigation组件分栏时生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

mode[NavigationMode](../misc/Navigation.md#ZH-CN_TOPIC_0000002497444902__navigationmode9枚举说明)否@Prop

设置导航栏的显示模式。

支持Stack、Split与Auto模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

navDestinationBuilder[NavDestinationBuilder](#ZH-CN_TOPIC_0000002497604942__navdestinationbuilder)否@BuilderParam

创建[NavDestination](../misc/NavDestination.md)组件所需要的Builder数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

navBarWidthRange[[Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10), [Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)]否@Prop

设置导航栏最小和最大宽度（双栏模式下生效）。默认值：最小默认值为240vp，最大默认值为组件宽度的40%，且不大于432vp，如果只设置一个值，则未设置的值按照默认值计算。单位：vp。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

minContentWidth[Dimension](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__dimension10)否@Prop

设置导航栏内容区最小宽度（双栏模式下生效）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

sideBarOptions18+[SideBarOptions](#ZH-CN_TOPIC_0000002497604942__sidebaroptions18)否@Prop

侧边栏的功能选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

sideBarContent18+Callback<void>否@BuilderParam

侧边栏的内容。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

menus18+[CustomBuilder](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__custombuilder8) | Array<[NavigationMenuItem](../misc/Navigation.md#ZH-CN_TOPIC_0000002497444902__navigationmenuitem)>否@BuilderParam

宽屏场景下用户自定义插入的布局样式。默认为空，不显示任何样式。屏幕宽度低于600vp为非宽屏场景，大于等于600vp为宽屏场景。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

stateChangeCallbackCallback<boolean>否-

导航栏显示状态切换时触发该回调。true表示导航栏显示状态发生了切换。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

modeChangeCallbackCallback<[NavigationMode](../misc/Navigation.md#ZH-CN_TOPIC_0000002497444902__navigationmode9枚举说明)>否-

当Navigation首次显示或者单双栏状态发生变化时触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### TitleOptions

标题栏选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明backgroundColor[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是

标题栏背景颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

isBlurEnabledboolean否是

标题栏是否模糊，默认值：true，表示标题栏模糊。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

barStyle[BarStyle](../misc/Navigation.md#ZH-CN_TOPIC_0000002497444902__barstyle12枚举说明)否是

标题栏样式属性设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

titleBarType18+[TitleBarType](#ZH-CN_TOPIC_0000002497604942__titlebartype18)否是

设置标题栏类型。默认值为TitleBarType.ROUND_ICON。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

titleIcon18+[Resource](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | [SymbolGlyphModifier](../misc/动态属性设置.md)否是

设置标题栏的图标。默认值为$r('sys.color.ohos_id_color_titlebar_icon')。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

#### GradientBackground18+

供开发者设置品牌渐变色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明primaryColor[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否否单色渐变色彩值和双色渐变第一色彩值。无默认值。secondaryColor[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是双色渐变色第二色彩值。无默认值。backgroundTheme[BackgroundTheme](#ZH-CN_TOPIC_0000002497604942__backgroundtheme18)否是导航栏背景底色。默认值为DEFAULT。mixMode[MixMode](#ZH-CN_TOPIC_0000002497604942__mixmode18)否是同时设置primaryColor和secondaryColor时此参数生效。代表双色渐变下两种颜色的融合方式。默认值为TOWARDS。alpha[GradientAlpha](#ZH-CN_TOPIC_0000002497604942__gradientalpha18)否是设置渐变色显示区域的透明度。默认值为OPACITY_20。

#### NavDestinationBuilder

type NavDestinationBuilder = (name: string, param?: Object) => void

NavDestination组件内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明namestring是[NavDestination](../misc/NavDestination.md)页面名称。paramObject否[NavDestination](../misc/NavDestination.md)页面详细参数。

#### MixMode18+

背景色颜色混合模式的可选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明AVERAGE1两种颜色各占一半。CROSS2一种颜色从另一种颜色中穿过。TOWARDS3一种颜色渐变为另一种颜色。

#### TitleBarType18+

标题栏类型的可选项，默认值为ROUND_ICON。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明SQUARED_ICON1方形图标样式。ROUND_ICON2圆形图标样式。DRAWER3抽屉样式。

#### GradientAlpha18+

导航栏背景底色的可选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明OPACITY_201不透明度为0.2。OPACITY_602不透明度为0.6。OPACITY_803不透明度为0.8。OPACITY_1004不透明度为1.0。

#### BackgroundTheme18+

导航栏背景色底色的可选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明DARK1背景底色为黑色。LIGHT2背景底色为白色。DEFAULT3背景底色为灰白色。颜色值#F1F3F5 。

#### SideBarOptions18+

侧边栏的功能选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明sideBarBackground[ResourceColor](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcecolor)否是设置侧边栏的背景颜色。默认为$r('sys.color.ohos_id_color_sub_background')。onChangeCallback<boolean>否是侧边栏显示隐藏回调。true表示显示，false表示隐藏。sideBarIcon[Resource](../misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resource) | [SymbolGlyphModifier](../misc/动态属性设置.md)否是侧边栏里的返回图标。默认值为$r('sys.symbol.open_sidebar')。

#### 示例

#### 示例1（AtomicServiceNavigation页面布局与渐变色背景）

AtomicServiceNavigation的基础样式，并展示渐变色背景。

```ets
import { AtomicServiceNavigation, MixMode, GradientAlpha, BackgroundTheme } from '@kit.ArkUI';
import { AtomicServiceTabs, TabBarOptions, TabBarPosition } from '@kit.ArkUI';
@Entry
@Component
struct Index {
  @State message: string = '主题';
  childNavStack: NavPathStack = new NavPathStack();
  @Builder
  tabContent1() {
    Text('first page')
      .onClick(() => {
        this.childNavStack.pushPath({ name: 'page one' })
      })
  }

  @Builder
  tabContent2() {
    Text('second page')
  }

  @Builder
  tabContent3() {
    Text('third page')
  }

  @Builder
  navigationContent() {
    AtomicServiceTabs({
      tabContents: [
        () => {
          this.tabContent1()
        },
        () => {
          this.tabContent2()
        },
        () => {
          this.tabContent3()
        }
      ],
      tabBarOptionsArray: [
        new TabBarOptions($r('sys.media.ohos_ic_public_phone'), '功能1'),
        new TabBarOptions($r('sys.media.ohos_ic_public_location'), '功能2', Color.Green, Color.Red),
        new TabBarOptions($r('sys.media.ohos_ic_public_more'), '功能3')
      ],
      tabBarPosition: TabBarPosition.BOTTOM,
      barBackgroundColor: $r('sys.color.ohos_id_color_bottom_tab_bg'),
      onTabBarClick: (index: Number) => {
        if (index == 0) {
          this.message = '功能1';
        } else if (index == 1) {
          this.message = '功能2';
        } else {
          this.message = '功能3';
        }
      }
    })
  }

  @Builder
  pageMap(name: string) {
    if (name === 'page one') {
      PageOne()
    } else if (name === 'page two') {
      PageTwo()
    }
  }

  build() {
    Row() {
      Column() {
        AtomicServiceNavigation({
          navigationContent: () => {
            this.navigationContent()
          },
          title: this.message,
          titleOptions: {
            isBlurEnabled: false
          },
          gradientBackground: {
            primaryColor: '#FF0000',
            secondaryColor: '#00FF00',
            backgroundTheme: BackgroundTheme.LIGHT,
            mixMode: MixMode.AVERAGE,
            alpha: GradientAlpha.OPACITY_100
          },
          navDestinationBuilder: this.pageMap,
          navPathStack: this.childNavStack,
          mode: NavigationMode.Stack
        })
      }
      .width('100%')
    }
    .height('100%')
  }
}

@Component
export struct PageOne {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Button('Next')
        .onClick(() => {
          this.pageInfo.pushPath({ name: 'page two'})
        })
    }
    .title('PageOne')
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
  }
}

@Component
export struct PageTwo {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Button('End')
    }
    .title('PageTwo')
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
  }
}
```

#### 示例2（抽屉模式，宽屏场景下插入自定义布局）

设备宽屏场景（宽度大于600vp）下设置抽屉模式，用户在标题栏插入自定义布局。

```ets
import { AtomicServiceNavigation, TitleBarType } from '@kit.ArkUI';
import { AtomicServiceTabs, TabBarOptions, TabBarPosition } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  childNavStack: NavPathStack = new NavPathStack();

  @Builder
  tabContent1() {
    Text('first page')
      .onClick(() => {
        this.childNavStack.pushPath({ name: 'page one' })
      })
  }

  @Builder
  tabContent2() {
    Text('second page')
  }

  @Builder
  tabContent3() {
    Text('third page')
  }

  @Builder
  navigationContent() {
    AtomicServiceTabs({
      tabContents: [
        () => {
          this.tabContent1()
        },
        () => {
          this.tabContent2()
        },
        () => {
          this.tabContent3()
        }
      ],
      tabBarOptionsArray: [
        new TabBarOptions($r('sys.media.ohos_ic_public_phone'), '功能1'),
        new TabBarOptions($r('sys.media.ohos_ic_public_location'), '功能2', Color.Green, Color.Red),
        new TabBarOptions($r('sys.media.ohos_ic_public_more'), '功能3')
      ],
      tabBarPosition: TabBarPosition.BOTTOM,
      barBackgroundColor: $r('sys.color.ohos_id_color_bottom_tab_bg'),
      onTabBarClick: (index: Number) => {
        if (index == 0) {
          this.message = '功能1';
        } else if (index == 1) {
          this.message = '功能2';
        } else {
          this.message = '功能3';
        }
      }
    })
  }

  @Builder
  pageMap(name: string) {
    if (name === 'page one') {
      PageOne()
    } else if (name === 'page two') {
      PageTwo()
    }
  }

  @State showText: string = 'time: ';
  @State time: number = 0;

  @Builder
  insertComp() {
    Text('This is menus area')
      .fontColor(Color.Red)
      .width(200)
      .height('100%')
  }

  build() {
    Column() {
      AtomicServiceNavigation({
        navigationContent: () => {
          this.navigationContent()
        },
        navDestinationBuilder: this.pageMap,
        navPathStack: this.childNavStack,
        title: this.message,
        titleOptions: {
          titleIcon: $r('app.media.startIcon'),
          backgroundColor: 'rgb(61, 157, 180)',
          titleBarType: TitleBarType.DRAWER
        },
        menus: () => { this.insertComp() },
        mode: NavigationMode.Stack
      })
    }
    .width('100%')
  }
}

@Component
export struct PageOne {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Button('Next')
        .onClick(() => {
          this.pageInfo.pushPath({ name: 'page two'})
        })
    }
    .title('PageOne')
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
  }
}

@Component
export struct PageTwo {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Button('End')
    }
    .title('PageTwo')
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
  }
}
```

#### 示例3（边栏使用场景）

设置边栏：背景色与内容样式。

```ets
import { AtomicServiceNavigation, TitleBarType } from '@kit.ArkUI';
import { AtomicServiceTabs, TabBarOptions, TabBarPosition } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  childNavStack: NavPathStack = new NavPathStack();

  @Builder
  tabContent1() {
    Text('first page')
      .onClick(() => {
        this.childNavStack.pushPath({ name: 'page one' })
      })
  }

  @Builder
  tabContent2() {
    Text('second page')
  }

  @Builder
  tabContent3() {
    Text('third page')
  }

  @Builder
  navigationContent() {
    AtomicServiceTabs({
      tabContents: [
        () => {
          this.tabContent1()
        },
        () => {
          this.tabContent2()
        },
        () => {
          this.tabContent3()
        }
      ],
      tabBarOptionsArray: [
        new TabBarOptions($r('sys.media.ohos_ic_public_phone'), '功能1'),
        new TabBarOptions($r('sys.media.ohos_ic_public_location'), '功能2', Color.Green, Color.Red),
        new TabBarOptions($r('sys.media.ohos_ic_public_more'), '功能3')
      ],
      tabBarPosition: TabBarPosition.BOTTOM,
      barBackgroundColor: $r('sys.color.ohos_id_color_bottom_tab_bg'),
      onTabBarClick: (index: Number) => {
        if (index == 0) {
          this.message = '功能1';
        } else if (index == 1) {
          this.message = '功能2';
        } else {
          this.message = '功能3';
        }
      }
    })
  }

  @Builder
  pageMap(name: string) {
    if (name === 'page one') {
      PageOne()
    } else if (name === 'page two') {
      PageTwo()
    }
  }

  @State showText: string = 'time: ';
  @State time: number = 0;

  @Builder
  insertComp() {
    Text('This is menus area')
      .fontColor(Color.Red)
      .width(200)
      .height('100%')
  }

  @Builder
  sideBarContentBuilder() {
    Text('This is sideBar content area')
      .fontSize(20)
  }

  build() {
    Column() {
      AtomicServiceNavigation({
        navigationContent: () => {
          this.navigationContent()
        },
        navDestinationBuilder: this.pageMap,
        navPathStack: this.childNavStack,
        title: this.message,
        titleOptions: {
          titleIcon: $r('app.media.startIcon'),
          backgroundColor: 'rgb(61, 157, 180)',
          titleBarType: TitleBarType.DRAWER
        },
        sideBarOptions: {
          sideBarBackground: '#409EFF'
        },
        sideBarContent: () => { this.sideBarContentBuilder() },
        mode: NavigationMode.Stack
      })
    }
    .width('100%')
  }
}

@Component
export struct PageOne {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Button('Next')
        .onClick(() => {
          this.pageInfo.pushPath({ name: 'page two'})
        })
    }
    .title('PageOne')
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
  }
}

@Component
export struct PageTwo {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Button('End')
    }
    .title('PageTwo')
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
  }
}
```