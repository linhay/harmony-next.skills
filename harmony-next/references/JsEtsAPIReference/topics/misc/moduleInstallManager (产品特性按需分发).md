# moduleInstallManager (产品特性按需分发)

借助该模块，您可以从应用的基本模块中分离特定功能和资源，并将其包含在子模块的包中。用户在使用应用过程中，可以动态下载子模块包。该模块包含判断模块是否安装、请求按需加载任务、监听模块下载进度、流量提醒弹窗、取消按需加载任务等功能。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

调用接口需捕获异常。

起始版本： 4.1.0(11)

**导入模块**

```ets
import { moduleInstallManager } from '@kit.AppGalleryKit';
```

**InstalledModule**

当前模块的安装信息。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moduleName | string | 是 | 否 | 模块名称。 |
| moduleType | bundleManager.ModuleType | 是 | 是 | 模块类型。 说明： 当installStatus=1时，moduleType默认返回0（UNKNOWN）。 |
| installStatus | InstallStatus | 是 | 否 | 模块安装结果。 |

**ModuleInstallSessionState**

请求、监听/注销监听接口，接口调用结果。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | RequestErrorCode | 是 | 否 | 接口调用结果码。 |
| taskStatus | TaskStatus | 是 | 否 | 按需下载任务状态码。 |
| taskId | string | 是 | 是 | 按需下载任务taskId，默认值为0。 |
| desc | string | 是 | 否 | 接口调用结果描述，默认值为“”。 |
| modules | string[] | 是 | 是 | 下载任务中的模块名列表，默认值为[]。 |
| totalSize | number | 是 | 是 | 下载的总模块大小（字节），默认值为0。 |
| downloadedSize | number | 是 | 是 | 已下载大小（字节），默认值为0。 |

**InstallStatus**

安装结果状态码类型的枚举。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INSTALLED | 0 | 模块已安装。 |
| NOT_INSTALLED | 1 | 模块未安装。 |

**ReturnCode**

添加模块、取消下载、流量提醒弹窗接口，接口调用结果码类型的枚举。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 成功。 |
| FAILURE | 1 | 失败。 |

**RequestErrorCode**

请求、监听/注销监听接口，接口调用结果码类型的枚举。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MODULE_DEBUG_FILES_SIZE_OVER_LIMIT | -10 | 单次请求所有模块调试文件大小总和超过8G。 起始版本： 5.0.2(14) |
| MODULE_DEBUG_FILES_NOT_EXIST | -9 | 模块调试文件不存在。 起始版本： 5.0.2(14) |
| MODULE_ALREADY_EXISTS | -8 | 模块已存在。 |
| MODULE_UNAVAILABLE | -7 | 要下载的模块不存在或者模块不适配该设备。 |
| INVALID_REQUEST | -6 | 该请求无效，请求中包含的信息不准确。 |
| NETWORK_ERROR | -5 | 网络异常，请求失败。 |
| INVOKER_VERIFICATION_FAILED | -4 | 调用者信息异常。 |
| FOREGROUND_REQUIRED | -3 | 仅允许前台时请求按需加载。 |
| ACTIVE_SESSION_LIMIT_EXCEEDED | -2 | 请求遭到拒绝，因为当前至少有一个请求正在下载。 |
| FAILURE | -1 | 失败。 |
| SUCCESS | 0 | 成功。 |
| DOWNLOAD_WAIT_WIFI | 1 | 当前使用的是流量，开发者需要调用showCellularDataConfirmation接口，提醒用户确认是否使用流量下载。 |

**TaskStatus**

请求、监听/注销监听接口，接口返回下载任务状态码类型的枚举。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CREATE_TASK_FAILED | -4 | 创建下载任务失败。 |
| HIGHER_VERSION_INSTALLED | -3 | 本地存在相同或者更高版本。 |
| TASK_ALREADY_EXISTS | -2 | 下载任务已存在。 |
| TASK_UNFOUND | -1 | 下载任务不存在。 |
| TASK_CREATED | 0 | 创建下载任务成功。 |
| DOWNLOADING | 1 | 下载中。 |
| DOWNLOAD_PAUSING | 2 | 暂停中。 |
| DOWNLOAD_WAITING | 3 | 等待下载中。 |
| DOWNLOAD_SUCCESSFUL | 4 | 下载成功完成。 |
| DOWNLOAD_FAILED | 5 | 下载失败。 |
| DOWNLOAD_WAIT_WIFI | 6 | Wi-Fi预约。 |
| INSTALL_WAITING | 20 | 等待安装。 |
| INSTALLING | 21 | 安装中。 |
| INSTALL_SUCCESSFUL | 22 | 安装完成。 |
| INSTALL_FAILED | 23 | 安装失败。 |

**moduleInstallManager.getInstalledModule**

getInstalledModule(moduleName: string): InstalledModule

