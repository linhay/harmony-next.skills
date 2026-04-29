# AbilityInfo

Ability信息，未做特殊说明的属性，均通过[bundle.getAbilityInfo](@ohos.bundle (Bundle模块).md#ZH-CN_TOPIC_0000002522080594__bundlegetabilityinfodeprecated)获取。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[bundleManager-AbilityInfo](AbilityInfo.md)替代。

**AbilityInfo(deprecated)**

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-AbilityInfo](AbilityInfo.md#ZH-CN_TOPIC_0000002553200545__abilityinfo-1)替代。

系统能力： SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 是 | 否 | 应用Bundle名称。 |
| name | string | 是 | 否 | Ability名称。 |
| label | string | 是 | 否 | Ability对用户显示的名称。 |
| description | string | 是 | 否 | Ability的描述。 |
| icon | string | 是 | 否 | Ability的图标资源文件索引。 |
| descriptionId | number | 是 | 否 | Ability的描述的资源id值。 |
| iconId | number | 是 | 否 | Ability的图标的资源id值。 |
| moduleName | string | 是 | 否 | Ability所属的HAP的名称。 |
| process | string | 是 | 否 | Ability的进程名称。 |
| targetAbility | string | 是 | 否 | 当前Ability重用的目标Ability。 模型约束： 此接口仅可在FA模型下使用。 |
| backgroundModes | number | 是 | 否 | 表示后台服务的类型。 模型约束： 此接口仅可在FA模型下使用。 |
| isVisible | boolean | 是 | 否 | 判断Ability是否可以被其他应用调用，取值为true表示Ability可以被其他应用调用，取值为false表示Ability不可以被其他应用调用。 |
| formEnabled | boolean | 是 | 否 | 判断Ability是否提供卡片能力，取值为true表示Ability提供卡片能力，取值为false表示Ability不提供卡片能力。 模型约束： 此接口仅可在FA模型下使用。 |
| type | bundle.AbilityType | 是 | 否 | Ability类型。 模型约束： 此接口仅可在FA模型下使用。 |
| orientation | bundle.DisplayOrientation | 是 | 否 | Ability的显示模式。 |
| launchMode | bundle.LaunchMode | 是 | 否 | Ability的启动模式。 |
| permissions | Array<string> | 是 | 否 | 被其他应用Ability调用时需要申请的权限集合。 通过调用bundle.getAbilityInfo接口时，传入GET_ABILITY_INFO_WITH_PERMISSION获取。 |
| deviceTypes | Array<string> | 是 | 否 | Ability支持的设备类型。 |
| deviceCapabilities | Array<string> | 是 | 否 | Ability需要的设备能力。 |
| readPermission | string | 是 | 否 | 读取Ability数据所需的权限。 模型约束： 此接口仅可在FA模型下使用。 |
| writePermission | string | 是 | 否 | 向Ability写数据所需的权限。 模型约束： 此接口仅可在FA模型下使用。 |
| applicationInfo | ApplicationInfo | 是 | 否 | 应用程序的配置信息。 通过调用bundle.getAbilityInfo接口时，传入GET_ABILITY_INFO_WITH_APPLICATION获取。 |
| uri | string | 是 | 否 | 获取Ability的统一资源标识符（URI）。 模型约束： 此接口仅可在FA模型下使用。 |
| labelId | number | 是 | 否 | Ability的标签的资源id值。 |
| subType | bundle.AbilitySubType | 是 | 否 | Ability中枚举使用的模板的子类型。 模型约束： 此接口仅可在FA模型下使用。 |
| metaData8+ | Array<CustomizeData> | 是 | 否 | ability的元信息。 通过调用bundle.getAbilityInfo接口时，传入GET_ABILITY_INFO_WITH_METADATA获取。 |
| enabled8+ | boolean | 是 | 否 | ability是否可用，取值为true表示Ability可用，取值为false表示Ability不可用。 |