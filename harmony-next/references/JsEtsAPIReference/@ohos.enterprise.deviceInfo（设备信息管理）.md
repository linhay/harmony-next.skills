# @ohos.enterprise.deviceInfo（设备信息管理）

本模块提供企业设备信息管理能力，包括获取设备序列号、设备名称等。

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-guide)。

#### 导入模块

```ets
import { deviceInfo } from '@kit.MDMKit';
```

#### deviceInfo.getDeviceInfo

getDeviceInfo(admin: Want, label: string): string

获取设备信息。

**需要权限：** ohos.permission.ENTERPRISE_GET_DEVICE_INFO

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。labelstring是

支持获取的设备信息标签。

- deviceName：设备名称。

- deviceSerial：设备序列号。

- simInfo：SIM卡信息。

- disk：硬盘信息。

- memory：内存信息。

**返回值：**

类型说明string

返回label对应的参数值。

当label为simInfo时，返回值为表示SIM卡信息的JSON字符串。例如：[{"slotId": 0, "MEID": "", "IMSI": "", "ICCID": "", "IMEI": ""}, {"slotId": 1, "MEID": "", "IMSI": "", "ICCID": "", "IMEI": ""}]，其中：slotId:0表示卡槽1，slotId:1表示卡槽2。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { deviceInfo } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 需根据实际情况进行替换
  let result: string = deviceInfo.getDeviceInfo(wantTemp, 'deviceName');
  console.info(`Succeeded in getting device name, result : ${result}`);
} catch (err) {
  console.error(`Failed to get device name. Code: ${err.code}, message: ${err.message}`);
}
```