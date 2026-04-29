# SOTER

SOTER提供移动端免密身份认证能力，支持使用SOTER协议的应用实现免密登录，免密支付等业务场景。

支持的设备类型为：Phone, PC/2in1, Tablet

起始版本： 5.0.0(12)

**导入模块**

```ets
import { soter } from '@kit.OnlineAuthenticationKit'
```

**KeyType**

密钥选型，为枚举值。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ECC_P256 | 0 | 密钥选型ECC P256。 |

**SignedResult**

表示签名结果。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力：SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | Uint8Array | 是 | 原始报文。 |
| signature | Uint8Array | 是 | 原始报文的签名。 |
| saltLength | number | 是 | 盐值长度，小于U32类型最大值。 |

**getVersionSync**

getVersionSync(): string

该接口用于获取SOTER免密认证API接口的版本号，同步返回结果。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| string | 返回SOTER免密认证的API接口版本号。最大长度64个字符。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
let res: string = soter.getVersionSync();// 开发者处理结果
```

**getVersion**

getVersion(): Promise<string>

该接口用于获取SOTER免密认证API接口的版本号，使用Promise异步回调。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回SOTER免密认证的API接口版本号。最大长度64个字符。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let resPromise: Promise<string> = soter.getVersion();
resPromise.then(result => {
  console.info('Succeeded in doing getVersion.');
  // 开发者处理结果
}).catch((error: BusinessError) => {
  console.error(`Failed to call getVersion. Code: ${error.code}, message: ${error.message}`);
});
```

**hasAppSecureKeySync**

hasAppSecureKeySync(keyType: KeyType): boolean

该接口用于查询应用密钥的生成状态，同步返回结果。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyType | KeyType | 是 | 密钥选型，当前只支持 soter.KeyType.ECC_P256。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 同步返回应用密钥的生成状态。true代表已生成，false代表未生成。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256

// 查询应用密钥生成状态 同步
let hasAppSecureKey: boolean = soter.hasAppSecureKeySync(keyType);
```

**hasAppSecureKey**

hasAppSecureKey(keyType: KeyType): Promise<boolean>

该接口用于查询应用密钥的生成状态，使用Promise异步回调。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyType | KeyType | 是 | 密钥选型，目前只支持 soter.KeyType.ECC_P256。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回应用密钥的生成状态。true代表已生成，false代表未生成。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256

// 异步查询应用密钥的生成状态
let hasAppSecureKeyPromise: Promise<boolean> = soter.hasAppSecureKey(keyType);
hasAppSecureKeyPromise.then(result => {
  console.info('Succeeded in doing hasAppSecureKey.');
  // 开发者处理结果
}).catch((error: BusinessError) => {
  console.error(`Failed to call hasAppSecureKey. Code: ${error.code}, message: ${error.message}`);
});
```

**generateAppSecureKeySync**

generateAppSecureKeySync(keyType: KeyType): Uint8Array

该接口用于生成App应用密钥，同步返回结果。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyType | KeyType | 是 | 密钥选型，目前只支持 soter.KeyType.ECC_P256。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回App应用密钥。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256

// 生成应用密钥
let appSecureKey: Uint8Array = soter.generateAppSecureKeySync(keyType);
```

**generateAppSecureKey**

generateAppSecureKey(keyType: KeyType): Promise<Uint8Array>

该接口用于生成App应用密钥，使用Promise异步回调。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyType | KeyType | 是 | 密钥选型，目前只支持 soter.KeyType.ECC_P256，其余枚举值均报错。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回App应用密钥。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256

// 生成应用密钥
let appSecureKeyPromise: Promise<Uint8Array> = soter.generateAppSecureKey(keyType);
appSecureKeyPromise.then(result => {
  console.info('Succeeded in doing generateAppSecureKey.');
  // 开发者处理结果
}).catch((error: BusinessError) => {
  console.error(`Failed to call generateAppSecureKey. Code: ${error.code}, message: ${error.message}`);
});
```

**getAppSecureKeySync**

getAppSecureKeySync(keyType: KeyType): Uint8Array

该接口用于获取App应用密钥，同步返回结果。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyType | KeyType | 是 | 密钥选型，目前只支持 soter.KeyType.ECC_P256。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回App应用密钥。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256

// 获取应用密钥 同步
let appSecureKey: Uint8Array = soter.getAppSecureKeySync(keyType);
```

**getAppSecureKey**

getAppSecureKey(keyType: KeyType): Promise<Uint8Array>

该接口用于获取App应用密钥，使用Promise异步回调。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyType | KeyType | 是 | 密钥选型，目前只支持 soter.KeyType.ECC_P256。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回App应用密钥。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256

// 获取应用密钥 Promise
let appSecureKeyPromise: Promise<Uint8Array> = soter.getAppSecureKey(keyType);
appSecureKeyPromise.then(result => {
  console.info('Succeeded in doing getAppSecureKey.');
  // 开发者处理结果
}).catch((error: BusinessError) => {
  console.error(`Failed to call getAppSecureKey. Code: ${error.code}, message: ${error.message}`);
});
```

