# @ohos.enterprise.usbManager（USB管理）

本模块提供USB管理能力。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-guide)。

全局通用限制类策略由restrictions统一提供，若要全局禁用USB，请参考[@ohos.enterprise.restrictions（限制类策略）](@ohos.enterprise.restrictions （限制类策略）.md)。

#### 导入模块

```ets
import { usbManager } from '@kit.MDMKit';
```

#### usbManager.addAllowedUsbDevices

addAllowedUsbDevices(admin: Want, usbDeviceIds: Array<UsbDeviceId>): void

添加USB设备可用名单。

以下情况下，调用本接口会报策略冲突：

1. 已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了设备USB能力。
1. 已经通过[setUsbStorageDeviceAccessPolicy](#ZH-CN_TOPIC_0000002497445614__usbmanagersetusbstoragedeviceaccesspolicy)接口设置了USB存储设备访问策略为禁用。
1. 已经通过[addDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanageradddisallowedusbdevices14)接口添加了禁止使用的USB设备类型。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。usbDeviceIdsArray<[UsbDeviceId](#ZH-CN_TOPIC_0000002497445614__usbdeviceid)>是USB设备ID数组，UsbDeviceId信息可以通过[getDevices](zh-cn_topic_0000002497445526.html#ZH-CN_TOPIC_0000002497445526__usbmanagergetdevices)接口获取。USB设备可用名单数组长度上限为1000，若当前允许名单中已有300个USB设备ID，则只允许再添加700个。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.9200010A conflict policy has been configured.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDeviceIds: Array<usbManager.UsbDeviceId> = [{
      vendorId: 1,
      productId: 1
  }];
  usbManager.addAllowedUsbDevices(wantTemp, usbDeviceIds);
  console.info(`Succeeded in adding allowed USB devices.`);
} catch (err) {
  console.error(`Failed to add allowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

#### usbManager.removeAllowedUsbDevices

removeAllowedUsbDevices(admin: Want, usbDeviceIds: Array<UsbDeviceId>): void

移除USB设备可用名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。usbDeviceIdsArray<[UsbDeviceId](#ZH-CN_TOPIC_0000002497445614__usbdeviceid)>是USB设备ID数组，UsbDeviceId信息可以通过[getDevices](zh-cn_topic_0000002497445526.html#ZH-CN_TOPIC_0000002497445526__usbmanagergetdevices)接口获取。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDeviceIds: Array<usbManager.UsbDeviceId> = [{
      vendorId: 1,
      productId: 1
  }];
  usbManager.removeAllowedUsbDevices(wantTemp, usbDeviceIds);
  console.info(`Succeeded in removing allowed USB devices.`);
} catch (err) {
  console.error(`Failed to remove allowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

#### usbManager.getAllowedUsbDevices

getAllowedUsbDevices(admin: Want): Array<UsbDeviceId>

获取USB设备可用名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明Array<[UsbDeviceId](#ZH-CN_TOPIC_0000002497445614__usbdeviceid)>可用USB允许名单设备ID数组。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: Array<usbManager.UsbDeviceId> = usbManager.getAllowedUsbDevices(wantTemp);
  console.info(`Succeeded in getting allowed USB devices. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get allowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

#### usbManager.setUsbStorageDeviceAccessPolicy

setUsbStorageDeviceAccessPolicy(admin: Want, usbPolicy: UsbPolicy): void

设置USB存储设备访问策略。

在调用接口前，确保已暂停USB存储设备的读写操作，保证操作的稳定性和数据的完整性，否则可能出现不可预期的异常。

以下情况下，通过本接口设置USB存储设备访问策略为可读可写/只读，会报策略冲突：

1. 已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了设备USB能力。
1. 已经通过[addDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanageradddisallowedusbdevices14)接口将存储类型的USB设备添加为禁止使用的USB设备类型。
1. 已经通过[setDisallowedPolicyForAccount](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicyforaccount14)接口禁用了某用户USB存储设备写入能力。

以下情况下，通过本接口设置USB存储设备访问策略为禁用，会报策略冲突：

1. 已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了设备USB能力。
1. 已经通过[addAllowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanageraddallowedusbdevices)接口添加了USB设备可用名单。
1. 已经通过[setDisallowedPolicyForAccount](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicyforaccount14)接口禁用了某用户USB存储设备写入能力。

通过本接口设置，或者通过[addDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanageradddisallowedusbdevices14)接口添加存储类型的USB设备，均可禁用USB存储设备。推荐使用后者。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。usbPolicy[UsbPolicy](#ZH-CN_TOPIC_0000002497445614__usbpolicy)是USB存储设备访问策略。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.9200010A conflict policy has been configured.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let policy: usbManager.UsbPolicy = usbManager.UsbPolicy.DISABLED;
  usbManager.setUsbStorageDeviceAccessPolicy(wantTemp, policy);
  console.info(`Succeeded in setting USB storage device access policy.`);
} catch (err) {
  console.error(`Failed to set USB storage device access policy. Code: ${err.code}, message: ${err.message}`);
}
```

#### usbManager.getUsbStorageDeviceAccessPolicy

getUsbStorageDeviceAccessPolicy(admin: Want): UsbPolicy

获取USB存储设备访问策略。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明[UsbPolicy](#ZH-CN_TOPIC_0000002497445614__usbpolicy)USB存储设备访问策略。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: usbManager.UsbPolicy = usbManager.getUsbStorageDeviceAccessPolicy(wantTemp);
  console.info(`Succeeded in getting USB storage device access policy. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get USB storage device access policy. Code: ${err.code}, message: ${err.message}`);
}
```

#### usbManager.addDisallowedUsbDevices14+

addDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void

添加禁止使用的USB设备类型。

以下情况下，调用本接口会报策略冲突：

1. 已经通过[setDisallowedPolicy](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了设备USB能力。
1. 已经通过[addAllowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanageraddallowedusbdevices)接口添加了USB设备可用名单。
1. 已经通过[setDisallowedPolicyForAccount](@ohos.enterprise.restrictions （限制类策略）.md#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicyforaccount14)接口禁用了某用户USB存储设备写入能力。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。usbDevicesArray<[UsbDeviceType](#ZH-CN_TOPIC_0000002497445614__usbdevicetype14)>是要添加的USB设备类型的数组，UsbDeviceType信息可以通过[getDevices](zh-cn_topic_0000002497445526.html#ZH-CN_TOPIC_0000002497445526__usbmanagergetdevices)接口获取。USB设备禁用名单数组长度上限为200，若当前禁用名单中已有100个USB设备ID，则只允许再添加100个。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.9200010A conflict policy has been configured.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDevices: Array<usbManager.UsbDeviceType> = [{
      baseClass: 8,
      subClass: 0,
      protocol: 0,
      descriptor: usbManager.Descriptor.INTERFACE
  }];
  usbManager.addDisallowedUsbDevices(wantTemp, usbDevices);
  console.info(`Succeeded in adding disallowed USB devices.`);
} catch (err) {
  console.error(`Failed to add disallowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

#### usbManager.removeDisallowedUsbDevices14+

removeDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void

移除禁止使用的USB设备类型。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。usbDevicesArray<[UsbDeviceType](#ZH-CN_TOPIC_0000002497445614__usbdevicetype14)>是要移除的USB设备类型的数组，UsbDeviceType信息可以通过[getDevices](zh-cn_topic_0000002497445526.html#ZH-CN_TOPIC_0000002497445526__usbmanagergetdevices)接口获取。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDevices: Array<usbManager.UsbDeviceType> = [{
      baseClass: 8,
      subClass: 0,
      protocol: 0,
      descriptor: usbManager.Descriptor.INTERFACE
  }];
  usbManager.removeDisallowedUsbDevices(wantTemp, usbDevices);
  console.info(`Succeeded in removing disallowed USB devices.`);
} catch (err) {
  console.error(`Failed to remove disallowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

#### usbManager.getDisallowedUsbDevices14+

getDisallowedUsbDevices(admin: Want): Array<UsbDeviceType>

获取禁止使用的USB设备类型。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。

**返回值：**

类型说明Array<[UsbDeviceType](#ZH-CN_TOPIC_0000002497445614__usbdevicetype14)>禁止使用的USB设备类型。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: Array<usbManager.UsbDeviceType> = usbManager.getDisallowedUsbDevices(wantTemp);
  console.info(`Succeeded in getting disallowed USB devices. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

#### UsbDeviceId

USB设备ID信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明vendorIdnumber否否厂商ID。productIdnumber否否产品ID。

#### UsbDeviceType14+

USB设备类型信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明baseClassnumber否否

类型编码。

可通过[getDevices](@ohos.usbManager (USB管理).md#ZH-CN_TOPIC_0000002497445526__usbmanagergetdevices)接口获取已接入主设备的USB设备列表，需在返回值列表中查找当前设备，查看其值。

先根据此值确定descriptor应该传入的类型。若descriptor为DEVICE，则本字段取USBDevice.clazz字段值，若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.clazz字段值。

若字段值为255，表示此设备的类型编码是厂商自定义编码，则使用[addDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效；若字段值未在[defined-class-codes](https://www.usb.org/defined-class-codes)中定义，则使用[addDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效。

subClassnumber否否

子类型编码。

可通过[getDevices](@ohos.usbManager (USB管理).md#ZH-CN_TOPIC_0000002497445526__usbmanagergetdevices)接口获取已接入主设备的USB设备列表，需在返回值列表中查找当前设备，查看其值。

先根据baseClass的值确定descriptor应该传入的类型。若descriptor为DEVICE，则本字段取USBDevice.subClass字段值，若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.subClass字段值。

若字段值为255，表示此设备的子类型编码是厂商自定义编码，则使用[addDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效；若字段值未在[defined-class-codes](https://www.usb.org/defined-class-codes)中定义，则使用[addDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效。

protocolnumber否否

协议编码。

可通过[getDevices](@ohos.usbManager (USB管理).md#ZH-CN_TOPIC_0000002497445526__usbmanagergetdevices)接口获取已接入主设备的USB设备列表，需在返回值列表中查找当前设备，查看其值。

先根据baseClass的值确定descriptor应该传入的类型。若descriptor为DEVICE，则本字段取USBDevice.protocol字段值，若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.protocol字段值。

若字段值为255，表示此设备的协议编码是厂商自定义编码，则使用[addDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效；若字段值未在[defined-class-codes](https://www.usb.org/defined-class-codes)中定义，则使用[addDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效。

descriptor[Descriptor](#ZH-CN_TOPIC_0000002497445614__descriptor14)否否

USB描述符。

可通过[getDevices](@ohos.usbManager (USB管理).md#ZH-CN_TOPIC_0000002497445526__usbmanagergetdevices)接口获取已接入主设备的USB设备列表，需在返回值列表中查找当前设备，查看其值。

若此值USBDevice.clazz字段值为0，则须在[defined-class-codes](https://www.usb.org/defined-class-codes)中的Base Class列查找此值USBDevice.configs.interfaces.clazz字段值，查找结果所在行所对应的Descriptor Usage列就表示当前应该传入的descriptor类型（若Descriptor Usage列为Both，表示两种类型都可以传入，需要设备级禁用时传入DEVICE，需要接口级禁用时传入INTERFACE）;

若此值USBDevice.clazz字段值为255，表示此设备的类型编码是厂商自定义编码，则使用[addDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](#ZH-CN_TOPIC_0000002497445614__usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效；若此值USBDevice.clazz字段值为其他值，则须在[defined-class-codes](https://www.usb.org/defined-class-codes)中的Base Class列查找该值，查找结果所在行所对应的Descriptor Usage列就表示当前应该传入的descriptor类型（若Descriptor Usage列为Both，表示两种类型都可以传入，需要设备级禁用时传入DEVICE，需要接口级禁用时传入INTERFACE）。

#### UsbPolicy

USB读写策略的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称值说明READ_WRITE0可读可写。READ_ONLY1只读。DISABLED2禁用。

#### Descriptor14+

USB描述符的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称值说明INTERFACE0接口描述符。DEVICE1设备描述符。