# @ohos.enterprise.systemManager （系统管理）

本模块提供系统管理能力。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-guide)。

#### 导入模块

```ets
import { systemManager } from '@kit.MDMKit';
```

#### systemManager.setNTPServer

setNTPServer(admin: Want, server: string): void

设置NTP时间服务器。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| server | string | 是 | NTP服务器地址（以","分隔，如"ntpserver1.com,ntpserver2.com"。最大长度96字节，包括结束符）。 |

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
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let server: string = "ntpserver.com";
try {
  systemManager.setNTPServer(wantTemp, server);
  console.info('Succeeded in setting NTPserver.');
} catch (err) {
  console.error(`Failed to set ntp server. Code is ${err.code}, message is ${err.message}`);
}
```

#### systemManager.getNTPServer

getNTPServer(admin: Want): string

获取NTP时间服务器信息。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | string对象，返回NTP时间服务器信息。 |

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
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  systemManager.getNTPServer(wantTemp);
  console.info('Succeeded in getting NTP server.');
} catch (err) {
  console.error(`Failed to get ntp server. Code is ${err.code}, message is ${err.message}`);
}
```

#### systemManager.setOtaUpdatePolicy

setOtaUpdatePolicy(admin: Want, policy: OtaUpdatePolicy): void

设置升级策略。内网升级场景下，需要先调用[systemManager.notifyUpdatePackages](#ZH-CN_TOPIC_0000002522081694__systemmanagernotifyupdatepackages)接口通知系统更新包，再调用该接口设置升级策略。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | OtaUpdatePolicy | 是 | 升级策略。 |

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
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 默认升级策略
let otaUpdatePolicy1: systemManager.OtaUpdatePolicy = {
  "policyType": systemManager.PolicyType.DEFAULT,
  "version": "version_1.0.0.0",
};
try {
  systemManager.setOtaUpdatePolicy(wantTemp, otaUpdatePolicy1);
  console.info('Succeeded in setting ota update policy.');
} catch (err) {
  console.error(`Failed to set ota update policy. Code is ${err.code}, message is ${err.message}`);
}
// 禁止升级
let otaUpdatePolicy2: systemManager.OtaUpdatePolicy = {
  "policyType": systemManager.PolicyType.PROHIBIT,
  "version": "version_1.0.0.1",
};
try {
  systemManager.setOtaUpdatePolicy(wantTemp, otaUpdatePolicy2);
  console.info('Succeeded in setting ota update policy.');
} catch (err) {
  console.error(`Failed to set ota update policy. Code is ${err.code}, message is ${err.message}`);
}
// 强制升级
let otaUpdatePolicy3: systemManager.OtaUpdatePolicy = {
  "policyType": systemManager.PolicyType.UPDATE_TO_SPECIFIC_VERSION,
  "version": "version_1.0.0.2",
  "latestUpdateTime": 1716343200, // 时间戳
};
try {
  systemManager.setOtaUpdatePolicy(wantTemp, otaUpdatePolicy3);
  console.info('Succeeded in setting ota update policy.');
} catch (err) {
  console.error(`Failed to set ota update policy. Code is ${err.code}, message is ${err.message}`);
}
// 指定时间窗口升级
let otaUpdatePolicy4: systemManager.OtaUpdatePolicy = {
  "policyType": systemManager.PolicyType.WINDOWS,
  "version": "version_1.0.0.3",
  "installStartTime": 1716281049, // // 时间戳
  "installEndTime": 1716343200, // // 时间戳
};
try {
  systemManager.setOtaUpdatePolicy(wantTemp, otaUpdatePolicy4);
  console.info('Succeeded in setting ota update policy.');
} catch (err) {
  console.error(`Failed to set ota update policy. Code is ${err.code}, message is ${err.message}`);
}
// 延迟升级
let otaUpdatePolicy5: systemManager.OtaUpdatePolicy = {
  "policyType": systemManager.PolicyType.POSTPONE,
  "version": "version_1.0.0.4",
  "delayUpdateTime": 5, // 单位（小时）
};
try {
  systemManager.setOtaUpdatePolicy(wantTemp, otaUpdatePolicy5);
  console.info('Succeeded in setting ota update policy.');
} catch (err) {
  console.error(`Failed to set ota update policy. Code is ${err.code}, message is ${err.message}`);
}
// 禁用公网升级
let otaUpdatePolicy6: systemManager.OtaUpdatePolicy = {
  "policyType": systemManager.PolicyType.DEFAULT,
  "version": "version_1.0.0.5",
  "disableSystemOtaUpdate": true,
};
try {
  systemManager.setOtaUpdatePolicy(wantTemp, otaUpdatePolicy6);
  console.info('Succeeded in setting ota update policy.');
} catch (err) {
  console.error(`Failed to set ota update policy. Code is ${err.code}, message is ${err.message}`);
}
```

#### systemManager.getOtaUpdatePolicy

getOtaUpdatePolicy(admin: Want): OtaUpdatePolicy

查询升级策略。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| OtaUpdatePolicy | OtaUpdatePolicy对象，返回升级策略。 |

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
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let policy: systemManager.OtaUpdatePolicy= systemManager.getOtaUpdatePolicy(wantTemp);
  console.info(`Succeeded in getting update policy: ${JSON.stringify(policy)}`);
} catch (err) {
  console.error(`Failed to get update policy. Code is ${err.code}, message is ${err.message}`);
}
```

#### systemManager.notifyUpdatePackages

notifyUpdatePackages(admin: Want, packageInfo: UpdatePackageInfo): Promise<void>

通知系统更新包信息。内网升级场景下，需要先调用该接口通知系统更新包，再调用[systemManager.setOtaUpdatePolicy](#ZH-CN_TOPIC_0000002522081694__systemmanagersetotaupdatepolicy)设置升级策略。


该接口比较耗时，当调用此接口后，后续如果在应用主线程调用其他同步接口时需要等待该接口异步返回。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| packageInfo | UpdatePackageInfo | 是 | 系统更新包信息。 说明： 传入的UpdatePackageInfo.packages.path必须是“update”开头的zip压缩包，传入其他形式的文件会报9201004错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当通知系统更新包失败时会抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9201004 | The update packages do not exist or analyzing failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ets
import { systemManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';
import { fileIo as fs } from '@kit.CoreFileKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let notify: systemManager.NotifyDescription = {
  // 需根据实际情况进行替换
  "installTips": "installTips",
  "installTipsDetail": "installTips detail"
};
let description: systemManager.PackageDescription = {
  // 需根据实际情况进行替换
  "notify": notify
};
let updatePackages: Array<systemManager.Package> = [];
// 应用沙箱路径，需根据实际情况进行替换
let fileDir = "/xxxx/xxxx/";
let path1: string = "update_sd_base.zip";
let path2: string = "update_sd_cust_xxxxx_all_cn.zip";
let path3: string = "update_sd_preload_xxxxx_all_cn_R1.zip";
let fd1: number = fs.openSync(fileDir + path1, fs.OpenMode.READ_ONLY).fd;
let fd2: number = fs.openSync(fileDir + "xxxxx/" + path2, fs.OpenMode.READ_ONLY).fd;
let fd3: number = fs.openSync(fileDir + "xxxxx/" + path3, fs.OpenMode.READ_ONLY).fd;
let package1: systemManager.Package = {
  // 需根据实际情况进行替换
  "type": systemManager.PackageType.FIRMWARE,
  "path": path1,
  "fd": fd1
};
let package2: systemManager.Package = {
  // 需根据实际情况进行替换
  "type": systemManager.PackageType.FIRMWARE,
  "path": path2,
  "fd": fd2
};
let package3: systemManager.Package = {
  // 需根据实际情况进行替换
  "type": systemManager.PackageType.FIRMWARE,
  "path": path3,
  "fd": fd3
};
updatePackages.push(package1);
updatePackages.push(package2);
updatePackages.push(package3);
let updatePackageInfo: systemManager.UpdatePackageInfo = {
  // 需根据实际情况进行替换
  "version" : "1.0",
  "packages" : updatePackages,
  "description" : description
};
systemManager.notifyUpdatePackages(wantTemp, updatePackageInfo).then(() => {
  console.info('Succeeded in notifying update packages.');
}).catch ((error: BusinessError) => {
  console.error(`Failed to notify update packages. Code is ${error.code},message is ${error.message}`);
});
```

#### systemManager.getUpdateResult

getUpdateResult(admin: Want, version: string): Promise<UpdateResult>

获取系统更新结果。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| version | string | 是 | 更新包版本号。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<UpdateResult> | Promise对象，返回系统更新结果。 |

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
import { systemManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
systemManager.getUpdateResult(wantTemp, "1.0").then((result:systemManager.UpdateResult) => {
    console.info(`Succeeded in getting update result: ${JSON.stringify(result)}`);
  }).catch((error: BusinessError) => {
    console.error(`Get update result failed. Code is ${error.code},message is ${error.message}`);
  });
```

#### systemManager.getUpdateAuthData19+

getUpdateAuthData(admin: Want): Promise<string>

获取系统更新的鉴权数据，用于校验系统更新信息。使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回系统更新的鉴权数据。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ets
import { systemManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
systemManager.getUpdateAuthData(wantTemp).then((result: string) => {
    console.info(`Succeeded in getting update auth data: ${JSON.stringify(result)}`);
  }).catch((error: BusinessError) => {
    console.error(`Get update auth data failed. Code is ${error.code},message is ${error.message}`);
  });
```

#### systemManager.addDisallowedNearLinkProtocols20+

addDisallowedNearLinkProtocols(admin: Want, protocols: Array<NearLinkProtocol>, accountId: number): void

为指定用户添加禁用的星闪协议名单。NearLink Kit（星闪服务）提供一种低功耗、高速率的短距离通信服务，支持星闪设备之间的连接、数据交互。具体请参考[NearLink Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-introduction)。本接口对键盘、手写笔等系统服务和系统应用不生效。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| protocols | Array<NearLinkProtocol> | 是 | 星闪协议列表。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过getOsAccountLocalId等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ets
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 需根据实际情况进行替换
let protocols: systemManager.NearLinkProtocol[] = [systemManager.NearLinkProtocol.SSAP,
  systemManager.NearLinkProtocol.DATA_TRANSFER];

// 需根据实际情况进行替换
let accountId: number = 100;

try {
  systemManager.addDisallowedNearLinkProtocols(wantTemp, protocols, accountId);
  console.info('Succeeded in adding the disabled Starlink protocol list for the specified user.');
} catch (err) {
  console.error(`Failed to add the disabled Starlink protocol list for the specified user. Code is ${err.code}, message is ${err.message}`);
}
```

#### systemManager.removeDisallowedNearLinkProtocols20+

removeDisallowedNearLinkProtocols(admin: Want, protocols: Array<NearLinkProtocol>, accountId: number): void

为指定用户移除禁用的星闪协议名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [合并](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| protocols | Array<NearLinkProtocol> | 是 | 星闪协议列表。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过getOsAccountLocalId等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ets
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 需根据实际情况进行替换
let protocols: systemManager.NearLinkProtocol[] = [systemManager.NearLinkProtocol.SSAP,
  systemManager.NearLinkProtocol.DATA_TRANSFER];

// 需根据实际情况进行替换
let accountId: number = 100;
try {
  systemManager.removeDisallowedNearLinkProtocols(wantTemp, protocols, accountId);
  console.info('Succeeded in removing the disabled Starlink protocol list for the specified user.');
} catch (err) {
  console.error(`Failed to remove the disabled Starlink protocol list for the specified user. Code is ${err.code}, message is ${err.message}`);
}
```

#### systemManager.getDisallowedNearLinkProtocols20+

getDisallowedNearLinkProtocols(admin: Want, accountId: number): Array<NearLinkProtocol>

获取指定用户下禁用的星闪协议名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。 accountId可以通过getOsAccountLocalId等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<NearLinkProtocol> | 指定用户下禁用的星闪协议名单。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ets
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 需根据实际情况进行替换
let accountId: number = 100;

try {
  let result: systemManager.NearLinkProtocol[] = systemManager.getDisallowedNearLinkProtocols(wantTemp, accountId);
  console.info(`Succeeded in querying the disabled Starlink protocol list for the specified user: ${result}`);
} catch (err) {
  console.error(`Failed to query the disabled Starlink protocol list for the specified user. Code is ${err.code}, message is ${err.message}`);
}
```

#### systemManager.setInstallLocalEnterpriseAppEnabled20+

setInstallLocalEnterpriseAppEnabled(admin: Want, isEnable: boolean): void

设置是否支持本地安装企业应用。设置为支持安装后，具备本地安装能力的PC/2in1设备可本地双击应用安装包，安装签名证书分发类型为enterprise_normal的企业应用。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [从严管控](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则1从严管控)。任意一个MDM应用设置支持本地安装企业应用，则综合策略即为支持本地安装企业应用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| isEnable | boolean | 是 | 是否支持本地安装企业应用。true表示支持，false表示不支持。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ets
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let isEnable: boolean = true;
try {
  systemManager.setInstallLocalEnterpriseAppEnabled(wantTemp, isEnable);
  console.info('Succeeded in setting InstallLocalEnterpriseAppEnabled.');
} catch (err) {
  console.error(`Failed to set installLocalEnterpriseAppEnabled. Code is ${err.code}, message is ${err.message}`);
}
```

#### systemManager.getInstallLocalEnterpriseAppEnabled20+

getInstallLocalEnterpriseAppEnabled(admin: Want): boolean

查询是否支持本地安装企业应用。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持本地安装企业应用，true为支持，false为不支持。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ets
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let isEnable: boolean = systemManager.getInstallLocalEnterpriseAppEnabled(wantTemp);
  console.info('Succeeded in getting installLocalEnterpriseAppEnabled.');
} catch (err) {
  console.error(`Failed to get installLocalEnterpriseAppEnabled. Code is ${err.code}, message is ${err.message}`);
}
```

#### systemManager.setAutoUnlockAfterReboot20+

setAutoUnlockAfterReboot(admin: Want, isAllowed: boolean): void

设置设备重启自动解锁，仅针对无锁屏密码设备生效。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

冲突规则： [从严管控](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则1从严管控)，任意一个MDM应用设置设备重启自动解锁，则综合策略即为设备重启自动解锁。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| isAllowed | boolean | 是 | true表示设备重启后自动解锁，false表示设备重启后不自动解锁。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let isAllowed: boolean = true;
try {
  systemManager.setAutoUnlockAfterReboot(wantTemp, isAllowed);
  console.info('Succeeded in setting setAutoUnlockAfterReboot.');
} catch (err) {
  console.error(`Failed to set auto unlock after reboot. Code is ${err.code}, message is ${err.message}`);
}
```

#### systemManager.getAutoUnlockAfterReboot20+

getAutoUnlockAfterReboot(admin: Want): boolean

获取设备是否重启自动解锁。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示设备重启后自动解锁，返回false表示设备重启后不自动解锁。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  systemManager.getAutoUnlockAfterReboot(wantTemp);
  console.info('Succeeded in getting auto unlock after reboot.');
} catch (err) {
  console.error(`Failed to get auto unlock after reboot. Code is ${err.code}, message is ${err.message}`);
}
```

**systemManager.addKeyEventPolicies23+**

addKeyEventPolicies(admin: Want, keyPolicies: Array<KeyEventPolicy>): void

添加按键事件处理策略。系统触发按键事件时，若匹配下发的按键事件策略，将通过[EnterpriseAdminExtensionAbility.onKeyEvent](@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）.md#ZH-CN_TOPIC_0000002553201659__enterpriseadminextensionabilityonkeyevent23)回调通知MDM应用，并携带匹配策略的按键事件信息。

需要权限： ohos.permission.ENTERPRISE_MANAGE_SYSTEM

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

设备行为差异： 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| keyPolicies | Array<KeyEventPolicy> | 是 | 按键策略。支持物理按键（电源键、音量加、音量减），导航键（回退、主页、最近打开）。物理键支持任意组合为组合键，导航键不支持组合。组合键事件响应详见按键事件回调接口。 |

错误码：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

示例：

```ets
import { Want } from '@kit.AbilityKit';
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let keypolicy: Array<systemManager.KeyEventPolicy> = [
  {
    "keyCode": systemManager.KeyCode.POWER,
    "keyPolicy": systemManager.KeyPolicy.CUSTOM
  },
  {
    "keyCode": systemManager.KeyCode.VOLUME_UP,
    "keyPolicy": systemManager.KeyPolicy.CUSTOM
  }
];

try {
  systemManager.addKeyEventPolicies(wantTemp, keypolicy);
  console.info('Succeeded in adding key event policies.');
} catch (err) {
  console.error(`Failed to add key event policies. Code is ${err.code}, message is ${err.message}`);
}
```

**systemManager.removeKeyEventPolicies23+**

removeKeyEventPolicies(admin: Want, keyCodes: Array<KeyCode>): void

删除按键事件处理策略。

需要权限： ohos.permission.ENTERPRISE_MANAGE_SYSTEM

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

设备行为差异： 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| keyCodes | Array<KeyCode> | 是 | 按键编码。支持一次删除多条按键策略，删除不支持按键时返回9200012错误码。 |

错误码：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

示例：

```ets
import { Want } from '@kit.AbilityKit';
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let keyCodes: Array<systemManager.KeyCode> = [
  systemManager.KeyCode.POWER, systemManager.KeyCode.VOLUME_UP,
];

try {
  systemManager.removeKeyEventPolicies(wantTemp, keyCodes);
  console.info('Succeeded in removing key event policies.');
} catch (err) {
  console.error(`Failed to remove key event policies. Code is ${err.code}, message is ${err.message}`);
}
```

**systemManager.getKeyEventPolicies23+**

getKeyEventPolicies(admin: Want): Array<KeyEventPolicy>

获取按键事件处理策略。

需要权限： ohos.permission.ENTERPRISE_MANAGE_SYSTEM

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

设备行为差异： 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Array<KeyEventPolicy> | 返回当前配置的按键事件策略列表。 |

错误码：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

示例：

```ets
import { Want } from '@kit.AbilityKit';
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let result = Array<systemManager.KeyEventPolicy>;
try {
  result = systemManager.getKeyEventPolicies(wantTemp);
  console.info('Succeeded in getting key event policies.');
} catch (err) {
  console.error(`Failed to get key event policies. Code is ${err.code}, message is ${err.message}`);
}
```

**systemManager.startCollectLog23+**

startCollectLog(admin: Want): Promise<void>

开始收集设备上已生成并存储至硬盘的[faultlog](@ohos.faultLogger (故障日志获取).md#ZH-CN_TOPIC_0000002522081784__faulttype)日志，不支持收集未存储至硬盘的faultlog日志、应用业务日志和系统运行日志。

- 调用接口后，系统会启动一个日志收集任务，任务启动后接口立即返回。任务可能会因为系统性能等原因导致收集失败。

- 允许多个MDM应用调用，不同MDM应用在不同用户下收集的日志分开保存，互不影响。同一时间只允许一个MDM应用启动日志收集任务，在任务执行完成前调用本接口会返回错误码9201009，任务执行完成后，允许其他MDM应用调用。

- 任务执行完成后，通过[EnterpriseAdminExtensionAbility.onLogCollected](@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）.md#ZH-CN_TOPIC_0000002553201659__enterpriseadminextensionabilityonlogcollected23)回调函数通知给MDM应用，系统将已收集的日志文件挂载到MDM应用沙箱路径，MDM应用可以在回调函数中读取已收集的日志。

- 如果日志收集任务执行超过5分钟，[EnterpriseAdminExtensionAbility.onLogCollected](@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）.md#ZH-CN_TOPIC_0000002553201659__enterpriseadminextensionabilityonlogcollected23)回调函数会返回日志收集任务失败。

- 应用取走日志后，建议调用[systemManager.finishLogCollected](#ZH-CN_TOPIC_0000002522081694__systemmanagerfinishlogcollected23)删除已收集到的日志。

需要权限： ohos.permission.ENTERPRISE_READ_LOG

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

设备行为差异： 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

模型约束： 此接口仅可在Stage模型下使用。

冲突规则： 允许多个MDM应用调用，不同MDM应用在不同用户下收集的日志分开保存，互不影响。同一时间只允许一个MDM应用启动日志收集任务，在任务执行完成前调用本接口会返回错误码9201009，任务执行完成后，允许其他MDM应用调用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当收集日志任务创建失败时，会抛出错误对象。 |

错误码：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9201009 | Collecting logs, please try again later. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

示例：

```ets
import { Want } from '@kit.AbilityKit';
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

systemManager.startCollectLog(wantTemp).then(() => {
  console.info('Succeeded in starting collect log');
}).catch((err: BusinessError) => {
  console.error(`Failed to start collect log. Code: ${err.code}, message: ${err.message}`);
});
```

**systemManager.finishLogCollected23+**

finishLogCollected(admin: Want): void

删除本MDM应用在当前用户下收集到的设备日志。


在应用调用[startCollectLog](#ZH-CN_TOPIC_0000002522081694__systemmanagerstartcollectlog23)开始收集日志后，收到[EnterpriseAdminExtensionAbility.onLogCollected](@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）.md#ZH-CN_TOPIC_0000002553201659__enterpriseadminextensionabilityonlogcollected23)回调时，建议立即拷贝或者处理日志，并调用此接口删除收集到的日志。

若不调本接口，设备日志会占用系统存储空间，不影响下一次调用[startCollectLog](#ZH-CN_TOPIC_0000002522081694__systemmanagerstartcollectlog23)启动日志收集任务。

需要权限： ohos.permission.ENTERPRISE_READ_LOG

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

设备行为差异： 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

模型约束： 此接口仅可在Stage模型下使用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | Want | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

错误码：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

示例：

```ets
import { Want } from '@kit.AbilityKit';
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  systemManager.finishLogCollected(wantTemp);
  console.info('Succeeded in finishing log collected.');
} catch (err) {
  console.error(`Failed to finish log collected. Code is ${err.code}, message is ${err.message}`);
}
```

#### SystemUpdateInfo

待更新的系统版本信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| versionName | string | 否 | 否 | 待更新的系统版本名称。 |
| firstReceivedTime | number | 否 | 否 | 第一次收到系统更新包的时间。 |
| packageType | string | 否 | 否 | 待更新的系统更新包类型。 |

#### OtaUpdatePolicy

升级策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| policyType | PolicyType | 否 | 否 | 表示升级策略类型。 |
| version | string | 否 | 否 | 表示待升级软件版本号。 |
| latestUpdateTime | number | 否 | 是 | 表示最晚升级时间（时间戳）。 |
| delayUpdateTime | number | 否 | 是 | 表示延迟升级时间（单位：小时）。 |
| installStartTime | number | 否 | 是 | 表示指定安装窗口起始时间（时间戳）。 |
| installEndTime | number | 否 | 是 | 表示指定安装窗口结束时间（时间戳）。 |
| disableSystemOtaUpdate20+ | boolean | 否 | 是 | 表示是否禁用在公网环境下升级。true表示禁用公网升级，false表示不禁用公网升级。如果作为systemManager.setOtaUpdatePolicy的入参，该字段可缺省，缺省时保持当前配置不变。当前配置可通过systemManager.getOtaUpdatePolicy接口获取。禁用公网升级后，可以采用内网升级。推荐使用[restrictions.setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)禁用公网升级。 |

#### PolicyType

升级策略类型枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认升级策略。周期提示用户，用户确认后升级。 |
| PROHIBIT | 1 | 禁止升级策略。 |
| UPDATE_TO_SPECIFIC_VERSION | 2 | 强制升级策略。需指定最晚升级时间（latestUpdateTime）参数。 |
| WINDOWS | 3 | 指定时间窗口升级策略。需指定时间窗口参数（installStartTime、installEndTime）。 |
| POSTPONE | 4 | 延迟升级策略。延迟指定时间（delayUpdateTime）后进入DEFAULT模式，周期提示用户升级。 |

#### UpdatePackageInfo

系统更新包信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| version | string | 否 | 否 | 系统更新包版本号。 |
| packages | Array<Package> | 否 | 否 | 系统更新包详情。 |
| description | PackageDescription | 否 | 是 | 系统更新包描述信息。 |
| authInfo19+ | string | 否 | 是 | 系统更新包的鉴权信息。 |

#### Package

系统更新包详情。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | PackageType | 否 | 否 | 系统更新包类型。 |
| path | string | 否 | 否 | 系统更新包文件路径。若传入fd参数，该参数传入更新包文件名。 |
| fd | number | 否 | 是 | 系统更新包文件句柄。当前不支持只传入path参数，需要传入fd。 |

#### PackageDescription

系统更新包描述信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| notify | NotifyDescription | 否 | 是 | 企业自定义更新通知说明。 |

#### NotifyDescription

企业自定义更新通知说明。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| installTips | string | 否 | 是 | 企业自定义更新提示。 |
| installTipsDetail | string | 否 | 是 | 企业自定义更新提示详情。 |

#### UpdateResult

系统更新结果信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| version | string | 否 | 否 | 系统当前版本号。 |
| status | UpdateStatus | 否 | 否 | 系统更新状态。 |
| errorInfo | ErrorInfo | 否 | 否 | 系统更新错误信息。 |

#### ErrorInfo

系统更新错误信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 错误码。 |
| message | string | 否 | 否 | 错误描述信息。 |

#### PackageType

系统更新包类型。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FIRMWARE | 1 | 固件。 |

#### UpdateStatus

系统更新状态。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO_UPDATE_PACKAGE | -4 | 指定版本系统更新包不存在。 |
| UPDATE_WAITING | -3 | 系统更新包等待安装中。 |
| UPDATING | -2 | 正在更新。 |
| UPDATE_FAILURE | -1 | 更新失败。 |
| UPDATE_SUCCESS | 0 | 更新成功。 |

#### NearLinkProtocol20+

星闪协议枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SSAP | 0 | SSAP（SparkLink Service Access Protocol）协议。具体请参考SSAP协议。 |
| DATA_TRANSFER | 1 | 数据传输协议。具体请参考Data Transfer协议。 |

**KeyEventPolicy23+**

按键事件处理策略。按键事件发生时，仅拦截响应已下发按键事件处理策略的按键。对于未下发按键事件处理策略的按键事件，系统执行原先的响应逻辑。

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

模型约束： 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyCode | KeyCode | 否 | 否 | 按键编码。 |
| keyPolicy | KeyPolicy | 否 | 否 | 按键策略。 |

**KeyCode23+**

按键编码。[添加按键事件策略](#ZH-CN_TOPIC_0000002522081694__systemmanageraddkeyeventpolicies23)、[删除按键事件策略](#ZH-CN_TOPIC_0000002522081694__systemmanagerremovekeyeventpolicies23)、[获取按键事件策略](#ZH-CN_TOPIC_0000002522081694__systemmanagergetkeyeventpolicies23)和[按键事件回调](@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）.md#ZH-CN_TOPIC_0000002553201659__enterpriseadminextensionabilityonkeyevent23)接口通过按键编码映射到设备对应实际按键。

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

模型约束： 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| POWER | 0 | 电源键。 |
| VOLUME_UP | 1 | 音量加。 |
| VOLUME_DOWN | 2 | 音量减。 |
| BACK | 3 | 导航键-回退。 |
| HOME | 4 | 导航键-主页。 |
| RECENT | 5 | 导航键-最近打开。 |

**KeyPolicy23+**

按键策略。MDM应用下发按键策略的按键编码与系统按键事件匹配后的系统行为。

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

模型约束： 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERCEPTION | 0 | 拦截消息。设置后仅会拦截当前按键事件，系统不会再处理该事件，按键回调接口也不会响应按键事件。例如：下发电源键拦截策略后，按电源键无任何响应，无法关机，无法锁屏，仅影响开机状态下电源键事件，关机时可通过电源键正常开机。 |
| CUSTOM | 1 | 拦截并转发消息。 设置后会拦截当前按键事件，系统不会再处理该事件，同时通过EnterpriseAdminExtensionAbility.onKeyEvent回调接口将发生的按键事件通知给MDM应用，通知MDM应用处理该事件的过程不会阻塞系统后续的其他事件处理。 |

**KeyEvent23+**

按键事件。[EnterpriseAdminExtensionAbility.onKeyEvent](@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）.md#ZH-CN_TOPIC_0000002553201659__enterpriseadminextensionabilityonkeyevent23)按键事件回调触发时，传递当前按键事件信息。

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

模型约束： 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyCode | KeyCode | 否 | 否 | 按键编码。 |
| keyAction | KeyAction | 否 | 否 | 按键动作。 |
| actionTime | number | 否 | 否 | 按键动作发生时间，系统开机后微秒级时间戳。当按键长按时后续按键事件该参数不发生改变，应用可以通过该时间来判断该事件是否属于长按事件，以执行长按事件逻辑处理。 |
| keyItems | Array<KeyItem> | 否 | 否 | 其他按键信息，当前按键事件发生时，其他正在被按下的按键信息。 |

**KeyAction23+**

按键动作。

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

模型约束： 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | -1 | 除按下和抬起动作以外，其他按键动作。 |
| DOWN | 0 | 按键按下动作。 |
| UP | 1 | 按键抬起动作。 |

**KeyItem23+**

其他按键信息。当前[KeyCode](#ZH-CN_TOPIC_0000002522081694__keycode23)事件发生时，其他已被按下的按键信息。

系统能力： SystemCapability.Customization.EnterpriseDeviceManager

模型约束： 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyCode | KeyCode | 否 | 否 | 按键编码。 |
| pressed | boolean | 否 | 否 | 按键动作。按键是否被按下。true：按下；false：抬起 |
| downTime | number | 否 | 否 | 按键动作发生时间，系统开机后微秒级时间戳。导航按键不支持组合扩展，发生时间显示为0。 |