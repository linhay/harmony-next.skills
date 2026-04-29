# @ohos.userIAM.userAuth (用户认证)

提供用户认证能力，应用于设备解锁、支付、应用登录等场景。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { userAuth } from '@kit.UserAuthenticationKit';
```

#### 常量

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| MAX_ALLOWABLE_REUSE_DURATION12+ | number | 300000 | 复用解锁认证结果最大有效时长，值为300000毫秒。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| PERMANENT_LOCKOUT_DURATION22+ | number | 0x7fffffff | 永久冻结时间，值为0x7fffffff毫秒。 元服务API： 从API version 22开始，该接口支持在元服务中使用。 |

#### AuthLockState22+

认证类型的身份认证冻结状态。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isLocked | boolean | 否 | 否 | 表示认证是否已被冻结。true表示已冻结；false表示未冻结。 |
| remainingAuthAttempts | number | 否 | 否 | 认证未被冻结时的剩余尝试次数，最大为5次。 |
| lockoutDuration | number | 否 | 否 | 认证被冻结时的剩余冻结时间，单位为毫秒。 当永久冻结时，值为PERMANENT_LOCKOUT_DURATION，需要PIN认证解锁。 |

#### UserAuthTipCode20+

表示身份认证中间状态的枚举。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMPARE_FAILURE | 1 | 认证失败。 |
| TIMEOUT | 2 | 认证超时。 |
| TEMPORARILY_LOCKED | 3 | 临时冻结。 |
| PERMANENTLY_LOCKED | 4 | 永久冻结。 |
| WIDGET_LOADED | 5 | 身份认证界面加载完毕。 |
| WIDGET_RELEASED | 6 | 当前的身份认证界面退出，切换其他认证界面或身份认证控件关闭。 |
| COMPARE_FAILURE_WITH_FROZEN | 7 | 认证失败并触发了认证冻结。 |

#### EnrolledState12+

用户注册凭据的状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credentialDigest | number | 否 | 否 | 注册的凭据摘要，在凭据增加时随机生成。 |
| credentialCount | number | 否 | 否 | 注册的凭据数量。 |

#### ReuseMode12+

复用解锁认证结果的模式。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTH_TYPE_RELEVANT | 1 | 与认证类型相关，只有当设备解锁认证结果在有效时间内，并且设备解锁的认证类型匹配上本次认证指定认证类型之一时，可以复用该结果。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| AUTH_TYPE_IRRELEVANT | 2 | 与认证类型无关，设备解锁认证结果在有效时间内，可以重复使用。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| CALLER_IRRELEVANT_AUTH_TYPE_RELEVANT14+ | 3 | 与认证类型相关，任意身份认证（包括设备解锁）结果在有效时间内，并且身份认证的认证类型匹配上本次认证指定认证类型之一时，可以复用该结果。 元服务API： 从API version 14开始，该接口支持在元服务中使用。 |
| CALLER_IRRELEVANT_AUTH_TYPE_IRRELEVANT14+ | 4 | 与认证类型无关，任意身份认证（包括设备解锁）结果在有效时间内，可以重复使用。 元服务API： 从API version 14开始，该接口支持在元服务中使用。 |

#### ReuseUnlockResult12+

复用解锁认证结果。

如果身份认证解锁（包括设备解锁）后，在有效时间内凭据发生了变化，身份认证的结果依然可以复用，认证结果中返回当前实际的EnrolledState。若复用认证结果时，之前认证时所使用的身份认证凭据已经被删除，如果删除的是人脸、指纹，则认证结果依然可以复用，只是返回的EnrolledState中credentialCount和credentialDigest均为0；如果删除的是锁屏口令，则此次复用会失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reuseMode | ReuseMode | 否 | 否 | 复用解锁认证结果的模式。 |
| reuseDuration | number | 否 | 否 | 允许复用解锁认证结果的有效时长，有效时长的值应大于0，最大值为MAX_ALLOWABLE_REUSE_DURATION。 |

#### userAuth.getAuthLockState22+

getAuthLockState(authType: UserAuthType): Promise<AuthLockState>

查询指定认证类型的冻结状态，使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authType | UserAuthType | 是 | 认证类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AuthLockState> | Promise对象，当查询成功时，返回值为指定认证类型的身份认证冻结状态。失败时报错。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[用户认证错误码]([用户认证错误码](../../errors/用户认证错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500008 | The parameter is out of range. |
| 12500010 | The type of credential has not been enrolled. |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let queryType = userAuth.UserAuthType.PIN;
let authLockState : userAuth.AuthLockState = {
  isLocked : false,
  remainingAuthAttempts : 0,
  lockoutDuration : 0
}

userAuth.getAuthLockState(queryType)
  .then((result : userAuth.AuthLockState) => {
    authLockState = result;
    console.info(`get auth lock state success, authLockState is: ${JSON.stringify(authLockState)}`);
  })
  .catch((err : BusinessError) => {
    console.info(`get auth lock state failed, err code is : ${err?.code}, err message is : ${err?.message}`);
  })
```

#### userAuth.getEnrolledState12+

getEnrolledState(authType: UserAuthType): EnrolledState

