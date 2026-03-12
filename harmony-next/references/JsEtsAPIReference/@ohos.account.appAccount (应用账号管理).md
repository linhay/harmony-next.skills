# @ohos.account.appAccount (应用账号管理)

本模块提供应用账号信息的添加、删除、修改和查询基础能力，并支持应用间鉴权和分布式数据同步功能。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { appAccount } from '@kit.BasicServicesKit';
```

#### appAccount.createAppAccountManager

createAppAccountManager(): AppAccountManager

创建应用账号管理器对象。

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

类型说明[AppAccountManager](#ZH-CN_TOPIC_0000002497605500__appaccountmanager)应用账号管理器对象。

**示例：**

```ets
let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
```

#### AppAccountManager

应用账号管理器，可用于管理应用自身的账号信息。

#### createAccount9+

createAccount(name: string, callback: AsyncCallback<void>): void

根据账号名创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。callbackAsyncCallback<void>是回调函数。当创建成功时，err为null，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name.12300004Account already exists.12300007The number of accounts reaches the upper limit.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.createAccount('WangWu', (err: BusinessError) => {
    if (err) {
      console.error(`createAccount code: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('createAccount successful.');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createAccount err: code is ${err.code}, message is ${err.message}`);
}
```

#### createAccount9+

createAccount(name: string, options: CreateAccountOptions, callback: AsyncCallback<void>): void

