[]()[]()

# HapModuleInfo

Hap模块信息，未做特殊说明的属性，均通过[bundle.getBundleInfo](../../modules/ohos/@ohos.bundle (Bundle模块).md#ZH-CN_TOPIC_0000002529284637__bundlegetbundleinfodeprecated)获取。

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 9开始，该模块不再维护，建议使用[bundleManager-HapModuleInfo](HapModuleInfo (js-apis-bundlemanager-hapmoduleinfo).md)替代。

[]()[]()

#### HapModuleInfo(deprecated)

从API version 9开始不再维护，建议使用[bundleManager-HapModuleInfo](HapModuleInfo (js-apis-bundlemanager-hapmoduleinfo).md#ZH-CN_TOPIC_0000002497444656__hapmoduleinfo-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称类型只读可选说明namestring是否模块名称。descriptionstring是否模块描述信息。descriptionIdnumber是否描述信息ID。iconstring是否模块图标。labelstring是否模块标签。labelIdnumber是否模块标签ID。iconIdnumber是否模块图标ID。backgroundImgstring是否模块背景图片。supportedModesnumber是否模块支持的模式。reqCapabilitiesArray<string>是否模块运行需要的能力。deviceTypesArray<string>是否支持运行的设备类型。abilityInfoArray<[AbilityInfo](AbilityInfo (js-apis-bundle-abilityinfo).md)>是否Ability信息。moduleNamestring是否模块名。mainAbilityNamestring是否入口Ability名称。installationFreeboolean是否是否支持免安装，取值为true表示支持免安装，取值为false表示不支持免安装。