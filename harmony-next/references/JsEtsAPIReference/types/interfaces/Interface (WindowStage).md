# Interface (WindowStage)

-

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Interface首批接口从API version 9开始支持。

-

针对系统能力SystemCapability.Window.SessionManager，请先使用[canIUse()](SysCap (系统能力).md#ZH-CN_TOPIC_0000002553202569__caniuse)接口判断当前设备是否支持此syscap及对应接口。

窗口管理器。管理各个基本窗口单元，即[Window](Interface (Window).md)实例。

下列API示例中都需在[onWindowStageCreate()](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002522240540__onwindowstagecreate)函数中使用WindowStage的实例调用对应方法。

#### 导入模块

```ets
import { window } from '@kit.ArkUI';
```

#### getMainWindow9+

getMainWindow(callback: AsyncCallback<Window>): void

获取该WindowStage实例下的主窗口，使用callback异步回调。

调用该接口前，建议先通过[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)方法或者[setUIContent](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__setuicontent9-1)方法完成页面加载。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Window> | 是 | 回调函数。返回当前WindowStage下的主窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码]([窗口错误码](../../errors/窗口错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300005 | This window stage is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error('Failed to load the content. Cause:' + JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
      let windowClass: window.Window | undefined = undefined;
      windowStage.getMainWindow((err: BusinessError, data) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to obtain the main window. Cause code: ${errCode}, message: ${err.message}`);
          return;
        }
        windowClass = data;
        console.info(`Succeeded in obtaining the main window. Data: ${JSON.stringify(data)}`);
      });
  }
};
```

#### getMainWindow9+

getMainWindow(): Promise<Window>

获取该WindowStage实例下的主窗口，使用Promise异步回调。

调用该接口前，建议先通过[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)方法或者[setUIContent](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__setuicontent9-1)方法完成页面加载。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Window> | Promise对象。返回当前WindowStage下的主窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300005 | This window stage is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error('Failed to load the content. Cause:' + JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
      let windowClass: window.Window | undefined = undefined;
      let promise = windowStage.getMainWindow();
      promise.then((data) => {
        windowClass = data;
        console.info('Succeeded in obtaining the main window.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
      });
  }
};
```

#### getMainWindowSync9+

getMainWindowSync(): Window

获取该WindowStage实例下的主窗口，该接口为同步调用。

调用该接口前，建议先通过[loadContent](Interface (WindowStage).md#ZH-CN_TOPIC_0000002553360677__loadcontent9)方法或者[setUIContent](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__setuicontent9-1)方法完成页面加载。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Window | 返回当前WindowStage下的主窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300005 | This window stage is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        console.error('Failed to load the content. Cause:' + JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
      try {
        let windowClass = windowStage.getMainWindowSync();
      } catch (exception) {
        console.error(`Failed to obtain the main window. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
};
```

#### createSubWindow9+

createSubWindow(name: string, callback: AsyncCallback<Window>): void

创建该WindowStage实例下的子窗口，使用callback异步回调。

子窗口创建后默认是[沉浸式布局](../../guides/窗口开发术语.md#沉浸式布局)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 子窗口的名字。 |
| callback | AsyncCallback<Window> | 是 | 回调函数。返回当前WindowStage下的子窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The subWindow has been created and can not be created again. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    try {
      windowStage.createSubWindow('mySubWindow', (err: BusinessError, data) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to create the subwindow. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        windowClass = data;
        console.info(`Succeeded in creating the subwindow. Data: ${JSON.stringify(data)}`);
        if (!windowClass) {
          console.info('Failed to load the content. Cause: windowClass is null');
        }
        else {
          windowClass.resize(500, 1000);
        }
      });
    } catch (exception) {
      console.error(`Failed to create the subwindow. Cause code: ${exception.code}, message: ${exception.message}`);
    }
};
```

#### createSubWindow9+

createSubWindow(name: string): Promise<Window>

创建该WindowStage实例下的子窗口，使用Promise异步回调。

子窗口创建后默认是[沉浸式布局](../../guides/窗口开发术语.md#沉浸式布局)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 子窗口的名字。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Window> | Promise对象。返回当前WindowStage下的子窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The subWindow has been created and can not be created again. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    try {
      let promise = windowStage.createSubWindow('mySubWindow');
      promise.then((data) => {
        windowClass = data;
        console.info(`Succeeded in creating the subwindow. Data: ${JSON.stringify(data)}`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to create the subwindow. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to create the subwindow. Cause code: ${exception.code}, message: ${exception.message}`);
    }
};
```

#### createSubWindowWithOptions11+

createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>

创建该WindowStage实例下的子窗口，使用Promise异步回调。

非[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态下，子窗口创建后默认是[沉浸式布局](../../guides/窗口开发术语.md#沉浸式布局)。

自由窗口状态下，子窗口参数[decorEnabled](Interfaces (其他).md#ZH-CN_TOPIC_0000002522240752__subwindowoptions11)为false时，子窗口创建后为沉浸式布局；子窗口参数decorEnabled为true，子窗口创建后为非沉浸式布局。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 子窗口的名字。 |
| options | SubWindowOptions | 是 | 子窗口参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Window> | Promise对象。返回当前WindowStage下创建的子窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. The subWindow has been created and can not be created again. |
| 1300005 | This window stage is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    try {
      let options : window.SubWindowOptions = {
        title: 'title',
        decorEnabled: true
      };
      let promise = windowStage.createSubWindowWithOptions('mySubWindow', options);
      promise.then((data) => {
        windowClass = data;
        console.info(`Succeeded in creating the subwindow. Data: ${JSON.stringify(data)}`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to create the subwindow. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to create the subwindow. Cause code: ${exception.code}, message: ${exception.message}`);
    }
};
```

#### getSubWindow9+

getSubWindow(callback: AsyncCallback<Array<Window>>): void

获取该WindowStage实例下的所有子窗口，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<Window>> | 是 | 回调函数。返回当前WindowStage下的所有子窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window[] = [];
    windowStage.getSubWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the subwindow. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      console.info(`Succeeded in obtaining the subwindow. Data: ${JSON.stringify(data)}`);
    });
  }
};
```

#### getSubWindow9+

getSubWindow(): Promise<Array<Window>>

获取该WindowStage实例下的所有子窗口，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<Window>> | Promise对象。返回当前WindowStage下的所有子窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    let windowClass: window.Window[] = [];
    let promise = windowStage.getSubWindow();
    promise.then((data) => {
      windowClass = data;
      console.info(`Succeeded in obtaining the subwindow. Data: ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to obtain the subwindow. Cause code: ${err.code}, message: ${err.message}`);
    });
  }
};
```

#### loadContent9+

loadContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void

根据当前工程中指定的页面路径为WindowStage的主窗口加载具体页面内容，通过LocalStorage传递状态属性给加载的页面，使用callback异步回调。

建议在UIAbility启动过程中调用该接口，重复调用将首先销毁旧的页面内容（即UIContent）再加载新页面内容，请谨慎使用。当前UI的执行上下文可能不明确，所以不建议在回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，该路径需添加到工程的main_pages.json文件中。 |
| storage | LocalStorage | 是 | 页面级UI状态存储单元，为加载到窗口的页面内容传递状态属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Invalid path parameter. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  storage: LocalStorage = new LocalStorage();

  onWindowStageCreate(windowStage: window.WindowStage) {
    this.storage.setOrCreate('storageSimpleProp', 121);
    console.info('onWindowStageCreate');
    try {
      windowStage.loadContent('pages/page2', this.storage, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info('Succeeded in loading the content.');
      });
    } catch (exception) {
      console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
    }
};
```

#### loadContent9+

loadContent(path: string, storage?: LocalStorage): Promise<void>

根据当前工程中指定的页面路径为WindowStage的主窗口加载具体页面内容，通过LocalStorage传递状态属性给加载的页面，使用Promise异步回调。

建议在UIAbility启动过程中调用该接口，重复调用将首先销毁旧的页面内容（即UIContent）再加载新页面内容，请谨慎使用。当前UI的执行上下文可能不明确，所以不建议在回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，该路径需添加到工程的main_pages.json文件中。 |
| storage | LocalStorage | 否 | 页面级UI状态存储单元，为加载到窗口的页面内容传递状态属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Invalid path parameter. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  storage: LocalStorage = new LocalStorage();

  onWindowStageCreate(windowStage: window.WindowStage) {
    this.storage.setOrCreate('storageSimpleProp', 121);
    console.info('onWindowStageCreate');
    try {
      let promise = windowStage.loadContent('pages/page2', this.storage);
      promise.then(() => {
        console.info('Succeeded in loading the content.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
    }
    ;
  }
};
```

#### loadContent9+

loadContent(path: string, callback: AsyncCallback<void>): void

根据当前工程中指定的页面路径为WindowStage的主窗口加载具体页面内容，使用callback异步回调。

建议在UIAbility启动过程中调用该接口，重复调用将首先销毁旧的页面内容（即UIContent）再加载新页面内容，请谨慎使用。当前UI的执行上下文可能不明确，所以不建议在回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载到窗口中的页面内容的路径，该路径需添加到工程的main_pages.json文件中。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Invalid path parameter. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    try {
      windowStage.loadContent('pages/page2', (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info('Succeeded in loading the content.');
      });
    } catch (exception) {
      console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
    }
};
```

#### loadContentByName11+

loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void

根据指定路由页面名称为当前WindowStage加载[命名路由](../classes/Class (Router).md)页面，通过LocalStorage传递状态属性至加载页面，使用callback异步回调。

建议在UIAbility启动过程中使用该接口，重复调用该接口将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。当前UI的执行上下文可能不明确，所以不建议在回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 命名路由页面的名称。 |
| storage | LocalStorage | 是 | 页面级UI状态存储单元，为加载到窗口的页面内容传递状态属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import * as Index from '../pages/Index'; // 导入命名路由页面
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  storage: LocalStorage = new LocalStorage();

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    this.storage.setOrCreate('storageSimpleProp', 121);
    try {
      windowStage.loadContentByName(Index.entryName, this.storage, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info('Succeeded in loading the content.');
      });
    } catch (exception) {
      console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
  }
};
```

```ets
// ets/pages/Index.ets
export const entryName : string = 'Index';
@Entry({routeName: entryName, useSharedStorage: true})
@Component
export struct Index {
  @State message: string = 'Hello World'
  @LocalStorageLink('storageSimpleProp') storageSimpleProp: number = 1;
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### loadContentByName11+

loadContentByName(name: string, callback: AsyncCallback<void>): void

根据指定路由页面名称为当前WindowStage加载[命名路由](../classes/Class (Router).md)页面，使用callback异步回调。

建议在UIAbility启动过程中使用该接口，重复调用该接口将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。当前UI的执行上下文可能不明确，所以不建议在回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 命名路由页面的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import * as Index from '../pages/Index'; // 导入命名路由页面
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    try {
      windowStage.loadContentByName(Index.entryName, (err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info('Succeeded in loading the content.');
      });
    } catch (exception) {
      console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
  }
};
```

```ets
// ets/pages/Index.ets
export const entryName : string = 'Index';
@Entry({routeName: entryName})
@Component
export struct Index {
  @State message: string = 'Hello World'
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### loadContentByName11+

loadContentByName(name: string, storage?: LocalStorage): Promise<void>

根据指定路由页面名称为当前WindowStage加载[命名路由](../classes/Class (Router).md)页面，通过LocalStorage传递状态属性至加载页面，使用promise异步回调。

建议在UIAbility启动过程中使用该接口，重复调用该接口将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。当前UI的执行上下文可能不明确，所以不建议在回调函数中做UI相关的操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 命名路由页面的名称。 |
| storage | LocalStorage | 否 | 页面级UI状态存储单元，为加载到窗口的页面内容传递状态属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import * as Index from '../pages/Index'; // 导入命名路由页面
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  storage: LocalStorage = new LocalStorage();

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    this.storage.setOrCreate('storageSimpleProp', 121);
    try {
      let promise = windowStage.loadContentByName(Index.entryName, this.storage);
      promise.then(() => {
        console.info('Succeeded in loading the content.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to load the content. Cause code: ${exception.code}, message: ${exception.message}`);
  }
};
```

```ets
// ets/pages/Index.ets
export const entryName : string = 'Index';
@Entry({routeName: entryName, useSharedStorage: true})
@Component
export struct Index {
  @State message: string = 'Hello World'
  @LocalStorageLink('storageSimpleProp') storageSimpleProp: number = 1;
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### on('windowStageEvent')9+

on(eventType: 'windowStageEvent', callback: Callback<[WindowStageEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstageeventtype9)>): void

开启WindowStage生命周期变化的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | string | 是 | 监听事件，固定为'windowStageEvent'，即WindowStage生命周期变化事件。 |
| callback | Callback<[WindowStageEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstageeventtype9)> | 是 | 回调函数。返回当前的WindowStage生命周期状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1300002 | This window state is abnormal. |
| 1300005 | This window stage is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    try {
      windowStage.on('windowStageEvent', (data) => {
        console.info(`Succeeded in enabling the listener for window stage event changes. Data: ${JSON.stringify(data)}`);
      });
    } catch (exception) {
      console.error(`Failed to enable the listener for window stage event changes. Cause code: ${exception.code}, message: ${exception.message}`);
    }
};
```

#### off('windowStageEvent')9+

off(eventType: 'windowStageEvent', callback?: Callback<[WindowStageEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstageeventtype9)>): void

关闭WindowStage生命周期变化的监听。

用于关闭[on('windowStageEvent')](#ZH-CN_TOPIC_0000002553360677__onwindowstageevent9)接口对WindowStage生命周期变化的监听。

如果没有调用[on('windowStageEvent')](#ZH-CN_TOPIC_0000002553360677__onwindowstageevent9)接口开启监听就关闭，程序正常执行不会抛出异常。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | string | 是 | 监听事件，固定为'windowStageEvent'，即WindowStage生命周期变化事件。 |
| callback | Callback<[WindowStageEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstageeventtype9)> | 否 | 回调函数。返回当前的WindowStage生命周期状态。若传入参数，则关闭该监听。若未传入参数，则关闭所有WindowStage生命周期变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1300002 | This window state is abnormal. |
| 1300005 | This window stage is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    windowStage.loadContent('page/Index', (err) =>{
      if(err.code) {
        console.error('Failed to load the content. Cause:' + JSON.stringify(err));
        return;
      }
      console.info('Succeeded in loading the content.');
      const callback = (windowStageEventType: window.WindowStageEventType) => {
        // ...
      }
      try {
        windowStage.on('windowStageEvent', callback);
      } catch (exception) {
        console.error(`Failed to enable the listener for window stage event changes. Cause code: ${exception.code}, message: ${exception.message}`);
      }
      try {
        windowStage.off('windowStageEvent', callback);
        // 如果通过on开启多个callback进行监听，同时关闭所有监听
        windowStage.off('windowStageEvent');
      } catch (exception) {
        console.error(`Failed to disable the listener for window stage event changes. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
};
```

#### on('windowStageLifecycleEvent')20+

on(eventType: 'windowStageLifecycleEvent', callback: Callback<[WindowStageLifecycleEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstagelifecycleeventtype20)>): void

开启WindowStage生命周期变化的监听。


[on('windowStageEvent')](#ZH-CN_TOPIC_0000002553360677__onwindowstageevent9)与本接口的区别：

1.前者无法保证状态切换间的顺序，对于状态间的顺序有要求的情况下不推荐使用，推荐使用本接口；

2.当前接口不提供WindowStage的获焦失焦状态监听，对于windowStage获焦失焦状态有监听需求的情况下，推荐使用[on('windowEvent')](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__onwindowevent10)；

3.其他系统机制及其生命周期状态切换的详细说明，请参考[主窗口的生命周期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-overview#主窗口的生命周期)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | string | 是 | 监听事件，固定为'windowStageLifecycleEvent'，即WindowStage生命周期变化事件。 |
| callback | Callback<[WindowStageLifecycleEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstagelifecycleeventtype20)> | 是 | 回调函数。返回当前的WindowStage生命周期状态。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300005 | This window stage is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    const callback = (data: window.WindowStageLifecycleEventType) => {
      console.info(`Succeeded in enabling the listener for window stage event changes. Data: ${JSON.stringify(data)}`);
      // 根据事件状态类型选择进行具体的处理
      if (data === window.WindowStageLifecycleEventType.SHOWN) {
        console.info('current window stage event is SHOWN');
        // ...
      } else if (data === window.WindowStageLifecycleEventType.RESUMED) {
        console.info('current window stage event is RESUMED');
        // ...
      } else if (data === window.WindowStageLifecycleEventType.PAUSED) {
        console.info('current window stage event is PAUSED');
        // ...
      } else if (data === window.WindowStageLifecycleEventType.HIDDEN) {
        console.info('current window stage event is HIDDEN');
        // ...
      }
      // ...
    }
    try {
      windowStage.on('windowStageLifecycleEvent', callback);
    } catch (exception) {
      console.error(`Failed to enable the listener for window stage event changes. Cause code: ${exception.code}, message: ${exception.message}`);
    }
};
```

#### off('windowStageLifecycleEvent')20+

off(eventType: 'windowStageLifecycleEvent', callback?: Callback<[WindowStageLifecycleEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstagelifecycleeventtype20)>): void

关闭WindowStage生命周期变化的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | string | 是 | 监听事件，固定为'windowStageLifecycleEvent'，即WindowStage生命周期变化事件。 |
| callback | Callback<[WindowStageLifecycleEventType](../enums/Enums.md#ZH-CN_TOPIC_0000002529444769__windowstagelifecycleeventtype20)> | 否 | 回调函数。返回当前的WindowStage生命周期状态。若传入参数，则关闭该监听。若未传入参数，则关闭所有WindowStage生命周期变化的监听。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300005 | This window stage is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    const callback = (windowStageLifecycleEvent: window.WindowStageLifecycleEventType) => {
      // ...
    }
    try {
      windowStage.on('windowStageLifecycleEvent', callback);
    } catch (exception) {
      console.error(`Failed to enable the listener for window stage event changes. Cause code: ${exception.code}, message: ${exception.message}`);
    }
    try {
      windowStage.off('windowStageLifecycleEvent', callback);
      // 如果通过on开启多个callback进行监听，同时关闭所有监听：
      windowStage.off('windowStageLifecycleEvent');
    } catch (exception) {
      console.error(`Failed to disable the listener for window stage event changes. Cause code: ${exception.code}, message: ${exception.message}`);
    }
};
```

#### on('windowStageClose')14+

on(eventType: 'windowStageClose', callback: Callback<void>): void

开启点击主窗三键区的关闭按钮监听事件。点击主窗口的三键区域的关闭键时触发该回调函数，将不执行注册的[UIAbility.onPrepareToTerminate](@ohos.app.ability.UIAbility (带界面的应用组件).md#ZH-CN_TOPIC_0000002522240540__onpreparetoterminate10)生命周期回调函数。

当重复注册窗口关闭事件的监听时，最后一次注册成功的监听事件生效。

触发的回调函数是同步执行，主窗口的异步关闭事件监听参考[on('windowWillClose')](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__onwindowwillclose15)方法。

如果存在[on('windowWillClose')](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__onwindowwillclose15)监听事件，只响应[on('windowWillClose')](Interface (Window).md#ZH-CN_TOPIC_0000002522080752__onwindowwillclose15)接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态后生效；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | string | 是 | 监听事件，固定为'windowStageClose'，即开启主窗三键区的关闭按钮监听。 |
| callback | Callback<void> | 是 | 回调函数。当点击主窗口右上角关闭按钮事件发生时的回调。该回调函数不返回任何参数。回调函数内部逻辑需要有boolean类型的返回值，该返回值决定当前主窗是否继续关闭，true表示不关闭，false表示关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    try {
      windowStage.on('windowStageClose', () => {
        console.info('Succeeded in enabling the listener for window stage close event.');
        return false;
      });
    } catch (exception) {
      console.error(`Failed to enable the listener for window stage close event. Cause code: ${exception.code}, message: ${exception.message}`);
    }
};
```

#### off('windowStageClose')14+

off(eventType: 'windowStageClose', callback?: Callback<void>): void

关闭主窗口关闭事件的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备及不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上调用返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态后生效；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | string | 是 | 监听事件，固定为'windowStageClose'，即关闭主窗口关闭事件的监听。 |
| callback | Callback<void> | 否 | 回调函数。当点击主窗口右上角关闭按钮事件发生时的回调。该回调函数不返回任何参数。回调函数内部逻辑需要有boolean类型的返回值，该返回值决定当前主窗是否继续关闭，true表示不关闭，false表示关闭。如果传入参数，则关闭该监听。如果未传入参数，则关闭所有主窗口关闭的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    const callback = () => {
      // ...
      return false;
    }
    try {
      windowStage.on('windowStageClose', callback);
      windowStage.off('windowStageClose', callback);
      windowStage.off('windowStageClose');
    } catch (exception) {
      console.error(`Failed to disable the listener for window stage close changes. Cause code: ${exception.code}, message: ${exception.message}`);
    }
};
```

#### setDefaultDensityEnabled12+

setDefaultDensityEnabled(enabled: boolean): void

设置应用主窗口是否使用系统默认Density，子窗和系统窗口会跟随主窗生效。调用此接口前，需先调用[WindowStage.loadContent()](#ZH-CN_TOPIC_0000002553360677__loadcontent9)初始化布局，确保接口调用时序正确。

不调用此接口进行设置，则表示不使用系统默认Density。

不使用系统默认Density时，若调用过[setCustomDensity()](#ZH-CN_TOPIC_0000002553360677__setcustomdensity15)，则窗口会跟随用户自定义的显示大小变化重新布局，否则跟随系统显示大小变化重新布局。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否设置应用使用系统默认Density。true表示使用系统默认Density，窗口不跟随系统显示大小变化重新布局；false表示不使用系统默认Density，窗口跟随系统显示大小变化重新布局。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The main window is not created or destroyed. |
| 1300005 | This window stage is abnormal. Possible cause: The window stage is not created or destroyed. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit'

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
      windowStage.loadContent("pages/page2", (err: BusinessError) => {
        let errCode: number = err.code;
        if (errCode) {
          console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        console.info('onWindowStageCreate');
      try {
        windowStage.setDefaultDensityEnabled(true);
        console.info('Succeeded in loading the content.');
      } catch (exception) {
        console.error(`Failed to set default density enabled. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }
};
```

#### setCustomDensity15+

setCustomDensity(density: number): void

支持应用主窗口自定义其显示大小缩放系数。

已创建的子窗和系统窗口不会立即跟随主窗的customDensity变化重新布局，而是在子窗或系统窗口下一次位置、大小、系统缩放大小等窗口布局信息变化时跟随主窗的customDensity变化重新布局。

当存在同时使用该接口和[setDefaultDensityEnabled(true)](#ZH-CN_TOPIC_0000002553360677__setdefaultdensityenabled12)的情况时，以最后调用的设置效果为准。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| density | number | 是 | 自定义显示大小缩放系数。该参数为浮点数，取值范围为[0.5, 4.0]或-1.0。4.0表示窗口可显示的最大显示大小缩放系数，-1.0表示窗口使用系统显示大小缩放系数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. |
| 1300005 | This window stage is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    try {
      windowStage.setCustomDensity(-1.0);
    } catch (exception) {
      console.error(`Failed to set custom density. Cause code: ${exception.code}, message: ${exception.message}`);
    }
};
```