查询模块安装信息接口。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 需要获取的模块名。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| InstalledModule | 当前模块的安装信息。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006500001 | Failed to invoke the BMS. |

示例：

```ets
import { moduleInstallManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const moduleInfo: moduleInstallManager.InstalledModule = moduleInstallManager.getInstalledModule('AModule');
  hilog.info(0, 'TAG', 'Succeeded in getting installedModule moduleInfo' );
} catch (error) {
  hilog.error(0, 'TAG', `getting installedModule onError.code is ${error.code}, message is ${error.message}`);
}
```

**InstallProvider**

按需加载controller父类对象。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

**InstallRequest**

按需加载请求父类对象。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

**ModuleInstallProvider**

实现按需加载的方法，提供创建按需加载请求对象能力，继承[InstallProvider](#ZH-CN_TOPIC_0000002522082310__installprovider)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

**ModuleInstallProvider.createModuleInstallRequest**

createModuleInstallRequest(context: common.UIAbilityContext | common.ExtensionContext): ModuleInstallRequest

创建按需加载请求对象，可通过返回值设置请求参数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.UIAbilityContext | common.ExtensionContext | 是 | 调用方应用的上下文。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| ModuleInstallRequest | 按需下载请求对象。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { moduleInstallManager } from '@kit.AppGalleryKit';

const TAG: string = 'createModuleInstallRequest';

@Entry
@Component
struct CreateModuleInstallRequest {

  build() {
    Column() {
      Button("createModuleInstallRequest")
        .onClick(() => {
          try {
            const myModuleInstallProvider: moduleInstallManager.ModuleInstallProvider =
              new moduleInstallManager.ModuleInstallProvider();
            const context: common.UIAbilityContext | common.ExtensionContext = this.getUIContext().getHostContext()  as common.UIAbilityContext;
            const myModuleInstallRequest: moduleInstallManager.ModuleInstallRequest =
              myModuleInstallProvider.createModuleInstallRequest(context);
          } catch (error) {
            hilog.error(0, TAG, `createModuleInstallRequest onError.code is ${error.code}, message is ${error.message}`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
```

**ModuleInstallRequest**

按需下载请求对象，继承[InstallRequest](#ZH-CN_TOPIC_0000002522082310__installrequest)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

**ModuleInstallRequest.addModule**

addModule(moduleName: string): ReturnCode

添加要按需加载的模块名。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 模块名。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| ReturnCode | 接口调用结果码。 |

错误码：

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { moduleInstallManager } from '@kit.AppGalleryKit';

const TAG: string = 'addModule';

@Entry
@Component
struct AddModule {

  build() {
    Column() {
      Button("addModule")
        .onClick(() => {
          try {
            const myModuleInstallProvider: moduleInstallManager.ModuleInstallProvider =
              new moduleInstallManager.ModuleInstallProvider();
            const context: common.UIAbilityContext | common.ExtensionContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            const myModuleInstallRequest: moduleInstallManager.ModuleInstallRequest =
              myModuleInstallProvider.createModuleInstallRequest(context);
            const aResult: moduleInstallManager.ReturnCode = myModuleInstallRequest.addModule('AModule');
            const bResult: moduleInstallManager.ReturnCode = myModuleInstallRequest.addModule('BModule');
            hilog.info(0, TAG, 'Succeeded in getting aResult:' + aResult + ' bResult:' + bResult);
          } catch (error) {
            hilog.error(0, TAG, `addModule onError.code is ${error.code}, message is ${error.message}`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
```

**moduleInstallManager.fetchModules**

fetchModules(moduleInstallRequest: ModuleInstallRequest): Promise<ModuleInstallSessionState>

按需加载请求接口，支持调试模式，使用Promise方式异步返回结果。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleInstallRequest | ModuleInstallRequest | 是 | 按需加载请求对象实例。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<ModuleInstallSessionState> | Promise对象，返回请求、监听/注销监听调用结果。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006500004 | SA connection failed. |
| 1006500008 | Write param into container failed. |
| 1006500009 | Request to service error. |
| 1006500010 | Response from service cannot be recognized. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { moduleInstallManager } from '@kit.AppGalleryKit';

const TAG: string = 'fetchModules';

@Entry
@Component
struct FetchModules {

  build() {
    Column() {
      Button("fetchModules")
        .onClick(() => {
          try {
            const myModuleInstallProvider: moduleInstallManager.ModuleInstallProvider =
              new moduleInstallManager.ModuleInstallProvider();
            const context: common.UIAbilityContext | common.ExtensionContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            const myModuleInstallRequest: moduleInstallManager.ModuleInstallRequest =
              myModuleInstallProvider.createModuleInstallRequest(context);
            myModuleInstallRequest.addModule('AModule');
            myModuleInstallRequest.addModule('BModule');
            moduleInstallManager.fetchModules(myModuleInstallRequest)
              .then(() => {
                hilog.info(0, TAG, 'Succeeded in fetching modules success data.' );
              })
          } catch (error) {
            hilog.error(0, TAG, `fetching modules onError.code is ${error.code}, message is ${error.message}`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
```

**moduleInstallManager.cancelTask**

cancelTask(taskId: string): ReturnCode

取消下载任务接口。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskId | string | 是 | 下载任务的taskId。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| ReturnCode | 接口调用结果码。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006500007 | The specified service extension connect failed. |
| 1006500008 | Write param into container failed. |
| 1006500009 | Request to service error. |
| 1006500010 | Response from service cannot be recognized. |

示例：

```ets
import { moduleInstallManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // taskId 是fetchModules返回结果ModuleInstallSessionState中的taskId字段
  const taskId: string = '********';
  const rtnCode: moduleInstallManager.ReturnCode = moduleInstallManager.cancelTask(taskId);
  hilog.info(0, 'TAG', "Succeeded in getting result:" + rtnCode);
} catch (error) {
  hilog.error(0, 'TAG', `cancelTask onError.code is ${error.code}, message is ${error.message}`);
}
```

**moduleInstallManager.showCellularDataConfirmation**

showCellularDataConfirmation(context: common.UIAbilityContext | common.ExtensionContext,taskId: string): ReturnCode

流量提醒弹窗接口。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.UIAbilityContext | common.ExtensionContext | 是 | Context上下文，目前只支持UIAbilityContext和ExtensionContext，其中UIAbilityContext用于校验当前应用是否在前台。 |
| taskId | string | 是 | 下载任务的taskId。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| ReturnCode | 接口调用结果码。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006500007 | The specified service extension connect failed. |
| 1006500008 | Write param into container failed. |
| 1006500009 | Request to service error. |
| 1006500010 | Response from service cannot be recognized. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { moduleInstallManager } from '@kit.AppGalleryKit';

const TAG: string = 'showCellularDataConfirmation';

@Entry
@Component
struct ShowCellularDataConfirmation {

  build() {
    Column() {
      Button("showCellularDataConfirmation")
        .onClick(() => {
          try {
            // taskId 是fetchModules返回结果ModuleInstallSessionState中的taskId字段
            const taskId: string = '********';
            const context = this.getUIContext().getHostContext()  as common.UIAbilityContext;
            const rtnCode: moduleInstallManager.ReturnCode =
              moduleInstallManager.showCellularDataConfirmation(context, taskId);
            hilog.info(0, TAG, "Succeeded in getting result:" + rtnCode);
          } catch (error) {
            hilog.error(0, TAG, `showCellularDataConfirmation onError.code is ${error.code}, message is ${error.message}`);
          }
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
```

**moduleInstallManager.on('moduleInstallStatus')**

on(type: 'moduleInstallStatus', callback: Callback<ModuleInstallSessionState>, timeout: number): void

监听当前应用下载任务的进度，不支持多线程调用。加载模块时，通过回调函数通知调用者。安装成功且是调试模式时，会删除安装成功模块路径下的调试文件。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定值"moduleInstallStatus"。 |
| callback | Callback<ModuleInstallSessionState> | 是 | 回调函数，使用Callback的方式获取结果。 |
| timeout | number | 是 | 注册监听允许的最大监听时间，默认30分钟（即30*60s），且最大超过30分钟也是按30分钟算。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006500002 | The interface is called repeatedly with the same input. |
| 1006500004 | SA connection failed. |

示例：

```ets
import { moduleInstallManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const timeout = 30 * 60;
  moduleInstallManager.on('moduleInstallStatus', (data: moduleInstallManager.ModuleInstallSessionState) => {
    // 注册监听
    hilog.info(0, 'TAG', 'Succeeded in getting moduleInstallManager.on.' );
  }, timeout)
} catch (error) {
  hilog.error(0, 'TAG', `moduleInstallManager.on onError.code is ${error.code}, message is ${error.message}`);
}
```

**moduleInstallManager.off('moduleInstallStatus')**

off(type: 'moduleInstallStatus', callback?: Callback<ModuleInstallSessionState>): void

取消监听当前应用下载任务的进度，不支持多线程调用。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.AppGalleryService.Distribution.OnDemandInstall

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定值"moduleInstallStatus"。 |
| callback | Callback<ModuleInstallSessionState> | 否 | 回调函数，使用Callback的方式获取结果。不传该参数则会取消当前应用的所有监听。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006500004 | SA connection failed. |
| 1006500006 | The interface is not used together with "on". |

示例：

```ets
import { moduleInstallManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  moduleInstallManager.off('moduleInstallStatus', (data: moduleInstallManager.ModuleInstallSessionState) => {
    // 取消监听
    hilog.info(0, 'TAG', 'Succeeded in getting moduleInstallManager.off.' );
  })
} catch (error) {
  hilog.error(0, 'TAG', `moduleInstallManager.off onError.code is ${error.code}, message is ${error.message}`);
}
```