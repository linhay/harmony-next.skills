# @ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）

本模块提供[企业设备管理扩展能力](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-term#企业设备管理扩展能力)。

设备管理应用需要存在一个EnterpriseAdminExtensionAbility并重写相关接口，以此具备模块提供的各项能力，比如接收由系统发送的该应用被激活或者解除激活的通知。

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';
```

#### EnterpriseAdminExtensionAbility.onAdminEnabled

onAdminEnabled(): void

设备管理应用被激活事件回调。企业管理员或者员工部署设备管理应用，激活设备管理，系统通知设备管理应用已激活admin权限。设备管理应用可在此回调函数中进行初始化策略设置。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAdminEnabled() {
  }
};
```

#### EnterpriseAdminExtensionAbility.onAdminDisabled

onAdminDisabled(): void

设备管理应用被解除激活事件回调。企业管理员或者员工解除激活设备管理，系统通知设备管理应用已解除激活admin权限。设备管理应用可在此回调函数中通知企业管理员设备已脱管。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAdminDisabled() {
  }
};
```

#### EnterpriseAdminExtensionAbility.onBundleAdded

onBundleAdded(bundleName: string): void

应用安装事件回调，回调中包含应用包名。通过接口[adminManager.subscribeManagedEventSync](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__adminmanagersubscribemanagedeventsync)注册MANAGED_EVENT_BUNDLE_ADDED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅应用安装事件，端侧应用安装事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明bundleNamestring是被安装应用的包名。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onBundleAdded(bundleName: string) {
    console.info(`Succeeded in calling onBundleAdded callback, added bundle name : ${bundleName}`);
  }
};
```

#### EnterpriseAdminExtensionAbility.onBundleAdded14+

onBundleAdded(bundleName: string, accountId: number): void

应用安装事件回调，回调中包含应用包名和账号ID。通过接口[adminManager.subscribeManagedEventSync](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__adminmanagersubscribemanagedeventsync)注册MANAGED_EVENT_BUNDLE_ADDED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅应用安装事件，端侧应用安装事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明bundleNamestring是被安装应用的包名。accountIdnumber是被安装应用所在的用户ID。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  // 由于存在同名回调方法onBundleAdded(bundleName: string)，该回调方法无accountId参数，因此在实际调用时accountId必须为可选参数，写法请参考示例代码。如果删除accountId后的问号"?"，编译会报错。
  onBundleAdded(bundleName: string, accountId?: number) {
    console.info(`Succeeded in calling onBundleAdded callback, added bundle name : ${bundleName}, accountId: ${accountId}`);
  }
};
```

#### EnterpriseAdminExtensionAbility.onBundleRemoved

onBundleRemoved(bundleName: string): void

应用卸载事件回调，回调中包含应用包名。通过接口[adminManager.subscribeManagedEventSync](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__adminmanagersubscribemanagedeventsync)注册MANAGED_EVENT_BUNDLE_REMOVED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅应用卸载事件，端侧应用卸载事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明bundleNamestring是被卸载应用的包名。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onBundleRemoved(bundleName: string) {
    console.info(`Succeeded in calling onBundleRemoved callback, removed bundle name : ${bundleName}`);
  }
};
```

#### EnterpriseAdminExtensionAbility.onBundleRemoved14+

onBundleRemoved(bundleName: string, accountId: number): void

应用卸载事件回调，回调中包含应用包名和账号ID。通过接口[adminManager.subscribeManagedEventSync](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__adminmanagersubscribemanagedeventsync)注册MANAGED_EVENT_BUNDLE_REMOVED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅应用卸载事件，端侧应用卸载事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明bundleNamestring是被卸载应用的包名。accountIdnumber是被卸载应用所在的用户ID。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  // 由于存在同名回调方法onBundleRemoved(bundleName: string)，该回调方法无accountId参数，因此在实际调用时accountId必须为可选参数，写法请参考示例代码。如果删除accountId后的问号"?"，编译会报错。
  onBundleRemoved(bundleName: string, accountId?: number) {
    console.info(`Succeeded in calling onBundleRemoved callback, removed bundle name : ${bundleName}, accountId: ${accountId}`);
  }
};
```

#### EnterpriseAdminExtensionAbility.onAppStart

onAppStart(bundleName: string): void

应用启动事件回调。通过接口[adminManager.subscribeManagedEventSync](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__adminmanagersubscribemanagedeventsync)注册MANAGED_EVENT_APP_START事件才能收到此回调。企业设备管理场景下，设备管理应用订阅应用启动事件，端侧应用启动事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明bundleNamestring是启动应用的包名。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAppStart(bundleName: string) {
    console.info(`Succeeded in calling onAppStart callback, started bundle name : ${bundleName}`);
  }
};
```

#### EnterpriseAdminExtensionAbility.onAppStop

onAppStop(bundleName: string): void

