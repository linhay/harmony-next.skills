# ExtensionAbilityInfo

ExtensionAbility信息，可以通过[bundleManager.getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)获取自身的ExtensionAbility信息，其中参数[bundleFlags](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundleflag)至少包含GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY。

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { bundleManager } from '@kit.AbilityKit';
```

#### ExtensionAbilityInfo

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**: SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明bundleNamestring是否应用Bundle名称。moduleNamestring是否ExtensionAbility所属的HAP的名称。namestring是否ExtensionAbility名称。labelIdnumber是否ExtensionAbility的标签资源ID。descriptionIdnumber是否ExtensionAbility的描述资源ID。iconIdnumber是否ExtensionAbility的图标资源ID。exportedboolean是否判断ExtensionAbility是否可以被其他应用调用，取值为true表示ExtensionAbility可以被其他应用调用，取值为false表示ExtensionAbility不可以被其他应用调用。extensionAbilityType[ExtensionAbilityType](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__extensionabilitytype)是否ExtensionAbility类型。permissionsArray<string>是否被其他应用ExtensionAbility调用时需要申请的权限集合。applicationInfo[ApplicationInfo](ApplicationInfo.md)是否应用程序的配置信息。通过调用[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY和GET_BUNDLE_INFO_WITH_APPLICATION获取。metadataArray<[Metadata](../misc/Metadata.md)>是否ExtensionAbility的元信息。通过调用[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY和GET_BUNDLE_INFO_WITH_METADATA获取。enabledboolean是否ExtensionAbility是否可用，取值为true表示ExtensionAbility可用，取值为false表示ExtensionAbility不可用。readPermissionstring是否读取ExtensionAbility数据所需的权限。writePermissionstring是否向ExtensionAbility写数据所需的权限。extensionAbilityTypeName11+string是否ExtensionAbility的类型名称，取值请参考[extensionabilities标签下的type字段](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#extensionabilities标签)。skills12+Array<[Skill](../misc/Skill.md)>是否ExtensionAbility的Skills信息。appIndex12+number是否应用包的分身索引标识，仅在分身应用中生效。