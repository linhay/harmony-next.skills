# @ohos.account.osAccount (系统账号管理)

本模块提供管理系统账号的基础能力，包括系统账号的添加、删除、查询、设置、订阅、启动等功能。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { osAccount } from '@kit.BasicServicesKit';
```

#### osAccount.getAccountManager

getAccountManager(): AccountManager

获取系统账号管理对象。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AccountManager | 系统账号管理对象。 |

**示例：**

```ets
let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
```

#### OsAccountType

表示系统账号类型的枚举。

**系统能力：** SystemCapability.Account.OsAccount

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ADMIN | 0 | 管理员账号。 |
| NORMAL | 1 | 普通账号。 |
| GUEST | 2 | 访客账号。 |

#### AccountManager

系统账号管理类。

#### checkMultiOsAccountEnabled9+

checkMultiOsAccountEnabled(callback: AsyncCallback<boolean>): void

判断是否支持多系统账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示支持多系统账号；返回false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码]([账号管理错误码](../../errors/账号管理错误码.md).md)和[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkMultiOsAccountEnabled((err: BusinessError, isEnabled: boolean) => {
    if (err) {
      console.error(`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkMultiOsAccountEnabled successfully, isEnabled: ' + isEnabled);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}`);
}
```

#### checkMultiOsAccountEnabled9+

checkMultiOsAccountEnabled(): Promise<boolean>

判断是否支持多系统账号。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示支持多系统账号；返回false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  accountManager.checkMultiOsAccountEnabled().then((isEnabled: boolean) => {
    console.info('checkMultiOsAccountEnabled successfully, isEnabled: ' + isEnabled);
  }).catch((err: BusinessError) => {
    console.error(`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}`);
}
```

#### checkOsAccountActivated(deprecated)

checkOsAccountActivated(localId: number, callback: AsyncCallback<boolean>): void

