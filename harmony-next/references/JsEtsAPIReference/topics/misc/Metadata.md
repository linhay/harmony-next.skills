# Metadata

元数据对象，可以通过[bundleManager.getBundleInfoForSelf](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002522080562__bundlemanagergetbundleinfoforself)获取，其中参数bundleFlags至少包含GET_BUNDLE_INFO_WITH_METADATA。此对象在[ApplicationInfo](ApplicationInfo.md)、[HapModuleInfo](HapModuleInfo.md)、[AbilityInfo](AbilityInfo.md)、[ExtensionAbilityInfo](ExtensionAbilityInfo.md)中均包含。


本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

描述的module、uiAbility、extensionAbility配置信息，标签值为数组类型，该标签下的配置只对当前module、uiAbility或者extensionAbility生效。

#### 导入模块

```ets
import { bundleManager } from '@kit.AbilityKit';
```

#### Metadata

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**: SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 元数据名称。 |
| value | string | 否 | 否 | 元数据值。 |
| resource | string | 否 | 否 | 元数据资源描述符，参考示例$profile:config_file，表示profile目录下配置了config_file.json文件。 |
| valueId18+ | number | 是 | 是 | 元数据值id。当valueId不为0时，表示当前元数据值为自定义配置，需要使用valueId去资源管理获取对应的值。 当valueId为0时，表示当前元数据值为固定字符串。 |