# Metadata

元数据对象，可以通过[bundleManager.getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)获取，其中参数bundleFlags至少包含GET_BUNDLE_INFO_WITH_METADATA。此对象在[ApplicationInfo](../system-services/ApplicationInfo.md)、[HapModuleInfo](../system-services/HapModuleInfo.md)、[AbilityInfo](../system-services/AbilityInfo.md)、[ExtensionAbilityInfo](../system-services/ExtensionAbilityInfo.md)中均包含。

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

描述的module、uiAbility、extensionAbility配置信息，标签值为数组类型，该标签下的配置只对当前module、uiAbility或者extensionAbility生效。

#### 导入模块

```ets
import { bundleManager } from '@kit.AbilityKit';
```

#### Metadata

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**: SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明namestring否否元数据名称。valuestring否否元数据值。resourcestring否否元数据资源描述符，参考示例$profile:config_file，表示profile目录下配置了config_file.json文件。valueId18+number是是元数据值id。当valueId不为0时，表示当前元数据值为自定义配置，需要使用valueId去资源管理获取对应的值。 当valueId为0时，表示当前元数据值为固定字符串。