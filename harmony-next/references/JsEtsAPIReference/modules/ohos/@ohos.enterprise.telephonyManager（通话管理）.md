# @ohos.enterprise.telephonyManager（通话管理）

本模块提供通话管理能力。

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅适用于Stage模型。

本模块接口仅对设备管理应用开放，调用接口前需激活该应用，详情请参考[MDM Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-guide)。

全局通用限制类策略由restrictions提供，若要全局禁用通话，请参考[@ohos.enterprise.restrictions（限制类策略）](@ohos.enterprise.restrictions （限制类策略）.md)。

#### 导入模块

```ets
import { telephonyManager } from '@kit.MDMKit';
```

#### telephonyManager.setSimDisabled

setSimDisabled(admin: Want, slotId: number): void

禁用指定卡槽的SIM卡。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。slotIdnumber是卡槽ID，目前仅支持单卡槽设备和双卡槽设备，取值范围为0或1，其中0表示卡槽1，1表示卡槽2。

**错误码**：

请参见[企业设备管理错误码](../../errors/企业设备管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let slotId: number = 0;
  telephonyManager.setSimDisabled(wantTemp, slotId);
  console.info(`Succeeded in setting slotId: ${slotId} disabled.`);
} catch (err) {
  console.error(`Failed to set slotId disabled. Code: ${err.code}, message: ${err.message}`);
}
```

#### telephonyManager.setSimEnabled

setSimEnabled(admin: Want, slotId: number): void

解除指定卡槽的SIM卡禁用。使用setSimDisabled禁用SIM卡后，再用setSimEnabled启用SIM卡，需要到设置-移动网络-SIM卡管理界面手动打开SIM卡开关。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。slotIdnumber是卡槽ID，目前仅支持单卡槽设备和双卡槽设备，取值范围为0或1，其中0表示卡槽1，1表示卡槽2。

**错误码**：

请参见[企业设备管理错误码](../../errors/企业设备管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let slotId: number = 0;
  telephonyManager.setSimEnabled(wantTemp, slotId);
  console.info(`Succeeded in setting slotId: ${slotId} enabled.`);
} catch (err) {
  console.error(`Failed to set slotId enabled. Code: ${err.code}, message: ${err.message}`);
}
```

#### telephonyManager.isSimDisabled

isSimDisabled(admin: Want, slotId: number): boolean

查询指定卡槽是否禁用。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。slotIdnumber是卡槽ID，目前仅支持单卡槽设备和双卡槽设备，取值范围为0或1，其中0表示卡槽1，1表示卡槽2。

**返回值：**

类型说明boolean指定卡槽的禁用状态。true表示已被禁用，false表示未被禁用。

**错误码**：

请参见[企业设备管理错误码](../../errors/企业设备管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let slotId: number = 0;
  let result: boolean = telephonyManager.isSimDisabled(wantTemp, slotId);
  console.info(`Succeeded in querying slotId: ${slotId} is disabled or not, result: ${result}`);
} catch (err) {
  console.error(`Failed to query sim is disabled or not. Code: ${err.code}, message: ${err.message}`);
}
```

#### telephonyManager.addOutgoingCallPolicyNumbers

addOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void

添加通话呼出的允许或禁用名单，如果不添加名单，任意号码都可以呼出，添加后只有名单内的号码允许或禁止呼出。

以下情况下，通过本接口添加通话呼出的允许或禁用名单，会报策略冲突：

1. 已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了设备通话能力，再通过本接口添加通话呼出的禁用或允许名单，返回203错误码。通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口解除禁用设备通话能力后，可解除冲突。
1. 已经通过本接口设置了通话呼出的禁用名单，再通过本接口添加通话呼出允许名单，返回9200010错误码。通过[removeOutgoingCallPolicyNumbers](#ZH-CN_TOPIC_0000002497605594__telephonymanagerremoveoutgoingcallpolicynumbers)接口将之前设置的通话呼出禁用名单移除后，可解除冲突。
1. 已经通过本接口设置了通话呼出的允许名单，再通过本接口添加通话呼出禁用名单，返回9200010错误码。通过[removeOutgoingCallPolicyNumbers](#ZH-CN_TOPIC_0000002497605594__telephonymanagerremoveoutgoingcallpolicynumbers)接口将之前设置的通话呼出允许名单移除后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。policy[adminManager.Policy](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__policy20)是允许或禁用名单策略。BLOCK_LIST为禁用名单，TRUST_LIST为允许名单。numbersArray<string>是通话号码列表，当前仅支持全号码匹配。数组总长度不能超过1000。例如，若当前允许名单数组中已有100个号码，则最多支持通过该接口再添加900个。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../errors/企业设备管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.9200010A conflict policy has been configured.9200012Parameter verification failed.201Permission verification failed. The application does not have the permission required to call the API.203This function is prohibited by enterprise management policies.801Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';
import { adminManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
  let numbers: Array<string> = [
    //需根据实际情况进行替换
    "13112345678"
  ];
  telephonyManager.addOutgoingCallPolicyNumbers(wantTemp, policy, numbers);
  console.info('Succeeded in adding outgoing call policy.');
} catch (err) {
  console.error(`Failed to add outgoing call policy. Code: ${err.code}, message: ${err.message}`);
}
```

#### telephonyManager.removeOutgoingCallPolicyNumbers

removeOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void

移除通话呼出的允许或禁用名单，若在该名单尚未设置时进行移除，则会移除失败。

以下情况下，通过本接口移除通话呼出的允许或禁用名单，会报策略冲突：

