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

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。serverstring是NTP服务器地址（以","分隔，如"ntpserver1.com,ntpserver2.com"。最大长度96字节，包括结束符）。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明stringstring对象，返回NTP时间服务器信息。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@ohos.base';

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

设置升级策略。内网升级场景下，需要先调用[systemManager.notifyUpdatePackages](#ZH-CN_TOPIC_0000002497605592__systemmanagernotifyupdatepackages)接口通知系统更新包，再调用该接口设置升级策略。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。policy[OtaUpdatePolicy](#ZH-CN_TOPIC_0000002497605592__otaupdatepolicy)是升级策略。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明[OtaUpdatePolicy](#ZH-CN_TOPIC_0000002497605592__otaupdatepolicy)OtaUpdatePolicy对象，返回升级策略。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

通知系统更新包信息。内网升级场景下，需要先调用该接口通知系统更新包，再调用[systemManager.setOtaUpdatePolicy](#ZH-CN_TOPIC_0000002497605592__systemmanagersetotaupdatepolicy)设置升级策略。

该接口比较耗时，当调用此接口后，后续如果在应用主线程调用其他同步接口时需要等待该接口异步返回。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。packageInfo[UpdatePackageInfo](#ZH-CN_TOPIC_0000002497605592__updatepackageinfo)是

系统更新包信息。

**说明：** 传入的UpdatePackageInfo.packages.path必须是“update”开头的zip压缩包，传入其他形式的文件会报9201004错误码。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。当通知系统更新包失败时会抛出错误对象。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.9201004The update packages do not exist or analyzing failed.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。versionstring是更新包版本号。

**返回值：**

类型说明Promise<[UpdateResult](#ZH-CN_TOPIC_0000002497605592__updateresult)>Promise对象，返回系统更新结果。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

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

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明Promise<string>Promise对象，返回系统更新的鉴权数据。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

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

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。protocolsArray<[NearLinkProtocol](#ZH-CN_TOPIC_0000002497605592__nearlinkprotocol20)>是星闪协议列表。accountIdnumber是

用户ID，取值范围：大于等于0。

accountId可以通过[getOsAccountLocalId](@ohos.account.osAccount (系统账号管理).md#ZH-CN_TOPIC_0000002529285493__getosaccountlocalid9)等接口来获取。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.9200012Parameter verification failed.201Permission verification failed. The application does not have the permission required to call the API.801Capability not supported. Failed to call the API due to limited device capabilities.

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

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。protocolsArray<[NearLinkProtocol](#ZH-CN_TOPIC_0000002497605592__nearlinkprotocol20)>是星闪协议列表。accountIdnumber是

用户ID，取值范围：大于等于0。

accountId可以通过[getOsAccountLocalId](@ohos.account.osAccount (系统账号管理).md#ZH-CN_TOPIC_0000002529285493__getosaccountlocalid9)等接口来获取。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.9200012Parameter verification failed.201Permission verification failed. The application does not have the permission required to call the API.801Capability not supported. Failed to call the API due to limited device capabilities.

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

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。accountIdnumber是

用户ID，取值范围：大于等于0。

accountId可以通过[getOsAccountLocalId](@ohos.account.osAccount (系统账号管理).md#ZH-CN_TOPIC_0000002529285493__getosaccountlocalid9)等接口来获取。

**返回值：**

类型说明Array<[NearLinkProtocol](#ZH-CN_TOPIC_0000002497605592__nearlinkprotocol20)>指定用户下禁用的星闪协议名单。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.801Capability not supported. Failed to call the API due to limited device capabilities.

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

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。isEnableboolean是是否支持本地安装企业应用。true表示支持，false表示不支持。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.801Capability not supported. Failed to call the API due to limited device capabilities.

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

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明boolean是否支持本地安装企业应用，true为支持，false为不支持。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.801Capability not supported. Failed to call the API due to limited device capabilities.

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

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。isAllowedboolean是true表示设备重启后自动解锁，false表示设备重启后不自动解锁。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.801Capability not supported. Failed to call the API due to limited device capabilities.

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

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明boolean返回true表示设备重启后自动解锁，返回false表示设备重启后不自动解锁。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.801Capability not supported. Failed to call the API due to limited device capabilities.

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

#### SystemUpdateInfo

待更新的系统版本信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明versionNamestring否否待更新的系统版本名称。firstReceivedTimenumber否否第一次收到系统更新包的时间。packageTypestring否否待更新的系统更新包类型。

#### OtaUpdatePolicy

升级策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明policyType[PolicyType](#ZH-CN_TOPIC_0000002497605592__policytype)否否表示升级策略类型。versionstring否否表示待升级软件版本号。latestUpdateTimenumber否是表示最晚升级时间（时间戳）。delayUpdateTimenumber否是表示延迟升级时间（单位：小时）。installStartTimenumber否是表示指定安装窗口起始时间（时间戳）。installEndTimenumber否是表示指定安装窗口结束时间（时间戳）。disableSystemOtaUpdate20+boolean否是表示是否禁用在公网环境下升级。true表示禁用公网升级，false表示不禁用公网升级。如果作为[systemManager.setOtaUpdatePolicy](#ZH-CN_TOPIC_0000002497605592__systemmanagersetotaupdatepolicy)的入参，该字段可缺省，缺省时保持当前配置不变。当前配置可通过[systemManager.getOtaUpdatePolicy](#ZH-CN_TOPIC_0000002497605592__systemmanagergetotaupdatepolicy)接口获取。禁用公网升级后，可以采用内网升级。推荐使用[restrictions.setDisallowedPolicy](zh-cn_topic_0000002529285583.html#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)禁用公网升级。

#### PolicyType

升级策略类型枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称值说明DEFAULT0默认升级策略。周期提示用户，用户确认后升级。PROHIBIT1禁止升级策略。UPDATE_TO_SPECIFIC_VERSION2强制升级策略。需指定最晚升级时间（latestUpdateTime）参数。WINDOWS3指定时间窗口升级策略。需指定时间窗口参数（installStartTime、installEndTime）。POSTPONE4延迟升级策略。延迟指定时间（delayUpdateTime）后进入DEFAULT模式，周期提示用户升级。

#### UpdatePackageInfo

系统更新包信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明versionstring否否系统更新包版本号。packagesArray<[Package](#ZH-CN_TOPIC_0000002497605592__package)>否否系统更新包详情。description[PackageDescription](#ZH-CN_TOPIC_0000002497605592__packagedescription)否是系统更新包描述信息。authInfo19+string否是系统更新包的鉴权信息。

#### Package

系统更新包详情。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明type[PackageType](#ZH-CN_TOPIC_0000002497605592__packagetype)否否系统更新包类型。pathstring否否系统更新包文件路径。若传入fd参数，该参数传入更新包文件名。fdnumber否是系统更新包文件句柄。当前不支持只传入path参数，需要传入fd。

#### PackageDescription

系统更新包描述信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明notify[NotifyDescription](#ZH-CN_TOPIC_0000002497605592__notifydescription)否是企业自定义更新通知说明。

#### NotifyDescription

企业自定义更新通知说明。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明installTipsstring否是企业自定义更新提示。installTipsDetailstring否是企业自定义更新提示详情。

#### UpdateResult

系统更新结果信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明versionstring否否系统当前版本号。status[UpdateStatus](#ZH-CN_TOPIC_0000002497605592__updatestatus)否否系统更新状态。errorInfo[ErrorInfo](#ZH-CN_TOPIC_0000002497605592__errorinfo)否否系统更新错误信息。

#### ErrorInfo

系统更新错误信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明codenumber否否错误码。messagestring否否错误描述信息。

#### PackageType

系统更新包类型。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称值说明FIRMWARE1固件。

#### UpdateStatus

系统更新状态。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称值说明NO_UPDATE_PACKAGE-4指定版本系统更新包不存在。UPDATE_WAITING-3系统更新包等待安装中。UPDATING-2正在更新。UPDATE_FAILURE-1更新失败。UPDATE_SUCCESS0更新成功。

#### NearLinkProtocol20+

星闪协议枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

名称值说明SSAP0SSAP（SparkLink Service Access Protocol）协议。具体请参考[SSAP协议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-terminology#section79222173354)。DATA_TRANSFER1数据传输协议。具体请参考[Data Transfer协议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-terminology#section6203121773712)。