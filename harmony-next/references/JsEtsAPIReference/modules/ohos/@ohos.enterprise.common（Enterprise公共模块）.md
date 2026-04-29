# @ohos.enterprise.common（Enterprise公共模块）

本模块提供MDM Kit中常用公共能力的纯类型定义，包含枚举类型和数据结构。本模块仅导出类型声明，不包含具体实现逻辑或可执行代码。

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { common } from '@kit.MDMKit';
```

#### ManagedPolicy

企业设备管控策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认，无管控策略。 |
| DISALLOW | 1 | 禁用。 |
| FORCE_OPEN | 2 | 强制开启。 |

#### ApplicationInstance

应用的实例数据。

该接口目前在[addUserNonStopApps](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002522081688__applicationmanageraddusernonstopapps22)、[removeUserNonStopApps](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002522081688__applicationmanagerremoveusernonstopapps22)、[addFreezeExemptedApps](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002522081688__applicationmanageraddfreezeexemptedapps22)、[removeFreezeExemptedApps](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002522081688__applicationmanagerremovefreezeexemptedapps22)接口中作为入参使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appIdentifier | string | 否 | 否 | 应用[唯一标识符](../../topics/misc/BundleInfo.md#ZH-CN_TOPIC_0000002529284625__signatureinfo)，可以通过接口bundleManager.getBundleInfo获取bundleInfo.signatureInfo.appIdentifier。 |
| accountId | number | 否 | 否 | 用户ID。取值范围：大于等于0的整数。  accountId可以通过getOsAccountLocalId接口获取。 |
| appIndex | number | 否 | 否 | 应用分身索引。取值范围：大于等于0的整数。  appIndex可以通过getAppCloneIdentity接口获取。 |

#### InstallationResult

应用安装结果。

该对象目前在[EnterpriseAdminExtensionAbility.onMarketAppInstallResult](@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）.md#ZH-CN_TOPIC_0000002553201659__onmarketappinstallresult22)作为回调入参使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | Result | 否 | 否 | 应用安装结果码。 |
| message | string | 否 | 否 | 应用安装结果消息。 |

#### Result

应用安装结果码。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 应用安装成功。 |
| FAIL | -1 | 应用安装失败。 |

**EnterpriseAdminExtensionContext23+**

type EnterpriseAdminExtensionContext = _EnterpriseAdminExtensionContext.default

EnterpriseAdminExtensionContext是[EnterpriseAdminExtensionAbility](@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）.md)的上下文环境，继承自[ExtensionContext](ExtensionContext.md)。

系统能力: SystemCapability.Customization.EnterpriseDeviceManager

模型约束：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| _EnterpriseAdminExtensionContext.default | EnterpriseAdminExtensionAbility组件的上下文。 |