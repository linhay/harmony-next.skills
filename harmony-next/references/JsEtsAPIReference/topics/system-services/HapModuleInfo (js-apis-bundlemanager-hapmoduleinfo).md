[]()[]()

# HapModuleInfo

HAP信息，可以通过[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)获取自身的HAP信息，其中参数[bundleFlags](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundleflag)至少包含GET_BUNDLE_INFO_WITH_HAP_MODULE。

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### 导入模块

```ets
import { bundleManager } from '@kit.AbilityKit';
```

[]()[]()

#### HapModuleInfo

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明namestring是否

模块名称。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

iconstring是否

当前模块入口Ability的[图标](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/layered-image)，取值为图标资源文件的索引，与模块配置文件中[abilities标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#abilities标签)或[extensionAbilities标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#extensionabilities标签)的icon字段值一致。若未配置入口Ability，则为空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

iconIdnumber是否

当前模块入口Ability的图标[资源id](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access#资源目录)值。若未配置入口Ability，则为空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

labelstring是否

当前模块入口Ability的名称，取值为字符串资源的索引，与模块配置文件中[abilities标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#abilities标签)或[extensionAbilities标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#extensionabilities标签)的label字段值一致。若未配置入口Ability，则为空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

labelIdnumber是否

当前模块入口Ability名称的[资源id](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access#资源目录)值。若未配置入口Ability，则为空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

descriptionstring是否

模块描述信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

descriptionIdnumber是否

描述信息的资源id值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

mainElementNamestring是否

当前模块的入口UIAbility名称或者ExtensionAbility名称。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

abilitiesInfoArray<[AbilityInfo](AbilityInfo (js-apis-bundlemanager-abilityinfo).md)>是否

当前模块所有Ability的信息。通过调用[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_ABILITY获取。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

extensionAbilitiesInfoArray<[ExtensionAbilityInfo](ExtensionAbilityInfo.md)>是否

当前模块所有ExtensionAbility的信息。通过调用[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY获取。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

metadataArray<[Metadata](../misc/Metadata.md)>是否

当前模块的元数据。通过调用[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_METADATA获取。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

deviceTypesArray<string>是否

模块支持安装运行的[设备类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#devicetypes标签)的集合。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

installationFreeboolean是否

模块是否支免安装（无需用户通过应用市场显式安装），取值为true表示支持免安装，取值为false表示不支持免安装。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

hashValuestring是否

模块的Hash值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

type[bundleManager.ModuleType](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__moduletype)是否

标识当前模块的类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

preloadsArray<[PreloadItem](#ZH-CN_TOPIC_0000002497444656__preloaditem)>是否

元服务中模块的预加载列表。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

dependenciesArray<[Dependency](#ZH-CN_TOPIC_0000002497444656__dependency)>是否

模块运行依赖的动态共享库列表。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

fileContextMenuConfig11+string是否

模块的文件菜单配置。通过调用[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_MENU获取。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

routerMap12+Array<[RouterItem](#ZH-CN_TOPIC_0000002497444656__routeritem12)>是否

[模块的路由表配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#routermap标签)。通过调用[getBundleInfoForSelf](../../modules/ohos/@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfoforself)接口，bundleFlags参数传入GET_BUNDLE_INFO_WITH_HAP_MODULE和GET_BUNDLE_INFO_WITH_ROUTER_MAP获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

codePath12+string是否

模块的安装路径。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

nativeLibraryPath12+string是否应用程序内模块本地库文件路径。[]()[]()

#### PreloadItem

描述元服务中模块的预加载模块信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明moduleNamestring是否模块名称。[]()[]()

#### Dependency

描述模块所依赖的动态共享库信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明bundleName10+string是否标识当前模块依赖的共享包包名。moduleNamestring是否标识当前模块依赖的共享包模块名。versionCode10+number是否标识当前共享包的版本号。[]()[]()

#### RouterItem12+

描述模块配置的路由表信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明namestring是否标识跳转页面的名称。pageSourceFilestring是否标识页面在模块内的路径。buildFunctionstring是否标识被@Builder修饰的函数，该函数描述页面的UI。dataArray<[DataItem](#ZH-CN_TOPIC_0000002497444656__dataitem12)>是否标识[路由表配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#routermap标签)中的字符串自定义数据，即data字段的信息，该字段已由系统解析，无需开发者自行解析。customDatastring是否标识[路由表配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#routermap标签)中的任意类型的自定义数据，即customData字段的JSON字符串，开发者需要调用JSON.parse函数解析出具体内容。[]()[]()

#### DataItem12+

描述模块配置的路由表中的自定义数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

名称类型只读可选说明keystring是否标识路由表自定义数据的键。valuestring是否标识路由表自定义数据的值。