# @ohos.enterprise.browser（浏览器管理）

本模块提供浏览器管理能力，包括设置/取消浏览器策略、获取浏览器策略等。

浏览器策略指通过配置或管理浏览器行为的一系列规则和设置，以确保安全性、合规性、性能优化和用户体验的一致性。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-guide)。

#### 导入模块

```ets
import { browser } from '@kit.MDMKit';
```

#### browser.setPolicySync

setPolicySync(admin: Want, appId: string, policyName: string, policyValue: string): void

为指定的浏览器设置浏览器子策略。

**需要权限：** ohos.permission.ENTERPRISE_SET_BROWSER_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appId | string | 是 | 应用ID，用于指定浏览器。 |
| policyName | string | 是 | 浏览器子策略名。当此值为空字符串时，表示设置应用ID对应的浏览器策略。 |
| policyValue | string | 是 | 浏览器子策略值。当此值为空字符串时，表示取消浏览器策略名对应浏览器子策略。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码]([企业设备管理错误码](../../errors/企业设备管理错误码.md).md)和[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { browser } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 此处参数appId的赋值应替换为开发者自己指定的浏览器的应用ID
let appId: string = 'com.example.******_******/******5t5CoBM=';
let policyName: string = 'InsecurePrivateNetworkRequestsAllowed';
let policyValue: string = '{"level":"mandatory","scope":"machine","source":"platform","value":true}';

try {
  browser.setPolicySync(wantTemp, appId, policyName, policyValue);
  console.info('Succeeded in setting browser policies.');
} catch (err) {
  console.error(`Failed to set browser policies. Code is ${err.code}, message is ${err.message}`);
}
```

#### browser.getPoliciesSync

getPoliciesSync(admin: Want, appId: string): string

通过appid获取指定浏览器设置的策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appId | string | 是 | 应用ID，用于指定浏览器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 浏览器策略。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { browser } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 此处参数appId的赋值应替换为开发者自己指定的浏览器的应用ID
let appId: string = 'com.example.******_******/******5t5CoBM=';

try {
  let result: string = browser.getPoliciesSync(wantTemp, appId);
  console.info(`Succeeded in getting browser policies, result : ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to get browser policies. Code is ${err.code}, message is ${err.message}`);
}
```

#### browser.setManagedBrowserPolicy15+

setManagedBrowserPolicy(admin: Want, bundleName: string, policyName: string, policyValue: string): void

为指定的浏览器设置浏览器策略，成功后会发布系统公共事件[COMMON_EVENT_MANAGED_BROWSER_POLICY_CHANGED](系统定义的公共事件.md#ZH-CN_TOPIC_0000002522241594__common_event_managed_browser_policy_changed)。

**需要权限：** ohos.permission.ENTERPRISE_SET_BROWSER_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 应用包名，用于指定浏览器。 |
| policyName | string | 是 | 浏览器策略名。 |
| policyValue | string | 是 | 浏览器策略值。当此值为空字符串时，表示取消浏览器策略名对应浏览器子策略。 |

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
import { browser } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let bundleName: string = 'com.example.testbrowser';
let policyName: string = 'InsecurePrivateNetworkRequestsAllowed';
let policyValue: string = '{"level":"mandatory","scope":"machine","source":"platform","value":true}';

try {
  browser.setManagedBrowserPolicy(wantTemp, bundleName, policyName, policyValue);
  console.info('Succeeded in setting managed browser policy.');
} catch (err) {
  console.error(`Failed to set managed browser policy. Code is ${err.code}, message is ${err.message}`);
}
```

#### browser.getManagedBrowserPolicy15+

getManagedBrowserPolicy(admin: Want, bundleName: string): ArrayBuffer

通过应用包名获取指定浏览器的浏览器策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 应用包名，用于指定浏览器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 浏览器策略。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { browser } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { util } from '@kit.ArkTS';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let bundleName: string = 'com.example.testbrowser';

try {
  let buffer: ArrayBuffer = browser.getManagedBrowserPolicy(wantTemp, bundleName);
  let intBuffer: Uint8Array = new Uint8Array(buffer);
  let decoder: util.TextDecoder = util.TextDecoder.create('utf-8');
  let stringData: string = decoder.decodeToString(intBuffer);
  console.info(`Succeeded in getting managed browser policy, result : ${stringData}`);
} catch(err) {
  console.error(`Failed to get managed browser policy. Code is ${err.code}, message is ${err.message}`);
}
```

#### browser.getSelfManagedBrowserPolicyVersion15+

getSelfManagedBrowserPolicyVersion(): string

获取指定浏览器的浏览器策略版本。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 浏览器策略版本。 |

**示例：**

```ets
import { browser } from '@kit.MDMKit';

try {
  let version: string = browser.getSelfManagedBrowserPolicyVersion();
  console.info(`Succeeded in getting self managed browser policy version, result : ${version}`);
} catch(err) {
  console.error(`Failed to get self managed browser policy version. Code is ${err.code}, message is ${err.message}`);
}
```

#### browser.getSelfManagedBrowserPolicy15+

getSelfManagedBrowserPolicy(): ArrayBuffer

获取当前设备浏览器策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 浏览器策略。 |

**示例：**

```ets
import { browser } from '@kit.MDMKit';
import { util } from '@kit.ArkTS';

try {
  let buffer: ArrayBuffer = browser.getSelfManagedBrowserPolicy();
  let intBuffer: Uint8Array = new Uint8Array(buffer);
  let decoder: util.TextDecoder = util.TextDecoder.create('utf-8');
  let stringData: string = decoder.decodeToString(intBuffer);
  console.info(`Succeeded in getting self managed browser policy, result : ${stringData}`);
} catch(err) {
  console.error(`Failed to get self managed browser policy. Code is ${err.code}, message is ${err.message}`);
}
```