**hasAuthKeySync**

hasAuthKeySync(keyAlias: string, keyType: KeyType): boolean

该接口用于查询AuthKey生成状态，同步返回结果。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), _(非首字符)。 |
| keyType | KeyType | 是 | 密钥选型，目前只支持 soter.KeyType.ECC_P256。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 同步返回AuthKey生成状态，true代表已生成，false代表未生成。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256
let keyAlias: string = 'keyAlias'; // 开发者自定义索引

// 查询AuthKey开通状态 同步
let hasAuthKey: boolean = soter.hasAuthKeySync(keyAlias, keyType);
```

**hasAuthKey**

hasAuthKey(keyAlias: string, keyType: KeyType): Promise<boolean>

该接口用于查询AuthKey生成状态，使用Promise异步回调。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), _(非首字符)。 |
| keyType | KeyType | 是 | 密钥选型，目前只支持 soter.KeyType.ECC_P256。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回查询AuthKey生成状态。true代表已生成，false代表未生成。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256
let keyAlias: string = 'keyAlias';

// 查询AuthKey生成状态 Promise
let hasAuthKeyPromise: Promise<boolean> = soter.hasAuthKey(keyAlias, keyType);
hasAuthKeyPromise.then(result => {
  console.info('Succeeded in doing hasAuthKey.');
  // 开发者处理结果
}).catch((error: BusinessError) => {
  console.error(`Failed to call hasAuthKey. Code: ${error.code}, message: ${error.message}`);
});
```

**generateAuthKeySync**

generateAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult

该接口用于生成AuthKey，同步返回结果。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), _(非首字符)。 |
| keyType | KeyType | 是 | 密钥选型，目前只支持 soter.KeyType.ECC_P256。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| SignedResult | 返回SignedResult对象。其中signature为返回报文的签名，message为返回报文的原文，saltLength为加密盐值长度。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256
let keyAlias: string = 'keyAlias';

// 生成AuthKey
let signedResult: soter.SignedResult = soter.generateAuthKeySync(keyAlias, keyType);
let authKey: Uint8Array = signedResult?.signature; // 开发者使用结果AuthKey
```

**generateAuthKey**

generateAuthKey(keyAlias: string, keyType: KeyType): Promise<SignedResult>

该接口用于生成AuthKey，使用Promise异步回调。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), _(非首字符)。 |
| keyType | KeyType | 是 | 密钥选型，目前只支持 soter.KeyType.ECC_P256。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<SignedResult> | Promise对象，返回SignedResult对象。其中signature为返回报文的签名，message为返回报文的原文，saltLength为加密盐值长度。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256
let keyAlias: string = 'keyAlias';

// 生成AuthKey
let authKeyPromise: Promise<soter.SignedResult> = soter.generateAuthKey(keyAlias, keyType);
authKeyPromise.then(result => {
  console.info('Succeeded in doing generateAuthKey.');
  // 开发者处理结果
}).catch((error: BusinessError) => {
   console.error(`Failed to call generateAuthKey. Code: ${error.code}, message: ${error.message}`);
});
```

**getAuthKeySync**

getAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult

该接口用于获取AuthKey，同步返回结果。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), _(非首字符)。 |
| keyType | KeyType | 是 | 密钥选型，目前只支持 soter.KeyType.ECC_P256。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| SignedResult | 返回SignedResult对象。其中signature为返回报文的签名，message为返回报文的原文，saltLength为加密盐值长度。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256
let keyAlias: string = 'keyAlias';

// 使用同步接口获取AuthKey
let signedResult: soter.SignedResult = soter.getAuthKeySync(keyAlias, keyType);
let authKey: Uint8Array = signedResult.message; // 开发者使用结果AuthKey
```

**getAuthKey**

getAuthKey(keyAlias: string, keyType: KeyType): Promise<SignedResult>

该接口用于获取AuthKey，使用Promise异步回调。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), _(非首字符)。 |
| keyType | KeyType | 是 | 密钥选型，目前只支持 soter.KeyType.ECC_P256。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<SignedResult> | Promise对象，返回SignedResult对象。其中signature为返回报文的签名，message为返回报文的原文，saltLength为加密盐值长度。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256
let keyAlias: string = 'keyAlias';

// 获取AuthKey Promise
let authKeyPromise: Promise<soter.SignedResult> = soter.getAuthKey(keyAlias, keyType);
authKeyPromise.then(result => {
  console.info('Succeeded in doing getAuthKey.');
  // 开发者处理结果
}).catch((error: BusinessError) => {
  console.error(`Failed to call getAuthKey. Code: ${error.code}, message: ${error.message}`);
});
```

