[]()[]()

# BundleInfo

应用包信息，可以通过[bundleManager.getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)获取自身的应用包信息，其中参数[bundleFlags](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundleflag)指定所返回的[BundleInfo](BundleInfo (js-apis-bundlemanager-bundleinfo).md)中所包含的信息。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### 导入模块

```ets
import { bundleManager } from '@kit.AbilityKit';
```

[]()[]()

#### BundleInfo

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明namestring是否

应用包的名称，对应[app.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file)中配置的bundleName字段。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

vendorstring是否

应用包的供应商，对应[app.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file)中配置的vendor字段。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

versionCodenumber是否

应用包的版本号，对应[app.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file)中配置的versionCode字段。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

versionNamestring是否

应用包的版本文本描述信息，对应[app.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file)中配置的versionName字段。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

minCompatibleVersionCodenumber是否

分布式场景下的应用包兼容的最低版本，对应[app.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file)中配置的minCompatibleVersionCode字段。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

targetVersionnumber是否

应用运行目标版本，对应[app.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file)中配置的targetAPIVersion字段。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

appInfo[ApplicationInfo](../system-services/ApplicationInfo (js-apis-bundlemanager-applicationinfo).md)是否

应用程序的配置信息，通过调用[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_APPLICATION获取。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

hapModulesInfoArray<[HapModuleInfo](../system-services/HapModuleInfo (js-apis-bundlemanager-hapmoduleinfo).md)>是否

模块的配置信息，通过调用[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE获取。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

reqPermissionDetailsArray<[ReqPermissionDetail](#ZH-CN_TOPIC_0000002529284625__reqpermissiondetail)>是否

应用运行时需向系统申请的权限集合的详细信息，通过调用[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION获取。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

permissionGrantStatesArray<[bundleManager.PermissionGrantState](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__permissiongrantstate)>是否

申请权限的授予状态，通过调用[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION获取。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

signatureInfo[SignatureInfo](#ZH-CN_TOPIC_0000002529284625__signatureinfo)是否

应用包的签名信息，通过调用[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_SIGNATURE_INFO获取。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

installTimenumber是否

应用包安装时间戳，表示从1970-01-01 08:00:00 UTC+8逝去的毫秒数，单位毫秒。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**说明：**

设备出厂首次开机时，如果未获取到当前时间，会以Unix时间戳基准（1970-01-01 08:00:00 UTC+8）作为当前系统的起始时间。例如，开机后未获取到时间，等待32s之后安装成功，则应用包安装时间戳为32000。

updateTimenumber是否

应用包更新时间戳，表示从1970-01-01 08:00:00 UTC+8逝去的毫秒数，单位毫秒。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

routerMap12+Array<[RouterItem](../system-services/HapModuleInfo (js-apis-bundlemanager-hapmoduleinfo).md#ZH-CN_TOPIC_0000002497444656__routeritem12)>是否

应用的路由表配置，由hapModulesInfo下的routerMap信息，根据RouterItem中的name字段进行去重后合并得到。通过调用[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_ROUTER_MAP获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

appIndex12+number是否应用包的分身索引标识，仅在分身应用中生效。firstInstallTime18+number是是

应用在当前设备的首次安装时间戳，表示从1970-01-01 08:00:00 UTC+8逝去的毫秒数，单位毫秒，预置应用的首次安装时间戳为1533657660000。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

[]()[]()

#### ReqPermissionDetail

应用运行时需向系统申请的权限集合的详细信息。

- 如果应用内多包申请的权限名称一样，但是权限申请理由不一致，系统只会返回一个权限申请理由，优先级从高到低顺序为entry类型HAP、feature类型HAP、应用内HSP。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明namestring否否需要使用的[权限名称](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)。moduleName10+string否否申请该权限的module名称。reasonstring否否描述申请权限的原因。reasonIdnumber否否描述申请权限的原因ID。usedScene[UsedScene](#ZH-CN_TOPIC_0000002529284625__usedscene)否否权限使用的场景和时机。[]()[]()

#### UsedScene

描述权限使用的场景和时机。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明abilitiesArray<string>否否使用到该权限的Ability集合。whenstring否否使用该权限的时机。支持的取值有inuse（使用时）、always（始终）。[]()[]()

#### SignatureInfo

描述应用包的签名信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明appIdstring是否

应用的appId，表示应用的唯一标识，详情信息可参考[什么是appId](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/common_problem_of_application#什么是appid)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

fingerprintstring是否

应用包的指纹信息，由签名证书通过SHA-256算法计算哈希值生成。使用的签名证书发生变化时，该字段也会发生变化。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

appIdentifier11+string是否

应用的唯一标识。详情信息可参考[什么是appIdentifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/common_problem_of_application#什么是appidentifier)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

certificate14+string是是

应用的证书公钥。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

[]()[]()

#### AppCloneIdentity14+

描述应用包的身份信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明bundleNamestring是否应用的bundleName。appIndexnumber是否应用包的分身索引信息。