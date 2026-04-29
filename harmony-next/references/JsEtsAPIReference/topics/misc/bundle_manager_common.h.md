# bundle_manager_common.h

**概述**

声明BundleManager定义的相关错误码。

引用文件： <bundle/bundle_manager_common.h>

库： libbundle_ndk.z.so

系统能力： SystemCapability.BundleManager.BundleFramework.Core

起始版本： 21

相关模块： [Native_Bundle](Native_Bundle.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| BundleManager_ErrorCode | BundleManager_ErrorCode | 枚举错误码。 |

**枚举类型说明**

**BundleManager_ErrorCode**

```ets
enum BundleManager_ErrorCode
```

描述

枚举错误码。

起始版本： 21

| 枚举项 | 描述 |
| --- | --- |
| BUNDLE_MANAGER_ERROR_CODE_NO_ERROR = 0 | 执行成功。 |
| BUNDLE_MANAGER_ERROR_CODE_PERMISSION_DENIED = 201 | 权限被拒绝。 |
| BUNDLE_MANAGER_ERROR_CODE_PARAM_INVALID = 401 | 参数无效。 |