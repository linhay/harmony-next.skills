# @ohos.enterprise.adminManager（admin权限管理）

本模块为企业MDM应用提供admin权限管理能力，包括激活/解除激活admin权限、事件订阅、委托授权等。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅对设备管理应用开放，具体请参考[MDM Kit开发指南](../../guides/MDM Kit开发指南.md)。

#### 导入模块

```ets
import { adminManager } from '@kit.MDMKit';
```

#### adminManager.disableAdmin

disableAdmin(admin: Want, userId?: number): Promise<void>

解除激活指定用户的设备管理应用。使用Promise异步回调。

需要权限： ohos.permission.MANAGE_ENTERPRISE_DEVICE_ADMIN（仅系统应用支持申请）或ohos.permission.START_PROVISIONING_MESSAGE或ohos.permission.ENTERPRISE_DEACTIVATE_DEVICE_ADMIN

- 从API version 23开始，支持申请ohos.permission.ENTERPRISE_DEACTIVATE_DEVICE_ADMIN权限。仅当SDA或DA设备管理应用解除激活自身时，可以申请该权限。

- 从API version 20开始，支持申请ohos.permission.START_PROVISIONING_MESSAGE权限。仅当BYOD设备管理应用解除激活自身时，可以申请该权限。

- API 19及之前的版本，需要申请ohos.permission.MANAGE_ENTERPRISE_DEVICE_ADMIN（仅系统应用支持申请）。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。解除激活BYOD设备管理应用时，仅支持传入当前应用的企业设备管理扩展组件。 |
| userId | number | 否 | 用户ID，取值范围：大于等于0。 - 调用接口时，若传入userId，表示指定用户。 - 调用接口时，若未传入userId，表示当前用户。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当解除激活设备管理应用失败时，会抛出错误对象。 |

**错误码**:

以下错误码的详细介绍请参见[企业设备管理错误码]([企业设备管理错误码](../../errors/企业设备管理错误码.md).md)和[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200005 | Failed to deactivate the administrator application of the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例**：

```ets
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

adminManager.disableAdmin(wantTemp, 100).catch((err: BusinessError) => {
  console.error(`Failed to disable admin. Code: ${err.code}, message: ${err.message}`);
});
```

#### adminManager.isByodAdmin20+

isByodAdmin(admin: Want): boolean

根据企业设备管理扩展组件查询当前应用是否被激活为BYOD设备管理应用。

**需要权限：** ohos.permission.START_PROVISIONING_MESSAGE

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。仅支持传入当前应用的企业设备管理扩展组件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示被激活为BYOD设备管理应用，返回false表示没有被激活为BYOD设备管理应用。 |

**错误码**:

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200012 | Parameter verification failed. |

**示例**：

```ets
import { Want } from '@kit.AbilityKit';
import { adminManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 请根据实际情况替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: boolean = adminManager.isByodAdmin(wantTemp);
  console.info(`Succeeded in querying admin is byod admin or not : ${result}`);
} catch (error) {
  console.error(`Failed to query admin is byod admin or not. Code is ${error.code}, message is ${error.message}`);
}
```

#### adminManager.subscribeManagedEventSync

subscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void

订阅系统管理事件。

**需要权限：** ohos.permission.ENTERPRISE_SUBSCRIBE_MANAGED_EVENT

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| managedEvents | Array<ManagedEvent> | 是 | 订阅事件数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200008 | The specified system event is invalid. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let events: Array<adminManager.ManagedEvent> = [adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_ADDED, adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_REMOVED];

try {
  adminManager.subscribeManagedEventSync(wantTemp, events);
  console.info('Succeeded in subscribing managed event.');
} catch (err) {
  console.error(`Failed to subscribe managed event. Code: ${err.code}, message: ${err.message}`);
}
```

#### adminManager.unsubscribeManagedEventSync

unsubscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void

取消订阅系统管理事件。

**需要权限：** ohos.permission.ENTERPRISE_SUBSCRIBE_MANAGED_EVENT

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| managedEvents | Array<ManagedEvent> | 是 | 取消订阅事件数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200008 | The specified system event is invalid. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let events: Array<adminManager.ManagedEvent> = [adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_ADDED, adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_REMOVED];

try {
  adminManager.unsubscribeManagedEventSync(wantTemp, events);
  console.info('Succeeded in unsubscribing managed event.');
} catch (err) {
  console.error(`Failed to unsubscribe managed event. Code: ${err.code}, message: ${err.message}`);
}
```

#### adminManager.setDelegatedPolicies14+

setDelegatedPolicies(admin: Want, bundleName: string, policies: Array<string>): void

委托其他应用来设置设备的管控策略。被委托的其他应用需申请委托策略对应接口所需权限。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_DELEGATED_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 被委托应用包名。被委托应用的分发类型需为enterprise_normal和enterprise_mdm，可以通过get[BundleInfo](../../topics/misc/BundleInfo.md)ForSelf接口查询应用自身的BundleInfo，其中BundleInfo.appInfo.appDistributionType为应用的分发类型。 |
| policies | Array<string> | 是 | 委托策略列表。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200009 | Failed to grant the permission to the application. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let admin: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let policies: Array<string> = ["disabled_hdc"];

try {
  // 参数需根据实际情况进行替换
  adminManager.setDelegatedPolicies(admin, "com.example.enterprise.xxx", policies);
  console.info('Succeeded in setting delegated policies.');
} catch (err) {
  console.error(`Failed to set delegated policies. Code: ${err.code}, message: ${err.message}`);
}
```

#### adminManager.getDelegatedPolicies14+

getDelegatedPolicies(admin: Want, bundleName: string): Array<string>

查询被委托应用可访问的策略列表。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_DELEGATED_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 被委托应用包名。被委托应用的分发类型需为enterprise_normal和enterprise_mdm，可以通过get[BundleInfo](../../topics/misc/BundleInfo.md)ForSelf接口查询应用自身的BundleInfo，其中BundleInfo.appInfo.appDistributionType为应用的分发类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 委托策略列表。 |

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
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let admin: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let policies: Array<string> = adminManager.getDelegatedPolicies(admin, "com.example.enterprise.xxx");
  console.info(`Succeeded in getting delegated policies.${JSON.stringify(policies)}`);
} catch (err) {
  console.error(`Failed to get delegated policies. Code: ${err.code}, message: ${err.message}`);
}
```

#### adminManager.getDelegatedBundleNames14+

getDelegatedBundleNames(admin: Want, policy: string): Array<string>

查询可以访问某个委托策略的被委托应用，输出被委托应用列表。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_DELEGATED_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | string | 是 | 委托策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 被委托应用列表。 |

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
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let admin: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let bundleNames: Array<string> = adminManager.getDelegatedBundleNames(admin, "disabled_hdc");
  console.info(`Succeeded in getting delegated bundles.${JSON.stringify(bundleNames)}`);
} catch (err) {
  console.error(`Failed to get delegated bundles. Code: ${err.code}, message: ${err.message}`);
}
```

#### adminManager.startAdminProvision15+

startAdminProvision(admin: Want, type: AdminType, context: common.Context, parameters: Record<string, string>): void

设备管理应用拉起BYOD管理员激活页面进行激活。

**需要权限：** ohos.permission.START_PROVISIONING_MESSAGE

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| type | AdminType | 是 | 激活的设备管理应用类型，仅支持ADMIN_TYPE_BYOD类型。 |
| context | common.Context | 是 | 管理应用的上下文信息。 |
| parameters | Record<string, string> | 是 | 自定义参数信息，其中Key值必须包含："activateId"，可以包含"customizedInfo"、"localDeactivationPolicy"。 - activateId：项目激活ID。 - customizedInfo：企业自定义信息。 - localDeactivationPolicy：从API version 22开始支持，本地延迟取消激活时间（单位：小时）。 |

**错误码**：

以下的错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { adminManager } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let recordParameters: Record<string, string> = {
  // 需根据实际情况进行替换
  "activateId": "activateId testValue",
  "customizedInfo": "customizedInfo testValue"
};
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  console.info('context:' + JSON.stringify(context));
  adminManager.startAdminProvision(wantTemp, adminManager.AdminType.ADMIN_TYPE_BYOD, context, recordParameters);
  console.info('startAdminProvision::success');
} catch (error) {
  console.error('startAdminProvision::errorCode: ' + error.code + ' errorMessage: ' + error.message);
}
```

