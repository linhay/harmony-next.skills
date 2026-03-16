# ModuleInfo

应用程序的模块信息。

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 9开始，该模块不再维护，建议使用[bundleManager-HapModuleInfo](HapModuleInfo.md)替代。

#### ModuleInfo(deprecated)

从API version 9开始不再维护，建议使用[bundleManager-HapModuleInfo](HapModuleInfo.md#ZH-CN_TOPIC_0000002497444656__hapmoduleinfo-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称类型只读可选说明moduleNamestring是否模块名称。moduleSourceDirstring是否安装目录。不能拼接路径访问资源文件，请使用[资源管理接口](../../modules/ohos/@ohos.resourceManager (资源管理).md)访问资源。