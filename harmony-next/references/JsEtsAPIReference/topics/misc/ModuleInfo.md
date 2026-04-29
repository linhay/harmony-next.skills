# ModuleInfo

应用程序的模块信息。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[bundleManager-HapModuleInfo](HapModuleInfo.md)替代。

**ModuleInfo(deprecated)**

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-HapModuleInfo](HapModuleInfo.md#ZH-CN_TOPIC_0000002522080584__hapmoduleinfo-1)替代。

系统能力： SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moduleName | string | 是 | 否 | 模块名称。 |
| moduleSourceDir | string | 是 | 否 | 安装目录。不能拼接路径访问资源文件，请使用资源管理接口访问资源。 |