**adminManager.enableDeviceAdmin23+**

enableDeviceAdmin(admin: Want): Promise<void>

[超级设备管理应用](../../guides/MDM Kit术语.md#sda)通过该接口可以激活其他[普通设备管理应用](../../guides/MDM Kit术语.md#da)，使用Promise异步回调。该接口仅支持超级设备管理应用调用。

需要权限： ohos.permission.ENTERPRISE_MANAGE_DEVICE_ADMIN

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

设备行为差异： 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当激活设备管理应用失败时，会抛出错误对象。 |

错误码：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200003 | The administrator ability component is invalid. |
| 9200004 | Failed to activate the administrator application of the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

示例：

```ets
import { Want } from '@kit.AbilityKit';
import { adminManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

adminManager.enableDeviceAdmin(wantTemp).catch((err: BusinessError) => {
  console.error(`Failed to enable device admin. Code: ${err.code}, message: ${err.message}`);
});
```

**adminManager.disableDeviceAdmin23+**

disableDeviceAdmin(admin: Want): Promise<void>

[超级设备管理应用](../../guides/MDM Kit术语.md#sda)通过该接口可以解除激活其他[普通设备管理应用](../../guides/MDM Kit术语.md#da)，使用Promise异步回调。该接口仅支持超级设备管理应用调用。

需要权限： ohos.permission.ENTERPRISE_MANAGE_DEVICE_ADMIN

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

设备行为差异： 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当解除激活设备管理应用失败时，会抛出错误对象。 |

错误码：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200005 | Failed to deactivate the administrator application of the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

示例：

```ets
import { Want } from '@kit.AbilityKit';
import { adminManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

adminManager.disableDeviceAdmin(wantTemp).catch((err: BusinessError) => {
  console.error(`Failed to disable device admin. Code: ${err.code}, message: ${err.message}`);
});
```

#### ManagedEvent

可订阅的系统管理事件。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MANAGED_EVENT_BUNDLE_ADDED | 0 | 应用安装事件。 |
| MANAGED_EVENT_BUNDLE_REMOVED | 1 | 应用卸载事件。 |
| MANAGED_EVENT_APP_START | 2 | 应用启动事件。 |
| MANAGED_EVENT_APP_STOP | 3 | 应用停止事件。 |
| MANAGED_EVENT_SYSTEM_UPDATE | 4 | 系统更新事件。 |
| MANAGED_EVENT_ACCOUNT_ADDED18+ | 5 | 账号新增事件。 |
| MANAGED_EVENT_ACCOUNT_SWITCHED18+ | 6 | 账号切换事件。 |
| MANAGED_EVENT_ACCOUNT_REMOVED18+ | 7 | 账号删除事件。 |

#### AdminType15+

设备管理应用的类型。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ADMIN_TYPE_BYOD | 0x02 | BYOD设备管理应用。 |

#### Policy20+

允许或禁用名单的策略类型。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BLOCK_LIST | 0 | 禁用名单。 |
| TRUST_LIST | 1 | 允许名单。 |

#### 附录

#### 可委托策略列表

| 策略名称 | 对应接口 | 说明 |
| --- | --- | --- |
| disallow_add_local_account | [accountManager.disallowOsAccountAddition](@ohos.enterprise.accountManager（账户管理）.md#ZH-CN_TOPIC_0000002529285577__accountmanagerdisallowosaccountaddition) [accountManager.isOsAccountAdditionDisallowed](@ohos.enterprise.accountManager（账户管理）.md#ZH-CN_TOPIC_0000002529285577__accountmanagerisosaccountadditiondisallowed) | 不传accountId参数，禁止设备创建本地用户。 不传accountId参数，查询是否禁止设备创建本地用户。 |
| disallow_add_os_account_by_user | [accountManager.disallowOsAccountAddition](@ohos.enterprise.accountManager（账户管理）.md#ZH-CN_TOPIC_0000002529285577__accountmanagerdisallowosaccountaddition) accountManager.isOsAccountAdditionDisallowed | 需传入accountId参数，禁止指定用户添加账号。 需传入accountId参数，查询是否禁止指定用户添加账号。 |
| disallow_running_bundles | [applicationManager.addDisallowedRunningBundlesSync](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002497605586__applicationmanageradddisallowedrunningbundlessync) [applicationManager.removeDisallowedRunningBundlesSync](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002497605586__applicationmanagerremovedisallowedrunningbundlessync) [applicationManager.getDisallowedRunningBundlesSync](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002497605586__applicationmanagergetdisallowedrunningbundlessync) | 添加应用至应用运行禁止名单，添加至禁止名单的应用不允许在当前/指定用户下运行。 从应用运行禁止名单中移除应用。 获取当前/指定用户下的应用运行禁止名单。 |
| manage_auto_start_apps | [applicationManager.addAutoStartApps](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002497605586__applicationmanageraddautostartapps) [applicationManager.removeAutoStartApps](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002497605586__applicationmanagerremoveautostartapps) [applicationManager.getAutoStartApps](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002497605586__applicationmanagergetautostartapps) | 添加开机自启动应用名单。 从开机自启动应用名单中移除应用。 查询开机自启动应用名单。 |
| allowed_bluetooth_devices | [bluetoothManager.addAllowedBluetoothDevices](@ohos.enterprise.bluetoothManager（蓝牙管理）.md#ZH-CN_TOPIC_0000002497445608__bluetoothmanageraddallowedbluetoothdevices) [bluetoothManager.removeAllowedBluetoothDevices](@ohos.enterprise.bluetoothManager（蓝牙管理）.md#ZH-CN_TOPIC_0000002497445608__bluetoothmanagerremoveallowedbluetoothdevices) [bluetoothManager.getAllowedBluetoothDevices](@ohos.enterprise.bluetoothManager（蓝牙管理）.md#ZH-CN_TOPIC_0000002497445608__bluetoothmanagergetallowedbluetoothdevices) | 添加蓝牙设备可用名单。 从蓝牙设备可用名单中移除。 查询蓝牙设备可用名单。 |
| set_browser_policies | [browser.setPolicySync](@ohos.enterprise.browser（浏览器管理）.md#ZH-CN_TOPIC_0000002529285579__browsersetpolicysync) [browser.getPoliciesSync](@ohos.enterprise.browser（浏览器管理）.md#ZH-CN_TOPIC_0000002529285579__browsergetpoliciessync) | 为指定的浏览器设置浏览器子策略。 获取指定浏览器的策略。 |
| allowed_install_bundles | [bundleManager.addAllowedInstallBundlesSync](@ohos.enterprise.bundleManager（包管理）.md#ZH-CN_TOPIC_0000002529445553__bundlemanageraddallowedinstallbundlessync) [bundleManager.removeAllowedInstallBundlesSync](@ohos.enterprise.bundleManager（包管理）.md#ZH-CN_TOPIC_0000002529445553__bundlemanagerremoveallowedinstallbundlessync) [bundleManager.getAllowedInstallBundlesSync](@ohos.enterprise.bundleManager（包管理）.md#ZH-CN_TOPIC_0000002529445553__bundlemanagergetallowedinstallbundlessync) | 添加应用至应用程序包安装允许名单，添加至允许名单的应用允许在当前/指定用户下安装，否则不允许安装。 从应用程序包安装允许名单中移除应用。 获取当前/指定用户下的应用程序包安装允许名单。 |
| disallowed_install_bundles | [bundleManager.addDisallowedInstallBundlesSync](@ohos.enterprise.bundleManager（包管理）.md#ZH-CN_TOPIC_0000002529445553__bundlemanageradddisallowedinstallbundlessync) [bundleManager.removeDisallowedInstallBundlesSync](@ohos.enterprise.bundleManager（包管理）.md#ZH-CN_TOPIC_0000002529445553__bundlemanagerremoveallowedinstallbundlessync) [bundleManager.getDisallowedInstallBundlesSync](@ohos.enterprise.bundleManager（包管理）.md#ZH-CN_TOPIC_0000002529445553__bundlemanagergetdisallowedinstallbundlessync) | 添加应用至应用程序包安装禁止名单，添加至禁止名单的应用不允许在当前/指定用户下安装。 从应用程序包安装禁止名单中移除应用。 获取当前/指定用户下的应用程序包安装禁止名单。 |
| disallowed_uninstall_bundles | [bundleManager.addDisallowedUninstallBundlesSync](@ohos.enterprise.bundleManager（包管理）.md#ZH-CN_TOPIC_0000002529445553__bundlemanageradddisalloweduninstallbundlessync) [bundleManager.removeDisallowedUninstallBundlesSync](@ohos.enterprise.bundleManager（包管理）.md#ZH-CN_TOPIC_0000002529445553__bundlemanagerremovedisalloweduninstallbundlessync) [bundleManager.getDisallowedUninstallBundlesSync](@ohos.enterprise.bundleManager（包管理）.md#ZH-CN_TOPIC_0000002529445553__bundlemanagergetdisalloweduninstallbundlessync) | 添加应用至应用程序包卸载禁止名单，添加至禁止名单的应用不允许在当前/指定用户下卸载。 从应用程序包卸载禁止名单中移除应用。 获取当前/指定用户下的应用包程序卸载禁止名单。 |
| get_device_info | [deviceInfo.getDeviceInfo](@ohos.enterprise.deviceInfo（设备信息管理）.md#ZH-CN_TOPIC_0000002529285581__deviceinfogetdeviceinfo) | 获取设备信息。 |
| location_policy | [locationManager.setLocationPolicy](@ohos.enterprise.locationManager（位置服务管理）.md#ZH-CN_TOPIC_0000002497605590__locationmanagersetlocationpolicy) [locationManager.getLocationPolicy](@ohos.enterprise.locationManager（位置服务管理）.md#ZH-CN_TOPIC_0000002497605590__locationmanagergetlocationpolicy) | 设置位置服务管理策略。 查询位置服务策略。 |
| disabled_network_interface | [networkManager.setNetworkInterfaceDisabledSync](@ohos.enterprise.networkManager（网络管理）.md#ZH-CN_TOPIC_0000002497445612__networkmanagersetnetworkinterfacedisabledsync) [networkManager.isNetworkInterfaceDisabledSync](@ohos.enterprise.networkManager（网络管理）.md#ZH-CN_TOPIC_0000002497445612__networkmanagerisnetworkinterfacedisabledsync) | 禁止设备使用指定网络。 查询指定网络接口是否被禁用。 |
| global_proxy | [networkManager.setGlobalProxySync](@ohos.enterprise.networkManager（网络管理）.md#ZH-CN_TOPIC_0000002497445612__networkmanagersetglobalproxysync) [networkManager.getGlobalProxySync](@ohos.enterprise.networkManager（网络管理）.md#ZH-CN_TOPIC_0000002497445612__networkmanagergetglobalproxysync) | 设置网络全局代理。 获取网络全局代理。 |
| disabled_bluetooth | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) [restrictions.getDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionsgetdisallowedpolicy) | feature传入bluetooth，禁用/启用蓝牙能力。 feature传入bluetooth，查询是否禁用蓝牙能力。 |
| disallow_modify_datetime | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy | feature传入modifyDateTime，禁用/启用设置系统时间能力。 feature传入modifyDateTime，查询是否禁用修改系统时间能力。 |
| disabled_printer | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy | feature传入printer，禁用/启用打印能力。 feature传入printer，查询是否禁用打印能力。 |
| disabled_hdc | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy | feature传入hdc，禁用/启用被其他设备通过hdc连接、调试的能力。 feature传入hdc，查询是否禁用被其他设备通过hdc连接、调试的能力。 |
| disable_microphone | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy | feature传入microphone，禁用/启用麦克风能力。 feature传入microphone，查询是否禁用麦克风能力。 |
| fingerprint_auth | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy [restrictions.setDisallowedPolicyForAccount](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicyforaccount14) [restrictions.getDisallowedPolicyForAccount](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionsgetdisallowedpolicyforaccount14) | feature传入fingerprint，禁用/启用指纹认证能力。 feature传入fingerprint，查询是否禁用指纹认证能力。 feature传入fingerprint，禁用/启用指定用户的指纹认证能力。 feature传入fingerprint，查询是否禁用指定用户的指纹认证能力。 |
| disable_usb | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy | feature传入usb，禁用/启用USB能力。 feature传入usb，查询是否禁用USB能力。 |
| disable_wifi | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy | feature传入wifi，禁用/启用Wi-Fi能力。 feature传入wifi，查询是否禁用Wi-Fi能力。 |
| disallowed_tethering | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy | feature传入tethering，禁用/启用网络共享能力。 feature传入tethering，查询是否禁用网络共享能力。 |
| inactive_user_freeze | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy | feature传入inactiveUserFreeze，禁用/启用非活跃用户运行能力。 feature传入inactiveUserFreeze，查询是否禁用非活跃用户运行能力。 |
| snapshot_skip | [restrictions.addDisallowedListForAccount](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionsadddisallowedlistforaccount14) [restrictions.removeDisallowedListForAccount](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionsremovedisallowedlistforaccount14) [restrictions.getDisallowedListForAccount](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionsgetdisallowedlistforaccount14) | feature传入snapshotSkip，禁用屏幕快照能力的应用名单。 feature传入snapshotSkip，从禁用屏幕快照能力的应用名单中移除。 feature传入snapshotSkip，查询禁用屏幕快照能力的应用名单。 |
| password_policy | [securityManager.setPasswordPolicy](@ohos.enterprise.securityManager（安全管理）.md#ZH-CN_TOPIC_0000002529445557__securitymanagersetpasswordpolicy) [securityManager.getPasswordPolicy](@ohos.enterprise.securityManager（安全管理）.md#ZH-CN_TOPIC_0000002529445557__securitymanagergetpasswordpolicy) | 设置设备口令策略。 获取设备口令策略。 |
| clipboard_policy | [securityManager.setAppClipboardPolicy](@ohos.enterprise.securityManager（安全管理）.md#ZH-CN_TOPIC_0000002529445557__securitymanagersetappclipboardpolicy) [securityManager.getAppClipboardPolicy](@ohos.enterprise.securityManager（安全管理）.md#ZH-CN_TOPIC_0000002529445557__securitymanagergetappclipboardpolicy) | 设置设备剪贴板策略。 获取设备剪贴板策略。 |
| watermark_image_policy | [securityManager.setWatermarkImage](@ohos.enterprise.securityManager（安全管理）.md#ZH-CN_TOPIC_0000002529445557__securitymanagersetwatermarkimage14) [securityManager.cancelWatermarkImage](@ohos.enterprise.securityManager（安全管理）.md#ZH-CN_TOPIC_0000002529445557__securitymanagercancelwatermarkimage14) | 设置水印策略，当前仅支持PC/2in1使用。 取消水印策略，当前仅支持PC/2in1使用。 |
| ntp_server | [systemManager.setNTPServer](@ohos.enterprise.systemManager （系统管理）.md#ZH-CN_TOPIC_0000002497605592__systemmanagersetntpserver) [systemManager.getNTPServer](@ohos.enterprise.systemManager （系统管理）.md#ZH-CN_TOPIC_0000002497605592__systemmanagergetntpserver) | 设置NTP服务器的策略。 获取NTP服务器信息。 |
| set_update_policy | [systemManager.setOtaUpdatePolicy](@ohos.enterprise.systemManager （系统管理）.md#ZH-CN_TOPIC_0000002497605592__systemmanagersetotaupdatepolicy) [systemManager.getOtaUpdatePolicy](@ohos.enterprise.systemManager （系统管理）.md#ZH-CN_TOPIC_0000002497605592__systemmanagergetotaupdatepolicy) | 设置升级策略。 查询升级策略。 |
| notify_upgrade_packages | [systemManager.notifyUpdatePackages](@ohos.enterprise.systemManager （系统管理）.md#ZH-CN_TOPIC_0000002497605592__systemmanagernotifyupdatepackages) [systemManager.getUpdateResult](@ohos.enterprise.systemManager （系统管理）.md#ZH-CN_TOPIC_0000002497605592__systemmanagergetupdateresult) | 通知系统更新包信息。 获取系统更新结果。 |
| allowed_usb_devices | [usbManager.addAllowedUsbDevices](@ohos.enterprise.usbManager（USB管理）.md#ZH-CN_TOPIC_0000002497445614__usbmanageraddallowedusbdevices) [usbManager.removeAllowedUsbDevices](@ohos.enterprise.usbManager（USB管理）.md#ZH-CN_TOPIC_0000002497445614__usbmanagerremoveallowedusbdevices) [usbManager.getAllowedUsbDevices](@ohos.enterprise.usbManager（USB管理）.md#ZH-CN_TOPIC_0000002497445614__usbmanagergetallowedusbdevices) | 添加USB设备可用名单。 移除USB设备可用名单。 获取USB设备可用名单。 |
| usb_read_only | [usbManager.setUsbStorageDeviceAccessPolicy](@ohos.enterprise.usbManager（USB管理）.md#ZH-CN_TOPIC_0000002497445614__usbmanagersetusbstoragedeviceaccesspolicy) [usbManager.getUsbStorageDeviceAccessPolicy](@ohos.enterprise.usbManager（USB管理）.md#ZH-CN_TOPIC_0000002497445614__usbmanagergetusbstoragedeviceaccesspolicy) | 设置USB存储设备访问策略。 获取USB存储设备访问策略。 |
| disallowed_usb_devices | [usbManager.addDisallowedUsbDevices](@ohos.enterprise.usbManager（USB管理）.md#ZH-CN_TOPIC_0000002497445614__usbmanageradddisallowedusbdevices14) [usbManager.removeDisallowedUsbDevices](@ohos.enterprise.usbManager（USB管理）.md#ZH-CN_TOPIC_0000002497445614__usbmanagerremovedisallowedusbdevices14) [usbManager.getDisallowedUsbDevices](@ohos.enterprise.usbManager（USB管理）.md#ZH-CN_TOPIC_0000002497445614__usbmanagergetdisallowedusbdevices14) | 添加禁止使用的USB设备类型。 移除禁止使用的USB设备类型。 获取禁止使用的USB设备类型。 |
| disallowed_sms | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy | feature传入sms，禁用/启用设备接收、发送短信的能力，当前仅支持手机、平板设备使用。 feature传入sms，查询是否禁用设备接收、发送短信的能力，当前仅支持手机、平板设备使用。 |
| disallowed_mms | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy | feature传入mms，禁用/启用设备接收、发送彩信的能力，当前仅支持手机、平板设备使用。 feature传入mms，查询是否禁用设备接收、发送彩信的能力，当前仅支持手机、平板设备使用。 |
| disable_backup_and_restore | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy | feature传入backupAndRestore，禁用/启用备份和恢复能力，当前仅支持手机、平板使用。 feature传入backupAndRestore，查询是否禁用备份和恢复能力，当前仅支持手机、平板使用。 |
| installed_bundle_info_list | [bundleManager.getInstalledBundleList](@ohos.enterprise.bundleManager（包管理）.md#ZH-CN_TOPIC_0000002529445553__bundlemanagergetinstalledbundlelist20) | 获取设备指定用户下已安装应用列表。 |
| clear_up_application_data | [applicationManager.clearUpApplicationData](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002497605586__applicationmanagerclearupapplicationdata20) | 清除应用产生的所有数据。 |
| disallow_unmute_device | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy | feature传入unmuteDevice，禁用/启用设备媒体播放声音能力。 feature传入unmuteDevice，查询是否禁用设备媒体播放声音能力。 |
| disabled_hdc_remote | [restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy) restrictions.getDisallowedPolicy | feature传入hdcRemote，禁用/启用设备通过hdc调试其他设备的能力。 feature传入hdcRemote，查询是否禁用设备通过hdc调试其他设备的能力。 |