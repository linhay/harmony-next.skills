# TrustedAuthentication（数字盾服务）

本模块提供数字盾密码创建、修改、删除、交易认证，开通生物特征（3D人脸/指纹）交易认证能力、生物特征交易认证，密钥信息导入导出相关接口，金融应用可以使用对应接口，支撑数字盾业务开发。

**起始版本：**6.0.0(20)

#### 导入模块

```ets
import { trustedAuthentication } from '@kit.DeviceSecurityKit';
```

#### enableTrustedAuthentication

enableTrustedAuthentication(challenge: Uint8Array, pwdInfo: PasswordInfo, label: TUILable): Promise<AuthInfo>

拉起TUI（Trusted User Interface）界面并指引用户创建数字盾密码。使用Promise异步回调。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**参数**：

参数名

类型

必填

说明

challenge

Uint8Array

是

在发起请求之前通过[Universal Keystore Kit初始化会话](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksinitsession9)获取的challenge值，参数规格为32字节随机数。

pwdInfo

[PasswordInfo](#section1550072910133)

是

密码对应的定制信息，详细信息参考PasswordInfo。

label

[TUILable](#section125211933134315)

是

用于TUI界面展示时的定制信息，详见TUILable。

**返回值：**

类型

说明

Promise<[AuthInfo](#section1214193712473)>

Promise对象，返回开通数字盾密码对应的authID和authToken信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAuthentication （数字盾服务）.md)**。**

错误码ID

错误信息

1019100001

The interface invoker does not have the corresponding permission.

1019100002

Parameter error.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1019100007

Unsupported custom image.

1019100008

The user canceled the operation.

1019100011

The title text cannot be displayed.

1019100013

Failed to set the password.

**示例：**

```ets
import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";
try {
  const rand = cryptoFramework.createRandom();
  const len: number = 32;
  const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
  const passwordInfo: trustedAuthentication.PasswordInfo = {
    pwdType: trustedAuthentication.PasswordType.PASSWORD_TYPE_MIXED,
    pwdMaxLength: 10,
    pwdMinLength: 6,
    maxAuthFailCount: 6
  };
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png');
  const buffer = fileData.buffer;
  const label:trustedAuthentication.TUILable = {
    image: buffer as ArrayBuffer,
    title: "开通数字盾",
  }
  const authToken = await trustedAuthentication.enableTrustedAuthentication(challenge, passwordInfo, label);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'enableTrustedAuthentication failed: %{public}d %{public}s', e.code, e.message);
}
```

#### modifyTrustedAuthenticationPwd

modifyTrustedAuthenticationPwd(challenge: Uint8Array, pwdInfo: PasswordInfo, authID: bigint, label: TUILable): Promise<AuthToken>

拉起TUI界面并指引用户修改数字盾密码，修改密码前会根据authID进行对应密码认证。使用Promise异步回调。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**参数**：

参数名

类型

必填

说明

challenge

Uint8Array

是

在发起请求之前通过[Universal Keystore Kit初始化会话](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksinitsession9)获取的challenge值，参数规格为32字节随机数。

pwdInfo

[PasswordInfo](#section1550072910133)

是

密码对应的定制信息。

authID

bigint

是

密码创建时获取的authID信息。

label

[TUILable](#section125211933134315)

是

用于TUI界面展示时的定制信息。

**返回值：**

类型

说明

Promise<[AuthToken](#section20919104010476)>

Promise对象，返回修改数字盾密码对应的authToken信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAuthentication （数字盾服务）.md)**。**

错误码ID

错误信息

1019100001

The interface invoker does not have the corresponding permission.

1019100002

Parameter error.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1019100003

The maximum number of password authentication attempts has been reached.

1019100005

Face/Fingerprint/Password authentication failed.

1019100007

Unsupported custom image.

1019100008

The user canceled the operation.

1019100011

The title text cannot be displayed.

1019100012

Invalid authentication ID.

1019100014

Failed to change the password.

**示例：**

```ets
import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const rand = cryptoFramework.createRandom();
 const len: number = 32;
 const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
 const passwordInfo: trustedAuthentication.PasswordInfo = {
   pwdType: trustedAuthentication.PasswordType.PASSWORD_TYPE_DIGITAL,
   pwdMaxLength: 10,
   pwdMinLength: 6,
   maxAuthFailCount: 6,
 };
 const authID: bigint = 1687413472599354502n;
 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
 const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
 const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png');
 const buffer = fileData.buffer;
 const label:trustedAuthentication.TUILable = {
   image: buffer as ArrayBuffer,
   title: "修改密码",
 }
 const authToken = await trustedAuthentication.modifyTrustedAuthenticationPwd(challenge, passwordInfo, authID, label);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'modifyTrustedAuthenticationPwd failed: %{public}d %{public}s', e.code, e.message);
}
```

#### disableTrustedAuthentication

disableTrustedAuthentication(challenge: Uint8Array, needAuth: boolean, authID: bigint, label: TUILable): Promise<AuthToken>

关闭数字盾服务，开发者可通过参数needAuth控制密码关闭前是否需要密码认证。使用Promise异步回调。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**参数**：

参数名

类型

必填

说明

challenge

Uint8Array

是

当needAuth为true时，在发起请求之前通过[Universal Keystore Kit初始化会话](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksinitsession9)获取的challenge值，参数规格为32字节随机数。

当needAuth为false时，该值可不从Universal Keystore Kit获取，challenge值为任意32字节数即可。

needAuth

boolean

是

是否需要进行密码认证标识。

当值为false时，表示不进行密码认证发起的数字盾服务关闭场景。

当值为true时，表示需要进行密码认证，密码认证通过后才可关闭数字盾服务。

authID

bigint

是

密码创建时获取的authID信息。

label

[TUILable](#section125211933134315)

是

用于TUI界面展示时的定制信息。

**返回值：**

类型

说明

Promise<[AuthToken](#section20919104010476)>

Promise对象，返回删除数字盾密码对应的authToken信息，当needAuth为false时，返回的authToken信息为全0无效的authToken。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAuthentication （数字盾服务）.md)**。**

错误码ID

错误信息

1019100001

The interface invoker does not have the corresponding permission.

1019100002

Parameter error.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1019100003

The maximum number of password authentication attempts has been reached.

1019100004

Failed to delete the password.

1019100005

Face/Fingerprint/Password authentication failed.

1019100007

Unsupported custom image.

1019100008

The user canceled the operation.

1019100011

The title text cannot be displayed.

1019100012

Invalid authentication ID.

**示例：**

```ets
import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const rand = cryptoFramework.createRandom();
 const len: number = 32;
 const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
 const authID: bigint = 1687413472599354502n;
 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
 const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
 const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png');
 const buffer = fileData.buffer;
 const label:trustedAuthentication.TUILable = {
   image: buffer as ArrayBuffer,
   title: "关闭数字盾",
 }
 const authToken = await trustedAuthentication.disableTrustedAuthentication(challenge, true, authID, label);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'disableTrustedAuthentication failed: %{public}d %{public}s', e.code, e.message);
}
```

#### trustedAuthentication

trustedAuthentication(challenge: Uint8Array, authID: bigint, label: TUILable): Promise<AuthToken>

提供数字盾密码认证能力，开发者可使用该接口完成绑定生物特征支付前的密码认证。使用Promise异步回调。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**参数**：

参数名

类型

必填

说明

challenge

Uint8Array

是

在发起请求之前通过[Universal Keystore Kit初始化会话](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksinitsession9)获取的challenge值，参数规格为32字节随机数。

authID

bigint

是

密码创建时获取的authID信息。

label

[TUILable](#section125211933134315)

是

用于TUI界面展示时的定制信息。

**返回值：**

类型

说明

Promise<[AuthToken](#section20919104010476)>

Promise对象，返回数字盾密码认证对应的authToken信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAuthentication （数字盾服务）.md)**。**

错误码ID

错误信息

1019100001

The interface invoker does not have the corresponding permission.

1019100002

Parameter error.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1019100003

The maximum number of password authentication attempts has been reached.

1019100005

Face/Fingerprint/Password authentication failed.

1019100007

Unsupported custom image.

1019100008

The user canceled the operation.

1019100012

Invalid authentication ID.

**示例：**

```ets
import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const rand = cryptoFramework.createRandom();
 const len: number = 32;
 const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
 const authID: bigint = 1687413472599354502n;
 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
 const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
 const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png');
 const buffer = fileData.buffer;
 const label:trustedAuthentication.TUILable = {
   image: buffer as ArrayBuffer,
   title: "密码认证",
 }
 const authToken = await trustedAuthentication.trustedAuthentication(challenge, authID, label);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'trustedAuthentication failed: %{public}d %{public}s', e.code, e.message);
}
```

#### procContentAuthentication

procContentAuthentication(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken>

数字盾交易认证接口。使用Promise异步回调。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**参数**：

参数名

类型

必填

说明

challenge

Uint8Array

是

在发起请求之前通过[Universal Keystore Kit初始化会话](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks#huksinitsession9)获取的challenge值，参数规格为32字节随机数。

authID

bigint

是

密码创建时获取的authID信息。

authMsg

[AuthReqParams](#section3989356115014)

是

交易认证请求相关参数。

label

[TUILable](#section125211933134315)

是

用于TUI界面展示时的定制信息。

**返回值：**

类型

说明

Promise<[AuthToken](#section20919104010476)>

Promise对象。

当使用密码认证时，返回结果包括交易数据信息的authToken。

当使用生物特征进行认证时，返回结果为临时authToken，在经过生物认证通过后，需使用[getBiometricAuthToken](#section627215120542)获取正式签发的包含交易信息的authToken。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAuthentication （数字盾服务）.md)**。**

错误码ID

错误信息

1019100001

The interface invoker does not have the corresponding permission.

1019100002

Parameter error.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1019100005

Face/Fingerprint/Password authentication failed.

1019100008

The user canceled the operation.

1019100011

The text content cannot be displayed.

1019100012

Invalid authentication ID.

1019100021

The corresponding biometric data has not been bound.

**示例：**

```ets
import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const rand = cryptoFramework.createRandom();
 const len: number = 32;
 const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;
 const authID: bigint = 1687413472599354502n;
 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
 const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
 const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png');
 const reqParams:trustedAuthentication.AuthReqParams = {
  reqType: trustedAuthentication.AuthType.AUTH_TYPE_TUI_PIN,
  authContent: ["用户：王xx", "账号：95588180804408xxxx", "交易金额：1000000000"],
 }
 const buffer = fileData.buffer;
 const label:trustedAuthentication.TUILable = {
  image: buffer as ArrayBuffer,
  title: "密码交易认证",
 }
 const result = await trustedAuthentication.procContentAuthentication(challenge, authID, reqParams, label);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'procContentAuthentication failed: %{public}d %{public}s', e.code, e.message);
}
```

#### getBiometricAuthToken

getBiometricAuthToken(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken>

获取生物特征绑定/生物特征交易认证对应的authToken信息。使用Promise异步回调。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**参数**：

参数名

类型

必填

说明

operType

[OperateType](#section14617053498)

是

获取生物特征authToken操作类型，详见[OperateType](#section14617053498)。

tuiAuthToken

Uint8Array

是

当操作类型为OPERATE_TYPE_BIOMETRIC_AUTH时，tuiAuthToken表示通过密码认证（即[trustedAuthentication](#section6763105845111)）获取的authToken信息。

当操作类型为OPERATE_TYPE_CONTENT_AUTH时，tuiAuthToken表示通过交易信息临时确认（即[procContentAuthentication](#section1381398185415)）获取的authToken信息。

bioAuthToken

Uint8Array

是

生物特征认证获取的authToken，要求tuiAuthToken和bioAuthToken获取时使用同一个challenge，即保障两个authToken通过同一次会话获取。

**返回值：**

类型

说明

Promise<[AuthToken](#section20919104010476)>

Promise对象。

在生物特征认证绑定流程中，获取的authToken为经数字盾服务认证签发的包括生物特征ID的authToken。

在生物特征交易认证流程中，获取的authToken为经数字盾服务认证前的包括交易信息和生物特征ID的authToken。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAuthentication （数字盾服务）.md)**。**

错误码ID

错误信息

1019100001

The interface invoker does not have the corresponding permission.

1019100002

Parameter error.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1019100005

Face/Fingerprint/Password authentication failed.

1019100015

Failed to get the biometric authToken.

1019100019

The biometric data for authentication does not match the bound biometric feature.

1019100020

The biometric data has already been bound.

**示例：**

```ets
import { userAuth } from '@kit.UserAuthenticationKit';
import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";
async function PwdVerify(challenge: Uint8Array, resourceMgr:resourceManager.ResourceManager):Promise<trustedAuthentication.AuthToken> {
  try {
    const authID: bigint = 11842183505170721246n;//实际填充为从服务器获取到的账号对应的authID值
    const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png'); //实际使用时请替换为应用要在TUI界面展示的logo图片名称
    const buffer = fileData.buffer;
    const label:trustedAuthentication.TUILable = {
      image: buffer as ArrayBuffer,
      title: "数字盾密码认证",
    }
    const result = await trustedAuthentication.trustedAuthentication(challenge, authID, label);
    return result;
  } catch (err) {
    hilog.error(0x0000, 'testTag', `Failed to trustedAuthentication, code:${err.code}, message:${err.message}`);
    throw new Error('Password verify failed:' + (err as BusinessError).message);
  }
}
const rand = cryptoFramework.createRandom();
const len: number = 32;
let challengeID: Uint8Array = rand?.generateRandomSync(len)?.data;
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
const TuiAuthToken: trustedAuthentication.AuthToken = await PwdVerify(challengeID, resourceMgr);
let authTypeList :number[] = new Array();
authTypeList[0] = userAuth.UserAuthType.FINGERPRINT;
authTypeList[1] = userAuth.UserAuthType.FACE;

const authParam : userAuth.AuthParam = {
  challenge:  challengeID,
  authType: authTypeList,
  authTrustLevel: userAuth.AuthTrustLevel.ATL4
};
const widgetParam: userAuth.WidgetParam = {
  title: '请输入盾密码',
  navigationButtonText: '请输入盾密码',
};

try {
  const userAuthInstance = await userAuth.getUserAuthInstance(authParam, widgetParam);
  userAuthInstance.on('result', {
	onResult (result) {
	  let authTokenData = result.token;
	  let operType = trustedAuthentication.OperateType.OPERATE_TYPE_BIOMETRIC_AUTH;
	  trustedAuthentication.getBiometricAuthToken(operType, TuiAuthToken.authToken, authTokenData).then((newAuthToken) => {
	    let authToken = newAuthToken.authToken as Uint8Array;
 	    hilog.info(0x0000, TAG, `authToken content: ${authToken}`);
	  });
	}
  })
  userAuthInstance.start();
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'getUserAuthInstance failed: %{public}d %{public}s', e.code, e.message);
}
```

#### importData

importData(data: ArrayBuffer, authID: bigint): Promise<void>

导入备份的数据信息（即与HUKS签名验签时使用的加密密钥信息）。使用Promise异步回调。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**参数**：

参数名

类型

必填

说明

data

ArrayBuffer

是

通常指定为从Universal Keystore Kit获取的wrapkey数据信息，导入数据大小限制在2048字节内，对应数据不支持反复导入。

authID

bigint

是

密码创建时获取的authID信息。

**返回值：**

类型

说明

Promise<void>

Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAuthentication （数字盾服务）.md)**。**

错误码ID

错误信息

1019100001

The interface invoker does not have the corresponding permission.

1019100002

Parameter error.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1019100010

Failed to import data.

1019100012

Invalid authentication ID.

**示例：**

```ets
import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const authID: bigint = 1687413472599354502n;
 const buffer = new ArrayBuffer(8);
 const bufferArray = new Uint8Array(buffer);
 bufferArray.set([1, 2, 3, 4, 5, 6, 7, 8]);
 const result = await trustedAuthentication.importData(buffer, authID);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'importData failed: %{public}d %{public}s', e.code, e.message);
}
```

#### exportData

exportData(authID: bigint, label: TUILable): Promise<ArrayBuffer>

导出备份的数据信息（即与HUKS签名验签时使用的加密密钥信息），在导出时，需要经过密码认证，认证通过后才可导出对应的备份数据信息。使用Promise异步回调。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**参数**：

参数名

类型

必填

说明

authID

bigint

是

密码创建时获取的authID信息。

label

[TUILable](#section125211933134315)

是

用于TUI界面展示时的定制信息，详见[TUILable](#section125211933134315)。

**返回值：**

类型

说明

Promise<ArrayBuffer>

Promise对象，返回备份的数据信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAuthentication （数字盾服务）.md)**。**

错误码ID

错误信息

1019100001

The interface invoker does not have the corresponding permission.

1019100002

Parameter error.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1019100009

Failed to export data.

1019100012

Invalid authentication ID.

**示例：**

```ets
import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const credentialID: bigint = 1687413472599354502n;
 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
 const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
 const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png');
 const buffer = fileData.buffer;
 const label:trustedAuthentication.TUILable = {
  image: buffer as ArrayBuffer,
  title: "备份数据导出",
 }
 const result = await trustedAuthentication.exportData(credentialID, label);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'exportData failed: %{public}d %{public}s', e.code, e.message);
}
```

#### checkConfirmUITextFormat

checkConfirmUITextFormat(text: string): Promise<TextCheckResult>

检查将在TUI呈现的内容是否可以在屏幕上单行完整展示。使用Promise异步回调。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**参数**：

参数名

类型

必填

说明

text

string

是

将在TUI界面展示的认证信息内容。在交易认证前，可通过该接口确认交易信息是否可以在屏幕上单行完整展示，长度规格为1~200字节。

**返回值：**

类型

说明

Promise<[TextCheckResult](#section27021232135111)>

Promise对象，TUI界面显示指定text对应检查结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAuthentication （数字盾服务）.md)**。**

错误码ID

错误信息

1019100001

The interface invoker does not have the corresponding permission.

1019100002

Parameter error.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1019100006

Check input confirm text failed.

**示例：**

```ets
import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const text: string = "检查将在TUI呈现的text是否可以正常展示";
 const result = await trustedAuthentication.checkConfirmUITextFormat(text);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'checkConfirmUITextFormat failed: %{public}d %{public}s', e.code, e.message);
}
```

#### getRemainAuthTimes

getRemainAuthTimes(authID: bigint): Promise<number>

获取数字盾剩余认证次数。使用Promise异步回调。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**参数**：

参数名

类型

必填

说明

authID

bigint

是

密码创建时获取的authID信息。

**返回值：**

类型

说明

Promise<number>

Promise对象，数字盾剩余认证次数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAuthentication （数字盾服务）.md)**。**

错误码ID

错误信息

1019100001

The interface invoker does not have the corresponding permission.

1019100002

Parameter error.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1019100012

Invalid authentication ID.

1019100017

Failed to get the remaining number of authentication attempts.

**示例：**

```ets
import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const authID: bigint = 1687413472599354502n;
 const remainTimes = await trustedAuthentication.getRemainAuthTimes(authID);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'getRemainAuthTimesfailed: %{public}d %{public}s', e.code, e.message);
}
```

#### disableTrustedBioAuthentication

disableTrustedBioAuthentication(authID: bigint, authType: AuthType): Promise<void>

解绑指定生物类型认证能力。使用Promise异步回调。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**参数**：

参数名

类型

必填

说明

authID

bigint

是

密码创建时获取的authID信息。

authType

AuthType

是

仅支持AUTH_TYPE_FACE、AUTH_TYPE_FINGERPRINT

**返回值：**

类型

说明

Promise<void>

Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](TrustedAuthentication （数字盾服务）.md)**。**

错误码ID

错误信息

1019100001

The interface invoker does not have the corresponding permission.

1019100002

Parameter error.

Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

1019100012

Invalid authentication ID.

1019100018

Failed to unbind the corresponding biometric data.

1019100021

The corresponding biometric data has not been bound.

**示例：**

```ets
import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "TrustedAuthenticationJsTest";

try {
 const authID: bigint = 1687413472599354502n;
 const remainTimes = await trustedAuthentication.disableTrustedBioAuthentication(authID, trustedAuthentication.AuthType.AUTH_TYPE_FACE);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'disableTrustedBioAuthentication: %{public}d %{public}s', e.code, e.message);
}
```

#### PasswordInfo

设置密码时业务对密码规格参数要求。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**名称**

**类型**

****只读

可选

**说明**

pwdType

[PasswordType](#section1365374114910)

否

否

密码类型，取值范围详见[PasswordType](#section1365374114910)。

pwdMaxLength

number

否

否

密码最大长度，取值范围6~18。

pwdMinLength

number

否

否

密码最小长度，取值范围6~18，且小于等于pwdMaxLength。

maxAuthFailCount

number

否

否

密码最大连续认证失败次数，取值范围1~10。

#### TUILable

TUI页面下的定制信息，包括定制图像logo和页面标题。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**名称**

**类型**

****只读

可选

**说明**

image

ArrayBuffer

否

否

定制logo信息，当前暂不支持透明图片。要求图片格式为PNG RGBA格式、最大宽度、长度要求均为216px。

title

string

否

否

定制TUI页面标题信息，最大长度要求为31字节。

#### AuthInfo

开通数字盾服务对应的参数信息。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**名称**

**类型**

****只读

可选

**说明**

authToken

Uint8Array

否

否

包括密码authID的authToken信息。

authID

bigint

否

否

表示数字盾密码authID索引，用于密码认证、删除、修改。

#### AuthToken

经数字盾服务指定操作获取的authToken，不同操作流程中authToken包括的加密信息不同，详细可参考各个接口参数说明。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**名称**

**类型**

****只读

可选

**说明**

authToken

Uint8Array

否

否

对应操作流程中authToken信息。

#### AuthType

交易认证类型定义。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**名称**

值

**说明**

AUTH_TYPE_FACE

2

人脸认证

AUTH_TYPE_FINGERPRINT

4

指纹认证

AUTH_TYPE_TUI_PIN

32

TUI密码认证

#### PasswordType

密码类型定义，根据密码类型TUI界面弹出不同类型的安全键盘。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**名称**

值

**说明**

PASSWORD_TYPE_DIGITAL

0

纯数字密码类型

PASSWORD_TYPE_MIXED

1

数字、字符混合密码类型

#### OperateType

操作类型定义。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**名称**

值

**说明**

OPERATE_TYPE_BIOMETRIC_AUTH

1

生物特征与密码认证绑定操作

OPERATE_TYPE_CONTENT_AUTH

2

使用生物特征进行交易认证操作

#### AuthReqParams

交易认证请求相关参数。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**名称**

**类型**

****只读

可选

**说明**

reqType

[AuthType](#section58527274920)

否

否

认证类型，取值范围详见[AuthType](#section58527274920)。

authContent

Array<string>

否

否

认证数据，即交易场景下交易数据，单条数据大小在1024字节以内。

#### TextCheckResult

TUI界面文本信息是否可以单行显示的检查结果。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**名称**

**类型**

****只读

可选

**说明**

result

number

否

否

指定输入文本检查结果，如果可以正常显示，返回为0，否则返回[1019100011 不合法的TUI认证信息](TrustedAuthentication （数字盾服务）.md#section19615182019615)。

lastIndex

number

否

否

输入字符串可正常显示的最后一个字符对应的索引。

#### TrustedAuthErrorCode

数字盾服务开放接口执行失败错误码。

**系统能力：**SystemCapability.Security.TrustedAuthentication

**起始版本：**6.0.0(20)

**名称**

值

**说明**

TRUSTED_AUTH_ERROR_NO_PERMISSION

1019100001

权限校验失败

TRUSTED_AUTH_ERROR_ILLEGAL_ARGUMENT

1019100002

参数检查失败

TRUSTED_AUTH_ERROR_PWD_LIMIT_REACHED

1019100003

密码认证连续失败次数达到应用定义的最大次数

TRUSTED_AUTH_ERROR_PWD_DELETE_FAILED

1019100004

删除密码失败

TRUSTED_AUTH_ERROR_VERIFY_FAILED

1019100005

密码认证失败

TRUSTED_AUTH_ERROR_CHECK_CONFIRM_TEXT_FAILED

1019100006

输入文本信息检查失败

TRUSTED_AUTH_ERROR_NOT_SUPPORT_IMAGE

1019100007

不支持的图片格式

TRUSTED_AUTH_ERROR_USER_REQ_CANCEL

1019100008

用户取消操作

TRUSTED_AUTH_ERROR_EXPORT_DATA_FAILED

1019100009

备份数据导出失败

TRUSTED_AUTH_ERROR_IMPORT_DATA_FAILED

1019100010

备份数据导入失败

TRUSTED_AUTH_ERROR_INVALID_CONTENT

1019100011

不合法的TUI认证信息

TRUSTED_AUTH_ERROR_INVALID_AUTH_ID

1019100012

无效的authID

TRUSTED_AUTH_ERROR_SET_PWD_FAILED

1019100013

创建密码失败

TRUSTED_AUTH_ERROR_MODIFY_PWD_FAILED

1019100014

修改密码失败

TRUSTED_AUTH_ERROR_BIO_RESIGN_FAILED

1019100015

生物认证authToken签发失败

TRUSTED_AUTH_FEATURE_INITIALIZATION_FAILED

1019100016

数字盾服务未使能

TRUSTED_AUTH_ERROR_GET_REMAIN_TIME

1019100017

获取数字盾剩余认证次数失败

TRUSTED_AUTH_ERROR_DISABLE_BIO_AUTH

1019100018

解绑指定生物特征认证能力失败

TRUSTED_AUTH_ERROR_BIO_MISMATCH

1019100019

认证的生物特征与绑定的生物特征不匹配

TRUSTED_AUTH_ERROR_BIO_REPEATED_BIND

1019100020

已绑定对应的生物特征

TRUSTED_AUTH_ERROR_NOT_BIND_BIO

1019100021

对应生物特征未绑定