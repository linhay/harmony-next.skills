# updateManager（更新功能）

提供检测新版本及升级功能。

调用接口需捕获异常。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { updateManager } from '@kit.AppGalleryKit';
```

#### UpdateAvailableCode

检测更新结果码类型的枚举。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AppGalleryService.Distribution.Update

**起始版本：**5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LATER_VERSION_NOT_EXIST | 0 | 不存在新版本。 |
| LATER_VERSION_EXIST | 1 | 存在新版本。 |

#### ShowUpdateResultCode

显示升级弹框结果码类型的枚举。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.Distribution.Update

**起始版本：**5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHOW_DIALOG_SUCCESS | 0 | 显示升级弹框成功。 |
| SHOW_DIALOG_FAILURE | 1 | 显示升级弹框失败。 |

#### CheckUpdateResult

检查是否有“更新”的接口调用结果。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AppGalleryService.Distribution.Update

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| updateAvailable | UpdateAvailableCode | 是 | 否 | 检查结果。 |
| versionName | string | 是 | 是 | 版本名称，例如1.0.0.1。 起始版本： 6.0.0(20) 说明： 用于元服务场景调用。 |
| versionCode | number | 是 | 是 | 版本号，例如1001。 起始版本： 6.0.0(20) 说明： 用于元服务场景调用。 |

#### RequestErrorCode

监听元服务更新检查接口结果码类型的枚举。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AppGalleryService.Distribution.Update

**起始版本：**6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO_UPGRADE | 0 | 无最新版本。 |
| NEED_UPGRADE | 1 | 有最新版本。 |
| DOWNLOADED | 2 | 下载完成。 |

#### UpdateSessionState

监听元服务更新检查接口的回调结果。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AppGalleryService.Distribution.Update

**起始版本：**6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | RequestErrorCode | 是 | 否 | 检查结果码。 |
| checkUpdateResult | CheckUpdateResult | 是 | 是 | 检查结果。 说明： 仅在RequestErrorCode为NEED_UPGRADE或NO_UPGRADE时不为空。 |

#### updateManager.checkAppUpdate

checkAppUpdate(context: common.UIAbilityContext): Promise<CheckUpdateResult>

检查是否有更新，使用Promise方式异步返回结果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.Distribution.Update

设备行为差异： 对于5.1.1(19)之前版本，该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型上该接口返回的CheckUpdateResult中updateAvailable值固定为LATER_VERSION_NOT_EXIST，无法检查出应用是否有更新。对于5.1.1(19)版本，该接口在Phone、Tablet、PC/2in1、TV中可正常调用，在其他设备类型上该接口返回的CheckUpdateResult中updateAvailable值固定为LATER_VERSION_NOT_EXIST，无法检查出应用是否有更新。对于6.0.0(20)及之后版本，该接口在Phone、Tablet、PC/2in1、TV、Wearable中可正常调用。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.UIAbilityContext | 是 | 调用方应用的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<CheckUpdateResult> | Promise对象，返回是否有更新检查结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码]([ArkTS API错误码](../../errors/ArkTS API错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1009400001 | SA connect error. |
| 1009400002 | Request to service error. |
| 1009400003 | Network error. |
| 1009400004 | The application is not in the foreground. |
| 1009400005 | Not agreeing to the privacy agreement. |
| 1009400006 | Time limited. |
| 1009400007 | Other error. |

**示例：**

```ets
import { updateManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'checkAppUpdate test'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            try {
              updateManager.checkAppUpdate(this.getUIContext().getHostContext() as common.UIAbilityContext)
                .then((checkResult: updateManager.CheckUpdateResult) => {
                  hilog.info(0, 'TAG', "Succeeded in checking Result updateAvailable:" + checkResult.updateAvailable);
                }).catch((error: BusinessError) => {
                hilog.error(0, 'TAG', `checkAppUpdate onError.code is ${error.code}, message is ${error.message}`);
              });
            } catch (error) {
              hilog.error(0, 'TAG', `checkAppUpdate onError.code is ${error.code}, message is ${error.message}`);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### updateManager.showUpdateDialog

showUpdateDialog(context: common.UIAbilityContext): Promise<ShowUpdateResultCode>

显示升级弹框，使用Promise方式异步返回结果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.AppGalleryService.Distribution.Update

设备行为差异： 对于5.1.1(19)之前版本，该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型上该接口返回的ShowUpdateResultCode值固定为SHOW_DIALOG_FAILURE，无法弹出应用更新弹框。对于5.1.1(19)版本，该接口在Phone、Tablet、PC/2in1、TV中可正常调用，在其他设备类型上该接口返回的ShowUpdateResultCode值固定为SHOW_DIALOG_FAILURE，无法弹出应用更新弹框。对于6.0.0(20)及之后版本，该接口在Phone、Tablet、PC/2in1、TV、Wearable中可正常调用。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.UIAbilityContext | 是 | 调用方应用的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ShowUpdateResultCode> | Promise对象，返回显示升级弹框获取结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1009400001 | SA connection error. |
| 1009400002 | Request to service error. |
| 1009400004 | The application is not in the foreground. |
| 1009400005 | Not agreeing to the privacy agreement. |
| 1009400007 | Other error. |

**示例：**

```ets
import { updateManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'showUpdateDialog test'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            try {
              updateManager.showUpdateDialog(this.getUIContext().getHostContext() as common.UIAbilityContext)
                .then((resultCode: updateManager.ShowUpdateResultCode) => {
                  hilog.info(0, 'TAG', "Succeeded in showing UpdateDialog resultCode:" + resultCode);
                })
                .catch((error: BusinessError) => {
                  hilog.error(0, 'TAG', `showUpdateDialog onError.code is ${error.code}, message is ${error.message}`);
                });
            } catch (error) {
              hilog.error(0, 'TAG', `showUpdateDialog onError.code is ${error.code}, message is ${error.message}`);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
```

#### updateManager.on('updateChange')

on(type: 'updateChange', callback: Callback<UpdateSessionState>, timeout?: number): void

监听元服务更新检查接口，检查到有/无更新后，使用callback方式返回结果。

同一元服务的调用次数不超过6次/天、每30分钟调用次数不超过1次。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AppGalleryService.Distribution.Update

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定值"updateChange"。 |
| callback | Callback<UpdateSessionState> | 是 | 回调函数，使用Callback方式获取结果。 |
| timeout | number | 否 | 注册监听允许的最大监听时间（单位：s），取值范围：不大于20的正整数，如果不传，取默认值20。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009400001 | SA connection error. |
| 1009400002 | Request to service error. |
| 1009400007 | Other error. |
| 1009400008 | The number of parameters for the on API is incorrect. |
| 1009400009 | The type parameter for the on API is invalid. |
| 1009400010 | The callback parameter for the on API is invalid. |
| 1009400011 | The timeout parameter for the on API is invalid. |

**示例：**

```ets
import { updateManager } from '@kit.AppGalleryKit';
import { abilityManager, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'on'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => this.callOn)
      }
      .width('100%')
    }
    .height('100%')
  }

  private callOn() {
    let callback = (state: updateManager.UpdateSessionState) => {
      if (state.code === updateManager.RequestErrorCode.NO_UPGRADE) {
        hilog.info (0, 'TAG', `on success, no need update`);
        updateManager.off('updateChange');
      } else if (state.code === updateManager.RequestErrorCode.NEED_UPGRADE) {
        hilog.info (0, 'TAG', `on success, need update`);
      } else if (state.code === updateManager.RequestErrorCode.DOWNLOADED) {
        hilog.info (0, 'TAG', `on success, need update and download success`);
        updateManager.off('updateChange');
        abilityManager.restartSelfAtomicService(this.getUIContext().getHostContext() as common.Context);
      }
    };
    try {
      updateManager.on('updateChange', callback, 20);
    } catch (error) {
      hilog.error(0, 'TAG', `on Error.code is ${error.code}, message is ${error.message}`);
    }
```

#### updateManager.off('updateChange')

off(type: 'updateChange', callback?: Callback<UpdateSessionState>): void

取消监听元服务更新检查接口。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AppGalleryService.Distribution.Update

**起始版本：**6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定值"updateChange"。 |
| callback | Callback<UpdateSessionState> | 否 | 回调函数，使用Callback的方式获取结果。不传该参数则会取消当前应用的所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009400001 | SA connection error. |
| 1009400002 | Request to service error. |
| 1009400007 | Other error. |
| 1009400012 | The number of parameters for the off API is incorrect. |
| 1009400013 | The type parameter for the off API is invalid. |
| 1009400014 | The callback parameter for the off API is invalid. |

**示例：**

```ets
import { updateManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
try {
  // 取消监听
  updateManager.off('updateChange');
} catch (error) {
  hilog.error(0, 'TAG', `moduleInstallManager.off onError.code is ${error.code}, message is ${error.message}`);
}
```