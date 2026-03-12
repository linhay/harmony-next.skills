# minorsProtection (华为账号未成年人模式)

当前模块提供Account Kit未成年人模式的相关能力，包括开启/关闭系统未成年人模式、获取系统未成年人模式的开启状态、年龄段信息等。开发者可调用本模块的能力，与系统未成年人模式联动，快速实现应用的未成年人模式的切换。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { minorsProtection } from '@kit.AccountKit';
```

#### MinorsProtectionInfo

该类提供未成年人模式的开启状态，以及年龄段信息。应用可跟随未成年人模式开启状态，进行开启/关闭应用的未成年人模式，使用年龄段信息，展示适龄内容。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

minorsProtectionMode

boolean

否

否

是否开启未成年人模式。

返回true表示未成年人模式为开启状态。

返回false表示未成年人模式为关闭状态。

ageGroup

[AgeGroup](#section397519409416)

否

是

年龄段信息。

 说明：

1. 仅当未成年人模式开启时才返回此字段。
1. 当登录中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）儿童账号（14周岁及以下）开启未成年人模式，则可能返回年龄段信息为[0,3)、[3,8)、[8,12)或[12,16)。

  1. 如用户登录4周岁儿童账号，则返回年龄段信息为[3,8)。
  1. 如用户登录9周岁儿童账号，则返回年龄段信息为[8,12)。

1. 当登录中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）非儿童账号开启未成年人模式，则可能返回年龄段信息为[0,3)、[3,8)、[8,12)、[12,16)或[16,18)。

  1. 如用户创建13岁临时使用者，则返回年龄段信息为[12,16)。
  1. 如用户创建17岁临时使用者，则返回年龄段信息为[16,18)。

#### AgeGroup

该类为年龄段信息对象。开发者可根据当前年龄段信息，展示适龄内容。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

lowerAge

number

否

否

年龄段下限，包含下限值。

 说明：

该字段取值范围：0、3、8、12或16。

upperAge

number

否

否

年龄段上限，不包含上限值。

 说明：

该字段取值范围：3、8、12、16或18。

#### MinorsModeErrorCode

该枚举为未成年人模式模块的错误码。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：**5.0.0(12)

**名称**

**值**

**说明**

MINORS_MODE_NOT_ENABLED

[1009900002](ArkTS错误码.md#section5166694516)

未成年人模式未开启。

USER_CANCELED

[1009900003](ArkTS错误码.md#section191691561188)

用户取消操作。

MINORS_MODE_ALREADY_ON

[1009900005](ArkTS错误码.md#section35901828161314)

未成年人模式已经开启。

MINORS_MODE_ALREADY_OFF

[1009900006](ArkTS错误码.md#section1451016215158)

未成年人模式已经关闭。

UNSUPPORTED_ACCOUNT

[1009900007](ArkTS错误码.md#section2076682413462)

不支持的账号。

SERVICE_NOT_AVAILABLE

[1009900011](ArkTS错误码.md#section13666164864818)

服务不可用。

#### supportMinorsMode

supportMinorsMode(): boolean

该方法为同步方法，调用该方法判断当前设备环境是否支持未成年人模式。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

boolean

返回boolean值。

返回true表示支持未成年人模式。

返回false表示不支持未成年人模式。

 说明：

当登录海外华为账号、隐私空间均会返回false，其他场景均为true。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

[1001502009](ArkTS错误码.md#section17561151616317)

Internal error.

**示例：**

```ets
import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    const supportMinorsMode: boolean = minorsProtection.supportMinorsMode();
    hilog.info(0x0000, 'testTag', `Succeeded in getting supportMinorsMode is: ${supportMinorsMode.valueOf()}`);
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the supportMinorsMode interface.');
}
```

#### getMinorsProtectionInfoSync

getMinorsProtectionInfoSync(): MinorsProtectionInfo

该方法为同步方法，调用该方法获取未成年人模式的开启状态，以及年龄段信息。应用可跟随未成年人模式开启状态，进行开启/关闭应用的未成年人模式，使用年龄段信息，展示适龄内容。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

[MinorsProtectionInfo](#section3551104714566)

返回[MinorsProtectionInfo](#section3551104714566)对象。用于获取未成年人模式开启状态、年龄段信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

[1001502009](ArkTS错误码.md#section17561151616317)

Internal error.

**示例：**

```ets
import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    if (minorsProtection.supportMinorsMode()) {
      const minorsProtectionInfo: minorsProtection.MinorsProtectionInfo =
        minorsProtection.getMinorsProtectionInfoSync();
      // 获取未成年人模式开启状态
      const minorsProtectionMode: boolean = minorsProtectionInfo.minorsProtectionMode;
      // 如开发者有频繁使用到未成年人模式开启状态，这里则需缓存未成年人模式开启状态
      hilog.info(0x0000, 'testTag',
        `Succeeded in getting minorsProtectionMode is: ${minorsProtectionMode.valueOf()}`);
      // 未成年人模式已开启，获取年龄段信息
      if (minorsProtectionMode) {
        const ageGroup: minorsProtection.AgeGroup | undefined = minorsProtectionInfo.ageGroup;
        if (ageGroup) {
          hilog.info(0x0000, 'testTag', `Succeeded in getting lowerAge is: ${ageGroup.lowerAge}`);
          hilog.info(0x0000, 'testTag', `Succeeded in getting upperAge is: ${ageGroup.upperAge}`);
          // 根据年龄段刷新内容展示。如开发者有频繁使用到年龄段信息，这里则需缓存年龄段信息
        }
      } else {
        // 未成年人模式未开启，应用需跟随系统未成年人模式，展示内容不做限制
      }
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      `Failed to invoke supportMinorsMode or getMinorsProtectionInfoSync. errCode: ${error.code},
      errMessage: ${error.message}`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the getMinorsProtectionInfoSync interface.');
}
```

#### getMinorsProtectionInfo

getMinorsProtectionInfo(): Promise<MinorsProtectionInfo>

调用该方法获取未成年人模式的开启状态，以及年龄段信息。应用可跟随未成年人模式开启状态，进行开启/关闭应用的未成年人模式，使用年龄段信息，展示适龄内容。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

Promise<[MinorsProtectionInfo](#section3551104714566)>

Promise对象，返回[MinorsProtectionInfo](#section3551104714566)对象。用于获取未成年人模式开启状态、年龄段信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

[1001502009](ArkTS错误码.md#section17561151616317)

Internal error.

**示例：**

```ets
import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    if (minorsProtection.supportMinorsMode()) {
      minorsProtection.getMinorsProtectionInfo()
        .then((minorsProtectionInfo: minorsProtection.MinorsProtectionInfo) => {
          // 获取未成年人模式开启状态
          const minorsProtectionMode: boolean = minorsProtectionInfo.minorsProtectionMode;
          // 如开发者有频繁使用到未成年人模式开启状态，这里则需缓存未成年人模式开启状态
          hilog.info(0x0000, 'testTag',
            `Succeeded in getting minorsProtectionMode is: ${minorsProtectionMode.valueOf()}`);
          // 未成年人模式已开启，获取年龄段信息
          if (minorsProtectionMode) {
            const ageGroup: minorsProtection.AgeGroup | undefined = minorsProtectionInfo.ageGroup;
            if (ageGroup) {
              hilog.info(0x0000, 'testTag', `Succeeded in getting lowerAge is: ${ageGroup.lowerAge}`);
              hilog.info(0x0000, 'testTag', `Succeeded in getting upperAge is: ${ageGroup.upperAge}`);
              // 根据年龄段刷新内容展示。如开发者有频繁使用到年龄段信息，这里则需缓存年龄段信息
            }
          } else {
            // 未成年人模式未开启，应用需跟随系统未成年人模式，展示内容不做限制
          }
        })
        .catch((error: BusinessError<Object>) => {
          dealGetMinorsInfoAllError(error);
        });
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the getMinorsProtectionInfo interface.');
}

function dealGetMinorsInfoAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to getMinorsProtectionInfo. Code: ${error.code}, message: ${error.message}`);
}
```

#### verifyMinorsProtectionCredential

verifyMinorsProtectionCredential(context: common.Context): Promise<boolean>

当用户需要调整应用的未成年人模式相关设置时，调用该方法拉起未成年人模式密码验证页面，验证身份。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common#context)

是

Context上下文。

应用可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)和[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)调用。

元服务可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。

**返回值：**

类型

说明

Promise<boolean>

Promise对象。返回true表示密码验证通过；返回false表示密码验证未通过。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

[1001502009](ArkTS错误码.md#section17561151616317)

Internal error.

[1009900002](ArkTS错误码.md#section5166694516)

The minors mode is not enabled.

**示例：**

```ets
import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    if (minorsProtection.supportMinorsMode()) {
      // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
      minorsProtection.verifyMinorsProtectionCredential(this.getUIContext().getHostContext())
        .then((result: boolean) => {
          hilog.info(0x0000, 'testTag', `Succeeded in getting verify result is: ${result.valueOf()}`);
          // 使用结果判断验密是否通过，执行后续流程
        })
        .catch((error: BusinessError<Object>) => {
          dealVerifyAllError(error);
        });
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the verifyMinorsProtectionCredential interface.');
}

function dealVerifyAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
}
```

#### leadToTurnOnMinorsMode

leadToTurnOnMinorsMode(context: common.Context): Promise<void>

应用提供开启未成年人模式入口，调用该方法拉起开启未成年人模式页面，引导用户开启未成年人模式。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common#context)

是

Context上下文。

应用可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)和[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)调用。

元服务可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。

**返回值：**

类型

说明

Promise<void>

Promise对象，无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

[1001502009](ArkTS错误码.md#section17561151616317)

Internal error.

[1009900003](ArkTS错误码.md#section191691561188)

The user canceled the operation.

[1009900005](ArkTS错误码.md#section35901828161314)

The minors mode is already on.

[1009900007](ArkTS错误码.md#section2076682413462)

Unsupported HUAWEI ID.

[1009900011](ArkTS错误码.md#section13666164864818)

Service not available.

**示例：**

```ets
import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    if (minorsProtection.supportMinorsMode()) {
      // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
      minorsProtection.leadToTurnOnMinorsMode(this.getUIContext().getHostContext())
        .then(() => {
          // 接口调用完成，如需显示弹窗，请在此处处理
        })
        .catch((error: BusinessError<Object>) => {
          dealTurnOnAllError(error);
        });
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the leadToTurnOnMinorsMode interface.');
}

function dealTurnOnAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to leadToTurnOnMinorsMode. Code: ${error.code}, message: ${error.message}`);
}
```

#### leadToTurnOffMinorsMode

leadToTurnOffMinorsMode(context: common.Context): Promise<void>

应用提供关闭未成年人模式入口，调用该方法拉起关闭未成年人模式页面，引导用户关闭未成年人模式。使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common#context)

是

Context上下文。

应用可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)和[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)调用。

元服务可支持的Context有：[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。

**返回值：**

类型

说明

Promise<void>

Promise对象，无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](ArkTS错误码.md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

[1001502009](ArkTS错误码.md#section17561151616317)

Internal error.

[1009900003](ArkTS错误码.md#section191691561188)

The user canceled the operation.

[1009900006](ArkTS错误码.md#section1451016215158)

The minors mode is already off.

[1009900011](ArkTS错误码.md#section13666164864818)

Service not available.

**示例：**

```ets
import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    if (minorsProtection.supportMinorsMode()) {
      // 此示例为代码片段，实际需在自定义组件实例中使用，以获取UIContext对象作为函数入参
      minorsProtection.leadToTurnOffMinorsMode(this.getUIContext().getHostContext())
        .then(() => {
          // 接口调用完成，如需显示弹窗，请在此处处理
        })
        .catch((error: BusinessError<Object>) => {
          dealTurnOffAllError(error);
        });
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the leadToTurnOffMinorsMode interface.');
}

function dealTurnOffAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to leadToTurnOffMinorsMode. Code: ${error.code}, message: ${error.message}`);
}
```