#### setCustomDensity20+

setCustomDensity(density: number, applyToSubWindow?: boolean): void

支持应用主窗口自定义显示大小缩放系数，并设置已创建的子窗和系统窗口跟随主窗重新布局的生效时机。

当存在同时使用该接口和[setDefaultDensityEnabled(true)](#ZH-CN_TOPIC_0000002553360677__setdefaultdensityenabled12)的情况时，以最后调用的设置效果为准。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| density | number | 是 | 自定义显示大小缩放系数。该参数为浮点数，取值范围为[0.5, 4.0]或-1.0。4.0表示窗口可显示的最大显示大小缩放系数，-1.0表示窗口使用系统显示大小缩放系数。 |
| applyToSubWindow | boolean | 否 | 设置当前已创建的子窗和系统窗口是否立即跟随主窗口更新customDensity并重新布局。设置为true时，表示立即跟随主窗生效；设置为false时，表示不会立即跟随主窗生效，而是在子窗或系统窗口下一次位置、大小、系统缩放大小等窗口布局信息变化时跟随主窗的customDensity变化重新布局。默认值为false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The main window is not created or destroyed. |
| 1300005 | This window stage is abnormal. Possible cause: The window stage is not created or destroyed. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    try {
      windowStage.setCustomDensity(2.0);
      windowStage.setCustomDensity(3.0, true);
      windowStage.setCustomDensity(-1.0, false);
    } catch (exception) {
      console.error(`Failed to set custom density. Cause code: ${exception.code}, message: ${exception.message}`);
    }
};
```

#### setWindowModal14+

setWindowModal(isModal: boolean): Promise<void>

设置主窗的模态属性是否启用，使用Promise异步回调。

主窗口调用该接口时，设置主窗口模态属性是否启用。启用主窗口模态属性后，其相同应用进程下的其他主窗口以及其他主窗口的子窗口不能响应用户操作，直到该主窗口关闭或者主窗口的模态属性被禁用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异： 该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备中可正常调用；在支持但不处于自由窗口状态的设备中返回801错误码；在不支持自由窗口状态的设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isModal | boolean | 是 | 设置主窗口模态属性是否启用，true为启用，false为不启用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: The window is not created or destroyed. |
| 1300003 | This window manager service works abnormally. |
| 1300005 | This window stage is abnormal. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    try {
      let promise = windowStage.setWindowModal(true);
      promise.then(() => {
        console.info('Succeeded in setting window modal');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set window modal. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to set window modal. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### removeStartingWindow14+

removeStartingWindow(): Promise<void>

支持应用控制启动页消失时机。

此接口只对应用主窗口生效，且需要在module.json5配置文件[abilities](../../guides/module.json5配置文件.md#abilities标签)标签中的metadata标签下配置"enable.remove.starting.window"为"true"才会生效。

在标签配置为"true"的情况下，系统提供了启动页超时保护机制，若5s内未调用此接口，系统将自动移除启动页。

若标签配置为"false"或未配置标签，则此接口不生效，启动页将会在应用首帧渲染完成后自动移除。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window stage is not created or destroyed; 2. The main window is not created or destroyed; 3. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...

  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info('onWindowStageCreate');
    windowStage.removeStartingWindow().then(() => {
      console.info('Succeeded in removing starting window.');
    }).catch((err: BusinessError) => {
        console.error(`Failed to remove starting window. Cause code: ${err.code}, message: ${err.message}`);
    });
  }
};
```

