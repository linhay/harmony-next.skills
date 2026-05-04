# @ohos.enterprise.applicationManager（应用管理）

本模块提供应用管理能力，包括添加应用运行禁止名单、获取应用运行禁止名单、移除应用运行禁止名单等。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../guides/MDM Kit开发指南.md)。[applicationManager.isAppKioskAllowed](#ZH-CN_TOPIC_0000002522081688__applicationmanagerisappkioskallowed20)除外，该接口对所有应用开放。

#### 导入模块

```ets
import { applicationManager } from '@kit.MDMKit';
```

#### applicationManager.addDisallowedRunningBundlesSync

addDisallowedRunningBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void

添加应用至应用运行禁止名单，添加至禁止名单的应用不允许在当前/指定用户下运行。从API version 21开始，如果应用运行允许名单[addallowedRunningBundles](#ZH-CN_TOPIC_0000002522081688__applicationmanageraddallowedrunningbundles21)非空，就不能再通过本接口添加应用运行禁止名单，否则会报9200010冲突错误码。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIds | Array<string> | 是 | 应用ID数组，指定具体应用。 说明： 从API version 21版本开始，支持传入应用的appId和appIdentifier，推荐使用appIdentifier。API version 20及之前版本，仅支持appId。 |
| accountId | number | 否 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 - 调用接口时，若传入accountId，表示指定用户。 - 调用接口时，若未传入accountId，表示当前用户。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码]([企业设备管理错误码](../../errors/企业设备管理错误码.md).md)和[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let appIds: Array<string> = ['com.example.******_******/******5t5CoBM='];

try {
  applicationManager.addDisallowedRunningBundlesSync(wantTemp, appIds);
  console.info('Succeeded in adding disallowed running bundles.');
} catch (err) {
  console.error(`Failed to add disallowed running bundles. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.removeDisallowedRunningBundlesSync

removeDisallowedRunningBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void

将应用从当前/指定用户下的应用运行禁止名单中移除。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIds | Array<string> | 是 | 应用ID数组，指定具体应用。 说明： 从API version 21版本开始，数组中的元素支持使用appId和appIdentifier，仅移除传入的appId（或appIdentifier），不会移除同一应用的appIdentifier（或appId）。API version 20及之前版本，数组中的元素只支持使用appId。 |
| accountId | number | 否 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 - 调用接口时，若传入accountId，表示指定用户。 - 调用接口时，若未传入accountId，表示当前用户。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let appIds: Array<string> = ['com.example.******_******/******5t5CoBM='];

try {
  applicationManager.removeDisallowedRunningBundlesSync(wantTemp, appIds);
  console.info('Succeeded in removing disallowed running bundles.');
} catch (err) {
  console.error(`Failed to remove disallowed running bundles. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.getDisallowedRunningBundlesSync

getDisallowedRunningBundlesSync(admin: Want, accountId?: number): Array<string>

获取当前/指定用户下的应用运行禁止名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 否 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 - 调用接口时，若传入accountId，表示指定用户。 - 调用接口时，若未传入accountId，表示当前用户。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回当前/指定用户下的应用运行禁止名单。 说明： API version 20及之前版本，返回值为应用appId列表。从API version 21版本开始，返回值为应用appId或appIdentifier列表。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<string> = applicationManager.getDisallowedRunningBundlesSync(wantTemp);
  console.info(`Succeeded in getting disallowed running bundles, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed running bundles. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.addAllowedRunningBundles21+

addAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void

添加应用至应用运行允许名单，添加至允许名单的应用允许在指定用户下运行，不在允许名单的应用不允许在指定用户下运行。

1.

由于MDM Kit下大多数接口仅对MDM应用开放，本接口使用时，请将MDM应用同时添加至应用运行允许名单，否则会导致MDM应用不允许运行，阻塞接口调用。接口是否仅对MDM应用开放请查看对应的模块说明。

1.

如果应用运行禁止名单非空，不支持再使用本接口添加应用运行允许名单，否则会报9200010冲突错误码。应用运行禁止名单相关接口包括[addDisallowedRunningBundlesSync](#ZH-CN_TOPIC_0000002522081688__applicationmanageradddisallowedrunningbundlessync)。

1.

本接口仅对三方应用生效，系统应用不受该名单管控，默认可以运行。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIdentifiers | Array<string> | 是 | 应用唯一标识符的数组，可以通过接口[bundleManager.getinstalledbundlelist](@ohos.enterprise.bundleManager（包管理）.md#ZH-CN_TOPIC_0000002529445553__bundlemanagergetinstalledbundlelist20)获取bundleInfo.signatureInfo.appIdentifier。 取值范围： - 单个用户下该名单总数不能超过200。例如100用户下已经设置了50个、101用户未设置，则100用户还能再设置150个，101用户还能再设置200个。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let appIdentifiers: Array<string> = ['0123456789123456789'];

try {
  applicationManager.addAllowedRunningBundles(wantTemp, appIdentifiers, 100);
  console.info('Succeeded in adding allowed running bundles.');
} catch (err) {
  console.error(`Failed to add allowed running bundles. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.removeAllowedRunningBundles21+

removeAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void

将应用从指定用户下的应用运行允许名单中移除。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIdentifiers | Array<string> | 是 | 应用唯一标识符的数组。可以通过接口[bundleManager.getinstalledbundlelist](@ohos.enterprise.bundleManager（包管理）.md#ZH-CN_TOPIC_0000002529445553__bundlemanagergetinstalledbundlelist20)获取bundleInfo.signatureInfo.appIdentifier。取值范围：数组长度不能超过200。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let appIdentifiers: Array<string> = ['0123456789123456789'];

try {
  applicationManager.removeAllowedRunningBundles(wantTemp, appIdentifiers, 100);
  console.info('Succeeded in removing allowed running bundles.');
} catch (err) {
  console.error(`Failed to remove allowed running bundles. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.getAllowedRunningBundles21+

getAllowedRunningBundles(admin: Want, accountId: number): Array<string>

获取指定用户下的应用运行允许名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回指定用户下的应用运行允许名单。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<string> = applicationManager.getAllowedRunningBundles(wantTemp, 100);
  console.info(`Succeeded in getting allowed running bundles, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get allowed running bundles. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.addAutoStartApps

addAutoStartApps(admin: Want, autoStartApps: Array<Want>): void

为当前用户添加开机自启动应用名单。通过本接口添加至自启动名单的应用，禁止用户在设备上手动取消应用自启动（用户通过设备上设置->应用和元服务->应用启动管理，取消应用自启动），但可通过[removeAutoStartApps](#ZH-CN_TOPIC_0000002522081688__applicationmanagerremoveautostartapps)接口将应用从自启动名单中移除。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 对于API version 20及之前的版本，该接口在PC/2in1设备可正常调用，在其他设备中调用无效果。从API version 21开始，该接口在Phone、Tablet、PC/2in1中均可正常使用。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| autoStartApps | Array<Want> | 是 | 开机自启动应用数组。数组长度上限为10。例如：如果名单中已有5个应用，则最多再通过本接口设置5个。Want中必须包含bundleName和abilityName。Ability支持UIAbility和ServiceExtensionAbility。当abilities标签中exported属性值为false时，不支持拉起Ability。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let autoStartApps: Array<Want> = [
  {
    // 需根据实际情况进行替换
    bundleName: 'com.example.autoStartApplication',
    abilityName: 'EntryAbility'
  }
];

try {
  applicationManager.addAutoStartApps(wantTemp, autoStartApps);
  console.info('Succeeded in adding auto start applications.');
} catch(err) {
  console.error(`Failed to add auto start applications. Code: ${err.code}, message: ${err.message}`);
}
```

#### applicationManager.removeAutoStartApps

removeAutoStartApps(admin: Want, autoStartApps: Array<Want>): void

为当前用户删除开机自启动应用名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 对于API version 20及之前的版本，该接口在PC/2in1设备可正常调用，在其他设备中调用无效果。从API version 21开始，该接口在Phone、Tablet、PC/2in1中均可正常使用。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| autoStartApps | Array<Want> | 是 | 开机自启动应用数组。Want中必须包含bundleName和abilityName。Ability支持UIAbility和ServiceExtensionAbility。当abilities标签中exported属性值为false时，不支持拉起Ability。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let autoStartApps: Array<Want> = [
  {
    // 需根据实际情况进行替换
    bundleName: 'com.example.autoStartApplication',
    abilityName: 'EntryAbility'
  }
];

try {
  applicationManager.removeAutoStartApps(wantTemp, autoStartApps);
  console.info('Succeeded in removing auto start applications.');
} catch(err) {
  console.error(`Failed to remove auto start applications. Code: ${err.code}, message: ${err.message}`);
}
```

#### applicationManager.removeAutoStartApps20+

removeAutoStartApps(admin: Want, autoStartApps: Array<Want>, accountId: number): void

删除指定用户的开机自启动应用名单中的指定应用。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 对于API version 20及之前的版本，该接口在PC/2in1设备可正常调用，在其他设备中调用无效果。从API version 21开始，该接口在Phone、Tablet、PC/2in1中均可正常使用。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| autoStartApps | Array<Want> | 是 | 开机自启动应用名单数组。Want中必须包含bundleName和abilityName。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let autoStartApps: Array<Want> = [
  // 需根据实际情况进行替换
  {
    bundleName: 'com.example.autoStartApplication',
    abilityName: 'EntryAbility'
  }
];

try {
  applicationManager.removeAutoStartApps(wantTemp, autoStartApps, 100);
  console.info('Succeeded in removing auto start applications.');
} catch(err) {
  console.error(`Failed to remove auto start applications. Code: ${err.code}, message: ${err.message}`);
}
```

#### applicationManager.getAutoStartApps

getAutoStartApps(admin: Want): Array<Want>

查询当前用户开机自启动应用名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 对于API version 20及之前的版本，该接口在PC/2in1设备可正常调用，在其他设备中调用无效果。从API version 21开始，该接口在Phone、Tablet、PC/2in1中均可正常使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<Want> | 应用自启动名单数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let res: Array<Want> = applicationManager.getAutoStartApps(wantTemp);
  console.info(`Succeeded in adding auto start apps: ${JSON.stringify(res)}`);
} catch(err) {
  console.error(`Failed to auto start apps. Code: ${err.code}, message: ${err.message}`);
}
```

#### applicationManager.addAutoStartApps20+

addAutoStartApps(admin: Want, autoStartApps: Array<Want>, accountId: number, disallowModify: boolean): void

为指定用户添加开机自启动应用名单，并设置是否禁止该用户手动取消应用自启动（用户通过设备上设置->应用和元服务->应用启动管理，取消应用自启动）。

通过本接口、[addAutoStartApps](#ZH-CN_TOPIC_0000002522081688__applicationmanageraddautostartapps)接口均可添加开机自启动应用名单，两个接口的设置可同时生效。同一用户下，开机自启动应用名单最多支持包含10个应用。例如：若当前名单中已有3个应用，则最多还能通过本接口为当前用户添加7个应用。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 对于API version 20及之前的版本，该接口在PC/2in1设备可正常调用，在其他设备中调用无效果。从API version 21开始，该接口在Phone、Tablet、PC/2in1中均可正常使用。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| autoStartApps | Array<Want> | 是 | 开机自启动应用名单数组，数组总长度不超过10。Want中必须包含bundleName和abilityName。Ability支持UIAbility和ServiceExtensionAbility。当abilities标签中exported属性值为false时，不支持拉起Ability。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |
disallowModifyboolean是是否禁止用户手动取消应用自启动，true表示禁止，false表示允许。设置为允许后，用户可通过设备上设置->应用和元服务->应用启动管理，取消应用自启动。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let autoStartApps: Array<Want> = [
  // 需根据实际情况进行替换
  {
    bundleName: 'com.example.autoStartApplication',
    abilityName: 'EntryAbility'
  }
];

try {
  applicationManager.addAutoStartApps(wantTemp, autoStartApps, 100, true);
  console.info('Succeeded in adding auto start applications and set disllowModify.');
} catch(err) {
  console.error(`Failed to add auto start applications and set disallowModify. Code: ${err.code}, message: ${err.message}`);
}
```

#### applicationManager.getAutoStartApps20+

getAutoStartApps(admin: Want, accountId: number): Array<Want>

查询指定用户下的开机自启动应用名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 对于API version 20及之前的版本，该接口在PC/2in1设备可正常调用，在其他设备中调用无效果。从API version 21开始，该接口在Phone、Tablet、PC/2in1中均可正常使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<Want> | 应用自启动名单数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let res: Array<Want> = applicationManager.getAutoStartApps(wantTemp, 100);
  console.info(`Succeeded in getting auto start apps: ${JSON.stringify(res)}`);
} catch(err) {
  console.error(`Failed to get auto start apps. Code: ${err.code}, message: ${err.message}`);
}
```

#### applicationManager.isModifyAutoStartAppsDisallowed20+

isModifyAutoStartAppsDisallowed(admin: Want, autoStartApp: Want, accountId: number): boolean

查询指定用户是否禁止取消应用自启动。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 对于API version 20及之前的版本，该接口在PC/2in1设备可正常调用，在其他设备中调用无效果。从API version 21开始，该接口在Phone、Tablet、PC/2in1中均可正常使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| autoStartApp | Want | 是 | 开机自启动应用。Want中必须包含bundleName和abilityName。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否禁止用户取消应用自启动，true表示禁止，false表示允许。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let autoStartApp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.autoStartApplication',
  abilityName: 'EntryAbility'
};

try {
  let res: boolean = applicationManager.isModifyAutoStartAppsDisallowed(wantTemp, autoStartApp, 100);
  console.info(`Succeeded in getting disallow modify auto start app: ${JSON.stringify(res)}`);
} catch(err) {
  console.error(`Failed to get disallow modify auto start app. Code: ${err.code}, message: ${err.message}`);
}
```

#### applicationManager.addKeepAliveApps14+

addKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number): void

添加保活应用名单，添加后将自动保活应用进程。在开机和应用被杀死后，由系统主动拉起应用进程。添加至名单后的应用，需要[接入状态栏](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/statusbar-extension-guide)，保活才能生效。通过本接口添加至保活名单的应用，禁止用户在设备上手动取消保活（用户通过设备上设置->应用和元服务->应用常驻管理，取消应用保活），但可通过[removeKeepAliveApps](#ZH-CN_TOPIC_0000002522081688__applicationmanagerremovekeepaliveapps14)接口将应用从保活名单中移除。如果将应用添加至应用禁止运行名单[addDisallowedRunningBundlesSync](#ZH-CN_TOPIC_0000002522081688__applicationmanageradddisallowedrunningbundlessync)，就不能将应用添加至保活应用名单，否则会报9200010冲突错误码。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleNames | Array<string> | 是 | 应用包名数组，指定需要添加至保活名单的应用，最大支持5个。应用需要满足条件：安装在普通用户下且应用接入状态栏开放服务。否则，会报错误码9201005。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9201005 | Add keep alive applications failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let bundleNames: Array<string> = ['com.example.myapplication'];

try {
  applicationManager.addKeepAliveApps(wantTemp, bundleNames, 100);
  console.info('Succeeded in adding keep alive apps.');
} catch (err) {
  console.error(`Failed to add keep alive apps. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.addKeepAliveApps20+

addKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number, disallowModify: boolean): void

添加保活应用名单，并设置是否禁止用户手动取消保活，添加后将自动保活应用进程。在开机和应用被杀死后，由系统主动拉起应用进程。

通过本接口、[addKeepAliveApps](#ZH-CN_TOPIC_0000002522081688__applicationmanageraddkeepaliveapps14)接口均可添加保活应用名单，两个接口的设置可同时生效。同一用户下，保活应用名单最多支持包含5个应用。例如：若当前名单中已有3个应用，则最多还能通过本接口为当前用户添加2个应用。

如果通过[addDisallowedRunningBundlesSync](#ZH-CN_TOPIC_0000002522081688__applicationmanageradddisallowedrunningbundlessync)接口将应用添加至应用禁止运行名单，就不能将应用添加至保活应用名单，否则会报9200010冲突错误码。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleNames | Array<string> | 是 | 应用包名数组，指定需要添加至保活名单的应用，最大支持5个。 应用需要满足条件：安装在1用户下（1用户是支持三方应用单例运行的用户），且应用接入后台服务；或者安装在普通用户下且应用接入状态栏开放服务。否则，会报错误码9201005。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |
disallowModifyboolean是是否禁止用户手动取消应用保活，true表示禁止，false表示允许。设置为允许后，用户可通过设备上设置->应用和元服务->应用常驻管理，取消应用保活。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9201005 | Add keep alive applications failed. |
| 201 | Permission verification failed.The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 需根据实际情况进行替换
let bundleNames: Array<string> = ['com.example.myapplication'];

try {
  applicationManager.addKeepAliveApps(wantTemp, bundleNames, 100, true);
  console.info('Succeeded in adding keep alive apps and set disallowModify.');
} catch (err) {
  console.error(`Failed to add keep alive apps and set disallowModify. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.removeKeepAliveApps14+

removeKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number): void

移除保活应用名单中的指定应用。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备上生效，在其他设备中调用无效果。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleNames | Array<string> | 是 | 应用包名数组，指定需要移除保活的应用，最大支持5个。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let bundleNames: Array<string> = ['com.example.myapplication'];

try {
  applicationManager.removeKeepAliveApps(wantTemp, bundleNames, 100);
  console.info('Succeeded in removing keep alive apps.');
} catch (err) {
  console.error(`Failed to remove keep alive apps. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.getKeepAliveApps14+

getKeepAliveApps(admin: Want, accountId: number): Array<string>

获取保活应用包名。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备上生效，在其他设备中调用无效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回指定用户下保活应用的包名。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<string> = applicationManager.getKeepAliveApps(wantTemp, 100);
  console.info('Succeeded in getting keep alive apps.');
} catch (err) {
  console.error(`Failed to get keep alive apps. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.isModifyKeepAliveAppsDisallowed20+

isModifyKeepAliveAppsDisallowed(admin: Want, accountId: number, bundleName: string): boolean

查询应用是否禁止取消保活。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备上生效，在其他设备中调用无效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |
bundleNamestring是查询的应用包名。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否禁止用户手动取消应用保活，true表示禁止，false表示允许。设置为允许后，用户可通过设备上设置->应用和元服务->应用常驻管理，取消应用保活。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 需根据实际情况进行替换
let keepAliveApp: string = 'com.example.keepAliveApplication';

try {
  let res: boolean = applicationManager.isModifyKeepAliveAppsDisallowed(wantTemp, 100, keepAliveApp);
  console.info(`Succeeded in getting disallow modify keep alive app: ${JSON.stringify(res)}`);
} catch(err) {
  console.error(`Failed to get disallow modify keep alive app. Code: ${err.code}, message: ${err.message}`);
}
```

#### applicationManager.clearUpApplicationData20+

clearUpApplicationData(admin: Want, bundleName: string, appIndex: number, accountId: number): void

清除应用产生的所有数据。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 应用包名，指定需要清除数据的应用包名。 |
| appIndex | number | 是 | 应用分身索引，取值范围：大于等于0的整数。 appIndex可以通过@ohos.bundle.bundleManager中的getAppCloneIdentity等接口来获取。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0的整数。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { applicationManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let bundleName: string = 'com.example.exampleapplication';

try {
  // 需根据实际情况进行替换
  applicationManager.clearUpApplicationData(wantTemp, bundleName, 0, 100);
  console.info('Succeeded in clearing up application data.');
} catch (err) {
  console.error(`Failed to clear up application data. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.setAllowedKioskApps20+

setAllowedKioskApps(admin: Want, appIdentifiers: Array<string>): void

设置允许在Kiosk模式下运行的应用。

Kiosk模式为系统层面提供的一种应用运行模式，该模式下会将设备锁定在单个应用或者一组应用运行，同时对锁屏状态、状态栏、手势操作和关键功能进行控制，防止用户在设备上启动其它应用或执行其它操作。

**需要权限：** ohos.permission.ENTERPRISE_SET_KIOSK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [配置](../../guides/多应用管控.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIdentifiers | Array<string> | 是 | 应用[唯一标识符](../../topics/misc/BundleInfo.md#ZH-CN_TOPIC_0000002529284625__signatureinfo)的数组，可以通过接口bundleManager.getBundleInfo获取bundleInfo.signatureInfo.appIdentifier。重复设置时，新设置的数组会覆盖旧的设置，最多设置200个。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { applicationManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 需根据实际情况进行替换
  let appIdentifiers: Array<string> = ['6917****3569'];
  applicationManager.setAllowedKioskApps(wantTemp, appIdentifiers);
  console.info('Succeeded in setting allowed kiosk apps.');
} catch (err) {
  console.error(`Failed to set allowed kiosk apps. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.getAllowedKioskApps20+

getAllowedKioskApps(admin: Want): Array<string>

获取允许在Kiosk模式下运行的应用。

**需要权限：** ohos.permission.ENTERPRISE_SET_KIOSK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 允许在Kiosk模式下运行的应用[唯一标识符](../../topics/misc/BundleInfo.md#ZH-CN_TOPIC_0000002529284625__signatureinfo)清单。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { applicationManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.edmtest',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let appIdentifiers: Array<string> = applicationManager.getAllowedKioskApps(wantTemp);
  console.info(`Succeeded in getting allowed kiosk apps, appIdentifiers: ${JSON.stringify(appIdentifiers)}`);
} catch (err) {
  console.error(`Failed to get allowed kiosk apps. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.isAppKioskAllowed20+

isAppKioskAllowed(appIdentifier: string): boolean

查询某应用是否允许在Kiosk模式下运行。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appIdentifier | string | 是 | 应用[唯一标识符](../../topics/misc/BundleInfo.md#ZH-CN_TOPIC_0000002529284625__signatureinfo)，可以通过接口bundleManager.getBundleInfo获取bundleInfo.signatureInfo.appIdentifier。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示允许在Kiosk模式下运行。false表示不允许在Kiosk模式下运行。 |

**示例：**

```ets
import { applicationManager } from '@kit.MDMKit';

try {
  // 需根据实际情况进行替换
  let isAllowed: boolean = applicationManager.isAppKioskAllowed('6917****3569');
  console.info(`Succeeded in querying if the app is allowed kiosk, isAllowed: ${isAllowed}`);
} catch (err) {
  console.error(`Failed to query if the app is allowed kiosk. Code is ${err.code}, message is ${err.message}`);
}
```

#### applicationManager.setKioskFeatures20+

setKioskFeatures(admin: Want, features: Array<KioskFeature>): void

设置Kiosk模式的特征。通过本接口可以控制在[Kiosk模式](@ohos.app.ability.kioskManager (Kiosk模式管理).md#ZH-CN_TOPIC_0000002522080560__kioskmanagerenterkioskmode)下能否进入通知中心和控制中心。非Kiosk模式时，本接口可以正常调用，但是不会生效，进入Kiosk模式后才会生效。

**需要权限：** ohos.permission.ENTERPRISE_SET_KIOSK

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

设备行为差异： 该接口在PC/2in1设备上调用无效果，在Phone和Tablet设备上可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| features | Array<KioskFeature> | 是 | Kiosk模式的特征集合。 当传入空数组时，系统会清空之前下发过的特征，恢复到Kiosk模式的默认状态，即禁用通知中心、控制中心和最近任务栏等能力。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed.The application does not have the permission required to call the API. |

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { applicationManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let kioskFeatures: Array<applicationManager.KioskFeature> = [];
kioskFeatures.push(applicationManager.KioskFeature.ALLOW_NOTIFICATION_CENTER);
kioskFeatures.push(applicationManager.KioskFeature.ALLOW_CONTROL_CENTER);
try {
  applicationManager.setKioskFeatures(wantTemp, kioskFeatures);
  console.info('Succeeded in setting kiosk feature.');
} catch (err) {
  console.error(`Failed to set kiosk feature. Code is ${err.code}, message is ${err.message}`);
}
```

#### KioskFeature20+

Kiosk模式的特征。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALLOW_NOTIFICATION_CENTER | 1 | 允许进入通知中心。 |
| ALLOW_CONTROL_CENTER | 2 | 允许进入控制中心。 |

#### applicationManager.addUserNonStopApps22+

addUserNonStopApps(admin: Want, applicationInstances: Array<[common.ApplicationInstance](@ohos.enterprise.common（Enterprise公共模块）.md#ZH-CN_TOPIC_0000002497605588__applicationinstance)>): void

为指定用户添加不可关停应用名单，仅可对已安装应用设置该策略。若参数列表中存在未安装应用，则返回9200012错误码。若设置策略后，名单中有应用被卸载，则卸载的应用将从名单中移除。若添加已存在于名单中的应用，返回成功，但已设置策略名单中不会重复添加该应用。

不可关停应用：用户不能在任务中心上划关闭应用；在设置-应用和元服务中点击应用名称进入详情页面后，页面中的强行停止按钮呈灰色不可用。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet中可正常调用，在其他设备中调用无效果。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| applicationInstances | Array<[common.ApplicationInstance](@ohos.enterprise.common（Enterprise公共模块）.md#ZH-CN_TOPIC_0000002497605588__applicationinstance)> | 是 | 不可关停应用名单数组。不可关停应用名单最多支持包含10个应用，该数量限制不区分用户，即所有用户下添加应用的总和的最大限制为10个。例如：若当前名单中已有3个应用，则最多还能通过本接口为指定用户添加7个应用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let applicationInstances: Array<common.ApplicationInstance> = [
  // 需根据实际情况进行替换
  {
    appIdentifier: '0123456789123456789',
    accountId: 100,
    appIndex: 0
  }
];

try {
  applicationManager.addUserNonStopApps(wantTemp, applicationInstances);
  console.info('Succeeded in adding UserNonStop applications.');
} catch(err) {
  console.error(`Failed to add UserNonStop applications. Code: ${err.code}, message: ${err.message}`);
}
```

#### applicationManager.removeUserNonStopApps22+

removeUserNonStopApps(admin: Want, applicationInstances: Array<[common.ApplicationInstance](@ohos.enterprise.common（Enterprise公共模块）.md#ZH-CN_TOPIC_0000002497605588__applicationinstance)>): void

为指定用户删除不可关停应用名单。执行删除策略时，若参数列表中包含未安装应用，删除操作仍能成功执行；已安装的应用将被删除，未安装的应用不影响删除操作。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet中可正常调用，在其他设备中调用无效果。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| applicationInstances | Array<[common.ApplicationInstance](@ohos.enterprise.common（Enterprise公共模块）.md#ZH-CN_TOPIC_0000002497605588__applicationinstance)> | 是 | 不可关停应用名单数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let applicationInstances: Array<common.ApplicationInstance> = [
  // 需根据实际情况进行替换
  {
    appIdentifier: '0123456789123456789',
    accountId: 100,
    appIndex: 0
  }
];

try {
  applicationManager.removeUserNonStopApps(wantTemp, applicationInstances);
  console.info('Succeeded in removing UserNonStop applications.');
} catch(err) {
  console.error(`Failed to remove UserNonStop applications. Code: ${err.code}, message: ${err.message}`);
}
```

#### applicationManager.getUserNonStopApps22+

getUserNonStopApps(admin: Want): Array<[common.ApplicationInstance](@ohos.enterprise.common（Enterprise公共模块）.md#ZH-CN_TOPIC_0000002497605588__applicationinstance)>

获取当前设备下所有用户不可关停应用名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet中可正常调用，在其他设备中调用无效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[common.ApplicationInstance](@ohos.enterprise.common（Enterprise公共模块）.md#ZH-CN_TOPIC_0000002497605588__applicationinstance)> | 不可关停应用名单数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<common.ApplicationInstance> = applicationManager.getUserNonStopApps(wantTemp);
  console.info(`Succeeded in getting UserNonStop applications, result : ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to get UserNonStop applications. Code: ${err.code}, message: ${err.message}`);
}
```

#### applicationManager.addFreezeExemptedApps22+

addFreezeExemptedApps(admin: Want, applicationInstances: Array<[common.ApplicationInstance](@ohos.enterprise.common（Enterprise公共模块）.md#ZH-CN_TOPIC_0000002497605588__applicationinstance)>): void

为指定用户添加后台防冻结应用名单，仅可对已安装应用设置该策略，该策略重启后失效。若参数列表中存在未安装应用，则返回9200012错误码。若设置策略后，名单中有应用被卸载，则卸载的应用将从名单中移除。若添加已存在于名单中的应用，返回成功，但已设置策略名单中不会重复添加该应用。

冻结操作：对目标应用的挂起、软件资源代理、硬件资源代理和高功耗管控等操作。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet中可正常调用，在其他设备中调用无效果。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| applicationInstances | Array<[common.ApplicationInstance](@ohos.enterprise.common（Enterprise公共模块）.md#ZH-CN_TOPIC_0000002497605588__applicationinstance)> | 是 | 后台防冻结应用名单数组，后台防冻结应用名单最多支持包含10个应用，该数量限制不区分用户，即所有用户下添加应用的总和的最大限制为10个。例如：若当前名单中已有3个应用，则最多还能通过本接口为指定用户添加7个应用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let applicationInstances: Array<common.ApplicationInstance> = [
  // 需根据实际情况进行替换
  {
    appIdentifier: '0123456789123456789',
    accountId: 100,
    appIndex: 0
  }
];

try {
  applicationManager.addFreezeExemptedApps(wantTemp, applicationInstances);
  console.info('Succeeded in adding FreezeExempted applications.');
} catch(err) {
  console.error(`Failed to add FreezeExempted applications. Code: ${err.code}, message: ${err.message}`);
}
```

#### applicationManager.removeFreezeExemptedApps22+

removeFreezeExemptedApps(admin: Want, applicationInstances: Array<[common.ApplicationInstance](@ohos.enterprise.common（Enterprise公共模块）.md#ZH-CN_TOPIC_0000002497605588__applicationinstance)>): void

为指定用户删除后台防冻结应用名单。执行删除策略时，若参数列表中包含未安装应用，删除操作仍能成功执行；已安装的应用将被删除，未安装的应用不影响删除操作。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet中可正常调用，在其他设备中调用无效果。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](../../guides/多应用管控.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| applicationInstances | Array<[common.ApplicationInstance](@ohos.enterprise.common（Enterprise公共模块）.md#ZH-CN_TOPIC_0000002497605588__applicationinstance)> | 是 | 后台防冻结应用名单数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let applicationInstances: Array<common.ApplicationInstance> = [
  // 需根据实际情况进行替换
  {
    appIdentifier: '0123456789123456789',
    accountId: 100,
    appIndex: 0
  }
];

try {
  applicationManager.removeFreezeExemptedApps(wantTemp, applicationInstances);
  console.info('Succeeded in removing FreezeExempted applications.');
} catch(err) {
  console.error(`Failed to remove FreezeExempted applications. Code: ${err.code}, message: ${err.message}`);
}
```

#### applicationManager.getFreezeExemptedApps22+

getFreezeExemptedApps(admin: Want): Array<[common.ApplicationInstance](@ohos.enterprise.common（Enterprise公共模块）.md#ZH-CN_TOPIC_0000002497605588__applicationinstance)>

获取当前设备下所有用户后台防冻结应用名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet中可正常调用，在其他设备中调用无效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[common.ApplicationInstance](@ohos.enterprise.common（Enterprise公共模块）.md#ZH-CN_TOPIC_0000002497605588__applicationinstance)> | 后台防冻结应用名单数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: Array<common.ApplicationInstance> = applicationManager.getFreezeExemptedApps(wantTemp);
  console.info(`Succeeded in getting FreezeExempted applications, result : ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to get FreezeExempted applications. Code: ${err.code}, message: ${err.message}`);
}
```

**applicationManager.setAbilityDisabled23+**

setAbilityDisabled(admin: Want, bundleName: string, accountId: number, abilityName: string, isDisabled: boolean): void

设置是否禁用指定应用（系统应用和三方应用均支持）的Ability组件。当前仅支持UIAbility类型，禁用后无法拉起此Ability组件的用户界面。

需要权限： ohos.permission.ENTERPRISE_MANAGE_APPLICATION

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

模型约束： 此接口仅可在Stage模型下使用。

冲突规则： [配置](../../guides/多应用管控.md#规则3配置)。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 应用包名，指定是否禁用的应用包名。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0的整数。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |
| abilityName | string | 是 | 表示要禁用/解除禁用的Ability组件名（当前仅支持UIAbility）。 |
| isDisabled | boolean | 是 | 是否禁用该Ability组件。true表示禁用该Ability组件，false表示解除禁用该Ability组件。 |

错误码：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

示例：

```ets
import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 需根据实际情况进行替换
  let bundleName: string = "com.example.exampleapplication";
  let accountId: number = 100;
  let abilityName: string = "EntryAbility";
  applicationManager.setAbilityDisabled(wantTemp, bundleName, accountId, abilityName, true);
  console.info('Succeeded in setting ability disabled');
} catch(err) {
  console.error(`Failed to set ability disabled. Code: ${err.code}, message: ${err.message}`);
}
```

**applicationManager.isAbilityDisabled23+**

isAbilityDisabled(admin: Want, bundleName: string, accountId: number, abilityName: string): boolean

获取指定应用（系统应用和三方应用均支持）的Ability组件是否被禁用。

需要权限： ohos.permission.ENTERPRISE_MANAGE_APPLICATION

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 应用包名，指定是否禁用的应用包名。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0的整数。 accountId可以通过@ohos.account.osAccount中的getOsAccountLocalId等接口来获取。 |
| abilityName | string | 是 | 表示要禁用/解除禁用的Ability组件名称（当前仅支持UIAbility）。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 该能力是否禁用。true表示该Ability组件被禁用，false表示该Ability组件未被禁用。 |

错误码：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

示例：

```ets
import { applicationManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 需根据实际情况进行替换
  let bundleName: string = "com.example.exampleapplication";
  let accountId: number = 100;
  let abilityName: string = "EntryAbility";
  let isDisabled: boolean = applicationManager.isAbilityDisabled(wantTemp, bundleName, accountId, abilityName);
  console.info(`Succeeded in querying whether the ability is disabled, isDisabled: ${isDisabled}`);
} catch(err) {
  console.error(`Failed to query whether the ability is disabled. Code: ${err.code}, message: ${err.message}`);
}
```