应用停止事件回调。通过接口[adminManager.subscribeManagedEventSync](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__adminmanagersubscribemanagedeventsync)注册MANAGED_EVENT_APP_STOP事件才能收到此回调。企业设备管理场景下，设备管理应用订阅应用停止事件，端侧应用停止事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明bundleNamestring是停止应用的包名。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAppStop(bundleName: string) {
    console.info(`Succeeded in calling onAppStop callback, stopped bundle name : ${bundleName}`);
  }
};
```

#### EnterpriseAdminExtensionAbility.onSystemUpdate

onSystemUpdate(systemUpdateInfo: systemManager.SystemUpdateInfo): void

系统更新事件回调。通过接口[adminManager.subscribeManagedEventSync](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__adminmanagersubscribemanagedeventsync)注册MANAGED_EVENT_SYSTEM_UPDATE事件才能收到此回调。企业设备管理场景下，设备管理应用订阅系统更新事件，端侧系统更新事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明systemUpdateInfo[systemManager.SystemUpdateInfo](@ohos.enterprise.systemManager （系统管理）.md#ZH-CN_TOPIC_0000002497605592__systemupdateinfo)是系统更新的版本信息。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';
import { systemManager } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onSystemUpdate(systemUpdateInfo: systemManager.SystemUpdateInfo) {
    console.info(`Succeeded in calling onSystemUpdate callback, version name  : ${systemUpdateInfo.versionName}`);
  }
};
```

#### EnterpriseAdminExtensionAbility.onStart

onStart(): void

EnterpriseAdminExtensionAbility启动事件回调。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onStart() {
    console.info(`Succeeded in calling onStart callback.`);
  }
};
```

#### EnterpriseAdminExtensionAbility.onAccountAdded18+

onAccountAdded(accountId: number): void

系统账号新增事件回调。通过接口[adminManager.subscribeManagedEventSync](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__adminmanagersubscribemanagedeventsync)注册MANAGED_EVENT_ACCOUNT_ADDED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅系统账号新增事件，系统账号新增事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明accountIdnumber是新增的用户ID。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAccountAdded(accountId: number) {
    console.info(`Succeeded in calling onAccountAdded callback, added accountId: ${accountId}`);
  }
};
```

#### EnterpriseAdminExtensionAbility.onAccountSwitched18+

onAccountSwitched(accountId: number): void

系统账号切换事件回调。通过接口[adminManager.subscribeManagedEventSync](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__adminmanagersubscribemanagedeventsync)注册MANAGED_EVENT_ACCOUNT_SWITCHED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅系统账号切换事件，系统账号切换事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明accountIdnumber是切换后的用户ID。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAccountSwitched(accountId: number) {
    console.info(`Succeeded in calling onAccountSwitched callback, switched accountId: ${accountId}`);
  }
};
```

#### EnterpriseAdminExtensionAbility.onAccountRemoved18+

onAccountRemoved(accountId: number): void

系统账号删除事件回调。通过接口[adminManager.subscribeManagedEventSync](@ohos.enterprise.adminManager（admin权限管理）.md#ZH-CN_TOPIC_0000002529445551__adminmanagersubscribemanagedeventsync)注册MANAGED_EVENT_ACCOUNT_REMOVED事件才能收到此回调。企业设备管理场景下，设备管理应用订阅系统账号删除事件，系统账号删除事件通知设备管理应用，设备管理应用可以在此回调函数中进行事件上报，通知企业管理员。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明accountIdnumber是被删除的用户ID。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onAccountRemoved(accountId: number) {
    console.info(`Succeeded in calling onAccountRemoved callback, removed accountId: ${accountId}`);
  }
};
```

#### EnterpriseAdminExtensionAbility.onKioskModeEntering20+

onKioskModeEntering(bundleName: string, accountId: number): void

应用进入Kiosk模式回调，回调中包含应用包名和用户ID。

Kiosk模式为系统层面提供的一种应用运行模式，该模式下会将设备锁定在单个应用或者一组应用运行，同时对锁屏状态、状态栏、手势操作和关键功能进行控制，防止用户在设备上启动其它应用或执行其它操作。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明bundleNamestring是进入Kiosk模式应用的包名。accountIdnumber是进入Kiosk模式应用所在的用户ID。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onKioskModeEntering(bundleName: string, accountId: number): void {
    console.info(`Succeeded in calling onKioskModeEntering callback, bundleName:${bundleName}, accountId:${accountId}`);
  }
};
```

#### EnterpriseAdminExtensionAbility.onKioskModeExiting20+

onKioskModeExiting(bundleName: string, accountId: number): void

应用退出Kiosk模式回调，回调中包含应用包名和用户ID。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明bundleNamestring是退出Kiosk模式应用的包名。accountIdnumber是退出Kiosk模式应用所在的用户ID。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onKioskModeExiting(bundleName: string, accountId: number): void {
    console.info(`Succeeded in calling onKioskModeExiting callback, bundleName:${bundleName}, accountId:${accountId}`);
  }
};
```

#### EnterpriseAdminExtensionAbility.onMarketAppInstallResult22+

onMarketAppInstallResult(bundleName: string, result: common.InstallationResult): void

安装应用市场应用接口[bundleManager.installMarketApps](@ohos.enterprise.bundleManager（包管理）.md#ZH-CN_TOPIC_0000002529445553__bundlemanagerinstallmarketapps22)安装结果回调，回调中包含应用包名和安装结果。

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明bundleNamestring是应用市场应用包名。result[common.InstallationResult](@ohos.enterprise.common（Enterprise公共模块）.md#ZH-CN_TOPIC_0000002497605588__installationresult)是安装结果。

**示例：**

```ets
import { EnterpriseAdminExtensionAbility, common } from '@kit.MDMKit';

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  onMarketAppInstallResult(bundleName: string, result: common.InstallationResult): void {
    console.info(`Succeeded in calling onMarketAppInstallResult callback, bundleName:${bundleName}, result:${result}`);
  }
};
```