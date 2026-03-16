# statusBarManager（状态栏管理服务）

本模块为应用提供接入状态栏的能力。应用可以通过接入相应的API，可快速在状态栏显示应用及下拉面板，实现对应用的管理；用户可以通过直接操作状态栏图标完成一些应用操作。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { statusBarManager } from '@kit.DeskTopExtensionKit';
```

#### statusBarManager.StatusBarItem

状态栏图标详细参数。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.0(12)

**名称**

**类型**

**只读**

可选

**说明**

icons

[StatusBarIcon](#section1844717231113)

否

否

状态栏应用图标的图片信息。

quickOperation

[QuickOperation](#section1139214183436)

否

否

状态栏应用图标的左键业务弹窗相关信息。

statusBarGroupMenu

[StatusBarGroupMenu](#section8291353172219)[]

否

是

状态栏图标的右键分组菜单相关信息。

默认值：undefined

 说明：

当前所有分组下一级菜单项的总和不可超过20个。

hoverTips

string

否

是

状态栏图标hover时的显示信息。

取值范围：1~128。

 说明：

**起始版本：**6.0.2(22)

如不配置该参数，则hover时显示内容默认取值为[statusBarManager.QuickOperation](#section1139214183436)中配置模块的[label](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-hapmoduleinfo#hapmoduleinfo-1)。

#### statusBarManager.StatusBarIcon

状态栏图标的图片信息。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.0(12)

**名称**

**类型**

**只读**

可选

**说明**

white

[image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

否

否

深色壁纸下展示的图标，建议采用纯白色图标，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。

 说明：

建议使用24[vp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units) * 24vp的图片。

black

[image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

否

否

浅色壁纸下展示的图标，建议采用纯黑色图标，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。

 说明：

建议使用24vp * 24vp的图片。

#### statusBarManager.QuickOperation

状态栏图标左键业务弹窗的详细信息。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.0(12)

**名称**

**类型**

**只读**

可选

**说明**

title

string

否

否

状态栏图标的左键业务弹窗的标题。

取值范围：无限制，超长显示省略号。

height

number

否

否

状态栏图标的左键业务弹窗的自定义区域高度，单位：vp。

取值范围：大于0。

abilityName

string

否

否

状态栏图标左键业务弹窗的应用定制区域对应的自定义[StatusBarViewExtensionAbility](StatusBarViewExtensionAbility（状态栏扩展Ability）.md)的名称。

 说明：

当传空字符串时，支持通过监听[statusBarIconClick](#section18493519506)事件处理点击业务。

moduleName

string

否

是

状态栏图标左键业务弹窗的应用定制区域对应的自定义[StatusBarViewExtensionAbility](StatusBarViewExtensionAbility（状态栏扩展Ability）.md)所在的模块名称。

默认值：''

loadingStatus

boolean

否

是

点击状态栏图标展开二级菜单场景下是否加载动效。

默认值：false

 说明：

**起始版本：**6.0.0(20)

#### statusBarManager.StatusBarGroupMenu

type StatusBarGroupMenu = StatusBarMenuItem[]

状态栏图标右键菜单的分组菜单信息。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.0(12)

类型

**说明**

[StatusBarMenuItem](#section3627115133810)[]

菜单组的信息，可以包含多个一级菜单项。

#### statusBarManager.StatusBarMenuItem

状态栏图标右键菜单的一级菜单项信息。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.0(12)

**名称**

**类型**

**只读**

可选

**说明**

title

string

否

否

菜单项标题。

取值范围：无限制，超长显示省略号。

menuAction

[StatusBarMenuAction](#section1196811528487)

否

是

菜单项行为信息。

默认值：undefined

 说明：

当前菜单行为仅支持打开应用内定义的UIAbility，且menuAction和subMenu两个参数不可同时缺省。

subMenu

[StatusBarSubMenuItem](#section18651641195110)[]

否

是

一级菜单项的子菜单项。

默认值：undefined

 说明：

当前单个一级菜单项最多支持20个子菜单项。

#### statusBarManager.StatusBarMenuAction

状态栏图标右键菜单的菜单项点击行为信息。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.0(12)

**名称**

**类型**

**只读**

可选

**说明**

abilityName

string

否

否

点击菜单项拉起的应用的Ability名称。

 说明：

当前仅支持拉起UIAbility。

moduleName

string

否

是

点击菜单项拉起的应用的Ability所在的模块名称。

默认值：''

notifyOnly

boolean

否

是

图标右键菜单点击事件使能。

取值范围：

false：不使能，此时点击右键菜单无事件通知

true：使能，此时点击右键菜单有事件通知

默认值：false - 无右键菜单点击事件触发

 说明：

当使能和提供菜单menuCode时，支持通过监听[rightMenuClick](#section10893144462716)事件处理图标右键菜单点击业务。

**起始版本：**5.0.2(14)

menuCode

string

否

是

图标右键菜单唯一标识。

默认值：''

 说明：

需保证菜单标识的唯一性，用于区分不同菜单项。

**起始版本：**5.0.2(14)

#### statusBarManager.StatusBarSubMenuItem

状态栏图标的右键菜单的二级菜单项信息

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.0(12)

**名称**

**类型**

**只读**

可选

**说明**

subTitle

string

否

否

二级菜单项标题。

取值范围：无限制，超长显示省略号。

menuAction

[StatusBarMenuAction](#section1196811528487)

否

否

菜单项行为信息。

 说明：

当前菜单行为仅支持打开应用内定义的UIAbility。

#### statusBarManager.addToStatusBar

addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void

应用接入状态栏方法，当前同一个应用仅支持添加一个图标，重复添加无效。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#context)

是

上下文信息。

 说明：

当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。

statusBarItem

[StatusBarItem](#section105181855219)

是

应用自定义接入状态栏的图标的详细信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

401

The parameter check failed.

1010710001

The size of the pixelmap exceeds the limit.

1010710002

The number of menu items or submenu items exceeds the limit.

1010710003

The API is being called too frequently.

1010710005

The string length exceeds the threshold.

1010720001

A menu item contains neither submenu nor menuAction.

**示例：**

```ets
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function addToStatusBar(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // 构建图标信息
  let icon: statusBarManager.StatusBarIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }

  // 构建右键菜单项内容
  let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
  let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
    abilityName: "EntryAbility"
  }
  let subMenu: statusBarManager.StatusBarSubMenuItem = {
    subTitle: "子菜单项",
    menuAction: subMenuItemAction
  }
  subMenus.push(subMenu);

  let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
  let menuItem: statusBarManager.StatusBarMenuItem = {
    title: "一级菜单项",
    // 一级menuAction和subMenu两项不可都缺省
    subMenu: subMenus
  };
  statusBarMenuItems.push(menuItem);

  let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
  statusBarGroupMenus.push(statusBarMenuItems);

  // 构建左键业务弹窗信息
  let operation: statusBarManager.QuickOperation = {
    abilityName: "MyStatusBarViewAbility",
    title: "测试Demo",
    height: 300,
    // 可缺省
    moduleName: 'entry'
  };

  // 构建添加到状态栏的图标详细信息
  let item: statusBarManager.StatusBarItem = {
    icons: icon,
    quickOperation: operation,
    statusBarGroupMenu: statusBarGroupMenus
  };

  try {
    statusBarManager.addToStatusBar(context, item);
  } catch (error) {
    console.error(`addToStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### statusBarManager.addToStatusBar

addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback<void>): void

应用接入状态栏方法，使用callback异步回调，当前同一个应用仅支持添加一个图标，重复添加无效。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.2(14)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#context)

是

上下文信息。

 说明：

当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。

statusBarItem

[StatusBarItem](#section105181855219)

是

应用自定义接入状态栏的图标的详细信息。

callback

AsyncCallback<void>

是

表示应用添加图标到状态栏回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

401

The parameter check failed.

1010710001

The size of the pixelmap exceeds the limit.

1010710002

The number of menu items or submenu items exceeds the limit.

1010710003

The API is being called too frequently.

1010710005

The string length exceeds the threshold.

1010720001

A menu item contains neither submenu nor menuAction.

**示例：**

```ets
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function addToStatusBar(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // 构建图标信息
  let icon: statusBarManager.StatusBarIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }

  // 构建右键菜单项内容
  let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
  let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
    abilityName: "EntryAbility"
  }
  let subMenu: statusBarManager.StatusBarSubMenuItem = {
    subTitle: "子菜单项",
    menuAction: subMenuItemAction
  }
  subMenus.push(subMenu);

  let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
  let menuItem: statusBarManager.StatusBarMenuItem = {
    title: "一级菜单项",
    // 一级menuAction和subMenu两项不可都缺省
    subMenu: subMenus
  };
  statusBarMenuItems.push(menuItem);

  let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
  statusBarGroupMenus.push(statusBarMenuItems);

  // 构建左键业务弹窗信息
  let operation: statusBarManager.QuickOperation = {
    abilityName: "MyStatusBarViewAbility",
    title: "测试Demo",
    height: 300,
    // 可缺省
    moduleName: 'entry'
  };

  // 构建添加到状态栏的图标详细信息
  let item: statusBarManager.StatusBarItem = {
    icons: icon,
    quickOperation: operation,
    statusBarGroupMenu: statusBarGroupMenus
  };

  try {
    statusBarManager.addToStatusBar(context, item, (error: BusinessError) => {
      if (error) {
        // ...
        return;
      }
      console.info('addToStatusBar success');
    });
  } catch (error) {
    console.error(`addToStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### statusBarManager.removeFromStatusBar

removeFromStatusBar(context: common.Context): void

应用移除状态栏对应图标方法。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#context)

是

上下文信息

 说明：

当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

401

The parameter check failed.

1010710003

The API is being called too frequently.

1010710004

The icon cannot be deleted when no window is in the foreground.

**示例：**

```ets
import { statusBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
function removeFromStatusBar(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  try {
    statusBarManager.removeFromStatusBar(context);
  } catch (error) {
    console.error(`removeFromStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### statusBarManager.removeFromStatusBar

removeFromStatusBar(context: common.Context, callback: AsyncCallback<void>): void

应用移除状态栏对应图标方法，使用callback异步回调。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.2(14)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#context)

是

上下文信息

 说明：

当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。

callback

AsyncCallback<void>

是

表示应用移除状态栏图标回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

401

The parameter check failed.

1010710003

The API is being called too frequently.

1010710004

The icon cannot be deleted when no window is in the foreground.

**示例：**

```ets
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { BusinessError } from '@kit.BasicServicesKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
function removeFromStatusBar(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  try {
    statusBarManager.removeFromStatusBar(context, (error: BusinessError) => {
      if (error) {
        // ...
        return;
      }
      console.info('removeFromStatusBar success');
    });
  } catch (error) {
    console.error(`removeFromStatusBar failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### statusBarManager.updateQuickOperationHeight

updateQuickOperationHeight(context: common.Context, height: number): void

应用更新状态栏图标的左键弹窗应用定制区域高度。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#context)

是

上下文信息。

 说明：

当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。

height

number

是

状态栏图标左键的应用面板自定义区域高度，单位：vp。

取值范围：大于0。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

401

The parameter check failed.

1010710003

The API is being called too frequently.

**示例：**

```ets
import { statusBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
function updateQuickOperationHeight(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  let height = 200;
  try {
    statusBarManager.updateQuickOperationHeight(context, height);
  } catch (error) {
    console.error(`updateQuickOperationHeight failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### statusBarManager.updateQuickOperationHeight

updateQuickOperationHeight(context: common.Context, height: number, callback: AsyncCallback<void>): void

应用更新状态栏图标的左键弹窗应用定制区域高度，使用callback异步回调。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.2(14)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#context)

是

上下文信息。

 说明：

当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。

height

number

是

状态栏图标左键的应用面板自定义区域高度，单位：vp。

取值范围：大于0。

callback

AsyncCallback<void>

是

表示应用更新状态栏图标的左键弹窗应用定制区域高度回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

401

The parameter check failed.

1010710003

The API is being called too frequently.

**示例：**

```ets
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { BusinessError } from '@kit.BasicServicesKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
function updateQuickOperationHeight(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  let height = 200;
  try {
    statusBarManager.updateQuickOperationHeight(context, height, (error) => {
      if (error) {
        // ...
        return;
      }
      console.info('updateQuickOperationHeight success');
    });
  } catch (error) {
    console.error(`updateQuickOperationHeight failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### statusBarManager.updateStatusBarMenu

updateStatusBarMenu(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu[]): void

应用更新状态栏图标的右键菜单内容。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#context)

是

上下文信息。

 说明：

当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。

statusBarGroupMenus

[StatusBarGroupMenu](#section8291353172219)[]

是

更新后的应用右键菜单栏相关信息。

 说明：

当前所有分组下一级菜单项的总和不可超过20个。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

401

The parameter check failed.

1010710002

The number of menu items or submenu items exceeds the limit.

1010710003

The API is being called too frequently.

1010720001

A menu item contains neither submenu nor menuAction.

**示例：**

```ets
import { statusBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
function updateStatusBarMenu(context: Context) {
  // 构建右键菜单项内容
  let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
  let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
    abilityName: "EntryAbility"
  }
  let subMenu: statusBarManager.StatusBarSubMenuItem = {
    subTitle: "二级菜单项",
    menuAction: subMenuItemAction
  }
  subMenus.push(subMenu);
  let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
  let menuItem: statusBarManager.StatusBarMenuItem = {
    title: "一级菜单项",
    // 一级menuAction和subMenu两项不可都缺省
    subMenu: subMenus
  };
  statusBarMenuItems.push(menuItem);
  let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
  statusBarGroupMenus.push(statusBarMenuItems);
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  try {
    statusBarManager.updateStatusBarMenu(context, statusBarGroupMenus);
  } catch (error) {
    console.error(`updateStatusBarMenu failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### statusBarManager.updateStatusBarMenu

updateStatusBarMenu(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu[], callback: AsyncCallback<void>): void

应用更新状态栏图标的右键菜单内容，使用callback异步回调。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.2(14)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#context)

是

上下文信息。

 说明：

当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。

statusBarGroupMenus

[StatusBarGroupMenu](#section8291353172219)[]

是

更新后的应用右键菜单栏相关信息。

 说明：

当前所有分组下一级菜单项的总和不可超过20个。

callback

AsyncCallback<void>

是

表示应用更新状态栏图标的右键菜单内容回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

401

The parameter check failed.

1010710002

The number of menu items or submenu items exceeds the limit.

1010710003

The API is being called too frequently.

1010720001

A menu item contains neither submenu nor menuAction.

**示例：**

```ets
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { BusinessError } from '@kit.BasicServicesKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
function updateStatusBarMenu(context: Context) {
  // 构建右键菜单项内容
  let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = [];
  let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
    abilityName: "EntryAbility"
  }
  let subMenu: statusBarManager.StatusBarSubMenuItem = {
    subTitle: "二级菜单项",
    menuAction: subMenuItemAction
  }
  subMenus.push(subMenu);
  let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = [];
  let menuItem: statusBarManager.StatusBarMenuItem = {
    title: "一级菜单项",
    // 一级menuAction和subMenu两项不可都缺省
    subMenu: subMenus
  };
  statusBarMenuItems.push(menuItem);
  let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = [];
  statusBarGroupMenus.push(statusBarMenuItems);
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  try {
    statusBarManager.updateStatusBarMenu(context, statusBarGroupMenus, (err: BusinessError) => {
      if (err) {
        // ...
        return;
      }
      console.info('updateStatusBarMenu success');
    });
  } catch (error) {
    console.error(`updateStatusBarMenu failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### statusBarManager.updateStatusBarIcon

updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon): void

应用更新接入状态栏的图标。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#context)

是

上下文信息。

 说明：

当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。

statusBarIcon

[StatusBarIcon](#section1844717231113)

是

更新的图标。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

401

The parameter check failed.

1010710001

The size of the pixelmap exceeds the limit.

1010710003

The API is being called too frequently.

**示例：**

```ets
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateStatusBarIcon(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // 构建图标信息
  let icons: statusBarManager.StatusBarIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }

  try {
    statusBarManager.updateStatusBarIcon(context, icons);
  } catch (error) {
    console.error(`updateStatusBarIcon failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### statusBarManager.updateStatusBarIcon

updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon, callback: AsyncCallback<void>): void

应用更新接入状态栏的图标，使用callback异步回调。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.2(14)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#context)

是

上下文信息。

 说明：

当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。

statusBarIcon

[StatusBarIcon](#section1844717231113)

是

更新的图标。

callback

AsyncCallback<void>

是

表示应用更新接入状态栏的图标回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

401

The parameter check failed.

1010710001

The size of the pixelmap exceeds the limit.

1010710003

The API is being called too frequently.

**示例：**

```ets
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateStatusBarIcon(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

  // 创建white pixelMap，需在资源rawfile文件夹中预置testWhite.png图片，图片大小为24vp * 24vp
  const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
  const whiteBuffer = whiteFileData.buffer;
  const whiteImageSource = image.createImageSource(whiteBuffer);
  let whitePixelMap = await whiteImageSource.createPixelMap();

  // 创建black pixelMap，需在资源rawfile文件夹中预置testBlack.png图片，图片大小为24vp * 24vp
  const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
  const blackBuffer = blackFileData.buffer;
  const blackImageSource = image.createImageSource(blackBuffer);
  let blackPixelMap = await blackImageSource.createPixelMap();

  // 构建图标信息
  let icons: statusBarManager.StatusBarIcon = {
    white: whitePixelMap,
    black: blackPixelMap
  }

  try {
    statusBarManager.updateStatusBarIcon(context, icons, (error: BusinessError) => {
      if (error) {
        // ...
        return;
      }
      console.info('updateStatusBarIcon success');
    });
  } catch (error) {
    console.error(`updateStatusBarIcon failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### statusBarManager.on('statusBarIconClick')

on(type: 'statusBarIconClick', callback: Callback<emitter.EventData>): void

监听状态栏图标点击事件。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.2(14)

**参数：**

参数名

类型

必填

说明

type

string

是

事件回调类型，支持的事件为'statusBarIconClick'，当点击应用图标时，触发该事件。

 说明：

当调用[addToStatusBar](#section665018220561)，入参[quickOperation](#section1139214183436)未指定abilityName时，支持通过监听statusBarIconClick事件处理点击业务。

callback

Callback<[emitter.EventData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter#eventdata)>

是

需要注册的回调函数，返回信息为图标点击相关信息。

 说明：

当前返回信息：

- iconClickType：点击事件类型，当前仅支持左键(leftClick)。

**示例：**

```ets
private onStatusBarIconClick = (eventData: emitter.EventData) => {
  // 自定义图标点击业务
  let data = eventData.data;
  if (data) {
    switch (data['iconClickType']) {
      case 'leftClickType':
        // 自定义左键点击业务
        break;
      default:
        break;
    }
  }
}

// 监听状态栏图标点击事件
statusBarManager.on('statusBarIconClick', this.onStatusBarIconClick);
```

#### statusBarManager.off('statusBarIconClick')

off(type: 'statusBarIconClick', callback?: Callback<emitter.EventData>): void

注销状态栏图标点击事件。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.2(14)

**参数：**

参数名

类型

必填

说明

type

string

是

取消事件回调类型，支持的事件为'statusBarIconClick'

callback

Callback<[emitter.EventData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter#eventdata)>

否

取消该事件的回调处理函数。

默认值：undefined

 说明：

若不传入callback，会取消该事件的所有回调函数

若传入callback，需要传入对应on方法相同的对象，否则会导致回调函数未成功注销，导致内存泄露。

**示例：**

```ets
private onStatusBarIconClick = (eventData: emitter.EventData) => {
  // 自定义图标点击业务
  let data = eventData.data;
  if (data) {
    switch (data['iconClickType']) {
      case 'leftClickType':
        // 自定义左键点击业务
        break;
      default:
        break;
    }
  }
}
// 取消事件回调处理函数
statusBarManager.off('statusBarIconClick', this.onStatusBarIconClick);

// 注销事件监听
statusBarManager.off('statusBarIconClick');
```

#### statusBarManager.on('rightMenuClick')

on(type: 'rightMenuClick', callback: Callback<emitter.EventData>): void

监听状态栏图标右键菜单点击事件。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.2(14)

**参数：**

参数名

类型

必填

说明

type

string

是

事件回调类型，支持的事件为'rightMenuClick'，当点击应用图标右键菜单时，触发该事件。

 说明：

当调用[updateStatusBarMenu](#section188071452172811)，添加菜单项时，指定[menuAction](#section1196811528487)的notifyOnly使能和菜单项menuCode时生效。

callback

Callback<[emitter.EventData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter#eventdata)>

是

需要注册的回调函数，返回信息为图标右键菜单点击相关信息。

 说明：

当前返回信息：

- menuCode：点击菜单项唯一标识。

**示例：**

```ets
private onRightMenuClick = (eventData: emitter.EventData) => {
  // 自定义图标右键菜单点击业务
  let data = eventData.data;
  if (data) {
    let menuCode = data['menuCode'] as string;
    // 处理点击菜单项业务
  }
}

// 监听右键菜单点击事件
statusBarManager.on('rightMenuClick', this.onRightMenuClick);
```

#### statusBarManager.off('rightMenuClick')

off(type: 'rightMenuClick', callback?: Callback<emitter.EventData>): void

注销状态栏图标右键菜单点击事件。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**5.0.2(14)

**参数：**

参数名

类型

必填

说明

type

string

是

取消事件回调类型，支持的事件为'rightMenuClick'。

callback

Callback<[emitter.EventData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter#eventdata)>

否

取消该事件的回调处理函数。

默认值：undefined

 说明：

若不传入callback，会取消该事件的所有回调函数

若传入callback，需要传入对应on方法相同的对象，否则会导致回调函数未成功注销，导致内存泄露。

**示例：**

```ets
private onRightMenuClick = (eventData: emitter.EventData) => {
  // 自定义图标右键菜单点击业务
  let data = eventData.data;
  if (data) {
    let menuCode = data['menuCode'] as string;
    // 处理点击菜单项业务
  }
}

// 取消事件回调处理函数
statusBarManager.off('rightMenuClick', this.onRightMenuClick);

// 注销事件监听
statusBarManager.off('rightMenuClick');
```

#### statusBarManager.updateStatusBarHoverTips

updateStatusBarHoverTips(context: common.Context, hoverTips: string): Promise<void>

更新状态栏图标hover时显示内容。

**系统能力：**SystemCapability.PCService.StatusBarManager

**起始版本：**6.0.2(22)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#context)

是

上下文信息。

 说明：

当前context仅支持传入Context的子类UIAbilityContext、ServiceExtensionContext、FormExtensionContext。

hoverTips

string

是

状态栏图标hover时的显示信息。

字符串长度范围：1~128。

**返回值：**

参数名

说明

Promise<void>

Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

1010710003

The API is being called too frequently.

1010710005

The string length exceeds the threshold.

**示例：**

```ets
import { statusBarManager } from '@kit.DeskTopExtensionKit';
import { BusinessError } from '@kit.BasicServicesKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
function  updateStatusBarHoverTips(context: Context) {
  if (!context) {
    console.error('getHostContext failed');
    return;
  }
  let hoverTips: string = 'hoverTips';
  try {
    await statusBarManager.updateStatusBarHoverTips(context, hoverTips);
  } catch (error) {
    console.error(`updateStatusBarHoverTips failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```