根据账号名和可选项创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。options[CreateAccountOptions](#ZH-CN_TOPIC_0000002497605500__createaccountoptions9)是创建应用账号的选项，可提供自定义数据，但不建议包含敏感数据（如密码、Token等）。callbackAsyncCallback<void>是回调函数。当创建成功时，err为null，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or options.12300004Account already exists.12300007The number of accounts reaches the upper limit.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.CreateAccountOptions = {
  customData: {
    age: '10'
  }
}
try {
  appAccountManager.createAccount('LiSi', options, (err: BusinessError) => {
    if (err) {
      console.error(`createAccount failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('createAccount successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

#### createAccount9+

createAccount(name: string, options?: CreateAccountOptions): Promise<void>

根据账号名和可选项创建应用账号。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。options[CreateAccountOptions](#ZH-CN_TOPIC_0000002497605500__createaccountoptions9)否创建应用账号的选项，可提供自定义数据，但不建议包含敏感数据（如密码、Token等）。不填无影响，默认为空，表示创建的该账号无额外信息需要添加。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or options.12300004Account already exists.12300007The number of accounts reaches the upper limit.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.CreateAccountOptions = {
  customData: {
    age: '10'
  }
}
try {
  appAccountManager.createAccount('LiSi', options).then(() => {
    console.info('createAccount successfully');
  }).catch((err: BusinessError) => {
    console.error(`createAccount failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

#### createAccountImplicitly9+

createAccountImplicitly(owner: string, callback: AuthCallback): void

根据指定的账号所有者隐式地创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明ownerstring是应用账号所有者的包名。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是认证器回调对象，返回创建结果。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid owner.12300007The number of accounts reaches the upper limit.12300010Account service busy.12300113Authenticator service not found.12300114Authenticator service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, result?: appAccount.AuthResult): void {
    console.info('resultCode: ' + code);
    console.info('result: ' + JSON.stringify(result));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    try {
      appAccountManager.createAccountImplicitly('com.example.accountjsdemo', {
        onResult: this.onResultCallback,
        onRequestRedirected: this.onRequestRedirectedCallback
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`createAccountImplicitly exception: code is ${err.code}, message is ${err.message}`);
    }
  }
  build() {}
}
```

#### createAccountImplicitly9+

createAccountImplicitly(owner: string, options: CreateAccountImplicitlyOptions, callback: AuthCallback): void

根据指定的账号所有者和可选项隐式地创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明ownerstring是应用账号所有者的包名。options[CreateAccountImplicitlyOptions](#ZH-CN_TOPIC_0000002497605500__createaccountimplicitlyoptions9)是隐式创建账号的选项。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是认证器回调对象，返回创建结果。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid owner or options.12300007The number of accounts reaches the upper limit.12300010Account service busy.12300113Authenticator service not found.12300114Authenticator service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, result?: appAccount.AuthResult): void {
    console.info('resultCode: ' + code);
    console.info('result: ' + JSON.stringify(result));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    let options: appAccount.CreateAccountImplicitlyOptions = {
      authType: 'getSocialData',
      requiredLabels: ['student']
    };
    try {
      appAccountManager.createAccountImplicitly('com.example.accountjsdemo', options, {
        onResult: this.onResultCallback,
        onRequestRedirected: this.onRequestRedirectedCallback
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`createAccountImplicitly exception: code is ${err.code}, message is ${err.message}`);
    }
  }
  build() {}
}
```

#### removeAccount9+

removeAccount(name: string, callback: AsyncCallback<void>): void

删除应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。callbackAsyncCallback<void>是回调函数。当删除成功时，err为null，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name.12300003Account not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.removeAccount('ZhaoLiu', (err: BusinessError) => {
    if (err) {
      console.error(`removeAccount failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('removeAccount successfully');
    }
 });
} catch (e) {
  const err = e as BusinessError;
  console.error(`removeAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

#### removeAccount9+

removeAccount(name: string): Promise<void>

删除应用账号。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name.12300003Account not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.removeAccount('Lisi').then(() => {
    console.info('removeAccount successfully');
  }).catch((err: BusinessError) => {
    console.error(`removeAccount failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`removeAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

#### setAppAccess9+

setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void

设置指定应用对特定账号的访问权限。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。bundleNamestring是第三方应用的包名。isAccessibleboolean是是否可访问。true表示允许访问，false表示禁止访问。callbackAsyncCallback<void>是回调函数，如果设置成功，err为null，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or bundleName.12300003Account not found.12400005The size of authorization list reaches the upper limit.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAppAccess('ZhangSan', 'com.example.accountjsdemo', true, (err: BusinessError) => {
    if (err) {
      console.error(`setAppAccess failed: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setAppAccess successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAppAccess exception: code is ${err.code}, message is ${err.message}`);
}
```

#### setAppAccess9+

setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>

设置指定应用对特定账号的数据访问权限。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。bundleNamestring是第三方应用的包名。isAccessibleboolean是是否可访问。true表示允许访问，false表示禁止访问。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or bundleName.12300003Account not found.12400005The size of authorization list reaches the upper limit.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAppAccess('ZhangSan', 'com.example.accountjsdemo', true).then(() => {
    console.info('setAppAccess successfully');
  }).catch((err: BusinessError) => {
    console.error(`setAppAccess failed: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAppAccess exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkAppAccess9+

checkAppAccess(name: string, bundleName: string, callback: AsyncCallback<boolean>): void

检查指定应用对特定账号的数据是否可访问。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。bundleNamestring是第三方应用的包名。callbackAsyncCallback<boolean>是回调函数。返回true表示指定应用可访问特定账号的数据；返回false表示不可访问。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or bundleName.12300003Account not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkAppAccess('ZhangSan', 'com.example.accountjsdemo',
    (err: BusinessError, isAccessible: boolean) => {
      if (err) {
        console.error(`checkAppAccess failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('checkAppAccess successfully');
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAppAccess exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkAppAccess9+

checkAppAccess(name: string, bundleName: string): Promise<boolean>

检查指定应用对特定账号的数据是否可访问。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。bundleNamestring是第三方应用的包名。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示指定应用可访问特定账号的数据；返回false表示不可访问。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or bundleName.12300003Account not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkAppAccess('ZhangSan', 'com.example.accountjsdemo').then((isAccessible: boolean) => {
    console.info('checkAppAccess successfully, isAccessible: ' + isAccessible);
  }).catch((err: BusinessError) => {
    console.error(`checkAppAccess failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAppAccess exception: code is ${err.code}, message is ${err.message}`);
}
```

#### setDataSyncEnabled9+

setDataSyncEnabled(name: string, isEnabled: boolean, callback: AsyncCallback<void>): void

开启或禁止指定应用账号的数据同步功能。使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。isEnabledboolean是是否开启数据同步。true表示开启数据同步，false表示关闭数据同步。callbackAsyncCallback<void>是回调函数。当开启或禁止成功时，err为null，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name.12300003Account not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    appAccountManager.setDataSyncEnabled('ZhangSan', true, (err: BusinessError) => {
        console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
    });
} catch (e) {
    const err = e as BusinessError;
    console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
}
```

#### setDataSyncEnabled9+

setDataSyncEnabled(name: string, isEnabled: boolean): Promise<void>

开启或禁止指定应用账号的数据同步功能。使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。isEnabledboolean是是否开启数据同步。true表示开启数据同步，false表示关闭数据同步。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name.12300003Account not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    appAccountManager.setDataSyncEnabled('ZhangSan', true).then(() => {
        console.info('setDataSyncEnabled Success');
    }).catch((err: BusinessError) => {
        console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
    });
} catch (e) {
    const err = e as BusinessError;
    console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
}
```

#### checkDataSyncEnabled9+

checkDataSyncEnabled(name: string, callback: AsyncCallback<boolean>): void

检查指定应用账号是否开启数据同步功能。使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。callbackAsyncCallback<boolean>是回调函数。返回true表示指定应用账号已开启数据同步功能；返回false表示未开启。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name.12300003Account not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkDataSyncEnabled('ZhangSan', (err: BusinessError, isEnabled: boolean) => {
    if (err) {
      console.error(`checkDataSyncEnabled failed, err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkDataSyncEnabled successfully, isEnabled: ' + isEnabled);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
}
```

#### checkDataSyncEnabled9+

checkDataSyncEnabled(name: string): Promise<boolean>

检查指定应用账号是否开启数据同步功能。使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示指定应用账号已开启数据同步功能；返回false表示未开启。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name.12300003Account not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkDataSyncEnabled('ZhangSan').then((isEnabled: boolean) => {
      console.info('checkDataSyncEnabled successfully, isEnabled: ' + isEnabled);
  }).catch((err: BusinessError) => {
    console.error(`checkDataSyncEnabled failed, err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
}
```

#### setCredential9+

setCredential(name: string, credentialType: string, credential: string,callback: AsyncCallback<void>): void

设置指定应用账号的凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。credentialTypestring是凭据类型。credentialstring是凭据取值。callbackAsyncCallback<void>是回调函数。当凭据设置成功时，err为null，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, credentialType or credential.12300003Account not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setCredential('ZhangSan', 'PIN_SIX', 'xxxxxx', (err: BusinessError) => {
    if (err) {
      console.error(`setCredential failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setCredential successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

#### setCredential9+

setCredential(name: string, credentialType: string, credential: string): Promise<void>

设置指定应用账号的凭据。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。credentialTypestring是凭据类型。credentialstring是凭据取值。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, credentialType or credential.12300003Account not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setCredential('ZhangSan', 'PIN_SIX', 'xxxxxx').then(() => {
    console.info('setCredential successfully');
  }).catch((err: BusinessError) => {
    console.error(`setCredential failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getCredential9+

getCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void

获取指定应用账号的凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。credentialTypestring是凭据类型。callbackAsyncCallback<string>是回调函数。当获取凭据成功时，err为null，data为指定应用账号的凭据；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or credentialType.12300003Account not found.12300102Credential not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getCredential('ZhangSan', 'PIN_SIX', (err: BusinessError, result: string) => {
    if (err) {
      console.error(`getCredential failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getCredential successfully, result: ' + result);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCredential err: code is ${err.code}, message is ${err.message}`);
}
```

#### getCredential9+

getCredential(name: string, credentialType: string): Promise<string>

获取指定应用账号的凭据。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。credentialTypestring是凭据类型。

**返回值：**

类型说明Promise<string>Promise对象，返回指定应用账号的凭据。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or credentialType.12300003Account not found.12300102Credential not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getCredential('ZhangSan', 'PIN_SIX').then((credential: string) => {
    console.info('getCredential successfully, credential: ' + credential);
  }).catch((err: BusinessError) => {
    console.error(`getCredential failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

#### setCustomData9+

setCustomData(name: string, key: string, value: string, callback: AsyncCallback<void>): void

设置指定应用账号的自定义数据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。keystring是自定义数据的键名。valuestring是自定义数据的取值。callbackAsyncCallback<void>是回调函数。当设置自定义数据成功时，err为null，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, key or value.12300003Account not found.12400003The number of custom data reaches the upper limit.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setCustomData('ZhangSan', 'age', '12', (err: BusinessError) => {
    if (err) {
      console.error(`setCustomData failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setCustomData successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setCustomData exception: code is ${err.code}, message is ${err.message}`);
}
```

#### setCustomData9+

setCustomData(name: string, key: string, value: string): Promise<void>

设置指定应用账号的自定义数据。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。keystring是自定义数据的键名。valuestring是自定义数据的取值。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, key or value.12300003Account not found.12400003The number of custom data reaches the upper limit.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setCustomData('ZhangSan', 'age', '12').then(() => {
    console.info('setCustomData successfully');
  }).catch((err: BusinessError) => {
    console.error(`setCustomData failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setCustomData exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getCustomData9+

getCustomData(name: string, key: string, callback: AsyncCallback<string>): void

根据指定键名获取特定应用账号的自定义数据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。keystring是自定义数据的键名。callbackAsyncCallback<string>是回调函数。当获取成功时，err为null，data为自定义数据的取值；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or key.12300003Account not found.12400002Custom data not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getCustomData('ZhangSan', 'age', (err: BusinessError, data: string) => {
    if (err) {
      console.error('getCustomData failed, error: ' + err);
    } else {
      console.info('getCustomData successfully, data: ' + data);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCustomData exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getCustomData9+

getCustomData(name: string, key: string): Promise<string>

根据指定键名获取特定应用账号的自定义数据。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。keystring是自定义数据的键名。

**返回值：**

类型说明Promise<string>Promise对象，返回自定义数据的取值。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or key.12300003Account not found.12400002Custom data not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getCustomData('ZhangSan', 'age').then((data: string) => {
    console.info('getCustomData successfully, data: ' + data);
  }).catch((err: BusinessError) => {
    console.error(`getCustomData failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCustomData exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getCustomDataSync9+

getCustomDataSync(name: string, key: string): string

根据指定键名获取特定应用账号的自定义数据。使用同步方式返回结果。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。keystring是自定义数据的键名。

**返回值：**

类型说明string自定义数据的取值。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or key.12300003Account not found.12400002Custom data not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value = appAccountManager.getCustomDataSync('ZhangSan', 'age');
  console.info('getCustomDataSync successfully, value: ' + value);
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCustomDataSync failed, code is ${err.code}, message is ${err.message}`);
}
```

#### getAllAccounts9+

getAllAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void

获取所有可访问的应用账号信息。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>是回调函数。当查询成功时，err为null，data为获取到的应用账号信息列表；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAllAccounts((err: BusinessError, data: appAccount.AppAccountInfo[]) => {
    if (err) {
      console.error(`getAllAccounts failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAllAccounts successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAllAccounts exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getAllAccounts9+

getAllAccounts(): Promise<Array<AppAccountInfo>>

获取所有可访问的应用账号信息。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

类型说明Promise<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>Promise对象，返回全部应用已授权账号信息对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)。

错误码ID错误信息12300001System service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAllAccounts().then((data: appAccount.AppAccountInfo[]) => {
    console.info('getAllAccounts successfully');
  }).catch((err: BusinessError) => {
    console.error(`getAllAccounts failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAllAccounts exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getAccountsByOwner9+

getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void

根据应用账号所有者获取调用方可访问的应用账号列表。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明ownerstring是应用账号所有者的包名。callbackAsyncCallback<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>是回调函数。如果获取成功，err为null，data为获取到的应用账号列表；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid owner.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAccountsByOwner('com.example.accountjsdemo2',
    (err: BusinessError, data: appAccount.AppAccountInfo[]) => {
      if (err) {
        console.error(`getAccountsByOwner failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('getAccountsByOwner successfully, data:' + JSON.stringify(data));
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAccountsByOwner exception:code is ${err.code}, message is ${err.message}`);
}
```

#### getAccountsByOwner9+

getAccountsByOwner(owner: string): Promise<Array<AppAccountInfo>>

根据应用账号所有者获取调用方可访问的应用账号列表。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明ownerstring是应用账号所有者的包名。

**返回值：**

类型说明Promise<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>Promise对象，返回获取到的应用账号列表。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid owner.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAccountsByOwner('com.example.accountjsdemo2').then((
    data: appAccount.AppAccountInfo[]) => {
    console.info('getAccountsByOwner successfully, data: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`getAccountsByOwner failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAccountsByOwner exception: code is ${err.code}, message is ${err.message}`);
}
```

#### on('accountChange')9+

on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void

订阅指定应用的账号信息变更事件。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明type'accountChange'是事件回调类型，支持的事件为'accountChange'，当目标应用更新账号信息时，触发该事件。ownersArray<string>是应用账号所有者的包名列表。callbackCallback<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>是需要注册的回调函数，返回信息为发生变更的应用账号列表。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid type or owners.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
  console.info('receive change data:' + JSON.stringify(data));
}

try {
  appAccountManager.on('accountChange', ['com.example.actsaccounttest'], changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`on accountChange failed, code is ${err.code}, message is ${err.message}`);
}
```

#### off('accountChange')9+

off(type: 'accountChange', callback?: Callback<Array<AppAccountInfo>>): void

取消订阅账号信息变更事件。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明type'accountChange'是事件回调类型，支持的事件为'accountChange'，当账号所有者更新账号信息时，触发该事件。callbackCallback<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>否需要注销的回调函数，默认为空，表示取消该类型事件所有的回调。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid type.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
  console.info('receive change data:' + JSON.stringify(data));
}

try {
  appAccountManager.on('accountChange', ['com.example.actsaccounttest'], changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`on accountChange failed, code is ${err.code}, message is ${err.message}`);
}
try {
  appAccountManager.off('accountChange', changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`off accountChange failed, code is ${err.code}, message is ${err.message}`);
}
```

#### auth9+

auth(name: string, owner: string, authType: string, callback: AuthCallback): void

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。authTypestring是鉴权类型。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是回调对象，返回鉴权结果。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, owner or authType.12300003Account not found.12300010Account service busy.12300113Authenticator service not found.12300114Authenticator service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, authResult?: appAccount.AuthResult): void {
    console.info('resultCode: ' + code);
    console.info('authResult: ' + JSON.stringify(authResult));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    try {
      appAccountManager.auth('LiSi', 'com.example.accountjsdemo', 'getSocialData', {
        onResult: this.onResultCallback,
        onRequestRedirected: this.onRequestRedirectedCallback
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`auth exception: code is ${err.code}, message is ${err.message}`);
    }
  }

  build() {}
}
```

#### auth9+

auth(name: string, owner: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。authTypestring是鉴权类型。optionsRecord<string, Object>是鉴权所需的可选项。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是回调对象，返回鉴权结果。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, owner, authType or options.12300003Account not found.12300010Account service busy.12300113Authenticator service not found.12300114Authenticator service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, authResult?: appAccount.AuthResult): void {
    console.info('resultCode: ' + code);
    console.info('authResult: ' + JSON.stringify(authResult));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    let options: Record<string, Object> = {
      'password': 'xxxx',
    };
    try {
      appAccountManager.auth('LiSi', 'com.example.accountjsdemo', 'getSocialData', options, {
        onResult: this.onResultCallback,
        onRequestRedirected: this.onRequestRedirectedCallback
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`auth exception: code is ${err.code}, message is ${err.message}`);
    }
  }

  build() {}
}
```

#### getAuthToken9+

getAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void

获取指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。authTypestring是鉴权类型。callbackAsyncCallback<string>是回调函数。当获取成功时，err为null，data为授权令牌值；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, owner or authType.12300003Account not found.12300107AuthType not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData',
    (err: BusinessError, token: string) => {
      if (err) {
        console.error(`getAuthToken failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('getAuthToken successfully, token: ' + token);
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getAuthToken9+

getAuthToken(name: string, owner: string, authType: string): Promise<string>

获取指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。authTypestring是鉴权类型。

**返回值：**

类型说明Promise<string>Promise对象，返回授权令牌。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, owner or authType.12300003Account not found.12300107AuthType not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData').then((token: string) => {
    console.info('getAuthToken successfully, token: ' + token);
  }).catch((err: BusinessError) => {
    console.error(`getAuthToken failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

#### setAuthToken9+

setAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void

为指定应用账号设置特定鉴权类型的授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。tokenstring是授权令牌。callbackAsyncCallback<void>是回调函数。当设置成功时，err为null；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, authType or token.12300003Account not found.12400004The number of tokens reaches the upper limit.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthToken('LiSi', 'getSocialData', 'xxxx', (err: BusinessError) => {
    if (err) {
      console.error(`setAuthToken failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setAuthToken successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

#### setAuthToken9+

setAuthToken(name: string, authType: string, token: string): Promise<void>

为指定应用账号设置特定鉴权类型的授权令牌。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。tokenstring是授权令牌。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, authType or token.12300003Account not found.12400004The number of tokens reaches the upper limit.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthToken('LiSi', 'getSocialData', 'xxxx').then(() => {
    console.info('setAuthToken successfully');
  }).catch((err: BusinessError) => {
    console.error(`setAuthToken failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

#### deleteAuthToken9+

deleteAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void

删除指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。authTypestring是鉴权类型。tokenstring是授权令牌。如果授权令牌不存在，则不执行任何操作。callbackAsyncCallback<void>是回调函数。当删除成功时，err为null；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, owner, authType or token.12300003Account not found.12300107AuthType not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.deleteAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx',
    (err: BusinessError) => {
      if (err) {
        console.error(`deleteAuthToken failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('deleteAuthToken successfully');
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

#### deleteAuthToken9+

deleteAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>

删除指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。authTypestring是鉴权类型。tokenstring是授权令牌。如果授权令牌不存在，则不执行任何操作。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, owner, authType or token.12300003Account not found.12300107AuthType not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.deleteAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx').then(() => {
    console.info('deleteAuthToken successfully');
  }).catch((err: BusinessError) => {
    console.error(`deleteAuthToken failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

#### setAuthTokenVisibility9+

setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void>): void

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。bundleNamestring是被设置可见性的应用包名。isVisibleboolean是是否可见。true表示可见，false表示不可见。callbackAsyncCallback<void>是回调函数。当设置成功时，err为null；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, authType or bundleName.12300003Account not found.12300107AuthType not found.12400005The size of authorization list reaches the upper limit.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true,
    (err: BusinessError) => {
      if (err) {
        console.error(`setAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('setAuthTokenVisibility successfully');
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
}
```

#### setAuthTokenVisibility9+

setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。bundleNamestring是被设置可见性的应用包名。isVisibleboolean是是否可见。true表示可见，false表示不可见。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, authType or bundleName.12300003Account not found.12300107AuthType not found.12400005The size of authorization list reaches the upper limit.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true).then(() => {
    console.info('setAuthTokenVisibility successfully');
  }).catch((err: BusinessError) => {
    console.error(`setAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkAuthTokenVisibility9+

checkAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>): void

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。bundleNamestring是检查可见性的应用包名。callbackAsyncCallback<boolean>是回调函数。当检查成功时，err为null，data为true表示可见，data为false表示不可见；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, authType or bundleName.12300003Account not found.12300107AuthType not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo',
    (err: BusinessError, isVisible: boolean) => {
      if (err) {
        console.error(`checkAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('checkAuthTokenVisibility successfully, isVisible: ' + isVisible);
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkAuthTokenVisibility9+

checkAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。bundleNamestring是用于检查可见性的应用包名。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示授权令牌对指定应用的可见，返回false表示不可见。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, authType or bundleName.12300003Account not found.12300107AuthType not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo').then((
    isVisible: boolean) => {
    console.info('checkAuthTokenVisibility successfully, isVisible: ' + isVisible);
  }).catch((err: BusinessError) => {
    console.error(`checkAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getAllAuthTokens9+

getAllAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<AuthTokenInfo>>): void

获取指定账号对调用方可见的所有授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。callbackAsyncCallback<Array<[AuthTokenInfo](#ZH-CN_TOPIC_0000002497605500__authtokeninfo9)>>是回调函数。当获取成功时，err为null，data为授权令牌数组；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or owner.12300003Account not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAllAuthTokens('LiSi', 'com.example.accountjsdemo',
    (err: BusinessError, tokenArr: appAccount.AuthTokenInfo[]) => {
      if (err) {
        console.error(`getAllAuthTokens failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('getAllAuthTokens successfully, tokenArr: ' + tokenArr);
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAllAuthTokens exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getAllAuthTokens9+

getAllAuthTokens(name: string, owner: string): Promise<Array<AuthTokenInfo>>

获取指定账号对调用方可见的所有授权令牌。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。

**返回值：**

类型说明Promise<Array<[AuthTokenInfo](#ZH-CN_TOPIC_0000002497605500__authtokeninfo9)>>Promise对象，返回授权令牌数组。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or owner.12300003Account not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAllAuthTokens('LiSi', 'com.example.accountjsdemo').then((
    tokenArr: appAccount.AuthTokenInfo[]) => {
    console.info('getAllAuthTokens successfully, tokenArr: ' + JSON.stringify(tokenArr));
  }).catch((err: BusinessError) => {
    console.error(`getAllAuthTokens failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAllAuthTokens exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getAuthList9+

getAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过[setAuthTokenVisibility](#ZH-CN_TOPIC_0000002497605500__setauthtokenvisibility9)来设置）。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。callbackAsyncCallback<Array<string>>是回调函数。当获取成功时，err为null，data为被授权的包名数组；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or authType.12300003Account not found.12300107AuthType not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAuthList('LiSi', 'getSocialData', (err: BusinessError, authList: string[]) => {
    if (err) {
      console.error(`getAuthList failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAuthList successfully, authList: ' + authList);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthList exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getAuthList9+

getAuthList(name: string, authType: string): Promise<Array<string>>

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过[setAuthTokenVisibility](#ZH-CN_TOPIC_0000002497605500__setauthtokenvisibility9)来设置）。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。

**返回值：**

类型说明Promise<Array<string>>Promise对象，返回被授权的包名数组。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or authType.12300003Account not found.12300107AuthType not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAuthList('LiSi', 'getSocialData').then((authList: string[]) => {
    console.info('getAuthList successfully, authList: ' + authList);
  }).catch((err: BusinessError) => {
    console.error(`getAuthList failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthList exception: code is ${err.code}, message is ${err.message}`);
}
```

#### getAuthCallback9+

getAuthCallback(sessionId: string, callback: AsyncCallback<AuthCallback>): void

获取鉴权会话的认证器回调对象。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明sessionIdstring是鉴权会话的标识。callbackAsyncCallback<[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)>是回调函数。当获取成功时，err为null，data为鉴权会话的认证器回调对象；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid sessionId.12300108Session not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
    let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
    try {
      appAccountManager.getAuthCallback(sessionId, (err: BusinessError, callback: appAccount.AuthCallback) => {
        if (err != null) {
          console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
          return;
        }
        let result: appAccount.AuthResult = {
          account: {
            name: 'Lisi',
            owner: 'com.example.accountjsdemo',
          },
          tokenInfo: {
            token: 'xxxxxx',
            authType: 'getSocialData'
          }
        };
        callback.onResult(0, result);
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`getAuthCallback exception: code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

#### getAuthCallback9+

getAuthCallback(sessionId: string): Promise<AuthCallback>

获取鉴权会话的认证器回调对象。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明sessionIdstring是鉴权会话的标识。

**返回值：**

类型说明Promise<[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)>Promise对象，返回鉴权会话的认证器回调对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid sessionId.12300108Session not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
    let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
    try {
      appAccountManager.getAuthCallback(sessionId).then((callback: appAccount.AuthCallback) => {
      let result: appAccount.AuthResult = {
        account: {
          name: 'Lisi',
          owner: 'com.example.accountjsdemo',
        },
        tokenInfo: {
          token: 'xxxxxx',
          authType: 'getSocialData'
        }
      };
      callback.onResult(0, result);
      }).catch((err: BusinessError) => {
        console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`getAuthCallback exception: code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

#### queryAuthenticatorInfo9+

queryAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void

获取指定应用的认证器信息。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明ownerstring是应用账号所有者的包名。callbackAsyncCallback<[AuthenticatorInfo](#ZH-CN_TOPIC_0000002497605500__authenticatorinfo8)>是回调函数。当获取成功时，err为null，data为认证器信息对象；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid owner.12300113Authenticator service not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.queryAuthenticatorInfo('com.example.accountjsdemo',
    (err: BusinessError, info: appAccount.AuthenticatorInfo) => {
      if (err) {
        console.error(`queryAuthenticatorInfo failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('queryAuthenticatorInfo successfully, info: ' + JSON.stringify(info));
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryAuthenticatorInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

#### queryAuthenticatorInfo9+

queryAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>

获取指定应用的认证器信息。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明ownerstring是应用账号所有者的包名。

**返回值：**

类型说明Promise<[AuthenticatorInfo](#ZH-CN_TOPIC_0000002497605500__authenticatorinfo8)>Promise对象，返回指定应用的认证器信息对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid owner.12300113Authenticator service not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.queryAuthenticatorInfo('com.example.accountjsdemo').then((
    info: appAccount.AuthenticatorInfo) => {
    console.info('queryAuthenticatorInfo successfully, info: ' + JSON.stringify(info));
  }).catch((err: BusinessError) => {
    console.error(`queryAuthenticatorInfo failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryAuthenticatorInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkAccountLabels9+

checkAccountLabels(name: string, owner: string, labels: Array<string>, callback: AsyncCallback<boolean>): void

检查指定应用账号是否满足特定的标签集合。使用callback异步回调。该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。labelsArray<string>是标签数组。callbackAsyncCallback<boolean>是回调函数。当检查成功时，err为null，data为true表示满足特定的标签集合，data为false表示不满足；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, owner or labels.12300003Account not found.12300010Account service busy.12300113Authenticator service not found.12300114Authenticator service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let labels = ['student'];
try {
  appAccountManager.checkAccountLabels('zhangsan', 'com.example.accountjsdemo', labels,
    (err: BusinessError, hasAllLabels: boolean) => {
      if (err) {
        console.error(`checkAccountLabels failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('checkAccountLabels successfully, hasAllLabels: ' + hasAllLabels);
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAccountLabels exception: code is ${err.code}, message is ${err.message}`);
}
```

#### checkAccountLabels9+

checkAccountLabels(name: string, owner: string, labels: Array<string>): Promise<boolean>

检查指定应用账号是否满足特定的标签集合。使用Promise异步回调。该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。labelsArray<string>是标签数组。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示指定账号满足特定的标签集合，返回false表示不满足。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, owner or labels.12300003Account not found.12300010Account service busy.12300113Authenticator service not found.12300114Authenticator service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let labels = ['student'];
try {
  appAccountManager.checkAccountLabels('zhangsan', 'com.example.accountjsdemo', labels).then((
    hasAllLabels: boolean) => {
    console.info('checkAccountLabels successfully: ' + hasAllLabels);
  }).catch((err: BusinessError) => {
    console.error(`checkAccountLabels failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAccountLabels exception: code is ${err.code}, message is ${err.message}`);
}
```

#### deleteCredential9+

deleteCredential(name: string, credentialType: string, callback: AsyncCallback<void>): void

删除指定应用账号的特定类型的凭据信息。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。credentialTypestring是凭据类型。callbackAsyncCallback<void>是回调函数。当删除成功时，err为null；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or credentialType.12300003Account not found.12300102Credential not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.deleteCredential('zhangsan', 'PIN_SIX', (err: BusinessError) => {
    if (err) {
      console.error(`deleteCredential failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('deleteCredential successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

#### deleteCredential9+

deleteCredential(name: string, credentialType: string): Promise<void>

删除指定应用账号的特定类型的凭据信息。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。credentialTypestring是凭据类型。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or credentialType.12300003Account not found.12300102Credential not found.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.deleteCredential('zhangsan', 'PIN_SIX').then(() => {
    console.info('deleteCredential successfully');
  }).catch((err: BusinessError) => {
    console.error(`deleteCredential failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

#### selectAccountsByOptions9+

selectAccountsByOptions(options: SelectAccountsOptions, callback: AsyncCallback<Array<AppAccountInfo>>): void

根据选项选择调用方可访问的账号列表。使用callback异步回调。如果选项中包含标签约束，则该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明options[SelectAccountsOptions](#ZH-CN_TOPIC_0000002497605500__selectaccountsoptions9)是选择账号的选项。callbackAsyncCallback<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>是回调函数。当根据选项选择请求方可访问的账号列表时，err为null，data为可访问的账号信息对象；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid options.12300010Account service busy.12300114Authenticator service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.SelectAccountsOptions = {
  allowedOwners: ['com.example.accountjsdemo'],
  requiredLabels: ['student']
};
try {
  appAccountManager.selectAccountsByOptions(options,
    (err: BusinessError, accountArr: appAccount.AppAccountInfo[]) => {
      if (err) {
        console.error(`selectAccountsByOptions failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('selectAccountsByOptions successfully, accountArr: ' + JSON.stringify(accountArr));
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`selectAccountsByOptions exception: code is ${err.code}, message is ${err.message}`);
}
```

#### selectAccountsByOptions9+

selectAccountsByOptions(options: SelectAccountsOptions): Promise<Array<AppAccountInfo>>

根据选项选择调用方可访问的账号列表。使用Promise异步回调。如果选项中包含标签约束，则该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明options[SelectAccountsOptions](#ZH-CN_TOPIC_0000002497605500__selectaccountsoptions9)是选择账号的选项。

**返回值：**

类型说明Promise<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>Promise对象，返回调用方可访问的账号列表。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid options.12300010Account service busy.12300114Authenticator service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.SelectAccountsOptions = {
  allowedOwners: ['com.example.accountjsdemo']
};
try {
  appAccountManager.selectAccountsByOptions(options).then((accountArr: appAccount.AppAccountInfo[]) => {
    console.info('selectAccountsByOptions successfully, accountArr: ' + JSON.stringify(accountArr));
  }).catch((err: BusinessError) => {
    console.error(`selectAccountsByOptions failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`selectAccountsByOptions exception: code is ${err.code}, message is ${err.message}`);
}
```

#### verifyCredential9+

verifyCredential(name: string, owner: string, callback: AuthCallback): void

验证指定账号的凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是回调函数，返回验证结果。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name or owner.12300003Account not found.12300010Account service busy.12300113Authenticator service not found.12300114Authenticator service exception.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.verifyCredential('zhangsan', 'com.example.accountjsdemo', {
    onResult: (resultCode: number, result?: appAccount.AuthResult) => {
      console.info('verifyCredential onResult, resultCode: ' + JSON.stringify(resultCode));
      console.info('verifyCredential onResult, result: ' + JSON.stringify(result));
    },
    onRequestRedirected: (request: Want) => {
      console.info('verifyCredential onRequestRedirected, request: ' + JSON.stringify(request));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`verifyCredential err: code is ${err.code}, message is ${err.message}`);
}
```

#### verifyCredential9+

verifyCredential(name: string, owner: string, options: VerifyCredentialOptions, callback: AuthCallback): void

验证用户凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。options[VerifyCredentialOptions](#ZH-CN_TOPIC_0000002497605500__verifycredentialoptions9)是验证凭据的选项。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是回调函数，返回验证结果。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid name, owner or options.12300003Account not found.12300010Account service busy.12300113Authenticator service not found.12300114Authenticator service exception.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.VerifyCredentialOptions = {
  credentialType: 'pin',
  credential: '123456'
};
try {
  appAccountManager.verifyCredential('zhangsan', 'com.example.accountjsdemo', options, {
    onResult: (resultCode: number, result?: appAccount.AuthResult) => {
      console.info('verifyCredential onResult, resultCode: ' + JSON.stringify(resultCode));
      console.info('verifyCredential onResult, result: ' + JSON.stringify(result));
    },
    onRequestRedirected: (request: Want) => {
      console.info('verifyCredential onRequestRedirected, request: ' + JSON.stringify(request));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`verifyCredential err: code is ${err.code}, message is ${err.message}`);
}
```

#### setAuthenticatorProperties9+

setAuthenticatorProperties(owner: string, callback: AuthCallback): void

设置指定应用的认证器属性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明ownerstring是认证器的所有者的包名。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是回调函数，返回设置属性的结果。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid owner.12300010Account service busy.12300113Authenticator service not found.12300114Authenticator service exception.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthenticatorProperties('com.example.accountjsdemo', {
    onResult: (resultCode: number, result?: appAccount.AuthResult) => {
      console.info('setAuthenticatorProperties onResult, resultCode: ' + JSON.stringify(resultCode));
      console.info('setAuthenticatorProperties onResult, result: ' + JSON.stringify(result));
    },
    onRequestRedirected: (request: Want) => {
      console.info('setAuthenticatorProperties onRequestRedirected, request: ' + JSON.stringify(request));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthenticatorProperties err: code is ${err.code}, message is ${err.message}`);
}
```

#### setAuthenticatorProperties9+

setAuthenticatorProperties(owner: string, options: SetPropertiesOptions, callback: AuthCallback): void

设置认证器属性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明ownerstring是认证器的所有者的包名。options[SetPropertiesOptions](#ZH-CN_TOPIC_0000002497605500__setpropertiesoptions9)是设置属性的选项。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是认证器回调，返回设置属性的结果。

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](账号管理错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.12300001System service exception.12300002Invalid owner or options.12300010Account service busy.12300113Authenticator service not found.12300114Authenticator service exception.

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.SetPropertiesOptions = {
  properties: { prop1: 'value1' }
};
try {
  appAccountManager.setAuthenticatorProperties('com.example.accountjsdemo', options, {
    onResult: (resultCode: number, result?: appAccount.AuthResult) => {
      console.info('setAuthenticatorProperties onResult, resultCode: ' + JSON.stringify(resultCode));
      console.info('setAuthenticatorProperties onResult, result: ' + JSON.stringify(result));
    },
    onRequestRedirected: (request: Want) => {
      console.info('setAuthenticatorProperties onRequestRedirected, request: ' + JSON.stringify(request));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthenticatorProperties err: code is ${err.code}, message is ${err.message}`);
}
```

#### addAccount(deprecated)

addAccount(name: string, callback: AsyncCallback<void>): void

根据账号名添加应用账号。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[createAccount](#ZH-CN_TOPIC_0000002497605500__createaccount9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。callbackAsyncCallback<void>是回调函数。当创建成功时，err为null，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.addAccount('WangWu', (err: BusinessError) => {
  console.error(`addAccount err: code is ${err.code}, message is ${err.message}`);
});
```

#### addAccount(deprecated)

addAccount(name: string, extraInfo: string, callback: AsyncCallback<void>): void

根据账号名和额外信息添加应用账号。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[createAccount](#ZH-CN_TOPIC_0000002497605500__createaccount9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。extraInfostring是额外信息(能转换string类型的其它信息)，额外信息不能是应用账号的敏感信息（如应用账号密码、token等）。callbackAsyncCallback<void>是回调函数。当创建成功时，err为null，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.addAccount('LiSi', 'token101', (err: BusinessError) => {
  console.error(`addAccount err: code is ${err.code}, message is ${err.message}`);
});
```

#### addAccount(deprecated)

addAccount(name: string, extraInfo?: string): Promise<void>

根据账号名和额外信息添加应用账号。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[createAccount](#ZH-CN_TOPIC_0000002497605500__createaccount9-2)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。extraInfostring否额外信息(能转换string类型的其它信息)，额外信息不能是应用账号的敏感信息（如应用账号密码、token等），默认为空，表示创建的该账号无额外信息需要添加。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.addAccount('LiSi', 'token101').then(()=> {
  console.info('addAccount Success');
}).catch((err: BusinessError) => {
  console.error(`addAccount err: code is ${err.code}, message is ${err.message}`);
});
```

#### addAccountImplicitly(deprecated)

addAccountImplicitly(owner: string, authType: string, options: {[key: string]: any;}, callback: AuthenticatorCallback): void

根据指定的账号所有者隐式地添加应用账号。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[createAccountImplicitly](#ZH-CN_TOPIC_0000002497605500__createaccountimplicitly9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明ownerstring是应用账号所有者的包名。authTypestring是鉴权类型。鉴权类型为自定义。options{[key: string]: any}是鉴权所需要的可选项。可选项可根据自己需要设置。callback[AuthenticatorCallback](#ZH-CN_TOPIC_0000002497605500__authenticatorcallbackdeprecated)是认证器回调对象，返回添加结果。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, result: Record<string, Object>): void {
    console.info('resultCode: ' + code);
    console.info('result: ' + JSON.stringify(result));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    appAccountManager.addAccountImplicitly('com.example.accountjsdemo', 'getSocialData', {}, {
      onResult: this.onResultCallback,
      onRequestRedirected: this.onRequestRedirectedCallback
    });
  }

  build() {}
}
```

#### deleteAccount(deprecated)

deleteAccount(name: string, callback: AsyncCallback<void>): void

删除应用账号。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[removeAccount](#ZH-CN_TOPIC_0000002497605500__removeaccount9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。callbackAsyncCallback<void>是回调函数。当删除成功时，err为null，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.deleteAccount('ZhaoLiu', (err: BusinessError) => {
  console.error(`deleteAccount err: code is ${err.code}, message is ${err.message}`);
});
```

#### deleteAccount(deprecated)

deleteAccount(name: string): Promise<void>

删除应用账号。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[removeAccount](#ZH-CN_TOPIC_0000002497605500__removeaccount9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.deleteAccount('ZhaoLiu').then(() => {
  console.info('deleteAccount Success');
}).catch((err: BusinessError) => {
  console.error(`deleteAccount err: code is ${err.code}, message is ${err.message}`);
});
```

#### disableAppAccess(deprecated)

disableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void

禁止指定第三方应用账号名称对指定的第三方应用进行访问。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[setAppAccess](#ZH-CN_TOPIC_0000002497605500__setappaccess9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。bundleNamestring是第三方应用的包名。callbackAsyncCallback<void>是回调函数。当禁止指定第三方应用账号名称对指定包名称的第三方应用进行访问设置成功时，err为null，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.disableAppAccess('ZhangSan', 'com.example.accountjsdemo', (err: BusinessError) => {
  console.error(`disableAppAccess err: code is ${err.code}, message is ${err.message}`);
});
```

#### disableAppAccess(deprecated)

disableAppAccess(name: string, bundleName: string): Promise<void>

禁止指定第三方应用账号名称对指定包名称的第三方应用进行访问。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[setAppAccess](#ZH-CN_TOPIC_0000002497605500__setappaccess9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是要禁用访问的第三方应用账号的名称。bundleNamestring是第三方应用的包名。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.disableAppAccess('ZhangSan', 'com.example.accountjsdemo').then(() => {
  console.info('disableAppAccess Success');
}).catch((err: BusinessError) => {
  console.error(`disableAppAccess err: code is ${err.code}, message is ${err.message}`);
});
```

#### enableAppAccess(deprecated)

enableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void

允许指定第三方应用账号名称对指定包名称的第三方应用进行访问。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[setAppAccess](#ZH-CN_TOPIC_0000002497605500__setappaccess9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。bundleNamestring是第三方应用的包名。callbackAsyncCallback<void>是回调函数。当允许指定第三方应用账号名称对指定包名称的第三方应用进行访问设置成功时，err为null，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.enableAppAccess('ZhangSan', 'com.example.accountjsdemo', (err: BusinessError) => {
  if (err) {
    console.error(`enableAppAccess err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('enableAppAccess successful.');
  }
});
```

#### enableAppAccess(deprecated)

enableAppAccess(name: string, bundleName: string): Promise<void>

允许指定第三方应用账号的名称对指定包名称的第三方应用进行访问。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[setAppAccess](#ZH-CN_TOPIC_0000002497605500__setappaccess9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。bundleNamestring是第三方应用的包名。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.enableAppAccess('ZhangSan', 'com.example.accountjsdemo').then(() => {
  console.info('enableAppAccess Success');
}).catch((err: BusinessError) => {
  console.error(`enableAppAccess err: code is ${err.code}, message is ${err.message}`);
});
```

#### checkAppAccountSyncEnable(deprecated)

checkAppAccountSyncEnable(name: string, callback: AsyncCallback<boolean>): void

检查指定应用账号是否开启数据同步功能。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[checkDataSyncEnabled](#ZH-CN_TOPIC_0000002497605500__checkdatasyncenabled9)替代。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。callbackAsyncCallback<boolean>是回调函数。返回true表示指定应用账号已开启数据同步功能；返回false表示未开启。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.checkAppAccountSyncEnable('ZhangSan', (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`checkAppAccountSyncEnable code: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('checkAppAccountSyncEnable result: ' + result);
  }
});
```

#### checkAppAccountSyncEnable(deprecated)

checkAppAccountSyncEnable(name: string): Promise<boolean>

检查指定应用账号是否开启数据同步功能。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[checkDataSyncEnabled](#ZH-CN_TOPIC_0000002497605500__checkdatasyncenabled9-1)替代。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示指定应用账号已开启数据同步功能；返回false表示未开启。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.checkAppAccountSyncEnable('ZhangSan').then((data: boolean) => {
  console.info('checkAppAccountSyncEnable, result: ' + data);
}).catch((err: BusinessError) => {
  console.error(`checkAppAccountSyncEnable err: code is ${err.code}, message is ${err.message}`);
});
```

#### setAccountCredential(deprecated)

setAccountCredential(name: string, credentialType: string, credential: string,callback: AsyncCallback<void>): void

设置指定应用账号的凭据。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃，建议使用[setCredential](#ZH-CN_TOPIC_0000002497605500__setcredential9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。credentialTypestring是凭据类型。credentialstring是凭据取值。callbackAsyncCallback<void>是回调函数。当设置此应用程序账号的凭据成功时，err为null，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAccountCredential('ZhangSan', 'credentialType001', 'credential001', (err: BusinessError) => {
  if (err) {
    console.error(`setAccountCredential err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setAccountCredential successful.');
  }
});
```

#### setAccountCredential(deprecated)

setAccountCredential(name: string, credentialType: string, credential: string): Promise<void>

设置指定应用账号的凭据。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃，建议使用[setCredential](#ZH-CN_TOPIC_0000002497605500__setcredential9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。credentialTypestring是凭据类型。credentialstring是凭据取值。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAccountCredential('ZhangSan', 'credentialType001', 'credential001').then(() => {
  console.info('setAccountCredential Success');
}).catch((err: BusinessError) => {
  console.error(`setAccountCredential err: code is ${err.code}, message is ${err.message}`);
});
```

#### setAccountExtraInfo(deprecated)

setAccountExtraInfo(name: string, extraInfo: string, callback: AsyncCallback<void>): void

设置指定应用账号的额外信息。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[setCustomData](#ZH-CN_TOPIC_0000002497605500__setcustomdata9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。extraInfostring是额外信息(能转换string类型的其它信息)，额外信息不能是应用账号的敏感信息（如应用账号密码、token等）。callbackAsyncCallback<void>是回调函数。当设置成功时，err为null，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAccountExtraInfo('ZhangSan', 'Tk002', (err: BusinessError) => {
  if (err) {
    console.error(`setAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setAccountExtraInfo successful.');
  }
});
```

#### setAccountExtraInfo(deprecated)

setAccountExtraInfo(name: string, extraInfo: string): Promise<void>

设置此应用程序账号的额外信息。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[setCustomData](#ZH-CN_TOPIC_0000002497605500__setcustomdata9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。extraInfostring是额外信息(能转换string类型的其它信息)，额外信息不能是应用账号的敏感信息（如应用账号密码、token等）。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAccountExtraInfo('ZhangSan', 'Tk002').then(() => {
  console.info('setAccountExtraInfo Success');
}).catch((err: BusinessError) => {
  console.error(`setAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
});
```

#### setAppAccountSyncEnable(deprecated)

setAppAccountSyncEnable(name: string, isEnable: boolean, callback: AsyncCallback<void>): void

开启或禁止指定应用账号的数据同步功能。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[setDataSyncEnabled](#ZH-CN_TOPIC_0000002497605500__setdatasyncenabled9)替代。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。isEnableboolean是是否开启数据同步。true表示开启数据同步，false表示关闭数据同步。callbackAsyncCallback<void>是回调函数。当开启或禁止成功时，err为null，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAppAccountSyncEnable('ZhangSan', true, (err: BusinessError) => {
  if (err) {
    console.error(`setAppAccountSyncEnable err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setAppAccountSyncEnable successful.');
  }
});
```

#### setAppAccountSyncEnable(deprecated)

setAppAccountSyncEnable(name: string, isEnable: boolean): Promise<void>

开启或禁止指定应用账号的数据同步功能。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[setDataSyncEnabled](#ZH-CN_TOPIC_0000002497605500__setdatasyncenabled9-1)替代。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。isEnableboolean是是否开启数据同步。true表示开启数据同步，false表示关闭数据同步。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAppAccountSyncEnable('ZhangSan', true).then(() => {
  console.info('setAppAccountSyncEnable Success');
}).catch((err: BusinessError) => {
  console.error(`setAppAccountSyncEnable err: code is ${err.code}, message is ${err.message}`);
});
```

#### setAssociatedData(deprecated)

setAssociatedData(name: string, key: string, value: string, callback: AsyncCallback<void>): void

设置指定应用账号的关联数据。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[setCustomData](#ZH-CN_TOPIC_0000002497605500__setcustomdata9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。keystring是关联数据的键名。valuestring是关联数据的取值。callbackAsyncCallback<void>是回调函数。当设置与此应用账号关联的数据成功时，err为null，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAssociatedData('ZhangSan', 'k001', 'v001', (err: BusinessError) => {
  if (err) {
    console.error(`setAssociatedData err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setAssociatedData successful.');
  }
});
```

#### setAssociatedData(deprecated)

setAssociatedData(name: string, key: string, value: string): Promise<void>

设置指定应用账号的关联数据。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[setCustomData](#ZH-CN_TOPIC_0000002497605500__setcustomdata9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。keystring是关联数据的键名。valuestring是关联数据的取值。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAssociatedData('ZhangSan', 'k001', 'v001').then(() => {
  console.info('setAssociatedData Success');
}).catch((err: BusinessError) => {
  console.error(`setAssociatedData err: code is ${err.code}, message is ${err.message}`);
});
```

#### getAllAccessibleAccounts(deprecated)

getAllAccessibleAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void

获取所有可访问的应用账号信息。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[getAllAccounts](#ZH-CN_TOPIC_0000002497605500__getallaccounts9)替代。

**需要权限：** ohos.permission.GET_ALL_APP_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>是回调函数。当查询成功时，err为null，data为获取到的应用账号信息列表；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAllAccessibleAccounts((err: BusinessError, data: appAccount.AppAccountInfo[])=>{
  if (err) {
    console.error(`getAllAccessibleAccounts err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAllAccessibleAccounts data: ' + JSON.stringify(data));
  }
});
```

#### getAllAccessibleAccounts(deprecated)

getAllAccessibleAccounts(): Promise<Array<AppAccountInfo>>

获取所有可访问的应用账号信息。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[getAllAccounts](#ZH-CN_TOPIC_0000002497605500__getallaccounts9-1)替代。

**需要权限：** ohos.permission.GET_ALL_APP_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

类型说明Promise<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>Promise对象，返回全部应用已授权账号信息对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAllAccessibleAccounts().then((data: appAccount.AppAccountInfo[]) => {
  console.info('getAllAccessibleAccounts: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAllAccessibleAccounts err: code is ${err.code}, message is ${err.message}`);
});
```

#### getAllAccounts(deprecated)

getAllAccounts(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void

根据应用账号所有者获取调用方可访问的应用账号列表。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[getAccountsByOwner](#ZH-CN_TOPIC_0000002497605500__getaccountsbyowner9)替代。

**需要权限：** ohos.permission.GET_ALL_APP_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明ownerstring是应用账号所有者的包名。callbackAsyncCallback<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>是应用账号信息列表。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const selfBundle = 'com.example.actsgetallaaccounts';
appAccountManager.getAllAccounts(selfBundle, (err: BusinessError, data: appAccount.AppAccountInfo[])=>{
  if (err) {
    console.error(`getAllAccounts err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAllAccounts data:' + JSON.stringify(data));
  }
});
```

#### getAllAccounts(deprecated)

getAllAccounts(owner: string): Promise<Array<AppAccountInfo>>

根据应用账号所有者获取调用方可访问的应用账号列表。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[getAccountsByOwner](#ZH-CN_TOPIC_0000002497605500__getaccountsbyowner9-1)替代。

**需要权限：** ohos.permission.GET_ALL_APP_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明ownerstring是应用账号所有者的包名。

**返回值：**

类型说明Promise<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>Promise对象，返回指定应用全部账号信息对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const selfBundle = 'com.example.actsgetallaaccounts';
appAccountManager.getAllAccounts(selfBundle).then((data: appAccount.AppAccountInfo[]) => {
  console.info('getAllAccounts: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAllAccounts err: code is ${err.code}, message is ${err.message}`);
});
```

#### getAccountCredential(deprecated)

getAccountCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void

获取指定应用账号的凭据。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[getCredential](#ZH-CN_TOPIC_0000002497605500__getcredential9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。credentialTypestring是凭据类型。callbackAsyncCallback<string>是回调函数。当获取凭据成功时，err为null，data为指定应用账号的凭据；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAccountCredential('ZhangSan', 'credentialType001', (err: BusinessError, result: string) => {
  if (err) {
    console.error(`getAccountCredential err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAccountCredential result: ' + result);
  }
});
```

#### getAccountCredential(deprecated)

getAccountCredential(name: string, credentialType: string): Promise<string>

获取指定应用账号的凭据。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[getCredential](#ZH-CN_TOPIC_0000002497605500__getcredential9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。credentialTypestring是凭据类型。

**返回值：**

类型说明Promise<string>Promise对象，返回指定应用账号的凭据。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAccountCredential('ZhangSan', 'credentialType001').then((data: string) => {
  console.info('getAccountCredential, result: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAccountCredential err: code is ${err.code}, message is ${err.message}`);
});
```

#### getAccountExtraInfo(deprecated)

getAccountExtraInfo(name: string, callback: AsyncCallback<string>): void

获取指定应用账号的额外信息（能转换成string类型的其它信息）。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[getCustomData](#ZH-CN_TOPIC_0000002497605500__getcustomdata9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。callbackAsyncCallback<string>是回调函数。当获取此应用账号的额外信息成功时，err为null，data返回此应用账号的额外信息对象；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAccountExtraInfo('ZhangSan', (err: BusinessError, result: string) => {
  if (err) {
    console.error(`getAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAccountExtraInfo result: ' + result);
  }
});
```

#### getAccountExtraInfo(deprecated)

getAccountExtraInfo(name: string): Promise<string>

获取指定应用账号的额外信息（能转换成string类型的其它信息）。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[getCustomData](#ZH-CN_TOPIC_0000002497605500__getcustomdata9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。

**返回值：**

类型说明Promise<string>Promise对象，返回此应用程序账号的额外信息对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAccountExtraInfo('ZhangSan').then((data: string) => {
  console.info('getAccountExtraInfo, result: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
});
```

#### getAssociatedData(deprecated)

getAssociatedData(name: string, key: string, callback: AsyncCallback<string>): void

根据指定键名获取特定应用账号的关联数据。使用callback异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[getCustomData](#ZH-CN_TOPIC_0000002497605500__getcustomdata9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。keystring是关联数据的键名。callbackAsyncCallback<string>是回调函数。当获取成功时，err为null，data为关联数据的取值；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAssociatedData('ZhangSan', 'k001', (err: BusinessError, result: string) => {
  if (err) {
    console.error(`getAssociatedData err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAssociatedData result: ' + result);
  }
});
```

#### getAssociatedData(deprecated)

getAssociatedData(name: string, key: string): Promise<string>

获取与此应用程序账号关联的数据。使用Promise异步回调。

从API version 7开始支持，从API version 9开始废弃。建议使用[getCustomData](#ZH-CN_TOPIC_0000002497605500__getcustomdata9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。keystring是关联数据的键名。

**返回值：**

类型说明Promise<string>Promise对象，返回关联数据的取值。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAssociatedData('ZhangSan', 'k001').then((data: string) => {
  console.info('getAssociatedData: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAssociatedData err: code is ${err.code}, message is ${err.message}`);
});
```

#### on('change')(deprecated)

on(type: 'change', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void

订阅指定应用的账号信息变更事件。

从API version 7开始支持，从API version 9开始废弃。建议使用[on('accountChange')](#ZH-CN_TOPIC_0000002497605500__onaccountchange9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明type'change'是事件回调类型，支持的事件为'change'，当账号所有者更新账号信息时，触发该事件。ownersArray<string>是应用账号所有者的包名列表。callbackCallback<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>是需要注册的回调函数，返回信息发生变更的应用账号列表。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
  console.info('receive change data:' + JSON.stringify(data));
}

try {
  appAccountManager.on('change', ['com.example.actsaccounttest'], changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`on accountOnOffDemo code is ${err.code}, message is ${err.message}`);
}
```

#### off('change')(deprecated)

off(type: 'change', callback?: Callback<Array<AppAccountInfo>>): void

取消订阅账号信息变更事件。

从API version 7开始支持，从API version 9开始废弃。建议使用[off('accountChange')](#ZH-CN_TOPIC_0000002497605500__offaccountchange9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明type'change'是事件回调类型，支持的事件为'change'，当账号所有者更新账号信息时，触发该事件。callbackCallback<Array<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>>否需要注销的回调函数，默认为空，表示取消该类型事件的所有回调。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
  console.info('receive change data: ' + JSON.stringify(data));
  appAccountManager.off('change', () => {
    console.info('off finish');
  })
}

try {
  appAccountManager.on('change', ['com.example.actsaccounttest'], changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`on accountOnOffDemo err: code is ${err.code}, message is ${err.message}`);
}
```

#### authenticate(deprecated)

authenticate(name: string, owner: string, authType: string, options: {[key: string]: any;}, callback: AuthenticatorCallback): void

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[auth](#ZH-CN_TOPIC_0000002497605500__auth9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。authTypestring是鉴权类型。options{[key: string]: any}是鉴权所需的可选项。callback[AuthenticatorCallback](#ZH-CN_TOPIC_0000002497605500__authenticatorcallbackdeprecated)是回调对象，返回鉴权结果。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, result: Record<string, Object>): void {
    console.info('resultCode: ' + code);
    console.info('result: ' + JSON.stringify(result));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    appAccountManager.authenticate('LiSi', 'com.example.accountjsdemo', 'getSocialData', {}, {
      onResult: this.onResultCallback,
      onRequestRedirected: this.onRequestRedirectedCallback
    });
  }

  build() {}
}
```

#### getOAuthToken(deprecated)

getOAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void

获取指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthToken](#ZH-CN_TOPIC_0000002497605500__getauthtoken9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。authTypestring是鉴权类型。callbackAsyncCallback<string>是回调函数。当获取成功时，err为null，data为授权令牌值；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData',
  (err: BusinessError, data: string) => {
    if (err) {
      console.error(`getOAuthToken err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getOAuthToken token: ' + data);
    }
  });
```

#### getOAuthToken(deprecated)

getOAuthToken(name: string, owner: string, authType: string): Promise<string>

获取指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthToken](#ZH-CN_TOPIC_0000002497605500__getauthtoken9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。authTypestring是鉴权类型。

**返回值：**

类型说明Promise<string>Promise对象，返回授权令牌。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData').then((data: string) => {
  console.info('getOAuthToken token: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getOAuthToken err: code is ${err.code}, message is ${err.message}`);
});
```

#### setOAuthToken(deprecated)

setOAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void

为指定应用账号设置特定鉴权类型的授权令牌。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[setAuthToken](#ZH-CN_TOPIC_0000002497605500__setauthtoken9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。tokenstring是授权令牌。callbackAsyncCallback<void>是回调函数。当设置成功时，err为null；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setOAuthToken('LiSi', 'getSocialData', 'xxxx', (err: BusinessError) => {
  if (err) {
    console.error(`setOAuthToken err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setOAuthToken successful.');
  }
});
```

#### setOAuthToken(deprecated)

setOAuthToken(name: string, authType: string, token: string): Promise<void>

为指定应用账号设置特定鉴权类型的授权令牌。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[setAuthToken](#ZH-CN_TOPIC_0000002497605500__setauthtoken9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。tokenstring是授权令牌。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setOAuthToken('LiSi', 'getSocialData', 'xxxx').then(() => {
  console.info('setOAuthToken successfully');
}).catch((err: BusinessError) => {
  console.error(`setOAuthToken err: code is ${err.code}, message is ${err.message}`);
});
```

#### deleteOAuthToken(deprecated)

deleteOAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void

删除指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[deleteAuthToken](#ZH-CN_TOPIC_0000002497605500__deleteauthtoken9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。authTypestring是鉴权类型。tokenstring是授权令牌。callbackAsyncCallback<void>是回调函数。当删除成功时，err为null；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.deleteOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx',
  (err: BusinessError) => {
    if (err) {
      console.error(`deleteOAuthToken err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('deleteOAuthToken successful.');
    }
  });
```

#### deleteOAuthToken(deprecated)

deleteOAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>

删除指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[deleteAuthToken](#ZH-CN_TOPIC_0000002497605500__deleteauthtoken9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。authTypestring是鉴权类型。tokenstring是授权令牌。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.deleteOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx').then(() => {
  console.info('deleteOAuthToken successfully');
}).catch((err: BusinessError) => {
  console.error(`deleteOAuthToken err: code is ${err.code}, message is ${err.message}`);
});
```

#### setOAuthTokenVisibility(deprecated)

setOAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void>): void

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[setAuthTokenVisibility](#ZH-CN_TOPIC_0000002497605500__setauthtokenvisibility9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。bundleNamestring是被设置可见性的应用包名。isVisibleboolean是是否可见。true表示可见，false表示不可见。callbackAsyncCallback<void>是回调函数。当设置成功时，err为null；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true,
  (err: BusinessError) => {
    if (err) {
      console.error(`setOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setOAuthTokenVisibility successful.');
    }
  });
```

#### setOAuthTokenVisibility(deprecated)

setOAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[setAuthTokenVisibility](#ZH-CN_TOPIC_0000002497605500__setauthtokenvisibility9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。bundleNamestring是被设置可见性的应用包名。isVisibleboolean是是否可见。true表示可见，false表示不可见。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true).then(() => {
  console.info('setOAuthTokenVisibility successfully');
}).catch((err: BusinessError) => {
  console.error(`setOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
});
```

#### checkOAuthTokenVisibility(deprecated)

checkOAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>): void

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[checkAuthTokenVisibility](#ZH-CN_TOPIC_0000002497605500__checkauthtokenvisibility9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。bundleNamestring是检查可见性的应用包名。callbackAsyncCallback<boolean>是回调函数。当检查成功时，err为null，data为true表示可见，data为false表示不可见；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.checkOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo',
  (err: BusinessError, data: boolean) => {
    if (err) {
      console.error(`checkOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkOAuthTokenVisibility isVisible: ' + data);
    }
  });
```

#### checkOAuthTokenVisibility(deprecated)

checkOAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[checkAuthTokenVisibility](#ZH-CN_TOPIC_0000002497605500__checkauthtokenvisibility9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。bundleNamestring是用于检查可见性的应用包名。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示指定鉴权类型的OAuth令牌对特定应用的可见，返回false表示不可见。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.checkOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo').then((
  data: boolean) => {
  console.info('checkOAuthTokenVisibility isVisible: ' + data);
}).catch((err: BusinessError) => {
  console.error(`checkOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
});
```

#### getAllOAuthTokens(deprecated)

getAllOAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<OAuthTokenInfo>>): void

获取指定账号对调用方可见的所有授权令牌。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[getAllAuthTokens](#ZH-CN_TOPIC_0000002497605500__getallauthtokens9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。callbackAsyncCallback<Array<[OAuthTokenInfo](#ZH-CN_TOPIC_0000002497605500__oauthtokeninfodeprecated)>>是回调函数。当获取成功时，err为null，data为授权令牌数组；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAllOAuthTokens('LiSi', 'com.example.accountjsdemo',
  (err: BusinessError, data: appAccount.OAuthTokenInfo[]) => {
    if (err) {
      console.error(`getAllOAuthTokens err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAllOAuthTokens data: ' + JSON.stringify(data));
    }
  });
```

#### getAllOAuthTokens(deprecated)

getAllOAuthTokens(name: string, owner: string): Promise<Array<OAuthTokenInfo>>

获取指定账号对调用方可见的所有授权令牌。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[getAllAuthTokens](#ZH-CN_TOPIC_0000002497605500__getallauthtokens9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。ownerstring是应用账号所有者的包名。

**返回值：**

类型说明Promise<Array< [OAuthTokenInfo](#ZH-CN_TOPIC_0000002497605500__oauthtokeninfodeprecated)>>Promise对象，返回授权令牌数组。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAllOAuthTokens('LiSi', 'com.example.accountjsdemo').then((
  data: appAccount.OAuthTokenInfo[]) => {
  console.info('getAllOAuthTokens data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`getAllOAuthTokens err: code is ${err.code}, message is ${err.message}`);
});
```

#### getOAuthList(deprecated)

getOAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过[setOAuthTokenVisibility](#ZH-CN_TOPIC_0000002497605500__setoauthtokenvisibilitydeprecated)来设置）。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthList](#ZH-CN_TOPIC_0000002497605500__getauthlist9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。callbackAsyncCallback<Array<string>>是回调函数。当获取成功时，err为null，data为被授权的包名数组；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getOAuthList('LiSi', 'getSocialData', (err: BusinessError, data: string[]) => {
  if (err) {
    console.error(`getOAuthList err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getOAuthList data: ' + JSON.stringify(data));
  }
});
```

#### getOAuthList(deprecated)

getOAuthList(name: string, authType: string): Promise<Array<string>>

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过[setOAuthTokenVisibility](#ZH-CN_TOPIC_0000002497605500__setoauthtokenvisibilitydeprecated)来设置）。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthList](#ZH-CN_TOPIC_0000002497605500__getauthlist9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是鉴权类型。

**返回值：**

类型说明Promise<Array<string>>Promise对象，返回被授权的包名数组。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getOAuthList('LiSi', 'getSocialData').then((data: string[]) => {
  console.info('getOAuthList data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`getOAuthList err: code is ${err.code}, message is ${err.message}`);
});
```

#### getAuthenticatorCallback(deprecated)

getAuthenticatorCallback(sessionId: string, callback: AsyncCallback<AuthenticatorCallback>): void

获取鉴权会话的认证器回调。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthCallback](#ZH-CN_TOPIC_0000002497605500__getauthcallback9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明sessionIdstring是鉴权会话的标识。callbackAsyncCallback<[AuthenticatorCallback](#ZH-CN_TOPIC_0000002497605500__authenticatorcallbackdeprecated)>是回调函数。当获取鉴权会话的认证器回调函数成功时，err为null，data为认证器回调函数；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
    let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
    appAccountManager.getAuthenticatorCallback(sessionId,
        (err: BusinessError, callback: appAccount.AuthenticatorCallback) => {
        if (err.code != appAccount.ResultCode.SUCCESS) {
            console.error(`getAuthenticatorCallback err: code is ${err.code}, message is ${err.message}`);
            return;
        }
        callback.onResult(appAccount.ResultCode.SUCCESS, {
          name: 'LiSi',
          owner: 'com.example.accountjsdemo',
          authType: 'getSocialData',
          token: 'xxxxxx'
        });
      });
  }
}
```

#### getAuthenticatorCallback(deprecated)

getAuthenticatorCallback(sessionId: string): Promise<AuthenticatorCallback>

获取鉴权会话的认证器回调。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthCallback](#ZH-CN_TOPIC_0000002497605500__getauthcallback9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明sessionIdstring是鉴权会话的标识。

**返回值：**

类型说明Promise<[AuthenticatorCallback](#ZH-CN_TOPIC_0000002497605500__authenticatorcallbackdeprecated)>Promise对象，返回鉴权会话的认证器回调对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
    let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
    appAccountManager.getAuthenticatorCallback(sessionId).then((
      callback: appAccount.AuthenticatorCallback) => {
      callback.onResult(appAccount.ResultCode.SUCCESS, {
        name: 'LiSi',
        owner: 'com.example.accountjsdemo',
        authType: 'getSocialData',
        token: 'xxxxxx'
      });
    }).catch((err: BusinessError) => {
      console.error(`getAuthenticatorCallback err: code is ${err.code}, message is ${err.message}`);
    });
  }
}
```

#### getAuthenticatorInfo(deprecated)

getAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void

获取指定应用的认证器信息。使用callback异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[queryAuthenticatorInfo](#ZH-CN_TOPIC_0000002497605500__queryauthenticatorinfo9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明ownerstring是应用账号所有者的包名。callbackAsyncCallback<[AuthenticatorInfo](#ZH-CN_TOPIC_0000002497605500__authenticatorinfo8)>是回调函数。当获取成功时，err为null，data为认证器信息对象；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAuthenticatorInfo('com.example.accountjsdemo',
  (err: BusinessError, data: appAccount.AuthenticatorInfo) => {
    if (err) {
      console.error(`getAuthenticatorInfo err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAuthenticatorInfo data: ' + JSON.stringify(data));
    }
  });
```

#### getAuthenticatorInfo(deprecated)

getAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>

获取指定应用的认证器信息。使用Promise异步回调。

从API version 8开始支持，从API version 9开始废弃。建议使用[queryAuthenticatorInfo](#ZH-CN_TOPIC_0000002497605500__queryauthenticatorinfo9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明ownerstring是应用账号所有者的包名。

**返回值：**

类型说明Promise<[AuthenticatorInfo](#ZH-CN_TOPIC_0000002497605500__authenticatorinfo8)>Promise对象，返回指定应用的认证器信息对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAuthenticatorInfo('com.example.accountjsdemo').then((
  data: appAccount.AuthenticatorInfo) => {
  console.info('getAuthenticatorInfo: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`getAuthenticatorInfo err: code is ${err.code}, message is ${err.message}`);
});
```

#### AppAccountInfo

表示应用账号信息。

**系统能力：** SystemCapability.Account.AppAccount

名称类型只读可选说明ownerstring否否应用账号所有者的包名。namestring否否应用账号的名称。

#### AuthTokenInfo9+

表示Auth令牌信息。

**系统能力：** SystemCapability.Account.AppAccount

名称类型只读可选说明authTypestring否否令牌的鉴权类型。tokenstring否否令牌的取值。account[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)否是令牌所属的账号信息，默认为空。

#### OAuthTokenInfo(deprecated)

表示OAuth令牌信息。

从API version 8开始支持，从API version 9开始废弃。建议使用[AuthTokenInfo](#ZH-CN_TOPIC_0000002497605500__authtokeninfo9)替代。

**系统能力：** SystemCapability.Account.AppAccount

名称类型只读可选说明authTypestring否否令牌的鉴权类型。tokenstring否否令牌的取值。

#### AuthenticatorInfo8+

表示OAuth认证器信息。

**系统能力：** SystemCapability.Account.AppAccount

名称类型只读可选说明ownerstring否否认证器的所有者的包名。iconIdnumber否否认证器的图标标识。labelIdnumber否否认证器的标签标识。

#### AuthResult9+

表示认证结果信息。

**系统能力：** SystemCapability.Account.AppAccount

名称类型只读可选说明account[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)否是令牌所属的账号信息，默认为空。tokenInfo[AuthTokenInfo](#ZH-CN_TOPIC_0000002497605500__authtokeninfo9)否是令牌信息，默认为空。

#### CreateAccountOptions9+

表示创建账号的选项。

**系统能力：** SystemCapability.Account.AppAccount

名称类型只读可选说明customDataRecord<string, string>否是自定义数据，默认为空。

#### CreateAccountImplicitlyOptions9+

表示隐式创建账号的选项。

**系统能力：** SystemCapability.Account.AppAccount

名称类型只读可选说明requiredLabelsArray<string>否是所需的标签，默认为空。authTypestring否是鉴权类型，默认为空。parametersRecord<string, Object>否是自定义参数对象，默认为空。

#### SelectAccountsOptions9+

表示用于选择账号的选项。

**系统能力：** SystemCapability.Account.AppAccount

名称类型只读可选说明allowedAccountsArray<[AppAccountInfo](#ZH-CN_TOPIC_0000002497605500__appaccountinfo)>否是允许的账号数组，默认为空。allowedOwnersArray<string>否是允许的账号所有者数组，默认为空。requiredLabelsArray<string>否是认证器的标签标识，默认为空。

#### VerifyCredentialOptions9+

表示用于验证凭据的选项。

**系统能力：** SystemCapability.Account.AppAccount

名称类型只读可选说明credentialTypestring否是凭据类型，默认为空。credentialstring否是凭据取值，默认为空。parametersRecord<string, Object>否是自定义参数对象，默认为空。

#### SetPropertiesOptions9+

表示用于设置属性的选项。

**系统能力：** SystemCapability.Account.AppAccount

名称类型只读可选说明propertiesRecord<string, Object>否是属性对象，默认为空。parametersRecord<string, Object>否是自定义参数对象，默认为空。

#### Constants8+

表示常量的枚举。

**系统能力：** SystemCapability.Account.AppAccount

名称值说明ACTION_ADD_ACCOUNT_IMPLICITLY(deprecated)'addAccountImplicitly'

表示操作，隐式添加账号。

**说明：**从API version 8开始支持，从API version 9开始废弃，建议使用ACTION_CREATE_ACCOUNT_IMPLICITLY替代。

ACTION_AUTHENTICATE(deprecated)'authenticate'

表示操作，鉴权。

**说明：**从API version 8开始支持，从API version 9开始废弃，建议使用ACTION_AUTH替代。

ACTION_CREATE_ACCOUNT_IMPLICITLY9+'createAccountImplicitly'表示操作，隐式创建账号。ACTION_AUTH9+'auth'表示操作，鉴权。ACTION_VERIFY_CREDENTIAL9+'verifyCredential'表示操作，验证凭据。ACTION_SET_AUTHENTICATOR_PROPERTIES9+'setAuthenticatorProperties'表示操作，设置认证器属性。KEY_NAME'name'表示键名，应用账号的名称。KEY_OWNER'owner'表示键名，应用账号所有者的包名。KEY_TOKEN'token'表示键名，令牌。KEY_ACTION'action'表示键名，操作。KEY_AUTH_TYPE'authType'表示键名，鉴权类型。KEY_SESSION_ID'sessionId'表示键名，会话标识。KEY_CALLER_PID'callerPid'表示键名，调用方PID。KEY_CALLER_UID'callerUid'表示键名，调用方UID。KEY_CALLER_BUNDLE_NAME'callerBundleName'表示键名，调用方包名。KEY_REQUIRED_LABELS9+'requiredLabels'表示键名，必需的标签。KEY_BOOLEAN_RESULT9+'booleanResult'表示键名，布尔返回值。

#### ResultCode(deprecated)

表示返回码的枚举。

从API version 8开始支持，从API version 9开始废弃。相关信息建议查看[错误码文档](账号管理错误码.md)替代。

**系统能力：** SystemCapability.Account.AppAccount

名称值说明SUCCESS0表示操作成功。ERROR_ACCOUNT_NOT_EXIST10001表示应用账号不存在。ERROR_APP_ACCOUNT_SERVICE_EXCEPTION10002表示应用账号服务异常。ERROR_INVALID_PASSWORD10003表示密码无效。ERROR_INVALID_REQUEST10004表示请求无效。ERROR_INVALID_RESPONSE10005表示响应无效。ERROR_NETWORK_EXCEPTION10006表示网络异常。ERROR_OAUTH_AUTHENTICATOR_NOT_EXIST10007表示认证器不存在。ERROR_OAUTH_CANCELED10008表示鉴权取消。ERROR_OAUTH_LIST_TOO_LARGE10009表示开放授权列表过大。ERROR_OAUTH_SERVICE_BUSY10010表示开放授权服务忙碌。ERROR_OAUTH_SERVICE_EXCEPTION10011表示开放授权服务异常。ERROR_OAUTH_SESSION_NOT_EXIST10012表示鉴权会话不存在。ERROR_OAUTH_TIMEOUT10013表示鉴权超时。ERROR_OAUTH_TOKEN_NOT_EXIST10014表示开放授权令牌不存在。ERROR_OAUTH_TOKEN_TOO_MANY10015表示开放授权令牌过多。ERROR_OAUTH_UNSUPPORT_ACTION10016表示不支持的鉴权操作。ERROR_OAUTH_UNSUPPORT_AUTH_TYPE10017表示不支持的鉴权类型。ERROR_PERMISSION_DENIED10018表示权限不足。

#### AuthCallback9+

认证器回调类。

#### onResult9+

onResult: (code: number, result?: AuthResult) => void

通知请求结果。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明codenumber是鉴权结果码。result[AuthResult](#ZH-CN_TOPIC_0000002497605500__authresult9)否鉴权结果，默认为空，表示不接收认证结果信息。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
let sessionId = '1234';
appAccountManager.getAuthCallback(sessionId).then((callback: appAccount.AuthCallback) => {
  let result: appAccount.AuthResult = {
    account: {
      name: 'Lisi',
      owner: 'com.example.accountjsdemo',
    },
    tokenInfo: {
      token: 'xxxxxx',
      authType: 'getSocialData'
    }
  };
  callback.onResult(appAccount.ResultCode.SUCCESS, result);
}).catch((err: BusinessError) => {
  console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
});
```

#### onRequestRedirected9+

onRequestRedirected: (request: Want) => void

通知请求被跳转。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明request[Want](@ohos.app.ability.Want (Want).md)是用于跳转的请求信息。

**示例：**

```ets
import { Want } from '@kit.AbilityKit';

class MyAuthenticator extends appAccount.Authenticator {
  createAccountImplicitly(
    options: appAccount.CreateAccountImplicitlyOptions, callback: appAccount.AuthCallback) {
    let want: Want = {
      bundleName: 'com.example.accountjsdemo',
      abilityName: 'com.example.accountjsdemo.LoginAbility',
    };
    callback.onRequestRedirected(want);
  }

  auth(name: string, authType: string,
    options: Record<string, Object>, callback: appAccount.AuthCallback) {
    let result: appAccount.AuthResult = {
      account: {
        name: 'Lisi',
        owner: 'com.example.accountjsdemo',
      },
      tokenInfo: {
        token: 'xxxxxx',
        authType: 'getSocialData'
      }
    };
    callback.onResult(appAccount.ResultCode.SUCCESS, result);
  }
}
```

#### onRequestContinued9+

onRequestContinued?: () => void

通知请求被继续处理。

**系统能力：** SystemCapability.Account.AppAccount

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
let sessionId = '1234';
appAccountManager.getAuthCallback(sessionId).then((callback: appAccount.AuthCallback) => {
  if (callback.onRequestContinued != undefined) {
    callback.onRequestContinued();
  }
}).catch((err: BusinessError) => {
  console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
});
```

#### AuthenticatorCallback(deprecated)

OAuth认证器回调接口。

从API version 8开始支持，从API version 9开始废弃。建议使用[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)替代。

#### onResult(deprecated)

onResult: (code: number, result: {[key: string]: any;}) => void

通知请求结果。

从API version 8开始支持，从API version 9开始废弃。建议使用[onResult](#ZH-CN_TOPIC_0000002497605500__onresult9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明codenumber是鉴权结果码。result{[key: string]: any}是鉴权结果。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
let sessionId = '1234';
appAccountManager.getAuthenticatorCallback(sessionId).then((callback: appAccount.AuthenticatorCallback) => {
  callback.onResult(appAccount.ResultCode.SUCCESS, {
    name: 'LiSi',
    owner: 'com.example.accountjsdemo',
    authType: 'getSocialData',
    token: 'xxxxxx'
  });
}).catch((err: BusinessError) => {
  console.error(`getAuthenticatorCallback err: code is ${err.code}, message is ${err.message}`);
});
```

#### onRequestRedirected(deprecated)

onRequestRedirected: (request: Want) => void

通知请求被跳转。

从API version 8开始支持，从API version 9开始废弃。建议使用[onRequestRedirected](#ZH-CN_TOPIC_0000002497605500__onrequestredirected9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明request[Want](@ohos.app.ability.Want (Want).md)是用于跳转的请求信息。

**示例：**

```ets
import { Want } from '@kit.AbilityKit';

class MyAuthenticator extends appAccount.Authenticator {
  addAccountImplicitly(authType: string, callerBundleName: string,
    options: Record<string, Object>, callback: appAccount.AuthenticatorCallback) {
    let want: Want = {
      bundleName: 'com.example.accountjsdemo',
      abilityName: 'com.example.accountjsdemo.LoginAbility',
    };
    callback.onRequestRedirected(want);
  }

  authenticate(name: string, authType: string, callerBundleName: string,
    options: Record<string, Object>, callback: appAccount.AuthenticatorCallback) {
    callback.onResult(appAccount.ResultCode.SUCCESS, {
      name: name,
      authType: authType,
      token: 'xxxxxx'
    });
  }
}
```

#### Authenticator8+

认证器基类。

#### createAccountImplicitly9+

createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void

根据指定的账号所有者隐式地创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明options[CreateAccountImplicitlyOptions](#ZH-CN_TOPIC_0000002497605500__createaccountimplicitlyoptions9)是隐式创建账号的选项。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是认证器回调对象，用于返回创建结果。

#### addAccountImplicitly(deprecated)

addAccountImplicitly(authType: string, callerBundleName: string, options: {[key: string]: any;}, callback: AuthenticatorCallback): void

根据指定的鉴权类型和可选项，隐式地添加应用账号。使用callback异步回调。

从API version 8开始支持, 从API version 9开始废弃。建议使用[createAccountImplicitly](#ZH-CN_TOPIC_0000002497605500__createaccountimplicitly9-2)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明authTypestring是应用账号的鉴权类型。callerBundleNamestring是鉴权请求方的包名。options{[key: string]: any}是鉴权所需要的可选项。callback[AuthenticatorCallback](#ZH-CN_TOPIC_0000002497605500__authenticatorcallbackdeprecated)是认证器回调，用于返回鉴权结果。

#### auth9+

auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是应用账号的鉴权类型。optionsRecord<string, Object>是鉴权所需要的可选项。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是回调对象，用于返回鉴权结果。

#### authenticate(deprecated)

authenticate(name: string, authType: string, callerBundleName: string, options: {[key: string]: any;}, callback: AuthenticatorCallback): void

对应用账号进行鉴权，获取OAuth令牌。使用callback异步回调。

从API version 8开始支持, 从API version 9开始废弃。建议使用[auth](#ZH-CN_TOPIC_0000002497605500__auth9-2)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。authTypestring是应用账号的鉴权类型。callerBundleNamestring是鉴权请求方的包名。options{[key: string]: any}是鉴权所需要的可选项。callback[AuthenticatorCallback](#ZH-CN_TOPIC_0000002497605500__authenticatorcallbackdeprecated)是认证器回调，用于返回鉴权结果。

#### verifyCredential9+

verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void

验证应用账号的凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。options[VerifyCredentialOptions](#ZH-CN_TOPIC_0000002497605500__verifycredentialoptions9)是验证凭据的可选项。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是认证器回调，用于返回验证结果。

**示例：**

接口需组合使用，请查看[getRemoteObject](#ZH-CN_TOPIC_0000002497605500__getremoteobject9)中的示例。

#### setProperties9+

setProperties(options: SetPropertiesOptions, callback: AuthCallback): void

设置认证器属性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明options[SetPropertiesOptions](#ZH-CN_TOPIC_0000002497605500__setpropertiesoptions9)是设置属性的可选项。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是认证器回调，用于返回设置结果。

**示例：**

接口需组合使用，请查看[getRemoteObject](#ZH-CN_TOPIC_0000002497605500__getremoteobject9)中的示例。

#### checkAccountLabels9+

checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void

检查账号标签。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。labelsArray<string>是标签数组。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是认证器回调，用于返回检查结果。

**示例：**

接口需组合使用，请查看[getRemoteObject](#ZH-CN_TOPIC_0000002497605500__getremoteobject9)中的示例。

#### checkAccountRemovable9+

checkAccountRemovable(name: string, callback: AuthCallback): void

判断账号是否可以删除。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

参数名类型必填说明namestring是应用账号的名称。callback[AuthCallback](#ZH-CN_TOPIC_0000002497605500__authcallback9)是认证器回调，用于返回判断结果。

**示例：**

接口需组合使用，请查看[getRemoteObject](#ZH-CN_TOPIC_0000002497605500__getremoteobject9)中的示例。

#### getRemoteObject9+

getRemoteObject(): rpc.RemoteObject

获取认证器的远程对象，不可以重载实现。

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

类型说明[rpc.RemoteObject](@ohos.rpc (RPC通信).md#ZH-CN_TOPIC_0000002529445269__remoteobject)认证器Authenticator的远程对象。用于跨进程通信。

**示例：**

接口需组合使用，请查看[getRemoteObject](#ZH-CN_TOPIC_0000002497605500__getremoteobject9)中的示例。

**示例：**

```ets
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';

class MyAuthenticator extends appAccount.Authenticator {
  verifyCredential(name: string,
    options: appAccount.VerifyCredentialOptions, callback: appAccount.AuthCallback) {
      let want: Want = {
        bundleName: 'com.example.accountjsdemo',
        abilityName: 'com.example.accountjsdemo.VerifyAbility',
        parameters: {
          name: name
        }
      };
      callback.onRequestRedirected(want);
  }

  setProperties(options: appAccount.SetPropertiesOptions, callback: appAccount.AuthCallback) {
    let want: Want = {
      bundleName: 'com.example.accountjsdemo',
      abilityName: 'com.example.accountjsdemo.SetPropertiesAbility',
      parameters: {
        options: options
      }
    };
    callback.onRequestRedirected(want);
  }

  checkAccountLabels(name: string, labels: string[], callback: appAccount.AuthCallback) {
    callback.onResult(0);
  }

  checkAccountRemovable(name: string, callback: appAccount.AuthCallback) {
    callback.onResult(0);
  }
}

export default {
  onConnect(want: Want): rpc.RemoteObject { // serviceAbility 生命周期函数, 需要放在serviceAbility中
    let authenticator = new MyAuthenticator();
    return authenticator.getRemoteObject();
  }
}
```