查询凭据注册的状态，以检测用户注册凭据的变更。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authType | UserAuthType | 是 | 认证类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| EnrolledState | 当查询成功时，返回值为用户注册凭据的状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户认证错误码](用户认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500010 | The type of credential has not been enrolled. |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let enrolledState = userAuth.getEnrolledState(userAuth.UserAuthType.FACE);
  console.info(`get current enrolled state success, enrolledState = ${JSON.stringify(enrolledState)}`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`get current enrolled state failed, Code is ${err?.code}, message is ${err?.message}`);
}
```

#### AuthParam10+

用户认证相关参数。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| challenge | Uint8Array | 否 | 否 | 随机挑战值，可用于防重放攻击。最大长度为32字节，可传Uint8Array([])。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| authType | UserAuthType[] | 否 | 否 | 认证类型列表，用来指定用户认证界面提供的认证方法。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| authTrustLevel | AuthTrustLevel | 否 | 否 | 期望达到的认证可信等级。典型操作需要的身份认证可信等级，以及身份认证可信等级的划分请参见认证可信等级划分原则。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| reuseUnlockResult12+ | ReuseUnlockResult | 否 | 是 | 表示可以复用解锁认证的结果。默认为不复用。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| skipLockedBiometricAuth20+ | boolean | 否 | 是 | 是否跳过已禁用的认证方式自动切换至其它方式的认证。若无可切换的认证方式则关闭控件，返回认证冻结错误码。 true表示生物认证冻结时，跳过倒计时界面直接切换到其他方式的认证； false表示不跳过；默认为false。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

#### WidgetParam10+

用户认证界面配置相关参数。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 用户认证界面的标题，建议传入认证目的，例如用于支付、登录应用等，不支持传空字串，最大长度为500字符。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| navigationButtonText | string | 否 | 是 | 导航按键的说明文本，最大长度为60字符。在单指纹、单人脸场景下支持，从API 18开始，增加支持人脸+指纹场景。默认为不展示自定义导航按键。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| uiContext18+ | Context | 否 | 是 | 以模应用方式显示身份认证对话框，仅支持在2in1设备上使用，如果没有此参数或其他类型的设备，身份认证对话框将以模系统方式显示。 默认以模系统方式显示身份认证对话框。 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |

#### UserAuthResult10+

用户认证结果。认证成功时，返回认证类型和认证成功的令牌信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | number | 否 | 否 | 用户认证结果。若成功返回SUCCESS，若失败返回相应错误码，参见UserAuthResultCode。 |
| token | Uint8Array | 否 | 是 | 认证成功时，返回认证成功的令牌信息。最大长度为1024字节。 |
| authType | UserAuthType | 否 | 是 | 认证成功时，返回认证类型。 |
| enrolledState12+ | EnrolledState | 否 | 是 | 认证成功时，返回注册凭据的状态。 |

#### IAuthCallback10+

返回认证结果的回调对象。

#### onResult10+

onResult(result: UserAuthResult): void

回调函数，返回认证结果。认证成功时，可以通过UserAuthResult获取到认证成功的令牌信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | UserAuthResult | 是 | 认证结果。 |

**示例1：**

发起用户认证，采用认证可信等级≥ATL3的锁屏口令认证，获取认证结果。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };

  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(`userAuthInstance callback result = ${JSON.stringify(result)}`);
    }
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

**示例2：**

发起用户认证，采用认证可信等级≥ATL3的锁屏口令+认证类型相关+复用设备解锁最大有效时长认证，获取认证结果。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

let reuseUnlockResult: userAuth.ReuseUnlockResult = {
  reuseMode: userAuth.ReuseMode.AUTH_TYPE_RELEVANT,
  reuseDuration: userAuth.MAX_ALLOWABLE_REUSE_DURATION,
}
try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
    reuseUnlockResult: reuseUnlockResult,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(`userAuthInstance callback result = ${JSON.stringify(result)}`);
    }
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

**示例3：**

发起用户认证，采用认证可信等级≥ATL3的锁屏口令+任意应用认证类型相关+复用任意应用最大有效时长认证，获取认证结果。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

let reuseUnlockResult: userAuth.ReuseUnlockResult = {
  reuseMode: userAuth.ReuseMode.CALLER_IRRELEVANT_AUTH_TYPE_RELEVANT,
  reuseDuration: userAuth.MAX_ALLOWABLE_REUSE_DURATION,
}
try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
    reuseUnlockResult: reuseUnlockResult,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(`userAuthInstance callback result = ${JSON.stringify(result)}`);
    }
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### AuthTipInfo20+

用户认证中间状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tipType | UserAuthType | 否 | 否 | 中间状态对应的认证类型。 |
| tipCode | UserAuthTipCode | 否 | 否 | 中间状态值。 |

#### AuthTipCallback20+

type AuthTipCallback = (authTipInfo: AuthTipInfo) => void

回调函数，返回认证中间状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authTipInfo | AuthTipInfo | 是 | 认证中间状态。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };

  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onAuthTip获取到认证中间状态。
  userAuthInstance.on('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info(`userAuthInstance callback authTipInfo = ${JSON.stringify(authTipInfo)}`);
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### UserAuthInstance10+

用于执行用户身份认证，并支持使用统一用户身份认证控件。

使用以下接口前，需先通过[getUserAuthInstance](#ZH-CN_TOPIC_0000002553361359__userauthgetuserauthinstance10)方法获取UserAuthInstance对象。

#### on10+

on(type: 'result', callback: IAuthCallback): void

订阅用户身份认证的最终结果。通过该接口获取到的是用户在认证控件完成身份认证交互后的最终身份认证结果。认证控件消失前，用户中间的认证失败尝试并不会通过该接口返回。如果需要感知整个认证过程中用户的每一次认证失败尝试，请通过[on('authTip')](#ZH-CN_TOPIC_0000002553361359__on20)接口订阅。


在PC/2in1设备上，应用如果使用模应用方式发起认证（即配置用户界面参数[widgetParam](#ZH-CN_TOPIC_0000002553361359__widgetparam10)时传入了有效的uiContext），收到认证结果后，若需弹出其他窗口，应先获取控件弹窗释放的标志消息，通过[on('authTip')](#ZH-CN_TOPIC_0000002553361359__on20)接口订阅控件释放消息（authTipInfo.tipCode = UserAuthTipCode.WIDGET_RELEASED）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'result' | 是 | 订阅事件类型，表明该事件用来返回认证结果。 |
| callback | IAuthCallback | 是 | 认证接口的回调函数，用于返回认证结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户认证错误码](用户认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
12500002General operation error.

**示例1：**

以模系统方式进行用户身份认证。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(`userAuthInstance callback result = ${JSON.stringify(result)}`);
    }
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

**示例2：**

以模应用方式进行用户身份认证。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

@Entry
@Component
struct Index {
  modelApplicationAuth(): void {
    try {
      const rand = cryptoFramework.createRandom();
      const len: number = 16;
      let randData: Uint8Array | null = null;
      let retryCount = 0;
      while(retryCount < 3){
        randData = rand?.generateRandomSync(len)?.data;
        if(randData){
          break;
        }
        retryCount++;
      }
      if(!randData){
        return;
      }
      const authParam: userAuth.AuthParam = {
        challenge: randData,
        authType: [userAuth.UserAuthType.PIN],
        authTrustLevel: userAuth.AuthTrustLevel.ATL3,
      };
      const uiContext: UIContext = this.getUIContext();
      const context: Context | undefined = uiContext.getHostContext();
      const widgetParam: userAuth.WidgetParam = {
        title: '请输入密码',
        uiContext: context,
      };
      const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
      console.info('get userAuth instance success');
      // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
      userAuthInstance.on('result', {
        onResult (result) {
          console.info(`userAuthInstance callback result = ${JSON.stringify(result)}`);
        }
      });
      console.info('auth on success');
      userAuthInstance.start();
      console.info('auth start success');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
    }

  build() {
    Column() {
      Button('start auth')
        .onClick(() => {
          this.modelApplicationAuth();
        })
    }
```