已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了设备通话能力，再通过本接口移除通话呼出的禁用或允许名单，返回203错误码。通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口解除禁用设备通话能力后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。policy[adminManager.Policy](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__policy20)是允许或禁用名单策略。BLOCK_LIST为禁用名单，TRUST_LIST为允许名单。numbersArray<string>是待移除的通话号码数组。数组总长度不能超过1000。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../errors/企业设备管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.9200012Parameter verification failed.201Permission verification failed. The application does not have the permission required to call the API.203This function is prohibited by enterprise management policies.801Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';
import { adminManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
  let numbers: Array<string> = [
    //需根据实际情况进行替换
    "13112345678"
  ];
  telephonyManager.removeOutgoingCallPolicyNumbers(wantTemp, policy, numbers);
  console.info('Succeeded in removing outgoing call policy.');
} catch (err) {
  console.error(`Failed to remove outgoing call policy. Code: ${err.code}, message: ${err.message}`);
}
```

#### telephonyManager.getOutgoingCallPolicyNumbers

getOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy): Array<string>

获取通话呼出的允许或禁用名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。policy[adminManager.Policy](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__policy20)是允许或禁用名单策略。 BLOCK_LIST为禁用名单，TRUST_LIST为允许名单。

**返回值：**

类型说明Array<string>通话呼出禁用或允许名单的号码数组。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../errors/企业设备管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.801Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';
import { adminManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
  let numbers: Array<string> = telephonyManager.getOutgoingCallPolicyNumbers(wantTemp, policy);
  console.info(`Succeeded in getting outgoing call policy. result: ${JSON.stringify(numbers)}`);
} catch (err) {
  console.error(`Failed to get outgoing call policy. Code: ${err.code}, message: ${err.message}`);
}
```

#### telephonyManager.addIncomingCallPolicyNumbers

addIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void

添加通话呼入的允许或禁用名单，如果不添加名单，则任意号码都可以呼入，添加后仅名单内的号码允许或禁止呼入。

以下情况下，通过本接口添加通话呼入的允许或禁用名单，会报策略冲突：

1. 已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了设备通话能力，再通过本接口添加通话呼入的禁用或允许名单，返回203错误码。通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口解除禁用设备通话能力后，可解除冲突。
1. 已经通过本接口设置了通话呼入的禁用名单，再通过本接口添加通话呼入允许名单，返回9200010错误码。通过[removeIncomingCallPolicyNumbers](#ZH-CN_TOPIC_0000002497605594__telephonymanagerremoveincomingcallpolicynumbers)接口将之前设置的通话呼入禁用名单移除后，可解除冲突。
1. 已经通过本接口设置了通话呼入的允许名单，再通过本接口添加通话呼入禁用名单，返回9200010错误码。通过[removeIncomingCallPolicyNumbers](#ZH-CN_TOPIC_0000002497605594__telephonymanagerremoveincomingcallpolicynumbers)接口将之前设置的通话呼入允许名单移除后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。policy[adminManager.Policy](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__policy20)是允许或禁用名单策略。BLOCK_LIST为禁用名单，TRUST_LIST为允许名单。numbersArray<string>是通话号码列表，当前仅支持全号码匹配。数组总长度不能超过1000。例如，若当前允许名单数组中已有100个号码，则最多支持通过该接口再添加900个。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../errors/企业设备管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.9200010A conflict policy has been configured.9200012Parameter verification failed.201Permission verification failed. The application does not have the permission required to call the API.203This function is prohibited by enterprise management policies.801Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';
import { adminManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
  let numbers: Array<string> = [
    //需根据实际情况进行替换
    "13112345678"
  ];
  telephonyManager.addIncomingCallPolicyNumbers(wantTemp, policy, numbers);
  console.info('Succeeded in adding incoming call policy.');
} catch (err) {
  console.error(`Failed to add incoming call policy. Code: ${err.code}, message: ${err.message}`);
}
```

#### telephonyManager.removeIncomingCallPolicyNumbers

removeIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void

移除通话呼入的允许或禁用名单，若在该名单尚未设置时进行移除，则会移除失败。

以下情况下，通过本接口移除通话呼入的允许或禁用名单，会报策略冲突：

1. 已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了设备通话能力，再通过本接口移除通话呼入的禁用或允许名单，返回203错误码。通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口解除禁用设备通话能力后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。policy[adminManager.Policy](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__policy20)是允许或禁用名单策略。BLOCK_LIST为禁用名单，TRUST_LIST为允许名单。numbersArray<string>是待移除的通话号码数组。数组总长度不能超过1000。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../errors/企业设备管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.9200012Parameter verification failed.201Permission verification failed. The application does not have the permission required to call the API.203This function is prohibited by enterprise management policies.801Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';
import { adminManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
  let numbers: Array<string> = [
    //需根据实际情况进行替换
    "13112345678"
  ];
  telephonyManager.removeIncomingCallPolicyNumbers(wantTemp, policy, numbers);
  console.info('Succeeded in removing incoming call policy.');
} catch (err) {
  console.error(`Failed to add remove incoming call policy. Code: ${err.code}, message: ${err.message}`);
}
```

#### telephonyManager.getIncomingCallPolicyNumbers

getIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy): Array<string>

获取通话呼入的允许或禁用名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。policy[adminManager.Policy](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__policy20)是允许或禁用名单策略。BLOCK_LIST为禁用名单，TRUST_LIST为允许名单。

**返回值：**

类型说明Array<string>通话呼入禁用或允许名单的号码数组。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](../../errors/企业设备管理错误码.md)和[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.801Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';
import { adminManager } from '@kit.MDMKit';

let wantTemp: Want = {
  //需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
  let numbers: Array<string> = telephonyManager.getIncomingCallPolicyNumbers(wantTemp, policy);
  console.info(`Succeeded in getting incoming call policy. result: ${JSON.stringify(numbers)}`);
} catch (err) {
  console.error(`Failed to get incoming call policy. Code: ${err.code}, message: ${err.message}`);
}
```