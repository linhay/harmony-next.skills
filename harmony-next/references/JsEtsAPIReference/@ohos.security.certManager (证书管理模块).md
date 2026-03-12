# @ohos.security.certManager (证书管理模块)

证书管理主要提供系统级的证书管理能力，实现证书全生命周期（安装，存储，使用，销毁）的管理和安全使用。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
```

#### CmKeyPurpose

表示密钥使用目的的枚举，用于签名、验签。

**系统能力：** SystemCapability.Security.CertificateManager

名称值说明CM_KEY_PURPOSE_SIGN4签名。CM_KEY_PURPOSE_VERIFY8验签。

#### CmKeyDigest

表示签名、验签使用的摘要算法的枚举。

**系统能力：** SystemCapability.Security.CertificateManager

名称值说明CM_DIGEST_NONE0不需要摘要算法，选用此项时，需要业务传入已经计算过摘要的数据进行签名、验签。CM_DIGEST_MD51MD5摘要算法。CM_DIGEST_SHA12SHA1摘要算法。CM_DIGEST_SHA2243SHA224摘要算法。CM_DIGEST_SHA2564SHA256摘要算法。CM_DIGEST_SHA3845SHA384摘要算法。CM_DIGEST_SHA5126SHA512摘要算法。CM_DIGEST_SM318+7SM3摘要算法。

#### CmKeyPadding

表示签名、验签使用的填充方式的枚举。

**系统能力：** SystemCapability.Security.CertificateManager

名称值说明CM_PADDING_NONE0无填充。CM_PADDING_PSS1PSS方式填充。CM_PADDING_PKCS1_V1_52PKCS1_V1_5方式填充。

#### CMSignatureSpec

表示签名、验签操作使用的参数集合，包括密钥使用目的、填充方式和摘要算法。

**系统能力：** SystemCapability.Security.CertificateManager

名称类型只读可选说明purpose[CmKeyPurpose](#ZH-CN_TOPIC_0000002529445349__cmkeypurpose)否否表示密钥使用目的的枚举。padding[CmKeyPadding](#ZH-CN_TOPIC_0000002529445349__cmkeypadding)否是表示填充方式的枚举。digest[CmKeyDigest](#ZH-CN_TOPIC_0000002529445349__cmkeydigest)否是表示摘要算法的枚举。

#### CertInfo

表示证书详细信息。

**系统能力：** SystemCapability.Security.CertificateManager

名称类型只读可选说明uristring否否表示证书的唯一标识符，最大长度为256字节。certAliasstring否否表示证书的别名，最大长度为128字节。stateboolean否否表示证书的状态，true为启用状态、false为禁用状态。issuerNamestring否否表示证书的颁发者名称，最大长度为256字节。subjectNamestring否否表示证书的使用者名称，最大长度为1024字节。serialstring否否表示证书的序列号，最大长度为64字节。格式为16进制字符串，例如：62C2CB4DE8405E96。notBeforestring否否表示证书有效期起始日期，最大长度为32字节。notAfterstring否否表示证书有效期截止日期，最大长度为32字节。fingerprintSha256string否否表示证书的指纹值，最大长度为128字节。certUint8Array否否表示证书二进制数据，最大长度为8196字节。

#### CertAbstract

表示证书简要信息。

**系统能力：** SystemCapability.Security.CertificateManager

名称类型只读可选说明uristring否否表示证书的唯一标识符，最大长度为256字节。certAliasstring否否表示证书的别名，最大长度为128字节。stateboolean否否表示证书的状态，true为启用状态、false为禁用状态。subjectNamestring否否表示证书的使用者名称，最大长度为1024字节。

#### Credential

表示凭据详细信息。

**系统能力：** SystemCapability.Security.CertificateManager

名称类型只读可选说明typestring否否表示凭据的类型，最大长度为8字节。aliasstring否否表示凭据的别名，最大长度为128字节。keyUristring否否表示凭据的唯一标识符，最大长度为256字节。certNumnumber否否表示凭据中包含的证书个数。keyNumnumber否否表示凭据中包含的密钥个数。credentialDataUint8Array否否表示凭据二进制数据，最大长度为20480字节。certPurpose22+[CertificatePurpose](#ZH-CN_TOPIC_0000002529445349__certificatepurpose22)否是表示凭据的用途。默认值为CertificatePurpose.PURPOSE_DEFAULT。

#### CredentialAbstract

表示凭据的简要信息。

**系统能力：** SystemCapability.Security.CertificateManager

名称类型只读可选说明typestring否否表示凭据的类型，最大长度为8字节。aliasstring否否表示凭据的别名，最大长度为128字节。keyUristring否否表示凭据的唯一标识符，最大长度为256字节。

#### CMResult

表示接口的返回结果。

**系统能力：** SystemCapability.Security.CertificateManager

名称类型只读可选说明certListArray<[CertAbstract](#ZH-CN_TOPIC_0000002529445349__certabstract)>否是表示证书简要信息的列表。certInfo[CertInfo](#ZH-CN_TOPIC_0000002529445349__certinfo)否是表示证书详情。credentialListArray<[CredentialAbstract](#ZH-CN_TOPIC_0000002529445349__credentialabstract)>否是表示凭据简要信息的列表。credential[Credential](#ZH-CN_TOPIC_0000002529445349__credential)否是表示凭据详情。appUidListArray<string>否是表示授权应用列表。uristring否是表示证书或凭据的唯一标识符，最大长度为256字节。outDataUint8Array否是表示签名结果。credentialDetailList22+Array<[Credential](#ZH-CN_TOPIC_0000002529445349__credential)>否是表示凭据详细信息。

#### CMHandle

表示签名、验签的初始化操作句柄。

**系统能力：** SystemCapability.Security.CertificateManager

名称类型只读可选说明handleUint8Array否否签名、验签的初始化操作句柄，最大长度为8字节。

#### CMErrorCode

表示调用证书管理相关API的错误码。

**系统能力：** SystemCapability.Security.CertificateManager

名称值说明CM_ERROR_NO_PERMISSION201表示应用程序无权限调用接口。CM_ERROR_INVALID_PARAMS401表示输入参数无效。CM_ERROR_GENERIC17500001表示调用接口时发生内部错误。CM_ERROR_NO_FOUND17500002表示证书或凭据不存在。CM_ERROR_INCORRECT_FORMAT17500003表示输入证书或凭据的数据格式无效。CM_ERROR_MAX_CERT_COUNT_REACHED12+17500004表示证书或凭据数量达到上限。CM_ERROR_NO_AUTHORIZATION12+17500005表示应用未经用户授权。CM_ERROR_DEVICE_ENTER_ADVSECMODE18+17500007表示设备进入坚盾守护模式。CM_ERROR_STORE_PATH_NOT_SUPPORTED20+17500009表示不支持指定的证书存储路径。CM_ERROR_ACCESS_UKEY_SERVICE_FAILED22+17500010表示访问USB凭据服务失败。CM_ERROR_PARAMETER_VALIDATION_FAILED22+17500011

表示输入参数校验失败。

例如：参数格式不正确、参数范围无效。

#### CertType18+

表示证书类型。

**系统能力：** SystemCapability.Security.CertificateManager

名称值说明CA_CERT_SYSTEM0表示系统CA证书。CA_CERT_USER1表示用户CA证书。

#### CertScope18+

表示证书的位置。

**系统能力：** SystemCapability.Security.CertificateManager

名称值说明CURRENT_USER1表示当前用户。GLOBAL_USER2表示设备公共，即所有用户都可以访问的位置。

#### CertAlgorithm20+

表示证书的算法类型。

**系统能力：** SystemCapability.Security.CertificateManager

名称值说明INTERNATIONAL1表示国际密码算法，如RSA、NIST ECC等。SM2表示商用密码算法，如SM2、SM4等。

#### CertStoreProperty18+

表示获取证书存储位置的参数集合，包括证书的类型及证书的位置。

**系统能力：** SystemCapability.Security.CertificateManager

名称类型只读可选说明certType[CertType](#ZH-CN_TOPIC_0000002529445349__certtype18)否否表示证书的类型。certScope[CertScope](#ZH-CN_TOPIC_0000002529445349__certscope18)否是表示证书的存储位置。当证书类型为CA_CERT_USER时，此项为必选项。certAlg20+[CertAlgorithm](#ZH-CN_TOPIC_0000002529445349__certalgorithm20)否是表示证书算法类型。仅当certType为CA_CERT_SYSTEM时有效，默认值为INTERNATIONAL。

#### AuthStorageLevel18+

表示凭据的存储级别。

**系统能力：** SystemCapability.Security.CertificateManager

名称值说明EL11EL1级别，表示设备启动后可以访问。EL22EL2级别，表示设备首次解锁后可以访问。EL44EL4级别，表示设备解锁时可以访问。

#### CertificatePurpose22+

表示凭据用途的枚举。

**系统能力：** SystemCapability.Security.CertificateManager

名称值说明PURPOSE_DEFAULT0默认用途，用于凭据签名。PURPOSE_ALL1用于查询所有凭据。PURPOSE_SIGN2用于凭据签名。PURPOSE_ENCRYPT3用于凭据加密。

#### UkeyInfo22+

提供USB凭据属性信息。

**系统能力：** SystemCapability.Security.CertificateManager

名称类型只读可选说明certPurpose[CertificatePurpose](#ZH-CN_TOPIC_0000002529445349__certificatepurpose22)否是表示凭据用途。

#### certificateManager.installPrivateCertificate

installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, callback: AsyncCallback<CMResult>): void

表示安装私有凭据，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明keystoreUint8Array是表示带有密钥对和证书的密钥库文件，最大长度为20480字节。keystorePwdstring是表示密钥库文件的密码，长度限制32字节以内。certAliasstring是表示用户输入的凭据别名，当前仅支持传入数字、字母或下划线，长度建议32字节以内。callbackAsyncCallback<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>是回调函数。当安装私有凭据成功时，err为null，data为[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)对象中的uri属性；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500003The keystore is in an invalid format or the keystore password is incorrect.17500004The number of certificates or credentials reaches the maximum allowed.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';

/* 安装的凭据数据需要业务赋值，本例数据非凭据数据 */
let keystore: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
]);
let keystorePwd: string = "123456";
try {
  certificateManager.installPrivateCertificate(keystore, keystorePwd, "test", (err, cmResult) => {
    if (err != null) {
      console.error(`Failed to install private certificate. Code: ${err.code}, message: ${err.message}`);
    } else {
      let uri: string = (cmResult?.uri == undefined) ? '' : cmResult.uri;
      console.info('Succeeded in installing private certificate.');
    }
  });
} catch (error) {
  console.error(`Failed to install private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.installPrivateCertificate

installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string): Promise<CMResult>

表示安装私有凭据，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明keystoreUint8Array是表示带有密钥对和证书的密钥库文件，最大长度为20480字节。keystorePwdstring是表示密钥库文件的密码，长度限制32字节以内。certAliasstring是表示用户输入的凭据别名，当前仅支持传入数字、字母或下划线，长度建议32字节以内。

**返回值**：

类型说明Promise<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>Promise对象。表示安装私有凭据的结果，返回值为[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)对象中的uri属性。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500003The keystore is in an invalid format or the keystore password is incorrect.17500004The number of certificates or credentials reaches the maximum allowed.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* 安装的凭据数据需要业务赋值，本例数据非凭据数据 */
let keystore: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
]);
let keystorePwd: string = "123456";
try {
  certificateManager.installPrivateCertificate(keystore, keystorePwd, 'test').then((cmResult) => {
    let uri: string = (cmResult?.uri == undefined) ? '' : cmResult.uri;
    console.info('Succeeded in installing private certificate.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to install private certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to install private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.installPrivateCertificate18+

installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, level: AuthStorageLevel): Promise<CMResult>

表示安装私有凭据并指定凭据的存储级别。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

参数名类型必填说明keystoreUint8Array是表示带有密钥对和证书的密钥库文件，最大长度为20480字节。keystorePwdstring是

表示密钥库文件的密码。

长度限制：32字节以内。

certAliasstring是

表示用户输入的凭据别名，当前仅支持传入数字、字母或下划线。

长度建议：32字节以内。

level[AuthStorageLevel](#ZH-CN_TOPIC_0000002529445349__authstoragelevel18)是表示凭据的存储级别。

**返回值：**

类型说明Promise<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>Promise对象。表示安装私有凭据的结果，返回值为[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)对象中的uri属性。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500003The keystore is in an invalid format or the keystore password is incorrect.17500004The number of certificates or credentials reaches the maximum allowed.

**示例：**

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* 安装的凭据数据需要业务赋值，本例数据非凭据数据。 */
let keystore: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
]);
let keystorePwd: string = "123456";
try {
  /* 安装凭据在首次解锁设备后可以使用。 */
  let level = certificateManager.AuthStorageLevel.EL2;
  certificateManager.installPrivateCertificate(keystore, keystorePwd, 'test', level).then((cmResult) => {
    let uri: string = (cmResult?.uri == undefined) ? '' : cmResult.uri;
    console.info('Succeeded in installing private certificate.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to install private certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to install private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.getPrivateCertificate

getPrivateCertificate(keyUri: string, callback: AsyncCallback<CMResult>): void

表示获取私有凭据的详细信息，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明keyUristring是表示待获取凭据的唯一标识符，长度限制256字节以内。callbackAsyncCallback<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>是回调函数。当获取私有凭据的详细信息成功时，err为null，data为[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)对象中的credential属性；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500002The certificate does not exist.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';

let uri: string = 'test'; /* 业务获取私有凭据详情，需要使用凭据的唯一标识符，此处省略 */
try {
  certificateManager.getPrivateCertificate(uri, (err, cmResult) => {
    if (err != null) {
      console.error(`Failed to get private certificate. Code: ${err.code}, message: ${err.message}`);
    } else {
      if (cmResult?.credential == undefined) {
        console.info('The result of getting private certificate is undefined.');
      } else {
        let list = cmResult.credential;
        console.info('Succeeded in getting private certificate.');
      }
    }
  });
} catch (error) {
  console.error(`Failed to get private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.getPrivateCertificate

getPrivateCertificate(keyUri: string): Promise<CMResult>

表示获取私有凭据详情，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明keyUristring是表示待获取凭据的唯一标识符，长度限制256字节以内。

**返回值**：

类型说明Promise<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>Promise对象。表示获取私有凭据详细信息的结果，返回值为[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)对象中的credential属性。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500002The certificate does not exist.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string = 'test'; /* 业务获取私有凭据详情，需要使用凭据的唯一标识符，此处省略 */
try {
  certificateManager.getPrivateCertificate(uri).then((cmResult) => {
    if (cmResult?.credential == undefined) {
      console.info('The result of getting private certificate is undefined.');
    } else {
      let list = cmResult.credential;
      console.info('Succeeded in getting private certificate.');
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get private certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.uninstallPrivateCertificate

uninstallPrivateCertificate(keyUri: string, callback: AsyncCallback<void>): void

表示卸载指定的私有凭据，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明keyUristring是表示待卸载凭据的唯一标识符，长度限制256字节以内。callbackAsyncCallback<void>是回调函数。当卸载私有凭据成功时，err为null，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500002The certificate does not exist.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';

let uri: string = 'test'; /* 业务删除私有凭据，需要使用凭据的唯一标识符，此处省略 */
try {
  certificateManager.uninstallPrivateCertificate(uri, (err, result) => {
    if (err != null) {
      console.error(`Failed to uninstall private certificate. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('Succeeded in uninstalling private certificate.');
    }
  });
} catch (error) {
  console.error(`Failed to uninstall private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.uninstallPrivateCertificate

uninstallPrivateCertificate(keyUri: string): Promise<void>

表示卸载指定的私有凭据，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明keyUristring是表示待卸载凭据的唯一标识符，长度限制256字节以内。

**返回值**：

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500002The certificate does not exist.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string = 'test'; /* 业务删除私有凭据，需要使用凭据的唯一标识符，此处省略 */
try {
  certificateManager.uninstallPrivateCertificate(uri).then((cmResult) => {
    console.info('Succeeded in uninstalling private certificate.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to uninstall private certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to uninstall private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.installUserTrustedCertificateSync18+

installUserTrustedCertificateSync(cert: Uint8Array, certScope: CertScope) : CMResult

表示安装用户CA证书。

**需要权限：** ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明certUint8Array是表示CA证书数据，最大长度为8196字节。certScope[CertScope](#ZH-CN_TOPIC_0000002529445349__certscope18)是表示CA证书安装的位置。

**返回值**：

类型说明[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)表示CA证书的安装结果，返回值CMResult对象中的uri属性。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500003Indicates that the certificate is in an invalid format.17500004Indicates that the number of certificates reaches the maximum allowed.17500007Indicates that the device enters advanced security mode. In this mode, the user CA certificate cannot be installed.

**示例**：

```ets
import {certificateManager} from '@kit.DeviceCertificateKit';

/* 安装的CA证书数据需要业务赋值，本例数据非CA证书数据 */
let certData: Uint8Array = new Uint8Array([
    0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
]);
try {
    let result: certificateManager.CMResult = certificateManager.installUserTrustedCertificateSync(certData, certificateManager.CertScope.CURRENT_USER);
    let certUri = result.uri;
    if (certUri === undefined) {
        console.error("The result of install user trusted certificate is undefined.");
    } else {
        console.info("Successed to install user trusted certificate.");
    }
} catch (error) {
    console.error(`Failed to install user trusted certificate. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.uninstallUserTrustedCertificateSync18+

uninstallUserTrustedCertificateSync(certUri: string) : void

表示删除用户CA证书。

**需要权限：** ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明certUristring是表示待卸删除证书的唯一标识符，长度限制256字节以内。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500002Indicates that the certificate does not exist.

**示例**：

```ets
import {certificateManager} from '@kit.DeviceCertificateKit';

let certUri: string = "test"; /* 业务删除证书，需要使用证书的标识符，此处省略 */
try {
    certificateManager.uninstallUserTrustedCertificateSync(certUri);
} catch (error) {
    console.error(`Failed to uninstall user trusted certificate. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.init

init(authUri: string, spec: CMSignatureSpec, callback: AsyncCallback<CMHandle>): void

表示使用凭据进行签名、验签的初始化操作，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明authUristring是表示使用凭据的唯一标识符，长度限制256字节以内。spec[CMSignatureSpec](#ZH-CN_TOPIC_0000002529445349__cmsignaturespec)是表示签名、验签的属性。callbackAsyncCallback<[CMHandle](#ZH-CN_TOPIC_0000002529445349__cmhandle)>是回调函数。当签名、验签的初始化操作成功时，err为null，data为获取到的CMHandle；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500002The certificate does not exist.17500005The application is not authorized by the user.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';

let uri: string = 'test'; /* 业务使用凭据进行签名、验签的初始化操作，需要使用凭据的唯一标识符，此处省略 */
const req: certificateManager.CMSignatureSpec = {
  purpose: certificateManager.CmKeyPurpose.CM_KEY_PURPOSE_SIGN,
  padding: certificateManager.CmKeyPadding.CM_PADDING_PSS,
  digest: certificateManager.CmKeyDigest.CM_DIGEST_SHA256
}
try {
  certificateManager.init(uri, req, (err, cmHandle) => {
    if (err != null) {
      console.error(`Failed to init. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('Succeeded in initiating.');
    }
  })
} catch (error) {
  console.error(`Failed to init. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.init

init(authUri: string, spec: CMSignatureSpec): Promise<CMHandle>

表示使用凭据进行签名、验签的初始化操作，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明authUristring是表示使用凭据的唯一标识符，长度限制256字节以内。spec[CMSignatureSpec](#ZH-CN_TOPIC_0000002529445349__cmsignaturespec)是表示签名、验签的属性。

**返回值**：

类型说明Promise<[CMHandle](#ZH-CN_TOPIC_0000002529445349__cmhandle)>Promise对象。表示签名、验签的初始化操作结果，返回CMHandle对象。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500002The certificate does not exist.17500005The application is not authorized by the user.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string = 'test'; /* 业务使用凭据进行签名、验签的初始化操作，需要使用凭据的唯一标识符，此处省略 */
const req: certificateManager.CMSignatureSpec = {
  purpose: certificateManager.CmKeyPurpose.CM_KEY_PURPOSE_VERIFY,
  padding: certificateManager.CmKeyPadding.CM_PADDING_PSS,
  digest: certificateManager.CmKeyDigest.CM_DIGEST_MD5
}
try {
  certificateManager.init(uri, req).then((handle) => {
    console.info('Succeeded in initiating.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to init. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to init. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.update

update(handle: Uint8Array, data: Uint8Array, callback: AsyncCallback<void>): void

表示签名、验签的数据更新操作，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明handleUint8Array是表示初始化操作返回的句柄，最大长度为8字节。dataUint8Array是表示待签名、验签的数据。callbackAsyncCallback<void>是回调函数。当签名、验签的数据更新操作成功时，err为null，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
let srcData: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.update(cmHandle, srcData, (err, result) => {
    if (err != null) {
      console.error(`Failed to update. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('Succeeded in updating.');
    }
  });
} catch (error) {
  console.error(`Failed to update. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.update

update(handle: Uint8Array, data: Uint8Array): Promise<void>

表示签名、验签的数据更新操作，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明handleUint8Array是表示初始化操作返回的句柄，最大长度为8字节。dataUint8Array是表示待签名、验签的数据。

**返回值**：

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
let srcData: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.update(cmHandle, srcData).then((result) => {
    console.info('Succeeded in updating.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to update. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to update. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.finish

finish(handle: Uint8Array, callback: AsyncCallback<CMResult>): void

表示完成签名的操作，Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明handleUint8Array是表示初始化操作返回的句柄，最大长度为8字节。callbackAsyncCallback<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>是回调函数。当签名成功时，err为null，data为[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)对象中的outData属性，表示签名数据；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.finish(cmHandle, (err, cmResult) => {
    if (err != null) {
      console.error(`Failed to finish. Code: ${err.code}, message: ${err.message}`);
    } else {
      if (cmResult?.outData != undefined) {
        let signRes: Uint8Array = cmResult.outData;
        console.info('Succeeded in finishing.');
      } else {
        console.info('The result of finishing is undefined.');
      }
    }
  });
} catch(error) {
  console.error(`Failed to finish. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.finish

finish(handle: Uint8Array, signature: Uint8Array, callback: AsyncCallback<CMResult>): void

表示完成验签的操作，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明handleUint8Array是表示初始化操作返回的句柄，最大长度为8字节。signatureUint8Array是表示签名数据。callbackAsyncCallback<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>是回调函数。当验签成功时，err为null；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
let signRes: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.finish(cmHandle, signRes, (err, cmResult) => {
    if (err != null) {
      console.error(`Failed to finish. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('Succeeded in finishing.');
    }
  });
} catch(error) {
  console.error(`Failed to finish. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.finish

finish(handle: Uint8Array, signature?: Uint8Array): Promise<CMResult>

表示完成签名、验签的操作，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明handleUint8Array是表示初始化操作返回的句柄，最大长度为8字节。signatureUint8Array否表示签名数据。

**返回值**：

类型说明Promise<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>Promise对象。执行签名操作时，表示签名的结果，返回值为[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)对象中的outData属性；执行验签操作时，无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  /* 签名的finish操作 */
  certificateManager.finish(cmHandle).then((cmResult) => {
    if (cmResult?.outData != undefined) {
      let signRes1: Uint8Array = cmResult.outData;
      console.info('Succeeded in finishing signature.');
    } else {
      console.info('The result of signature is undefined.');
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to finish signature. Code: ${err.code}, message: ${err.message}`);
  })

  /* 签名的结果 */
  let signRes: Uint8Array = new Uint8Array([
    0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
  ]);
  /* 验签的finish操作 */
  certificateManager.finish(cmHandle, signRes).then((cmResult) => {
    console.info('Succeeded in finishing verification.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to finish verification. Code: ${err.code}, message: ${err.message}`);
  })
} catch(error) {
  console.error(`Failed to finish. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.abort

abort(handle: Uint8Array, callback: AsyncCallback<void>): void

表示中止签名、验签的操作，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明handleUint8Array是表示初始化操作返回的句柄，最大长度为8字节。callbackAsyncCallback<void>是回调函数。当中止签名、验签成功时，err为null，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.abort(cmHandle, (err, cmResult) => {
    if (err != null) {
      console.error(`Failed to abort. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('Succeeded in aborting.');
    }
  });
} catch(error) {
  console.error(`Failed to abort. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.abort

abort(handle: Uint8Array): Promise<void>

表示中止签名、验签的操作，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明handleUint8Array是表示初始化操作返回的句柄，最大长度为8字节。

**返回值**：

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.abort(cmHandle).then((result) => {
    console.info('Succeeded in aborting.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to abort. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to abort. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.getPublicCertificate12+

getPublicCertificate(keyUri: string): Promise<CMResult>

表示获取用户公共凭据的详细信息，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明keyUristring是表示用户公共凭据的唯一标识符，长度限制256字节以内。

**返回值**：

类型说明Promise<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>Promise对象。表示获取用户公共凭据详细信息的结果，返回值为[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)对象中的credential属性。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500002The certificate does not exist.17500005The application is not authorized by the user.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string = 'test'; /* 用户获取公共凭据详情，需要使用凭据的唯一标识符，此处省略 */
try {
  certificateManager.getPublicCertificate(uri).then((cmResult) => {
    if (cmResult?.credential == undefined) {
      console.info('The result of getting public certificate is undefined.');
    } else {
      let cred = cmResult.credential;
      console.info('Succeeded in getting Public certificate.');
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get Public certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get Public certificate. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.isAuthorizedApp12+

isAuthorizedApp(keyUri: string): Promise<boolean>

表示当前应用是否由指定的用户凭据授权，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明keyUristring是表示用户授权给应用使用的凭据的唯一标识符，长度限制256字节以内。

**返回值**：

类型说明Promise<boolean>Promise对象。表示查询应用是否被授权的结果，true为已授权，false为未授权。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string = 'test'; /* 用户授权给应用使用的凭据的唯一标识符，此处省略 */
try {
  certificateManager.isAuthorizedApp(uri).then((res) => {
    if (res) {
      console.info('The application is authorized by the user.');
    } else {
      console.info('The application is not authorized by the user.');
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to check if the application is authorized. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to check if the application is authorized. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.getAllUserTrustedCertificates12+

getAllUserTrustedCertificates(): Promise<CMResult>

表示获取当前用户和设备公共位置的所有用户根CA证书列表，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**返回值**：

类型说明Promise<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>Promise对象。表示获取用户根CA证书列表的结果，返回值[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)对象中的certList属性。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  certificateManager.getAllUserTrustedCertificates().then((cmResult) => {
    if (cmResult === undefined) { // 用户根CA证书个数为0时，返回cmResult为undefined。
      console.info('the count of the user trusted certificates is 0');
    } else if (cmResult.certList == undefined) {
      console.info('The result of getting all user trusted certificates is undefined.');
    } else {
      let list = cmResult.certList;
      console.info('Succeeded in getting all user trusted certificates.');
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get all user trusted certificates. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get all user trusted certificates. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.getAllUserTrustedCertificates18+

getAllUserTrustedCertificates(scope: CertScope): Promise<CMResult>

表示根据证书的位置获取用户根CA证书列表，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明scope[CertScope](#ZH-CN_TOPIC_0000002529445349__certscope18)是表示证书的位置。

**返回值**：

类型说明Promise<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>Promise对象。表示获取用户根CA证书列表的结果，返回值[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)对象中的certList属性。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  /* 获取当前用户下的用户根CA证书列表; 如果需要获取设备公共位置的用户根CA列表，则传入GLOBAL_USER */
  let scope: certificateManager.CertScope = certificateManager.CertScope.CURRENT_USER;
  certificateManager.getAllUserTrustedCertificates(scope).then((cmResult) => {
    if (cmResult === undefined) { // 用户根CA证书个数为0时，返回cmResult为undefined。
      console.info('the count of the user trusted certificates is 0');
    } else if (cmResult.certList == undefined) {
      console.info('The result of getting current user trusted certificates is undefined.');
    } else {
      let list = cmResult.certList;
      console.info('Succeeded in getting current user trusted certificates.');
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get current user trusted certificates. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get current user trusted certificates. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.getUserTrustedCertificate12+

getUserTrustedCertificate(certUri: string): Promise<CMResult>

表示获取用户根CA证书的详细信息，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明certUristring是表示用户根CA证书的唯一标识符，长度限制256字节以内。

**返回值**：

类型说明Promise<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>Promise对象。表示获取用户根CA证书详细信息的结果，返回值为[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)对象中的certInfo属性。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500002The certificate does not exist.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let certUri: string = 'testUserCert'; /* 用户获取用户根CA证书详情，需要使用CA证书的唯一标识符，此处省略 */
try {
  certificateManager.getUserTrustedCertificate(certUri).then((cmResult) => {
    if (cmResult?.certInfo == undefined) {
      console.info('The result of getting user trusted certificate is undefined.');
    } else {
      let cert = cmResult.certInfo;
      console.info('Succeeded in getting user trusted certificate.');
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get user trusted certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get user trusted certificate. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.getPrivateCertificates13+

getPrivateCertificates(): Promise<CMResult>

表示获取应用安装的凭据列表，使用Promise方式异步返回结果。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**返回值**：

类型说明Promise<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>Promise对象。表示获取应用安装的凭据列表的结果，返回值[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)对象中的credentialList属性。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed. The application does not have the permission required to call the API.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  certificateManager.getPrivateCertificates().then((cmResult) => {
    if (cmResult === undefined) { // 应用安装的凭据个数为0时，返回cmResult为undefined。
      console.info('the count of the private certificates is 0');
    } else if (cmResult.credentialList == undefined) {
      console.info('The result of getting all private certificates installed by the application is undefined.');
    } else {
      let list = cmResult.credentialList;
      console.info('Succeeded in getting all private certificates installed by the application.');
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get all private certificates installed by the application. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get all private certificates installed by the application. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.getCertificateStorePath18+

getCertificateStorePath(property: CertStoreProperty): string;

表示获取证书的存储路径。

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

参数名类型必填说明property[CertStoreProperty](#ZH-CN_TOPIC_0000002529445349__certstoreproperty18)是表示获取证书存储路径的参数集合。

**返回值**：

类型说明string表示证书的存储路径。

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. For example, CertStoreProperty.certType is set to CA_CERT_USER, but CertStoreProperty.certScope is not specified.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500009The device does not support the specified certificate storage path, For example, the device outside China does not support the certificate that uses SM algorithm.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';

try {
  /* 获取系统CA的存储位置 */
  let property1: certificateManager.CertStoreProperty = {
    certType: certificateManager.CertType.CA_CERT_SYSTEM,
  }
  let systemCAPath = certificateManager.getCertificateStorePath(property1);
  console.info(`Success to get system ca path: ${systemCAPath}`);

  /* 获取当前用户的用户CA存储位置 */
  let property2: certificateManager.CertStoreProperty = {
    certType: certificateManager.CertType.CA_CERT_USER,
    certScope: certificateManager.CertScope.CURRENT_USER,
  }
  let userCACurrentPath = certificateManager.getCertificateStorePath(property2);
  console.info(`Success to get current user's user ca path: ${userCACurrentPath}`);

  /* 获取设备公共的用户CA存储位置 */
  let property3: certificateManager.CertStoreProperty = {
    certType: certificateManager.CertType.CA_CERT_USER,
    certScope: certificateManager.CertScope.GLOBAL_USER,
  }
  let globalCACurrentPath = certificateManager.getCertificateStorePath(property3);
  console.info(`Success to get global user's user ca path: ${globalCACurrentPath}`);

  /* 获取SM算法系统CA的存储位置 */
  let property4: certificateManager.CertStoreProperty = {
    certType: certificateManager.CertType.CA_CERT_SYSTEM,
    certAlg: certificateManager.CertAlgorithm.SM,
  }
  let smSystemCAPath = certificateManager.getCertificateStorePath(property4);
  console.info(`Success to get SM system ca path: ${smSystemCAPath}`);
} catch (error) {
  console.error(`Failed to get store path. Code: ${error.code}, message: ${error.message}`);
}
```

#### certificateManager.getUkeyCertificate22+

getUkeyCertificate(keyUri: string, ukeyInfo: UkeyInfo): Promise<CMResult>

表示获取USB凭据详细信息。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**设备行为差异：** 该接口在PC设备可正常调用，在其他设备中返回801错误码。

**参数**：

参数名类型必填说明keyUristring是表示USB凭据的唯一标识符，长度限制256字节以内。ukeyInfo[UkeyInfo](#ZH-CN_TOPIC_0000002529445349__ukeyinfo22)是表示USB凭据的属性信息。

**返回值**：

类型说明Promise<[CMResult](#ZH-CN_TOPIC_0000002529445349__cmresult)>Promise对象，返回获取到的USB凭据详情的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[证书管理错误码](证书管理错误码.md)。

错误码ID错误信息201Permission verification failed.801Capability not supported. The application does not have the permission required to call the API.17500001Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again.17500002Indicates that the certificate does not exist.17500010Indicates that access USB key service failed.17500011Indicates that the input parameters validation failed. For example, the parameter format is incorrect or the value range is invalid.

**示例**：

```ets
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyUri: string = 'test'; /* USB凭据的唯一标识符，此处省略 */
let ukeyInfo: certificateManager.UkeyInfo = { /* USB凭据的属性信息，此处省略 */
    certPurpose: certificateManager.CertificatePurpose.PURPOSE_DEFAULT,
  }
try {
  certificateManager.getUkeyCertificate(keyUri, ukeyInfo).then((cmResult) => {
      let list = cmResult.credentialDetailList;
      console.info('Succeeded in getting detail of USB key certificate.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to get detail of USB key certificate. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Failed to get detail of USB key certificate. Code: ${error.code}, message: ${error.message}`);
}
```