#### off10+

off(type: 'result', callback?: IAuthCallback): void

取消订阅用户身份认证的结果。


需要使用已经成功订阅事件的[UserAuthInstance](#ZH-CN_TOPIC_0000002553361359__userauthinstance10)对象调用该接口进行取消订阅。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'result' | 是 | 订阅事件类型，表明该事件用来返回认证结果。 |
| callback | IAuthCallback | 否 | 认证接口的回调函数，用于返回认证结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户认证错误码](用户认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
12500002General operation error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  userAuthInstance.off('result', {
    onResult (result) {
      console.info(`auth off result = ${JSON.stringify(result)}`);
    }
  });
  console.info('auth off success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### start10+

start(): void

开始认证。

每个UserAuthInstance只能进行一次认证，需要再次认证时，必须重新获取UserAuthInstance。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC 或 ohos.permission.USER_AUTH_FROM_BACKGROUND（仅向系统应用开放）

从API 20开始，仅系统应用可以通过申请ohos.permission.USER_AUTH_FROM_BACKGROUND，在后台发起认证。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户认证错误码](用户认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Possible causes: 1.No permission to access biometric. 2.No permission to start authentication from background. |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |
| 12500002 | General operation error. |
| 12500003 | Authentication canceled. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500009 | Authentication is locked out. |
| 12500010 | The type of credential has not been enrolled. |
| 12500011 | Switched to the customized authentication process. |
| 12500013 | Operation failed because of PIN expired. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### cancel10+

cancel(): void

取消认证。

此时UserAuthInstance必须是正在进行认证的对象。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |
12500002General operation error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam : userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能调用cancel()接口。
  userAuthInstance.start();
  console.info('auth start success');
  userAuthInstance.cancel();
  console.info('auth cancel success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### on20+

on(type: 'authTip', callback: AuthTipCallback): void

订阅身份认证过程中的提示信息。通过该接口可以获取到认证过程中控件的拉起和退出提示，以及认证过程中用户的每一次认证失败尝试。使用callback异步回调。


在PC/2in1设备上，应用如果使用模应用方式发起认证（即配置用户界面参数[widgetParam](#ZH-CN_TOPIC_0000002553361359__widgetparam10)时传入了有效的uiContext），收到认证结果后，若需弹出其他窗口，应先获取控件弹窗释放的标志消息，通过[on('authTip')](#ZH-CN_TOPIC_0000002553361359__on20)接口订阅控件释放消息（authTipInfo.tipCode = UserAuthTipCode.WIDGET_RELEASED）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件类型，支持的事件为'authTip'，当start()调用完成，发起身份认证，触发该事件。 |
| callback | AuthTipCallback | 是 | 认证接口的回调函数，用于返回认证中间状态。 |

**错误码：**

以下错误码的详细介绍请参见[用户认证错误码](用户认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12500002 | General operation error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onAuthTip获取到认证中间状态。
  userAuthInstance.on('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info(`userAuthInstance callback authTipInfo = ${JSON.stringify(authTipInfo)}`);
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### off20+

off(type: 'authTip', callback?: AuthTipCallback): void

取消订阅用户身份认证中间状态。


需要使用已经成功订阅事件的[UserAuthInstance](#ZH-CN_TOPIC_0000002553361359__userauthinstance10)对象调用该接口进行取消订阅。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型，支持的事件为'authTip'，当start()调用完成，发起身份认证并调用on()订阅该事件后，调用该方法可取消订阅，不会再触发该事件。 |
| callback | AuthTipCallback | 否 | 认证接口的回调函数，用于返回认证中间状态。 当不传该参数时默认值为调用on()接口时传递的参数值。 |

**错误码：**

以下错误码的详细介绍请参见[用户认证错误码](用户认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12500002 | General operation error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  userAuthInstance.off('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info(`userAuthInstance callback authTipInfo = ${JSON.stringify(authTipInfo)}`);
  });
  console.info('auth off success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### userAuth.getUserAuthInstance10+

getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance

获取[UserAuthInstance](#ZH-CN_TOPIC_0000002553361359__userauthinstance10)对象，执行用户身份认证，并支持使用统一用户身份认证控件。


每个UserAuthInstance只能进行一次认证，需要再次认证时，必须重新获取UserAuthInstance。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authParam | AuthParam | 是 | 用户认证相关参数。 |
| widgetParam | WidgetParam | 是 | 用户认证界面配置相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| UserAuthInstance | 支持用户界面的认证器对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户认证错误码](用户认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### AuthResultInfo(deprecated)

表示认证结果信息，用于描述认证结果。


从 API version 9 开始支持，从 API version 11 开始废弃，请使用[UserAuthResult](#ZH-CN_TOPIC_0000002553361359__userauthresult10)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | number | 否 | 否 | 认证结果。 |
| token | Uint8Array | 否 | 是 | 用户身份认证通过的凭证。 |
| remainAttempts | number | 否 | 是 | 剩余的认证尝试次数。 |
| lockoutDuration | number | 否 | 是 | 认证操作的锁定时长，时间单位为毫秒ms。 |

#### TipInfo(deprecated)

表示认证过程中的提示信息，用于提供认证过程的反馈。


从 API version 9 开始支持，从 API version 11 开始废弃，请使用[AuthTipInfo](#ZH-CN_TOPIC_0000002553361359__authtipinfo20)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| module | number | 否 | 否 | 发送提示信息的模块标识。 |
| tip | number | 否 | 否 | 认证过程提示信息。 |

#### EventInfo(deprecated)

type EventInfo = AuthResultInfo | TipInfo

表示认证过程中事件信息的类型。

该类型为下表类型取值中的联合类型。


从 API version 9 开始支持，从 API version 11 开始废弃，请使用[UserAuthResult](#ZH-CN_TOPIC_0000002553361359__userauthresult10)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| --- | --- |
| AuthResultInfo | 获取到的认证结果信息。 |
| TipInfo | 认证过程中的提示信息。 |

#### AuthEventKey(deprecated)

type AuthEventKey = 'result' | 'tip'

表示认证事件类型的关键字，作为[on](#ZH-CN_TOPIC_0000002553361359__ondeprecated)接口的参数。

该类型为下表类型取值中的联合类型。

从 API version 9 开始支持，从 API version 11 开始废弃。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| --- | --- |
| 'result' | on接口第一个参数为"result"时，callback回调返回认证的结果信息。 |
| 'tip' | on接口第一个参数为"tip"时，callback回调返回认证操作中的提示信息。 |

#### AuthEvent(deprecated)

认证接口的异步回调对象。


从 API version 9 开始支持，从 API version 11 开始废弃，请使用[IAuthCallback](#ZH-CN_TOPIC_0000002553361359__iauthcallback10)替代。

#### callback(deprecated)

callback(result : EventInfo) : void

通过该回调获取认证结果信息或认证过程中的提示信息。


从 API version 9 开始支持，从 API version 11 开始废弃，请使用[onResult](#ZH-CN_TOPIC_0000002553361359__onresult10)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | EventInfo | 是 | 返回的认证结果信息或提示信息。 |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
// 通过callback获取认证结果。
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(`authV9 result ${result.result}`);
      console.info(`authV9 token ${result.token}`);
      console.info(`authV9 remainAttempts ${result.remainAttempts}`);
      console.info(`authV9 lockoutDuration ${result.lockoutDuration}`);
    }
  } as userAuth.AuthEvent);
  auth.start();
  console.info('authV9 start success');
} catch (error) {
  console.error(`authV9 error = ${error}`);
  // do error.
}
// 通过callback获取认证过程中的提示信息。
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.on('tip', {
    callback : (result : userAuth.TipInfo) => {
      switch (result.tip) {
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_BRIGHT:
          // do something;
          break;
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_DARK:
          // do something;
          break;
        default:
          // do others.
      }
  } as userAuth.AuthEvent);
  auth.start();
  console.info('authV9 start success');
} catch (error) {
  console.error(`authV9 error = ${error}`);
  // do error.
}
```

#### AuthInstance(deprecated)

执行用户认证的对象。


从 API version 9 开始支持，从 API version 10 开始废弃，请使用[UserAuthInstance](#ZH-CN_TOPIC_0000002553361359__userauthinstance10)替代。

#### on(deprecated)

on : (name : AuthEventKey, callback : AuthEvent) => void

订阅指定类型的用户认证事件。


从 API version 9 开始支持，从 API version 10 开始废弃，请使用[on](#ZH-CN_TOPIC_0000002553361359__on10)替代。

使用获取到的[AuthInstance](#ZH-CN_TOPIC_0000002553361359__authinstancedeprecated)对象调用该接口进行订阅。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | AuthEventKey | 是 | 表示认证事件类型，取值为"result"时，回调函数返回认证结果；取值为"tip"时，回调函数返回认证过程中的提示信息。 |
| callback | AuthEvent | 是 | 认证接口的回调函数，用于返回认证结果或认证过程中的提示信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户认证错误码](用户认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  // 订阅认证结果。
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(`authV9 result ${result.result}`);
      console.info(`authV9 token ${result.token}`);
      console.info(`authV9 remainAttempts ${result.remainAttempts}`);
      console.info(`authV9 lockoutDuration ${result.lockoutDuration}`);
    }
  });
  // 订阅认证过程中的提示信息。
  auth.on('tip', {
    callback : (result : userAuth.TipInfo) => {
      switch (result.tip) {
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_BRIGHT:
          // do something;
          break;
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_DARK:
          // do something;
          break;
        default:
          // do others.
      }
  } as userAuth.AuthEvent);
  auth.start();
  console.info('authV9 start success');
} catch (error) {
  console.error(`authV9 error = ${error}`);
  // do error.
}
```

#### off(deprecated)

off : (name : AuthEventKey) => void

取消订阅特定类型的认证事件。


从 API version 9 开始支持，从 API version 10 开始废弃，请使用[off](#ZH-CN_TOPIC_0000002553361359__off10)替代。

需要使用已经成功订阅事件的[AuthInstance](#ZH-CN_TOPIC_0000002553361359__authinstancedeprecated)对象调用该接口进行取消订阅。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | AuthEventKey | 是 | 表示认证事件类型，取值为"result"时，取消订阅认证结果；取值为"tip"时，取消订阅认证过程中的提示信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户认证错误码](用户认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  // 订阅认证结果。
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(`authV9 result ${result.result}`);
      console.info(`authV9 token ${result.token}`);
      console.info(`authV9 remainAttempts ${result.remainAttempts}`);
      console.info(`authV9 lockoutDuration ${result.lockoutDuration}`);
    }
  });
  // 取消订阅结果。
  auth.off('result');
  console.info('cancel subscribe authentication event success');
} catch (error) {
  console.error(`cancel subscribe authentication event failed, error = ${error}`);
  // do error.
}
```

#### start(deprecated)

start : () => void

开始认证。


从 API version 9 开始支持，从 API version 10 开始废弃，请使用[start](#ZH-CN_TOPIC_0000002553361359__start10)替代。

使用获取到的[AuthInstance](#ZH-CN_TOPIC_0000002553361359__authinstancedeprecated)对象调用该接口进行认证。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户认证错误码](用户认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 12500001 | Authentication failed. |
| 12500002 | General operation error. |
| 12500003 | The operation is canceled. |
| 12500004 | The operation is time-out. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500007 | The authentication task is busy. |
| 12500009 | The authenticator is locked. |
| 12500010 | The type of credential has not been enrolled. |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.start();
  console.info('authV9 start auth success');
} catch (error) {
  console.error(`authV9 start auth failed, error = ${error}`);
}
```

#### cancel(deprecated)

cancel : () => void

取消认证。


从 API version 9 开始支持，从 API version 10 开始废弃，请使用[cancel](#ZH-CN_TOPIC_0000002553361359__cancel10)替代。

使用获取到的[AuthInstance](#ZH-CN_TOPIC_0000002553361359__authinstancedeprecated)对象调用该接口进行取消认证，此[AuthInstance](#ZH-CN_TOPIC_0000002553361359__authinstancedeprecated)需要是正在进行认证的对象。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户认证错误码](用户认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.cancel();
  console.info('cancel auth success');
} catch (error) {
  console.error(`cancel auth failed, error = ${error}`);
}
```

#### userAuth.getAuthInstance(deprecated)

getAuthInstance(challenge : Uint8Array, authType : UserAuthType, authTrustLevel : AuthTrustLevel): AuthInstance

获取AuthInstance对象，用于执行用户身份认证。


从 API version 9 开始支持，从 API version 10 开始废弃，请使用[getUserAuthInstance](#ZH-CN_TOPIC_0000002553361359__userauthgetuserauthinstance10)替代。

每个AuthInstance只能进行一次认证，若需要再次进行认证则需重新获取AuthInstance。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| challenge | Uint8Array | 是 | 挑战值，最大长度为32字节，可以传Uint8Array([])。 |
| authType | UserAuthType | 是 | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | AuthTrustLevel | 是 | 认证信任等级。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AuthInstance | 认证器对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户认证错误码](用户认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  console.info('let auth instance success');
} catch (error) {
  console.error(`get auth instance success failed, error = ${error}`);
}
```

#### userAuth.getAvailableStatus9+

getAvailableStatus(authType : UserAuthType, authTrustLevel : AuthTrustLevel): void

查询指定类型和等级的认证能力是否支持。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authType | UserAuthType | 是 | 认证类型。从 API version 11 开始支持PIN查询。 |
| authTrustLevel | AuthTrustLevel | 是 | 认证信任等级。 |


如果未注册对应执行器，系统不支持该认证能力，需返回12500005。

如果已注册对应执行器，功能未禁用，但认证安全等级低于业务指定时，需返回12500006。

如果已注册对应执行器，功能未禁用，但用户未注册凭据时，需返回12500010。

如果已注册对应执行器，功能未禁用，但密码过期时，需返回12500013。

若用户注册的锁屏口令是4位PIN时，其认证可信等级为ATL3，调用该接口查询是否支持ATL4级别的密码认证时，需返回12500010。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户认证错误码](用户认证错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500010 | The type of credential has not been enrolled. |
| 12500013 | Operation failed because of PIN expired. |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL3);
  console.info('current auth trust level is supported');
} catch (error) {
  console.error(`current auth trust level is not supported, error = ${error}`);
}
```

#### UserAuthResultCode9+

表示返回码的枚举。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 12500000 | 执行成功。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| FAIL | 12500001 | 认证失败。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| GENERAL_ERROR | 12500002 | 操作通用错误。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| CANCELED | 12500003 | 认证取消。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| TIMEOUT | 12500004 | 认证超时。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| TYPE_NOT_SUPPORT | 12500005 | 认证类型不支持。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| TRUST_LEVEL_NOT_SUPPORT | 12500006 | 认证等级不支持。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| BUSY | 12500007 | 系统繁忙。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| INVALID_PARAMETERS20+ | 12500008 | 参数校验失败。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| LOCKED | 12500009 | 认证器已锁定。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| NOT_ENROLLED | 12500010 | 用户未录入指定的系统身份认证凭据。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| CANCELED_FROM_WIDGET10+ | 12500011 | 用户取消了系统认证方式，选择应用自定义认证。需调用者拉起自定义认证界面。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| PIN_EXPIRED12+ | 12500013 | 当前的认证操作执行失败。返回这个错误码，表示系统锁屏口令过期。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

#### UserAuth(deprecated)

认证器对象。

#### constructor(deprecated)

constructor()

创建认证器对象。


从 API version 8 开始支持，从 API version 9 开始废弃，请使用[getAuthInstance](#ZH-CN_TOPIC_0000002553361359__userauthgetauthinstancedeprecated)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
```

#### getVersion(deprecated)

getVersion() : number

获取认证器的版本信息。

从 API version 8 开始支持，从 API version 9 开始废弃。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 认证器版本信息。 |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let version = auth.getVersion();
console.info(`auth version = ${version}`);
```

#### getAvailableStatus(deprecated)

getAvailableStatus(authType : UserAuthType, authTrustLevel : AuthTrustLevel) : number

查询指定类型和等级的认证能力是否支持。


从 API version 8 开始支持，从 API version 9 开始废弃，请使用[getAvailableStatus](#ZH-CN_TOPIC_0000002553361359__userauthgetavailablestatus9)替代。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authType | UserAuthType | 是 | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | AuthTrustLevel | 是 | 认证信任等级。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 查询结果，结果为SUCCESS时表示支持，其他返回值参见ResultCode。 |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let checkCode = auth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1);
if (checkCode == userAuth.ResultCode.SUCCESS) {
  console.info('check auth support success');
} else {
  console.error(`check auth support fail, code = ${checkCode}`);
}
```

#### auth(deprecated)

auth(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel, callback: IUserAuthCallback): Uint8Array

执行用户认证，使用回调函数返回结果。


从 API version 8 开始支持，从 API version 9 开始废弃，请使用[start](#ZH-CN_TOPIC_0000002553361359__startdeprecated)代替。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| challenge | Uint8Array | 是 | 挑战值，可以传Uint8Array([])。 |
| authType | UserAuthType | 是 | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | AuthTrustLevel | 是 | 认证信任等级。 |
| callback | IUserAuthCallback | 是 | 回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | ContextId，作为取消认证cancelAuth接口的入参。 |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      console.info(`auth onResult extraInfo = ${JSON.stringify(extraInfo)}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // 此处添加认证成功逻辑。
      } else {
        // 此处添加认证失败逻辑。
      }
    } catch (error) {
      console.error(`auth onResult error = ${error}`);
    }
});
```

#### cancelAuth(deprecated)

cancelAuth(contextID : Uint8Array) : number

表示通过contextID取消本次认证。


从 API version 8 开始支持，从 API version 9 开始废弃，请使用[cancel](#ZH-CN_TOPIC_0000002553361359__canceldeprecated)代替。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contextID | Uint8Array | 是 | 上下文的标识，通过auth接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 取消认证的结果，结果为SUCCESS时表示取消成功，其他返回值参见ResultCode。 |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

// contextId可通过auth接口获取，此处直接定义。
let contextId = new Uint8Array([0, 1, 2, 3, 4, 5, 6, 7]);
let auth = new userAuth.UserAuth();
let cancelCode = auth.cancelAuth(contextId);
if (cancelCode == userAuth.ResultCode.SUCCESS) {
  console.info('cancel auth success');
} else {
  console.error('cancel auth fail');
}
```

#### IUserAuthCallback(deprecated)

返回认证结果的回调对象。


从 API version 8 开始支持，从 API version 9 开始废弃，请使用[AuthEvent](#ZH-CN_TOPIC_0000002553361359__autheventdeprecated)代替。

#### onResult(deprecated)

onResult: (result : number, extraInfo : AuthResult) => void

回调函数，返回认证结果。


从 API version 8 开始支持，从 API version 9 开始废弃，请使用[callback](#ZH-CN_TOPIC_0000002553361359__callbackdeprecated)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | number | 是 | 认证结果，参见ResultCode。 |
| extraInfo | AuthResult | 是 | 扩展信息，不同情况下的具体信息， 如果身份验证通过，则在extraInfo中返回用户认证令牌， 如果身份验证失败，则在extraInfo中返回剩余的用户认证次数， 如果身份验证执行器被锁定，则在extraInfo中返回冻结时间。 |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      console.info(`auth onResult extraInfo = ${JSON.stringify(extraInfo)}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // 此处添加认证成功逻辑。
      }  else {
        // 此处添加认证失败逻辑。
      }
    } catch (error) {
      console.error(`auth onResult error = ${error}`);
    }
});
```

#### onAcquireInfo(deprecated)

onAcquireInfo ?: (module : number, acquire : number, extraInfo : any) => void

回调函数，返回认证过程中的提示信息，非必须实现。


从 API version 8 开始支持，从 API version 9 开始废弃，请使用[callback](#ZH-CN_TOPIC_0000002553361359__callbackdeprecated)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| module | number | 是 | 发送提示信息的模块标识。 |
| acquire | number | 是 | 认证执过程中的提示信息。 |
| extraInfo | any | 是 | 预留字段。 |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      console.info(`auth onResult extraInfo = ${JSON.stringify(extraInfo)}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // 此处添加认证成功逻辑。
      }  else {
        // 此处添加认证失败逻辑。
      }
    } catch (error) {
      console.error(`auth onResult error = ${error}`);
    }
  },
  onAcquireInfo: (module, acquire, extraInfo : userAuth.AuthResult) => {
    try {
      console.info(`auth onAcquireInfo module = ${module}`);
      console.info(`auth onAcquireInfo acquire = ${acquire}`);
      console.info(`auth onAcquireInfo extraInfo = ${JSON.stringify(extraInfo)}`);
    } catch (error) {
      console.error(`auth onAcquireInfo error = ${error}`);
    }
});
```

#### AuthResult(deprecated)

表示认证结果的对象。


从 API version 8 开始支持，从 API version 9 开始废弃，请使用[AuthResultInfo](#ZH-CN_TOPIC_0000002553361359__authresultinfodeprecated)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| token | Uint8Array | 否 | 是 | 认证成功的令牌信息。 |
| remainTimes | number | 否 | 是 | 剩余的认证操作次数。 |
| freezingTime | number | 否 | 是 | 认证操作的冻结时间。 |

#### ResultCode(deprecated)

表示返回码的枚举。


从 API version 8 开始支持，从 API version 9 开始废弃，请使用[UserAuthResultCode](#ZH-CN_TOPIC_0000002553361359__userauthresultcode9)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 执行成功。 |
| FAIL | 1 | 认证失败。 |
| GENERAL_ERROR | 2 | 操作通用错误。 |
| CANCELED | 3 | 操作取消。 |
| TIMEOUT | 4 | 操作超时。 |
| TYPE_NOT_SUPPORT | 5 | 不支持的认证类型。 |
| TRUST_LEVEL_NOT_SUPPORT | 6 | 不支持的认证等级。 |
| BUSY | 7 | 忙碌状态。 |
| INVALID_PARAMETERS | 8 | 无效参数。 |
| LOCKED | 9 | 认证器已锁定。 |
| NOT_ENROLLED | 10 | 用户未录入认证信息。 |

#### FaceTips(deprecated)

表示人脸认证过程中提示码的枚举。

从 API version 8 开始支持，从 API version 11 开始废弃。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FACE_AUTH_TIP_TOO_BRIGHT | 1 | 光线太强，获取的图像太亮。 |
| FACE_AUTH_TIP_TOO_DARK | 2 | 光线太暗，获取的图像太暗。 |
| FACE_AUTH_TIP_TOO_CLOSE | 3 | 人脸距离设备过近。 |
| FACE_AUTH_TIP_TOO_FAR | 4 | 人脸距离设备过远。 |
| FACE_AUTH_TIP_TOO_HIGH | 5 | 设备太高，仅获取到人脸上部。 |
| FACE_AUTH_TIP_TOO_LOW | 6 | 设备太低，仅获取到人脸下部。 |
| FACE_AUTH_TIP_TOO_RIGHT | 7 | 设备太靠右，仅获取到人脸右部。 |
| FACE_AUTH_TIP_TOO_LEFT | 8 | 设备太靠左，仅获取到人脸左部。 |
| FACE_AUTH_TIP_TOO_MUCH_MOTION | 9 | 在图像采集过程中，用户人脸移动太快。 |
| FACE_AUTH_TIP_POOR_GAZE | 10 | 没有正视摄像头。 |
| FACE_AUTH_TIP_NOT_DETECTED | 11 | 没有检测到人脸信息。 |

#### FingerprintTips(deprecated)

表示指纹认证过程中提示码的枚举。

从 API version 8 开始支持，从 API version 11 开始废弃。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FINGERPRINT_AUTH_TIP_GOOD | 0 | 获取的指纹图像良好。 |
| FINGERPRINT_AUTH_TIP_DIRTY | 1 | 由于传感器上可疑或检测到的污垢，指纹图像噪音过大。 |
| FINGERPRINT_AUTH_TIP_INSUFFICIENT | 2 | 由于检测到的情况，指纹图像噪声太大，无法处理。 |
| FINGERPRINT_AUTH_TIP_PARTIAL | 3 | 仅检测到部分指纹图像。 |
| FINGERPRINT_AUTH_TIP_TOO_FAST | 4 | 快速移动，指纹图像不完整。 |
| FINGERPRINT_AUTH_TIP_TOO_SLOW | 5 | 缺少运动，指纹图像无法读取。 |

#### UserAuthType8+

表示身份认证的凭据类型枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PIN10+ | 1 | 口令认证。 |
| FACE | 2 | 人脸认证。 |
| FINGERPRINT | 4 | 指纹认证。 |

#### AuthTrustLevel8+

表示认证结果的信任等级枚举。

典型场景及举例可参考[认证可信等级划分原则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-authentication-overview#生物认证可信等级划分原则)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ATL1 | 10000 | 认证结果的信任等级级别1，表示该认证方案能够识别用户个体，具备一定的活体检测能力。适用于业务风控、一般个人数据查询等场景。 |
| ATL2 | 20000 | 认证结果的信任等级级别2，表示该认证方案能够精确识别用户个体，具备一定的活体检测能力。适用于维持设备解锁状态、应用登录等场景。 |
| ATL3 | 30000 | 认证结果的信任等级级别3，表示该认证方案能够精确识别用户个体，具备较强的活体检测能力。适用于设备解锁等场景。 |
| ATL4 | 40000 | 认证结果的信任等级级别4，表示该认证方案能够高精度的识别用户个体，具备很强的活体检测能力。适用于小额支付等场景。 |

#### SecureLevel(deprecated)

type SecureLevel = string

表示认证的安全级别。


从 API version 6 开始支持，从 API version 8 开始废弃，请使用[AuthTrustLevel](#ZH-CN_TOPIC_0000002553361359__authtrustlevel8)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| --- | --- |
| string | 表示类型为字符，认证的安全级别包括：'S1' | 'S2'|'S3'|'S4'。 - 'S1'：认证结果的信任等级级别1，代表该认证方案能够识别用户个体，有一定的活体检测能力。常用的业务场景有业务风控、一般个人数据查询等。 - 'S2'：认证结果的信任等级级别2，代表该认证方案能够精确识别用户个体，有一定的活体检测能力。常用的业务场景有维持设备解锁状态，应用登录等。 - 'S3'：认证结果的信任等级级别3，代表该认证方案能够精确识别用户个体，有较强的活体检测能力。常用的业务场景有设备解锁等。 - 'S4'：认证结果的信任等级级别4，代表该认证方案能够高精度的识别用户个体，有很强的活体检测能力。常用的业务场景有小额支付等。 |

#### AuthType(deprecated)

type AuthType = string

表示认证类型。


从 API version 6 开始支持，从 API version 8 开始废弃，请使用[UserAuthType](#ZH-CN_TOPIC_0000002553361359__userauthtype8)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| --- | --- |
| string | 表示认证类型为字符，认证类型包括：'ALL'|'FACE_ONLY'。 - 'ALL'：预留参数，当前版本暂不支持ALL类型的认证。 - 'FACE_ONLY'：人脸认证。 |

#### userAuth.getAuthenticator(deprecated)

getAuthenticator(): Authenticator

获取Authenticator对象，用于执行用户身份认证。


从 API version 6 开始支持，从 API version 8 开始废弃，请使用[getAuthInstance](#ZH-CN_TOPIC_0000002553361359__userauthgetauthinstancedeprecated)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Authenticator | 认证器对象。 |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let authenticator = userAuth.getAuthenticator();
```

#### Authenticator(deprecated)

认证器对象。


从 API version 6 开始支持，从 API version 8 开始废弃，请使用[AuthInstance](#ZH-CN_TOPIC_0000002553361359__authinstancedeprecated)替代。

#### execute(deprecated)

execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void

执行用户认证，使用callback方式作为异步方法。


从 API version 6 开始支持，从 API version 8 开始废弃，请使用[start](#ZH-CN_TOPIC_0000002553361359__startdeprecated)替代。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | AuthType | 是 | 认证类型，当前只支持"FACE_ONLY"。 ALL为预留参数。当前版本暂不支持ALL类型的认证。 |
| level | SecureLevel | 是 | 安全级别，对应认证的安全级别，有效值为"S1"（最低）、"S2"、"S3"、"S4"（最高）。 具备3D人脸识别能力的设备支持"S3"及以下安全级别的认证。 具备2D人脸识别能力的设备支持"S2"及以下安全级别的认证。 |
| callback | AsyncCallback<number> | 是 | 回调函数。number表示认证结果，参见AuthenticationResult。 |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

let authenticator = userAuth.getAuthenticator();
authenticator.execute('FACE_ONLY', 'S2', (error, code)=>{
  if (code === userAuth.ResultCode.SUCCESS) {
    console.info('auth success');
    return;
  }
  console.error(`auth fail, code = ${code}`);
});
```

#### execute(deprecated)

execute(type : AuthType, level : SecureLevel): Promise<number>

执行用户认证，使用promise方式作为异步方法。


从 API version 6 开始支持，从 API version 8 开始废弃，请使用[start](#ZH-CN_TOPIC_0000002553361359__startdeprecated)替代。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | AuthType | 是 | 认证类型，当前只支持"FACE_ONLY"。 ALL为预留参数。当前版本暂不支持ALL类型的认证。 |
| level | SecureLevel | 是 | 安全级别，对应认证的安全级别，有效值为"S1"（最低）、"S2"、"S3"、"S4"（最高）。 具备3D人脸识别能力的设备支持"S3"及以下安全级别的认证。 具备2D人脸识别能力的设备支持"S2"及以下安全级别的认证。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回携带一个number的Promise。number 为认证结果，参见AuthenticationResult。 |

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  let authenticator = userAuth.getAuthenticator();
  authenticator.execute('FACE_ONLY', 'S2').then((code)=>{
    console.info('auth success');
  })
} catch (error) {
  console.error(`auth fail, code = ${error}`);
}
```

#### AuthenticationResult(deprecated)

表示认证结果的枚举。


从 API version 6 开始支持，从 API version 8 开始废弃，请使用[ResultCode](#ZH-CN_TOPIC_0000002553361359__resultcodedeprecated)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO_SUPPORT | -1 | 设备不支持当前的认证方式。 |
| SUCCESS | 0 | 认证成功。 |
| COMPARE_FAILURE | 1 | 比对失败。 |
| CANCELED | 2 | 用户取消认证。 |
| TIMEOUT | 3 | 认证超时。 |
| CAMERA_FAIL | 4 | 开启相机失败。 |
| BUSY | 5 | 认证服务忙，请稍后重试。 |
| INVALID_PARAMETERS | 6 | 认证参数无效。 |
| LOCKED | 7 | 认证失败次数过多，已锁定。 |
| NOT_ENROLLED | 8 | 未录入认证凭据。 |
| GENERAL_ERROR | 100 | 其他错误。 |