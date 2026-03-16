# quickBarManager（快捷栏管理服务）

本模块为应用提供接入快捷栏能力。应用可以通过接入相应的API，可自定义应用在快捷栏右键菜单。

**起始版本：**6.0.2(22)

#### 导入模块

```ets
import { quickBarManager } from '@kit.DeskTopExtensionKit';
```

#### quickBarManager.QuickTaskInfo

快捷栏菜单任务的详细参数。

**系统能力：**SystemCapability.PCService.QuickBarManager

**起始版本：**6.0.2(22)

**名称**

**类型**

**只读**

可选

**说明**

taskName

string

否

否

快捷栏图标菜单任务的任务名称。

字符串长度范围：1~512。

abilityName

string

否

否

点击菜单任务拉起的应用的Ability名称。

字符串长度范围：1~512。

moduleName

string

否

是

点击菜单项任务拉起的应用的Ability所在的模块名称。

字符串长度范围：1~512。

默认值：''

taskIcon

[image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

否

是

快捷栏图标菜单任务的图片信息，支持JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG等图片类型。

默认值：undefined

 说明：

建议使用512vp * 512vp大小的图片，若不传入图片信息，则使用应用图标作为任务图标。

taskDetail

string

否

是

快捷栏图标菜单任务的描述信息。

默认值：''

parameters

[ParameterItem](#section1217412444191)[]

否

是

快捷栏图标菜单任务的自定义参数。

数组大小范围：小于等于64。

默认值：undefined

#### quickBarManager.QuickTask

应用的快捷栏菜单任务的信息。

**系统能力：**SystemCapability.PCService.QuickBarManager

**起始版本：**6.0.2(22)

**名称**

**类型**

**只读**

可选

**说明**

taskId

number

是

否

快捷栏图标菜单任务的任务Id。

categoryId

number

是

否

快捷栏图标菜单分组的分组Id。

taskInfo

[QuickTaskInfo](#section105181855219)

否

否

接入快捷栏的任务信息。

#### quickBarManager.ParameterItem

快捷栏菜单任务的自定义参数，表示WantParams，由开发者自行决定传入的键值对。

**系统能力：**SystemCapability.PCService.QuickBarManager

**起始版本：**6.0.2(22)

**名称**

**类型**

**只读**

可选

**说明**

key

string

否

否

自定义参数的key值。

字符串长度范围：1~512。

value

string

否

否

自定义参数的value值。

字符串长度范围：1~512。

#### quickBarManager.CustomCategory

应用的快捷栏菜单分组的信息。

**系统能力：**SystemCapability.PCService.QuickBarManager

**起始版本：**6.0.2(22)

**名称**

**类型**

**只读**

可选

**说明**

categoryId

number

是

否

快捷栏图标菜单分组的分组Id。

categoryName

string

否

否

快捷栏图标菜单分组的分组名称。

字符串长度范围：1~512。

#### quickBarManager.addCustomCategory

addCustomCategory(context: common.Context, categoryName: string): Promise<CustomCategory>

应用接入快捷栏方法，应用可通过addCustomCategory接口添加快捷栏分组。添加一个分组后才可以往分组里添加任务，最多可以添加三个分组。

**系统能力：**SystemCapability.PCService.QuickBarManager

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

categoryName

string

是

快捷栏图标菜单分组的分组名称。

字符串长度范围：1~512。

**返回值：**

参数名

说明

Promise<[CustomCategory](#section19779819185015)>

Promise对象，返回菜单分组信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

1020210001

Maximum number of categories reached

1020210002

Duplicate category name.

1020210008

The string length exceeds the threshold

**示例：**

```ets
import { quickBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function addCustomCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    const res = await quickBarManager.addCustomCategory(context, '最近任务');
    console.info(`customCategory info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`addCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### quickBarManager.addQuickTask

addQuickTask(context: common.Context, categoryId: number, taskInfo: QuickTaskInfo): Promise<QuickTask>

应用接入快捷栏方法，应用可通过addQuickTask接口添加快捷栏任务。打开应用图标在快捷栏的右键菜单，即可看到添加后对应的菜单项。

**系统能力：**SystemCapability.PCService.QuickBarManager

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

categoryId

number

是

快捷栏图标菜单分组的分组Id。

taskInfo

[QuickTaskInfo](#section105181855219)

是

快捷栏图标菜单任务的详细信息。

**返回值：**

参数名

说明

Promise<[QuickTask](#section16180063819)>

Promise对象，返回菜单任务信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

1020210003

Category not found.

1020210008

The string length exceeds the threshold

1020210009

Invalid parameter.

**示例：**

```ets
import { quickBarManager } from '@kit.DeskTopExtensionKit';
import { resourceManager } from '@kit.LocalizationKit';
import { image } from '@kit.ImageKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function addQuickTask(context: Context) {
  if (context === undefined) {
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 创建任务的pixelMap，需在资源rawfile文件夹中预置testImage.png图片
  const whiteFileData = resourceMgr.getRawFileContentSync('testImage.png');
  const whiteImageSource = image.createImageSource(whiteFileData.buffer);
  const imagePixelMap = await whiteImageSource.createPixelMap();
  // 构建parameters信息
  let parameters: quickBarManager.ParameterItem = {
    key: 'testKey',
    value: 'testValue'
  }
  // 构建QuickTaskInfo信息
  let task: quickBarManager.QuickTaskInfo = {
    taskName: '测试任务名称',
    abilityName: 'TestAbility1',
    moduleName: 'entry',
    // 参数可选
    taskIcon: imagePixelMap,
    // 参数可选
    taskDetail: '任务的描述',
    parameters: [parameters]
  }
  try {
    // 获取所有的分组信息，将任务添加到想要的分组中
    const categoryList = await quickBarManager.getCustomCategories(context);
    // 选择添加任务到第一个分组中
    let res = await quickBarManager.addQuickTask(context, categoryList[0].categoryId, task);
    console.info(`quickTask info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`addQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### quickBarManager.getCustomCategories

getCustomCategories(context: common.Context): Promise<CustomCategory[]>

应用接入快捷栏方法，应用可通过getCustomCategories接口获取在快捷栏定义的所有分组。

**系统能力：**SystemCapability.PCService.QuickBarManager

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

**返回值：**

参数名

说明

Promise<[CustomCategory](#section19779819185015)[]>

Promise对象，返回所有菜单分组信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

1020210003

Category not found.

**示例：**

```ets
import { quickBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function getCustomCategories(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    const res = await quickBarManager.getCustomCategories(context);
    console.info(`customCategoryList info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`getCustomCategories failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### quickBarManager.getTasksFromCategory

getTasksFromCategory(context: common.Context, categoryId: number): Promise<QuickTask[]>

应用接入快捷栏方法，应用可通过getTasksFromCategory接口获取某个快捷栏分组下的所有任务信息。

**系统能力：**SystemCapability.PCService.QuickBarManager

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

categoryId

number

是

快捷栏图标菜单分组的分组Id。

**返回值：**

参数名

说明

Promise<[QuickTask](#section16180063819)[]>

Promise对象，返回一个分组下的所有任务信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

1020210003

Category not found.

1020210004

Quick task not found.

**示例：**

```ets
import { quickBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function getTasksFromCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // 获取所有的分组信息，用于获取分组下所有的任务
    const category = await quickBarManager.getCustomCategories(context);
    // 选择获取第一个分组下的所有任务
    const res = await quickBarManager.getTasksFromCategory(context, category[0].categoryId)
    console.info(`quickTaskList info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`getTasksFromCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### quickBarManager.updateCustomCategory

updateCustomCategory(context: common.Context, category: CustomCategory): Promise<void>

应用接入快捷栏方法，应用可通过updateCustomCategory接口更新快捷栏分组。

**系统能力：**SystemCapability.PCService.QuickBarManager

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

category

[CustomCategory](#section19779819185015)

是

快捷栏图标的菜单分组信息。

**返回值：**

参数名

说明

Promise<void>

Promise对象，无返回值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

1020210002

Duplicate category name.

1020210003

Category not found.

1020210008

The string length exceeds the threshold

**示例：**

```ets
import { quickBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateCustomCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  const category: quickBarManager.CustomCategory = {
    categoryId: 1,
    categoryName: 'demo'
  }
  try {
    await quickBarManager.updateCustomCategory(context, category);
  } catch (error) {
    console.error(`updateCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### quickBarManager.updateQuickTask

updateQuickTask(context: common.Context, task: QuickTask): Promise<void>

应用接入快捷栏方法，应用可通过updateQuickTask接口更新快捷栏任务。

**系统能力：**SystemCapability.PCService.QuickBarManager

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

task

[QuickTask](#section16180063819)

是

快捷栏图标的菜单任务信息。

**返回值：**

参数名

说明

Promise<void>

Promise对象，无返回值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

1020210004

Quick task not found.

1020210008

The string length exceeds the threshold

1020210009

Invalid parameter.

**示例：**

```ets
import { quickBarManager } from '@kit.DeskTopExtensionKit';
import { resourceManager } from '@kit.LocalizationKit';
import { image } from '@kit.ImageKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateQuickTask(context: Context) {
  if (context === undefined) {
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 创建任务的pixelMap，需在资源rawfile文件夹中预置testUpdateImage.png图片
  const fileData = resourceMgr.getRawFileContentSync('testUpdateImage.png');
  const imageSource = image.createImageSource(fileData.buffer);
  const imagePixelMap = await imageSource.createPixelMap();
  // 构建parameters
  let parameters: quickBarManager.ParameterItem = {
    key: 'testKey',
    value: 'testValue'
  }
  let taskInfo: quickBarManager.QuickTaskInfo = {
    taskName: 'newTaskName',
    abilityName: 'newEntryAbility',
    moduleName: 'newModuleName',
    // 参数可选
    taskIcon: imagePixelMap,
    // 参数可选
    taskDetail: '任务的描述',
    // 参数可选
    parameters: [parameters]
  }

  const task: quickBarManager.QuickTask = {
    taskId: 1,
    categoryId: 1,
    taskInfo: taskInfo
  }

  try {
    await quickBarManager.updateQuickTask(context,task);
  } catch (error) {
    console.error(`updateQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### quickBarManager.deleteQuickTask

deleteQuickTask(context: common.Context, taskId: number): Promise<void>

应用接入快捷栏方法，应用可通过deleteQuickTask接口删除快捷栏任务。

**系统能力：**SystemCapability.PCService.QuickBarManager

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

taskId

number

是

快捷栏图标的菜单任务的Id。

**返回值：**

参数名

说明

Promise<void>

Promise对象，无返回值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

1020210004

Quick task not found.

**示例：**

```ets
import { quickBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function deleteQuickTask(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // 删除任务id为1的任务
    await quickBarManager.deleteQuickTask(context, 1);
  } catch (error) {
    console.error(`deleteQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

#### quickBarManager.deleteCustomCategory

deleteCustomCategory(context: common.Context, categoryId: number): Promise<void>

应用接入快捷栏方法，应用可通过deleteCustomCategory接口删除快捷栏分组，其下的所有任务也会随着一起删除。

**系统能力：**SystemCapability.PCService.QuickBarManager

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

taskId

number

是

快捷栏图标的菜单任务的Id。

**返回值：**

参数名

说明

Promise<void>

Promise对象，无返回值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ArkTS API错误码](../../errors/ArkTS API错误码 (statusbar-extension-error-code).md)。

错误码ID

错误信息

1020210003

Category not found.

**示例：**

```ets
import { quickBarManager } from '@kit.DeskTopExtensionKit';

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function deleteCustomCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // 删除分组id为1的分组
    await quickBarManager.deleteCustomCategory(context, 1);
  } catch (error) {
    console.error(`deleteCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```