判断指定系统账号是否处于激活状态。使用callback异步回调。

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示账号已激活；返回false表示账号未激活。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：** 判断ID为100的系统账号是否处于激活状态

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.checkOsAccountActivated(localId, (err: BusinessError, isActivated: boolean) => {
    if (err) {
      console.error(`checkOsAccountActivated failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkOsAccountActivated successfully, isActivated:' + isActivated);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountActivated exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkOsAccountActivated(deprecated)

checkOsAccountActivated(localId: number): Promise<boolean>

判断指定系统账号是否处于激活状态。使用Promise异步回调。

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示账号已激活；返回false表示账号未激活。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：** 判断ID为100的系统账号是否处于激活状态

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.checkOsAccountActivated(localId).then((isActivated: boolean) => {
    console.info('checkOsAccountActivated successfully, isActivated: ' + isActivated);
  }).catch((err: BusinessError) => {
    console.error(`checkOsAccountActivated failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountActivated exception: code is ${err.code}, message is ${err.message}`);
}
```

#### isOsAccountConstraintEnabled11+

isOsAccountConstraintEnabled(constraint: string): Promise<boolean>

判断当前系统账号是否使能指定约束。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| constraint | string | 是 | 指定的约束名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示已使能指定的约束；返回false表示未使能指定的约束。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：** 判断ID为100的系统账号是否有禁止使用Wi-Fi的约束

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let constraint: string = 'constraint.wifi';
try {
  accountManager.isOsAccountConstraintEnabled(constraint).then((isEnabled: boolean) => {
    console.info('isOsAccountConstraintEnabled successfully, isEnabled: ' + isEnabled);
  }).catch((err: BusinessError) => {
    console.error(`isOsAccountConstraintEnabled failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`isOsAccountConstraintEnabled exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkOsAccountConstraintEnabled(deprecated)

checkOsAccountConstraintEnabled(localId: number, constraint: string, callback: AsyncCallback<boolean>): void

判断指定系统账号是否具有指定约束。使用callback异步回调。

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| constraint | string | 是 | 指定的约束名称。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示已使能指定的约束；返回false表示未使能指定的约束。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId or constraint. |
| 12300003 | Account not found. |

**示例：** 判断ID为100的系统账号是否有禁止使用Wi-Fi的约束

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let constraint: string = 'constraint.wifi';
try {
  accountManager.checkOsAccountConstraintEnabled(localId, constraint, (err: BusinessError, isEnabled: boolean)=>{
    if (err) {
      console.error(`checkOsAccountConstraintEnabled failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkOsAccountConstraintEnabled successfully, isEnabled: ' + isEnabled);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountConstraintEnabled exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkOsAccountConstraintEnabled(deprecated)

checkOsAccountConstraintEnabled(localId: number, constraint: string): Promise<boolean>

判断指定系统账号是否具有指定约束。使用Promise异步回调。

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| constraint | string | 是 | 指定的约束名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示已使能指定的约束；返回false表示未使能指定的约束。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId or constraint. |
| 12300003 | Account not found. |

**示例：** 判断ID为100的系统账号是否有禁止使用Wi-Fi的约束

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let constraint: string = 'constraint.wifi';
try {
  accountManager.checkOsAccountConstraintEnabled(localId, constraint).then((isEnabled: boolean) => {
    console.info('checkOsAccountConstraintEnabled successfully, isEnabled: ' + isEnabled);
  }).catch((err: BusinessError) => {
    console.error(`checkOsAccountConstraintEnabled failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountConstraintEnabled exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkOsAccountTestable9+

checkOsAccountTestable(callback: AsyncCallback<boolean>): void

检查当前系统账号是否为测试账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前账号为测试账号；返回false表示当前账号非测试账号。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkOsAccountTestable((err: BusinessError, isTestable: boolean) => {
    if (err) {
      console.error(`checkOsAccountTestable failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkOsAccountTestable successfully, isTestable: ' + isTestable);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountTestable code is ${err.code}, message is ${err.message}`);
}
```

#### checkOsAccountTestable9+

checkOsAccountTestable(): Promise<boolean>

检查当前系统账号是否为测试账号。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前账号为测试账号；返回false表示当前账号非测试账号。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkOsAccountTestable().then((isTestable: boolean) => {
    console.info('checkOsAccountTestable successfully, isTestable: ' + isTestable);
  }).catch((err: BusinessError) => {
    console.error(`checkOsAccountTestable failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountTestable exception: code is ${err.code}, message is ${err.message}`);
}
```

#### isOsAccountUnlocked11+

isOsAccountUnlocked(): Promise<boolean>

检查当前系统账号是否已认证解锁。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前账号已认证解锁；返回false表示当前账号未认证解锁。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.isOsAccountUnlocked().then((isVerified: boolean) => {
    console.info('isOsAccountUnlocked successfully, isVerified: ' + isVerified);
  }).catch((err: BusinessError) => {
    console.error(`isOsAccountUnlocked failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`isOsAccountUnlocked exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkOsAccountVerified(deprecated)

checkOsAccountVerified(callback: AsyncCallback<boolean>): void

检查当前系统账号是否已认证解锁。使用callback异步回调。


从API version 9开始支持，从API version 11开始废弃。建议使用[isOsAccountUnlocked](#ZH-CN_TOPIC_0000002522081590__isosaccountunlocked11)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前账号已认证解锁；返回false表示当前账号未认证解锁。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkOsAccountVerified((err: BusinessError, isVerified: boolean) => {
    if (err) {
      console.error(`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkOsAccountVerified(deprecated)

checkOsAccountVerified(): Promise<boolean>

检查当前系统账号是否已认证解锁。使用Promise异步回调。


从API version 9开始支持，从API version 11开始废弃。建议使用[isOsAccountUnlocked](#ZH-CN_TOPIC_0000002522081590__isosaccountunlocked11)替代。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前账号已认证解锁；返回false表示当前账号未认证解锁。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkOsAccountVerified().then((isVerified: boolean) => {
    console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
  }).catch((err: BusinessError) => {
    console.error(`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkOsAccountVerified(deprecated)

checkOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void

检查指定系统账号是否已验证。使用callback异步回调。

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前账号已认证解锁；返回false表示当前账号未认证解锁。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.checkOsAccountVerified(localId, (err: BusinessError, isVerified: boolean) => {
    if (err) {
      console.error(`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkOsAccountVerified(deprecated)

checkOsAccountVerified(localId: number): Promise<boolean>

检查指定系统账号是否已验证。使用Promise异步回调。

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。不填则检查当前系统账号是否已验证。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前账号已认证解锁；返回false表示当前账号未认证解锁。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.checkOsAccountVerified(localId).then((isVerified: boolean) => {
    console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
  }).catch((err: BusinessError) => {
    console.error(`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountCount9+

getOsAccountCount(callback: AsyncCallback<number>): void

获取已创建的系统账号数量。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。如果获取成功，err为null，data为已创建的系统账号的数量；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountCount((err: BusinessError, count: number) => {
    if (err) {
      console.error(`getOsAccountCount failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getOsAccountCount successfully, count: ' + count);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountCount exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountCount9+

getOsAccountCount(): Promise<number>

获取已创建的系统账号数量。使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回已创建的系统账号的数量。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountCount().then((count: number) => {
    console.info('getOsAccountCount successfully, count: ' + count);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountCount failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountCount exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountLocalId9+

getOsAccountLocalId(callback: AsyncCallback<number>): void

获取当前进程所属的系统账号ID。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。如果获取成功，err为null，data为当前进程所属的系统账号ID；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountLocalId((err: BusinessError, localId: number) => {
    if (err) {
      console.error(`getOsAccountLocalId failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getOsAccountLocalId successfully, localId: ' + localId);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalId exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountLocalId9+

getOsAccountLocalId(): Promise<number>

获取当前进程所属的系统账号ID。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回当前进程所属的系统账号ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountLocalId().then((localId: number) => {
    console.info('getOsAccountLocalId successfully, localId: ' + localId);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountLocalId failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalId exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountLocalIdForUid9+

getOsAccountLocalIdForUid(uid: number, callback: AsyncCallback<number>): void

根据uid查询对应的系统账号ID。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 进程uid。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果查询成功，err为null，data为对应的系统账号ID；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid uid. |

**示例：** 查询值为12345678的uid所属的系统账号的账号ID

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let uid: number = 12345678;
try {
  accountManager.getOsAccountLocalIdForUid(uid, (err: BusinessError, localId: number) => {
    if (err) {
      console.error(`getOsAccountLocalIdForUid failed, code is ${err.code}, message is ${err.message}`);
    }
    console.info('getOsAccountLocalIdForUid successfully, localId: ' + localId);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalIdForUid exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountLocalIdForUid9+

getOsAccountLocalIdForUid(uid: number): Promise<number>

根据uid查询对应的系统账号ID。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 进程uid。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回指定uid对应的系统账号ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid uid. |

**示例：** 查询值为12345678的uid所属的系统账号ID

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let uid: number = 12345678;
try {
  accountManager.getOsAccountLocalIdForUid(uid).then((localId: number) => {
    console.info('getOsAccountLocalIdForUid successfully, localId: ' + localId);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountLocalIdForUid failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalIdForUid exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountLocalIdForUidSync10+

getOsAccountLocalIdForUidSync(uid: number): number

根据uid查询对应的系统账号ID。使用同步方式返回结果。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 进程uid。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回指定uid对应的系统账号ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300002 | Invalid uid. |

**示例：** 查询值为12345678的uid所属的系统账号ID

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let uid: number = 12345678;
try {
  let localId : number = accountManager.getOsAccountLocalIdForUidSync(uid);
  console.info('getOsAccountLocalIdForUidSync successfully, localId: ' + localId);
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalIdForUidSync exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountLocalIdForDomain9+

getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void

根据域账号信息，获取与其关联的系统账号ID。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainInfo | DomainAccountInfo | 是 | 域账号信息。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果查询成功，err为null，data为域账号关联的系统账号ID；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid domainInfo. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountLocalIdForDomain(domainInfo, (err: BusinessError, localId: number) => {
    if (err) {
      console.error(`getOsAccountLocalIdForDomain failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getOsAccountLocalIdForDomain successfully, localId: ' + localId);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalIdForDomain exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountLocalIdForDomain9+

getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo): Promise<number>

根据域账号信息，获取与其关联的系统账号的账号ID。使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainInfo | DomainAccountInfo | 是 | 域账号信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回域账号关联的系统账号ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid domainInfo. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
try {
  accountManager.getOsAccountLocalIdForDomain(domainInfo).then((localId: number) => {
    console.info('getOsAccountLocalIdForDomain successfully, localId: ' + localId);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountLocalIdForDomain failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalIdForDomain exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountConstraints(deprecated)

getOsAccountConstraints(localId: number, callback: AsyncCallback<Array<string>>): void

获取指定系统账号的全部约束。使用callback异步回调。

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数，如果获取成功，err为null，data为该系统账号的全部约束；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：** 获取ID为100的系统账号的全部约束

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.getOsAccountConstraints(localId, (err: BusinessError, constraints: string[]) => {
    if (err) {
      console.error(`getOsAccountConstraints failed, err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getOsAccountConstraints successfully, constraints: ' + JSON.stringify(constraints));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountConstraints exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountConstraints(deprecated)

getOsAccountConstraints(localId: number): Promise<Array<string>>

获取指定系统账号的全部约束。使用Promise异步回调。

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回指定系统账号的全部约束。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：** 获取ID为100的系统账号的全部约束

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.getOsAccountConstraints(localId).then((constraints: string[]) => {
    console.info('getOsAccountConstraints, constraints: ' + constraints);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountConstraints err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountConstraints exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getActivatedOsAccountLocalIds9+

getActivatedOsAccountLocalIds(callback: AsyncCallback<Array<number>>): void

查询当前处于激活状态的系统账号的ID列表。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数。如果查询成功，err为null，data为当前处于激活状态的系统账号的ID列表；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getActivatedOsAccountLocalIds((err: BusinessError, idArray: number[])=>{
    if (err) {
      console.error(`getActivatedOsAccountLocalIds code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getActivatedOsAccountLocalIds idArray length:' + idArray.length);
      for(let i=0;i<idArray.length;i++) {
        console.info('activated os account id: ' + idArray[i]);
      }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getActivatedOsAccountLocalIds exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getActivatedOsAccountLocalIds9+

getActivatedOsAccountLocalIds(): Promise<Array<number>>

查询当前处于激活状态的系统账号的ID列表。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回当前处于激活状态的系统账号的ID列表。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getActivatedOsAccountLocalIds().then((idArray: number[]) => {
    console.info('getActivatedOsAccountLocalIds, idArray: ' + idArray);
  }).catch((err: BusinessError) => {
    console.error(`getActivatedOsAccountLocalIds err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getActivatedOsAccountLocalIds exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getCurrentOsAccount(deprecated)

getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void

查询当前进程所属的系统账号的信息。使用callback异步回调。

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.GET_LOCAL_ACCOUNTS10+，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<OsAccountInfo> | 是 | 回调函数。如果查询成功，err为null，data为当前进程所属的系统账号信息；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getCurrentOsAccount((err: BusinessError, curAccountInfo: osAccount.OsAccountInfo)=>{
    if (err) {
      console.error(`getCurrentOsAccount code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getCurrentOsAccount curAccountInfo:' + JSON.stringify(curAccountInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCurrentOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getCurrentOsAccount(deprecated)

getCurrentOsAccount(): Promise<OsAccountInfo>

查询当前进程所属的系统账号的信息。使用Promise异步回调。

从API version 9开始支持，从API version 11开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.GET_LOCAL_ACCOUNTS10+，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<OsAccountInfo> | Promise对象，返回当前进程所属的系统账号信息。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getCurrentOsAccount().then((accountInfo: osAccount.OsAccountInfo) => {
    console.info('getCurrentOsAccount, accountInfo: ' + JSON.stringify(accountInfo));
  }).catch((err: BusinessError) => {
    console.error(`getCurrentOsAccount err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCurrentOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountType9+

getOsAccountType(callback: AsyncCallback<OsAccountType>): void

查询当前进程所属的系统账号的账号类型。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<OsAccountType> | 是 | 回调函数。如果查询成功，err为null，data为当前进程所属的系统账号的账号类型；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountType((err: BusinessError, accountType: osAccount.OsAccountType) => {
    if (err) {
      console.error(`getOsAccountType err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getOsAccountType accountType: ' + accountType);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountType exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountType9+

getOsAccountType(): Promise<OsAccountType>

查询当前进程所属的系统账号的账号类型。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<OsAccountType> | Promise对象，返回当前进程所属的系统账号的账号类型。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountType().then((accountType: osAccount.OsAccountType) => {
    console.info('getOsAccountType, accountType: ' + accountType);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountType err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountType exception: code is ${err.code}, message is ${err.message}`);
}
```

#### queryDistributedVirtualDeviceId9+

queryDistributedVirtualDeviceId(callback: AsyncCallback<string>): void

获取分布式虚拟设备ID。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS（仅系统应用可申请）或 ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。如果获取成功，err为null，data为分布式虚拟设备ID；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.queryDistributedVirtualDeviceId((err: BusinessError, virtualID: string) => {
    if (err) {
      console.error(`queryDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('queryDistributedVirtualDeviceId virtualID: ' + virtualID);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryDistributedVirtualDeviceId exception: code is ${err.code}, message is ${err.message}`);
}
```

#### queryDistributedVirtualDeviceId9+

queryDistributedVirtualDeviceId(): Promise<string>

获取分布式虚拟设备ID。使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS（仅系统应用可申请）或 ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回分布式虚拟设备ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.queryDistributedVirtualDeviceId().then((virtualID: string) => {
    console.info('queryDistributedVirtualDeviceId, virtualID: ' + virtualID);
  }).catch((err: BusinessError) => {
    console.error(`queryDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryDistributedVirtualDeviceId exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountLocalIdForSerialNumber9+

getOsAccountLocalIdForSerialNumber(serialNumber: number, callback: AsyncCallback<number>): void

通过SN码查询与其关联的系统账号的账号ID。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serialNumber | number | 是 | 账号SN码。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果成功，err为null，data为与SN码关联的系统账号的账号ID；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid serialNumber. |
| 12300003 | The account indicated by serialNumber does not exist. |

**示例：** 查询与SN码12345关联的系统账号的ID

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let serialNumber: number = 12345;
try {
  accountManager.getOsAccountLocalIdForSerialNumber(serialNumber, (err: BusinessError, localId: number)=>{
    if (err) {
      console.error(`get localId code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('get localId:' + localId + ' by serialNumber: ' + serialNumber);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`get localId exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountLocalIdForSerialNumber9+

getOsAccountLocalIdForSerialNumber(serialNumber: number): Promise<number>

通过SN码查询与其关联的系统账号的账号ID。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serialNumber | number | 是 | 账号SN码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回与SN码关联的系统账号的账号ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid serialNumber. |
| 12300003 | The account indicated by serialNumber does not exist. |

**示例：** 查询与SN码12345关联的系统账号的ID

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let serialNumber: number = 12345;
try {
  accountManager.getOsAccountLocalIdForSerialNumber(serialNumber).then((localId: number) => {
    console.info('getOsAccountLocalIdForSerialNumber localId: ' + localId);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountLocalIdForSerialNumber err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalIdForSerialNumber exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getSerialNumberForOsAccountLocalId9+

getSerialNumberForOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void

通过系统账号ID获取与该系统账号关联的SN码。使用callback异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果获取成功，err为null，data为与该系统账号关联的SN码；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：** 获取ID为100的系统账号关联的SN码

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.getSerialNumberForOsAccountLocalId(localId, (err: BusinessError, serialNumber: number)=>{
    if (err) {
      console.error(`get serialNumber code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('get serialNumber:' + serialNumber + ' by localId: ' + localId);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`get serialNumber exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getSerialNumberForOsAccountLocalId9+

getSerialNumberForOsAccountLocalId(localId: number): Promise<number>

通过系统账号ID获取与该系统账号关联的SN码。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回与该系统账号关联的SN码。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**示例：** 获取ID为100的系统账号关联的SN码

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.getSerialNumberForOsAccountLocalId(localId).then((serialNumber: number) => {
    console.info('getSerialNumberForOsAccountLocalId serialNumber: ' + serialNumber);
  }).catch((err: BusinessError) => {
    console.error(`getSerialNumberForOsAccountLocalId err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getSerialNumberForOsAccountLocalId exception: code is ${err.code}, message is ${err.message}`);
}
```

#### isMultiOsAccountEnable(deprecated)

isMultiOsAccountEnable(callback: AsyncCallback<boolean>): void

判断是否支持多系统账号。使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[checkMultiOsAccountEnabled](#ZH-CN_TOPIC_0000002522081590__checkmultiosaccountenabled9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示支持多系统账号；返回false表示不支持。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isMultiOsAccountEnable((err: BusinessError, isEnabled: boolean) => {
  if (err) {
    console.error(`isMultiOsAccountEnable failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('isMultiOsAccountEnable successfully, isEnabled: ' + isEnabled);
  }
});
```

#### isMultiOsAccountEnable(deprecated)

isMultiOsAccountEnable(): Promise<boolean>

判断是否支持多系统账号。使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[checkMultiOsAccountEnabled](#ZH-CN_TOPIC_0000002522081590__checkmultiosaccountenabled9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示支持多系统账号；返回false表示不支持。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isMultiOsAccountEnable().then((isEnabled: boolean) => {
  console.info('isMultiOsAccountEnable successfully, isEnabled: ' + isEnabled);
}).catch((err: BusinessError) => {
  console.error(`isMultiOsAccountEnable failed, code is ${err.code}, message is ${err.message}`);
});
```

#### isOsAccountActived(deprecated)

isOsAccountActived(localId: number, callback: AsyncCallback<boolean>): void

判断指定系统账号是否处于激活状态。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示账号已激活；返回false表示账号未激活。 |

**示例：** 判断ID为100的系统账号是否处于激活状态

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.isOsAccountActived(localId, (err: BusinessError, isActived: boolean) => {
  if (err) {
    console.error(`isOsAccountActived failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('isOsAccountActived successfully, isActived:' + isActived);
  }
});
```

#### isOsAccountActived(deprecated)

isOsAccountActived(localId: number): Promise<boolean>

判断指定系统账号是否处于激活状态。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示账号已激活；返回false表示账号未激活。 |

**示例：** 判断ID为100的系统账号是否处于激活状态

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.isOsAccountActived(localId).then((isActived: boolean) => {
  console.info('isOsAccountActived successfully, isActived: ' + isActived);
}).catch((err: BusinessError) => {
  console.error(`isOsAccountActived failed, code is ${err.code}, message is ${err.message}`);
});
```

#### isOsAccountConstraintEnable(deprecated)

isOsAccountConstraintEnable(localId: number, constraint: string, callback: AsyncCallback<boolean>): void

判断指定系统账号是否具有指定约束。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| constraint | string | 是 | 指定的约束名称。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示已使能指定的约束；返回false表示未使能指定的约束。 |

**示例：** 判断ID为100的系统账号是否有禁止使用Wi-Fi的约束

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let constraint: string = 'constraint.wifi';
accountManager.isOsAccountConstraintEnable(localId, constraint, (err: BusinessError, isEnabled: boolean) => {
  if (err) {
    console.error(`isOsAccountConstraintEnable failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('isOsAccountConstraintEnable successfully, isEnabled: ' + isEnabled);
  }
});
```

#### isOsAccountConstraintEnable(deprecated)

isOsAccountConstraintEnable(localId: number, constraint: string): Promise<boolean>

判断指定系统账号是否具有指定约束。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| constraint | string | 是 | 指定的约束名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示已使能指定的约束；返回false表示未使能指定的约束。 |

**示例：** 判断ID为100的系统账号是否有禁止使用Wi-Fi的约束

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let constraint: string = 'constraint.wifi';
accountManager.isOsAccountConstraintEnable(localId, constraint).then((isEnabled: boolean) => {
  console.info('isOsAccountConstraintEnable successfully, isEnabled: ' + isEnabled);
}).catch((err: BusinessError) => {
  console.error(`isOsAccountConstraintEnable err: code is ${err.code}, message is ${err.message}`);
});
```

#### isTestOsAccount(deprecated)

isTestOsAccount(callback: AsyncCallback<boolean>): void

检查当前系统账号是否为测试账号。使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[checkOsAccountTestable](#ZH-CN_TOPIC_0000002522081590__checkosaccounttestable9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前账号为测试账号；返回false表示当前账号非测试账号。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isTestOsAccount((err: BusinessError, isTestable: boolean) => {
  if (err) {
    console.error(`isTestOsAccount failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('isTestOsAccount successfully, isTestable: ' + isTestable);
  }
});
```

#### isTestOsAccount(deprecated)

isTestOsAccount(): Promise<boolean>

检查当前系统账号是否为测试账号。使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[checkOsAccountTestable](#ZH-CN_TOPIC_0000002522081590__checkosaccounttestable9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前账号为测试账号；返回false表示当前账号非测试账号。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  accountManager.isTestOsAccount().then((isTestable: boolean) => {
    console.info('isTestOsAccount successfully, isTestable: ' + isTestable);
  }).catch((err: BusinessError) => {
    console.error(`isTestOsAccount failed, code is ${err.code}, message is ${err.message}`);
});
```

#### isOsAccountVerified(deprecated)

isOsAccountVerified(callback: AsyncCallback<boolean>): void

检查当前系统账号是否已验证。使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[checkOsAccountVerified](#ZH-CN_TOPIC_0000002522081590__checkosaccountverifieddeprecated)替代。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示指定账号已验证；返回false表示指定账号未验证。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isOsAccountVerified((err: BusinessError, isVerified: boolean) => {
  if (err) {
    console.error(`isOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('isOsAccountVerified successfully, isVerified: ' + isVerified);
  }
});
```

#### isOsAccountVerified(deprecated)

isOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void

检查指定系统账号是否已验证。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示指定账号已验证；返回false表示指定账号未验证。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.isOsAccountVerified(localId, (err: BusinessError, isVerified: boolean) => {
  if (err) {
    console.error(`isOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('isOsAccountVerified successfully, isVerified: ' + isVerified);
  }
});
```

#### isOsAccountVerified(deprecated)

isOsAccountVerified(localId?: number): Promise<boolean>

检查指定系统账号是否已验证。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 否 | 系统账号ID。不填则检查当前系统账号是否已验证，默认为-1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示指定账号已验证；返回false表示指定账号未验证。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isOsAccountVerified().then((isVerified: boolean) => {
  console.info('isOsAccountVerified successfully, isVerified: ' + isVerified);
}).catch((err: BusinessError) => {
  console.error(`isOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
});
```

#### getCreatedOsAccountsCount(deprecated)

getCreatedOsAccountsCount(callback: AsyncCallback<number>): void

获取已创建的系统账号数量。使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountCount](#ZH-CN_TOPIC_0000002522081590__getosaccountcount9)替代。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。如果获取成功，err为null，data为已创建的系统账号的数量；否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getCreatedOsAccountsCount((err: BusinessError, count: number)=>{
  if (err) {
    console.error(`getCreatedOsAccountsCount failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getCreatedOsAccountsCount successfully, count: ' + count);
  }
});
```

#### getCreatedOsAccountsCount(deprecated)

getCreatedOsAccountsCount(): Promise<number>

获取已创建的系统账号数量。使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountCount](#ZH-CN_TOPIC_0000002522081590__getosaccountcount9-1)替代。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回已创建的系统账号的数量。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getCreatedOsAccountsCount().then((count: number) => {
  console.info('getCreatedOsAccountsCount successfully, count: ' + count);
}).catch((err: BusinessError) => {
  console.error(`getCreatedOsAccountsCount failed, code is ${err.code}, message is ${err.message}`);
});
```

#### getOsAccountLocalIdFromProcess(deprecated)

getOsAccountLocalIdFromProcess(callback: AsyncCallback<number>): void

获取当前进程所属的系统账号ID。使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalId](#ZH-CN_TOPIC_0000002522081590__getosaccountlocalid9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。如果获取成功，err为null，data为当前进程所属的系统账号ID；否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountLocalIdFromProcess((err: BusinessError, localId: number) => {
  if (err) {
    console.error(`getOsAccountLocalIdFromProcess failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getOsAccountLocalIdFromProcess id:: ' + localId);
  }
});
```

#### getOsAccountLocalIdFromProcess(deprecated)

getOsAccountLocalIdFromProcess(): Promise<number>

获取当前进程所属的系统账号ID。使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalId](#ZH-CN_TOPIC_0000002522081590__getosaccountlocalid9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回当前进程所属的系统账号ID。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountLocalIdFromProcess().then((localId: number) => {
  console.info('getOsAccountLocalIdFromProcess successfully, localId: ' + localId);
}).catch((err: BusinessError) => {
  console.error(`getOsAccountLocalIdFromProcess failed, code is ${err.code}, message is ${err.message}`);
});
```

#### getOsAccountLocalIdFromUid(deprecated)

getOsAccountLocalIdFromUid(uid: number, callback: AsyncCallback<number>): void

根据uid查询对应的系统账号ID。使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalIdForUid](#ZH-CN_TOPIC_0000002522081590__getosaccountlocalidforuid9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 进程uid。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果查询成功，err为null，data为对应的系统账号ID；否则为错误对象。 |

**示例：** 查询值为12345678的uid所属的系统账号ID

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let uid: number = 12345678;
accountManager.getOsAccountLocalIdFromUid(uid, (err: BusinessError, localId: number) => {
  if (err) {
    console.error(`getOsAccountLocalIdFromUid failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getOsAccountLocalIdFromUid successfully, localId: ' + localId);
  }
});
```

#### getOsAccountLocalIdFromUid(deprecated)

getOsAccountLocalIdFromUid(uid: number): Promise<number>

根据uid查询对应的系统账号ID。使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalIdForUid](#ZH-CN_TOPIC_0000002522081590__getosaccountlocalidforuid9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uid | number | 是 | 进程uid。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回uid对应的系统账号ID。 |

**示例：** 查询值为12345678的uid所属的系统账号ID

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let uid: number = 12345678;
accountManager.getOsAccountLocalIdFromUid(uid).then((localId: number) => {
  console.info('getOsAccountLocalIdFromUid successfully, localId: ' + localId);
}).catch((err: BusinessError) => {
  console.error(`getOsAccountLocalIdFromUid failed, code is ${err.code}, message is ${err.message}`);
});
```

#### getOsAccountLocalIdFromDomain(deprecated)

getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void

根据域账号信息，获取与其关联的系统账号的账号ID。使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalIdForDomain](#ZH-CN_TOPIC_0000002522081590__getosaccountlocalidfordomain9)替代。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainInfo | DomainAccountInfo | 是 | 域账号信息。 |
| callback | AsyncCallback<number> | 是 | 回调函数，如果获取成功，err为null，data为域账号关联的系统账号ID；否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountLocalIdFromDomain(domainInfo, (err: BusinessError, localId: number) => {
  if (err) {
    console.error(`getOsAccountLocalIdFromDomain failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getOsAccountLocalIdFromDomain successfully, localId: ' + localId);
  }
});
```

#### getOsAccountLocalIdFromDomain(deprecated)

getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo): Promise<number>

根据域账号信息，获取与其关联的系统账号的账号ID。使用Promise异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalIdForDomain](#ZH-CN_TOPIC_0000002522081590__getosaccountlocalidfordomain9-1)替代。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainInfo | DomainAccountInfo | 是 | 域账号信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回域账号关联的系统账号ID。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
accountManager.getOsAccountLocalIdFromDomain(domainInfo).then((localId: number) => {
  console.info('getOsAccountLocalIdFromDomain successfully, localId: ' + localId);
}).catch((err: BusinessError) => {
  console.error(`getOsAccountLocalIdFromDomain failed, code is ${err.code}, message is ${err.message}`);
});
```

#### getOsAccountAllConstraints(deprecated)

getOsAccountAllConstraints(localId: number, callback: AsyncCallback<Array<string>>): void

获取指定系统账号的全部约束。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数。如果获取成功，err为null，data为指定系统账号的全部约束；否则为错误对象。 |

**示例：** 获取ID为100的系统账号的全部约束

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.getOsAccountAllConstraints(localId, (err: BusinessError, constraints: string[])=>{
  if (err) {
    console.error(`getOsAccountAllConstraints code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getOsAccountAllConstraints:' + JSON.stringify(constraints));
  }
});
```

#### getOsAccountAllConstraints(deprecated)

getOsAccountAllConstraints(localId: number): Promise<Array<string>>

获取指定系统账号的全部约束。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回指定系统账号的全部约束。 |

**示例：** 获取ID为100的系统账号的全部约束

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.getOsAccountAllConstraints(localId).then((constraints: string[]) => {
  console.info('getOsAccountAllConstraints, constraints: ' + constraints);
}).catch((err: BusinessError) => {
  console.error(`getOsAccountAllConstraints err: code is ${err.code}, message is ${err.message}`);
});
```

#### queryActivatedOsAccountIds(deprecated)

queryActivatedOsAccountIds(callback: AsyncCallback<Array<number>>): void

查询当前处于激活状态的系统账号的ID列表。使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[getActivatedOsAccountLocalIds](#ZH-CN_TOPIC_0000002522081590__getactivatedosaccountlocalids9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数。如果查询成功，err为null，data为当前处于激活状态的系统账号的ID列表；否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.queryActivatedOsAccountIds((err: BusinessError, idArray: number[]) => {
  if (err) {
    console.error(`queryActivatedOsAccountIds code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('queryActivatedOsAccountIds idArray length:' + idArray.length);
    for (let i = 0; i < idArray.length; i++) {
      console.info('activated os account id: ' + idArray[i]);
    }
});
```

#### queryActivatedOsAccountIds(deprecated)

queryActivatedOsAccountIds(): Promise<Array<number>>


从API version 8开始支持，从API version 9开始废弃。建议使用[getActivatedOsAccountLocalIds](#ZH-CN_TOPIC_0000002522081590__getactivatedosaccountlocalids9-1)替代。

查询当前处于激活状态的系统账号的ID列表。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回当前处于激活状态的系统账号的ID列表。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.queryActivatedOsAccountIds().then((idArray: number[]) => {
  console.info('queryActivatedOsAccountIds, idArray: ' + idArray);
}).catch((err: BusinessError) => {
  console.error(`queryActivatedOsAccountIds err: code is ${err.code}, message is ${err.message}`);
});
```

#### queryCurrentOsAccount(deprecated)

queryCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void

查询当前进程所属的系统账号的信息。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<OsAccountInfo> | 是 | 回调函数。如果查询成功，err为null，data为当前进程所属的系统账号信息；否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.queryCurrentOsAccount((err: BusinessError, curAccountInfo: osAccount.OsAccountInfo)=>{
  if (err) {
    console.error(`queryCurrentOsAccount code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('queryCurrentOsAccount curAccountInfo:' + JSON.stringify(curAccountInfo));
  }
});
```

#### queryCurrentOsAccount(deprecated)

queryCurrentOsAccount(): Promise<OsAccountInfo>

查询当前进程所属的系统账号的信息。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。替代方法仅向系统应用开放。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<OsAccountInfo> | Promise对象，返回当前进程所属的系统账号信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.queryCurrentOsAccount().then((accountInfo: osAccount.OsAccountInfo) => {
  console.info('queryCurrentOsAccount, accountInfo: ' + JSON.stringify(accountInfo));
}).catch((err: BusinessError) => {
  console.error(`queryCurrentOsAccount err: code is ${err.code}, message is ${err.message}`);
});
```

#### getOsAccountTypeFromProcess(deprecated)

getOsAccountTypeFromProcess(callback: AsyncCallback<OsAccountType>): void

查询当前进程所属的系统账号的账号类型。使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountType](#ZH-CN_TOPIC_0000002522081590__getosaccounttype9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<OsAccountType> | 是 | 回调函数。如果查询成功，err为null，data为当前进程所属的系统账号的账号类型；否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountTypeFromProcess((err: BusinessError, accountType: osAccount.OsAccountType) => {
  if (err) {
    console.error(`getOsAccountTypeFromProcess err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getOsAccountTypeFromProcess accountType: ' + accountType);
  }
});
```

#### getOsAccountTypeFromProcess(deprecated)

getOsAccountTypeFromProcess(): Promise<OsAccountType>

查询当前进程所属的系统账号的账号类型。使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[getOsAccountType](#ZH-CN_TOPIC_0000002522081590__getosaccounttype9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<OsAccountType> | Promise对象，返回当前进程所属的系统账号的账号类型。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountTypeFromProcess().then((accountType: osAccount.OsAccountType) => {
  console.info('getOsAccountTypeFromProcess, accountType: ' + accountType);
}).catch((err: BusinessError) => {
  console.error(`getOsAccountTypeFromProcess err: code is ${err.code}, message is ${err.message}`);
});
```

#### getDistributedVirtualDeviceId(deprecated)

getDistributedVirtualDeviceId(callback: AsyncCallback<string>): void

获取分布式虚拟设备ID。使用callback异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[queryDistributedVirtualDeviceId](#ZH-CN_TOPIC_0000002522081590__querydistributedvirtualdeviceid9)替代。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS（仅系统应用可申请）或 ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。如果获取成功，err为null，data为分布式虚拟设备ID；否则为错误对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getDistributedVirtualDeviceId((err: BusinessError, virtualID: string) => {
  if (err) {
    console.error(`getDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getDistributedVirtualDeviceId virtualID: ' + virtualID);
  }
});
```

#### getDistributedVirtualDeviceId(deprecated)

getDistributedVirtualDeviceId(): Promise<string>

获取分布式虚拟设备ID。使用Promise异步回调。


从API version 7开始支持，从API version 9开始废弃。建议使用[queryDistributedVirtualDeviceId](#ZH-CN_TOPIC_0000002522081590__querydistributedvirtualdeviceid9-1)替代。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS（仅系统应用可申请）或ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回分布式虚拟设备ID。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getDistributedVirtualDeviceId().then((virtualID: string) => {
  console.info('getDistributedVirtualDeviceId, virtualID: ' + virtualID);
}).catch((err: BusinessError) => {
  console.error(`getDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}`);
});
```

#### getOsAccountLocalIdBySerialNumber(deprecated)

getOsAccountLocalIdBySerialNumber(serialNumber: number, callback: AsyncCallback<number>): void

通过SN码查询与其关联的系统账号的账号ID。使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalIdForSerialNumber](#ZH-CN_TOPIC_0000002522081590__getosaccountlocalidforserialnumber9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serialNumber | number | 是 | 账号SN码。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果查询成功，err为null，data为与SN码关联的系统账号的账号ID；否则为错误对象。 |

**示例：** 查询与SN码12345关联的系统账号的ID

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let serialNumber: number = 12345;
accountManager.getOsAccountLocalIdBySerialNumber(serialNumber, (err: BusinessError, localId: number)=>{
  if (err) {
    console.error(`get localId code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('get localId:' + localId + ' by serialNumber: ' + serialNumber);
  }
});
```

#### getOsAccountLocalIdBySerialNumber(deprecated)

getOsAccountLocalIdBySerialNumber(serialNumber: number): Promise<number>

通过SN码查询与其关联的系统账号的账号ID。使用Promise异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[getOsAccountLocalIdForSerialNumber](#ZH-CN_TOPIC_0000002522081590__getosaccountlocalidforserialnumber9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serialNumber | number | 是 | 账号SN码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回与SN码关联的系统账号的账号ID。 |

**示例：** 查询与SN码12345关联的系统账号的ID

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let serialNumber: number = 12345;
accountManager.getOsAccountLocalIdBySerialNumber(serialNumber).then((localId: number) => {
  console.info('getOsAccountLocalIdBySerialNumber localId: ' + localId);
}).catch((err: BusinessError) => {
  console.error(`getOsAccountLocalIdBySerialNumber err: code is ${err.code}, message is ${err.message}`);
});
```

#### getSerialNumberByOsAccountLocalId(deprecated)

getSerialNumberByOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void

通过系统账号ID获取与该系统账号关联的SN码。使用callback异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[getSerialNumberForOsAccountLocalId](#ZH-CN_TOPIC_0000002522081590__getserialnumberforosaccountlocalid9)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |
| callback | AsyncCallback<number> | 是 | 回调函数。如果获取成功，err为null，data为与该系统账号关联的SN码；否则为错误对象。 |

**示例：** 获取ID为100的系统账号关联的SN码

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.getSerialNumberByOsAccountLocalId(localId, (err: BusinessError, serialNumber: number)=>{
  if (err) {
    console.error(`get serialNumber code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('get serialNumber:' + serialNumber + ' by localId: ' + localId);
  }
});
```

#### getSerialNumberByOsAccountLocalId(deprecated)

getSerialNumberByOsAccountLocalId(localId: number): Promise<number>

通过系统账号ID获取与该系统账号关联的SN码。使用Promise异步回调。


从API version 8开始支持，从API version 9开始废弃。建议使用[getSerialNumberForOsAccountLocalId](#ZH-CN_TOPIC_0000002522081590__getserialnumberforosaccountlocalid9-1)替代。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回与该系统账号关联的SN码。 |

**示例：** 获取ID为100的系统账号关联的SN码

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.getSerialNumberByOsAccountLocalId(localId).then((serialNumber: number) => {
  console.info('getSerialNumberByOsAccountLocalId serialNumber: ' + serialNumber);
}).catch((err: BusinessError) => {
  console.error(`getSerialNumberByOsAccountLocalId err: code is ${err.code}, message is ${err.message}`);
});
```

#### getOsAccountName12+

getOsAccountName(): Promise<string>

查询调用方所属系统账号的名称。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回调用方所属系统账号的名称。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountName().then((name: string) => {
    console.info('getOsAccountName, name: ' + name);
  }).catch((err: BusinessError) => {
    console.error('getOsAccountName err: ' + err);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountName exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getForegroundOsAccountLocalId15+

getForegroundOsAccountLocalId(): Promise<number>

获取前台系统账号的ID。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回前台系统账号的ID。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getForegroundOsAccountLocalId().then((localId: number) => {
    console.info('getForegroundOsAccountLocalId, localId: ' + localId);
  }).catch((err: BusinessError) => {
    console.error(`getForegroundOsAccountLocalId err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getForegroundOsAccountLocalId exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getOsAccountDomainInfo15+

getOsAccountDomainInfo(localId: number): Promise<DomainAccountInfo>

获取指定系统账号关联的域账号信息。使用Promise异步回调。

**需要权限：** ohos.permission.GET_DOMAIN_ACCOUNTS 和 ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS，以上权限允许系统应用和企业应用进行申请。

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localId | number | 是 | 系统账号ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DomainAccountInfo> | Promise对象。返回与指定系统账号关联的域账号信息。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300003 | OS account not found. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.getOsAccountDomainInfo(localId).then((domainAccountInfo: osAccount.DomainAccountInfo) => {
  if (domainAccountInfo === null) {
    console.info('The target OS account is not a domain account.')
  } else {
    console.info('getOsAccountDomainInfo domain: ' + domainAccountInfo.domain);
    console.info('getOsAccountDomainInfo accountName: ' + domainAccountInfo.accountName);
  }
}).catch((err: BusinessError) => {
  console.error(`getOsAccountDomainInfo err: code is ${err.code}, message is ${err.message}`);
})
```

#### DomainAccountManager18+

域账号管理类。

#### updateAccountInfo18+

updateAccountInfo(oldAccountInfo: DomainAccountInfo, newAccountInfo: DomainAccountInfo): Promise<void>

修改指定域账号信息。使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS或ohos.permission.MANAGE_DOMAIN_ACCOUNTS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oldAccountInfo | DomainAccountInfo | 是 | 表示旧域账号信息。 |
| newAccountInfo | DomainAccountInfo | 是 | 表示新域账号信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300002 | The new account info is invalid. |
| 12300003 | The old account not found. |
| 12300004 | The new account already exists. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let oldDomainInfo: osAccount.DomainAccountInfo =
  {domain: 'testDomain', accountName: 'oldtestAccountName'};
let newDomainInfo: osAccount.DomainAccountInfo =
  {domain: 'testDomain', accountName: 'newtestAccountName'};
try {
  osAccount.DomainAccountManager.updateAccountInfo(oldDomainInfo, newDomainInfo).then(() => {
    console.info('updateAccountInfo, success');
  }).catch((err: BusinessError) => {
    console.error('updateAccountInfo err: ' + err);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`updateAccountInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

#### OsAccountInfo

表示系统账号信息。

**系统能力：** SystemCapability.Account.OsAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| localId | number | 否 | 否 | 系统账号ID。 |
| localName | string | 否 | 否 | 系统账号名称。 |
| type | OsAccountType | 否 | 否 | 系统账号类型。 |
| constraints | Array<string> | 否 | 否 | 系统账号约束，默认为空。 |
| isVerified(deprecated) | boolean | 否 | 否 | 账号是否验证。true表示指定账号已验证；false表示指定账号未验证。 **说明：**从API version 7开始支持，从API version 11开始废弃，建议使用isUnlocked。 |
| isUnlocked11+ | boolean | 否 | 否 | 账号是否已解锁（EL2级别目录是否解密）。true表示指定账号已解锁；false表示指定账号未解锁。 |
| photo8+ | string | 否 | 否 | 系统账号头像，默认为空。 |
| createTime8+ | number | 否 | 否 | 系统账号创建时间。 |
| lastLoginTime8+ | number | 否 | 否 | 系统账号最后一次登录时间，默认为空。 |
| serialNumber8+ | number | 否 | 否 | 系统账号SN码。 |
| isActived(deprecated) | boolean | 否 | 否 | 系统账号激活状态。true表示指定账号处于激活状态；false表示指定账号处于未激活状态。 **说明：**从API version 7开始支持，从API version 11开始废弃，建议使用isActivated。 |
| isActivated11+ | boolean | 否 | 否 | 系统账号是否激活。true表示指定账号已激活；false表示指定账号未激活。 |
| isCreateCompleted8+ | boolean | 否 | 否 | 系统账号创建是否完整。true表示指定账号已创建完整；false表示指定账号未创建完整。 |
| distributedInfo | distributedAccount.DistributedInfo | 否 | 否 | 分布式账号信息，默认为空。 |
| domainInfo8+ | DomainAccountInfo | 否 | 否 | 域账号信息，默认为空。 |

#### DomainAccountInfo8+

表示域账号信息。

**系统能力：** SystemCapability.Account.OsAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| domain | string | 否 | 否 | 域名。 |
| accountName | string | 否 | 否 | 域账号名。 |
| serverConfigId18+ | string | 否 | 是 | 域账号配置ID，默认为空字符串。 |

#### DomainServerConfig18+

域服务器配置。

**系统能力：** SystemCapability.Account.OsAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| parameters | Record<string, Object> | 否 | 否 | 服务器配置参数。 |
| id | string | 否 | 否 | 服务器配置标识。 |
| domain | string | 否 | 否 | 服务器所属的域。 |

#### DomainServerConfigManager18+

域服务器配置管理类。

#### addServerConfig18+

static addServerConfig(parameters: Record<string, Object>): Promise<DomainServerConfig>

添加域服务器配置。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameters | Record<string, Object> | 是 | 表示域服务器配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DomainServerConfig> | Promise对象，返回新添加的域服务器配置。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid server config parameters. |
| 12300211 | Server unreachable. |
| 12300213 | Server config already exists. |
| 12300215 | The number of server config reaches the upper limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add server configuration successfully, the return config: ' + JSON.stringify(serverConfig));
}).catch((err: BusinessError) => {
  console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
});
```

#### removeServerConfig18+

static removeServerConfig(configId: string): Promise<void>

删除域服务器配置。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configId | string | 是 | 表示服务器配置标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300212 | Server config not found. |
| 12300214 | Server config has been associated with an account. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
  osAccount.DomainServerConfigManager.removeServerConfig(serverConfig.id);
  console.info('remove domain server configuration successfully');
}).catch((err: BusinessError) => {
  console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
});
```

#### updateServerConfig18+

static updateServerConfig(configId: string, parameters: Record<string, Object>): Promise<DomainServerConfig>

更新域服务器配置。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configId | string | 是 | 表示服务器配置标识。 |
| parameters | Record<string, Object> | 是 | 表示域服务器配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DomainServerConfig> | Promise对象，返回更新后的域服务器配置。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid server config parameters. |
| 12300211 | Server unreachable. |
| 12300212 | Server config not found. |
| 12300213 | Server config already exists. |
| 12300214 | Server config has been associated with an account. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
  osAccount.DomainServerConfigManager.updateServerConfig(serverConfig.id, configParams).then((data) => {
    console.info('update domain server configuration successfully, return config: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`update domain server configuration failed, code is ${err.code}, message is ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
});
```

#### getServerConfig18+

static getServerConfig(configId: string): Promise<DomainServerConfig>

获取域服务器配置。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configId | string | 是 | 表示服务器配置标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DomainServerConfig> | Promise对象，返回获取的域服务器配置。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300212 | Server config not found. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
  osAccount.DomainServerConfigManager.getServerConfig(serverConfig.id).then((data: osAccount.DomainServerConfig) => {
    console.info('get domain server configuration successfully, return config: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`get domain server configuration failed, code is ${err.code}, message is ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
});
```

#### getAllServerConfigs18+

static getAllServerConfigs(): Promise<Array<DomainServerConfig>>

获取所有域服务器配置。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<DomainServerConfig>> | Promise对象，返回获取的所有域服务器配置。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
  osAccount.DomainServerConfigManager.getAllServerConfigs().then((data: Array<osAccount.DomainServerConfig>) => {
    console.info('get all domain server configuration successfully, return config: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`get all domain server configuration failed, code is ${err.code}, message is ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
});
```

#### getAccountServerConfig18+

static getAccountServerConfig(domainAccountInfo: DomainAccountInfo): Promise<DomainServerConfig>

获取目标域账号的服务器配置。使用Promise异步回调。

**系统能力：** SystemCapability.Account.OsAccount

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainAccountInfo | DomainAccountInfo | 是 | 表示目标域账号信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DomainServerConfig> | Promise对象，返回目标账号的域服务器配置。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300003 | Domain account not found. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let accountInfo: osAccount.DomainAccountInfo = {
  'accountName': 'demoName',
  'domain': 'demoDomain'
};
osAccount.DomainServerConfigManager.getAccountServerConfig(accountInfo).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('get account server configuration successfully, the return config: ' + JSON.stringify(serverConfig));
}).catch((err: BusinessError) => {
  console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
});
```

#### 系统账号约束列表

| 约束 | 说明 |
| --- | --- |
| constraint.wifi | 禁止使用Wi-Fi |
| constraint.wifi.set | 禁止配置Wi-Fi |
| constraint.locale.set | 禁止配置设备语言 |
| constraint.app.accounts | 禁止添加和删除应用账号 |
| constraint.apps.install | 禁止安装应用 |
| constraint.apps.uninstall | 禁止卸载应用 |
| constraint.location.shared | 禁止打开位置共享 |
| constraint.unknown.sources.install | 禁止安装未知来源的应用 |
| constraint.global.unknown.app.install | 禁止所有用户安装未知来源的应用 |
| constraint.bluetooth.set | 禁止配置蓝牙 |
| constraint.bluetooth | 禁止使用蓝牙 |
| constraint.bluetooth.share | 禁止共享使用蓝牙 |
| constraint.usb.file.transfer | 禁止通过USB传输文件 |
| constraint.credentials.set | 禁止配置用户凭据 |
| constraint.os.account.remove | 禁止删除用户 |
| constraint.managed.profile.remove | 禁止删除此用户的托管配置文件 |
| constraint.debug.features.use | 禁止启用或访问调试功能 |
| constraint.vpn.set | 禁止配置VPN |
| constraint.date.time.set | 禁止配置日期时间和时区 |
| constraint.tethering.config | 禁止配置Tethering |
| constraint.network.reset | 禁止重置网络设置 |
| constraint.factory.reset | 禁止出厂设置 |
| constraint.os.account.create | 禁止创建新用户 |
| constraint.add.managed.profile | 禁止添加托管配置文件 |
| constraint.apps.verify.disable | 强制应用程序验证 |
| constraint.cell.broadcasts.set | 禁止配置小区广播 |
| constraint.mobile.networks.set | 禁止配置移动网络 |
| constraint.control.apps | 禁止在设置或启动模块中修改应用程序 |
| constraint.physical.media | 禁止装载物理外部介质 |
| constraint.microphone | 禁止使用麦克风 |
| constraint.microphone.unmute | 禁止取消麦克风静音 |
| constraint.volume.adjust | 禁止调整音量 |
| constraint.calls.outgoing | 禁止拨打外呼电话 |
| constraint.sms.use | 禁止发送或接收短信 |
| constraint.fun | 禁止享受乐趣 |
| constraint.windows.create | 禁止创建应用程序窗口以外的窗口 |
| constraint.system.error.dialogs | 禁止显示崩溃或无响应应用程序的系统错误对话框 |
| constraint.cross.profile.copy.paste | 禁止通过将数据粘贴到其他用户或配置文件来导出剪贴板内容 |
| constraint.beam.outgoing | 禁止使用NFC从应用程序传送数据 |
| constraint.wallpaper | 禁止管理壁纸 |
| constraint.safe.boot | 禁止进入安全引导模式 |
| constraint.parent.profile.app.linking | 禁止父配置文件中的应用程序处理来自托管配置文件的Web链接 |
| constraint.audio.record | 禁止录制音频 |
| constraint.camera.use | 禁止使用摄像机 |
| constraint.os.account.background.run | 禁止在后台运行 |
| constraint.data.roam | 禁止漫游通话时使用蜂窝数据 |
| constraint.os.account.set.icon | 禁止修改用户头像 |
| constraint.wallpaper.set | 禁止设置壁纸 |
| constraint.oem.unlock | 禁止启用oem解锁 |
| constraint.device.unmute | 禁止取消设备静音 |
| constraint.password.unified | 禁止托管配置文件与主用户进行统一锁屏质询 |
| constraint.autofill | 禁止使用自动填充服务 |
| constraint.content.capture | 禁止捕获用户屏幕 |
| constraint.content.suggestions | 禁止接收内容建议 |
| constraint.os.account.activate | 禁止前台启动用户 |
| constraint.location.set | 禁止配置位置服务 |
| constraint.airplane.mode.set | 禁止飞行模式 |
| constraint.brightness.set | 禁止配置亮度 |
| constraint.share.into.profile | 禁止将主要用户的文件/图片/数据共享到托管配置文件中 |
| constraint.ambient.display | 禁止显示环境 |
| constraint.screen.timeout.set | 禁止配置屏幕关闭的超时 |
| constraint.print | 禁止打印 |
| constraint.private.dns.set | 禁止配置专用DNS |