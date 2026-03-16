[]()[]()

# BundleInfo

应用包的信息，通过[bundle.getBundleInfo](../../modules/ohos/@ohos.bundle (Bundle模块).md#ZH-CN_TOPIC_0000002529284637__bundlegetbundleinfodeprecated)获取。

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 9开始，该模块不再维护，建议使用[bundleManager-BundleInfo](BundleInfo (js-apis-bundlemanager-bundleinfo).md)替代。

[]()[]()

#### BundleInfo(deprecated)

从API version 9开始不再维护，建议使用[bundleManager-BundleInfo](BundleInfo (js-apis-bundlemanager-bundleinfo).md#ZH-CN_TOPIC_0000002529284625__bundleinfo-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称类型只读可选说明namestring是否应用包的名称。typestring是否应用包类型。appIdstring是否应用包里应用程序的id。uidnumber是否应用包里应用程序的uid。installTimenumber是否HAP安装时间。updateTimenumber是否HAP更新时间。appInfo[ApplicationInfo](../system-services/ApplicationInfo (js-apis-bundle-applicationinfo).md)是否应用程序的配置信息。abilityInfosArray<[AbilityInfo](../system-services/AbilityInfo (js-apis-bundle-abilityinfo).md)>是否

Ability的配置信息

通过调用[bundle.getBundleInfo](../../modules/ohos/@ohos.bundle (Bundle模块).md#ZH-CN_TOPIC_0000002529284637__bundlegetbundleinfodeprecated)接口时，传入GET_BUNDLE_WITH_ABILITIES获取。

reqPermissionsArray<string>是否

应用运行时需向系统申请的权限集合

通过调用[bundle.getBundleInfo](../../modules/ohos/@ohos.bundle (Bundle模块).md#ZH-CN_TOPIC_0000002529284637__bundlegetbundleinfodeprecated)接口时，传入GET_BUNDLE_WITH_REQUESTED_PERMISSION获取。

reqPermissionDetailsArray<[ReqPermissionDetail](#ZH-CN_TOPIC_0000002497604650__reqpermissiondetaildeprecated)>是否

应用运行时需向系统申请的权限集合的详细信息

通过调用[bundle.getBundleInfo](../../modules/ohos/@ohos.bundle (Bundle模块).md#ZH-CN_TOPIC_0000002529284637__bundlegetbundleinfodeprecated)接口时，传入GET_BUNDLE_WITH_REQUESTED_PERMISSION获取。

vendorstring是否应用包的供应商。versionCodenumber是否应用包的版本号。versionNamestring是否应用包的版本文本描述信息。compatibleVersionnumber是否运行应用包所需要最低的SDK版本号。targetVersionnumber是否运行应用包所需要最高SDK版本号。isCompressNativeLibsboolean是否是否压缩应用包的本地库，取值为true表示压缩应用包的本地库，取值为false表示不压缩应用包的本地库。hapModuleInfosArray<[HapModuleInfo](../system-services/HapModuleInfo (js-apis-bundle-hapmoduleinfo).md)>是否模块的配置信息。entryModuleNamestring是否Entry的模块名称。cpuAbistring是否应用包的cpuAbi信息。isSilentInstallationstring是否是否通过静默安装。minCompatibleVersionCodenumber是否分布式场景下的应用包兼容的最低版本。entryInstallationFreeboolean是否Entry是否支持免安装，取值为true表示支持免安装，取值为false表示不支持免安装。reqPermissionStates8+Array<number>是否申请权限的授予状态。0表示申请成功，-1表示申请失败。[]()[]()

#### ReqPermissionDetail(deprecated)

从API version 9开始不再维护，建议使用[ReqPermissionDetail](BundleInfo (js-apis-bundlemanager-bundleinfo).md)替代。

应用运行时需向系统申请的权限集合的详细信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称类型只读可选说明namestring否否需要使用的权限名称。reasonstring否否描述申请权限的原因。usedScene[UsedScene](#ZH-CN_TOPIC_0000002497604650__usedscenedeprecated)否否权限使用的场景和时机。[]()[]()

#### UsedScene(deprecated)

从API version 9开始不再维护，建议使用[UsedScene](BundleInfo (js-apis-bundlemanager-bundleinfo).md#ZH-CN_TOPIC_0000002529284625__usedscene)替代。

描述权限使用的场景和时机。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称类型只读可选说明abilitiesArray<string>否否使用到该权限的Ability集合。whenstring否否使用该权限的时机。