#### setWindowRectAutoSave14+

setWindowRectAutoSave(enabled: boolean): Promise<void>

设置是否启用最后关闭的主窗尺寸的记忆功能，使用Promise异步回调。

启用记忆功能后，在同一个UIAbility下，记忆最后关闭的主窗口的尺寸；此主窗口再次启动时，以记忆的尺寸按照规则进行打开。

层叠规则：1、当前实例是自由窗口时，打开下一实例窗口层叠时，大小要跟随。2、当前实例是最大化或全屏窗口时，打开下一个实例窗口层叠时，保持最大化。

记忆规则：

| 上一次窗口状态 | 记忆规则 |
| --- | --- |
| 自由窗口 | 保留自由窗口的大小/位置，超出工作区回弹 |
| 二分屏窗口 | 保留二分屏之前自由窗口的大小/位置 |
| 最大化窗口 | 保留最大化 |
| 沉浸式窗口 | 保留沉浸式之前自由窗口的大小/位置 |
| 最小化窗口 | 保留最小化之前自由窗口的大小/位置 |

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态后生效；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否启用主窗尺寸的记忆功能，true为启用，false为不启用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    try {
      let promise = windowStage.setWindowRectAutoSave(true);
      promise.then(() => {
        console.info('Succeeded in setting window rect auto-save');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set window rect auto-save. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to set window rect auto-save. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### setWindowRectAutoSave17+

setWindowRectAutoSave(enabled: boolean, isSaveBySpecifiedFlag: boolean): Promise<void>

设置是否启用主窗的尺寸记忆功能，使用Promise异步回调。

在同一个UIAbility下，可记忆最后关闭的主窗口尺寸，也可针对每个主窗口尺寸单独进行记忆。只有在UIAbility启动模式为specified，且isSaveBySpecifiedFlag设置为true时，才能针对每个主窗口尺寸进行单独记忆。

启用记忆功能后，记忆主窗口关闭时的尺寸；对应主窗口再次启动时，以记忆的尺寸按照规则进行打开。

记忆规则：

| 上一次窗口状态 | 记忆规则 |
| --- | --- |
| 自由窗口 | 保留自由窗口的大小/位置，超出工作区回弹。 |
| 二分屏窗口 | 保留二分屏之前自由窗口的大小/位置。 |
| 最大化窗口 | 保留最大化。 |
| 沉浸式窗口 | 保留沉浸式之前自由窗口的大小/位置。 |
| 最小化窗口 | 保留最小化之前自由窗口的大小/位置。 |

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备上可正常调用；在支持但不处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效，切换到[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态后生效；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否启用主窗的尺寸记忆功能，true为启用，false为不启用。 |
| isSaveBySpecifiedFlag | boolean | 是 | 设置specified模式下是否启用对窗口进行单独记忆，true为启用，false为不启用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Function setWindowRectAutoSave can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    try {
      let promise = windowStage.setWindowRectAutoSave(true, true);
      promise.then(() => {
        console.info('Succeeded in setting window rect auto-save');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set window rect auto-save. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to set window rect auto-save. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### isWindowRectAutoSave14+

isWindowRectAutoSave(): Promise<boolean>

判断当前主窗口是否已经启用尺寸记忆，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

设备行为差异：

在HarmonyOS开发套件（基于API 23）配套的系统版本之前，该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

从HarmonyOS开发套件（基于API 23）配套的系统版本开始，该接口在支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备正常调用；在不支持[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备调用不报错，返回false。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前窗口启用尺寸记忆，返回false表示当前窗口禁用尺寸记忆。 |

**错误码：**

以下错误码的详细介绍请参见[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed; 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    try {
      let promise = windowStage.isWindowRectAutoSave();
      promise.then((data) => {
        console.info(`Succeeded in checking whether the window support the rect auto-save. Data: ${data}`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to check whether the window support the rect auto-save. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to check whether the window support the rect auto-save. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### setSupportedWindowModes15+

setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>): Promise<void>

设置主窗的窗口支持模式，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 6.0.2之前，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备中可正常调用；在支持但不处于自由窗口状态的设备中返回801错误码；在不支持自由窗口状态的设备中返回801错误码。

从HarmonyOS 6.0.2开始，该接口在支持并处于自由窗口状态的设备中可正常调用且立即生效；在支持但不处于自由窗口状态的设备中可正常调用，切换为自由窗口状态时生效；在不支持自由窗口状态的设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| supportedWindowModes | Array<bundleManager.SupportWindowMode> | 是 | 设置主窗的窗口支持模式。 - FULL_SCREEN：支持全屏模式。 - FLOATING：支持悬浮窗模式。 - SPLIT：支持分屏模式。需要配合FULL_SCREEN或FLOATING一起使用，不支持仅配置SPLIT。 注：数组中SupportWindowMode字段取值不应该与该UIAbility对应的module.json5配置文件中abilities标签的supportWindowMode字段取值或者StartOptions中属性的supportWindowModes字段取值冲突。当取值冲突时，最终以该参数设置的窗口支持模式为准。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility, bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    try {
      let promise = windowStage.setSupportedWindowModes([
        bundleManager.SupportWindowMode.FULL_SCREEN,
        bundleManager.SupportWindowMode.SPLIT,
        bundleManager.SupportWindowMode.FLOATING
      ]);
      promise.then(() => {
        console.info('Succeeded in setting window support modes');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set window support modes. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to set window support modes. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```

#### setSupportedWindowModes20+

setSupportedWindowModes(supportedWindowModes: Array<bundleManager.SupportWindowMode>, grayOutMaximizeButton: boolean): Promise<void>

设置主窗的窗口支持模式，并提供最大化按钮置灰功能，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**设备行为差异：**

在HarmonyOS 6.0.2之前，该接口在支持并处于[自由窗口](../../guides/窗口开发术语.md#自由窗口)状态的设备中可正常调用；在支持但不处于自由窗口状态的设备中返回801错误码；在不支持自由窗口状态的设备中返回801错误码。

从HarmonyOS 6.0.2开始，该接口在支持并处于自由窗口状态的设备中可正常调用且立即生效；在支持但不处于自由窗口状态的设备中可正常调用，切换为自由窗口状态时生效；在不支持自由窗口状态的设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| supportedWindowModes | Array<bundleManager.SupportWindowMode> | 是 | 设置主窗的窗口支持模式。 - FULL_SCREEN：支持全屏模式。 - FLOATING：支持悬浮窗模式。 - SPLIT：支持分屏模式。需要配合FULL_SCREEN或FLOATING一起使用，不支持仅配置SPLIT。 注：数组中SupportWindowMode字段取值不应该与该UIAbility对应的module.json5配置文件中abilities标签的supportWindowMode字段取值或者StartOptions中属性的supportWindowModes字段取值冲突。当取值冲突时，最终以该参数设置的窗口支持模式为准。 |
grayOutMaximizeButtonboolean是是否显示并将主窗口的最大化按钮置灰。true表示显示并将主窗口的最大化按钮置灰，此时最大化按钮不可用；false表示不显示主窗口的最大化按钮。此参数配置仅在supportedWindowModes不支持FULL_SCREEN时生效。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[窗口错误码](窗口错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function setSupportedWindowModes can not work correctly due to limited device capabilities. |
| 1300002 | This window state is abnormal. Possible cause: 1. The window is not created or destroyed. 2. Internal task error. |
| 1300003 | This window manager service works abnormally. |
| 1300016 | Parameter error. Possible cause: 1. Invalid parameter range. 2. Invalid parameter length. 3. Incorrect parameter format. |

**示例：**

```ets
// EntryAbility.ets
import { UIAbility, bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('onWindowStageCreate');
    try {
      let promise = windowStage.setSupportedWindowModes([
        bundleManager.SupportWindowMode.FULL_SCREEN,
        bundleManager.SupportWindowMode.SPLIT,
        bundleManager.SupportWindowMode.FLOATING
      ], true);
      promise.then(() => {
        console.info('Succeeded in setting window support modes');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set window support modes. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to set window support modes. Cause code: ${exception.code}, message: ${exception.message}`);
    }
```