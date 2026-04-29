# ExtensionAbilityInfo

ExtensionAbility信息，可以通过[bundleManager.getBundleInfoForSelf](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002522080562__bundlemanagergetbundleinfoforself)获取自身的ExtensionAbility信息，其中参数[bundleFlags](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002522080562__bundleflag)至少包含GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**导入模块**

```ets
import { bundleManager } from '@kit.AbilityKit';
```

**ExtensionAbilityInfo**

系统能力: SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 是 | 否 | 应用Bundle名称。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| moduleName | string | 是 | 否 | ExtensionAbility所属的HAP的名称。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| name | string | 是 | 否 | ExtensionAbility名称。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| labelId | number | 是 | 否 | ExtensionAbility的标签资源ID。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| descriptionId | number | 是 | 否 | ExtensionAbility的描述资源ID。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| iconId | number | 是 | 否 | ExtensionAbility的图标资源ID。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| exported | boolean | 是 | 否 | 判断ExtensionAbility是否可以被其他应用调用，取值为true表示ExtensionAbility可以被其他应用调用，取值为false表示ExtensionAbility不可以被其他应用调用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| extensionAbilityType | bundleManager.ExtensionAbilityType | 是 | 否 | ExtensionAbility类型。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| permissions | Array<string> | 是 | 否 | 被其他应用ExtensionAbility调用时需要申请的权限集合。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| applicationInfo | ApplicationInfo | 是 | 否 | 应用程序的配置信息。 getBundleInfoForSelf或者getBundleInfo接口获取ExtensionAbilityInfo信息时不会返回该字段内容，可以通过获取bundleInfo.appInfo对象来获取相关信息。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| metadata | Array<Metadata> | 是 | 否 | ExtensionAbility的元信息。通过调用getBundleInfoForSelf接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY和GET_BUNDLE_INFO_WITH_METADATA获取。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| enabled | boolean | 是 | 否 | ExtensionAbility是否可用，取值为true表示ExtensionAbility可用，取值为false表示ExtensionAbility不可用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| readPermission | string | 是 | 否 | 读取ExtensionAbility数据所需的权限。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| writePermission | string | 是 | 否 | 向ExtensionAbility写数据所需的权限。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| extensionAbilityTypeName11+ | string | 是 | 否 | ExtensionAbility的类型名称，取值请参考extensionabilities标签下的type字段。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| skills12+ | Array<Skill> | 是 | 否 | ExtensionAbility的Skills信息。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| appIndex12+ | number | 是 | 否 | 应用包的分身索引标识，仅在分身应用中生效。 |