**generateChallengeSync**

generateChallengeSync(keyAlias: string): Uint8Array

该接口用于生成Challenge，同步返回结果。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), _(非首字符)。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回生成的Challenge。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
let keyAlias: string = 'keyAlias';

// 生成Challenge
let challenge: Uint8Array = soter.generateChallengeSync(keyAlias);
```

**generateChallenge**

generateChallenge(keyAlias: string): Promise<Uint8Array>

该接口用于生成Challenge，使用Promise异步回调。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), _(非首字符)。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回生成的Challenge。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let keyAlias: string = 'keyAlias';

// 生成Challenge
let challengePromise: Promise<Uint8Array> = soter.generateChallenge(keyAlias);
challengePromise.then(result => {
  console.info('Succeeded in doing generateChallenge.');
  // 开发者处理结果
}).catch((error: BusinessError) => {
  console.error(`Failed to call generateChallenge. Code: ${error.code}, message: ${error.message}`);
});
```

**signWithAuthKeySync**

signWithAuthKeySync(keyAlias: string, authToken: Uint8Array, info: string): SignedResult

该接口用于SOTER免密认证，同步返回签名的报文。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), _(非首字符)。 |
| authToken | Uint8Array | 是 | 用户身份认证通过的凭证（通过用户认证模块可获取，调用@ohos.userIAM.userAuth的getUserAuthInstance）。 |
| info | string | 是 | 开发者自定义信息，info最大长度为511字符。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| SignedResult | 返回SignedResult对象。其中signature为返回报文的签名，message为返回报文的原文，saltLength为加密盐值长度。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
let keyAlias: string = 'keyAlias';
// 开发者调用@ohos.userIAM.userAuth的getUserAuthInstance获取authToken；authToken需要开发者替换为真实入参。
let authToken = new Uint8Array([0]);
let info = '';
let authResult: soter.SignedResult = soter.signWithAuthKeySync(keyAlias, authToken, info)
```

**signWithAuthKey**

signWithAuthKey(keyAlias: string, authToken: Uint8Array, info: string): Promise<SignedResult>

该接口用于SOTER免密认证，使用Promise异步回调返回签名的报文。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), _(非首字符)。 |
| authToken | Uint8Array | 是 | 用户身份认证通过的凭证（通过用户认证模块可获取，调用@ohos.userIAM.userAuth的getUserAuthInstance）。 |
| info | string | 是 | 开发者自定义信息，info最大长度为511字符。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<SignedResult> | Promise对象，返回SignedResult对象。其中signature为返回报文的签名，message为返回报文的原文，saltLength为加密盐值长度。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let keyAlias: string = 'keyAlias';
// 开发者调用@ohos.userIAM.userAuth的getUserAuthInstance获取authToken；authToken需要开发者替换为真实入参。
let authToken = new Uint8Array([0]);
let info = '';
let authResultPromise: Promise<soter.SignedResult> = soter.signWithAuthKey(keyAlias, authToken, info);
authResultPromise.then(result => {
  console.info('Succeeded in doing signWithAuthKey.');
  // 开发者处理结果
}).catch((error: BusinessError) => {
  console.error(`Failed to call signWithAuthKey. Code: ${error.code}, message: ${error.message}`);
});
```

**deleteAuthKeySync**

deleteAuthKeySync(keyAlias: string): void

该接口用于删除AuthKey。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), _(非首字符)。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
// 删除认证密钥
let keyAlias: string = 'keyAlias';
soter.deleteAuthKeySync(keyAlias);
```

**deleteAuthKey**

deleteAuthKey(keyAlias: string): Promise<void>

该接口用于删除AuthKey，使用Promise异步回调。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), _(非首字符)。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let keyAlias: string = 'keyAlias';
// 删除AuthKey
let delPromise: Promise<void> = soter.deleteAuthKey(keyAlias);
delPromise.then(() => {
  console.info('Succeeded in doing deleteAuthKey.');
}).catch((error: BusinessError) => {
  console.error(`Failed to call deleteAuthKey. Code: ${error.code}, message: ${error.message}`);
});
```

**deleteAppSecureKeySync**

deleteAppSecureKeySync(): void

该接口用于删除应用密钥，同步返回结果。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
//删除应用密钥
soter.deleteAppSecureKeySync();
```

**deleteAppSecureKey**

deleteAppSecureKey(): Promise<void>

该接口用于删除应用密钥，使用Promise异步回调。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.SOTER

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[SOTER免密认证错误码](SOTER.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 删除应用密钥
let delAppSecureKeyPromise: Promise<void> = soter.deleteAppSecureKey();
delAppSecureKeyPromise.then(() => {
  console.info('Succeeded in doing deleteAppSecureKey.');
}).catch((error: BusinessError) => {
  console.error(`Failed to call deleteAppSecureKey. Code: ${error.code}, message: ${error.message}`);
});
```