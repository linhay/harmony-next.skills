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

名称值说明DEFAULT0默认，无管控策略。DISALLOW1禁用。FORCE_OPEN2强制开启。

#### ApplicationInstance

应用的实例数据。

该接口目前在[addUserNonStopApps](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002497605586__applicationmanageraddusernonstopapps22)、[removeUserNonStopApps](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002497605586__applicationmanagerremoveusernonstopapps22)、[addFreezeExemptedApps](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002497605586__applicationmanageraddfreezeexemptedapps22)、[removeFreezeExemptedApps](@ohos.enterprise.applicationManager（应用管理）.md#ZH-CN_TOPIC_0000002497605586__applicationmanagerremovefreezeexemptedapps22)接口中作为入参使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明appIdentifierstring否否应用[唯一标识符](../../topics/misc/BundleInfo.md#ZH-CN_TOPIC_0000002529284625__signatureinfo)，可以通过接口[bundleManager.getBundleInfo](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfo14-2)获取bundleInfo.signatureInfo.appIdentifier。accountIdnumber否否

用户ID。取值范围：大于等于0的整数。

 accountId可以通过[getOsAccountLocalId](@ohos.account.osAccount (系统账号管理).md#ZH-CN_TOPIC_0000002529285493__getosaccountlocalid9-1)接口获取。

appIndexnumber否否

应用分身索引。取值范围：大于等于0的整数。

 appIndex可以通过[getAppCloneIdentity](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetappcloneidentity14)接口获取。

#### InstallationResult

应用安装结果。

该对象目前在[EnterpriseAdminExtensionAbility.onMarketAppInstallResult](@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）.md#ZH-CN_TOPIC_0000002529445559__enterpriseadminextensionabilityonmarketappinstallresult22)作为回调入参使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称类型只读可选说明result[Result](#ZH-CN_TOPIC_0000002497605588__result)否否应用安装结果码。messagestring否否应用安装结果消息。

#### Result

应用安装结果码。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

名称值说明SUCCESS0应用安装成功。FAIL-1应用安装失败。