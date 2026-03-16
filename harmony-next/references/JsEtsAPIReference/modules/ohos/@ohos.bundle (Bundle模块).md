# @ohos.bundle (Bundle模块)

本模块提供应用信息查询能力，支持[包信息](../../topics/misc/BundleInfo.md)、[应用信息](../../topics/system-services/ApplicationInfo.md)、[Ability组件信息](../../topics/system-services/AbilityInfo.md)等信息的查询，以及应用禁用状态的查询、设置等。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 9开始，该模块不再维护，建议使用[@ohos.bundle.bundleManager](@ohos.bundle.bundleManager (应用程序包管理模块).md)替代。

#### 导入模块

```ets
import bundle from '@ohos.bundle';
```

#### 权限列表

权限权限等级描述ohos.permission.GET_BUNDLE_INFOnormal查询指定应用信息。ohos.permission.GET_BUNDLE_INFO_PRIVILEGEDsystem_basic可查询所有应用信息。

权限等级参考[权限APL等级说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permission-mgmt-overview#权限机制中的基本概念)。

#### bundle.getApplicationInfodeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getApplicationInfo(bundleName: string, bundleFlags: number, userId?: number): Promise<ApplicationInfo>

根据给定的Bundle名称获取ApplicationInfo。使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是要查询的应用Bundle名称。bundleFlagsnumber是用于指定返回的应用信息对象中包含信息的标记。取值范围请参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中应用信息相关flag。userIdnumber否用户ID。默认值：调用方所在用户，取值范围：大于等于0。

**返回值：**

类型说明Promise<[ApplicationInfo](../../topics/system-services/ApplicationInfo.md)>Promise形式返回应用程序信息。

**示例：**

```ets
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 0;
let userId: number = 100;

bundle.getApplicationInfo(bundleName, bundleFlags, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getApplicationInfodeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getApplicationInfo(bundleName: string, bundleFlags: number, userId: number, callback: AsyncCallback<ApplicationInfo>): void

根据给定的Bundle名称获取指定用户下的ApplicationInfo，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是要查询的应用Bundle名称。bundleFlagsnumber是用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中应用信息相关flag。userIdnumber是用户ID。取值范围：大于等于0。callbackAsyncCallback<[ApplicationInfo](../../topics/system-services/ApplicationInfo.md)>是程序启动作为入参的回调函数，返回应用程序信息。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 0;
let userId: number = 100;

bundle.getApplicationInfo(bundleName, bundleFlags, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getApplicationInfodeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getApplicationInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<ApplicationInfo>): void

根据给定的Bundle名称获取ApplicationInfo，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是要查询的应用Bundle名称。bundleFlagsnumber是用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中应用信息相关flag。callbackAsyncCallback<[ApplicationInfo](../../topics/system-services/ApplicationInfo.md)>是程序启动作为入参的回调函数，返回应用程序信息。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 0;

bundle.getApplicationInfo(bundleName, bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAllBundleInfodeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getAllBundleInfo(bundleFlag: BundleFlag, userId?: number): Promise<Array<BundleInfo>>

获取指定用户所有的BundleInfo，使用Promise形式异步回调。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleFlagBundleFlag是用于指定返回的包信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中包信息相关flag。userIdnumber否用户ID。默认值：调用方所在用户，取值范围：大于等于0。

**返回值：**

类型说明Promise<Array<[BundleInfo](../../topics/misc/BundleInfo.md)>>Promise形式返回所有可用的BundleInfo

**示例：**

```ets
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleFlag: number = 0;
let userId: number = 100;

bundle.getAllBundleInfo(bundleFlag, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getAllBundleInfodeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getAllBundleInfo(bundleFlag: BundleFlag, callback: AsyncCallback<Array<BundleInfo>>): void

获取当前用户所有的BundleInfo，使用callback异步回调。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleFlagBundleFlag是用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中包信息相关flag。callbackAsyncCallback<Array<[BundleInfo](../../topics/misc/BundleInfo.md)>>是程序启动作为入参的回调函数，返回所有可用的BundleInfo。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleFlag: number = 0;

bundle.getAllBundleInfo(bundleFlag, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAllBundleInfodeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getAllBundleInfo(bundleFlag: BundleFlag, userId: number, callback: AsyncCallback<Array<BundleInfo>>): void

获取系统中指定用户下所有的BundleInfo，使用callback异步回调。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleFlagBundleFlag是用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中包信息相关flag。userIdnumber是用户ID。默认值：调用方所在用户，取值范围：大于等于0。callbackAsyncCallback<Array<[BundleInfo](../../topics/misc/BundleInfo.md)>>是程序启动作为入参的回调函数，返回指定用户下所有包的BundleInfo。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleFlag: number = 0;
let userId: number = 100;

bundle.getAllBundleInfo(bundleFlag, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getBundleInfodeprecated

从API version 9开始不再维护，建议使用[bundleManager.getBundleInfo](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfo14-2)替代。

getBundleInfo(bundleName: string, bundleFlags: number, options?: BundleOptions): Promise<BundleInfo>

根据给定的Bundle名称获取BundleInfo，使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是要查询的应用Bundle名称。bundleFlagsnumber是用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中包信息相关flag。options[BundleOptions](#ZH-CN_TOPIC_0000002529284637__bundleoptionsdeprecated)否包含userid的查询选项。

**返回值：**

类型说明Promise<[BundleInfo](../../topics/misc/BundleInfo.md)>Promise对象，获取成功时返回包信息。

**示例：**

```ets
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 1;
let options: bundle.BundleOptions = {
  "userId": 100
};

bundle.getBundleInfo(bundleName, bundleFlags, options)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getBundleInfodeprecated

从API version 9开始不再维护，建议使用[bundleManager.getBundleInfo](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfo14-1)替代。

getBundleInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void

根据给定的Bundle名称获取BundleInfo，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是需要查询的应用Bundle名称。bundleFlagsnumber是用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中包信息相关flag。callbackAsyncCallback<[BundleInfo](../../topics/misc/BundleInfo.md)>是程序启动作为入参的回调函数，返回包信息。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 1;

bundle.getBundleInfo(bundleName, bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getBundleInfodeprecated

从API version 9开始不再维护，建议使用[bundleManager.getBundleInfo](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundleinfo14)替代。

getBundleInfo(bundleName: string, bundleFlags: number, options: BundleOptions, callback: AsyncCallback<BundleInfo>): void

根据给定的Bundle名称获取BundleInfo，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是要查询的应用Bundle名称。bundleFlagsnumber是用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中包信息相关flag。options[BundleOptions](#ZH-CN_TOPIC_0000002529284637__bundleoptionsdeprecated)是包含userid。callbackAsyncCallback<[BundleInfo](../../topics/misc/BundleInfo.md)>是程序启动作为入参的回调函数，返回包信息。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 1;
let options: bundle.BundleOptions = {
  "userId": 100
};

bundle.getBundleInfo(bundleName, bundleFlags, options, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAllApplicationInfodeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getAllApplicationInfo(bundleFlags: number, userId?: number): Promise<Array<ApplicationInfo>>

获取指定用户下所有已安装的应用信息，使用promise异步回调。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleFlagsnumber是用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中应用信息相关flag。userIdnumber否用户ID。默认值：调用方所在用户，取值范围：大于等于0。

**返回值：**

类型说明Promise<Array<[ApplicationInfo](../../topics/system-services/ApplicationInfo.md)>>Promise对象，获取成功时返回应用信息列表。

**示例：**

```ets
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleFlags: number = 8;
let userId: number = 100;

bundle.getAllApplicationInfo(bundleFlags, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getAllApplicationInfodeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getAllApplicationInfo(bundleFlags: number, userId: number, callback: AsyncCallback<Array<ApplicationInfo>>): void

获取指定用户下所有已安装的应用信息，使用callback异步回调。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleFlagsnumber是用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中应用信息相关flag。userIdnumber是用户ID。默认值：调用方所在用户，取值范围：大于等于0。callbackAsyncCallback<Array<[ApplicationInfo](../../topics/system-services/ApplicationInfo.md)>>是程序启动作为入参的回调函数，返回应用信息列表。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleFlags: number = bundle.BundleFlag.GET_APPLICATION_INFO_WITH_PERMISSION;
let userId: number = 100;

bundle.getAllApplicationInfo(bundleFlags, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAllApplicationInfodeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getAllApplicationInfo(bundleFlags: number, callback: AsyncCallback<Array<ApplicationInfo>>): void

获取调用方所在用户下已安装的应用信息，使用callback异步回调。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleFlagsnumber是用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中应用信息相关flag。callbackAsyncCallback<Array<[ApplicationInfo](../../topics/system-services/ApplicationInfo.md)>>是程序启动作为入参的回调函数，返回应用信息列表。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleFlags: number = bundle.BundleFlag.GET_APPLICATION_INFO_WITH_PERMISSION;

bundle.getAllApplicationInfo(bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getBundleArchiveInfodeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getBundleArchiveInfo(hapFilePath: string, bundleFlags: number) : Promise<BundleInfo>

获取有关HAP中包含的应用程序包的信息，使用Promise异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明hapFilePathstring是HAP存放路径。支持当前应用程序的绝对路径和数据目录沙箱路径。bundleFlagsnumber是用于指定要返回的BundleInfo对象中包含信息的标记。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中包信息相关flag。

**返回值：**

类型说明Promise<[BundleInfo](../../topics/misc/BundleInfo.md)>返回值为Promise对象，Promise中包含有关HAP中包含的应用程序的信息。

**示例：**

```ets
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let hapFilePath: string = "/data/storage/el2/base/test.hap";
let bundleFlags: number = 0;

bundle.getBundleArchiveInfo(hapFilePath, bundleFlags)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getBundleArchiveInfodeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getBundleArchiveInfo(hapFilePath: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>) : void

获取有关HAP中包含的应用程序包的信息，使用callback异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明hapFilePathstring是HAP存放路径，支持当前应用程序的绝对路径和数据目录沙箱路径。bundleFlagsnumber是用于指定要返回的BundleInfo对象中包含信息的标记。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中包信息相关flag。callbackAsyncCallback<[BundleInfo](../../topics/misc/BundleInfo.md)>是程序启动作为入参的回调函数，返回HAP中包含的应用程序包的信息。

**示例：**

```ets
import bundle from '@ohos.bundle';

let hapFilePath: string = "/data/storage/el2/base/test.hap";
let bundleFlags: number = 0;

bundle.getBundleArchiveInfo(hapFilePath, bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAbilityInfodeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getAbilityInfo(bundleName: string, abilityName: string): Promise<AbilityInfo>

通过Bundle名称和组件名获取Ability组件信息，使用Promise形式异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是应用Bundle名称。abilityNamestring是Ability组件名称。

**返回值：**

类型说明Promise<[AbilityInfo](../../topics/system-services/AbilityInfo.md)>Promise形式返回Ability信息。

**示例：**

```ets
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getAbilityInfodeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getAbilityInfo(bundleName: string, abilityName: string, callback: AsyncCallback<AbilityInfo>): void

通过Bundle名称和组件名获取Ability组件信息，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是应用Bundle名称。abilityNamestring是Ability名称。callbackAsyncCallback<[AbilityInfo](../../topics/system-services/AbilityInfo.md)>是程序启动作为入参的回调函数，返回Ability信息。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAbilityLabel8+deprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getAbilityLabel(bundleName: string, abilityName: string): Promise<string>

通过Bundle名称和ability名称获取应用名称，使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是应用Bundle名称。abilityNamestring是Ability名称。

**返回值：**

类型说明Promise<string>Promise形式返回应用名称信息。

**示例：**

```ets
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityLabel(bundleName, abilityName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getAbilityLabel8+deprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getAbilityLabel(bundleName: string, abilityName: string, callback : AsyncCallback<string>): void

通过Bundle名称和Ability组件名获取应用名称，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是应用Bundle名称。abilityNamestring是Ability名称。callbackAsyncCallback<string>是程序启动作为入参的回调函数，返回应用名称信息。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityLabel(bundleName, abilityName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.isAbilityEnabled8+deprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

isAbilityEnabled(info: AbilityInfo): Promise<boolean>

根据给定的AbilityInfo查询ability是否已经启用，使用Promise异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明info[AbilityInfo](../../topics/system-services/AbilityInfo.md)是Ability的配置信息。

**返回值：**

类型说明Promise<boolean>Promise形式返回boolean代表是否启用。

**示例：**

```ets
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName).then((abilityInfo) => {
  bundle.isAbilityEnabled(abilityInfo).then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
})
```

#### bundle.isAbilityEnabled8+deprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

isAbilityEnabled(info : AbilityInfo, callback : AsyncCallback<boolean>): void

根据给定的AbilityInfo查询ability是否已经启用，使用callback异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明info[AbilityInfo](../../topics/system-services/AbilityInfo.md)是Ability的配置信息。callbackAsyncCallback<boolean>是回调函数，返回boolean代表是否启用。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName).then((abilityInfo) => {
  bundle.isAbilityEnabled(abilityInfo, (err, data) => {
    if (err) {
      console.error('Operation failed. Cause: ' + JSON.stringify(err));
      return;
    }
    console.info('Operation successful. Data:' + JSON.stringify(data));
  })
})
```

#### bundle.isApplicationEnabled8+deprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

isApplicationEnabled(bundleName: string): Promise<boolean>

根据给定的bundleName查询指定应用程序是否已经启用，使用Promise异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是要查询的应用Bundle名称。

**返回值：**

类型说明Promise<boolean>Promise形式返回boolean代表是否启用。

**示例：**

```ets
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";

bundle.isApplicationEnabled(bundleName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.isApplicationEnabled8+deprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

isApplicationEnabled(bundleName: string, callback : AsyncCallback<boolean>): void

根据给定的bundleName查询指定应用程序是否已经启用，使用callback异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是要查询的应用Bundle名称。callbackAsyncCallback<boolean>是回调函数，返回boolean代表是否启用。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";

bundle.isApplicationEnabled(bundleName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.queryAbilityByWantdeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

queryAbilityByWant(want: Want, bundleFlags: number, userId?: number): Promise<Array<AbilityInfo>>

根据给定的意图获取Ability组件信息，使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明want[Want](@ohos.application.Want (Want).md)是包含要查询的应用Bundle名称的意图。bundleFlagsnumber是用于指定返回abilityInfo信息。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中Ability信息相关flag。userIdnumber否用户ID。默认值：调用方所在用户，取值范围：大于等于0。

**返回值：**

类型说明Promise<Array<[AbilityInfo](../../topics/system-services/AbilityInfo.md)>>Promise形式返回Ability信息。

**示例：**

```ets
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';
import Want from '@ohos.app.ability.Want';

let bundleFlags: number = 0;
let userId: number = 100;
let want: Want = {
  bundleName: "com.example.myapplication",
  abilityName: "EntryAbility"
};

bundle.queryAbilityByWant(want, bundleFlags, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.queryAbilityByWantdeprecated

从API version 9开始不再维护。

queryAbilityByWant(want: Want, bundleFlags: number, userId: number, callback: AsyncCallback<Array<AbilityInfo>>): void

根据给定的意图获取指定用户下Ability信息，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明want[Want](@ohos.application.Want (Want).md)是指示包含要查询的应用Bundle名称的意图。bundleFlagsnumber是用于指定返回abilityInfo信息。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中Ability信息相关flag。userIdnumber是用户ID。取值范围：大于等于0。callbackAsyncCallback<Array<[AbilityInfo](../../topics/system-services/AbilityInfo.md)>>是程序启动作为入参的回调函数，返回Ability信息。

**示例：**

```ets
import bundle from '@ohos.bundle';
import Want from '@ohos.app.ability.Want';

let bundleFlags: number = 0;
let userId: number = 100;
let want: Want = {
  bundleName: "com.example.myapplication",
  abilityName: "EntryAbility"
};

bundle.queryAbilityByWant(want, bundleFlags, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.queryAbilityByWantdeprecated

从API version 9开始不再维护。

queryAbilityByWant(want: Want, bundleFlags: number, callback: AsyncCallback<Array<AbilityInfo>>): void

根据给定的意图获取Ability信息，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明want[Want](@ohos.application.Want (Want).md)是指示包含要查询的应用Bundle名称的意图。bundleFlagsnumber是用于指定返回abilityInfo信息。取值范围：参考[BundleFlag说明](#ZH-CN_TOPIC_0000002529284637__bundleflagdeprecated)中Ability信息相关flag。callbackAsyncCallback<Array<[AbilityInfo](../../topics/system-services/AbilityInfo.md)>>是程序启动作为入参的回调函数，返回Ability信息。

**示例：**

```ets
import bundle from '@ohos.bundle';
import Want from '@ohos.app.ability.Want';

let bundleFlags: number = 0;
let want: Want = {
  bundleName: "com.example.myapplication",
  abilityName: "EntryAbility"
};

bundle.queryAbilityByWant(want, bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getLaunchWantForBundledeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getLaunchWantForBundle(bundleName: string): Promise<Want>

查询拉起指定应用的want对象，使用Promise异步回调。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是要查询的应用Bundle名称。

**返回值：**

类型说明Promise<[Want](@ohos.application.Want (Want).md)>返回值为Promise对象，Promise中包含拉起指定应用的Want对象。

**示例：**

```ets
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";

bundle.getLaunchWantForBundle(bundleName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getLaunchWantForBundledeprecated

从API version 9开始不再维护，替代接口仅向系统应用开放。

getLaunchWantForBundle(bundleName: string, callback: AsyncCallback<Want>): void

查询拉起指定应用的want对象，使用callback异步回调。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是要查询的应用Bundle名称。callbackAsyncCallback<[Want](@ohos.application.Want (Want).md)>是程序启动作为入参的回调函数，返回拉起指定应用的want对象。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";

bundle.getLaunchWantForBundle(bundleName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getNameForUid8+deprecated

从API version 9开始不再维护，建议使用[bundleManager.getBundleNameByUid](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundlenamebyuid14-1)替代。

getNameForUid(uid: number): Promise<string>

通过uid获取对应的Bundle名称，使用Promise异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明uidnumber是要查询的uid。

**返回值：**

类型说明Promise<string>返回值为Promise对象，Promise中包含指定uid的Bundle名称。

**示例：**

```ets
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let uid: number = 20010005;

bundle.getNameForUid(uid)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getNameForUid8+deprecated

从API version 9开始不再维护，建议使用[bundleManager.getBundleNameByUid](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundlemanagergetbundlenamebyuid14)替代。

getNameForUid(uid: number, callback: AsyncCallback<string>) : void

通过uid获取对应的Bundle名称，使用callback异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明uidnumber是要查询的uid。callbackAsyncCallback<string>是程序启动作为入参的回调函数，返回指定uid的Bundle名称。

**示例：**

```ets
import bundle from '@ohos.bundle';

let uid: number = 20010005;

bundle.getNameForUid(uid, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAbilityIcon8+deprecated

从API version 9开始不再维护，建议使用[resourceManager.getMediaContent](@ohos.resourceManager (资源管理).md#ZH-CN_TOPIC_0000002497445338__getmediacontent9)替代。

getAbilityIcon(bundleName: string, abilityName: string): Promise<image.PixelMap>

通过bundleName和abilityName获取对应Icon的[PixelMap](../../types/interfaces/Interface (PixelMap).md)，使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是要查询的应用Bundle名称。abilityNamestring是要查询的Ability组件名。

**返回值：**

类型说明Promise<image.PixelMap>返回值为[PixelMap](../../types/interfaces/Interface (PixelMap).md)。

**示例：**

```ets
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityIcon(bundleName, abilityName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getAbilityIcon8+deprecated

从API version 9开始不再维护，建议使用[resourceManager.getMediaContent](@ohos.resourceManager (资源管理).md#ZH-CN_TOPIC_0000002497445338__getmediacontent9)替代。

getAbilityIcon(bundleName: string, abilityName: string, callback: AsyncCallback<image.PixelMap>): void

通过bundleName和abilityName获取对应Icon的[PixelMap](../../types/interfaces/Interface (PixelMap).md)，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET_BUNDLE_INFO_PRIVILEGED 或 ohos.permission.GET_BUNDLE_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

参数名类型必填说明bundleNamestring是要查询的应用Bundle名称。abilityNamestring是要查询的Ability组件名。callbackAsyncCallback<image.PixelMap>是程序启动作为入参的回调函数，返回指定[PixelMap](../../types/interfaces/Interface (PixelMap).md)。

**示例：**

```ets
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityIcon(bundleName, abilityName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### InstallErrorCodedeprecated

从API version 9开始不再维护，建议使用[errorcode-bundle](../../errors/包管理子系统通用错误码.md)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称值说明SUCCESS0安装成功。STATUS_INSTALL_FAILURE1安装失败（不存在安装的应用）。STATUS_INSTALL_FAILURE_ABORTED2安装中止。STATUS_INSTALL_FAILURE_INVALID3安装参数无效。STATUS_INSTALL_FAILURE_CONFLICT4安装冲突 （常见于升级和已有应用基本信息不一致）。STATUS_INSTALL_FAILURE_STORAGE5存储包信息失败。STATUS_INSTALL_FAILURE_INCOMPATIBLE6安装不兼容（常见于版本降级安装或者签名信息错误）。STATUS_UNINSTALL_FAILURE7卸载失败 （不存在卸载的应用）。STATUS_UNINSTALL_FAILURE_BLOCKED8卸载中止 （没有使用）。STATUS_UNINSTALL_FAILURE_ABORTED9卸载中止 （参数无效导致）。STATUS_UNINSTALL_FAILURE_CONFLICT10卸载冲突 （卸载系统应用失败， 结束应用进程失败）。STATUS_INSTALL_FAILURE_DOWNLOAD_TIMEOUT0x0B安装失败 （下载超时）。STATUS_INSTALL_FAILURE_DOWNLOAD_FAILED0x0C安装失败 （下载失败）。STATUS_RECOVER_FAILURE_INVALID8+0x0D恢复预置应用失败。STATUS_ABILITY_NOT_FOUND0x40Ability未找到。STATUS_BMS_SERVICE_ERROR0x41BMS服务错误。STATUS_FAILED_NO_SPACE_LEFT8+0x42设备空间不足。STATUS_GRANT_REQUEST_PERMISSIONS_FAILED8+0x43应用授权失败。STATUS_INSTALL_PERMISSION_DENIED8+0x44缺少安装权限。STATUS_UNINSTALL_PERMISSION_DENIED8+0x45缺少卸载权限。

#### BundleFlagdeprecated

从API version 9开始不再维护，建议使用[bundleManager.BundleFlag](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__bundleflag)替代。

包信息标志，指示需要获取的包信息的内容。

当接口与标志不匹配时，该标志会被忽略，例如获取application时使用GET_ABILITY_INFO_WITH_PERMISSION对结果不会产生影响。

标志可以叠加使用，例如使用GET_APPLICATION_INFO_WITH_PERMISSION + GET_APPLICATION_INFO_WITH_DISABLE可以使结果同时包含应用权限信息和被禁用的应用信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称值说明GET_BUNDLE_DEFAULT0x00000000获取默认的应用信息。GET_BUNDLE_WITH_ABILITIES0x00000001获取包括Ability信息的包信息。GET_ABILITY_INFO_WITH_PERMISSION0x00000002获取包括权限的Ability信息。GET_ABILITY_INFO_WITH_APPLICATION0x00000004获取包括Application的ability信息。GET_APPLICATION_INFO_WITH_PERMISSION0x00000008获取包括权限的应用信息。GET_BUNDLE_WITH_REQUESTED_PERMISSION0x00000010获取包括所需权限的包信息。GET_ABILITY_INFO_WITH_METADATA8+0x00000020获取ability的元数据信息。GET_APPLICATION_INFO_WITH_METADATA8+0x00000040获取应用的元数据信息。GET_ABILITY_INFO_SYSTEMAPP_ONLY8+0x00000080获取仅包括系统应用的ability信息。GET_ABILITY_INFO_WITH_DISABLE8+0x00000100获取包括被禁用的ability信息。GET_APPLICATION_INFO_WITH_DISABLE8+0x00000200获取包括被禁用的应用信息。GET_ALL_APPLICATION_INFO0xFFFF0000获取应用所有的信息。

#### BundleOptionsdeprecated

从API version 9开始不再维护，不推荐使用。

查询选项，包含userId。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称类型只读可选说明userIdnumber否是用户ID。默认值：调用方所在用户，取值范围：大于等于0。

#### AbilityTypedeprecated

从API version 9开始不再维护，建议使用[bundleManager.AbilityType](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__abilitytype)替代。

Ability组件类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称值说明UNKNOWN无未知Ability类型。PAGE无表示基于Page模板开发的FA，用于提供与用户交互的能力。SERVICE无表示基于Service模板开发的PA，用于提供后台运行任务的能力。DATA无表示基于Data模板开发的PA，用于对外部提供统一的数据访问对象。

#### DisplayOrientationdeprecated

从API version 9开始不再维护，建议使用[bundleManager.DisplayOrientation](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__displayorientation)替代。

屏幕显示方向。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称值说明UNSPECIFIED无屏幕方向--不指定。LANDSCAPE无屏幕方向--横屏。PORTRAIT无屏幕方向--竖屏。FOLLOW_RECENT无屏幕方向--紧跟上一个组件。

#### LaunchModedeprecated

从API version 9开始不再维护，建议使用[bundleManager.LaunchType](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__launchtype)替代。

Ability组件的启动模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称值说明SINGLETON0Ability只有一个实例。STANDARD1Ability有多个实例。

#### AbilitySubTypedeprecated

从API version 9开始不再维护，不推荐使用。

Ability组件的子类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称值说明UNSPECIFIED0未定义Ability子类型。CA1Ability子类型是带有 UI 的服务。

#### ColorModedeprecated

从API version 9开始不再维护，不推荐使用。

应用、卡片等的颜色模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称值说明AUTO_MODE-1自动模式。DARK_MODE0黑色模式。LIGHT_MODE1亮度模式。

#### GrantStatusdeprecated

从API version 9开始不再维护，建议使用[bundleManager.PermissionGrantState](@ohos.bundle.bundleManager (应用程序包管理模块).md#ZH-CN_TOPIC_0000002497444634__permissiongrantstate)替代。

权限授予状态。

**系统能力：** SystemCapability.BundleManager.BundleFramework

名称值说明PERMISSION_DENIED-1拒绝授予权限。PERMISSION_GRANTED0授予权限。