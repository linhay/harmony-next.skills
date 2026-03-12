# @ohos.enterprise.restrictions （限制类策略）

本模块提供设置通用限制类策略能力。可以全局禁用和解除禁用蓝牙、HDC、USB、Wi-Fi等特性。

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-guide)。

#### 导入模块

```ets
import { restrictions } from '@kit.MDMKit';
```

#### restrictions.setDisallowedPolicy

setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void

设置禁用/启用某特性。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS 或者 ohos.permission.PERSONAL_MANAGE_RESTRICTIONS15+

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。featurestring是

支持设置的特性清单参考表1。

**说明：** 从API version 15开始，应用申请权限ohos.permission.PERSONAL_MANAGE_RESTRICTIONS并[激活为自带设备管理应用](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__adminmanagerstartadminprovision15)，可以使用此接口设置以下特性：bluetooth、hdc、microphone、usb、wifi、tethering、camera、screenshot、screenRecord、nearLink、resetFactory。

disallowboolean是true表示禁止使用，false表示允许使用。

**表1 支持设置的特性清单：**

特性说明bluetooth设备蓝牙能力。当已经通过[addDisallowedBluetoothDevices](@ohos.enterprise.bluetoothManager（蓝牙管理）.md#ZH-CN_TOPIC_0000002497445608__bluetoothmanageradddisallowedbluetoothdevices20)接口或者[addAllowedBluetoothDevices](@ohos.enterprise.bluetoothManager（蓝牙管理）.md#ZH-CN_TOPIC_0000002497445608__bluetoothmanageraddallowedbluetoothdevices)接口设置了蓝牙设备禁用名单或者允许名单，再通过本接口禁用设备蓝牙能力，会优先生效禁用设备蓝牙能力。直到设备蓝牙能力启用后，禁止或允许名单才会生效。modifyDateTime设备修改系统时间能力。printer设备打印能力，当前仅支持PC/2in1设备使用。本接口禁用了设备打印能力时，通过[setDisallowedPolicyForAccount](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicyforaccount14)接口开启某用户的打印能力，该用户下的打印能力仍然被禁用。hdc被其他设备通过hdc连接、调试的能力。设置禁用后，其他设备无法通过hdc连接、调试此设备。microphone设备麦克风能力。fingerprint设备指纹认证能力。当已经通过[setDisallowedPolicyForAccount](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicyforaccount14)设置了某用户禁用设备指纹认证能力时，再通过本接口启用设备指纹认证能力，会报策略冲突。usb

设备USB能力。禁用后外接的USB设备无法使用，即在当前设备为HOST模式时，无法外接其他DEVICE设备。

以下四种情况再通过本接口禁用设备USB能力，会报策略冲突。

1）通过[addAllowedUsbDevices](@ohos.enterprise.usbManager（USB管理）.md#ZH-CN_TOPIC_0000002497445614__usbmanageraddallowedusbdevices)接口添加了USB设备可用名单。

2）通过[setUsbStorageDeviceAccessPolicy](@ohos.enterprise.usbManager（USB管理）.md#ZH-CN_TOPIC_0000002497445614__usbmanagersetusbstoragedeviceaccesspolicy)接口设置了USB存储设备访问策略为只读/禁用。

3）通过[addDisallowedUsbDevices](@ohos.enterprise.usbManager（USB管理）.md#ZH-CN_TOPIC_0000002497445614__usbmanageradddisallowedusbdevices14)接口添加了禁止使用的USB设备类型。

4）通过[setDisallowedPolicyForAccount](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicyforaccount14)接口禁用了某用户USB存储设备写入能力。

wifi设备Wi-Fi能力。tethering14+网络共享能力（设备已有网络共享给其他设备的能力，即共享热点能力）。inactiveUserFreeze14+非活跃用户运行能力，当前仅支持PC/2in1设备使用。企业空间场景下，系统切换到企业空间用户，个人空间用户属于非活跃用户。camera14+设备相机能力。mtpClient18+MTP客户端能力(包含读取和写入)，当前仅支持PC/2in1设备使用。MTP（MediaTransferProtocol，媒体传输协议），该协议允许用户在移动设备上线性访问媒体文件。当已经通过[setDisallowedPolicyForAccount](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicyforaccount14)设置了某用户禁用MTP客户端写入能力时，再通过本接口禁用MTP客户端能力，会报策略冲突。mtpServer18+MTP服务端能力。sambaClient20+samba客户端能力，当前仅支持PC/2in1设备使用。samba是在Linux和UNIX系统上实现SMB协议的一个免费软件，由服务器及客户端程序构成。SMB（Server Messages Block，信息服务块）是一种在局域网上共享文件和打印机的一种通信协议，它为局域网内的不同计算机之间提供文件及打印机等资源的共享服务。SMB协议是客户机/服务器型协议，客户机通过该协议可以访问服务器上的共享文件系统、打印机及其他资源。sambaServer20+samba服务端能力，当前仅支持PC/2in1设备使用。backupAndRestore20+备份和恢复能力，禁用后设备的"设置--系统--备份和恢复"、"设置--云空间"置灰，当前仅支持手机、平板使用。如果要完全禁用设备的备份和恢复能力，建议同时调用[applicationManager.addDisallowedRunningBundlesSync](zh-cn_topic_0000002497605586.html#ZH-CN_TOPIC_0000002497605586__applicationmanageradddisallowedrunningbundlessync)接口禁止具备备份和恢复能力的应用运行，如备份和恢复、手机助手、云空间应用。maintenanceMode20+设备维修模式能力。mms20+multimedia messaging service，设备接收、发送彩信的能力，当前仅支持手机、平板设备使用。sms20+short messaging service，设备接收、发送短信的能力，当前仅支持手机、平板设备使用。mobileData20+蜂窝数据能力，当前仅支持手机、平板设备使用。airplaneMode20+飞行模式能力，当前仅支持手机、平板设备使用。vpn20+Virtual Private Network（虚拟专用网络），VPN能力。notification20+设备通知能力。禁用后，由系统应用和三方应用发出的通知将不会显示，而系统服务通知能力不受影响。nfc20+Near Field Communication（近距离无线通信），NFC能力。privateSpace20+创建隐私空间能力，当前仅支持手机、平板使用。对已创建的隐私空间无效。telephoneCall20+设备通话能力，禁用后电话无法呼入和呼出。当前仅支持手机、平板设备使用。appClone21+[应用分身能力](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-clone)，禁用后无法创建应用分身。对已创建的应用分身无效。externalStorageCard21+

外置存储能力，禁用后设备无法使用外置存储，并且当前已连接的外置存储会被卸载。如果外置存储卸载时有文件正在被使用，可能会导致卸载失败，返回9200013错误码。

外置存储禁用后重新启用，需要手动重新连接外置存储。

randomMac21+Wi-Fi连接时使用随机MAC能力，设置禁用后，连接Wi-Fi仅能使用设备物理MAC。unmuteDevice22+设备媒体播放声音能力，设置禁用后，设备媒体播放将静音，[蜂窝通话](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-call-overview)能力不受影响。hdcRemote22+设备通过hdc调试其他设备的能力，当前仅支持PC/2in1设备设置。设置禁用后，无法通过hdc调试手机、平板、PC、智能手表等设备。screenshot设备截屏能力。screenRecord设备录屏能力。diskRecoveryKey恢复密钥导出能力。nearLink设备星闪能力。developerMode14+开发者模式，当前仅支持2in1设备使用。resetFactory18+恢复出厂能力。remoteDesk20+远程桌面能力，可通过点击我的华为-服务-快捷服务-智能检测-右上角更多-远程服务，查看远程桌面功能，当前仅支持手机、平板、2in1设备使用。remoteDisagnosis20+远程诊断能力，可通过点击我的华为-服务-快捷服务-智能检测-右上角更多-诊断分析，查看远程诊断功能，当前仅支持手机、平板、2in1设备使用。otaUpdate20+公网环境下系统升级能力。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.9200013The enterprise management policy has been successfully set, but the function has not taken effect in real time.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  restrictions.setDisallowedPolicy(wantTemp, 'printer', true);
  console.info('Succeeded in setting printer disabled');
} catch (err) {
  console.error(`Failed to set printer disabled. Code is ${err.code}, message is ${err.message}`);
}
```

#### restrictions.getDisallowedPolicy

getDisallowedPolicy(admin: Want | null, feature: string): boolean

查询某特性是否被禁用。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS 或者 ohos.permission.PERSONAL_MANAGE_RESTRICTIONS15+

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md) | null是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。featurestring是

支持查询的特性清单参考下表2。

**说明：** 从API version 15开始，应用申请权限ohos.permission.PERSONAL_MANAGE_RESTRICTIONS并[激活为自带设备管理应用](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__adminmanagerstartadminprovision15)，可以使用此接口获取以下特性状态：bluetooth、hdc、microphone、usb、wifi、tethering、camera、screenshot、screenRecord、nearLink、resetFactory。

**表2 支持查询的特性清单：**

特性说明bluetooth设备蓝牙能力。modifyDateTime设备修改系统时间能力。printer设备打印能力，当前仅支持PC/2in1设备使用。hdc被其他设备通过hdc连接、调试的能力。microphone设备麦克风能力。fingerprint设备指纹认证能力。usb设备USB能力。禁用后外接的USB设备无法使用，即在当前设备为HOST模式时，无法外接其他DEVICE设备。wifi设备Wi-Fi能力。tethering14+网络共享能力（设备已有网络共享给其他设备的能力，即共享热点能力）。inactiveUserFreeze14+非活跃用户运行能力，当前仅支持PC/2in1设备使用。企业空间场景下，系统切换到企业空间用户，个人空间用户属于非活跃用户。camera14+设备相机能力。mtpClient18+MTP客户端能力（包含读取和写入），当前仅支持PC/2in1设备使用。MTP（MediaTransferProtocol，媒体传输协议），该协议允许用户在移动设备上线性访问媒体文件。mtpServer18+MTP服务端能力。sambaClient20+samba客户端能力，当前仅支持PC/2in1设备使用。samba是在Linux和UNIX系统上实现SMB协议的一个免费软件，由服务器及客户端程序构成。SMB（Server Messages Block，信息服务块）是一种在局域网上共享文件和打印机的一种通信协议，它为局域网内的不同计算机之间提供文件及打印机等资源的共享服务。SMB协议是客户机/服务器型协议，客户机通过该协议可以访问服务器上的共享文件系统、打印机及其他资源。sambaServer20+samba服务端能力，当前仅支持PC/2in1设备使用。backupAndRestore20+备份和恢复能力，禁用后设备的"设置--系统--备份和恢复"、"设置--云空间"置灰，当前仅支持手机、平板使用。maintenanceMode20+设备维修模式能力。mms20+multimedia messaging service，设备接收、发送彩信的能力，当前仅支持手机、平板设备使用。sms20+short messaging service，设备接收、发送短信的能力，当前仅支持手机、平板设备使用。mobileData20+蜂窝数据能力，当前仅支持手机、平板设备使用。airplaneMode20+飞行模式能力，当前仅支持手机、平板设备使用。vpn20+Virtual Private Network（虚拟专用网络），VPN能力。notification20+设备通知能力。nfc20+Near Field Communication（近距离无线通信），NFC能力。privateSpace20+创建隐私空间能力，当前仅支持手机、平板使用。telephoneCall20+设备通话能力，禁用后电话无法呼入和呼出。当前仅支持手机、平板设备使用。appClone21+[应用分身能力](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-clone)，禁用后无法创建应用分身。externalStorageCard21+外置存储能力。randomMac21+Wi-Fi连接时使用随机MAC能力。unmuteDevice22+设备媒体播放声音能力，设置禁用后，设备媒体播放将静音，[蜂窝通话](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-call-overview)能力不受影响。hdcRemote22+设备通过hdc调试其他设备的能力，当前仅支持PC/2in1设备设置。screenshot设备截屏能力。screenRecord设备录屏能力。diskRecoveryKey恢复密钥导出能力。nearLink设备星闪能力。developerMode14+开发者模式，当前仅支持2in1设备使用。resetFactory18+恢复出厂能力。remoteDesk20+远程桌面能力，可通过点击我的华为-服务-快捷服务-智能检测-右上角更多-远程服务，查看远程桌面功能，当前仅支持手机、平板、2in1设备使用。remoteDisagnosis20+远程诊断能力，可通过点击我的华为-服务-快捷服务-智能检测-右上角更多-诊断分析，查看远程诊断功能，当前仅支持手机、平板、2in1设备使用。otaUpdate20+公网环境下系统升级能力。

**返回值：**

类型说明boolean返回true表示feature对应的某种特性被禁用，false表示feature对应的某种特性未被禁用。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: boolean = restrictions.getDisallowedPolicy(wantTemp, 'printer');
  console.info(`Succeeded in querying whether the printing function is disabled. Disabled status: ${result}`);
} catch (err) {
  console.error(`Failed to get printer disabled status. Code is ${err.code}, message is ${err.message}`);
}
```

#### restrictions.setDisallowedPolicyForAccount14+

setDisallowedPolicyForAccount(admin: Want, feature: string, disallow: boolean, accountId: number): void

设置禁用/启用指定用户的某特性。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。featurestring是

feature名称。

- fingerprint：设备指纹认证能力，当前仅支持PC/2in1设备使用。使用此参数时有以下规则：

1. 通过[setDisallowedPolicy](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了设备指纹认证能力，再使用本接口传入此参数，会报策略冲突。

2. 通过本接口设置禁用/启用指定用户的设备指纹认证能力后，再通过[setDisallowedPolicy](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用设备指纹认证能力时，后者会覆盖前者的策略。此后再通过[setDisallowedPolicy](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口启用设备指纹认证能力，则所有用户都允许使用设备指纹认证能力。

- print20+：设备打印能力，当前仅支持PC/2in1设备使用。如果使用本接口禁用了指定用户的设备打印能力，再通过[setDisallowedPolicy](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口启用设备打印能力，该用户下的设备打印能力仍然被禁用。

- mtpClient20+：MTP客户端能力（仅包含写入），当前仅支持PC/2in1设备使用。MTP（MediaTransferProtocol，媒体传输协议），该协议允许用户在移动设备上线性访问媒体文件。当已经通过[setDisallowedPolicy](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了设备MTP客户端能力时，再通过本接口禁用某用户MTP客户端写入能力，会报策略冲突。

- usbStorageDeviceWrite20+：USB存储设备写入能力，当前仅支持PC/2in1设备使用。

以下三种情况再通过本接口禁用某用户USB存储设备写入能力，会报策略冲突。

1）通过[setDisallowedPolicy](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口设置了设备USB能力禁用。

2）通过[setUsbStorageDeviceAccessPolicy](@ohos.enterprise.usbManager（USB管理）.md#ZH-CN_TOPIC_0000002497445614__usbmanagersetusbstoragedeviceaccesspolicy)接口设置了USB存储设备访问策略为只读/禁用。

3）通过[addDisallowedUsbDevices](@ohos.enterprise.usbManager（USB管理）.md#ZH-CN_TOPIC_0000002497445614__usbmanageradddisallowedusbdevices14)接口添加了存储类型的USB设备禁用。

- diskRecoveryKey20+：恢复[密钥导出](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-export-key-arkts)能力，当前仅支持2in1设备使用。

- sudo20+：superuser do，表示以超级用户执行，当前仅支持PC/2in1设备使用。禁用后企业空间或个人空间不能以超级用户执行。

- distributedTransmissionOutgoing20+：设备间单向传输数据的能力（仅包含向其他设备传输数据）。

disallowboolean是true表示禁用，false表示启用。accountIdnumber是

用户ID，取值范围：大于等于0。

accountId可以通过[getOsAccountLocalId](@ohos.account.osAccount (系统账号管理).md#ZH-CN_TOPIC_0000002529285493__getosaccountlocalid9)等接口来获取。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002the administrator application does not have permission to manage the device.9200010A conflict policy has been configured.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  restrictions.setDisallowedPolicyForAccount(wantTemp, 'fingerprint', true, 100);
  console.info('Succeeded in setting fingerprint disabled');
} catch (err) {
  console.error(`Failed to set fingerprint disabled. Code is ${err.code}, message is ${err.message}`);
}
```

#### restrictions.getDisallowedPolicyForAccount14+

getDisallowedPolicyForAccount(admin: Want | null, feature: string, accountId: number): boolean

获取指定用户的某特性状态。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md) | null是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。featurestring是

feature名称。

- fingerprint：设备指纹认证能力，当前仅支持PC/2in1设备使用。使用此参数时有以下规则：当已经通过[setDisallowedPolicyForAccount](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicyforaccount14)接口设置禁用/启用指定用户的设备指纹认证能力后，再通过[setDisallowedPolicy](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用设备指纹认证能力时，后者会覆盖前者的策略。即此时调用本接口结果为false。

- mtpClient20+：MTP客户端能力（仅包含写入），当前仅支持PC/2in1设备使用。MTP（MediaTransferProtocol，媒体传输协议），该协议允许用户在移动设备上线性访问媒体文件。

- usbStorageDeviceWrite20+：USB存储设备写入能力，当前仅支持PC/2in1设备使用。

- diskRecoveryKey20+：恢复[密钥导出](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-export-key-arkts)能力，当前仅支持2in1设备使用。

- sudo20+：superuser do，表示以超级用户执行，当前仅支持PC/2in1设备使用。禁用后企业空间或个人空间不能以超级用户执行。

- distributedTransmissionOutgoing20+：设备间单向传输数据的能力（仅包含向其他设备传输数据）。

- print20+：设备打印能力，当前仅支持PC/2in1设备使用。如果使用[setDisallowedPolicy](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicy)接口禁用了设备打印能力，再通过[setDisallowedPolicyForAccount](#ZH-CN_TOPIC_0000002529285583__restrictionssetdisallowedpolicyforaccount14)接口启用某用户下的设备打印能力，通过本接口查询结果是该用户已启用打印能力，但实际打印能力已被禁用。

accountIdnumber是

用户ID，取值范围：大于等于0。

accountId可以通过[getOsAccountLocalId](@ohos.account.osAccount (系统账号管理).md#ZH-CN_TOPIC_0000002529285493__getosaccountlocalid9)等接口来获取。

**返回值：**

类型说明boolean返回true表示参数feature对应的特性被禁用，false表示参数feature对应的特性未被禁用。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002the administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: boolean = restrictions.getDisallowedPolicyForAccount(wantTemp, 'fingerprint', 100);
  console.info(`Succeeded in querying is the fingerprint function disabled : ${result}`);
} catch (err) {
  console.error(`Failed to set fingerprint disabled. Code is ${err.code}, message is ${err.message}`);
}
```

#### restrictions.addDisallowedListForAccount14+

addDisallowedListForAccount(admin: Want, feature: string, list: Array<string>, accountId: number): void

为指定用户添加禁止使用某特性的应用名单。指定用户下，添加到名单中的应用不允许使用指定的特性能力。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。featurestring是

feature名称。

- snapshotSkip：屏幕快照能力。

listArray<string>是包名等内容的名单集合。accountIdnumber是

用户ID，取值范围：大于等于0。

accountId可以通过[getOsAccountLocalId](@ohos.account.osAccount (系统账号管理).md#ZH-CN_TOPIC_0000002529285493__getosaccountlocalid9)等接口来获取。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let valueList:Array<string> = ["com.xx.aa.", "com.xx.bb"];
try {
  // 参数需根据实际情况进行替换
  restrictions.addDisallowedListForAccount(wantTemp, 'snapshotSkip', valueList, 100);
  console.info('Succeeded in adding disallowed snapshotSkip feature');
} catch (err) {
  console.error(`Failed to add disallowed snapshotSkip feature. Code is ${err.code}, message is ${err.message}`);
}
```

#### restrictions.removeDisallowedListForAccount14+

removeDisallowedListForAccount(admin: Want, feature: string, list: Array<string>, accountId: number): void

为指定用户移除禁止使用某特性的应用名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。featurestring是

feature名称。

- snapshotSkip：屏幕快照能力。

listArray<string>是包名等内容的名单集合。accountIdnumber是

用户ID，取值范围：大于等于0。

accountId可以通过[getOsAccountLocalId](@ohos.account.osAccount (系统账号管理).md#ZH-CN_TOPIC_0000002529285493__getosaccountlocalid9)等接口来获取。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let valueList:Array<string> = ["com.xx.aa.", "com.xx.bb"];
try {
  // 参数需根据实际情况进行替换
  restrictions.removeDisallowedListForAccount(wantTemp, 'snapshotSkip', valueList, 100);
  console.info('Succeeded in removing disallowed snapshotSkip feature');
} catch (err) {
  console.error(`Failed to remove disallowed snapshotSkip feature. Code is ${err.code}, message is ${err.message}`);
}
```

#### restrictions.getDisallowedListForAccount14+

getDisallowedListForAccount(admin: Want, feature: string, accountId: number): Array<string>

获取指定用户禁止使用某特性的应用名单。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。featurestring是

feature名称。

- snapshotSkip：屏幕快照能力。

accountIdnumber是

用户ID，取值范围：大于等于0。

accountId可以通过[getOsAccountLocalId](@ohos.account.osAccount (系统账号管理).md#ZH-CN_TOPIC_0000002529285493__getosaccountlocalid9)等接口来获取。

**返回值：**

类型说明Array<string>用户已添加的禁用某特征的应用名单。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: Array<string> = restrictions.getDisallowedListForAccount(wantTemp, 'snapshotSkip', 100);
  console.info('Succeeded in querying disallowed list for account');
} catch (err) {
  console.error(`Failed to query disallowed list for account. Code is ${err.code}, message is ${err.message}`);
}
```

#### restrictions.setUserRestriction20+

setUserRestriction(admin: Want, settingsItem: string, restricted: boolean): void

设置用户行为的限制规则。

**需要权限：** ohos.permission.ENTERPRISE_SET_USER_RESTRICTION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。settingsItemstring是

行为名称。

- setApn：APN设置，当前仅支持手机、平板使用。

- powerLongPress：长按电源键打开电源菜单，当前仅支持手机、平板使用。

- setEthernetIp：修改以太网IP地址，当前仅支持PC/2in1设备使用。

- setDeviceName：修改设备名称，当前仅支持PC/2in1设备、手机、平板使用。禁用后，PC/2in1设备的设置中以下设备名称无法修改，包括关于本机、蓝牙、多设备协同->星闪。手机、平板设备设置中的关于本机、蓝牙、个人热点的设备名称无法修改。

- setBiometricsAndScreenLock：修改锁屏密码，当前仅支持PC/2in1设备、手机、平板使用。

restrictedboolean是是否禁用行为。true表示禁用，false表示不禁用。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { restrictions } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  restrictions.setUserRestriction(wantTemp, 'setApn', true);
  console.info('Succeeded in restricting from setting apn');
} catch (err) {
  console.error(`Failed to restrict from setting apn. Code is ${err.code}, message is ${err.message}`);
}
```

#### restrictions.getUserRestricted20+

getUserRestricted(admin: Want, settingsItem: string): boolean

获取设置项的禁用状态。

**需要权限：** ohos.permission.ENTERPRISE_SET_USER_RESTRICTION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明admin[Want](@ohos.app.ability.Want (Want).md)是企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。settingsItemstring是

指定设置项。

- setEthernetIp：修改以太网IP地址，当前仅支持PC/2in1设备使用。

- setDeviceName：修改设备名称，当前仅支持PC/2in1设备、手机、平板使用。PC/2in1设备设置中关于本机、蓝牙、多设备协同->星闪中的设备名称。手机、平板设备设置中关于本机、蓝牙、个人热点的设备名称。

- setBiometricsAndScreenLock：修改锁屏密码，当前仅支持PC/2in1设备、手机、平板使用。

**返回值：**

类型说明boolean返回指定设置项的禁用状态，true表示已禁用，false表示未禁用。

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](企业设备管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息9200001The application is not an administrator application of the device.9200002The administrator application does not have permission to manage the device.201Permission verification failed. The application does not have the permission required to call the API.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { restrictions } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 入参需根据实际情况替换
  let result: boolean = restrictions.getUserRestricted(wantTemp, 'setEthernetIp');
  console.info('Succeeded in getting user restricted');
} catch (err) {
  console.error(`Failed to get user restricted. Code is ${err.code}, message is ${err.message}`);
}
```