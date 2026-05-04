# ShortcutInfo

应用配置文件中定义的快捷方式信息，[FA模型](../../guides/Ability Kit术语.md#fa模型)配置在[config.json](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-configuration-file-overview-fa)文件中进行配置，[Stage模型](../../guides/Ability Kit术语.md#stage模型)配置在开发视图的resources/base/profile下面定义配置文件即可。

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护。建议使用[bundleManager-ShortcutInfo](ShortcutInfo.md)替代。

#### ShortcutInfo(deprecated)


从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-ShortcutInfo](ShortcutInfo.md#ZH-CN_TOPIC_0000002553360509__shortcutinfo-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 是 | 否 | 快捷方式所属应用程序的Id。 |
| bundleName | string | 是 | 否 | 包含该快捷方式的Bundle名称。 |
| hostAbility | string | 是 | 否 | 快捷方式的本地Ability信息。 |
| icon | string | 是 | 否 | 快捷方式的图标。 |
| iconId8+ | number | 是 | 否 | 快捷方式的图标Id。 |
| label | string | 是 | 否 | 快捷方式的名称。 |
| labelId8+ | number | 是 | 否 | 快捷方式的名称Id。 |
| disableMessage | string | 是 | 否 | 快捷方式的禁用消息。 |
| wants | Array<ShortcutWant> | 是 | 否 | 快捷方式意图列表。 |
| isStatic | boolean | 是 | 是 | 快捷方式是否为静态，取值为true表示是静态的快捷方式，取值为false表示不是静态的快捷方式。 |
| isHomeShortcut | boolean | 是 | 是 | 快捷方式是否为主页面快捷方式，取值为true表示是主页面快捷方式，取值为false表示不是主页面快捷方式。 |
| isEnabled | boolean | 是 | 是 | 是否启用快捷方式，取值为true表示启用快捷方式，取值为false表示停用快捷方式。 |