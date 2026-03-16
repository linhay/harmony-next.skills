# Class (TextMenuController)

提供控制文本菜单的能力。

-

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Class首批接口从API version 16开始支持。

-

以下非静态API需先使用UIContext中的[getTextMenuController()](Class (UIContext).md#ZH-CN_TOPIC_0000002529444749__gettextmenucontroller16)方法获取TextMenuController实例，再通过此实例调用对应方法。

#### setMenuOptions16+

setMenuOptions(options: TextMenuOptions): void

设置菜单选项。

**元服务API：** 从API version 16开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明options[TextMenuOptions](../../topics/misc/文本组件公共接口.md#ZH-CN_TOPIC_0000002529444865__textmenuoptions16对象说明)是

设置菜单选项。

默认值:{showMode: TextMenuShowMode.DEFAULT}

**示例：**

```ets
// xxx.ets
@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // 设置在对应的UIContext下优先使用独立窗口显示文本选择菜单
    this.getUIContext()
      .getTextMenuController()
      .setMenuOptions(
        {
          showMode: TextMenuShowMode.PREFER_WINDOW
        }
      );
  }

  build() {
    Row() {
      Column() {
        TextInput({ text: "这是一个TextInput，长按弹出文本选择菜单" })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })

        Text("这是一个Text，长按弹出文本选择菜单")
          .height(60)
          .copyOption(CopyOptions.InApp)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
      }.width('100%')
    }
    .height('100%')
  }
}
```

#### disableSystemServiceMenuItems20+

static disableSystemServiceMenuItems(disable: boolean): void

屏蔽文本选择菜单内所有系统服务菜单项。

-

此接口调用后整个应用进程都会生效。

-

此接口可在[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)使用。

-

此接口调用后将影响文本组件的接口[editMenuOptions](../../topics/graphics/Text.md#ZH-CN_TOPIC_0000002497444914__editmenuoptions12)，其回调方法[onCreateMenu](../../topics/misc/文本组件公共接口.md#ZH-CN_TOPIC_0000002529444865__oncreatemenu12)的入参列表中不包含被屏蔽的菜单选项。

-

涉及文本选择菜单的组件有 [Text](../../topics/graphics/Text.md)、[TextArea](../../topics/graphics/TextArea.md)、[TextInput](../../topics/graphics/TextInput.md)、[Search](../../topics/components/search.md)、[RichEditor](../../topics/misc/RichEditor.md)、[Web](../../topics/misc/组件描述.md)。

-

系统服务菜单项指除[TextMenuItemId](../../topics/misc/文本组件公共接口.md#ZH-CN_TOPIC_0000002529444865__textmenuitemid12)中的复制、剪切、全选、粘贴以外的菜单项。

-

当disableSystemServiceMenuItems与disableMenuItems同时设置时，优先生效先设置的disableSystemServiceMenuItems。

-

使用该接口时，全局生效，多次调用以最后一次为准。

-

可以通过以下三种方式恢复禁用菜单：

  - 仅设置disableSystemServiceMenuItems(true)禁用菜单时，设置false即可恢复禁用；
  - 仅设置disableMenuItems禁用菜单时，设置为空数组即可恢复禁用；
  - 当disableSystemServiceMenuItems与disableMenuItems同时使用时，则前者设置为false，后者设置为空数组，即可恢复禁用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明disableboolean是

是否禁用系统服务菜单。true表示禁用，false表示不禁用。

默认值: false

**示例：**

```ets
import { TextMenuController } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // 禁用所有系统服务菜单。
    TextMenuController.disableSystemServiceMenuItems(true)
  }

  aboutToDisappear(): void {
    // 页面消失恢复系统服务菜单。
    TextMenuController.disableSystemServiceMenuItems(false)
  }

  build() {
    Row() {
      Column() {
        TextInput({ text: "这是一个TextInput，长按弹出文本选择菜单" })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
                // menuItems不包含被屏蔽的系统菜单项。
                return menuItems
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
                return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}
```

#### disableMenuItems20+

static disableMenuItems(items: Array<TextMenuItemId>): void

屏蔽文本选择菜单内指定的系统服务菜单项。

-

此接口调用后整个应用进程都会生效。

-

此接口可在[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)使用。

-

此接口调用后将影响文本组件的接口[editMenuOptions](../../topics/graphics/Text.md#ZH-CN_TOPIC_0000002497444914__editmenuoptions12)，其回调方法[onCreateMenu](../../topics/misc/文本组件公共接口.md#ZH-CN_TOPIC_0000002529444865__oncreatemenu12)的入参列表中不包含被屏蔽的菜单选项。

-

涉及文本选择菜单的组件有 [Text](../../topics/graphics/Text.md)、[TextArea](../../topics/graphics/TextArea.md)、[TextInput](../../topics/graphics/TextInput.md)、[Search](../../topics/components/search.md)、[RichEditor](../../topics/misc/RichEditor.md)、[Web](../../topics/misc/组件描述.md)。

-

系统服务菜单项指除[TextMenuItemId](../../topics/misc/文本组件公共接口.md#ZH-CN_TOPIC_0000002529444865__textmenuitemid12)中的复制、剪切、全选、粘贴以外的菜单项。

-

当disableSystemServiceMenuItems与disableMenuItems同时设置时，优先生效先设置的disableSystemServiceMenuItems。

-

使用该接口时，全局生效，多次调用以最后一次为准。

-

可以通过以下三种方式恢复禁用菜单：

  - 仅设置disableSystemServiceMenuItems(true)禁用菜单时，设置false即可恢复禁用；
  - 仅设置disableMenuItems禁用菜单时，设置为空数组即可恢复禁用；
  - 当disableSystemServiceMenuItems与disableMenuItems同时使用时，则前者设置为false，后者设置为空数组，即可恢复禁用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

参数名类型必填说明itemsArray<[TextMenuItemId](../../topics/misc/文本组件公共接口.md#ZH-CN_TOPIC_0000002529444865__textmenuitemid12)>是

禁用菜单项的列表。

默认值: []

默认不禁用任何菜单。

**示例：**

```ets
import { TextMenuController } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // 禁用搜索和翻译菜单。
    TextMenuController.disableMenuItems([TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE])
  }

  aboutToDisappear(): void {
    // 恢复系统服务菜单。
    TextMenuController.disableMenuItems([])
  }

  build() {
    Row() {
      Column() {
        TextInput({ text: "这是一个TextInput，长按弹出文本选择菜单" })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
                // menuItems不包含搜索和翻译。
                return menuItems;
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
                return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}
```