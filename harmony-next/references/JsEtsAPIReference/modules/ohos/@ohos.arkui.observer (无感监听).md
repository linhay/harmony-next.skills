# @ohos.arkui.observer (无感监听)

提供UI组件行为变化的无感监听能力。推荐使用[UIObserver](../../types/classes/Class (UIObserver).md)进行组件监听。

-

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

UIObserver仅能监听到本进程内的相关信息，不支持获取跨进程场景的信息。

#### 导入模块

```ets
import { uiObserver } from '@kit.ArkUI';
```

#### NavDestinationState

NavDestination组件状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明ON_SHOWN0

NavDestination组件显示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

ON_HIDDEN1

NavDestination组件隐藏。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

ON_APPEAR12+2

NavDestination从组件树上挂载。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

ON_DISAPPEAR12+3

NavDestination从组件树上卸载。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

ON_WILL_SHOW12+4

NavDestination组件显示之前。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

ON_WILL_HIDE12+5

NavDestination组件隐藏之前。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

ON_WILL_APPEAR12+6

NavDestination挂载到组件树之前。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

ON_WILL_DISAPPEAR12+7

NavDestination从组件树上卸载之前。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

ON_ACTIVE17+8

NavDestination组件处于激活态。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

ON_INACTIVE17+9

NavDestination组件处于非激活态。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

ON_BACKPRESS12+100

NavDestination组件返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

#### ScrollEventType12+

滚动事件的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明SCROLL_START0滚动事件开始。SCROLL_STOP1滚动事件结束。

#### RouterPageState

