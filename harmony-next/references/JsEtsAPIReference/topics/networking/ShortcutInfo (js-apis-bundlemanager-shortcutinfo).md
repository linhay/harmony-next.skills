[]()[]()

# ShortcutInfo

应用[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#shortcuts标签)中定义的快捷方式信息，可以通过[getAllShortcutInfoForSelf接口](../../modules/ohos/@ohos.bundle.shortcutManager (shortcutManager模块).md#ZH-CN_TOPIC_0000002497444636__shortcutmanagergetallshortcutinfoforself)获取。

本模块首批接口从API version 20 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### 导入模块

```ets
import { shortcutManager } from '@kit.AbilityKit';
```

[]()[]()

#### ShortcutWant

快捷方式内定义的目标[wants](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#wants标签)信息集合。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

名称类型只读可选说明targetBundlestring否否快捷方式的目标包名。targetModulestring否是快捷方式的目标模块名。targetAbilitystring否否快捷方式的目标组件名。parametersArray<[ParameterItem](#ZH-CN_TOPIC_0000002529284629__parameteritem)>否是拉起快捷方式时的自定义数据，仅支持配置字符串类型的数据。其中键值均最大支持1024长度的字符串。[]()[]()

#### ShortcutInfo

快捷方式的配置信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

名称类型只读可选说明idstring否否快捷方式的ID。bundleNamestring否否快捷方式所属应用的包名。moduleNamestring否是快捷方式的模块名。hostAbilitystring否是快捷方式的宿主组件名, 即承载此快捷方式的组件名。iconstring否是快捷方式的图标，取值为资源文件的索引。iconIdnumber否是快捷方式图标的资源ID。labelstring否是快捷方式的标签信息，即快捷方式对外显示的文字描述信息。可以是描述性内容，也可以是标识label的资源索引。labelIdnumber否是快捷方式标签信息为资源索引时的资源ID。wantsArray<[ShortcutWant](#ZH-CN_TOPIC_0000002529284629__shortcutwant)>否是快捷方式内定义的目标wants信息集合。appIndexnumber否否快捷方式所属应用的分身索引。sourceTypenumber否否快捷方式来源类型，0：自定义快捷方式；1：静态快捷方式。visibleboolean否是快捷方式是否显示。true：快捷方式显示；false：快捷方式不显示。默认值为true。[]()[]()

#### ParameterItem

快捷方式配置信息中的自定义数据。由开发者自行决定传入的键值对，可以通过key值获取对应的value值。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

名称类型只读可选说明keystring否否快捷方式配置信息中的自定义数据的键。valuestring否否快捷方式配置信息中的自定义数据的值。