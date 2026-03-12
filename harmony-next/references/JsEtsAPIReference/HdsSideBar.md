# HdsSideBar

本模块支持显示和隐藏的侧边栏容器，并且可以自定义侧边栏和内容区。

**起始版本：**6.0.0(20)

#### 导入模块

```ets
import { HdsSideBar } from '@kit.UIDesignKit';
```

#### 接口

HdsSideBar({contentAreaMask?: boolean, isShowSideBar?: boolean, $isShowSideBar?: Callback<boolean>, minSideBarWidth?: Length, maxSideBarWidth?: Length, minContentWidth?: Length, sideBarColor?: ResourceColor, contentColor?: ResourceColor, sideBarWidth?: Length, autoHide?: boolean, isSideBarBlur?: boolean, sideBarPosition?: sideBarPosition, onChange?: Callback<boolean>, sideBarPanelBuilder: CustomBuilder, contentPanelBuilder: CustomBuilder, sideBarContainerType?: SideBarContainerType})

**装饰器类型：**@ComponentV2

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

装饰器类型

说明

contentAreaMask

boolean

否

@Param

设置HdsSideBar组件侧边栏悬浮显示的场景下内容区是否有蒙层。

true：内容区有蒙层。false：内容区没有蒙层。

默认值：true。

isShowSideBar

boolean

否

@Param

设置HdsSideBar组件是否显示侧边栏。

true：显示侧边栏。

false：不显示侧边栏。

默认值：true。

$isShowSideBar

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)<boolean>

否

@Event

HdsSideBar组件侧边栏控制按钮点击后，是否显示侧边栏的回调。

minSideBarWidth

[Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length)

否

@Param

设置HdsSideBar组件侧边栏的最小宽度。

默认值：200vp。

maxSideBarWidth

[Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length)

否

@Param

设置HdsSideBar组件侧边栏的最大宽度。

默认值：280vp。

minContentWidth

[Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length)

否

@Param

设置HdsSideBar组件内容区可显示的最小宽度。

默认值：360vp。

sideBarColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

@Param

设置HdsSideBar组件侧边栏区的背景颜色。

默认值：Color.Transparent。

contentColor

[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)

否

@Param

设置HdsSideBar组件内容区的背景颜色。

默认值：Color.Transparent。

sideBarWidth

[Length](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#length)

否

@Param

设置HdsSideBar组件侧边栏的宽度。

默认值：240vp。

autoHide

boolean

否

@Param

设置HdsSideBar组件侧边栏拖拽到小于最小宽度后，是否自动隐藏。

true：会自动隐藏。

false：不会自动隐藏。

默认值：true。

isSideBarBlur

boolean

否

@Param

设置HdsSideBar组件窗口获焦时侧边栏是否有模糊效果。

true：窗口获焦时HdsSideBar组件侧边栏会有模糊效果，失焦时没有模糊效果。

false：窗口始终没有模糊效果。

默认值：true。

sideBarPosition

[SideBarPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-sidebarcontainer#sidebarposition9枚举说明)

否

@Param

设置HdsSideBar组件侧边栏显示位置。

默认值：SideBarPosition.Start，侧边栏位于容器左侧。

onChange

[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)<boolean>

否

@Param

当HdsSideBar组件侧边栏的状态在显示和隐藏之间切换时触发回调。

触发该事件的条件：

1. showSideBar属性值变换时。
1. showSideBar属性自适应行为变化时。
1. 分割线拖拽触发autoHide时。

true表示显示侧边栏，false表示隐藏侧边栏。

sideBarPanelBuilder

[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)

是

@Require

@BuilderParam

设置HdsSideBar组件侧边栏的子组件。

contentPanelBuilder

[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)

是

@Require

@BuilderParam

设置HdsSideBar组件内容区的子组件。

sideBarContainerType

[SideBarContainerType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-sidebarcontainer#sidebarcontainertype枚举说明)

否

@Param

设置HdsSideBar组件侧边栏的显示类型。

默认值：SideBarContainerType.AUTO，侧边栏嵌入到组件内，和内容区并列显示。

#### build

build(): void

struct的默认构造函数，无法直接调用此方法。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力****：**SystemCapability.UIDesign.HDSPattern.Standard

**起始版本：**6.0.0(20)

#### 示例

HdsSideBar提供侧边栏可以显示和隐藏的侧边栏容器，可以自定义侧边栏区和内容区。

```ets
import { HdsSideBar } from '@kit.UIDesignKit';

@Entry
@ComponentV2
struct Index {
  @Local isShowSidebar: boolean = true;

  //左侧侧边栏区
  @Builder
  SideBarPanelBuilder() {
    Column() {
      Text('左侧侧边栏区')
    }
    .width('100%')
    .height('100%')
    .margin(40)
  }

  //右侧内容区
  @Builder
  ContentPanelBuilder() {
    Text('右侧内容区')
      .margin(40)
  }

  @BuilderParam contentBuilder: () => void = this.ContentPanelBuilder
  @BuilderParam sideBarBuilder: () => void = this.SideBarPanelBuilder

  @Builder
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Button() {
        SymbolGlyph(this.isShowSidebar ? $r('sys.symbol.open_sidebar') : $r('sys.symbol.close_sidebar'))
          .fontWeight(FontWeight.Normal)
          .fontSize($r('sys.float.ohos_id_text_size_headline7'))
          .fontColor([$r('sys.color.ohos_id_color_titlebar_icon')])
          .hitTestBehavior(HitTestMode.None)
      }
      .id('side_bar_button')
      .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
      .height(30)
      .width(30)
      .onClick(() => {
        this.isShowSidebar = !this.isShowSidebar;
      })
      .zIndex(1)
      .margin({ top: 10, left: 10 })

      HdsSideBar({
        sideBarPanelBuilder: (): void => {
          this.sideBarBuilder()
        },
        contentPanelBuilder: (): void => {
          this.contentBuilder()
        },
        sideBarContainerType: SideBarContainerType.Overlay,
        maxSideBarWidth: 100,
        isShowSideBar: this.isShowSidebar,
        $isShowSideBar: (isShowSidebar: boolean) => {
          this.isShowSidebar = !isShowSidebar
        },
      })
    }
  }
}
```