routerPage生命周期触发时对应的状态。RouterPageState用于[RouterPageInfo](#ZH-CN_TOPIC_0000002529444737__routerpageinfo)中，作为[routerPageUpdate](#ZH-CN_TOPIC_0000002529444737__uiobserveronrouterpageupdate11)无感监听的返回值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明ABOUT_TO_APPEAR0page即将显示。ABOUT_TO_DISAPPEAR1page即将销毁。ON_PAGE_SHOW2page显示。ON_PAGE_HIDE3page隐藏。ON_BACK_PRESS4page返回时。

#### TabContentState12+

TabContent组件的状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称值说明ON_SHOW0TabContent组件显示。ON_HIDE1TabContent组件隐藏。

#### NavDestinationInfo

NavDestination组件信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明navigationId[ResourceStr](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否否

包含NavDestination组件的Navigation组件的id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

name[ResourceStr](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否否

NavDestination组件的名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

state[NavDestinationState](#ZH-CN_TOPIC_0000002529444737__navdestinationstate)否否

NavDestination组件的状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

index12+number否否

NavDestination在页面栈中的索引。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 取值范围：[0, +∞)

param12+Object否是

NavDestination组件的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

navDestinationId12+string否否

NavDestination组件的唯一标识ID。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

mode15+[NavDestinationMode](../../topics/misc/NavDestination.md#ZH-CN_TOPIC_0000002529284873__navdestinationmode枚举说明11)否是

NavDestination类型。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

uniqueId15+number否是

NavDestination组件的uniqueId。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

#### NavigationInfo12+

Navigation组件信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明navigationIdstring否否

Navigation组件的id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

pathStack[NavPathStack](../../topics/misc/Navigation.md#ZH-CN_TOPIC_0000002497444902__navpathstack10)否否

Navigation组件的导航控制器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

uniqueId20+number否是

Navigation组件的uniqueId，可以通过[queryNavigationInfo](../../topics/misc/自定义组件内置方法.md#ZH-CN_TOPIC_0000002497444970__querynavigationinfo12)获取。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

#### ScrollEventInfo12+

ScrollEvent滚动信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明idstring否否

滚动组件的id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

uniqueIdnumber否否

滚动组件的uniqueId。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

scrollEvent[ScrollEventType](#ZH-CN_TOPIC_0000002529444737__scrolleventtype12)否否

滚动事件的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

offsetnumber否否

滚动组件的当前偏移量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

axis20+[Axis](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__axis)否是

滚动组件的滚动方向。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

#### ObserverOptions12+

Observer选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明idstring否否组件的id。

#### RouterPageInfo

RouterPageInfo包含的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md) | [UIContext](../../types/classes/Class (UIContext).md)否否触发生命周期的routerPage页面对应的上下文信息。indexnumber否否

触发生命周期的routerPage在栈中的位置。

 取值范围：[0, +∞)

namestring否否触发生命周期的routerPage页面的名称。pathstring否否触发生命周期的routerPage页面的路径。state[RouterPageState](#ZH-CN_TOPIC_0000002529444737__routerpagestate)否否触发生命周期的routerPage页面的状态。pageId12+string否否触发生命周期的routerPage页面的唯一标识。

#### DensityInfo12+

屏幕像素密度变化回调包含的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明context[UIContext](../../types/classes/Class (UIContext).md)否否屏幕像素密度变化时页面对应的上下文信息。densitynumber否否

变化后的屏幕像素密度。

取值范围：[0, +∞)

#### NavDestinationSwitchInfo12+

Navigation组件页面切换的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md) | [UIContext](../../types/classes/Class (UIContext).md)否否触发页面切换的Navigation对应的上下文信息。from[NavDestinationInfo](#ZH-CN_TOPIC_0000002529444737__navdestinationinfo) | [NavBar](../../topics/misc/Navigation.md#ZH-CN_TOPIC_0000002497444902__navbar12)否否页面切换的源页面。to[NavDestinationInfo](#ZH-CN_TOPIC_0000002529444737__navdestinationinfo) | [NavBar](../../topics/misc/Navigation.md#ZH-CN_TOPIC_0000002497444902__navbar12)否否页面切换的目的页面。operation[NavigationOperation](../../topics/misc/Navigation.md#ZH-CN_TOPIC_0000002497444902__navigationoperation11枚举说明)否否页面切换操作类型。

#### NavDestinationSwitchObserverOptions12+

Navigation组件页面切换事件的监听选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明navigationId[ResourceStr](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr)否否指定需要监听的Navigation的ID。

#### TextChangeEventInfo22+

输入框文本变化的信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明idstring否否文本输入组件的ID。uniqueIdnumber否否文本输入组件的唯一标识符。contentstring否否变化后的文本内容。

#### TabContentInfo12+

TabContent页面的切换信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明tabContentIdstring否否

TabContent组件的id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

tabContentUniqueIdnumber否否

TabContent组件的uniqueId。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

state[TabContentState](#ZH-CN_TOPIC_0000002529444737__tabcontentstate12)否否

TabContent组件的状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

indexnumber否否

TabContent组件的下标索引。索引从0开始。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

idstring否否

Tabs组件的id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

uniqueIdnumber否否

Tabs组件的uniqueId。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

lastIndex22+number否是

最近一次聚焦的TabsContent组件的下标索引。索引从0开始。仅在[on('tabChange')](../../types/classes/Class (UIObserver).md#ZH-CN_TOPIC_0000002497444806__ontabchange22)的回调函数中存在。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

#### WindowSizeLayoutBreakpointInfo22+

窗口尺寸布局断点变化回调的信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

名称类型只读可选说明widthBreakpoint[WidthBreakpoint](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__widthbreakpoint13)是否窗口宽度所在的布局断点枚举。heightBreakpoint[HeightBreakpoint](../../guides/枚举说明.md#ZH-CN_TOPIC_0000002529284967__heightbreakpoint13)是否窗口高度所在的布局断点枚举。

#### uiObserver.on('navDestinationUpdate')

on(type: 'navDestinationUpdate', callback: Callback<NavDestinationInfo>): void

监听NavDestination组件的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'navDestinationUpdate'，即NavDestination组件的状态变化。callbackCallback<[NavDestinationInfo](#ZH-CN_TOPIC_0000002529444737__navdestinationinfo)>是回调函数。返回当前的NavDestination组件状态。

**示例：**

```ets
// Index.ets
// 演示 uiObserver.on('navDestinationUpdate', callback)
// uiObserver.off('navDestinationUpdate', callback)
import { uiObserver } from '@kit.ArkUI';

@Component
struct PageOne {
  build() {
    NavDestination() {
      Text("pageOne")
    }.title("pageOne")
  }
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  @Builder
  PageBuilder(name: string) {
    PageOne()
  }

  aboutToAppear() {
    uiObserver.on('navDestinationUpdate', (info) => {
      console.info(`NavDestination state update ${JSON.stringify(info)}`);
    });
  }

  aboutToDisappear() {
    uiObserver.off('navDestinationUpdate');
  }

  build() {
    Column() {
      Navigation(this.stack) {
        Button("push").onClick(() => {
          this.stack.pushPath({ name: "pageOne" });
        })
      }
      .title("Navigation")
      .navDestination(this.PageBuilder)
    }
    .width('100%')
    .height('100%')
  }
}
```

#### uiObserver.off('navDestinationUpdate')

off(type: 'navDestinationUpdate', callback?: Callback<NavDestinationInfo>): void

取消监听NavDestination组件的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'navDestinationUpdate'，即NavDestination组件的状态变化。callbackCallback<[NavDestinationInfo](#ZH-CN_TOPIC_0000002529444737__navdestinationinfo)>否回调函数。返回当前的NavDestination组件状态。

**示例：**

参考[uiObserver.on('navDestinationUpdate')](#ZH-CN_TOPIC_0000002529444737__uiobserveronnavdestinationupdate)示例。

#### uiObserver.on('navDestinationUpdate')

on(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback: Callback<NavDestinationInfo>): void

监听NavDestination组件的状态变化。与[uiObserver.on](#ZH-CN_TOPIC_0000002529444737__uiobserveronnavdestinationupdate)相比，新增了options参数，即支持指定监听的Navigation的id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'navDestinationUpdate'，即NavDestination组件的状态变化。options{ navigationId: [ResourceStr](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) }是指定监听的Navigation的id。callbackCallback<[NavDestinationInfo](#ZH-CN_TOPIC_0000002529444737__navdestinationinfo)>是回调函数。返回当前的NavDestination组件状态。

**示例：**

```ets
// Index.ets
// 演示 uiObserver.on('navDestinationUpdate', navigationId, callback)
// uiObserver.off('navDestinationUpdate', navigationId, callback)
import { uiObserver } from '@kit.ArkUI';

@Component
struct PageOne {
  build() {
    NavDestination() {
      Text("pageOne")
    }.title("pageOne")
  }
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  @Builder
  PageBuilder(name: string) {
    PageOne()
  }

  aboutToAppear() {
    uiObserver.on('navDestinationUpdate', { navigationId: "testId" }, (info) => {
      console.info(`NavDestination state update ${JSON.stringify(info)}`);
    });
  }

  aboutToDisappear() {
    uiObserver.off('navDestinationUpdate', { navigationId: "testId" });
  }

  build() {
    Column() {
      Navigation(this.stack) {
        Button("push").onClick(() => {
          this.stack.pushPath({ name: "pageOne" });
        })
      }
      .id("testId")
      .title("Navigation")
      .navDestination(this.PageBuilder)
    }
    .width('100%')
    .height('100%')
  }
}
```

#### uiObserver.off('navDestinationUpdate')

off(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback?: Callback<NavDestinationInfo>): void

取消监听NavDestination组件的状态变化。与[uiObserver.off](#ZH-CN_TOPIC_0000002529444737__uiobserveroffnavdestinationupdate)相比，新增了options参数，即支持指定监听的Navigation的id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'navDestinationUpdate'，即NavDestination组件的状态变化。options{ navigationId: [ResourceStr](../../topics/misc/基础类型定义.md#ZH-CN_TOPIC_0000002497604974__resourcestr) }是指定监听的Navigation的id。callbackCallback<[NavDestinationInfo](#ZH-CN_TOPIC_0000002529444737__navdestinationinfo)>否回调函数。返回当前的NavDestination组件状态。

**示例：**

参考[uiObserver.on('navDestinationUpdate')](#ZH-CN_TOPIC_0000002529444737__uiobserveronnavdestinationupdate-1)示例。

#### uiObserver.on('scrollEvent')12+

on(type: 'scrollEvent', callback: Callback<ScrollEventInfo>): void

监听所有滚动组件滚动事件的开始和结束。滚动组件包括[List](../../topics/components/list.md)、[Grid](../../topics/components/Grid.md)、[Scroll](../../topics/components/Scroll.md)、[WaterFlow](../../topics/misc/WaterFlow.md)、[ArcList](../../topics/components/ArcList.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'scrollEvent'，即滚动事件的开始和结束。callbackCallback<[ScrollEventInfo](#ZH-CN_TOPIC_0000002529444737__scrolleventinfo12)>是回调函数。返回滚动事件的信息。

**示例：**

参考[uiObserver.off('scrollEvent')](#ZH-CN_TOPIC_0000002529444737__uiobserveroffscrollevent12-1)示例。

#### uiObserver.off('scrollEvent')12+

off(type: 'scrollEvent', callback?: Callback<ScrollEventInfo>): void

取消监听所有滚动组件滚动事件的开始和结束。滚动组件包括[List](../../topics/components/list.md)、[Grid](../../topics/components/Grid.md)、[Scroll](../../topics/components/Scroll.md)、[WaterFlow](../../topics/misc/WaterFlow.md)、[ArcList](../../topics/components/ArcList.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'scrollEvent'，即滚动事件的开始和结束。callbackCallback<[ScrollEventInfo](#ZH-CN_TOPIC_0000002529444737__scrolleventinfo12)>否回调函数。返回滚动事件的信息。

**示例：**

参考[uiObserver.off('scrollEvent')](#ZH-CN_TOPIC_0000002529444737__uiobserveroffscrollevent12-1)示例。

#### uiObserver.on('scrollEvent')12+

on(type: 'scrollEvent', options: ObserverOptions, callback: Callback<ScrollEventInfo>): void

监听指定id的滚动组件滚动事件的开始和结束。滚动组件包括[List](../../topics/components/list.md)、[Grid](../../topics/components/Grid.md)、[Scroll](../../topics/components/Scroll.md)、[WaterFlow](../../topics/misc/WaterFlow.md)、[ArcList](../../topics/components/ArcList.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'scrollEvent'，即滚动事件的开始和结束。options[ObserverOptions](#ZH-CN_TOPIC_0000002529444737__observeroptions12)是指定监听的滚动组件的id。callbackCallback<[ScrollEventInfo](#ZH-CN_TOPIC_0000002529444737__scrolleventinfo12)>是回调函数。返回滚动事件的信息。

**示例：**

参考[uiObserver.off('scrollEvent')](#ZH-CN_TOPIC_0000002529444737__uiobserveroffscrollevent12-1)示例。

#### uiObserver.off('scrollEvent')12+

off(type: 'scrollEvent', options: ObserverOptions, callback?: Callback<ScrollEventInfo>): void

取消监听指定id的滚动组件滚动事件的开始和结束。滚动组件包括[List](../../topics/components/list.md)、[Grid](../../topics/components/Grid.md)、[Scroll](../../topics/components/Scroll.md)、[WaterFlow](../../topics/misc/WaterFlow.md)、[ArcList](../../topics/components/ArcList.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'scrollEvent'，即滚动事件的开始和结束。options[ObserverOptions](#ZH-CN_TOPIC_0000002529444737__observeroptions12)是指定监听的滚动组件的id。callbackCallback<[ScrollEventInfo](#ZH-CN_TOPIC_0000002529444737__scrolleventinfo12)>否回调函数。返回滚动事件的信息。

**示例：**

```ets
import { uiObserver } from '@kit.ArkUI'

@Entry
@Component
struct Index {
  scroller: Scroller = new Scroller();
  options: uiObserver.ObserverOptions = { id: 'testId' };
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7]

  build() {
    Column() {
      Column() {
        Scroll(this.scroller) {
          Column() {
            ForEach(this.arr, (item: number) => {
              Text(item.toString())
                .width('90%')
                .height(150)
                .backgroundColor(0xFFFFFF)
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .margin({ top: 10 })
            }, (item: string) => item)
          }.width('100%')
        }
        .id('testId')
        .height('80%')
      }
      .width('100%')

      Row() {
        Button('UIObserver on')
          .onClick(() => {
            uiObserver.on('scrollEvent', (info) => {
              console.info(`scrollEventInfo ${JSON.stringify(info)}`);
            });
          })
        Button('UIObserver off')
          .onClick(() => {
            uiObserver.off('scrollEvent');
          })
      }

      Row() {
        Button('UIObserverWithId on')
          .onClick(() => {
            uiObserver.on('scrollEvent', this.options, (info) => {
              console.info(`scrollEventInfo ${JSON.stringify(info)}`);
            });
          })
        Button('UIObserverWithId off')
          .onClick(() => {
            uiObserver.off('scrollEvent',this.options);
          })
      }
    }
    .height('100%')
  }
}
```

#### uiObserver.on('routerPageUpdate')11+

on(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>): void

监听router中page页面的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'routerPageUpdate'，即router中page页面的状态变化。context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md) | [UIContext](../../types/classes/Class (UIContext).md)是上下文信息，用以指定监听页面的范围。callbackCallback<[RouterPageInfo](#ZH-CN_TOPIC_0000002529444737__routerpageinfo)>是回调函数。携带pageInfo，返回当前的page页面状态。

**示例：**

```ets
// used in UIAbility
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { UIContext, window, uiObserver } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  private uiContext: UIContext | null = null;

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // 注册监听，范围是abilityContext内的page
    uiObserver.on('routerPageUpdate', this.context, (info: uiObserver.RouterPageInfo) => {
      console.info(`[uiObserver][abilityContext] got info: ${JSON.stringify(info)}`)
    })
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (err) => {
      windowStage.getMainWindow((err: BusinessError, data) => {
        let windowInfo: window.Window = data;
        // 获取UIContext实例
        this.uiContext = windowInfo.getUIContext();
        // 注册监听，范围是uiContext内的page
        uiObserver.on('routerPageUpdate', this.uiContext, (info: uiObserver.RouterPageInfo)=>{
          console.info(`[uiObserver][uiContext] got info: ${JSON.stringify(info)}`)
        })
      })
    });
  }

  // ... other function in EntryAbility
}
```

#### uiObserver.off('routerPageUpdate')11+

off(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback?: Callback<RouterPageInfo>): void

取消监听router中page页面的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'routerPageUpdate'，即router中page页面的状态变化。context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md) | [UIContext](../../types/classes/Class (UIContext).md)是上下文信息，用以指定监听页面的范围。callbackCallback<[RouterPageInfo](#ZH-CN_TOPIC_0000002529444737__routerpageinfo)>否需要被注销的回调函数。

**示例：**

```ets
// used in UIAbility
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { uiObserver, UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // 实际使用前uiContext需要被赋值。参见示例uiObserver.on('routerPageUpdate')
  private uiContext: UIContext | null = null;

  onDestroy(): void {
    // 注销当前abilityContext上的所有routerPageUpdate监听
    uiObserver.off('routerPageUpdate', this.context)
  }

  onWindowStageDestroy(): void {
    // 注销在uiContext上的所有routerPageUpdate监听
    if (this.uiContext) {
      uiObserver.off('routerPageUpdate', this.uiContext);
    }
  }

  // ... other function in EntryAbility
}
```

#### uiObserver.on('densityUpdate')12+

on(type: 'densityUpdate', context: UIContext, callback: Callback<DensityInfo>): void

监听屏幕像素密度变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'densityUpdate'，即屏幕像素密度变化。context[UIContext](../../types/classes/Class (UIContext).md)是上下文信息，用以指定监听页面的范围。callbackCallback<[DensityInfo](#ZH-CN_TOPIC_0000002529444737__densityinfo12)>是回调函数。携带densityInfo，返回变化后的屏幕像素密度。

**示例：**

```ets
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State density: number = 0;
  @State message: string = '未注册监听';

  densityUpdateCallback = (info: uiObserver.DensityInfo) => {
    this.density = info.density;
    this.message = '变化后的DPI：' + this.density.toString();
  }

  build() {
    Column() {
      Text(this.message)
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
      Button('注册屏幕像素密度变化监听')
        .onClick(() => {
          this.message = '已注册监听'
          uiObserver.on('densityUpdate', this.getUIContext(), this.densityUpdateCallback);
        })
    }
  }
}
```

#### uiObserver.off('densityUpdate')12+

off(type: 'densityUpdate', context: UIContext, callback?: Callback<DensityInfo>): void

取消监听屏幕像素密度的变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'densityUpdate'，即屏幕像素密度变化。context[UIContext](../../types/classes/Class (UIContext).md)是上下文信息，用以指定监听页面的范围。callbackCallback<[DensityInfo](#ZH-CN_TOPIC_0000002529444737__densityinfo12)>否需要被注销的回调函数。若不指定具体的回调函数，则注销指定UIContext下所有densityUpdate事件监听。

```ets
import { uiObserver, UIContext } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State density: number = 0;
  @State message: string = '未注册监听'

  densityUpdateCallback = (info: uiObserver.DensityInfo) => {
    this.density = info.density;
    this.message = '变化后的DPI：' + this.density.toString();
  }

  build() {
    Column() {
      Text(this.message)
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
      Button('注册屏幕像素密度变化监听')
        .margin({ bottom: 10 })
        .onClick(() => {
          this.message = '已注册监听'
          uiObserver.on('densityUpdate', this.getUIContext(), this.densityUpdateCallback);
        })
      Button('解除注册屏幕像素密度变化监听')
        .onClick(() => {
          this.message = '未注册监听'
          uiObserver.off('densityUpdate', this.getUIContext(), this.densityUpdateCallback);
        })
    }
  }
}
```

#### uiObserver.on('willDraw')12+

on(type: 'willDraw', context: UIContext, callback: Callback<void>): void

监听每一帧绘制指令下发情况。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'willDraw'，即是否将要绘制。context[UIContext](../../types/classes/Class (UIContext).md)是上下文信息，用以指定监听页面的范围。callbackCallback<void>是回调函数。

**示例：**

```ets
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  willDrawCallback = () => {
    console.info("willDraw指令下发");
  }
  build() {
    Column() {
      Button('注册绘制指令下发监听')
        .onClick(() => {
          uiObserver.on('willDraw', this.getUIContext(), this.willDrawCallback);
        })
    }
  }
}
```

#### uiObserver.off('willDraw')12+

off(type: 'willDraw', context: UIContext, callback?: Callback<void>): void

取消监听每一帧绘制指令下发情况。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'willDraw'，即是否将要绘制。context[UIContext](../../types/classes/Class (UIContext).md)是上下文信息，用以指定监听页面的范围。callbackCallback<void>否需要被注销的回调函数。

```ets
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  willDrawCallback = () => {
    console.info("willDraw指令下发")
  }

  build() {
    Column() {
      Button('注册绘制指令下发监听')
        .margin({ bottom: 10 })
        .onClick(() => {
          uiObserver.on('willDraw', this.getUIContext(), this.willDrawCallback);
        })
      Button('解除注册绘制指令下发监听')
        .onClick(() => {
          uiObserver.off('willDraw', this.getUIContext(), this.willDrawCallback);
        })
    }
  }
}
```

#### uiObserver.on('didLayout')12+

on(type: 'didLayout', context: UIContext, callback: Callback<void>): void

监听每一帧布局完成情况。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'didLayout'，即是否布局完成。context[UIContext](../../types/classes/Class (UIContext).md)是上下文信息，用以指定监听页面的范围。callbackCallback<void>是回调函数。

**示例：**

```ets
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  didLayoutCallback = () => {
    console.info("Layout布局完成");
  }
  build() {
    Column() {
      Button('注册布局完成监听')
        .onClick(() => {
          uiObserver.on('didLayout', this.getUIContext(), this.didLayoutCallback);
        })
    }
  }
}
```

#### uiObserver.off('didLayout')12+

off(type: 'didLayout', context: UIContext, callback?: Callback<void>): void

取消监听每一帧布局完成情况。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'didLayout'，即是否布局完成。context[UIContext](../../types/classes/Class (UIContext).md)是上下文信息，用以指定监听页面的范围。callbackCallback<void>否需要被注销的回调函数。

```ets
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  didLayoutCallback = () => {
    console.info("Layout布局完成")
  }

  build() {
    Column() {
      Button('注册布局完成监听')
        .margin({ bottom: 10 })
        .onClick(() => {
          uiObserver.on('didLayout', this.getUIContext(), this.didLayoutCallback);
        })
      Button('解除布局完成监听')
        .onClick(() => {
          uiObserver.off('didLayout', this.getUIContext(), this.didLayoutCallback);
        })
    }
  }
}
```

#### uiObserver.on('navDestinationSwitch')12+

on(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback: Callback<NavDestinationSwitchInfo>): void

监听Navigation的页面切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'navDestinationSwitch'，即Navigation的页面切换事件。context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md) | [UIContext](../../types/classes/Class (UIContext).md)是上下文信息，用以指定监听页面切换事件的范围。callbackCallback<[NavDestinationSwitchInfo](#ZH-CN_TOPIC_0000002529444737__navdestinationswitchinfo12)>是回调函数。携带NavDestinationSwitchInfo，返回页面切换事件的信息。

**示例：**

```ets
// EntryAbility.ets
// 演示 uiObserver.on('navDestinationSwitch', UIAbilityContext, callback)
// uiObserver.off('navDestinationSwitch', UIAbilityContext, callback)
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { uiObserver, window } from '@kit.ArkUI';
import { hilog } from "@kit.PerformanceAnalysisKit";

function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
  console.info(`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}`)
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    uiObserver.on('navDestinationSwitch', this.context, callbackFunc);
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
    uiObserver.off('navDestinationSwitch', this.context, callbackFunc);
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

```ets
// Index.ets
// 演示 uiObserver.on('navDestinationSwitch', UIContext, callback)
// uiObserver.off('navDestinationSwitch', UIContext, callback)
import { uiObserver } from '@kit.ArkUI';

@Component
struct PageOne {
  build() {
    NavDestination() {
      Text("pageOne")
    }.title("pageOne")
  }
}

function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
  console.info(`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}`)
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  @Builder
  PageBuilder(name: string) {
    PageOne()
  }

  aboutToAppear() {
    uiObserver.on('navDestinationSwitch', this.getUIContext(), callbackFunc)
  }

  aboutToDisappear() {
    uiObserver.off('navDestinationSwitch', this.getUIContext(), callbackFunc)
  }

  build() {
    Column() {
      Navigation(this.stack) {
        Button("push").onClick(() => {
          this.stack.pushPath({ name: "pageOne" });
        })
      }
      .title("Navigation")
      .navDestination(this.PageBuilder)
    }
    .width('100%')
    .height('100%')
  }
}
```

#### uiObserver.off('navDestinationSwitch')12+

off(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback?: Callback<NavDestinationSwitchInfo>): void

取消监听Navigation的页面切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'navDestinationSwitch'，即Navigation的页面切换事件。context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md) | [UIContext](../../types/classes/Class (UIContext).md)是上下文信息，用以指定监听页面切换事件的范围。callbackCallback<[NavDestinationSwitchInfo](#ZH-CN_TOPIC_0000002529444737__navdestinationswitchinfo12)>否需要被注销的回调函数。

**示例：**

参考[uiObserver.on('navDestinationSwitch')](#ZH-CN_TOPIC_0000002529444737__uiobserveronnavdestinationswitch12)示例。

#### uiObserver.on('navDestinationSwitch')12+

on(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, observerOptions: NavDestinationSwitchObserverOptions, callback: Callback<NavDestinationSwitchInfo>): void

监听Navigation的页面切换事件。与[uiObserver.on](#ZH-CN_TOPIC_0000002529444737__uiobserveronnavdestinationswitch12)相比，新增了observerOptions参数，即支持设置监听选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'navDestinationSwitch'，即Navigation的页面切换事件。context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md) | [UIContext](../../types/classes/Class (UIContext).md)是上下文信息，用以指定监听页面切换事件的范围。observerOptions[NavDestinationSwitchObserverOptions](#ZH-CN_TOPIC_0000002529444737__navdestinationswitchobserveroptions12)是监听选项。callbackCallback<[NavDestinationSwitchInfo](#ZH-CN_TOPIC_0000002529444737__navdestinationswitchinfo12)>是回调函数。携带NavDestinationSwitchInfo，返回页面切换事件的信息。

**示例：**

```ets
// EntryAbility.ets
// 演示 uiObserver.on('navDestinationSwitch', UIAbilityContext, NavDestinationSwitchObserverOptions, callback)
// uiObserver.off('navDestinationSwitch', UIAbilityContext, NavDestinationSwitchObserverOptions, callback)
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { uiObserver, window } from '@kit.ArkUI';
import { hilog } from "@kit.PerformanceAnalysisKit"

function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
  console.info(`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}`)
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    uiObserver.on('navDestinationSwitch', this.context, {
      navigationId: "myNavId"
    }, callbackFunc);
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
    uiObserver.off('navDestinationSwitch', this.context, {
      navigationId: "myNavId"
    }, callbackFunc);
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

```ets
// Index.ets
// 演示 uiObserver.on('navDestinationSwitch', UIContext, NavDestinationSwitchObserverOptions, callback)
// uiObserver.off('navDestinationSwitch', UIContext, NavDestinationSwitchObserverOptions, callback)
import { uiObserver } from '@kit.ArkUI';

@Component
struct PageOne {
  build() {
    NavDestination() {
      Text("pageOne")
    }.title("pageOne")
  }
}

function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
  console.info(`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}`)
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  @Builder
  PageBuilder(name: string) {
    PageOne()
  }

  aboutToAppear() {
    uiObserver.on('navDestinationSwitch', this.getUIContext(), { navigationId: "myNavId" }, callbackFunc)
  }

  aboutToDisappear() {
    uiObserver.off('navDestinationSwitch', this.getUIContext(), { navigationId: "myNavId" }, callbackFunc)
  }

  build() {
    Column() {
      Navigation(this.stack) {
        Button("push").onClick(() => {
          this.stack.pushPath({ name: "pageOne" });
        })
      }
      .id("myNavId")
      .title("Navigation")
      .navDestination(this.PageBuilder)
    }
    .width('100%')
    .height('100%')
  }
}
```

#### uiObserver.off('navDestinationSwitch')12+

off(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, observerOptions: NavDestinationSwitchObserverOptions, callback?: Callback<NavDestinationSwitchInfo>): void

取消监听Navigation的页面切换事件。与[uiObserver.off](#ZH-CN_TOPIC_0000002529444737__uiobserveroffnavdestinationswitch12)相比，新增了observerOptions参数，即支持设置监听选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'navDestinationSwitch'，即Navigation的页面切换事件。context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md) | [UIContext](../../types/classes/Class (UIContext).md)是上下文信息，用以指定监听页面切换事件的范围。observerOptions[NavDestinationSwitchObserverOptions](#ZH-CN_TOPIC_0000002529444737__navdestinationswitchobserveroptions12)是监听选项。callbackCallback<[NavDestinationSwitchInfo](#ZH-CN_TOPIC_0000002529444737__navdestinationswitchinfo12)>否需要被注销的回调函数。

**示例：**

参考[uiObserver.on('navDestinationSwitch')](#ZH-CN_TOPIC_0000002529444737__uiobserveronnavdestinationswitch12-1)接口示例。

#### uiObserver.on('tabContentUpdate')12+

on(type: 'tabContentUpdate', callback: Callback<TabContentInfo>): void

监听TabContent页面的切换事件。相比[on('tabChange')](../../types/classes/Class (UIObserver).md#ZH-CN_TOPIC_0000002497444806__ontabchange22)，本接口不支持监听Tabs组件初始化时，显示首个页签的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'tabContentUpdate'，即TabContent页面的切换事件。callbackCallback<[TabContentInfo](#ZH-CN_TOPIC_0000002529444737__tabcontentinfo12)>是回调函数。携带TabContentInfo，返回TabContent页面切换事件的信息。

**示例：**

```ets
import { uiObserver } from '@kit.ArkUI';

function callbackFunc(info: uiObserver.TabContentInfo) {
  console.info(`tabContentUpdate ${JSON.stringify(info)}`);
}

@Entry
@Component
struct TabsExample {

  aboutToAppear(): void {
    uiObserver.on('tabContentUpdate', callbackFunc);
  }

  aboutToDisappear(): void {
    uiObserver.off('tabContentUpdate', callbackFunc);
  }

  build() {
    Column() {
      Tabs() {
        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#00CB87')
        }.tabBar('green').id('tabContentId0')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#007DFF')
        }.tabBar('blue').id('tabContentId1')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#FFBF00')
        }.tabBar('yellow').id('tabContentId2')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#E67C92')
        }.tabBar('pink').id('tabContentId3')
      }
      .width(360)
      .height(296)
      .backgroundColor('#F1F3F5')
      .id('tabsId')
    }.width('100%')
  }
}
```

#### uiObserver.off('tabContentUpdate')12+

off(type: 'tabContentUpdate', callback?: Callback<TabContentInfo>): void

取消监听TabContent页面的切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'tabContentUpdate'，即TabContent页面的切换事件。callbackCallback<[TabContentInfo](#ZH-CN_TOPIC_0000002529444737__tabcontentinfo12)>否需要被注销的回调函数。

**示例：**

参考[uiObserver.on('tabContentUpdate')](#ZH-CN_TOPIC_0000002529444737__uiobserverontabcontentupdate12)接口示例。

#### uiObserver.on('tabContentUpdate')12+

on(type: 'tabContentUpdate', options: ObserverOptions, callback: Callback<TabContentInfo>): void

监听指定Tabs组件id的TabContent页面切换事件。相比[on('tabChange')](../../types/classes/Class (UIObserver).md#ZH-CN_TOPIC_0000002497444806__ontabchange22)，本接口不支持监听Tabs组件初始化时，显示首个页签的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'tabContentUpdate'，即TabContent页面的切换事件。options[ObserverOptions](#ZH-CN_TOPIC_0000002529444737__observeroptions12)是指定监听的Tabs组件的id。callbackCallback<[TabContentInfo](#ZH-CN_TOPIC_0000002529444737__tabcontentinfo12)>是回调函数。携带TabContentInfo，返回TabContent页面切换事件的信息。

**示例：**

```ets
import { uiObserver } from '@kit.ArkUI';

function callbackFunc(info: uiObserver.TabContentInfo) {
  console.info(`tabContentUpdate ${JSON.stringify(info)}`);
}

@Entry
@Component
struct TabsExample {

  aboutToAppear(): void {
    uiObserver.on('tabContentUpdate', { id: 'tabsId' }, callbackFunc);
  }

  aboutToDisappear(): void {
    uiObserver.off('tabContentUpdate', { id: 'tabsId' }, callbackFunc);
  }

  build() {
    Column() {
      Tabs() {
        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#00CB87')
        }.tabBar('green').id('tabContentId0')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#007DFF')
        }.tabBar('blue').id('tabContentId1')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#FFBF00')
        }.tabBar('yellow').id('tabContentId2')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#E67C92')
        }.tabBar('pink').id('tabContentId3')
      }
      .width(360)
      .height(296)
      .backgroundColor('#F1F3F5')
      .id('tabsId')
    }.width('100%')
  }
}
```

#### uiObserver.off('tabContentUpdate')12+

off(type: 'tabContentUpdate', options: ObserverOptions, callback?: Callback<TabContentInfo>): void

取消监听指定Tabs组件id的TabContent页面切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明typestring是监听事件，固定为'tabContentUpdate'，即TabContent页面的切换事件。options[ObserverOptions](#ZH-CN_TOPIC_0000002529444737__observeroptions12)是指定监听的Tabs组件的id。callbackCallback<[TabContentInfo](#ZH-CN_TOPIC_0000002529444737__tabcontentinfo12)>否需要被注销的回调函数。

**示例：**

参考[uiObserver.on('tabContentUpdate')](#ZH-CN_TOPIC_0000002529444737__uiobserverontabcontentupdate12-1)接口示例。