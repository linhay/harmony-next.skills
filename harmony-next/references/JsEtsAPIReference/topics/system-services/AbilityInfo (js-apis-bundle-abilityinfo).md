[]()[]()

# AbilityInfo

Ability信息，未做特殊说明的属性，均通过[bundle.getAbilityInfo](../../modules/ohos/@ohos.bundle (Bundle模块).md#ZH-CN_TOPIC_0000002529284637__bundlegetabilityinfodeprecated)获取。

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 9开始，该模块不再维护，建议使用[bundleManager-AbilityInfo](AbilityInfo (js-apis-bundlemanager-abilityinfo).md)替代。

[]()[]()

#### AbilityInfo(deprecated)

从API version 9开始不再维护，建议使用[bundleManager-AbilityInfo](AbilityInfo (js-apis-bundlemanager-abilityinfo).md#ZH-CN_TOPIC_0000002497604632__abilityinfo-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称类型只读可选说明bundleNamestring是否应用Bundle名称。namestring是否Ability名称。labelstring是否Ability对用户显示的名称。descriptionstring是否Ability的描述。iconstring是否Ability的图标资源文件索引。descriptionIdnumber是否Ability的描述的资源id值。iconIdnumber是否Ability的图标的资源id值。moduleNamestring是否Ability所属的HAP的名称。processstring是否Ability的进程名称。targetAbilitystring是否

当前Ability重用的目标Ability。

**模型约束：** 此接口仅可在FA模型下使用。

backgroundModesnumber是否

表示后台服务的类型。

**模型约束：** 此接口仅可在FA模型下使用。

isVisibleboolean是否判断Ability是否可以被其他应用调用，取值为true表示Ability可以被其他应用调用，取值为false表示Ability不可以被其他应用调用。formEnabledboolean是否

判断Ability是否提供卡片能力，取值为true表示Ability提供卡片能力，取值为false表示Ability不提供卡片能力。

**模型约束：** 此接口仅可在FA模型下使用。

typebundle.AbilityType是否

Ability类型。

**模型约束：** 此接口仅可在FA模型下使用。

orientation[bundle.DisplayOrientation](../../modules/ohos/@ohos.bundle (Bundle模块).md#ZH-CN_TOPIC_0000002529284637__displayorientationdeprecated)是否Ability的显示模式。launchMode[bundle.LaunchMode](../../modules/ohos/@ohos.bundle (Bundle模块).md#ZH-CN_TOPIC_0000002529284637__launchmodedeprecated)是否Ability的启动模式。permissionsArray<string>是否

被其他应用Ability调用时需要申请的权限集合。

通过调用[bundle.getAbilityInfo](../../modules/ohos/@ohos.bundle (Bundle模块).md#ZH-CN_TOPIC_0000002529284637__bundlegetabilityinfodeprecated)接口时，传入GET_ABILITY_INFO_WITH_PERMISSION获取。

deviceTypesArray<string>是否Ability支持的设备类型。deviceCapabilitiesArray<string>是否Ability需要的设备能力。readPermissionstring是否

读取Ability数据所需的权限。

**模型约束：** 此接口仅可在FA模型下使用。

writePermissionstring是否

向Ability写数据所需的权限。

**模型约束：** 此接口仅可在FA模型下使用。

applicationInfo[ApplicationInfo](ApplicationInfo (js-apis-bundle-applicationinfo).md)是否

应用程序的配置信息。

通过调用[bundle.getAbilityInfo](../../modules/ohos/@ohos.bundle (Bundle模块).md#ZH-CN_TOPIC_0000002529284637__bundlegetabilityinfodeprecated)接口时，传入GET_ABILITY_INFO_WITH_APPLICATION获取。

uristring是否

获取Ability的统一资源标识符（URI）。

**模型约束：** 此接口仅可在FA模型下使用。

labelIdnumber是否Ability的标签的资源id值。subTypebundle.AbilitySubType是否

Ability中枚举使用的模板的子类型。

**模型约束：** 此接口仅可在FA模型下使用。

metaData8+Array<[CustomizeData](../misc/CustomizeData.md)>是否

ability的元信息。

通过调用[bundle.getAbilityInfo](../../modules/ohos/@ohos.bundle (Bundle模块).md#ZH-CN_TOPIC_0000002529284637__bundlegetabilityinfodeprecated)接口时，传入GET_ABILITY_INFO_WITH_METADATA获取。

enabled8+boolean是否ability是否可用，取值为true表示Ability可用，取值为false表示Ability不可用。